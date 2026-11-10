---
source_url: https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/
source_type: blog-post
title: "Safely scaling multi-agent teams with Claude Fable 5.2"
author: Barry Zhang, Tianyi Peng, Elle Najt, Keller Scholl, Lance Martin (Anthropic)
date_published: 2026-11-09
date_extracted: 2026-11-10
last_checked: 2026-11-10
status: current
confidence_overall: emerging
issue: "#4618"
---

# Safely scaling multi-agent teams with Claude Fable 5.2

> First-party description of a 1,000-agent run (one lead, 999 helpers) that formalized Fermat's Last Theorem in Lean using only general tools (sandbox shell, Git, shared Postgres), plus the layered sandbox and CoT-aware monitoring design that made the run safe enough to attempt.

## Source Context

- **Type**: blog-post (Anthropic, Agents section, Nov 9 2026)
- **Author credibility**: Five Anthropic authors describing their own experiment. First-party and detailed, but a single run with an early model version; the post itself calls it a "toy experiment" per our fetch summary. No independent replication.
- **Scope**: Harness (tools, collaboration, prompting), safety (sandboxing, real-time and offline monitoring), run timeline and conclusions. Does not give the monitor's prompt, red-team eval counts, or false-positive rates.

## Extracted Claims

### Claim 1: A shared SQL database plus Git was enough for 1,000 agents to coordinate without a purpose-built platform
- **Evidence**: Single run; the lead created five tables (Announce, Assign, Notes, Subtasks, Landed) in the first 10 minutes; 16-17 helpers per statement with a captain per crew; task tree of 2,418 tasks up to 10 levels deep; final theorem proved at hour 28.7.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Strong existence proof for the "shared state" pattern at large scale. The agent-designed schema is notable. N=1, vendor-run, and the authors concede domain platforms (Prove2Me) may be more efficient.

### Claim 2: A single shared machine failed at about 100 agents; per-agent lightweight VMs removed the ceiling
- **Evidence**: Stated measurement from the post's Collaboration section.
- **Confidence**: emerging
- **Quote**: "A single shared machine hit its limits at about 100 agents: more than half of our 100-agent runs had to be stopped or restarted because memory, disk, or CPU ran out."
- **Our assessment**: Practical sizing datum: agent count is bounded by sandbox resources before coordination logic. Applies to local multi-agent setups too.

### Claim 3: A prompted LLM classifier can gate every tool call in real time, and across >1M tool calls none met the block bar
- **Evidence**: Run statistic; one root-access check "came close" per the post.
- **Confidence**: emerging
- **Quote**: "To make runs like this safer, we use a prompted LLM classifier that can block each tool call, including shell commands and file edits."
- **Our assessment**: Zero blocks is consistent with a benign task but says little about detection quality; the red-team evals (Claim 4) are the real evidence.

### Claim 4: Monitors that see chain of thought and inter-agent communication detected all sabotage attempts in red-team evals
- **Evidence**: Multi-agent side-task and sabotage evaluations where red-team agents used decomposition attacks to try to obtain a sandbox escape. No sample sizes given.
- **Confidence**: emerging
- **Quote**: "We found that monitors that viewed the agents’ chain of thought (CoT) and interagent communication were able to detect all sabotage attempts in these evaluations, so we now use them to monitor our multi-agent runs."
- **Our assessment**: Important and plausible, but "all" with undisclosed eval size is weak. Decomposition attacks are specifically multi-agent, so per-agent action review alone is likely insufficient.

### Claim 5: An action-only monitor is run in parallel to guard against reasoning persuading the monitor, and this run used only that one
- **Evidence**: Design statement plus an explicit caveat.
- **Confidence**: emerging
- **Quote**: "In parallel, we run an action-based version of the same monitor—which sees only actions, not CoT—to guard against an agent’s reasoning persuading the monitor to permit a harmful action."
- **Our assessment**: Caveat quote: "In the run in this post, we used only the action-based monitor." So the headline run was NOT covered by the CoT-aware monitor; the zero-blocks result applies to the weaker one.

### Claim 6: An offline monitor with extra affordances reviews team behavior against the same threat models
- **Evidence**: Design description only.
- **Confidence**: emerging
- **Quote**: "This monitor analyzes the agent team’s actions against the same threat models as the real-time monitor, but with additional affordances, such as being able to look up actions from other agents."
- **Our assessment**: Cross-agent lookup is what makes decomposition attacks detectable after the fact. Cheap pattern to copy: post-hoc review with wider context than real-time.

