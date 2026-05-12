---
source_url: https://github.github.com/gh-aw/reference/triggering-ci
source_type: docs
title: "GitHub Agentic Workflows: Triggering CI Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: settled
issue: "#417"
---

# GitHub Agentic Workflows: Triggering CI Reference

> Authoritative reference for the GitHub Actions default restriction that prevents
> agent-created PRs from triggering CI workflows, and the four concrete solutions
> (PAT, GitHub App, magic secret, full token override) with their security trade-offs —
> a specific operational pain point not covered by any existing corpus note on CI
> integration or safe outputs.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/triggering-ci` page,
  in the "Reference" section alongside `reference/permissions`, `reference/safe-outputs`,
  `reference/sandbox`. Reference pages document platform configuration authoritatively
  with CLI commands and YAML examples.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's agent factory and the `gh aw` CLI. The restriction being
  documented (GITHUB_TOKEN event-cascade prevention) is a settled GitHub Actions platform
  behavior; the four solutions are first-party platform design. Claims are authoritative
  for the gh-aw platform.
- **Scope**: Covers exactly one problem: agent-created PRs and branch pushes that fail to
  trigger CI workflow runs. Documents three configuration-based solutions
  (`github-token-for-extra-empty-commit` via PAT, GitHub App, or magic secret) and one
  broader alternative (full token override via `github-token:`). Does NOT cover: the Safe
  Outputs mechanism in general (see `docs-ghaw-safe-outputs-specification.md`), the
  permissions model (see `docs-ghaw-permissions-reference.md`), or how to *read* CI check
  state from within an agent (see `blog-ghaw-weekly-2026-04-06.md` Claim 5).

## Extracted Claims

### Claim 1: By default, pull requests created with the standard `GITHUB_TOKEN` in GitHub Actions do not trigger CI workflow runs — this is an intentional GitHub Actions safeguard against event cascades

- **Evidence**: The page states this directly in its opening sentence: "By default, pull
  requests created using the default `GITHUB_TOKEN` in GitHub Actions do not trigger CI
  workflow runs. This is a GitHub Actions feature to prevent event cascades." The
  restriction is framed as a deliberate platform design, not a bug.
- **Confidence**: settled (first-party documentation describing a settled GitHub Actions
  platform behavior; this is not a gh-aw-specific choice but a GitHub platform constraint
  that gh-aw must work around)
- **Quote**: "By default, pull requests created using the default `GITHUB_TOKEN` in
  GitHub Actions do not trigger CI workflow runs. This is a GitHub Actions feature to
  prevent event cascades."
- **Our assessment**: This is the canonical statement of the problem every team hits
  when building agentic workflows that create PRs. The "event cascade" rationale is
  important: GitHub prevents the GITHUB_TOKEN from triggering new workflow runs to stop
  infinite loops (workflow creates PR → PR triggers workflow → workflow creates PR...).
  It is a security-by-default posture that is correct in general but problematic for
  agentic workflows where the PR creation and the CI verification are deliberately
  separate steps. For Ch02 (Harness Engineering): this restriction is a gotcha that
  every team building agentic PR-creation workflows will encounter. It must be
  documented prominently.

### Claim 2: The CI-triggering limitation applies to both `create-pull-request` and `push-to-pull-request-branch` safe outputs — covering both PR creation and branch push operations

- **Evidence**: The page states explicitly: "This applies to both
  [`create-pull-request`] and [`push-to-pull-request-branch`] safe outputs." Both
  are linked to their respective sections in the safe outputs reference.
- **Confidence**: settled (first-party; both safe output types are explicitly named)
- **Quote**: "This applies to both [`create-pull-request`] and
  [`push-to-pull-request-branch`] safe outputs."
- **Our assessment**: The scope of the limitation is broader than just PR creation.
  An agent that pushes to a PR branch (without creating the PR) also cannot trigger
  CI via `push` events. This means the workaround must be applied at every safe output
  that writes to a branch, not only at PR-creation time. For Ch02: practitioners who
  split PR creation from subsequent commits must apply the CI trigger fix to both safe
  output types.

### Claim 3: The recommended quickest fix is the magic secret `GH_AW_CI_TRIGGER_TOKEN` — a PAT with `Contents: Read & Write` that is recognized by gh-aw without requiring explicit workflow references

- **Evidence**: The page highlights this in a prominent **Note** callout immediately
  after describing the problem: "The easiest way to fix this problem is to set a
  secret `GH_AW_CI_TRIGGER_TOKEN` with a Personal Access Token (PAT) with 'Contents:
  Read & Write' permission to your repo." The command is: `gh aw secrets set
  GH_AW_CI_TRIGGER_TOKEN --value "<your-pat-token>"`. The page later explains:
  "This secret name is known to GitHub Agentic Workflows and does not need to be
  explicitly referenced in your workflow."
- **Confidence**: settled (first-party; the magic secret name and its convention are
  explicitly documented)
- **Quote**: "The easiest way to fix this problem is to set a secret
  `GH_AW_CI_TRIGGER_TOKEN` with a Personal Access Token (PAT) with 'Contents: Read
  & Write' permission to your repo."
- **Our assessment**: The "magic secret" pattern (a pre-agreed secret name that the
  platform recognizes automatically) is a deliberate developer experience choice —
  it reduces the configuration needed from three steps (create PAT, set secret, update
  workflow) to two steps (create PAT, set secret with the magic name). This is the
  correct recommendation for teams who want minimal workflow changes. The trade-off:
  the magic secret applies globally to all workflows in the repo that encounter the
  CI trigger problem, which may not always be desirable if different workflows need
  different token identities. For Ch02: present the magic secret as the first-choice
  solution with a note about the implicit global scope.

### Claim 4: The CI-trigger mechanism works by pushing an extra empty commit to the PR branch after PR creation — this extra commit triggers `push` and `pull_request` events normally

- **Evidence**: The page states this mechanism directly: "When configured, the token
  will be used to push an extra empty commit to the PR branch after PR creation.
  This will trigger `push` and `pull_request` events normally."
- **Confidence**: settled (first-party; the mechanism is explicitly documented with
  the specific events it triggers)
- **Quote**: "the token will be used to push an extra empty commit to the PR branch
  after PR creation. This will trigger `push` and `pull_request` events normally."
- **Our assessment**: The extra-empty-commit mechanism is architecturally notable:
  rather than finding a way to exempt the GITHUB_TOKEN from the event-cascade
  restriction, gh-aw sidesteps it entirely by using a different token (PAT or App)
  to push a semantically empty commit. The commit is "extra" and "empty" — it does
  not change file content — but it carries a different actor identity, which GitHub
  allows to trigger workflows. This is a clean workaround that doesn't require
  changes to the CI workflow's trigger conditions. For Ch02: the mechanism is worth
  explaining because practitioners who see an "empty commit" in their PR history
  should understand why it appears and that it is intentional harness behavior, not
  a bug.

### Claim 5: PAT-based CI triggering can be configured per-safe-output via the `github-token-for-extra-empty-commit` field, supporting custom secret names for per-workflow token control

- **Evidence**: The page documents a three-step PAT setup. Step 3 references the token
  in the workflow:
  ```
  safe-outputs:
    create-pull-request:
      github-token-for-extra-empty-commit: ${{ secrets.MY_CI_TRIGGER_PAT }}
  ```
  and equivalently for `push-to-pull-request-branch`. The custom secret name
  (`MY_CI_TRIGGER_PAT` vs. the magic `GH_AW_CI_TRIGGER_TOKEN`) is the differentiator.
- **Confidence**: settled (first-party; the YAML configuration field is explicitly named
  and documented with both applicable safe output types)
- **Quote**: (no single prose quote; the claim is substantiated by the YAML
  configuration artifact — see Concrete Artifacts)
- **Our assessment**: The explicit `github-token-for-extra-empty-commit` field allows
  different workflows to use different PAT identities for the CI-trigger commit, which
  may matter for audit trails (the empty commit will be attributed to the PAT owner).
  The field name precisely describes its effect — it only applies to the extra empty
  commit, not to the PR creation itself. The PR authorship remains the GITHUB_TOKEN
  identity; only the triggering commit uses the PAT. This is a narrower permission
  grant than the full token override (Claim 7). For Ch02: document
  `github-token-for-extra-empty-commit` as the per-workflow explicit configuration
  alternative to the global magic secret.

### Claim 6: GitHub App authentication can be used for CI triggering by setting `github-token-for-extra-empty-commit: app`, using the GitHub App configured for the workflow

- **Evidence**: The page's "Using a GitHub App" section provides: "You can also use
  `app` to authenticate via [the GitHub App configured for the workflow]." The YAML:
  ```
  safe-outputs:
    create-pull-request:
      github-token-for-extra-empty-commit: app
  ```
- **Confidence**: settled (first-party; the literal value `app` is a documented
  configuration option referencing the workflow's configured GitHub App)
- **Quote**: "You can also use `app` to authenticate via the GitHub App configured
  for the workflow."
- **Our assessment**: Using a GitHub App for CI triggering has distinct advantages
  over a PAT: Apps are not tied to a specific user account, rotate credentials
  automatically, and can be granted fine-grained per-repository permissions at the
  organization level. The commit will be attributed to the App's identity rather than
  a personal account. For teams that already configure a GitHub App for their gh-aw
  workflows (e.g., for the extended permissions documented in
  `docs-ghaw-permissions-reference.md` Claim 6), the `app` value requires no
  additional PAT management. For Ch02: recommend `app` over PAT for production
  deployments if a GitHub App is already configured — it is the more maintainable
  long-term choice.

### Claim 7: The full token override (`github-token:` replacing `github-token-for-extra-empty-commit:`) changes PR authorship to the token owner and grants more permissions than the empty-commit approach

- **Evidence**: The page's "Alternative: Full Token Override" section: "If you want
  all PR operations to use a different token (not just the CI trigger), use the
  `github-token` field instead... This changes the author of the PR to the user or
  app associated with the token, and triggers CI directly. However, it grants more
  permissions than the empty commit approach."
- **Confidence**: settled (first-party; the authorship change and permission scope
  difference are explicitly stated as trade-offs)
- **Quote**: "This changes the author of the PR to the user or app associated with
  the token, and triggers CI directly. However, it grants more permissions than the
  empty commit approach."
- **Our assessment**: The authorship change is a meaningful side effect. When an
  agent creates a PR via the full token override, the PR appears as created by the
  PAT owner or App, not by the GITHUB_TOKEN-associated identity (typically the
  GitHub Actions bot). This affects audit trails, code ownership attribution, and
  any branch protection rules that filter by author. The "more permissions" warning
  is critical: the full token override applies the alternative token to all PR
  operations, not just the CI-triggering commit — meaning the token's identity
  participates in the entire PR creation flow, not just the empty commit. For Ch03
  (Safety and Verification): the full token override is the highest-permission
  solution and should only be chosen when the authorship change and broader scope
  are intentional design decisions, not as the default CI-triggering fix.

## Concrete Artifacts

### Magic Secret Setup (quickest fix, from source)

```bash
# Set the magic secret — gh-aw recognizes this name automatically
# PAT requires 'Contents: Read & Write' permission scoped to relevant repos
gh aw secrets set GH_AW_CI_TRIGGER_TOKEN --value "<your-pat-token>"
```

*Source: "Note" callout and "Using a magic secret" section*

### PAT Method — Workflow Configuration (from source)

```bash
# Step 1: Create fine-grained PAT with Contents: Read & Write
# (gh-aw docs link pre-fills: token name, description, Contents permission)

