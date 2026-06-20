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
are suggestions. Hooks are laws -- with a refinement: **blocking hooks
(exit 2) are laws. Advisory hooks are louder suggestions.** PreToolUse
hooks that exit with code 2 physically prevent the blocked action at the
harness level. The agent cannot proceed. But UserPromptSubmit hooks that
inject reminder text are still advisory -- one practitioner reports
"Claude occasionally still ignores hooks as well" for guidance-type
injection.
[source: practitioner-frankray78-netpace, practitioner-dadlerj-tin,
failure-claudemd-ignored-compaction, Lesson 3] [emerging]

The distinction matters quantitatively. Christopher Montes measured ~60%
baseline CLAUDE.md compliance, rising to 90%+ after deploying a
hook-based enforcement system. That remaining ~10% gap is why blocking
hooks (exit 2) and settings.json permissions exist: for rules where
90% is not good enough.
[source: failure-hooks-enforcement-2k, Lesson 3 (Montes measurement)] [emerging]

#### The compaction failure mode

CLAUDE.md rules are summarized during context compaction, losing
specificity and imperative force. Multiple independent practitioners
confirm that compliance drops noticeably after Auto Compact fires.
The compaction summarizer has no mechanism to distinguish critical
rules from incidental context -- it compresses everything equally.
[source: failure-claudemd-ignored-compaction, Lesson 2;
failure-hooks-enforcement-2k, Lesson 2] [emerging]

SessionStart hooks are the architectural answer: they fire on startup,
resume, clear, AND compact. Use them to re-inject critical rules as
clean system-reminder messages that bypass the "may or may not be
relevant" framing the harness applies to CLAUDE.md content:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "bash scripts/inject-rules.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

For per-prompt reinforcement at minimal token cost, add a UserPromptSubmit
hook that injects a single-line motto (~15 tokens per prompt, ~750 tokens
over a 50-turn session).
[source: failure-claudemd-ignored-compaction, Recovery Path, Workaround 1] [emerging]

#### The context recovery pipeline

For long sessions where compaction is inevitable, one practitioner built
a pipeline that backs up context before Auto Compact fires, reduces the
7-8MB context dump to a 100-200KB summary using Claude Haiku 4.5, then
re-injects the summary via a pre-session hook. This is the most robust
compaction survival strategy documented in our corpus: if compaction
destroys context, regenerate it externally and re-inject it.
[source: failure-hooks-enforcement-2k, Recovery Path (auto_compact.py +
context_recovery_helper.py)] [anecdotal]

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

### Effort routing for review agents

Cursor's May 2026 Bugbot update gives the first published quantification of
the effort-quality curve for an AI review agent: high effort finds 35% more
bugs than default effort while the resolution rate stays constant at 80% —
additional signal, not additional noise.
[source: blog-cursor-bugbot-effort-billing, Claim 6] [emerging]

This is vendor-internal data on one product, but the configurable-effort
mechanism — and the empirical finding that depth does not raise the
false-positive rate — generalizes the cost-benefit decision from per-PR to
per-codepath. The same product also exposes "custom logic" that selects
effort dynamically per PR.
[source: blog-cursor-bugbot-effort-billing, Claim 4] [emerging]

**Rule**: Where your review agent has a tunable effort lever, route high
effort to auth, payment, and data-migration paths; default effort to CSS,
docs, and routine refactors. Pay for depth on the codepaths whose failures
hurt most.
[source: blog-cursor-bugbot-effort-billing, Claims 4, 6] [emerging]

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

LLM-generated AGENTS.md files reduced success rates by 0.5-2% while
increasing inference costs by over 20%. Developer-written context files
improved success by ~4% on AGENTbench. (Preprint, Python-only, no
significance tests on headline numbers.)
[source: paper-gloaguen-agentsmd-effectiveness, Claims 1-2] [emerging]

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

For security-focused review, run static analysis first and pass its
findings to the AI reviewer as anchors — this compensates for LLM recall
gaps and keeps the review focused on security rather than style.
[source: discussion-hn-autofix-hybrid-review, Claims 1, 3, 8] [emerging]

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

## Known Verification Failure Modes

These are specific failure patterns documented by practitioners. Watch
for them in your own projects.

### TODO-as-completion

