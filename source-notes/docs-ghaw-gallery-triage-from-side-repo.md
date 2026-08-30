---
source_url: https://github.github.com/gh-aw/gallery/multi-repo/triage-from-side-repo
source_type: docs
title: "Example: Triage from Side Repo"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: settled
issue: "#3066"
---

# Example: Triage from Side Repo

> A first-party gh-aw gallery walkthrough for running scheduled issue triage on
> a main repository entirely from an isolated side repository, plus a two-part
> slash-command relay bridge that works around the platform limitation that
> `slash_command` triggers (and GitHub webhooks generally) only fire in the
> repository where the comment was posted.

## Source Context

- **Type**: docs (gh-aw "Gallery" section — a single worked example page under
  `gallery/multi-repo/`, structurally similar to the "Examples" section pages
  already in the corpus, e.g. `docs-ghaw-examples-ai-issue-triage.md` and
  `docs-ghaw-code-quality-monitoring.md`. Short, prescriptive, with two complete
  workflow YAML samples, one plain GitHub Actions relay YAML sample, a permission
  table, and a mermaid flowchart. Site navigation places it between "Multi-Repository
  Examples" (previous) and "Code Quality Monitoring" (next) in the Gallery's
  multi-repo reading order.)
- **Author credibility**: First-party GitHub Next / Microsoft Research documentation
  for the `gh-aw` platform — the same team and doc set behind
  `docs-ghaw-multi-repo-ops.md`, `docs-ghaw-code-quality-monitoring.md`, and
  `docs-ghaw-chatops.md`. Authoritative for the exact YAML schema, setup commands,
  and stated platform constraints (e.g. webhook scoping). No external metrics or
  field-usage data are cited.
- **Scope**: One concrete multi-repo scenario — issue triage run from a side
  automation repository, combining a scheduled `every 6h` triage workflow with an
  on-demand `/triage`-triggered workflow reached via a cross-repo relay. Does NOT
  cover: the abstract MultiRepoOps topology taxonomy (`docs-ghaw-multi-repo-ops.md`),
  same-repo issue triage (`docs-ghaw-examples-ai-issue-triage.md`), the native
  `slash_command` trigger's own schema (`docs-ghaw-chatops.md`), or general
  `workflow_dispatch` typed-input mechanics (`docs-ghaw-dispatch-ops.md`).

## Extracted Claims

### Claim 1: The side repo hosts all triage automation; the main repo receives only the resulting labels and comments, with a slash-command bridge for real-time response alongside the scheduled run

- **Evidence**: The page's opening paragraph states the architecture directly,
  and the page's meta description repeats the same framing.
- **Confidence**: settled (first-party description of a shipped gallery example)
- **Quote**: "This example shows how to run automated triage on `my-org/main-repo`
  from a dedicated side repository. The side repo hosts all automation workflows;
  the main repo receives only the resulting labels and comments. A slash-command
  bridge is included for real-time `/triage` response alongside the scheduled
  triage run."
- **Our assessment**: This is a concrete instantiation of the SideRepoOps isolation
  pattern referenced abstractly in `docs-ghaw-ephemerals.md` Claim 12 and applied
  to code quality monitoring in `docs-ghaw-code-quality-monitoring.md` Claim 1 —
  here applied to issue triage specifically. The novel element is not the isolation
  itself (already documented for code quality monitoring) but the addition of a
  real-time human-triggered path (`/triage`) layered on top of the scheduled batch
  run, which the code-quality-monitoring example does not have.

### Claim 2: Scheduled triage runs every 6 hours from the side repo, finding unlabeled issues opened in the last 7 days and adding labels plus a triage comment, capped at 20 issues per run

- **Evidence**: The "How It Works" section's first bullet, plus the scheduled
  workflow's `on: every 6h` trigger and its prompt body's "Limit to 20 issues per
  run to avoid rate limits" instruction (see Concrete Artifacts).
- **Confidence**: settled (stated directly; YAML and prompt shown verbatim)
- **Quote**: "Scheduled triage runs every 6 hours from the side repo, finding
  unlabeled issues and adding appropriate labels and a triage comment."
