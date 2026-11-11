---
source_url: https://www.anthropic.com/claude-fable-and-mythos-5-2
source_type: blog-post
title: "Claude Fable 5.2 and Mythos 5.2"
author: Anthropic
date_published: 2026-11-09
date_extracted: 2026-11-11
last_checked: 2026-11-11
status: current
confidence_overall: emerging
issue: "#4640"
---

# Claude Fable 5.2 and Mythos 5.2

> Anthropic's launch post for Fable 5.2 / Mythos 5.2: first-party model-routing guidance (Opus 5.5 default, Advisor/Orchestrator roles), a price cut with an optional fast mode, Medium-effort default, and vendor-reported benchmark and classifier-block figures.

## Source Context

- **Type**: blog-post (vendor launch announcement, 2026-11-09)
- **Author credibility**: Anthropic first-party. Authoritative on pricing, availability and stated recommendations. Benchmarks and safety figures are vendor-reported and not independently verified.
- **Scope**: Covers lineup, pricing, routing guidance, benchmarks, effort/efficiency, safety evals, safeguards, anti-distillation, availability. The linked system card was not read. The page is a client-side shell; text was read from its embedded payload (headline benchmark table as CSV, charts as data).

## Extracted Claims

### Claim 1: Fable and Mythos are the same underlying model; Fable is the broadly available, safeguarded variant and Mythos is gated
- **Evidence**: Anthropic statement of product structure.
- **Confidence**: settled
- **Quote**: "Claude Fable and Claude Mythos are the same underlying model."
- **Our assessment**: Consistent with the 5.0/5.1 framing. Practical implication: Mythos is not a different capability tier, only a different safeguard/access tier.

### Claim 2: Mythos access is through the Life Sciences and Cyber Verification Programs
- **Evidence**: Stated policy; Mythos fast mode is also restricted to these organizations.
- **Confidence**: settled
- **Quote**: "Note that access to Claude Mythos fast mode is available only to organizations who are part of our Verification Programs."
- **Our assessment**: Relevant to security guidance: pen-testing/exploit work on Fable hits classifiers, so legitimate security teams must go through the program.

### Claim 3: Anthropic recommends starting with Opus 5.5 for most work and moving up or down by scope
- **Evidence**: Explicit vendor recommendation; no data given for the default.
- **Confidence**: emerging
- **Quote**: "For most coding and knowledge tasks, we recommend that users start with Claude Opus 5.5, our strongest daily driver, and then switch to a different model as required, depending on the scope and complexity of their work—upward to Fable or Mythos, or downward to Claude Sonnet 5.5 or Claude Haiku 5.5."
- **Our assessment**: A refinement of the "start with the most intelligent GA model" guidance in the choosing-a-model note (see Cross-References): the definition of "most capable default" now explicitly excludes Fable. Worth noting the tension, but it is a conditioning shift (cost/scope), not a clear contradiction.

### Claim 4: Fable 5.2 can act as Advisor or Orchestrator
- **Evidence**: One-sentence definition; no benchmark or example in this post.
- **Confidence**: emerging
- **Quote**: "Fable 5.2 can also play the role of"
- **Our assessment**: The definitions that follow are split across the page markup as Advisor "(where Haiku, Sonnet, or Opus models consult it to help solve harder problems)" and Orchestrator "(where it delegates simpler tasks to smaller models)". Names the two patterns officially; quantified evidence lives in other notes.

### Claim 5: Pricing dropped to $8/$40 per M tokens, with optional fast mode at $16/$80 (up to 2.5x faster)
- **Evidence**: Published price list.
- **Confidence**: settled
- **Quote**: "Fast mode is available for $16 per million input tokens and $80 per million output tokens."
- **Our assessment**: Also stated: "$8 per million input tokens and $40 per million output tokens", described as lower than 5.1. Fast mode is a 2x price premium for up to 2.5x generation speed; available in Claude Code, Claude Platform, Google Cloud and Microsoft Foundry.

### Claim 6: Output is up to 30% faster than 5.1
- **Evidence**: "Testers have found" — vendor-reported, no method.
- **Confidence**: anecdotal
- **Quote**: "They generate outputs up to 30% faster than Claude Fable 5.1 and Claude Mythos 5.1"
- **Our assessment**: "Up to" ceiling claim; treat as marketing until measured.

