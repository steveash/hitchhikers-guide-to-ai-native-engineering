---
source_url: https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates
source_type: docs
title: "Copilot code review: API management and review overview updates"
author: GitHub (changelog)
date_published: 2026-11-06
date_extracted: 2026-11-08
last_checked: 2026-11-08
status: current
confidence_overall: settled
issue: "#4590"
---

# Copilot code review: API management and review overview updates

> GitHub makes Copilot code review settings manageable via REST and GraphQL from enterprise down to repo, exposes review-effort and cited-source attribution metadata, compacts the review overview comment, and runs Balanced reviews on three reviewer models plus a combiner.

## Source Context

- **Type**: docs (official GitHub changelog, 2026-11-06; applies to Pro, Pro+, Max, Business, Enterprise)
- **Author credibility**: First-party vendor announcement; authoritative on what shipped, silent on rationale, cost, or measured quality.
- **Scope**: Settings-management APIs and permissions, attribution fields, compact overview, 👎 reasons, Balanced ensemble, misc fixes. Does not give endpoint paths or payloads here; it links to the docs page "Configuring Copilot code review with the API" (not followed).

## Extracted Claims

### Claim 1: Code review settings can be managed via REST and GraphQL across enterprise, organization, and repository scopes
- **Evidence**: Vendor changelog.
- **Confidence**: settled (that it shipped)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Makes the effort hierarchy documented in the earlier notes scriptable, i.e. review config as code. Endpoint shapes are not in the changelog; point readers to the GitHub docs.

### Claim 2: Role-scoped management with upstream enforcement
- **Evidence**: Vendor description: enterprise admins can enable/disable review for all orgs or delegate to org admins; org admins manage enablement, default effort and runner config but cannot override enterprise-managed settings; repo admins manage effort and whether reviews use custom instructions and MCP tools.
- **Confidence**: settled
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Gives a three-tier governance model with enterprise as ceiling. Extends the runner lock concept from the config-controls note to all settings.

### Claim 3: Token support differs by scope
- **Evidence**: Enterprise and org endpoints (including org runner endpoint) do not support GitHub Apps or fine-grained PATs; repo endpoints support both, needing Administration read (read) / write (update); classic PATs need repo admin access.
- **Confidence**: settled
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Practical constraint: org/enterprise automation needs a classic PAT, a weaker credential. Worth a security caveat for config-as-code pipelines.

### Claim 4: The API exposes attribution metadata: review effort used and the skills, MCP servers, and custom instructions cited per comment
- **Evidence**: Vendor description.
- **Confidence**: settled (shipped); emerging (usefulness)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: A concrete observability hook for auditing what context the reviewer used, e.g. verifying that AGENTS.md or a skill actually influenced findings. No measurement of completeness given.

### Claim 5: Balanced-effort reviews use three reviewer models whose findings are combined by another model
- **Evidence**: Vendor statement, no benchmarks.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: A vendor-confirmed multi-reviewer ensemble with a combiner, an architecture pattern relevant to verification chapters. Since Balanced is the default (see the Oct 2 note), this explains higher cost. No quality or cost numbers.

### Claim 6: The review overview comment is more compact
- **Evidence**: Findings first; effort and surveys in footer; skipped and content-excluded files grouped under "Files not reviewed"; empty sections hidden; long lists show overflow count.
- **Confidence**: settled
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Continues the noise-reduction theme from the comment-UX note.

### Claim 7: A 👎 now prompts for a reason (disagreeable approval, verbose comments, incorrect or nitpicky findings)
- **Evidence**: Vendor description.
- **Confidence**: settled
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Structured feedback taxonomy; shows vendors' own view of review failure modes (false approval, verbosity, nitpicks).

### Claim 8: Smaller changes: AI credits shown in agent sessions; bypass list for the "Automatically request Copilot code review" rule; on later reviews, findings unrelated to recent changes are collapsed then hidden
- **Evidence**: Vendor list.
- **Confidence**: settled
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Bypass list matters for rulesets governance; credit visibility helps cost tracking.

### Claim 9: Reliability fixes: failed/timed-out reviews retried once with model fallback; bot-authored PRs (Actions, Dependabot, org/enterprise apps) can again request reviews under the external-license block when the org pays; billing/preview settings persist across off/on
- **Evidence**: Vendor bug-fix list.
- **Confidence**: settled
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Minor; noted only.

## Concrete Artifacts

No code or payloads in the changelog. Permission matrix (paraphrased from changelog):

```
Enterprise/org endpoints: no GitHub App, no fine-grained PAT (classic PAT, admin)
Repo endpoints: GitHub App + fine-grained PAT OK; Administration: read to read, write to update
Classic PAT: repo admin access required
```

## Cross-References

- **Corroborates**: `docs-github-copilot-code-review-effort-levels-ga.md` Claim 7 (effort label shown on reviews; now also in API) and Claims 4-5 (org default, repo override).
- **Contradicts**: None.
- **Extends**: `docs-github-copilot-code-review-api-balanced-default.md` Claim 1 (review request API; now settings API too) and Claim 6 (override hierarchy); `docs-github-copilot-code-review-config-controls.md` Claim 2 (runner lock; generalized to upstream-managed settings); `docs-github-copilot-code-review-personal-enterprise-settings.md` Claim 6 (enterprise default effort); `docs-github-copilot-code-review-comment-ux.md` Claim 3 (noise reduction); `docs-github-copilot-code-review-agents-md-ui.md` Claim 2 (AGENTS.md sourcing, now auditable).
- **Novel**: Settings-management API with token-type constraints; per-comment attribution of skills/MCP/instructions; Balanced three-model ensemble; 👎 reason taxonomy.

## Guide Impact

- **Chapter 02**: Note that Copilot review config and attribution are API-accessible, enabling audit that instructions/skills were actually used.
- **Chapter 03**: Cite the Balanced three-reviewer-plus-combiner design as a vendor example of ensemble review; mention 👎 reason categories as known failure modes.
- **Chapter 05**: Add enterprise → org → repo governance with non-overridable upstream settings, plus the token-type caveat for automation.

## Extraction Notes

- The fetch tool returned only a summarized version of the page, not verbatim text, so no verbatim quotes could be verified; all Quote fields are intentionally marked as having none, and content is paraphrased. The Assayer may want a manual check against the source.
- Did not follow the linked API docs page.
