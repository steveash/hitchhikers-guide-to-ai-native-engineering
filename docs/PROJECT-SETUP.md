# GitHub Project (v2) Setup — Hitchhiker's Guide Pipeline

This is the runbook for creating the **Hitchhikers Guide Pipeline** GitHub
Project. It is referenced from the README's "Pipeline Status" section.

The project is a single shared dashboard for everyone watching the agent
pipeline run: triagers, reviewers, and chapter editors. It is **native GitHub
Projects v2** — no custom build, no scraper, no separate web app.

## TL;DR

```bash
# One-time auth refresh (gh defaults omit this scope)
gh auth refresh -s project

# Bootstrap script — creates project, custom fields, links to repo, and
# attempts view creation via GraphQL
./scripts/setup-github-project.sh

# Open the project and finish view configuration in the UI (filters/groupings
# cannot be set via gh CLI as of 2026-04)
gh project view <NUMBER> --owner steveash --web
```

Then update `README.md` "Pipeline Status" with the project URL.

## Prerequisites

1. You have admin on `steveash/hitchhikers-guide-to-ai-native-engineering`.
2. `gh` CLI is installed and authenticated as a user with the `project` scope.
   Default `gh auth login` does **not** grant this scope. Run:
   ```bash
   gh auth refresh -s project
   ```
3. `jq` is installed (used by the bootstrap script).
4. Pipeline labels exist on the repo. The bootstrap step is handled separately
   — see [Labels](#labels) below.

## What gets created

### The project

| Setting | Value |
|---------|-------|
| Title   | `Hitchhikers Guide Pipeline` |
| Owner   | `steveash` (user-scoped, not org) |
| Linked repo | `steveash/hitchhikers-guide-to-ai-native-engineering` |
| Visibility  | Public |

### Custom fields

The bootstrap script creates three single-select custom fields:

| Field | Options | Used by |
|-------|---------|---------|
| **Triage Status** | `untriaged`, `accepted`, `rejected`, `duplicate`, `in-progress`, `done` | Source intake view |
| **Assayer Check** | `pending`, `running`, `passed`, `failed`, `skipped` | PR review queue view |
| **Chapter** | `ch00-principles`, `ch01-daily-workflows`, `ch02-harness-engineering`, `ch03-safety-and-verification`, `ch04-context-engineering`, `ch05-team-adoption`, `cross-cutting` | Chapter health view |

### Views

Three views, all created against the linked repo:

#### 1. Source intake (Table layout)

**Purpose:** triage queue for new sources flagged by humans or by the
Repo Scout / Failure Scanner agents.

**Filter:**
```
is:issue is:open label:new-source,new-repo,failure-report
```

**Group by:** `Triage Status`

**Columns shown:** Title, Labels, Triage Status, Assignees, Updated

#### 2. PR review queue (Board layout)

**Purpose:** at-a-glance view of every open PR and where it sits in the
Assayer (automated review agent) gate.

**Filter:**
```
is:pr is:open
```

**Group by:** `Assayer Check`

**Columns shown:** Title, Author, Assayer Check, Reviewers, Created

#### 3. Chapter health (Table layout)

**Purpose:** show all open work tagged to a specific guide chapter, so
chapter editors know what's queued against their chapter.

**Filter:**
```
is:issue is:open label:ch00-principles,ch01-daily-workflows,ch02-harness-engineering,ch03-safety-and-verification,ch04-context-engineering,ch05-team-adoption
```

**Group by:** `Chapter` (the custom field, not the label — fall back to label
grouping if you prefer)

**Columns shown:** Title, Chapter, Labels, Assignees, Updated

## Why these three views

| View | Audience | Question it answers |
|------|----------|---------------------|
| Source intake | Triagers | "What new sources need a yes/no/duplicate decision?" |
| PR review queue | Reviewers, maintainer | "What's blocking each open PR — Assayer? Reviewer? Me?" |
| Chapter health | Chapter editors | "What's queued against my chapter and what state is it in?" |

These map directly to the three roles humans play in the pipeline:
filtering noise, gating quality, and curating chapters.

## Labels

The views above filter on these labels. They are created automatically by the
bootstrap script (or manually with `gh label create`):

**Intake labels** (auto-applied by issue templates in `.github/ISSUE_TEMPLATE/`):
- `new-source` — generic source submission
- `source-submission` — submitted via UI form
- `new-repo` — practitioner repo flagged for analysis
- `practitioner-repo` — practitioner repo source
- `failure-report` — "this didn't work" report
- `contradiction` — two sources disagree
- `needs-resolution` — awaiting human verdict

**Chapter labels** (one per chapter in `guide/`):
- `ch00-principles`
- `ch01-daily-workflows`
- `ch02-harness-engineering`
- `ch03-safety-and-verification`
- `ch04-context-engineering`
- `ch05-team-adoption`

To recreate any missing labels:
```bash
gh label create <name> --repo steveash/hitchhikers-guide-to-ai-native-engineering --color <hex>
```

## Manual steps (gh CLI limitations as of 2026-04)

The `gh project` command supports project / field / item operations but
**cannot configure view filters or groupings**. After running the bootstrap
script, open each view in the UI and apply the filter strings above.

GraphQL `createProjectV2View` is available but does not accept filter strings —
they must be set with a follow-up `updateProjectV2View` mutation that uses an
internal undocumented field. For now the simpler path is the click-through.

If/when `gh` adds first-class view-configuration support, replace the manual
step with a script call here.

## Verification checklist

After setup, confirm:

- [ ] Project visible at `https://github.com/users/steveash/projects/<NUMBER>`
- [ ] Project linked to the repo (visible under repo → Projects tab)
- [ ] Three views present and named correctly
- [ ] Source intake shows recent issues with intake labels
- [ ] PR review queue shows at least one open PR (or is correctly empty)
- [ ] Chapter health shows chapter-tagged issues grouped by chapter
- [ ] README "Pipeline Status" section updated with the project URL

## Updating the README

After the project URL is final, edit `README.md` and replace the placeholder
in the "Pipeline Status" section:

```markdown
## Pipeline Status

Live dashboard: <https://github.com/users/steveash/projects/NUMBER>
```

The placeholder is intentionally absent from the bootstrap script — the
README change is human-reviewed because URLs in READMEs outlive scripts.
