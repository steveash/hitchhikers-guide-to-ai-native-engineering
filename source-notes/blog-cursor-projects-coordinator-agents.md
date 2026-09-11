---
source_url: https://cursor.com/blog/projects
source_type: blog-post
title: "Introducing Projects"
author: Alexi Robbins & Fredrika Lindh (Cursor)
date_published: 2026-09-10
date_extracted: 2026-09-11
last_checked: 2026-09-11
status: current
confidence_overall: emerging
issue: "#3378"
---

# Introducing Projects (Cursor)

> Cursor's product launch of "Projects" — a persistent, chat-directed coordinator agent that delegates to thousands of subagents across cloud and local machines, accumulates a synced shared-context store over the life of a body of work, and can be subscribed to Slack channels, PR streams, or schedules to act without being prompted — framed explicitly as the concrete product implementation of Cursor's February 2026 "third era" vision, backed by internal metrics (new users merge 30% more PRs; primary users merge 6x as many).

## Source Context

- **Type**: blog-post (Cursor official blog, "product" category, ~5 min read, published September 10, 2026, byline Alexi Robbins & Fredrika Lindh)
- **Author credibility**: Named Cursor employees writing on Cursor's own official blog about Cursor's own product launch. This is first-party vendor product-announcement disclosure — the same pattern as `blog-cursor-third-era.md` (CEO strategic framing) and `blog-cursor-cloud-agent-lessons.md` (engineering retrospective), but this piece sits closer to the third-era post on the marketing-to-engineering spectrum: it is a feature launch with a headline productivity metric, not an engineering deep-dive. No implementation detail (model routing, VM orchestration internals, shared-context storage format) is disclosed. Treat the productivity metric as first-party and unaudited; treat the architectural/capability descriptions as vendor product description.
- **Scope**: Covers what Projects is, three "core capabilities" (cloud-by-default/local-when-needed execution, shared context, subscriptions), three internal usage patterns (feature work, migrations, gardening) with one named worked example (a design-system Project), and general availability terms (beta, rolling out September 10, 2026). Does NOT cover: pricing, the underlying coordinator/subagent model selection, the shared-context storage mechanism or format, failure modes, how conflicts between parallel subagents are resolved (contrast with the detailed conflict-resolution mechanisms in `blog-cursor-agent-swarm-model-economics.md`), or a technical description of the "subscription" trigger implementation.

## Extracted Claims

### Claim 1: Projects lets a user take on a body of work — a feature, a migration, or a full app — via a coordinator that maintains context over months, delegates to thousands of subagents, and performs recurring work without being prompted
- **Evidence**: Opening product description, the framing sentence for the entire launch.
- **Confidence**: emerging (vendor product description; internal usage in Claim 3 lends some substantiation)
- **Quote**: "Today we're launching Projects in Cursor. Projects lets you take on larger bodies of work, such as a feature, a migration, or a full app. It maintains context over months of work, delegates tasks to thousands of subagents, and performs recurring work without being prompted."
- **Our assessment**: The "months of work" and "thousands of subagents" figures are unqualified vendor claims with no supporting detail (no case study cites either figure directly). The core shape of the claim — a long-lived, delegating, proactive coordinator — is a real step up in scope from a single chat session or even a single cloud-agent task, and is corroborated structurally by the coordinator/delegate pattern already documented in `blog-cursor-agent-swarm-model-economics.md`.

### Claim 2: Projects is explicitly framed as the concrete implementation of the "third era of software development" vision Cursor outlined in February 2026, moving developers up a level of abstraction from managing individual agents to directing the work itself
- **Evidence**: Direct textual link back to Cursor's own prior strategic post, presented as a fulfillment of that vision.
- **Confidence**: emerging (self-referential vendor narrative; the link is explicit and the framing is consistent with the earlier post's content)
- **Quote**: "In February we outlined our vision for a third era of software development, where fleets of agents take on entire bodies of work. Projects is the concrete implementation of that vision. By moving up a level of abstraction, it frees developers from managing agents and lets them direct the work itself."
- **Our assessment**: This is a useful narrative anchor connecting `blog-cursor-third-era.md`'s abstract "factory" framing (Claim 8 in that note) to a shipped product surface, roughly seven months later. It's worth noting the third-era post's own metrics (35% of Cursor's internal PRs from cloud agents, Feb 2026) and this post's metrics (30%/6x PR-merge multipliers, Sept 2026) use different denominators and are not directly comparable as a single growth trajectory — they measure different things (share of PRs vs. per-user merge-rate multiplier).

