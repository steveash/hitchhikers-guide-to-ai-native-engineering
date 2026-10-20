---
source_url: https://cursor.com/blog/navan
source_type: blog-post
title: "Navan cuts a month-long migration down to a week, without freezing the codebase"
author: "Cursor Team (vendor case study; named practitioners: Rahul Popuri — Sr. Staff Software Engineer, Elton Yang — Staff Software Engineer, both at Navan)"
date_published: 2026-10-16
date_extracted: 2026-10-20
last_checked: 2026-10-20
status: current
confidence_overall: anecdotal
issue: "#4224"
---

# Navan Cuts a Month-Long Migration Down to a Week, Without Freezing the Codebase

> A short vendor case study describing a plan-once, fan-out-per-component Spring Boot 4 migration run by Cloud Agents on self-hosted machines, with a before/after comparison against a manual migration that locked `master`, plus a human-review-retained caveat.

## Source Context

- **Type**: blog-post (Cursor customer story, ~4 min read, Oct 16, 2026; quotes from two named Navan engineers)
- **Author credibility**: Published by Cursor (vendor marketing). Named practitioners give quotes, but the headline numbers are vendor-reported with no methodology, baselines, or failure discussion.
- **Scope**: Covers one migration (Spring Boot 4, 8 apps, 15 libraries), the Cloud Agent setup (Cursor-managed GitHub work, self-hosted MCPs and browsers), adoption numbers, and two product-team examples. Does NOT cover: cost, prompts/plan format, how the 8 agents were coordinated, how conflicts were avoided, failure or rollback rates, or how the "36%" was measured.

## Extracted Claims

### Claim 1: Planning a migration once and delegating each component to a parallel cloud agent let 8 apps and 15 libraries move simultaneously
- **Evidence**: Single named-engineer account; ~1 week outcome. No plan artifact or merge/conflict data shown.
- **Confidence**: anecdotal
- **Quote**: "Rahul planned the upgrade in advance, then delegated each component to Cloud Agents running on Navan's self-hosted machines, so 8 applications and 15 libraries moved at the same time instead of one after another."
- **Our assessment**: Plausible and consistent with the Faire Swarm pattern, but unlike Faire (sequential, merge-triggered) this is truly parallel, and the post gives no detail on dependency ordering between shared libraries and apps — the hard part. Treat the timing as vendor-reported.

### Claim 2: Parallel migration avoided the codebase freeze and master-branch disruption that a prior manual migration caused
- **Evidence**: Before/after narrative from the same engineer: a prior comparable migration took over a month and a bad merge locked master for a day.
- **Confidence**: anecdotal
- **Quote**: "Two years ago, a comparable migration took over a month, and a bad merge locked the master branch for a day."
- **Our assessment**: Useful failure context for the "before" state; the comparison is not controlled (different Spring version, different time, different tooling). "Without freezing" is asserted via the engineer's quote, not measured.

### Claim 3: The larger cost of a manual migration is the engineer's lost time and lingering catch-up, not just the lock itself
- **Evidence**: Author's framing of the earlier incident.
- **Confidence**: anecdotal
- **Quote**: "The bigger cost wasn't the lock itself. It was the month of an engineer's time spent on the migration instead of shipping features or fixing bugs."
- **Our assessment**: Reasonable framing for ROI of agent migrations: opportunity cost of a senior engineer, not compute cost.

### Claim 4: Agents on self-hosted machines used internal tooling and drove a real browser to verify their own changes
- **Evidence**: Description of the setup; no verification pass rates or examples.
- **Confidence**: anecdotal
- **Quote**: "The agents used Navan's internal tooling and spun up browsers on those same machines to click through flows and verify their changes."
- **Our assessment**: The one genuinely incremental detail over earlier Cursor case studies: self-verification via browser happens inside the customer's network, where internal systems are reachable. How reliable that verification was is not reported.

### Claim 5: Cloud Agents use a hybrid split — GitHub work on Cursor-managed infrastructure, internal MCPs and browser verification on customer self-hosted machines
- **Evidence**: Architecture described in one paragraph.
- **Confidence**: anecdotal
- **Quote**: "GitHub work runs on Cursor-managed infrastructure. Internal MCPs for Snowflake and Slack run on Navan's own self-hosted machines, where agents can also spin up a browser to verify their own changes."
- **Our assessment**: A concrete hybrid deployment example for the self-hosted note: the split follows data/network sensitivity (internal MCPs local, repo operations hosted).

### Claim 6: Asynchronous, unattended operation was the deciding capability versus the previous coding agent, which required a person at a desktop
- **Evidence**: Author statement about Navan's previous setup; no tool named.
- **Confidence**: anecdotal
- **Quote**: "Before Cursor, Navan's engineers had built real infrastructure around their previous coding agent, but it required someone at one desktop with the session open the whole time."
- **Our assessment**: Supports the corpus theme that headless/cloud execution, not model quality, unlocks parallelism. Vendor comparison of an unnamed competitor; weigh accordingly.

