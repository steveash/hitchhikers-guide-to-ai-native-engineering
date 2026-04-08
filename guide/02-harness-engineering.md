# Harness Engineering

> Your AI agent reads your configuration files before it reads your code.
> The harness — CLAUDE.md, settings, commands, hooks, rules — is the single
> highest-leverage surface you control. Get it right and the agent works
> inside your guardrails from the first turn. Get it wrong and you spend
> every session re-correcting the same mistakes.

This chapter shows you exactly how to structure that harness, with every
recommendation grounded in real practitioner configurations.

---

## CLAUDE.md Structure

The first design decision is shape: how much goes in the root file, and
how does it connect to everything else?

Practitioners have converged on four distinct structures. Pick the one
that matches your situation.

### The Thin Redirect (multi-tool teams)

Put your guidance in a tool-agnostic file and make CLAUDE.md a pointer.
[source: practitioner-getsentry-sentry] [settled]

Sentry's CLAUDE.md is 11 bytes:

```
@AGENTS.md
```

All guidance lives in `AGENTS.md` files (root + subdirectory), and an
`agents.toml` declares support for both Claude and Cursor:

```toml
agents = ["claude", "cursor"]
```

The `@AGENTS.md` syntax is a Claude Code include directive — it imports the
referenced file as if it were inline.

**Use this when**: You support multiple AI tools and want one source of truth.

### The Hub-and-Spoke (documentation-rich monorepos)

Make CLAUDE.md self-contained but link to satellite documents for depth.
[source: practitioner-supabase-supabase-js] [emerging]

Supabase's CLAUDE.md is 931 lines and opens with a link block:

```markdown
> **Essential Documentation**: Always refer to these guides for detailed information:
>
> - **[CONTRIBUTING.md](CONTRIBUTING.md)** - Development guidelines, commit format, PR process
> - **[TESTING.md](docs/TESTING.md)** - Complete testing guide with Docker requirements
> - **[RELEASE.md](docs/RELEASE.md)** - Release workflows and versioning strategy
> - **[MIGRATION.md](docs/MIGRATION.md)** - Migration context from old repositories
> - **[SECURITY.md](docs/SECURITY.md)** - Security policies and responsible disclosure
```

This is "link AND repeat" — the CLAUDE.md still has extensive inline content
but delegates depth to existing human documentation.

**Use this when**: You already have good CONTRIBUTING.md, TESTING.md, etc.

### The Monolith (single-tool, single-developer)

Put everything in one file. Accept the length.
[source: practitioner-frankray78-netpace] [anecdotal]

NetPace's `.claude/CLAUDE.md` is ~450 lines covering TDD enforcement, C#
coding standards, architecture rules, commit checklists, and test scope
boundaries — all in one file. The developer simplified over time: the footer
reads "Last Updated: December 2025 (Simplified - removed custom agents)".

**Use this when**: You are the sole developer with one AI tool and a small project.

### The Terse Redirect-to-External (domain-specific projects)

Keep CLAUDE.md under 30 lines and delegate to an external rule set.
[source: practitioner-nikolays-postgres-dba] [anecdotal]

postgres_dba's entire CLAUDE.md:

```markdown
## Engineering Standards

Follow the rules at https://gitlab.com/postgres-ai/rules/-/tree/main/rules
— always pull latest before starting work.

## SQL Style

- Lowercase keywords (`select`, `from`, `where` — not `SELECT`, `FROM`, `WHERE`)
- `<>` not `!=`

## CI

GitHub Actions (`test.yml`): runs on push and PRs — tests across
PostgreSQL 13, 14, 15, 16, 17, 18.

## Code Review

All changes go through PRs. Before merging, run a REV review
(https://gitlab.com/postgres-ai/rev/) and post the report as a PR comment.

Never merge without explicit approval from the project owner.

## Stack

- Pure SQL reports loaded via `psql` (`\i start.psql`)
- Interactive menu system — user picks a report number
- Works on any Postgres 13+ including managed services
```

**Use this when**: Your standards live somewhere maintainable (wiki, GitLab
repo, handbook) and you want to point rather than duplicate.

**Caveat**: Claude Code cannot fetch arbitrary URLs unless WebFetch or MCP
is configured. The external rules may be opaque to the agent. postgres_dba's
Cursor rules file compensates by inlining the SQL style guide (~100 lines).
[source: practitioner-nikolays-postgres-dba] [anecdotal]

---

## What to Put in CLAUDE.md

