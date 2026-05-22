---
source_url: https://github.github.com/gh-aw/examples/multi-repo/code-quality-monitoring
source_type: docs
title: "GitHub Agentic Workflows Examples: Multi-Repo Code Quality Monitoring"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: emerging
issue: "#850"
---

# GitHub Agentic Workflows Examples: Multi-Repo Code Quality Monitoring

> Concrete practitioner walkthrough for implementing automated code quality
> monitoring from a side repository — documents the complete workflow YAML,
> fine-grained PAT scoping, the `current: true` working-directory footgun,
> multi-language linting orchestration (ESLint, flake8, complexity), and
> per-category issue aggregation rules that prevent noise in the target
> repository's tracker.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Examples" section —
  a worked end-to-end implementation of the side-repository pattern applied
  to the code quality monitoring use case. Distinct from the abstract
  "Patterns" reference pages; this page is a practitioner walkthrough with
  runnable configuration and explicit setup steps.)
- **Author credibility**: GitHub Agentic Workflows team — first-party examples
  from the same team behind the Peli de Halleux "Agent Factory" blog series
  and the `gh aw` CLI. YAML configurations and step-by-step setup instructions
  are authoritative for the gh-aw platform. The analysis commands (ESLint,
  flake8) are standard open-source tools used as examples; the specific
  thresholds (>5 errors, >10 errors, >500 lines) are opinionated defaults, not
  platform-enforced constraints.
- **Scope**: End-to-end code quality monitoring workflow using the side-repo
  pattern: repository creation, fine-grained PAT configuration, complete
  frontmatter YAML, multi-language analysis instructions, issue creation rules,
  and advanced variants (type checking, directory targeting, multi-repo
  comparison). Does NOT cover: the abstract MultiRepoOps design primitives (see
  `docs-ghaw-multi-repo-ops.md`), the monitoring pattern configuration options
  (`group-reports`, `noop`) documented in `docs-ghaw-monitoring-patterns.md`,
  or the general `checkout` reference (see `docs-ghaw-checkout-reference.md`).

## Extracted Claims

### Claim 1: The side-repository pattern keeps automation infrastructure entirely separate from the codebase it monitors, enabling code quality analysis without adding workflows, secrets, or dependencies to the target repository

- **Evidence**: Page overview section states the architectural intent explicitly;
  the workflow runs in a dedicated `my-org/main-repo-quality` side repo that
  checks out `my-org/main-repo` as a target.
- **Confidence**: emerging (first-party documentation with a concrete example;
  the isolation benefit is stated but not quantified with production metrics)
- **Quote**: "keeping automation infrastructure entirely separate from the codebase
  it monitors"
- **Our assessment**: The side-repo isolation is the defining characteristic of
  this pattern over simply adding a `code-quality.yml` workflow directly to the
  target repo. Isolation means: (1) the target repo has no knowledge of the
  monitoring setup; (2) the monitoring workflow's secrets, bash tool allowlists,
  and dependencies do not appear in the target repo's security surface; (3) the
  monitoring cadence and configuration can be changed without touching the target
  repo. This is the key architectural justification for accepting the additional
  complexity of cross-repo checkout and fine-grained token setup. For Ch02
  (Harness Engineering): document the side-repo pattern as the canonical approach
  for externally-owned quality monitoring workflows.

### Claim 2: Fine-grained PAT authentication for cross-repo code quality monitoring requires Contents:Read-only (for checkout) and Issues:Read & write (for issue creation) — no broader access is needed

- **Evidence**: "2. Create the Authentication Token" section provides a permissions
  table. The explicit token (`GH_AW_MAIN_REPO_TOKEN`) must be stored as a secret
  in the side repository (not the target), and passed explicitly to both
  `checkout.github-token` and `safe-outputs.github-token`.
- **Confidence**: settled (first-party documentation; the permission table is
  explicit and the scoping is deterministic for the described operations)
