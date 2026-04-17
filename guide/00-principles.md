# Principles

> The mental models that hold up across tools, models, and workflows.
> These are the load-bearing ideas underneath every recommendation in this guide.
> If you skip this chapter, the rest of the guide is a bag of tricks.
> If you internalize this chapter, you can derive the rest yourself.

---

## Verification Over Generation

The bottleneck is no longer generation. It is verification.
[source: blog-addyosmani-code-agent-orchestra, Claim 5] [emerging]

This is the lead principle because it reframes everything else. AI coding
agents can produce code faster than you can read it. The scarce resource
is not writing speed -- it is your ability to confirm that what was written
is correct, secure, and comprehensible.

### What this looks like in practice

Sentry's `/gh-review` command encodes a verification-first stance:

```markdown
Do NOT assume feedback is valid. You should always verify that the
feedback is truthful (the bug is real, for example), and then attempt
to address it.
```

This is anti-sycophancy applied to code review. The agent is told to
distrust feedback -- including feedback from other agents.
[source: practitioner-getsentry-sentry] [anecdotal]

Five of six profiled repos enforce CI gates on pull requests. The CI
pipeline is the verification backstop that catches what human review
misses after a long session.
[source: practitioner-getsentry-sentry, practitioner-nikolays-postgres-dba,
practitioner-supabase-supabase-js, practitioner-mikelane-pytest-test-categories,
practitioner-frankray78-netpace] [settled]

### The rule

**Treat every AI-generated change as untrusted input.** Review it with
the same rigor you would apply to a pull request from a new contractor
who has never seen your codebase. If you cannot explain what the code
does and why, you have not verified it -- you have just approved it.
[editorial]

### Counter-evidence

Some practitioners report running 50+ turn sessions with no quality
degradation when the harness is well-configured (strong CLAUDE.md,
CI gates, hooks). The comprehension debt research studied engineers
without these guardrails. It is possible that a sufficiently good
harness reduces comprehension loss -- but no study has tested this yet.
[editorial]

---

## Specification Quality Is the New Leverage Point

When you orchestrate multiple agents in parallel, vague thinking multiplies
errors across the entire fleet. Specification clarity is what separates
engineers who get 10x leverage from agents from those who get 10x bugs.
[source: blog-addyosmani-code-agent-orchestra, Claim 10] [emerging]

GitHub analyzed 2,500+ agent configuration files and found that most
fail because they are too vague -- not because they are wrong.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4 (Good Spec)] [emerging]

This finding has a corollary that some engineers find uncomfortable:
strong software engineers get MORE leverage from AI tools than weak ones,
not less. The skill that matters is not "prompting" -- it is the ability
to decompose problems, specify acceptance criteria, and anticipate edge
cases. These are the same skills that made engineers effective before AI.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 2 (Factory Model)] [emerging]

### What this looks like in practice

NetPace's CLAUDE.md encodes a complete TDD specification in its MUST
NEVER / MUST ALWAYS lists. The spec is so precise that the agent has
no room for interpretation:

```markdown
You **MUST NEVER**:
- Write production code without a failing test first
- Skip the RED step (must see test fail)
- Refactor on red (always get to green first)
- Add "bonus" features not covered by tests

You **MUST ALWAYS**:
- Start with a failing test (RED)
- Run the test and verify it fails
- Write minimal code to pass (GREEN)
- Run all tests before refactoring
```

This is not a vague instruction to "follow TDD." It is a specification
with unambiguous success and failure criteria.
[source: practitioner-frankray78-netpace] [anecdotal]

Sentry takes a different approach to the same principle: domain-specific
skills with explicit acceptance criteria. The `sentry-backend-bugs` skill
encodes patterns from 638 real production issues with confidence thresholds
(HIGH = report with fix, MEDIUM = needs verification, LOW = do not report).
[source: practitioner-getsentry-sentry] [anecdotal]

### The rule

**Write specs with the precision of test cases.** Every task you give an
agent should have: (1) what "done" looks like, (2) what the agent must
not touch, and (3) how to verify the result. If you cannot write these
three things, you do not understand the task well enough to delegate it.
[editorial]

---

## Deterministic Tools for Deterministic Work

