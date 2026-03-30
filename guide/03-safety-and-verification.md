# Safety and Verification

> The bottleneck is no longer generation. It is verification.
> This chapter is about building a verification stack that catches what you
> miss -- because you will miss things. Every practitioner we studied has been
> bitten at least once. The ones who survive have layers.

---

## The Verification-as-Bottleneck Thesis

AI coding agents can generate code faster than any human can review it.
This creates an asymmetry: generation capacity permanently exceeds
verification capacity. Human review is the safety system, and it is
always the bottleneck.
[source: blog-addyosmani-code-agent-orchestra, Claim 5;
blog-addyosmani-code-agent-orchestra, Linked Source 2 (Factory Model)] [emerging]

The evidence for this is both structural and empirical. Structurally,
a single engineer can run 3-5 agents in parallel, each producing code
at machine speed. Empirically, Anthropic's study of 52 engineers found
that those who delegated to AI scored 17% lower on comprehension quizzes
-- with the largest drops in debugging capability. Velocity metrics
stayed green while understanding degraded invisibly.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 6 (Comprehension Debt)] [emerging]

The implication: you need layered verification that does not depend
entirely on your attention span at 4pm on a Friday.

### What happens without verification layers

When verification is a single layer (human review only), failure modes
include:
- **Rubber-stamping**: The diff looks reasonable, you approve it, the
  bug ships. You did not test the edge case the agent missed.
- **Sycophancy loops**: Agent A writes code, you ask it to review its
  own code, it says the code looks great.
- **Comprehension debt**: You approve code you cannot fully explain.
  It works today. Six months later, nobody on the team understands it.

---

## The Verification Stack

Build verification in layers, from cheapest to most expensive. Each
layer catches what the layer below misses.

### Layer 1: Deterministic Tools (cost: zero human attention)

Linters, formatters, type checkers, and test suites run automatically
and catch mechanical errors without human involvement. This is your
foundation.
[source: practitioner-mikelane-pytest-test-categories,
practitioner-frankray78-netpace] [settled]

pytest-test-categories enforces this with pre-commit hooks:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    hooks:
      - id: ruff
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    hooks:
      - id: mypy
```

The agent cannot commit code that fails type checking or lint. No
human review required for these classes of errors.
[source: practitioner-mikelane-pytest-test-categories] [emerging]

**Rule**: Every rule your linter can enforce is a rule you should remove
from your CLAUDE.md. Free up human attention for judgment calls.
[editorial]

### Layer 2: Hooks (cost: minimal human attention)

Hooks fire at lifecycle events and enforce behavior the agent cannot
choose to skip. They are the only mechanism that guarantees compliance
without relying on the agent reading and obeying a prose instruction.
[source: practitioner-dadlerj-tin] [anecdotal]

tin configures four Claude Code lifecycle hooks:

```json
{
  "hooks": {
    "SessionStart": [
      {"hooks": [{"type": "command",
                   "command": "tin hook session-start",
                   "timeout": 30}]}
    ],
    "Stop": [
      {"hooks": [{"type": "command",
                   "command": "tin hook stop",
                   "timeout": 30}]}
    ],
    "SessionEnd": [
      {"hooks": [{"type": "command",
                   "command": "tin hook session-end",
                   "timeout": 30}]}
    ]
  }
}
```

The `SessionEnd` hook auto-commits with the first human prompt as the
commit message. The agent never invokes these -- they fire silently.
This guarantees conversation tracking regardless of agent behavior.
[source: practitioner-dadlerj-tin] [anecdotal]

**Rule**: If a rule is critical enough to state three times in your
CLAUDE.md, it is critical enough to enforce with a hook. Prose rules
are suggestions. Hooks are laws.
[source: practitioner-frankray78-netpace, practitioner-dadlerj-tin] [editorial]

### Layer 3: CI as Verification Backstop (cost: minutes of wall time)

Five of six profiled repos enforce CI gates on pull requests. CI catches
what hooks miss because it runs the full test suite in a clean environment,
not just the checks the developer configured locally.
[source: practitioner-getsentry-sentry, practitioner-nikolays-postgres-dba,
practitioner-supabase-supabase-js, practitioner-mikelane-pytest-test-categories,
practitioner-frankray78-netpace] [settled]

postgres_dba runs tests across six PostgreSQL versions (13-18):

```markdown
## CI

