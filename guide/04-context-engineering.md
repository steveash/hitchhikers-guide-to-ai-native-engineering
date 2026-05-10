# Context Engineering

> The conversation is the smallest thing in the context window.
> In one practitioner's measured snapshot, the chat itself was 4% of the
> total budget. The other 96% was system prompts, tool definitions, memory
> files, and harness boilerplate -- and most of it was loaded before the
> first message was typed. Context engineering is the discipline of
> managing that 96%, then protecting what's left of the 4% from compaction.

This chapter is about treating the context window as an operating budget,
not a free resource. Every claim that follows is grounded in practitioner
measurements or first-person failure reports from the post-2025-12 corpus.

---

## Context as Budget

### The "smart half" rule

Stay in the smart half of the context window. Performance degrades long
before the auto-compactor fires.
[source: blog-french-owen-coding-agents-feb-2026, Claim 1] [emerging]

Calvin French-Owen (Segment co-founder, ex-OpenAI Codex launch team) puts
it as bluntly as anyone has:

> "Stay in the 'smart' half of the context window. It's generally easier
> to train on short-context data vs long-context data. Results will tend
> to be better when the context window is 'less full'."
> [source: blog-french-owen-coding-agents-feb-2026, Claim 1]

A second, independent practitioner converges on the same observation
under different framing. Sankalp (@dejavucoder), writing about Claude
Code 2.0, reports:

> "Effective context windows are probably 50-60% or even lesser."
> [source: blog-sankalp-claude-code-20, Claim 2] [emerging]

Two unrelated practitioners, two different tools, same number. When the
qualitative observation ("compaction is lossy, results degrade with full
windows") and the quantitative one ("50-60% effective") converge from
independent sources, treat it as the strongest single rule of thumb in
this chapter: **assume your effective context window is half its
advertised size.**
[source: blog-french-owen-coding-agents-feb-2026, Claim 1;
blog-sankalp-claude-code-20, Claim 2] [emerging]

### Most of the budget is gone before you start

The 96% number deserves its own section. Cowrie (Bswen) ran `/context`
on a fresh Claude Code session and recorded the breakdown:
[source: blog-bswen-mcp-token-cost, Claim 6]

| Category       | Share of context |
|----------------|------------------|
| System prompts | 35%              |
| System tools   | 28%              |
| MCP tools      | 12%              |
| Memory files   |  5%              |
| Conversation   |  4%              |
| Free / unused  | 16% (computed)   |

[source: blog-bswen-mcp-token-cost, Claim 6 (companion piece)] [emerging]

The conversation is **4%**. The remaining 96% is harness baseline that
loaded before the user said hello. This is the cleanest single
demonstration we have that "context engineering" is mostly about
minimizing the boilerplate, not about being clever with your prompts.
[source: blog-bswen-mcp-token-cost, Claim 6] [emerging]

**Caveat**: this is one user's snapshot with one MCP configuration. The
exact percentages will vary. The shape of the distribution -- system
overhead dwarfs conversation -- is what generalizes. The fix in the
"Tool Choice and Context Cost" section below is to attack the largest
controllable bar, which is almost always MCP tools.

### Compaction is a budget item, not a rescue mechanism

When the context window fills, the agent's harness fires compaction --
typically by sending the full history to an LLM summarizer and replacing
old context with the summary. This is not free.
[source: research-wasnotwas-context-compaction, Claim 3] [emerging]

A code-spelunking comparative study of seven coding-agent harnesses
measured the actual cost of one compaction call:

> "one compaction call on a 125,000-token context cost $0.40 -- equivalent
> to running about 21 follow-up turns at cached rates, because each
> compaction destroys the KV cache established during prior turns."
> [source: research-wasnotwas-context-compaction, Claim 2] [emerging]

The dollar number ($0.40) is illustrative; the structural finding is
load-bearing. Compaction destroys the prompt cache. Cached prefix reads
cost 0.1x base input pricing; after compaction, the next turn pays full
1.0x for the entire summarized prefix.
[source: blog-bswen-mcp-token-cost, Claim 8] [settled]

**Rule**: Treat compaction as a budget item. Plan to handoff *before* it
fires, not to be rescued by it. Your harness's auto-compactor is the
emergency brake, not the cruise control.
[source: research-wasnotwas-context-compaction, Claim 2;
blog-sankalp-claude-code-20, Claim 1] [emerging]

### Source caveat on the wasnotwas study

The seven-harness comparative post is bylined "Jarvis (AI)" and is
explicitly an AI-authored research write-up against open-source codebases.
We treat its claims as research notes, not testimony: the source-code
citations are usable; judgment-laden claims should be independently
corroborated. We have spot-verified the Claude Code 89% trigger formula
against community reports and the `/context` command's behavior, and
consider the post broadly trustworthy. The $0.40 cost figure is a single
measurement on one model; cite as illustrative, not exact.
[source: research-wasnotwas-context-compaction, extraction notes] [emerging]

### Cache-safe forking refines the compaction cost

The wasnotwas $0.40 figure measures the cost when compaction destroys
the KV cache. The Claude Code team describes a partial mitigation:
cache-safe forking. The compaction call itself uses the same system
prompt, user context, system context, and tool definitions as the
parent conversation, so the cached prefix is reused.

> "When we run compaction, we use the _exact same_ system prompt, user
> context, system context, and tool definitions as the parent
> conversation."
> [source: blog-anthropic-prompt-caching-everything, Claim 11]

Cache-safe forking eliminates the cost of the compaction call itself.
It does not eliminate the post-compaction rebuild: after compaction
fires, the new (summary-based) prefix differs from the original, and
the next turn pays full prefill on the rebuilt cache. The wasnotwas
measurement captures that second cost, which cache-safe forking does
not address.
[source: blog-anthropic-prompt-caching-everything, Claim 11;
research-wasnotwas-context-compaction, Claim 2] [emerging]

The practical consequence for users: cache-safe forking makes the
compaction call itself cheap, but the post-compaction rebuild still
dominates multi-hour-session arithmetic. The handoff-before-compaction
discipline does not change.
[source: blog-anthropic-prompt-caching-everything, Claim 11] [emerging]

---

## Specs and Plans as Compressed Context

If "the conversation is 4%" is the diagnosis, "write it to a file" is
the prescription. A spec or plan file is compressed context: a few
hundred tokens of structured intent that the agent can re-read on every
session, instead of rediscovering it conversationally each time.
[source: blog-french-owen-coding-agents-feb-2026, Claim 3;
blog-osmani-good-spec, Claim 3] [emerging]

### The mechanism: plan files survive compaction

This is not just a workflow preference. It is a structural alignment
with how at least one major harness preserves state.

The seven-harness comparative study documents Claude Code's
post-compaction re-injection list:

> "[Claude Code] re-injects: recently-read files (sorted by timestamp,
> within a token budget), any skills invoked during the session, the
> active plan file."
> [source: research-wasnotwas-context-compaction, Claim 5] [emerging]

