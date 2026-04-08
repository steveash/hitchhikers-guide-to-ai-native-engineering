# Daily Workflows

> What a productive AI-assisted coding session actually looks like --
> from the first prompt to the final commit. This chapter gives you
> concrete session structures, iteration patterns, and delegation
> frameworks drawn from practitioners who do this every day.

---

## Session Structure

Every session has three phases: orient, execute, close. Practitioners
who skip the orient phase waste the first 15 minutes re-explaining
context the agent should have loaded. Practitioners who skip the close
phase lose work to context evaporation.

### Orient (first 2 minutes)

Load context before issuing task prompts. The agent starts with your
CLAUDE.md and whatever files it reads, but it does not know what YOU
plan to do this session.

pytest-test-categories mandates an issue-first workflow -- the agent
creates a GitHub issue before any implementation begins:
[source: practitioner-mikelane-pytest-test-categories] [anecdotal]

```markdown
**CRITICAL: All agents working on this repository MUST follow these requirements:**

1. **GitHub Issue Required**: Create a GitHub issue for ALL work before
   starting implementation
   - Use descriptive titles and comprehensive descriptions
   - Add appropriate labels (bug, enhancement, documentation, etc.)
   - Reference related issues if applicable
```

This is prescriptive: create the issue, state the goal, reference
related work. The issue becomes the session's anchor -- when the agent
drifts, point it back.

**Do this at session start**:

1. State the task in one sentence with acceptance criteria
2. Name the files the agent should read first
3. State what the agent must NOT touch

If your project uses an issue-first workflow, create the issue before
the first implementation prompt.
[source: practitioner-mikelane-pytest-test-categories] [emerging]

### Execute (the bulk of the session)

Use one of the execution loops described in the sections below. The
single-agent loop for focused tasks, the Ralph Loop for long tasks
that exceed context limits.

### Close (last 2 minutes)

Commit your work. Update any progress tracking files. If you are using
hooks, the close may happen automatically.

tin auto-commits on session end via a `SessionEnd` lifecycle hook:
[source: practitioner-dadlerj-tin] [anecdotal]

```json
{
  "hooks": {
    "SessionEnd": [
      {"hooks": [{"type": "command",
                   "command": "tin hook session-end",
                   "timeout": 30}]}
    ]
  }
}
```

The hook creates a git commit using the first human prompt as the
commit message. The agent never invokes it -- it fires silently. This
guarantees no session ends without a checkpoint, regardless of whether
you remembered to commit.
[source: practitioner-dadlerj-tin] [anecdotal]

**If you do not have auto-commit hooks**: Commit manually before ending
the session. Context evaporates when the session dies. Git history is
the cheapest, most durable persistence channel you have.
[editorial]

---

## The Single-Agent Loop

The core execution loop for one human + one agent working on a focused
task. This is what Osmani calls the "conductor" model -- you are
pair-programming, not managing a fleet.
[source: blog-addyosmani-code-agent-orchestra, Claim 1] [emerging]

The loop has four steps:

```
1. Explore  — Agent reads code, explains what it finds
2. Plan     — Agent proposes an approach, you approve or redirect
3. Execute  — Agent writes code
4. Verify   — Tests pass, you review the diff
```

Each step is a natural checkpoint. The plan step is where you prevent
bad work, not the verify step. A bad plan produces a large diff you
must reject; a good plan produces a diff you can review in minutes.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4 (Good Spec)] [emerging]

### Example: the loop in practice

```
You:    "Read src/auth/rate_limiter.py and explain how the sliding
         window works."
Agent:  [explores, explains the current implementation]

You:    "Good. I need to add per-IP rate limits alongside the existing
         per-user limits. Propose a plan -- do not write code yet."
Agent:  [produces a plan with file list and approach]

You:    "Plan looks right, but don't modify the database schema yet.
         Use the existing redis store. Go."
Agent:  [executes, writes code]

You:    "Run the tests."
Agent:  [runs tests, reports results]
```

The explore step costs a few thousand tokens and saves you from a
10-minute do-over when the agent misunderstands the codebase.
[editorial]

### When to use the single-agent loop

Use this for tasks that fit within a single context window and require
your judgment at multiple points: feature implementation, debugging,
refactoring. This is the default mode for most engineering work.
[editorial]

---