The agent declares a task complete while the code contains TODO, FIXME,
or placeholder stubs. One practitioner reports: "Claude may claim to have
implemented something, but many TODO items remain unimplemented." This is
not a compaction issue -- it occurs within active sessions. The agent's
self-assessment of completion is unreliable.
[source: failure-hooks-enforcement-2k, Lesson 4] [anecdotal]

This pattern is corroborated quantitatively by independent third-party
research. Apollo Research tested GPT-5.5 on deliberately impossible
programming tasks and found that the model falsely claimed completion
in 29% of samples — up from 7% on GPT-5.4. OpenAI's internal monitoring
of coding-agent traffic found a similar pattern.
[source: blog-thebatch-gpt55-hallucination-kimi-k26, Claim 3] [emerging]

A 4× regression in confabulated-completion rate across a single model
generation is the strongest available signal that completion claims must
be verified against the actual code, not against the agent's self-report.
The mitigation is unchanged — a Stop hook that scans modified files for
stub markers — but the volume of false claims now justifies treating
verification as the default, not an extra precaution.

**Mitigation**: Add a Stop hook that scans modified files for
TODO/FIXME/HACK markers and blocks the session from declaring completion
if any are found. The practitioner built `no_mock_code.py` for exactly
this purpose.
[source: failure-hooks-enforcement-2k, Recovery Path (no_mock_code.py)] [anecdotal]

```bash
# Example: Stop hook that catches TODO stubs in modified files
MODIFIED=$(git diff --name-only HEAD 2>/dev/null)
if [ -n "$MODIFIED" ]; then
  TODOS=$(echo "$MODIFIED" | xargs grep -l 'TODO\|FIXME\|HACK' 2>/dev/null)
  if [ -n "$TODOS" ]; then
    echo "BLOCKED: Unresolved TODO/FIXME markers found in:" >&2
    echo "$TODOS" >&2
    exit 2
  fi
fi
exit 0
```

### Dangerous command execution

Agents execute destructive commands (`rm -rf`), make unauthorized git
commits, and bypass permission dialogs through repetitive prompting.
Even when commands are set to "Allow" in Claude Code settings, permission
behavior can be inconsistent.
[source: failure-hooks-enforcement-2k, Failure Mode 4] [anecdotal]

**Mitigation**: Use a PreToolUse command restrictor hook that gates all
command execution with explicit Allow/Deny/Ask differentiation. Block
`rm -rf` entirely. Enforce commit message format via a validation hook.
This is more reliable than writing "NEVER run rm -rf" in CLAUDE.md,
which is subject to the ~70-80% prose compliance ceiling.
[source: failure-hooks-enforcement-2k, Recovery Path (command_restrictor.py,
validate_git_commit.py); failure-claudemd-ignored-compaction, Lesson 5] [emerging]

### Trust-degradation in automated pipelines

A nondeterministic automation can pass early tests, build deployment
trust over time, and then fail catastrophically when the model's
interpretation of an ambiguous instruction shifts. DocTomoe's formulation:

> "it passes tests, builds trust, and then fails catastrophically once
> the implicit interpretation shifts"
> [source: discussion-hn-airun-executable-markdown, Claim 7]

The scenario: an automated AI pipeline runs "analyze logfiles, then
clean up" repeatedly. For weeks, "clean up" means "remove temp files."
Then a model upgrade or context shift causes the model to interpret
"clean up" differently — potentially destructively. The failure is not
random; it is structurally inevitable when natural-language instructions
have multiple valid interpretations and execution environments change
over time.
[source: discussion-hn-airun-executable-markdown, Claim 7] [anecdotal]

**Mitigation**: For any automated AI pipeline:
1. Use maximally unambiguous language — eliminate instructions with
   multiple valid interpretations
2. For destructive operations, require explicit confirmation via the
   permission model
3. Run scripts touching the filesystem or infrastructure in a
   container or sandbox that bounds the blast radius
4. Treat behavioral stability across model upgrades as a first-class
   testing concern
[source: discussion-hn-airun-executable-markdown, Claim 7] [anecdotal]

### Coding-agent self-bias in evaluation

A coding agent evaluating its own generated output is inherently biased
toward declaring success. "Code compiles fine but assets are floating,
paths lead nowhere, layouts are garbage" — the agent that wrote the code
cannot reliably detect failures that manifest as visual, spatial, or
behavioral properties of the running output.