- **Our assessment**: The `every 6h` cadence is more frequent than the weekly
  cadence used in `docs-ghaw-code-quality-monitoring.md`'s side-repo example
  (`on: weekly on monday`) — appropriate because issue triage has a freshness
  requirement (new issues should not sit unlabeled for a week) that code quality
  monitoring does not. The `Limit to 20 issues per run` instruction is a prompt-level
  cap distinct from any `safe-outputs: max:` field — it bounds how many issues the
  agent even attempts to process per invocation, not how many labels/comments it
  can write, complementing (not duplicating) the `allowed-labels`/target-repo
  bounding in Claim 4 below.

### Claim 3: Because GitHub webhooks only fire in the repository where the event occurs, real-time `/triage` support requires a two-part relay: a plain (non-agentic) GitHub Actions workflow in the main repo that forwards the command to the side repo via `workflow_dispatch`

- **Evidence**: The "How It Works" section's second bullet states the platform
  constraint and the workaround directly. The relay workflow (Part A) is
  explicitly flagged in a callout as not being a compiled gh-aw workflow.
- **Confidence**: settled (states a platform-level webhook-scoping constraint,
  not a gh-aw-specific design choice, and shows the complete workaround YAML)
- **Quote**: "Slash-command triage is triggered by `/triage` in the main repo.
  Because GitHub webhooks only fire in the repository where the event occurs, a
  thin relay workflow in the main repo forwards the command to the side repo via
  `workflow_dispatch`."
- **Our assessment**: This is the most architecturally significant claim in the
  source and directly answers the Prospector's key question about how the
  slash-command bridge differs from `docs-ghaw-chatops.md`'s native `slash_command`
  trigger. The native `slash_command` trigger (`docs-ghaw-chatops.md` Claim 1)
  only works because gh-aw compiles it into a GitHub Actions `issue_comment`
  listener in the *same* repository as the workflow — it cannot listen for
  comments posted in a *different* repository. This source shows the necessary
  workaround for the cross-repo case: a deliberately non-agentic, hand-written
  GitHub Actions YAML file (not a `.md` gh-aw source, not compiled by `gh aw
  compile`) whose only job is to detect the `/triage` comment and re-dispatch it
  as a `workflow_dispatch` call against the side repo via the GitHub REST API.
  This is a materially different mechanism from anything in `docs-ghaw-chatops.md`
  or `docs-ghaw-dispatch-ops.md`: those cover same-repo human-triggered patterns;
  this shows the cross-repo bridge those patterns cannot reach unassisted.

### Claim 4: `add-labels` in this cross-repo workflow uses the field name `allowed-labels:` (not `allowed:`) alongside `target-repo`, appearing identically in both the scheduled and on-demand workflow YAML

- **Evidence**: Both YAML code samples on the page — the scheduled `triage.md`
  workflow and the on-demand `triage-on-demand.md` workflow — configure
  `add-labels` with `target-repo: "my-org/main-repo"` and an 8-item
  `allowed-labels:` list (`bug`, `enhancement`, `question`, `documentation`,
  `good first issue`, `wontfix`, `duplicate`, `needs-info`). Verified directly
  against the page's raw HTML (see Extraction Notes), not just a rendered
  summary.
- **Confidence**: settled (verbatim YAML, appears twice on the same page,
  internally consistent)
- **Quote**: (no direct prose quote; YAML verbatim in Concrete Artifacts —
  `add-labels: { target-repo: "my-org/main-repo", allowed-labels: [bug,
  enhancement, question, documentation, good first issue, wontfix, duplicate,
  needs-info] }`)
- **Our assessment**: **This contradicts `docs-ghaw-issueops.md` Claim 3 and
  `docs-ghaw-examples-ai-issue-triage.md` Claim 4**, both of which show the same
  `add-labels` allowlist field named `allowed:` (not `allowed-labels:`) in
  verbatim same-repo YAML samples. `docs-ghaw-multi-repo-ops.md` Claim 1 states
  that adding `target-repo` does not change a safe output's API surface, which
  predicts the field name should be identical whether or not `target-repo` is
  present — this source's two consistent, verbatim samples contradict that
  prediction. Filed as **contradiction issue #3089** — see Cross-References.

