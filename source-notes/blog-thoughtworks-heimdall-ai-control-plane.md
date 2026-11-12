---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/we-built-ai-control-plane-reduce-LLM-expenses-prevent-data-leaks
source_type: blog-post
title: "We built an AI control plane to reduce LLM expenses and prevent data leaks"
author: Rahit Kar, Camila Oliveira and Anshul Kumar (Thoughtworks)
date_published: 2026-11-10
date_extracted: 2026-11-12
last_checked: 2026-11-12
status: current
confidence_overall: anecdotal
issue: "#4678"
---

# We built an AI control plane to reduce LLM expenses and prevent data leaks

> Thoughtworks describes Heimdall, a hackathon-built OpenAI-compatible gateway that chains fail-closed PII scrubbing, semantic caching, complexity routing, a graceful budget-degradation ladder, and OpenTelemetry, and reports self-measured results from a four-week, six-person internal pilot.

## Source Context

- **Type**: blog-post (practitioner experience report from an internal hackathon project)
- **Author credibility**: Three Thoughtworks engineers who built the tool for the internal AI/works Global Hackathon (2nd place LATAM, Best Collaboration Award per the post). Practitioners, but writing about their own project; no code, repo, or methodology is published.
- **Scope**: Architecture of a six-stage gateway and a four-week pilot with six users. Does NOT give a baseline methodology, quality impact of routing/caching, PII false-positive/false-negative rates, absolute dollar savings, or the complexity-scoring method.

## Extracted Claims

### Claim 1: Without centralized routing, every prompt defaults to the highest-tier model at uniform per-token rates, which is the structural cost problem a gateway addresses
- **Evidence**: Authors' framing of their motivation; no measurement of the share of "simple" prompts is given.
- **Confidence**: anecdotal
- **Quote**: "without centralized routing, every prompt, ranging from simple queries like \"what is HTTP 429?\" to complex tasks like \"refactor this system”, defaulted to the highest-tier, most expensive models at uniform per-token rates."
- **Our assessment**: Plausible and consistent with the waste pattern in the Kamelman note, but asserted rather than measured.

### Claim 2: Unfiltered AI access exposes corporate IP, PII and API credentials to external servers, and audit trails and protective filters are missing
- **Evidence**: Stated as motivation; the pilot reports 4,170 "leaks prevented" (see Claim 8).
- **Confidence**: anecdotal
- **Quote**: "Without audit trails or protective filters, prompts often expose sensitive corporate IP, personal data (PII) and API credentials to external servers, putting organizations and clients at risk."
- **Our assessment**: Credible threat; the post offers no incident data beyond the pilot count.

### Claim 3: Heimdall is a proxy gateway with a modular six-stage pipeline ("Guardians") between clients/IDEs/agent frameworks and LLM providers
- **Evidence**: Architecture description: Bifrost (proxy), Gjallarhorn (PII scrubber), Mimir's Well (semantic cache), The Norns (complexity router), Wall of Asgard (budget guard), Himinbjorg (observability).
- **Confidence**: anecdotal
- **Quote**: "Heimdall acts as a control plane and proxy gateway operating seamlessly between client applications, IDE extensions, or agentic frameworks and downstream LLM providers."
- **Our assessment**: A useful reference decomposition of what a "control plane" contains. The stage order given in the post is proxy → PII → cache → router → budget → observability, which also matters (scrub before cache so cached content is already clean), though the post does not argue this explicitly.

### Claim 4: Adoption friction is minimal because the gateway exposes an OpenAI-compatible endpoint; integration is a base-URL change
- **Evidence**: Design description of the Bifrost stage.
- **Confidence**: anecdotal
- **Quote**: "Serves an OpenAI-compatible API endpoint. Integration requires changing a base URL string without installing custom SDKs."
- **Our assessment**: Same adoption lever as other gateways in the corpus. Caveat: tools that speak only Anthropic-native protocols would need translation, which the post does not discuss.

### Claim 5: PII/credential scrubbing combines Presidio, spaCy NER and custom regex, and is fail-closed: a scrubbing error halts the request
- **Evidence**: Design description; no accuracy numbers.
- **Confidence**: anecdotal
- **Quote**: "Configured as a fail-closed mechanism: if scrubbing encounters an error, the request is halted immediately."
- **Our assessment**: Fail-closed is the right default for a security control, but it trades availability for safety and the post gives no false-positive rate or failure-rate data. Redaction of code (identifiers, paths) by NER could degrade prompt quality; unaddressed.