# Step 2: Set as a custom-named repository secret
gh aw secrets set MY_CI_TRIGGER_PAT --value "<your-pat-token>"
```

```yaml
# Step 3a: Reference in create-pull-request safe output
safe-outputs:
  create-pull-request:
    github-token-for-extra-empty-commit: ${{ secrets.MY_CI_TRIGGER_PAT }}
```

```yaml
# Step 3b: Or in push-to-pull-request-branch safe output
safe-outputs:
  push-to-pull-request-branch:
    github-token-for-extra-empty-commit: ${{ secrets.MY_CI_TRIGGER_PAT }}
```

*Source: "Using a Personal Access Token (PAT)" section*

### GitHub App Method — Workflow Configuration (from source)

```yaml
safe-outputs:
  create-pull-request:
    github-token-for-extra-empty-commit: app
```

*Source: "Using a GitHub App" section*

### Full Token Override (alternative, higher-permission, from source)

```yaml
# Applies the alternative token to ALL PR operations — not just the CI-trigger commit
# Side effect: PR author becomes the token owner, not the GITHUB_TOKEN identity
safe-outputs:
  create-pull-request:
    github-token: ${{ secrets.CI_USER_PAT }}
```

*Source: "Alternative: Full Token Override" section*

### Decision Table: CI Trigger Method Comparison

```
Method                         | Token scope     | PR authorship      | Workflow change required?
-------------------------------|-----------------|--------------------|--------------------------
Magic secret                   | CI trigger only | GITHUB_TOKEN       | No (magic name auto-detected)
(GH_AW_CI_TRIGGER_TOKEN)      |                 |                    |
                               |                 |                    |