GitHub Actions (`test.yml`): runs on push and PRs -- tests across
PostgreSQL 13, 14, 15, 16, 17, 18.
```

NetPace runs four CI workflows including CodeQL security analysis:

```
.github/workflows/dotnet.yml        # PR build and test gate
.github/workflows/codeql.yml        # Weekly CodeQL security scan
.github/workflows/publish-nuget.yml # Tag-triggered NuGet publish
.github/workflows/release-binaries.yml  # Cross-platform release
```

[source: practitioner-nikolays-postgres-dba,
practitioner-frankray78-netpace] [emerging]

**Rule**: If your repo does not have CI gates on pull requests, add them
before adding AI agents. An agent without CI is a machine that writes
untested code at scale.
[editorial]

### Layer 4: Human Review (cost: highest, most valuable)

Human review is the only layer that catches semantic errors, architectural
problems, and "this code works but is the wrong approach" mistakes. It is
also the most expensive layer, which is why the three layers below it
exist: to reduce the volume of issues that reach human review.

**Rule**: Your goal is not to eliminate human review. Your goal is to
ensure that by the time code reaches human review, the only issues left
are the ones that require human judgment.
[editorial]

---

## The Two-Agent Review Pattern

Use a second agent to review the first agent's output. This is not
a replacement for human review -- it is an additional layer between
CI and human review.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 5 (Coding Agents Manager)] [emerging]

The pattern:

```
1. Agent A implements the task
2. Agent B reviews Agent A's output against the spec
3. Agent A (or Agent C) applies Agent B's feedback
4. Human reviews the final result
```

Sentry implements a variant of this with its `/gh-review` command, which
instructs the reviewing agent to adopt a skeptical stance:

```markdown
Do NOT assume feedback is valid. You should always verify that the
feedback is truthful (the bug is real, for example), and then attempt
to address it.
```

This anti-sycophancy instruction is critical. Without it, Agent B
tends to approve Agent A's work -- the same way a human rubber-stamps
a reasonable-looking diff.
[source: practitioner-getsentry-sentry] [anecdotal]

### Example: implementing two-agent review

```bash
# Agent A: implement the feature
claude --print "Implement the login rate limiter per spec in TASK-42.md" > /tmp/impl.log

# Agent B: review the implementation (separate context, fresh perspective)
claude --print "Review the changes in the current git diff against the spec
in TASK-42.md. Check for: missed edge cases, security issues, test coverage
gaps. Do NOT assume the implementation is correct."
```

The key is that Agent B operates in a separate context. It does not
share Agent A's reasoning, assumptions, or confirmation bias.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 5] [emerging]

### Counter-evidence

Two-agent review adds cost (roughly double the tokens) and latency.
For small, well-specified tasks with strong test coverage, the benefit
may not justify the cost. Reserve this pattern for: security-sensitive
changes, architectural decisions, and code that is hard to test.
[editorial]

---

## Quality Gates Framework

Quality gates are decision points where work pauses for approval or
automated verification before proceeding. They prevent runaway agents
from compounding errors across multiple steps.
[source: blog-addyosmani-code-agent-orchestra, Claim 11] [emerging]

### Gate 1: Plan Approval

Before the agent writes code, it produces a plan. You approve the plan
or redirect it. This catches misunderstandings before they become 500-line
diffs.

The three-tier boundary system structures what the agent can do
without asking:
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4 (Good Spec)] [emerging]

```
Always Do:    "Always run tests before commits"
Ask First:    "Ask before modifying database schemas"
Never Do:     "Never commit secrets or API keys"
```

This is more nuanced than a flat list of prohibitions. The "Ask First"
tier creates natural gates: the agent pauses, presents its plan for that
specific operation, and waits for approval.

tin implements per-command permission scoping as a variant of this pattern:

```yaml
# checkout.md frontmatter
allowed-tools: Bash(tin checkout:*), Bash(tin branch:*)