- **Quote**: (from permissions table on page: Contents: Read-only, Issues: Read & write)
- **Our assessment**: This is the minimum viable PAT scope for this use case —
  no write access to contents, no PR access, no admin access. It demonstrates
  the least-privilege principle from `docs-ghaw-multi-repo-ops.md` Claim 7
  applied to a concrete scenario: the side repo needs to read the target's code
  and write to its issue tracker, nothing more. The token must be set on both
  `checkout` AND `safe-outputs` — the page explicitly warns this cannot be the
  default `GITHUB_TOKEN`. For Ch03 (Safety and Verification): this PAT scope is
  the reference minimum for read-source / write-issues cross-repo workflows.

### Claim 3: The `checkout: current: true` field designates the issue-creation target repository for GitHub operations but does NOT automatically change the working directory — the prompt must include an explicit `cd` or the agent analyzes the wrong directory

- **Evidence**: Dedicated warning section "Important: `current: true` and Working
  Directory" on the page. The side repo is the default `$GITHUB_WORKSPACE`; after
  checkout with `current: true`, the agent starts in the side repo's directory
  unless explicitly directed to `cd ${{ github.workspace }}/repo`.
- **Confidence**: settled (first-party documentation; the warning is explicitly
  called out as a footgun, not an edge case)
- **Quote**: "`current: true` tells the agent which repository to treat as the
  primary target for GitHub operations (issue creation, PR references). It does
  **not** automatically change the working directory. Always include an explicit
  `cd` in the prompt: `cd ${{ github.workspace }}/repo`. Without it, the agent
  starts in `$GITHUB_WORKSPACE` (the side repo) and may analyze the wrong
  directory."
- **Our assessment**: This is the most operationally dangerous footgun in the
  workflow: a misconfigured or incomplete prompt causes the agent to run ESLint
  and flake8 against the side repo's (empty) workspace rather than the checked-out
  target repo — with no error, just wrong or empty results. The failure mode is
  silent: the agent would find zero issues (the side repo has no source files)
  and report success. For Ch02: document `current: true` + explicit `cd` as
  a required paired configuration in any side-repo workflow that performs local
  analysis. For Ch03: list as a silent failure footgun alongside the `GITHUB_TOKEN`
  cross-repo scope issue from `docs-ghaw-multi-repo-ops.md` Claim 3.

### Claim 4: The bash tool allowlist in the workflow frontmatter controls which package managers and linters the agent may invoke — `"npx:*"`, `"eslint:*"`, and `"pip:*"` enable the full multi-language analysis without granting unrestricted shell access

- **Evidence**: The complete frontmatter YAML shows `tools.bash` with three entries:
  `"npx:*"`, `"eslint:*"`, `"pip:*"`. The wildcard suffix permits any subcommand
  under those tool prefixes.
- **Confidence**: emerging (first-party YAML configuration; the exact semantics
  of bash tool allowlist entries are documented in the tools reference, not
  detailed here)
- **Quote**: (from YAML: `bash: ["npx:*", "eslint:*", "pip:*"]`)
- **Our assessment**: The explicit allowlist means the agent cannot invoke
  arbitrary bash commands — only the declared tool namespaces. This is the
  principle of least capability applied to the bash tool: the workflow declares
  exactly what analysis tools it needs, and the platform enforces that boundary.
  Teams adding new analysis tools (e.g., TypeScript's `tsc` for type checking,
  or `radon` for Python complexity) must extend this allowlist. For Ch02: document
  the bash tool allowlist as the sandboxing mechanism for code analysis workflows —
  specify only what you need.

### Claim 5: Multi-language code quality analysis orchestrates four categories: JavaScript/TypeScript ESLint scanning (>5 errors threshold), Python flake8 scanning (>10 errors threshold), file complexity by line count (>500 lines threshold), and Dependabot advisory checks via GitHub toolsets

- **Evidence**: Analysis directives listed in the agent prompt on the page:
  - JS/TS: `npx eslint . --format json --max-warnings 0`, flag files with >5 errors
  - Python: `pip install flake8 --quiet && flake8 . --count --statistics`, flag modules with >10 errors
  - Complexity: `find . -name "*.ts" -o -name "*.js" -o -name "*.py" | xargs wc -l | sort -rn`, flag files over 500 lines
  - Dependencies: "Check for packages with known security advisories using GitHub tools — look at open Dependabot alerts"
