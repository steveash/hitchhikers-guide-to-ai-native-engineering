---
source_url: https://claude.com/blog/projects-redesigned
source_type: blog-post
title: "Projects redesigned: from folder to conversation"
author: Anthropic (product announcement)
date_published: 2026-09-17
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: emerging
issue: "#3530"
---

# Projects redesigned: from folder to conversation

> Anthropic's September 17, 2026 beta announcement of a redesigned Claude Code
> "project": a coordinator chat that scopes, delegates, and assembles work
> across parallel "threads," where each thread is literally an independent
> Claude Code cloud session on its own git branch, conflicts between threads
> resolve as ordinary merge conflicts in PRs, and every thread reads from and
> writes to a shared cross-thread project memory.

## Source Context

- **Type**: blog-post (official claude.com/blog product announcement, "Product
  announcements, Claude Code" category, ~5 min read, published September 17,
  2026)
- **Author credibility**: First-party Anthropic product announcement.
  Authoritative for what the feature does and its rollout status; no named
  individual author (standard house style for claude.com/blog product posts).
  No independent practitioner accounts, case studies, or usage metrics
  accompany this announcement — it is a beta launch description, not a
  post-adoption retrospective.
- **Scope**: Covers the redesigned project's coordinator/thread architecture,
  two worked examples (checkout-latency reduction, v1-endpoint retirement
  across repos), the shared cross-thread project memory, the new project
  "library," usage/quota mechanics for multi-thread sessions, and beta
  rollout/availability terms. Does NOT cover: pricing, the underlying
  coordinator-to-thread task-splitting algorithm, how thread-level permission
  prompts or auto-mode-style approval gating work for unattended threads, the
  shared-memory storage format, or how the merge-conflict resolution
  mechanism behaves when more than two threads touch the same file. The
  post's only two substantive outbound links are a waitlist signup form
  (`claude.com/form/projects`) and a link to the live product surface itself
  (`claude.com/projects`, which redirects to the authenticated `claude.ai/projects`
  app and was not a fetchable content page); neither contains additional prose
  content, so no sub-pages were followed.

## Extracted Claims

### Claim 1: Projects replace manual multi-session work division with a single natural-language goal that Claude scopes, delegates, coordinates, reviews, and assembles on its own

- **Evidence**: Opening framing statement contrasting the old manual workflow with the new one.
- **Confidence**: emerging (first-party product framing for a beta feature)
- **Quote**: "Managing multiple sessions across a build used to require you to divide the work, juggle handoffs, and stitch the results back together. Now in a Claude Code project, you describe what needs to get done and Claude manages the work."
- **Our assessment**: This is the same coordinator/delegate framing Cursor shipped roughly a week earlier in `blog-cursor-projects-coordinator-agents.md` (Claim 1: a coordinator that "delegates tasks to thousands of subagents" over "months of work"). Two vendors converging on "describe the goal, let a coordinator divide and reassemble the work" within days of each other is moderate evidence this is becoming the expected shape of a multi-agent coding product, not an isolated Anthropic bet.

### Claim 2: Projects can be steered remotely (including from a phone) and continue running unattended after the user steps away

- **Evidence**: Direct statement immediately following the coordinator description.
- **Confidence**: emerging (vendor feature description of a beta capability)
- **Quote**: "You can steer progress throughout, even from your phone, and it keeps working after you step away from your computer."
- **Our assessment**: "Keeps working after you step away" is functionally the same unattended-execution property documented for Claude Code's auto mode (`blog-anthropic-claude-code-auto-mode.md`), which found a 17% false-negative rate on real overeager actions even with its two-stage permission classifier. This post does not describe what permission model gates unattended thread actions (shell commands, deploys, force pushes) — a gap the guide should flag: steering "from your phone" implies reduced attention exactly when a misclassified risky action is least likely to be caught in time.

### Claim 3: Two worked examples show the two thread-splitting strategies — parallel threads within one repo (by task) versus one thread per repo (by codebase)

