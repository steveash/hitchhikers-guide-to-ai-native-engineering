# Agent Pipeline

Seven agents form the source-to-guide pipeline. Each has a defined role,
clear ownership boundaries, and explicit triggers.

## Pipeline Flow

```
Discovery                    Extraction              Review           Synthesis
─────────                    ──────────              ──────           ─────────
                             ┌─────────┐
REPO SCOUT ──[new-repo]────→│         │
                             │  MINER  │──[PR]──→ ASSAYER ──[merge]─→ SMITH
FAILURE SCANNER ──[new]────→│  or     │              ▲                 │
                             │  REPO   │              │                 ▼
COMMUNITY ──[submission]──→ PROSPECTOR │  SCOUT  │              │              Guide
                      │      └─────────┘              │            chapters
                      │                               │                │
                      ├──[reject]                     │         GARDENER
                      │                               │    (staleness patrol)
                      └──[feed-candidate]──[PR]───────┘

Editorial                                                      ┌─────────────┐
─────────                                                      │    SMITH    │
COMMUNITY ──[sticky-notes issue]──→ SCRIBE ──→ sticky-notes/ ─→│  (consults  │
                                                               │   during    │
                                                               │  synthesis) │
                                                               └─────────────┘
```

## Agents

| Agent | Role | Trigger | Owns | Cannot |
|-------|------|---------|------|--------|
| [Prospector](PROSPECTOR.md) | Source triage | New issues | Issue labels | Edit notes or guide |
| [Miner](MINER.md) | Deep extraction (text sources) | Triaged text issues | Source note PRs | Edit guide, merge |
| [Repo Scout](REPO-SCOUT.md) | Discovery + extraction (repos) | Weekly scan / triaged repo issues | Practitioner profiles, registry | Edit guide, merge |
| [Assayer](ASSAYER.md) | Quality gate | PRs with source-note/guide-update/feed-candidate labels | PR approval | Create notes, edit guide |
| [Smith](SMITH.md) | Report synthesis | source-notes merge (diff-aware) / weekly batch | Guide chapter PRs | Create notes, approve, merge |
| [Gardener](GARDENER.md) | Staleness patrol | Weekly | Staleness tags, metadata | Write guide, create notes |
| [Scribe](../.github/workflows/scribe.yml) | Parse sticky-note issues into structured repo files | `issues.labeled` with `sticky-notes` | `sticky-notes/*.md` files, SN-ID assignment | Edit guide chapters, approve notes into the guide |

### Prospector Outcomes

The Prospector has four triage outcomes:

| Outcome | Label | Next step |
|---------|-------|-----------|
| Triaged (text) | `triaged:text` | Miner extracts a source note |
| Triaged (repo) | `triaged:repo` | Repo Scout profiles the repository |
| Rejected | `rejected` | Issue closed, no further action |
| Feed candidate | `feed-candidate` | Prospector opens a PR to add the feed to `registry/trusted-feeds.json`; Assayer reviews |

### Scribe Model

The Scribe runs as a GitHub Actions workflow using Haiku (cheap parsing task).
It has no agent definition file — the prompt is inline in
`.github/workflows/scribe.yml`.

## Key Principle: Separation of Concerns

No agent can both create content AND approve it. The Miner writes source
notes but the Assayer reviews them. The Smith writes guide chapters but
the Assayer reviews those too. This separation is what prevents the
"same LLM talking to itself" problem that plagued the original approach.

## How agents run (automation status)

All agents run as GitHub Actions workflows. There is no manual orchestration
in steady state — a human files an issue or comments `/rework` and the
pipeline does the rest.

### Trigger and model per workflow