> **Caveat: CLAUDE.md rules are advisory, not mandatory.** The Claude Code
> harness wraps CLAUDE.md content in a system-reminder that tells the model
> "this context may or may not be relevant to your tasks." This framing gives
> the model permission to deprioritize or skip your rules. Compliance is
> approximately 70-80% under ideal conditions, degrading further with session
> length, file size, and context compaction. Multiple independent practitioners
> have confirmed this across Opus and Sonnet models, spanning six months of
> reports. Everything in this section still matters -- good CLAUDE.md content
> meaningfully improves agent behavior -- but do not expect 100% compliance
> from prose alone. For rules that must be followed every time, use
> settings.json permissions, blocking hooks, or CI gates (see "The Enforcement
> Hierarchy" below).
> [source: failure-claudemd-ignored-compaction, Lessons 1, 5, 6;
> failure-hooks-enforcement-2k, Lesson 1] [emerging]

Six out of six profiled repos share a common priority order. Lead with
prohibitions, then surgical corrections, then stack context.
[source: practitioner-getsentry-sentry, practitioner-frankray78-netpace,
practitioner-nikolays-postgres-dba, practitioner-supabase-supabase-js,
practitioner-dadlerj-tin, practitioner-mikelane-pytest-test-categories] [settled]

### 1. Prohibitions First

Every profiled repo opens with or prominently features what the agent must
NOT do. This is the highest-signal content in your CLAUDE.md.

**tin** leads with its single most important prohibition:
[source: practitioner-dadlerj-tin]

```markdown
## Important: Use Tin Commands

**Always use built-in tin commands instead of directly modifying `.tin/`
storage on disk.** For example:
- Use `tin thread delete` instead of `rm .tin/threads/<id>.json`
- Use `tin add --unstage` instead of editing `.tin/index.json`

Direct file manipulation can leave the repository in an inconsistent state
(e.g., orphaned staging entries, missing index updates).
```

Note the structure: rule, concrete right-vs-wrong examples, and the failure
mode explaining *why*.
[source: practitioner-dadlerj-tin] [emerging]

**NetPace** uses parallel MUST NEVER / MUST ALWAYS lists:
[source: practitioner-frankray78-netpace]

```markdown
You **MUST NEVER**:
- ❌ Write production code without a failing test first
- ❌ Skip the RED step (must see test fail)
- ❌ Refactor on red (always get to green first)
- ❌ Add "bonus" features not covered by tests
- ❌ Proceed if tests are failing

You **MUST ALWAYS**:
- ✅ Start with a failing test (RED)
- ✅ Run the test and verify it fails
- ✅ Write minimal code to pass (GREEN)
- ✅ Run all tests before refactoring
- ✅ Commit before refactoring
- ✅ Run all tests after refactoring
```

**Supabase** frames prohibitions as numbered pitfalls with wrong/right comparisons:
[source: practitioner-supabase-supabase-js]

```markdown
### Pitfall 2: Running npm Directly

❌ Wrong:
```bash
cd packages/core/auth-js && npm test
```

✅ Correct:
```bash
nx test:auth auth-js
```
```

All three formats work. The key principle: prohibitions before positive guidance.
[source: practitioner-getsentry-sentry, practitioner-frankray78-netpace,
practitioner-supabase-supabase-js, practitioner-dadlerj-tin] [settled]

### 2. Surgical LLM-Targeting Rules

Do not restate your entire style guide. Instead, identify the specific
mistakes your AI agent makes and write one-line corrections for each.
[source: practitioner-nikolays-postgres-dba, practitioner-mikelane-pytest-test-categories] [emerging]

postgres_dba's CLAUDE.md contains exactly two style rules — the two things
LLMs get wrong in SQL:
[source: practitioner-nikolays-postgres-dba]

```markdown
- Lowercase keywords (`select`, `from`, `where` — not `SELECT`, `FROM`, `WHERE`)
- `<>` not `!=`
```

LLMs default to uppercase SQL and `!=`. These two rules have the highest
correction-per-byte ratio in any profiled CLAUDE.md.

pytest-test-categories applies the same strategy for Python:
[source: practitioner-mikelane-pytest-test-categories]

```markdown
- all import statements must be at the top of the file unless there is
  literally no way around it.
- You will never import anything from unittest. If you need something like
  unittest.Mock, fetch it from the pytest-mock mocker fixture.
```

LLMs scatter inline imports and default to `unittest.Mock`. Two lines fix both.

**The pattern**: Identify the 2-5 mistakes your agent makes repeatedly. Write
a one-line rule for each. Skip everything your linter already catches.
[source: practitioner-nikolays-postgres-dba,
practitioner-mikelane-pytest-test-categories] [emerging]

### 3. Stack Context (for non-obvious architectures)

Tell the agent what your project IS when the answer is not obvious from
the file tree.
[source: practitioner-nikolays-postgres-dba, practitioner-dadlerj-tin] [emerging]

postgres_dba explains its unusual architecture:
[source: practitioner-nikolays-postgres-dba]

```markdown
## Stack

- Pure SQL reports loaded via `psql` (`\i start.psql`)
- Interactive menu system — user picks a report number
- Works on any Postgres 13+ including managed services (RDS, Cloud SQL, AlloyDB, etc.)
```

Without this, the agent might try to create a Node.js test harness for a
psql-loaded SQL toolkit.

### 4. CI Awareness

Name your CI file and what it checks. Five of six profiled repos reference CI
in their AI config.
[source: practitioner-getsentry-sentry, practitioner-nikolays-postgres-dba,
practitioner-supabase-supabase-js, practitioner-mikelane-pytest-test-categories,
practitioner-frankray78-netpace] [settled]

```markdown
## CI

GitHub Actions (`test.yml`): runs on push and PRs — tests across
PostgreSQL 13, 14, 15, 16, 17, 18.
```
*[source: practitioner-nikolays-postgres-dba]*

---

## What NOT to Put in CLAUDE.md

### Do not duplicate your linter's job

If a rule is enforced by a linter, formatter, or type checker, remove it
from CLAUDE.md. The tool will catch it; the CLAUDE.md line is wasted context.
[editorial]

pytest-test-categories has ruff, mypy, and isort configured in
`pyproject.toml` and enforced via pre-commit hooks. The CLAUDE.md does not
restate those rules — it only adds the surgical corrections that the tools
do not catch (import placement, unittest prohibition).
[source: practitioner-mikelane-pytest-test-categories] [emerging]

NetPace has an `.editorconfig` with ~180 lines of C# naming and formatting
rules. The CLAUDE.md does not duplicate them — it focuses on TDD workflow
and architecture rules that no linter can enforce.
[source: practitioner-frankray78-netpace] [emerging]

### Do not put architecture documentation that belongs elsewhere

If your CLAUDE.md is mostly architecture docs, move them out. The behavioral
instructions ("when you do X, do Y") are what the agent needs most.
[source: practitioner-mikelane-pytest-test-categories] [anecdotal]

pytest-test-categories' CLAUDE.md is 298 lines, but roughly 200 are
architecture documentation (component descriptions, design patterns). The
actual agent workflow rules — the novel, high-value content — are compressed
into the first ~60 lines.
[source: practitioner-mikelane-pytest-test-categories] [anecdotal]

### Do not use examples from the wrong language

NetPace's `/bugmagnet` command uses JavaScript/Jest examples despite being
a C# project, with a disclaimer: "These examples use JavaScript/Jest syntax
for illustration." This creates a translation burden for the agent and risks
contaminating output style.
[source: practitioner-frankray78-netpace] [anecdotal]

**Rule**: Use your project's actual language and frameworks in all examples.

### Do not auto-generate your AGENTS.md

The ETH Zurich study (Gloaguen et al., arXiv:2602.11988) tested four
agents across SWE-bench Lite and AGENTbench (138 tasks from 12 repos)
and found that LLM-generated AGENTS.md files **reduced success rates
by 0.5-2%** while **increasing inference costs by over 20%** (including
22% more reasoning tokens). Developer-written context files improved
success by ~4% on AGENTbench. The paper is a preprint without significance
tests on headline numbers and covers Python only — treat as strong
directional evidence.
[source: paper-gloaguen-agentsmd-effectiveness, Claims 1-2] [emerging]

The mechanism: auto-generated content is redundant. When documentation
was stripped from the codebase, auto-generated AGENTS.md files actually
improved performance by 2.7% — because the content was just restating
what the agent could discover by reading the code. In a normal codebase
with intact documentation, this redundancy wastes context budget and
dilutes the signal from rules the agent truly needs.
[source: paper-gloaguen-agentsmd-effectiveness, Claim 3] [emerging]

Worse, auto-generated content introduces **anchoring effects**: mentioning
a technology (e.g., tRPC) biases the agent toward using it, even if the
technology is deprecated or not the right choice for the task.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 1] [emerging]

