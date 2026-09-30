---
source_url: https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
source_type: blog-post
title: "Agents you can coach: how Asana builds human-agent teams with Claude"
author: Arnab Bose (Asana CPO), interviewed by Anthropic staff (bylines Aleksandra Todorova, Kristen Swanson)
date_published: 2026-09-29
date_extracted: 2026-09-30
last_checked: 2026-09-30
status: current
confidence_overall: anecdotal
issue: "#3802"
---

# Agents you can coach: how Asana builds human-agent teams with Claude

> Third post in Anthropic's human-agent-teams series: Asana runs agents as teammates inside its existing Work Graph, with role-scoped profiles, access bounded by the triggering user's permissions, a split between using an agent and training it (only admins/editors write permanent memory), and agent work posted visibly on shared tasks.

## Source Context

- **Type**: blog-post (claude.com blog, Sep 29, 2026; customer interview format, "Agents" category, Claude Platform product)
- **Author credibility**: Arnab Bose is Asana's Chief Product Officer and speaks about Asana's internal use and its product design. The post is published by Anthropic and is a vendor-hosted customer story: no metrics, no failure cases, and product claims are not independently verifiable. Treat as a practitioner description of design intent, not measured results.
- **Scope**: Covers Asana's agent ("AI teammate") model: roles, profile pages, access scoping, shared memory with role-based write permissions, visible work on tasks, and three internal use cases (product Q&A from Slack, at-risk renewal digest, engineering cycle planning in Command). Does NOT cover: implementation details (prompts, skill formats, memory storage), evaluation, cost, or incidents.

## Extracted Claims

### Claim 1: Asana put agents inside its existing structured work model rather than creating new context structures for AI
- **Evidence**: Description of Work Graph (tasks, projects, goals, conversations with owners, contributors, dependencies); agents get roles, assigned tasks, messages, and appear in activity feeds. No metrics.
- **Confidence**: anecdotal
- **Quote**: "When they started building AI agents, they decided that rather than adding new context structures for AI, agents would operate within this same model."
- **Our assessment**: Plausible and consistent with the Slack post's theme (agents need context humans already maintain). It depends on a company already having a rigorous work-tracking substrate, which most teams do not; generalizable takeaway is "reuse the human coordination surface."

### Claim 2: Human-side sensemaking should be structured before agents act on it (think with Claude, then log actionable items to the work system)
- **Evidence**: Bose's description of how employees turn unstructured inputs (Slack, Zoom, Databricks, Docs) into projects/tasks via Claude; three-step "how to put this into practice" list.
- **Confidence**: anecdotal
- **Quote**: "Log the actionable items to the Work Graph. Move what's actionable into projects and tasks, where agents and colleagues can pick it up."
- **Our assessment**: A workflow recommendation rather than a tested result. Useful as a description of the human-in-front-of-agent step; analogous to writing a spec/ticket before handing to a coding agent.

### Claim 3: Agents are defined by role (type of work) with pre-built skills and integrations, and each has a profile page listing purpose, users, admins, instructions, skills, integrations, permissions
- **Evidence**: Role examples (content writer, insights analyst, project manager, work intake specialist, campaign analyst, campaign coordinator); profile-page field list.
- **Confidence**: anecdotal
- **Quote**: "Each agent also has a profile page that lists its name and purpose, the people who can use it, the administrators, instructions, skills, integrations, and permissions."
- **Our assessment**: Concrete, copyable schema for an "agent manifest". Mirrors the roster idea in the earlier series post but adds an explicit user-vs-admin split on the manifest.

### Claim 4: An agent's effective access is bounded by the permissions of the person who triggers it
- **Evidence**: Stated design of Asana's permission model; rationale is letting agents have broad public-content access while limiting leakage of what they learned in a private context.
- **Confidence**: anecdotal
- **Quote**: "Asana says an agent’s effective access is bounded by the permissions of the person who triggers it."
- **Our assessment**: Important governance pattern (confused-deputy mitigation via caller-scoped permissions). The post does not discuss residual risk: memory committed from a privileged session could still surface content to less-privileged triggerers unless memory writes are also scoped. Needs corroboration from Asana docs.

### Claim 5: Working with an agent should be separated from training it — anyone can give task feedback, but only admins and editors can commit to, undo, or delete permanent memory
- **Evidence**: Description of Asana's shared-memory rule; example of comms team owning the writing agent while the CPO can draft with it but not change its behavior.
- **Confidence**: anecdotal
- **Quote**: "While anyone can give an agent feedback on a task, only admins and editors can commit feedback to permanent memory, as well as undo, or delete from that memory."
- **Our assessment**: The most novel claim for our corpus: a write-permission model on shared agent memory (ephemeral per-task feedback vs. curated permanent memory). Directly addresses memory poisoning/drift by ordinary users. Untested at scale in the post.

