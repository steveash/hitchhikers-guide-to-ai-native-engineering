---
source_url: https://news.ycombinator.com/item?id=46874059
source_type: discussion
title: "Show HN: kiln.bot — Orchestrate Claude Code from GitHub"
author: elondemirock
date_published: 2026-02-03
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: archived (project disappeared ~56 days post-launch; repo and website inaccessible)
confidence_overall: anecdotal
issue: "#79"
---

# Show HN: kiln.bot — Orchestrate Claude Code from GitHub

> A brief Show HN tool announcement describing an architecture for orchestrating
> multiple local Claude Code instances using GitHub Projects as a control plane —
> notable for three concrete design decisions: polling over webhooks, all state in
> GitHub Issues, and one git worktree per issue. The project and its repository
> disappeared approximately 56 days after launch, making the HN post text the only
> recoverable artifact.

## Source Context

- **Type**: discussion (Show HN announcement, 8 points, 4 comments, 2026-02-03)
- **Author credibility**: elondemirock is anonymous on HN. No prior track record or
  affiliation verifiable. The post is the sole public artifact of a project that
  subsequently vanished; treat all claims as self-reported from an unverified single
  author. The engagement was low (8 points, 4 comments including one that is just
  "looks great"), reducing crowd-corroboration value. However, the architectural claims
  are specific and coherent, and the core design decisions (GitHub Projects control
  plane, polling, worktrees, issue-as-state) are independently sensible patterns, not
  marketing fluff.
- **Scope**: The post covers only the Kiln tool's high-level architecture and design
  rationale. It does not include code, configuration files, benchmarks, usage metrics,
  or failure modes. The GitHub repository (`agentic-metallurgy/kiln`) and the
  `kiln.bot` website, both referenced in the post, became inaccessible before the
  Prospector triage. No source beyond the HN post text could be read.

## Extracted Claims

### Claim 1: GitHub Projects columns map directly to Claude Code CLI commands — moving a card triggers agent dispatch

- **Evidence**: Author's design description: "orchestrates Claude Code instances on
  your local machine using GitHub projects as its control panel." The stated workflow
  is that column transitions in GitHub Projects invoke corresponding Claude Code CLI
  commands. A separate commenter (JJneid) confirms they already run Claude Code on GH
  issues manually, implying this automation fills a real gap.
- **Confidence**: anecdotal
- **Quote**: "Kiln orchestrates Claude Code instances on your local machine using
  GitHub projects as its control panel."
- **Our assessment**: The architecture is architecturally clean: GitHub Projects already
  has a Kanban-style board with configurable columns; mapping those columns to agent
  commands creates a no-extra-UI dispatch interface. The key insight is using an
  existing project-management surface as the orchestration control plane rather than
  building a new one. This is the most novel claim in the post. However, it's entirely
  self-reported — we have no independent confirmation it worked as described, no code,
  and no user reports beyond two brief positive comments.

### Claim 2: All context and state is stored in GitHub Issues — no local databases, no markdown files

- **Evidence**: Direct design rationale from the author: "All context and state is on
  GitHub (no markdown mess, no local DBs, easy recovery)."
- **Confidence**: anecdotal
- **Quote**: "All context and state is on GitHub (no markdown mess, no local DBs, easy
  recovery)."
- **Our assessment**: This is a concrete stance against the common pattern of using
  local markdown files (`.claude/context.md`, `tasks.md`) or local state databases for
  multi-agent coordination. Storing state in GitHub Issues means: (a) state persists
  across reboots without manual management; (b) state is visible in the same UI used to
  dispatch agents; (c) recovery from a crashed or killed session is a GitHub API call
  away rather than a local file-repair operation. The tradeoff — GitHub API rate limits,
  latency, and the risk of GitHub outages affecting agent state — is not addressed. The
  claim directly contradicts the "plans-as-local-files" pattern advocated by
  French-Owen and Sankalp (see Cross-References).

### Claim 3: Polling is architecturally preferred over webhooks for local agent orchestration