### Claim 5: The fine-grained PAT (`GH_AW_MAIN_REPO_TOKEN`) is scoped only to the main repo, with `Issues: Read & write` (to read issues, add labels and comments) and `Contents: Read-only` (to read repo structure for GitHub tools), and must be supplied to both `tools.github` and `safe-outputs`

- **Evidence**: The "Create the Authentication Token" section's permission table
  and the accompanying warning callout.
- **Confidence**: settled (verbatim table and callout)
- **Quote**: "The default `GITHUB_TOKEN` cannot access other repositories. You
  must use this additional token for both `tools.github` and `safe-outputs`."
- **Our assessment**: This directly corroborates `docs-ghaw-multi-repo-ops.md`
  Claim 3 (the `GITHUB_TOKEN` cross-repo scoping footgun) and
  `docs-ghaw-code-quality-monitoring.md` Claim 9 (the same token required on two
  separate config locations). The permission table's two-row scope (`Issues:
  Read & write` / `Contents: Read-only`) is narrower than
  `docs-ghaw-multi-repo-issue-tracking.md` Claim 10's `repo`/`public_repo` PAT
  scope guidance for cross-repo issue tracking, and matches the least-privilege
  principle from `docs-ghaw-multi-repo-ops.md` Claim 7 almost exactly — it is
  effectively the same two-permission scope already documented in
  `docs-ghaw-code-quality-monitoring.md` Claim 2 (`Contents: Read-only` +
  `Issues: Read & write`) for the code-quality side-repo pattern, now confirmed
  for the triage side-repo pattern as well. Two independent gallery examples
  converging on the identical two-permission scope is stronger evidence that
  this is gh-aw's house-recommended minimum for any side-repo-to-main-repo,
  read-code/write-issues workflow.

### Claim 6: The page recommends a GitHub App token over a PAT for this pattern, citing on-demand minting and automatic revocation after each job

- **Evidence**: The note immediately following the PAT authentication section.
- **Confidence**: settled (verbatim recommendation)
- **Quote**: "For enhanced security, use a GitHub App token instead of a PAT —
  tokens are minted on demand and automatically revoked after each job."
- **Our assessment**: Corroborates `docs-ghaw-multi-repo-ops.md` Claim 8's four
  named advantages of GitHub App installation tokens over PATs (per-job minting,
  automatic revocation, fine-grained permissions, better attribution) — this
  source repeats exactly two of those four (minting, revocation) in a more
  compressed form, consistent with but not adding new detail to the existing
  claim.

### Claim 7: The main-repo relay workflow requires its own separate secret, `GH_AW_SIDE_REPO_TOKEN` — a PAT scoped to `Actions: write` on the side (automation) repository, distinct from `GH_AW_MAIN_REPO_TOKEN`

- **Evidence**: The sentence following the relay workflow's YAML code sample.
- **Confidence**: settled (stated directly, names the exact permission scope)
- **Quote**: "This relay needs a `GH_AW_SIDE_REPO_TOKEN` secret in `main-repo` —
  a PAT with `Actions: write` on `main-repo-automation`."
- **Our assessment**: This is a second, independent token role not covered by
  Claim 5's `GH_AW_MAIN_REPO_TOKEN` — the two tokens point in opposite
  directions (`GH_AW_MAIN_REPO_TOKEN`: side repo → writes to main repo;
  `GH_AW_SIDE_REPO_TOKEN`: main repo → dispatches a workflow in the side repo).
  This is architecturally close to the three-token model in
  `docs-ghaw-central-repo-ops.md` Claim 3 (one token per directional role, no
  sharing), but here the roles are bridge-relay and triage-write rather than
  orchestrator-read/checkout/output-delivery — a different topology (bidirectional
  bridge between exactly two repos) reusing the same least-privilege,
  one-token-per-role principle. No prior source note documents an `Actions:
  write`-scoped PAT used specifically to trigger a `workflow_dispatch` in a
  *different* repository as its sole purpose.

### Claim 8: The relay workflow is deliberately a plain GitHub Actions `.yml` file, not a compiled gh-aw agentic workflow, and must be authored directly as `.yml` rather than as a `.md` source

- **Evidence**: A "Note" callout directly beneath the relay workflow's heading.
- **Confidence**: settled (explicit platform-authoring guidance)
- **Quote**: "This is a plain GitHub Actions YAML file, not a compiled agentic
  workflow. Create it directly as `.yml`."
- **Our assessment**: This is a new and specific authoring-boundary rule not
  documented elsewhere in the corpus: not every workflow file in a gh-aw-managed
  repository needs to be (or should be) an agentic `.md` source compiled via
  `gh aw compile`. The relay's job — check a comment body for an exact string
  match and call one GitHub API endpoint — has no AI component and gains nothing
  from being agentic; making it a deterministic plain-YAML workflow is both
  simpler and removes an unnecessary AI-in-the-loop step from a security-relevant
  trigger path (the relay is the thing standing between an arbitrary commenter and
  a cross-repo `workflow_dispatch` call). This mirrors the design principle in
  `docs-ghaw-central-repo-ops.md` Claim 1 (separate policy from mechanism) and the
  explicit determinism requirement for relay-class workflows in
  `docs-ghaw-correction-ops.md` Claim 4 ("the relay workflow must be purely
  deterministic... no diffs, no intent inference, no correctness decisions") —
  though that note's relay forwards data one-way within a single conceptual
  system (production → ops), while this relay's determinism requirement is about
  bridging trigger events across two separate repositories, a distinct use case
  reaching a structurally similar conclusion (relays should not be agentic).

### Claim 9: The relay's trigger condition combines an exact string match on the comment body with an explicit pull-request exclusion, so `/triage` on a PR comment does not fire the relay

- **Evidence**: The relay workflow's job-level `if:` condition, shown verbatim in
  the code sample.
- **Confidence**: settled (shown directly in the code sample)
- **Quote**: (no direct prose quote; YAML verbatim in Concrete Artifacts —
  `if: github.event.comment.body == '/triage' && github.event.issue.pull_request
  == null`)
- **Our assessment**: The `github.event.issue.pull_request == null` check is
  necessary because, as `docs-ghaw-chatops.md` Claim 2 documents for the native
  `slash_command` trigger, GitHub's underlying `issue_comment` event fires
  identically for both issue comments and PR comments — gh-aw's own
  `events:` field abstracts this distinction away for native `slash_command`
  triggers, but this hand-written relay is plain GitHub Actions YAML with no
  such abstraction, so the author must write the PR-exclusion check manually.
  This is a concrete illustration of what a harness author gives up (automatic
  event-context filtering) by choosing the deterministic-relay escape hatch from
  Claim 8 over the native `slash_command` trigger.

### Claim 10: The on-demand workflow passes the triggering issue's number and URL through `workflow_dispatch` typed string inputs, and reuses the identical `add-labels`/`add-comment` cross-repo safe-outputs configuration as the scheduled workflow except that `add-comment` targets the specific dispatched issue rather than `target: "*"`

- **Evidence**: The on-demand workflow's `on: workflow_dispatch: inputs:` block
  (`issue_number`, `issue_url`, both required strings) and its `safe-outputs:
  add-comment: target: "${{ github.event.inputs.issue_number }}"` versus the
  scheduled workflow's `add-comment: target: "*"`.
- **Confidence**: settled (shown directly in the code sample)
- **Quote**: (no direct prose quote; YAML verbatim in Concrete Artifacts)
- **Our assessment**: This is a concrete example of `docs-ghaw-dispatch-ops.md`
  Claim 2's typed `string` input parameter being used specifically to carry
  cross-repo dispatch context (issue number + URL) from the relay call into the
  side repo's agent prompt, rather than for direct human-typed CLI input as
  `docs-ghaw-dispatch-ops.md` primarily illustrates. The `target: "*"` (scheduled,
  agent must find the right issues among many) vs. `target:
  "${{ github.event.inputs.issue_number }}"` (on-demand, target is already known
  from the relay) distinction is the on-demand/scheduled variant of the same
  `add-comment` cross-repo primitive documented abstractly in
  `docs-ghaw-multi-repo-issue-tracking.md` Claim 3.

## Concrete Artifacts

### Architecture flowchart (mermaid source, as embedded in the page)

```
flowchart LR
    subgraph side["Side repo (automation)"]
        schedule([Every 6h / dispatch]) --> triage[Triage agent]
    end
    triage -->|add-labels / add-comment| main[main-repo]

    subgraph main_repo["main-repo"]
        slash(["/triage comment"]) --> relay[Relay workflow]
    end
    relay -->|workflow_dispatch| triage