- **Evidence**: Two concrete named scenarios: reducing checkout p75 latency (single app, threads split by endpoint) and retiring a deprecated v1 endpoint (API/web/mobile repos, threads split by repo).
- **Confidence**: anecdotal (illustrative vendor-authored examples, not measured case studies)
- **Quote**: "configure a project and set a goal to reduce your app's checkout p75 latency. Then ask Claude to profile each endpoint, test optimizations, and open PRs in parallel threads. Or connect your API, web, and mobile repos and set a goal to retire a deprecated v1 endpoint. Claude creates a thread per repo to migrate the callers, run the tests, open PRs, and then tells you which ones need to merge first."
- **Our assessment**: The second example ("tells you which ones need to merge first") is the most operationally specific detail in the pair — it implies the coordinator reasons about cross-repo merge ordering (e.g., the API repo's PR must land before the web/mobile repos' PRs that depend on it), not just parallel independent execution. Neither example states how many threads ran, how long the work took, or what fraction of the PRs needed human correction — these are illustrative scenarios, not audited outcomes.

### Claim 4: A project has threads that do the work and a coordinator that directs them; project setup selects a goal plus repo/context, cloud environment, connectors, plugins, instructions, and model

- **Evidence**: Named architectural section ("Threads do the work, Claude directs it") with an explicit configuration-surface list.
- **Confidence**: emerging (vendor architectural description of a beta feature)
- **Quote**: "Projects have threads that do the work and a coordinator that directs them." ... "You can configure the project’s cloud environment, connectors, plugins, instructions, and model."
- **Our assessment**: This is architecturally identical to the planner/worker split Cursor names "coordinator" and "subagents" in `blog-cursor-projects-coordinator-agents.md` (Claim 4: "The coordinator doesn't write code itself but directs other agents that do"). The configuration surface (cloud environment, connectors, plugins, instructions, model) maps directly onto existing Claude Code primitives already documented elsewhere in the corpus (connectors, plugins, CLAUDE.md-style instructions) — the novelty here is binding all of them to a persistent project rather than a single session.

### Claim 5: Users are meant to brief the project coordinator the way they would brief a "chief of staff," and the coordinator routes each request to a new or pre-existing thread

- **Evidence**: Explicit interaction-model framing with a named analogy.
- **Confidence**: anecdotal (a stated mental-model analogy, not a measured behavior)
- **Quote**: "Brief Claude in the project the way you'd brief a chief of staff and it routes work to new or pre-existing threads."
- **Our assessment**: The "chief of staff" framing is a concrete, quotable mental model for how much delegation and initiative the coordinator is meant to exercise — more than a search assistant, less than a fully autonomous decision-maker. It is new phrasing to the corpus; the closest analog, Cursor's "coordinator," carries no equivalent human-role analogy in its own announcement.

### Claim 6: Each thread is literally an independent Claude Code cloud session working on its own git branch and copy of the repo; when two threads touch the same code, the overlap is resolved as an ordinary merge conflict in a PR, not by special coordinator logic

- **Evidence**: Explicit "under the hood" architectural disclosure.
- **Confidence**: emerging (vendor architectural description; the merge-conflict-as-resolution-mechanism claim is specific enough to be testable but not independently verified)
- **Quote**: "Under the hood, each thread is a Claude Code cloud session working on its own branch and copy of the repo."
- **Quote**: "The coordinator keeps work organized, but if any threads work on the same code, the overlap is resolved as a merge conflict just like any other PR."
- **Our assessment**: This is the most concrete and novel technical detail in the post. Rather than inventing a bespoke distributed-locking or conflict-avoidance mechanism, Anthropic explicitly reuses git's existing merge-conflict semantics as the coordination boundary between parallel threads — the same failure mode a human would hit merging two colleagues' branches. Neither Cursor's Projects post nor any other corpus source states this mechanism this explicitly; Cursor's "shared context" (Claim 6 in `blog-cursor-projects-coordinator-agents.md`) describes agents avoiding redundant work via shared research files, not a stated commitment to resolve code-level conflicts as standard PR merge conflicts.