- **Evidence**: Author's explicit design rationale: "works behind VPN" and has "no
  external attack surfaces." No performance data or comparative study provided.
- **Confidence**: anecdotal
- **Quote**: "works behind VPN, no external attack surfaces" (paraphrased from the
  architectural description of polling vs. webhooks)
- **Our assessment**: The rationale is sound for the stated deployment scenario (local
  machine). Webhooks require an inbound network path from GitHub's servers to the
  local machine, which is blocked by most corporate VPNs and home NAT setups.
  Polling eliminates the inbound requirement entirely: the local process queries GitHub
  on a schedule. The tradeoff is latency (polling interval = minimum dispatch lag) and
  API call overhead. For a local developer tool where sub-second dispatch timing is not
  required, polling wins on operational simplicity. This is a well-reasoned design
  decision, not just a claim.

### Claim 4: Each GitHub Issue gets its own isolated git worktree

- **Evidence**: Author's description: "Claude creates the worktrees, researches the
  codebase, creates and implements the plan. Stores it in GitHub Issues." The one-
  worktree-per-issue pattern is implied by the issue-as-unit-of-work design.
- **Confidence**: anecdotal
- **Quote**: "Claude creates the worktrees, researches the codebase, creates and
  implements the plan."
- **Our assessment**: One git worktree per issue is the canonical isolation primitive
  for parallel agent work. It prevents file-locking conflicts when multiple Claude Code
  instances are running simultaneously on different tasks. This is consistent with
  community consensus (see Cross-References: failure-sukit-parallel-session-ceiling,
  blog-addyosmani-code-agent-orchestra). The claim is brief but credible — it is the
  standard architecture for this problem.

### Claim 5: The tool runs entirely locally against the user's existing Claude subscription, with no SaaS layer

- **Evidence**: Author's stated design constraint: "no auth trickery, runs locally"
  using "existing Claude subscriptions."
- **Confidence**: anecdotal
- **Quote**: "no auth trickery, runs locally" (uses existing Claude subscriptions)
- **Our assessment**: A significant design choice. "No auth trickery" means the tool
  does not proxy the Claude API or require users to share credentials with a third
  party. This reduces the security attack surface and eliminates per-call markup costs.
  The tradeoff is that the tool depends entirely on the Claude Code CLI's auth model
  and cannot offer token-level usage analytics or model routing without that
  infrastructure. Given the project's disappearance, this design choice may have
  constrained the monetization path, though this is speculative.

### Claim 6: The tool targets developers at Stage 6-7 on the Gas Town scale — those running 3-15 parallel terminal sessions

- **Evidence**: Author's explicit framing: "If you're around Stage 6-7 on the Gas Town
  scale, you may have 3-15 terminal windows open."
- **Confidence**: anecdotal
- **Quote**: "If you're around Stage 6-7 on the Gas Town scale, you may have 3-15
  terminal windows open."
- **Our assessment**: The "Gas Town scale" is a practitioner maturity framework for
  AI adoption. Stage 6-7 corresponds to developers already running multiple parallel
  Claude Code sessions. This framing tells us Kiln was not intended as an onboarding
  tool — it is targeting practitioners already at the terminal-multiplexing phase of
  the adoption curve. The scale itself is worth tracking; the addyosmani-code-agent-
  orchestra note mentions "Gastown" in passing as infrastructure for this project but
  does not extract the stage definitions. If a canonical source for the Gas Town stage
  definitions can be found, it should be enqueued for extraction.

### Claim 7: The orchestrator supports MCPs, extending Claude Code's native capabilities

- **Evidence**: Author's feature description: "Supports MCPs and anything else Claude
  can do."
- **Confidence**: anecdotal
- **Quote**: "Supports MCPs and anything else Claude can do."
- **Our assessment**: Thin claim. It says the tool passes through Claude Code's MCP
  support rather than restricting it. This is architecturally expected (if you're
  invoking Claude Code, MCP support comes along for free) but confirms the tool does
  not impose a restricted subset of Claude's capabilities. Not independently notable.

