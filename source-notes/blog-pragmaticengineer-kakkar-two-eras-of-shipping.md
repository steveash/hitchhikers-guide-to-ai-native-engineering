---
source_url: https://newsletter.pragmaticengineer.com/p/how-software-engineering-is-changing
source_type: blog-post
title: "How software engineering is changing: a tale of two eras"
author: Neil Kakkar (reader essay; published in The Pragmatic Engineer, introduced and annotated by Gergely Orosz)
date_published: 2026-11-03
date_extracted: 2026-11-04
last_checked: 2026-11-04
status: current
confidence_overall: anecdotal
issue: "#4516"
---

# How software engineering is changing: a tale of two eras

> A first-person, data-backed account from one engineer at a ~10-person AI-native startup who runs with no human PR review (a CI review agent is the only reviewer, fixes go forward not back), reporting ~11x PR throughput versus his pre-AI baseline, two concrete incidents a human reviewer might have caught, and the personal and team costs (thrashing, lost shared context, fatigue).

## Source Context

- **Type**: blog-post (winning entry in The Pragmatic Engineer's 5th-anniversary reader essay challenge; 125 submissions, $10,000 prize)
- **Author credibility**: Neil Kakkar, London-based, nine years' experience (Bloomberg ~3 yrs, PostHog ~4 yrs, now founding engineer at Tano, an influencer-marketing agency building AI agents). Uses his own PR history across all three jobs. Orosz adds a framing intro and "Takeaways" section.
- **Scope**: One engineer, one company (~10 people, "I was the first engineer"), measured against his own earlier PostHog work (May 2021–Jan 2025, pre-AI). Not a controlled comparison. The author himself says "PRs can be an easily gamed metric". Covers workflow, review, migrations, costs, culture. Does not report defect/incident rates beyond the revert ratio and two anecdotes, nor revenue or product outcomes (Orosz notes that "iteration speed is pretty meaningless by itself").

## Extracted Claims

### Claim 1: The author ships ~11x more merged PRs per month at an AI-native startup than at his pre-AI PostHog baseline (8–20/month before, 200+/month now), but he attributes the multiplier to AI plus removed organisational constraints, not AI alone
- **Evidence**: Author's own merged-PR history (charts of monthly and cumulative PRs at Bloomberg, PostHog, Tano). Self-reported; PRs conceded to be gameable; PostHog treated as "pre-AI baseline" rather than controlled comparison. He estimates a time-traveller with AI inside pre-AI PostHog would get only "1-2x".
- **Confidence**: anecdotal
- **Quote**: "I’m shipping 11x more PRs at Tano than at PostHog, where I shipped 2.4x as many as I did at Bloomberg."
- **Our assessment**: Useful as a data point on the *upper range* of individual throughput, but n=1, different company, different product scope (he also notes work that "used to take a month now often takes a week"). The key analytical contribution is his decomposition: the gain comes from AI *and* dropping review/communication bottlenecks. Do not quote "11x" as an AI productivity effect.

### Claim 2: Code review is optional at the company once the engineer has onboarded; the only review on most PRs is an automated Claude Code GitHub Actions agent running in CI, with a deeper on-demand agent for risky changes
- **Evidence**: Description of the author's own team's practice. Onboarding time-to-confidence reported as 3 weeks for him, up to 8 weeks depending on experience, defined by "how quickly human PR review comments go down to zero".
- **Confidence**: anecdotal
- **Quote**: "In most cases, this automated reviewer is the only review on PRs. There are no human PR reviews."
- **Our assessment**: Concrete, rare example of fully removing human PR review (compare tiered models in code-review-approaches). Important conditioning variables: tiny team, single-owner areas, founding-engineer trust, a deliberate risk appetite, and a "deeper" on-demand agent for risky PRs, which is effectively a lightweight risk tier. Human review is still used for newcomers ("we review our own code and new team members’, but seldom for experienced colleagues").

### Claim 3: The team accepts forward-fixing over revert and human review as an explicit trade-off, with a reported 6x lower revert rate than the pre-AI baseline
- **Evidence**: Author's PR statistics (PostHog May 2021–Jan 2025 vs. Tano Jan–Sep 2026); median time to merge is under an hour. Author gives two causes for the lower revert rate: forward-fixing instead of reverting, plus better models/automated review.
- **Confidence**: anecdotal
- **Quote**: "The revert rate is 6x lower at Tano because we fix things forward most of the time, rather than revert."
- **Our assessment**: Caution: a lower *revert* rate is not a lower *defect* rate; by the author's own explanation it is partly an artefact of the policy (fixing forward means fewer reverts by construction). Should not be cited as evidence of higher quality. Median merge time under an hour echoes the Duckbill figure (1 hr for no-human-review PRs, code-review-approaches Claim 8).

### Claim 4: Incident 1 — an agent-written currency conversion assumed 100 minor units per currency, ignored an existing currency utility, and shipped without a human reviewer who would have caught it
- **Evidence**: Specific incident; detected after deployment when reporting numbers didn't match; fixed within the hour.
- **Confidence**: anecdotal
- **Quote**: "It’s a dumb mistake to assume every currency has 100 minor units. For example, the minor unit of the Bahraini dinar is the fulūs, and one dinar is 1,000 fulūs."
- **Our assessment**: Good illustration of a class of failure (agent ignores an in-repo utility, domain-knowledge edge case) the review agent did not catch. The author concedes: "a human reviewer would have caught the generated code not using it." Detection came from a business-level signal (reports mismatching), not from tests or review.

### Claim 5: Incident 2 — a blocking Postgres index migration on a ~25 GB / 6M-row table stalled ingestion and failed deploys; the fix was a concurrent-migration rule plus encoding a list of the largest tables in the review agent's prompt
- **Evidence**: Specific incident with sizes; the remediation (rule + table list in review prompt, screenshot "Migration safety guards in code review prompt").
- **Confidence**: anecdotal
- **Quote**: "We make sure to add any new way that things can break to the review agent. Now, it has a list of the largest tables and doesn’t allow blocking migrations on them."
- **Our assessment**: The strongest transferable pattern in the essay: every production incident becomes a standing guard in the review agent's prompt (incident → guardrail feedback loop). Fits harness-engineering ideas (encode learned constraints), though unlike a deterministic check (e.g., a migration linter) a prompt rule is probabilistic. Not clear from the source whether the guard has since been tested.

### Claim 6: Incident 3 — a fast agent-architecture migration missed guardrails and caused creators to be paid twice for the same work; the author judged speed worth the cost
- **Evidence**: Single anecdote; two architecture migrations completed in "weeks" rather than a year (compare PostHog person-on-events migration).
- **Confidence**: anecdotal
- **Quote**: "Duplicate payments are not great, but moving fast and breaking things was a trade-off we were very willing to make because getting the new architecture in place meant we could scale faster."
- **Our assessment**: Financial-side-effect bug accepted deliberately; a risk appetite that many teams (especially with money movement) would not share. Useful as a counterweight to the speed narrative: the failure is exactly the class that blast-radius tiering (code-review-approaches Claim 6, Claim 9) would route to human review. The author later wishes for an agent that could detect such double payments from conversation logs.

### Claim 7: Removing review and cross-engineer communication overhead is as important as AI itself; mandatory review is the bottleneck that caps AI gains in a pre-AI process
- **Evidence**: Thought experiment (time-traveller with AI at pre-AI PostHog gets "1-2x" because the review queue grows) plus the author's observation that one-owner end-to-end work replaced a 2 engineers + 1 designer team on "surveys".
- **Confidence**: emerging
- **Quote**: "Your productivity gains are limited if the rest of the company is not onboard with AI."
- **Our assessment**: Consistent with the verification-bottleneck thesis in the guide (it *is* the bottleneck) but draws the opposite conclusion about response: relax review rather than scale it. The 1–2x figure is speculation, not measurement.

### Claim 8: Without human review, shared context erodes and bus factor worsens; the proposed mitigation is writing context into AGENTS.md files per product area
- **Evidence**: Author's experience: he reads far fewer PRs than at PostHog (reviewed/merged ratio "nearly zero"), PR volume ~30/day at Tano with engineers at roughly a third of that; first-hand description of silos.
- **Confidence**: anecdotal
- **Quote**: "I think AI provides the solution: if I’m good at writing down context in AGENTS.md files in my product areas, anyone can hit the ground running, learn with AI, and contribute."
- **Our assessment**: Identifies a real hidden benefit of human review (shared awareness) that the guide's Ch05 should list. The AGENTS.md remedy is asserted, not shown to work yet.

### Claim 9: Agent speed induces reactive "thrashing" and parallel-work fatigue; pacing and hard stop times are needed
- **Evidence**: Author runs 3–5 workstreams at once; agent runs take 1–2 hours; charts of project overlap per month; first-person experience of exhaustion and mistakes when drained.
- **Confidence**: anecdotal
- **Quote**: "The fix is to limit concurrency and get the highest priority tasks done first."
- **Our assessment**: Believable and consistent with Orosz’s referenced "Dracula effect" discussion. His guardrails (leave the laptop at work so agents run overnight locally, fixed 6pm end) are practical. Note the quote is the author's definition-based remedy, not an empirical finding.

### Claim 10: Per-engineer token budget is a flat-rate Claude Max 20x plan; API-equivalent cost would be $8,000+/month, and limits are hit when running autonomous loops
- **Evidence**: Author's own estimate.
- **Confidence**: anecdotal
- **Quote**: "If we were paying API rates, my usage would come to $8,000+ per month."
- **Our assessment**: Helpful cost datapoint for a very high-output individual; corroborates flat-rate-subscription subsidy concerns in roi-of-ai-spend (Claim 6). Self-estimated.

### Claim 11: Orosz’s framing: industry-wide PR output has roughly doubled since January, and the AI-native advantage over "pre-AI" startups may be temporary and not cost-free for businesses that already work
- **Evidence**: Orosz commentary referencing his own PR-frequency deepdive.
- **Confidence**: emerging
- **Quote**: "Of course, we know that iteration speed is pretty meaningless by itself, without looking at things like finding product-market-fit, generating revenue, or having healthy unit economics."
- **Our assessment**: A needed caveat from the publisher, supports treating the essay as an experience report.

### Claim 12: Organisations that remove one bottleneck find the next one (review → CI → source control); the author cites Anthropic redesigning source control
- **Evidence**: Second-hand assertion; no citation given in the essay.
- **Confidence**: anecdotal
- **Quote**: "Anthropic also automated code reviews away, but then ended up constrained by continuous integration (CI) pipelines."
- **Our assessment**: Unsupported in the essay itself; treat as hearsay. Compare to what our notes say Anthropic actually does (human merge still, risk tiering: code-review-approaches Claim 7), which does not support "automated code reviews away" literally.

## Concrete Artifacts

```
Source: Kakkar essay, sections "Code reviews" and "Move fast and break things"

Workflow (as described):
- Claude Code (Desktop) agents, 3-5 parallel workstreams; agent runs 1-2 h
- Agent runs plan -> implementation -> PR -> addresses review comments
- Claude is instructed to generate an HTML summary artifact with every PR
- Code review agent via Claude Code GitHub Actions on every PR (CI)
- Deeper on-demand review agent for risky changes
- Review-agent prompt includes: list of largest tables; no blocking migrations on them
- Postgres migrations on large tables must be concurrent

Metrics (self-reported):
- Merged PRs/month: ~8-20 (PostHog) vs 200+ (Tano); "11x"; PostHog 2.4x Bloomberg
- Revert rate 6x lower at Tano; median time to merge < 1 hour
- ~30 PRs/day at Tano (author and one peer); newer engineers + CTO ~1/3
- Share of PRs opened 9-11 AM: 18% (Tano) vs 9% (PostHog)
- Time-to-confidence for review-optional: 3 weeks (author) up to 8 weeks
- Incident table: 25 GB / 6M rows posts table; fixed currency bug within the hour
- Cost: one 20x Claude Max plan per person; ~$8,000+/month at API rates
```

## Cross-References

- **Corroborates:**
  - `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 8 (Duckbill: PRs with no human review merged in a median 1 hour vs. 26 hours), Claim 11 (Sigil CEO: only the database schema merits careful review; Kakkar's blocking-migration incident is exactly a schema-class failure), and Claim 2 (AI reviews the PR, human reviews the review).
  - `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 7 (Cursor data: sharp rise in changes accepted with no human review) and Claim 11 (OpenAI Codex team keeps background agents running, laptop lids propped open; Kakkar leaves his laptop at work so agents run overnight).
  - `blog-pragmaticengineer-orosz-roi-of-ai-spend.md` Claim 6 (flat-rate subscriptions hide true cost).
- **Contradicts:** No contradiction issue filed. The guide's Ch03 line "Human review is the safety system, and it is always the bottleneck" (citing `blog-addyosmani-code-agent-orchestra.md` Claim 5, "The bottleneck has shifted from code generation to verification") is not directly refuted: Kakkar agrees verification is the bottleneck and responds by removing human review for experienced engineers, at an explicitly accepted cost in incidents. That is a difference of risk appetite and context (10-person startup, no regulated domain, forward-fix culture), i.e. a conditioning variable per MINER §4a, not an opposed factual claim. The Assayer/Smith should treat "always" wording in Ch03 as needing this qualification. It also partially tensions with `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 6 (Anthropic, OpenAI, Duckbill keep mandatory human review for high-risk changes), whereas Kakkar's team does not tier by risk beyond an on-demand deeper agent.
- **Extends:** `blog-pragmaticengineer-orosz-code-review-approaches.md` Claims 8–9 with an individual-level, longer-running example and named failure incidents; `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 9 (Cherny runs ~5 parallel agents) with the cost side of parallel agent work.
- **Novel:** (a) A named, dated, quantified example of fully removing human PR review at a startup, with the 3–8 week onboarding gate; (b) the incident → review-agent-prompt guardrail feedback loop (largest-tables list); (c) the reviewed/merged ratio as a metric (near zero); (d) first-person fatigue/thrashing data and "leave the laptop at work" overnight-agent habit; (e) loss of shared context from not reading PRs as a named cost of removing review.

## Guide Impact

- **Chapter 03 (Verification)**: Layer 4 / "Verification-as-Bottleneck": qualify "always the bottleneck" and "human review is the safety system" with a counter-case: one small startup removes human review for onboarded engineers, using a CI review agent plus forward-fix, and reports 3 incidents (currency units, blocking migration, duplicate payments). Present as [anecdotal], with conditions (small team, accepted risk, no regulated domain). Add the incident→review-prompt guardrail loop as a harness pattern, and warn that fewer reverts is not evidence of fewer defects.
- **Chapter 05 (Team Adoption)**: "Code Review When AI Wrote It": add loss of shared context / bus factor as a cost of dropping human review, with AGENTS.md per product area as the proposed (unproven) mitigation; add the 3–8 week onboarding gate as a possible rule for when review becomes optional.
- **Chapter 01 (Daily Workflows)**: add parallelism limits (3–5 streams), thrashing, hard end-of-day, and overnight local agent runs as pacing guidance.
- **Chapter 02 (Harness)**: example of prompt-based migration guards in a CI review agent; recommend pairing with a deterministic migration linter (our suggestion; not in the source).

## Extraction Notes

- Read the full essay text (fetched HTML, ~35k characters). Charts are interactive/image-only; figures cited are from text and chart captions only. Did not read the linked interactive charts or the Orosz "PR frequency and AI cost" deepdive (see `blog-pragmaticengineer-orosz-roi-of-ai-spend.md` for that).
- Quotes are verbatim from the page text (curly apostrophes preserved).
- Claim 11 attributes to Orosz (the publisher), not Kakkar. The "twofold increase" figure comes from the Takeaways section; I did not quote it directly.
- Confidence set to `anecdotal` overall: single engineer, single company, self-reported, no controlled comparison.
