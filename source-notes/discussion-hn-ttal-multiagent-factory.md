---
source_url: https://news.ycombinator.com/item?id=47435275
source_type: discussion
title: "Show HN: TTal – CLI that turns Claude Code into a multi-agent software factory"
author: neilbb
date_published: 2026-03-19
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: current
confidence_overall: anecdotal
issue: "#32"
---

# Show HN: TTal – CLI that turns Claude Code into a multi-agent software factory

> A Show HN announcement of TTal, a Go CLI that automates the "babysitting"
> overhead of parallel Claude Code sessions using a two-plane architecture
> (persistent Manager plane + ephemeral Worker plane) — notable for four
> specific design decisions absent from other tools in our corpus: named
> specialized agents with explicit identity, a bash-only subagent runtime
> that eliminates tool-schema overhead, external state stored entirely in
> standard OS-level CLI tools (Taskwarrior, FlickNote, diary-cli), and
> Telegram as the human-in-the-loop interface for remote phone-based oversight.

## Source Context

- **Type**: discussion (Show HN announcement + linked GitHub repo + author's
  FlickNote on multi-agent patterns; 6 points, 4 comments, 2026-03-19)
- **Author credibility**: neilbb is anonymous on HN. No prior track record or
  affiliation verifiable beyond the TTal tool itself. The GitHub repository
  (`tta-lab/ttal-cli`) and companion project `logos` are live and publicly
  accessible at time of extraction (unlike Kiln, which disappeared). The
  architecture described is coherent, the implementation exists, and the linked
  FlickNote expands the claims into a seven-pattern taxonomy. Engagement is low
  (6 points, 4 comments), reducing crowd-corroboration. Treat all claims as
  self-reported from a single author building an active but early-stage tool.
- **Scope**: The HN post covers the tool's motivation and architecture overview.
  The GitHub README (`tta-lab/ttal-cli`) expands this with implementation
  details, agent roles, and the technology stack. The linked FlickNote
  (`dev.flicknote.app/notes/5a95cdcd...`) contains a seven-pattern taxonomy of
  multi-agent design that the author has distilled from building TTal. The
  `logos` companion library (`tta-lab/logos`) provides implementation details
  on the bash-only agent loop. This note synthesizes all four sources.
  It does NOT cover: performance benchmarks, failure modes, cost data, or
  adoption metrics. The Pro licensing tier ($100/year) implies some commercial
  intent; the free tier (2 agents) indicates the tool is intended for broad use.

## Extracted Claims

### Claim 1: The dominant overhead in parallel Claude Code workflows is not task execution but session management — window-switching, copy-paste feedback loops, and babysitting

- **Evidence**: Author's stated motivation: "I got tired of babysitting Claude
  Code sessions. Every PR meant switching between windows, copy-pasting review
  feedback, telling the coder what to fix, and repeating until it merged."
  This is the triggering problem that drives the entire architecture.
- **Confidence**: anecdotal
- **Quote**: "I got tired of babysitting Claude Code sessions. Every PR meant
  switching between windows, copy-pasting review feedback, telling the coder
  what to fix, and repeating until it merged."
- **Our assessment**: This pain point corroborates sukit's "parallel session
  ceiling" (failure-sukit-parallel-session-ceiling) from the demand side. The
  cognitive overhead sukit documents (context-switching, 2-session ceiling)
  is the same friction TTal is engineering away. Importantly, TTal's solution
  is automation of the human's context-switching role, not raising the
  practitioner's cognitive ceiling. The pain is real; TTal is a tool-builder's
  response to the same problem the practitioner-side data documents.

### Claim 2: A two-plane architecture — persistent Manager plane + ephemeral Worker plane — is the right structure for a software-factory orchestrator

- **Evidence**: Author's explicit design description in the HN post and README.
  Manager plane: "Long-running agents that persist across sessions. They draft
  plans, break them into tasks, assign priorities, and unblock workers when
  they get stuck." Worker plane: "Short-lived agents spawned per task, each
  receiving an isolated git worktree + tmux session."