```

*Source: gh-aw gallery, "Example: Triage from Side Repo" — "How It Works" section.*

### Fine-grained PAT permission table

```
Permission | Level        | Purpose
---------- | ------------ | -----------------------------------------
Issues     | Read & write | Read issues, add labels and comments
Contents   | Read-only    | Read repo structure (for GitHub tools)
```

*Source: gh-aw gallery, "Example: Triage from Side Repo" — "2. Create the Authentication Token" section. Table extracted from the page's raw HTML `<table>` element.*

### Side repository setup commands

```bash
gh repo create my-org/main-repo-automation --private
gh repo clone my-org/main-repo-automation
cd main-repo-automation

gh secret set GH_AW_MAIN_REPO_TOKEN --repo my-org/main-repo-automation
```

*Source: gh-aw gallery, "Example: Triage from Side Repo" — "1. Create the Side Repository" and "2. Create the Authentication Token" sections.*

### Scheduled triage workflow — `.github/workflows/triage.md` (side repo)

```yaml
---
on: every 6h
permissions:
  contents: read
safe-outputs:
  github-token: ${{ secrets.GH_AW_MAIN_REPO_TOKEN }}
  add-labels:
    target-repo: "my-org/main-repo"
    allowed-labels:
      - bug
      - enhancement
      - question
      - documentation
      - good first issue
      - wontfix
      - duplicate
      - needs-info
  add-comment:
    target-repo: "my-org/main-repo"
    target: "*"