### Claim 6: Complexity scoring and PII sanitization run in parallel via async workers, with ~14ms total overhead against 2–15 second LLM calls
- **Evidence**: Self-reported latency figure from the pilot.
- **Confidence**: anecdotal
- **Quote**: "The total processing overhead is approximately 14ms, virtually imperceptible when downstream LLM calls take anywhere from two to 15 seconds."
- **Our assessment**: Plausible for small regex/NER workloads. Note the tension: PII scrubbing is described as running in parallel with scoring, yet fail-closed semantics require the scrub to complete before forwarding. No percentile latency or load data.

### Claim 7: A router sends simple prompts (score < 0.30) to a local model at $0, and budget degradation shifts to cheaper models instead of failing
- **Evidence**: Design description; tier prices listed as Local (0) → Haiku (1/M) → Sonnet (3/M) → Opus (5/M), units/currency symbols are missing in the post. The scoring method and quality impact are not described.
- **Confidence**: anecdotal
- **Quote**: "Simple queries (score < 0.30) route to a local LLM at $0."
- **Our assessment**: Pattern is credible, but quality of local-model answers on "simple" prompts is unmeasured. Quoted tier prices should be treated as illustrative.

### Claim 8: The budget guard enforces per-team, per-model, per-period thresholds and degrades gracefully (Opus → Sonnet → Haiku → Local) instead of terminating queries
- **Evidence**: Design description; no pilot data on how often degradation triggered or developer reaction.
- **Confidence**: anecdotal
- **Quote**: "Instead of abruptly terminating developer queries when a tier's budget is reached, it implements an automated, graceful degradation ladder (Opus → Sonnet → Haiku → Local)."
- **Our assessment**: Distinct from hard-cap budgets in the corpus (Vercel blocks requests when a key's limit is exceeded). Silent downgrade preserves flow but could surprise users with lower quality; the post doesn't say whether developers are notified.

### Claim 9: Pilot result: only 36.4% of requests reached a paid API (63.6% reduction), with a 34.2% cache hit rate and 4,170 PII/credential leaks "prevented"
- **Evidence**: Four-week internal pilot, six Thoughtworkers; table compares "Without Heimdall" (100% paid) with "With Heimdall". No baseline methodology, no dollar figures, no quality or false-positive data.
- **Confidence**: anecdotal
- **Quote**: "To validate Heimdall under real conditions, we conducted a four-week internal production pilot with six Thoughtworkers across diverse delivery streams."
- **Our assessment**: The 63.6% is request-count, not cost, and is arithmetically the combination of cache hits (34.2%) and local/other routing (~29.4%); the "without" column is assumed at 100% by construction. "Leaks prevented" counts detections, not verified true leaks. n=6; do not generalize.

### Claim 10: Cache-key normalization (stripping IDE metadata such as file paths and cursor positions) mattered more than the caching algorithm
- **Evidence**: Authors' lesson from the pilot; no ablation data.
- **Confidence**: anecdotal
- **Quote**: "Smart cache keys mattered more than smart caching algorithms."
- **Our assessment**: The most transferable insight: IDE/agent clients inject volatile context that defeats exact or semantic matching. Plausible and cheap to apply, but unquantified.

### Claim 11: Provider-side prompt caching and output/context limits are further cost layers; the post claims 11x discounts on repeated system prompts
- **Evidence**: One-line assertion under "Make each call cheaper"; unclear whether implemented in Heimdall or merely recommended.
- **Confidence**: anecdotal
- **Quote**: "Anthropic prompt caching gives 11x discounts on repeated system prompts."
- **Our assessment**: Figure is unsourced and doesn't match the commonly cited ~10x cheaper cache reads; treat as approximate. Also note the interaction with routing: per-model prompt caches mean switching models mid-session forfeits cache benefits (see Google note Claim 9).

### Claim 12: Policy does not scale; engineering controls do
- **Evidence**: Argument by assertion in the conclusion.
- **Confidence**: anecdotal
- **Quote**: "Most answer with policy. \"Don't paste sensitive data into ChatGPT.\" But policy doesn't scale. Engineering controls do."
- **Our assessment**: A clean statement of the editorial thesis for the security and cost-governance chapters; supported by design, not by comparative evidence.

### Claim 13: Components are decoupled so teams can adopt individual guardians (e.g., only the PII scrubber or only the semantic cache)
- **Evidence**: Design principle; no open-source release or repo is cited.
- **Confidence**: anecdotal
- **Quote**: "Any organization or internal team can easily deploy the full suite or adopt individual components, such as the PII scrubber or semantic cache, into their existing AI architecture with minimal overhead."
- **Our assessment**: Sensible, but the claim is unverifiable since the tool does not appear to be publicly available.

### Claim 14: Observability via OpenTelemetry covers cost, latency, cache hit rate, routing decisions and PII filtration events
- **Evidence**: Design description (e.g. New Relic integration).
- **Confidence**: anecdotal
- **Quote**: "Utilizes OpenTelemetry integration with platforms like New Relic to deliver fine-grained telemetry spanning cost, latency, cache hit rates, model routing decisions, and PII filtration events."
- **Our assessment**: Logging routing decisions and filtration events alongside cost is what makes the other controls auditable.

## Concrete Artifacts

```
Heimdall pipeline (source: "What Heimdall does")
Bifrost        proxy gateway, OpenAI-compatible endpoint (change base URL)
Gjallarhorn    PII/IP scrubber: Presidio + spaCy NER + custom regex; fail-closed
Mimir's Well   semantic cache (IDE noise stripped from keys)
The Norns      complexity router (score < 0.30 -> local Ollama model)
Wall of Asgard budget guard per team/model/period; Opus -> Sonnet -> Haiku -> Local
Himinbjorg     OpenTelemetry observability (e.g. New Relic)
```

```
Pilot table (source: "Results from a four week pilot"; 4 weeks, 6 users)
Metric                     Without Heimdall   With Heimdall
Requests hitting paid API  100%               36.4% (63.6% reduction)
Model selection            Always expensive   Dynamic (Local / Haiku / Sonnet)
PII protection             None               4,170 leaks prevented
Cost visibility            Blind spend        Per-request tracing
Cache hit rate             -                  34.2%
```

## Cross-References

- **Corroborates**: `blog-thoughtworks-kamelman-token-crisis.md` Claim 8 (premium models used for non-premium tasks is a primary waste pattern); Heimdall's router/cache are an implementation of the mitigation. `blog-anthropic-claude-apps-gateway.md` Claim 2 (self-hosted control plane with centrally enforced policy and per-user cost attribution) and Claim 7 (spend limits) show the same gateway-as-control-plane pattern from a vendor.
- **Contradicts**: None filed. Mild tension, not a contradiction: `blog-google-cost-per-task-classifier-routing.md` Claim 9 says prompt caching is bound to one model so per-turn routing conflicts with caching, whereas Heimdall advocates routing and provider prompt caching together without addressing the conflict. Also Heimdall degrades silently on budget exhaustion, whereas `blog-vercel-ai-gateway-api-key-budgets.md` Claim 1 blocks requests at the limit; these are different design choices, not opposed claims.
- **Extends**: `blog-google-cost-per-task-classifier-routing.md` (Claims 1 and 7 on classifier-based routing) by adding PII scrubbing, semantic caching and a budget ladder around the router.
- **Novel**: Fail-closed PII/credential scrubbing at the gateway with reported overhead; budget degradation ladder as an alternative to hard cutoffs; the cache-key-normalization lesson for IDE traffic; first pilot-metric set (cache hit rate, paid-request share) for a gateway in the corpus.

## Guide Impact

- **Chapter 05 (team adoption / cost governance)**: Add Heimdall as an example of a gateway-level control, contrasting hard budget caps (Vercel) with a graceful degradation ladder; attribute the 36.4% / 34.2% figures to a six-person internal pilot, not as generalizable savings.
- **Chapter 06 (security threat model)**: Cite the fail-closed PII/credential scrubbing stage as a concrete mitigation for leakage to external providers, with the explicit caveat that no false-positive/false-negative data is provided and "leaks prevented" is a detection count.
- **Chapter 02 (harness engineering)**: Mention normalizing volatile IDE metadata (file paths, cursor positions) before cache-key generation as a practical lesson when caching agent/IDE traffic.

## Extraction Notes

- Read the full article (single page, no sub-pages); fetched raw HTML and extracted text so quotes are verbatim (a straight-quote escape `\"` is used inside the quoted strings for the source's inner quotation marks).
- The source is thin on method: no repo, no scoring algorithm, no baseline definition, no quality metrics. The "$" signs for tier prices are absent in the source text ("Haiku(1/M)"), so units are uncertain.
- The Prospector's triage comments disagree on which stats to emphasize (63.6% vs 36.4%); both are the same figure. Confidence graded anecdotal given n=6 and self-reporting.