If a linter, formatter, type checker, or test suite can enforce a rule,
that rule should not be in your CLAUDE.md. AI agents are for judgment calls,
not mechanical enforcement.
[editorial, see also: Editorial Constitution Tenet #10]

This principle now has quantitative support. The ETH Zurich study
(Gloaguen et al., arXiv:2602.11988) tested four agents across SWE-bench
Lite and AGENTbench (138 tasks) and found that LLM-generated AGENTS.md
files reduced success rates by 0.5-2% while increasing inference costs
by over 20% (including a 22% reasoning token overhead). The auto-generated
content was redundant: agents could discover it by reading the code.
[source: paper-gloaguen-agentsmd-effectiveness, Claim 1] [emerging]

Developer-written context files improved success by ~4% on AGENTbench.
The difference: developers wrote what the agent could NOT discover on its
own -- judgment calls, historical context, "we tried X and it broke Y."
Note: the paper is a preprint without significance tests on headline
numbers and covers Python-only repos, so treat as strong directional
evidence rather than settled fact.
[source: paper-gloaguen-agentsmd-effectiveness, Claim 2] [emerging]

### What this looks like in practice

pytest-test-categories has ruff, mypy, and isort configured in
`pyproject.toml` and enforced via pre-commit hooks. The CLAUDE.md does
not restate those rules. It adds only the two surgical corrections that
the tools do not catch:

```markdown
- all import statements must be at the top of the file unless there is
  literally no way around it.
- You will never import anything from unittest. If you need something like
  unittest.Mock, fetch it from the pytest-mock mocker fixture.
```

Two lines. High correction-per-byte ratio. Everything the linter handles
is left to the linter.
[source: practitioner-mikelane-pytest-test-categories] [emerging]

postgres_dba demonstrates the same principle at the extreme: its entire
CLAUDE.md is ~30 lines, containing exactly two style rules that LLMs
consistently get wrong (lowercase SQL keywords, `<>` not `!=`). Everything
else is delegated to CI and an external rule repository.
[source: practitioner-nikolays-postgres-dba] [anecdotal]

### The rule

**Apply the filter test to every line of your CLAUDE.md**: Can the agent
discover this by reading the code, config files, or tool output? If yes,
delete it. Keep only what requires human judgment, historical context, or
knowledge the codebase does not encode.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 1 (AGENTS.md post)] [emerging]

---

## Context Is a Budget, Not a Feature

Every line you add to CLAUDE.md costs attention. Model performance drops
as instructions pile up, even for frontier models -- a phenomenon documented
as "the Curse of Instructions."
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4 (Good Spec)] [emerging]

This interacts with the "deterministic tools" principle above: lines that
restate linter rules are not just redundant, they actively degrade performance
on the rules that matter. Bloated context files dilute signal.

### What this looks like in practice

The profiled repos show a clear pattern: the most effective configurations
are not the longest. postgres_dba's 30-line CLAUDE.md is arguably more
effective per-byte than supabase's 931-line version, because every line
in postgres_dba carries novel, non-discoverable information.
[source: practitioner-nikolays-postgres-dba, practitioner-supabase-supabase-js] [emerging]

Sentry solves the length problem architecturally: a thin root CLAUDE.md
(11 bytes) redirects to AGENTS.md, which acts as a router to subdirectory
guides. The agent loads only the guide relevant to the files it is editing.
[source: practitioner-getsentry-sentry] [anecdotal]

```
- Backend (src/**/*.py) -> src/AGENTS.md
- Tests (tests/**/*.py) -> tests/AGENTS.md
- Frontend (static/**/*.{ts,tsx}) -> static/AGENTS.md
```

### The rule

**Treat your agent configuration like a token budget.** Every line must
earn its place. If you cannot point to a concrete failure it prevents,
cut it.
[editorial]

---

## The Comprehension Work Is the Job

AI makes code cheap to generate. It does not make understanding cheap to
skip. The comprehension work -- reading the code, understanding why it
was written that way, knowing what breaks when you change it -- is still
the job.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 6 (Comprehension Debt)] [emerging]

The Anthropic study found two distinct usage patterns among engineers using
AI tools:

1. **Delegation** (below 40% comprehension): "Write the function for me."
2. **Conceptual inquiry** (above 65% comprehension): "Explain how this
   function handles edge case X."

Sessions where you use the agent to learn produce better comprehension
outcomes than sessions where you delegate blindly.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 6] [emerging]

### What this looks like in practice

Simon Willison's heuristic, cited in the Good Spec post: "I won't commit
code I couldn't explain to someone else." This is the practitioner version
of the comprehension principle -- a personal rule that forces understanding
before approval.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4] [anecdotal]

NetPace's TDD-first workflow enforces comprehension structurally: you write
the failing test first, which means you must understand the expected
behavior before the agent writes any implementation code.
[source: practitioner-frankray78-netpace] [anecdotal]

### The rule

**Before you approve AI-generated code, answer two questions**: (1) What
does this code do? (2) What would break if I changed line N? If you cannot
answer both, you are accumulating comprehension debt. Use the agent to help
you understand, not to help you avoid understanding.
[editorial]

---

## Summary: Five Principles

| # | Principle | One-line test |
|---|-----------|---------------|
| 1 | Verification over generation | Can I explain what this code does and why? |
| 2 | Specification quality is leverage | Does my task spec have acceptance criteria? |
| 3 | Deterministic tools for deterministic work | Can the linter catch this? Then delete it from CLAUDE.md. |
| 4 | Context is a budget | Does every line in my config prevent a concrete failure? |
| 5 | The comprehension work is the job | Would I stake my reputation on this code? |

---

*Sources for this chapter:
blog-addyosmani-code-agent-orchestra (Claims 5, 7, 10; Linked Sources 1, 2, 4, 6),
paper-gloaguen-agentsmd-effectiveness,
practitioner-getsentry-sentry,
practitioner-frankray78-netpace,
practitioner-nikolays-postgres-dba,
practitioner-supabase-supabase-js,
practitioner-mikelane-pytest-test-categories*

*Last updated: 2026-04-08*
