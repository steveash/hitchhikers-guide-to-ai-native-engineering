---
source_url: https://github.github.com/gh-aw/patterns/project-ops/
source_type: docs
title: "GitHub Agentic Workflows: ProjectOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: emerging
issue: "#331"
---

# GitHub Agentic Workflows: ProjectOps Pattern

> The authoritative reference for agent-driven GitHub Projects board management — documents
> the authentication gap that forces a dual-token layout (read vs. write PAT separate from
> `GITHUB_TOKEN`), the three-tier write-escalation model (auto-apply → suggest-only →
> explicit approval), the field-contract pattern for preventing single-select field drift,
> and four project-specific Safe Output commands; the first corpus source to cover Projects
> API authentication requirements and project board write-control patterns.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Patterns > ProjectOps"
  — prescriptive pattern reference for agent-driven GitHub Projects management, not API
  reference or conceptual overview. Patterns pages document proven interaction models for
  specific use cases.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw` platform.
  Claims about Projects API authentication requirements, safe-output configurations, and
  write-gate tiers are authoritative for this platform. Claims about generalizability
  of the three-tier write-escalation model or field-contract pattern beyond gh-aw and
  GitHub Projects require additional evidence.
- **Scope**: The ProjectOps pattern — Projects API authentication (PAT vs. GitHub App
  token, user-owned vs. org-owned, dual-token layout), two-layer architecture (GitHub
  Tools for reads + Safe Outputs for writes), four project-specific safe-output commands,
  three-tier write-gate escalation model, field-contract allowlist pattern, and the
  agent-vs-automation decision rubric. Does NOT cover: the five-layer security architecture
  (in `docs-ghaw-how-they-work.md`), ChatOps/IssueOps/LabelOps/DailyOps trigger patterns
  (covered in their respective notes), MCP server integration (`docs-ghaw-mcps.md`), or
  monitoring patterns (`docs-ghaw-monitoring-patterns.md`).

## Extracted Claims

### Claim 1: ProjectOps is explicitly scoped to judgment-intensive decisions — for simple rule-based project transitions, GitHub's built-in automations suffice

- **Evidence**: The page states the system "proves most valuable when judgment-intensive
  routing and field modifications are required. For straightforward, condition-based
  transitions, GitHub's built-in automations typically suffice."
- **Confidence**: emerging (design intent from first-party documentation; no measurement
  of judgment-intensity threshold is provided)
- **Quote**: "It proves most valuable when judgment-intensive routing and field modifications
  are required. For straightforward, condition-based transitions, GitHub's built-in
  automations typically suffice."
- **Our assessment**: This is a crisp agent-vs-automation decision rubric for project
  boards. The signal: if the routing decision can be expressed as a deterministic rule
  (e.g., "move to In Progress when a PR is linked"), use GitHub's native project
  automations. If the decision requires contextual judgment (e.g., "assess whether this
  issue is blocked, considering related PRs and comments"), reach for ProjectOps. This
  framing extends the pattern seen in `blog-gh-aw-operations-release-workflows.md`
  (release versioning works well for agents because the decision space is rule-bound)
  to project management: agents add value where the decision space cannot be enumerated.
  For Ch01 (Daily Workflows): add ProjectOps to the "when to use agents vs. automations"
  decision guide.

### Claim 2: `GITHUB_TOKEN` is repository-scoped and cannot access the GitHub Projects API — a separate PAT or GitHub App token is required as a repository secret

- **Evidence**: Authentication requirements documented on the page: `GITHUB_TOKEN` is
  implicitly excluded because the page mandates "A Project token (either PAT or GitHub
  App token)" as a prerequisite — a separate credential, not the workflow's default token.
  The user-owned and org-owned project sections both specify PAT or GitHub App tokens
  stored as repository secrets, with no mention of `GITHUB_TOKEN` as a viable option.
- **Confidence**: settled (first-party documentation; `GITHUB_TOKEN` scope limitations
  are a GitHub platform constraint)
- **Quote**: (from prerequisites list) "A Project token (either PAT or GitHub App token)"
- **Our assessment**: This is the most concrete harness engineering detail in the source —
  and it is a gotcha. Most gh-aw patterns can use `GITHUB_TOKEN` for read operations and
  Safe Outputs for writes. ProjectOps breaks this pattern: the GitHub Projects API requires
  out-of-band credentials entirely. Any team implementing ProjectOps must provision a
  separate PAT or GitHub App token before the workflow can do anything, including reads.
  For Ch02 (Harness Engineering): document this as an exception to the standard
  `GITHUB_TOKEN`-first approach — agents operating on project boards need explicitly
  provisioned credentials with `project` scope. This should be flagged prominently
  because practitioners accustomed to other gh-aw patterns will encounter auth failures
  if they assume `GITHUB_TOKEN` works.

### Claim 3: User-owned projects require a classic PAT with `project` and `repo` scopes; org-owned projects require a fine-grained PAT or GitHub App token with organization-level Projects permissions

- **Evidence**: Two-path authentication:
  - **User-owned**: "utilize a classic PAT stored as a repository secret. Required
    scopes include `project` and `repo` (when private repositories are involved)."
  - **Org-owned**: "employ either a fine-grained PAT or GitHub App token. Configuration
    requirements include: Resource owner selection for the organization; Repository access
    specification; Repository permissions: Contents Read (plus optional Issues/Pull
    Requests permissions); Organization permissions: Projects Read or Read and write."
- **Confidence**: settled (first-party documentation; these are GitHub API permission
  requirements)
- **Quote**: "For user-controlled projects, utilize a classic PAT stored as a repository
  secret. Required scopes include `project` and `repo`."
- **Our assessment**: The authentication split between user-owned and org-owned projects
  is a practical harness engineering consideration. Org-owned projects are the more common
  case in team workflows, and they require fine-grained PATs or GitHub App tokens — not
  the older classic PAT format. The fine-grained PAT requirement also means practitioners
  need to configure both repository-level and organization-level permissions, which involves
  organizational admin access in most GitHub org setups. For Ch02: document this two-path
  authentication decision. Flag that org-owned projects (the team workflow default) require
  more setup than user-owned and may require admin coordination to configure GitHub App
  tokens or org-level PAT permissions.

### Claim 4: The dual-token layout (`GH_AW_READ_PROJECT_TOKEN` / `GH_AW_WRITE_PROJECT_TOKEN`) enforces least-privilege at the credential level — matching the read/write capability split

- **Evidence**: Secret configuration: "Implement separate read and write tokens:
  `GH_AW_READ_PROJECT_TOKEN` for analysis operations; `GH_AW_WRITE_PROJECT_TOKEN` for
  write operations."
- **Confidence**: settled (first-party; the recommended secret names and their purpose
  are explicit)
- **Quote**: "`GH_AW_READ_PROJECT_TOKEN` for analysis operations; `GH_AW_WRITE_PROJECT_TOKEN`
  for write operations"
- **Our assessment**: The dual-token layout adds a second layer of least-privilege beyond
  the Safe Outputs architecture. In most gh-aw patterns, permission separation is achieved
  at the Safe Outputs level (AI job has no write access; write job executes pre-approved
  operations). ProjectOps adds token-level separation: even if the Safe Outputs layer were
  bypassed, the read token would be insufficient for write operations and vice versa. This
  is defense-in-depth at the credential layer. The naming convention
  (`GH_AW_READ_PROJECT_TOKEN` / `GH_AW_WRITE_PROJECT_TOKEN`) is also a documentation
  choice — it makes the purpose of each secret self-evident in the frontmatter. For Ch02:
  document the dual-token layout as the ProjectOps credential pattern. For Ch03 (Safety
  and Verification): present it as an example of defense-in-depth extending beyond the
  five-layer model into credential architecture.

### Claim 5: Four Safe Output commands exist specifically for project operations: `update-project`, `create-project-status-update`, `create-project`, and `add-comment`

- **Evidence**: The Safe Outputs Layer description: "`update-project` — for adding
  issues/PRs and modifying fields; `create-project-status-update` — for stakeholder-facing
  summaries; `create-project` — for bootstrapping new boards; `add-comment` — for
  decision explanations."
- **Confidence**: settled (first-party; the command names and purposes are explicit)
- **Quote**: "`update-project` — for adding issues/PRs and modifying fields;
  `create-project-status-update` — for stakeholder-facing summaries"
- **Our assessment**: These are the controlled write surfaces for project board operations.
  The bounded write surface is important: the agent can only perform these four operations —
  it cannot delete project items, archive boards, or modify project settings. `update-project`
  is the workhorse (field modifications, adding issues/PRs); `create-project-status-update`
  is significant because it generates stakeholder-facing summaries, making the agent a
  communication actor, not just a board maintainer. `add-comment` here mirrors its use in
  IssueOps and ChatOps — a cross-cutting Safe Output for AI decision explanations. For Ch02:
  document these four commands as the ProjectOps write surface. For Ch03: present them as
  the boundary between the agent's read access and its write surface — agents cannot modify
  project fields without using `update-project`.

### Claim 6: The two-layer architecture (GitHub Tools for reads + Safe Outputs for writes) applies directly to project operations — the `projects` toolset enables board analysis; Safe Outputs execute changes

- **Evidence**: "ProjectOps combines two functional layers: **GitHub Tools Layer**
  (`tools.github` with `projects` toolset) handles project state reading and analysis.
  **Safe Outputs Layer** manages controlled write operations."
- **Confidence**: settled (first-party; the two-layer architecture is explicit in the
  YAML examples on the page)
- **Quote**: "GitHub Tools Layer (`tools.github` with `projects` toolset) handles project
  state reading and analysis."
- **Our assessment**: The `projects` toolset is a named capability in the `tools.github`
  MCP integration that adds Projects API read access. This extends the tool-layer
  configuration already documented in existing notes — the standard gh-aw frontmatter
  typically uses `toolsets: [default]` or `toolsets: [default, projects]`. The key
  implication: read access to project boards is additive (adding `projects` to the
  toolset), while write access requires both a separate token and Safe Output commands.
  This reinforces the "reads are easy, writes require explicit configuration" pattern
  seen across gh-aw patterns. For Ch02: document `toolsets: [default, projects]` as
  the frontmatter configuration for ProjectOps read access.

### Claim 7: Auto-apply is appropriate for low-risk maintenance tasks; suggestion-only for commitments affecting roadmap; explicit approval gates for cross-team or cross-repo impact

- **Evidence**: Best practices: "Auto-apply low-risk maintenance tasks (item addition,
  initial status/team assignment); Use suggestion-only mode for commitments (priority/
  date/iteration modifications); Gate cross-team or cross-repository impact through
  approval mechanisms."
- **Confidence**: emerging (design guidance from first-party; no measurement of risk
  categorization accuracy is provided)
- **Quote**: "Auto-apply low-risk maintenance tasks (item addition, initial status/team
  assignment). Use suggestion-only mode for commitments (priority/date/iteration
  modifications). Gate cross-team or cross-repository impact through approval mechanisms."
- **Our assessment**: This three-tier escalation model is the most actionable governance
  framework in the source. The taxonomy of risk tiers is valuable: tier 1 (item
  addition, initial status/team) is write-and-forget; tier 2 (priority, dates, iteration)
  affects planning commitments and needs human review; tier 3 (cross-team/cross-repo)
  affects multiple stakeholders and requires explicit approval. This maps cleanly onto
  the `docs-ghaw-how-they-work.md` Claim 10 pattern ("critical actions can require human
  approval") but provides the specific criteria for what qualifies as "critical" in the
  project management context. For Ch03 (Safety and Verification): add this three-tier
  framework as a template for write-risk classification in project automation.

### Claim 8: The field-contract pattern — enumerating exact allowed single-select values in the prompt — prevents field drift and silent write failures when agents modify project fields

- **Evidence**: Best practices: "Maintain exact single-select values to prevent field
  inconsistency." The Project Board Maintainer YAML example demonstrates this: the agent
  prompt specifies "Set structured fields only from allowed values: Status: Needs Triage |
  Proposed | In Progress | Blocked; Priority: Low | Medium | High; Team: Platform | Docs |
  Product."
- **Confidence**: settled (first-party; the YAML example explicitly enumerates field
  values in the prompt)
- **Quote**: "Set structured fields only from allowed values: Status: Needs Triage |
  Proposed | In Progress | Blocked"
- **Our assessment**: The field-contract pattern closes an important gap in project
  board automation: GitHub Projects single-select fields have predefined values, and
  attempting to set a non-existent value either silently fails or creates an error. By
  enumerating the allowed values in the agent's prompt instructions, the practitioner
  ensures the agent operates within the board's actual field schema. This is analogous
  to `add-labels: allowed:` in `docs-ghaw-issueops.md` Claim 3 (label allowlisting) —
  both patterns bound what the agent can write to a pre-enumerated set. The difference:
  label allowlisting is enforced by the Safe Outputs infrastructure; field-contract is
  enforced by the agent's prompt instructions (a softer bound). For Ch02: recommend
  including a complete field contract (all single-select fields with their allowed values)
  in any ProjectOps agent prompt. For Ch03: flag that field-contract is a prompt-level
  bound, not an infrastructure-level bound — unlike `allowed:` in `add-labels`.

### Claim 9: The gradual adoption path — start read-only for board analysis, then incrementally add targeted writes as confidence grows — is the recommended ProjectOps rollout sequence

- **Evidence**: Best practices: "Prefer GitHub's built-in Project workflows for simple
  event-based transitions." The Project Board Summarizer example (read-only, no Safe
  Outputs) is presented as the natural starting point before the Project Board Maintainer
  (write-enabled). The page notes this proves most valuable when "workflow confidence and
  policy maturity increase" — implying a maturity progression.
- **Confidence**: emerging (design recommendation from first-party; no data on adoption
  sequences is provided)
- **Quote**: (implicit in presenting the read-only Summarizer before the write-enabled
  Maintainer, and the framing around "judgment-intensive" vs. "rule-based" decisions)
- **Our assessment**: The staged adoption sequence (read-only analysis → targeted writes →
  broader automation) is consistent with the staged buildout pattern seen in
  `blog-gh-aw-operations-release-workflows.md` Claim 5 (metrics first, operations second,
  security third). For ProjectOps specifically: start with the Summarizer workflow to
  understand the agent's board analysis quality before trusting it with field modifications.
  For Ch05 (Team Adoption): document this gradual-confidence model. Teams rolling out
  ProjectOps should run read-only for at least a few weeks to calibrate agent judgment
  before enabling `GH_AW_WRITE_PROJECT_TOKEN` and `update-project` Safe Outputs.

### Claim 10: `max: 1` on `update-project` is the write-rate control for project field modifications — limiting how many project items can be modified per workflow run

- **Evidence**: The Project Board Maintainer YAML:
  ```yaml
  safe-outputs:
    update-project:
      github-token: ${{ secrets.GH_AW_WRITE_PROJECT_TOKEN }}
      project: https://github.com/orgs/my-mona-org/projects/1
      max: 1
    add-comment:
      max: 1
  ```
  Both `update-project` and `add-comment` carry `max: 1`.
- **Confidence**: settled (first-party; the YAML is explicit)
- **Quote**: (from YAML artifact)
- **Our assessment**: `max: 1` on `update-project` is conservative write-rate limiting —
  each workflow run can modify only one project item. This prevents runaway writes (e.g.,
  if an issue storm triggers many simultaneous IssueOps workflows, each one is bounded to
  one project update). The `max: 1` on `add-comment` is consistent with the same pattern
  seen in IssueOps (`docs-ghaw-issueops.md` Claim 2) and LabelOps notes — `max:` is the
  universal Safe Output volume-control mechanism. For Ch02: `max: 1` is a safe starting
  value for `update-project` in a new ProjectOps deployment; increase only after
  validating agent judgment at lower volumes.

## Concrete Artifacts

### Project Board Summarizer — Read-Only Analysis Workflow

```yaml
---
on:
  schedule:
    - cron: "0 14 * * 1"