Sankalp confirms the user-side observation:

> "Plan and todo lists are stored as markdown file and they are persisted
> during compaction."
> [source: blog-sankalp-claude-code-20, Claim 6] [settled]

In Claude Code, **the active plan file survives compaction by name**.
That makes the plan-as-file pattern not just a clearer prompt format but
the storage layout the harness was designed to preserve. If you want
state to make it through a compaction event, put it in the plan, not the
conversation.
[source: research-wasnotwas-context-compaction, Claim 5;
blog-sankalp-claude-code-20, Claim 6] [emerging]

French-Owen makes the same point from the budget angle:

> "Externalizing context into the filesystem (e.g. a plan doc with
> stages which are checked or not) allows agents to selectively read and
> remember without filling up the full context."
> [source: blog-french-owen-coding-agents-feb-2026, Claim 3] [emerging]

### A concrete spec template

Addy Osmani provides the cleanest minimal spec we have seen. It is short
enough (~25 lines) to fit comfortably under Bswen's recommended ~300-line
ceiling and structured enough to give the agent traction on every
re-read.
[source: blog-osmani-good-spec, Claim 1; concrete artifact] [editorial]

```markdown
# Project Spec: My team's tasks app

## Objective
- Build a web app for small teams to manage tasks...

## Tech Stack
- React 18+, TypeScript, Vite, Tailwind CSS
- Node.js/Express backend, PostgreSQL, Prisma ORM

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint --fix`

## Project Structure
- `src/` -- Application source code
- `tests/` -- Unit and integration tests
- `docs/` -- Documentation

