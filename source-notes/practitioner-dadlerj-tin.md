---
source_url: https://github.com/dadlerj/tin
repo: dadlerj/tin
stars: ~64
language: Go
project_type: developer tool (thread-based version control for conversational coding)
date_extracted: 2026-03-30
last_checked: 2026-03-30
commit_analyzed: main branch (HEAD as of 2026-03-30)
status: current
---

# Practitioner Profile: dadlerj/tin

> A self-referential AI developer tool that eats its own dog food: CLAUDE.md instructs agents to use tin's own CLI commands, while .claude/settings.json wires hooks that auto-track every conversation as a versioned thread. The configuration is notable for its prohibition on direct storage manipulation and its programmatic generation of slash commands from Go source code.

## Repo Context

tin is "git for AI coding conversations" -- a Go CLI that wraps git, treating conversation threads as the primary unit of change. It captures agent sessions (prompts, responses, tool calls, git state) as structured threads, stages and commits them alongside code. The project supports Claude Code (via hooks) and Amp (via `tin amp pull`). The README states it is "100% vibe coded" and "this README.md is the only human-edited file in this repo."

The repo includes a push/pull remote protocol (`tin serve`), a web viewer, merge support with thread conflict handling, and configuration commands. It is architecturally similar to git itself -- `.tin/` directory with threads/, commits/, refs/heads/, index.json (staging), HEAD.

## AI Configuration Inventory

| File | Present | Lines | Purpose |
|------|---------|-------|---------|
| `CLAUDE.md` | Yes | 78 | Project overview, CLI reference, prohibition on direct storage manipulation |
| `AGENTS.md` | Yes | 78 | Identical content to CLAUDE.md |
| `.claude/settings.json` | Yes | 47 | Four lifecycle hooks wiring tin's own hook handlers |
| `.claude/commands/branches.md` | Yes | 6 | Slash command: list tin branches |
| `.claude/commands/checkout.md` | Yes | 14 | Slash command: switch tin branches |
| `.claude/commands/commit.md` | Yes | 14 | Slash command: commit tin threads |
| `COMMANDS.md` | Yes | 260 | Full CLI reference (not AI config per se, but referenced context) |

**Total AI config files**: 6 (CLAUDE.md, AGENTS.md, settings.json, 3 slash commands)
**Total AI config lines**: ~237 lines
**Additional context files**: COMMANDS.md (260 lines), README.md (~170 lines)

No `.cursorrules`, `.cursor/`, `.editorconfig`, `agents.toml`, or `.github/workflows/` found.

## CLAUDE.md -- Verbatim Content

```markdown
# Tin

Thread-based version control for conversational coding. Wraps git, treating conversation threads as the primary unit of change.

## Important: Use Tin Commands

**Always use built-in tin commands instead of directly modifying `.tin/` storage on disk.** For example:
- Use `tin thread delete` instead of `rm .tin/threads/<id>.json`
- Use `tin add --unstage` instead of editing `.tin/index.json`

Direct file manipulation can leave the repository in an inconsistent state (e.g., orphaned staging entries, missing index updates).

## Quick Reference

```bash
tin init                  # Initialize (also runs git init if needed)
tin status                # Show current branch and staged threads
tin branch [name]         # List or create branches
tin checkout <ref>        # Switch branch/commit (restores git state)
tin add <thread-id>       # Stage a thread (or --all)
tin commit -m "msg"       # Commit staged threads
tin log                   # Show commit history
tin thread list           # List all threads
tin thread show <id>      # Display thread conversation
tin thread delete <id>    # Delete a thread (use -f for committed/active)
tin hooks install         # Install Claude Code hooks (--global for ~/.claude)
tin hooks uninstall       # Remove hooks
tin amp pull [id|count]   # Pull threads from Amp CLI
```

## Project Structure

```
cmd/tin/main.go           # Entry point
internal/
  commands/               # CLI command implementations
  model/                  # Message, Thread, TinCommit, Branch structs
  storage/                # .tin directory operations
  hooks/                  # Claude Code hook handlers + installation