**Rule**: Never run `/init` or equivalent auto-generation commands for
your agent config. Write it by hand. Apply the **filter test** to every
line: Can the agent discover this by reading the code, config files, or
tool output? If yes, delete it. Keep only what requires human judgment,
historical context, or knowledge the codebase does not encode.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 1] [emerging]

**Example** — applying the filter test to a hypothetical AGENTS.md:

```markdown
# BEFORE (auto-generated, fails filter test)
This is a TypeScript project using React 18 and Next.js 14.    ← Agent can read package.json
We use ESLint and Prettier for code formatting.                 ← Agent can read .eslintrc
The test framework is Jest with React Testing Library.          ← Agent can read jest.config.js
Never commit secrets or API keys.                               ← Keep (judgment call)
We migrated from tRPC to REST in Q4 2025; do not use tRPC.     ← Keep (historical context)
Always run `nx affected:test` before commits, not `npm test`.   ← Keep (non-obvious command)

# AFTER (developer-written, passes filter test)
Never commit secrets or API keys.
We migrated from tRPC to REST in Q4 2025; do not use tRPC.
Always run `nx affected:test` before commits, not `npm test`.
```

Three lines instead of six. Every surviving line carries information
the agent cannot discover on its own.

---

## The Three-Tier Boundary System

NetPace's MUST NEVER / MUST ALWAYS pattern (shown above in "Prohibitions
First") is effective but binary: the agent either always does something
or never does. There is no middle ground for operations that require
human judgment.