- **Confidence**: anecdotal
- **Quote**: "Manager plane — long-running agents that persist across sessions.
  They draft plans, break them into tasks, assign priorities, and unblock workers
  when they get stuck. Worker plane — short-lived agents spawned per task, each
  receiving an isolated git worktree + tmux session."
- **Our assessment**: This is TTal's central and most novel architectural
  contribution relative to the rest of our corpus. Kiln (discussion-hn-kiln-
  orchestration) used GitHub Projects as its control plane with column
  transitions dispatching work, but did not distinguish between persistent
  strategic agents and ephemeral tactical agents. Osmani's Agent Teams
  (blog-addyosmani-code-agent-orchestra, Claim 4) is similar — Team Lead +
  Teammates — but is an experimental Claude Code feature, not a standalone
  CLI. TTal's Manager plane is a long-lived process (not just a coordination
  abstraction), which means it retains context across multiple Worker
  completions. The practical implication: the Manager plane can update
  priorities in response to completed work without requiring the human to
  manually re-read state and redirect. This is a meaningful architectural
  advance over the Kiln pattern.

### Claim 3: Named specialized agents with explicit identity and personality perform better than anonymous generic workers

- **Evidence**: Author's naming scheme (Yuki=routing, Athena=research/investigation,
  Inke=planning, Workers=implementation) and FlickNote claim: "agents with
  identity and personality genuinely perform better. They maintain consistent
  behavior, develop recognizable working styles." Inspired by the game
  Forgotten Anne.
