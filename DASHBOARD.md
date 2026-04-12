# Guide Dashboard

_Generated 2026-04-12 (UTC) by `scripts/generate_dashboard.py`._

Content-derived metrics for the living guide. Refreshed daily by
`.github/workflows/daily-scan.yml`. For workflow status (PRs, issues,
scanner queues) see the GitHub Project linked from README.md.

| Chapter | Sources | Oldest source | Stale % | Lines (Δ7d) |
|---|---|---|---|---|
| `guide/00-principles.md` | 7/30 | 2026-02-12 (`paper-gloaguen-agentsmd-effectiveness`) | 0% | 288 (n/a) |
| `guide/01-daily-workflows.md` | 5/30 | 2026-03-26 (`blog-addyosmani-code-agent-orchestra`) | 0% | 510 (n/a) |
| `guide/02-harness-engineering.md` | 10/30 | 2025-09-17 (`failure-claudemd-ignored-compaction`) | 0% | 1016 (n/a) |
| `guide/03-safety-and-verification.md` | 10/30 | 2025-09-17 (`failure-claudemd-ignored-compaction`) | 0% | 660 (n/a) |
| `guide/04-context-engineering.md` | 6/30 | 2025-12-27 (`blog-sankalp-claude-code-20`) | 0% | 861 (n/a) |
| `guide/05-team-adoption.md` | 6/30 | 2025-11-06 (`paper-miller-speed-cost-quality`) | 0% | 975 (n/a) |

**Source cap**: 30 per chapter (see `hitchhiker.config.json`). 
Chapters at the cap are marked ⚠ and block new Smith additions until 
the Gardener prunes.

**Staleness**: percentage of cited source notes whose `last_checked` 
frontmatter field is more than 90 days old. Matches the 
`[stale]` confidence tag defined in README.md.

**Δ7d**: line-count delta vs. the most recent commit from at least 7 
days ago. `n/a` means the repo (or this chapter) is younger than a week.