- **Confidence**: emerging (thresholds are explicitly stated but are opinionated
  defaults from the example, not platform-enforced limits)
- **Quote**: "flag modules with >10 flake8 errors" / "flag files over 500 lines — they are candidates for splitting"
- **Our assessment**: The four categories cover static analysis, runtime errors,
  structural complexity, and security advisories — a pragmatic baseline that avoids
  style nitpicking while catching real quality debt. The different thresholds for
  JS/TS (>5) vs. Python (>10) reflect realistic noise levels for the respective
  linters; flake8 is generally noisier on mixed codebases. For Ch02: these
  thresholds are a starting-point reference, not a specification. Teams should
  tune them based on their codebase's baseline error count before deploying.

### Claim 6: Issue creation follows per-category aggregation rules: one issue per distinct finding category (not one per file), with a minimum of 3 instances required before creating an issue, and a maximum of 10 issues per run enforced by `safe-outputs: create-issue: max: 10`

- **Evidence**: Two explicit rules from the agent prompt instructions: "Create
  **one issue per distinct finding category** (not one issue per file)." and
  "Skip findings with fewer than 3 instances — they are not worth the noise."
  The `max: 10` is in the safe-outputs config.
- **Confidence**: settled (first-party documentation; rules are stated explicitly
  in the prompt and config)
- **Quote**: "Create **one issue per distinct finding category** (not one issue
  per file)." / "Skip findings with fewer than 3 instances — they are not worth
  the noise."
- **Our assessment**: The three-part rule (per-category, ≥3 instances, ≤10 issues)
  is a carefully designed noise-prevention system. Per-file reporting would generate
  dozens of issues from a single ESLint run; per-category aggregation collapses
  them into one actionable issue with a list of affected files. The ≥3-instance
  threshold eliminates one-off findings that aren't systemic patterns. The `max: 10`
  cap from safe-outputs prevents runaway issue creation if the analysis surfaces
  more categories than expected. For Ch02: document this three-part rule as the
  canonical issue creation discipline for code analysis workflows — it applies
  equally to security scanning, performance analysis, and any other automated
  finding workflow.

### Claim 7: The agent prompt explicitly defines skip categories to prevent false positives: style preferences without an established linter rule, files with a `// quality-exempt` comment, and test files (`*.test.*`, `*.spec.*`, `__tests__/`)

- **Evidence**: Explicit exclusion list from the agent prompt: "Do not create
  issues for: Style preferences without an established linter rule, Files with
  a `// quality-exempt` comment, Test files (`*.test.*`, `*.spec.*`, `__tests__/`)"
- **Confidence**: settled (first-party documentation; rules are stated explicitly
  in the prompt)
- **Quote**: "Do not create issues for: Style preferences without an established
  linter rule, Files with a `// quality-exempt` comment, Test files (`*.test.*`,
  `*.spec.*`, `__tests__/`)"
- **Our assessment**: The escape hatch (`// quality-exempt`) is the most
  practically important element: it gives codebase owners a way to suppress
  monitoring alerts for files that are intentionally in a degraded state (e.g.,
  generated code, legacy files in gradual refactor). Without this escape hatch,
  automated quality issues would create friction against known technical debt
  that teams have decided to defer. The test file exclusion prevents noise from
  test utilities that intentionally violate production code standards. For Ch02:
  document the `// quality-exempt` escape hatch as a standard pattern for automated
  analysis workflows; it is the opt-out mechanism that makes automated enforcement
  sustainable.

### Claim 8: The workflow uses the `pull_requests` GitHub toolset (not just `issues`) to enable the agent to review recent merged PRs for recurring pattern analysis — a qualitative complement to quantitative linting

- **Evidence**: The frontmatter shows `tools.github.toolsets: [repos, pull_requests]`
  and the analysis instructions include: "Look at the last 10 merged PRs" for
  recurring issues like skipped tests or structural coupling.
