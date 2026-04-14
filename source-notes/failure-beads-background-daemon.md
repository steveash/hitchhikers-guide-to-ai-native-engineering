---
source_url: https://news.ycombinator.com/item?id=46487580
source_type: failure-report
platform: hn
title: "Show HN: I replaced Beads with a faster, simpler Markdown-based task tracker"
author: wild_egg
date_published: 2026-01-04
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: current
confidence_overall: anecdotal
issue: "#17"
---

# Failure Report: Beads Background Daemon Degraded Six-Month Claude Code Workflow

> A practitioner running Claude Code continuously for six months with Beads
> (Steve Yegge's SQLite-backed task tracker) as the AI task layer found that
> Beads' background daemon progressively decayed in reliability — syncing the
> wrong things at the wrong times, getting slower with every release — until
> they ripped it out and wrote a simpler replacement (wedow/ticket): a single
> bash script storing tickets as markdown files with YAML frontmatter, no
> daemon, with dependency graph tracking as the core value. The source
> documents both the failure mode and the design choices that make the
> replacement durable.

## Source Context

- **Platform**: Hacker News Show HN (84 points, 51 comments, 2026-01-04); primary
  artifact is the GitHub repository https://github.com/wedow/ticket (725 stars,
  54 forks as of 2026-04-13). The HN post provides the failure narrative; the
  repo provides the replacement design and CLAUDE.md.
- **Author credibility**: wild_egg is an anonymous HN user with no verifiable
  prior track record, but the failure narrative is detailed, first-person, and
  covers six months of sustained usage with Claude Code — not a beginner
  complaint. The replacement tool (ticket) has 725 stars and 54 forks as of
  April 2026, indicating community resonance. The 51-comment HN thread shows
  significant engagement, with multiple commenters confirming the Beads
  frustration and contributing alternative approaches.
- **Community response**: Overall confirmatory. nmfisher found Beads' language
  off-putting and praised ticket's simplicity. azeirah praised the author for
  "distilling it to its core." Multiple comments discussed parallel use cases
  without disputing the Beads failure. Only one commenter (rollcat) criticized
  the bash implementation choice (arguing Python/Perl is more maintainable for
  embedded awk/jq scripts), which is a design choice disagreement, not a
  dispute of the failure.

## What Was Attempted

- **Goal**: Manage AI coding tasks across long-duration Claude Code sessions
  over a six-month period using a dedicated task-tracking tool optimized for
  AI agents.