### Claim 7: Automations, Skills, and Memories layered on cloud agents let eval loops and migrations continue without supervision
- **Evidence**: Single sentence; no config shown.
- **Confidence**: anecdotal
- **Quote**: "Automations, Skills, and Memories run on top of that setup, so eval loops and migrations continue asynchronously without someone watching them."
- **Our assessment**: Assertion only; no specifics on what runs unattended or what monitoring exists. The engineer role shifts to monitoring multiple agents ("monitoring multiple agents upgrading different applications at once").

### Claim 8: Agents can bootstrap new agents from a plain description by following existing design patterns and writing prompts
- **Evidence**: Named quote from Elton Yang; one team example.
- **Confidence**: anecdotal
- **Quote**: "We don't even have to write out the agent prompt ourselves anymore. Cursor follows our prior designs and gets an agent working the same day."
- **Our assessment**: Interesting prompt-generation-by-agent pattern, dependent on a corpus of prior designs in the repo. No quality evaluation of generated prompts.

### Claim 9: One engineer replaced 2–3 engineers' multi-sprint feature work, including crossing stack boundaries (Angular→React plus backend)
- **Evidence**: Manual bank-linking example, narrative only.
- **Confidence**: anecdotal
- **Quote**: "one engineer took over feature work that previously needed 2 or 3 engineers across multiple sprints."
- **Our assessment**: Vendor-reported; confounded by team reorganization (many engineers had left the AI-agent team). Do not use as a productivity number.

### Claim 10: Agents accelerate onboarding to unfamiliar codebases by investigating logs and database records
- **Evidence**: Named quote and an estimate of ~2 days saved.
- **Confidence**: anecdotal
- **Quote**: "It pulled the logs and the database and walked me through it like I had been living in that repo for months."
- **Our assessment**: Depends on agent access to logs/DB (via internal MCPs); the "two days" estimate is the author's, unmeasured. Access-to-production-data implications are not discussed.

### Claim 11: Human review and staging verification remain the control point; engineers own the merge
- **Evidence**: Description of Navan's process.
- **Confidence**: anecdotal
- **Quote**: "Agents plan and execute the work, but engineers make the judgment calls and own the final merge."
- **Our assessment**: Consistent with the common pattern; the specifics (human plus AI review, staging for complex changes, pair-programmer posture watching reasoning) are lightweight but usable. Note this sits in tension with the "36% of PRs authored" headline only if review is a bottleneck, which is unaddressed.

## Concrete Artifacts

Vendor-reported headline metrics (not independently validated; per triage, not treated as standalone claims):

```
Source: https://cursor.com/blog/navan (stat tiles)
~1 week  — Spring Boot migration across 8 apps and 15 libraries
~200     — engineers actively using Cursor's Cloud Agents, "a 10x increase since April 2026"
36%      — share of merged core-repo pull requests authored with Cursor over a 30-day period
```

Setup as described (paraphrased, no config published): plan once → one Cloud Agent per component (8 apps, 15 libraries) on self-hosted machines → agents use internal tooling + headless/real browser to click through flows → normal human + AI review, staging, human merge.

No code, prompts, or configuration were published.

## Cross-References

- **Corroborates**: `blog-cursor-faire-cloud-agents.md` (migration fanned out to isolated cloud agents; Claim 5 describes the Swarm queue), `blog-cursor-nab-legacy-migration.md` (enterprise migration via agents), `blog-cursor-self-hosted-cloud-agents.md` (self-hosted execution environment).
- **Contradicts**: None found. (Faire runs migration units sequentially on merge; Navan runs components in parallel — a difference in context, not a contradiction.)
- **Extends**: `blog-cursor-faire-cloud-agents.md` and `blog-cursor-grab-cross-functional-adoption.md` as vendor case studies with adoption metrics; adds before/after failure context (master lock) and browser-based self-verification on self-hosted machines.
- **Novel**: Fully parallel plan-once migration across apps and shared libraries with no code freeze; hybrid hosting split (GitHub work on vendor infra, internal MCPs and browsers on customer machines); agent-authored agent prompts from prior designs.

## Guide Impact

- **Chapter 01**: Can add Navan as another migration example, noting the parallel (vs. Faire's sequential) topology and that the post omits how shared-library ordering was handled; mark as vendor-reported.
- **Chapter 02**: For cloud/self-hosted agents, cite the hybrid hosting split and in-network browser verification as a harness design option (Claim 4, Claim 5).
- **Chapter 05**: Navan's adoption figures may be mentioned only as vendor-reported alongside Faire/Grab; the retained-human-review statement (Claim 11) is the usable operational guidance.

## Extraction Notes

- Read the full article (single page, no sub-pages to follow). Quotes copied verbatim from the page text.
- Source is thin on mechanics: no plan format, coordination method, or failure data. Overall confidence set to anecdotal accordingly.
- Per Prospector triage, headline metrics are retained only as vendor-reported artifacts.