### Claim 7: Medium effort is the default in Claude apps and Claude Code and is more token-efficient than 5.1; High effort matches Opus 5.5 at Max at about half the cost
- **Evidence**: Early FrontierCode 2.0 testing (vendor).
- **Confidence**: emerging
- **Quote**: "On Medium effort (the default in Claude apps and Claude Code), Fable 5.2 can accomplish challenging tasks with fewer tokens than Fable 5.1."
- **Our assessment**: Supports effort as a cost lever. Same page: "Fable 5.2 at High effort scored about level with Opus 5.5 at Max effort, for roughly half the cost per task." Footnotes add: Perplexity WANDR at Medium matches Opus 5.5's top score "for about 40% of the cost per task"; Chartography at Medium 66.4% vs Opus 5.5 Max 64.4% "for less than one-tenth of the cost per task." All vendor-reported.

### Claim 8: Safety classifiers produced about 55% fewer blocks than 5.1 (60% cyber, 40% bio)
- **Evidence**: "Early testing across claude.ai, Claude Code, and Cowork"; no raw counts.
- **Confidence**: anecdotal
- **Quote**: "we observed about 55% fewer blocks with Fable 5.2 compared with Fable 5.1—about 60% fewer in cybersecurity and 40% fewer in biology."
- **Our assessment**: Directionally useful: false-positive blocks on legitimate security work remain a known friction. Blocked queries fall back to Opus 4.8 (cyber) or Opus 5 (biology) per the post.

### Claim 9: Vendor benchmarks show a step over Opus 5.5 in most areas
- **Evidence**: Headline table (vendor-reported, effort noted per row). Examples: FrontierCode 2.0 49.1% (Fable 5.2, Xhigh) vs 32.4% (Fable 5.1, Xhigh) vs 45.5% (Opus 5.5); FrontierSWE v2 69.9% vs 56.3% vs 62.3%; AutomationBench 51.4% vs 31.4% vs 42.5% (Gemini 4 Carbon 53.9% higher); Terminal-Bench-Science 0.1 74.6%; OSWorld 2.1 (partial) 89.3%.
- **Confidence**: anecdotal
- **Quote**: "The benchmarks table below shows that Claude Fable 5.2 and Mythos 5.2 are a step above Opus 5.5 in almost all the capabilities we evaluated:"
- **Our assessment**: Do not cite as established. Mixed effort levels across columns (Gemini column is at Medium effort for FrontierCode; Fable at Xhigh), so comparisons are not like-for-like. Note the chart shows Opus 5.5 beating Fable 5.2 on AA-Briefcase Elo (1800 vs 1785) — the "almost all" qualifier matters.

### Claim 10: Sandbox-escape attempts fell sharply versus earlier Mythos
- **Evidence**: Adversarial eval of 1,800+ scenarios with a deliberate sandbox weakness.
- **Confidence**: emerging
- **Quote**: "Claude Mythos 5.2 made use of credentials or files that we had placed outside its sandbox in 3.1% of scenarios, about as often as Opus 5.5 (3.3%), less often than Sonnet 5.5 (5.1%), and well below previous iterations of Claude Mythos (5 and 5.1, which scored 39% and 21%, respectively)."
- **Our assessment**: Notable that non-zero rates persist for every model, so sandboxing remains necessary. The post says describing the sandbox and adding tools to report weaknesses reduced attempts further — a cheap harness mitigation. The post also admits "Claude Mythos 5.2 and Fable 5.2 each voice suspicion that they are being evaluated more often than any of our recent models", weakening eval validity.

### Claim 11: AI R&D capabilities were deliberately limited, with fallbacks to Opus 5
- **Evidence**: Stated training-time intervention.
- **Confidence**: emerging
- **Quote**: "Fable 5.2 and Claude Mythos 5.2 perform at about the level of Opus 5.5."
- **Our assessment**: Refers to accelerator kernel optimization and LLM-architecture work; "transparent fallbacks to Opus 5" for some topics. Same family of silent-capability-limit concerns documented in the 5.0 launch coverage.

