---
source_url: https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day
source_type: blog-post
title: "How an Anthropic Japan BDR runs his day with a fleet of Claude agents"
author: Shahboz Ibragimov (Business Development Representative, Anthropic Japan)
date_published: 2026-10-16
date_extracted: 2026-10-17
last_checked: 2026-10-17
status: current
confidence_overall: anecdotal
issue: "#4175"
---

# How an Anthropic Japan BDR runs his day with a fleet of Claude agents

> A first-party, non-developer operator case study of a six-agent "Nakama" fleet on Claude Managed Agents — one job per agent, a coordinator agent that edits the others' instructions, a shared memory store fed by draft-vs-sent diffs, per-role model tiering (plus an advisor pattern), and a Claude Tag handoff with self-set reminders — extending the Cowork-era BDR note to the Managed Agents stage.

## Source Context

- **Type**: blog-post (first-party Anthropic practitioner case study, claude.com/resources/articles; category "Best practices", product "Claude Managed Agents"; 14-minute read)
- **Author credibility**: Bylined to Shahboz Ibragimov, a BDR on Anthropic's Japan team, describing his own workflow on his employer's product. Credible on how the fleet is structured; the outcome figure is self-measured, and the post is vendor-published and promotional in intent ("Get started with Claude Managed Agents").
- **Scope**: Covers fleet design (six agents), prototyping in Claude, migration to Managed Agents (schedules, memory store, vaults), Claude Tag handoff, efficiency/model-tiering, and lessons. It does not give prompts, config files, code, cost figures, or quality metrics for drafts.

## Extracted Claims

### Claim 1: Split one workflow into single-responsibility agents, each with one clear job
- **Evidence**: Description of five working agents — Furiwake (routes inbound leads to reps, posts a report to a Slack channel), Sabaki (qualifies/categorizes leads, updates Salesforce, drafts first-touch email), Henji (hourly inbox scan, drafts JA/EN replies), Shoudan (pushes customer-interaction updates into Salesforce), Nokori (end-of-day: reads calendar and meeting transcripts, summarizes, drafts follow-ups) — plus a sixth coordinator.
- **Confidence**: anecdotal
- **Quote**: "A single responsibility keeps each one easy to reason about and easy to track, especially when something is off."
- **Our assessment**: Matches the guide's one-agent-one-job thinking, with a concrete non-coding decomposition. No comparison against a single-agent baseline, so the benefit is asserted, not measured.

### Claim 2: A coordinator agent applies plain-language change requests to the other agents' instructions and the shared knowledge base, gated to a single authorized requester
- **Evidence**: The operator posts requests in a dedicated Slack channel; the coordinator polls about every 15 minutes and edits instructions/system prompts. It also ingests a Claude-posted morning brief of product/pricing updates and writes changes into the knowledge base.
- **Confidence**: anecdotal
- **Quote**: "Only I can post requests for changes to agents’ instructions and system prompts."
- **Our assessment**: Novel "meta-agent" pattern. The access restriction is the key safety control; the author separately notes that a bad coordinator edit "would reach every agent" (Claim 8). Worth flagging as a blast-radius concern (Ch06); the post describes no review gate beyond versioning.

### Claim 3: Prototype with skill + scheduled task + shared folder, then migrate to Managed Agents when the fleet outgrows manual tracking
- **Evidence**: Mapping given: skill → system prompt, scheduled task → deployment schedule, shared folder → memory store. Motivation: the same skill was edited from many chats and sharing meant a zip file.
- **Confidence**: anecdotal
- **Quote**: "I'd suggest starting in Claude and moving your agents to Managed Agents once you have more than you can comfortably keep track of."
- **Our assessment**: Useful staged-adoption rule with an explicit trigger (loss of overview), and a clean concept mapping. Practical for Ch05.

### Claim 4: Versioned instructions plus a deployed-version pin let the operator experiment without breaking scheduled runs
- **Evidence**: Each instruction change is saved as a new numbered version; scheduled runs keep using the deployed version while edits are in progress; each run's steps are inspectable in the Console.
- **Confidence**: anecdotal
- **Quote**: "while I'm trying out a change to an agent, the scheduled runs keep using the version that’s deployed, so a half-finished edit doesn't end up in tomorrow's run."
- **Our assessment**: Consistent with the staging/versioning in the sales-inbound note. A solid, low-effort safeguard for unattended agents.

### Claim 5: A shared memory store that captures draft-vs-sent diffs lets a correction made once propagate to every agent
- **Evidence**: Agents compare drafts with sent emails, save each difference as a phrasing note, and also store facts found while researching from internal docs and official sites. Author reports "a few hundred cheap rounds" to reach his voice.
- **Confidence**: anecdotal
- **Quote**: "I fix a phrasing once in Henji's drafts, and Sabaki and Nokori stop making the same mistake."
- **Our assessment**: Strongest new idea: the human's edit is the training signal and the memory is shared across roles. Extends the Cowork-era "write corrections back into the skill" (Albert, Claim 8) from per-skill instructions to a cross-agent store. No measurement of drift or stale/contradictory notes.

