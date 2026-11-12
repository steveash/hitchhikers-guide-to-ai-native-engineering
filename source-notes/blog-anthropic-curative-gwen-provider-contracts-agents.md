---
source_url: https://claude.com/resources/articles/how-curative-is-building-a-national-provider-network-with-agents-on-claude
source_type: blog-post
title: "How Curative is building a national provider network with agents on Claude"
author: Anthropic (Camy Pearson, Michael Segner); interviews with Curative CEO Fred Turner and CTO Isaac Turner
date_published: 2026-11-10
date_extracted: 2026-11-12
last_checked: 2026-11-12
status: current
confidence_overall: anecdotal
issue: "#4669"
---

# How Curative is building a national provider network with agents on Claude

> A vendor-published customer case study of a production agent hierarchy (Opus negotiator, Sonnet rate reviewer, Haiku outbound judge) with concrete operating lessons: one general tool, stateless per-deal runs, second-agent review instead of more authority, and a Claude Code improvement loop over sampled runs.

## Source Context

- **Type**: blog-post (Anthropic "How startups build with Claude" customer case study; category "Best practices")
- **Author credibility**: Written by Anthropic staff with first-person quotes from Curative's CEO and CTO. Operators' accounts of their own system, but no code, config, or prompts are published, and Anthropic has a commercial interest in the story.
- **Scope**: Covers Curative's contracting agent "Gwen" and its supporting agents, team impact, and seven lessons plus a short best-practices Q&A. Does not cover prompts, tool schemas, the judge's criteria, error rates, or independent measurement. All figures are self-reported.

## Extracted Claims

### Claim 1: A hierarchy of differently sized models handles one deal: Opus negotiator, Sonnet rate reviewer, Haiku outbound judge
- **Evidence**: Architecture description from Curative. No accuracy or cost-by-tier data.
- **Confidence**: anecdotal
- **Quote**: "The rate reviewer runs on Sonnet."
- **Our assessment**: Concrete model-tier split matching the "expensive model does the work, cheaper models gate it" pattern. The article says Gwen runs "mostly on Claude Opus" and does not say what the "mostly" excludes. Haiku is the judge: "A judge, which runs on Haiku, reads every communication before it’s sent."

### Claim 2: A second reviewer agent worked better than granting the primary agent more authority
- **Evidence**: CEO's account of an approval queue loosened over time; reviewer clears about two-thirds of requests, with the rest going to the CEO.
- **Confidence**: anecdotal
- **Quote**: "Having a second agent review rates worked better than just giving Gwen more authority"
- **Our assessment**: Credible design lesson, but "worked better" is unquantified. The CEO says the residual requests are ones "that would come to me even if this wasn’t an agent-led motion", suggesting the human is left with the genuinely hard cases. The two-thirds figure is self-reported.

### Claim 3: A judge on every outbound message was added after a real leak, and blocked messages return their reason so the agent can retry
- **Evidence**: Specific incident (copying providers on internal notes about the rate ceiling) that motivated the control.
- **Confidence**: anecdotal
- **Quote**: "Curative added it after Gwen copied providers on internal notes about how high it could go. A blocked message comes back with the reason, so Gwen can rewrite it and try again."
- **Our assessment**: A rare named failure mode paired with the control it caused: confidential negotiating limits leaking into outbound text. The reason-returned loop makes the judge a feedback channel rather than a hard stop. No false-positive or block rates given.

### Claim 4: Start with one general tool (run Python with a docx library) rather than bespoke redlining tools
- **Evidence**: Curative's experience: specific tools "doesn't work that well" for redlining.
- **Confidence**: anecdotal
- **Quote**: "What we found works best is that the model just has one tool, which is run Python, and it does all the redlining with a docx library. It works beautifully."
- **Our assessment**: Consistent with the broader "fewer, more general tools" direction. Single vendor-reported case, no comparison data. Note the same tool let Gwen produce unrequested artifacts (see Claim 9), a side effect of generality.

### Claim 5: Per-deal runs are isolated with no cross-deal memory; the agent that does keep memory risks uncorrectable "doom loops"
- **Evidence**: Design choice for Gwen; experience with Brad (sales agent) cited as the counter-example.
- **Confidence**: anecdotal
- **Quote**: "You can end up making notes that are wrong and then get into these doom loops, where it has a bad memory that can never be cleared,"
- **Our assessment**: Useful failure mode for persistent memory: wrong notes self-reinforce. Brad's memory "works but needs care", so this is not a ban on memory. Isolation is also a confidentiality property: "so nothing from other deals influences it."

