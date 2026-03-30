# Practitioner Profile: mikelane/pytest-test-categories

**Repository**: [mikelane/pytest-test-categories](https://github.com/mikelane/pytest-test-categories)
**Language**: Python | **Stars**: ~8 | **Domain**: pytest plugin for hermetic test enforcement
**Owner**: Mike Lane (solo maintainer, writing "Effective Testing with Python" book)
**Scouted**: 2026-03-30

## Config Surface Area

| File | Lines | Purpose |
|------|-------|---------|
| `CLAUDE.md` | 298 | Agent workflow rules + architecture guide |
| `CONTRIBUTING.md` | 574 | Human + agent contribution protocol |
| `.pre-commit-config.yaml` | 50 | Pre-commit hooks (isort, ruff, mypy, tox) |
| `pyproject.toml` | 293 | Tooling config (ruff, mypy, pytest, commitizen) |
| `.github/pull_request_template.md` | 61 | PR checklist template |
| `.github/PULL_REQUEST_TEMPLATE/release.md` | ~80 | Release PR template |
| `.github/ISSUE_TEMPLATE/` (7 files) | 557 | Structured issue intake (bug, feature, docs, perf, refactor, test, config) |
| `.github/labels.yml` | 184 | Label taxonomy (35+ labels) |
| `.github/workflows/` (6 files) | 908 | CI, release, security, auto-merge |
| `.github/dependabot.yml` | 30 | Weekly dependency updates |
| `.coveragerc` | 14 | Coverage exclusion patterns |
| `ROADMAP.md` | ~350 | Vision, milestones, feature backlog |
| `RELEASING.md` | ~500 | Full release process documentation |

**Total AI config files**: 1 (CLAUDE.md only; no `.claude/`, no AGENTS.md, no agents.toml, no .cursorrules)
**Total AI config lines**: 298
**Total process infrastructure lines**: ~3,500+ (CLAUDE.md + CONTRIBUTING.md + templates + workflows + tooling config)
**No `.claude/` directory, no nested CLAUDE.md files, no Cursor config.**

## Key Insight

This repo is notable not for its AI config file count but for its **process-enforcement depth**. The CLAUDE.md encodes a complete contribution workflow (issue-first, branch, PR, review) that constrains AI agents to the same discipline as human contributors. The surrounding infrastructure (7 issue templates, PR templates, labels taxonomy, CI matrix, pre-commit hooks) makes the CLAUDE.md rules enforceable rather than aspirational.

---

## Patterns

### Pattern 1: Issue-First Workflow Mandate

The CLAUDE.md opens its "Agent Workflow Requirements" with an explicit "CRITICAL" preamble and a numbered 5-step process that begins with issue creation.

**Verbatim** (CLAUDE.md, "Agent Workflow Requirements"):
```
**CRITICAL: All agents working on this repository MUST follow these requirements:**

1. **GitHub Issue Required**: Create a GitHub issue for ALL work before starting implementation
   - Use descriptive titles and comprehensive descriptions
   - Add appropriate labels (bug, enhancement, documentation, etc.)
   - Reference related issues if applicable
   - Keep the issue updated with progress, blockers, and decisions
```

This is reinforced in CONTRIBUTING.md:
```
### 1. Create an Issue First

**All work must be tracked through GitHub issues.** Before starting any work:

1. Search existing issues to avoid duplicates
2. Create a new issue using the appropriate template
```

**Cross-reference**: This is **novel** across all three existing profiles. Sentry delegates to AGENTS.md but never mandates issue creation. NetPace focuses on TDD workflow, not issue tracking. postgres_dba has no workflow rules at all. This is the first profile where the AI agent is expected to create its own issues before writing code.

**Guide impact**: Chapter on "Process Enforcement" -- demonstrates how CLAUDE.md can encode organizational workflow, not just coding rules.

---

### Pattern 2: Branch Protection as Agent Constraint

The prohibition on direct commits to main is stated in both CLAUDE.md and CONTRIBUTING.md.

**Verbatim** (CLAUDE.md):
```
2. **Pull Request Required**: ALL changes MUST go through a Pull Request
   - Never commit directly to main branch
   - Create a feature branch for your work
   - Open a PR as soon as you have commits to share
   - Link the PR to the issue (use "Fixes #issue-number" in PR description)
```

**Verbatim** (CONTRIBUTING.md):
```
Never commit directly to `main`. Create a descriptive feature branch:

git checkout -b feature/your-feature-name
```

Branch naming conventions are prescribed:
```
- `feature/*` - New features
- `fix/*` - Bug fixes
- `docs/*` - Documentation only
- `refactor/*` - Code refactoring
- `test/*` - Test improvements
- `perf/*` - Performance improvements
```

**Cross-reference**: **Extends** Sentry's approach. Sentry has `includeCoAuthoredBy: false` and PR split enforcement, but does not explicitly prohibit direct commits to main in its CLAUDE.md (it relies on GitHub branch protection). Here the prohibition is stated as an agent instruction, making it enforceable even without server-side branch protection.

**Guide impact**: Chapter on "Guardrails" -- prohibition stated in config vs. enforced by platform.

---

### Pattern 3: Anti-Attribution Rule

The CLAUDE.md explicitly prohibits co-authored-by lines in commits.

**Verbatim** (CLAUDE.md, "When modifying the plugin"):
```
- do not add attribution or co-authored lines to commits.
```

**Verbatim** (CONTRIBUTING.md, "Commit Message Guidelines > Important Notes"):
```
- **No attribution lines**: Do not add "Co-Authored-By" or attribution lines
```

**Cross-reference**: **Directly corroborates** Sentry's `includeCoAuthoredBy: false` in settings.json. This is the same intent expressed as a prose rule rather than a settings toggle. Two independent practitioners arriving at the same conclusion strengthens the pattern.

**Guide impact**: Chapter on "Attribution" -- two data points now for "suppress AI attribution in commits."

---

### Pattern 4: Documentation-as-Code Synchronization Rule

CLAUDE.md mandates that documentation must be updated in the same commit as code changes.

**Verbatim** (CLAUDE.md):
```
4. **Documentation Maintenance**: Keep documentation synchronized with code changes
   - Update relevant documentation in the SAME commit as code changes
   - This includes: README.md, CHANGELOG.md, docstrings, and this CLAUDE.md
   - Documentation is code - treat it with the same rigor
   - Never merge a PR with outdated documentation
```

This is not just a "keep docs updated" suggestion -- it requires atomicity ("SAME commit") and names the specific files that must be updated.

**Cross-reference**: **Novel** in its specificity. No existing profile requires doc updates in the same commit. NetPace mentions documentation but doesn't enforce co-location with code changes. This is a stronger form of the pattern.

**Guide impact**: Chapter on "Documentation Rules" -- atomic doc updates as an enforceable standard.

---

### Pattern 5: Book Ecosystem Integration

The CLAUDE.md contains a unique rule connecting development work to book content creation.

**Verbatim** (CLAUDE.md):
```
5. **Book Content Updates**: This project is part of the "Effective Testing with Python" book ecosystem
   - Location: `/Users/mikelane/dev/effective-testing-with-python/`
   - When making **significant design decisions**, add an entry to `design-decisions/` using the template
   - When discovering **key insights or quotable content**, add to `notes/key-insights.md`
   - When changing **how tools integrate**, update `notes/tool-ecosystem.md`
   - Design decisions become book content — document the "why" not just the "what"
   - This is NOT required for routine bug fixes or minor changes
```

This is remarkable: the AI agent is instructed to generate content for a book manuscript as a side effect of development work. The local path (`/Users/mikelane/dev/...`) suggests this is a personal dev machine rule, not something that would work in CI.

**Cross-reference**: **Completely novel**. No existing profile uses CLAUDE.md to generate artifacts outside the repository itself. This extends the concept of AI agent instructions beyond code contribution into knowledge capture.

**Guide impact**: New section on "Cross-Repository Side Effects" -- using agent config to capture design rationale for external consumption.

---

### Pattern 6: Explicit Import and Mocking Constraints

The CLAUDE.md contains two surgical rules targeting common AI coding defaults.

**Verbatim** (CLAUDE.md, "When modifying the plugin"):
```
- all import statements must be at the top of the file unless there is literally no way around it.
- You will never import anything from unittest. If you need something like unittest.Mock, fetch it from the pytest-mock mocker fixture.
```

**Cross-reference**: **Corroborates** postgres_dba's pattern of surgical rules targeting LLM defaults. postgres_dba has two rules (`lowercase SQL`, `<> not !=`) that correct specific LLM tendencies. Here, the two rules correct LLM tendencies to (a) use inline imports and (b) default to `unittest.Mock` instead of pytest-mock. Same strategy: identify the specific bad habit and write a one-line prohibition.

**Guide impact**: Chapter on "Surgical Rules" -- add Python-specific examples alongside SQL examples.

---

### Pattern 7: Coverage Target as Infrastructure

The project enforces 100% code coverage through multiple reinforcing mechanisms.

**Verbatim** (CLAUDE.md):
```
### Coverage Validation
```bash
# Check that coverage meets the target (100% by default)
uv run python tests/_utils/check_coverage.py
```

The coverage target is stored in `coverage_target.txt` (currently 100.0).
```

This is enforced via:
1. Pre-commit hooks (tox runs with coverage)
2. CI workflow (coverage report generated, uploaded to Codecov)
3. PR template checklist: `- [ ] Tests achieve 100% coverage`
4. CONTRIBUTING.md: "100% test coverage is required for all new code"

**Cross-reference**: **Extends** NetPace's quality enforcement. NetPace uses TDD ceremony (RED-GREEN-REFACTOR) but doesn't have machine-enforced coverage targets. Here, the coverage target is externalized to a file (`coverage_target.txt`) and checked programmatically.

**Guide impact**: Chapter on "Quality Gates" -- externalized quality thresholds as enforceable infrastructure.

---

### Pattern 8: Structured Issue Templates as Agent Guardrails

The repository has 7 issue templates covering: bug report, feature request, documentation, performance, refactoring, test improvement, and a config.yml for blank issues. Each template uses YAML-based form fields with required/optional validation.

The documentation issue template is notable for including CLAUDE.md as a selectable documentation type:
```yaml
  - type: dropdown
    id: doc-type
    attributes:
      label: Documentation Type
      options:
        - README.md
        - CONTRIBUTING.md
        - CLAUDE.md (architecture/development)
        - API Documentation (docstrings)
```

This means the agent's own config file is treated as a first-class documentation artifact that can have issues filed against it.

**Cross-reference**: **Novel**. No existing profile treats CLAUDE.md as a documented artifact in the issue template system. This creates a feedback loop: the agent can file issues about improving its own instructions.

**Guide impact**: Chapter on "Self-Referential Configuration" -- CLAUDE.md as a living document with its own maintenance workflow.

---

### Pattern 9: Conventional Commits with Scope Enforcement

The CONTRIBUTING.md prescribes a strict conventional commit format with defined types and scopes.

**Verbatim** (CONTRIBUTING.md):
```
### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `test`: Test improvements
- `refactor`: Code refactoring
- `perf`: Performance improvement
- `build`: Build system changes
- `ci`: CI/CD changes
- `chore`: Maintenance tasks

### Scope (Optional)

- `plugin`: Plugin hooks and integration
- `timing`: Timing enforcement
- `distribution`: Distribution validation
- `reporting`: Test size reporting
- `types`: Type definitions
- `docs`: Documentation
- `ci`: CI/CD
```

Combined with commitizen configuration in pyproject.toml:
```toml
[tool.commitizen]
name = "cz_conventional_commits"
version_provider = "pep621"
tag_format = "v$version"
```

**Cross-reference**: **Extends** existing profiles. No other profile specifies commit message format for AI agents. This is process discipline applied to the commit message level.

---

### Pattern 10: Explicit `git add` Prohibition

Both CLAUDE.md and CONTRIBUTING.md prohibit blanket staging.

**Verbatim** (CONTRIBUTING.md):
```
- **Explicit staging**: Never use `git add -A` or `git add --all` - stage files explicitly
```

**Cross-reference**: **Corroborates** a common AI safety pattern. Claude Code's own system prompt includes similar guidance ("prefer adding specific files by name rather than using 'git add -A'"). This practitioner independently arrived at the same rule and encoded it in their CLAUDE.md.

---

## Anti-Patterns Observed

### 1. Local Path Hardcoding
The book ecosystem rule references `/Users/mikelane/dev/effective-testing-with-python/` -- a macOS-specific absolute path. This would break for any other contributor or CI environment. The rule is only useful for the solo maintainer working locally with Claude Code.

### 2. Massive CLAUDE.md Architecture Section
The CLAUDE.md is 298 lines, but roughly 200 of those are architecture documentation (component descriptions, design patterns, testing strategy). This is useful context for an AI agent but duplicates what could live in a dedicated ARCHITECTURE.md. The agent workflow rules (the novel part) are compressed into the first ~60 lines.

### 3. CONTRIBUTING.md Redundancy
Many rules in CLAUDE.md are restated in CONTRIBUTING.md with slight variations. For example, the "never commit to main" rule appears in both, and the "no attribution lines" rule appears in both. This creates a maintenance burden and risk of divergence.

### 4. No `.claude/` Directory
Despite the sophisticated CLAUDE.md, there is no `.claude/settings.json` to configure permissions, no custom commands, and no skills directory. The practitioner relies entirely on prose instructions rather than using Claude Code's native configuration surface. This means the agent must interpret and self-enforce all rules rather than having them enforced by the harness.

---

## Summary Assessment

**Configuration Philosophy**: Process-first, infrastructure-deep. The CLAUDE.md is primarily a workflow document that encodes organizational discipline, not a coding style guide. The surrounding infrastructure (7 issue templates, 6 CI workflows, pre-commit hooks, PR templates, label taxonomy) makes the rules enforceable through the platform rather than through agent self-discipline alone.

**Distinguishing Feature**: The "issue-first" mandate is unique among all profiled practitioners. This is the only profile where the AI agent is expected to create GitHub issues, follow a branch naming convention, link PRs to issues, and maintain a running commentary on its progress -- essentially behaving like a junior developer following team process.

**Scale Comparison**:
- vs. Sentry (43k stars): Far smaller codebase but deeper process encoding. Sentry delegates to AGENTS.md with permission allowlists; this repo uses CLAUDE.md as a complete contribution handbook.
- vs. NetPace (10 stars): Similar scale, different focus. NetPace enforces coding discipline (TDD, naming); this repo enforces process discipline (issues, PRs, documentation atomicity).
- vs. postgres_dba (1.2k stars): Opposite end of spectrum. postgres_dba uses extreme brevity (30 lines); this repo uses extreme thoroughness (298 lines + 574 lines of CONTRIBUTING.md).

**Novel Contributions to the Guide**:
1. Issue-first workflow mandate for AI agents
2. Cross-repository side effects (book content generation)
3. CLAUDE.md as a self-referential documented artifact
4. Documentation atomicity rule ("same commit")
5. Anti-attribution as prose rule (complementing Sentry's settings toggle)
