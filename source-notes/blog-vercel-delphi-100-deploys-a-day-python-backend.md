---
source_url: https://vercel.com/blog/how-delphi-ships-100-times-a-day-with-its-python-backend-on-vercel
source_type: blog-post
title: "How Delphi ships 100 times a day with its Python backend on Vercel"
author: Susan Aziz, Kevin Sundstrom (Vercel); quotes Spencer Schoeben (Delphi founding engineer)
date_published: 2026-09-15
date_extracted: 2026-10-13
last_checked: 2026-10-13
status: current
confidence_overall: anecdotal
issue: "#4086"
---

# How Delphi ships 100 times a day with its Python backend on Vercel

> Vendor-authored customer story in which a 10-engineer startup self-reports 100+ daily production deploys with no staging step (feature flags and A/B tests instead), hands work to cloud agents whose output is first checked on per-push preview URLs, and says agent failures usually trace to missing information rather than model capability.

## Source Context

- **Type**: blog-post (Vercel customer story, ~5 min read; auto-discovered from Vercel's trusted Atom feed).
- **Author credibility**: Vercel marketing/content authors; the substantive claims are all attributed to one Delphi founding engineer, Spencer Schoeben. Vendor-authored, so platform claims are promotional. No independent verification.
- **Scope**: Covers Delphi's backend migration from AWS (ECS, Docker Desktop, local databases) to Vercel, deploy cadence, preview deployments as the agent check surface, an internal Slack-facing support agent on Sandbox, and per-customer model routing via AI Gateway. Gives no figures beyond team size and the 100+/day deploy count. No data on defect rates, rollbacks, flag debt, or agent task success.

## Extracted Claims

### Claim 1: A 10-engineer team with no dedicated infrastructure role ships 100+ production deploys a day, skipping staging
- **Evidence**: Self-report in the post's headline bullets and body; no metrics, dashboards, or independent confirmation.
- **Confidence**: anecdotal
- **Quote**: "The team used to deploy to staging, then production. Now it skips the middle step, shipping 100+ times a day behind feature flags and running A/B tests instead of batching changes into a release."
- **Our assessment**: Plausible for a small product team that is deliberately experimenting; the cadence is the customer's own claim. "Deploy" counts are not "releases" (flags decouple them), so 100+/day says little about user-visible change rate. Hard-won safety comes from flags and anomaly detection, not from the deploy count.

### Claim 2: Feature flags plus A/B tests replace staging and batched releases as the risk-control mechanism
- **Evidence**: Stated as the operating model; no detail on flag lifecycle, rollout stages, or cleanup.
- **Confidence**: anecdotal
- **Quote**: "Moving the backend to Vercel let Delphi stop treating backend changes as heavyweight releases and ship them as everyday product work."
- **Our assessment**: Consistent with Vercel's own flag-first practice (see Cross-References), but this source provides no operational detail. Worth recording as a pattern (trunk-to-prod + flags) while noting the absence of failure-handling evidence.

### Claim 3: Preview deployments are where humans first see what a cloud agent built
- **Evidence**: Description of Delphi's workflow; little development happens locally.
- **Confidence**: anecdotal
- **Quote**: "Delphi's engineers hand problems to cloud agents, with very little development happening locally. The preview deployment is where they first see what the agent built."
- **Our assessment**: A concrete verification-surface pattern: per-push live URL as the review artifact for agent work. Note the framing is *human* review of an agent's result, not agent self-verification, despite the section heading "Preview deployments are how agents check their work".

### Claim 4: Per-push preview URLs make agent output checkable by anyone, from a phone or Slack, without pulling the branch
- **Evidence**: Product description of Vercel preview deployments.
- **Confidence**: anecdotal
- **Quote**: "Vercel preview deployments give every push its own live URL, so anyone can check the result from a phone or a Slack thread without pulling the branch."
- **Our assessment**: Real benefit for non-engineer review and for async agent workflows; it is a vendor feature description, not an evaluated result.

### Claim 5: Agent failures are usually information-access failures, so the platform exposes logs, deployments, and env vars through SDK, MCP, and CLI
- **Evidence**: Author/vendor assertion; no failure analysis or counts offered.
- **Confidence**: anecdotal
- **Quote**: "When an agent fails, it's usually because it couldn't get at the information it needed."
- **Our assessment**: Matches a recurring harness-engineering theme (give agents observability/context). Unquantified, and the source is a vendor that sells those interfaces.

### Claim 6: Agents are now the main users of the platform's tools, so tooling must be as easy for agents as for people
- **Evidence**: Stated by the authors.
- **Confidence**: anecdotal
- **Quote**: "For Delphi, agents are now the main users of those tools, so the platform has to be as easy for them as it is for people."
- **Our assessment**: Interesting design-stance claim ("agent-first" ergonomics), but no usage data supports "main users".

### Claim 7: Old infrastructure was unworkable for agents because it assumed human-scale debugging effort
- **Evidence**: Founding-engineer quote; no concrete failing case described.
- **Confidence**: anecdotal
- **Quote**: "We couldn't keep up with AI on our old infrastructure. If it took a human eight hours to figure out, an agent would have given up."
- **Our assessment**: Rhetorical but points at a real hypothesis: environments requiring long, tacit setup defeat agents. Unsupported by measurement.

### Claim 8: Local-environment setup (ECS, Docker Desktop, local DBs) made new-engineer onboarding take a full day; moving to the platform deploy workflow shortened it
- **Evidence**: Qualitative; the post gives no after-figure.
- **Confidence**: anecdotal
- **Quote**: "getting a new engineer to their first deploy took a full day of environment setup."
- **Our assessment**: Credible direction; "much faster" after the move is not quantified. Also a "tacit context in people's heads" admission worth noting.

### Claim 9: Durable long-running work and queued background jobs are expressed as ordinary functions in the codebase, which is what made the migration feasible
- **Evidence**: Description of Workflows and Queues; Schoeben says the move would have been much harder without them.
- **Confidence**: anecdotal
- **Quote**: "A developer writes the workflow or the queue handler as a function in the codebase, and Vercel provisions what's needed to run it on deploy."
- **Our assessment**: Platform-promotional; low value as a general finding. Useful only as a data point that agent-heavy backends (durable agents, ingestion pipelines) drive demand for durable-execution primitives.

### Claim 10: Production anomaly detection compensates for the lack of a staging gate
- **Evidence**: One sentence; no detection rates or examples.
- **Confidence**: anecdotal
- **Quote**: "Vercel Agent's anomaly detection watches production at that pace, flagging when something is misbehaving and why."
- **Our assessment**: The only stated post-deploy safety net besides flags; treat as unproven vendor claim. Without staging, detection quality is the crux, and the post gives none.

### Claim 11: Non-engineers (CPO, growth) build and deploy dashboards, prototypes, and experiments themselves
- **Evidence**: Self-report; "wouldn't have happened on the old setup" is Schoeben's view.
- **Confidence**: anecdotal
- **Quote**: "Delphi's CPO and its growth teams build and deploy dashboards, prototypes, and experiments themselves, which Spencer says wouldn't have happened on the old setup."
- **Our assessment**: Relevant to team-adoption chapters; no detail on guardrails for non-engineer deploys.

### Claim 12: An internal Sandbox agent lets customer success trace reported issues to a root cause and proposed fix; built on eve so tools are Delphi-written code
- **Evidence**: Described workflow; the first version on a hosted agent platform was limited to that platform's integrations.
- **Confidence**: anecdotal
- **Quote**: "In eve, tools are code Delphi writes, so when a question needs one that doesn't exist, the team adds it."
- **Our assessment**: A reasonable internal-agent pattern (Slack in, isolated checkout out, hand engineer a root cause). The "tools as code you own vs. integration catalog" contrast is the transferable point.

### Claim 13: Model choice is per customer, adjusted as evals change, with same-day routing to new models and gateway-managed failover
- **Evidence**: Description of use of AI Gateway; no eval methodology or results.
- **Confidence**: anecdotal
- **Quote**: "Every digital mind is different, and some come out better on one model than another, so Delphi picks the model for each customer and adjusts as its own evals change."
- **Our assessment**: Per-tenant model selection backed by own evals is a sound pattern; the post offers no eval details.

## Concrete Artifacts

No code, configs, or transcripts. Headline facts (all self-reported, Vercel blog, 15 Sep 2026):

```
10 engineers with no dedicated infrastructure role
Everyone ships code, including product and design
100+ production deploys a day behind feature flags
```

Stack described: Vercel Workflows (long-running), Queues (background jobs), Preview deployments, Vercel Agent anomaly detection, Sandbox + eve (internal agent), AI Gateway (model routing/failover). Prior stack: AWS ECS, Docker Desktop, local databases.

## Cross-References

- **Corroborates**: `blog-vercel-flags-platform-native-feature-flags.md` Claim 7 (every feature behind a flag, merge to main continuously) and Claim 9 (flags control AI model traffic), same flag-first shipping model, but Vercel's own practice, so not independent. `blog-vercel-sandstone-legal-growth.md` Claim 3 (preview branches as most time-saving feature) and Claim 5 (automatic preview on every push); same vendor customer-story format. `blog-vercel-agent-runs-mcp-cli.md` Claim 1 (coding agents can inspect platform data via MCP and CLI), consistent with the "expose data to agents via SDK/MCP/CLI" stance.
- **Contradicts**: None found. Note the tension (not a filed contradiction) between "no staging" here and `blog-vercel-flags-platform-native-feature-flags.md` Claim 10, where a high-stakes DB migration used repeated staging rehearsals; the difference is context (routine changes vs. a one-off migration).
- **Extends**: `blog-vercel-ai-gateway-production-index-may2026.md` Claim 10 (production apps route across many models) with a per-customer, eval-driven example. `blog-vercel-sandbox-routing-18x-faster.md` and `blog-vercel-sandbox-managed-images.md` with a customer-side Sandbox internal-agent use case.
- **Novel**: A customer's first-person account of preview URL as the human review surface for cloud-agent output, the "agent failures are information-access failures" stance, and a staging-free flag-gated cadence for a team of ten.

## Guide Impact

- **Chapter 03 (verification)**: Could cite as a single anecdotal example that per-push preview URLs serve as the review artifact for agent work, with the caveat that the source gives no defect data and relies on unproven anomaly detection in place of staging.
- **Chapter 02 (harness)**: Weak supporting evidence for "expose logs/deployments/config to agents via CLI/MCP" as a failure-reduction lever (Claim 5); cite only as anecdotal alongside stronger sources.
- **Chapter 05 (team adoption)**: Optional anecdote on non-engineers deploying and on onboarding time; do not cite figures (none exist).
- No change recommended to existing guide advice; do not present 100+ deploys/day as verified.

## Extraction Notes

- Read the full page (fetched HTML, stripped); no sub-pages followed, as the post links only to product pages.
- Per triage guidance, Vercel product claims (Workflows, Queues, Gateway) were recorded sparingly and flagged as promotional.
- Section heading says agents "check their work", but the body describes humans viewing the preview; flagged in Claim 3.
- The first triage comment cites `blog-vercel-ai-gateway-production-index-june2026.md`; the claim cross-referenced here is from the May index, whose claim numbers were verified.
