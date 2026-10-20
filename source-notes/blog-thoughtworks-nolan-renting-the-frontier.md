---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/renting-the-frontier--owning-the-core-ip--how-we-cut-ai-forecast
source_type: blog-post
title: "Renting the Frontier, Owning the Core IP: How We Cut AI Forecast Costs from $40M to $11M"
author: Andy Nolan (Thoughtworks)
date_published: 2026-10-15
date_extracted: 2026-10-20
last_checked: 2026-10-20
status: current
confidence_overall: emerging
issue: "#4231"
---

# Renting the Frontier, Owning the Core IP: How We Cut AI Forecast Costs from $40M to $11M

> A Thoughtworks internal case study of a per-workload "token sourcing strategy": a two-axis placement grid, one AI gateway fronting three fixed user tiers (frontier / open-weight / light) with per-person and per-unit chargeback, and a traffic-replay plus Monte Carlo method used to get leadership to approve a cost range rather than a point estimate. All dollar figures are self-reported forecasts, not realized savings.

## Source Context

- **Type**: blog-post (vendor-authored practitioner case study, Thoughtworks Insights; carries a disclaimer that opinions are the author's, not necessarily Thoughtworks').
- **Author credibility**: Andy Nolan, Global Vice President, Artificial Intelligence at Thoughtworks; co-author of the Nemotron 3.5 evaluation posts. First-hand operator of the internal gateway ("Agent/works") whose logs form the basis of the analysis. Commercial interest: the post promotes Thoughtworks' AI Factory offering ("Take control of your AI Future, today.").
- **Scope**: Internal Thoughtworks AI spend (inference only; the chart caption states it "excludes the platform team and change program"). Covers the sourcing framework, the six-step method, the gateway/tier design, and rollout/enablement. Does NOT publish the grid image data, the benchmark numbers, per-tier model names, per-person budget sizes, or the simulation inputs, so the 55%/72% reductions cannot be independently checked. The Nemotron results are only referenced (see Cross-References).

## Extracted Claims

### Claim 1: Thoughtworks' internal frontier-API spend reached $450K/month by September 2026 and had grown more than eightfold in nine months, about 27% per month
- **Evidence**: Self-reported internal spend figures and a chart ("2026 AI frontier model token spend for internal usage"); no raw data.
- **Confidence**: anecdotal
- **Quote**: "By September 2026, Thoughtworks was spending $450K a month on frontier model APIs for internal use alone, and the bill was growing about 27% a month."
- **Our assessment**: A useful single-organization data point on adoption-driven cost growth, consistent with other cost-shock reports in the corpus (Uber, Meta). Self-reported; 27%/month is a trailing rate, not a durable trend.

### Claim 2: Cost and IP exposure share one root cause — all intelligence is rented — and the answer is to decide per workload what to rent versus own, not to stop renting
- **Evidence**: Argument by the author; cites Satya Nadella's July 2026 statement that models learn from customers' prompts and corrections, and an Enterprise Technology Research survey (Sept 2026) putting open-weight models at 34% of enterprise token usage (up from 23%).
- **Confidence**: emerging
- **Quote**: "The answer is not to stop renting. Frontier models are worth their price for some work. The answer is to decide, workload by workload, which AI you rent and which you own."
- **Our assessment**: The framing is reasonable but the "providers see your IP" argument is stated as a general risk without evidence of actual leakage; the post itself concedes "None of this requires bad faith." Read as a risk-posture argument, not a demonstrated harm. The survey statistics are second-hand and not verified here.

### Claim 3: Workloads are placed on a nine-cell grid using six questions across two axes (domain differentiation × security/sovereignty)
- **Evidence**: Framework description; a heat-map image (not extractable as text) shows the nine cells. No worked placement of named workloads is given in the text.
- **Confidence**: emerging
- **Quote**: "For a given workload, the highest score on a given axis determines the right position in the grid."
- **Our assessment**: Novel, reusable, and cheap to adopt as a checklist. Weakness: placement rule is stated in one sentence, and there are no examples of which real workloads landed in which cells.

### Claim 4: The six placement questions
- **Evidence**: Listed verbatim in the article.
- **Confidence**: emerging
- **Quote**: "How unique is the task to us?"; "What if a competitor used the same model?"; "Can the data leave our environment?"; "What if the provider changed terms or switched off?"
- **Our assessment**: The "what if the provider changed terms or switched off?" question pairs well with the export-control shutdown described in the sovereign-AI note. Remaining questions: "How much does a better model change the result?" and "Where must it run?" (quoted separately here to keep each quote contiguous).

### Claim 5: Open-weight models can close the capability gap to frontier on a specific task via post-training, so they belong in every sourcing strategy
- **Evidence**: Asserted; backed only by reference to the author's two Nemotron evaluations (adapters "trained in hours", optimized models "roughly halving GPU cost per output token").
- **Confidence**: emerging
- **Quote**: "So by post-training open-weight models on your specific task you can close the performance gaps."
- **Our assessment**: Plausible and supported in the linked Nemotron note for legal/healthcare domains, but the sentence generalizes beyond the evidence (two domains, one model family). The "roughly halving" figure is the author's own result and should not be cited as independently measured.

