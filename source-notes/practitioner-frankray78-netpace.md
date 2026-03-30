---
source_url: https://github.com/FrankRay78/NetPace
repo: FrankRay78/NetPace
stars: 10
language: C#
project_type: cli
date_extracted: 2026-03-30
last_checked: 2026-03-30
commit_analyzed: main branch (HEAD as of 2026-03-30)
status: current
---

# Practitioner Profile: FrankRay78/NetPace

> A solo developer uses Claude Code's configuration system as an automated quality enforcement mechanism, centering on a "TDD is non-negotiable" philosophy with an ASCII art RED-GREEN-REFACTOR diagram, comprehensive C#/.NET coding standards, and a remarkably thorough custom `/bugmagnet` command for systematic test coverage and bug discovery.

## Repo Context

NetPace is a cross-platform .NET 8.0 CLI application for network speed testing using Ookla's Speedtest servers. It ships both a CLI app (`NetPace.Console` using Spectre.Console) and a reusable Core library (`NetPace.Core`) published to NuGet. The developer, Frank Ray, is a former Spectre.Console CLI sub-system maintainer who built this project as a dogfooding exercise following clig.dev guidelines.

The repo has ~10 stars, 4 GitHub Actions workflows (build/test, CodeQL security, NuGet publish, cross-platform binary release), and an `.editorconfig` with extensive C# style rules. The AI config is mature and clearly the product of iterative refinement -- the CLAUDE.md footer reads "Last Updated: December 2025 (Simplified - removed custom agents)".

## AI Configuration Inventory

| File | Type | Size | Purpose |
|------|------|------|---------|
| `.claude/CLAUDE.md` | System prompt | ~450 lines | Master development guide with TDD enforcement, C# standards, architecture rules |
| `.claude/commands/bugmagnet.md` | Custom command | ~767 lines | Systematic test coverage analysis and bug discovery workflow |
| `.claude/plans/aot-investigation.md` | Plan document | ~500 lines | AOT compilation feasibility investigation with structured test plan |
| `.claude/plans/netpace-iot-mvp.md` | Plan document | ~700 lines | IoT MVP implementation plan with work packages |
| `.editorconfig` | Code style | ~180 lines | Comprehensive C# naming, formatting, and style rules |
| `.github/workflows/dotnet.yml` | CI | ~25 lines | PR build and test gate |
| `.github/workflows/codeql.yml` | CI | ~40 lines | Weekly CodeQL security analysis |
| `.github/workflows/publish-nuget.yml` | CI | ~40 lines | Tag-triggered NuGet publish |
| `.github/workflows/release-binaries.yml` | CI | ~80 lines | Cross-platform binary release (6 runtimes x 2 deployment modes) |

No `.claude/settings.json`, `.claude/rules/`, `AGENTS.md`, `.cursorrules`, or `.cursor/` config found.

## Patterns Identified

### Pattern 1: Repetition-Based Enforcement ("Say It Three Times")

The phrase "TDD is non-negotiable" appears THREE times in CLAUDE.md -- in the summary, in the Core Philosophy heading, and in the closing footer. This is deliberate redundancy to ensure the instruction survives context window pressure.

**Verbatim (summary):**
> **TDD (Test-Driven Development) is non-negotiable.** Every line of production code must be written in response to a failing test. No exceptions.

**Verbatim (core philosophy):**
> **TDD is non-negotiable.** Every line of production code must be written in response to a failing test following the **RED-GREEN-REFACTOR** cycle

**Verbatim (footer):**
> **Philosophy**: Test-Driven Development is non-negotiable

### Pattern 2: ASCII Art Process Diagram

Rather than just describing the RED-GREEN-REFACTOR cycle in text, the config includes an ASCII art flowchart with boxes and arrows. This is a novel approach to making process instructions visually distinct from surrounding text, potentially reducing the chance the AI skims over them.