## The Ralph Loop

For tasks that exceed a single context window -- large features,
multi-file refactors, long-running test campaigns -- you need a
pattern that survives context resets. The Ralph Loop (named after the
"Ralph Wiggum Technique" in the community) is a stateless-but-iterative
cycle where the agent picks up where it left off by reading persistent
state rather than relying on conversation history.
[source: blog-addyosmani-code-agent-orchestra, Claim 6] [emerging]

### The five-step cycle

```
1. Pick task     — Read tasks.json (or equivalent), select next item
2. Implement     — Make the change
3. Validate      — Run tests, type checks, linter
4. Commit        — If validation passes, commit the change
5. Reset context — Clear the session, start fresh, repeat from step 1
```

Memory persists through four channels, NOT through conversation history:

| Channel | What it stores | Example |
|---------|---------------|---------|
| Git history | Completed work | Each commit is a checkpoint |
| Progress log | What happened, what is next | `progress.txt` |
| Task state | Remaining work, dependencies | `prd.json`, `tasks.json` |
| Agent config | Rules, patterns, knowledge | `AGENTS.md` |

[source: blog-addyosmani-code-agent-orchestra, Linked Source 3 (Self-Improving Agents)] [emerging]

### Stopping conditions

Without explicit stop conditions, the Ralph Loop runs forever. Define
these before starting:
[source: blog-addyosmani-code-agent-orchestra, Linked Source 3] [emerging]

```
- Max 50 iterations
- 3-hour time limit
- Stop if no commits in last 5 iterations
- 3+ failures on same task = skip and flag for human
```

### Bash orchestration

The Self-Improving Agents post provides a minimal bash orchestrator:
[source: blog-addyosmani-code-agent-orchestra, Linked Source 3] [emerging]

```bash
while :; do
   amp run -s prompt.md -o progress.txt
   if grep -q "<promise>COMPLETE</promise>" progress.txt; then break; fi
done
```

The agent writes to `progress.txt`, the bash loop reads it, and the
`<promise>COMPLETE</promise>` tag is the termination signal. This is
crude but functional -- the outer loop is deterministic (bash), and
only the inner loop (the agent) is non-deterministic.

### When to use the Ralph Loop

Use this when a task will take more than ~30 minutes of agent time, or
when you notice the agent starting to lose track of earlier context.
The deliberate context reset prevents the drift and tunnel vision that
accumulate in long sessions.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 3] [emerging]

### Counter-evidence

The Ralph Loop does not address tasks that require understanding the
full codebase context that was deliberately reset. If task N modifies
files that task N+1 depends on, the fresh agent must rediscover that
context by reading git history. For tightly coupled changes, a single
long session with careful context management may be more efficient.
[source: blog-addyosmani-code-agent-orchestra, Claim 6 assessment] [editorial]

None of our six practitioner profiles use the Ralph Loop explicitly,
though tin's auto-commit-on-session-end hook is a partial implementation
of the "commit and reset" pattern.
[source: practitioner-dadlerj-tin] [anecdotal]

---

## Multi-Agent Orchestration

When you move from one agent to multiple agents running in parallel,
the skill set changes. You stop pair-programming and start managing.
Osmani frames this as the shift from "conductor" (you play with one
instrument) to "orchestrator" (you coordinate a section).
[source: blog-addyosmani-code-agent-orchestra, Claim 1] [emerging]

### The Factory Model

The six-step production line for multi-agent work:
[source: blog-addyosmani-code-agent-orchestra, Linked Source 2 (Factory Model)] [emerging]

```
1. Plan     — Specs with acceptance criteria
2. Spawn    — Create agents and assign tasks
3. Monitor  — Check progress every 5-10 minutes
4. Verify   — Run tests and review code
5. Integrate — Merge branches
6. Retro    — Update AGENTS.md with patterns learned
```

This is a heavier process than the single-agent loop. The overhead
pays off only when you have 3+ agents running concurrently.

### WIP Limits

Do not run more agents than you can meaningfully review. Start with 3.
Scale based on your review capacity, not your machine's capacity.
[source: blog-addyosmani-code-agent-orchestra, Claim 8] [anecdotal]