### Claim 6: Memory ownership should map to domain expertise; one or two experts set agents up so everyone else benefits
- **Evidence**: Bose quote and the "Match editors to expertise" guidance; comms team as editors of the writing agent.
- **Confidence**: anecdotal
- **Quote**: "Not everybody on the team needs to understand these concepts, like skills and behavior and memory."
- **Our assessment**: Organizational pattern (agent "owner" = owner of the standard being applied). Fits a champion/steward model for team adoption; no evidence on how well it holds up when experts leave or disagree.

### Claim 7: Agent work on shared tasks should be visible: the agent posts its plan and steps, and reviewers can comment and steer it
- **Evidence**: Asana's behavior for tasks assigned to AI teammates; example of Bose @-mentioning the agent on a briefing-doc task while a colleague watches and interjects.
- **Confidence**: anecdotal
- **Quote**: "The agent posts activity, including its research plan and the steps it took, so everyone with access to that task can read what it did, comment, and steer it toward the result they want."
- **Our assessment**: Good argument that shared, inspectable threads beat private 1:1 agent chats for review. Overlaps with the Slack post's public-by-default channels. Claim is a product behavior, not validated quality uplift.

### Claim 8: One-on-one agent use hides the prompt and back-and-forth, making reviewer disagreement about guidance hard to resolve
- **Evidence**: Bose's reasoning; no data.
- **Confidence**: anecdotal
- **Quote**: "But at that point, the other human beings who are reviewing that content don't know what the prompt was and what the back-and-forth was."
- **Our assessment**: Reasonable, and a useful argument for prompt/transcript provenance on reviewed artifacts (applicable to AI-authored PRs too). Opinion, not measured.

### Claim 9: Agents can turn a high-volume Slack Q&A channel into triaged tasks, with escalation to product intake and enablement when answers are missing or repeated
- **Evidence**: Described workflow: Asana app converts each question to a task; agent replies with source links if approved guidance exists, otherwise creates a product intake task, and creates an enablement task on repeated questions. No volume or accuracy numbers.
- **Confidence**: anecdotal
- **Quote**: "If approved guidance exists, the agent replies with source links."
- **Our assessment**: Concrete example of an agent with three bounded outcomes (answer / escalate to product / escalate to enablement) and a feedback loop into documentation. Note "approved guidance" gating: the agent only answers from curated answers.

### Claim 10: A daily agent-generated digest in a shared space improves over time as leaders coach it
- **Evidence**: At-Risk Renewal agent reads every at-risk renewal task, produces a digest in three buckets (positive momentum, negative momentum, recommended follow-ups), global then by region, pushed each morning to CCO, CRO and regional leaders. No outcome metrics.
- **Confidence**: anecdotal
- **Quote**: "They could probably have Claude generate a report for themselves,"
- **Our assessment**: The point is standardization plus shared workspace plus compounding memory versus personal one-off reports. Plausible, unquantified; the claim that the report "improves each morning" is asserted, not measured.

### Claim 11: Automated coding loops (feedback to synthesis to PRs) bloated Asana's cycles; the bottleneck moved to planning and decision-making, so humans gate what moves from the agent-filled unplanned board into the cycle
- **Evidence**: Asana's own experience described in the Command section: cycle times and releases slipped; agents populate the unplanned board; people decide what enters the cycle; Command gives optimistic/balanced/conservative completion estimates. No numbers on slippage.
- **Confidence**: anecdotal
- **Quote**: "Code generation is now no longer the bottleneck,"
- **Our assessment**: A mild failure report embedded in a product story: unthrottled agent-generated changes degrade delivery cadence. Valuable as a counterpoint to "more agent output is better", but vendor-interested (promotes Command) and quantification is absent.

### Claim 12: Agents need distinct identities so contributions and access can be audited, and a durable record of what agents learn so team knowledge compounds
- **Evidence**: Bose's closing statement; no implementation detail.
- **Confidence**: anecdotal
- **Quote**: "with a distinct identity for every agent so its contributions and access can be audited, and a durable record of what agents can learn so the team’s knowledge compounds instead of evaporating."
- **Our assessment**: Summarizes the design principles (identity, audit, durable memory). Consistent with the three capabilities in the first series post.

