---
source_url: https://github.blog/changelog/2026-07-02-copilot-cli-no-longer-needs-a-personal-access-token-in-github-actions
source_type: docs
title: "Copilot CLI no longer needs a personal access token in GitHub Actions"
author: GitHub (official changelog)
date_published: 2026-07-02
date_extracted: 2026-07-06
last_checked: 2026-07-06
status: current
confidence_overall: settled
issue: "#1577"
---

# Copilot CLI No Longer Needs a Personal Access Token in GitHub Actions

> GitHub's July 2, 2026 changelog announces that the `copilot` CLI binary can now
> authenticate in GitHub Actions using the built-in `GITHUB_TOKEN` (via a new
> `copilot-requests: write` permission) instead of a personal access token — but
> the linked how-to doc states GitHub's actual recommendation is to use GitHub
> Agentic Workflows rather than invoking `copilot` directly in a workflow step,
> because direct invocation gives the CLI broad access to the workflow
> environment, a risk called out explicitly for fork-triggered PR workflows.

## Source Context

- **Type**: docs (GitHub official product changelog, July 2, 2026, ~200 words)
  plus one linked how-to doc followed for implementation detail:
  `docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli-in-actions`
  ("Using Copilot CLI in GitHub Actions with GITHUB_TOKEN").
- **Author credibility**: GitHub engineering/docs team announcing and documenting
  a production platform capability. Authoritative for: the existence of the
  feature, the exact permission and policy names, the billing behavior, the
  example workflow YAML, and GitHub's own stated recommendation between the two
  invocation paths (Agentic Workflows vs. direct CLI). Not a source for
  quantitative security or cost outcomes — no incident data or usage metrics are
  cited for either path.
- **Scope**: Covers authenticating the `copilot` CLI binary itself (not the
  `gh aw` agentic-workflow compiler/runtime) when run inside a GitHub Actions
  step. Covers: the new `GITHUB_TOKEN` auth path, the org billing policy
  prerequisite, the `copilot-requests: write` permission, cost-control options,
  the CLI version prerequisite, and GitHub's recommended-vs-direct-invocation
  guidance. Does NOT cover: rate limits or quota differences between PAT and
  `GITHUB_TOKEN` auth for the CLI, whether this changes anything about the
  `gh aw` platform's own Copilot-invocation safe outputs (`create-agent-session`,
  `assign-to-agent`), or migration steps for existing PAT-based Copilot CLI
  workflows.

## Extracted Claims

