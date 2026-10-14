---
source_url: https://newsletter.pragmaticengineer.com/p/building-resilient-systems
source_type: blog-post
title: "Building resilient AI-powered software, and planning for when things go wrong"
author: Gergely Orosz (publisher), excerpting Sam Newman, Building Resilient Distributed Systems (O'Reilly, 2026)
date_published: 2026-10-13
date_extracted: 2026-10-14
last_checked: 2026-10-14
status: current
confidence_overall: anecdotal
issue: "#4103"
---

# Building resilient AI-powered software, and planning for when things go wrong

> Book-excerpt practitioner guidance on running AI models as production dependencies: degrade gracefully and hedge with backup hosts, test for silent model drift with functional tests plus evals, scale timeouts to expected output, avoid chaining vendors, and make AI spend visible.

## Source Context

- **Type**: blog-post (book excerpt, O'Reilly, reprinted by The Pragmatic Engineer, 2026-10-13, with Orosz intro and closing takeaways)
- **Author credibility**: Sam Newman wrote *Building Microservices* and *Building Resilient Distributed Systems*; strong distributed-systems credentials. The AI sections are practitioner opinion with a few anecdotes and no measured data.
- **Scope**: The page has five excerpt sections. Sections 1-3 (RPO/RTO, DR patterns, infrastructure availability) are general DR material and were mostly skipped per triage. Sections 4-5 ("Resiliency of AI-powered software", "How to handle uncertainty", both from Chapter 7: Resiliency and AI) are mined here. The GPU/memory scarcity paragraph from section 3 (Chapter 10) is captured as Claim 8.

## Extracted Claims

### Claim 1: Model providers have a weaker availability record than other managed services, so software should keep operating (with reduced functionality) when the model is unavailable, rate limited, or out of tokens
- **Evidence**: Newman's assertion; no outage data in the excerpt.
- **Confidence**: emerging
- **Quote**: "Foundation model providers OpenAI and Anthropic don’t have a great track record in terms of providing high levels of availability for their services, at least when compared to other managed service providers, like public cloud vendors."
- **Further quote**: "This could be achieved by limiting functionality in the case of the model being unavailable (or you getting rate limited or running out of tokens!)"
- **Our assessment**: Sound and consistent with the Mugrage outage note, which supplies the dated incident evidence this excerpt lacks. Applies to AI features inside products; for agent harnesses it implies a defined behaviour on 429/529 rather than a crash.

### Claim 2: Use backup vendors that host the same model, accepting that they lag on the newest versions
- **Evidence**: Examples only: OpenAI models on Azure, Anthropic models via Google's Gemini Enterprise Agent Platform.
- **Confidence**: emerging
- **Quote**: "When using backup vendors like this, there may be a lag in terms of how quickly the latest models may be available, but given that you may not always want to be on the bleeding edge of the models you use to embed in your software (something we’ll discuss in just a moment), this is probably fine."
- **Our assessment**: A concrete, cheaper alternative to cross-vendor failover: same model, different host, so prompts and evals stay valid (contrast Claim 5). The "not on the bleeding edge" stance is a deliberate trade-off that conflicts with chasing newest models.

### Claim 3: Models can change behaviour without the vendor flagging it, and upgrades can change how prompts are handled, so AI code needs functional tests plus evals
- **Evidence**: Newman's reports ("I’ve seen reports") and the nondeterminism of LLMs; no specific incident cited.
- **Confidence**: emerging
- **Quote**: "You want to make sure that when the unexpected occurs, you are ones who get surprised first, rather than your users."
- **Further quote**: "this should be a mix of traditional functional tests, together with the use of AI evaluation tools (evals)"
- **Our assessment**: Supports pinning model versions and running evals before upgrades. The silent-drift premise is unevidenced here, but the test recommendation is low-regret. He points to *Evals for AI Engineers* (Shankar and Husain) and Gayathri Mohan's *Full Stack Testing* for depth.

### Claim 4: LLM call latency is hard to predict, so scale timeouts to expected output tokens or monitor streaming output to tell a hung call from a long one
- **Evidence**: Reasoning from the earlier chapter's preference for narrow latency variation; sources of variance listed (provider performance, rate limiting, long prompts). No implementation or measurement.
- **Confidence**: emerging
- **Quote**: "Some techniques to solve this can include dynamically setting timeouts based on the number of tokens being generated, or monitoring the streaming output from a model so you can track when the response starts coming back rather than waiting for the full response."
- **Our assessment**: Concrete and directly usable for harness design (stall detection on stream vs fixed wall-clock timeout). Stated as options, not a validated recipe.

### Claim 5: Mixing vendors in one flow multiplies failure modes, and prompts are not portable across models
- **Evidence**: Availability reasoning (every model in the flow must be up) and the claim that tuned prompts need re-evaluation.
- **Confidence**: emerging
- **Quote**: "All those models have to be available and functioning correctly at the time the flow is executed."
- **Further quote**: "a prompt tuned against one model will have to be reevaluated when moving to a different model, even if you stay within the same vendor ecosystem."
- **Our assessment**: Important counterweight to naive multi-model routing advice: multi-vendor as swap-ability is good, multi-vendor in series is a reliability cost. Product-of-availabilities is simple arithmetic, so we buy it.

### Claim 6: Build for swappable models and vendors, including checking whether your vendors depend on a single upstream model provider (Cursor/Anthropic pricing example)
- **Evidence**: Anecdote: Cursor passed on a significant cost increase in 2025 after Anthropic changed pricing. Stated by the author without a citation.
- **Confidence**: anecdotal
- **Quote**: "Make sure you aren’t wholly dependent on a single model or AI platform."
- **Our assessment**: Extends the podcast note's hedging claim with a second-order point (your vendor's vendor). The Cursor account is unverified here.

### Claim 7: Make AI spend visible, per person if possible, to understand value and catch runaway bills
- **Evidence**: James Stanier's LeadDev Berlin 2025 talk (a QA engineer spent €1,000 in a week on Claude Code, which turned out productive); reported Uber budget exhaustion in four months and Microsoft pulling Claude licences; an unsubstantiated Axios report of a $500 million licence spend.
- **Confidence**: anecdotal
- **Quote**: "This doesn’t need to be about limiting spend necessarily; it can be about understanding how you spend money and understanding what value that brings."
- **Our assessment**: The framing of spend visibility as a learning tool, not a policing one, is useful for team adoption. The anecdotes are second-hand and one is flagged by the author as unsubstantiated.

### Claim 8: GPU and memory shortages reduce general cloud capacity, so DR plans must not assume on-demand provisioning
- **Evidence**: Newman's conversations with clients struggling to secure capacity for non-AI workloads; no data.
- **Confidence**: anecdotal
- **Quote**: "I’ve already spoken to clients who are struggling to run “normal” (non-AI) workloads on some of the large public cloud providers, as they can’t secure enough capacity."
- **Our assessment**: Peripheral to the guide. Relevant only as a note that AI demand can degrade capacity for self-hosted or fallback infrastructure; mitigations (reserve, prioritise, run redundant) are standard DR.

### Claim 9: Review AI vendors and threat models more often than normal
- **Evidence**: A Thoughtworks vendor-health review anecdote; the volatility of the AI sector.
- **Confidence**: anecdotal
- **Quote**: "Review Your AI Vendors Regularly! Given the volatility in the space, make sure you review your AI vendors much more frequently than normal vendors."
- **Our assessment**: Process advice with no cadence given. Fine as a checklist item.

## Concrete Artifacts

```
Techniques named in the excerpt (Chapter 7: Resiliency and AI):
- Graceful degradation when model unavailable / rate limited / out of tokens
- Backup vendor for the same model (OpenAI models on Azure; Anthropic models via Google's Gemini Enterprise Agent Platform)
- Functional tests + evals as a pre-user tripwire for model changes
- Dynamic timeouts based on number of tokens being generated
- Monitor streaming output to track when the response starts coming back
- Per-person AI spend visibility
- More frequent vendor analysis and threat assessment for AI vendors
```

```
Orosz's closing takeaway (Pragmatic Engineer, 2026-10-13):
"My sense is that AI is making “resiliency basics” more important than before."
```

No code, configs or measurements in the source.

## Cross-References

- **Corroborates**: `blog-thoughtworks-mugrage-claude-outage-infrastructure.md` Claim 6 (graceful degradation with deterministic fallbacks), Claim 5 (single-vendor dependency as a single point of failure) and Claim 8 (AI-specific observability beyond uptime/latency). `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` Claim 10 (open-weight switching as insurance and pricing power) agrees with Claim 6 here.
- **Contradicts**: None filed. Claim 5's warning that multi-vendor flows lower availability is in mild tension with `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` Claim 4 (heterogeneous multi-model routing stack), but the two address different things (serial chaining vs. swap-ability), so it is a conditioning variable, not a contradiction.
- **Extends**: `blog-pragmaticengineer-orosz-newman-resilient-systems.md` Claim 3 (hedge vendors; multi-vendor, multi-model) with same-model backup hosting, the serial-chain availability warning, vendor-of-vendor dependency and spend visibility. Its Claim 4 (deterministic code over LLM calls) pairs with graceful degradation here. `blog-thoughtworks-mugrage-claude-outage-infrastructure.md` Claim 9 (multi-LLM failover needs a continuous eval suite per model) is echoed by Claim 5's prompt re-evaluation point.
- **Novel**: Dynamic token-based timeouts and stream-start monitoring for LLM calls; the argument that lagging a model version behind via a backup host is acceptable; the product-of-availabilities warning for multi-vendor flows; per-person spend visibility as an adoption tool.

## Guide Impact

- **Chapter 03**: When recommending evals, add that model upgrades and silent provider-side changes are a regression source, so run functional tests plus evals before moving model versions (Claim 3, anecdotal-level support). Hamel/Shankar eval references already exist in the corpus.
- **Chapter 05**: Vendor hedging section can add three points: same-model backup hosts, avoiding serial multi-vendor chains, and checking tool vendors' own upstream dependency (Claims 2, 5, 6). Add per-person spend visibility to adoption guidance (Claim 7). Keep the evidence level at anecdotal.
- **Chapter 02**: Where harness runtime behaviour is discussed, consider token-scaled timeouts and stream-start stall detection (Claim 4) and defined degradation on rate limits (Claim 1).

## Extraction Notes

- Fetched the page HTML directly and read the full text, including the Orosz intro and takeaways. Did not follow external links (Stanier's talk, Axios report, the cited books).
- Sections 1-3 (RPO/RTO, DR patterns) were read but not mined, per triage. Section 3's capacity paragraph is included as Claim 8.
- Quotes were copied from the page text; curly apostrophes are preserved.
- Anecdotes about Cursor, Uber, Microsoft and the $500 million spend are the author's second-hand accounts; none were verified.
