# The Hitchhiker's Guide to AI-Native Engineering

A living, opinionated, citation-backed handbook for practitioners building software
with AI coding agents. Updated weekly as new patterns emerge and old ones decay.

**This guide is unapologetically point-in-time.** What works today may not work
next month. Every recommendation cites its source. Every claim states its confidence
level. When the landscape shifts, the guide shifts with it.

## What This Is

A practitioner's field guide. Concrete advice: do this, don't do that, here's why,
here's the evidence. Not a survey of the space. Not a tutorial. Not marketing copy.

The guide is maintained by a pipeline of AI agents that:
1. **Discover** practitioner repos and community discussions weekly
2. **Extract** concrete patterns, anti-patterns, and configuration examples
3. **Analyze** with cross-referencing, contradiction tracking, and evidence grading
4. **Synthesize** findings into actionable guide chapters with full citations
5. **Review** every change through structured editorial gates

## Reading the Guide

The guide lives in [`guide/`](guide/). Read in order, or jump to what you need:
- [Principles](guide/00-principles.md) — The mental models that hold up
- [Daily Workflows](guide/01-daily-workflows.md) — What a good session looks like
- [Harness Engineering](guide/02-harness-engineering.md) — CLAUDE.md, rules, commands, hooks
- [Safety and Verification](guide/03-safety-and-verification.md) — Layered verification, kill criteria, comprehension debt
- [Context Engineering](guide/04-context-engineering.md) — Context as budget, compaction, plan files, MCP cost
- [Team Adoption](guide/05-team-adoption.md) — Scaling from one engineer to a team, measurement, rollout
- [Sources](guide/SOURCES.md) — Master index of every source the guide cites

## How Sources Work

Every claim in the guide traces back to a source note in [`source-notes/`](source-notes/).
Source notes come from three pipelines:

| Pipeline | What it finds | Frequency |
|----------|--------------|-----------|
| **Repo Scout** | Real CLAUDE.md files, .claude/ configs, and AGENTS.md from active GitHub repos | Weekly |
| **Failure Scanner** | "I tried X and it broke" reports from HN, Reddit, GitHub Discussions | Weekly |
| **Community Submissions** | Sources filed by humans via GitHub Issues | Continuous |

## Contributing

**Anyone can submit a source.** See [SUBMISSION.md](SUBMISSION.md) for instructions.

File an issue using the [source submission template](.github/ISSUE_TEMPLATE/source-submission.yml)
with the URL, what you found interesting, and where you think it's relevant. The agent
pipeline will process it with the same rigor as any automated discovery.

## Trust Model

Every claim in the guide has a confidence tag:

| Tag | Meaning |
|-----|---------|
| `[settled]` | Multiple independent sources confirm. Safe to rely on. |
| `[emerging]` | 2-3 sources, consistent but limited evidence. Promising. |
| `[anecdotal]` | Single practitioner report. Interesting but unverified. |
| `[editorial]` | Our synthesis — not directly from a source. Flagged as opinion. |
| `[stale]` | Source is >90 days old and hasn't been re-verified. May have drifted. |

## Pipeline Status

Two complementary views into the guide's health:

- [**DASHBOARD.md**](DASHBOARD.md) — content-derived metrics regenerated
  daily by `scripts/generate_dashboard.py`: per-chapter source counts vs
  cap, oldest cited source, staleness percentage, weekly line-count delta.
  These are things GitHub Projects can't show natively.
- **GitHub Project (v2)** — workflow status across PRs, issues, and the
  scanner queues. Three views: *Source intake* (new sources flagged for
  triage), *PR review queue* (open PRs grouped by Assayer check), and
  *Chapter health* (open work tagged per guide chapter). Setup runbook:
  [`docs/PROJECT-SETUP.md`](docs/PROJECT-SETUP.md). Once the project is
  created the URL will be linked here.

## Architecture

See [`agents/`](agents/) for the full agent pipeline design.
See [`.github/workflows/`](.github/workflows/) for automation.
See [`registry/`](registry/) for tracked repos and sources.