## Concrete Artifacts

Agent profile page fields (source: "Give every agent a role and the tools and access it needs" section):

```
name, purpose, people who can use it, administrators,
instructions, skills, integrations, permissions
```

Example agent roles (same section): content writer, insights analyst, project manager, work intake specialist, campaign analyst, campaign coordinator.

Memory write policy (source: "Separate working with an agent from training it" section, paraphrased from the post):

```
Anyone:            feedback applies to the current task only
Admins / editors:  can commit feedback to permanent memory, undo it, or delete it
```

At-Risk Renewal digest structure (source: "Briefing executives on at-risk renewals" section, paraphrased): three buckets (positive momentum, negative momentum, recommended follow-ups); global view first, then by region; pushed each morning to the Chief Customer Officer, Chief Revenue Officer, and regional customer success leaders.

"How to put this into practice" checklists (paraphrased): (1) bring unstructured inputs to Claude, debate, log actionables; (2) define the role before creating the agent, scope access, name users and admins separately; (3) decide who trains vs. works with each agent, match editors to expertise, build memory as you work; (4) bring agents in where teams review work, make agent work visibly agent work, let reviewers coach.

## Cross-References

- **Corroborates**:
  - `blog-anthropic-human-agent-teams.md` Claim 2 (persistent memory, independent credentials, broad information access) — this post cites that framework and adds an implementation: distinct agent identity, durable memory, shared context. Claim 5 (explicit rosters of roles) matches Asana's role-based agents and profile pages.
  - `blog-anthropic-slack-cpo-human-agent-teams.md` Claim 1 (public-by-default channels so agents build context) and Claim 3 (handoff cycle: agents produce, human reviews) — Asana's visible tasks and human review of agent output are the same pattern on a task system.
  - `blog-anthropic-claude-managed-agents-memory.md` Claim 5 (memory stores shared across agents with differing access scopes) — same idea of scoped memory write access; Asana implements it by user role rather than store.
- **Contradicts**: None found. The Claim 4 caller-bounded-permissions design and the Claim 5 admin-only memory writes are compatible with existing notes; no material opposition, so no contradiction issue filed.
- **Extends**:
  - `blog-anthropic-human-agent-teams.md` Claim 9 (autonomy proportional to demonstrated reliability) — adds a separation of who may change agent behavior (editors/admins) from who may use it.
  - `blog-openai-asana-codex-case-study.md` Claim 3 (Asana engineering uses review-and-approve workflow for agent changes as standing practice) — this post covers Asana's non-migration, team-level agent architecture and its Command note that agent-generated changes bloated cycles, which complements that note's single-project view. Different vendor (Claude vs Codex) and different subject.
- **Novel**: (a) write-permissioned shared agent memory (task-scoped feedback vs. admin/editor-committed permanent memory); (b) agent effective access bounded by the triggering user's permissions; (c) agent profile page with separate user and admin lists; (d) embedded report that unthrottled agent-generated coding changes slowed cycles and that planning became the bottleneck.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the caller-bounded-permissions pattern (Claim 4) and the task-only vs. permanent-memory write split (Claim 5) as design options for shared agent memory, flagged as a single vendor-reported, unmeasured practice.
- **Chapter 03 (Agent Patterns)**: Cite the role-plus-profile manifest (Claim 3; Concrete Artifacts) as a template for scoping persistent agents; cite the Slack Q&A agent (Claim 9) as a worked example of answer / escalate / feed-back-to-docs outcomes.
- **Chapter 05 (Team Adoption)**: Add the steward model (Claim 6): domain owners of a standard own the agent that applies it, everyone else gives task-level feedback; pair with visible-agent-work guidance (Claims 7-8). Cite Claim 11 as a caution that agent throughput needs a human gate at planning, not just at review.

## Extraction Notes

- Read the full post via direct HTML fetch (no paywall). It is about a 5 minute read. It links to two earlier posts in the series (the first is already in our corpus as `blog-anthropic-human-agent-teams.md`; the second as `blog-anthropic-slack-cpo-human-agent-teams.md`), so I did not re-fetch them.
- Quotes copied from the page text; two contain typographic apostrophes exactly as in the source. Quote for Claim 10 and 11 are truncated fragments ending at a comma, as they appear in the source mid-sentence.
- Source is thin on evidence: no quantitative results, no failure modes, no security analysis. Hence `confidence_overall: anecdotal`.
- Did not edit `registry/sources.json` (derived index).