### Claim 3: Cursor's internal usage of Projects over several months produced a "substantial productivity multiplier": new users merge 30% more PRs, and users who primarily use Projects merge six times as many
- **Evidence**: First-party internal usage metric, tied to specific internal use cases (migrations of "a few hundred PRs," design-system consistency work, and using Projects to ship Projects itself).
- **Confidence**: anecdotal (single vendor's internal, unaudited metric; no cohort definition, no confidence interval, no explanation of what "primarily use" means as a threshold)
- **Quote**: "At Cursor, we've been using Projects for several months, doing work such as running migrations of a few hundred PRs, keeping our design system consistent, and shipping Projects itself. We've found it to be a substantial productivity multiplier: new users merge 30% more PRs while users who primarily use Projects merge six times as many."
- **Our assessment**: The 6x figure for heavy users is the headline number but is the least interpretable: it could reflect selection effects (developers who adopt heavily may already work on more parallelizable, PR-heavy tasks like migrations and lint fixes) rather than a like-for-like productivity gain. The 30% figure for new users is more interpretable as an adoption-curve effect but still lacks a control group. Treat both as directional vendor claims, not measured causal effects.

### Claim 4: The coordinator agent does not write code itself — it only directs other agents that do — and because it delegates rather than executes, it is "never blocked and always responsive to direction"
- **Evidence**: Direct architectural/behavioral description of the coordinator's role.
- **Confidence**: anecdotal (product description of designed behavior, not a measured property)
- **Quote**: "You oversee a Project by chatting with its coordinator agent. The coordinator doesn't write code itself but directs other agents that do. Because it delegates rather than executes, it is never blocked and is always responsive to direction."
- **Our assessment**: This is architecturally the same planner/worker separation-of-concerns already documented in `blog-cursor-agent-swarm-model-economics.md` Claim 1 ("Planner agents... split a goal into pieces and delegate them," "Worker agents... execute those pieces") and Claim 2 (planners stay responsive because their context never fills with implementation detail). The novel framing here is packaging that separation as a single persistent, user-facing chat partner (the "coordinator") rather than an internal harness role invisible to the user — this is the product-surface version of the swarm-economics post's internal-harness architecture.

### Claim 5: Projects run cloud-by-default on a dedicated machine so the work continues after the user's laptop closes, and this lets a Project run more subagents in parallel than the user's laptop could support; when something needs testing on the user's own machine, the coordinator spins up a local agent for that purpose
- **Evidence**: Named "core capability" ("Cloud by default, local when needed"), with an explicit mechanism (local agent spin-up for local-machine testing needs).
- **Confidence**: emerging (vendor architectural description, consistent with disclosed cloud-agent VM architecture elsewhere in the corpus)
- **Quote**: "A Project runs on its own computer, so closing your laptop doesn't stop it. This lets a Project run more subagents in parallel than your laptop could support. When something needs testing on your machine, the coordinator spins up a local agent to run it there."
- **Our assessment**: This is a hybrid cloud/local execution model, distinct from the purely local-vs-cloud dichotomy in `blog-cursor-third-era.md` (Claim 5: synchronous/local agents "compete for resources on the local machine" vs. cloud agents on dedicated VMs) and from the pure cloud-VM execution described in `blog-cursor-self-hosted-cloud-agents.md`. Here, the default execution venue is cloud, but the architecture explicitly falls back to the user's own machine for tasks that require it (e.g., a mobile simulator, a local-only service, hardware access) — extending rather than replacing the cloud-first model with a local escape hatch.

### Claim 6: Each Project maintains a set of files that sync across every cloud and local machine its agents use, accumulating research, artifacts, and learned preferences about the codebase and how the user prefers work to be done — making the coordinator more effective over time
- **Evidence**: Named "core capability" ("Shared context"), with a worked mechanism example (one agent's discovery becomes reusable by all future agents).
- **Confidence**: emerging (vendor architectural description; no detail on the storage format, retrieval mechanism, or how staleness/conflicts in the shared files are handled)
- **Quote**: "You shouldn't have to onboard an agent every time you start a task. Each Project maintains a set of files that sync across every cloud and local machine its agents use. Agents add research and artifacts, along with what they learn about the codebase and how you prefer work to be done. If one agent figures out how to test a service, for example, every future agent can use those instructions. This context grows with the Project, making the coordinator more effective over time."
- **Our assessment**: This is a project-scoped, agent-populated persistent memory store, distinct from static developer-authored context (CLAUDE.md-style files) in that the agents themselves are the ones writing to it as they work. It resembles the "Field Guide" stigmergy mechanism in `blog-cursor-agent-swarm-model-economics.md` Claim 11 (a shared, agent-authored artifact injected into every agent, capturing "surprise encounters" so future trajectories are shorter) but is framed here as a persistent per-Project store rather than a single run-scoped folder — suggesting the same underlying pattern applied at a longer time horizon (a whole Project's lifetime vs. one swarm run).

### Claim 7: The coordinator can be subscribed to a Slack channel, a schedule, or a stream of pull requests (fixing CI, acting when PRs open or merge), enabling it to act on detected signals without the user having to prompt it
- **Evidence**: Named "core capability" ("Subscriptions"), with three concrete trigger types listed.
- **Confidence**: emerging (vendor product description of a shipped feature)
- **Quote**: "The coordinator can watch a Slack channel, run on a schedule, or follow all your PRs, fixing CI and acting when they open or merge. This way it can take action based on signals it detects, without waiting for you to prompt it."
- **Our assessment**: This is functionally convergent with Cognition's "Scheduled Devins" feature (`blog-cognition-devin-schedule-devins.md`), which independently ships the same underlying pattern — a persistent agent that carries state across recurring, trigger-based runs rather than requiring a fresh prompt each time — including an explicit Slack-monitoring example (Claim 5 in that note) and a PR/release-notes-tracking example (Claim 4). Two vendors converging on "give the agent a standing subscription, not a one-off task" within roughly six months of each other is moderate evidence this is becoming a expected capability tier for agent products, not a one-off feature bet.

### Claim 8: In the feature-work usage pattern, agents research the system and record findings as shared context, the coordinator creates a plan and sends agents to implement and test different parts in parallel, and after shipping the same Project continues monitoring logs and handling bug reports with the full context behind the original decisions
- **Evidence**: Named usage pattern ("Feature work") with a described end-to-end lifecycle (research → plan → parallel implementation → local testing → post-ship monitoring).
- **Confidence**: anecdotal (vendor-described intended workflow, not a specific measured case study)
- **Quote**: "A feature usually starts with agents researching the system and recording what they learn as shared context. The coordinator then creates a plan and sends agents to implement and test different parts of it in parallel." ... "After it ships, the same Project can monitor logs and handle bug reports with the full context behind the original decisions."
- **Our assessment**: The claim that post-ship bug handling retains "the full context behind the original decisions" is the most interesting part for context engineering: it implies the shared-context store (Claim 6) persists past the initial delivery of the feature, so a bug report weeks later can be triaged by an agent that already knows the original design rationale — closing a loop that normally requires a human to reconstruct context from commit history and old tickets.

### Claim 9: In the migrations usage pattern, the user and coordinator first establish a safe approach together, then the coordinator applies it incrementally across the codebase, with the user reviewing closely at first and reviewing less as the pattern proves reliable
- **Evidence**: Named usage pattern ("Migrations"), with two concrete internal examples (framework adoption, styling-system replacement across "hundreds of PRs") and an explicit trust-tapering review model.
- **Confidence**: anecdotal (vendor-described workflow; the "hundreds of PRs" figure is internal and unaudited)
- **Quote**: "Projects are especially useful for migrations that are easy to start and difficult to finish. At Cursor, we've used them to adopt new frameworks and replace styling systems across hundreds of PRs." ... "You work with the coordinator to establish a safe approach, then it applies that approach incrementally across the codebase. Early on, you review each PR closely. As the fixes hold up, you review less, and the coordinator keeps working through the migration on its own."
- **Our assessment**: The explicit tapering-review model (review every PR closely → review less as trust builds → coordinator proceeds autonomously) is a concrete, reusable heuristic for how much human oversight a long-running autonomous migration needs at different points in its lifecycle. This is more operationally specific than the general "trust but verify" framing common elsewhere in the corpus, because it ties the tapering explicitly to observed reliability within a single migration rather than treating trust as a fixed policy.

### Claim 10: A named internal example — a design-system Project run by one Cursor engineer — evolved from the engineer reviewing and correcting every fix to the coordinator scanning every new PR, extracting design-system components, and adding a lint rule whenever it sees the same mistake twice, on track to touch 20 to 100 PRs a day
- **Evidence**: Single named (if anonymized — "one engineer on our team") worked example under the "Gardening" usage pattern, with a specific daily-throughput figure.
- **Confidence**: anecdotal (single internal example, not independently verifiable, no named individual)
- **Quote**: "One engineer on our team runs a design-system Project this way. At first, the engineer reviewed each fix and corrected the ones it got wrong. Now the coordinator scans every new PR, extracts components that belong in the design system, and adds a lint rule whenever it sees the same mistake twice. The Project is on track to touch 20 to 100 PRs a day, so the coordinator organizes the work and the engineer checks in where attention is needed."
- **Our assessment**: The self-reinforcing lint-rule-generation loop ("adds a lint rule whenever it sees the same mistake twice") is the single most concrete, mechanistic detail in the source — a specific example of an agent converting a recurring correction into a durable, automatically-enforced artifact rather than repeating the same correction indefinitely. This is a pattern worth generalizing beyond design systems: any Project where a human keeps making the same category of correction is a candidate for auto-generating an enforcement rule from that correction. The "20 to 100 PRs a day" figure is a wide, unaudited range for a single anonymized example and should not be treated as a typical throughput figure.

### Claim 11: Projects launched in beta and is rolling out to all users starting September 10, 2026, positioned as best suited for "work that will outlive a single chat"
- **Evidence**: General availability / rollout statement with an explicit fit criterion.
- **Confidence**: settled (a factual, verifiable launch-status statement as of publication)
- **Quote**: "Projects are available in beta and rolling out to all users starting today. Start a Project from the left hand nav, describe what you want built, and the coordinator takes it from there. It works best on work that will outlive a single chat, whether that's a feature with several PRs, a migration, or a job you want handled while you're away."
- **Our assessment**: The explicit fit criterion ("outlive a single chat") is a useful practical heuristic for when to reach for a Project versus a single agent session or a one-off cloud-agent task: multi-PR features, migrations, and unattended/recurring jobs are the target use cases; single-session tasks are explicitly out of scope for this framing.

## Concrete Artifacts

```
Projects — three named "core capabilities"
Source: "Introducing Projects," Cursor (Sept 10, 2026)

1. Cloud by default, local when needed
   - Runs on its own dedicated computer (survives laptop closing)
   - Enables more parallel subagents than a local machine could support
   - Coordinator spins up a local agent when testing requires the user's machine

2. Shared context
   - A set of files synced across every cloud and local machine the Project's agents use
   - Agents write research, artifacts, and learned codebase/preference info into it
   - Grows over the Project's lifetime; later agents reuse earlier agents' discoveries

3. Subscriptions
   - Watch a Slack channel
   - Run on a schedule
   - Follow all PRs (fix CI, act on open/merge)
   - Enables proactive action on detected signals without an explicit prompt
```

```
Projects — three named usage patterns at Cursor (internal)
Source: "Introducing Projects," Cursor (Sept 10, 2026)

Feature work:
  research system -> record as shared context -> coordinator plans
  -> parallel implement/test -> local test run when ready
  -> post-ship: monitor logs, handle bug reports with original decision context

Migrations:
  establish safe approach with coordinator -> apply incrementally across codebase
  -> review each PR closely (early) -> review less as fixes hold up
  -> coordinator proceeds autonomously through remaining migration
  Named examples: framework adoption, styling-system replacement ("hundreds of PRs")

Gardening (worked example — one engineer's design-system Project):
  Phase 1: engineer reviews and corrects every fix
  Phase 2: coordinator scans every new PR, extracts design-system components,
           adds a lint rule whenever it sees the same mistake twice
  Throughput: "on track to touch 20 to 100 PRs a day"
```

```
Headline internal productivity metric
Source: "Introducing Projects," Cursor (Sept 10, 2026)

New users:              merge 30% more PRs
Primary Projects users: merge 6x as many PRs
Internal use cases cited: migrations of "a few hundred PRs", design-system
  consistency, and using Projects to ship Projects itself
```

## Cross-References

- **Extends**: `blog-cursor-third-era.md` — This post explicitly names itself the "concrete implementation" of the third-era vision (Claim 2 here; corroborates that note's Claim 8, the "factory" metaphor, and Claim 7, the developer-as-teammate-manager framing). Note the metrics are NOT a continuous series: the third-era post's 35%→40%+ figures measure share of internal PRs from cloud agents generally, while this post's 30%/6x figures measure a per-user PR-merge multiplier specific to Projects adoption — cite them as related-but-distinct metrics, not points on the same trend line.

- **Corroborates**: `blog-cursor-agent-swarm-model-economics.md` — The coordinator/subagent split described here (Claim 4) is the same planner/worker separation of concerns documented in that note's Claims 1–2, now packaged as a single user-facing chat partner rather than an internal harness role. The "Shared context" capability (Claim 6 here) is architecturally similar to that note's "Field Guide" stigmergy artifact (Claim 11) — both are agent-authored, agent-consumed shared stores meant to shorten future agent trajectories — but this post applies the pattern at a whole-Project lifetime horizon rather than a single run.

- **Corroborates**: `blog-cognition-devin-schedule-devins.md` — Cursor's "Subscriptions" capability (Claim 7 here) and Cognition's "Schedule Devins" feature independently converge on the same pattern: a persistent agent that carries state across recurring, trigger-based runs (Slack monitoring, PR tracking, schedules) rather than requiring a fresh prompt each time. Two competing vendors shipping the same capability tier within roughly six months is moderate evidence this is becoming an expected agent-product feature, not an isolated bet.

- **Extends**: `blog-cursor-self-hosted-cloud-agents.md` and `blog-cursor-cloud-agent-lessons.md` — Both describe a cloud-VM-centric execution model for Cursor's background/cloud agents. This post's "Cloud by default, local when needed" capability (Claim 5) extends that model with an explicit local-fallback mechanism for tasks that require the user's own machine (e.g., local-only test dependencies), which neither prior post describes.

- **Contradicts**: None identified. No existing source note makes a claim about coordinator/subagent architecture, shared-context stores, or subscription-based triggering that this post's claims conflict with.

- **Novel**: 
  - The specific packaging of the planner/worker split as a single, persistent, user-facing "coordinator" chat partner (rather than an invisible harness role) is new to the corpus as a *product* framing, even though the underlying architectural pattern is corroborated elsewhere.
  - The explicit "review closely early, review less as trust builds, then let the coordinator finish alone" tapering model for long-running migrations (Claim 9) is a new, reusable operational heuristic not stated this explicitly in any other corpus source.
  - The self-reinforcing "adds a lint rule whenever it sees the same mistake twice" mechanism (Claim 10) is a concrete, generalizable example of an agent converting a recurring human correction into a durable enforcement artifact — not documented elsewhere in the corpus in this specific mechanistic form.
  - The hybrid "cloud by default, local when needed" execution split (Claim 5) is new; prior corpus sources describe either pure local execution or pure cloud VM execution, not an architecture that defaults to cloud but falls back to local per-task.

## Guide Impact

- **Chapter 01 (Daily Workflows) — "Multi-Agent Orchestration" / "The Factory Model" / "Quality Enforcement in Coordinator Prompts"**: This source is a first-party vendor description of a shipped product that matches the chapter's existing "coordinator" and "factory model" vocabulary almost exactly. The tapering-review model for migrations (Claim 9) and the self-reinforcing lint-rule mechanism (Claim 10) are concrete enough to cite as illustrative examples of how a coordinator's role should shift from close supervision to autonomous execution as reliability is demonstrated — this could sharpen the existing "Quality Enforcement in Coordinator Prompts" section with a real vendor example beyond the guide's current framing.

- **Chapter 04 (Context Engineering) — "Memory and Persistence"**: The "Shared context" capability (Claim 6) — an agent-populated, cross-session, cross-machine persistent store that grows over a Project's lifetime — is a concrete example of externalized, agent-authored memory distinct from the developer-authored CLAUDE.md pattern the chapter currently emphasizes. Worth citing alongside the "Field Guide" pattern from `blog-cursor-agent-swarm-model-economics.md` as two vendor implementations of the same underlying idea: let agents write down what they learn so future agents/sessions don't re-discover it.

- **Chapter 01 (Daily Workflows) — new "when to reach for a persistent coordinator vs. a single session" guidance**: Claim 11's explicit fit criterion ("work that will outlive a single chat") is a crisp, quotable heuristic for a decision the guide currently addresses only implicitly (e.g., in "When to Restart a Session" and "When NOT to Delegate"). Recommend citing it as vendor-stated framing for a threshold the guide already discusses from a different angle.

## Extraction Notes

- The article is short (~700 words in the main prose body) but was read in full, including the embedded Next.js page-data JSON that contains the complete verbatim article text (the rendered HTML is client-side rendered and does not expose body text directly to a plain HTTP fetch, so the source was located and extracted from the page's server-rendered JSON payload to guarantee verbatim quotes rather than an LLM-summarized rendering). The linked "third era" post (`https://cursor.com/blog/third-era`) was not re-read in full since it is already covered by the existing `blog-cursor-third-era.md` note in this corpus; that note was used directly for cross-referencing instead of re-extracting.
- The Prospector's triage comments on the source issue were inconsistent: two of the three comments (filed before the source was actually read) guessed at generic "project management" / "workspace organization" content and rated novelty medium, based only on the title "Introducing Projects." The third comment correctly anticipated multi-agent fleet coordination content and specific productivity metrics (30%/6x), which matches what this note found on actually reading the source — the third comment's assessment is the accurate one and was used to guide extraction; the first two appear to have been filed without reading the body.
- No sub-pages beyond the linked third-era post were followed, since the article itself is short and self-contained and the one substantive outbound link was already covered in the corpus.
- No paywall or access issues; the source was fully readable.