# commit.md frontmatter
allowed-tools: Bash(tin commit:*), Bash(tin status:*)
```

Each command gets only the tools it needs. An agent running `/checkout`
cannot accidentally commit.
[source: practitioner-dadlerj-tin] [anecdotal]

### Gate 2: Test-on-Complete

After the agent completes a task, tests run automatically before the
result is accepted. NetPace enforces this as a MUST ALWAYS:

```markdown
You **MUST ALWAYS**:
- Run all tests before refactoring
- Commit before refactoring
- Run all tests after refactoring
```

The "commit before refactoring" gate is especially important: it creates
a rollback point. If the refactor breaks tests, you can revert to the
last known-good state.
[source: practitioner-frankray78-netpace] [anecdotal]

### Gate 3: AGENTS.md as Living Guardrail

AGENTS.md files that encode project-specific knowledge act as persistent
gates -- rules the agent loads on every session. But there is an important
caveat: the content must be developer-written, not auto-generated.

LLM-generated AGENTS.md files offer no benefit and can reduce success
rates by ~3% while increasing costs over 20%. Developer-written context
files provide ~4% improvement.
[source: blog-addyosmani-code-agent-orchestra, Claim 7] [settled]

**Rule**: Never let an agent auto-generate your AGENTS.md via `/init`
or similar commands. Write it yourself. Apply the filter test: can the
agent discover this by reading the code? If yes, delete it from AGENTS.md.
Keep only what requires human knowledge.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 1 (AGENTS.md post)] [emerging]

---

## Kill Criteria: When to Stop the Agent

Not every agent task succeeds. Knowing when to kill a stuck agent saves
tokens, time, and frustration.

### The 3-iteration rule

Kill an agent that has attempted the same error fix 3 or more times.
Three iterations allows for: one genuine fix attempt, one retry with
a different approach, and one signal that the task needs human
intervention.
[source: blog-addyosmani-code-agent-orchestra, Claim 12] [anecdotal]

The Self-Improving Agents post elaborates on stopping conditions:

```
- Max 50 iterations per session
- 3-hour time limit
- Stop if no commits in last 5 iterations
- 3+ failures on same task = skip and flag for human
```

[source: blog-addyosmani-code-agent-orchestra, Linked Source 3 (Self-Improving Agents)] [emerging]

### What stuck looks like

Symptoms that an agent is looping without progress:
- Same error message appears in 3+ consecutive turns
- Agent proposes reverting a change it just made
- Token count spikes without corresponding code changes
- Agent says "let me try a different approach" and produces the same code

### Example: implementing a kill switch

NetPace's `/bugmagnet` command includes a built-in attempt limit:

```markdown
Maximum 3 attempts per test
```

This is a concrete, per-test kill criterion embedded in the command
definition. The agent does not decide when to give up -- the command
tells it.
[source: practitioner-frankray78-netpace] [anecdotal]

**Rule**: Set explicit attempt limits in your agent instructions. Do
not rely on the agent to recognize when it is stuck. An agent in a
failure loop will burn tokens indefinitely unless told to stop.
[editorial]

---

## Comprehension Debt: The Invisible Risk

Comprehension debt is the gap between code that exists and your team's
understanding of that code. AI-generated code creates comprehension debt
by default because you did not write it -- and the act of writing is how
engineers build mental models.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 6 (Comprehension Debt)] [emerging]

### The numbers

Anthropic's randomized controlled trial (52 engineers):
- AI users scored **17% lower** on comprehension quizzes (50% vs. 67%)
- Largest declines in **debugging capability** specifically
- Two usage patterns emerged:
  - **Delegation** (below 40% comprehension): "Write the function for me"
  - **Conceptual inquiry** (above 65% comprehension): "Explain how this handles X"

[source: blog-addyosmani-code-agent-orchestra, Linked Source 6] [emerging]

### Why metrics miss it

Velocity and DORA metrics remain green while comprehension declines.
You ship more features, your cycle time drops, your test coverage is
high -- but nobody on the team can debug the code without asking the
agent. This becomes visible only when:
- The agent is unavailable (outage, rate limit, policy change)
- A bug requires understanding the full call chain across 10 files
- A new team member asks "why does it work this way?" and nobody knows

[source: blog-addyosmani-code-agent-orchestra, Linked Source 6] [emerging]

### Mitigating comprehension debt

**1. Use TDD to force understanding before generation.**
Writing the test first means you must understand the expected behavior
before the agent writes any implementation code. NetPace's TDD-first
workflow is the strongest structural mitigation in our profiled repos.
[source: practitioner-frankray78-netpace] [anecdotal]

```markdown
TDD (Test-Driven Development) is non-negotiable. Every line of
production code must be written in response to a failing test.
```

**2. Use the agent for inquiry, not just delegation.**
Ask "explain this function" and "what edge cases does this miss?"
The comprehension study found that conceptual inquiry sessions produced
above-65% comprehension scores -- better than the control group in some
cases.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 6] [emerging]

**3. Apply Willison's rule: "I won't commit code I couldn't explain to
someone else."**
This is a personal kill criterion for comprehension debt. If you cannot
explain the code, do not commit it -- ask the agent to explain it until
you can.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4 (Good Spec)] [anecdotal]

**4. Require documentation in the same commit as code.**
pytest-test-categories mandates this:

```markdown
Keep documentation synchronized with code changes.
Update relevant documentation in the SAME commit as code changes.
```

Documentation forces articulation, and articulation forces comprehension.
[source: practitioner-mikelane-pytest-test-categories] [anecdotal]

---

## CI as Verification Backstop: Patterns from Practice

CI is not a nice-to-have when agents write your code. It is the minimum
viable verification layer.

### Pattern: Multi-version matrix testing

postgres_dba tests across six PostgreSQL versions. This catches
agent-generated code that uses features from a newer version than
the minimum supported:

```yaml
# test.yml (simplified)
strategy:
  matrix:
    pg_version: [13, 14, 15, 16, 17, 18]