The three-tier boundary system adds an intermediate tier — "Ask First" —
for operations that are sometimes appropriate and sometimes dangerous.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4 (Good Spec)] [emerging]

```
Always Do:    "Always run tests before commits"
Ask First:    "Ask before modifying database schemas"
Never Do:     "Never commit secrets or API keys"
```

This framework comes from GitHub's analysis of 2,500+ agent configuration
files. It is a complementary tool to the MUST NEVER / MUST ALWAYS pattern,
not a replacement.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4] [emerging]

### When to use three tiers vs. two tiers

Use the two-tier pattern (MUST NEVER / MUST ALWAYS) when your project
is small, your agent operates in a narrow scope, and every operation is
clearly safe or clearly dangerous. This is NetPace's situation — a solo
developer on a CLI tool where TDD is the universal rule.
[source: practitioner-frankray78-netpace] [anecdotal]

Use the three-tier pattern when your project involves operations with
conditional risk — database migrations, API schema changes, permission
modifications, dependency upgrades. These are not universally dangerous,
but they require human judgment about timing and context.
[source: blog-addyosmani-code-agent-orchestra, Linked Source 4] [emerging]

### Example: three-tier boundaries for a web application

```markdown
## Agent Boundaries

### Always Do
- Run the full test suite before committing
- Include type annotations on all new functions
- Update CHANGELOG.md with user-facing changes

### Ask First
- Modifying database migrations (show the migration plan first)
- Changing API response schemas (show affected consumers)
- Adding new dependencies (justify why existing deps don't suffice)
- Modifying authentication or authorization logic

### Never Do
- Commit secrets, API keys, or credentials
- Force-push to main or release branches
- Delete or modify production data access patterns
- Bypass CI checks or pre-commit hooks
```

The "Ask First" tier creates natural quality gates: the agent pauses,
presents its plan, and waits for approval before proceeding. This is
more practical than listing every possible prohibition, because it
acknowledges that some operations are fine in context but dangerous
without it.

### How this maps to existing permission models

tin's per-command tool scoping is a programmatic implementation of the
three-tier pattern: each command declares exactly which tools it can use.
A `/checkout` command cannot commit; a `/commit` command cannot checkout.
The boundaries are enforced by settings.json, not by prose.
[source: practitioner-dadlerj-tin] [anecdotal]

Sentry's granular allowlist (60+ specific Bash command prefixes) is the
"Always Do" tier made explicit — the agent can run listed commands without
asking, and everything else is implicitly forbidden.
[source: practitioner-getsentry-sentry] [anecdotal]

---

## Repetition for Context Resilience

Repeat your most critical rules. This is not sloppiness — it is a
deliberate strategy to survive context window pressure.
[source: practitioner-frankray78-netpace, practitioner-supabase-supabase-js] [emerging]

NetPace repeats "TDD is non-negotiable" three times: in the summary, in
the Core Philosophy heading, and in the closing footer.
[source: practitioner-frankray78-netpace]

```markdown
<!-- In summary -->
**TDD (Test-Driven Development) is non-negotiable.**

<!-- In core philosophy section -->
**TDD is non-negotiable.** Every line of production code must be
written in response to a failing test following the **RED-GREEN-REFACTOR** cycle

<!-- In footer -->
**Philosophy**: Test-Driven Development is non-negotiable
```

Supabase achieves the same effect through structural parallelism — the
Docker requirements table appears 4 times across 4 files.
[source: practitioner-supabase-supabase-js]

**The technique**: Place your cardinal rule at the top, in the relevant
section, and at the bottom. Three placements. The agent encounters it
regardless of where it starts reading.
[source: practitioner-frankray78-netpace, practitioner-supabase-supabase-js] [emerging]

**Caveat**: Repetition improves survival through compaction but does not
guarantee compliance. One practitioner documented emphatic CLAUDE.md rules
("DO *NOT* IGNORE THIS MANDATORY INSTRUCTION!!!!!!!!!") that were still
ignored. For rules that must be followed 100% of the time, repetition is
necessary but not sufficient -- use hooks (Ch03) or settings.json
permissions as the enforcement layer.
[source: failure-claudemd-ignored-compaction, Lesson 4] [emerging]

---

## The Enforcement Hierarchy

Not all enforcement mechanisms are equal. The following hierarchy ranks them
by reliability, from strongest to weakest. Use it to decide WHERE to put
each rule -- the higher up the hierarchy, the more certain the enforcement.
[source: failure-claudemd-ignored-compaction, Lessons 1, 3, 5;
failure-hooks-enforcement-2k, Lessons 1, 3] [emerging]