### Claim 6: The knowledge base matters more than the prompt
- **Evidence**: Corrections and past interactions are stored where agents can read and write; context is pulled from there instead of from a longer prompt.
- **Confidence**: anecdotal
- **Quote**: "The knowledge base matters more than the prompt."
- **Our assessment**: Aligns with the "less is more" prompt advice in the sales-inbound note (Claim 10) and the "knowledge base before workflows" advice in Albert (Claim 9). Single-practitioner assertion, but convergent across three Anthropic internal teams.

### Claim 7: Tier models by role: Sonnet for rulebook-following agents, Opus for judgment-heavy ones, and use the advisor strategy for high-frequency judgment work
- **Evidence**: Furiwake and Shoudan on Sonnet; Sabaki, Nokori and the coordinator on Opus; Henji (most frequent, needs judgment) runs on Sonnet and escalates hard decisions to an Opus advisor that "sends back a plan, a correction, or a stop signal". Effort level is set per agent separately from model, raised only for hard reasoning.
- **Confidence**: anecdotal
- **Quote**: "Running it on Opus every time would be the most expensive option, so I use the advisor strategy (opens in new tab) in Managed Agents"
- **Our assessment**: Concrete, reusable decision rule (rulebook-bound → small model; judgment/blast radius → large model; frequent + judgmental → small model + advisor). No cost or quality numbers, so the economics are unverified.

### Claim 8: The coordinator gets the largest model because one bad edit would reach every agent
- **Evidence**: Explicit reasoning for assigning Opus to the agent that edits other agents' instructions.
- **Confidence**: anecdotal
- **Quote**: "The coordinator needs it most, since it edits the other agents' instructions and one bad edit would reach every agent."
- **Our assessment**: Good heuristic: allocate capability by blast radius, not just task difficulty. Not backed by an incident or eval.

### Claim 9: Scheduled agents compound waste, so design for efficiency: update rather than append to instructions, limit context, and don't default to the biggest model and effort
- **Evidence**: Lists the "most common mistakes" and ties efficiency to design (one job each, wake-do-stop schedule, shared memory).
- **Confidence**: anecdotal
- **Quote**: "Scheduled agents run every day whether I'm watching or not, so waste can add up, in cost and reliability."
- **Our assessment**: Sensible but unquantified. "Updating instead of appending" instructions is a specific, testable hygiene rule that complements the instruction-bloat theme.

### Claim 10: Managed Agents moved scheduling and secrets off the operator's laptop: background runs, cadence/timezone in the Console, per-agent scoped vaults
- **Evidence**: Agents run when the laptop is offline; each deployment uses only the vaults its job needs, never sees the credentials, and access can be revoked in one step.
- **Confidence**: anecdotal
- **Quote**: "Each agent’s deployment uses only the vaults its job needs, it never sees the credentials, and I can revoke access in one step."
- **Our assessment**: Operator-level confirmation of the vault and scheduling features documented in the platform notes; adds the least-privilege-per-agent framing for non-developers.

### Claim 11: Agents hand off out-of-routine items to Claude Tag in Slack, which sets reminders for itself to check back
- **Evidence**: An agent posts the action item to the Nakama channel and tags Claude; Claude checks rules/terms, lays out options, drafts, tags the human for review/sign-off, and sets a self-reminder when waiting on a customer or another team; on due date it checks and reports status in-thread.
- **Confidence**: anecdotal
- **Quote**: "When a customer or another team needs to reply first, Claude sets a reminder for itself to check back on a set day."
- **Our assessment**: Shows agent-to-agent handoff through a human-visible channel (auditable by design). Extends the Claude Tag note's scheduled-routine examples with a follow-up/wait loop.

### Claim 12: Humans stay in the loop through a written rulebook and summary-first drafts
- **Evidence**: A rulebook defines each agent's lane; pricing questions, sensitive accounts, and ambiguous asks route to the human; each draft starts with a short context summary; the human reads, confirms, revises, sends.
- **Confidence**: anecdotal
- **Quote**: "A written rulebook defines each agent's lane and items like pricing questions, sensitive accounts, or ambiguous asks route to me."
- **Our assessment**: Human stays the sender and judgment gate; no autonomous customer sends. Consistent with "keep a human on every send" in Albert.

### Claim 13: Claimed saving of about 60 hours per week (self-measured)
- **Evidence**: The author counts each task in the weekly log at the time it would have taken manually.
- **Confidence**: anecdotal
- **Quote**: "the fleet saves me around 60 hours of work."
- **Our assessment**: Not credible as a rigorous number: it exceeds a normal work week, counts avoided effort rather than measured time, and has no review-time offset. Record only as anecdote; do not cite as an effect size.

