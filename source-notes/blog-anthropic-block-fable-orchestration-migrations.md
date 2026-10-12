---
source_url: https://claude.com/resources/articles/how-block-orchestrates-claude-fable-across-thousands-of-pull-requests
source_type: blog-post
title: "How Block orchestrates Claude Fable across thousands of pull requests"
author: Anthropic (interview with Bradley Axen, Head of AI Capabilities at Block)
date_published: 2026-10-08
date_extracted: 2026-10-12
last_checked: 2026-10-12
status: current
confidence_overall: anecdotal
issue: "#4067"
---

# How Block orchestrates Claude Fable across thousands of pull requests

> A vendor-hosted customer interview describing Block's frontier-orchestrator / cheap-worker pattern for thousand-PR migrations, a model-by-effort benchmarking grid, and a dual-human-approval deploy gate. Scale is stated concretely, but no cost, quality or defect figures are given.

## Source Context

- **Type**: blog-post (Anthropic-published Q&A, "Perspectives" category, Claude Enterprise; 11 min read)
- **Author credibility**: Bradley Axen leads AI capabilities at Block (Square, Cash App) and a team building Buzz, an open-source human-agent workspace. First-hand operator, but the piece is published by Anthropic about Anthropic's own model, so favourable framing is expected.
- **Scope**: Covers migration orchestration, model selection and effort levels, tech-debt sweeps, and safeguards. It does not give cost numbers, defect rates, human-hours per migration, or the orchestration prompts or tooling details.

## Extracted Claims

### Claim 1: A frontier model (Fable) orchestrates large migrations, doing high-level design and directing up to dozens of cheaper workers
- **Evidence**: Interviewee's description of Block's practice; no metrics or transcripts.
- **Confidence**: anecdotal
- **Quote**: "A human engineer steers, and Fable focuses on the higher-level design work: data models, API specs, algorithms. It then directs up to dozens of smaller, more cost-effective models like Opus or Sonnet to do the individual tasks, such as making the actual file edits and running tests."
- **Our assessment**: Matches the planner/worker split seen elsewhere in the corpus, now with a named enterprise user. The division of labour (design vs. mechanical edits and tests) is specific and useful; the absence of any detail on how work is decomposed or handed off limits how actionable it is.

### Claim 2: Orchestration is claimed to shift token share to smaller models without a quality drop, but this is explicitly "early results" and unquantified
- **Evidence**: Self-reported; no figures for token split, cost, or quality.
- **Confidence**: anecdotal
- **Quote**: "Early results show the orchestrator using frontier tokens for complex, upfront planning before driving a higher percentage of tokens to smaller worker models, without a drop in quality."
- **Our assessment**: Directionally plausible, and consistent with measured data in the Cursor swarm note, but here it's an assertion. Don't cite as evidence of equal quality; cite as a practitioner claim.

### Claim 3: Scale: migrations of hundreds or thousands of PRs across repos, with about a thousand Fable-orchestrated PRs merged in a single migration
- **Evidence**: Self-reported counts.
- **Confidence**: anecdotal
- **Quote**: "In any given migration, we might merge a thousand pull requests orchestrated by Fable."
- **Our assessment**: Concrete scale claim, but "might" is hedged and says nothing about review burden, revert rate, or how many PRs were rejected. Human involvement per migration is not reported.

### Claim 4: Before Fable, orchestration of this kind rarely worked; the change is attributed to the model generation
- **Evidence**: Interviewee's retrospective.
- **Confidence**: anecdotal
- **Quote**: "Before Claude Fable 5, you had to have a particularly well-shaped problem for frontier models to really shine."
- **Our assessment**: Useful as a "model capability gates the harness pattern" datapoint, but it is a vendor-hosted claim about the vendor's model.

### Claim 5: Model choice is no longer "always use the most frontier model"; orchestration puts the frontier model on big problems and smaller models on details
- **Evidence**: Interviewee's experience since LLM coding began.
- **Confidence**: emerging
- **Quote**: "It's literally the first time I can remember since we started using LLMs for code where the answer wasn't just \"use the most frontier model 100% of the time.\""
- **Our assessment**: Notable framing from a practitioner with long history. Consistent with the Anthropic migration playbook's advice against using the largest model for every step.

### Claim 6: Effort level should be treated as a grid dimension (model × effort), benchmarked per use case, not as a spectrum
- **Evidence**: Stated internal practice; no benchmark data shown.
- **Confidence**: anecdotal
- **Quote**: "Every single use case we benchmark, we check not just every model but every effort level of every model."
- **Our assessment**: The most checkable and transferable claim. A related quote: "Fable on low might just be better than another model on xhigh." Without data it is a hypothesis to test locally, not a rule. Block also wants the output to be simple defaults ("Use this model on high as the default for this kind of task") with experts free to explore.

### Claim 7: Block gives broad frontier access but builds an auto-selector to steer employees to appropriately sized models
- **Evidence**: Stated in-progress internal tooling; no description of mechanism or results.
- **Confidence**: anecdotal
- **Quote**: "Using Fable to fix a typo in a README is a very bad use of resources."
- **Our assessment**: Policy pattern: open access plus guidance rather than gating. The latentspace note records a practitioner objection that pre-classifier routing can be unreliable, so the auto-selector's effectiveness is an open question.

### Claim 8: Agents do daily or weekly whole-codebase tech-debt passes
- **Evidence**: Stated practice for a roughly million-line codebase; no results.
- **Confidence**: anecdotal
- **Quote**: "We have agents that do daily or weekly passes across a whole codebase asking, \"How's it going in here? What do we need to clean up and consolidate?\""
- **Our assessment**: Motivation (more PRs means faster debt accumulation) is a sound argument; effectiveness is unreported.