- **Confidence**: anecdotal
- **Quote**: "agents with identity and personality genuinely perform better.
  They maintain consistent behavior, develop recognizable working styles."
  (From author's FlickNote on multi-agent patterns)
- **Our assessment**: The specialization-by-name claim has two separable
  components: (a) functional specialization (Athena only does research, Inke
  only does planning) is a well-supported pattern — focusing context on a
  single task type improves output quality; (b) the claim that *named identity
  with personality* specifically improves consistency goes further and is not
  supported by controlled evidence. The game-inspiration explanation is
  evocative but not rigorous. We accept the functional-specialization claim
  with moderate confidence and note the personality claim as a novel but
  unverified hypothesis. It is worth watching: if multiple tools converge on
  named persistent agents (TTal, Sentry's skill system), that convergence is
  itself signal.

### Claim 4: logos — a bash-only subagent runtime using `<cmd>` blocks instead of tool schemas — eliminates tool-call overhead

- **Evidence**: The `tta-lab/logos` GitHub README describes the runtime
  design: "prompt → LLM → scan `<cmd>` blocks → execute → feed `<result>`
  back → repeat." The LLM outputs plain text with shell commands in `<cmd>`
  tags; logos executes them and injects `<result>` markers. No JSON tool
  schemas involved.
- **Confidence**: anecdotal
- **Quote**: "Zero tool call overhead" (logos README tagline). From the
  README: "The LLM wraps shell commands in `<cmd>` blocks that the system
  automatically detects and executes."
- **Our assessment**: This is a meaningful alternative architecture to the
  standard Claude Code tool-use model. Claude Code uses JSON-structured tool
  calls (Bash, Read, Write, Edit) with explicit schema definitions; logos
  uses free-form bash commands in a tagged-text protocol. The advantage is
  that the LLM doesn't need to compose valid JSON — any bash command it knows
  works. The disadvantage is loss of structured output and harder
  interoperability with typed tools. The "zero overhead" claim likely refers
  to not needing to define or validate tool schemas, not to execution
  performance. The logos runtime also supports two security modes:
  `Sandbox: false` (direct bash on host) and `Sandbox: true` (restricted via
  `temenos` daemon). This is the only bash-over-tool-schemas pattern in our
  corpus, and it is worth tracking as an alternative design point.

### Claim 5: Agents should be stateless executors, with all state externalized to standard CLI tools

- **Evidence**: From author's FlickNote: "Agents are stateless executors with
  external persistence." The TTal stack uses Taskwarrior for task queue,
  FlickNote for knowledge/memory, and diary-cli for agent memory persistence.
  No custom database or proprietary state format.
- **Confidence**: anecdotal
- **Quote**: "Agents are stateless executors with external persistence."
  (FlickNote multi-agent patterns note)
- **Our assessment**: This is a clear architectural principle, not just an
  implementation choice. By making agents stateless, TTal gains: (a) session
  recoverability — killing a worker doesn't lose state; (b) inspectability —
  Taskwarrior and FlickNote are human-readable; (c) composability — any agent
  can read from the same task queue. The tradeoff vs. Kiln's approach:
  Kiln put everything in GitHub Issues (globally accessible, no local setup);
  TTal uses local CLI tools (no API dependency, works offline, but requires
  local tool installation). Both are implementations of the same underlying
  principle: externalize state from agent memory. French-Owen and Sankalp
  advocate local filesystem files (PLAN.md, tasks.md); TTal advocates
  structured tools (Taskwarrior) over flat files. This is a continuum, not a
  contradiction.

### Claim 6: A P2P mesh topology — where workers communicate directly with the Manager when blocked, rather than through a central queue — prevents bottlenecks

- **Evidence**: From author's HN reply clarifying the architecture: "workers
  get blocked, they alert the designer directly rather than waiting." From
  the FlickNote pattern taxonomy (Pattern 7: Swarm): "Mesh network topology
  with agents communicating directly rather than through centralized control."
  The `ttal send --to [agent]` command enables direct agent-to-agent messaging.
- **Confidence**: anecdotal
- **Quote**: "workers get blocked, they alert the designer directly rather
  than waiting." (neilbb, HN comment reply to parsak)
- **Our assessment**: This is a direct response to the bottleneck problem of
  hub-and-spoke orchestration. If all inter-agent communication routes through
  a single coordinator, that coordinator is a performance and reliability
  bottleneck. A mesh (each node can message any other node) eliminates single
  points of failure but increases complexity — any agent must know the
  addresses of all other agents it might need to contact. In TTal's case, the
  Telegram interface serves as a human-visible message bus, which limits
  topology complexity in practice. The Manager still acts as strategic
  coordinator; the mesh enables tactical direct communication to skip the
  queue when a worker is genuinely blocked.

### Claim 7: Telegram is the right interface for human-in-the-loop oversight, enabling remote management from a phone

- **Evidence**: Author's primary motivation: "I wanted to manage all of this
  from my phone while doing other things." The Manager plane is "managed via
  Telegram." The P2P message bridge routes "humans and agents via Telegram."
- **Confidence**: anecdotal
- **Quote**: "I wanted to manage all of this from my phone while doing other
  things." (HN post)
- **Our assessment**: The phone-management angle is novel to our corpus.
  Kiln ran locally on a machine and assumed the developer was at their
  terminal. TTal's design assumption is that the developer is intentionally
  *not* attending to the terminal — they are doing other things and checking
  in remotely. This represents a different vision of AI-assisted engineering:
  not "AI at the keyboard" but "AI in the background, human on-call." The
  Telegram choice is practical (existing app, good mobile UX, easy bot
  integration) but creates a dependency on a third-party messaging service.
  The human-in-the-loop approval gate described by commenter maxbeech
  (openhelm.ai uses a "hard rule: user sign-off before execution") is not
  documented as a TTal default, suggesting TTal defaults to more automation
  with less mandatory gates.

### Claim 8: The hardest unsolved problem in multi-agent orchestration is distinguishing stuck tasks from slow tasks

- **Evidence**: Commenter maxbeech (building openhelm.ai, parallel multi-agent
  architecture) asks directly: "How do you handle the heuristics for deciding
  when something is stuck vs. just taking a long time?" maxbeech reports
  their own current approach: a 30-minute timeout. neilbb did not provide a
  specific answer in the thread.
- **Confidence**: anecdotal
- **Quote**: "How do you handle the heuristics for deciding when something is
  stuck vs. just taking a long time?" (maxbeech, HN comment)
- **Our assessment**: This is a real unsolved problem that the HN thread
  surfaces without resolving. A timeout-based approach (30 minutes) is simple
  but crude — some tasks legitimately take longer. A progress-signal approach
  (is the agent producing output?) is better but harder to implement. TTal's
  manager-plane alert mechanism (workers alert the manager when blocked) pushes
  the detection responsibility onto the Worker itself, which may miss the case
  where a worker is in an infinite loop and doesn't know it's stuck. This
  problem is worth a guide section: it is a systematic challenge for any
  autonomous multi-agent harness.

### Claim 9: The complete worker task lifecycle is: task → research → design → implement → review → merge → cleanup

- **Evidence**: From the TTal GitHub README: "The stated workflow progression:
  'task → research → design → implement → review → merge → cleanup'."
  The key command `ttal go [task-id]` advances any task through its pipeline
  automatically.
- **Confidence**: anecdotal
- **Quote**: "task → research → design → implement → review → merge → cleanup"
  (TTal GitHub README)
- **Our assessment**: This is the most explicit formalization of a complete
  agent task lifecycle in our corpus. Previous notes (dontwannahearit's
  11-step workflow in failure-sukit-parallel-session-ceiling) capture a
  similar sequence in practitioner form. TTal's version is cleaner and maps
  each stage to specific named agents (Athena for research, Inke for design,
  Workers for implementation). The "cleanup" stage (auto-cleanup of worktree
  and tmux session) is underemphasized in other sources — it is operationally
  important for preventing worktree accumulation, which sukit explicitly flags
  as a "nightmare managing" risk.

### Claim 9a: The multi-agent orchestration problem decomposes into seven patterns

- **Evidence**: From the author's FlickNote on multi-agent patterns (linked in
  HN thread). The seven patterns: (1) Executor-Reviewer, (2) Router/Dispatcher,
  (3) Orchestrator/Central Coordinator, (4) Pipeline/Sequential Chain,
  (5) Debate/Consensus, (6) Supervisor/Monitor-Correct, (7) Swarm/P2P Handoff.
  The author notes about Pattern 3: "orchestration isn't a single agent but
  rather 'the entire manager plane, including me.'"
- **Confidence**: anecdotal
- **Quote**: "orchestration isn't a single agent but rather 'the entire manager
  plane, including me'" (FlickNote)
- **Our assessment**: This is a practitioner-derived taxonomy, not a research
  classification. The seven patterns overlap with known distributed systems
  patterns (supervisor trees, pipelines, gossip protocols) but are framed
  for LLM agents specifically. The most interesting claim is Pattern 3: by
  explicitly including the human ("including me") in the orchestration plane,
  the author pushes back against fully autonomous orchestration. This is a
  nuanced position — fully automated coordination is the goal, but the human
  is structurally part of the current control plane.

### Claim 10: organon enables structure-aware reading and editing by symbolic ID rather than text matching

- **Evidence**: From the TTal GitHub README: "Structure-aware reading/editing
  system using `src` and `web` commands — targets by symbolic ID rather than
  text matching."
- **Confidence**: anecdotal
- **Quote**: "targets by symbolic ID rather than text matching" (TTal README)
- **Our assessment**: Thin claim — no implementation details beyond the README
  description. The concept (address code by its structural identity rather
  than its textual location) is interesting as an alternative to the Edit
  tool's old-string/new-string matching or grep-based navigation. No other
  source in our corpus describes this pattern. Not independently verifiable
  from this source alone.

## Concrete Artifacts

### TTal Two-Plane Architecture (from HN post + GitHub README)

```
TTal Architecture Overview:

Manager Plane (persistent):
  - Long-running agents (survive session resets)
  - Roles: Yuki (routing/dispatch), Athena (research), Inke (planning)
  - State: reads from Taskwarrior task queue + FlickNote knowledge base
  - Interface: Telegram (human oversight, remote management)
  - Behavior: "never blocks" — routes tasks, unblocks workers, re-priorities

Worker Plane (ephemeral):
  - Spawned per task, auto-cleaned up on completion
  - Isolation: one tmux session + one git worktree per worker
  - Lifecycle: task → research → design → implement → review → merge → cleanup
  - State: writes results back to Taskwarrior + GitHub PR

Message Bridge (daemon):
  - P2P topology: ttal send --to [agent]
  - Enables: agent-to-agent, agent-to-human, human-to-agent
  - Human channel: Telegram

External State Stack:
  - Taskwarrior: task queue, priorities, status
  - FlickNote: knowledge, plans, notes
  - diary-cli: agent memory/diary
  - (no custom database, no markdown state files)
```

### logos Bash-Only Agent Loop (from tta-lab/logos GitHub README)

```
logos execution model:

  prompt → LLM → scan <cmd> blocks → execute → feed <result> back → repeat

Example interaction (conceptual):
  [LLM response]:
    I'll check the current test status.
    <cmd>cd /workspace && npm test 2>&1 | tail -20</cmd>
  
  [logos]: executes command, wraps output:
    <result>
    ... test output ...
    </result>
  
  [LLM continues]: Based on the test output, I'll fix...
    <cmd>sed -i 's/foo/bar/' src/utils.js</cmd>

Execution modes:
  - Sandbox: false → direct bash on host
  - Sandbox: true  → restricted via temenos daemon

No tool schemas, no JSON function calls, no SDK tool definitions required.
```

### Task Lifecycle from TTal README

```
ttal go [task-id]  →  advances task through pipeline automatically:

  1. Route    (Yuki determines appropriate worker type)
  2. Research (Athena investigates, documents findings)  
  3. Design   (Inke produces plan from research)
  4. Implement (Worker: git worktree + tmux, implements plan)
  5. Review   (Worker: runs linters, tests, internal review)
  6. Merge    (Worker: opens PR, handles feedback, merges)
  7. Cleanup  (Worker: destroys worktree + tmux session)
```

### Seven Multi-Agent Patterns (from author's FlickNote)

```
1. Executor-Reviewer (Generator-Critic)
   - Sequential validation; reviewers spawn parallel subagents per aspect
   - Applied at planning and code-review stages
   - Author's note: "can't do this easily with Claude Code's native Agent tool"

2. Router (Dispatcher)
   - Manager distributes tasks based on role
   - TTal uses Taskwarrior as queue + Telegram for human approval gates

3. Orchestrator (Central Coordinator)
   - Author's framing: "the entire manager plane, including me"
   - Managing everything in one context window is unwieldy at scale

4. Pipeline (Sequential Chain)
   - task → research → design → implement; configurable gates (human or auto)
   - Embedded reviewer checkpoints at each stage

5. Debate/Consensus (Multi-Perspective Reasoning)
   - ttal send --to [agent] enables agent diagnosis exchange
   - Goal: surface problems faster than single-agent analysis

6. Supervisor (Monitor-Correct)
   - Daemon processes poll CI, partially automated monitoring
   - Human judgment retained for calls requiring context

7. Swarm (Peer-to-Peer Handoff)
   - Mesh topology: agents communicate directly when blocked
   - Workers alert Manager directly; no queue bottleneck
```

### Installation

```bash
brew tap tta-lab/ttal && brew install ttal
# or
go install github.com/tta-lab/ttal-cli@latest
# then:
ttal doctor --fix
ttal daemon install
```

## Cross-References

- **Corroborates**:
  - **failure-sukit-parallel-session-ceiling**: Sukit documented the
    "babysitting" overhead from the practitioner side: window-switching,
    copy-pasting feedback, cognitive ceiling at 2 interactive sessions.
    TTal is explicitly designed to automate that same overhead from the
    tool-builder side. The pain point descriptions are nearly identical,
    confirming the friction is real and widely felt.
  - **discussion-hn-kiln-orchestration**: Both Kiln and TTal use one git
    worktree per task as the isolation primitive (Kiln: Claim 4; TTal:
    Worker plane design). Both run locally against the user's existing Claude
    subscription. Both are single-author Go CLIs with low HN engagement at
    launch. The structural parallels are strong.
  - **blog-addyosmani-code-agent-orchestra**: Osmani's "Agent Teams" pattern
    (Claim 4) describes a Team Lead + Teammates architecture with a shared
    task list and tmux-based Teammates — structurally close to TTal's Manager
    + Worker planes. Osmani's experimental flag (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
    is the vendor version of what TTal implements as an independent CLI.
    TTal's implementation predates (or is concurrent with) any wider
    rollout of Claude Code Agent Teams; the convergence on similar patterns
    from both sides (vendor feature vs. independent tool) is strong signal.
  - **practitioner-dadlerj-tin**: Both tin and TTal wrap Claude Code with
    lifecycle management. tin handles session start/stop via hooks; TTal
    handles full task lifecycle (research through cleanup). TTal is
    structurally more ambitious (whole pipeline vs. session bookends) but
    both reflect the same underlying need: the Claude Code session lifecycle
    needs external orchestration.

- **Extends**:
  - **discussion-hn-kiln-orchestration**: Kiln established the GitHub Issues
    control-plane pattern but used a static dispatch mechanism (column
    transitions). TTal extends the idea with named persistent agents that
    actively update priorities based on ongoing work — a dynamic control
    plane vs. Kiln's static one. TTal also adds the explicit Manager/Worker
    plane separation that Kiln implied but did not formalize.
  - **failure-sukit-parallel-session-ceiling**: Sukit's worktree + atomic
    tasks insight (Lesson 3) is the manual implementation of what TTal
    automates. TTal's Worker plane architecture is the "just works" version
    of dontwannahearit's 11-step workflow. The sukit note surfaces the
    demand; TTal is one supply-side response.

- **Contradicts**: None filed. The three approaches to state persistence in
  our corpus (GitHub Issues in Kiln, local filesystem in French-Owen/Sankalp,
  CLI tools in TTal) represent different design points on the same spectrum
  rather than mutually exclusive claims. The Kiln note already captures this
  as a conditioning variable (online-first vs. offline-first deployment).
  TTal adds a third data point: purpose-built CLI tools (Taskwarrior,
  FlickNote) as an intermediate option — structured and queryable like a
  database but local and dependency-free like the filesystem approach.

- **Novel**:
  - **Named specialized agents with stated personality**: No other source in
    our corpus documents giving agents named identities (Yuki, Athena, Inke)
    as a deliberate performance and consistency strategy. This is a new
    design axis relative to all other harness patterns in our corpus.
  - **Bash-over-tool-schemas (logos)**: The `<cmd>` block pattern as an
    alternative to JSON tool schemas is not captured by any other source
    note. It represents a genuinely different philosophy: trust the LLM's
    bash knowledge rather than constraining it to declared tools.
  - **Telegram as the human oversight interface for remote management**: No
    other source describes a phone-based oversight model. All other parallel
    session patterns assume the developer is at a terminal or at least at a
    computer.
  - **Stuck-vs-slow as an open problem**: The maxbeech comment surfaces a
    systematic challenge (detecting stuck agents) that is mentioned in no
    other source. This is a live unsolved problem in autonomous orchestration.
  - **Auto-cleanup as a first-class worker concern**: The "cleanup" stage
    (destroy worktree + tmux on completion) is named explicitly in the TTal
    lifecycle but treated as an afterthought in all other sources. Sukit
    flags worktree accumulation as a "nightmare," confirming cleanup is
    important; TTal is the first source to make it a formal lifecycle stage.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The Manager/Worker plane separation is
  the most architecturally precise formulation of the persistent-coordinator +
  ephemeral-executor pattern in our corpus. Add a design section: "Two-Plane
  Orchestration Architecture" — persistent agents that maintain strategic state
  and route work vs. ephemeral agents that execute bounded tasks in isolated
  worktrees. Cite TTal as the concrete instantiation, with Osmani's Agent Teams
  as a vendor-side corroboration.

- **Chapter 02 (Harness Engineering)**: Add the logos bash-over-tool-schemas
  approach as an alternative design point for agent runtimes. Frame it as:
  "Tool schemas constrain the agent to declared capabilities; bash gives the
  agent access to the full command line at the cost of structured output and
  schema validation." Neither is universally superior — the tradeoff depends on
  whether the harness needs typed outputs or maximum flexibility.

- **Chapter 02 (Harness Engineering)**: Add the stuck-vs-slow detection
  problem as an unsolved challenge in autonomous orchestration. Document the
  current state of practice: timeout-based (maxbeech's 30-minute threshold),
  self-reporting (TTal workers alert manager when blocked), and open question
  (how to detect infinite loops that don't self-identify). This belongs
  alongside CI integration as a quality-gate design problem.

- **Chapter 01 (Daily Workflows)**: Add the "remote oversight" pattern as an
  alternative to the "at-the-terminal" interaction model. TTal's Telegram
  interface represents a different answer to "what does AI-assisted engineering
  look like?" than Claude Code's interactive terminal: background execution
  with mobile check-ins. Both modes are real; the guide should describe both.

- **Chapter 01 (Daily Workflows)**: The task lifecycle formalization
  (task → research → design → implement → review → merge → cleanup) is the
  most explicit step-by-step agent workflow in our corpus. Reference TTal's
  lifecycle alongside dontwannahearit's 11-step workflow (failure-sukit note)
  as two concrete instantiations of the full-cycle autonomous PR pattern.

- **Chapter 02 or Chapter 05 (Team Adoption)**: The agent identity/personality
  hypothesis (Claim 3) is worth a short note as an emerging pattern. If
  multiple tools converge on named persistent agents, that convergence becomes
  a testable design principle. For now: present as "one author's observation,
  corroborated by the functional-specialization evidence, but not yet a
  confirmed general principle."

## Extraction Notes

- Four sources were read for this note: (1) the HN post and its 4-comment
  thread, retrieved via the Algolia HN API; (2) the TTal GitHub README at
  `tta-lab/ttal-cli`; (3) the logos GitHub README at `tta-lab/logos`;
  (4) the author's FlickNote on multi-agent patterns, linked in a comment.
  All four were accessible at extraction time. The GitHub repos and FlickNote
  are live, unlike Kiln, which had disappeared before its extraction.
- The FlickNote at `dev.flicknote.app/notes/5a95cdcd-...` is a first-person
  design note by neilbb, not independently reviewed or peer-validated. It is
  the author explaining their own patterns. Treat as primary source on TTal's
  design rationale, not as independently corroborated claims.
- The logos README describes the `temenos` daemon for sandboxing. No additional
  documentation for `temenos` was accessible — it appears to be an unpublished
  companion project. The sandboxing details are therefore thin.
- Low engagement (6 points, 4 comments) means the thread has not been
  validated by the practitioner community. The architecture claims are coherent
  and the code is real, but real-world usage reports, failure modes, and
  performance characteristics are absent. Confidence is anecdotal throughout.
- Unlike Kiln (discussion-hn-kiln-orchestration, status: archived), TTal's
  artifacts are live and accessible. Status set to `current`; this may warrant
  a follow-up check in 60-90 days to confirm the project has not disappeared.