### Claim 14: Letting go of manual maintenance worked better than expected — give the agents more room sooner
- **Evidence**: Author initially hand-edited the knowledge base and agent instructions, then delegated both to agents/coordinator.
- **Confidence**: anecdotal
- **Quote**: "I had been too cautious with work I could trust the agents to do."
- **Our assessment**: A single-person trust calibration, in a low-to-medium stakes domain with a human sending every email. It should not be generalized to higher-stakes writes (e.g., Salesforce edits are done autonomously here — no verification described).

## Concrete Artifacts

```
Nakama fleet (Shahboz Ibragimov, Anthropic blog, 2026-10-16)
Agent       Job                                              Model (per post)
Furiwake    route daily inbound queue to reps, Slack report  Sonnet
Sabaki      qualify/categorize my leads, Salesforce, 1st email  Opus
Henji       hourly inbox scan, JA/EN reply drafts            Sonnet + Opus advisor
Shoudan     push interactions into Salesforce opportunities  Sonnet
Nokori      end-of-day: transcripts -> summaries, follow-ups Opus
Coordinator edits agent instructions + knowledge base        Opus
            (polls Slack channel ~every 15 min; only the operator may request changes)
```

```
Prototype -> Managed Agents mapping (paraphrased table from the post's text)
skill                 -> agent system prompt (versioned)
scheduled task        -> schedule on the agent's deployment (cadence + timezone in Console)
shared laptop folder  -> memory store (shared read/write by all agents)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-albert-cowork-bd-scale.md` Claim 8 (write corrections back so the skill doesn't repeat mistakes), Claim 9 (build the knowledge base before workflows; human on every send).
  - `blog-anthropic-sales-inbound-buying-agent-managed-agents.md` Claim 8 (agent versioning makes iteration cheap and reversible) and Claim 10 ("less is more" prompts; knowledge over procedure).
  - `blog-claude-dev-building-effective-agent-automations.md` Claim 9 (scoped credentials in a vault) and Claim 7 (separate human-edited preferences from agent-owned state); this post instead uses one shared read/write store with a coordinator-gated human channel.
- **Contradicts**: None filed. Tension worth noting (not a contradiction): the building-effective-automations note's Claim 7 separates a read-only human-edited preferences store from a read-write agent state store, whereas Nakama uses a single store every agent reads and writes, and lets a coordinator edit instructions. Different risk postures, not opposed claims on the same question.
- **Extends**:
  - `blog-anthropic-albert-cowork-bd-scale.md`: the same BDR role in the Cowork era (single skills + hourly inbox skill); this post is the multi-agent, Managed Agents successor.
  - `blog-anthropic-claude-managed-agents-memory.md` Claim 5 (stores shared across agents) and Claim 6 (concurrent agents on one store): a real-world use with draft-vs-sent diffs.
  - `blog-anthropic-managed-agents-scheduled-vaults.md` Claim 1 (scheduled deployments): operator-level usage.
  - `blog-anthropic-claude-tag-employee-workflows.md` Claim 10 (scheduled routine by Claude) — here, self-set reminders and agent-initiated tags.
- **Novel**: The coordinator/meta-agent that edits other agents' instructions via a gated chat channel; draft-vs-sent diff as a cross-agent memory signal; model tiering by role with the advisor strategy for frequent judgment work; prototype-then-migrate mapping; agent-to-Claude-Tag handoff.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a non-coding multi-agent example of single-responsibility decomposition and a model-tiering rule (rulebook-bound → smaller model; judgment/high blast radius → larger model; frequent-and-judgmental → small model + advisor), citing this note's Claims 1, 7, 8. Mention the coordinator pattern together with the caveat that an instruction-editing agent needs restricted requesters and versioning.
- **Chapter 04 (Context Engineering)**: Add the draft-vs-sent diff loop as a shared-memory pattern (Claim 5), and "knowledge base over longer prompt" (Claim 6) with the caveat that no staleness/conflict handling is described.
- **Chapter 05 (Team Adoption)**: Add the prototype-in-Claude, migrate-when-unmanageable path (Claim 3) and the non-developer-operator evidence; treat the 60-hour figure as anecdote only.
- **Chapter 06 (Security Threat Model)**: Note the coordinator as a single point of blast radius, mitigated here by sender restriction and versioning (Claims 2, 4, 8); per-agent vault scoping (Claim 10).

## Extraction Notes

- Read the full article via direct HTML fetch (all body text; no sub-pages followed — links point to Managed Agents docs, memory, vaults, Claude Tag, advisor strategy pages, and related articles, which are covered by existing notes). The Claude Tag Slack thread screenshot is an image and not extracted.
- All quotes were copied from the fetched page text. Quotes in Claims 4, 5, and 10 contain curly apostrophes as in the source.
- Triage comments suggested extending existing notes; a new note was written because the fleet decomposition, coordinator, and tiering material doesn't fit any existing note's scope. The cross-reference claim numbers above were checked against each cited note's heading list.
- Article is vendor-published and promotional in intent; all outcome evidence is self-reported.
