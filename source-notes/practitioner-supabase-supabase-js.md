# Practitioner Profile: supabase/supabase-js

**Repository**: https://github.com/supabase/supabase-js
**Language**: TypeScript
**Stars**: ~4,400
**Type**: Nx monorepo consolidating 6 published npm packages (@supabase/supabase-js, auth-js, postgrest-js, realtime-js, storage-js, functions-js)
**Default Branch**: `master`
**Date Analyzed**: 2026-03-30

---

## Config Surface Area

| File | Lines | Role |
|------|-------|------|
| `CLAUDE.md` | 931 | Primary AI instructions (Claude) |
| `.cursorrules` | 183 | Cursor IDE instructions |
| `WARP.md` | 660 | Warp terminal AI instructions |
| `CONTRIBUTING.md` | 367 | Human + AI contribution guide |
| `docs/TESTING.md` | 128 | Testing reference (linked from CLAUDE.md) |
| `docs/RELEASE.md` | 219 | Release workflows (linked from CLAUDE.md) |
| `.cursor/mcp.json` | 3 | Empty MCP server config (`{}`) |
| **Total** | **~2,491** | **7 files** |

**Sophistication Tier**: HIGH -- Triple-tool coverage (Claude, Cursor, Warp) with a documentation constellation pattern where the main CLAUDE.md links to 5 supporting docs. No per-package CLAUDE.md files; no .claude/ directory; no AGENTS.md; no agents.toml.

---

## Pattern Catalog

### Pattern 1: Triple-Tool AI Config Parity

The repository maintains three parallel AI configuration files -- CLAUDE.md (931 lines), .cursorrules (183 lines), and WARP.md (660 lines) -- covering Claude, Cursor, and Warp respectively. All three convey the same core knowledge (monorepo structure, Nx commands, Docker requirements, testing per-package) but at different verbosity levels.

**CLAUDE.md opening:**
```
# Claude AI Instructions for Supabase JS Libraries Monorepo

You are assisting with development in a unified Nx monorepo that consolidates all Supabase JavaScript SDKs, built with Nx for optimal developer experience and maintainability.
```

**WARP.md opening:**
```
# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.
```

**.cursorrules opening:**
```
# Cursor Rules for Supabase JS Libraries Monorepo

You are working in a unified Nx monorepo that consolidates all Supabase JavaScript SDKs.
```

**Cross-reference**: This is **novel** vs all three existing profiles. No other profiled repo maintains parallel configs for 3 different AI tools. postgres_dba has dual Claude/Cursor config but with intentionally different verbosity (30 lines vs ~100 lines). Supabase's approach is closer to "same content, different depth" -- CLAUDE.md is 5x longer than .cursorrules because it includes release process detail, TypeScript project references, and a pitfalls section.

### Pattern 2: Documentation Constellation (Hub-and-Spoke)

CLAUDE.md acts as a hub that explicitly links to 5 satellite documents:

```
> **📚 Essential Documentation**: Always refer to these guides for detailed information:
>
> - **[CONTRIBUTING.md](CONTRIBUTING.md)** - Development guidelines, commit format, PR process
> - **[TESTING.md](docs/TESTING.md)** - Complete testing guide with Docker requirements
> - **[RELEASE.md](docs/RELEASE.md)** - Release workflows and versioning strategy
> - **[MIGRATION.md](docs/MIGRATION.md)** - Migration context from old repositories
> - **[SECURITY.md](docs/SECURITY.md)** - Security policies and responsible disclosure
```

This is a structured approach where AI-facing documentation leverages pre-existing human documentation rather than duplicating it. The CLAUDE.md still contains extensive inline content (931 lines), so this is "link AND repeat" rather than "link instead of."

**Cross-reference**: **Contradicts** Sentry's thin-redirect pattern (11-byte CLAUDE.md that redirects to AGENTS.md). Supabase's CLAUDE.md is self-contained AND cross-references. **Extends** the general pattern of documentation layering seen in all profiles.

### Pattern 3: Pitfall-Driven Teaching (7 Explicit Anti-Patterns)

