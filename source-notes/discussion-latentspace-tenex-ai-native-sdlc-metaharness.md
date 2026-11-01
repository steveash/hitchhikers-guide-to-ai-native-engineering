---
source_url: https://latent.space/p/tenex/
source_type: discussion
title: "AI for the Fortune 2000: How Tenex Builds an AI-Native SDLC — Alex Lieberman & CJ Hess"
author: Latent Space (swyx) interviewing Alex Lieberman and CJ Hess (Tenex)
date_published: 2026-10-21
date_extracted: 2026-11-01
last_checked: 2026-11-01
status: current
confidence_overall: anecdotal
issue: "#4475"
---

# AI for the Fortune 2000: How Tenex Builds an AI-Native SDLC

> A ~44-minute podcast interview in which a 75-person applied-AI consultancy describes its repo-resident "MetaHarness" (plans, agent decision logs, skills and a CLI checked into Git), its story-point output-based pay model, and enterprise AI adoption rates. All numbers are self-reported.

## Source Context

- **Type**: discussion (podcast with show notes and an auto-generated, unlabeled-speaker transcript; the page says the "wording may contain errors")
- **Author credibility**: Alex Lieberman is Tenex cofounder; CJ Hess is the first hire and "special projects lead" who builds the internal MetaHarness. Host is swyx / Latent Space. Practitioners with real client work, but no independent verification and a commercial interest in the model they describe.
- **Scope**: Covers pay-for-output compensation, MetaHarness mechanics (briefly, ~7:20–10:25), model preference, token spend, enterprise AI adoption milestones, vertical AI, "Kill My SaaS", AI and jobs. It does not give file layouts, schemas or CLI commands. The show notes link Tenex's own "Building an AI-native SDLC" article (not fetched here; not in the corpus and a better primary source for MetaHarness mechanics).

## Extracted Claims

### Claim 1: Plans and agent decisions are checked into Git so an agent returning to a task can recover *why* something was built, not just what
- **Evidence**: Description by the engineer who builds it (CJ); no metrics or example artifacts shown.
- **Confidence**: anecdotal
- **Quote**: "Plans and decisions are checked into Git alongside the code. When an agent comes back to a task, it can read not just what was built, but why the team chose to build it that way."
- **Our assessment**: Quote is from the Latent Space show-notes summary, not the speaker. Consistent with the commit-a-versioned-artifact pattern in the Anthropic playbook, but here it is a practitioner report rather than vendor guidance. Mechanics (format, size, retention) are unspecified.

### Claim 2: MetaHarness = standardized skills, a structured documentation set inside the repo, and a CLI the models use to drive the work (planning, visualization, client readouts)
- **Evidence**: Self-described by CJ; "most engineering orgs have done something similar by this point".
- **Confidence**: anecdotal
- **Quote**: "a very structured set of documentation within a repo and then a CLI that's around it that kind of the models are using to actually drive the work that's being done, whether it's creating a plan, a visualization, you know, creating some readout for a client"
- **Our assessment**: Useful as a concrete data point that the "meta-harness" is, at Tenex, a repo-doc-plus-CLI convention rather than an orchestrator of agents (contrast with the orchestration-style meta-harnesses in the AINews note). Terminology is overloaded.

### Claim 3: The canonical plan document's enforced structure was loosened as models improved
- **Evidence**: CJ's firsthand report.
- **Confidence**: anecdotal
- **Quote**: "as the models have gotten better, we've actually reduced the enforcements there in the structure."
- **Our assessment**: Notable counter-trend to "add more scaffolding" and supports the idea that harness structure should be re-audited per model generation. Single data point, no before/after.

### Claim 4: Agents follow an opinionated protocol to log decisions and activity; everything is committed, now increasingly as HTML rather than Markdown
- **Evidence**: CJ's description.
- **Confidence**: anecdotal
- **Quote**: "we have a very opinionated way on how agents will go and log their decisions and log what they're doing and just keep track of what they're up to. Everything checked into Git."
- **Our assessment**: The HTML "picture books" detail ("All of this is really kind of marked down for me now, more HTML") is an interesting human-review-surface choice; effect unmeasured.