PAT via explicit field          | CI trigger only | GITHUB_TOKEN       | Yes (add field to safe-outputs)
(github-token-for-extra-       |                 |                    |
 empty-commit: ${{ secrets.*}}) |                |                    |
                               |                 |                    |
GitHub App via field            | CI trigger only | GITHUB_TOKEN       | Yes (set github-token-for...=app)
(github-token-for-extra-       |                 |                    |
 empty-commit: app)             |                |                    |
                               |                 |                    |
Full token override             | ALL PR ops      | Token owner        | Yes (replace github-token field)
(github-token: ${{ secrets.*}})|                 | (user or App)      |
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-04-06.md` Claim 5 (the `checks` MCP tool returning
    normalized CI verdicts: success/failed/pending/no_checks/policy_blocked): That
    claim covers *reading* CI state from within an agent. This source covers *triggering*
    CI to run in the first place. The two together describe the full CI integration loop
    for agentic workflows: trigger CI → wait for verdict → read result via `checks` tool.
    Note that `policy_blocked` as a distinct verdict (not `failed`) is relevant here:
    an agent that successfully triggers CI via the PAT empty-commit approach may still
    encounter `policy_blocked` if a branch protection policy blocks check execution for
    the PAT identity. The two notes should be read together for complete CI integration.

  - `docs-ghaw-permissions-reference.md` Claim 2 (four security rationales for the
    read/safe-outputs separation: audit trail, blast radius, compliance gates, prompt
    injection defense): The CI triggering restriction is a parallel dimension of the same
    underlying concern — GITHUB_TOKEN identity restrictions for security. The permissions
    reference explains why writes go through safe outputs (audit trail, blast radius);
    this source explains why the GITHUB_TOKEN is additionally restricted from triggering
    new workflow runs (event cascade prevention). Both are GitHub's layered security
    model applied to automated workflows.

  - `docs-ghaw-safe-outputs-specification.md` Claim 3 (agents MUST execute without
    write permissions; communication via NDJSON artifact storage): The `create-pull-request`
    and `push-to-pull-request-branch` safe outputs mentioned in this source are precisely
    the Safe Output types processed via the NDJSON pipeline. The CI-triggering limitation
    occurs at the GitHub platform level *after* the Safe Output Processor executes the
    operation — the GITHUB_TOKEN restriction is orthogonal to, and independent of, the
    Safe Outputs privilege-separation mechanism.

- **Extends**:
  - `blog-gh-aw-operations-release-workflows.md` (Changeset Generator, 78% merge rate
    on agent-created release PRs): That source documents agent-created PRs in production
    but does not cover CI triggering. The 22% rejection rate (6/28 PRs) raises the
    question of whether CI failures contributed — without CI triggering properly configured,
    reviewers cannot use CI green/red as a signal. This source provides the missing
    infrastructure piece for making agent-created PRs reviewable against CI results.

  - `docs-ghaw-permissions-reference.md` Claim 1 (read-only permissions by default,
    write via safe-outputs): The `github-token-for-extra-empty-commit` field extends
    the permissions model with a third token slot: (1) agent read token (from
    `permissions:`), (2) safe-outputs write token (from `safe-outputs:` processing),
    (3) CI-trigger token (from `github-token-for-extra-empty-commit:`). This three-token
    architecture — each with distinct scope and identity — is not described in the
    permissions reference.

- **Contradicts**: None. No existing source note addresses the GITHUB_TOKEN CI-trigger
  restriction or the solutions. This is a gap in the corpus, not a contradiction with
  any existing claim.

- **Novel**:
  - **GITHUB_TOKEN CI-trigger restriction as a named gotcha**: No existing source note
    in the corpus identifies or explains the default behavior that prevents agent-created
    PRs from triggering CI. This is entirely new to the corpus and fills a high-impact gap.
  - **Four CI-trigger solutions with trade-offs**: The PAT / GitHub App / magic secret /
    full override taxonomy with their specific trade-offs (scope, authorship, workflow
    change required) is not documented in any existing note.
  - **Extra empty commit mechanism**: The implementation detail — that the workaround
    works by pushing a semantically empty commit with a different token identity — is new
    and explains behavior (empty commits in PR history) that would otherwise confuse
    practitioners.
  - **`github-token-for-extra-empty-commit` field**: This specific YAML field name and
    its semantics (applies only to the CI-triggering commit, not the PR creation itself)
    are not described in any existing source note, including `docs-ghaw-safe-outputs-specification.md`.
  - **Magic secret pattern**: The `GH_AW_CI_TRIGGER_TOKEN` convention (a pre-agreed
    secret name that the platform recognizes automatically without workflow references)
    is a novel platform design pattern not described elsewhere in the corpus.
  - **Full token override authorship side effect**: The explicit trade-off that using
    `github-token:` changes PR authorship is not noted in any existing source.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "CI triggering for agent-created PRs" as
  a named gotcha in the harness engineering chapter. The default GITHUB_TOKEN restriction
  (Claim 1) affects every team building agentic PR workflows. The recommended configuration
  path should follow the decision table: magic secret first (lowest workflow change cost),
  then explicit PAT field, then GitHub App, with full token override reserved for cases
  where authorship change is intentional. Pair with the `checks` MCP tool
  (`blog-ghaw-weekly-2026-04-06.md` Claim 5) to show the full CI integration loop
  (trigger → verify → read verdict).

- **Chapter 03 (Safety and Verification)**: Add the full token override security
  trade-off as a named anti-pattern risk (Claim 7). When teams want agent-created PRs
  to trigger CI, the tempting shortcut (`github-token: ${{ secrets.MY_PAT }}`) silently
  changes PR authorship and grants broader permissions than the targeted empty-commit
  approach. The correct default is `github-token-for-extra-empty-commit:` (narrower
  scope, preserved authorship). Document the authorship change as a concrete audit trail
  risk: if the PR appears authored by a personal account, it bypasses the GitHub Actions
  bot identity that signals "this was automated."

## Extraction Notes

1. **YAML formatting in source**: The WebFetch rendering concatenated multi-line YAML
   onto single lines (e.g., `safe-outputs:  create-pull-request:    github-token-for-extra-empty-commit:...`).
   The YAML blocks in Concrete Artifacts have been normalized to standard multi-line YAML
   format. The field names and values are character-for-character accurate from the source;
   only line breaks were restored.

2. **Linked sub-pages not followed**: The page links to `reference/safe-outputs` (for
   `create-pull-request` and `push-to-pull-request-branch` parameter schemas) and
   `reference/auth` (for GitHub App token setup and permissions). These are covered by
   existing corpus notes (`docs-ghaw-safe-outputs-specification.md` and
   `docs-ghaw-permissions-reference.md`) and were not re-fetched.

3. **Video content not extracted**: The source includes a video player ("Creating a CI
   trigger token for agentic workflows") that was not accessible via WebFetch. The
   surrounding text provides sufficient context.

4. **No publication date**: The documentation page does not carry an explicit publication
   date. `date_published` is left null, consistent with other gh-aw reference notes.

5. **No contradictions to file**: All existing corpus notes checked. No existing claim
   addresses the GITHUB_TOKEN CI-trigger restriction or the solutions. No contradiction
   issue required.