tools:
  github:
    github-token: ${{ secrets.GH_AW_MAIN_REPO_TOKEN }}
    toolsets: [issues]
---
# Triage Main Repository Issues
Find all unlabeled issues in my-org/main-repo opened in the last 7 days.
For each issue:
1. Read the title and body carefully
2. Assign one primary label (bug / enhancement / question / documentation / good first issue)
3. Add a second label if clearly applicable (e.g., duplicate, needs-info, wontfix)
4. Post a brief triage comment explaining the label choice and any suggested next step

Limit to 20 issues per run to avoid rate limits.
```

Compiled with: `gh aw compile`

*Source: gh-aw gallery, "Example: Triage from Side Repo" — "3. Create the Scheduled Triage Workflow" section. Reconstructed from the page's raw HTML `<pre>` block; keys, values, and prompt text are verbatim.*

### Slash-command relay (main repo) — plain GitHub Actions YAML, `.github/workflows/triage-relay.yml`

```yaml
name: Triage relay
on:
  issue_comment:
    types: [created]

jobs:
  relay:
    if: github.event.comment.body == '/triage' && github.event.issue.pull_request == null
    runs-on: ubuntu-latest
    steps:
      - name: Forward to automation repo
        uses: actions/github-script@v7
        with:
          github-token: ${{ secrets.GH_AW_SIDE_REPO_TOKEN }}
          script: |
            await github.rest.actions.createWorkflowDispatch({
              owner: 'my-org',
              repo: 'main-repo-automation',
              workflow_id: 'triage-on-demand.lock.yml',
              ref: 'main',
              inputs: {
                issue_number: String(context.issue.number),
                issue_url: context.payload.issue.html_url,
              }
            });
```

*Source: gh-aw gallery, "Example: Triage from Side Repo" — "4. Create the Slash-Command Bridge", Step 1. Explicitly labeled on the page as "not a compiled agentic workflow" (see Claim 8).*

### On-demand triage workflow (side repo) — `.github/workflows/triage-on-demand.md`

```yaml
---
on:
  workflow_dispatch:
    inputs:
      issue_number:
        description: "Issue number to triage"
        required: true
      issue_url:
        description: "Issue URL for context"
        required: true

permissions:
  contents: read