### Claim 5: Code alone is not sufficient memory; decision rationale must live in a durable repo record, "never in someone's head"
- **Evidence**: Argued position, taking a side in the "do you even need docs?" debate.
- **Confidence**: anecdotal
- **Quote**: "You need to know why you made a decision. You need to know the context around the conversation that was had."
- **Our assessment**: Reasonable and aligned with file-based durable state in the Weng note; but no experiment compares agent performance with and without the decision record.

### Claim 6: The stated cost is that this much structure can be overkill for a small team on one project
- **Evidence**: Stated in the Latent Space summary, attributed to Tenex's article ("Tenex's article also notes the cost").
- **Confidence**: anecdotal
- **Quote**: "that much structure can be overkill for a small team on one project."
- **Our assessment**: Rare explicit cost/applicability caveat; useful for a "when not to" note. Second-hand (host summary of article), and the interview itself does not discuss the cost.

### Claim 7: Tenex measures process effectiveness by average story points per engineer per month, reporting roughly 2x output over the year
- **Evidence**: Internal metric, estimate given on the fly ("I don't know. What do you think?"), with acknowledged recalibration of story points at least quarterly.
- **Confidence**: anecdotal
- **Quote**: "I'd really say, overall, it's been a 2x increase, this year in particular."
- **Our assessment**: Weak: the unit is recalibrated by the same organization, so deflation/inflation is uncontrolled (speakers admit "It's a tricky equation"). Compare Orosz Claim 12 (story-level metrics as a more credible velocity signal than PR counts) — here the story points are also the pay unit, which creates a Goodhart risk.

### Claim 8: Output-based (story point) pay has a roughly 4x spread between highest- and lowest-paid engineers, and feared gaming (sandbagging, shipping junk) has not materialized
- **Evidence**: Self-reported; attributes lack of gaming to AI strategists whose incentives are retention and growth.
- **Confidence**: anecdotal
- **Quote**: "It's probably something around 4X difference."
- **Our assessment**: Triage asked us to record this as low-confidence. The anti-gaming mechanism (a counterweight role with opposed incentives) is the interesting, testable part; the firm is 75 people so generalization is doubtful.

### Claim 9: The hard part of output pay is rewarding non-coding work (architecture, client meetings, context gathering)
- **Evidence**: Both speakers; CJ says time shifts from coding to getting customer context into a form the model can use.
- **Confidence**: anecdotal
- **Quote**: "the biggest challenge has been how do you compensate engineers for all the time that's not spent coding, whether it's architecting, meeting with clients."
- **Our assessment**: Supports the point that as agents absorb coding, the scarce human input is context elicitation. No resolved comp design is offered ("we've had to find nuance").

### Claim 10: Token spend relative to employee spend — AI-native orgs ~10%, AI startups ~1x; Tenex says 1:1 to 2:1 raw tokens
- **Evidence**: Host's figure from unspecified source; Tenex's answer is an estimate ("I actually don't have a number off the top of my head").
- **Confidence**: anecdotal
- **Quote**: "The average AI startup employee is about 1x in terms of employee spend and token spend"
- **Our assessment**: Triage says to treat as unverified. Host's numbers are unsourced and internally muddy ("$10 to $200 in spend per employee"). Do not cite as a benchmark.

### Claim 11: Per-task costs have fallen, making runaway "token-maxing" harder than six to eight months ago; Opus-class model covers most economically valuable tasks
- **Evidence**: Opinion plus a model-preference anecdote (Opus 5.5 as default driver, Codex for review/computer-use).
- **Confidence**: anecdotal
- **Quote**: "it is way harder today for someone to token max and like really F the company in terms of cost than it was six to eight months ago."
- **Our assessment**: Matches the Orosz note's Claim 4 (per-dev spend peaked in summer 2026 and is falling, largely from model change), a rare independent corroboration. Also: "you have to do the weird stuff first to discover the lessons" is a defense of unconstrained early experimentation.

### Claim 12: Enterprise adoption drops sharply by milestone: ~90% rolled out a general LLM, ~60% training, ~50% coding agents, ~5% agents in production for non-engineering work (among ~100 enterprises they talk to)
- **Evidence**: Alex's estimates from Tenex's pipeline; a self-selected sample.
- **Confidence**: anecdotal
- **Quote**: "agents in production for non-engineering work drops to like 5%."
- **Our assessment**: Selection-biased but useful as an order-of-magnitude. The 50% coding-agent figure runs against attendee expectations ("70 or 80%") per the speaker.

