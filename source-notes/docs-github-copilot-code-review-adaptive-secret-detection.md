---
source_url: https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more
source_type: docs
title: "Copilot code review: Adaptive effort, secret detection, and more"
author: GitHub (official changelog)
date_published: 2026-11-17
date_extracted: 2026-11-20
last_checked: 2026-11-20
status: current
confidence_overall: emerging
issue: "#4851"
---

# Copilot Code Review: Adaptive Effort, Secret Detection, and More

> GitHub's 2026-11-17 changelog adds Adaptive review effort (Copilot picks Lite/Balanced/Max per PR, capped by admin policy), in-review secret detection (deterministic regex plus LLM/ML), and cross-repository context, all in public preview, and announces Azure DevOps GA.

## Source Context

- **Type**: docs (GitHub official changelog, 2026-11-17, ~3 minute read, five sections).
- **Author credibility**: GitHub product team. Authoritative for what features exist, their preview/GA status, plan availability and config paths. Not authoritative for effectiveness: no recall, false-positive, cost or quality numbers are given.
- **Scope**: Five items. Preview vs GA status: Adaptive = public preview; cross-repository context = public preview (public repos only); secret detection = public preview; Repo Insights review-outcome tracking = no status stated (appears released); Azure DevOps = generally available. The page links to config and secret-scanning docs; those were not fetched, so the mechanics of how Adaptive scores complexity/risk are unspecified.

## Extracted Claims

### Claim 1: Adaptive lets Copilot choose Lite, Balanced, or Max for each pull request based on its complexity and risk (public preview)
- **Evidence**: Official changelog description; no metrics or description of the selection heuristics.
- **Confidence**: emerging (vendor-stated, preview)
- **Quote**: "Copilot looks at each pull request’s complexity and risk, then reviews it with Lite, Balanced, or Max."
- **Our assessment**: Automates the per-review effort choice introduced in the GA note. The selector is opaque (no stated signals), so teams cannot predict cost or depth per PR. No evidence that its choices match a human's.

### Claim 2: The changelog motivates Adaptive by the burden of manually choosing effort, with docs changes needing Lite and auth changes needing Max
- **Evidence**: Illustrative examples only.
- **Confidence**: anecdotal
- **Quote**: "A documentation update may only need Lite, while a change to authentication logic benefits from Max."
- **Our assessment**: Reasonable heuristic (scale scrutiny to blast radius), but it is an illustration, not a measured result.

### Claim 3: Each Adaptive review discloses which effort level was picked
- **Evidence**: Stated feature behavior.
- **Confidence**: emerging
- **Quote**: "Each review shows which effort level Adaptive picked."
- **Our assessment**: Makes the selector auditable after the fact, which matters for spotting under-reviewed risky PRs. Consistent with effort labels shown in timeline events in the GA note.

### Claim 4: Adaptive can be set per PR from the Reviewers bar or as the default at personal, repository, organization, or enterprise level; Balanced remains the default
- **Evidence**: Configuration description.
- **Confidence**: emerging
- **Quote**: "Balanced remains the default review effort level."
- **Our assessment**: Adaptive is opt-in; the safe default remains fixed Balanced. Teams must explicitly switch.

### Claim 5: Adaptive is bounded by the maximum effort level set by enterprise, organization, or repository
- **Evidence**: Stated policy rule plus a warning callout.
- **Confidence**: emerging
- **Quote**: "Adaptive never picks a level above the maximum review effort level set for your enterprise, organization, or repository."
- **Our assessment**: Important governance property: admins retain a cost/depth ceiling. A low max cap silently stops Adaptive from using Max on risky PRs, so the cap interacts with the "risky changes get a deeper look" promise.

### Claim 6: Cross-repository context lets review read related public repositories (dependents, docs, custom instructions, skills)
- **Evidence**: Feature description; public preview only for public repositories.
- **Confidence**: emerging
- **Quote**: "Cross-repository context is now in public preview for public repositories."
- **Our assessment**: Addresses a real blind spot (downstream consumers of a change), but the restriction to public repos excludes most enterprise multi-repo setups for now. Also an expanded context-ingestion surface (instructions/skills from other repos).

### Claim 7: Secret detection in reviews combines deterministic and non-deterministic methods and surfaces secrets as review comments (public preview)
- **Evidence**: Feature description; enabled in repo/org settings under Copilot → Code review.
- **Confidence**: emerging
- **Quote**: "Using both deterministic and non-deterministic approaches, Copilot code review points out exposed credentials in review comments, so you can remove them before you merge."
- **Our assessment**: Positions review as an extra pre-merge layer. Note "before you merge" only: a secret already pushed to a branch is already exposed, so this does not replace push protection.