safe-outputs:
  github-token: ${{ secrets.GH_AW_MAIN_REPO_TOKEN }}
  add-labels:
    target-repo: "my-org/main-repo"
    allowed-labels:
      - bug
      - enhancement
      - question
      - documentation
      - good first issue
      - wontfix
      - duplicate
      - needs-info
  add-comment:
    target-repo: "my-org/main-repo"
    target: "${{ github.event.inputs.issue_number }}"

tools:
  github:
    github-token: ${{ secrets.GH_AW_MAIN_REPO_TOKEN }}
    toolsets: [issues]
---
# Triage Issue on Demand
Triage issue #${{ github.event.inputs.issue_number }} in my-org/main-repo.
Read the issue at ${{ github.event.inputs.issue_url }}, assign the most appropriate label, and post a brief comment explaining the triage decision.
```

Compiled with: `gh aw compile`

*Source: gh-aw gallery, "Example: Triage from Side Repo" — "4. Create the Slash-Command Bridge", Step 2.*

### "Learn More" related pages linked from this page (not fetched for this note)

```
- MultiRepoOps               — Side repository pattern and other topologies  → /gh-aw/patterns/multi-repo-ops/
- IssueOps                   — Event-driven issue automation in the main repo → /gh-aw/patterns/issue-ops/
- ChatOps                    — Slash command workflows                       → /gh-aw/patterns/chat-ops/
- Cross-Repository Operations — target-repo configuration                    → (link target not captured in raw-text extraction)
- Authentication             — PAT and GitHub App setup                      → /gh-aw/reference/auth/
- Safe Outputs                — Labels, comments, and allowed-labels          → (link target not captured in raw-text extraction)
```

*Source: gh-aw gallery, "Example: Triage from Side Repo" — "Learn More" section. Note the page's own link label reads "Safe Outputs — Labels, comments, and allowed-labels" (i.e., the page's own site copy names the field `allowed-labels`, consistent with Claim 4's YAML, not a stray typo confined to the code block.)*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 3 (default `GITHUB_TOKEN` scoped to the
    current repository only): Claim 5 above restates the identical constraint in
    the triage side-repo context.
  - `docs-ghaw-multi-repo-ops.md` Claim 7 (PAT least-privilege: read on source,
    write on target) and Claim 8 (GitHub App tokens preferred for per-job minting
    and automatic revocation): Claims 5 and 6 above are concrete instantiations of
    both.
  - `docs-ghaw-code-quality-monitoring.md` Claim 2 (fine-grained PAT scope of
    `Contents: Read-only` + `Issues: Read & write` for a side-repo-to-main-repo
    workflow) and Claim 9 (the token must be set on both the read-side config and
    `safe-outputs`, or cross-repo operations silently fail): Claim 5 above shows
    an independently-authored gallery example converging on the identical
    two-permission PAT scope and the same two-location token requirement, for a
    different use case (triage vs. code quality) — corroborating that this is
    gh-aw's house-recommended minimum scope for the side-repo pattern generally,
    not an artifact of one example.
  - `docs-ghaw-ephemerals.md` Claim 12 (SideRepoOps isolates automation from the
    main repository by running workflows in a dedicated side repo targeting the
    main repo via PAT): this source is a complete, concrete worked example of
    that abstractly-referenced pattern.
  - `docs-ghaw-chatops.md` Claim 2 (the `issue_comment` GitHub Actions event fires
    identically for issue and PR comments; gh-aw's `events:` field filters this
    automatically for native `slash_command` triggers): Claim 9 above shows the
    same underlying event-firing behavior from the opposite side — a hand-written
    relay that must implement the PR-exclusion filtering manually because it has
    no `events:` field to rely on.
  - `docs-ghaw-dispatch-ops.md` Claim 2 (`workflow_dispatch` supports typed
    `string` input parameters): Claim 10 above shows a concrete use of typed
    string inputs (`issue_number`, `issue_url`) for a purpose that note does not
    illustrate — carrying cross-repo relay context rather than direct human input.

- **Contradicts**:
  - **`docs-ghaw-issueops.md` Claim 3 and `docs-ghaw-examples-ai-issue-triage.md`
    Claim 4** (Claim 4 above): both existing notes show `add-labels`'s allowlist
    field verbatim as `allowed:` in same-repo YAML samples; this source shows the
    same field verbatim as `allowed-labels:` in two independent cross-repo YAML
    samples, and the page's own "Learn More" link copy also uses
    `allowed-labels`. This conflicts with `docs-ghaw-multi-repo-ops.md` Claim 1's
    statement that adding `target-repo` does not change a safe output's API
    surface. **Filed as contradiction issue #3089** (`add-labels` allowlist field
    name: `allowed:` vs `allowed-labels:`) — no verdict is asserted in this note;
    see that issue for resolution status.

- **Extends**:
  - `docs-ghaw-code-quality-monitoring.md`: that note is the corpus's first
    complete side-repo worked example (for code quality monitoring, weekly
    cadence, no human-triggered path). This note extends the side-repo pattern to
    issue triage specifically, at a much higher cadence (every 6h vs. weekly),
    and adds a real-time human-triggered path that the code-quality example
    entirely lacks.
  - `docs-ghaw-chatops.md`: that note documents gh-aw's native, same-repo
    `slash_command` trigger and states the trigger "activates a workflow when a
    user posts a matching slash command in a GitHub comment." This source shows
    the necessary workaround when the command is posted in a *different*
    repository from the one that should act on it — a hand-rolled,
    non-agentic relay plus `workflow_dispatch`, not a variant of the native
    trigger. This is the first corpus source to document why the native
    `slash_command` trigger cannot be used across repository boundaries and what
    replaces it.
  - `docs-ghaw-central-repo-ops.md`: that note documents a three-token,
    one-directional (control-plane → target repos) permission model for org-scale
    orchestration. This source shows a two-token, *bidirectional* model between
    exactly two repos (`GH_AW_MAIN_REPO_TOKEN` for side→main writes,
    `GH_AW_SIDE_REPO_TOKEN` for main→side dispatch) — the same one-token-per-role
    principle applied to a smaller, two-party bridge topology rather than
    one-to-many fan-out.
  - `docs-ghaw-correction-ops.md` Claim 4 (relay workflows must be purely
    deterministic, with no inference or correctness decisions): Claim 8 above is
    an independent instance of the same design conclusion — deterministic
    plain-YAML relays, not agentic ones — reached for a structurally different
    problem (cross-repo trigger bridging vs. production-to-ops data forwarding).

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **The stated reason native `slash_command` triggers cannot bridge
    repositories** (Claim 3): "GitHub webhooks only fire in the repository where
    the event occurs" is the first explicit statement in the corpus of *why*
    ChatOps-style triggers are repository-scoped, and the first documented
    workaround (a plain-YAML relay + cross-repo `workflow_dispatch`).
  - **A deterministic, non-agentic relay workflow as the correct authoring choice
    for a cross-repo trigger bridge, with an explicit "author as `.yml`, not
    `.md`" rule** (Claim 8): no existing source states this authoring-boundary
    guidance (when a workflow file in a gh-aw-managed repo should deliberately
    NOT be a compiled agentic workflow).
  - **A two-token, bidirectional bridge permission model between exactly two
    repositories** (Claim 7): distinct from the corpus's existing one-directional,
    fan-out token models (`docs-ghaw-multi-repo-ops.md`, `docs-ghaw-central-repo-ops.md`).
  - **`allowed-labels:` as an alternate (and, per the filed contradiction,
    disputed) field name for the `add-labels` allowlist in a cross-repo
    configuration** (Claim 4): new to the corpus and in direct tension with prior
    notes — see Contradicts above.
  - **Manual PR-comment exclusion (`github.event.issue.pull_request == null`) as
    a required condition in a hand-written relay, illustrating what is lost by
    not using the native `slash_command` trigger's `events:` field** (Claim 9).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the side-repo triage pattern as a
  named variant of SideRepoOps alongside the existing code-quality-monitoring
  example (Claims 1–2), and add the cross-repo slash-command relay (Claims 3, 8,
  9) as the documented pattern for bridging a `/command` posted in one repository
  to an agentic workflow running in another — explicitly noting that this
  requires a hand-written, non-agentic relay `.yml` file rather than a native
  `slash_command` trigger, and that the relay must implement its own
  event-context filtering (PR vs. issue) since it has no `events:` field. Flag
  the `allowed:` vs. `allowed-labels:` field-name question (Claim 4) as unresolved
  pending contradiction issue #3089 — do not commit either spelling to guide text
  until that issue is resolved.
- **Chapter 03 (Safety and Verification)**: Add the two-token bidirectional bridge
  model (Claim 7: `GH_AW_MAIN_REPO_TOKEN` scoped to `Issues: Read & write` +
  `Contents: Read-only` on the main repo; `GH_AW_SIDE_REPO_TOKEN` scoped to
  `Actions: write` on the side repo) as a second concrete least-privilege
  reference alongside the three-token CentralRepoOps model, for the specific case
  of a two-repository automation bridge rather than one-to-many orchestration.
  Add the "relay workflows should be deterministic, non-agentic YAML" guidance
  (Claim 8) as a general safety pattern for any cross-repo or cross-boundary
  trigger bridge, cross-referencing `docs-ghaw-correction-ops.md` Claim 4 as a
  second, independent source reaching the same conclusion.

## Extraction Notes

1. **WebFetch output cross-checked against raw HTML.** Given the documented
   systematic WebFetch failure mode for `github.github.com/gh-aw/examples/*` and
   `guides/*` pages noted in `docs-ghaw-examples-ai-issue-triage.md` Extraction
   Note 1 (fabricated headings and reworded prose on short Astro/Starlight
   pages), I did not trust the initial WebFetch summary at face value even
   though it looked plausible. I downloaded the page's raw HTML directly via
   `curl`, located the `sl-markdown-content` container, and extracted the prose,
   code blocks, table, and asides by parsing the HTML myself. Every quote, the
   permission table, the two full workflow YAML samples, and the relay YAML in
   this note are copied from that raw HTML extraction (verified independently in
   two passes — a full-text regex-stripped pass and a targeted per-element
   pass for the table and "Note" asides), not from the WebFetch summary alone.
   In this case the WebFetch summary happened to match the raw HTML closely
   (no fabricated headings were detected), but I did not rely on that
   without checking.
2. **Related pages not fetched.** The "Learn More" section links to
   MultiRepoOps, IssueOps, ChatOps, Cross-Repository Operations, Authentication,
   and Safe Outputs reference pages — all already covered by existing corpus
   notes (`docs-ghaw-multi-repo-ops.md`, `docs-ghaw-issueops.md`,
   `docs-ghaw-chatops.md`) except the Safe Outputs and Cross-Repository
   Operations reference pages, whose exact link targets were not captured by the
   raw-text extraction (see Concrete Artifacts). Given the source page itself is
   short and self-contained, and its own reference-style links didn't surface
   new content beyond what's already in those existing notes, I did not fetch
   them separately as part of this extraction.
3. **Mermaid flowchart embedded as source, not rendered.** The page includes a
   mermaid diagram illustrating the architecture; I extracted its literal source
   text (a code block, not a description of a rendered image) since gh-aw docs
   pages embed mermaid as text that a browser renders client-side.
4. **No publication date.** The page carries no visible publication or
   last-updated date; `date_published` is left null, consistent with other
   gh-aw docs notes in this corpus.
5. **One contradiction filed.** Reviewed `docs-ghaw-issueops.md`,
   `docs-ghaw-examples-ai-issue-triage.md`, `docs-ghaw-multi-repo-ops.md`,
   `docs-ghaw-multi-repo-issue-tracking.md`, `docs-ghaw-code-quality-monitoring.md`,
   `docs-ghaw-central-repo-ops.md`, `docs-ghaw-chatops.md`,
   `docs-ghaw-dispatch-ops.md`, `docs-ghaw-ephemerals.md`, and
   `docs-ghaw-correction-ops.md`. One claim (Claim 4, the `add-labels` allowlist
   field name) materially opposes `docs-ghaw-issueops.md` Claim 3 and
   `docs-ghaw-examples-ai-issue-triage.md` Claim 4 at the MINER.md §4a threshold —
   filed as contradiction issue #3089, verdict left to human/Smith resolution.
   No other claims in this source oppose existing source notes; the PAT scoping,
   GitHub App preference, and Safe Outputs write-separation claims are all
   consistent with (and corroborate) the existing corpus.