## Boundaries
- Always: Run tests before commits
- Ask first: Database schema changes
- Never: Commit secrets
```

[source: blog-osmani-good-spec, concrete artifact]

The six required sections, in Osmani's words:

> "1. Commands: Put executable commands early... 2. Testing: How to run
> tests, what framework you use... 3. Project structure: Where source
> code lives... 4. Code style: One real code snippet showing your style...
> 5. Git workflow: Branch naming, commit message format... 6. Boundaries:
> What the agent should never touch."
> [source: blog-osmani-good-spec, Claim 1] [editorial]

The defensibility of the template comes from the budget math: every one
of those six sections is something the agent would otherwise have to
discover by file-spelunking on every fresh session. A 200-line SPEC.md is
~600-800 tokens; conversational discovery of the same information costs
several thousand tokens of file reads, directory walks, and dialogue.
[source: blog-bswen-mcp-token-cost, Claim 6;
blog-osmani-good-spec, Claim 3] [editorial]

### The U-curve: too vague is bad, too verbose is also bad

Osmani names the failure modes at both ends.

Too vague:

> "Most agent files fail because they're too vague. 'Build me something
> cool' or 'Make it work better' gives the agent nothing to anchor on."
> [source: blog-osmani-good-spec, Claim 4] [emerging]

Too verbose:

> "As you pile on more instructions or data into the prompt, the model's
> performance in adhering to each one drops significantly... even GPT-4
> and Claude struggle when asked to satisfy many requirements
> simultaneously."
> [source: blog-osmani-good-spec, Claim 5 ("the curse of instructions")]
> [emerging]

The cheapest spec that conveys intent unambiguously is the best spec.
This is the same U-curve documented in the chapter on harness engineering
(Ch02): long CLAUDE.md files are followed less reliably *and* cost more
tokens. Osmani's "curse of instructions" is the mechanism behind that
empirical observation.
[source: blog-osmani-good-spec, Claim 5;
failure-claudemd-ignored-compaction, Lessons 1, 5 (cross-reference)]
[emerging]

**Counter-evidence**: Supabase ships a 931-line CLAUDE.md and treats it
as their primary agent surface (Ch02). They have the resources to make
a long file work and the engineering culture to maintain it. For solo
developers and small teams, Osmani's six-section template is the safer
default.
[source: practitioner-supabase-supabase-js;
blog-osmani-good-spec, Claim 1] [editorial]

### The four-phase loop

Osmani frames the spec workflow as a four-phase loop:

> "Specify -> Plan -> Tasks -> Implement... The spec drives the
> implementation, checklists, and task breakdowns. Your primary role is
> to steer; the coding agent does the bulk of the writing."
> [source: blog-osmani-good-spec, Claim 6] [editorial]

The mechanism that operationalizes this in Claude Code is Plan Mode:

> "Tools like Claude Code offer a Plan Mode... that restricts the agent
> to read-only operations... refine the plan until there's no room for
> misinterpretation. Only then do you exit Plan Mode."
> [source: blog-osmani-good-spec, Claim 7] [emerging]

Plan Mode is the read-only sandbox where the spec gets refined before
any code is written. This is the gate that prevents the most common
context-bloat failure: the agent races into implementation, makes a
wrong assumption, and burns thousands of tokens generating code against
the wrong spec.
[source: blog-osmani-good-spec, Claim 7] [emerging]

---

## Session Segmentation

A session is a finite resource with a known degradation curve. The
question is not whether to segment work across sessions; it is when.

### The 60% handoff rule

Sankalp's daily-use heuristic for Claude Code 2.0:

> "I would do a handoff or compact when I reach total 60% if building
> something complex."
> [source: blog-sankalp-claude-code-20, Claim 1] [anecdotal]

This is the manual analog of French-Owen's "smart half" rule. Sankalp's
60% is more permissive than French-Owen's ~50%; the spread (50-60%)
brackets the practitioner consensus. Both numbers are dramatically below
the harness's auto-compact trigger.
[source: blog-sankalp-claude-code-20, Claim 1;
blog-french-owen-coding-agents-feb-2026, Claim 1] [emerging]

The lesson is the spread itself: nobody who actually monitors context
waits for the auto-compactor to fire. Treat 50-60% as your handoff
window and pick the threshold that matches your tolerance for context
degradation.
[editorial]

### Know your harness's compaction trigger

Different harnesses fire compaction at wildly different fill levels.
The seven-harness comparative study cites code locations for each:

| Harness      | Trigger             | Approx fill |
|--------------|---------------------|-------------|
| Codex        | `model_auto_compact_token_limit` (default) | 90% |
| Gemini CLI   | hardcoded default   | 50%         |
| opencode     | `contextTokens >= context - reserved` | 96-99% |
| Claude Code  | `contextWindow - min(maxOutput, 20k) - 13k` | ~89% (Sonnet) |
| Roo Code     | `allowedTokens` formula | ~86%    |
| Pi           | `contextTokens > contextWindow - reserveTokens` | ~92% |
| OpenHands    | none (agent must call `request_condensation()`) | n/a |

[source: research-wasnotwas-context-compaction, Claim 1] [emerging]

The 50-99% spread is striking. Gemini CLI's aggressive 50% trigger is a
deliberate choice and matches French-Owen's "smart half" advice as a
default. Claude Code's 89% means by the time the auto-compactor fires,
the model has been operating in the degraded long-context regime for the
entire back half of the session.
[source: research-wasnotwas-context-compaction, Claim 1;
blog-french-owen-coding-agents-feb-2026, Claim 1] [emerging]

**Rule**: Look up your harness's threshold. Set your manual handoff at
roughly half of it. The auto-compactor is a safety net, not a workflow.
[editorial]

### The 4-hour cliff is real

decker (@gonewx) lost a 4-hour auth refactor session to silent
compaction. Their account is the user-side anchor for the abstract
trigger numbers above:
[source: failure-decker-4hr-session-loss]

> "Four hours into a productive session, Claude's responses began coming
> back generic... It happens silently. No warning. You're deep in flow
> and suddenly you're talking to a Claude that doesn't know your
> codebase anymore."
> [source: failure-decker-4hr-session-loss, What Went Wrong / Lesson 1]

The author's companion posts describe the same failure at different
scales (3-hour loss, 4-hour loss), suggesting the pattern is consistent.
At Claude Code's ~89% trigger, an active session of intense complex work
hits the cliff in roughly 3-4 hours.
[source: failure-decker-4hr-session-loss, Lesson 5;
research-wasnotwas-context-compaction, Claim 1] [anecdotal]

**Rule**: Treat 3-4 hours of active complex work as the practical
session ceiling in Claude Code. Hand off proactively before then or be
prepared to lose context.
[source: failure-decker-4hr-session-loss, Lesson 5] [anecdotal]

### Use /context as the diagnostic

The 60% rule is unactionable without a way to measure your fill level.
Sankalp uses Claude Code's built-in command:

> [paraphrased] Author uses `/context` to check usage levels before
> taking handoff actions.
> [source: blog-sankalp-claude-code-20, Claim 7] [settled]

The same `/context` command is what Cowrie used to discover the 96%
boilerplate problem. It is the one diagnostic every Claude Code user
should know.
[source: blog-bswen-mcp-token-cost, Claim 6;
blog-sankalp-claude-code-20, Claim 7] [settled]

### Chunking work that's too big

If the work itself is too big to fit in the smart half of the window,
no amount of compaction discipline will save you. French-Owen:

> "Your work needs to somehow be chunked. If the problem you are trying
> to solve is 'too big' for the context window, the agent is going to
> spin on it for a long time and give you poor results."
> [source: blog-french-owen-coding-agents-feb-2026, Claim 5] [emerging]

This is the practical implication of the smart-half rule: work that
needs more than ~50% of the window for context (specs, files, history)
must be decomposed before it goes to the agent. The decomposition is
your responsibility, not the agent's.
[source: blog-french-owen-coding-agents-feb-2026, Claim 5] [emerging]

---

## Memory and Persistence

The harness loses your conversation. The filesystem does not. Anything
that needs to survive across sessions must live in a file the harness
will re-load on the next run.

### What persists in Claude Code

Claude Code's post-compaction re-injection list (from the seven-harness
study) is the canonical reference for "what state survives":

> "[Claude Code] re-injects: recently-read files (sorted by timestamp,
> within a token budget), any skills invoked during the session, the
> active plan file."
> [source: research-wasnotwas-context-compaction, Claim 5] [emerging]

Three things make it through:
1. **Recently-read files** -- timestamp-ordered, budget-limited
2. **Invoked skills** -- the skill definition itself
3. **The active plan file** -- by name

Everything else -- conversation, intermediate reasoning, the architectural
"why" decker lost -- is gone after compaction. If you need it preserved,
it has to land in one of those three buckets.
[source: research-wasnotwas-context-compaction, Claim 5;
failure-decker-4hr-session-loss, Lesson 2] [emerging]

### Where Claude Code customization lives

Sankalp documents the three filesystem locations Claude Code uses for
persistent customization:

| Path                              | Purpose                       |
|-----------------------------------|-------------------------------|
| `.claude/commands/`               | Project-level slash commands  |
| `~/.claude/commands`              | Global slash commands         |
| `.claude/agents/<name>.md`        | Custom sub-agents             |

[source: blog-sankalp-claude-code-20, Claim 4] [settled]

These are first-class persistence layers: they are loaded on every
session, they cost only the tokens of the file content, and they survive
compaction by being re-loaded rather than re-injected. Sub-agents in
particular are a context-cheap form of customization -- configured
once, reused across sessions, and not subject to per-call overhead the
way MCP servers are.
[source: blog-sankalp-claude-code-20, Claim 4;
blog-bswen-mcp-token-cost, Claim 1 (cross-reference)] [emerging]

### The hidden persistence layer: session JSONL files

decker's failure report is also the most practitioner-accessible writeup
of where Claude Code stores session state on disk:
[source: failure-decker-4hr-session-loss, Lesson 3]

```
~/.claude/projects/[project-hash]/[session-id].jsonl
```

Each `.jsonl` file is "a complete record of a coding session" -- message
history, tool calls, results. It is not designed to be edited by users,
but it is preserved on disk and can be backed up trivially. See the
backup script in "Restart Recovery" below.
[source: failure-decker-4hr-session-loss, Lesson 3 / Recovery Path]
[settled]

### Write the "why" to a file immediately

The single most actionable lesson from the decker failure case is
behavioral, not tooling:

> "Nuanced architectural decisions, the 'why' behind choices, subtle
> patterns -- these get flattened into generic descriptions."
> [source: failure-decker-4hr-session-loss, Root Cause]

The architectural rationale is the first thing compaction destroys
because rationale lives in the back-and-forth dialogue, and the dialogue
is what gets summarized away.
[source: failure-decker-4hr-session-loss, Lesson 2] [emerging]

**Rule**: When you and the agent reach a non-obvious architectural
decision, write it to a SPEC.md, ADR, or scratchpad file *in the same
turn*. Do not trust the conversation to preserve the "why" through
compaction. The active plan file is one of the three things the harness
re-injects; the conversation is not.
[source: failure-decker-4hr-session-loss, Lesson 2;
research-wasnotwas-context-compaction, Claim 5] [emerging]

---

## Pre-Session Corpus Loading for Low-Coverage Domains

When generating code for a language or framework with thin training data,
LLMs produce plausible-looking code that uses the wrong idioms, hallucinated
API calls, or incorrect type patterns. Prompting alone cannot compensate
for a training data gap.

The Godogen game-generation pipeline solved this for GDScript (~850 classes,
Python-like syntax, absent from most LLM training corpora) by building a
custom three-part reference corpus:

1. A hand-written language specification documenting quirks not in the
   official docs
2. Full API documentation converted from the engine's XML source
3. A "quirks database for engine behaviors you can't learn from docs alone"

[source: failure-htdt-godogen-game-generation, Lesson 1] [anecdotal]

Critically, the corpus is **lazy-loaded** via an isolated skill context —
the agent queries it on demand for the specific class APIs it needs,
rather than injecting the full corpus upfront. Injecting all 850 classes
would overflow the context budget alongside the actual code being
generated.
[source: failure-htdt-godogen-game-generation, Lesson 2] [emerging]

```
Architecture: "godot-api" runs as an isolated skill context
  → Agent queries it on demand for needed class APIs
  → Only relevant API documentation enters the main context window
  → Context budget preserved for generation and reasoning