```
1. settings.json permissions     (100% — harness-enforced, immune to compaction and framing)
2. PreToolUse hooks with exit 2  (100% — harness-enforced blocking, agent cannot proceed)
3. CI gates                      (100% — catches violations post-hoc on committed code)
4. Advisory hooks                (~85-90% — SessionStart/UserPromptSubmit injection,
                                   no "may or may not" framing, but still advisory)
5. CLAUDE.md prose               (~70-80% — subject to harness framing disclaimer
                                   and compaction summarization)
6. Verbal corrections in chat    (~50% — effective in the current turn,
                                   forgotten after compaction)
```

**How to use this**: Move every enforceable prohibition as high up the
hierarchy as possible. "Never run git push --force" belongs in settings.json
(level 1), not in CLAUDE.md (level 5). "Always use conventional commit
messages" belongs in a PreToolUse hook that validates format (level 2) or
CI (level 3). Reserve CLAUDE.md for guidance the model needs to *understand*
-- the "why" behind decisions, architectural context, and stylistic
preferences where imperfect compliance is acceptable.
[source: failure-claudemd-ignored-compaction, Lesson 5;
failure-hooks-enforcement-2k, Lesson 3] [emerging]

The ~60% baseline CLAUDE.md compliance measured by Christopher Montes rose
to 90%+ after deploying a hook-based enforcement system. This is the first
quantitative before/after measurement in our corpus and directly validates
the hierarchy above.
[source: failure-hooks-enforcement-2k, Lesson 3 (Montes measurement)] [emerging]

---

## .claude/settings.json — Permission Models

### The Granular Allowlist (enterprise / high-security)

Sentry's `.claude/settings.json` uses 60+ specific Bash command prefixes.
Each tool is individually listed:
[source: practitioner-getsentry-sentry] [anecdotal]

```json
"Bash(git diff:*)", "Bash(git log:*)", "Bash(git status:*)"
```

Not `"Bash(git:*)"`. They also scope WebFetch to documentation domains
(`"WebFetch(domain:develop.sentry.dev)"`, `"WebFetch(domain:react.dev)"`),
include MCP permissions for internal tools (`mcp__sentry__search_issues`),
and set `"includeCoAuthoredBy": false`.
[source: practitioner-getsentry-sentry] [anecdotal]

### The Per-Command Scope (minimal-privilege per operation)

tin scopes tool permissions to individual slash commands rather than globally.
Each command declares only the specific subcommands it needs:
[source: practitioner-dadlerj-tin] [anecdotal]

```yaml
# branches.md frontmatter
allowed-tools: Bash(tin branch:*)

# checkout.md frontmatter
allowed-tools: Bash(tin checkout:*), Bash(tin branch:*)

# commit.md frontmatter
allowed-tools: Bash(tin commit:*), Bash(tin status:*)
```

Each command gets only the specific subcommands it needs.
[source: practitioner-dadlerj-tin] [anecdotal]

### No Settings at All (prompt-only enforcement)

Three of six profiled repos have no `.claude/settings.json` — all
enforcement is through prose rules in CLAUDE.md. These are "soft"
constraints the agent could technically violate.
[source: practitioner-frankray78-netpace, practitioner-nikolays-postgres-dba,
practitioner-mikelane-pytest-test-categories] [emerging]

**Debated: How granular should permissions be?** Sentry lists 60+
command prefixes. tin scopes per command. Three repos use none. The right
answer depends on your threat model: for open-source repos where anyone
can trigger an agent, granular allowlists are defensive. For solo projects,
prompt-based rules may suffice.
[source: practitioner-getsentry-sentry, practitioner-dadlerj-tin,
practitioner-frankray78-netpace] [editorial]

---

## Custom Commands

### The Mega-Command (complete methodology in one file)

NetPace's `/bugmagnet` is a 767-line custom command encoding a complete
testing methodology with 5 phases, explicit user pause points, and a
30+ category edge case checklist.
[source: practitioner-frankray78-netpace] [anecdotal]

Key structural elements: phase gates ("pause and wait for user input"),
attempt limits ("Maximum 3 attempts per test"), assertion quality checks
("CRITICAL: Ensure assertions match the test title"), and a bug
documentation standard (root cause, code location, proposed fix).

The command is language-agnostic and portable. Its Common Edge Case Checklist
(~220 lines) covers numeric boundaries, date/time edge cases, Unicode,
file path limits, and geographic data formats.
[source: practitioner-frankray78-netpace] [anecdotal]

### Workflow Commands (PR, review, setup)

Sentry uses three targeted commands for specific workflows:
[source: practitioner-getsentry-sentry] [anecdotal]

**`/gh-pr`** — creates a PR, checks if the diff mixes `static/` with
`src/`/`tests/`, and splits into separate PRs if so. Enforces backend-first
landing when frontend depends on new APIs.