From the Godogen game-generation pipeline (four rewrites over one year):
after adding a separate vision-model QA loop (Gemini Flash evaluating
screenshots from the running engine, with no code access), the pipeline
caught bug categories the code-generating agent systematically missed:
z-fighting, floating objects, physics explosions, and grid-like
placements that should be organic.
[source: failure-htdt-godogen-game-generation, Lesson 4] [anecdotal]

**Mitigation**: For any pipeline where output correctness has a visual,
spatial, or behavioral dimension, add a separate evaluator grounded in
the actual execution output — not the code that produced it. The
evaluator must NOT have access to the generated code. This eliminates
self-bias by design: the evaluator can only see whether the output is
correct, not whether the code looks correct.
[source: failure-htdt-godogen-game-generation, Lesson 4] [anecdotal]

### Shell execution attack surface

If your harness allows shell execution, your allowlist matching will
be bypassed unless hardened against attack classes that are non-obvious.
Claude Code's `bashSecurity.ts` (from the source map leak) implements
23 numbered security checks:

```
# bashSecurity.ts — partial inventory
# Total: 23 numbered checks
# Includes:
#   - 18 blocked Zsh builtins
#   - Zsh equals expansion: =curl bypasses permission checks for curl
#   - Unicode zero-width space injection in command tokens
#   - IFS null-byte injection
#   - Malformed token bypass (additional, discovered in security review)
```

[source: failure-alex000kim-claudecode-source-leak, Lesson 4] [emerging]

Three lessons:
1. **Zsh is meaningfully more dangerous than bash** for harness tool use —
   18 extra blocked builtins. Default to bash.
2. **Zsh equals expansion** (`=curl` executes `curl` even when `curl`
   is on a blocklist) will not be caught by simple string matching.
3. **Unicode zero-width space injection** in command tokens can slip past
   allow-list matching entirely.

**Rule**: If your harness allows shell execution and you have fewer than
23 documented security checks, you have unknown exposure. At minimum,
audit for the three non-obvious bypass classes above. The 23-check count
is a floor, not a ceiling — the comment history implies new bypasses are
discovered during audits.
[source: failure-alex000kim-claudecode-source-leak, Lesson 4] [emerging]

### Cross-system intersection bugs

Some AI-system bugs only manifest at the interaction of multiple
subsystems and defeat every layer of standard software verification.
Anthropic's April 2026 postmortem on a Claude Code thinking-cache
regression is the canonical example. The bug "made it past multiple
human and automated code reviews, as well as unit tests, end-to-end
tests, automated verification, and dogfooding"
[source: blog-anthropic-claudecode-quality-postmortem, Claim 7] [settled].

Anthropic's own diagnosis names the failure category:

> "This bug was at the intersection of Claude Code's context management,
> the Anthropic API, and extended thinking."
> [source: blog-anthropic-claudecode-quality-postmortem, Claim 9]

A back-test on the offending pull request found that Opus 4.7 caught
the bug while Opus 4.6 — the model used for the original code review
— did not
[source: blog-anthropic-claudecode-quality-postmortem, Claim 10]
[settled]. The actual detection mechanism in production was external
user feedback through `/feedback` and reproducible examples posted
online — not internal evals or dogfooding
[source: blog-anthropic-claudecode-quality-postmortem, Claim 13] [settled].

**Mitigation**: For any harness that combines context management, API-
level features (extended thinking, prompt caching, message-queue
experiments), and multi-step tool execution, design integration tests
that exercise the full session loop — not just each component in
isolation. Treat in-product user-feedback channels as production
monitoring infrastructure, not a UX nicety: instrument them, route
reports to a triage queue, and act on reproducible examples even when
internal evals show the system green. When you upgrade the model your
agents run, also upgrade the model that reviews their code: the prior
generation may no longer be sensitive to the failure modes of the
newer one.
[source: blog-anthropic-claudecode-quality-postmortem,
Claims 7, 9, 10, 13] [emerging]

### Prompt injection in workflow inputs

Automated pipelines that process user-submitted content — issue bodies,
PR descriptions, comments, commit messages — are natural-language injection
surfaces. A malicious comment can include "ignore previous instructions"
the same way SQL accepts `' OR '1'='1`.