CLAUDE.md dedicates ~120 lines to 7 numbered "Common Pitfalls & Solutions" with explicit wrong/right comparisons using visual markers:

```
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

The 7 pitfalls are:
1. Hardcoding internal versions (use `*` protocol)
2. Running npm directly in library directories (use Nx from root)
3. Testing everything at once (use per-package complete test suites)
4. Breaking changes without process (add new, deprecate old)
5. Running commands incorrectly (Nx from root, not npm in subdirs)
6. Not using the commit tool (use `npm run commit`)
7. Not checking documentation before testing

**Cross-reference**: **Corroborates** NetPace's "MUST NEVER/MUST ALWAYS" dual-list pattern, but uses a more pedagogical wrong/right format with code examples rather than terse rules. The visual ❌/✅ markers echo NetPace's emoji usage. **Extends** the concept by providing 7 worked examples rather than categorical lists.

### Pattern 4: Per-Package Test Command Matrix

A recurring pattern across all three AI config files is a detailed table mapping packages to their Docker requirements and exact test commands:

```
| Package      | Docker Required | Complete Test Command               |
| ------------ | --------------- | ----------------------------------- |
| auth-js      | ✅ Yes          | `nx test:auth auth-js`              |
| storage-js   | ✅ Yes          | `nx test:storage storage-js`        |
| postgrest-js | ✅ Yes          | `nx test:ci:postgrest postgrest-js` |
| functions-js | ✅ Yes          | `nx test functions-js`              |
| realtime-js  | ❌ No           | `nx test realtime-js`               |
| supabase-js  | ❌ No           | `nx test supabase-js`               |
```

This table appears in CLAUDE.md, .cursorrules, WARP.md, and docs/TESTING.md -- repeated 4 times. The critical insight is that each package has a DIFFERENT test command (not a uniform `nx test <pkg>`), and the AI must know which variant to use.

**Cross-reference**: **Novel** -- no other profile has per-subproject command variation at this level. Sentry has frontend/backend split but uniform test commands within each. This is a monorepo-specific pattern where test infrastructure heterogeneity (Docker vs testcontainers vs mock) forces per-package command awareness.

### Pattern 5: Nx-First Command Discipline

All three AI config files enforce using Nx as the command interface rather than npm:

```
> **⚠️ Important**: Always use Nx commands from the repository root rather than running npm scripts directly in library directories.

```bash
# ✅ Correct: Use Nx from root
nx test:auth auth-js
nx build postgrest-js --watch

# ❌ Avoid: Don't run npm directly in library directories
# cd packages/core/auth-js && npm test
```
```

CLAUDE.md also includes Nx-specific meta-instructions appended by Nx tooling:

```
<!-- nx configuration start-->
- For navigating/exploring the workspace, invoke the `nx-workspace` skill first
- When running tasks, always prefer running the task through `nx`
- Prefix nx commands with the workspace's package manager
- NEVER guess CLI flags - always check nx_docs or `--help` first when unsure
<!-- nx configuration end-->
```

**Cross-reference**: **Novel** -- this is the first profile with build-tool-injected AI instructions. The `<!-- nx configuration start-->` block is auto-maintained by Nx tooling, creating a hybrid human-authored + tool-authored CLAUDE.md.

### Pattern 6: Zero Breaking Changes as Cardinal Rule

The principle "zero breaking changes" appears as the #1 core development principle and is reinforced throughout:

```
### 1. Zero Breaking Changes

Every change must maintain full backward compatibility. The migration itself introduces no breaking changes - all packages maintain their original npm names and APIs.
```

And in the pitfalls section with a concrete code example showing the deprecation pattern:

```typescript
// Add new method
signIn(credentials: Credentials): Promise<void>