### Claim 8: The project vanished approximately 56 days after launch — both the GitHub repo and the website became inaccessible

- **Evidence**: HN commenter threecee (posting ~56 days after the original launch)
  reported: unable to find the page or the GitHub repo. The Prospector confirmed both
  `agentic-metallurgy/kiln` on GitHub and `kiln.bot` were inaccessible at triage time.
- **Confidence**: settled (confirmed by Prospector triage, consistent with commenter
  report)
- **Quote**: threecee: "What happened to kiln.bot? can't find the page or the github
  repo"
- **Our assessment**: The project's disappearance is itself a first-class signal.
  Multi-agent Claude Code orchestration is a high-churn area: tools appear, gain brief
  attention, then go private, pivot, or abandon. This is the second ecosystem-churn
  signal in our corpus after blog-french-owen's comment on fast-moving tooling. For
  the guide: the disappearance reinforces the principle that architectural *patterns*
  (GitHub Projects control plane, polling, worktrees, issue-as-state) are more durable
  than specific tool implementations. Extract the patterns; don't recommend specific
  tools that may disappear.

## Concrete Artifacts

The HN post is brief and contains no code, configuration files, or metrics. The only
extractable structural artifact is the architecture description:

```
Kiln Orchestration Architecture (from HN post text):

Control Plane:    GitHub Projects (Kanban board)
Dispatch Unit:    GitHub Issue (one worktree per issue)
State Store:      GitHub Issues (comments, status, plan text)
Polling Target:   GitHub API (not webhook receiver)
Execution Host:   Local machine (user's Claude Code subscription)
Agent:            Claude Code CLI instance per worktree
Extensions:       MCPs supported (pass-through)
```

### Commenter-Identified Use Pattern

JJneid's comment reveals the manual workflow Kiln was automating:

```
Manual (JJneid's existing workflow):
  1. Create a GitHub Issue
  2. Manually invoke Claude Code on that issue
  3. Claude researches and implements

Automated (Kiln's claimed workflow):
  1. Create a GitHub Issue
  2. Move issue card in GitHub Projects to trigger column
  3. Kiln invokes Claude Code automatically, creates worktree,
     stores plan and results back to the Issue
```

This shows Kiln was compressing steps 2-3 of the manual workflow into a single
project-board gesture — a UI affordance optimization, not a fundamental architectural
invention.

## Cross-References

- **Corroborates**:
  - **blog-addyosmani-code-agent-orchestra**: Osmani's Claim 11 specifically lists "git
    worktrees for isolation" as one of five concrete patterns to adopt. Kiln's one-
    worktree-per-issue architecture is a direct implementation of that recommendation,
    showing practitioners arrived at the same conclusion independently.
  - **failure-sukit-parallel-session-ceiling**: The sukit thread's community consensus
    is that "git worktrees + atomic tasks" is the infrastructure bridge that makes
    parallel Claude Code sessions viable. Kiln's design is exactly this pattern,
    confirmed from the supply side (a tool builder) vs. the demand side (a practitioner
    hitting failure modes).
  - **practitioner-dadlerj-tin**: Both Kiln and tin wrap Claude Code with automatic
    lifecycle management. tin uses Claude Code hooks (SessionStart/Stop/End). Kiln uses
    GitHub Projects column transitions. Both reduce orchestration friction to a single
    gesture. The architectural complement: tin handles the session lifecycle inside a
    single worktree; Kiln handles worktree creation and dispatch across multiple issues.

- **Contradicts**:
  - **blog-french-owen-coding-agents-feb-2026** and **blog-sankalp-claude-code-20**:
    Both French-Owen and Sankalp advocate externalizing state to the *local filesystem*
    (plan docs, task state files checked into git). Kiln advocates externalizing state
    to *GitHub Issues* instead. These are opposite choices for the same requirement
    (persist agent state across sessions). The GitHub-Issues approach has easier
    recovery and a visible UI; the local-filesystem approach avoids API dependencies
    and works offline. Neither source acknowledges the tradeoff the other is making.
    This is a conditioning variable (online-first vs. offline-first deployment
    preferences), not a deep contradiction — but practitioners choosing between these
    approaches need both data points.

