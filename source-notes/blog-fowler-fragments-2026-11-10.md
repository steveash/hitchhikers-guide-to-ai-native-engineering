---
source_url: https://martinfowler.com/fragments/2026-11-10.html
source_type: blog-post
title: "Fragments: November 10"
author: Martin Fowler (curator); linked sources — Hadley Wickham, "How much do tokens really cost?"; Houck et al. (CAFE(S), ACM Queue); Cindy Sridharan (X post); Chris Ford (Thoughtworks)
date_published: 2026-11-10
date_extracted: 2026-11-11
last_checked: 2026-11-11
status: current
confidence_overall: anecdotal
issue: "#4645"
---

# Fragments: November 10 (Fowler on CAFE(S) context quality, verification token spend, and token subsidies)

> Fowler relays a five-dimension context-quality framework (CAFE(S)), a single practitioner's claim that ~70% of her token spend is verification, and Hadley Wickham's argument that per-token API prices are roughly unsubsidised while subscriptions are subsidised; the Wickham post was read in full, the other two are second-hand.

## Source Context

- **Type**: blog-post (Fowler's "Fragments" link-blog, 10 November 2026). Trusted-feed source.
- **Author credibility**: Martin Fowler is Chief Scientist at Thoughtworks. Hadley Wickham (tidyverse, Posit) writes the primary token-cost analysis, which I read directly. Cindy Sridharan is an observability/distributed-systems practitioner; her statement is a one-line self-report. Houck et al. are not characterised beyond Fowler's remark that the author list includes "some folks who I've learned to pay a lot of attention to".
- **Scope**: Four extracted items per Prospector triage: CAFE(S), Sridharan verification spend, Wickham subsidy analysis, and (framing only) Chris Ford's enterprise operating-model questions.
- **Not extracted** (per triage): Stratechery data-centre item, Takehi et al. weight-space programming (covered by `source-notes/blog-simonwillison-qwen-interpret-model-weights.md`), Jessica Kerr quote.
- **Primary sources**: Wickham's Substack post (https://substack.hadley.nz/p/how-much-do-tokens-really-cost) was read in full. The ACM Queue CAFE(S) article (https://queue.acm.org/doi/10.1145/3847288) returned HTTP 403 to curl and WebFetch, so it was NOT read. Sridharan's X post was not fetched.

## Extracted Claims

### Claim 1: Context quality for an agent is a property of the assembled context, not of its individual sources
- **Evidence**: Argument by Houck et al., quoted by Fowler. No data on the page.
- **Confidence**: emerging
- **Quote**: "Whether each source is individually useful does not reveal whether the resulting context is fit for the work the agent is being asked to do."
- **Our assessment**: Useful reframing for Ch04: auditing individual files (AGENTS.md, specs, tickets) is not enough; the combination the agent sees at task time must be assessed. Second-hand via Fowler.

### Claim 2: CAFE(S) gives five questions for judging assembled context: Clarity, Actionability, Fidelity, Efficiency, Security
- **Evidence**: Framework defined by Houck et al.; Fowler lists the dimensions with their guiding questions. No empirical validation shown on his page.
- **Confidence**: emerging
- **Quote**: "Clarity: Can the agent interpret the request as intended?" / "Actionability: Can the agent proceed, and know when it is done?" / "Fidelity: Can the agent trust that this context is true?" / "Efficiency: Can the agent focus on what matters?" / "Security: Should the agent have this context at all?"
- **Our assessment**: Compact, reusable as a review checklist; the "know when it is done" part of Actionability links context quality to verification. Unvalidated, and the paper itself was not read, so treat as a vocabulary, not a finding. Each question above is on a separate line on Fowler's page; the slashes are mine.

### Claim 3: The paper lists about six "context smells" where the dimensions break down, but Fowler does not name them
- **Evidence**: Fowler's one-sentence description only.
- **Confidence**: anecdotal
- **Quote**: "They also list a set of half-a-dozen “context smells”: common cases where these break down (and a nod to Kent’s original metaphor)"
- **Our assessment**: The smells themselves are not available here. The guide should not cite specific smells until someone reads the ACM Queue article. Follow-up needed.

### Claim 4: Fowler's reservations: the name is awkward and the article has heavy LLM voice, but the framing is good
- **Evidence**: Fowler's opinion.
- **Confidence**: anecdotal
- **Quote**: "But on the whole I think this is a good framing for thinking about an important part of feeding our silicon servants/overlords."
- **Our assessment**: Endorsement from a trusted curator, plus a caveat about the paper's prose quality that argues for checking its claims directly.

### Claim 5: A practitioner's verification process now takes most of her token spend: about 70% on verifying patches vs ~20-30% on creating them
- **Evidence**: Self-report by Cindy Sridharan, quoted by Fowler. No method, task mix, or time window.
- **Confidence**: anecdotal
- **Quote**: "70% of my daily token spend goes into verifying patches, and only ~20-30% into creating them."
- **Our assessment**: A single data point from an experienced engineer; do not generalise it to a ratio. Note the preceding line, "What was missing in my setup 6 months ago was the verification process I now use.", which implies the share reflects a deliberate verification setup (the debugging method in `source-notes/blog-fowler-fragments-2026-10-21.md` is likely related, but this page does not say so). The 70% and the 20-30% don't sum to 100%; the remainder is unexplained.

### Claim 6: Enterprise agent deployments spend more tokens checking model output than generating it
- **Evidence**: Fowler's recollection of conversations with enterprise users; no numbers or named companies.
- **Confidence**: anecdotal
- **Quote**: "A single request to a model from a customer may trigger a dozen turns to other models to probe its input and verify its output."
- **Our assessment**: Corroborates Claim 5 in direction only; both are informal. "A dozen turns" is illustrative ("may trigger"). Context is customer-facing guardrail/eval pipelines, which differs from a developer verifying patches.

### Claim 7: Per-token API pricing for an open frontier-class model looks close to cost, based on a self-hosting cost model
- **Evidence**: Wickham's primary post (read in full). Setup: Kimi K3 as proxy for a frontier model; OpenRouter prices from $0.59 to $1.81 per million blended tokens (20:1 input:output, 95% cached input); self-hosting estimate of about $23,000/month for an 8x GB300 server ($550,000 purchase, 8% interest, 3 years, colocation), ~124 billion tokens/month at ~6000 tokens/s/GPU and 75% utilisation, giving $0.25/M versus $1.13/M at common providers. Claude helped with cost figures (colocation costs were "Claude claims"); Wickham calls it a "crude analysis".
- **Confidence**: emerging
- **Quote**: "So I think I’m convinced that token prices are reasonably accurate measurements of the underlying cost."
- **Our assessment**: Transparent arithmetic and honest caveats, but it analyses an open model sold by many competing hosts, not closed frontier models such as Opus. A commenter on the post (Carl Boettiger) makes exactly this point: the open-model market is competitive, so closed-model prices are the open question. Fowler's summary ("per-token API basis") drops that scoping.

### Claim 8: Subsidies are on subscription plans, not API tokens
- **Evidence**: Wickham cites a SemiAnalysis post that a $200/month plan gets between $2,000 and $10,000 of tokens (not independently checked here); also notes such plans are for individuals and small businesses, while enterprises pay per-token.
- **Confidence**: emerging
- **Quote**: "That’s not to say subsidies aren’t still happening! I just don’t think they’re on per-token API costs. Instead, they’re happening on subscription plans."
- **Our assessment**: Gives a primary, quantified basis (a 10-50x token-value multiple on a $200 plan) for the earlier anecdotal "subsidies are ending" claims. It implies enterprise per-token budgets are the planning number, and individual subscription experience understates real cost.

### Claim 9: Model-training costs are excluded and could be called a subsidy
- **Evidence**: Wickham's own caveat; training "might have cost several hundred million dollars", paid by investors in Moonshot AI.
- **Confidence**: settled (as a stated limitation)
- **Quote**: "It’s also worth noting that my analysis ignores the cost of model training which might have cost several hundred million dollars."
- **Our assessment**: A real limit on the "unsubsidised" claim: it holds for inference only. Fowler preserves the caveat.

### Claim 10: Enterprise agent adoption raises a second layer of problems around shared context, token bill, review demand, agent permissions, and harness ownership
- **Evidence**: Chris Ford's Thoughtworks macro-trends article, quoted by Fowler; Thoughtworks field experience; no data.
- **Confidence**: anecdotal
- **Quote**: "Two hundred people, though, cannot work that way."
- **Our assessment**: Framing only (low priority per triage). The question list in the page ("How is context shared between teams? What’s the token bill? How do we deal with increased review demands? What’s the agent allowed to reach, read and change? And who’s now responsible for the harness everyone depends on?") is a usable Ch05 checklist; Fowler's summary lists "shared context, token cost, cognitive load, security, and platform building".

## Concrete Artifacts

```
Wickham's self-hosting cost model (Kimi K3), from https://substack.hadley.nz/p/how-much-do-tokens-really-cost (2026-11-03)
Hardware:  8x GB300 server ~ $550,000; 8% interest, 3 years ~ $17,000/month
Hosting:   colo ~ $3,750/mo + $600 bandwidth + ~$700 power; other items -> ~ $23,000/month total
Throughput: ~6000 tokens/s/GPU x 8 = 48,000 tokens/s ~ 124 billion tokens/month
At 75% utilisation: ~ $0.25 per million tokens
Provider API (20:1 input:output, 95% of input cached, blended): $0.59-$1.81 /M; most large hosts $1.13 /M
Subscription: $200/month plan ~ $2,000-$10,000 of tokens (Wickham citing SemiAnalysis)
Excluded: model training cost.
```

```
CAFE(S) dimensions (Houck et al., as listed by Fowler)
Clarity | Actionability | Fidelity | Efficiency | Security
(six "context smells" exist in the paper; not named on Fowler's page)
```

## Cross-References

- **Corroborates**: `source-notes/blog-pragmaticengineer-orosz-roi-of-ai-spend.md` Claim 6 (flat-rate subscriptions hide true cost; subsidies ending) — Wickham's post gives a quantified basis for subscription subsidy. `source-notes/blog-simonwillison-uber-caps-usage.md` Claim 6 (Willison's ~$1,000/month list-price usage costing ~$100/month on subsidised plans) is consistent with the 10x+ multiple Wickham cites. `source-notes/blog-ghuntley-agency-nobody-types-code.md` Claim 15 (subsidies drying up).
- **Contradicts**: None found; no contradiction issue filed. Wickham's "API tokens not significantly subsidised" is not opposed by the above, which concern subscriptions. Note: the Prospector pointed to Claim 6 of `blog-fowler-fragments-2026-10-21.md`, but that claim is about the hypotheses × signals table, not subsidies; the relevant subsidy claims are those listed above.
- **Extends**: `source-notes/blog-fowler-fragments-2026-10-21.md` — Claim 8 and Claim 9 (human value lies in designing verification) gain a weak quantitative echo from Sridharan's 70% figure, though it is a different source (X post) and this page does not tie them together. Also `source-notes/blog-anthropic-claude-code-verification-loops-skills.md` (verification loops "can increase token spend") and `source-notes/blog-anthropic-modernization-preparation-playbook.md` Claim 12 (verification as the larger token share in regulated runs).
- **Novel**: CAFE(S) vocabulary; the "verification is ~70% of spend" figure; the cost-model for self-hosted vs API token price.

