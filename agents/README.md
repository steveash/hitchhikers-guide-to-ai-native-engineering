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

## Current Status: Manual Orchestration

The agents are currently run manually (human triggers Claude Code with
the agent definition as context). See [VALIDATION.md](../VALIDATION.md)
for the manual validation protocol.

Automation via GitHub Actions will be enabled after the manual validation
proves the agents produce deep, useful output.
