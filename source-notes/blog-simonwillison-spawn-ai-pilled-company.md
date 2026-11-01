---
source_url: https://simonwillison.net/2026/Oct/29/how-i-built-the-most-ai-pilled-company-in-the-world/
source_type: blog-post
title: "How I Built the Most AI-Pilled Company in the World (Willison link post on Jacob Sansbury's Spawn account)"
author: Simon Willison (quoting Jacob Sansbury)
date_published: 2026-10-29
date_extracted: 2026-11-01
last_checked: 2026-11-01
status: current
confidence_overall: anecdotal
issue: "#4468"
---

# How I Built the Most AI-Pilled Company in the World (Spawn)

> A single-company self-report of agents shipping to production hourly, treating an hour without a ship as a SEV-0, rolling back in 30 seconds, and owning incidents. It also includes a failure anecdote in which a security-review pass disabled features instead of fixing them.

## Source Context

- **Type**: blog-post (Willison link post quoting a first-party operator account; the primary is an X thread by Jacob Sansbury, https://twitter.com/jsnnsa/status/2115623382721126826)
- **Author credibility**: Willison is a widely read LLM-tooling commentator who tried the product himself. Sansbury is the founder/operator of Spawn (https://spawn.co) and reports on his own company, so he has a stake in the story.
- **Scope**: Spawn is a massively multiplayer game environment where players use prompts to modify the world via an agent called Savi. The post covers the ship cadence, bug intake, incident handling, rollback, the model-tier claims, and the Astra security-pass anecdote. It publishes no metrics and no independent verification.
- **Access caveat**: Only the Willison page was fetched, through a summarizing fetch tool. Quotes below are the fragments that tool returned as blockquotes. The primary X thread was not fetched. The $3M/month figure and the Opus 5.5 remark are summarized, not verbatim. The "30x payroll" figure from the triage comment was not confirmed in the fetched text.

## Extracted Claims

### Claim 1: Agents change live code and ship to production hourly
- **Evidence**: Operator self-report. No metrics.
- **Confidence**: anecdotal
- **Quote**: "Our agents change the live code directly and ship to production hourly"
- **Our assessment**: A strong claim of continuous deployment with no human gate. Willison calls it "continuous deployment turned up to 11" and doubts it would work on higher-stakes software. Treat it as an existence proof in a low-stakes domain (a game), not a general recommendation.

### Claim 2: An hour without a ship is treated as a SEV-0
- **Evidence**: Stated policy. No incident data.
- **Confidence**: anecdotal
- **Quote**: "we treat an hour without a ship as a SEV-0, our most severe kind of incident."
- **Our assessment**: Novel framing: the absence of change is the incident. The stated rationale is that unshipped changes accumulate risk and slow feedback (see Claim 3). It is a cadence-as-safety argument and should be read alongside the rollback claim, since the two depend on each other.

### Claim 3: Short ship cycles help agent coherence because agents hold only a few hours of work in context
- **Evidence**: Author's reasoning. No experiment.
- **Confidence**: anecdotal
- **Quote**: "An agent can only keep a few hours of work in its head, so shipping faster than that actually helps it stay coherent."
- **Our assessment**: Plausible and consistent with context-limit experience, but untested here. Related: "Unshipped changes pile up, and every problem already in production lasts longer."

### Claim 4: Rollback of a broken change takes about 30 seconds, scoped to the broken change only
- **Evidence**: Stated capability. No demonstration.
- **Confidence**: anecdotal
- **Quote**: "We can roll back a broken change in 30 seconds, exactly where it's broken and nowhere else."
- **Our assessment**: This is what makes the hourly cadence defensible. Per-change scoped rollback implies feature-level isolation. Compare the roll-forward/feature-toggle debate in the Erez CI/CD note.

### Claim 5: Monitors and log alerts start or wake an agent that owns the incident
- **Evidence**: Stated design. The triage comment also says they deliberately break things to test recovery paths, but that sentence was not captured in the verbatim fragments I retrieved.
- **Confidence**: anecdotal
- **Quote**: "When a monitor or a log alert fires, it starts or wakes an agent that owns the incident"
- **Our assessment**: Agent-as-incident-owner. No detail on escalation to humans, so the human fallback is unknown. The deliberate-fault-injection claim is unverified in my extraction.

### Claim 6: Production errors and user bug reports are the main work source, filed by the product agent herself
- **Evidence**: Self-report. The figure is about 60% of work.
- **Confidence**: anecdotal
- **Quote**: "About 60% of our work starts from a production error, a Savi bug report"
- **Our assessment**: Closed-loop bug intake: "Savi files bugs herself." and "Usually it becomes a change, delivered to that user within an hour, with a message in the same chat." The 60% number is unverified. Feedback-to-fix latency is the real claim.

### Claim 7: A tight loop only works if it never stops
- **Evidence**: Author's argument, motivating Claim 2.
- **Confidence**: anecdotal
- **Quote**: "A loop this tight only works if it never stops"
- **Our assessment**: Reasonable as a motivation for the SEV-0 policy. It also reveals the fragility: the system depends on continuous operation.

### Claim 8: Fable 5 / 5.1 enabled this autonomy; Opus 5.5 did not quite manage it
- **Evidence**: Team self-report. No controlled comparison.
- **Confidence**: anecdotal
- **Quote**: "Jacob says that Fable 5 (and then 5.1) was the model that made this level of autonomy possible."
- **Our assessment**: This is Willison's paraphrase of Sansbury. The Opus 5.5 "doesn't quite hack it" remark is only summarized in what I fetched. Do not generalize without independent evidence.

### Claim 9: GPT-6 Astra's security pass made things "secure" by disabling features (failure report)
- **What was attempted**: Running GPT-6 Astra over the whole product as a security-review/fix pass.
- **What went wrong**: Features were switched off wholesale. The product effectively stopped until they were re-enabled.
- **Root cause (author's)**: The model fixed insecurity by removing function. The remediation scope and success criteria were not constrained to preserve functionality.
- **Recovery**: Features were re-enabled after the fixes. Recovery details are not captured here.
- **Evidence**: Single anecdote.
- **Confidence**: anecdotal
- **Quote**: "Astra had gone through our whole product and made the insecure things secure by turning them off."
- **Also**: "Every feature had been disabled and marked to be turned on again once the security fixes were done."
- **Our assessment**: A real failure mode (fix by disabling) that a specification asking for "no remaining vulnerabilities" invites. This is most likely a scope or specification gap, not a model verdict. It would be caught by a functional regression gate on security PRs.

### Claim 10: Token spend is over $3M/month
- **Evidence**: Author's figure, unverified. Summarized from the post, not quoted.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The fetched summary says a swarm of Fable-powered agents develops Spawn autonomously at over $3 million in tokens per month. The "30x payroll" comparison from the triage comment was not confirmed. Treat both as marketing-adjacent and unverified.

### Claim 11: The approach is unlikely to transfer to higher-stakes software (Willison's view)
- **Evidence**: Willison's opinion.
- **Confidence**: anecdotal
- **Quote**: "I have trouble imagining this style of development working on software with higher stakes"
- **Our assessment**: The most useful caveat in the post. Willison adds "These kinds of extreme experiments are why I'm excited about game development".

## Concrete Artifacts

```
Operating loop as described (Sansbury, quoted by Willison):
  production error / user or Savi bug report
    -> Savi files bug
    -> agent triages: real bug?
    -> change shipped to production (hourly cadence)
    -> message to user in same chat
  monitor / log alert -> starts or wakes an agent that owns the incident
  broken change -> rollback in 30 seconds, scoped to the change
  policy: an hour without a ship = SEV-0
```

## Cross-References

- **Corroborates**: None directly. `blog-simonwillison-vibe-game-development.md` (Claims 1, 10) shares the game-development-as-low-stakes-testbed framing but is a different claim set.
- **Contradicts**: None filed. The nearest tension is with `blog-pragmaticengineer-erez-cicd.md` Claim 3 (continuous deployment is often overkill versus delivery) and Claim 1 (roll forward rather than back). Those differ in context: stateful systems versus a game with scoped rollback. This is a conditioning variable, not a contradiction. `blog-latentspace-ainews-reality-checks-gas-town-astra-cost.md` Claim 7 (removing human code review is risky) and Claim 8 (software factories need heavy guardrails and observability) also differ in stakes and context.
- **Extends**: `blog-simonwillison-claude-fable-5.md` (capability context for Fable 5). `blog-simonwillison-gpt6-astra-launch.md` (Astra background; the security gains it reports contrast with this anecdote). `blog-latentspace-ainews-reality-checks-gas-town-astra-cost.md` Claim 3 (spend can rise with a more capable model).
- **Novel**: The hourly-ship SEV-0 policy, the context-coherence rationale for short cycles, agent-owned incident response, and the "fix security by disabling features" failure.

## Guide Impact

- **Chapter 03 (verification)**: Add the Astra "secure by disabling" anecdote as a failure mode for security-remediation agents, with a mitigation: a functional-regression gate and scoped instructions that forbid removing features. Mark it as single-source anecdote.
- **Chapter 01 / Ch00 (workflows, autonomy)**: Cite the hourly-ship and SEV-0 framing as an extreme end-of-spectrum data point, with Willison's own stakes caveat. Do not present it as a recommendation.
- **Chapter 03**: Note scoped 30-second rollback as the enabling mechanism for high-cadence agent shipping, contrasted with the roll-forward advice in the Erez note.
- **Chapter 05 (economics)**: At most a footnote on the unverified $3M/month figure.

## Extraction Notes

- Only the Willison page was fetched, via a summarizing tool, so quotes are the blockquote fragments it returned, each under about 125 characters. Please spot-check against the page.
- The primary X thread was not reachable, so claims that appear only in Sansbury's thread (deliberate breakage tests, "30x payroll", the exact Opus 5.5 wording) are not verified.
- The issue title ("Building a multiplayer game world with autonomous Fable-class models") does not match the post headline; the URL is the source of truth.
- No contradiction issue was filed, since the differences found are contextual.