### Claim 7: Each thread can further decompose its own delegated work using subagents, loops, and workflows to finish large assignments faster

- **Evidence**: Explicit statement of intra-thread decomposition mechanisms.
- **Confidence**: emerging (vendor feature description)
- **Quote**: "Each thread can further split its delegated work into pieces using subagents, loops, and workflows when needed so large assignments finish faster."
- **Our assessment**: This establishes a three-level hierarchy — project (coordinator) → thread (Claude Code cloud session) → subagents/loops/workflows within a thread — none of which is described in further mechanistic detail here. It positions projects as a superset that composes with, rather than replaces, the existing Claude Code primitives (subagents, loops, workflows) already documented elsewhere in the corpus.

### Claim 8: Every thread in a project reads from and writes to a shared project memory, reducing the need for complex prompt engineering, and can recall specifics like schedule changes, design rationale, and key contacts

- **Evidence**: Named architectural section ("Context builds over time") with a concrete illustrative example.
- **Confidence**: emerging (vendor architectural description; the specific recall example is illustrative, not a documented production case)
- **Quote**: "Every thread now adds to and draws from a shared memory, reducing the need for complex prompt engineering."
- **Quote**: "For example, Claude can remember the release moved to Friday, why the export was dropped, or who to check in with before touching the billing service."
- **Our assessment**: This is a third distinct Anthropic memory implementation in the corpus, alongside Claude Managed Agents' filesystem-mounted memory (`blog-anthropic-claude-managed-agents-memory.md`, Claim 2: files mounted onto a sandbox, accessed via bash/code execution) and consumer chat/Cowork's topic-file memory (`blog-anthropic-memory-works-everywhere.md`, Claim 3: topic files updated live during a conversation). None of the three posts states that projects share a storage mechanism or implementation with either of the other two — they should be treated as three separate memory systems unified only by shared design philosophy (a persistent, inspectable store that reduces the need to re-explain context), not as the same underlying feature.

### Claim 9: Claude also learns and adapts to the user's working and communication style within a project, including adjustable check-in frequency, thread-starting frequency, and update detail level

- **Evidence**: Explicit statement of user-configurable communication-style controls.
- **Confidence**: anecdotal (vendor feature description; no detail on how "adjust how often it checks in" is actually configured — natural language instruction vs. a settings UI)
- **Quote**: "Claude also remembers your working and communication style. You can ask it to adjust how often it checks in, how frequently it starts new threads, or how detailed to make each update."
- **Our assessment**: This extends the "chief of staff" framing (Claim 5) into a concrete, tunable set of behaviors rather than a fixed cadence. It is new to the corpus — no other source documents a coding-agent product where the update cadence and thread-creation aggressiveness are themselves user-adjustable, learned preferences rather than fixed harness settings.

### Claim 10: Projects now include a "library" that collects both user-added files and Claude-generated artifacts, making past materials easier to find and reuse in new work

- **Evidence**: Explicit feature description in the "Context builds over time" section.
- **Confidence**: emerging (vendor feature description of a beta capability)
- **Quote**: "Alongside memory, projects now include a library that collects the files you add and the artifacts produced by Claude. This makes it easier to find relevant materials and for new work to build on past efforts."
- **Our assessment**: The explicit mention of "artifacts" ties this library directly to the Claude Code artifacts feature already documented in `blog-anthropic-claude-code-artifacts.md` (Claim 5: a "gallery" that "lets you browse and manage all artifacts you've made"). The project library appears to be a project-scoped extension of that same artifact-management surface, now also holding user-uploaded files alongside Claude-generated ones — but this post does not state whether the library and the artifacts gallery are the same underlying store or two separate ones, which is a gap the guide should not paper over.

