---
source_url: https://github.github.com/gh-aw/reference/triggering-ci
source_type: docs
title: "GitHub Agentic Workflows: Triggering CI Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-26
last_checked: 2026-05-26
status: current
confidence_overall: emerging
issue: "#417"
---

# GitHub Agentic Workflows: Triggering CI Reference

> Authoritative reference for a common agentic-workflow integration gap: PRs created
> by agents using the default `GITHUB_TOKEN` do not trigger CI — documents four
> concrete solutions (PAT, GitHub App, magic secret, full token override), their
> security tradeoffs, and the CLI commands to configure them.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/triggering-ci` page — a
  focused reference entry in the same `reference/` section as `reference/permissions`
  covered by `docs-ghaw-permissions-reference.md` and `reference/safe-outputs-specification`
  covered by `docs-ghaw-safe-outputs-specification.md`. Reference pages document platform
  behavior and configuration authoritatively.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same team
  behind Peli de Halleux's agent factory blog series and the `gh aw` CLI platform. Claims
  about GitHub Actions token behavior and Safe Outputs configuration fields are authoritative
  for the platform.
- **Scope**: The complete solution set for triggering CI on agent-created PRs — why the
  default fails, and four options to fix it. Applies to both the `create-pull-request` and
  `push-to-pull-request-branch` safe outputs. Does NOT cover: general token setup
  (`reference/auth`), the full Safe Outputs configuration model
  (`reference/safe-outputs-specification`), or how to read CI check results once they run
  (covered by the `checks` MCP tool in `blog-ghaw-weekly-2026-04-06.md` Claim 5).

## Extracted Claims

### Claim 1: By default, PRs created using the standard `GITHUB_TOKEN` in GitHub Actions do not trigger CI workflow runs — a deliberate GitHub platform restriction to prevent event cascades

- **Evidence**: Opening architectural fact on the page, applying explicitly to both
  `create-pull-request` and `push-to-pull-request-branch` safe outputs.
- **Confidence**: settled (first-party documentation of a well-known GitHub Actions
  platform behavior; the event-cascade rationale is GitHub's documented design intent)
- **Quote**: "By default, pull requests created using the default `GITHUB_TOKEN` in
  GitHub Actions do not trigger CI workflow runs. This is a GitHub Actions feature to
  prevent event cascades."
- **Our assessment**: This is the foundational gap that makes CI triggering a non-trivial
  concern for agentic workflows. An agent that creates a PR via `create-pull-request` will
  produce a PR with no CI checks unless explicitly configured — reviewers who rely on CI
  verdicts to make merge decisions cannot trust the CI state on agent-created PRs. For Ch02
  (Harness Engineering): any agentic workflow that creates PRs for human review must
  explicitly configure CI triggering or risk a gap where the CI gate is silently absent.
  For Ch03 (Safety and Verification): a PR without CI checks is a verification gap — the
  human reviewer has no automated signal about code correctness.

### Claim 2: The `github-token-for-extra-empty-commit` field is the least-privilege CI-trigger mechanism — it pushes an empty commit to the PR branch after creation using a narrow-scoped token, triggering `push` and `pull_request` events normally

- **Evidence**: Mechanism documented precisely on the page, with the token semantics and
  trigger events stated explicitly. Supported on both `create-pull-request` and
  `push-to-pull-request-branch` safe outputs.
- **Confidence**: settled (first-party documentation; the mechanism is described precisely
  with its trigger semantics)
- **Quote**: "the token will be used to push an extra empty commit to the PR branch after
  PR creation. This will trigger `push` and `pull_request` events normally."
- **Our assessment**: The empty-commit approach is architecturally minimal: a separate token
  is used only to push one empty commit — no additional permission scope beyond
  `Contents: Read & Write` is needed, the commit content is empty (no code risk), and the
  event triggers are the standard GitHub CI events (`push`, `pull_request`). This is a
  narrower permission footprint than the full token override approach (Claim 6), which
  changes the PR author and triggers CI directly but grants broader permissions. For Ch02:
  recommend `github-token-for-extra-empty-commit` as the default CI trigger approach —
  it minimizes the token's permission scope while achieving the CI trigger goal.

### Claim 3: A fine-grained PAT with only `Contents: Read & Write` scoped to the relevant repositories is the minimum credential for CI triggering via the extra-empty-commit approach

- **Evidence**: The PAT instructions are explicit, with a pre-filled GitHub link for
  creating the PAT with the correct name, description, and Contents permission.
- **Confidence**: settled (first-party documentation; the minimum scope is explicitly stated)
- **Quote**: "Create a fine-grained PAT... with `Contents: Read & Write` scoped to the
  relevant repositories where pull requests will be created."
- **Our assessment**: The `Contents: Read & Write` scope is the minimum because pushing an
  empty commit requires write access to repository contents. Fine-grained PATs allow
  repository-level scoping — the token can be restricted to only the repositories that
  receive agent-created PRs, not the broader organization. For Ch02: when configuring CI
  triggering, prefer fine-grained PATs over classic PATs for least-privilege. For Ch03: the
  `Contents: Read & Write` scope is worth naming explicitly — it is less obvious than a
  `pull-requests: write` token for a "CI triggering" use case; practitioners may over-scope
  by instinct.

### Claim 4: The magic secret `GH_AW_CI_TRIGGER_TOKEN` provides zero-configuration CI triggering — gh-aw auto-detects this named secret without requiring explicit workflow YAML changes

- **Evidence**: The page describes this as the simplest approach, stated in the Note box
  at the top of the page and elaborated in a dedicated section.
- **Confidence**: settled (first-party documentation; the auto-detection behavior is
  explicitly described)
- **Quote**: "This secret name is known to GitHub Agentic Workflows and does not need to
  be explicitly referenced in your workflow."
- **Our assessment**: The magic secret approach externalizes CI trigger configuration:
  existing workflows do not need to be modified. This is a significant operational advantage
  — organizations deploying gh-aw at scale can configure CI triggering once per repository
  via `gh aw secrets set GH_AW_CI_TRIGGER_TOKEN` without editing any workflow YAML. However,
  implicit configuration has a discoverability cost: practitioners reading a workflow spec
  will not see any CI-trigger configuration, even though the secret is active. For Ch02:
  recommend the explicit `github-token-for-extra-empty-commit` field for new workflows
  (visible, self-documenting), and `GH_AW_CI_TRIGGER_TOKEN` for retrofitting existing
  workflows without YAML changes.

### Claim 5: GitHub App authentication can substitute for PATs in `github-token-for-extra-empty-commit` by setting the value to `app` — using the GitHub App already configured for the workflow

- **Evidence**: Documented on the page in a dedicated "Using a GitHub App" section.
- **Confidence**: settled (first-party documentation; the `app` value is explicitly defined)
- **Quote**: "You can also use `app` to authenticate via the GitHub App configured for
  the workflow."
- **Our assessment**: The `app` option reuses the GitHub App already configured for the
  workflow rather than requiring a separate PAT. For organizations that have already
  deployed a GitHub App for their gh-aw workflows, this avoids creating and managing an
  additional PAT credential. The GitHub App must include `Contents: write` in its
  permissions to push the empty commit. For Ch02: if the workflow already uses a GitHub App
  for authentication, using `app` for CI triggering is simpler than managing a separate PAT
  — one credential instead of two. Organizations without a GitHub App should use the PAT
  approach.

### Claim 6: The full token override (`github-token` instead of `github-token-for-extra-empty-commit`) changes the PR author to the token holder and triggers CI directly, but grants more extensive permissions than the empty-commit approach — a deliberate security tradeoff

- **Evidence**: Documented in an "Alternative: Full Token Override" section that explicitly
  names the permission-scope difference.
- **Confidence**: settled (first-party documentation; the tradeoff is explicitly stated)
- **Quote**: "This changes the author of the PR to the user or app associated with the
  token, and triggers CI directly. However, it grants more permissions than the empty
  commit approach."
- **Our assessment**: The `github-token` field substitutes the token used by the Safe
  Output Processor for all operations in the `create-pull-request` flow — not just the
  empty commit push. This means the PR is created under the token holder's identity, which
  is useful when PRs should appear to come from a named bot account or compliance requires
  non-bot-attributed PRs. The "more permissions" caveat is because the full token is used
  for all PR operations, not just a contents-scoped empty commit. For Ch02 and Ch03:
  document this as a secondary option when PR authorship identity matters. The preference
  order for minimal permission exposure is: magic secret → explicit PAT → GitHub App `app`
  → full `github-token` override.

### Claim 7: CI triggering configuration applies symmetrically to both `create-pull-request` and `push-to-pull-request-branch` safe outputs — both are affected by the GITHUB_TOKEN restriction and both support the same auth fields

- **Evidence**: Both safe output types are explicitly named on the page as affected, and
  the PAT configuration examples are shown for both.
- **Confidence**: settled (first-party documentation; both safe output types are explicitly
  named)
- **Quote**: "This applies to both `create-pull-request` and `push-to-pull-request-branch`
  safe outputs."
- **Our assessment**: This symmetry matters for practitioners who use `push-to-pull-request-branch`
  (which updates an existing PR branch) versus `create-pull-request` (which creates a new PR).
  Both are affected by the same underlying GitHub Actions restriction, and both require the
  same configuration to trigger CI. Workflows that use `push-to-pull-request-branch` for
  iterative agentic PR updates need CI triggering configuration just as much as those using
  `create-pull-request`. For Ch02: when documenting either safe output type, include the CI
  triggering configuration as a standard setup step.

## Concrete Artifacts

### Quick Setup: Magic Secret (from page)

```bash
# One-time setup per repository — gh-aw auto-detects this secret, no workflow YAML changes needed
gh aw secrets set GH_AW_CI_TRIGGER_TOKEN --value "<your-pat-token>"
```

*Source: "Using a magic secret" section and the Note box at page top*

### PAT-based CI Triggering Configuration (from page)

```bash
# Step 1: Store a fine-grained PAT as a repository secret
gh aw secrets set MY_CI_TRIGGER_PAT --value "<your-pat-token>"
```

```yaml
# Step 2: Reference in workflow frontmatter (create-pull-request)
safe-outputs:
  create-pull-request:
    github-token-for-extra-empty-commit: ${{ secrets.MY_CI_TRIGGER_PAT }}