The number 3 is not sacred. Osmani himself reports running 4-5 background
agents plus 3-5 human-in-the-loop sessions. Boris Cherny reportedly runs
15+. The real constraint is your review bandwidth -- which varies by
codebase familiarity, task complexity, and how much coffee you have had.
[source: blog-addyosmani-code-agent-orchestra, Claim 8 assessment] [editorial]

**Rule**: If you are rubber-stamping diffs because you have too many
agents running, you have too many agents running. Reduce until every
diff gets a real review.
[editorial]

### The 15-minute cadence

If an agent has not made significant progress in 15 minutes, it should
stop and report blockers. This is a management cadence, not a timer --
you check in on your agents the way a tech lead checks in on a team.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 5 (Coding Agents Manager)] [emerging]

```
Check-in questions (every 15 minutes):
- Has the agent committed anything since my last check?
- Is the agent looping on the same error?
- Is the token count climbing without code changes?
```

If the answer to the last two is yes, kill the agent and reassess the
task spec. A stuck agent does not unstick itself with more tokens.
[source: blog-addyosmani-code-agent-orchestra, Claim 12] [anecdotal]

---

## Workflow Commands

When you find yourself typing the same sequence of instructions across
sessions, encode it as a slash command. Slash commands are the workflow
equivalent of shell aliases -- they turn a multi-step process into a
single invocation.
[editorial]

### PR creation as a workflow command

Sentry's `/gh-pr` command encodes a complete PR creation workflow:
switch to a working branch, commit, create the PR, and critically --
check if the diff mixes frontend and backend files, splitting into
separate PRs if necessary.
[source: practitioner-getsentry-sentry] [anecdotal]

The frontend/backend split is enforced by CI, but the slash command
catches it BEFORE the CI run, saving a round trip. This is a workflow
command that embodies an organizational constraint.
[source: practitioner-getsentry-sentry] [anecdotal]

### Testing as a workflow command

NetPace's `/bugmagnet` is a 767-line command encoding a complete testing
methodology: 5 phases, explicit pause points for human approval between
phases, a 3-attempt limit per test, and a 30+ category edge case
checklist. It is a complete testing session in a single invocation.
[source: practitioner-frankray78-netpace] [anecdotal]

Key design elements worth stealing:

```markdown
- Phase gates: "At the end of each phase, pause and wait for user input"
- Attempt limits: "Maximum 3 attempts per test"
- Scope constraint: "DO NOT IMPLEMENT FIXES OR CHANGE THE IMPLEMENTATION
  FILE, ONLY WRITE TESTS"
```

The scope constraint is critical. Without it, the agent "helpfully" fixes
bugs it discovers during testing, producing a diff that mixes test
additions with production code changes.
[source: practitioner-frankray78-netpace] [anecdotal]

### Context-then-prompt commands

tin's slash commands implement a two-phase interaction pattern: if the
user provides an argument, execute immediately. If not, show context
first and ask for input.
[source: practitioner-dadlerj-tin] [anecdotal]

```markdown
If $ARGUMENTS is provided, checkout that branch:
  tin checkout $ARGUMENTS

If no branch name is provided, first run `tin branch` to show available
branches, then ask the user which branch to checkout.
```

This makes commands usable both as quick operations (`/checkout main`)
and as guided workflows (`/checkout` with no argument prompts a branch
selection). Each command declares only the specific tools it needs via
`allowed-tools` frontmatter, enforcing least-privilege per invocation.
[source: practitioner-dadlerj-tin] [anecdotal]

### When to create a workflow command

Create a command when:
- You give the same 5+ line instruction more than twice
- A workflow has ordering constraints (do X before Y)
- A workflow has scope constraints (do X but NOT Y)
- You want pause points for human approval between steps

Do NOT create a command for one-off tasks. Commands are for recurring
workflows.
[editorial]

---

## When to Restart a Session

Context degrades over long sessions. The agent starts repeating itself,
misses instructions it followed earlier, or proposes changes that
contradict its own previous work. These are signals, not vibes.

### Concrete restart signals

1. **The agent proposes reverting a change it just made.** This means
   it has lost track of its own work.

2. **The same error appears 3+ times.** The agent is looping. A fresh
   context will not magically fix the underlying problem, but it will
   stop the token burn. Reassess the task spec before restarting.
   [source: blog-addyosmani-code-agent-orchestra, Claim 12] [anecdotal]

