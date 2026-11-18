---
source_url: https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers
source_type: blog-post
title: "Inference engineering for software engineers"
author: Gergely Orosz and Ivan Klaric (The Pragmatic Engineer)
date_published: 2026-11-17
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: emerging
issue: "#4798"
---

# Inference engineering for software engineers

> A vendor-neutral (but vendor-interviewed) survey of when and how to move from frontier-lab APIs to open models on inference providers, with a three-stage graduation path (frontier API → multi-tenant open-model API → dedicated GPUs) and the TTFT tail-latency and stateless-API caching problems that motivate it.

## Source Context

- **Type**: blog-post (Pragmatic Engineer deepdive, marked "Paid"; only the free preview was readable — it ends in Section 4, right after the sentence "Here's an example to illustrate the problems that stateless APIs cause: an app with user's inputs, LLM prompts, and the agentic context layer:").
- **Author credibility**: Gergely Orosz runs the Pragmatic Engineer newsletter; the piece draws on interviews with Richard Gong (Modal), Dmytro Dzhulgakov (Fireworks CTO) and Philip Kiely (Baseten). The authors state they have no vendor affiliation, but nearly all technical claims are vendor-sourced.
- **Scope**: Covers provider-vs-lab differences, switch triggers, model/provider/deployment selection, and Stage 1 (multi-tenant API) problems. NOT read (paywalled): rest of caching section, "Signs you've outgrown multi-tenant inference APIs", Stage 2 dedicated GPU configuration, speculative decoding. GPU/KV-cache internals are out of guide scope and deliberately not extracted.

## Extracted Claims

### Claim 1: Teams move from frontier APIs to open models mainly for cost, latency control, and fine-tuning
- **Evidence**: Author synthesis from provider interviews; cost cuts at Uber (50%), Pinterest (90%), AT&T (56%) cited from earlier coverage, not measured here.
- **Confidence**: emerging
- **Quote**: "Moving from frontier AI labs to an independent inference provider is often driven by three factors: cost, control, and the need for more customization."
- **Our assessment**: Plausible and consistent with the Uber note. Cost figures are cited, not demonstrated; they are not evidence of method.

### Claim 2: A prompt-aware "smart router" sending simple requests to cheaper models is the obvious cost lever, and switching is trivial because providers expose compatible endpoints
- **Evidence**: Attributed to Uber's ~50% per-token cut; no routing details given in the free portion.
- **Confidence**: emerging
- **Quote**: "Providers offer OpenAI/Anthropic-compatible API endpoints, so switching providers is trivial."
- **Our assessment**: "Trivial" is optimistic; the OpenRouter gotchas note documents per-provider parser, reasoning-effort and history-validation differences behind the same API shape.

### Claim 3: Generic benchmarks are insufficient; teams should use private evals, or an A/B with engineers if no eval set exists
- **Evidence**: Authors' advice plus Satya Nadella quote from the Pragmatic Engineer Podcast.
- **Confidence**: emerging
- **Quote**: "Public benchmarks are great, but your private evals will matter more: you need your own eval for the outcome that matters to you."
- **Our assessment**: Agrees with common practice. The A/B suggestion ("let some engineers use the new model and give feedback") is a lightweight, practical decision method, but is subjective.

### Claim 4: Per-task cost, not per-token cost, is the right comparison unit across models
- **Evidence**: Artificial Analysis cost-per-task chart; example $5.46/task for Sonnet 5.5 vs $2.00 for Kimi K3 (~60% cheaper). Chart is an image; figures taken from article text.
- **Confidence**: emerging
- **Quote**: "Note that the cost comparison here is per-task, not per-token."
- **Our assessment**: Sound point (token counts differ per model). The $/task figures are on a generic index and may not transfer to a team's workload, as the authors themselves note.

### Claim 5: The same open model served by different providers differs in quality; Artificial Analysis' endpoint accuracy index measures this (Kimi K3 providers ranged 93%–102%)
- **Evidence**: Artificial Analysis chart; scores carry a 95% confidence interval due to non-determinism.
- **Confidence**: emerging
- **Quote**: "Endpoint accuracy is broadly similar and the scores of providers range from 93% to 102%."
- **Our assessment**: Corroborates the OpenRouter-gotchas finding of provider variance, though that note found far larger gaps on tool-calling benchmarks (e.g. 90.2% vs 75.3% GPQA). The two sources disagree in magnitude, not direction; likely a difference of benchmark and model, so not filed as a contradiction.

### Claim 6: Deployment follows a graduation path: frontier API → open model on multi-tenant provider API → dedicated GPUs
- **Evidence**: Authors' account of what all three providers told them; coupled with product-market fit and spend.
- **Confidence**: emerging
- **Quote**: "This deployment progression is typically a graduation path: most deployments start as drop-in API replacements of frontier labs' APIs, and as usage grows they start switching to dedicated infrastructure."
- **Our assessment**: The core reusable idea. Vendor-sourced (they sell stage 2), so the incentive favors recommending graduation. Triggers for stage 2 are listed only in the (unread) paid part; the free preview names them in the intro: rate limits, performance consistency, overpaying.

### Claim 7: Dedicated capacity is scarce and typically needs upfront long-term commitments
- **Evidence**: Provider interviews; GPU shortage.
- **Confidence**: emerging
- **Quote**: "Scarce capacity is one of the reasons why getting a dedicated setup typically requires long-term budget commitments upfront."
- **Our assessment**: A real constraint on the "just graduate" advice; teams should weigh commitment risk against model churn.

