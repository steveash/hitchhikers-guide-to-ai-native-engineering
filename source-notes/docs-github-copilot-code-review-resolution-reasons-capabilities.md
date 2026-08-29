---
source_url: https://github.blog/changelog/2026-08-27-copilot-code-review-resolution-reasons-and-expanded-capabilities
source_type: docs
title: "Copilot code review: Resolution reasons and expanded capabilities"
author: GitHub (official changelog)
date_published: 2026-08-27
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#3019"
---

# Copilot Code Review: Resolution Reasons and Expanded Capabilities

> GitHub's August 27, 2026 changelog announcing that Copilot code review can
> now review bot-authored pull requests (with billing routed to the org),
> gives Copilot cloud agent PRs a full agentic review instead of a fallback
> experience, has dropped its prior 300-file / 20,000-line size ceiling
> entirely, and lets users record why they resolved a review comment
> (Addressed / Won't fix / Incorrect) — cross-referenced against the linked
> "Copilot code review without a Copilot license" documentation section for
> the two-policy mechanics the changelog itself only names.

## Source Context

- **Type**: docs (GitHub official product changelog, August 27, 2026; ~230
  words across two sections — "🤖 Expanded capabilities" with three
  sub-sections, and "☑️ Comment resolution reasons" — plus the linked
  documentation section
  `https://docs.github.com/copilot/concepts/agents/code-review#copilot-code-review-without-a-copilot-license`,
  followed per MINER.md's linked-page-following guidance because it is the
  only substantive outbound link in the changelog article and it directly
  elaborates the "bot-authored pull requests" capability the changelog only
  summarizes in one sentence).
- **Author credibility**: GitHub engineering team announcing production
  feature changes on the official changelog. Authoritative for the fact that
  these capabilities exist, their names, the policy names required to enable
  them, and their plan-tier availability. Not authoritative for review
  quality on very large PRs now that the size ceiling is gone, for how often
  practitioners actually use the new resolution-reason dropdown, or for
  whether removing the file/LOC ceiling introduces latency or cost
  differences on very large reviews — none of that is measured or claimed in
  either the changelog or the linked docs page.
- **Scope**: Covers four specific capability changes to Copilot code review:
  bot-authored PR support (with the org-billing and policy mechanics pulled
  from the linked docs page), Copilot cloud agent PR review depth, removal of
  the PR size ceiling, and comment resolution reasons. The linked docs section
  additionally covers plan-tier gating, the two-policy enablement chain, IDE
  availability, a fixed file-type exclusion list, and two "agentic
  capabilities" (full project context gathering; passing suggestions to
  Copilot cloud agent). Does NOT cover: a quantified LOC/file count for how
  large a PR can now be (only that the prior ceiling "no longer applies"),
  what "full agentic review" actually adds over the prior CCA-PR fallback
  experience mechanically, how resolution-reason data is used by the product
  team beyond "feedback," or any metrics on adoption of any of these features.

## Extracted Claims

### Claim 1: Copilot code review previously had a 300-file or 20,000-line-of-code limit on the size of a pull request it could review, and this limitation no longer applies

- **Evidence**: Dedicated changelog sub-section titled "Large pull requests"
  under "🤖 Expanded capabilities."
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Copilot code review previously had a 300 file or 20,000 lines of code limit on the size of a pull request it could review. This limitation no longer applies."
- **Our assessment**: This is the first corpus source to document that Copilot
  code review ever had a size ceiling, and the first to document its removal
  — no existing source note mentions a 300-file or 20,000-LOC limit. The
  claim is a plain removal statement with no quantified replacement (no new
  cap, no "up to N files" figure), so the honest reading is "no documented
  limit," not "unlimited in practice" — very large monorepo-scale PRs may
  still hit undocumented practical ceilings (timeout, cost, or Actions
  runner limits) that this changelog does not address. For Ch02 (Harness
  Engineering): large refactors, bulk dependency bumps, and monorepo-wide
  changes that were previously out of scope for automated Copilot review are
  now in scope, but teams should not assume unbounded scalability without
  their own testing on their largest realistic PRs.

