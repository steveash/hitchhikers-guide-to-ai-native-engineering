---
source_url: https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/
source_type: blog-post
title: "My experience with Claude Code 2.0 and how to get better at using coding agents"
author: Sankalp (@dejavucoder)
date_published: 2025-12-27
date_extracted: 2026-04-08
last_checked: 2026-04-08
status: current
confidence_overall: emerging
issue: "hi-e93.2"
---

# Sankalp on Claude Code 2.0 (60% Handoff Rule + Custom /handoff Command)

> A working engineer's daily-use account of Claude Code 2.0 with concrete
> heuristics for context-window management. Coins (or popularizes) the
> "handoff at 60%" rule, describes a custom /handoff slash command for
> session restart, and gives the file paths used by Claude Code for
> commands and sub-agents. This is the practitioner anchor for Ch04's
> "session segmentation" and "restart/recovery pattern" sections.

## Source Context

- **Type**: blog-post (practitioner write-up)
- **Author credibility**: Sankalp (@dejavucoder) is a working software
  engineer who runs a coding-agent-focused blog and tweets actively about
  Claude Code, Codex, and Cursor. Multi-tool practitioner with hands-on
  daily use. Not a vendor; not a researcher; a working dev sharing a
  workflow.
- **Scope**: Personal workflow tactics for getting better results from
  Claude Code 2.0. Covers the context window threshold for handoff/compact,
  the custom /handoff command pattern, file paths for commands and
  sub-agents, /clear as a deliberate reset, and how plans and todos
  survive compaction. Does NOT cover team adoption, hooks, or security.

## Extracted Claims

### Claim 1: Handoff or compact when context reaches 60% on complex work
- **Evidence**: Author's daily-use heuristic. No experiment, but a clearly
  stated rule of thumb that's been picked up by other practitioners in the
  Dec 2025 - Apr 2026 window.
- **Confidence**: anecdotal (one practitioner; widely repeated but not
  benchmarked)
- **Quote**: "I would do a handoff or compact when I reach total 60% if
  building something complex."
- **Our assessment**: This is the manual analog of French-Owen's "smart half"
  rule (separate source). Sankalp's 60% is more permissive than French-Owen's
  ~50%, but both agree the practical limit is far below the harness's
  auto-compact trigger (~89% in Claude Code per
  research-wasnotwas-context-compaction). The spread of practitioner
  preferences (50-60%) is itself the finding: nobody who actually monitors
  context waits for the auto-compactor. Cite Sankalp's 60% as the
  "permissive" practitioner threshold and French-Owen's "smart half" as the
  "conservative" one; the truth is somewhere in between.

### Claim 2: Effective context windows are 50-60% of advertised
- **Evidence**: Author's direct observation from running near the auto-compact
  threshold and seeing degraded output.
- **Confidence**: emerging
- **Quote**: "Effective context windows are probably 50-60% or even lesser."
- **Our assessment**: Same observation as French-Owen's "smart half" under
  different framing. Use as the second corroborating practitioner data point
  for the section's lead claim. The convergence of two unrelated
  practitioners on the same 50-60% number is the strongest evidence we have
  that "stay in the smart half" is a real, replicable rule.

### Claim 3: Custom /handoff command pattern — Claude writes the session summary before /clear
- **Evidence**: Author's custom workflow.
- **Confidence**: emerging
- **Quote**: "I prefer to make Claude write what happened in current session
  (with some specific stuff) before I kill it and start a new one. I made a
  `/handoff` command for this."
- **Our assessment**: This is the cleanest, most-easily-adopted recovery
  pattern in the corpus. Instead of relying on lossy auto-compaction (which
  destroys architectural rationale per failure-decker-4hr-session-loss in a
  separate source), the user proactively asks the agent to write a structured
  handoff document, then /clears with a clean conscience. Use as the
  recommended "restart recovery pattern" for Ch04. Pair with Bswen's
  HANDOFF.md template (mentioned in extraction notes — separate source not
  pulled in here) for a fully-spec'd version.

### Claim 4: Claude Code file paths used for state and customization
- **Evidence**: Author's working configuration.
- **Confidence**: settled (matches Claude Code documented file paths)
- **Quote**: Project-level commands at `.claude/commands/`, global commands
  at `~/.claude/commands`, custom sub-agents at `.claude/agents/your-agent-name.md`.
- **Our assessment**: Useful as the canonical reference for "where do I put
  custom commands and sub-agents?" Many practitioners don't know there are
  three distinct locations. Cite in Ch02 (harness engineering) and Ch04
  (memory and persistence — these directories are how memory and
  customization persist across sessions).

### Claim 5: /clear is a deliberate reset for context bloat or model struggle
- **Evidence**: Author's stated workflow.
- **Confidence**: emerging
- **Quote**: "when the context window starts getting full or I feel the model
  is struggling with a complex task, I want to start a new conversation
  using `/clear`"
- **Our assessment**: /clear is not just a panic button; it's a tactical
  tool used proactively. Note the author's two distinct triggers: (1)
  context window filling, (2) model "struggling" (a quality signal that
  often correlates with long sessions). The "model is struggling" trigger is
  worth highlighting separately — it's a behavioral cue that the context
  has degraded, not just a token count.