// Deprecate old method with backward compatibility
/** @deprecated Use signIn(credentials) instead */
signInWithEmail(email: string): Promise<void> {
  return this.signIn({ email })
}
```

**Cross-reference**: **Extends** NetPace's prohibition-centric approach. Both repos place cardinal rules prominently, but Supabase provides concrete code examples of how to maintain compatibility rather than just stating the prohibition.

### Pattern 7: Interactive Commit Tool Enforcement

Multiple files enforce using `npm run commit` instead of `git commit`:

```
### Pitfall 6: Not Using the Commit Tool

❌ Wrong: Using git commit directly

```bash
git commit -m "fix auth bug"  # Missing scope, will fail validation
```

✅ Correct: Use the interactive commit tool

```bash
npm run commit  # Guides you through proper format
```
```

CONTRIBUTING.md reinforces with a full conventional commit type/scope table. The commit scope is REQUIRED with library-specific scopes (auth, functions, postgrest, realtime, storage, supabase) and workspace scopes (repo, deps, ci, release, docs, scripts, misc).

**Cross-reference**: **Novel** in specificity. No other profile enforces an interactive commit tool. Sentry and NetPace have commit conventions but don't mandate a specific tool.

### Pattern 8: Quick Decision Tree

CLAUDE.md ends with a decision tree for common questions:

```
**Q: Where does this code belong?**

- Authentication logic → auth-js
- Database queries → postgrest-js
- Real-time subscriptions → realtime-js
- File operations → storage-js
- Edge function calls → functions-js
- Integration of above → supabase-js
- Shared utilities → packages/shared/ (create if needed)

**Q: How to test this change?**
...

**Q: How will this release?**
...
```

**Cross-reference**: **Novel** -- no other profile uses an explicit Q&A decision tree format. This is a monorepo navigation aid that helps the AI route changes to the correct package.

### Pattern 9: Redundancy-as-Reliability

The Docker requirements table appears 4 times across files. The test commands are repeated in CLAUDE.md (twice -- in the commands section and the decision tree), .cursorrules, WARP.md, TESTING.md, and CONTRIBUTING.md. The conventional commit format is specified in CLAUDE.md, .cursorrules, WARP.md, and CONTRIBUTING.md.

This is deliberate -- each file must be self-sufficient since different AI tools only read their respective config file. But even within CLAUDE.md, critical information like test commands appears in multiple sections.

**Cross-reference**: **Corroborates** NetPace's "say it three times" philosophy, though Supabase achieves repetition through structural parallelism (multiple files covering same content) rather than literal in-file repetition.

### Pattern 10: Hybrid Release Model Documentation

CLAUDE.md devotes ~150 lines to the canary/stable/preview release model with exact command sequences:

```bash
# Canary releases (automated in CI)
nx release --tag=canary --yes

# Stable releases (manual promotion)
nx release --tag=latest --yes

# Preview and debugging
nx release --dry-run
```

This is unusual -- most AI config files don't document release processes in detail. The assumption is that AI agents will help with releases, not just code changes.

**Cross-reference**: **Novel** -- no other profiled repo includes release workflow documentation in AI config. This reflects a broader scope of AI-assisted development beyond just coding.

---

## Prohibitions Extracted

The files use instructional rather than prohibitive language. Explicit prohibitions are framed as pitfalls:

1. **Do not hardcode internal dependency versions** -- use `*` protocol
2. **Do not run npm directly in library directories** -- use Nx from root
3. **Do not run all tests together** -- use per-package complete test suites
4. **Do not make breaking changes without proper process** -- add new, deprecate old
5. **Do not skip commit message validation** -- use `npm run commit`
6. **Do not bypass the Nx build system** by running npm scripts directly
7. **Do not mix unrelated changes** in a single commit
8. **Do not assume all packages use standard test commands** -- check for special targets
9. **NEVER guess CLI flags** -- always check nx_docs or `--help` first (from Nx-injected block)

From WARP.md Do's/Don'ts section:
```
### Don'ts ❌

