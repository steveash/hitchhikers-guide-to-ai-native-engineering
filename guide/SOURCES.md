# Source Index

Master index of all approved sources. Each entry links to its source note.

## Practitioner Repos

| Repo | Language | Key Patterns | Source Note |
|------|----------|-------------|-------------|
| [dadlerj/tin](https://github.com/dadlerj/tin) | Go | Self-referential dogfooding; lifecycle hooks auto-track conversations as versioned threads; programmatic slash command generation from Go source | [practitioner-dadlerj-tin.md](../source-notes/practitioner-dadlerj-tin.md) |
| [FrankRay78/NetPace](https://github.com/FrankRay78/NetPace) | C# | "TDD is non-negotiable" enforcement; ASCII RED-GREEN-REFACTOR diagram; ~767-line custom `/bugmagnet` command for systematic test coverage | [practitioner-frankray78-netpace.md](../source-notes/practitioner-frankray78-netpace.md) |
| [getsentry/sentry](https://github.com/getsentry/sentry) | Python, TypeScript | Thin `CLAUDE.md` → `AGENTS.md` redirect; context-aware subdirectory guides (src/, tests/, static/); 16 domain skills under `.agents/skills/`; `agents.toml` cross-tool sharing | [practitioner-getsentry-sentry.md](../source-notes/practitioner-getsentry-sentry.md) |
| [mikelane/pytest-test-categories](https://github.com/mikelane/pytest-test-categories) | Python | Single 298-line `CLAUDE.md`; heavy reliance on process infrastructure (CONTRIBUTING.md, issue templates, workflows) over `.claude/` tooling | [practitioner-mikelane-pytest-test-categories.md](../source-notes/practitioner-mikelane-pytest-test-categories.md) |
| [NikolayS/postgres_dba](https://github.com/NikolayS/postgres_dba) | PLpgSQL | Concise `CLAUDE.md` governs a pure-SQL repo; cross-version CI matrix (PG 13–18); mandatory review tooling for non-application code | [practitioner-nikolays-postgres-dba.md](../source-notes/practitioner-nikolays-postgres-dba.md) |
| [supabase/supabase-js](https://github.com/supabase/supabase-js) | TypeScript | 931-line `CLAUDE.md` as primary; triple-tool coverage (Claude, Cursor, Warp); documentation constellation pattern linking 5 supporting docs | [practitioner-supabase-supabase-js.md](../source-notes/practitioner-supabase-supabase-js.md) |

## Blog Posts & Articles

| Title | Author | Key Claims | Source Note |
|-------|--------|-----------|-------------|
| [The Code Agent Orchestra](https://addyosmani.com/blog/code-agent-orchestra/) | Addy Osmani | Shift from single-agent "conductor" to multi-agent "orchestrator" requires new skills; subagents / agent teams / Ralph loop patterns; verification has replaced code generation as the bottleneck | [blog-addyosmani-code-agent-orchestra.md](../source-notes/blog-addyosmani-code-agent-orchestra.md) |
| [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988) (paper) | Gloaguen, Mündler, Müller, Raychev, Vechev (ETH Zurich SRI Lab) | LLM-generated context files reduce success rates and increase cost; developer-written files give only marginal improvement; introduces AGENTbench (138 tasks, 12 repos) | [paper-gloaguen-agentsmd-effectiveness.md](../source-notes/paper-gloaguen-agentsmd-effectiveness.md) |

## Failure Reports

| Description | Platform | Key Lessons | Source Note |
|-------------|----------|-------------|-------------|
| CLAUDE.md instructions systematically ignored after context compaction | dev.to, GitHub Issues (#19635, #7777, #28158), HumanLayer blog | Harness framing ("this context may or may not be relevant") gives the model permission to deprioritize rules; compaction then summarizes weakened instructions away; prose rules are ~70–80% advisory at best, degrading with session length | [failure-claudemd-ignored-compaction.md](../source-notes/failure-claudemd-ignored-compaction.md) |
| $2K practitioner builds 14-hook enforcement system after compaction failures | Hacker News (item 45871445) + GitHub (meloncafe/claude-code-hooks) | Markdown-based guidelines are unenforceable without hooks; hooks are the real enforcement mechanism; working around prose-rule failure requires sustained engineering effort, not config tweaks | [failure-hooks-enforcement-2k.md](../source-notes/failure-hooks-enforcement-2k.md) |

## Documentation

<!-- No vendor documentation sources in the current set. Populate as docs are analyzed. -->

| Title | Vendor | Key Guidance | Source Note |
|-------|--------|-------------|-------------|

## Discussions

<!-- No discussion-type sources in the current set. Populate as discussions are analyzed. -->

| Title | Platform | Key Points | Source Note |
|-------|----------|-----------|-------------|