### Claim 6: The strategy was built from 18 months of gateway logs, and any gateway-routed enterprise can repeat the six steps
- **Evidence**: Self-described method: gateway logs → map workloads to grid → segment users/model demand → replay traffic across models and hosting modes → Monte Carlo simulation → decide mix.
- **Confidence**: emerging
- **Quote**: "Eighteen months of logs, covering thousands of users on frontier and open-weight models, gave us the baseline."
- **Our assessment**: The most transferable part of the post: gateway telemetry as the foundation for sourcing decisions. Note that it presupposes a gateway already exists.

### Claim 7: Spend is concentrated — a few hundred heavy users and three heavy workloads (~27% of the bill) drive most cost
- **Evidence**: Stated segmentation result; no distribution shown.
- **Confidence**: anecdotal
- **Quote**: "a few hundred heavy users who drive most of the spend, the three heaviest AI workloads, which together carried about 27% of the bill, and the long tail of everyone else."
- **Our assessment**: Consistent with the heavy-user spend figures in the Uber report. The coincidental "27%" (share of bill) vs "27%" (monthly growth) are distinct numbers in the source.

### Claim 8: Utilization, not list price, determines whether dedicated capacity beats serverless; managed vs rented GPUs is a price-vs-people trade
- **Evidence**: Benchmark replay of real traffic across serverless, managed inference, and IaaS (rented GPUs); qualitative findings only, no numbers.
- **Confidence**: emerging
- **Quote**: "Utilization, not list price, decides the cost."
- **Our assessment**: Matches standard cloud economics; the value is confirmation on LLM traffic with business-hours demand. Also: "For spiky demand, serverless wins because you're not paying for idle compute." And "Managed inference gives the lower per-token price without a dedicated inference team." Without numbers, the break-even point is unknown.

### Claim 9: Monte Carlo simulation lets leadership approve a cost range with a probability of staying in budget instead of a point estimate
- **Evidence**: Method description; outcome stated as 2028 do-nothing $16M (up to $40M) vs $6.8M–$11M under the strategy at 70–90% confidence; 55% worst-case reduction in 2027, 72% in 2028.
- **Confidence**: anecdotal
- **Quote**: "Doing nothing is forecast at $16M in 2028, and up to $40M if growth doesn't slow; the strategy lands between $6.8M and $11M at 70–90% confidence."
- **Our assessment**: The headline numbers are model outputs from the author's own assumptions, vendor-published, with no realized results. The title's "Cut ... from $40M to $11M" compares a worst-case forecast to a worst-case forecast. Treat the *method* (range-based approval) as the contribution, not the savings.

### Claim 10: One gateway exposes three fixed user-facing tiers; the backing model is swapped centrally
- **Evidence**: Architecture description of Agent/works (launched June 2026). Top tier = frontier model for highest-judgment work (complex agentic coding, strategy, research); middle = state-of-the-art open-weight for daily use (drafting, summarizing, code assistance, analysis); light = high-efficiency open-weight for classification, extraction, routing. Initially only lower tiers move to open-weight.
- **Confidence**: emerging
- **Quote**: "People choose a tier, high, medium or light, not a model or a provider."
- **Our assessment**: Strong reusable pattern: stable user vocabulary decoupled from fast-changing model supply. Risk not discussed: users who want frontier quality for "daily" tasks, and how tier misuse is policed. No developer-satisfaction or quality data on the open-weight middle tier is given, which is the biggest unproven assumption.

### Claim 11: Every request is metered and attributed, with per-person and per-unit budgets and chargeback to the unit generating spend
- **Evidence**: Design statement; no description of budget sizes or enforcement behavior.
- **Confidence**: emerging
- **Quote**: "Every request is metered and attributed to a person, a workload and a business unit, with budgets per person and per unit, and spend charged back to the unit that creates it."
- **Our assessment**: Aligns with the feature-level budget and circuit-breaker practices elsewhere; this adds organizational chargeback. Hard-limit versus soft-limit behavior unspecified.

### Claim 12: The tiers stay fixed while what sits behind them is reviewed on triggers (workload change, major price change, model release) by replaying traffic
- **Evidence**: Process description.
- **Confidence**: emerging
- **Quote**: "The review is triggered by changes in workload characteristics, major price changes and model releases."
- **Our assessment**: Sensible; effectively a regression-eval loop for model selection. Requires retained traffic samples and an eval harness, which the post does not detail.

### Claim 13: Access expansion is gated by enablement: briefing, chargeback education before the first bill, policy on key hygiene/client work/data residency, cohort onboarding with token-literacy training, and visibility of own usage against budget
- **Evidence**: Description of rollout plan (planned, not reported outcomes).
- **Confidence**: anecdotal
- **Quote**: "Wider access only stays affordable if people understand how their choices drive cost."
- **Our assessment**: Directly relevant to team adoption. It describes a plan; no adoption results are reported.