- **Confidence**: emerging (first-party YAML configuration; the PR pattern analysis
  instruction is described but the specific fields queried are not enumerated)
- **Quote**: "Look at the last 10 merged PRs" (for recurring issues)
- **Our assessment**: Combining static linting with PR pattern review adds a
  qualitative dimension that linters cannot provide: recurring anti-patterns that
  individually pass linting but systematically degrade codebase quality (e.g.,
  every PR that adds new catch blocks empties them). The `pull_requests` toolset
  access is what enables the agent to read merged PR data without additional
  authentication. For Ch02: document the toolset pairing (`repos` + `pull_requests`)
  as the standard configuration when the workflow needs both code content access
  and change-history access for pattern analysis.

### Claim 9: The `GITHUB_TOKEN` cannot access external repositories — the explicit fine-grained PAT must be set on both `checkout.github-token` and `safe-outputs.github-token` or cross-repo operations silently fail

- **Evidence**: Warning callout on the page: "The default `GITHUB_TOKEN` cannot
  access other repositories. The explicit token must be set on both `checkout`
  and `safe-outputs`."
- **Confidence**: settled (first-party documentation; consistent with
  `docs-ghaw-multi-repo-ops.md` Claim 3)
- **Quote**: "The default `GITHUB_TOKEN` cannot access other repositories. The
  explicit token must be set on both `checkout` and `safe-outputs`."
- **Our assessment**: This is the same `GITHUB_TOKEN` cross-repo restriction
  documented in `docs-ghaw-multi-repo-ops.md` Claim 3, presented here in the
  concrete context of code quality monitoring. The two-location requirement
  (`checkout` AND `safe-outputs`) is easy to miss — a workflow author who sets
  the token only on `checkout` will successfully check out the target repo but
  fail to create issues in it. The failure mode on `safe-outputs` without a
  token depends on the platform's error handling, but the page frames it as
  silent failure. For Ch03: this is a required pre-flight checklist item for any
  side-repo workflow that both reads from and writes to a target repository.

### Claim 10: Advanced variants extend the base pattern: TypeScript type checking adds `tsc --noEmit` to the bash tools, directory targeting uses `path:` parameter with explicit subdirectory navigation, and multi-repo comparison checks out multiple repositories for cross-repo analysis

- **Evidence**: "Customization Options" section documents three extension patterns:
  type checking (add TypeScript compiler to bash tools and prompt), directory
  targeting (`path:` parameter for specific subdirectories), and multiple
  repositories (multiple checkout entries, one with `current: true` designating
  the issue creation target).
- **Confidence**: emerging (first-party documentation; extension patterns are
  described at a high level without complete YAML examples for each variant)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The multi-repo comparison variant is the most architecturally
  significant extension: when multiple `checkout` entries are configured, the
  agent can perform cross-repo comparisons (e.g., comparing shared library versions
  across services, or checking that configuration files are consistent across
  microservices). The single `current: true` designation means issue creation
  targets one repo regardless of how many repos are checked out. The directory
  targeting variant is important for monorepos where only a subset of the codebase
  should be analyzed. For Ch06 (Orchestration and Multi-Agent Coordination):
  the multi-repo comparison variant represents a cross-repo analysis topology
  that complements the hub-and-spoke and upstream-to-downstream topologies in
  `docs-ghaw-multi-repo-ops.md` Claims 4–5.

## Concrete Artifacts

### Complete Workflow YAML Configuration

From the page's "Workflow File" section. File location: `.github/workflows/code-quality.yml`
in the side repository.

```yaml
---
on: weekly on monday
permissions:
  contents: read
checkout:
  repository: my-org/main-repo
  github-token: ${{ secrets.GH_AW_MAIN_REPO_TOKEN }}
  path: repo
  current: true
tools:
  github:
    github-token: ${{ secrets.GH_AW_MAIN_REPO_TOKEN }}
    toolsets: [repos, pull_requests]
  bash:
    - "npx:*"
    - "eslint:*"
    - "pip:*"
safe-outputs:
  github-token: ${{ secrets.GH_AW_MAIN_REPO_TOKEN }}
  create-issue:
    target-repo: "my-org/main-repo"
    title-prefix: "[quality] "
    labels: [code-quality, automation]
    max: 10
---
```