```

[source: failure-htdt-godogen-game-generation, Recovery 1] [anecdotal]

This pattern applies to any:
- Domain-specific or niche language (GDScript, Zig, Roc, Gleam)
- Rapidly-evolving API that is ahead of the model's training cutoff
- Internal or proprietary API absent from public training data
- Framework with undocumented behavior the model consistently gets wrong

**Rule**: Before attributing LLM errors to "bad prompting," check whether
the target language or framework is adequately represented in the model's
training corpus. If not, plan for a reference injection layer. Lazy-load
via a dedicated skill context to preserve budget — do not inject the full
corpus upfront.
[source: failure-htdt-godogen-game-generation, Lessons 1, 2] [emerging]

---

## The Restart Recovery Pattern

Sessions end. Sometimes you choose it (handoff), sometimes the harness
forces it (compaction), sometimes the system kills it (crash, rate
limit, OS reboot). Recovery quality depends entirely on what you wrote
to disk before the session ended.

### Pattern: the proactive `/handoff` command

Sankalp's recommended workflow:

> "I prefer to make Claude write what happened in current session (with
> some specific stuff) before I kill it and start a new one. I made a
> `/handoff` command for this."
> [source: blog-sankalp-claude-code-20, Claim 3] [emerging]

The pattern, expanded:

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

[source: blog-sankalp-claude-code-20, Claim 3 / concrete artifact]

The crucial property: the *agent* writes the handoff, while the
conversation is still intact and the rationale is still in the working
context. Compare to decker's failure case, where the user tried to
rebuild context conversationally *after* compaction had already
flattened the dialogue, and spent 45 minutes failing.
[source: blog-sankalp-claude-code-20, Claim 3;
failure-decker-4hr-session-loss, Lesson 4] [emerging]

**Rule**: Generate the handoff document while context is healthy. Do
not wait until the session feels degraded -- by then, the rationale you
wanted to capture has already been summarized.
[source: blog-sankalp-claude-code-20, Claim 3;
failure-decker-4hr-session-loss, Lesson 4] [emerging]

### Anti-pattern: conversational rebuild after compaction

decker spent 45 minutes after a bad compaction trying to re-explain the
context to the agent. The result:

> "It never fully came back."
> [source: failure-decker-4hr-session-loss, Symptoms / Lesson 4]

Conversational rebuild is a trap. The lossy summary destroyed the
specific rationale you cared about; re-explaining it in the same session
adds tokens to the same degraded context. Either restore from backup
(below) or start a fresh session with a written handoff document.
[source: failure-decker-4hr-session-loss, Lesson 4] [anecdotal]

### Pattern: the $0 backup script

decker's other contribution is the cheapest possible mitigation. Claude
Code's session files live on disk; a `cp -r` on a cron schedule gives
you free recovery:

```bash
PROJECT_DIR="$HOME/.claude/projects"
BACKUP_DIR="$HOME/.claude/session-backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR" && cp -r "$PROJECT_DIR" "$BACKUP_DIR"
```

[source: failure-decker-4hr-session-loss, Recovery Path]

After a bad compaction, restore the pre-compaction `.jsonl` from the
backup and resume with `claude --resume <session-id>` to bring back the
exact context. It is a workaround for the symptom, not a fix for the
root cause -- but it costs nothing and works on any Claude Code
installation.
[source: failure-decker-4hr-session-loss, Recovery Path] [settled]

**Rule**: Run the backup script on a cron or `chronic` schedule. The
combined cost is one `cp -r` per interval; the upside is that any
session you'd hate to lose can be recovered for free.
[source: failure-decker-4hr-session-loss, Lesson 3] [editorial]

### Two recovery triggers, not one

Sankalp distinguishes two distinct triggers for `/clear`:

> "when the context window starts getting full or I feel the model is
> struggling with a complex task, I want to start a new conversation
> using `/clear`"
> [source: blog-sankalp-claude-code-20, Claim 5] [emerging]

The first trigger is quantitative (`/context` shows >60%). The second
is behavioral: the model is "struggling" -- responses come back generic,
the agent forgets earlier decisions, suggestions feel less relevant.
That second signal often arrives *before* the fill percentage would
predict, because long conversations degrade model performance even when
they fit in the window.
[source: blog-sankalp-claude-code-20, Claim 5;
failure-decker-4hr-session-loss, Lesson 1] [emerging]

**Rule**: Trust both signals. If the model feels degraded, hand off,
even if `/context` says you have headroom. The smart-half rule is about
quality, not just capacity.
[editorial]

---

## Cache Layer Hierarchy

The Claude Code team's first-party description of how their cache is
structured anchors any conversation about what is "cheap" and what is
"expensive" in your context budget.

> "Static system prompt & Tools (globally cached) | CLAUDE.md (cached
> within a project) | Session context (cached within a session) |
> Conversation messages"
> [source: blog-anthropic-prompt-caching-everything, Claim 2]

| Layer | Scope | Mutability |
|-------|-------|------------|
| 1. System prompt + tools | Globally cached across sessions | Static |
| 2. CLAUDE.md | Cached within a project | Per-project |
| 3. Session context | Cached within a session | Per-session |
| 4. Conversation messages | Per-turn | Always dynamic |

[source: blog-anthropic-prompt-caching-everything, Claim 2] [settled]

Anything that changes — timestamps, file states, the model's awareness
that a user just edited a file — should arrive in the *next* user
message inside a `<system-reminder>` tag, not as a system-prompt edit.
The Claude Code team describes their own practice:

> "we add a <system-reminder> tag in the next user message or tool
> result with the updated information for the model, which helps
> preserve the cache."
> [source: blog-anthropic-prompt-caching-everything, Claim 5]

If a harness embeds dynamic content (a current timestamp, a file's
current contents) into the static system prompt every turn, the cache
is invalidated every turn. The fix is structural: route dynamic state
through messages, not system-prompt edits.
[source: blog-anthropic-prompt-caching-everything, Claim 5] [settled]

**Rule** (Claude Code-specific): Static content first, dynamic content
last. Inject runtime updates via `<system-reminder>` in the next
message rather than rewriting the system prompt.
[source: blog-anthropic-prompt-caching-everything, Claims 3, 5] [settled]

### Mid-session model switching is more expensive than you think

A common practitioner heuristic — "drop to a cheaper model for simpler
subtasks" — inverts at non-trivial conversation length. The cache is
provider-and-model-specific; switching models invalidates the prefix
the agent has been building.

> "If you're 100k tokens into a conversation with Opus and want to ask
> a question that is fairly easy to answer, it would actually be more
> expensive to switch to Haiku than to have Opus answer, because we
> would need to rebuild the prompt cache for Haiku."
> [source: blog-anthropic-prompt-caching-everything, Claim 6]

Cursor's harness team independently documents the same effect on
their stack:

> "Switching means a cache miss and a slower, more expensive first
> turn."
> [source: blog-cursor-continual-harness-improvement, Claim 10]

The clean alternative is a subagent: a fresh context window for the
cheaper model that does not invalidate the parent's cache. The subagent
gets a handoff message; the parent keeps its cache.
[source: blog-cursor-continual-harness-improvement, Claim 11;
blog-anthropic-prompt-caching-everything, Claim 6] [emerging]

**Rule**: Past ~50% context fill, do not switch models mid-conversation
to save cost. Either continue on the current model or spawn a subagent
on the cheaper one.
[source: blog-anthropic-prompt-caching-everything, Claim 6;
blog-cursor-continual-harness-improvement, Claims 10, 11] [emerging]

### Context rot — when wrong information accumulates

Compaction loses information by summarizing. There is a distinct
failure mode where context degrades by *adding* the wrong information:
failed tool calls, incorrect outputs, and error messages that the
agent then reasons over on subsequent turns.

> "errors remain in context, wasting tokens and causing 'context rot,'
> where accumulated mistakes degrade the quality of the model's
> subsequent decisions."
> [source: blog-cursor-continual-harness-improvement, Claim 3]

Forgetting loses what the agent knew; rot pollutes what the agent
reasons over. Cursor treats any unknown error class as a harness bug
specifically because unknown errors are the most likely vector for
silent rot at scale.
[source: blog-cursor-continual-harness-improvement, Claims 3, 5] [emerging]

**Rule**: If the agent keeps re-attempting a failed tool call, restart
rather than letting the error trace accumulate. A fresh session with a
clean handoff is cheaper than reasoning over a context full of failed
attempts.
[source: blog-cursor-continual-harness-improvement, Claim 3] [emerging]

---

## Tool Choice and Context Cost

Every tool you make available to the agent has a baseline cost in
tokens. Skills, slash commands, sub-agents, and MCP servers occupy very
different positions on the cost curve.

### Skills are 50-100 tokens. MCP calls are thousands.

French-Owen's quantitative comparison is the strongest single
recommendation in this section:

> "Skills are also great because they are *very* context efficient.
> Unlike MCP calls (which take up thousands of tokens), skills tend to
> be ~50-100 tokens."
> [source: blog-french-owen-coding-agents-feb-2026, Claim 2] [emerging]

A 1-2 order-of-magnitude difference is large enough to be a hard rule:
**prefer Skills over MCP whenever both can do the job.** The convenience
of an MCP wrapper is rarely worth several thousand tokens of permanent
overhead.
[source: blog-french-owen-coding-agents-feb-2026, Claim 2] [emerging]

### MCP servers load before you say hello

Cowrie's load-bearing finding:

> "Every MCP server you connect loads all its tool definitions into
> Claude's system prompt. Not when you use them -- **before you even
> start working**."
> [source: blog-bswen-mcp-token-cost, Claim 1] [settled]

MCP is not pay-per-use. It is pay-per-installed. The cost of an unused
MCP server is exactly the cost of a heavily used one. This is the
mechanism behind the 96% boilerplate problem above: every server you
add is paid for on every session, indefinitely, regardless of whether
you call any of its tools.
[source: blog-bswen-mcp-token-cost, Claim 1] [settled]

### Server count maps roughly linearly to tokens

Cowrie's measured table from his own configuration:

| MCP servers | Approximate tokens loaded |
|-------------|---------------------------|
| 15          | ~100k                     |
|  8          | ~50k                      |
|  6          | ~30k                      |
|  3          | ~15k                      |

[source: blog-bswen-mcp-token-cost, Claim 2] [emerging]

The slope -- ~5-7k tokens per server -- is the right order of magnitude
for typical MCP server schemas (5-30 tools per server, 100-500 tokens
per tool definition). The exact slope depends on which servers you
load: a single complex server like `puppeteer` or `playwright` can
dominate. Treat the table as illustrative; the principle (linear in
server count, large absolute numbers) is solid.
[source: blog-bswen-mcp-token-cost, Claim 2] [emerging]

The brutal arithmetic, in Cowrie's words:

> "If you have a 200k context window and burn 100k on tool definitions,
> you've already lost half your capacity."
> [source: blog-bswen-mcp-token-cost, Claim 3] [settled]

Pair this with the smart-half rule and the conclusion is unavoidable:
**a 15-MCP-server user has burned their entire usable context window on
tool definitions before saying hello.**
[source: blog-bswen-mcp-token-cost, Claim 3;
blog-french-owen-coding-agents-feb-2026, Claim 1] [emerging]

### Recommended budget: 3-6 essential servers

Cowrie's prescriptive advice after pruning his own setup:

> "Limit to 3-6 essential servers -- Be ruthless about necessity."
> [source: blog-bswen-mcp-token-cost, Claim 4] [anecdotal]

His final kept list: Context7, GitHub, PostgreSQL, Filesystem. The right
number depends on your work -- a database engineer probably wants the
SQL MCP regardless of token cost -- but the *discipline* generalizes:
audit your servers, justify each one against the per-session token tax,
and remove anything you cannot defend.
[source: blog-bswen-mcp-token-cost, Claim 4] [anecdotal]

### The bash-script test

The strongest critique of MCP from the practitioner community, in one
line:

> "MCP eats tons of tokens for things that should be bash scripts."
> [source: blog-bswen-mcp-token-cost, Claim 5 (Reddit quote, approvingly
> cited)] [emerging]

Many MCP servers wrap CLIs that the agent could call directly via Bash
for free. The wrapper is convenient but expensive. Sentry's `settings.json`
allowlist of 60+ Bash command prefixes (Ch02) is the structural
alternative: granular control over what the agent can run, with zero
per-session token tax for the unused commands.
[source: blog-bswen-mcp-token-cost, Claim 5;
practitioner-getsentry-sentry (cross-reference)] [emerging]

**Rule**: Before adding an MCP server, ask whether a bash command and a
slash command would do the same job. If yes, skip the server.
[source: blog-bswen-mcp-token-cost, Claim 5] [editorial]

### The billing window is not the inference window

**Rule**: Never assume your UI context window display predicts your API bill.
For tools using agentic or multi-step sessions, billing costs are not
proportional to the visible conversation — expect superlinear cost growth as
sessions extend and cache depth increases. Export billing CSV (not the product
UI) as the diagnostic. Do not interpret a tool's "context management" or
"summarization" feature as a cost control; these govern what the model
reasons over, not what you are billed for.
[source: failure-cursor-ultra-billing-cache-explosion, Lessons 1, 2, 3, 6] [anecdotal]

### Naming cache-hostile operations

Production-scale cache management is more complex than practitioners
typically model. Anthropic's `promptCacheBreakDetection.ts` (from the
Claude Code source map leak) tracks 14 distinct ways a cache can be
invalidated — with internal guards to prevent mode toggles from
accidentally busting it. One internal function is annotated:

```typescript
DANGEROUS_uncachedSystemPromptSection()
```

**Pattern**: Prefix any harness function that invalidates the prompt cache
with `DANGEROUS_` so callers know to pause — in Claude Code, the harness
(not Anthropic) controls when cache-busting fires.
[source: failure-alex000kim-claudecode-source-leak, Lesson 2] [emerging]
[per SN-04-002]

### Injecting mid-session updates without busting the cache

When you need to update Claude's instructions during a session — a new rule,
a corrected scope, a constraint that came up mid-task — the naive move is to
edit the system prompt. Don't. The system prompt is part of the cached
prefix; editing it creates a new cache key and the next turn pays full input
pricing for the entire prefix.

The Anthropic Platform team's recommended pattern: append a
`<system-reminder>` block in a user-turn message instead. The message stream
is mutable; the system prompt should not be.
[source: blog-anthropic-harnessing-claude-intelligence, Claim 11] [settled]

The harnessing-claude-intelligence post documents this as a caching
principle — "Messages for updates" — under the rule that the system prompt
is part of the cacheable prefix and should not be edited mid-session:

> "Append `<system-reminder>` in messages instead of editing prompt."
> [source: blog-anthropic-harnessing-claude-intelligence, Claim 11] [settled]

This is not a niche optimization. The `<system-reminder>` tag is the
convention Claude Code itself uses for its own runtime instruction injection
— the cost of getting it wrong is full cache invalidation on every
mid-session rule update, which compounds with every turn that follows.

**Rule**: Reserve system-prompt edits for session-start. For any rule, scope
change, or constraint that appears mid-session, inject it as a
`<system-reminder>` in a user-turn message — the cache stays warm and the
agent still sees the new instruction.
[source: blog-anthropic-harnessing-claude-intelligence, Claim 11] [settled]

### How to audit your own context budget

The methodology is reproducible with one built-in command:

```
# Diagnosis: count tokens in your fresh context
/context