### Claim 14: Regional and regulatory rules impose hard limits that shape sourcing
- **Evidence**: Two examples given by the author.
- **Confidence**: settled (as stated constraints at this company)
- **Quote**: "EU traffic stays in EU regions under GDPR, and staff in China cannot use the frontier models the rest of the firm uses."
- **Our assessment**: A concrete illustration that a single global model catalog is often infeasible; the gateway is where this is enforced.

## Concrete Artifacts

```
Six placement questions (Andy Nolan, Thoughtworks, 2026-10-15):

Domain differentiation (vertical axis):
How unique is the task to us?
What if a competitor used the same model?
How much does a better model change the result?
Security and sovereignty (horizontal axis):
Can the data leave our environment?
Where must it run?
What if the provider changed terms or switched off?
```

```
Grid axes (paraphrase of the article's description, not a quote):
  Vertical:   commodity compute -> frontier-level reasoning -> custom tuning
  Horizontal: vendor-hosted API -> own cloud account in own region -> governed enclave on own infrastructure
  Nine cells; "cheapest capable API" at one extreme, "fine-tuned open model on our own infrastructure" at the other.
```

```
Three hosting modes benchmarked (paraphrase):
  serverless          - pay per token, no capacity reserved
  managed inference   - dedicated capacity someone else operates
  infrastructure as a service - rented GPUs the org operates
```

```
Headline figures (self-reported by Thoughtworks, forecasts):
  Sept 2026 internal frontier API spend: $450K/month, ~27%/month growth
  2028 do-nothing: $16M (up to $40M)
  2028 with strategy: $6.8M-$11M at 70-90% confidence
  Worst-case reduction vs do-nothing: 55% (2027), 72% (2028)
  Inference spend only; excludes platform team and change program
```

## Cross-References

- **Corroborates**: `blog-thoughtworks-kamelman-token-crisis.md` Claim 8 (waste from premium reasoning models used on non-premium tasks such as classification) and Claim 9 (waste stems from unreviewed defaults, no owner of aggregate outcome): the tier design here assigns classification/extraction to a light tier by construction. `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` Claim 4 (multi-model routing pattern) and Claim 3 (self-hosting cost is engineering talent): echoed by the "price vs people" finding here. `blog-thoughtworks-lovin-gall-local-inference-boundary.md` Claim 13 (hybrid inference as the design pattern).
- **Contradicts**: None found. (Mild tension, not a contradiction: Kimi K3 note Claim 6 warns that self-hosted open-weight models shift guardrail burden to the deployer; this post does not discuss that cost.)
- **Extends**: `blog-thoughtworks-lujan-roush-nolan-nemotron-3-5-lightning-eval.md` (same author; Claims 1-4 on domain adapters and Claim 9 on throughput/cost per million output tokens underpin this post's "post-train open-weight" and "halving GPU cost" assertions; this post generalizes them without new evidence). `blog-thoughtworks-kamelman-sovereign-ai-dependency.md` Claim 4 (export-control shutdown of frontier models) gives the real-world instance of the "provider switched off" risk this grid asks about. `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 8a (Shopify dashboard + circuit breakers) is the per-person control analog of this post's per-person/per-unit budgets. `blog-vercel-ai-gateway-api-key-budgets.md` is a related gateway-budget mechanism (not claim-cited).
- **Novel**: The two-axis, six-question workload placement grid; the fixed high/medium/light tier abstraction over a gateway with centrally swappable backing models; replaying real gateway traffic across hosting modes; Monte Carlo cost ranges as the approval artifact; chargeback-before-first-bill enablement sequencing.

## Guide Impact

- **Chapter 05 (team adoption)**: Add the fixed-tier gateway pattern (users choose high/medium/light, not a model) with per-person/per-unit metering and chargeback as a cost-control option for orgs rolling out AI broadly; cite Claims 10, 11, 13. Add the enablement sequence (brief leaders on chargeback before the first bill; token-literacy training per cohort). Label the savings figures as self-reported forecasts.
- **Chapter 06 (security/threat model)**: Add the "security and sovereignty" axis questions (can data leave, where must it run, what if the provider changes terms) as a workload-classification checklist, with the EU/China examples (Claim 14). Link to the sovereign-AI note for the shutdown risk.
- **Chapter 00 (principles)**: Possible principle: decide model sourcing per workload; use measured traffic rather than list price (Claims 6, 8). Keep as "emerging".
- **Chapter 01 (daily workflows)**: Tier-choice guidance (frontier for complex agentic coding; open-weight for drafting/summarizing/code assistance) is the author's design, not evidence that the middle tier suffices for coding; do not recommend without quality data.

## Extraction Notes

- Fetched the full article HTML via curl and read the entire text (about 17K chars). Charts and the grid heat map are images; only their captions are available. Several sentences are quoted as separate fragments to keep each quote contiguous.
- Followed no sub-pages: the linked Nemotron posts are already covered by an existing note; the AI Factory page is marketing.
- The post is vendor-authored and promotional; all financial figures are forecasts from undisclosed assumptions. The title claims "cut ... from $40M to $11M," which compares upper-bound forecasts, not realized spend. No contradiction issue filed.