### Claim 8: Known-format detection covers 500+ secret types via deterministic methods, built with partners
- **Evidence**: Vendor statement; partner program numbers.
- **Confidence**: emerging
- **Quote**: "These 500+ secret types use deterministic methods like regex to find secrets."
- **Our assessment**: The deterministic half is the same detector family as secret scanning. Trustworthy for known formats; no new capability versus existing scanning besides placement in review.

### Claim 9: Unformatted secrets are detected with LLMs and a purpose-built GitHub model
- **Evidence**: Vendor statement; no recall/FP numbers.
- **Confidence**: anecdotal (no measurements)
- **Quote**: "It uses LLMs and GitHub’s purpose-built model for secret to find exposed secrets."
- **Our assessment**: The only genuinely new part. Non-deterministic, so guide advice should treat it as best-effort advisory, not a gate. Unquantified.

### Claim 10: Adaptive, cross-repo context and secret detection are available on Pro, Pro+, Max, Business, Enterprise
- **Evidence**: Stated plan availability.
- **Confidence**: emerging
- **Quote**: "Adaptive, cross-repository context, and secret detection are available to Copilot Pro, Pro+, Max, Business, and Enterprise plans."
- **Our assessment**: Same plan set as GA effort levels; no extra plan gating beyond that.

### Claim 11: Repository Insights now shows how Copilot code review feedback is addressed and utilized per repository
- **Evidence**: Feature pointer to a separate doc.
- **Confidence**: emerging
- **Quote**: "You can now see how Copilot code review feedback is addressed and utilized in each repository."
- **Our assessment**: Provides the feedback loop needed to evaluate Adaptive/secret detection empirically; details live in the linked doc (not fetched).

### Claim 12: Copilot code review for Azure Repos moves from public preview to GA with Lite/Balanced defaults, branch policy, audit logs, and Azure billing
- **Evidence**: Feature list in the changelog.
- **Confidence**: settled for status (official); billing details vendor-stated
- **Quote**: "Copilot code review for Azure Repos, previously in public preview, is now generally available."
- **Our assessment**: Updates the June technical-preview note. Notably Azure DevOps supports Lite/Balanced defaults only (no Max or Adaptive stated).

## Concrete Artifacts

```
Settings path (secret detection), per changelog:
  repository or organization settings -> Copilot -> Code review

Adaptive selection: Reviewers bar (single PR) or default in personal /
repository / organization / enterprise settings.
Ceiling: max review effort level configured at enterprise/org/repo.

Azure DevOps (GA) controls listed: org/project/repo enablement; branch policy
for automatic review; Lite or Balanced default; custom instructions + skills;
audit log events; billing in GitHub AI credits to the linked Azure subscription.
```

(Attribution: GitHub changelog, 2026-11-17.)

## Cross-References

- **Corroborates**: `docs-github-copilot-code-review-effort-levels-ga.md` Claims 3–7 (per-review selection, org default, repo override, plan availability, effort label shown); Adaptive uses the same Lite/Balanced tiers and Balanced default.
- **Contradicts**: none found.
- **Extends**: `docs-github-copilot-code-review-effort-levels-ga.md` (Claim 8 describes Lite vs Balanced; Max and Adaptive are new here); `docs-github-copilot-code-review-azure-repos.md` Claims 1, 3, 4 (technical preview, AI-credit billing, pricing subject to change at GA) now updated to GA with billing to the Azure subscription; `docs-github-copilot-code-review-config-controls.md` (admin controls, ceiling semantics); `docs-github-copilot-repository-level-usage-metrics.md` (Repo Insights outcomes).
- **Novel**: Adaptive per-PR effort selection; Max as a named effort level; LLM-based secret detection inside code review; cross-repository context.

## Guide Impact

- **Chapter 03**: Where automated review is described as a verification layer, note that vendors are moving from fixed effort to risk-routed effort (Adaptive), and that selector choices are shown per review so teams can audit them. Treat as preview, unmeasured.
- **Chapter 05**: Record that Adaptive is capped by the enterprise/org/repo max; admins should set the cap deliberately because it bounds how deep risky PRs get reviewed.
- **Chapter 06**: Add that in-review secret detection is a deterministic (500+ formats) plus non-deterministic (LLM) layer that fires at review time; it complements, not replaces, push protection. Mark the LLM component as unquantified.

## Extraction Notes

- Fetched the full changelog page and read all five sections. Linked docs (configuration, secret scanning, Repo Insights, Azure DevOps) were not followed, so selector heuristics and Repo Insights details are unknown.
- Cross-reference claim numbers were verified against the headings in the cited notes.
- Product changelog: no independent metrics, failure data, or practitioner evidence; hence overall confidence "emerging".
