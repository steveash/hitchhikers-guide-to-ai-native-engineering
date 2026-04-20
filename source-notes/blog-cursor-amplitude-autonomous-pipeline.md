---
source_url: https://cursor.com/blog/amplitude
source_type: blog-post
title: "Amplitude ships 3x more production code with Cursor"
author: Curtis Liu (CTO), Adam Lohner (Staff Software Engineer), Spencer Pauly (Head of Engineering AI Feedback) — Amplitude engineering team; published on Cursor blog
date_published: 2026-04-15
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#246"
---

# Amplitude Ships 3x More Production Code with Cursor

> A named practitioner case study from Amplitude documenting a fully operational autonomous development pipeline — event-driven Slack→Linear→PR triage, risk-stratified auto-merge (60–70% of PRs), hourly cron legacy-migration bots, and a cloud-vs-local workflow split — with specific operational metrics and a named "false plateau" failure mode for local-only agent adoption.

## Source Context

- **Type**: blog-post (vendor case study — Amplitude engineering team's first-person account, published on Cursor's blog, April 15, 2026; ~1,500 words)
- **Author credibility**: Three named Amplitude engineers — Curtis Liu (CTO), Adam Lohner (Staff Software Engineer), Spencer Pauly (Head of Engineering, AI Feedback) — provide attributed quotes throughout. Amplitude is a public SaaS analytics company (~600 employees at time of writing); their engineering team is credible as a named practitioner source. The piece is published on Cursor's blog, making it vendor-sourced marketing. The specific operational details (hourly cron schedule, Linear integration logic, PR auto-merge rates, 20,000+ React component instances) are credible as genuine practitioner evidence. No failure modes are discussed. Treat as practitioner evidence at emerging confidence, marketing framing acknowledged.
- **Scope**: Covers the cloud agent deployment workflow (Slack→Linear→PR pipeline), Bugbot risk-stratified auto-merge, hourly cron legacy migration automations, the cloud-vs-local workflow split, and the "false plateau" failure mode for local-only agent adoption. Does NOT cover: cost of cloud agent infrastructure, how Bugbot risk thresholds were calibrated, what safeguards prevent bad auto-merges, team rollout timeline, or any discussion of failures or rollbacks.

## Extracted Claims

### Claim 1: An event-driven Slack→Linear→PR pipeline fully delegates customer-facing bug triage to cloud agents, eliminating a dedicated human triage role

- **Evidence**: Named engineers describe the workflow in operational detail: a dedicated Slack channel for customer bug reports → cloud agent monitors the channel → agent checks Linear for existing ticket → if no ticket exists, agent explores the codebase, opens a ticket, implements a fix, and opens a PR. Spencer Pauly explicitly states this eliminated the dedicated triage role.
- **Confidence**: emerging (vendor case study; named engineers; specific operational details; no independent validation)
- **Quote**: "We're running many cloud agents at once in Cursor, each with full access to our tool stack." — Adam Lohner
- **Our assessment**: This is the most architecturally specific claim in the source. The workflow embeds three distinct agent behaviors: (1) event listening (monitor Slack channel), (2) deduplication (check Linear before creating a ticket), and (3) end-to-end task completion (explore codebase → ticket → PR). The deduplication step prevents duplicate work — without it, agents would open multiple PRs for the same reported bug. The elimination of a dedicated human triage role is a significant operational claim: an entire job function is delegated. No specifics on how often the agent gets the fix wrong, how authors verify the PR before merge, or what happens when the Slack report is ambiguous.

### Claim 2: Bugbot risk-stratifies every PR and auto-merges 60–70% of low-risk PRs to production without developer review

- **Evidence**: Specific operational metric from Spencer Pauly. Bugbot assesses every PR's risk level; low-risk PRs merge automatically; high-risk PRs route to appropriate engineers. This represents 60–70% of Amplitude's total PR volume merging to production autonomously.
- **Confidence**: emerging (self-reported; vendor-sourced; no definition of "low-risk" criteria; no error/rollback rate given)
- **Quote**: "Bugbot regularly catches really hard bugs and proposes solid fixes to the issues." — Spencer Pauly
- **Our assessment**: The 60–70% auto-merge rate is the most quantitatively significant operational claim in the source. It implies Amplitude has calibrated a risk classifier that is reliable enough to trust for 60–70% of production changes. The criteria for "low-risk" are not described — this is the critical gap. A risk classifier that auto-merges changes touching configuration files (low blast radius) but gates changes touching authentication or payment logic (high blast radius) is a very different system from one that simply classifies by diff size. The source does not reveal Bugbot's criteria. `blog-cursor-bugbot-learning.md` documents the Bugbot mechanism (three-signal rule lifecycle); this source provides the first named-customer deployment rate.