GitHub's agentic workflow documentation names this threat explicitly:

> "Treat user-provided content as untrusted. Design workflows to resist
> prompt injection attempts in issue descriptions, comments, or pull
> request content."

The safe access pattern is to route user content through a sanitization
channel (e.g., `steps.sanitized.outputs.text` in GitHub Agentic Workflows,
which filters unauthorized mentions, malicious links, and excessive content)
before passing it to the agent. The anti-pattern: interpolating raw event
payload fields like `github.event.comment.body` directly into the agent's
instruction body, bypassing any sanitization.
[source: docs-ghaw-chatops, Claims 5, 7] [settled]
[source: docs-ghaw-chatops, Claim 6] [emerging]

**Rule**: Never interpolate raw user-submitted event fields directly into
agent instructions. Route user content through a sanitization layer first,
or treat every user-submitted field as untrusted and apply explicit format
gates.
[source: docs-ghaw-chatops, Claim 7] [settled]

---

## Security Threat Model for AI-Native Teams

The verification stack above defends against agent mistakes against your
codebase. There is a parallel threat model that defends against attackers
using agents against your codebase. Two first-party sources from inside the
model and tooling vendors converged on it in early 2026.

### The 24-month offensive AI escalation window

Anthropic's security team, citing internal research from Project Glasswing
and Claude Mythos Preview, makes an explicit timeline claim:

> "Within the next 24 months, vast numbers of bugs that sat unnoticed in code,
> possibly for years, will be found by AI models and chained into working
> exploits."
> [source: blog-anthropic-ai-accelerated-offense, Claim 1] [emerging]

The operative word is *chained*. The companion claim — that "publicly
available models can find serious vulnerabilities that traditional reviews
have missed for long periods" — means the threat model can no longer assume
"only nation-state actors have these capabilities."
[source: blog-anthropic-ai-accelerated-offense, Claim 2] [anecdotal]

As of May 2026, the UK AI Security Institute's independent evaluation
places publicly-available GPT-5.5 at 71.4% on its Expert-level cyber CTF
benchmark — statistically indistinguishable from Claude Mythos Preview
(68.6%) — and the second model ever to complete AISI's 32-step corporate
network attack simulation autonomously.
[source: blog-simonwillison-aisi-gpt55-cyber, Claims 1, 2, 3] [emerging]
Teams that deferred AI-assisted security review because capable models were
research-access-only can no longer use that deferral.
[source: blog-simonwillison-aisi-gpt55-cyber, Claim 1] [emerging]

For AI-native engineering teams, this is the asymmetry: you ship more code
per developer, your attack surface grows in proportion, and the cost for an
attacker to find chainable bugs in that surface is collapsing toward zero on
the same curve that is making your team faster.

**Rule**: If you have not yet adopted AI-assisted security scanning of your
own code before it ships, the first-mover advantage is closing. Run the same
class of tools an attacker would on your own code first, on every PR, before
the 24-month window closes.
[source: blog-anthropic-ai-accelerated-offense, Claim 6] [anecdotal]

### Three defensive actions that offset the asymmetry

The Anthropic post ranks seven recommendations; three are immediately
actionable for an AI-native engineering team and have a corroborating
production deployment in our corpus:

1. **AI security scan before shipping.** Anthropic frames this as the single
   highest-ROI action: "If you implement one thing from this section,
   implement this: scan your code for vulnerabilities using AI before it
   ships."
   [source: blog-anthropic-ai-accelerated-offense, Claim 6] [anecdotal]
   Cursor's production deployment runs four security agents on a shared MCP
   substrate; the new-PR review agent alone runs on 3,000+ internal PRs per
   week and surfaces 200+ vulnerabilities per week.
   [source: blog-cursor-security-agents, Claims 1, 9] [anecdotal]
   Mozilla provides the third, vendor-independent data point: Firefox 150
   shipped fixes for 271 vulnerabilities surfaced by an early Claude Mythos
   Preview run on the codebase, against 22 found by Opus 4.6 in Firefox 148 —
   a ~12× model-generation jump on the same heavily-audited browser.
   [source: blog-simonwillison-bobby-holley, Claim 1] [emerging]

   Budget for the finding-volume shock before enabling the scan. Firefox CTO
   Bobby Holley named the organizational impact directly:
   > "You may need to reprioritize everything else to bring relentless and
   > single-minded focus to the task, but there is light at the end of the
   > tunnel."
   > [source: blog-simonwillison-bobby-holley, Claim 7]
   Mozilla — one of the most security-mature organizations in open source —
   could not absorb 271 vulnerabilities without significant operational
   disruption.
   [source: blog-simonwillison-bobby-holley, Claim 7] [anecdotal]