| Workflow file | Agent | Trigger | Model | Notes |
|---------------|-------|---------|-------|-------|
| `daily-scan.yml` | Site/feed scanners | Daily cron 06:00 UTC + workflow_dispatch | Haiku (site crawl synthesis) | Uses `PROJECT_PAT` so the issues it files trigger downstream `source-pipeline.yml` |
| `source-pipeline.yml` (pre-screen job) | Pre-screen | `issues:[opened, labeled]` with `new-source` / `source-submission` / `new-repo` / `new-failure` | Haiku | ~$0.01/issue. Rejects obvious bad submissions (no URL, paywall, marketing, dupes) before the Prospector |
| `source-pipeline.yml` (prospector job) | Prospector | After pre-screen passes (job dependency) | Haiku | Triages into `triaged:text` / `triaged:repo` / `triaged:failure` / `feed-candidate` / `rejected`. Applies `mining-queued` for text and failure triages. Opens a feed-candidate PR if the source is a feed |
| `miner-batch.yml` | Miner | Hourly cron at `:17` + workflow_dispatch | Sonnet | Picks 2 oldest priority-sorted (high → medium → unset → low) `mining-queued` issues. Branch is `miner/issue-N-r<run_id>` (the `-rXXX` suffix avoids per-branch dispatch suppression on retries) |
| `assayer.yml` | Assayer review | `pull_request:[opened, synchronize, reopened, labeled]` with `source-note` / `guide-update` / `feed-candidate` | Sonnet | Auto-merges `source-note` PRs on APPROVE. On REQUEST CHANGES for `guide-update` PRs, runs the auto-rework Smith one time (gated by `rework-attempted` label) |
| `assayer.yml` (auto-rework Smith step) | Smith | Inside Assayer when guide-update PR fails review and `rework-attempted` is absent | Opus | Pushes a fix commit to the PR branch using `PROJECT_PAT` so the resulting `synchronize` event re-triggers Assayer |
| `smith-on-source-merge.yml` | Smith (batch synthesis) | Twice-weekly cron — Sat 15:17 UTC and Thu 00:00 UTC + workflow_dispatch | Opus | Reads ALL source-note changes since the last run (tracked via the `smith-last-run` git tag), runs diff-aware synthesis on the affected chapters, opens a fresh `smith/source-merge-<run_id>` branch + `guide-update` PR if any chapter material changes. The cadence lets Miner output accumulate between runs and gives review time on the resulting guide-update PRs |
| `smith-rework.yml` | Smith | `issue_comment` or `pull_request_review` containing `/rework` or `/rebase` on a `guide-update` PR (owner/collaborator/member only) | Opus | `/rework` = incremental fix on the existing branch. `/rebase` = reset branch to `main` and re-synthesize from scratch. Either resets the `rework-attempted` label so the auto-cycle can run one more time |
| `contradiction-resolver.yml` (assess job) | Assayer (contradiction mode) | `issues:[labeled]` with `contradiction` | Sonnet | Reads both source notes, weighs evidence, posts the proposed verdict comment with structured fields. Adds `assessment-complete` label |
| `contradiction-resolver.yml` (resolve job) | Assayer (commit phase) | `issues:[labeled]` with `resolution-approved` (added by a human after reviewing the assessment) | Haiku | Mechanical edit to `CONTRADICTIONS.md`. Opens a `guide-update` PR for the entry |
| `scribe.yml` | Scribe | `issues:[labeled]` with `sticky-notes` | Haiku | Parses the issue into structured `sticky-notes/chNN-*.md` entries. Inline prompt — no agent definition file |
| `gardener.yml` | Gardener | Weekly cron Sun 09:00 UTC + workflow_dispatch | Python (no LLM) | Tags source notes with `last_checked > 90 days` as stale; demotes confidence grades in chapters that cite them; opens a `guide-update` PR labeled `gardener` if anything changes |

## Failure modes and self-healing

The pipeline is designed to recover from transient failures without
human intervention. The recovery mechanism for each common failure:

| Failure | Agent | Human needed? | Recovery |
|---------|-------|---------------|----------|
| Run fails mid-extraction (Anthropic stream timeout, network blip) | Miner | No | Issue keeps `mining-queued`, doesn't get `mining-complete`. Next hourly cron picks it up automatically |
| Real source rejected by mistake | Pre-screen | Yes | Issue is closed with `rejected` label. A human can reopen and remove `rejected` to re-run, or file a fresh issue |
| Triages incorrectly (e.g. should be `triaged:text` not `triaged:repo`) | Prospector | Yes | Human swaps labels — the Miner picks up `triaged:text` + `mining-queued` automatically |
| Source-note PR fails Assayer review | Miner | Yes | No automated rework path for source-note PRs. Default action: close the PR, requeue the source issue (`mining-queued`, remove `mining-complete`); the next batch re-mines on a fresh `-r<run_id>` branch |
| Guide-update PR fails review (first time) | Smith | No | Auto-rework Smith fires inside the Assayer workflow once, addressing the feedback. Gated by the `rework-attempted` label so it can't loop |
| Guide-update PR fails again after auto-rework | Smith | Yes | Sits waiting for human to comment `/rework <specific guidance>` or `/rebase`. Either resets the `rework-attempted` label so the auto-cycle gets one more chance |
| `/rework` comment is the only human comment (feedback file would be empty) | Smith | No | smith-rework.yml falls back to using the trigger-comment body (with the slash-command line stripped) as guidance, so guidance the user wrote alongside `/rework` isn't lost |
| Hallucinated citations or fabricated quotes | Smith | Yes | Assayer rejects on Accuracy or Cross-references. `/rework` cycle can usually fix; `agents/SMITH.md` §3a forbids fabrication explicitly |
| Hallucinated cross-references | Miner | Yes | Same pattern — `agents/MINER.md` §4b/§2a require verbatim verification of every cited claim and quote. If a specific source keeps hallucinating, label its issue `miner-blocked` |
| Workflow YAML broken by an edit | | Yes | Workflow runs fail at startup. Other workflows continue normally. Diagnose with `gh run view --log-failed` and push a fix |
| Cron schedule miss after a `cron:` change | | No | First tick after the change can be skipped (GitHub propagation delay). Subsequent ticks fire normally. Manual `workflow_dispatch` covers the gap |
| `pull_request` workflow events silently dropped on a recreated branch | | No | Per-branch dispatch suppression. Mitigated: every Miner attempt uses a fresh `miner/issue-N-r<run_id>` branch so the suppression state can't carry over. If it still recurs, label the source issue `miner-blocked` |
| 3rd+ PR opened in tight succession from the same user — workflow doesn't dispatch | | No | `BATCH_SIZE=2` in `miner-batch.yml` keeps each batch under GitHub's abuse-detection threshold. If a manual workflow_dispatch produces a stuck PR, recycle via close + requeue |
| Source URL is unreachable, paywalled, or otherwise unreadable | Miner | No | Marks the issue `miner-blocked` and exits without opening a PR. The issue stays open with the block label so a human can investigate later if desired |

## When humans need to step in

Most of the pipeline is autonomous. Human action is required for:

| Phase | Human action |
|-------|--------------|
| **Source filing** | File `[source]` issues from blog posts / docs / discussions / failure reports. Or trust the daily scanner to discover them via feeds and site crawls |
| **Repo discovery** | Repo Scout is event-driven; human files `[source]` issues with the repo URL, Prospector triages them as `triaged:repo` |
| **Sticky-note authoring** | File a `sticky-notes` issue when an editorial directive should constrain Smith synthesis going forward (e.g., "always include a failure case in §tooling"). The Scribe parses it into `sticky-notes/chNN-*.md` |
| **Contradiction resolution** | When a `contradiction` issue gets `assessment-complete`, the Assayer's proposed verdict appears as a comment. A human reviews, optionally corrects with a comment, and adds `resolution-approved` to fire the resolve job |
| **Guide-update PR merging** | `auto-merge` only fires for `source-note` PRs (single-file additions). All `guide-update` PRs (Smith batch, Smith rework, Gardener, contradiction-resolver) require a human merge — usually after Assayer APPROVE |
| **Persistent Assayer rejections on a Smith PR** | If `auto-rework` and one round of human `/rework` both fail to address feedback, judgment-call: comment `/rebase` for fresh synthesis, or close the PR and re-trigger Smith via a forced empty commit on `main` |
| **Persistent Miner failures on the same source** | If a source issue cycles through 2-3 stuck PRs (e.g., dead-branch state, persistent cross-ref hallucination on a hard-to-cite source), label the issue `miner-blocked` and move on. Loss is acceptable |
| **Backlog drain** | The hourly Miner cron drains 48 issues/day. If the queue exceeds ~80 issues, dispatch extra batches via `gh workflow run miner-batch.yml` to keep latency reasonable |
| **Workflow YAML changes** | Rare — only when adding a new agent, changing triggers, or fixing a bug uncovered by a new failure mode |
| **Re-triage of an old backlog** | If issues were filed before automation was complete and never triaged, toggle the `source-submission` label off and on each one (with ~30s spacing to avoid rate limits) to re-fire `source-pipeline.yml` |