### Claim 3: Hourly cron automations safely run continuous legacy-code migration without displacing developer time

- **Evidence**: Two specific automation pipelines described: (1) hourly cron scanning CSS files for Tailwind-replaceable styles, replacing them, deleting old files, and opening PRs; (2) separate automation migrating 20,000+ legacy React layout component instances. Both run as background cloud jobs.
- **Confidence**: emerging (specific operational details; two named automation types; no error handling or rollback details given)
- **Quote**: (no direct quote for this claim; described by Adam Lohner)
- **Our assessment**: The hourly cron cadence is a specific operational choice worth extracting: it is frequent enough to make continuous progress but slow enough to not flood the PR queue. The CSS→Tailwind automation is a canonical "well-defined mechanical transformation" use case: the agent has an unambiguous mapping (this CSS → equivalent Tailwind) and can verify correctness by checking that the output compiles and renders equivalently. The React layout migration (20,000+ instances) is a larger-scope version of the same pattern. What is not described: how scope is controlled (does each cron run process all remaining instances or a batched subset?), how merge conflicts are handled when a developer edits a file the cron has also touched, and what the PR review process looks like for cron-generated PRs.

### Claim 4: Local-only agent adoption produces a "false plateau" — a productivity ceiling caused by memory limits, resource conflicts, and inability to self-test