*Source: gh-aw examples, "Code Quality Monitoring — Workflow Configuration" section*

### Side Repository Setup Commands

From the page's "Setup Requirements" section.

```bash
# 1. Create and clone the side repository
gh repo create my-org/main-repo-quality --private
gh repo clone my-org/main-repo-quality
cd main-repo-quality

# 2. Store the fine-grained PAT as a secret in the SIDE repo
gh secret set GH_AW_MAIN_REPO_TOKEN
```

*Source: gh-aw examples, "Code Quality Monitoring — Setup Requirements" section*

### Fine-Grained PAT Permission Scope

From the page's "Create the Authentication Token" section.

```
Token name: GH_AW_MAIN_REPO_TOKEN
Scoped to: my-org/main-repo (the TARGET repository, not the side repo)

Required permissions:
  Contents:  Read-only    (for checkout)
  Issues:    Read & write (for issue creation)
```

*Source: gh-aw examples, "Code Quality Monitoring — Authentication Token" section*

### Agent Prompt Analysis Instructions

From the page's workflow prompt section.

```
# Code Quality Analysis

cd ${{ github.workspace }}/repo  [REQUIRED — see current: true footgun]

JavaScript/TypeScript:
  Run: npx eslint . --format json --max-warnings 0
  Flag: Files with >5 ESLint errors (immediate fix), missing error handling
        (catch(e) {}, empty catch blocks), unused imports accumulating across files

Python:
  Run: pip install flake8 --quiet && flake8 . --count --statistics
  Flag: Modules with >10 flake8 errors

Complexity:
  Run: find . -name "*.ts" -o -name "*.js" -o -name "*.py" | xargs wc -l | sort -rn
  Flag: Files over 500 lines — candidates for splitting

Dependencies:
  Use GitHub tools — look at open Dependabot alerts for known security advisories

PR Patterns:
  Look at the last 10 merged PRs for recurring issues (skipped tests, structural coupling)

Issue creation rules:
  - One issue per distinct finding CATEGORY (not per file)
  - Skip findings with fewer than 3 instances
  - Maximum: 10 issues per run (enforced by safe-outputs max)
  - Severity: High/Medium/Low with actionable remediation steps

DO NOT create issues for:
  - Style preferences without an established linter rule
  - Files with a // quality-exempt comment
  - Test files (*.test.*, *.spec.*, __tests__/)
```

