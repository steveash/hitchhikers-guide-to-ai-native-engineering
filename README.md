# The Hitchhiker's Guide to AI-Native Engineering

A living, opinionated, citation-backed handbook for practitioners building software
with AI coding agents. Updated weekly as new patterns emerge and old ones decay.

**This guide is unapologetically point-in-time.** What works today may not work
next month. Every recommendation cites its source. Every claim states its confidence
level. When the landscape shifts, the guide shifts with it.

---

## Read the Guide

The guide lives in [`guide/`](guide/). Read in order, or jump to what you need:

- [Principles](guide/00-principles.md) — The mental models that hold up
- [Daily Workflows](guide/01-daily-workflows.md) — What a good session looks like
- [Harness Engineering](guide/02-harness-engineering.md) — CLAUDE.md, rules, commands, hooks
- [Safety and Verification](guide/03-safety-and-verification.md) — Layered verification, kill criteria, comprehension debt
- [Context Engineering](guide/04-context-engineering.md) — Context as budget, compaction, plan files, MCP cost
- [Team Adoption](guide/05-team-adoption.md) — Scaling from one engineer to a team, measurement, rollout
- [Sources](guide/SOURCES.md) — Master index of every source the guide cites

### Trust Model

Every claim in the guide has a confidence tag:

| Tag | Meaning |
|-----|---------|
| `[settled]` | Multiple independent sources confirm. Safe to rely on. |
| `[emerging]` | 2-3 sources, consistent but limited evidence. Promising. |
| `[anecdotal]` | Single practitioner report. Interesting but unverified. |
| `[editorial]` | Our synthesis — not directly from a source. Flagged as opinion. |
| `[stale]` | Source is >90 days old and hasn't been re-verified. May have drifted. |

---

## Improve the Guide

Anyone can help improve the guide by submitting feedback. Two ways to contribute:

### Submit a Source

Found a practitioner repo, blog post, failure report, or community discussion that
should inform the guide? File an issue:

- [**Source submission**](.github/ISSUE_TEMPLATE/source-submission.yml) — article URL, blog feed, practitioner repo
- [**Practitioner repo**](.github/ISSUE_TEMPLATE/practitioner-repo.yml) — real CLAUDE.md, .claude/ configs, AGENTS.md from active repos
- [**Failure report**](.github/ISSUE_TEMPLATE/failure-report.yml) — "I tried X and it broke" reports

See [SUBMISSION.md](SUBMISSION.md) for full instructions. The agent pipeline processes
community submissions with the same rigor as automated discoveries.

### Submit Editorial Feedback

Have opinions on layout, omissions, emphasis, or framing? File a sticky note:

- [**Sticky notes**](.github/ISSUE_TEMPLATE/sticky-notes.yml) — editorial guidance for synthesis agents

Sticky notes are prescriptive or conditional rules that agents must respect when
updating guide content. They live in [`sticky-notes/`](sticky-notes/) and are
consulted during every synthesis pass.

---

### Review Guide Updates

When the Smith agent opens a `guide-update` PR, you can review and request changes
directly:

1. Read the PR diff
2. Leave as many comments as you want — what to change, tone down, add, remove
3. When you're done, post a comment containing `/rework`

The Smith reads **all** your comments holistically in one pass, pushes fixes, and
the Assayer re-reviews automatically. You can `/rework` as many times as needed.
Only repo collaborators can trigger rework.

---

## How the Automation Works

The guide is maintained by a pipeline of AI agents that discover, extract, review,
synthesize, and patrol for staleness — so the guide stays current without manual
curation. For the full pipeline design, see [`agents/README.md`](agents/README.md).

Additional references:

- [**DASHBOARD.md**](DASHBOARD.md) — Content health metrics: per-chapter source counts, oldest cited source, staleness percentage, weekly delta
- [**CONTRADICTIONS.md**](CONTRADICTIONS.md) — Where sources disagree and how the guide resolves it
- [**docs/PROJECT-SETUP.md**](docs/PROJECT-SETUP.md) — Development environment and project setup
- **GitHub Project** [https://github.com/users/steveash/projects/1] — Workflow status across PRs, issues, and scanner queues
