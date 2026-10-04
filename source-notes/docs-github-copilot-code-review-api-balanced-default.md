---
source_url: https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level
source_type: docs
title: "Copilot code review: API support and new default effort level"
author: GitHub (changelog)
date_published: 2026-10-02
date_extracted: 2026-10-04
last_checked: 2026-10-04
status: current
confidence_overall: settled
issue: "#3890"
---

# Copilot code review: API support and new default effort level

> GitHub makes Copilot code review requestable via REST and GraphQL APIs with a per-request effort level, and flips the "Default" effort level from Lite to Balanced (effective 2026-09-28).

## Source Context

- **Type**: docs (official GitHub product changelog, ~1 minute read)
- **Author credibility**: First-party vendor announcement; authoritative on what shipped, silent on rationale, cost impact, or measured quality.
- **Scope**: Two changes: (1) API-based review requests with optional effort level; (2) Balanced becomes the Default effort. Includes the settings navigation paths per level. Does NOT give endpoint names, request/response shapes, or permissions; no billing numbers.

## Extracted Claims

### Claim 1: Copilot code review can now be requested through the REST and GraphQL APIs, with a per-request effort level
- **Evidence**: Vendor changelog; GA on Pro, Pro+, Max, Business, Enterprise. No endpoint signatures given.
- **Confidence**: settled (that it shipped); anecdotal on usage details (none provided)
- **Quote**: "You can now request a GitHub Copilot code review through the REST and GraphQL APIs and set the review effort level for each request."
- **Our assessment**: Real new capability. Prior notes only cover UI/auto-trigger paths. Because the changelog gives no endpoint names, guide advice must point readers to GitHub docs rather than stating API shapes.

### Claim 2: The API path is meant for embedding reviews in scripts, workflows, and internal tools
- **Evidence**: Vendor statement of intent.
- **Confidence**: emerging
- **Quote**: "This lets you bring Copilot code review into your own scripts, workflows, and internal tools, so reviews can start from the systems your team already uses."
- **Our assessment**: Enables harness-style orchestration (e.g. effort chosen by risk classification of a change). Untested claim; no example provided.

### Claim 3: The effort level on an API request is optional
- **Evidence**: Vendor text.
- **Confidence**: settled
- **Quote**: "When you make a request, you can optionally set the review effort level for that review."
- **Our assessment**: Omitting it presumably falls back to the configured hierarchy (inference, not stated).

### Claim 4: Balanced is now the Default effort level for new and existing repos/orgs; explicit Lite selections were preserved
- **Evidence**: Vendor statement with effective date.
- **Confidence**: settled
- **Quote**: "the Default review effort level now uses Balanced for new and existing repositories and organizations using Copilot code review. If you explicitly selected Lite in your settings, that selection was respected. This change took effect September 28, 2026."
- **Our assessment**: Silent behavior change for anyone who left the setting at Default: reviews now cost more (see cross-refs on Balanced using more credits/Actions minutes). Teams tracking spend should check whether usage rose after 2026-09-28.

### Claim 5: The default change had been pre-announced on August 28, 2026
- **Evidence**: Self-reference in the changelog; the August 28 post itself was not fetched.
- **Confidence**: settled
- **Quote**: "As announced on August 28, 2026"
- **Our assessment**: Roughly one month notice. Candidate for a follow-up source.

### Claim 6: Effort level is configurable at enterprise, organization, repository, and personal scope, and lower levels override higher ones
- **Evidence**: Listed settings paths.
- **Confidence**: settled
- **Quote**: "Each level can override the one above it."
- **Our assessment**: Consistent with earlier notes; this entry adds the exact enterprise path (AI controls → Agents → Copilot code review).

## Concrete Artifacts

Settings paths (GitHub changelog, 2026-10-02):

```
Enterprise:   enterprise settings -> AI controls -> Agents -> Copilot code review
Organization: organization settings -> Copilot -> Code review
Repository:   repository settings -> Copilot -> Code review
Personal:     profile picture -> Copilot settings -> Copilot -> Code review
```

## Cross-References

- **Corroborates**: `docs-github-copilot-code-review-personal-enterprise-settings.md` Claim 6 (enterprise default with org/repo overrides) and Claim 5 (personal default effort); `docs-github-copilot-code-review-effort-levels-ga.md` Claim 3 (per-review effort choice, now extended to API requests).
- **Contradicts**: None filed. `docs-github-copilot-code-review-effort-levels-ga.md` Claim 8 quotes Lite as "(default)"; this source supersedes that with Balanced as of 2026-09-28. This is a temporal change (August GA text vs. later change), not a conflicting position, so no contradiction issue was filed. Claim 8 of that note is now stale.
- **Extends**: `docs-github-copilot-code-review-effort-levels-ga.md` (Claim 8 on Balanced using more AI credits and Actions minutes, now the default); `docs-github-copilot-code-review-personal-enterprise-settings.md` Claim 8 (which observed no programmatic request path existed as of Sept 23 — now it does, 9 days later); `docs-github-copilot-code-review-actions-billing.md` (cost implications).
- **Novel**: Programmatic (REST/GraphQL) review requests; the Balanced default switch and its date.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Where Copilot code review is discussed, note that reviews can be triggered programmatically with per-request effort, enabling risk-based effort selection in custom pipelines; link to GitHub API docs for signatures.
- **Chapter 05 (Team Adoption)**: Add a cost caveat that the Default effort is now Balanced (since 2026-09-28); teams wanting Lite must set it explicitly at the relevant scope.
- **Chapter 01 (Daily Workflows)**: Update any text stating Lite is the default review effort.

## Extraction Notes

- Fetched and read the full changelog page (short). Did not follow the linked August 28 announcement or "Configuring code review" docs; the triage-comment claim about specific endpoint signatures is not supported by the page.
- Triage comments said the default changed "from Lite"; the page implies this via the Lite-preserved wording but does not literally say "previously Lite."