- **Don't run npm commands** directly in library directories
- **Don't skip commit message validation** (use `npm run commit`)
- **Don't hardcode internal versions** (use `*` protocol)
- **Don't try to run all tests together** - use complete test suites for packages individually
- **Don't make breaking changes** without discussion and proper commit format
- **Don't assume all packages use standard test commands** (check for special targets)
```

---

## Anti-Patterns Observed

1. **Content duplication across tool configs**: The same information exists in CLAUDE.md (931 lines), .cursorrules (183 lines), and WARP.md (660 lines). When a test command changes, 3+ files need updating. This creates drift risk. A shared source of truth with tool-specific thin wrappers would be more maintainable.

2. **No per-package CLAUDE.md**: Despite being a monorepo with 6 packages, there are no subdirectory-level AI config files. Claude's subdirectory CLAUDE.md loading would allow package-specific instructions to be co-located. Currently the root file must enumerate all per-package nuances.

3. **No permission allowlists**: Unlike Sentry's granular 60+ bash command prefixes, there are no tool permission configurations. The .cursor/mcp.json is empty (`{}`). No .claude/settings.json exists.

4. **Verbose but instruction-light**: CLAUDE.md is 931 lines but much of it is command reference and architecture documentation that could live in separate docs (and does -- TESTING.md, RELEASE.md). The actual behavioral instructions for the AI ("when you do X, do Y") are relatively sparse compared to the reference material.

5. **No anti-sycophancy or review behavior rules**: Unlike Sentry's explicit anti-sycophancy instruction for PR reviews, there are no instructions shaping how the AI should review code, handle disagreements, or calibrate confidence.

---

## Cross-Reference Summary

| Pattern | vs Sentry | vs NetPace | vs postgres_dba |
|---------|-----------|------------|-----------------|
| Triple-tool parity | Novel (Sentry: single tool) | Novel | Extends (dual tool) |
| Hub-and-spoke docs | Contradicts (thin redirect) | Novel | Novel |
| Pitfall-driven teaching | Novel | Corroborates (MUST NEVER lists) | Novel |
| Per-package command matrix | Extends (frontend/backend split) | Novel | Novel |
| Nx-first discipline | Novel | Novel | Novel |
| Zero-breaking-changes rule | Novel | Corroborates (cardinal rules) | Novel |
| Interactive commit tool | Novel | Novel | Novel |
| Decision tree | Novel | Novel | Novel |
| Redundancy-as-reliability | Novel | Corroborates ("say it 3 times") | Novel |
| Tool-injected config block | Novel | Novel | Novel |

---

## Guide Chapter Impact

1. **Chapter: Multi-Tool Configuration** -- This is the strongest example of maintaining parallel AI configs for 3 tools. Should drive a section on trade-offs: parity vs drift risk, and strategies like shared source docs with tool-specific adapters.

2. **Chapter: Monorepo Patterns** -- The per-package test command matrix, Nx-first discipline, and decision tree routing are monorepo-specific patterns that deserve dedicated coverage. The absence of per-package CLAUDE.md is notable and worth discussing as a design choice (centralized vs distributed config).

3. **Chapter: Pitfall Documentation** -- The 7-pitfall format with ❌/✅ code examples is a highly effective teaching pattern. Could be recommended as a template for any repo where common mistakes are well-known.

4. **Chapter: Tool-Injected Configuration** -- The Nx-appended `<!-- nx configuration start-->` block in CLAUDE.md is a new category: build tools that contribute to AI config. This has implications for config ownership and maintenance.

5. **Chapter: Documentation as AI Context** -- The hub-and-spoke pattern (CLAUDE.md links to CONTRIBUTING.md, TESTING.md, RELEASE.md) raises the question of whether AI tools actually follow these links. If not, the redundancy in CLAUDE.md is necessary; if so, the file could be much shorter.

6. **Chapter: Prohibitions and Guardrails** -- Supabase's prohibitions are instructional ("don't do X, do Y instead with this exact command") rather than bare ("NEVER do X"). This is a third style alongside Sentry's permission allowlists and NetPace's emphatic repetition.

7. **Chapter: Scope of AI Assistance** -- Including release process documentation in AI config suggests Supabase expects AI to assist beyond code changes (release management, version bumping, changelog generation). This broadens the expected AI task surface.