- **Extends**:
  - **blog-addyosmani-code-agent-orchestra**: Osmani describes GitHub Projects as a
    control plane concept in passing (the "Factory Model" section). Kiln is the only
    concrete implementation of that concept in our corpus and extends Osmani's
    description with a specific dispatch mechanism (column transitions) and polling
    architecture rationale.

- **Novel**:
  - **GitHub Projects Kanban columns as agent-dispatch triggers**: No other source in
    our corpus describes this specific dispatch mechanism. The pattern (project
    management UI column = CLI invocation) is genuinely new to our corpus.
  - **Polling-over-webhooks rationale for local orchestration**: No existing note
    discusses the polling vs. webhook tradeoff for agent dispatch. The VPN-friendly,
    no-attack-surface rationale is a concrete operational argument worth capturing in
    the guide's harness engineering chapter.
  - **Project churn as ecosystem signal**: The disappearance of a tool 56 days post-
    launch is the first documented case in our corpus of agent-tooling churn. It
    provides an empirical argument for why the guide should teach patterns, not tools.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the polling-over-webhooks pattern under a
  new "Agent dispatch" section. Frame it as: "For local agent orchestration, polling
  the task source (GitHub Issues, a local task file) is more reliable than webhooks —
  it works behind VPNs, requires no inbound network path, and eliminates external
  attack surfaces. The tradeoff is dispatch latency equal to the polling interval."
  Cite this source alongside the sukit parallel-sessions thread.

- **Chapter 02 (Harness Engineering) or Chapter 01 (Daily Workflows)**: Add a
  note on "GitHub Projects as a control plane" as an emerging pattern for teams that
  already use GitHub for issue tracking. The Kiln architecture (columns → commands,
  issues → state, worktrees → isolation) is the most concrete instantiation of the
  "use existing infrastructure as orchestration UI" principle. Even though Kiln
  disappeared, the pattern it demonstrated is reproducible without the tool.

- **Chapter 03 (Safety and Verification, skeleton)**: The "all state in GitHub Issues"
  approach is a concrete answer to the session-recovery problem. When an agent crashes
  or a session is killed, state recovery means reading the relevant Issue — not
  reconstructing a local markdown file. Cite as one architectural option, with the
  caveat that it introduces an API dependency and rate-limit risk.

- **Chapter 05 (Team Adoption, skeleton)**: The project's disappearance in 56 days
  is the canonical example for a principle worth including: "In AI agent tooling, the
  half-life of specific tools is short. Learn the patterns the tools implement, not
  the tools themselves. The Kiln architecture (GitHub Projects control plane, polling,
  worktrees, issue-as-state) survived the tool's death because it is a pattern, not a
  product." This should be paired with French-Owen's observation that the tooling
  landscape is fast-moving.

## Extraction Notes

- **Severely limited source**: The HN post is short (~200 words of substantive
  content). The GitHub repo and website were inaccessible before the Prospector
  triage. This source note is therefore extracting from a self-promotional post
  with minimal supporting evidence. All claims are `anecdotal` by necessity.
- **No code artifacts**: No CLAUDE.md, settings.json, configuration examples, or
  implementation details are available. The architectural patterns described here
  are claims, not verified implementations.
- **Gas Town scale**: The post references the "Gas Town scale" (Stage 6-7 = 3-15
  terminal windows open). The addyosmani-code-agent-orchestra note mentions
  "Gastown" as infrastructure for this guide project, suggesting "Gas Town" may be
  a term of art originating from or associated with this project. The stage
  definitions (beyond stages 6-7) are not available in this source. If a canonical
  source for the full scale can be identified, it should be enqueued separately.
- **Ecosystem churn signal**: This is the only source in our corpus where the tool
  itself disappeared before extraction was complete. The Prospector correctly
  identified this as extractable because the architectural patterns, not the
  implementation, are the value.