```

```yaml
# Or for push-to-pull-request-branch:
safe-outputs:
  push-to-pull-request-branch:
    github-token-for-extra-empty-commit: ${{ secrets.MY_CI_TRIGGER_PAT }}
```

*Source: "Using a Personal Access Token (PAT)" section*

### GitHub App CI Triggering Configuration (from page)

```yaml
safe-outputs:
  create-pull-request:
    github-token-for-extra-empty-commit: app
```

*Source: "Using a GitHub App" section*

### Full Token Override Configuration (from page)

```yaml
safe-outputs:
  create-pull-request:
    github-token: ${{ secrets.CI_USER_PAT }}
```

*Source: "Alternative: Full Token Override" section — note: changes PR author to token
holder; grants broader permissions than the empty-commit approach*

### Decision Guide: CI Triggering Approach Selection

```
Priority order (least to most permission exposure):

1. Magic secret (retrofit — zero YAML change needed):
   gh aw secrets set GH_AW_CI_TRIGGER_TOKEN --value "<pat>"
   → Implicit behavior; no workflow modification; PAT scope: Contents: R&W

2. Explicit PAT (new workflows — self-documenting):
   github-token-for-extra-empty-commit: ${{ secrets.MY_CI_TRIGGER_PAT }}
   → Visible in YAML; PAT scope: Contents: R&W only