**Verbatim:**
```
┌─────────────────────────────────────────────┐
│  1. RED - Write failing test                │
│     - Describes desired behavior            │
│     - Run and watch it FAIL                 │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  2. GREEN - Make test pass                  │
│     - Write minimum code needed             │
│     - Run and watch it PASS                 │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│  3. REFACTOR - Improve code (optional)      │
│     - Commit before refactoring             │
│     - Improve design/remove duplication     │
│     - Run tests - still PASS                │
└──────────────┬──────────────────────────────┘
               │
               ▼
         Back to RED for next behavior
```

### Pattern 3: Dual MUST NEVER / MUST ALWAYS Lists

The config uses parallel negative/positive constraint lists with emoji checkmarks/crosses for maximum clarity. This "what to do AND what not to do" pattern leaves no ambiguity.

**Verbatim:**
```
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

### Pattern 4: Pre-Commit Quality Gate Checklist

The config defines a concrete "Before Committing" checklist that serves as a manual quality gate. This goes beyond just tests to include warnings, conventions, documentation, and the specific files that need updating.

**Verbatim:**
```
### Before Committing
- Build succeeds with **no warnings**
- **All tests pass**
- Code follows **naming conventions**
- Public APIs have **XML documentation**
- No **commented-out code** (delete it, git remembers)
- **Documentation is updated**
   - **README.md** - Contains static `--help` output
   - **USER_GUIDE.md** - Check if any sections reference the changed options
```

### Pattern 5: Separation of "Claude Must" from General Standards

The config maintains a distinct "When Working with Claude Code" section separate from the general coding standards. This creates role-specific instructions rather than mixing AI-specific rules into general documentation.

**Verbatim:**
```
### Claude Must Always
- **Follow TDD strictly** - write failing test before any production code (RED-GREEN-REFACTOR cycle)
- **Add XML documentation** to all public APIs (methods, properties, classes)
- **Consider cross-platform compatibility** (Windows, Linux, macOS)
- **Write testable code** (interfaces, dependency injection)
- **Ask for clarification** if requirements are ambiguous
- **Use built-in planning tools** for non-trivial changes before writing code

### Never Let Claude
- Write production code without a failing test first
- Skip the RED step (must see test fail)
- Change public APIs without discussion and approval
- Add dependencies to NetPace.Core without justification
- Commit code with failing tests or build warnings
```

### Pattern 6: Negative/Positive Test Scope ("What NOT to Test")

The config explicitly lists what should NOT be tested, preventing over-testing and wasted effort. This is rare in AI configs.

**Verbatim:**
```
### What NOT to Test
- **Spectre.Console output** - trust the library works
- **Simple property getters/setters** with no logic
- **Third-party libraries** - assume they work
```

### Pattern 7: Plans as Structured Investigation Templates

The `.claude/plans/` directory contains remarkably detailed investigation templates with pre-built results tables (with blank cells to fill in), decision trees, and step-by-step execution plans. The AOT investigation plan includes a decision tree in ASCII art:

**Verbatim (decision tree excerpt):**
```
Can we AOT compile NetPace with Spectre.Console.Cli?
│
├─ ✅ Yes, all tests pass
│   └─ Recommendation: Use AOT for all IoT builds
│
├─ ⚠️ Partially - Basic commands work, --help broken
│   └─ Recommendation: Add DynamicallyAccessedMembers attributes
│
└─ ❌ No, critical functionality broken
    └─ Recommendation: Switch CLI framework