## Guide Impact

- **Chapter 03 (verification)**: Mention Sridharan's self-reported ~70% verification / 20-30% creation split as an anecdote that verification can dominate token budgets; plan budgets accordingly. Label single-practitioner.
- **Chapter 04 (context engineering)**: Add CAFE(S) as a candidate review checklist (five questions), flagged second-hand until the ACM Queue paper is read; do not cite the smells.
- **Chapter 00/01/05 (cost)**: Add Wickham's finding that subscriptions, not per-token API prices, carry the subsidy (with the open-model and training-cost caveats), as a planning caution for moving from subscription to API/enterprise billing.
- **Chapter 05 (enterprise)**: Optionally use Ford's five questions (shared context, token cost, review load, agent reach, harness ownership) as framing.
- **Follow-up**: File an issue for the ACM Queue paper (https://queue.acm.org/doi/10.1145/3847288) when an accessible copy exists.

## Extraction Notes

- Fowler's page was read in full via curl with HTML stripped; all Fowler-page quotes are verbatim from that text. Quote 2 is five separate lines joined with " / ".
- Wickham's post fetched directly (HTTP 200) and read through the Subsidies section and first comment; the quoted passages are from that text.
- ACM Queue article returned HTTP 403, so CAFE(S) claims are second-hand, and the smells are unknown. Sridharan's X post was not fetched.
- Prospector triage's confidence guidance followed: Sridharan figure and CAFE(S) are marked anecdotal/emerging; overall `anecdotal`.