### Claim 6: Plans and todos survive compaction as markdown files
- **Evidence**: Author's observation of how Claude Code's plan/todo features
  work.
- **Confidence**: settled (this is documented Claude Code behavior; matches
  research-wasnotwas-context-compaction Claim 5)
- **Quote**: "Plan and todo lists are stored as markdown file and they are
  persisted during compaction."
- **Our assessment**: This is a critical finding for Ch04: the plan file is
  the one piece of state Claude Code's harness explicitly preserves through
  compaction. Cross-reference with the wasnotwas finding that Claude Code
  re-injects "the active plan file" post-compaction. If you want state to
  survive, put it in the plan, not the conversation. This is the
  load-bearing technical justification for the "specs/plans as compressed
  context" Ch04 section.

### Claim 7: Use /context to monitor before deciding to handoff
- **Evidence**: Author's stated workflow.
- **Confidence**: settled
- **Quote**: (paraphrased) Author uses `/context` to check usage levels
  before taking handoff actions.
- **Our assessment**: /context is the diagnostic tool that makes the 60%
  rule actionable. Without /context, you can't know your fill level. Cite
  /context as the recommended discipline for any user trying to apply the
  60% rule.

## Concrete Artifacts

The post does not include the full /handoff command source, but sketches
the pattern:

```
# Custom /handoff command (conceptual)
# Triggered when context > 60% on complex work
# Claude writes a session summary including:
#   - Current state of the work
#   - Decisions made and why
#   - What's done, what's in progress
#   - Next steps for the next session
# User then /clears and starts fresh, reading the handoff doc
```

File path conventions confirmed by the author:

| Path                              | Purpose                       |
|-----------------------------------|-------------------------------|
| `.claude/commands/`               | Project-level slash commands  |
| `~/.claude/commands`              | Global slash commands         |
| `.claude/agents/<name>.md`        | Custom sub-agents             |

## Cross-References

- **Corroborates**: blog-french-owen-coding-agents-feb-2026 (the "smart
  half" / 50-60% effective window observation — two independent practitioners,
  same number)
- **Corroborates**: research-wasnotwas-context-compaction Claim 5 (Claude
  Code re-injects the active plan file after compaction; Sankalp confirms
  plans and todos persist as markdown)
- **Corroborates**: failure-decker-4hr-session-loss (decker shows what
  happens when you don't proactively handoff; Sankalp shows the workflow
  that prevents it)
- **Extends**: practitioner-dadlerj-tin (tin uses lifecycle hooks to
  auto-track conversations; Sankalp's /handoff is a lighter-weight,
  user-initiated version of the same idea — explicit checkpoint instead of
  automatic logging)
- **Novel**: The 60% threshold as a concrete number is original to this
  post in our corpus. French-Owen's "smart half" is qualitative; Sankalp
  is willing to commit to an actual percentage.

## Guide Impact

- **Chapter 04 (Session segmentation)**: This is the primary source for the
  section. Use the 60% rule as the lead recommendation. Pair with /context
  as the diagnostic, /handoff as the action, /clear as the reset.

- **Chapter 04 (The restart recovery pattern)**: Use Claim 3 (custom
  /handoff command) as the canonical pattern. Plus the failure-decker-4hr-
  session-loss case as the negative example (what happens if you don't).

- **Chapter 04 (Memory and persistence)**: Use Claim 6 (plans and todos
  survive compaction) as the load-bearing technical claim. Plans are the
  one form of state the harness will preserve for you. Use this to
  motivate the spec/plan pattern from a context-engineering angle, not just
  a workflow angle.

- **Chapter 02 (Harness Engineering)**: Cite Claim 4 (the three file path
  locations for commands and sub-agents) as the canonical reference for
  customization layout. Many users don't know about all three locations.

- **Chapter 04 (Tool choice)**: Sub-agents are first-class state that lives
  in `.claude/agents/<name>.md`. They are configured once and reused across
  sessions, making them a context-cheap form of customization. Cite as a
  contrast with MCP servers (which have permanent overhead per
  blog-bswen-mcp-token-cost).

## Extraction Notes

- The post is the earliest source in our Ch04 corpus that gives a specific
  threshold percentage for handoff. The "60% rule" has spread in the
  practitioner community since this post and is now widely cited; if Ch04
  uses the rule, attribute it to Sankalp.
- Sankalp's tone is matter-of-fact and undated for individual claims. The
  post is dated Dec 27, 2025, which puts it just inside our 2025-12-01
  inclusion bar. If we ever tighten the bar (e.g., to 2026-01-01), we
  would lose this source — flag for editorial review.
- The post discusses Claude Code 2.0 specifically. Claude Code has had
  several releases since (we are in April 2026); some of the file paths
  and command behaviors may have changed. The 60% heuristic is not
  version-specific.
- The author's framing of /handoff as a custom command (rather than a
  built-in) is itself instructive: when the user identifies a recurring
  workflow gap, the right move is to build a slash command, not to wait
  for the vendor to add a feature. This is a Ch02 pattern worth
  cross-citing.
- We did not pull the actual content of Sankalp's /handoff command from
  the post (the post does not include it). For a fully-specified
  HANDOFF.md template, see the bswen handoff coordination post (not yet a
  source note in this corpus).