### Claim 11: Because a project can run several full Claude Code sessions in parallel, projects can reach usage limits faster; practitioners can check project-specific usage and separately select the model and effort level for the coordinator chat versus the worker threads

- **Evidence**: Explicit statement in the "What's next" section naming the resource-consumption mechanism and the two mitigations (usage visibility, independent model/effort selection).
- **Confidence**: settled (a factual, verifiable product-mechanics statement about how usage is metered and configured)
- **Quote**: "Projects can run several threads at once, and each one is a full Claude Code session. Because of this, projects can reach usage limits faster. You can check project specific usage and select the model and effort levels used by the coordinator chat as well as the worker threads."
- **Our assessment**: This is a direct, practitioner-actionable cost-management detail: because each thread is a full session (Claim 6), N parallel threads consume roughly N times the usage of a single session, not a fraction of it. The ability to set a cheaper/faster model for worker threads while keeping a stronger model on the coordinator is a concrete cost-control lever the guide should name explicitly — it parallels the quota-budgeting concern already raised for Claude Code routines (`blog-anthropic-claude-code-routines.md`, Claim 7), though routines are quota-capped per plan tier while projects are usage-metered with no stated daily cap in this post.

### Claim 12: Redesigned projects launch today in beta to a narrow slice of users (Pro/Max subscribers using Claude Code cloud sessions with no existing projects), with cloud-only thread execution today and local execution "coming very soon"; existing projects are unaffected until the rollout reaches chat and Cowork

- **Evidence**: Explicit rollout/availability statement plus a forward-looking roadmap statement.
- **Confidence**: settled (a factual, verifiable launch-status statement as of publication)
- **Quote**: "Starting today, updated projects are available in beta to select Claude Pro and Max subscribers who use cloud sessions in Claude Code and don’t have any existing projects on the web or desktop."
- **Quote**: "Existing projects on Pro and Max plans keep working as they do today. We'll upgrade them as the rollout expands to chat and Cowork."
- **Quote**: "Threads run in the cloud today; running on your machine alongside your local tools and code and behind your network is coming very soon."
- **Our assessment**: The eligibility carve-out ("don’t have any existing projects on the web or desktop") means early adopters of the redesign are, by construction, projects-feature novices rather than existing heavy users — a detail relevant to interpreting any future usage data from this rollout phase as not representative of experienced project users. The cloud-only-today / local-coming-soon roadmap mirrors the same cloud-first-then-local-fallback trajectory Cursor already shipped in `blog-cursor-projects-coordinator-agents.md` (Claim 5: "cloud by default, local when needed").

## Concrete Artifacts

```
Claude Code Projects (redesigned) — architecture, from the announcement
(Anthropic, "Projects redesigned: from folder to conversation," Sept 17, 2026)
Source: https://claude.com/blog/projects-redesigned

HIERARCHY:
  Project (coordinator chat)
    -> Thread (independent Claude Code cloud session, own git branch + repo copy)
      -> Subagents / loops / workflows (intra-thread decomposition)

PROJECT SETUP SELECTS:
  - Goal
  - Repo or context
  - Cloud environment
  - Connectors
  - Plugins
  - Instructions
  - Model

CONFLICT RESOLUTION:
  "the overlap is resolved as a merge conflict just like any other PR"
  (no special coordinator-level locking or conflict-avoidance mechanism stated)

SHARED STATE:
  - Cross-thread shared memory (schedule changes, design decisions, contacts)
  - Library: user-added files + Claude-generated artifacts, project-scoped

USAGE / COST CONTROLS:
  - Project-specific usage visibility
  - Independent model + effort-level selection: coordinator chat vs. worker threads
  - Caveat: N parallel threads = N full Claude Code sessions of usage, not a fraction

ROLLOUT (as of Sept 17, 2026):
  Today:       beta, Pro/Max + cloud sessions + no existing projects
  Next week:   more Claude Code users on Pro/Max
  Later:       all Claude/Team/Enterprise plans; upgrade of existing projects;
               expansion to chat and Cowork
  Coming soon: local (on-machine, behind-network) thread execution
```