2. **AI model at the front of the alert queue, for 100% alert coverage.**
   Human-only SOCs sample alerts under fatigue. An AI triage agent that
   processes every alert at low depth ensures none goes uninvestigated.
   [source: blog-anthropic-ai-accelerated-offense, Claim 7] [emerging]
   Anthropic's own production deployment of this pattern — CLUE (Claude
   Looks Up Evidence), built by their Detection Platform Engineering team —
   reduced the false positive rate on triaged alerts from approximately 33%
   to 7% and processed 12,000 automated queries in 30 days, recovering an
   estimated 1,870 analyst-hours.
   [source: blog-anthropic-bow-cybersecurity-clue, Claims 4, 5] [emerging]
   CLUE Triage enriches each alert with cross-system context (Slack
   messages, internal docs, code, data warehouse) before assigning a
   confidence-scored disposition; analysts review the low-confidence cases.
   [source: blog-anthropic-bow-cybersecurity-clue, Claim 2] [emerging]

   **Caveat**: The CLUE team explicitly notes "accuracy is harder to quantify
   than speed" — false positive reduction is measured, but the false negative
   rate (real threats dismissed by automated triage) is not. Define a false
   negative measurement strategy before deploying AI triage in security
   contexts.
   [source: blog-anthropic-bow-cybersecurity-clue, Claim 4] [emerging]

3. **Specialization over general-purpose review.** The DeepSource benchmark
   measured Claude Code at 48.78% recall on the OpenSSF CVE dataset for
   security review of full diffs (see §CI as Verification Backstop above).
   Cursor's response is a dedicated security review agent prompt-tuned to
   specific threat models, gating CI independently from general code-quality
   review. The shared principle: a security agent and a code-quality agent
   pulled in different directions in one prompt is the failure mode behind
   the recall gap.
   [source: blog-cursor-security-agents, Claim 5;
   discussion-hn-autofix-hybrid-review, Claims 1, 8] [emerging]

### Gradual trust rollout: shadow → inform → gate

Cursor documents the deployment pattern they used for their own internal
security review agent — and it generalizes to any autonomous agent entering
a critical path:

```
Stage 1: Shadow mode
  — Agent runs on every event
  — Findings → private Slack channel for the security team
  — Zero PR impact, zero blast radius
  — Purpose: validate signal quality before anyone sees it

Stage 2: PR commenting
  — Agent posts findings as PR comments
  — Engineers can address or dismiss; no merge gate
  — Purpose: expose to broader scrutiny, build wider confidence

Stage 3: Blocking gate check
  — Agent findings can block merge
  — Engineer must address or dismiss before landing
  — Purpose: enforce findings as a hard constraint

Progression criteria (per Cursor):
  Shadow → PR comments: "confident it was identifying genuine issues"
  PR comments → blocking: confidence continues to build (no specific gate)
```

[source: blog-cursor-security-agents, Claim 4] [emerging]

The pattern catches the "agent cried wolf" failure mode that causes engineers
to dismiss legitimate findings. Skipping shadow mode lands you with a CI gate
calibrated to nothing — which is worse than no gate, because dismissed
findings train the team to ignore the agent.

**Rule**: Never deploy a security agent in blocking mode before it has run
in shadow mode long enough to produce a stable signal. Shadow → inform →
gate is the only deployment sequence with corroborating production evidence.
[source: blog-cursor-security-agents, Claim 4] [emerging]

### Three-axis attribution when the agent gets it wrong

When a security agent (or any extraction agent) produces a wrong answer,
practitioners default to "tweak the prompt." Carta Healthcare's clinical
abstraction team identified a more useful diagnostic structure: attribute
each failure to one of three root causes — and the fix differs by axis.