```

## Data Model

- **Message**: hash (merkle chain), role, content, timestamp, tool_calls, git_hash_after
- **Thread**: id (first message hash), agent, messages[], parent refs for branching
- **TinCommit**: id, message, thread refs, git_commit_hash

Storage in `.tin/`: threads/, commits/, refs/heads/, index.json (staging), HEAD

## Agent Integrations

### Claude Code

Hooks auto-track conversations:
- `SessionStart` → new thread
- `UserPromptSubmit` → append human message, auto-stage
- `Stop` → append assistant response + tool calls + git hash
- `SessionEnd` → mark thread complete

Slash commands: `/branches`, `/commit [msg]`, `/checkout [branch]`

### Amp

Pull threads from Amp CLI:
```bash
tin amp pull                    # Pull latest thread
tin amp pull 5                  # Pull 5 most recent threads
tin amp pull T-019b7d09-...     # Pull specific thread by ID
tin amp pull https://ampcode.com/threads/T-...  # Pull by URL
```

Threads are deduplicated by Amp thread ID (stored in `AgentSessionID`).

## Building

```bash
go build -o tin ./cmd/tin
```
```

## AGENTS.md -- Content

AGENTS.md is byte-for-byte identical to CLAUDE.md. Both files contain the same 78 lines.

## Patterns Identified

### Pattern 1: Self-Referential Dogfooding -- Tool Instructs Agents to Use Itself

This is the defining pattern of this repo. tin is an AI developer tool, and its CLAUDE.md instructs the AI agent to use tin's own CLI commands. The agent working on tin's code is simultaneously a user of tin.

**Verbatim (CLAUDE.md, "Important: Use Tin Commands" section):**
> **Always use built-in tin commands instead of directly modifying `.tin/` storage on disk.** For example:
> - Use `tin thread delete` instead of `rm .tin/threads/<id>.json`
> - Use `tin add --unstage` instead of editing `.tin/index.json`

This goes further than just documentation -- the `.claude/settings.json` hooks automatically invoke `tin hook session-start`, `tin hook user-prompt`, `tin hook stop`, and `tin hook session-end` at every conversation lifecycle event. The agent's own session IS a tin thread.

**Cross-reference**: Novel. No existing profile shows a project whose CLAUDE.md instructs the agent to use the project's own product as part of the development workflow. Sentry's CLAUDE.md references internal tools (like `sentry` CLI) but not the product itself as the version control layer.

### Pattern 2: Prohibition on Direct Storage Manipulation

The single most prominent rule in CLAUDE.md is a prohibition -- do not directly modify `.tin/` files:

**Verbatim:**
> Direct file manipulation can leave the repository in an inconsistent state (e.g., orphaned staging entries, missing index updates).

This provides a concrete reason for the prohibition (inconsistent state), names specific failure modes (orphaned staging entries, missing index updates), and gives before/after examples (`rm .tin/threads/<id>.json` vs `tin thread delete`).

**Cross-reference**: Corroborates sentry's pattern of explicit prohibitions. Extends it by providing the *why* alongside the *what* -- sentry's prohibitions tend to be bare commands, while tin explains the failure mode.

### Pattern 3: Hooks as Automatic Behavior Injection

The `.claude/settings.json` configures four Claude Code lifecycle hooks:

```json
{
  "hooks": {
    "SessionEnd": [{"hooks": [{"type": "command", "command": "/Users/danieladler/Dev/tin/tin/tin hook session-end", "timeout": 30}]}],
    "SessionStart": [{"hooks": [{"type": "command", "command": "/Users/danieladler/Dev/tin/tin/tin hook session-start", "timeout": 30}]}],
    "Stop": [{"hooks": [{"type": "command", "command": "/Users/danieladler/Dev/tin/tin/tin hook stop", "timeout": 30}]}],
    "UserPromptSubmit": [{"hooks": [{"type": "command", "command": "/Users/danieladler/Dev/tin/tin/tin hook user-prompt", "timeout": 30}]}]
  }
}
```

Notable: The hook commands use a hardcoded absolute path (`/Users/danieladler/Dev/tin/tin/tin`) rather than relying on PATH resolution. This is the developer's local build path, committed to the repo. The `tin hooks install` command generates these dynamically using `findTinBinary()`, but the checked-in version reflects the developer's machine.

**Cross-reference**: Novel. No existing profile uses Claude Code hooks for automatic behavior injection. Sentry uses hooks implicitly (via the permission allowlist), but tin's hooks are silent background processes that run without the agent's awareness -- the agent does not invoke them; they fire automatically on every lifecycle event.

### Pattern 4: Slash Commands with Scoped Tool Permissions

The three slash commands (`.claude/commands/`) each declare minimal `allowed-tools` in their YAML frontmatter:

**branches.md:**
```
allowed-tools: Bash(tin branch:*)
```

**checkout.md:**
```
allowed-tools: Bash(tin checkout:*), Bash(tin branch:*)
```

**commit.md:**
```
allowed-tools: Bash(tin commit:*), Bash(tin status:*)
```

Each command grants only the specific tin subcommands it needs. The `/checkout` command also grants `tin branch:*` because it may need to list branches first if no argument is given.