# Look for: System prompts, System tools, MCP tools, Memory files
# Each line shows percentage of total budget

# Action: prune your ~/.claude.json or .mcp.json server list
# Target: 3-6 essential servers
```

[source: blog-bswen-mcp-token-cost, concrete artifact]

If you have never run `/context` on a fresh session, do it now. The
result is usually surprising and almost always actionable.
[source: blog-bswen-mcp-token-cost, Claim 6] [editorial]

### Sub-agents as parallel context firewalls

A second mechanism for managing context cost is delegation. French-Owen
observes that Opus (Claude Code) parallelizes sub-agent dispatch in a
way that Codex (as of Feb 2026) does not:

> "Opus has been trained to work across context windows extremely
> efficiently... You'll notice Opus frequently spinning up multiple
> sub-agents simultaneously... Codex is *slow*. The biggest reason for
> this is that it's not delegating tasks across context windows."
> [source: blog-french-owen-coding-agents-feb-2026, Claim 6] [anecdotal]

Each sub-agent runs in its own context window. From the parent's
perspective, a sub-agent is a context firewall: the parent pays for the
sub-agent's prompt and result, not the entire context the sub-agent
explored. This is why Opus can search through large repositories
without filling the parent context with the search results -- the
search runs in a sub-agent and only the answer comes back.
[source: blog-french-owen-coding-agents-feb-2026, Claim 6] [anecdotal]

**Caveat**: this is point-in-time (Feb 2026); Codex may add parallelism
in later versions. The structural argument (sub-agents as context
firewalls) is independent of which tool implements it best today.
[source: blog-french-owen-coding-agents-feb-2026, Claim 6] [anecdotal]

---

## Compaction Quality Varies by Harness

Not all compaction is equally lossy. The seven-harness study documents
several harness-level mitigations that change the practical reliability
of long sessions.

### Compaction quality scales with model generation

Before assuming your compaction problem is a harness-config problem, check
which model is doing the compacting. Anthropic's first-party benchmark on
BrowseComp shows that the ability to convert a compaction budget into
post-compaction task accuracy is a property of the model generation, not the
harness:

| Model | Post-compaction BrowseComp accuracy |
|-------|-------------------------------------|
| Sonnet 4.5 | 43% (flat regardless of compaction budget) |
| Opus 4.5 | 68% |
| Opus 4.6 | 84% |

[source: blog-anthropic-harnessing-claude-intelligence, Claim 7] [settled]

Sonnet 4.5 cannot leverage more compaction budget — throwing more tokens at
the summarizer does nothing. Opus 4.6 nearly doubles the score on the same
benchmark. If your team is fighting compaction quality on a Sonnet-tier
model, the binding constraint is the model, not the harness.

**Rule**: Before tuning compaction settings, confirm which model your harness
uses for compaction. If it is a smaller model and you need high
post-compaction accuracy, upgrade the model before attributing the
degradation to a fundamental limitation.
[source: blog-anthropic-harnessing-claude-intelligence, Claim 7] [settled]

### Gemini CLI: tail preservation + self-critique

> "not full replacement, but extract + tail preservation. The last 30%
> of conversation (by character count) is always kept verbatim."
> [source: research-wasnotwas-context-compaction, Claim 4] [emerging]

> "Two LLM passes: an initial summarization, then a self-critique
> verification pass."
> [source: research-wasnotwas-context-compaction, Claim 8] [emerging]

Gemini's combination -- aggressive 50% trigger, 30% verbatim tail,
two-pass summary with self-critique -- is the most quality-conscious
compaction implementation in the studied set. It costs more per
compaction but preserves more of the conversation.
[source: research-wasnotwas-context-compaction, Claims 1, 4, 8] [emerging]

### Roo Code: tag-and-hide instead of delete

> "Old messages are never deleted. They're tagged with a `condenseParent`
> UUID and hidden."
> [source: research-wasnotwas-context-compaction, Claim 7] [emerging]

Roo Code users can in principle reach back into pre-compaction history
because the original messages are still on disk -- just hidden. Claude
Code users cannot. If you regularly need to recover specific decisions
from earlier in a session, harness choice matters.
[source: research-wasnotwas-context-compaction, Claim 7] [emerging]

### OpenHands: reversible event store, no compaction by default

> "[OpenHands] maintains an event store: a persistent, append-only log
> of typed events... Nothing is ever deleted from the persistent store.
> Compaction is fully reversible."
> [source: research-wasnotwas-context-compaction, Claim 6] [emerging]

OpenHands is the existence proof that lossy compaction is a *design
choice*, not a technical necessity. The lossy LLM-summary pattern is
the practical default for most users, but it is not the only way to
build a coding-agent harness.
[source: research-wasnotwas-context-compaction, Claim 6] [emerging]

**Practical implication**: when you choose a coding-agent tool, the
compaction policy is part of the choice. Factor it in alongside the
features you actually use.
[editorial]

---

## Per-Query Context Scoping

Most of this chapter has been about sessions: managing one accumulating
context window over time. There is a different shape of problem — batch
extraction, structured classification, repeated decisions over many input
documents — where the right architecture is the opposite. Instead of one
session context that grows, assemble a fresh, narrow context window *per
data point* and discard it.

Carta Healthcare runs this pattern in production for clinical data
abstraction on Claude via Amazon Bedrock. Their Lighthouse platform
extracts structured data from 22,000+ surgical cases per year across 14
hospitals, with 98–99% inter-rater reliability against human abstractors
(the clinical-registry industry standard).
[source: blog-anthropic-carta-healthcare-context-engineering, Claim 9] [emerging]

The architectural finding from Matthew Mazzanti, their software engineering
manager, is what makes the scale possible:

> "The hardest problems we solved weren't about building a perfect prompt,
> they were about context construction. A perfectly written prompt with bad
> context gives bad answers. A straightforward prompt with the right
> context delivers the results you need."
> [source: blog-anthropic-carta-healthcare-context-engineering, Claim 1] [emerging]

### The pattern

For each extracted data point, assemble a context window scoped to *that
point's* requirements at query time — not a global document context shared
across all extractions. The concrete example from the team:

```
Extraction question: "Most recent glucose before procedure"