**`/gh-review`** — reviews PR feedback with an anti-sycophancy stance:

> Do NOT assume feedback is valid. You should always verify that the
> feedback is truthful (the bug is real, for example), and then attempt
> to address it.

[source: practitioner-getsentry-sentry] [anecdotal]

### Conversational Commands (context-then-prompt)

tin's slash commands implement a two-phase interaction pattern:
[source: practitioner-dadlerj-tin] [anecdotal]

```markdown
If $ARGUMENTS is provided, checkout that branch:
```
tin checkout $ARGUMENTS
```

If no branch name is provided, first run `tin branch` to show available
branches, then ask the user which branch to checkout.
```

When the user provides an argument, execute immediately. When they do not,
show context and prompt for input. This makes commands usable both as
quick fire-and-forget operations and as guided workflows.
[source: practitioner-dadlerj-tin] [anecdotal]

---

## Hooks — Silent Behavior Injection

Hooks run automatically at lifecycle events without the agent's awareness.
They are the only mechanism that enforces behavior the agent cannot choose
to skip.
[source: practitioner-dadlerj-tin] [anecdotal]

tin configures four Claude Code lifecycle hooks in `.claude/settings.json`:
[source: practitioner-dadlerj-tin]

```json
{
  "hooks": {
    "SessionStart": [
      {"hooks": [{"type": "command",
                   "command": "tin hook session-start",
                   "timeout": 30}]}
    ],
    "UserPromptSubmit": [
      {"hooks": [{"type": "command",
                   "command": "tin hook user-prompt",
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

These hooks track every conversation as a versioned tin thread. The
`SessionEnd` hook auto-commits with the first human prompt as the commit
message. The agent never invokes these — they fire silently.

### Anti-pattern: Hardcoded absolute paths

tin's committed settings.json contains `/Users/danieladler/Dev/tin/tin/tin`.
pytest-test-categories hardcodes `/Users/mikelane/dev/effective-testing-with-python/`.
Both break for any other contributor.
[source: practitioner-dadlerj-tin, practitioner-mikelane-pytest-test-categories] [emerging]

**Rule**: Never commit machine-specific absolute paths in AI config files.
Use PATH resolution, relative paths, or generate the config dynamically.

---

## Multi-Tool Configuration

### Strategy 1: Tool-Agnostic Canonical File (AGENTS.md)

Sentry uses `AGENTS.md` as the source of truth. CLAUDE.md redirects with
`@AGENTS.md`. Cursor reads AGENTS.md natively. The `agents.toml` declares
`agents = ["claude", "cursor"]`.
[source: practitioner-getsentry-sentry]

**Advantage**: Single source of truth, no drift.
**Disadvantage**: Requires all tools to support AGENTS.md (or redirects).

### Strategy 2: Parallel Files at Different Depths

postgres_dba maintains `CLAUDE.md` (~30 lines, terse) and
`.cursor/rules/sql-style.mdc` (~100 lines, with good/bad examples).
Same ground, different detail levels. The `.gitignore` excludes
`.cursor/environment.json` but commits `.cursor/rules/`.
[source: practitioner-nikolays-postgres-dba]

**Advantage**: Each tool gets instructions calibrated to its behavior.
**Disadvantage**: Two files to maintain; drift risk.

### Strategy 3: Triple-Tool Parity

Supabase maintains three parallel files — CLAUDE.md (931 lines),
.cursorrules (183 lines), and WARP.md (660 lines) — covering Claude,
Cursor, and Warp respectively.
[source: practitioner-supabase-supabase-js]

All three convey the same core knowledge at different verbosity levels.
The Docker requirements table is repeated in all three files plus
docs/TESTING.md — four copies total.

**Advantage**: Each tool gets a purpose-built config.
**Disadvantage**: When a command changes, 3+ files need updating.
[source: practitioner-supabase-supabase-js] [anecdotal]

### Strategy 4: Identical Duplication

tin maintains byte-for-byte identical CLAUDE.md and AGENTS.md (both 78 lines).
[source: practitioner-dadlerj-tin]

**Advantage**: Simple to understand.
**Disadvantage**: Any edit must be applied to both files. Sentry's redirect
pattern (`@AGENTS.md`) avoids this.
[source: practitioner-dadlerj-tin] [anecdotal]

**Our take** [editorial]: Strategy 1 (tool-agnostic canonical file with
redirects) is the most maintainable for teams. Strategy 2 (parallel files at
different depths) is reasonable when tools genuinely need different instruction
density. Strategy 3 (triple parity) creates too much drift risk for most
teams. Strategy 4 (identical duplication) is strictly worse than a redirect.

---

## Monorepo Patterns

### Subdirectory Routing

Sentry's root AGENTS.md acts as a router, directing agents to load the
right guide based on what files they are editing:
[source: practitioner-getsentry-sentry] [anecdotal]

```markdown
- **Backend** (`src/**/*.py`) -> `src/AGENTS.md` (backend patterns)
- **Tests** (`tests/**/*.py`) -> `tests/AGENTS.md` (testing patterns)
- **Frontend** (`static/**/*.{ts,tsx}`) -> `static/AGENTS.md` (frontend patterns)
- **General** -> This file (`AGENTS.md`) for Sentry overview and commands
```

Each subdirectory guide is self-contained. The root file serves as a router,
not a summary.
[source: practitioner-getsentry-sentry] [anecdotal]

### Per-Package Test Command Matrix

When packages in a monorepo have different test commands, document the
mapping explicitly.
[source: practitioner-supabase-supabase-js] [anecdotal]

```markdown
| Package      | Docker Required | Complete Test Command               |
| ------------ | --------------- | ----------------------------------- |
| auth-js      | ✅ Yes          | `nx test:auth auth-js`              |
| storage-js   | ✅ Yes          | `nx test:storage storage-js`        |
| postgrest-js | ✅ Yes          | `nx test:ci:postgrest postgrest-js` |
| functions-js | ✅ Yes          | `nx test functions-js`              |
| realtime-js  | ❌ No           | `nx test realtime-js`               |
| supabase-js  | ❌ No           | `nx test supabase-js`               |
```

Each package has a DIFFERENT test command — not a uniform `nx test <pkg>`.
[source: practitioner-supabase-supabase-js] [anecdotal]

### Build-Tool-Injected Config Blocks

Supabase's CLAUDE.md contains an Nx-maintained block auto-appended by tooling:
[source: practitioner-supabase-supabase-js] [anecdotal]

```html
<!-- nx configuration start-->
- When running tasks, always prefer running the task through `nx`
- NEVER guess CLI flags - always check nx_docs or `--help` first when unsure
<!-- nx configuration end-->
```

The HTML comments mark the auto-managed section boundaries. If your build
system can contribute to AI config, let it — but use clear delimiters.
[source: practitioner-supabase-supabase-js] [anecdotal]

---

## Skills and External Config

### External Skill Repositories

Sentry's `agents.toml` pulls skills from external repositories:
[source: practitioner-getsentry-sentry] [anecdotal]

```toml
[[skills]]
name = "*"
source = "getsentry/skills"

