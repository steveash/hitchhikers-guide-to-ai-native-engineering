---
source_url: https://claude.com/resources/articles/introducing-claude-ship
source_type: blog-post
title: "Introducing Claude Ship"
author: Anthropic (Claude Code team; unsigned product announcement)
date_published: 2026-11-23
date_extracted: 2026-11-24
last_checked: 2026-11-24
status: current
confidence_overall: anecdotal
issue: "#4920"
---

# Introducing Claude Ship

> Vendor launch post for a review → fix → approve pipeline (Code Review, PR Steward, Claude Approvals) whose novel content is a repo-file approval policy ("a smarter CODEOWNERS") with observe-only rollout, and an explicit rule that the fixer agent does not approve or merge.

## Source Context

- **Type**: blog-post (vendor product announcement on claude.com Resources; 6 min read; includes two customer quotes)
- **Author credibility**: Anthropic describing its own product and its own Claude Code team's usage. First-party for the mechanics; all outcome numbers are vendor-reported with no methodology. Customer quotes are unnamed-company, title-only attributions.
- **Scope**: Product mechanics, rollout options, billing, and availability limits. It does not describe the policy file format, classifier syntax, or how PR Steward avoids loops (those live in the linked docs, which were not read).

## Extracted Claims

### Claim 1: The post-PR loop is the bottleneck once agents write most code, so review, fixes and approval are automated as one pipeline
- **Evidence**: Authorial framing; "On the Claude Code team, Claude writes most of our code". Product design rather than measurement.
- **Confidence**: anecdotal
- **Quote**: "we wanted everything after the PR to move that fast too."
- **Our assessment**: Consistent with the Code Review note's claim that review became the constraint. Framing, not evidence.

### Claim 2: Claude Ship is three components: Code Review (GA), PR Steward (beta), Claude Approvals (beta)
- **Evidence**: Product description.
- **Confidence**: settled (as a description of the product)
- **Quote**: "Claude Ship is made up of"
- **Our assessment**: Useful as a reviewer / fixer / approver separation of duties. Maturity differs: only Code Review is GA.

### Claim 3: Code Review uses multiple lenses and adversarially verifies findings before posting, with per-repo Quick / Standard / Deep levels
- **Evidence**: Mechanism description; no precision/recall data.
- **Confidence**: emerging
- **Quote**: "It collects findings, adversarially verifies them, categorizes them, and posts them to a PR."
- **Our assessment**: Corroborates the verifier-voting design in the Code Review note (Claim 5). The Quick/Standard/Deep tiers are a cost/depth dial not covered before.

### Claim 4: The Claude Code team's merged PRs more than doubled June–September while the reverted share fell by more than 40%
- **Evidence**: Vendor-reported, no baseline or methodology; explicitly attributed to Claude's review being "one layer of a broader process". Identical figure appears in the Code Review note (Claim 1), so it is not independent.
- **Confidence**: anecdotal
- **Quote**: "merged PRs more than doubled from June to September while the share reverted fell by more than 40%."
- **Our assessment**: Do not treat as a finding. Share-reverted falling while volume doubles is directional at best; the post itself says review is one layer among several.

### Claim 5: PR Steward fixes CI failures, merge conflicts and review feedback but is designed not to approve or merge
- **Evidence**: Design statement; no description of enforcement (permissions vs. policy).
- **Confidence**: emerging
- **Quote**: "works to keep a PR green, but is designed not to approve or merge pull requests."
- **Our assessment**: Separation of authority: the agent that edits code cannot be the one that approves it. "Designed not to" is softer than "cannot"; the post doesn't say whether this is enforced by token scope.

### Claim 6: PR Steward is auditable and steerable: it comments after every push with what changed and how to undo, and responds to `@claude` / `@claude stop`
- **Evidence**: Interface description.
- **Confidence**: emerging
- **Quote**: "After every push, it comments with what it changed and how to undo it."
- **Our assessment**: A concrete pattern for autonomous fixers (change narration plus revert instructions plus a kill phrase). Nothing said about loop caps; compare convergence controls in the Code Review note (Claim 10).

### Claim 7: Claude Approvals applies an approval policy stored as a file on the repo's default branch; it can approve routine changes or require human sign-off
- **Evidence**: Mechanism description: policy file in the repository; activation occurs when a connected repo has a policy file on its default branch; admin can turn it off.
- **Confidence**: emerging
- **Quote**: "It works like a smarter CODEOWNERS file."
- **Our assessment**: Policy-as-code for approval, versioned and reviewed like any file. Placing it on the default branch means policy changes go through normal review. The note does not say who may edit the file (no CODEOWNERS-for-the-policy detail).

### Claim 8: Policy inputs include Code Review findings and team-defined natural-language classifiers
- **Evidence**: Feature description; billing section adds that classifiers are billed per token and a policy using Claude's review triggers a billed Code Review even in observe mode.
- **Confidence**: emerging
- **Quote**: "including Code Review findings or their own classifiers using natural language."
- **Our assessment**: Productized form of the classifier-set risk tier in the Code Review note (Claim 7). Natural-language classifiers are non-deterministic gates; no accuracy data given.

### Claim 9: Roll out approvals in observe-only mode before making them a required branch-protection check
- **Evidence**: Vendor recommendation for most customers; admin settings add per-repo enablement, monthly spend limit, and review timing.
- **Confidence**: emerging
- **Quote**: "we recommend enabling this first in observe-only mode to build confidence before configuring branch protection to require Claude Approvals' green light."
- **Our assessment**: Shadow-mode-before-enforce is sound rollout practice for any AI gate. Note the hidden cost: observe mode still bills Code Review runs if the policy uses it.