- **Evidence**: Amplitude engineers describe hitting specific limitations with local-only agent use: resource competition causing performance degradation with 2–3 concurrent agents, memory constraints on high-end developer machines with large codebases, inability to test/verify work without manual environment configuration. Switching to cloud agents broke through this ceiling.
- **Confidence**: emerging (named engineers; specific technical limitations described; consistent with the self-hosted cloud agents note's description of why enterprises need cloud execution)
- **Quote**: (paraphrased; Amplitude engineers describe the local limitations without a single extractable quote)
- **Our assessment**: The "false plateau" framing is the most analytically useful concept in this source for the guide. It names a repeatable failure pattern: a team adopts local agents, sees initial gains, then hits a ceiling as concurrent agents compete for resources and lack full dev environments. The ceiling is not a model quality issue — it is an execution infrastructure issue. This directly corroborates `blog-cursor-self-hosted-cloud-agents.md` Claim 1 (enterprise blockers are infrastructure access, not model quality). Teams that plateau on local-only agents may misattribute the problem to tool capability rather than execution environment. The specific ceiling triggers (2–3 concurrent agents = resource competition; large codebase = memory limit; verification = no self-test capability) are actionable diagnostic criteria.

### Claim 5: 3x increase in weekly production commits since adopting cloud agents

- **Evidence**: Headline metric attributed to Amplitude's adoption of cloud agents. Cursor is now top-3 contributor by commit volume at Amplitude.
- **Confidence**: anecdotal (self-reported; no baseline definition; no time window specified; vendor-sourced; no cohort comparison)
- **Quote**: "Most AI coding tools give you more code. Cursor gives you more useful production software." — Curtis Liu (CTO)
- **Our assessment**: The 3x metric is the headline claim but the weakest evidentially. No baseline is defined: is this 3x over pre-AI adoption? Over local-only agent adoption? Over a subset of the team? No time window is given. The "production commits" definition is not specified — does this count only non-automated commits, or does it include Bugbot auto-merges? If 60–70% of PRs auto-merge via Bugbot, a significant portion of the 3x increase may be automated PRs rather than developer-produced code. The Curtis Liu quote correctly reframes the metric: production software that ships, not raw code volume, is the right measure. Apply `blog-faros-claude-code-roi.md`'s measurement framework — the 3x claim needs cohort comparison, baseline definition, and quality metrics to be load-bearing.

### Claim 6: "Garbage in, garbage out" — agents require clean codebase conventions; competing legacy patterns degrade agent output quality

- **Evidence**: Amplitude engineers explicitly note that agents struggle when the codebase has competing legacy patterns without clear conventions. The hourly cron CSS migration and React layout migration are specifically designed to clean up this technical debt to improve agent effectiveness.
- **Confidence**: anecdotal (single company's experience; logical consistency with context engineering principles)
- **Quote**: (described without a direct extractable quote; framing attributed to Amplitude engineers)
- **Our assessment**: This is the most practically useful negative pattern in the source. It reframes technical debt as an agent-autonomy prerequisite: a codebase with multiple competing patterns for the same problem (three CSS frameworks, two layout component libraries) confuses agent output, increasing false merges and incorrect migrations. The Amplitude team's response — running migration bots to normalize the codebase — is a concrete strategy: clean up the debt specifically to improve agent effectiveness, not for human readability. For the guide: code hygiene is not just a code quality concern; it is an agent-autonomy enabler. Teams that want high auto-merge rates need consistent conventions the agent can reliably follow.

### Claim 7: Cloud-first, local-for-iteration workflow split: new and exploratory work starts in cloud agents; engineers pull locally for controlled review

- **Evidence**: Named quote from Spencer Pauly explicitly describes the two-mode workflow.
- **Confidence**: emerging (named engineer; direct quote; operationally specific)
- **Quote**: "Cloud is where software is built, local is where we test and iterate." — Spencer Pauly
- **Our assessment**: This is the most quotable and portable concept from the source. It names a repeatable workflow split that teams can adopt: cloud agents for long-horizon autonomous work (new features, background migrations, customer bug triage); local Cursor for tight edit–test loops and fine-grained review. The split resolves the resource-conflict problem: cloud agents get dedicated VMs with full dev environments; local work gets the developer's full attention and judgment. For the guide: this is the operational answer to "when do I use cloud agents vs. local agents?" — scope and autonomy level, not task type.

### Claim 8: 1,000+ automated agent runs per week with no manual prompting is operational at Amplitude

- **Evidence**: Specific scale metric from Amplitude's deployment.
- **Confidence**: anecdotal (self-reported; vendor-sourced; no definition of "agent run")
- **Quote**: (attributed to Amplitude engineers)
- **Our assessment**: 1,000+ runs per week (~140/day) without manual prompting means the three trigger types — Slack events, hourly crons, and PR events (Bugbot) — collectively generate this volume. If Bugbot runs on every PR, this implies 1,000+ PRs per week through Bugbot alone. That volume is consistent with a 200–500 person engineering org. The "no manual prompting" qualifier is the key: these are fully autonomous trigger-driven runs, not engineer-initiated sessions.

### Claim 9: Amplitude aims to extend automation into CI/CD build validation and deployment to achieve end-to-end production deployment without developer intervention

- **Evidence**: Forward-looking statement from Amplitude engineers about planned automation extensions.
- **Confidence**: anecdotal (stated intentions; not yet implemented)
- **Quote**: (paraphrased; described as future plans)
- **Our assessment**: The trajectory from current state (triage + auto-merge + background migration) to planned state (CI/CD and deployment) maps the full adoption arc. Each step adds another phase of the SDLC to autonomous agent control. The current state (idea → PR → merge) is already deployed; the planned state (merge → build → deploy) extends automation downstream. For the guide: this is the clearest published roadmap of what "fully autonomous development pipeline" means in practice, from a named company that is actually executing toward it.

### Claim 10: Real velocity gains come from agents producing useful production software, not just code volume

- **Evidence**: Direct framing from Adam Lohner (Staff Software Engineer) contrasting code volume with production impact.
- **Confidence**: anecdotal (single practitioner's framing; consistent with `blog-faros-claude-code-roi.md` vanity-metrics critique)
- **Quote**: "Real accelerants to development velocity come when agents produce genuinely useful production software, not just lots of code." — Adam Lohner
- **Our assessment**: This is the most strategically aligned claim with the guide's measurement critique. It independently corroborates the Faros vanity-metrics warning (`blog-faros-claude-code-roi.md` Claim 5): lines of code and raw PR counts are the wrong metrics; production-shipped value is the right metric. From a practitioner at a company running 1,000+ automated runs per week, this framing carries operational weight — they have learned this through experience, not just reasoning about it in the abstract.

## Concrete Artifacts

### Slack→Linear→PR Bug Triage Pipeline

```
Amplitude autonomous bug triage workflow (Cursor blog, April 2026)

INPUT: Customer bug report posted to dedicated Slack channel

AGENT STEPS:
  1. Cloud agent monitors Slack channel for new reports
  2. Agent queries Linear: does a ticket for this bug already exist?
     ├─ YES → add context to existing ticket; no new PR
     └─ NO  → continue
  3. Agent explores codebase to identify root cause
  4. Agent opens Linear ticket describing the bug and planned fix
  5. Agent implements fix and opens PR with solution

OUTPUT: PR with fix implemented, Linear ticket created

RESULT: Customer-facing bug triage workstream fully delegated to agents;
        dedicated human triage role eliminated
```

### Risk-Stratified Auto-Merge (Bugbot)

```
Amplitude PR auto-merge flow via Bugbot (Cursor blog, April 2026)

INPUT: Every new PR opened at Amplitude

BUGBOT ASSESSMENT:
  ├─ LOW RISK  → PR auto-merges to production (60–70% of all PRs)
  └─ HIGH RISK → PR routed to appropriate human engineer for review

SCALE: 60–70% of Amplitude's production PRs merge without developer intervention

NOTE: Risk classification criteria not disclosed in source.
      See blog-cursor-bugbot-learning.md for Bugbot mechanism details.
```

### Hourly Cron Legacy Migration Automations

```
Amplitude background migration automations (Cursor blog, April 2026)

AUTOMATION 1: CSS → Tailwind migration
  Schedule: hourly cron
  Action:   scan CSS files → identify Tailwind-replaceable patterns
            → replace with Tailwind equivalents → delete old CSS files
            → open PR → notify via Slack
  Status:   ongoing background automation

AUTOMATION 2: React layout component migration
  Scope:    20,000+ legacy React layout component instances
  Action:   identify legacy component usage → migrate to current component
            → open PRs
  Status:   ongoing background automation

SHARED PROPERTIES:
  - Both run as cloud agents (dedicated VMs; full dev environment)
  - Both generate PRs for automated merge or review
  - Neither displaces developer time during business hours
```

### Amplitude Agent Workflow Metrics (self-reported, April 2026)

```
Metric                               Value          Confidence
-------------------------------------------------------------------
Weekly production commits increase   3x             anecdotal
PR auto-merge rate (low-risk)        60–70%         emerging
Automated agent runs/week            1,000+         anecdotal
Cursor contributor rank by commit    Top 3          anecdotal
React components in migration        20,000+        emerging
```

## Cross-References

- **Corroborates**: `blog-cursor-self-hosted-cloud-agents.md` — The "false plateau" claim (Claim 4) is the practitioner-side confirmation of that source's Claim 1 (enterprise blockers are infrastructure access, not model quality). Money Forward's in-progress PR-from-Slack workflow (described in that source) is the enterprise-equivalent of what Amplitude has fully deployed. Both sources converge on the same two-mode architecture: cloud for autonomous long-horizon work, local for developer-controlled iteration.

- **Corroborates**: `blog-cursor-bugbot-learning.md` — Amplitude's 60–70% auto-merge rate (Claim 2) is the first named-customer deployment rate for Bugbot. The mechanism described in `blog-cursor-bugbot-learning.md` (three-signal rule lifecycle, 78.13% resolution rate) provides the underlying engine explanation. Together: the mechanism note explains how Bugbot works; this note provides a real-world deployment percentage. The two are complementary, not duplicative.

- **Corroborates**: `blog-cursor-security-agents.md` — The Bugbot risk-routing pattern (Claim 2) is a generalization of the security-specific PR review pattern documented there. Both sources show Cursor's consistent design philosophy: route different risk levels to different handling paths rather than applying uniform human review to all PRs. This source extends the pattern from security-specific PRs to all PRs.

- **Extends**: `blog-cursor-self-hosted-cloud-agents.md` — That source covers the cloud agent infrastructure architecture; this source covers the workflow patterns built on top of that infrastructure. Infrastructure precedes patterns. Together they provide the full picture: what the cloud agent platform enables (that note) and what a team actually does with it (this note).

- **Tension with** `blog-bvp-shopify-ai-playbook.md` Claim 3: Shopify explicitly does not allow AI to merge code automatically ("Shopify is not yet at the place where we allow AI to check in code automatically"). Amplitude auto-merges 60–70% of PRs without developer review. This is not filed as a formal contradiction because both positions appear conditioned on organizational context: Shopify is a high-stakes e-commerce platform with financial transaction risk; Amplitude is an analytics SaaS. The guide should present both positions as points on a risk-tolerance spectrum — the key variable is not "allow auto-merge or not" but "what risk classification framework and codebase characteristics make auto-merge appropriate." Teams reading the guide need this spectrum presented explicitly. See Guide Impact for the recommended framing.

- **Complements**: `blog-faros-claude-code-roi.md` — The Faros measurement framework (cohort design, no vanity metrics) is the right lens through which to read Amplitude's 3x claim. The 3x figure lacks baseline definition, time window, and cohort comparison — it should not be cited as settled evidence without these qualifications. Adam Lohner's framing (Claim 10: production software, not code volume) independently corroborates Faros's vanity-metric critique.

- **Novel**: The following claims are not documented in any other source note:
  - **Slack→Linear→PR as a complete event-driven triage architecture**: No other source documents this specific three-step pipeline (monitor → deduplicate → implement) for customer-facing bug triage delegation. This is a concrete, reusable agent orchestration template.
  - **60–70% auto-merge rate as a named operational benchmark**: No other source provides a specific auto-merge percentage with named risk classification at a named company. This is the first concrete calibration point for "what does risk-stratified auto-merge look like in practice?"
  - **"False plateau" as a named failure pattern for local-only agent adoption**: No other source names this specific ceiling (local agents plateau; cloud agents break through). `blog-cursor-self-hosted-cloud-agents.md` describes the infrastructure reasons; this source names the symptom from the practitioner's perspective.
  - **Hourly cron as a named migration cadence**: No other source specifies the cron schedule for continuous background migration bots. The hourly cadence is an operational design choice that practitioners can adopt directly.
  - **Code hygiene as agent-autonomy prerequisite**: No other source explicitly states that competing legacy patterns degrade agent output quality. The "garbage in, garbage out" framing names this dependency and provides the response (run migration bots to normalize the codebase before relying on agents for autonomous work).

## Guide Impact

- **Chapter 01 (Daily Workflows)**: The cloud-vs-local split (Claim 7 — "Cloud is where software is built, local is where we test and iterate") is the cleanest practitioner answer to "when should I use cloud agents vs. local agents?" Add as a named operational pattern alongside the interactive-vs-background agent distinction. The Slack→Linear→PR pipeline is a concrete template for event-driven triage; any team receiving high-volume customer bug reports in Slack can adopt it.

- **Chapter 02 (Harness Engineering)**: The hourly cron migration automation (Claim 3) belongs in any section on background automation patterns. Extract the three-component structure: trigger (hourly schedule), action (scan → transform → PR), and notification (Slack). The CSS→Tailwind and React component migrations are concrete examples of "well-defined mechanical transformation" tasks suited to background agents. The code hygiene prerequisite (Claim 6) should appear in any discussion of agent autonomy requirements: before deploying autonomous agents, normalize codebase conventions.

- **Chapter 03 (Safety and Verification)**: The risk-stratified auto-merge (Claim 2) is the most concrete published example of "how do you safely give agents merge authority?" Add the Amplitude 60–70% rate as the current calibration benchmark from a named practitioner. Pair with the Shopify counter-position (`blog-bvp-shopify-ai-playbook.md` Claim 3) to present the full spectrum: high-stakes platforms may prohibit autonomous merges; lower-blast-radius SaaS may auto-merge the majority of PRs. The decision variable is risk profile, not tool capability.

- **Chapter 05 (Team Adoption)**: The "false plateau" pattern (Claim 4) belongs in any discussion of adoption failure modes. Teams that plateau on local-only agents may misdiagnose the problem as tool inadequacy when the real constraint is execution infrastructure. The diagnostic criteria (2–3 concurrent agents = resource competition; large codebase = memory ceiling; verification = no self-test) give teams a concrete checklist for identifying whether they have hit the ceiling. The 3x metric (Claim 5) should be presented with measurement caveats (no baseline definition, no cohort comparison) and paired with `blog-faros-claude-code-roi.md`'s framework for what a credible productivity claim requires.

## Extraction Notes

- Source is published on Cursor's blog and is clearly marketing-framed: no failure modes, no discussion of what went wrong, CTA at end. The named engineers (Curtis Liu, Adam Lohner, Spencer Pauly) and specific technical details (hourly cron schedules, Linear integration logic, PR auto-merge rates) are credible as practitioner evidence, but all claims should be treated as `confidence: emerging` and vendor-sourced framing noted.
- The 3x production commit increase (Claim 5) is the weakest claim evidentially. No baseline, no time window, no definition of "production commits." If Bugbot auto-merges 60–70% of PRs, a significant portion of the 3x may be automated PRs, not developer-produced code. Do not cite as settled evidence.
- The Bugbot auto-merge rate (60–70%) is the most operationally significant claim and also lacks the risk-classification criteria needed to replicate it. Miner recommends follow-up extraction of the Bugbot Autofix companion post (Feb 2026) and any Amplitude-specific Cursor Automations documentation to fill this gap.
- The "false plateau" pattern (Claim 4) is the highest-novelty concept in the source for practitioners at early adoption stages. It names an experience that many teams will recognize but have not seen labeled.
- Full blog post was read in its entirety. No sub-pages linked. The Cursor Automations marketplace templates referenced in related sources (`blog-cursor-security-agents.md`) were not fetched for this extraction — they would provide implementation artifacts for the cron and triage automation patterns.