**Cross-reference**: Corroborates sentry's granular permission allowlists but at a finer grain -- sentry allows 60+ command prefixes globally, while tin scopes permissions per slash command. This is a more restrictive, per-operation permission model.

### Pattern 5: Programmatic Generation of AI Config from Source Code

The slash commands checked into `.claude/commands/` are also embedded as string literals in `internal/hooks/install.go`. The `tin hooks install` command writes these files programmatically. This means the AI config files are both:
1. Checked into the repo as static files (for agents to read)
2. Generated from Go source code (for `tin hooks install` to write to any project)

The `InstallSlashCommands` function includes collision detection -- it checks if an existing command file contains tin-related content before overwriting, and warns if a non-tin command already exists at that path.

**Cross-reference**: Novel. No existing profile shows AI config files that are also generated artifacts of the project's own build system. This dual nature (static config + generated output) is unique to self-referential tooling projects.

### Pattern 6: CLAUDE.md as Combined User Manual and Agent Instructions

Unlike most CLAUDE.md files which give terse rules, tin's CLAUDE.md reads like a condensed user manual: project description, quick reference with 14 commands, project structure map, data model explanation, and integration documentation. It serves double duty -- both instructing the AI agent working on the code AND documenting the tool for human users.

**Cross-reference**: Contradicts postgres_dba's "extreme brevity" pattern and partially contradicts sentry's "thin redirect" pattern. Extends NetPace's approach of putting detailed context in CLAUDE.md, but without the repetition-for-emphasis style. The 78-line length is moderate -- between postgres_dba's 30 lines and NetPace's 1200+ total lines.

### Pattern 7: AGENTS.md as CLAUDE.md Mirror

AGENTS.md contains identical content to CLAUDE.md. This is likely intentional -- AGENTS.md is read by tools other than Claude (e.g., Cursor, Amp, Copilot), so duplicating ensures all agents receive the same instructions regardless of which file their tool reads.

**Cross-reference**: Contradicts sentry's pattern where CLAUDE.md redirects to AGENTS.md with `@AGENTS.md`. Sentry uses AGENTS.md as the single source of truth with CLAUDE.md as a pointer; tin uses both as identical copies. This is a simpler but less maintainable approach -- any edit must be applied to both files.

### Pattern 8: Conversational Slash Command Design

The slash commands implement a conversational pattern: if the user provides an argument, execute immediately; if not, show context and ask:

**Verbatim (checkout.md):**
> If $ARGUMENTS is provided, checkout that branch:
> ```
> tin checkout $ARGUMENTS
> ```
>
> If no branch name is provided, first run `tin branch` to show available branches, then ask the user which branch to checkout.

**Verbatim (commit.md):**
> If no message is provided, first run `tin status` to show what will be committed, then ask the user for a commit message before running the commit.

**Cross-reference**: Extends sentry's slash command approach. Sentry's commands tend to be fire-and-forget; tin's commands implement a two-phase interaction pattern (show context, then prompt for input) when arguments are missing.

### Pattern 9: Auto-Git-Commit on Session End

The `HandleSessionEnd` hook handler automatically creates a git commit when a Claude Code session ends, staging all changed files and using the first human prompt as the commit message:

From `claude_code.go`:
```go
commitMsg := formatGitCommitMessage(thread)
```

The commit message format is `[tin <short-id>] <first human message>`. This means every Claude Code session that modifies files results in an automatic git commit -- the agent does not need to remember to commit.

**Cross-reference**: Novel. No existing profile implements automatic git commits. This inverts the typical pattern where CLAUDE.md tells the agent *how* to commit; here, the hook system commits *for* the agent silently.

## Anti-Patterns Observed

### 1. Hardcoded Absolute Path in Committed settings.json

The `.claude/settings.json` contains `/Users/danieladler/Dev/tin/tin/tin` -- the developer's local build path. This will not work for any other contributor or machine. The `tin hooks install` command generates the correct path dynamically, but the committed file is machine-specific.

### 2. CLAUDE.md / AGENTS.md Duplication

Maintaining identical content in two files creates a synchronization burden. If one is edited and the other is not, agents reading different files will receive different instructions. Sentry's redirect pattern (`@AGENTS.md` in CLAUDE.md) avoids this.

### 3. No Explicit Prohibitions Beyond Storage Manipulation

The only "do not" rule concerns direct `.tin/` file manipulation. There are no prohibitions about code style, testing requirements, commit message format, or common Go mistakes. For a "100% vibe coded" project, this is perhaps intentional -- the developer may prefer minimal constraints. But it means the agent has wide latitude for stylistic decisions.