### Claim 10: Claude Ship layers on, rather than replaces, existing branch protection and required checks; merge ability still depends on the developer's permissions
- **Evidence**: Admin and developer section statements.
- **Confidence**: emerging
- **Quote**: "Claude Ship works with existing branch protection and required checks."
- **Our assessment**: Keeps the deterministic gates under the agent layer. Good defense-in-depth stance.

### Claim 11: `/ship` in Claude Code pushes, opens the PR, reviews it and works feedback and failing checks
- **Evidence**: Command description; rolling out in Claude Code and the desktop app.
- **Confidence**: settled (as a feature description)
- **Quote**: "Claude pushes it, opens the PR, reviews the change, and works on feedback and failing checks to help get it ready to merge."
- **Our assessment**: Developer-side entry point; repo-level enablement removes the need to invoke it.

### Claim 12: Anecdote: a docs fix opened via Claude Tag went from report to merged in one evening with no human code review beyond a docs reviewer
- **Evidence**: Single vendor anecdote (Analytics API docs / Admin key confusion).
- **Confidence**: anecdotal
- **Quote**: "Code Review found nothing blocking, a docs reviewer signed off, Claude Approvals passed, and the fix merged that same evening."
- **Our assessment**: A low-risk docs change; illustrates the low-tier path only. Says nothing about high-risk changes.

### Claim 13: Cost and availability constraints: token-billed, Team/Enterprise on GitHub only, unavailable under ZDR, HIPAA configuration or customer-managed keys
- **Evidence**: Availability section.
- **Confidence**: settled
- **Quote**: "Claude Ship is not available to organizations with Zero Data Retention, the HIPAA configuration, or customer-managed encryption keys."
- **Our assessment**: Material adoption blocker for regulated orgs. Spend limits cover Code Review and PR Steward; the post doesn't mention a limit on Approvals classifiers.

### Claim 14: Customer testimonials say humans stay in the loop with time redirected to changes that need it
- **Evidence**: Two quotes, attributed by title only (Director of Engineering; SVP Engineering and Analytics); company names are not in the extracted text.
- **Confidence**: anecdotal
- **Quote**: "We keep a human in the loop, and the human’s time now goes to the changes that need it."
- **Our assessment**: Marketing testimonial; no evidence value beyond showing intended positioning.

## Concrete Artifacts

```
Claude Ship pipeline (source: "How Claude Ship works"):
  Code Review (GA)  -> findings, adversarially verified, Quick/Standard/Deep per repo
  PR Steward (beta) -> fixes CI, merge conflicts, review feedback; designed not to approve or merge
                       controls: "@claude <instruction>", "@claude stop"
  Claude Approvals (beta) -> approval policy file on default branch; signals = Code Review findings
                       and natural-language classifiers; recommended: observe-only first
Admin controls: per-repo enablement, review level, review timing, monthly spend limit
Billing: tokens; Approvals has no base charge; classifiers billed per token;
         Claude-review-based policy triggers billed Code Review even in observe mode
```

Vendor metrics (source text, unvalidated): merged PRs "more than doubled" June–Sept and reverted share down "more than 40%" on the Claude Code team. Promotion: at least $10,000 credits for eligible Enterprise orgs, claim by January 15, 2027.

## Cross-References

- **Corroborates**: `blog-claude-dev-claude-code-team-code-review.md` Claim 5 (verifier-voted findings) and Claim 7 (classifier-set approval tiers) and Claim 8 (agent approvals never count as a person's; here, the fixer cannot approve at all).
- **Contradicts**: None. Tension only: the Code Review note's Claim 14 says the team lacks circuit breakers to tighten approval when revert metrics move; this post offers observe mode and spend limits but no metric-driven circuit breaker.
- **Extends**: `blog-claude-dev-claude-code-team-code-review.md` by productizing its internal pipeline (policy-as-file, classifiers, fixer agent) and adding the PR Steward role, which the earlier note does not cover. The June–September metrics are the same figures as its Claim 1, not independent corroboration.
- **Novel**: Approval policy as a default-branch file with natural-language classifiers; observe-only mode before required-check enforcement; PR Steward's narrate-and-undo comment plus `@claude stop`; hidden observe-mode costs; ZDR/HIPAA/CMEK exclusions.

## Guide Impact

- **Chapter 02**: Add policy-as-file approval gates (default-branch policy file, "smarter CODEOWNERS") as a harness example, with the caveat that file format and edit-authorization were not documented in this post.
- **Chapter 03**: Add the reviewer / fixer / approver separation (fixer cannot approve or merge) alongside the existing verification-layer material; cite as vendor-described design.
- **Chapter 05**: Add observe-only-then-enforce rollout, per-repo enablement, spend limits, and the plan/data-residency exclusions as adoption considerations. Label all outcome metrics vendor-reported and non-independent.

## Extraction Notes

- Full article text read (fetched raw HTML and stripped markup); the linked setup guide and docs (code.claude.com/docs/en/claude-ship) were not followed, so policy-file syntax and PR Steward loop limits are unknown.
- Customer company names did not appear in extracted text; only titles and names appear in the quotes' attributions (names omitted here).
- Quotes are verbatim from the fetched page text.
