---
source_url: https://github.com/getsentry/sentry
repo: getsentry/sentry
stars: 43400
language: Python, React/TypeScript
project_type: web-app / monorepo
date_extracted: 2026-03-30
last_checked: 2026-03-30
commit_analyzed: master branch (HEAD as of 2026-03-30)
status: current
---

# Practitioner Profile: getsentry/sentry

> A large-scale monorepo (~43k stars) uses a sophisticated multi-layered AI agent configuration with a thin CLAUDE.md that redirects to a canonical AGENTS.md system, context-aware subdirectory guides for backend/frontend/tests, 16 domain-specific skills under `.agents/skills/`, an `agents.toml` for cross-tool skill sharing, and granular permission allowlists -- representing the most mature agent configuration observed in a production open-source codebase.

## Repo Context

Sentry is a developer-first error tracking and performance monitoring platform. The main repo contains a large-scale Django 5.2+ backend (Python 3.13+) with a React 19/TypeScript frontend. Key infrastructure includes Celery for task queues, PostgreSQL/ClickHouse/Redis for data stores, Kafka for message queuing, and a hybrid cloud architecture with Control Silo / Cell Silo separation. The codebase has ~31 GitHub Actions workflows and uses `devservices` for local development orchestration.

The AI configuration is clearly the product of a dedicated platform/DevEx team. It is multi-agent aware (supporting both Claude Code and Cursor), uses an external skills repository (`getsentry/skills`), and enforces strict frontend/backend PR separation via CI.

## AI Configuration Inventory

| File | Type | Size | Purpose |
|------|------|------|---------|
| `CLAUDE.md` | Redirect | 11 bytes | Contains only `@AGENTS.md` -- thin redirect to canonical source |
| `AGENTS.md` | System prompt (root) | ~300 lines | Project overview, command guide, context-aware loading instructions |
| `src/AGENTS.md` | Backend guide | ~700+ lines | Backend patterns, security (IDOR), architecture, anti-patterns, code templates |
| `tests/AGENTS.md` | Testing guide | ~200 lines | Test conventions, factories, pytest patterns, date stability rules |
| `static/AGENTS.md` | Frontend guide | ~600+ lines | React/TS patterns, core components, design system, RTL testing |
| `agents.toml` | Multi-agent config | ~20 lines | Cross-tool skill registry (Claude + Cursor), trust settings |
| `.claude/settings.json` | Permissions | ~100 lines | Granular bash allowlist, MCP server config, domain-scoped WebFetch |
| `.claude/commands/gh-pr.md` | Command | ~30 lines | PR creation workflow with frontend/backend split enforcement |
| `.claude/commands/gh-review.md` | Command | ~15 lines | PR feedback review with skeptical verification stance |
| `.claude/commands/setup-dev.md` | Command | ~40 lines | Development environment setup guide |
| `.claude/plans/.gitkeep` | Placeholder | 0 bytes | Empty plans directory (reserved) |
| `.claude/skills/` | Symlink | -- | Symlinks to `.agents/skills/` |
| `.agents/skills/` | Skills directory | 16 skills | Domain-specific agent skills with SKILL.md + references |

### Skills Inventory (`.agents/skills/`)

| Skill | SKILL.md Size | Description |
|-------|---------------|-------------|
| `cell-architecture` | ~2KB | Cell/silo routing architecture guide |
| `design-system` | 16.5KB | Core component usage (Flex, Grid, Text, Heading, etc.) |
| `generate-frontend-forms` | unknown | Frontend form generation |
| `generate-migration` | 2KB | Django migration generation with safe deletion/rename patterns |
| `hybrid-cloud-outboxes` | unknown | Cross-silo outbox patterns |
| `hybrid-cloud-rpc` | ~15KB | RPC service creation/testing/deprecation (most detailed skill) |
| `hybrid-cloud-test-gen` | unknown | Hybrid cloud test generation |
| `lint-fix` | 4KB | ESLint scraps rule violation fixing workflow |
| `lint-new` | unknown | New lint rule creation |
| `migrate-frontend-forms` | unknown | Frontend form migration |
| `notification-platform` | ~8KB | Notification system (Email/Slack/Discord/Teams) guide |
| `react-component-documentation` | unknown | React component docs/stories |
| `sentry-backend-bugs` | ~12KB | Bug pattern detection from 638 real production issues |
| `sentry-javascript-bugs` | unknown | JavaScript bug patterns |
| `sentry-security` | ~6KB | Security review based on 37 historical patches |
| `setup-dev` | unknown | Dev environment setup |