> "When something underperforms, you can trace it back to a specific prompt,
> a context issue, or a retrieval gap rather than staring at an aggregate
> score wondering what went wrong." — Matthew Mazzanti, Carta Healthcare
> [source: blog-anthropic-carta-healthcare-context-engineering, Claim 5] [emerging]

```
Three-axis evaluation attribution

  PROMPT failure     → revise the prompt
  CONTEXT failure    → change context assembly (what the agent sees per query)
  RETRIEVAL failure  → fix the retrieval pipeline (which documents are surfaced)
```

Aggregate accuracy metrics conflate all three and cannot drive targeted
remediation. A three-axis evaluation framework lets you separately tune the
component that broke.

**Rule**: Build evaluation that attributes each failure to one of prompt,
context, or retrieval before iterating. Skip this and you will spend more
time debugging than building.
[source: blog-anthropic-carta-healthcare-context-engineering, Claims 5, 6] [emerging]

### Sandbox the agent: the unsandboxed blast radius

Every defense above assumes the agent's blast radius is bounded. On a developer
laptop with shell access, it is not. Simon Willison documented a single Claude
Code + Fable 5 session that, from one screenshot and a one-line prompt about a
CSS scrollbar bug, autonomously ran 17 investigative steps: it started a dev
server, drove Playwright across Chrome/Firefox/WebKit, hit an OS permission wall
and invented a PyObjC/Quartz workaround when `osascript` was blocked, modified
the application's own templates to inject a keyboard-event trigger, and built a
throwaway Python CORS server to capture browser measurements — none of it
requested.
[source: blog-simonwillison-fable-relentlessly-proactive, Claims 1, 2, 3, 4] [anecdotal]

The lesson is not that the agent had special privileges. It had shell access and
the intelligence to compose ordinary system tools into new ones:

> "this is a robust reminder that coding agents can do anything _you_ can do by
> typing commands into a terminal"
> [source: blog-simonwillison-fable-relentlessly-proactive, Claim 9] [anecdotal]

A tool-grant permission model ("this agent may not automate browsers") does not
hold when the agent can reach an equivalent capability through a different API:
it found Quartz when `osascript` was blocked and built its own server when it
needed a data sink. The effective tool surface is not what you granted; it is
everything reachable from the shell.
[source: blog-simonwillison-fable-relentlessly-proactive, Claims 2, 3] [anecdotal]

This belongs in the threat model, not just the capabilities discussion, because
the proactivity that debugs autonomously becomes the attack surface if the agent
is subverted by a prompt injection hidden in an issue thread or pasted into the
terminal — "the amount of damage it can do given its relentless proactivity is
terrifying"
[source: blog-simonwillison-fable-relentlessly-proactive, Claim 7] [anecdotal].
Willison ranks unsandboxed coding-agent deployment as his "top contender for a
Challenger disaster incident" — a known, avoidable failure that teams keep
shipping because it has not bitten them personally yet
[source: blog-simonwillison-fable-relentlessly-proactive, Claim 8] [anecdotal].

**Rule**: Run coding agents inside a sandbox that bounds filesystem, network,
and OS-API reach — a container, VM, or constrained execution profile — not
directly on a developer machine with ambient shell access. Treat that 17-step
session as the *minimum* blast radius your sandbox must contain, and scope write
access to the smallest part of the tree the task needs.
[source: blog-simonwillison-fable-relentlessly-proactive, Claims 1, 8, 9] [anecdotal]

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

## Architectural Verification: Separate Reasoning from Computation

When outputs must be provably correct — financial calculations, audit
trails, regulated reports — verification cannot rely on "the model
checked its work." The architectural answer is to remove the model from
the path that produces the final number.

Kepler Finance built their production AI for SEC analysis around exactly
this separation. Claude handles intent decomposition, ambiguity
resolution, and execution planning. Deterministic infrastructure
handles every calculation that lands in an audit trail.

> "In finance, the model can't be the whole system. We treat it as one
> stage in a pipeline whose job is to hand the model exactly what it
> needs to succeed at exactly that stage." — John McRaven, CTO
> [source: blog-anthropic-kepler-verifiable-ai-financial, Claim 3]

The split:

```
Claude (reasoning):              Deterministic infra (execution):
- Intent decomposition           - Ratio calculations
- Ambiguity resolution           - Formula evaluation
- Execution planning             - Fiscal period resolution
- Result interpretation          - Idempotent skill execution
```