[[skills]]
name = "warden-sweep"
source = "getsentry/warden"

[[skills]]
name = "warden"
source = "getsentry/warden"
```

With `pin = false` and `gitignore = true`, skills update dynamically. The
`.claude/skills/` directory is a symlink to `.agents/skills/`, bridging
Claude Code's expected path to the tool-agnostic location.
[source: practitioner-getsentry-sentry] [anecdotal]

### Production Data as Agent Skills

Sentry's `sentry-backend-bugs` skill encodes patterns from 638 real
production issues (27M events, 65k+ users). Each check is ordered by
frequency and impact, includes "not a bug" guardrails, and uses a
confidence threshold (HIGH = report with fix, MEDIUM = needs verification,
LOW = do not report).
[source: practitioner-getsentry-sentry] [anecdotal]

```markdown
Check 1: Metric Subscription Query Errors — 113 issues, 3,035,640 events
Check 2: Missing Record / Stale Reference — 81 issues, 1,403,592 events
Check 7: Database Constraint Violations — 22 issues, 2,962,198 events
```

If you have a bug tracker with categorized issues, you can build this.
[source: practitioner-getsentry-sentry] [anecdotal]

### Domain-Specific Skills as Workflow Guides

Sentry also maintains skills for `hybrid-cloud-rpc` (8-step RPC service
guide), `notification-platform` (9-step notification system guide), and
`generate-migration` (Django migration patterns with two-phase
`SafeRemoveField`).

**Pattern**: If a task requires more than 5 steps and involves
domain-specific knowledge, extract it into a skill rather than keeping it
in AGENTS.md.
[source: practitioner-getsentry-sentry] [editorial]

---

## Process Enforcement via CLAUDE.md

### Issue-First Workflow

pytest-test-categories mandates that the agent create a GitHub issue
before starting any work:
[source: practitioner-mikelane-pytest-test-categories] [anecdotal]

```markdown
**CRITICAL: All agents working on this repository MUST follow these requirements:**

1. **GitHub Issue Required**: Create a GitHub issue for ALL work before
   starting implementation
   - Use descriptive titles and comprehensive descriptions
   - Add appropriate labels (bug, enhancement, documentation, etc.)
   - Reference related issues if applicable
   - Keep the issue updated with progress, blockers, and decisions
```

[source: practitioner-mikelane-pytest-test-categories] [anecdotal]

### Documentation Atomicity

pytest-test-categories requires doc updates in the same commit as code:
[source: practitioner-mikelane-pytest-test-categories] [anecdotal]

```markdown
4. **Documentation Maintenance**: Keep documentation synchronized with code changes
   - Update relevant documentation in the SAME commit as code changes
   - This includes: README.md, CHANGELOG.md, docstrings, and this CLAUDE.md