### Claim 9: Merges to main and production deploys stay human-controlled; agent changes pass security checks, then two humans approve the deploy
- **Evidence**: Described as Block policy.
- **Confidence**: anecdotal
- **Quote**: "Agents can make code changes, but those changes have to pass our security checks, and then two humans have to approve the deploy."
- **Our assessment**: A clear, adoptable control pattern. Note the gate is on deploy (and merges to main, feature flags), not on PR creation, which Block intentionally lets the model do.

### Claim 10: Many guardrails run outside the model loop as cheap deterministic checks, secure-by-default environments, and small classifiers
- **Evidence**: Stated design principles (network allow list, remote workstations, regexes).
- **Confidence**: emerging
- **Quote**: "A lot of our security guardrails are really cheap, efficient checks that run without the model needing to be involved."
- **Our assessment**: Strong, uncontroversial principle: enforcement in code not prompts. Also: "a network allow list instead of a deny list".

### Claim 11: Claude reportedly refuses to bypass the dual-approval system when asked, and Block benchmarks this
- **Evidence**: "In our testing"; no methodology or results published.
- **Confidence**: anecdotal
- **Quote**: "In our testing, even if someone asks Claude to \"hack around\" our dual-approval system, it refuses to try to bypass it."
- **Our assessment**: Self-reported by a vendor customer in a vendor publication. Block's own framing positions model refusal as a secondary layer behind the dual-approval control that makes pushing changes "impossible"; treat the refusal as defence in depth, not a control.

### Claim 12: Organizational maturity means capturing individual learnings (skills, context) into shared system-level knowledge
- **Evidence**: Interviewee's advice; example of personal local skills enabling non-front-end work.
- **Confidence**: anecdotal
- **Quote**: "Organizational maturity comes when all of this context and organizational knowledge is remembered at a system level, not an individual level."
- **Our assessment**: Common theme; light on mechanism.

### Claim 13: Tooling must keep up with many concurrent agents; single-conversation interfaces don't scale
- **Evidence**: Motivation for Buzz (Block's open-source workspace).
- **Confidence**: anecdotal
- **Quote**: "Some tools are very single-conversation focused, and the interface doesn't keep up with you having 45 agents working with you all the time."
- **Our assessment**: Authors have a product interest (Buzz). The observability need is real.

## Concrete Artifacts

No code or configs in the source. Summary of the described operating model (paraphrased by Miner from the Q&A, not a quotation):

```
Migration orchestration (Block, per Axen interview)
  Human engineer: steers
  Fable (orchestrator): data models, API specs, algorithms, upfront planning
  Opus / Sonnet workers (up to dozens): file edits, test runs
  Runs on: Buzz (open-source shared channels/threads for humans + agents)
  Gate: security checks -> two human approvals -> merge to main / prod deploy
```

Stated numbers: "hundreds or thousands of individual pull requests across multiple repos and millions of lines of code" per migration; "45 agents" as a working-with-you example; a ~1M-line codebase for tech-debt sweeps.

## Cross-References

- **Corroborates**: `blog-cursor-agent-swarm-model-economics.md` Claim 1 (planner/worker tiering) and Claims 15-16 (token share on workers; planner costs more per token), which supply measured data this article lacks. `blog-anthropic-code-migration-playbook.md` Claim 11 (don't use the largest model for every step) and Claim 2/3 (large migrations at scale). `blog-latentspace-ainews-fable-relaunch-orchestration.md` Claim 3 (practitioner uses Fable only for planning and delegates implementation) and Claim 4 (model-combination strategies).
- **Contradicts**: None found. Claim 7 sits in mild tension with the router-skepticism in `blog-latentspace-ainews-fable-relaunch-orchestration.md` Claim 4, but Block gives no evidence either way, so this is not filed as a contradiction.
- **Extends**: `blog-anthropic-balyasny-fable5-governance.md` Claim 8 (a more capable model doesn't get broader authority) with a concrete deploy-gate design (two-human approval). `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7 (orchestrator-subagent as default) with an enterprise instance. `blog-fowler-garg-orchestrator-tax.md` relates as a cost counterweight: Block reports no orchestration overhead figures.
- **Novel**: The model × effort benchmarking grid stance; dual-human approval on deploys as an explicit control for agent-authored changes; auto-selector for model choice among employees; recurring agent tech-debt sweeps; claim that the model refuses to circumvent the approval layer (benchmarked internally).

## Guide Impact

- **Model selection / effort chapter (Ch01 per triage; verify numbering)**: Add the "grid" recommendation (benchmark model × effort per use case, publish a default per task type) as a practitioner stance, attributed to Block and flagged as unquantified.
- **Multi-agent / orchestration chapter (Ch02 per triage; verify numbering)**: Add Block as a named at-scale instance of the planner/worker pattern for migrations; pair with the Cursor swarm data for measured economics rather than relying on Block's "without a drop in quality" claim.
- **Safeguards chapter (Ch06 per triage; verify numbering)**: Add the "agents open PRs; humans approve merges/deploys; checks run outside the model loop" pattern, and note that refusal behaviour is defence in depth, not a control. Compare with the BAM governance note.
- **Team adoption chapter (Ch05 per triage)**: Optional mention of broad frontier access plus an auto-selector as an org cost-management pattern.

## Extraction Notes

- Fetched the full page HTML and read the entire Q&A (all questions). No sub-pages followed; related-article links are unrelated product stories.
- All quotes were copied verbatim from the page text; escaped quote marks inside quotes correspond to the source's inner double quotes.
- Evidence quality is low-to-medium: customer interview hosted by the model vendor, no measurements. Confidence is `anecdotal` overall.
- Cross-reference claim numbers were verified against the headings of the cited notes. No contradiction issue filed.