- **Tool/approach**: Beads (https://github.com/steveyegge/beads) — Steve
  Yegge's task tracker for AI agents. Beads stores issues in a `.beads/`
  directory backed by a SQLite file and runs a background daemon that syncs
  state. The daemon is a key architectural feature: it watches for file changes
  and keeps the SQLite index synchronized.
- **Setup**: Single developer running Claude Code for long-duration agentic
  coding sessions continuously for six months, starting after Beads' October
  2025 release.

## What Went Wrong

- **Symptoms**: The author describes a progressive pattern:
  1. "Every release made it slower and more frustrating to use"
  2. "I started battling it several times a week"
  3. "Its background daemon took to syncing the wrong things at the wrong times"
  4. By the December 2025 holidays, it was causing enough friction to justify
     a complete replacement.

- **Severity**: Degraded quality escalating to workflow-disruption. Not a
  total failure (tasks were still tracked) but the tool became an active
  source of friction rather than a productivity aid.

- **Reproducibility**: Consistent — "several times a week" across the final
  months of usage. The failure worsened over time (release-to-release quality
  decay) rather than being episodic.

## Root Cause (if identified)

- **Author's diagnosis**: The background daemon syncing architecture was the
  root cause. The daemon's job is to keep the SQLite file synchronized with
  the markdown files in `.beads/`. Under sustained agentic usage (many
  creates, status changes, and reads), the daemon appears to have synced at
  incorrect times, leading to state inconsistency. Progressive feature
  additions to Beads made each release slower.

- **Our assessment**: The author's diagnosis is plausible and consistent with
  a well-known class of failure: background sync processes are fragile under
  high-frequency concurrent writes. AI agents create and modify many tickets
  rapidly; the daemon's sync logic may not have been designed for this
  throughput or concurrency pattern. The SQLite backing store also requires
  coordinated reads/writes, whereas plain file operations (as in ticket) are
  atomic at the OS level. The "every release got worse" pattern is consistent
  with a growing codebase accumulating edge cases rather than a single-point
  regression. This is third-party tool quality decay under sustained agentic
  use — a distinct failure class from Claude's own compaction or session-limit
  failures.

- **Category**: tool-limitation (architectural — background daemon sync is
  fragile under AI agent write throughput) + progressive quality decay
  (release-to-release regression under heavy usage)

## Recovery Path

- **What they switched to**: wedow/ticket — a single bash script (~1000
  lines) storing tickets as markdown files with YAML frontmatter in a
  `.tickets/` directory. No background process. No SQLite. Git-native.

- **Key design decisions in the replacement** (from README and source code):

  **Ticket file format**:
  ```yaml
  # .tickets/<dir-prefix>-<4-char-random>.md
  ---
  id: nw-5c46
  status: open
  deps: []
  links: []
  created: 2026-01-04T13:00:00Z
  type: task
  priority: 2
  assignee: git user.name
  ---

  # Add SSE connection management

  ## Description
  ...

  ## Acceptance Criteria
  ...
  ```

  **Agent integration** (from README):
  ```
  This project uses a CLI ticket system for task management. Run `tk help` when you need to use it.
  ```
  One line in CLAUDE.md or AGENTS.md. Claude Opus picks it up naturally.

  **Dependency graph commands** (core value proposition):
  ```bash
  tk dep <id> <dep-id>       # Add dependency (id depends on dep-id)
  tk dep tree <id>           # Show dependency tree
  tk dep cycle               # Find dependency cycles in open tickets
  tk ready                   # List tickets with all deps resolved
  tk blocked                 # List tickets with unresolved deps
  ```

  **ID format** (from generate_id() in source):
  ```bash
  # Prefix = first letter of each hyphenated segment of directory name
  # Suffix = 4-char alphanumeric random string
  # Example: project "next-wave" -> "nw-5c46"
  ```

- **Migrate from Beads**:
  ```bash
  tk migrate-beads      # Import from .beads/issues.jsonl (bundled plugin)
  git rm -rf .beads
  git add .tickets
  git commit -am "ditch beads"
  ```

- **Unresolved**: The author notes "mixed feelings" about the parent-directory
  walk for `.tickets/` (the script searches parent dirs to find the tickets
  store) — this previously caused bugs in Beads (presumably directory traversal
  finding the wrong store). The author inherited this behavior but is uncertain
  about it. Merge handling across worktrees/branches was asked in the HN thread
  and left unanswered.

## Extracted Lessons

### Lesson 1: Background daemon architecture is a liability for AI agent task management under sustained load
- **Evidence**: Author describes a progressive failure over months where Beads'
  "background daemon took to syncing the wrong things at the wrong times."
  wild_egg's replacement explicitly has no daemon. The README states: "without
  the need for keeping a SQLite file in sync or a rogue background daemon
  mangling your changes."
- **Confidence**: anecdotal (single practitioner, single tool, but the
  architectural analysis is sound — background daemons under high-frequency
  agent writes are a known concurrency challenge)
- **Actionable as**: When evaluating or designing task-tracking tools for AI
  agent workflows, treat "no background process" as a positive signal. Prefer
  tools where state is plain files and all writes are single-process operations.

### Lesson 2: Tool quality decay under sustained agentic usage is a distinct failure category
- **Evidence**: Beads worked well initially ("a massive unlock") then degraded
  over six months of heavy use. This is not a one-time failure but a trajectory.
  The author "started battling it several times a week" toward the end.
- **Confidence**: anecdotal (one data point, but the pattern is structurally
  coherent — tools not designed for high-volume agent interaction will surface
  edge cases that don't appear in light use)
- **Actionable as**: Evaluate tools under representative AI agent load before
  committing to them for long projects. A tool that works well for occasional
  human interaction may degrade under continuous agent CRUD at 10-100x human
  frequency.

### Lesson 3: Markdown files with YAML frontmatter are the optimal ticket format for AI agent consumption
- **Evidence**: The README explicitly states: "Tickets are markdown files with
  YAML frontmatter in `.tickets/`. This allows AI agents to easily search them
  for relevant content without dumping ten thousand character JSONL lines into
  their context window." The author contrasts this with Beads' JSONL format,
  which apparently dumps large payloads into the agent's context.
- **Confidence**: emerging (the context-efficiency claim is corroborated by
  general principles in our corpus about context-window economics; the specific
  file format is the author's design choice, not a rigorous benchmark)
- **Actionable as**: When choosing or designing AI-readable data stores, prefer
  small, individually-queryable files over large concatenated formats. Each
  ticket as its own file means the agent can grep for relevant content and read
  only what it needs.

### Lesson 4: Dependency graph traversal is the primary value of task tracking for AI agents, not status management
- **Evidence**: The README positions dependency tracking as the core value
  ("git-native ticket tracking... Dependency graphs, priority levels"). The `tk
  ready` and `tk blocked` commands (listing tickets with all deps resolved vs.
  unresolved) are the primary navigation interface. The author's reply in the HN
  thread confirms: wild_egg navigates 1,900 tickets primarily via `tk ready` and
  `tk blocked` — not by browsing all tickets. The `dep cycle` command (detect
  circular dependencies) addresses a specific AI agent anti-pattern where agents
  create mutually-blocking tickets.
- **Confidence**: anecdotal (author's own usage pattern)
- **Actionable as**: For orchestration workflows, prioritize task trackers that
  expose dependency state (`ready` / `blocked` queries) over those that only
  track status. An agent that can query "what can I work on right now?" needs
  dependency resolution, not just status fields.

### Lesson 5: Git-native ticket storage enables free versioning and IDE integration
- **Evidence**: Tickets in `.tickets/` are plain markdown files versioned
  alongside code in git. The README documents VS Code integration: ticket IDs
  appear in `git log` output and can be Ctrl+Clicked in VS Code to jump to the
  ticket file. The `migrate-beads` command does a straightforward file migration
  followed by `git rm -rf .beads && git add .tickets`.
- **Confidence**: settled (these are features, not claims, documented in the
  tool)
- **Actionable as**: Prefer ticket systems that store state as versioned files
  rather than databases. Git history then records when tickets were created,
  modified, and closed, alongside the code changes they correspond to.

### Lesson 6: Single-file tools with no runtime dependencies are more durable in agentic environments
- **Evidence**: ticket is one bash script (~1000 lines) requiring only bash,
  sed, awk, find (POSIX-standard). No daemon, no database, no server. The
  README states: "portable bash script requiring only coreutils." The tool can
  be installed by symlinking the script; it works on any POSIX system.
- **Confidence**: anecdotal (durability is a design property, not a measured
  outcome — though 725 stars and 54 forks suggest community adoption)
- **Actionable as**: When an AI agent tool becomes a source of friction (slow,
  inconsistent, requires maintenance), evaluate whether its architecture
  (daemon, database, network dependency) is the root cause. A tool that can
  fail independently of the rest of the system will eventually fail at the wrong
  time.

### Lesson 7: Agents use task tracker fields on create but rarely reference metadata afterward
- **Evidence**: wild_egg replies to lemming's HN question about which fields
  agents actually use: "Agents set fields on create but don't reference them
  afterward; author's orchestration layer relies heavily on them." The fields
  (type, assignee, priority, tags, external-ref) are set by agents during
  ticket creation but not queried by the agents themselves — they are consumed
  by the orchestration layer.
- **Confidence**: anecdotal (single practitioner's observation from their
  specific workflow)
- **Actionable as**: When designing agent task-tracking instructions, be aware
  that agents may not reliably read back fields they set. If orchestration
  depends on those fields, the orchestration layer (not the agent) should be
  the primary consumer. Don't rely on agents to check their own previously-set
  metadata.

## Cross-References

- **Corroborates failures in**:
  - `failure-decker-4hr-session-loss.md` — shares the theme "long-duration
    usage exposes tooling limits." Different failure class (Claude's compaction
    vs. third-party task tracker daemon degradation), but both document how
    tools that work fine in short sessions degrade under sustained agentic use.
    Together they cover two distinct long-session failure modes.
  - `practitioner-dadlerj-tin.md` — tin (conversation versioning, not ticket
    tracking) shares the design philosophy of git-native, file-based tooling.
    Pattern 3 in tin (Hooks as Automatic Behavior Injection) documents the
    success side of the same design space this source documents the failure of.
    tin is "this is how to do tool integration right"; this failure report is
    "this is what happens when the tool has a rogue daemon."
  - `discussion-hn-ttal-multiagent-factory.md` — TTal uses Taskwarrior for
    task state management in multi-agent workflows. wedow/ticket is a direct
    competitor in the same design space (agent-native task tracking). TTal
    accepts Taskwarrior's complexity for its feature set; ticket opts for
    simplicity. The trade-off is explicit.

- **Contradicts success in**: None in our corpus. No existing source note
  documents Beads as a success. The failure is novel.

- **Known issue**: Not a documented Beads issue as far as our corpus covers.
  The Beads project itself (steveyegge/beads) is not in our corpus.

- **Novel**: This is the first source note in our corpus documenting
  third-party tool quality decay under sustained agentic usage as a distinct
  failure class. Prior failure notes cover Claude's own compaction/amnesia
  failures (failure-decker, failure-claudemd-ignored-compaction,
  failure-hooks-enforcement-2k) — this is the first about an external tool
  degrading under agent load.

## Guide Impact

- **Chapter 04 (Long-duration sessions and tooling)**: Add the Beads → ticket
  pattern as the canonical example of third-party tool quality decay under
  sustained agentic use. Frame: tools designed for human interaction may not
  be designed for AI agent write throughput. Pair with failure-decker (Claude's
  own compaction) to cover both first-party and third-party long-session failure
  modes.

- **Chapter 03 or Ch04 (Choosing task trackers for AI workflows)**: Extract a
  "task tracker selection criteria" recommendation from this source:
  - No background daemons
  - File-system-based state (plain files, not SQLite)
  - Git-versionable by default
  - Dependency graph querying (`ready`/`blocked`) as first-class feature
  - Small per-ticket files, not monolithic JSONL dumps
  Cite wedow/ticket as the reference implementation and the Beads failure as
  the negative example.

- **Chapter 04 (Agent-native data format design)**: The markdown-files +
  YAML-frontmatter pattern is worth documenting explicitly. The author's framing
  — "without dumping ten thousand character JSONL lines into their context
  window" — gives a concrete, quotable reason for the design choice. This
  extends discussion-hn-ttal-multiagent-factory's external state pattern.

- **Chapter 04 (Dependency-graph task management)**: The `tk ready` / `tk
  blocked` command pattern as the core navigation interface for large ticket
  sets deserves a callout. 1,900 tickets navigated without browsing — the
  dependency graph is the index. This is a teachable design principle for
  agentic task management at scale.

## Extraction Notes

- The original post body in the issue is truncated in the scanner preview.
  The full first-person narrative comes from HN item 46487580, accessed via
  the Algolia HN API and the HN thread directly.
- The GitHub repo (wedow/ticket) has a CLAUDE.md, README.md, CHANGELOG.md,
  and the full bash implementation. All were read. The CHANGELOG confirms
  the initial release was 2026-01-02 (two days before the Show HN post) and
  the tool has been actively maintained through at least 2026-03-16.
- The author is "wild_egg" on HN — no real name, no affiliation verifiable.
  The tool's popularity (725 stars, 54 forks) is the credibility signal.
- The CLAUDE.md in the wedow/ticket repo explicitly instructs: "Always update
  the README.md usage content when adding/changing commands and flags" and
  documents the plugin system architecture for agent-facing command extension.
  This is a well-maintained CLAUDE.md, not boilerplate.
- The original Show HN post references "tic" not "ticket" — the repo was
  either renamed or the tool's working name changed between the post and the
  release. The canonical name is `ticket` (CLI: `tk`).
- The HN thread did not resolve the question of merge handling — how ticket
  state merges when two branches modify the same tickets. This is an open
  limitation for multi-worktree agentic workflows.
- 51 comments across 22 top-level threads were reviewed. No commenters
  disputed the Beads failure narrative. Several added complementary tool
  references (Beans, git-bug, Backlog.md, task-master.dev, git notes) but
  none claimed Beads worked well for them.