```

NetPace takes a lighter approach — a pre-commit checklist naming specific files:
[source: practitioner-frankray78-netpace]

```markdown
### Before Committing
- **Documentation is updated**
   - **README.md** - Contains static `--help` output
   - **USER_GUIDE.md** - Check if any sections reference the changed options
```

---

## Anti-Patterns (With Evidence)

### 1. Plans That Contain Results

NetPace's `.claude/plans/aot-investigation.md` contains both the blank
template ("After completing all tests, fill this section") AND filled-in
results from an actual investigation run ("AOT Compilation Status: BROKEN").
This mixes template with data, making the plan unreusable.
[source: practitioner-frankray78-netpace] [anecdotal]

**Fix**: Keep plan templates clean. Store investigation results in a
separate file or in a git commit message.

### 2. Content Duplication Across Guide Layers

Sentry's `static/AGENTS.md` overlaps with the `design-system` skill.
Supabase's Docker table appears in 4 files.
[source: practitioner-getsentry-sentry, practitioner-supabase-supabase-js] [anecdotal]

**Rule**: Intentional repetition of cardinal rules is a feature. Accidental
duplication of reference material is a maintenance burden. Know the difference.
[editorial]

### 3. No Settings.json When You Need One — CRITICAL

Three repos have no `.claude/settings.json`. NetPace's "TDD is
non-negotiable" is entirely prompt-enforced — the agent could skip it.
[source: practitioner-frankray78-netpace, practitioner-nikolays-postgres-dba,
practitioner-mikelane-pytest-test-categories] [emerging]

This is now a known structural vulnerability, not just a missed best
practice. CLAUDE.md prose is followed approximately 70-80% of the time
(see "The Enforcement Hierarchy" above). These three repos have ZERO
harness-enforced constraints. Every prohibition, every workflow rule,
every safety boundary is subject to the model's discretion and will
degrade further after context compaction. Settings.json permissions are
the only mechanism that is 100% reliable, immune to compaction, and
immune to the "may or may not be relevant" framing the harness applies
to CLAUDE.md content.
[source: failure-claudemd-ignored-compaction, Lessons 1, 5;
failure-hooks-enforcement-2k, Lesson 1] [emerging]

**Rule**: If a rule is critical enough to state in your CLAUDE.md at all,
ask whether it can be enforced with settings.json or a hook instead.
CLAUDE.md rules are followed ~70-80% of the time. Settings.json
permissions are followed 100% of the time.
[source: failure-claudemd-ignored-compaction, Lesson 5] [emerging]

### 4. Very Long Subdirectory Guides

Sentry's `src/AGENTS.md` is ~700 lines. This risks overwhelming agent
context windows. Extract stable content into skills; keep guides focused
on rules that change.
[source: practitioner-getsentry-sentry] [editorial]

### 5. CLAUDE.md as Architecture Dump

pytest-test-categories' CLAUDE.md is 298 lines, but ~200 are architecture
docs. The high-value workflow rules are in the first ~60 lines.
Move architecture docs to ARCHITECTURE.md. Keep CLAUDE.md behavioral.
[source: practitioner-mikelane-pytest-test-categories] [editorial]

---

## Quick Reference: Harness File Inventory

| File | Purpose | Who Has It |
|------|---------|-----------|
| `CLAUDE.md` | Primary agent instructions | 6/6 repos |
| `AGENTS.md` | Tool-agnostic agent instructions | sentry (canonical), tin (duplicate of CLAUDE.md) |
| `.claude/settings.json` | Permissions, hooks, MCP | sentry, tin |
| `.claude/commands/*.md` | Slash commands | sentry (3), NetPace (1), tin (3) |
| `.claude/plans/*.md` | Investigation/implementation plans | NetPace (2) |
| `.claude/skills/` | Domain-specific skill guides | sentry (16, via symlink) |
| `agents.toml` | Multi-tool skill registry | sentry |
| `.cursorrules` | Cursor IDE instructions | supabase |
| `.cursor/rules/*.mdc` | Cursor rule files | postgres_dba |
| `WARP.md` | Warp terminal AI instructions | supabase |

---

*Sources for this chapter:
blog-addyosmani-code-agent-orchestra (Claims 7, 11; Linked Sources 1, 4),
failure-claudemd-ignored-compaction,
failure-hooks-enforcement-2k,
paper-gloaguen-agentsmd-effectiveness,
practitioner-getsentry-sentry,
practitioner-frankray78-netpace,
practitioner-nikolays-postgres-dba,
practitioner-supabase-supabase-js,
practitioner-dadlerj-tin,
practitioner-mikelane-pytest-test-categories*

*Last updated: 2026-04-08*