permissions:
  contents: read
  actions: read
tools:
  github:
    github-token: ${{ secrets.GH_AW_READ_PROJECT_TOKEN }}
    toolsets: [default, projects]
---
# Project Board Summarizer
Review [project 1](https://github.com/orgs/my-mona-org/projects/1).
Return only:
- New this week
- Blocked + why
- Stale/inconsistent fields
- Top 3 human actions

Read-only. Do not update the project.
```

*Source: gh-aw ProjectOps patterns documentation, "Project Board Summarizer" example.
Note: Uses `GH_AW_READ_PROJECT_TOKEN` (not `GITHUB_TOKEN`) with `toolsets: [default, projects]`.
No Safe Outputs block — purely analytical.*

### Project Board Maintainer — Write-Enabled Issue Triage Workflow

```yaml
---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  actions: read
tools:
  github:
    github-token: ${{ secrets.GH_AW_READ_PROJECT_TOKEN }}
    toolsets: [default, projects]
safe-outputs:
  update-project:
    github-token: ${{ secrets.GH_AW_WRITE_PROJECT_TOKEN }}
    project: https://github.com/orgs/my-mona-org/projects/1
    max: 1
  add-comment:
    max: 1
---
# Intelligent Issue Triage
Analyze each new issue in this repository and decide whether it belongs on the project board.
Set structured fields only from allowed values:
- Status: Needs Triage | Proposed | In Progress | Blocked
- Priority: Low | Medium | High
- Team: Platform | Docs | Product

Post a short comment on the issue explaining your routing decision and any uncertainty.
```

*Source: gh-aw ProjectOps patterns documentation, "Project Board Maintainer" example.
Key: read token in `tools.github`, separate write token in `safe-outputs.update-project`.
Field contract enumerated directly in prompt instructions.*

### Authentication Requirements Summary

```
User-Owned Projects:
  Token type:   Classic PAT
  Scopes:       project + repo (if private repos involved)
  Storage:      Repository secret (e.g., GH_AW_READ_PROJECT_TOKEN)

Org-Owned Projects:
  Token type:   Fine-grained PAT or GitHub App token
  Config:       Resource owner = organization
                Repository access = specified repos
                Repo permissions: Contents Read (+ optional Issues/PR)
                Org permissions:  Projects Read (read-only)
                                  Projects Read and write (write-enabled)
  Storage:      Repository secret (split: read token + write token)

IMPORTANT: GITHUB_TOKEN is repository-scoped and CANNOT access Projects API.
Any ProjectOps workflow will fail authentication if it attempts to use
GITHUB_TOKEN for project operations.
```

*Source: gh-aw ProjectOps patterns documentation, "Authentication Requirements" section*

### Dual-Token Secret Configuration

```yaml
# In workflow frontmatter (read operations):
tools:
  github:
    github-token: ${{ secrets.GH_AW_READ_PROJECT_TOKEN }}
    toolsets: [default, projects]

# In workflow frontmatter (write operations via Safe Outputs):
safe-outputs:
  update-project:
    github-token: ${{ secrets.GH_AW_WRITE_PROJECT_TOKEN }}
    project: https://github.com/orgs/OWNER/projects/PROJECT_NUMBER
    max: 1
```

*Source: gh-aw ProjectOps patterns documentation, implied by dual-secret convention*

### Three-Tier Write-Gate Model

```
Tier 1 — Auto-apply (low risk, no human review):
  Operations:  Item addition, initial Status/Team assignment
  Rationale:   Hygiene operations; easily corrected; narrow impact
  Config:      update-project with max: 1 (or low value)

Tier 2 — Suggest-only (commitments; human reviews before apply):
  Operations:  Priority modification, Target Date, Iteration assignment
  Rationale:   Affects planning commitments; stakeholder expectations
  Config:      Safe Output proposal + human approval before execution

Tier 3 — Explicit approval gate (high impact):
  Operations:  Cross-team routing, cross-repo impact, board restructuring
  Rationale:   Multiple stakeholders; reversing mistakes is costly
  Config:      Approval mechanism required (issue comment, PR, etc.)
```

*Source: gh-aw ProjectOps best practices documentation*

### Field-Contract Pattern (from Project Board Maintainer example)

```
Pattern: enumerate allowed single-select values in the agent's prompt instructions.

Example:
  Set structured fields only from allowed values:
  - Status: Needs Triage | Proposed | In Progress | Blocked
  - Priority: Low | Medium | High
  - Team: Platform | Docs | Product

Why: GitHub Projects single-select fields reject values not in the field schema.
     An agent attempting to set "Status: Reviewing" when the board has no such
     option will silently fail or produce an error. The field contract bounds the
     agent to values that exist.

Note: This is a prompt-level constraint, not an infrastructure-level constraint
      like add-labels: allowed: in IssueOps. The agent could still attempt an
      out-of-contract value if it ignores the instruction.
```

*Source: gh-aw ProjectOps patterns documentation, Project Board Maintainer YAML example*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claims 4–5 (no write access by default; Safe Outputs as
    permission-separated state mutation): ProjectOps is a direct instantiation of both.
    The AI job uses `contents: read` + `actions: read`; all project writes go through
    `update-project` and `add-comment` Safe Outputs. Both sources fully consistent; this
    note provides the Projects API-specific instantiation.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human approval):
    Claim 7 in this note operationalizes that principle for project operations — the
    three-tier write-gate model specifies exactly what qualifies as "critical" in the
    project management context (cross-team, cross-repo, roadmap commitments).
  - `docs-ghaw-issueops.md` Claim 3 (`add-labels: allowed:` for label allowlisting):
    The field-contract pattern (Claim 8 here) is the ProjectOps analog — both bound the
    agent to a pre-enumerated set of allowed values. The mechanisms differ (Safe Outputs
    infrastructure vs. prompt instructions), but the security intent is the same.
  - `docs-ghaw-issueops.md` Claims 1, 2 (read-only AI job permissions; `add-comment` with
    `max:` for volume control): the Project Board Maintainer workflow uses the same
    structural pattern — `contents: read`, `actions: read` for the AI job, `add-comment`
    with `max: 1` for the comment write. ProjectOps and IssueOps share the same safe
    comment pattern but have different primary write operations.
  - `docs-ghaw-labelops.md`, `docs-ghaw-chatops.md`, `docs-ghaw-dailyops.md` (Safe Outputs
    `max:` as universal volume-control mechanism): `max: 1` on `update-project` and
    `add-comment` (Claim 10) is consistent with how `max:` is used across all gh-aw
    trigger patterns.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs concept): this note extends the
    base Safe Outputs concept with four project-specific commands not documented in
    `docs-ghaw-how-they-work.md`: `update-project`, `create-project-status-update`,
    `create-project`, `add-comment` (in ProjectOps context). The base concept covers the
    mechanism; this note covers the project management write surface.
  - `docs-ghaw-issueops.md` (IssueOps for issue triage): IssueOps handles the issue at
    creation time (triage, labeling, initial comment). ProjectOps extends the agent's
    action to the project board — routing the issue onto the board, setting project fields,
    and posting a decision comment. The two patterns can work in tandem: IssueOps fires
    first (on issue creation), ProjectOps can fire second (populating the project board).
    Together they form a complete automated triage pipeline from issue filing to board
    placement.
  - `blog-gh-aw-operations-release-workflows.md` (operations workflow patterns): that note
    covers release automation (Changeset Generator, Daily Workflow Updater). ProjectOps
    extends the "operations" category to project board management — a different domain but
    the same Safe Outputs + controlled-writes pattern.
  - `docs-ghaw-agentic-authoring.md` (authoring lifecycle): the Project Board Summarizer
    and Maintainer YAMLs are concrete examples of the authoring patterns documented there.
    The Summarizer follows the read-only pattern; the Maintainer follows the Safe Outputs
    write pattern.

- **Contradicts**: None. No existing source note makes claims that contradict the
  authentication requirements, dual-token layout, three-tier write-gate model, or
  field-contract pattern described here. The Safe Outputs architecture is consistent
  with `docs-ghaw-how-they-work.md`. No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **GITHUB_TOKEN authentication gap for Projects API** (Claim 2): No prior corpus note
    documents that `GITHUB_TOKEN` cannot access the GitHub Projects API. This is a concrete
    harness engineering gotcha — practitioners who assume `GITHUB_TOKEN` works for all
    gh-aw operations will encounter silent auth failures on ProjectOps deployments.
  - **Dual-token layout at credential level** (Claims 3–4): The
    `GH_AW_READ_PROJECT_TOKEN` / `GH_AW_WRITE_PROJECT_TOKEN` split is new to the corpus.
    Prior notes document permission separation at the Safe Outputs layer; this note adds
    token-level credential separation as an additional defense-in-depth measure.
  - **Three-tier write-gate escalation model** (Claim 7): No prior corpus note provides
    a structured three-tier framework for scoping agent write authority by risk level
    in a project management context. `docs-ghaw-how-they-work.md` Claim 10 names
    human approval as an option for critical actions; this note provides the criteria
    for classifying actions across three tiers.
  - **Field-contract pattern for single-select fields** (Claim 8): No prior corpus note
    documents the pattern of enumerating allowed field values in the agent's prompt to
    prevent out-of-schema writes. The analogous infrastructure-level constraint
    (`add-labels: allowed:`) exists in IssueOps, but the prompt-level field-contract
    for project fields is new.
  - **Project-specific Safe Output commands** (Claim 5): `update-project`,
    `create-project-status-update`, and `create-project` are new to the corpus. Prior
    notes cover `add-comment`, `add-labels`, `create-pull-request-review-comment`, and
    other Safe Outputs — but not project board management commands.
  - **Agent-vs-automation decision rubric for project boards** (Claim 1): No prior note
    provides a specific rubric for deciding between GitHub built-in project automations
    and ProjectOps. The "judgment-intensive vs. rule-based" criterion is an actionable
    decision signal not documented elsewhere.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add ProjectOps to the "when to use agents vs. automations" decision guide** (Claim 1):
  The rubric — judgment-intensive routing and field modifications → ProjectOps; simple
  rule-based transitions → GitHub built-in automations — is a crisp practitioner signal.
  Pair with the IssueOps vs. DailyOps decision guide in `docs-ghaw-issueops.md` Claim 8
  to give teams a complete trigger selection framework.
- **Document the IssueOps + ProjectOps triage pipeline** (Claims 1, 6): IssueOps fires
  on issue creation for initial classification; ProjectOps extends to board placement and
  field assignment. Together they form an automated triage pipeline. Recommend running
  both in tandem for teams that use GitHub Projects as their primary planning layer.

### Chapter 02: Harness Engineering

- **Document the GITHUB_TOKEN exception for Projects API** (Claim 2): This is a
  practitioner gotcha that deserves explicit coverage. Any `tools.github` frontmatter
  targeting the Projects API must use `GH_AW_READ_PROJECT_TOKEN` (not `GITHUB_TOKEN`).
  Any `safe-outputs.update-project` block must use `GH_AW_WRITE_PROJECT_TOKEN`. Make
  this prominent — it is counterintuitive for practitioners who have used `GITHUB_TOKEN`
  successfully in all other gh-aw patterns.
- **Document the dual-token layout as the ProjectOps credential pattern** (Claims 3–4):
  Extend the harness credential section with the two-path setup (user-owned vs.
  org-owned projects, classic PAT vs. fine-grained PAT/GitHub App token) and the
  dual-secret naming convention.
- **Document `toolsets: [default, projects]` as the read-access frontmatter for ProjectOps**
  (Claim 6): The Projects toolset is an additive capability that must be explicitly
  enabled. Contrast with standard `toolsets: [default]`.
- **Add `max: 1` as the recommended starting value for `update-project`** (Claim 10):
  Conservative write-rate limiting while validating agent judgment on the board.

### Chapter 03: Safety and Verification

- **Add three-tier write-gate model as a write-risk classification framework** (Claim 7):
  Extend the Safe Outputs section with the three-tier model: auto-apply (low-risk hygiene),
  suggest-only (planning commitments), explicit approval gate (cross-team/cross-repo impact).
  This operationalizes `docs-ghaw-how-they-work.md` Claim 10's "critical actions require
  human approval" into a concrete decision framework.
- **Present dual-token layout as defense-in-depth beyond Safe Outputs** (Claim 4):
  The five-layer security model in `docs-ghaw-how-they-work.md` covers permission
  separation at the workflow job level. The dual-token layout extends this to the
  credential layer — a sixth defense layer not in the original model. Document as a
  recommended extension for any workflow where read and write operations touch different
  APIs or permission scopes.
- **Distinguish field-contract (prompt-level) from `allowed:` (infrastructure-level)**
  (Claim 8): Ch03's Safe Outputs section should clarify: `add-labels: allowed:` is
  enforced by the Safe Outputs infrastructure (agent literally cannot apply labels
  outside the list); field-contract is enforced by the agent's prompt instructions
  (a softer bound — the agent could deviate if it ignores the instruction). Teams
  with strict write-control requirements should treat field-contract as advisory and
  add validation at the `update-project` level where possible.

### Chapter 05: Team Adoption

- **Document the gradual adoption sequence for ProjectOps** (Claim 9): Start with the
  Project Board Summarizer (read-only, `GH_AW_READ_PROJECT_TOKEN` only) to calibrate
  agent judgment on the board. Add the write-enabled Maintainer (with
  `GH_AW_WRITE_PROJECT_TOKEN` and `update-project`) only after validating read-only
  analysis quality. This is consistent with the staged buildout pattern across the
  gh-aw corpus.

## Extraction Notes

1. **Source confirmed live at extraction**: The page at
   https://github.github.com/gh-aw/patterns/project-ops/ returned HTTP 200 and
   complete content as of 2026-05-02. The Prospector triage comment confirms the source
   was live as of 2026-04-22.

2. **Rendering note**: The page is an Astro/Starlight-rendered SPA. The WebFetch-based
   extraction returned rendered text without JavaScript execution. Both YAML workflow
   examples (Project Board Summarizer and Project Board Maintainer) were fully captured.
   No interactive diagrams or video content was identified on this page.

3. **No publication date**: The documentation page does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with gh-aw platform state
   as of 2026-05-02, based on the Safe Outputs configuration syntax matching other
   recently extracted notes (IssueOps #326, LabelOps #327).

4. **Field-contract not followed for linked sub-pages**: The page references "Project
   Token Authentication patterns," "Safe Outputs Reference documentation," "Projects
   & Monitoring integration," and "IssueOps pattern implementation" as related
   documentation. These were not followed, as they are covered in existing source notes
   (`docs-ghaw-how-they-work.md`, `docs-ghaw-issueops.md`, `docs-ghaw-monitoring-patterns.md`).

5. **No contradictions filed**: Reviewed all existing source notes. No claims in this
   source materially oppose existing source notes at the MINER.md §4a threshold. The
   authentication requirements, dual-token layout, and three-tier write-gate model are
   all new to the corpus; they extend rather than contradict existing patterns.
