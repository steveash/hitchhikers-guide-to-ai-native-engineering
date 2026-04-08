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
| [Inside Shopify's AI-first engineering playbook](https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook) | Taj Shorter (Bessemer), interviewing Farhan Thawar (Shopify VP Eng) | Multi-tool by policy (Cursor + Claude Code + Copilot + Codex + Gemini); LLM proxy as central control; no autonomous merges; "humble" 20% productivity estimate; comprehension-debt warning ("brain is a muscle"); AI-reflexivity in performance reviews | [blog-bvp-shopify-ai-playbook.md](../source-notes/blog-bvp-shopify-ai-playbook.md) |
| [How to measure Claude Code ROI](https://www.faros.ai/blog/how-to-measure-claude-code-roi-developer-productivity-insights-with-faros-ai) | Thierry Donneau-Golencer (Faros AI) | Cohort design (≥20 devs/group, ≥1 quarter, matched on stack and seniority); three-layer measurement framework (adoption, trust, team performance); vanity metric list; "Team A 5% vs Team B 60%: 47% more PRs daily but 35% longer review times" | [blog-faros-claude-code-roi.md](../source-notes/blog-faros-claude-code-roi.md) |

## Research Papers & Surveys

| Title | Authors | Key Claims | Source Note |
|-------|---------|-----------|-------------|
| [Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?](https://arxiv.org/abs/2602.11988) | Gloaguen, Mündler, Müller, Raychev, Vechev (ETH Zurich SRI Lab) | LLM-generated context files reduce success rates and increase cost; developer-written files give only marginal improvement; introduces AGENTbench (138 tasks, 12 repos) | [paper-gloaguen-agentsmd-effectiveness.md](../source-notes/paper-gloaguen-agentsmd-effectiveness.md) |
| [Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects](https://arxiv.org/abs/2511.04427) | He, Miller, Agarwal, Kästner, Vasilescu (CMU; MSR '26 peer-reviewed) | Difference-in-differences study, n=806 Cursor adopters + 1,380 matched controls. 281%/48%/0% velocity decay across months 1–3; persistent +41.6% cognitive complexity, +30.3% static analysis warnings. "Quality assurance is the major bottleneck for early Cursor adopters." | [paper-miller-speed-cost-quality.md](../source-notes/paper-miller-speed-cost-quality.md) |
| [How AI Is Transforming Work at Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic) | Huang, Seethor, Durmus, Handa, McCain, Stern, Ganguli (Anthropic Societal Impacts; Dec 2025) | Mixed-methods study: 132 surveys + 53 interviews + 200k Clio-analyzed transcripts. 60% of work uses Claude (up from 28% YoY); >50% of engineers can only fully delegate 0–20% of work; autonomous tool calls doubled (Feb→Aug 2025); engineer-voiced skill-atrophy and supervision-paradox concerns | [research-anthropic-ai-transforming-work.md](../source-notes/research-anthropic-ai-transforming-work.md) |
| [The Pragmatic Engineer 2026 AI Tooling Survey](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) | Gergely Orosz | n=906 (Jan–Feb 2026); Claude Code rose to #1 in 8 months tied with Copilot at 46%; 70% use 2–4 AI tools simultaneously; staff+ engineers are heaviest agent users (63.5% vs 49.7% for regular engineers); 95% use AI weekly | [survey-pragmaticengineer-ai-tooling-2026.md](../source-notes/survey-pragmaticengineer-ai-tooling-2026.md) |

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