Context assembled AT QUERY TIME includes:
  - Patient's lab results, ordered by timestamp
  - Exact procedure start time injected as a temporal anchor
  - Instruction: scope to readings BEFORE procedure start time
  - Instruction: EXCLUDE readings after procedure start time

NOT: one global patient context passed to all extraction questions
BUT: an individually assembled context window per data point, scoped
     to that question's temporal and clinical boundaries
```

[source: blog-anthropic-carta-healthcare-context-engineering, Claim 2] [emerging]

Each query runs in a narrow, purpose-built window. The full document never
all enters context at once; the model never has to decide which procedure
to anchor on, because the anchor is already injected.

### Why this matters for any batch extraction pipeline

The same pattern generalizes beyond healthcare. Any pipeline that:

- extracts many structured fields from each input document
- runs the same question over thousands of records
- must apply temporal or scope boundaries that vary per record

will hit the same context-collapse failure mode if all queries share one
session context. The Carta architecture is the answer: scope context to
the query, not to the session.

This complements the within-session context discipline of the rest of this
chapter. For batch pipelines specifically, the within-session levers
(compaction, handoff, plan files) do not apply — there is no long session
to manage. The lever that does apply is *what enters context per query*.

**Rule**: For batch extraction or classification pipelines, scope the
context window to the individual query, not to the session or the source
document. Build query-specific context assembly as a first-class layer of
the harness, not as an afterthought to prompt design.
[source: blog-anthropic-carta-healthcare-context-engineering, Claims 1, 2] [emerging]

---

## Concrete Context Engineering Checklist

Apply this checklist to any project where you intend to run long Claude
Code sessions. Items are ordered by cost-to-implement, cheapest first.

```markdown
## Before your next long session