### Claim 13: You cannot automate a process that doesn't exist — standardize the human process first, or evals and agent hand-off are impossible
- **Evidence**: CJ's consulting experience (e.g., 40 people doing the same function 40 ways).
- **Confidence**: anecdotal
- **Quote**: "you can't automate a process that does not exist."
- **Our assessment**: Plausible and relevant to team adoption; the eval link ("impossible for the agent to know whether it's doing it right ... build evals") is argued, not demonstrated.

### Claim 14: Permissioning/RBAC for per-employee agents is a major blocker for CIOs/CISOs, with no good data-permission gateway
- **Evidence**: Tenex built bespoke gateways, then productized one (vendor interest).
- **Confidence**: anecdotal
- **Quote**: "it has turned into an absolute nightmare for CIOs and CISOs."
- **Our assessment**: Corroborates the permissioning critiques in the AINews meta-harness note; the speaker sells a solution.

## Concrete Artifacts

No code, configs or file listings are in the source. The only structural description is verbatim from the transcript (CJ Hess, 7:44–8:55):

```
- shared set of skills
- structured documentation within a repo (big canonical plan document;
  structure loosened as models improved)
- CLI around it that models use to drive: plan, visualization, client readout
- agents log decisions and activity under an opinionated protocol
- everything checked into Git (Markdown, increasingly HTML)
```
(The list is our condensation of the speakers' description, not source text.)

Reported metrics (all self-reported): 75 staff, 90% engineers or AI strategists; customers ~50% Fortune 2000 / ~50% mid-market ($100–500M revenue); ~4x pay spread; ~2x story points per engineer year over year; story-point criteria reviewed "at least once a quarter".

## Cross-References

- **Corroborates**: `blog-anthropic-ai-native-sdlc-playbook.md` Claim 2 (each stage commits a version-controlled artifact the next reads) and Claim 5 (accepted plan committed as `plan.md`); `blog-lilianweng-harness-engineering-rsi.md` Claim 3 (durable state in files rather than context); `blog-pragmaticengineer-orosz-roi-of-ai-spend.md` Claim 4 (per-dev spend falling from model change).
- **Contradicts**: None filed. Tension, not a contradiction: Tenex says it *reduced* structural enforcement in the plan doc as models improved, while the Anthropic playbook recommends tightening gates and hooks; these differ in context (consultancy of strong engineers vs. enterprise controls), so no contradiction issue.
- **Extends**: `blog-latentspace-ainews-meta-harness-summer.md` — adds a second, different meaning of "meta-harness" (repo-resident documentation plus CLI, per Claim 2) alongside the agent-coordinating architectures that note describes (Claim 2 there).
- **Novel**: Output-based (story-point) engineer compensation as an operating model and its reported failure mode (non-ticket work); the explicit "overkill for small teams" caveat on repo-resident project records; enterprise adoption milestone percentages.

## Guide Impact

- **Chapter 02 (harness engineering)**: Add Tenex as a practitioner example of repo-resident decision/plan records, and the reported loosening of plan-doc structure as models improve (Claims 1, 3); flag that this is anecdotal and that the small-team overkill caveat (Claim 6) applies. Recommend following up on the primary "Building an AI-native SDLC" article before relying on specifics.
- **Chapter 04 (context engineering)**: Cite Claim 5/9 for "decision rationale as durable context" and for the shift of human effort to eliciting customer context.
- **Chapter 05 (team adoption)**: Cite Claims 8, 9, 13 as anecdotal evidence on output-based comp and process standardization before agent hand-off; do not use the 2x or 4x numbers as benchmarks.

## Extraction Notes

- Fetched the full page HTML (show notes plus complete auto-generated transcript) and read it end to end. Quotes are verbatim from the page; transcript speakers are unlabeled, so attribution within the conversation (Alex vs CJ) is inferred from context.
- Did not follow the linked Tenex article (outside the ≤5 substantive pages budget decision: not fetched in this pass); recommended as a separate issue per the Prospector.
- Skipped largely off-topic sections (New York ecosystem, hiring) and only summarized vertical AI / Kill My SaaS, which are not claims we extract for the guide.
- Source is thin on mechanics (~3 minutes of 44 on MetaHarness); confidence kept at anecdotal.