## Patterns Identified

### Pattern 1: Thin CLAUDE.md Redirect to Canonical AGENTS.md

The `CLAUDE.md` file is exactly 11 bytes: `@AGENTS.md`. All guidance lives in `AGENTS.md` files, which are declared the "source of truth":

> **IMPORTANT**: AGENTS.md files are the source of truth for AI agent instructions. Always update the relevant AGENTS.md file when adding or modifying agent guidance. Do not add to CLAUDE.md or Cursor rules.

This is a deliberate multi-tool strategy. The `agents.toml` confirms support for both Claude and Cursor:

```toml
agents = ["claude", "cursor"]
```

**Why this matters**: Avoids duplicating guidance across tool-specific files. A single canonical location reduces drift. The `@AGENTS.md` include syntax is a Claude Code feature that imports another file.

### Pattern 2: Context-Aware Subdirectory Loading

The root AGENTS.md explicitly directs agents to load the right guide based on what files they're editing:

> - **Backend** (`src/**/*.py`) -> `src/AGENTS.md` (backend patterns)
> - **Tests** (`tests/**/*.py`, `src/**/tests/**/*.py`) -> `tests/AGENTS.md` (testing patterns)
> - **Frontend** (`static/**/*.{ts,tsx,js,jsx,css,scss}`) -> `static/AGENTS.md` (frontend patterns)
> - **General** -> This file (`AGENTS.md`) for Sentry overview and commands

Each subdirectory AGENTS.md is self-contained with its own tech stack description, patterns, and anti-patterns. The root file avoids duplicating content, instead serving as a router.

### Pattern 3: Extremely Granular Permission Allowlists

The `.claude/settings.json` uses a fine-grained allowlist of 60+ specific Bash command prefixes. Rather than allowing broad categories, each tool is individually listed:

```json
"Bash(git diff:*)", "Bash(git log:*)", "Bash(git status:*)"
```

Not just `"Bash(git:*)"`. They also scope WebFetch to specific documentation domains:

```json
"WebFetch(domain:develop.sentry.dev)",
"WebFetch(domain:docs.djangoproject.com)",
"WebFetch(domain:react.dev)"
```

And include MCP tool permissions for Sentry's own MCP server and Linear:

```json
"mcp__sentry__search_issues",
"mcp__sentry__get_issue_details",
"mcp__claude_ai_Linear__list_issues"
```

Notable: `"includeCoAuthoredBy": false` -- they explicitly disable the co-authored-by trailer.

### Pattern 4: Production Bug Patterns as Agent Skills

The `sentry-backend-bugs` skill is extraordinary. It encodes patterns from **638 real production issues (393 resolved, 220 unresolved, 25 ignored) generating over 27 million error events across 65,000+ affected users**. Each check is ordered by combined frequency and impact:

> Check 1: Metric Subscription Query Errors -- 113 issues, 3,035,640 events
> Check 2: Missing Record / Stale Reference -- 81 issues, 1,403,592 events
> Check 7: Database Constraint Violations -- 22 issues, 2,962,198 events

The skill includes explicit "Not a bug -- do not flag" guardrails:

> - Infrastructure invariants: `.get()` enforcing a deployment precondition (e.g., "default org must exist in single-org mode") should crash -- a 500 signals misconfiguration, not a code defect.

And a confidence threshold system:

> | HIGH | Traced the code path, confirmed the pattern matches a known bug class | Report with fix |
> | MEDIUM | Pattern is present but context may mitigate it | Report as needs verification |
> | LOW | Theoretical or mitigated elsewhere | Do not report |

### Pattern 5: External Skills Registry via agents.toml

The `agents.toml` pulls skills from two external repositories:

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

With `pin = false` and `gitignore = true`, allowing skills to update dynamically. The `.claude/skills/` directory is a symlink to `.agents/skills/`, bridging the tool-agnostic `.agents/` layout to Claude Code's expected structure.

### Pattern 6: Security-First IDOR Prevention in Backend Guide

The `src/AGENTS.md` has an entire section on IDOR prevention, a critical concern for multi-tenant SaaS:

```python
# WRONG: Vulnerable to IDOR - user can access any resource by guessing IDs
resource = Resource.objects.get(id=request.data["resource_id"])

# RIGHT: Properly scoped to organization
resource = Resource.objects.get(
    id=request.data["resource_id"],
    organization_id=organization.id
)
```

And explicitly prohibits trusting user-supplied project IDs:

> When project IDs are passed in the request (query string or body), NEVER directly access or trust `request.data["project_id"]` or `request.GET["project_id"]`. Instead, use the endpoint's `self.get_projects()` method which performs proper permission checks.

### Pattern 7: Frontend/Backend PR Separation Enforced by CI

A recurring theme across multiple config files is the strict separation of frontend and backend changes:

> Frontend (`static/`) and backend (`src/`, `tests/`) are **not atomically deployed**. A CI check enforces this.
> - If your changes touch both frontend and backend, split them into **separate PRs**.
> - Land the backend PR first when the frontend depends on new API changes.

This is enforced at the CI level AND in the agent commands (`gh-pr.md`), creating defense in depth.

### Pattern 8: Skeptical PR Review Stance

The `gh-review.md` command instructs:

> Do NOT assume feedback is valid. You should always verify that the feedback is truthful (the bug is real, for example), and then attempt to address it.

This is a deliberate counterweight to the tendency of AI agents to blindly apply all review feedback.

## Anti-Patterns Observed

### Anti-Pattern 1: Empty Plans Directory

The `.claude/plans/` directory contains only `.gitkeep`. This suggests plans were anticipated but not yet utilized, or that the team decided skills are a better organizational unit. The empty directory adds configuration noise without value.

### Anti-Pattern 2: Potential Content Duplication Across Guide Layers

While the subdirectory routing is well-designed, there is some content overlap. For example, the frontend `static/AGENTS.md` has extensive core component guidance that partially overlaps with the `design-system` skill. The root `AGENTS.md` duplicates the project structure tree that also appears in `src/AGENTS.md`. This creates a maintenance burden despite the "single source of truth" aspiration.

### Anti-Pattern 3: No Explicit AI-Generated Code CI Gate

Despite 31 GitHub Actions workflows, there is no specific workflow that gates AI-generated code differently from human code. The `pre-commit.yml` runs on all PRs equally. While this is arguably the right approach (same standards for all code), there's no additional scrutiny for AI-authored commits (e.g., verifying test coverage, checking for hallucinated imports). The `sentry-pull-request-bot.yml` is only for triggering cross-repo tests.

### Anti-Pattern 4: Very Long Backend Guide

The `src/AGENTS.md` is extremely comprehensive (~700+ lines) with copy-paste patterns, decision trees, API design rules, Arroyo streaming patterns, integration development guides, and more. While thorough, this risks overwhelming agent context windows. The skills system partially addresses this by extracting domain-specific guidance, but the base backend guide remains very large.

## Notable Custom Commands

### `/gh-pr` (`.claude/commands/gh-pr.md`)
A PR creation workflow that:
1. Switches from main to a working branch
2. Commits changes
3. Creates or updates a PR with a concise description focused on "features, breaking changes, major bug fixes, and architectural changes"
4. **Critically**: Checks if the diff mixes `static/` with `src/`/`tests/` and splits if needed
5. Enforces backend-first landing when frontend depends on new API changes

### `/gh-review` (`.claude/commands/gh-review.md`)
A PR review response workflow that:
1. Reviews status checks for failures
2. If no failures, reviews PR feedback
3. Verifies feedback validity before applying -- a deliberate anti-sycophancy measure

### `/setup-dev` (`.claude/commands/setup-dev.md`)
Development environment setup covering devenv installation, `devenv bootstrap`/`devenv sync`, `devservices up`/`devservices serve`, and diagnostic commands.

## Notable Skills (`.agents/skills/`)

### `sentry-backend-bugs`
The most impressive skill in the inventory. Encodes 11 bug pattern checks derived from 638 real production issues. Each check has red flags, safe patterns, and explicit "not a bug" exclusions. This is a pioneering example of using production incident data to train an AI code reviewer.

### `hybrid-cloud-rpc`
An extremely detailed 8-step guide for creating, modifying, and deprecating RPC services in Sentry's hybrid cloud architecture. Includes critical constraints (no `from __future__ import annotations`), step-by-step checklists, and comprehensive testing patterns including silo mode compatibility, serialization round-trips, and cross-silo resource verification.

### `sentry-security`
A security review framework based on 37 historical security patches, checking 6 vulnerability classes. Requires HIGH/MEDIUM confidence threshold and traces a 7-layer enforcement chain before flagging issues.

### `generate-migration`
A compact but critical skill covering Django migration generation with safe patterns for column deletion (two-phase `SafeRemoveField`), table deletion (`SafeDeleteModel`), and a "don't rename in Postgres" rule.