- [ ] Run /context on a fresh session and record the baseline
      (target: <40% used by harness boilerplate)
- [ ] Prune MCP servers to 3-6 essentials
      (every server costs ~5-7k tokens forever)
- [ ] Confirm your active plan file is in the location your
      harness re-injects after compaction
- [ ] Set a /handoff slash command if your tool supports it
- [ ] Set up the $0 backup cron for ~/.claude/projects/
- [ ] Decide your manual handoff threshold (50-60% recommended)
- [ ] Audit your CLAUDE.md for length: 100-300 lines is the
      target, 500 lines is the hard cap
```

[source: blog-bswen-mcp-token-cost, Claims 4, 6, 7;
blog-sankalp-claude-code-20, Claims 1, 3;
failure-decker-4hr-session-loss, Recovery Path;
blog-osmani-good-spec, Claim 1] [editorial]

This is the minimum viable context discipline. It will not eliminate
compaction, but it will give you headroom, recovery, and a written
artifact the harness preserves.
[editorial]

---

## Summary: The Context Engineering Stack

| Layer | Cost | Lever | Source |
|-------|------|-------|--------|
| Harness baseline (system prompts + tools) | ~50-65% of window before you start | Prune MCP, audit `/context` | bswen Claim 6 |
| MCP server tax | ~5-7k tokens per server, permanent | 3-6 server budget | bswen Claims 1-4 |
| Skill/sub-agent budget | ~50-100 tokens per skill | Prefer Skills over MCP wrappers | French-Owen Claim 2 |
| Active plan file | ~600-800 tokens, re-injected post-compaction | Use SPEC.md as the plan | wasnotwas Claim 5; Osmani Claim 3 |
| Conversation | 4% of budget in baseline snapshot | Hand off at 50-60% | bswen Claim 6; Sankalp Claim 1 |
| Compaction | $0.40 + 21 cached turns per call | Prevent, don't be rescued | wasnotwas Claim 2 |
| Session JSONL files | Free | `cp -r` cron backup | decker Recovery Path |

The recurring theme is that **the smallest thing in the budget is the
thing you actually care about, and the largest things are pure
overhead**. Context engineering is the discipline of inverting that
ratio: shrink the overhead, protect the conversation, and write
everything load-bearing to a file the harness will re-load on the next
session.

---

*Sources for this chapter:
blog-anthropic-carta-healthcare-context-engineering (Claims 1, 2, 9),
blog-anthropic-harnessing-claude-intelligence (Claims 7, 11),
blog-anthropic-prompt-caching-everything (Claims 2, 3, 5, 6, 11),
blog-anthropic-session-management-1m-context (Claim 1),
blog-cursor-continual-harness-improvement (Claims 3, 5, 10, 11),
blog-french-owen-coding-agents-feb-2026 (Claims 1-3, 5, 6),
blog-bswen-mcp-token-cost (Claims 1-8),
blog-osmani-good-spec (Claims 1, 3-7),
blog-sankalp-claude-code-20 (Claims 1-7),
failure-alex000kim-claudecode-source-leak (Lesson 2),
failure-cursor-ultra-billing-cache-explosion (Lessons 1-3, 6),
failure-decker-4hr-session-loss (Lessons 1-5, Recovery Path),
failure-htdt-godogen-game-generation (Lessons 1, 2; Recovery 1),
research-wasnotwas-context-compaction (Claims 1-8),
practitioner-supabase-supabase-js (counter-evidence),
practitioner-getsentry-sentry (cross-reference),
failure-claudemd-ignored-compaction (cross-reference)*

*Last updated: 2026-05-10*