```
Two worked examples from the announcement (verbatim scenarios)
Source: https://claude.com/blog/projects-redesigned

1. Single-repo, task-split threads:
   Goal: "reduce your app's checkout p75 latency"
   Threads: profile each endpoint, test optimizations, open PRs — in parallel

2. Multi-repo, repo-split threads:
   Goal: "retire a deprecated v1 endpoint" across API, web, and mobile repos
   Threads: one per repo — migrate callers, run tests, open PRs
   Coordinator output: tells the user which PRs need to merge first
```

## Cross-References

- **Corroborates** `blog-cursor-projects-coordinator-agents.md`: Both posts describe a persistent, chat-directed coordinator that delegates to parallel session-level workers (Cursor: "subagents"; Anthropic: "threads") and both explicitly frame this as replacing the old model of a developer manually dividing and reassembling work across sessions (Claim 1 here corroborates that note's Claim 1). Both also share a cloud-by-default-with-local-coming architecture (Claim 12 here corroborates that note's Claim 5). Two vendors shipping structurally identical coordinator/worker products within roughly a week of each other (Cursor: Sept 10, 2026; Anthropic: Sept 17, 2026) is moderate evidence this is becoming a converged product category, not an isolated feature bet by either vendor.

- **Extends** `blog-anthropic-claude-code-artifacts.md`: The new project "library" (Claim 10) explicitly names "the artifacts produced by Claude" as one of its two contents, directly referencing the artifacts feature that note documents (Claim 5's "gallery"). This post does not state whether the library and the artifacts gallery are the same underlying store — flagged as an open gap rather than assumed.

- **Extends** `blog-anthropic-claude-managed-agents-memory.md` and `blog-anthropic-memory-works-everywhere.md`: All three posts describe an Anthropic product with a persistent, cross-session memory store that reduces the need to re-explain context (Claim 8 here). None states a shared implementation across the three products — Managed Agents memory is filesystem-mounted and API-managed (that note's Claim 2), consumer chat/Cowork memory is topic-file-based and edited via a settings UI (that note's Claim 3-4), and this post's project memory is thread-shared with no storage mechanism disclosed. Treat as three parallel instances of the same design philosophy, not one feature described three times.

- **Extends** `blog-anthropic-claude-code-auto-mode.md`: Claim 2 here (threads "keep working after you step away from your computer") depends on some form of unattended-permission handling for thread actions, which this post never names. That note's two-stage classifier and its disclosed 17% false-negative rate on real overeager actions is the closest documented Anthropic mechanism for exactly this problem — the guide should not assume redesigned projects have solved unattended-safety more thoroughly than auto mode has, absent a stated mechanism.

- **Extends** `blog-anthropic-claude-code-routines.md`: Claim 11's usage/quota mechanics (parallel threads consume usage faster; practitioners must budget model/effort selection) is the same category of cost-management concern as that note's Claim 7 (routines' plan-tiered daily quotas competing with interactive session usage), but the mechanism differs — routines are hard-capped per plan tier, while this post describes metered usage with independent model/effort selection as the mitigation, not a stated daily cap.

- **Contradicts**: None identified. No existing source note makes a claim about Claude Code's coordinator/thread architecture, project-scoped memory, or artifact library that this post's claims conflict with.

- **Novel**:
  - The explicit "resolved as a merge conflict just like any other PR" statement (Claim 6) is the most concrete conflict-resolution mechanism disclosed for a coordinator/parallel-worker product anywhere in the corpus — no prior source (including the closely analogous Cursor Projects post) states this level of mechanistic detail.
  - The "chief of staff" briefing analogy (Claim 5) and the user-adjustable communication cadence/thread-starting-frequency controls (Claim 9) are new framing not present in any prior corpus source describing a coordinator-agent product.
  - The three-level hierarchy (project coordinator → thread-as-full-session → intra-thread subagents/loops/workflows) is the first corpus source to explicitly nest an entire pre-existing agent-composition stack (subagents, loops, workflows) inside a higher-level, multi-thread coordination layer.
  - The explicit "N threads = N full sessions of usage, with independent coordinator/worker model and effort selection" cost model (Claim 11) is new; no prior corpus source names this specific lever for controlling multi-agent coordination cost.

## Guide Impact

- **Chapter 01 (Daily Workflows) — Multi-Agent Orchestration / coordinator model**: Add this post as a first-party Anthropic implementation of the coordinator/worker pattern already documented via Cursor's Projects (`blog-cursor-projects-coordinator-agents.md`). Cite the explicit merge-conflict resolution mechanism (Claim 6) and the "chief of staff" briefing analogy (Claim 5) as concrete, quotable details that sharpen the existing coordinator-pattern discussion — the guide currently lacks a stated answer for "what happens when two parallel agents touch the same file," and this is the first source to give one explicitly.

- **Chapter 02 (Harness Engineering) — Cost and resource management**: Add Claim 11 (parallel threads multiply usage; coordinator and worker threads can be assigned different models/effort levels independently) as a concrete cost-control recommendation for any multi-agent coordination harness, alongside the existing routines quota-budgeting guidance from `blog-anthropic-claude-code-routines.md`. Recommend defaulting worker threads to a cheaper/faster model and reserving the strongest model for the coordinator, unless a specific thread's task requires otherwise.

- **Chapter 02/03 (Harness Engineering / Memory)**: When discussing Anthropic's approach to persistent agent memory, distinguish the three separate implementations now in the corpus (Managed Agents filesystem memory, consumer chat/Cowork topic-file memory, and this post's project-scoped thread-shared memory) rather than treating "Claude has memory" as a single unified capability. Flag the open gap (this post does not state a storage mechanism) rather than inferring one from the other two products.

- **Chapter 02 (Harness Engineering) — Unattended execution safety**: Add a caution alongside any recommendation to use projects for unattended, phone-steerable work (Claim 2): the post does not name a permission-gating mechanism for thread actions, and the closest documented Anthropic mechanism (auto mode) has a disclosed 17% false-negative rate on real overeager actions (`blog-anthropic-claude-code-auto-mode.md`). Recommend the same reversible-actions-first design principle already given for routines: prefer draft PRs and draft comments over irreversible actions in unattended threads until the permission model for threads is documented.

## Extraction Notes

- The claude.com blog post is short (~700 words of body prose across five section headers plus a rollout paragraph). The WebFetch tool's default summarization pass produced a paraphrased/restructured version of the article (headings and bullet points that do not appear verbatim on the page); to guarantee verbatim quotes per MINER.md §2a, the page was instead fetched directly via `curl` with a browser user agent and stripped of HTML markup with a Python HTMLParser, then every quote above was copied character-for-character from that raw-text extraction.
- The post's only two substantive outbound links are a waitlist signup form (`claude.com/form/projects`) and a link to the live product itself (`claude.com/projects`), which returns an HTTP 302 redirect to the authenticated `claude.ai/projects` app and has no fetchable public content. Per MINER.md §1, both were checked; neither qualifies as a substantive linked page worth following, so no sub-pages were extracted beyond the announcement itself.
- No contradiction with any existing corpus note was found (see Cross-References → Contradicts), so no contradiction issue was filed per MINER.md §4a.
- Confidence set to `emerging`: first-party Anthropic announcement of a shipping beta feature with a narrow initial eligibility window (Claim 12). High authority for what the feature does and its rollout terms; no independent practitioner accounts or production usage data accompany this announcement, and several architecturally significant mechanisms (unattended-thread permission gating, shared-memory storage format, library/artifacts-gallery relationship) are left undocumented by the post itself.