### Claim 1: The `copilot` CLI binary can now run in GitHub Actions using the built-in `GITHUB_TOKEN`, with no personal access token required
- **Evidence**: Official GitHub changelog, opening statement of the announcement.
- **Confidence**: settled (first-party announcement of a shipped production feature)
- **Quote**: "You can now run GitHub Copilot CLI in GitHub Actions using the built-in GITHUB_TOKEN."
- **Our assessment**: This closes the same class of gap that `docs-github-copilot-aw-github-token-auth.md`
  (June 11, 2026) documented for GitHub Agentic Workflows, but for a different
  surface: the `copilot` CLI invoked directly as a workflow step, rather than
  the `gh aw` compiled-workflow runtime. Teams that were separately provisioning
  PATs for ad hoc `copilot` CLI steps (e.g., "run copilot to summarize this
  commit") can now drop that PAT entirely and rely on the Actions token like any
  other step.

### Claim 2: Eliminating the PAT requirement removes the operational and security risk of managing long-lived credentials for automation at scale
- **Evidence**: Stated directly as the motivation for the change.
- **Confidence**: settled (first-party stated rationale)
- **Quote**: "This means that you no longer need to create and store a personal access token (PAT), eliminating the operational and security risks of managing long-lived PATs for automations at scale."
- **Our assessment**: Identical rationale to the `gh aw` PAT-elimination announcement
  (`docs-github-copilot-aw-github-token-auth.md`, Claim 2) — GitHub is applying the
  same "replace long-lived PAT with ephemeral Actions token" pattern across both
  of its Copilot-invocation surfaces (the `gh aw` compiler and the raw `copilot`
  CLI). This corroborates a platform-wide direction rather than a one-off fix.

### Claim 3: When Copilot CLI runs with the Actions token in an organization-owned repository, AI credits it consumes are billed directly to the organization
- **Evidence**: Stated directly in the changelog as the billing consequence of using the Actions token.
- **Confidence**: settled
- **Quote**: "When you run Copilot CLI with the Actions token in an organization-owned repository, AI credits consumed by the CLI are billed directly to the organization."
- **Our assessment**: Same billing-consolidation pattern documented for `gh aw`
  in `docs-github-copilot-aw-github-token-auth.md` Claim 3 and for Copilot code
  review in `docs-github-copilot-code-review-actions-billing.md` Claim 1 — a
  third confirmation that GitHub is moving Copilot AI spend to org-level billing
  wherever `GITHUB_TOKEN` is the auth mechanism in an org repo. Individual
  contributors are no longer the cost center for CI-triggered Copilot CLI usage.

### Claim 4: Enabling this requires the "Allow use of Copilot CLI billed to the organization" policy, which is enabled by default if the org's existing "Copilot CLI" policy is active
- **Evidence**: Stated as a configuration prerequisite, with the default-enablement condition specified.
- **Confidence**: settled (exact policy name and default-state condition given in the how-to doc)
- **Quote**: "This policy is enabled by default for organizations with Copilot CLI turned on, but you can confirm or change this setting in your organization's policy settings."
- **Our assessment**: For orgs already running Copilot CLI, this is a zero-action
  rollout — the prerequisite policy is already on. For orgs that have Copilot CLI
  disabled at the org level (or scoped narrowly), an admin must separately confirm
  or enable "Allow use of Copilot CLI billed to the organization" under the
  "Copilot CLI" policy settings before any workflow can use this auth path. This
  is the same "org-policy gate, enabled by default for existing adopters" shape
  as the `gh aw` prerequisite in `docs-github-copilot-aw-github-token-auth.md`
  Claim 5, though the two are almost certainly the same underlying org policy
  given the identical policy name ("Allow use of Copilot CLI billed to the
  organization") appearing in both changelogs.

### Claim 5: Workflows need only the `copilot-requests: write` permission to authenticate with the built-in `GITHUB_TOKEN` — no additional secrets are required
- **Evidence**: Stated directly in the changelog and the linked how-to doc, with a full example workflow.
- **Confidence**: settled (exact permission name given, and demonstrated in a working YAML example)
- **Quote**: "Once enabled, workflows just need the copilot-requests: write permission and can authenticate with the workflow's built-in GITHUB_TOKEN. No additional secrets are required."
- **Our assessment**: This is the identical permission key (`copilot-requests: write`)
  used to enable `GITHUB_TOKEN` billing for `gh aw` agentic workflows
  (`docs-github-copilot-aw-github-token-auth.md` Claim 4). The two products share
  one permission surface for Copilot billing/auth — a practitioner who has already
  added `copilot-requests: write` for one product's workflows is using the exact
  same declaration the other product needs. For Ch02: document this permission
  once as "the Copilot Actions-token permission," applicable to both `gh aw`
  compiled workflows and direct `copilot` CLI steps.

### Claim 6: Since user-level AI credit budgets don't apply under organization billing, cost is instead governed via cost centers, org billing dashboards, and per-workflow session limits
- **Evidence**: Stated directly, with three named mechanisms.
- **Confidence**: settled
- **Quote**: "User-level budgets are not considered when billing directly to the organization because the cost is not attributed to a user. There are multiple ways to manage spend when using this billing method"
- **Our assessment**: Same three-mechanism cost-control shape as
  `docs-github-copilot-aw-github-token-auth.md` Claim 7 (cost centers + dashboards
  + per-run caps), specialized here as a per-workflow "session limit" rather than
  a per-workflow-run cap — worth confirming with the Smith whether "session limit"
  and "per-workflow-run cap" are the same underlying primitive across the two
  docs pages or genuinely distinct controls. Either way, the operational
  takeaway is identical: enabling org billing without also configuring one of
  these three controls leaves CLI-driven AI spend unbounded at the org level.

### Claim 7: A recent Copilot CLI version is required — update via `copilot update` or reinstall via `npm install -g @github/copilot`
- **Evidence**: Stated as an explicit prerequisite with both update commands.
- **Confidence**: settled (exact commands given)
- **Quote**: "You must be on a recent version of Copilot CLI. Update with copilot update, or reinstall the latest version with npm install -g @github/copilot."
- **Our assessment**: Low-friction but blocking — any CI image or setup step
  that pins an older `@github/copilot` npm version will silently lack this auth
  path until upgraded. Teams should add a version check or unconditional
  `npm install -g @github/copilot` step ahead of the Copilot CLI invocation
  step in any workflow adopting this pattern, mirroring the `gh extension
  upgrade aw` prerequisite documented for the `gh aw` CLI in
  `docs-github-copilot-aw-github-token-auth.md` Claim 6.

### Claim 8: GitHub's stated recommendation is to use GitHub Agentic Workflows rather than invoking `copilot` directly in a workflow step, because Agentic Workflows use `GITHUB_TOKEN` by default and add guardrails suited for automated environments
- **Evidence**: Stated in the linked how-to doc's dedicated "Recommended approach" section, positioned ahead of the direct-invocation instructions.
- **Confidence**: settled (explicit, first-party recommendation, not an inference)
- **Quote**: "For most automation use cases, we recommend using GitHub Agentic Workflows rather than invoking copilot directly in workflow steps. Agentic workflows use GITHUB_TOKEN authentication by default and include additional guardrails suited for automated environments."
- **Our assessment**: This is the single most guide-relevant claim in the source
  and is easy to miss if only the changelog (not the linked how-to) is read — the
  changelog itself only documents direct CLI invocation and never mentions this
  preference. GitHub is explicitly steering practitioners toward the `gh aw`
  platform (documented extensively elsewhere in the corpus, e.g.
  `docs-ghaw-how-they-work.md`, `docs-ghaw-safe-outputs-specification.md`) as
  the *default* choice for CI-triggered Copilot automation, with raw `copilot`
  CLI invocation positioned as the fallback for cases Agentic Workflows doesn't
  cover. Prior corpus notes about `gh aw` document its safety architecture
  (Safe Outputs, least-privilege) as a design choice; this source is the first
  to show GitHub explicitly telling practitioners to prefer it over the simpler
  alternative for this reason.

### Claim 9: Invoking Copilot CLI directly in a workflow step gives it broad access to the workflow environment; this is called out as a particular risk for workflows triggered by pull requests from forks
- **Evidence**: Stated as an explicit warning callout in the "Using Copilot CLI directly in a workflow" section of the linked how-to doc, immediately before the example workflow.
- **Confidence**: settled (explicit first-party security warning)
- **Quote**: "Invoking Copilot CLI directly in workflow steps gives it broad access to your workflow environment. Review your workflow triggers and permissions carefully before using this approach. Workflows triggered by pull requests from forks are particularly at risk."
- **Our assessment**: This is a direct, first-party statement of the exact threat
  model the guide's security chapter should already be covering for any
  agent-in-CI pattern: an agent step with workflow-level access (secrets, token
  scope, checkout contents) run against untrusted input (a fork PR's diff or
  branch) can be steered by that untrusted input. GitHub's own fix for this
  class of risk in the `gh aw` product is the Safe Outputs architecture
  (agents execute without write permissions; writes are mediated — see
  `docs-ghaw-safe-outputs-specification.md`). This warning is effectively GitHub
  telling practitioners: "if you don't want to adopt that architecture, at
  least don't run this against fork PRs, or scope permissions and triggers very
  carefully." It is the security rationale underpinning Claim 8's
  recommendation, made concrete rather than abstract.

### Claim 10: The example direct-invocation workflow uses `copilot --yolo -p "<prompt>"`, where `--yolo` suppresses interactive prompts required for non-interactive CI use
- **Evidence**: Full example workflow YAML with an explanatory bullet list immediately following it in the how-to doc.
- **Confidence**: settled (working example provided directly by GitHub)
- **Quote**: "The --yolo flag suppresses interactive prompts, which is required for non-interactive environments like GitHub Actions."
- **Our assessment**: `--yolo` is effectively Copilot CLI's "skip permission
  prompts" flag for unattended execution — the same class of flag as
  `--dangerously-skip-permissions`-style settings documented elsewhere in the
  corpus for other CLI agent harnesses. Combined with Claim 9's warning about
  broad workflow-environment access, `--yolo` removes the one interactive
  checkpoint (prompt confirmation) that might otherwise catch an agent about to
  take an unexpected action — reinforcing why GitHub scopes this warning
  specifically to the direct-invocation path and not to Agentic Workflows
  (which mediate writes through Safe Outputs instead of relying on interactive
  confirmation).

## Concrete Artifacts

### Example Direct-Invocation Workflow (verbatim from the how-to doc)

```yaml
name: Copilot CLI example
on: [push]

permissions:
  contents: read
  copilot-requests: write

jobs:
  copilot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Install Copilot CLI
        run: npm install -g @github/copilot
      - name: Run Copilot
        run: copilot --yolo -p "Summarize the changes in this commit"
        env:
          GITHUB_TOKEN: $
```
*Source: docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli-in-actions
("Using Copilot CLI in GitHub Actions with GITHUB_TOKEN"). Note: the `env:`
block's `GITHUB_TOKEN` value was truncated by the fetch tool at the interpolation
syntax (`${{ secrets.GITHUB_TOKEN }}` or `${{ github.token }}`, standard GitHub
Actions expression syntax) — the doc's rendered HTML confirms the key is
`GITHUB_TOKEN:` under `env:` on the same step; the Assayer should confirm the
exact expression against the live page.*

### Migration/Setup Checklist (assembled from changelog + how-to doc)

```
Prerequisites for GITHUB_TOKEN authentication in direct Copilot CLI workflow steps:

1. Org policy: "Allow use of Copilot CLI billed to the organization" must be enabled
   → Enabled by default for orgs with the existing "Copilot CLI" policy active
   → Otherwise requires org-admin confirmation in org policy settings

2. CLI version: update with `copilot update`, or `npm install -g @github/copilot`

3. Workflow permissions: add `copilot-requests: write` (no additional secrets)

4. Decision point (per GitHub's own recommendation):
   → Most automation use cases: use GitHub Agentic Workflows (GITHUB_TOKEN by
     default + additional guardrails)
   → Only if invoking `copilot` directly: review workflow triggers/permissions
     carefully; treat fork-PR-triggered workflows as high risk; use `--yolo`
     for non-interactive execution

5. Cost management (org billing means no user-level budget applies):
   → Configure cost centers, and/or
   → Monitor org billing/usage dashboards, and/or
   → Set a session limit capping AI credits per workflow
```
*Assembled by the Miner from github.blog/changelog/2026-07-02-... and the linked
how-to doc; not a verbatim quote.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-aw-github-token-auth.md` (Claims 1–7): The June 11,
    2026 `gh aw` PAT-elimination announcement and this July 2, 2026 `copilot`
    CLI announcement share: the same rationale (eliminate long-lived PAT
    risk), the same org-billing consequence when using `GITHUB_TOKEN` in an
    org repo, the same `copilot-requests: write` permission key, the same named
    org policy ("Allow use of Copilot CLI billed to the organization"), and the
    same three-part cost-control shape (cost centers / dashboards / per-run or
    per-session caps). This is strong evidence the two products share
    underlying billing and policy infrastructure, not just a similar-sounding
    feature.
  - `docs-github-copilot-code-review-actions-billing.md` (Claim 1): A third
    Copilot surface (code review) confirming the general pattern of shifting
    AI credit billing to the organization when Copilot runs via `GITHUB_TOKEN`
    in Actions.
  - `docs-ghaw-safe-outputs-specification.md`: Claim 9's warning about broad
    workflow-environment access from direct CLI invocation is the practical,
    user-facing restatement of the threat model that the Safe Outputs
    architecture (agents run without write permissions) is designed to solve.

- **Contradicts**: None identified. This source's direct-CLI-invocation auth
  path is a distinct mechanism from the `gh aw` platform's Copilot-invocation
  safe outputs (`create-agent-session`, `assign-to-agent`), which
  `docs-ghaw-copilot-cloud-agent.md` (Claim 5) documents as still requiring a
  fine-grained PAT (`GITHUB_TOKEN` explicitly insufficient, GitHub App tokens
  unsupported). These are not competing claims about the same mechanism — one
  is "invoke the `copilot` binary as a workflow step" (this source, now
  `GITHUB_TOKEN`-capable), the other is "invoke Copilot as a `gh aw` safe
  output that dispatches a cloud coding session" (still PAT-only as of that
  note's extraction date, 2026-06-06). Worth flagging for the Smith: it is easy
  for a reader to conflate "Copilot CLI now accepts GITHUB_TOKEN" with "all
  Copilot dispatch mechanisms now accept GITHUB_TOKEN" — they should not be
  merged in the guide without checking whether `docs-ghaw-copilot-cloud-agent.md`
  has since been superseded.

- **Extends**:
  - `docs-github-copilot-cli-security-review.md`: That note documents
    Copilot CLI's `/security-review` command as a pre-commit, developer-
    initiated scan. This source adds a second CI-specific security
    consideration for the same CLI: when run unattended in Actions with broad
    workflow access, particularly against fork PRs. Together they suggest two
    distinct threat surfaces for the same tool — interactive local use (where
    `/security-review` helps) vs. unattended CI use (where the `GITHUB_TOKEN`
    auth path introduces the fork-PR risk this source warns about).
  - `docs-ghaw-fork-support.md` (if that note documents `gh aw`'s handling of
    fork-triggered workflows): this source's fork-PR warning for direct CLI
    invocation is a natural point of comparison — worth checking whether
    Agentic Workflows' fork handling is exactly the mitigation GitHub is
    implicitly recommending in Claim 8/9.

- **Novel**:
  - **Explicit GitHub recommendation to prefer Agentic Workflows over direct
    CLI invocation for automation** (Claim 8): No prior corpus note documents
    GitHub itself stating this preference in these terms. Prior notes describe
    `gh aw`'s architecture as advantageous by design; this is the first
    first-party statement telling practitioners which surface to default to
    and naming the direct-invocation alternative as the non-default,
    higher-risk path.
  - **Explicit fork-PR risk warning for direct Copilot CLI invocation in
    Actions** (Claim 9): This specific warning, tied to this specific
    invocation pattern, is new to the corpus.
  - **`--yolo` flag documented for Copilot CLI's non-interactive/CI use**
    (Claim 10): Not previously documented in the corpus for this tool.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: When documenting Copilot CLI use in
  CI, present GitHub's own two-tier recommendation as the default guidance:
  prefer GitHub Agentic Workflows for automation; reserve direct `copilot
  --yolo` invocation for cases Agentic Workflows doesn't cover, and only after
  reviewing triggers/permissions. Add the `copilot-requests: write` permission
  and CLI-version-update step to the setup checklist for either path.

- **Chapter 06 (Security and Threat Model)**: Add GitHub's own fork-PR warning
  (Claim 9) as a first-party citation for the general principle "don't give an
  agent broad, unattended, `--yolo`-style access to a workflow triggered by
  untrusted (fork) input without additional isolation or a mediated-writes
  architecture." Pair it with the Safe Outputs mitigation
  (`docs-ghaw-safe-outputs-specification.md`) as the concrete alternative
  GitHub itself recommends (Agentic Workflows) for exactly this reason.

- **Chapter 04/05 (Cost Management)**: Note the shared `copilot-requests:
  write` permission and org-billing-policy prerequisite across both `gh aw`
  and direct Copilot CLI use (Claims 3–6), so cost-management guidance can be
  written once and applied to both surfaces rather than duplicated per-product.

## Extraction Notes

1. **Changelog + one linked how-to doc followed**: Per MINER.md §1, followed
   the changelog's single substantive outbound link
   (`docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli-in-actions`).
   That how-to doc contained the most guide-relevant material in the entire
   source (Claims 8–10: the Agentic-Workflows-first recommendation, the
   fork-PR warning, and the example workflow) — none of which appears in the
   changelog itself. A source note extracted from the changelog alone would
   have missed the most actionable content.
2. **Verbatim extraction method**: WebFetch's summarizing layer paraphrased
   content on both the changelog and the how-to doc across repeated attempts
   (confirmed by comparing two independent WebFetch passes on the changelog,
   which produced differently-worded summaries of the same facts). All quotes
   above were instead obtained by fetching raw HTML via `curl` and extracting
   the article/main content directly, then copying the exact text between
   tags character-for-character. This is a more reliable verbatim-extraction
   method than WebFetch alone and is noted here in case future Miner runs on
   github.blog or docs.github.com pages hit the same paraphrasing behavior.
3. **Example workflow's `GITHUB_TOKEN` env value**: The rendered HTML for the
   how-to doc's example workflow shows the `env:` block's value for
   `GITHUB_TOKEN` was present in the source but rendered as a bare `$` in the
   plain-text extraction (likely a `${{ ... }}` GitHub Actions expression that
   the HTML-to-text conversion mangled). The permission name, job structure,
   and all other lines were extracted cleanly and are exact. Flagged in
   Concrete Artifacts for the Assayer to verify directly against the live page
   if the exact expression syntax matters for the guide.
4. **No contradiction filed**: This source complements rather than contradicts
   `docs-ghaw-copilot-cloud-agent.md`'s PAT requirement for `gh aw` safe
   outputs — the two document different Copilot-invocation mechanisms. See
   Cross-References → Contradicts for the reasoning; no contradiction issue
   was warranted.