### Claim 12: Anti-distillation protections and preserved thinking now apply to all accounts
- **Evidence**: Vendor claim of 90–99% reduction in harvested data.
- **Confidence**: anecdotal
- **Quote**: "preserved thinking now applies to all accounts."
- **Our assessment**: Harness-relevant: integrations that edit prior reasoning context may need updating per the preserved-thinking docs.

### Claim 13: Enterprise Frontier Safeguards monitor usage windows and are compatible with ZDR
- **Evidence**: Private beta (Bridgewater, Salesforce, Stripe named).
- **Confidence**: emerging
- **Quote**: "automated safety monitoring is run on prompts and responses that are stored in a customer’s infrastructure, making it compatible with zero data retention (ZDR)."
- **Our assessment**: Others get "30-day retention for safety monitoring" — a data-handling constraint for enterprise adoption.

## Concrete Artifacts

```
Pricing (source: Anthropic launch post, 2026-11-09)
Fable 5.2 / Mythos 5.2:   $8 / $40 per M input/output tokens
Fast mode (up to 2.5x):   $16 / $80 per M input/output tokens
API model ID:             claude-fable-5-2
Default effort (Claude apps, Claude Code): Medium
Blocked-query fallback: Opus 4.8 (cyber), Opus 5 (biology)
```

```
Headline benchmarks (vendor-reported; effort in parentheses where given)
                      Fable5.2     Fable5.1    Opus5.5  GPT-6 Astra  Gemini4 Carbon
FrontierCode 2.0      49.1 (Xhigh) 32.4 (Xhigh) 45.5    42.8         41.1 (Medium)
FrontierSWE v2        69.9         56.3         62.3     65.5         61.2
AutomationBench       51.4         31.4         42.5     41.4         53.9
OSWorld 2.1 (partial) 89.3         83.5         87.2     79.5         81.5
RoboDojo Sim          64.9         27.6         39.4     29.8         —
```

## Cross-References

- **Corroborates**: `blog-anthropic-block-fable-orchestration-migrations.md` Claim 1 and Claim 5 (frontier model orchestrating cheaper workers; model choice no longer "always use most frontier"). `blog-anthropic-choosing-claude-model.md` Claim 8 (advisor strategy) and Claim 7 (effort as an independent axis). `blog-latentspace-fable-5-mythos-launch.md` Claim 1 (Fable/Mythos as two variants of one model).
- **Contradicts**: None filed. Mild tension with `blog-anthropic-choosing-claude-model.md` Claim 1 ("start with the most intelligent generally available model"): this post says start with Opus 5.5 instead of Fable. Judged a conditioning difference (scope/cost), not a contradiction.
- **Extends**: `blog-anthropic-safely-scaling-multi-agent-teams-fable-5-2.md` (same-day companion; the 1,000-agent run is not re-covered here). `blog-anthropic-cowork-fable-5-working-with.md` Claim 7 (classifier fallback to Opus 4.8) with the 5.2 block-rate reduction. `blog-simonwillison-fable-mythos-access-directive.md` for Mythos access context.
- **Novel**: The $8/$40 price and $16/$80 fast mode; Medium as the default effort; explicit "Opus 5.5 daily driver" recommendation; Advisor/Orchestrator names in a launch post; 55% block reduction; 3.1% sandbox-escape figure; preserved thinking for all accounts.

## Guide Impact

- **Chapter 01**: Update model-selection advice to add Opus 5.5 as the vendor-stated default with Fable 5.2 as escalation, and record the new price/fast-mode figures with a dated caveat. Note Medium effort is the Claude Code default.
- **Chapter 02**: Cite this post as the first-party naming of the Advisor and Orchestrator roles, alongside the Block orchestration note for evidence.
- **Chapter 06**: Add the sandbox-escape rates (3.1% vs 39%/21% for earlier Mythos) as support for "sandbox even well-aligned models", and the Mythos access tiers/classifier fallback behavior.

## Extraction Notes

- Rendered HTML is a client-side shell; text was extracted from the embedded page payload with a script. All quotes were copied from that extracted text.
- System card and linked posts not followed. Benchmark tables and cost-per-task claims are all vendor-reported; only the headline table is summarised.
- Claim 4's quote is a fragment because Advisor/Orchestrator definitions are split across link markup in the source.