### Claim 7: Layered sandboxing: no network except a pipe to an identity-tagging gateway, own-branch push only, unprivileged DB role with limits
- **Evidence**: Enumerated controls: agents coordinate only via DB and Git; push only to own branch with a separate job merging to main; shared unprivileged DB role, 5 s per-statement limit, writes refused above 256 MiB; gateway tags requests with agent identity; kernels lacking root-enabling features, in lockdown mode; agents run unprivileged and cannot read or change the agent loop.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Concrete, copyable checklist. Gateway-tagged identity aligns with the identity/audit model in our existing note.

### Claim 8: Block semantics are team-level; a lead block stops the run, a helper block removes only that helper
- **Evidence**: Two statements in the post. One: "When the classifier blocks a tool call, the whole agent team stops and a person must review the block before the team can restart." Elsewhere: "Only a block on the lead would have ended the run; a block on a helper removed just that helper."
- **Confidence**: emerging
- **Quote**: "When the classifier blocks a tool call, the whole agent team stops and a person must review the block before the team can restart."
- **Our assessment**: The post is internally inconsistent about whether any block halts the team or only a lead block does, and does not reconcile them. Treat the policy as unclear; the design question (blast radius of a block) is still valuable.

### Claim 9: Agents misjudge difficulty and give up early; the lead reallocating helpers rescued the run
- **Evidence**: Helpers judged 47 of 60 statements infeasible, yet most were proved; at ~27 min the lead shelved 47 and focused on 10, all proved in ~70 min; at ~hour 18 only Langlands-Tunnell remained (captain estimated under 1% chance) and the lead moved ~750 helpers to it; proved at hour 28.4.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Suggests a lead that overrides local pessimism is valuable, and that prompting leads to encourage persistence matters. Single run.

### Claim 10: The run was far cheaper than the earlier formalization
- **Evidence**: September effort: researcher plus dozens of agents, 11 days, ~6B output tokens, 13M lines of Lean. This run: 28.7 hours, one-third the output tokens, proof one-seventh the length.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Comparison confounds model version, scaffolding and prior art (the earlier proof existed). Don't treat as a controlled efficiency result.

## Concrete Artifacts

```
Coordination tables created by the lead (source: post, Results section):
Announce, Assign, Notes, Subtasks, Landed

Run numbers (source: post): 1 lead + 999 helpers; 28.7 h; 19 automatic
time-remaining reminders to the lead; 60 statements, 47 judged infeasible
then reallocated to 10; task tree 2,418 tasks / 10 levels; >1M tool calls.

Safety limits (source: post): DB statement limit 5 s; write cap 256 MiB;
no direct network, pipe-only gateway with agent-identity tagging.
```

## Cross-References

- **Corroborates**: `blog-anthropic-multi-agent-coordination-patterns.md` Claim 10 (shared state when agents need each other's intermediate findings) and Claim 11 (hybrid orchestrator plus shared state; here lead/helper plus SQL). `blog-green-sandboxing-rogue-agents.md` Claim 7 (monitoring agent traffic at scale must be done by other models) and Claim 4 (peer instructions not reliably distrusted) are consistent with the CoT/inter-agent communication monitoring.
- **Contradicts**: None filed. Tension to note: `blog-anthropic-claude-code-auto-mode.md` Claim 3 favors a reasoning-blind classifier; this post finds CoT-visible monitors detect all sabotage but keeps an action-only monitor in parallel against persuasion. These read as complementary layers rather than opposed claims, so no contradiction issue was filed.
- **Extends**: `blog-anthropic-multi-agent-coordination-patterns.md` Claim 5 (shared state needs termination conditions; here time reminders and lead-driven reallocation), `blog-anthropic-agent-identity-access-model.md` Claim 8 (credential/identity handled at the network boundary; here gateway-tagged identity).
- **Novel**: Measured 1,000-agent run; ~100-agent single-machine ceiling; agent-designed five-table schema; CoT-aware vs action-only monitor result for multi-agent decomposition attacks.

## Guide Impact

- **Chapter 02**: Add the run as evidence that Git plus a shared database suffices as a coordination layer, with the ~100-agent single-machine ceiling as sizing guidance.
- **Chapter 06**: Add the layered design (no network, gateway identity, own-branch push, limited DB role, real-time plus offline monitors) and the finding that CoT/inter-agent visibility catches decomposition attacks; note the headline run used only the action-based monitor.
- **Chapter 05**: Optional: lead/helper hierarchy with captains per crew and lead reallocation.

## Extraction Notes

- Fetched via a summarizing fetch tool; direct quotes were obtained through a targeted second pass. Claims without verbatim quotes are marked as such. The triage comment's "toy experiment" wording was not independently confirmed verbatim, so it is not quoted above.
- The post's inconsistency on block semantics (Claim 8) is flagged rather than resolved.
- No sub-pages followed.