```

### Pattern 8: The BugMagnet Command -- A Complete Testing Methodology

The `/bugmagnet` command is a 767-line custom command that encodes an entire systematic testing methodology. It is language-agnostic, phased (5 phases with explicit pause points for user input), and includes a comprehensive "Common Edge Case Checklist" covering 30+ categories from numeric boundaries to internationalized text to violated domain constraints.

Key structural elements:
- **Phase gates**: "At the end of each phase, pause and wait for user input or confirmation to proceed"
- **Bug documentation standard**: Bugs must be documented in skipped tests with root cause, code location, proposed fix, and expected vs actual
- **Maximum attempt limits**: "Maximum 3 attempts per test" -- prevents infinite loops
- **Cluster exploration**: "Bugs often cluster together - test similar scenarios"
- **Assertion quality rules**: "CRITICAL: Ensure assertions match the test title"

## Anti-Patterns Observed

### Anti-Pattern 1: Plans Contain Results (Contaminated Templates)

The `aot-investigation.md` plan file contains BOTH the template (blank results tables) AND filled-in results from an actual investigation run. The "Final Recommendation Template" section says "After completing all tests, fill this section" but then contains actual filled-in results (e.g., "AOT Compilation Status: BROKEN - Not Supported"). This mixes template with data, making the plan less reusable.

### Anti-Pattern 2: IoT MVP Plan Has Excessive Scope for AI Context

The `netpace-iot-mvp.md` plan is ~700 lines covering 12 sections including market research, hardware procurement, project board structure, risk assessment, and a 4-phase implementation timeline. While thorough for a human planning document, this is extremely long for AI context consumption. Much of it (market size, success metrics, customer validation quotes) is not actionable by Claude Code.

### Anti-Pattern 3: No Settings.json or Permissions Configuration

Despite the detailed CLAUDE.md, there is no `.claude/settings.json` to configure tool permissions, allowed commands, or MCP settings. The enforcement is entirely prompt-based rather than using Claude Code's native permission system. This means the TDD rules are "soft" constraints -- Claude could technically violate them.

### Anti-Pattern 4: No .claude/rules/ Directory

Claude Code supports a `.claude/rules/` directory for context-specific rules that activate based on file patterns. For a project with distinct Core vs Console components and explicit rules about "Never add dependencies to NetPace.Core without justification," pattern-matched rules would provide targeted enforcement.

### Anti-Pattern 5: BugMagnet Uses JavaScript Examples Despite Being a C# Project

The bugmagnet command's examples are all in JavaScript/Jest syntax with a disclaimer: "These examples use JavaScript/Jest syntax for illustration. Treat them as pseudo-code." For a C#/xUnit project, this creates a translation burden. The examples should use the project's actual testing patterns.

## Notable Custom Commands

### `/bugmagnet <implementation-file-path>`

**Purpose**: Systematic test coverage analysis and bug discovery.

**Structure**: 5-phase workflow with explicit user pause points:
1. **Initial Analysis** -- Read implementation, locate tests, check coverage tools, detect language/framework
2. **Gap Analysis** -- Evaluate missing coverage using the Common Edge Case Checklist, categorize by priority (High/Medium/Low)
3. **Iterative Test Implementation** -- Write tests one at a time, handle failures with 3-attempt limit, document bugs in skipped tests
4. **Advanced Coverage** -- Deep edge case testing using the 30+ category checklist (numbers, dates, strings, collections, state, security, file paths, internationalization, domain constraints)
5. **Summary and Documentation** -- Bug summary with root cause analysis, file locations, proposed fixes

**Key enforcement mechanisms**:
- "DO NOT IMPLEMENT FIXES OR CHANGE THE IMPLEMENTATION FILE, ONLY WRITE TESTS" (caps emphasis)
- Test naming format: "returns X when Y", "throws error when Z" (outcome-focused)
- "CRITICAL: Ensure assertions match the test title" -- prevents weak assertions
- Bug documentation requires: root cause, code location, current code snippet, proposed fix, expected vs actual
- Bug suffix convention: mark test name with "- BUG"
- Cluster exploration: "When you find one bug, look for similar bugs nearby"

**Notable**: This command is completely language-agnostic and portable. It could be dropped into any project. The Common Edge Case Checklist alone (~220 lines) is a standalone testing reference covering: numbers (including currency/financial), dates/times (including leap seconds, DST, 32-bit limits), strings (including Unicode edge cases like ZWJ emoji, homograph attacks), file paths (OS-specific limits, reserved filenames), geographic data (postal code format variations by country), and violated domain constraints (implicit assumptions about uniqueness, ordering, state, temporal validity).

## Cross-References

This is one of the first profiles being built, so cross-references are limited. However, several patterns are notable as potential archetypes:

1. **Repetition-based enforcement** -- The "say it three times" pattern for critical rules (TDD non-negotiable) is a technique worth tracking across repos to see if others independently discover it.

2. **ASCII art process diagrams** -- Novel use of visual formatting in markdown to make process steps stand out. Worth comparing to repos that use mermaid diagrams or other visual approaches.

3. **Language-agnostic custom commands** -- The bugmagnet command is designed to work across any language/framework. This is unusual; most custom commands are project-specific. It suggests the developer may have extracted this from a broader testing practice.

4. **Plans as investigation frameworks** -- Using `.claude/plans/` for structured investigation templates with pre-built results tables and decision trees is a unique workflow pattern. Most repos use plans for implementation, not investigation.

5. **Solo developer using AI config as quality gate** -- This is the central insight. Without a team to enforce code review standards, Frank Ray has encoded his quality expectations into the AI configuration itself. The CLAUDE.md effectively functions as a "reviewer persona" that cannot be bypassed by social pressure.

## Guide Impact

### Chapter: TDD Enforcement
- **Recommendation**: Feature the RED-GREEN-REFACTOR ASCII diagram as a best practice for encoding process workflows. The visual format is more resistant to being skimmed by the AI.
- **Recommendation**: Document the "say it three times" pattern for critical constraints. Note the specific locations: summary, body, and footer/closing.
- **Recommendation**: The dual MUST NEVER/MUST ALWAYS list format with emoji markers should be recommended as a standard pattern for constraint communication.

### Chapter: Custom Commands
- **Recommendation**: The `/bugmagnet` command should be highlighted as an exemplar of a portable, language-agnostic custom command. The phased approach with explicit user pause points is a pattern worth recommending.
- **Recommendation**: The Common Edge Case Checklist from bugmagnet is valuable enough to excerpt as a standalone reference appendix.

### Chapter: Pre-Commit Quality Gates
- **Recommendation**: The "Before Committing" checklist that references specific files (README.md for --help output, USER_GUIDE.md for option references) is a pattern for connecting commit quality to documentation freshness.

### Chapter: Architecture Documentation in AI Config
- **Recommendation**: The separation of general coding standards from "When Working with Claude Code" instructions is a good structural pattern. It keeps the config useful as human documentation while adding AI-specific guardrails.

### Chapter: Anti-Patterns
- **Recommendation**: Warn against putting investigation results back into plan templates (contaminates reusability).
- **Recommendation**: Warn against using JavaScript examples in non-JavaScript projects (bugmagnet).
- **Recommendation**: Recommend using `.claude/settings.json` and `.claude/rules/` for enforcement that goes beyond prompt-based constraints.

## Extraction Notes

- **Branch analyzed**: `main` (default branch)
- **No `.claude/settings.json`** found -- enforcement is entirely through CLAUDE.md prompt instructions
- **No `.claude/rules/`** directory -- no file-pattern-matched rules
- **No `AGENTS.md`** -- single-agent workflow (footer notes "Simplified - removed custom agents" as of Dec 2025, suggesting there were previously multiple agent definitions)
- **No `.cursorrules`** or Cursor config -- Claude Code appears to be the only AI tool configured
- **The bugmagnet command appears to be a general-purpose tool** potentially used across multiple projects (language-agnostic design, generic examples)
- **The plan files contain a mix of template and filled-in results** -- the AOT investigation plan appears to have been used as a living document during an actual investigation, with results filled in alongside the original template structure
- **The IoT MVP plan is extremely detailed** (~700 lines) suggesting it was collaboratively authored with Claude Code as a planning partner, not just as an execution guide
- **CLAUDE.md footer states "Last Updated: December 2025 (Simplified - removed custom agents)"** -- indicating the config has been actively maintained and simplified over time, suggesting maturity