```

[source: practitioner-nikolays-postgres-dba] [anecdotal]

### Pattern: Security scanning as CI gate

NetPace runs CodeQL weekly and on every PR. This catches security
issues that neither the agent nor the human reviewer noticed:

```yaml
# codeql.yml
on:
  schedule:
    - cron: '0 0 * * 1'  # Weekly
  pull_request:
    branches: [main]
```

[source: practitioner-frankray78-netpace] [anecdotal]

### Pattern: Pre-commit hooks as local CI

pytest-test-categories runs isort, ruff, and mypy as pre-commit hooks.
These catch issues BEFORE the code enters CI, giving faster feedback:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

[source: practitioner-mikelane-pytest-test-categories] [emerging]

### The coverage gap

Tests cannot fully answer correctness. You cannot write tests for
unspecified behaviors. This is the fundamental limitation of CI as a
verification layer -- it catches regressions against known requirements,
but it cannot catch "this code does something we never thought to test."
[source: blog-addyosmani-code-agent-orchestra, Linked Source 6] [emerging]

**Rule**: CI is necessary but not sufficient. Use it to catch known
failure modes. Use human review and two-agent review to catch unknown
ones.
[editorial]

---

## Concrete Verification Checklist

Use this checklist when reviewing AI-generated code:

```markdown
## Before approving AI-generated code

- [ ] Tests pass (CI green, not just local)
- [ ] I can explain what this code does to a colleague
- [ ] I can identify what would break if line N changed
- [ ] Edge cases from the spec are covered by tests
- [ ] No secrets, API keys, or credentials in the diff
- [ ] No unrelated changes snuck in (common with agents)
- [ ] The approach matches what I would have chosen
      (if not, understand WHY the agent chose differently)
- [ ] Documentation updated in the same commit (if applicable)
```

This is not aspirational. This is the minimum verification standard
for code you did not write. Treat AI output as a pull request from
a contractor -- verify everything, approve nothing on faith.
[editorial]

---

## Summary: The Verification Stack

| Layer | Cost | Catches | Example |
|-------|------|---------|---------|
| Deterministic tools | Zero attention | Format, lint, type errors | ruff, mypy, pre-commit hooks |
| Hooks | Minimal attention | Lifecycle violations | tin's auto-commit on session end |
| CI | Minutes of wall time | Test failures, security issues | postgres_dba's PG 13-18 matrix |
| Two-agent review | Double tokens | Logic errors, missed edge cases | Sentry's `/gh-review` |
| Human review | Highest | Architectural issues, wrong approach | Your brain |

Build all five layers. Each one is a safety net for the layer above it.

---

*Sources for this chapter:
blog-addyosmani-code-agent-orchestra (Claims 5, 7, 11, 12; Linked Sources 1, 2, 3, 4, 5, 6),
practitioner-getsentry-sentry,
practitioner-frankray78-netpace,
practitioner-nikolays-postgres-dba,
practitioner-supabase-supabase-js,
practitioner-mikelane-pytest-test-categories,
practitioner-dadlerj-tin*

*Last updated: 2026-03-30*