### Claim 6: Improve the system from outside the run by having Claude Code sample recent runs on a schedule and open PRs
- **Evidence**: Described cadence ("every few days") and sample size (last 10,000 runs) from the CEO.
- **Confidence**: anecdotal
- **Quote**: "Every few days, Fred gives Claude Code the same prompt: sample the last 10,000 runs, flag anything weird, and open a PR to fix it."
- **Our assessment**: Concrete, replicable operating loop. Unknown: what the PRs change (prompts, tools, policy docs?), acceptance rate, and who reviews them.

### Claim 7: Authority should start low, be loosened in steps, and deterministic decisions loosen first
- **Evidence**: Curative's progression from a human approval queue to the reviewer agent.
- **Confidence**: anecdotal
- **Quote**: "Less than you think it can handle."
- **Our assessment**: Matches progressive-trust guidance. The article adds that limits were loosened "for more deterministic decisions" first, then the reviewer was added.

### Claim 8: Experiment away from regulated data first, then transfer controls; use back-end limits and audit logging for PHI
- **Evidence**: Gwen was barred from PHI for a long time; controls then transferred.
- **Confidence**: anecdotal
- **Quote**: "We learned how to do it there and then transferred it over into PHI land,"
- **Our assessment**: Sensible staged rollout. Controls named are generic ("back-end controls limit what enters a conversation", activity logged for audit); no implementation details.

### Claim 9: Monitor for unrequested agent behavior and check it against your risk profile
- **Evidence**: Two examples: Gwen made a flyer with its Python tool, and asked an in-network office to train staff after a member was turned away.
- **Confidence**: anecdotal
- **Quote**: "Watch what the agent starts doing on its own and make sure it matches your risk profile."
- **Our assessment**: The article frames these examples mostly as positive, but they are scope expansion. Triaged as a monitoring signal, not a success. Pairs naturally with the sampling loop in Claim 6.

### Claim 10: Meeting counterparties on their channel (fax) more than doubled win rate
- **Evidence**: CTO statement; no baseline numbers.
- **Confidence**: anecdotal
- **Quote**: "A fax tool more than doubled Gwen’s win rate."
- **Our assessment**: Domain-specific (healthcare providers) but generalizes to "integrate the channel the counterparty actually uses". Magnitude unverified.

### Claim 11: Reported scale and cost: 2,000–2,400 contracts/week, ~20M tokens per contract (about a tenth of original cost), ~50x faster than 2025
- **Evidence**: Self-reported figures in the "quick pitch" and body.
- **Confidence**: anecdotal
- **Quote**: "Each contract takes about 20 million tokens to complete, roughly a tenth of the original cost."
- **Our assessment**: Useful order-of-magnitude token budget for a long-running negotiation agent. "Original cost" baseline undefined; "50x faster" comes from the article's own intro ("about 50 times faster than its team did in 2025"). Not independently measured.

### Claim 12: Team adoption: contracting team grew 45 to ~55, each ~2.5x as productive, with a shared pay target for people and agents
- **Evidence**: Self-reported headcount and productivity; compensation design described.
- **Confidence**: anecdotal
- **Quote**: "Curative pays its contracting team on Gwen’s deals too, so people and agents share one target."
- **Our assessment**: The shared-incentive detail is the interesting, non-obvious part; humans take warm leads by phone while Gwen handles cold outreach and paperwork. The 2.5x figure is unaudited.

### Claim 13: Agents should be judged against human error rates, not perfection, and audited via logging + judge + sampling
- **Evidence**: CTO's framing in the Q&A.
- **Confidence**: anecdotal
- **Quote**: "The bar isn’t perfect,"
- **Our assessment**: Reasonable acceptance-criteria framing (continuing in source: "The bar is, if you had a thousand people signing contracts, how many mistakes would they make that you regret?"). Provides no actual error data, so the comparison is asserted rather than shown.

## Concrete Artifacts