### Claim 2: Copilot code review can now review pull requests authored by bots, including Copilot cloud agent, and bill that review's usage to the organization when the org enables the "Allow members without a Copilot license" policy

- **Evidence**: Changelog sub-section "Pull requests authored by bots,"
  corroborated and substantially extended by the linked docs section
  "Copilot code review without a Copilot license."
- **Confidence**: settled (product fact stated in official changelog and
  official docs)
- **Quote**: "When a pull request is authored by a bot and requested automatically, there's no Copilot-licensed account to attribute the review to. With the "Allow members without a Copilot license to use Copilot code review in GitHub.com" policy enabled, Copilot code review can now review these pull requests and bill the usage directly to your organization." (changelog)
- **Quote**: "Organization members without a Copilot license can use Copilot code review on GitHub.com. An enterprise administrator or organization owner must enable it. This capability is available to organizations on Copilot Business and Copilot Enterprise plans." (linked docs section, "Copilot code review without a Copilot license")
- **Our assessment**: The changelog names one policy; the docs page reveals it
  is actually a two-policy chain (see Claim 5 below) and restricts the
  capability to Business/Enterprise plans — a plan-tier gate the changelog
  itself never states. Without following the linked page, a reader would not
  know this feature is unavailable on Pro/Pro+/Max. This is the mechanism
  that makes bot-authored-PR review (Claim 1's structural cousin) actually
  billable and attributable: bots don't hold Copilot seats, so GitHub needed
  a distinct org-billing path rather than attributing the review to a human
  license holder. For Ch05 (Team Adoption / TCO): any org running
  bot-authored automation (dependency-update bots, codegen bots, or Copilot
  cloud agent itself opening PRs) that wants those PRs reviewed by Copilot
  now needs Business or Enterprise, plus both policies enabled — this is a
  new TCO/plan-tier gate distinct from the AI-Credits-vs-Actions-minutes
  billing dimension already documented in
  `docs-github-copilot-code-review-actions-billing.md`.

### Claim 3: Previously, when Copilot code review was automatically requested on pull requests authored by Copilot cloud agent, it fell back to a limited experience; it can now give those pull requests a full agentic review

- **Evidence**: Changelog sub-section "Copilot cloud agent pull requests."
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Previously, when Copilot code review was automatically requested due to automatic review settings on pull requests authored by Copilot cloud agent, Copilot code review would fall back to a limited experience. Copilot code review can now give pull requests opened by Copilot cloud agent a full agentic review."
- **Our assessment**: This retroactively confirms a gap that no prior source
  note flagged: CCA-authored PRs were getting a degraded review experience
  under automatic review settings, not the same review depth as
  human-authored PRs. The changelog does not define what "limited experience"
  meant mechanically (fewer comments? no skills/MCP invocation? shallower
  context gathering?) nor precisely what "full agentic review" now adds —
  both are asserted, not itemized. Given the linked docs page separately
  states that "full project context gathering" and "the ability to pass
  suggestions to Copilot cloud agent" are "enabled automatically for all
  plans that include Copilot code review" (see Claim 7), a plausible reading
  is that the prior CCA-PR fallback skipped one or both of those
  capabilities — but this is inference, not a stated fact, and should be
  flagged as such if used in guide prose. For Ch04 (Agentic Workflows): teams
  that route Copilot cloud agent output through automatic Copilot code review
  as a self-review gate previously got a weaker check than a human-authored
  PR would; that gap is now closed, which strengthens the case for CCA→Copilot-review
  as a viable automated verification step in an agent pipeline.

### Claim 4: Users can now specify why they are resolving a Copilot code review comment, choosing "Addressed," "Won't fix," or "Incorrect" from a dropdown next to the "Resolve conversation" button

- **Evidence**: Dedicated changelog section "☑️ Comment resolution reasons."
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "You can now specify the reason for resolving a Copilot code review comment by either selecting "Addressed", "Won't fix", or "Incorrect", after clicking the new dropdown next to the "Resolve conversation" button, located at the bottom of any Copilot code review comment. Selecting one of these options provides valuable feedback to the product team and helps improve the product."
- **Our assessment**: This is a structured feedback-collection mechanism, not
  a workflow feature for the practitioner — the changelog frames the benefit
  entirely in terms of what it gives GitHub ("valuable feedback to the
  product team"), not what it gives the reviewer. It does, however, create an
  implicit practitioner-facing taxonomy for triaging Copilot suggestions:
  "Incorrect" as a distinct category from "Won't fix" means a team could, in
  principle, later query which suggestions were wrong (false positives) vs.
  which were correct-but-intentionally-skipped — though the changelog does
  not state that this data is exposed anywhere to the org (e.g., in the usage
  metrics API documented in
  `docs-github-copilot-code-review-usage-metrics-aggregate.md`). For Ch01
  (Daily Workflows): recommend practitioners actually use the distinction
  (not just always click the fastest option) since "Incorrect" is the signal
  most likely to influence future review quality, per the stated intent. For
  Ch05: this is a new, low-effort observability primitive for judging
  Copilot code review's false-positive rate at the team level, if and when
  the resolution-reason data becomes queryable — worth monitoring for a
  follow-up product announcement exposing it via the metrics API.

### Claim 5: Enabling Copilot code review for organization members without a Copilot license requires enabling two separate policies in sequence — "AI credits paid usage" first, then "Allow members without a Copilot license to use Copilot code review in GitHub.com" — and the second policy is disabled by default and is the most restrictive setting available

- **Evidence**: Linked docs page, "Enabling code review for users without a
  license" subsection.
- **Confidence**: settled (product configuration mechanics stated directly in
  official documentation)
- **Quote**: "To allow organization members without a Copilot license to use Copilot code review, you must enable two policies: AI credits paid usage. Enable this policy first. It allows the enterprise or organization to incur charges for Copilot code review AI credits usage. Allow members without a Copilot license to use Copilot code review in GitHub.com. This sub-policy enables Copilot code review for users without a license."
- **Quote**: "It is disabled by default. Once this policy is set at the enterprise level, it becomes visible, but not editable at the organization level. The policy is most restrictive. Copilot code review is only available in repositories under an organization where you have explicitly enabled the policy."
- **Our assessment**: This is significant operational detail the changelog
  itself never mentions — the changelog's single sentence ("With the ... policy
  enabled") implies a one-step toggle, but the docs page reveals a two-policy
  dependency chain plus a "most restrictive wins" enterprise-vs-org
  precedence rule (consistent in spirit with the org-runner lock precedence
  pattern already documented in
  `docs-github-copilot-code-review-config-controls.md`, Claim 2, though this
  is a distinct policy surface, not the same lock mechanism). Platform teams
  rolling this out need to enable "AI credits paid usage" before the
  sub-policy will even be effective, and need to know that once an enterprise
  admin sets the sub-policy, individual orgs can see but not override it. For
  Ch02 (Harness Engineering) and Ch05 (Team Adoption): document this as a
  two-step, enterprise-admin-gated rollout sequence, not a single toggle a
  team lead can flip unilaterally.

### Claim 6: Copilot code review for users without a Copilot license is not available in IDEs, and automatic code review (triggered regardless of author license status) still runs on all pull requests in a repository where it is enabled

- **Evidence**: Linked docs page, "How it works for users without a license"
  subsection.
- **Confidence**: settled (product behavior stated directly in official
  documentation)
- **Quote**: "In repositories where automatic code review is enabled, Copilot automatically reviews all pull requests. This happens regardless of whether the author has a Copilot license. For more information about how to configure automatic code review, see Configuring automatic code review by GitHub Copilot. Copilot code review for users without a license is not available in IDEs."
- **Our assessment**: This clarifies scope: the no-license capability is
  specifically about *requesting* a review (or being the author of a PR that
  gets auto-reviewed) on GitHub.com, not a general-purpose IDE feature grant.
  A contributor without a Copilot seat cannot get Copilot code review inside
  their IDE even under this policy — only via GitHub.com pull request flows.
  For Ch01 (Daily Workflows): if practitioners without a Copilot license ask
  why they can see PR-level Copilot reviews but get no Copilot assistance in
  their editor, this is the documented reason — it is a deliberate scope
  boundary, not a bug or partial rollout.

### Claim 7: Copilot code review has two "agentic capabilities" enabled automatically on all plans that include the feature — full project context gathering (analyzing the entire repository, not just the diff, for more accurate reviews) and the ability to pass suggestions to Copilot cloud agent to automatically open a new PR with the fix applied (in public preview)

- **Evidence**: Linked docs page, "Agentic capabilities for Copilot code
  review" subsection.
- **Confidence**: settled for the capability descriptions (official docs);
  the CCA-suggestion-passing piece is explicitly labeled preview, so
  emerging for that specific sub-capability
- **Quote**: "Copilot code review utilizes agentic capabilities to extend its functionality. Full project context gathering. This provides more specific, accurate, and contextually aware code reviews. This capability analyzes your entire repository to better understand the context of code changes. The ability to pass suggestions to Copilot cloud agent. This automates creating a new pull request against your branch with the suggested fixes applied. Passing suggestions to Copilot cloud agent is in public preview and subject to change. These capabilities are enabled automatically for all plans that include Copilot code review."
- **Our assessment**: "Full project context gathering" is new corpus
  vocabulary for a capability already implied but not named this precisely in
  `docs-github-copilot-code-review-skills-mcp-tier.md` (that note's framing:
  prior review "was limited to what the model could infer from the diff and
  repository context alone" before skills/MCP were added). This docs-page
  wording suggests context gathering is now a first-class, always-on
  capability distinct from the optional skills/MCP layer, though the exact
  relationship (is context gathering a prerequisite for skills/MCP
  invocation, or fully separate?) is not stated. The second capability —
  passing suggestions to CCA to auto-open a fix PR — is a distinct mechanism
  from the "Fix with Copilot" dialog documented in
  `docs-github-copilot-cca-apply-review-feedback.md` (that note's Claim 1:
  a UI dialog with application-target/model/instructions controls, invoked
  per-suggestion by a human). This docs-page capability describes an
  automated PR-opening flow rather than a human-driven dialog; whether these
  are the same underlying mechanism described from two different UI entry
  points, or genuinely separate features, is not resolved by either source.
  Flagged for the Assayer/Smith to reconcile if both are cited in the same
  guide section. For Ch02: both capabilities belong in the code review
  configuration/behavior surface as always-on defaults, not opt-in settings.

### Claim 8: Some file types are automatically excluded from Copilot code review regardless of configuration: dependency management files (e.g., package.json, Gemfile.lock), log files, and SVG files

- **Evidence**: Linked docs page, "Excluded files" subsection.
- **Confidence**: settled (product behavior stated directly in official
  documentation)
- **Quote**: "Some file types are excluded from Copilot code review: Dependency management files, such as package.json and Gemfile.lock. Log files. SVG files. If you include these file types in a pull request, Copilot code review will not review the file."
- **Our assessment**: This is a fixed, non-configurable exclusion list,
  distinct from the admin-configurable content exclusion feature (repository/
  organization/enterprise path-based rules) already documented in
  `docs-github-copilot-code-review-config-controls.md` (Claim 4). That
  feature lets admins choose what to exclude; this list is baked into the
  product and applies regardless of admin configuration. Practitioners who
  wonder why Copilot never comments on a `package-lock.json` or `.svg` change
  in a PR now have a documented answer — it's an unconditional product
  behavior, not a missed review. For Ch01: worth a short note in any "what
  Copilot code review does and doesn't cover" section, since dependency-file
  changes (a common source of supply-chain risk) are explicitly out of scope
  regardless of org policy.

## Concrete Artifacts

### Changelog Full Text (verbatim, August 27, 2026)

```
Title: Copilot code review: Resolution reasons and expanded capabilities
Published: August 27, 2026
Source: https://github.blog/changelog/2026-08-27-copilot-code-review-resolution-reasons-and-expanded-capabilities

Copilot code review can now review two types of pull requests it didn't
cover before:

  - Reviews requested automatically on pull requests authored by bots,
    including Copilot cloud agent
  - Very large pull requests

Additionally, you can now submit the reason for why you're resolving a
particular Copilot code review comment.

--- SECTION: 🤖 Expanded capabilities ---

Pull requests authored by bots

When a pull request is authored by a bot and requested automatically,
there's no Copilot-licensed account to attribute the review to. With the
"Allow members without a Copilot license to use Copilot code review in
GitHub.com" policy enabled, Copilot code review can now review these pull
requests and bill the usage directly to your organization. To learn more,
see Copilot code review without a Copilot license.

Copilot cloud agent pull requests

Previously, when Copilot code review was automatically requested due to
automatic review settings on pull requests authored by Copilot cloud agent,
Copilot code review would fall back to a limited experience. Copilot code
review can now give pull requests opened by Copilot cloud agent a full
agentic review.

Large pull requests

Copilot code review previously had a 300 file or 20,000 lines of code limit
on the size of a pull request it could review. This limitation no longer
applies.

--- SECTION: ☑️ Comment resolution reasons ---

You can now specify the reason for resolving a Copilot code review comment
by either selecting "Addressed", "Won't fix", or "Incorrect", after clicking
the new dropdown next to the "Resolve conversation" button, located at the
bottom of any Copilot code review comment. Selecting one of these options
provides valuable feedback to the product team and helps improve the
product.

Tags: copilot
```

### Linked Documentation Excerpt: "Copilot code review without a Copilot license" (verbatim)

```
Source: https://docs.github.com/copilot/concepts/agents/code-review#copilot-code-review-without-a-copilot-license
(followed from the changelog's "Copilot code review without a Copilot
license" link)

Organization members without a Copilot license can use Copilot code review
on GitHub.com. An enterprise administrator or organization owner must
enable it. This capability is available to organizations on Copilot
Business and Copilot Enterprise plans.

Enabling code review for users without a license

To allow organization members without a Copilot license to use Copilot code
review, you must enable two policies:

  - AI credits paid usage. Enable this policy first. It allows the
    enterprise or organization to incur charges for Copilot code review AI
    credits usage.
  - Allow members without a Copilot license to use Copilot code review in
    GitHub.com. This sub-policy enables Copilot code review for users
    without a license.

The second policy has these characteristics:

  - It is disabled by default.
  - Once this policy is set at the enterprise level, it becomes visible, but
    not editable at the organization level.
  - The policy is most restrictive. Copilot code review is only available in
    repositories under an organization where you have explicitly enabled the
    policy.

How it works for users without a license

When both policies are enabled, users without a Copilot license can request
a review from Copilot code review on their pull requests in the
organization's repositories.

In repositories where automatic code review is enabled, Copilot
automatically reviews all pull requests. This happens regardless of whether
the author has a Copilot license. For more information about how to
configure automatic code review, see Configuring automatic code review by
GitHub Copilot.

Copilot code review for users without a license is not available in IDEs.

Excluded files

Some file types are excluded from Copilot code review:

  - Dependency management files, such as package.json and Gemfile.lock
  - Log files
  - SVG files

If you include these file types in a pull request, Copilot code review will
not review the file. For more information, see Files excluded from GitHub
Copilot code review.

Agentic capabilities for Copilot code review

Copilot code review utilizes agentic capabilities to extend its
functionality.

  - Full project context gathering. This provides more specific, accurate,
    and contextually aware code reviews. This capability analyzes your
    entire repository to better understand the context of code changes.
  - The ability to pass suggestions to Copilot cloud agent. This automates
    creating a new pull request against your branch with the suggested
    fixes applied. Passing suggestions to Copilot cloud agent is in public
    preview and subject to change.

These capabilities are enabled automatically for all plans that include
Copilot code review.
```

### Feature Summary Table

```
Copilot Code Review — Resolution Reasons and Expanded Capabilities (Aug 27, 2026)

Feature 1: Bot-authored PR review
  Requires:   "AI credits paid usage" policy (enterprise/org), THEN
              "Allow members without a Copilot license to use Copilot code
              review in GitHub.com" sub-policy (disabled by default)
  Plan gate:  Copilot Business or Copilot Enterprise only
  Billing:    Usage billed directly to the organization
  IDE:        Not available — GitHub.com pull request flows only

Feature 2: Copilot cloud agent PR review
  Before:     Fallback to a "limited experience" under automatic review settings
  After:      Full agentic review

Feature 3: Large pull request support
  Before:     300 file or 20,000 LOC ceiling
  After:      No stated ceiling ("this limitation no longer applies")

Feature 4: Comment resolution reasons
  Options:    Addressed | Won't fix | Incorrect
  Location:   Dropdown next to "Resolve conversation" button, bottom of comment
  Stated purpose: Feedback signal to the GitHub product team

Always-on (all plans with code review):
  - Full project context gathering (whole-repo analysis, not diff-only)
  - Passing suggestions to Copilot cloud agent to auto-open a fix PR (preview)

Always-excluded file types (non-configurable):
  - Dependency management files (package.json, Gemfile.lock, etc.)
  - Log files
  - SVG files
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-actions-billing.md` (issue
  #445): That note established the AI-Credits + Actions-minutes dual billing
  model for Copilot code review generally (Claims 1, 4) and that
  "non-licensed users billed via direct org billing" was already a covered
  category for the *pre-existing* billing structure (Claim 4 of that note).
  This source's Claim 2 and Claim 5 add the specific, previously-undocumented
  enablement mechanism for that category as it applies to *automated,
  bot-authored* reviews: the two-policy chain and the Business/Enterprise
  plan gate. The April 27 note established that non-licensed billing exists
  as a category; this source establishes exactly how an org turns it on for
  bot-authored PRs and what plan tier is required.

- **Extends** `docs-github-copilot-code-review-config-controls.md` (issue
  #1168): That note's Claim 2 documented org-level runner-setting lock
  enforcement ("organizational defaults override repository-level runner
  configurations... the policy is most restrictive" in spirit). This source's
  Claim 5 documents a structurally similar enterprise-over-organization
  precedence rule for a different policy (no-license code review access):
  "most restrictive" wins, and enterprise-level settings become
  visible-but-not-editable at the org level. Note this is a distinct policy
  from the runner lock — cite both as separate instances of the same
  enterprise-governance pattern, not the same control. That note's Claim 4
  (admin-configurable content exclusion at repo/org/enterprise levels) is
  also distinct from this source's Claim 8 (fixed, non-configurable file-type
  exclusion list) — the guide should not conflate the two exclusion
  mechanisms.

- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md` (issue
  #1052): That note's Extraction Notes/Claim framing described pre-skills
  review as "limited to what the model could infer from the diff and
  repository context alone." This source's Claim 7 gives that
  now-superseded-sounding limitation a specific named replacement — "full
  project context gathering," analyzing the entire repository rather than
  the diff alone — stated as always-on for all plans, distinct from the
  optional skills/MCP customization layer that note documents.

- **Extends** `docs-github-copilot-cca-apply-review-feedback.md` (issue
  #723 area, per that note's own issue reference): That note's Claim 1–2
  documented the "Fix with Copilot" dialog as a human-driven, per-suggestion
  UI control (application target, model, instructions) replacing an implicit
  comment-based invocation. This source's Claim 7 (second bullet) describes
  a capability with similar surface effect — passing a suggestion to Copilot
  cloud agent to auto-open a fix PR — but framed as an always-on, automatic
  "agentic capability" in public preview, not a dialog a human configures per
  invocation. Whether these are the same underlying mechanism viewed from two
  documentation angles, or two distinct features (a manual dialog vs. an
  automatic pass-through), is not resolved by either source. Flagged
  explicitly for the Assayer/Smith — do not merge these into a single guide
  claim without further verification.

- **Extends** `docs-github-copilot-code-review-effort-levels-ga.md` (issue
  #2585): That note's Claim 9 established that code review has no
  user-facing model switching and uses "a carefully tuned mix of models,
  prompts, and system behaviors." This source's removal of the size ceiling
  (Claim 1) and the CCA-PR fallback-to-full-review upgrade (Claim 3) are both
  changes to *review scope/depth*, not to the underlying model-routing
  policy that note documents — the two dimensions (effort level: Lite/
  Balanced; scope: what PRs qualify for review at all) remain independent
  configuration axes as far as either source states.

- **Corroborates**: No existing source note directly corroborates any of
  this source's four headline claims (bot-authored PR review, CCA-PR full
  review, size-ceiling removal, resolution reasons) — see Novel, below.

- **Contradicts**: None found. No existing source note claims Copilot code
  review has no size limit (this source is the first to reveal the limit
  existed at all, then document its removal), that bot-authored PRs cannot be
  reviewed, or that CCA-authored PRs always received full review depth. No
  contradiction issue filed per MINER.md §4a.

- **Novel**:
  - First corpus source to document that Copilot code review ever had a
    300-file / 20,000-LOC size ceiling, and the first to document its
    removal.
  - First corpus source to document Copilot code review support for
    bot-authored pull requests, including the org-billing attribution
    mechanism and the two-policy enablement chain (AI credits paid usage →
    Allow members without a Copilot license).
  - First corpus source to document that Copilot cloud agent PRs previously
    received a degraded ("limited") review experience under automatic review
    settings, and that this has been upgraded to full agentic review.
  - First corpus source to document comment resolution reasons (Addressed /
    Won't fix / Incorrect) as a feedback-collection mechanism in Copilot code
    review.
  - First corpus source to name "full project context gathering" as a
    specific, always-on agentic capability of Copilot code review across all
    plans.
  - First corpus source to document a fixed, non-configurable file-type
    exclusion list (dependency files, log files, SVG files) for Copilot code
    review, distinct from admin-configurable content exclusion.
  - First corpus source to document the enterprise-vs-organization
    visible-but-not-editable precedence behavior for a Copilot code review
    policy outside the runner-lock context.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Update the "code review configuration
  surface" material (built across `docs-github-copilot-code-review-skills-mcp-tier.md`,
  `docs-github-copilot-code-review-config-controls.md`, and
  `docs-github-copilot-code-review-effort-levels-ga.md`) to add: (1) the
  removed size ceiling — large refactors and monorepo-scale PRs are now
  in-scope for automated review, with the caveat that no replacement limit is
  documented; (2) "full project context gathering" as a named, always-on
  capability distinct from the optional skills/MCP layer; (3) the fixed
  file-type exclusion list (dependency files, logs, SVGs) as a hardcoded
  behavior separate from admin-configurable content exclusion. Recommend the
  Smith flag the CCA-suggestion-passing-vs-"Fix with Copilot"-dialog overlap
  (see Cross-References) for follow-up verification before writing prose that
  treats them as one feature.
- **Chapter 04 (Agentic Workflows)**: Update any guidance on using Copilot
  code review as an automated check on Copilot-cloud-agent-authored PRs — the
  prior "limited experience" fallback for CCA PRs under automatic review
  settings is gone; CCA PRs now get the same full agentic review as
  human-authored PRs. This strengthens the case for chaining CCA → automatic
  Copilot code review as a verification gate in an agent pipeline, though
  neither source quantifies the practical difference in review quality
  between the old fallback and the new full review.
- **Chapter 05 (Team Adoption / Tool Evaluation)**: Add to any GitHub Copilot
  TCO or rollout playbook: (1) reviewing bot-authored PRs (dependency-update
  bots, codegen bots, CCA itself) now requires Copilot Business or Enterprise
  plus a two-policy enablement chain — a new plan-tier and configuration gate
  distinct from the AI-Credits/Actions-minutes billing dimension already
  documented; (2) the enterprise-set-then-org-visible-but-not-editable
  precedence pattern for this policy, which platform teams should plan around
  when deciding whether to set it at the enterprise or org level; (3) the
  new resolution-reason dropdown as a potential future observability source
  for Copilot code review false-positive rate, worth watching for exposure
  via the usage metrics API documented in
  `docs-github-copilot-code-review-usage-metrics-aggregate.md`.
- **Chapter 01 (Daily Workflows)**: Add practitioner-facing notes: (1) when
  resolving a Copilot code review comment, the resolution-reason dropdown now
  exists and should be used deliberately — "Incorrect" is the signal most
  likely to influence future review quality per GitHub's stated intent; (2)
  Copilot code review will never comment on dependency-management files, log
  files, or SVGs, regardless of org configuration — this is expected
  behavior, not a coverage gap; (3) contributors without a Copilot license
  may now see Copilot reviews on their GitHub.com PRs (if their org enabled
  the policy) but will not get Copilot code review assistance inside their
  IDE — the capability is GitHub.com-only for non-licensed users.

## Extraction Notes

1. **WebFetch summarization avoided for quotes**: An initial WebFetch call
   against the changelog URL returned an AI-restructured version of the page
   (correct in substance, reorganized with headers). All quotes in this note
   were instead sourced from a direct `curl` fetch of the raw changelog HTML,
   with the `<article>` element isolated, tags stripped, and HTML entities
   unescaped programmatically — then cross-checked line-by-line against the
   WebFetch summary for consistency. The same direct-fetch approach was used
   for the linked documentation page.
2. **One linked page followed**: Per MINER.md's instruction to follow
   substantive linked pages, the changelog's only content link —
   `https://docs.github.com/copilot/concepts/agents/code-review#copilot-code-review-without-a-copilot-license`
   — was fetched. It is the source of Claims 5, 6, 7, and 8, and the
   plan-tier gate detail folded into Claim 2. All other links on the
   changelog page were same-page anchor links (table of contents) or the
   "copilot" tag-browse link, neither substantive.
3. **No quantified replacement for the removed size limit**: The changelog
   states the 300-file/20,000-LOC limit "no longer applies" but does not
   state a new limit, if any. Any guide content should avoid implying
   "unlimited" — the honest claim is "no documented limit as of this
   changelog."
4. **CCA-suggestion-passing vs. "Fix with Copilot" dialog not reconciled**:
   Flagged explicitly in Cross-References. This is a genuine open question
   from reading both sources closely, not an oversight — the two features
   may be the same underlying mechanism or two different ones, and neither
   source states which. Recommend the Assayer or Smith investigate directly
   (e.g., by triggering both flows) before conflating them in guide prose.
5. **No contradictions to file**: This source documents capability additions
   and removals (a limit going away, a fallback experience being upgraded)
   with no existing corpus source asserting the contrary present-tense state.
   No contradiction issue filed per MINER.md §4a.