3. GitHub App (if App already configured for the workflow):
   github-token-for-extra-empty-commit: app
   → Reuses existing App credential; App must have Contents: write

4. Full token override (when PR authorship identity matters):
   github-token: ${{ secrets.CI_USER_PAT }}
   → Changes PR author to token holder; broader permissions; triggers CI directly
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-04-06.md` Claim 5 (the `checks` MCP tool returns normalized CI
    verdicts: success, failed, pending, no_checks, policy_blocked): This source covers the
    complementary half of CI integration — *triggering* CI to run. The April 6 note covers
    *reading* CI verdicts after CI runs. Together they form the complete CI integration picture:
    trigger CI on PR creation (this source) → read CI verdicts via MCP (April 6 note). A
    workflow that reads `checks` verdicts but never configured CI triggering will always see
    `no_checks`.

- **Extends**:
  - `docs-ghaw-safe-outputs-specification.md` Claim 10 (two-level Safe Outputs configuration
    model — global parameters and type-specific blocks): The `github-token-for-extra-empty-commit`
    and `github-token` fields documented here are type-specific configuration parameters within
    the `create-pull-request` and `push-to-pull-request-branch` safe output types. This source
    extends the specification note by naming specific auth configuration fields within those types
    that are not documented in the spec's general configuration model.
  - `docs-ghaw-permissions-reference.md` Claim 1 (read-only by default; writes through Safe
    Outputs): The CI triggering issue reveals a gap in the standard Safe Outputs model — even
    when a workflow correctly routes PR creation through a safe output, the default GITHUB_TOKEN
    used by the Safe Output Processor cannot trigger CI on the resulting PR. The triggering-ci
    page adds token-override fields that extend the safe output configuration beyond what the
    permissions reference covers.
  - `blog-gh-aw-operations-release-workflows.md` Claim 1 (agent-created release PRs achieved a
    78% merge rate): The CI triggering issue is operationally critical for that release workflow
    pattern. If CI does not trigger on agent-created release PRs, reviewers cannot rely on CI
    verdicts before merging — which would likely require manual CI invocation or reduce review
    confidence. This source provides the configuration steps that make CI-gated human review
    viable for agent-created PRs.

- **Contradicts**: None. No existing source note contradicts the GITHUB_TOKEN restriction on CI
  triggering, or claims agent-created PRs automatically trigger CI. No contradiction issue
  required.

- **Novel**:
  - **The GITHUB_TOKEN CI-triggering restriction as a named failure mode for agentic workflows**
    (Claim 1): No existing source note in the corpus identifies this specific gap — agent-created
    PRs silently not triggering CI. This is the first documentation of this failure class in the
    corpus.
  - **`github-token-for-extra-empty-commit` field** (Claim 2): The empty-commit mechanism is a
    new configuration field not documented in any existing source note, including
    `docs-ghaw-safe-outputs-specification.md`.
  - **Magic secret `GH_AW_CI_TRIGGER_TOKEN` for zero-config CI triggering** (Claim 4): The
    auto-detected magic secret pattern is novel — it establishes that gh-aw has named secrets
    with implicit behaviors, not just explicitly-referenced secrets. This has security-audit
    implications not yet in the corpus.
  - **Four-option CI triggering decision framework with explicit tradeoffs** (Claims 2–6): The
    explicit comparison of PAT, GitHub App, magic secret, and full override with their permission
    tradeoffs is not documented anywhere in the existing corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add "CI triggering on agent-created PRs" as a required configuration step for any agentic
    workflow that creates PRs for human review. Current corpus notes on `create-pull-request`
    (via `docs-ghaw-safe-outputs-specification.md` and `docs-ghaw-permissions-reference.md`) do
    not warn practitioners that CI will not trigger by default. Add the magic-secret quick fix
    and the explicit PAT approach as the standard recommended configurations.
  - Add `Contents: Read & Write` as the minimum PAT scope for CI triggering — practitioners
    often assume a "CI trigger" token needs CI-related permissions (e.g., `checks: write`), but
    the mechanism is a content push.
  - Pair with `blog-ghaw-weekly-2026-04-06.md` Claim 5 (`checks` MCP tool) as the complete CI
    integration workflow: trigger CI on PR creation (this source) → read CI verdicts via MCP
    (April 6 note) → gate agent next steps on verdict.

- **Chapter 03 (Safety and Verification)**:
  - Add the GITHUB_TOKEN CI-triggering restriction as a named verification gap: an agentic
    workflow that creates PRs but does not configure CI triggering leaves reviewers without an
    automated quality signal. This is a silent failure — no error is thrown, CI simply never
    runs.
  - Add the magic secret pattern as a security-audit note: `GH_AW_CI_TRIGGER_TOKEN` provides
    implicit behavior that is not visible in workflow YAML. Security auditors reviewing workflow
    files will not see this configuration — it must be checked at the repository secrets level.

## Extraction Notes

1. **Source is compact and focused**: The page is a single-topic reference covering one specific
   problem (CI triggering on agent-created PRs) with four solutions. The content is approximately
   500 words plus four code blocks. All substantive claims were fully extracted.

2. **No sub-pages followed**: The page links to `reference/auth` (Authentication Reference) and
   `reference/safe-outputs` (Safe Outputs Reference). These were not followed — they are covered
   by existing source notes (`docs-ghaw-permissions-reference.md`,
   `docs-ghaw-safe-outputs-specification.md`).

3. **No publication date**: The documentation page does not carry an explicit publication date.
   `date_published` is left null. Content is current as of 2026-05-26.

4. **No contradictions identified**: All existing source notes are consistent with the GITHUB_TOKEN
   restriction described here. No existing note claims agent-created PRs automatically trigger CI.
   No contradiction issue filed.

5. **Video reference**: The page references an embedded video ("Creating a CI trigger token for
   agentic workflows"). The video content was not accessible via WebFetch; the textual content
   fully covers the configuration steps.