```
Agent hierarchy (source: Curative case study, Nov 10 2026)
- Gwen: one run = one provider deal, mostly Claude Opus, no memory across deals
  - single tool: run Python (docx library) for redlining and merging both sides' changes
  - fax tool (more than doubled win rate)
- Rate reviewer: Sonnet; Gwen writes why it wants to exceed the standard rate template;
  clears ~2/3, remainder goes to CEO
- Judge: Haiku; reads every outbound communication; blocked message returns reason -> Gwen rewrites
- Downstream: credentialing agent, then agents load provider data/contract for claims pricing
- Outside the run: Claude Code, every few days: "sample the last 10,000 runs, flag anything
  weird, and open a PR to fix it"
```

```
Reported metrics (all self-reported; attribute to Curative/Anthropic)
- 23,000 provider contracts signed with Gwen
- 2,000-2,400 new contracts/week, vs 2,100 in all of 2025
- ~20M tokens/contract, "roughly a tenth of the original cost"
- Form-to-signature as quick as an hour
- Contracting team 45 -> ~55, ~2.5x productivity each
- Claims dispute responses ~90 days -> under 30 minutes (email/fax)
- 13 engineers rebuilt claims/prior-auth/finance systems with Claude Code this year
```

No prompts, tool schemas, or config were published.

## Cross-References

- **Corroborates**: `blog-anthropic-block-fable-orchestration-migrations.md` Claim 5 (frontier model on big problems, smaller models on details) and Claim 10 (guardrails run outside the model loop as cheap checks and small classifiers); Curative's Haiku judge is a small-model guard of the same kind. `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2 (generator-verifier) maps to the Sonnet rate reviewer and Haiku judge. `blog-anthropic-asana-coachable-agents.md` Claim 12 (audit of agent contributions, durable records) aligns with Curative's logging for audit.
- **Contradicts**: None filed. Curative's stateless Gwen vs. persistent memory is a conditioning difference (negotiator vs. sales agent), not a direct contradiction of `blog-anthropic-claude-managed-agents-memory.md` Claim 1 (memory enables learning across sessions); it is a cautionary counterweight.
- **Extends**: `blog-anthropic-asana-coachable-agents.md` Claim 5 (separate working with an agent from training it, gate permanent memory edits): Curative adds a concrete failure ("doom loops" from uncorrectable wrong notes). `blog-anthropic-multi-agent-coordination-patterns.md` Claim 4 (persistent vs. bounded context) gains a production data point favoring bounded runs for isolated tasks. `blog-anthropic-ibragimov-japan-bdr-nakama-agent-fleet.md` and `blog-anthropic-carta-healthcare-context-engineering.md` are neighbouring case studies (sales agent fleet; regulated healthcare) without overlap on these specific controls.
- **Novel**: A named incident (leaking the rate ceiling) driving an every-outbound-message judge with reasoned rejection; the stateless-run vs. persistent-memory split with the "doom loop" failure; the single run-Python tool finding for redlining; a scheduled Claude Code sampling loop over 10,000 runs; the shared human/agent pay target; production token-per-task figure (~20M).

## Guide Impact

- **Chapter 02 (harness / agent hierarchy)**: Add Curative as a production example of tiered models in one workflow (Opus worker, Sonnet reviewer, Haiku judge) and of preferring one general tool over bespoke tools for complex document edits. Attribute as anecdotal vendor-reported.
- **Chapter 02 / memory discussion**: Cite the "doom loops" caution alongside the Asana note's memory-governance material: default to isolated runs where cross-task context is not needed; if memory is kept, plan how wrong notes get cleared.
- **Chapter 03 / verification**: Add the pattern "judge on every outbound message, block with reason, agent rewrites", and "add a reviewer agent rather than more authority".
- **Chapter 05 (team adoption)**: Add the shared-target compensation detail and the 45 -> ~55 team-growth claim, flagged as self-reported.
- **Chapter 06 (security/operations)**: Add staged regulated-data rollout (away from PHI first), audit logging, and the scheduled sampling loop; flag unrequested agent actions as a monitoring signal.

## Extraction Notes

- Read the full article text (fetched raw HTML and stripped markup so quotes are verbatim). No sub-pages were followed; the article has none that are substantive beyond "Related articles".
- Confidence is `anecdotal`: single vendor-hosted case study, no independent validation, no published artifacts.
- The "deterministic decisions loosen first" point comes from the Q&A section at the end of the article.
- Cross-reference claim numbers were checked against the cited notes' `### Claim` headings.