### Claim 8: Multi-tenant APIs have long-tailed TTFT latency, so p95/p99 matter as much as p50; causes are replica scaling, noisy neighbours, cold starts, and cold KV caches
- **Evidence**: Baseten illustrative TTFT distribution (illustrative shape, not measured data); explanations from providers.
- **Confidence**: emerging
- **Quote**: "So, when measuring latencies, the p95/p99 latencies are just as important as p50 latencies."
- **Our assessment**: Standard performance engineering; useful to apply to agent harnesses. Note the chart is explicitly illustrative.

### Claim 9: Measure TTFT in two places — provider-instrumented (pure inference) and client-instrumented (user-experienced) — and use connection pooling to improve p95
- **Evidence**: Authors' guidance; notes frontier labs typically expose no provider-side TTFT.
- **Confidence**: emerging
- **Quote**: "Frontier labs typically do neither."
- **Our assessment**: Actionable and cheap. Practical for anyone building a harness or gateway.

### Claim 10: Frontier-lab self-declared uptime is below cloud-provider norms, and degradation is not counted as downtime, so a 99.99% app cannot rely on a single lab; use a gateway with fallback
- **Evidence**: Status-page figures cited (Anthropic 99.5%, OpenAI API 99.97%, ChatGPT 99.2%); screenshots of status pages.
- **Confidence**: emerging
- **Quote**: "As all these APIs are multi-tenant, it means that performance degradations will naturally hit some tenants – with no way to be aware of the degradation, or do anything about it."
- **Our assessment**: Reasonable reading, though self-declared uptime is a weak basis for the "unmeasured degradation" claim. Fallback gateways link to the Ramp deepdive. The OpenRouter note provides counter-evidence: a fully pinned three-provider chain still went down, so fallback is not a cure.

### Claim 11: Stateless chat-completions APIs make caching the provider's burden ("the original sin")
- **Evidence**: Quote from Dmytro Dzhulgakov, Fireworks CTO (vendor-sourced). The worked example is paywalled.
- **Confidence**: anecdotal
- **Quote**: "the original sin"
- **Our assessment**: Interesting framing relevant to harness design (stateless API vs. stateful agent context), but the details are paywalled; cannot assess further. Prompt-cache utilization being observable in responses is a concrete tip ("You can get prompt cache utilization metrics from the response of the OpenAI completions API").

### Claim 12: Only ~10% of Modal's customers fine-tune; customization is for "power users"
- **Evidence**: Single vendor figure (Richard Gong, Modal).
- **Confidence**: anecdotal
- **Quote**: "Richard Gong of Modal says that around 10% of their customers go this far, suggesting that customization is for “power users”."
- **Our assessment**: Useful sanity check against over-investing in fine-tuning. Single vendor, no methodology.

### Claim 13: Vendor efficiency claim: Fireworks' Ember-1 (post-trained on Kimi K3) gives similar quality with 40% fewer reasoning tokens
- **Evidence**: Fireworks announcement, self-reported.
- **Confidence**: anecdotal
- **Quote**: "delivering a similar quality level but with 40% fewer reasoning tokens consumed"
- **Our assessment**: Vendor-reported; do not adopt as fact. Illustrates that reasoning-token count is a cost lever.

## Concrete Artifacts

```
Three-stage graduation path (Orosz & Klaric, section 3):
1. Use a frontier lab's API endpoints
2. Move over to using an open model, using the API endpoint of an inference provider
3. Rent dedicated GPUs from the inference provider

Selection sequence (section 3): Model -> Provider -> Deployment model (multi-tenant vs dedicated)

Signs of outgrowing multi-tenant (intro bullet): hitting rate limits, performance
consistency problems, overpaying for usage.
```

No code or config in the free portion.

## Cross-References

- **Corroborates**: `blog-simonwillison-openrouter-provider-gotchas.md` Claim 2 (same open model scores differently by provider) and Claim 11 (provider availability risk); `blog-latentspace-baseten-inference-engineering-masterclass.md` Claim 3 (customers move from shared pay-per-token APIs to dedicated deployments for reliability and control); `blog-pragmaticengineer-orosz-ubers-ai-infra-from-the-inside.md` Claim 1 (gateway) and Claim 5 (token costs fell ~50%).
- **Contradicts**: None filed. Mild tension with the OpenRouter note's "trivial switching" implications (Claim 2 here vs its Claims 6, 9), but this is a conditioning difference (API shape vs behavior), not an opposed claim.
- **Extends**: Uber note's Claim 5 by giving the mechanism (smart routing) and a staged path; Baseten note Claim 3 by describing the stages leading up to dedicated deployment.
- **Novel**: Staged graduation framing with product-market-fit coupling; two-point TTFT measurement; per-task-not-per-token comparison; endpoint accuracy index range 93–102%.

## Guide Impact

- **Chapter 05**: Could add a short cost-governance note: evaluate open-model/provider switches with private evals and per-task cost, and treat dedicated GPUs as a later stage requiring commitments (cite this note with Uber note Claim 5). Low priority; mostly outside guide scope.
- **Chapter 02**: Gateway fallback and provider heterogeneity: add the point that frontier APIs expose no provider-side TTFT and that p95/p99 should be tracked, paired with the OpenRouter note's warning that pinned fallbacks can fail.
- **Chapter 04**: Optional mention that stateless LLM APIs shift caching burden to the provider (Claim 11); wait for fuller evidence.

## Extraction Notes

- Only the free preview (~23k characters, roughly the first 60%) was available; claims are limited to visible text. Quotes were copied from the fetched page text.
- Chart contents (Artificial Analysis, Baseten) are images; only figures stated in the prose were used.
- Vendor quotes (Modal, Fireworks, Baseten) and figures are flagged as vendor-sourced.
- Overlap with the Latent Space Baseten note was checked; serving internals (KV cache, speculative decoding) intentionally skipped.