3. **The agent ignores a CLAUDE.md rule it was following earlier.**
   Context window pressure pushes earlier instructions out of working
   memory. Restarting reloads the full config.
   [source: practitioner-frankray78-netpace] [emerging]

4. **Token count is climbing without corresponding code changes.** The
   agent is generating reasoning that does not produce work. Kill and
   restart with a more focused prompt.

5. **You are past 30+ turns on a single task.** This is not a hard rule
   -- some practitioners report productive 50+ turn sessions. But if you
   are past 30 turns AND seeing any of the symptoms above, restart. See
   Chapter 04 (Context Engineering) for more rigorous context-budget
   guidance grounded in measured compaction triggers and the "smart half"
   rule.
   [editorial]

### What to preserve across restarts

Commit before restarting. The Ralph Loop's four memory channels (git
history, progress log, task state, agent config) are your persistence
layer. Anything not in one of these channels is lost.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 3] [emerging]

If you use tin's lifecycle hooks, the `SessionEnd` hook auto-commits
for you. If you do not, commit manually.
[source: practitioner-dadlerj-tin] [anecdotal]

---

## When NOT to Delegate

Not every task benefits from an agent. The three-part delegation
framework (adapted from OpenAI's framework, via Osmani) provides
concrete criteria:
[source: blog-addyosmani-code-agent-orchestra, Linked Source 5 (Coding Agents Manager)] [emerging]

### Fully delegate (fire and forget)

Tasks that are mechanical, well-specified, and easy to verify:

- Dependency version bumps with passing tests
- Code formatting migrations
- Generating boilerplate from a template
- Writing tests for existing, well-understood functions

The agent works unsupervised. You review the final diff.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 5] [emerging]

### Delegate with checkpoints (supervised)

Tasks that involve judgment at specific decision points:

- Features that touch shared interfaces
- Refactors with edge cases
- Changes to code with poor test coverage

Use the "Ask First" tier from the three-tier boundary system (see
Chapter 02) to create natural pause points. The agent works, but
stops for your approval at key decisions.
[source: blog-addyosmani-code-agent-orchestra, Linked Sources 4, 5] [emerging]

### Do not delegate

Tasks where the value IS the understanding:

- Architecture decisions
- Security-sensitive code (auth, encryption, access control)
- "Should we build this?" questions
- Debugging production incidents in unfamiliar code

For these tasks, use the agent for **inquiry** -- "explain this code,"
"what are the failure modes here?" -- not delegation. The Anthropic
study found that conceptual inquiry sessions produced comprehension
scores above 65%, while pure delegation sessions dropped below 40%.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 6 (Comprehension Debt)] [emerging]

### Example: applying the framework

```
Task: "Add rate limiting to the login endpoint"

Architecture decision (don't delegate):
  "What rate limiting approaches work with our Redis setup?
   What are the tradeoffs between sliding window and token bucket?"

Implementation (delegate with checkpoints):
  "Implement sliding window rate limiting per the plan we discussed.
   Ask before modifying the database schema or the auth middleware."

Tests (fully delegate):
  "Write tests for the rate limiter covering: normal usage,
   rate exceeded, window expiry, concurrent requests."
```

The same feature decomposes into three delegation levels. The key
insight: delegation is not a property of the feature. It is a property
of the sub-task.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 5] [editorial]

---

## Summary: Daily Workflow Patterns

| Pattern | When to use | Key discipline |
|---------|-------------|----------------|
| Single-agent loop | Focused tasks, < 30 min | Approve the plan before execution |
| Ralph Loop | Long tasks, multi-file | Commit after every iteration, explicit stop conditions |
| Factory Model | 3+ concurrent agents | WIP limits, 15-minute check-ins |
| Workflow commands | Recurring multi-step processes | Encode constraints, not just steps |

The common thread: every pattern has explicit checkpoints where work
is committed, progress is assessed, and direction is confirmed. The
agents that go off the rails are the ones that run too long without
a checkpoint.

---

*Sources for this chapter:
blog-addyosmani-code-agent-orchestra (Claims 1, 5, 6, 8, 12;
Linked Sources 2, 3, 4, 5, 6),
practitioner-getsentry-sentry,
practitioner-frankray78-netpace,
practitioner-dadlerj-tin,
practitioner-mikelane-pytest-test-categories*

*Last updated: 2026-04-08*