*Source: gh-aw examples, "Code Quality Monitoring — Agent Prompt Instructions" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 3 ("The default `GITHUB_TOKEN` only has
    access to the current repository."): Claim 9 above reproduces the same
    restriction in the specific context of side-repo code quality monitoring.
    The two notes together give the same footgun from two angles: the abstract
    pattern reference (MultiRepoOps) and a concrete use-case example.
  - `docs-ghaw-multi-repo-ops.md` Claim 7 (PAT scope: read on source, write on
    target only): Claim 2 above is a concrete instantiation of this guidance —
    Contents:Read-only on the target is the "read on source" part; Issues:Read &
    write is the "write on target" part. This example confirms the least-privilege
    scoping recommended in the patterns reference.
  - `docs-ghaw-multi-repo-ops.md` Claim 8 (GitHub App tokens preferred over PATs
    for per-job minting and automatic revocation): The source page's security
    enhancement note aligns: "For enhanced security, use a GitHub App token —
    minted on demand and automatically revoked after each job."
  - `docs-ghaw-monitoring-patterns.md` Claim 4 (`title-prefix` + labels for
    searchable, filterable failure issues): The `title-prefix: "[quality] "` and
    `labels: [code-quality, automation]` in this workflow's safe-outputs config
    follow the same naming convention documented there for failure reporting.
    Both patterns use title prefix + labels to make automated issues filterable
    in the issue tracker.

- **Extends**:
  - `docs-ghaw-multi-repo-ops.md`: That note documents the `target-repo`
    safe-output primitive and three topology archetypes (hub-and-spoke,
    upstream-to-downstream, org-wide broadcast) abstractly. This example is a
    complete practitioner walkthrough of the side-repo variant (a fourth topology:
    monitor → target, one-directional): the side repo checks out, analyzes, and
    writes findings to the target. It provides the `current: true` + explicit `cd`
    paired pattern not documented in the abstract reference.
  - `docs-ghaw-monitoring-patterns.md`: That note covers monitoring configuration
    primitives (`update-project`, `group-reports`, `noop`, operational CLI). This
    example provides the end-to-end code quality monitoring use case — a concrete
    scenario for those configuration options. The issue creation strategy here
    (per-category, ≥3 instances, `max: 10`) is complementary to the
    `group-reports: true` pattern documented in `docs-ghaw-monitoring-patterns.md`
    Claim 5 for grouping failure reports.
  - `docs-ghaw-multi-repo-issue-tracking.md`: That note covers eight cross-repo
    issue-tracking workflow patterns. This note covers a related but distinct use
    case: automated code analysis feeding issue creation, rather than issue-event
    propagation. Both use `create-issue: target-repo` but for different trigger
    types (scheduled vs. event-driven).

- **Contradicts**: None identified. The PAT scope guidance (Contents: Read-only,
  Issues: Read & write) is consistent with — and a concrete demonstration of —
  the least-privilege guidance in `docs-ghaw-multi-repo-ops.md` Claim 7. No
  contradiction issue filed.

- **Novel**:
  - **`current: true` working-directory footgun documented explicitly** (Claim 3):
    No existing source note documents the `current: true` behavior as a footgun
    in the checkout context. `docs-ghaw-multi-repo-ops.md` uses `current: true`
    in its Deterministic Multi-Repo Checkout artifact (Concrete Artifacts section)
    but does not call out the silent-failure risk from missing the `cd`. This is
    the first corpus entry with an explicit warning.
  - **Bash tool allowlist pattern for multi-language analysis** (Claim 4): The
    `bash: ["npx:*", "eslint:*", "pip:*"]` allowlist as a sandboxing mechanism
    for analysis workflows is not documented in any existing corpus note. The
    wildcard suffix (`*`) and the multi-namespace pattern are new.
  - **Per-category aggregation with ≥3-instance threshold** (Claim 6): The
    three-part rule (per-category, ≥3 instances, `max: 10`) for automated
    finding issue creation is not documented in any existing source note. Prior
    notes document `max:` on safe-outputs but not the per-category aggregation
    strategy or instance threshold.
  - **Explicit skip categories with escape hatch** (Claim 7): The `// quality-exempt`
    escape hatch comment pattern, the test file exclusion, and the no-linter-rule
    style exclusion are not documented anywhere in the corpus. This is the first
    source documenting an opt-out mechanism for automated code analysis.
  - **`pull_requests` toolset for merged PR pattern analysis** (Claim 8): Using
    the `pull_requests` GitHub toolset to review merged PR history as a qualitative
    analysis complement to quantitative linting is not documented in any existing
    corpus note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the side-repo pattern as the canonical approach for externally-owned
  quality monitoring** (Claim 1): The architectural justification (infrastructure
  isolation, no target-repo secrets exposure, independent configuration lifecycle)
  should be documented as the primary reason to prefer a side repo over adding
  quality workflows directly to the target. Cross-reference the MultiRepoOps
  pattern for the underlying mechanics.

- **Document `current: true` + explicit `cd` as a required paired configuration**
  (Claim 3): Any workflow using `checkout.current: true` for side-repo analysis
  must include `cd ${{ github.workspace }}/<path>` as the first action in the
  agent prompt. Document as a footgun with a silent failure mode (wrong-directory
  analysis produces empty or zero-finding results without errors).

- **Add bash tool allowlist as the sandboxing pattern for analysis workflows**
  (Claim 4): The `bash: ["npx:*", "eslint:*", "pip:*"]` pattern demonstrates
  least-capability enforcement for the bash tool. Ch02 should document the
  wildcard allowlist syntax and recommend declaring only the tool namespaces
  needed for the specific workflow's analysis.

- **Add per-category aggregation + instance threshold as the standard issue
  creation discipline** (Claim 6): The three-part rule (one issue per finding
  category, ≥3 instances, `max: N`) should be the recommended pattern for any
  workflow that creates issues from automated analysis. Without it, a single
  linter run can flood the issue tracker. Cross-reference the `group-reports`
  config from `docs-ghaw-monitoring-patterns.md` for the complementary failure
  aggregation pattern.

- **Add `// quality-exempt` escape hatch as the opt-out pattern** (Claim 7):
  Document as a required element for automated enforcement sustainability —
  without an escape hatch, teams route around automated issues by ignoring them
  entirely.

### Chapter 03: Safety and Verification

- **Add `current: true` silent failure to the cross-repo footgun checklist**
  (Claim 3): Alongside the `GITHUB_TOKEN` cross-repo scope restriction (Claim 9,
  corroborated by `docs-ghaw-multi-repo-ops.md` Claim 3), add the missing `cd`
  footgun: the agent analyzes the side repo's empty workspace instead of the
  target repo's code, producing misleading zero-finding results.

- **Add fine-grained PAT scope as the reference minimum for read-source /
  write-issues workflows** (Claim 2): Contents:Read-only + Issues:Read & write
  is the concrete least-privilege scope for this use case. Pair with the abstract
  "read on source, write on target" guidance from `docs-ghaw-multi-repo-ops.md`
  Claim 7.

### Chapter 06: Orchestration and Multi-Agent Coordination

- **Add multi-repo comparison as a fourth analysis topology** (Claim 10): The
  multi-checkout variant (multiple `checkout` entries, one `current: true`) enables
  cross-repo comparison analysis — checking configuration consistency, shared
  library version alignment, or API contract conformance across services. Document
  alongside the hub-and-spoke, upstream-to-downstream, and org-wide broadcast
  topologies from `docs-ghaw-multi-repo-ops.md` Claims 4–6.

## Extraction Notes

1. **WebFetch made three passes**: Three separate fetches were performed to
   capture verbatim content. YAML configuration and prompt instructions were
   consistent across passes. All direct quotes in this note are verbatim from
   the source page.

2. **Threshold values are opinionated defaults, not platform limits**: The >5
   ESLint errors, >10 flake8 errors, and >500 lines thresholds are the example's
   suggested starting points. The page does not present these as gh-aw platform
   constraints — they are prompt instructions that practitioners should tune to
   their codebase's baseline.

3. **`current: true` in `checkout` vs. `target-repo` in `safe-outputs`**: These
   are two separate fields with related but distinct meanings. `current: true` in
   `checkout` designates the primary repository context for the agent's GitHub
   operations; `target-repo` in `safe-outputs` routes specific safe output actions
   to a different repository. In this workflow, both point to the same repo
   (`my-org/main-repo`), but they can diverge in multi-checkout scenarios.

4. **No publication date**: The page does not carry an explicit publication date.
   Content is consistent with gh-aw platform behavior as of 2026-05-22.

5. **Sub-pages not followed**: The "For enhanced security" note links to
   `/gh-aw/reference/auth/#using-a-github-app-for-authentication`. This was not
   fetched as it is an auth reference page already partially covered in
   `docs-ghaw-multi-repo-ops.md` Claims 7–8. No new content was expected.

6. **No contradictions filed**: Reviewed `docs-ghaw-multi-repo-ops.md`,
   `docs-ghaw-monitoring-patterns.md`, `docs-ghaw-multi-repo-issue-tracking.md`,
   and `docs-ghaw-checkout-reference.md`. No claims in this source materially
   oppose existing source notes. No contradiction issue filed.
