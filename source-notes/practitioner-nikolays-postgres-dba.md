---
source_url: https://github.com/NikolayS/postgres_dba
repo: NikolayS/postgres_dba
stars: 1249
language: PLpgSQL
project_type: library (SQL diagnostic toolkit)
date_extracted: 2026-03-30
last_checked: 2026-03-30
commit_analyzed: edfb9d36 (master branch, 2026-03-11)
status: current
---

# Practitioner Profile: NikolayS/postgres_dba

> A concise, opinionated AI configuration for a pure-SQL project that demonstrates how CLAUDE.md can effectively govern non-application-code repos by enforcing SQL style conventions, cross-version CI, and mandatory review tooling.

## Repo Context

postgres_dba is a collection of 34 diagnostic SQL reports for PostgreSQL, loaded interactively via `psql` (`\i start.psql`). Users type `:dba` and select a numbered report. There is no application code -- only `.sql` and `.psql` files, plus shell scripts for menu generation and CI. The project targets PostgreSQL 13 through 18 and works on managed services (RDS, Cloud SQL, AlloyDB). It requires only `pg_monitor` privileges (no superuser) for most reports.

## AI Configuration Inventory

| File | Present | Size | Purpose |
|------|---------|------|---------|
| `CLAUDE.md` | Yes | ~30 lines | Engineering standards, SQL style, CI, review policy |
| `.claude/` | No | -- | Not present |
| `AGENTS.md` | No | -- | Not present |
| `.cursor/rules/sql-style.mdc` | Yes | ~100 lines | Detailed SQL style guide with examples |
| `.cursorrules` | No | -- | Not present |
| `.github/workflows/test.yml` | Yes | ~180 lines | CI matrix testing PG 13-18 |
| `.gitignore` | Yes | 2 lines | Excludes `.cursor/environment.json` |

## CLAUDE.md -- Verbatim Content

```markdown
# CLAUDE.md

## Engineering Standards

Follow the rules at https://gitlab.com/postgres-ai/rules/-/tree/main/rules — always pull latest before starting work.

## SQL Style

- Lowercase keywords (`select`, `from`, `where` — not `SELECT`, `FROM`, `WHERE`)
- `<>` not `!=`

## CI

GitHub Actions (`test.yml`): runs on push and PRs — tests across PostgreSQL 13, 14, 15, 16, 17, 18.

## Code Review

All changes go through PRs. Before merging, run a REV review (https://gitlab.com/postgres-ai/rev/) and post the report as a PR comment. REV is designed for GitLab but works on GitHub PRs too.

Never merge without explicit approval from the project owner.

## Stack

- Pure SQL reports loaded via `psql` (`\i start.psql`)
- Interactive menu system — user picks a report number
- Works on any Postgres 13+ including managed services (RDS, Cloud SQL, AlloyDB, etc.)
```

## Patterns Identified

### Pattern 1: Extreme Brevity in CLAUDE.md with External Rule Delegation

The CLAUDE.md is approximately 30 lines and delegates the bulk of engineering standards to an external URL: `https://gitlab.com/postgres-ai/rules/-/tree/main/rules`. This keeps the CLAUDE.md maintainable while linking to a living, versioned rule set.

**Verbatim:**
> Follow the rules at https://gitlab.com/postgres-ai/rules/-/tree/main/rules — always pull latest before starting work.

### Pattern 2: Two Surgical SQL Style Rules

Rather than restating the full style guide, CLAUDE.md distills it to exactly two rules that Claude is most likely to get wrong:

**Verbatim:**
> - Lowercase keywords (`select`, `from`, `where` — not `SELECT`, `FROM`, `WHERE`)
> - `<>` not `!=`

This is effective because: (a) LLMs default to uppercase SQL keywords, and (b) `!=` is the common operator in most programming languages. These two rules are high-frequency, high-impact corrections.

### Pattern 3: Dual-Tool AI Configuration (Claude + Cursor)

The repo maintains both `CLAUDE.md` and `.cursor/rules/sql-style.mdc`, with the Cursor config being substantially more detailed (~100 lines with formatted examples, good/bad comparisons). The CLAUDE.md is a summary; the Cursor rules file is the exhaustive reference. They cover the same ground but at different levels of detail, suggesting the maintainer tailors the level of instruction to the tool's behavior.

### Pattern 4: CI as Verification Backstop

CLAUDE.md explicitly names the CI file and the version matrix, making it clear to the AI that changes must pass across 6 PostgreSQL versions:

**Verbatim:**
> GitHub Actions (`test.yml`): runs on push and PRs — tests across PostgreSQL 13, 14, 15, 16, 17, 18.

The CI itself (`test.yml`) is thorough: it tests every SQL file in both "wide" and "normal" display modes, runs with minimal-privilege `dba_user` (not superuser), and includes regression assertions checking specific output content.

### Pattern 5: Mandatory External Review Tool

The repo requires running a specific external review tool (REV) before merging, and posting its output as a PR comment:

**Verbatim:**
> Before merging, run a REV review (https://gitlab.com/postgres-ai/rev/) and post the report as a PR comment. REV is designed for GitLab but works on GitHub PRs too.

This is notable because it adds a tool-specific step to the AI's PR workflow that goes beyond standard code review.

### Pattern 6: Stack Context for Non-Obvious Architecture

The "Stack" section explains the project's unusual architecture (interactive psql menu, no application code) to prevent the AI from misunderstanding the codebase:

**Verbatim:**
> - Pure SQL reports loaded via `psql` (`\i start.psql`)
> - Interactive menu system — user picks a report number
> - Works on any Postgres 13+ including managed services (RDS, Cloud SQL, AlloyDB, etc.)

### Pattern 7: Comprehensive Cursor Style Guide with PEP8 Philosophy

The `.cursor/rules/sql-style.mdc` file opens by quoting PEP8's consistency hierarchy, then provides detailed formatting rules with good/bad examples. Key rules include:

**Verbatim (from sql-style.mdc):**
> * **Use lowercase SQL keywords** (not uppercase)
> * Root keywords on their own line (except with single argument)
> * Use CTEs instead of nested queries
> * Use meaningful aliases that reflect the data (not just single letters)

### Pattern 8: Minimal-Privilege CI Testing

The CI creates a `dba_user` with only `pg_monitor` role and `SELECT` grants, then runs all tests as that user. This mirrors the real-world usage pattern and catches privilege escalation bugs that superuser testing would miss.

## Anti-Patterns Observed

### 1. No .claude/ Directory
There is no `.claude/settings.json` or `.claude/commands/` directory. Custom Claude commands (like a "run tests" or "check style" command) could reduce friction. Given the project's reliance on specific tools (REV review, CI), pre-built commands would be valuable.

### 2. External Rule Link May Be Opaque to Claude
The CLAUDE.md delegates to `https://gitlab.com/postgres-ai/rules/` but Claude cannot fetch URLs during normal operation (unless using a tool). The rules at that URL are not inlined, so Claude may not actually follow them. The Cursor rules file partially compensates by inlining the SQL style rules.

### 3. No Explicit "Do Not" List
Beyond `!=` vs `<>`, there are no explicit prohibitions (e.g., "do not use implicit joins", "do not use SELECT *"). The Cursor file covers some of these but the CLAUDE.md does not.

## Notable Custom Commands

None found. The repo has no `.claude/commands/` directory.

## Cross-References

This is one of the first profiles being generated, so cross-references are limited. Notable distinctions:

- **Pure SQL domain**: This is unusual -- most AI config files govern application code (TypeScript, Python, etc.). This proves CLAUDE.md is valuable even for SQL-only repos.
- **Dual-tool config**: Having both CLAUDE.md and `.cursor/rules/` is a pattern worth tracking across other repos.
- **Surgical brevity**: The two-rule SQL style section is a model for how to handle LLM-specific failure modes (uppercase keywords, `!=` operator) without over-specifying.

## Guide Impact

### Chapter: "Writing Effective CLAUDE.md"
- **Example of extreme brevity**: This CLAUDE.md should be featured as a model for small, focused projects. The two-rule SQL style section demonstrates "target what the AI gets wrong, not everything."
- **External rule delegation**: The pattern of linking to a living external rule set is worth discussing -- with the caveat that Claude cannot fetch URLs.

### Chapter: "Domain-Specific Configuration"
- **SQL projects**: This is a reference example for configuring AI tools for SQL codebases. Key insight: LLMs default to uppercase SQL and `!=`, so these must be explicitly overridden.

### Chapter: "CI Integration"
- **Version matrix testing**: The 6-version PostgreSQL matrix with minimal-privilege testing is a strong example of verification that catches real compatibility bugs.

### Chapter: "Multi-Tool Configuration"
- **Claude + Cursor coexistence**: The differing levels of detail between CLAUDE.md (terse) and `.cursor/rules/` (verbose with examples) suggests practitioners tune instruction density per tool.

## Extraction Notes

- **Branch analyzed**: `master` (the default branch)
- **No .claude/ directory**: The repo uses CLAUDE.md at root level only, with no Claude-specific settings or commands.
- **Pure SQL is unusual**: This is one of very few repos where CLAUDE.md governs SQL files rather than application code. The configuration is effective precisely because it targets the two most common LLM SQL mistakes.
- **External rules not fetched**: The GitLab rules URL (`https://gitlab.com/postgres-ai/rules/`) was not fetched; its contents may add significant constraints not captured here.
- **CLAUDE.md is recent**: Added on 2026-03-11 (commit edfb9d36), titled "docs: add CLAUDE.md with engineering standards, SQL style, review policy". This is a deliberate, standalone addition rather than organic growth.
- **The .gitignore excludes `.cursor/environment.json`** but commits `.cursor/rules/`, showing intentional separation of local Cursor config from shared rules.