### 4. No CI Configuration

There are no GitHub Actions workflows. For a Go project, this means there is no automated testing or linting. The CLAUDE.md does not mention tests or testing at all.

### 5. No .gitignore for .tin/ State Files

The `.gitignore` only excludes `tin`, `.tin/`, and `.DS_Store`. The `.tin-session` state file (created by hooks in the `.tin/` directory) is covered by the `.tin/` exclusion, but there is no protection against accidentally committing other transient state.

## Notable Custom Commands

| Command | Lines | Allowed Tools | Behavior |
|---------|-------|---------------|----------|
| `/branches` | 6 | `Bash(tin branch:*)` | Run `tin branch`, display output |
| `/checkout [branch]` | 14 | `Bash(tin checkout:*)`, `Bash(tin branch:*)` | If arg: checkout. If not: list branches, ask user |
| `/commit [message]` | 14 | `Bash(tin commit:*)`, `Bash(tin status:*)` | If arg: commit with message. If not: show status, ask for message |

All three commands are generated programmatically by `tin hooks install` from string literals in `internal/hooks/install.go`.

## Cross-References Summary

| Pattern | vs Sentry | vs NetPace | vs postgres_dba |
|---------|-----------|------------|-----------------|
| Self-referential dogfooding | Novel | Novel | Novel |
| Storage manipulation prohibition | Corroborates (with richer rationale) | Corroborates | N/A |
| Lifecycle hooks | Novel | N/A | N/A |
| Per-command tool permissions | Extends (finer grain) | N/A | N/A |
| Programmatic config generation | Novel | Novel | Novel |
| CLAUDE.md as user manual | Contradicts (thin redirect) | Extends (verbose) | Contradicts (brevity) |
| AGENTS.md duplication | Contradicts (redirect pattern) | N/A | N/A |
| Conversational slash commands | Extends | N/A | N/A |
| Auto-commit on session end | Novel | Novel | Novel |

## Guide Impact

### Chapter: "Self-Referential Tooling" (or "Dogfooding Your AI Config")

tin is the canonical example of a project that uses CLAUDE.md to instruct the agent to use the project's own product. This creates a unique feedback loop: the agent's development session is simultaneously a test case for the tool. This pattern is likely to become more common as AI developer tools proliferate.

Key insight: When your project IS an AI developer tool, the CLAUDE.md serves triple duty -- (1) agent instructions, (2) product documentation, (3) integration test specification.

### Chapter: "Claude Code Hooks"

tin is the first profile to demonstrate lifecycle hooks in `.claude/settings.json`. The four-hook pattern (SessionStart, UserPromptSubmit, Stop, SessionEnd) provides a complete model for transparent background behavior injection. The guide should discuss:
- Hooks run silently -- the agent is unaware they fired
- Timeout configuration (30s per hook)
- The risk of committing machine-specific absolute paths

### Chapter: "Slash Command Design"

tin's slash commands demonstrate the two-phase interaction pattern: execute immediately with arguments, or show context and prompt without. The per-command `allowed-tools` scoping is a best practice for least-privilege command design.

### Chapter: "Prohibitions and Rationale"

tin's single prohibition (no direct `.tin/` manipulation) is a model for effective rule writing: it states the rule, gives concrete examples of what to do instead, and explains the failure mode. Compare with sentry's bare prohibition lists and NetPace's emoji-marked MUST NEVER rules.

### Chapter: "CLAUDE.md vs AGENTS.md Strategies"

tin's duplication strategy (identical files) contrasts with sentry's redirect strategy (`@AGENTS.md`). The guide should discuss tradeoffs: duplication is simpler but creates sync risk; redirection is DRY but assumes all tools support the redirect syntax.

## Extraction Notes

- **Branch analyzed**: `main` (default branch)
- **100% vibe coded claim**: The README states "this README.md is the only human-edited file in this repo!" -- meaning all Go source, all AI config files, and the COMMANDS.md were generated by AI agents. This makes the AI config files themselves artifacts of AI coding, creating an interesting recursive provenance question.
- **Hardcoded path**: The `.claude/settings.json` contains a path specific to the developer's macOS machine (`/Users/danieladler/Dev/tin/tin/tin`). This is a development artifact, not a portable configuration.
- **No tests mentioned**: Neither CLAUDE.md nor any configuration file mentions testing. The `go.mod` was not examined but no test infrastructure was found in the directory listing.
- **Amp integration**: tin supports both Claude Code (hooks) and Amp (pull-based), making it one of the first multi-agent-tool version control systems. The CLAUDE.md documents both integration paths.