### `notification-platform`
A comprehensive 9-step guide for the notification system covering data classes, templates, renderers, providers, rollout registration, and testing. Shows how complex internal platforms can be documented as agent skills.

## Cross-References

This is the most mature AI agent configuration in the starter set. Key novelties compared to the NetPace profile:

1. **Multi-tool strategy**: `agents.toml` + AGENTS.md pattern vs. single-tool CLAUDE.md approach
2. **External skill repositories**: Skills pulled from `getsentry/skills` and `getsentry/warden` -- no other profiled repo does this
3. **Production incident data as agent input**: The `sentry-backend-bugs` skill encodes real production data (638 issues, 27M events) -- unprecedented
4. **Layered context loading**: Subdirectory AGENTS.md files create a routing system vs. monolithic config
5. **MCP server integration**: `.claude/settings.json` includes Sentry's own MCP server for issue/event access during development
6. **Trust model**: `agents.toml` uses `[trust] allow_all = true` combined with granular `.claude/settings.json` permissions
7. **Co-authored-by disabled**: `"includeCoAuthoredBy": false` -- they don't want AI attribution in commits

## Guide Impact

### Chapter: CLAUDE.md Structure
- **Recommendation**: Document the `@AGENTS.md` redirect pattern as a best practice for multi-tool teams
- **Verbatim example**: CLAUDE.md containing only `@AGENTS.md` (11 bytes)
- **Recommendation**: Document the subdirectory AGENTS.md routing pattern for monorepos

### Chapter: Permission Configuration
- **Recommendation**: Show Sentry's granular bash allowlist as the gold standard for enterprise repos
- **Recommendation**: Document domain-scoped WebFetch as a security pattern
- **Verbatim example**: `"WebFetch(domain:develop.sentry.dev)"` pattern

### Chapter: Custom Commands
- **Recommendation**: Highlight the skeptical review stance (`gh-review.md`) as an anti-sycophancy pattern
- **Recommendation**: Document the PR split enforcement pattern for non-atomic deploy architectures

### Chapter: Skills and Knowledge Injection
- **Recommendation**: Feature the `sentry-backend-bugs` skill as the exemplar of production-data-driven agent guidance
- **Recommendation**: Document the external skill registry pattern (`agents.toml` + `getsentry/skills`)
- **Recommendation**: Show the `hybrid-cloud-rpc` skill as an example of encoding complex architectural workflows

### Chapter: Security
- **Recommendation**: Feature the IDOR prevention section and `sentry-security` skill as models for security guidance
- **Recommendation**: Document the multi-tenant scoping patterns (`organization_id` filtering)

### Chapter: Testing
- **Recommendation**: Feature the testing AGENTS.md as a model for test convention documentation
- **Key rules**: No `Model.objects.create` (use factories), no `unittest` (use pytest), no branching in tests, date-stable test patterns

### Chapter: CI/CD Integration
- **Observation**: Despite sophisticated agent config, Sentry has no AI-specific CI gate -- all code goes through the same 31 workflows. This validates the "same standards for all code" philosophy.

## Extraction Notes

1. **CLAUDE.md content**: The file is only 11 bytes (`@AGENTS.md`). The WebFetch initially returned confusingly as if viewing the included AGENTS.md content; confirmed via GitHub API that the raw file is just the include directive.

2. **No .cursorrules**: A 404 was returned for `.cursorrules` and `.cursor/` directory. Cursor support comes through `agents.toml` declaring `agents = ["claude", "cursor"]` and the tool-agnostic `.agents/skills/` directory.

3. **Skills symlink**: `.claude/skills/` is a symlink to `../.agents/skills/`, bridging Claude Code's expected path to the tool-agnostic location.

4. **External skills not read**: The `getsentry/skills` and `getsentry/warden` external repositories were not fetched. These contain additional skills pulled in by `agents.toml` that would require separate analysis.

5. **Not all 16 skills read in detail**: Full content was retrieved for 7 of 16 skills (cell-architecture, design-system, generate-migration, hybrid-cloud-rpc, lint-fix, notification-platform, sentry-backend-bugs, sentry-security). The remaining 8 skills likely follow the same SKILL.md + references pattern.

6. **WebFetch summarization**: Several file fetches were summarized by the WebFetch tool rather than returned verbatim, particularly for longer files. Key quotes and structural details were preserved but exact line counts may be approximate.

7. **Branch**: All content read from `master` branch (the default branch for getsentry/sentry).