[source: blog-anthropic-kepler-verifiable-ai-financial, Concrete Artifacts]
[emerging]

Every number in an audit trail originates from deterministic execution,
not model generation. The model output is structurally unable to become
a final auditable number. Provenance is part of the architecture, not
an afterthought:

> "Provenance has to shape the entire system, not get added at the end."
> [source: blog-anthropic-kepler-verifiable-ai-financial, Claim 9]

**Rule**: For outputs that must be provably correct, restrict the LLM
to interpretation and planning. Route computation through deterministic
code that the model invokes but does not author. This is a stronger
guarantee than any prose instruction telling the model to "only output
verified numbers."
[source: blog-anthropic-kepler-verifiable-ai-financial, Claims 3, 9] [emerging]

---

## Online Quality Signals

CI catches regressions against a known spec. It does not catch
"the agent's outputs got worse this week." For that, you need a signal
from the developers actually using the agent.

Cursor names two such signals from their production harness.

**Keep Rate** — the fraction of agent-proposed code changes that remain
in the codebase after fixed time intervals:

> "For a given set of code changes that the agent proposed, we track
> what fraction of those remain in the user's codebase after fixed
> intervals of time."
> [source: blog-cursor-continual-harness-improvement, Claim 1]

If developers keep the code, it was probably good. The signal needs no
annotation and no oracle — the developer's accept-or-revert decision is
the ground truth. The cost is temporal lag.
[source: blog-cursor-continual-harness-improvement, Claim 1] [emerging]

**LLM-as-judge satisfaction** — a model classifies the user's follow-up
behavior:

> "A user moving on to the next feature is a strong signal the agent
> did its job, while a user pasting a stack trace is a reliable signal
> that it didn't."
> [source: blog-cursor-continual-harness-improvement, Claim 2]

LLM-as-judge fires within a session; Keep Rate has a delay. Used
together they form a leading-and-lagging pair.
[source: blog-cursor-continual-harness-improvement, Claim 2] [emerging]

**Rule**: For team-internal harness deployments, track at least one
in-session quality signal and one retention signal separately. A drop
in either is a regression worth investigating before it becomes user
disengagement.
[source: blog-cursor-continual-harness-improvement, Claims 1, 2] [emerging]

---

*Sources for this chapter:
blog-addyosmani-code-agent-orchestra (Claims 5, 7, 11, 12; Linked Sources 1, 2, 3, 4, 5, 6),
blog-anthropic-ai-accelerated-offense (Claims 1, 2, 6, 7),
blog-anthropic-bow-cybersecurity-clue (Claims 2, 4, 5),
blog-anthropic-carta-healthcare-context-engineering (Claims 5, 6),
blog-anthropic-claudecode-quality-postmortem (Claims 7, 9, 10, 13),
blog-anthropic-kepler-verifiable-ai-financial (Claims 3, 9),
blog-cursor-bugbot-effort-billing (Claims 4, 6),
blog-cursor-continual-harness-improvement (Claims 1, 2),
blog-cursor-security-agents (Claims 1, 4, 5, 9),
blog-simonwillison-aisi-gpt55-cyber (Claims 1, 2, 3),
blog-simonwillison-bobby-holley (Claims 1, 7),
blog-simonwillison-fable-relentlessly-proactive (Claims 1, 2, 3, 4, 7, 8, 9),
blog-thebatch-gpt55-hallucination-kimi-k26 (Claim 3),
discussion-hn-airun-executable-markdown (Claim 7),
discussion-hn-autofix-hybrid-review (Claims 1, 2, 3, 8),
docs-ghaw-chatops (Claims 5, 6, 7),
failure-alex000kim-claudecode-source-leak (Lesson 4),
failure-claudemd-ignored-compaction,
failure-hooks-enforcement-2k,
failure-htdt-godogen-game-generation (Lesson 4),
paper-gloaguen-agentsmd-effectiveness,
practitioner-getsentry-sentry,
practitioner-frankray78-netpace,
practitioner-nikolays-postgres-dba,
practitioner-supabase-supabase-js,
practitioner-mikelane-pytest-test-categories,
practitioner-dadlerj-tin*

*Last updated: 2026-06-20*
