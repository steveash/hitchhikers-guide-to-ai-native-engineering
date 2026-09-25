---
source_url: https://github.blog/changelog/2026-09-23-copilot-code-review-more-ways-to-request-and-configure-reviews
source_type: docs
title: "More ways to request and configure Copilot code reviews"
author: GitHub (official changelog)
date_published: 2026-09-23
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: settled
issue: "#3690"
---

# More Ways to Request and Configure Copilot Code Reviews

> GitHub's September 23, 2026 changelog announcing two GA improvements to Copilot code
> review's configuration surface: a dedicated personal settings page (now available on
> every Copilot plan, not just Pro/Pro+/Max) with separate toggles for automatic review
> on new pushes and on draft pull requests plus a personal default review-effort setting,
> and a new enterprise-wide default review-effort level that inherits down to
> organization-owned repositories. Despite the title's "more ways to request" framing,
> this entry adds no new *trigger mechanism* (no comment-based or API-based request path) —
> it only adds a fourth governance layer (enterprise) and a practitioner-scoped default to
> the effort-level precedence chain already documented by the June 2 and August 7, 2026
> changelogs.

## Source Context

- **Type**: docs (GitHub official product changelog, September 23, 2026; tagged "copilot",
  "1 minute read", ~230 words across two sections). Fetched via direct `curl` of the raw
  HTML (the redirect-following canonical URL ends in a trailing slash) and HTML-stripped
  for verbatim text, not via AI-summarizing WebFetch, so all quotes below are
  character-verified against the live page.
- **Author credibility**: GitHub engineering/product team announcing production feature
  changes as already GA ("These improvements are now generally available"). Authoritative
  for the existence of the settings page, the toggles it exposes, the trigger conditions
  for automatic review, and the enterprise default-effort mechanism. Not authoritative for
  precedence when a personal default and an org/repo default conflict for the same review —
  the source states each setting's own scope but does not give a single combined precedence
  statement covering all four layers (enterprise, org, repo, personal/per-review) at once.
- **Scope**: Covers exactly two features: (1) an expanded, more granular personal
  Copilot-code-review settings page, and (2) an enterprise-level default review-effort
  setting. Does NOT cover: any new way to *trigger* a review (no comment-trigger, no API,
  no automation-workflow change — contrary to what the title alone might suggest); the
  underlying model-routing mechanics of Lite/Balanced (covered by
  `docs-github-copilot-code-review-effort-levels-ga.md`); or how the new enterprise default
  interacts with `docs-github-copilot-global-model-policy-ga.md`'s enterprise/org model-policy
  hierarchy, a structurally similar but functionally separate governance surface. No linked
  documentation pages were present in the article body to follow (checked; only boilerplate
  GitHub privacy/terms links appear in the raw HTML — see Extraction Notes).

## Extracted Claims

### Claim 1: GitHub shipped two GA improvements to Copilot code review configuration on September 23, 2026: an expanded personal settings page and an enterprise-wide default review effort
- **Evidence**: Opening summary paragraph of the changelog.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "GitHub Copilot code review now offers additional personal configurations to an expanded set of Copilot plans and an enterprise-level default setting. These improvements are now generally available:"
- **Our assessment**: Unlike the Low/Medium → Lite/Balanced arc (`docs-github-copilot-code-review-skills-mcp-tier.md` preview, `docs-github-copilot-code-review-effort-levels-ga.md` GA), both features here ship directly as GA with no preview period documented. This is a configuration-surface expansion, not a new capability of the review agent itself — nothing here changes what Copilot analyzes or how.

### Claim 2: The personal code-review settings page, previously restricted to Copilot Pro, Pro+, and Max users on the general "Copilot features" page, is now a dedicated "code review" page available under every Copilot plan, including Business and Enterprise
- **Evidence**: "⚙️ Manage your personal review settings" section, contrasting prior and current state.
- **Confidence**: settled (plan-availability fact stated directly in the changelog)
- **Quote**: "Previously, personal Copilot code review settings were available only with Copilot Pro, Pro+, and Max on the \"Copilot features\" page. They covered a single automatic review setting without separate controls for draft pull requests or new pushes."
- **Quote**: "Under your profile → Copilot settings, a dedicated \"code review\" page under Copilot is now available on every Copilot plan, including Copilot Business and Copilot Enterprise."
- **Our assessment**: This closes a plan-tier gap: Business and Enterprise users — who make up the fleet-adoption audience this corpus's Ch05 material is written for — previously had no personal automatic-review controls at all (only org/repo-level admin settings existed for them). Business/Enterprise practitioners now get the same self-service controls Pro/Pro+/Max users already had. For Ch05 (Team Adoption): this removes a prior asymmetry where individual contributors on Business/Enterprise plans could not opt into or granularly configure automatic review for their own pull requests.

### Claim 3: The new settings page separates the previously-single automatic-review toggle into independent controls for automatic review on new pushes and automatic review on draft pull requests
- **Evidence**: Direct contrast between the "single automatic review setting without separate controls" (prior state) and the "Turn on automatic review for new pushes and for draft pull requests you create or coauthor" bullet (new state).
- **Confidence**: settled (stated directly in the changelog)
- **Quote**: "Turn on automatic review for new pushes and for draft pull requests you create or coauthor."
- **Our assessment**: This is a genuine granularity increase, not a renaming. Previously a practitioner could not, for example, enable automatic review on every push while declining automatic review on draft PRs (or vice versa) — one toggle controlled both. Draft-PR review is a meaningfully different use case (early, incomplete-code feedback while iterating) from new-push review on an already-open, non-draft PR (feedback on incremental changes to reviewable code); separating the toggles lets practitioners opt into one without the other. For Ch01 (Daily Workflows): update any description of "the automatic review toggle" (singular) to reflect the two independent controls.

### Claim 4: Automatic review from Copilot triggers on three practitioner actions: creating a pull request, coauthoring a pull request, or moving a pull request out of draft state
- **Evidence**: Bulleted list of settings-page capabilities.
- **Confidence**: settled (stated directly in the changelog)
- **Quote**: "Turn on automatic reviews from Copilot, which will trigger when you create a pull request, coauthor a pull request, or move a pull request out of draft state."
- **Our assessment**: This is the first corpus source to enumerate the exact trigger-event list for automatic Copilot code review as a named set of three conditions. Note this is a *pull-request-lifecycle* trigger list, distinct from the comment-based trigger mechanism documented in `docs-github-copilot-automations-comment-trigger.md` (issue #2472) — that source covers Copilot cloud agent *automations* (scheduled/issue-creation/PR-open/PR-sync/comment-matched jobs), a different product surface from code review's own automatic-review toggle. The two should not be conflated in guide prose: automations run arbitrary agent tasks on a trigger; automatic code review specifically reviews a PR on these three lifecycle events.

### Claim 5: Practitioners can set a personal default review effort (Lite or Balanced) from the settings page; this default applies to reviews they request, including automatically-triggered reviews of their own pull requests, but a different effort can still be chosen at the moment of manually requesting a review
- **Evidence**: Settings-page bullet list plus the paragraph explaining scope and override behavior.
- **Confidence**: settled (stated directly in the changelog)
- **Quote**: "Set your default review effort, shown today as Lite or Balanced."
- **Quote**: "Your default effort applies to reviews you request, including reviews configured to automatically review your pull request. When manually requesting a review from Copilot via the pull request page under \"Reviewers\", you can still select a different review effort before requesting."
- **Our assessment**: This adds a fourth precedence layer to the hierarchy `docs-github-copilot-code-review-effort-levels-ga.md` documented as three tiers (org default → repo override → per-review choice). This source's personal default sits alongside that chain but is scoped specifically to reviews the *practitioner themselves* requests (as PR author/coauthor), whereas the org/repo defaults from the August 7 source govern reviews generally for a repository. The source does not state a single combined precedence rule spanning enterprise, org, repo, and personal defaults simultaneously — it only confirms each layer's own scope and that an explicit per-review choice always wins for that one review. The Assayer/Smith should treat "which default wins when personal and repo/org defaults conflict for a self-authored PR" as an open question this source does not resolve.

### Claim 6: Authorized enterprise administrators can now set a single default review effort — Lite, Balanced, or "the GitHub default" — for the whole enterprise, which inherits to organization-owned repositories while organizations and repositories retain their own override capability
- **Evidence**: "🏢 Set an enterprise default review effort" section.
- **Confidence**: settled (new configuration surface, stated directly in the changelog)
- **Quote**: "Authorized enterprise administrators can now set one default review effort (i.e., Lite, Balanced, or the GitHub default) for the whole enterprise. The default applies to organization-owned repositories through inheritance. Organizations and repositories can still set their own overrides."
- **Our assessment**: This is the first corpus source to document an enterprise-level tier in the review-effort hierarchy, extending the three-tier chain from `docs-github-copilot-code-review-effort-levels-ga.md` (org default → repo override → per-review choice) to four tiers: enterprise default → org default → repo override → per-review choice. The explicit phrase "Organizations and repositories can still set their own overrides" confirms the new enterprise tier is additive (a fallback), not a replacement — consistent with the non-destructive, override-preserving pattern this corpus has already observed for org-level runner locks (`docs-github-copilot-code-review-config-controls.md`, Claim 2) and org-level model policy (`docs-github-copilot-global-model-policy-ga.md`). For Ch02 (Harness Engineering): document the full four-tier precedence chain as the current (September 2026) state of the effort-level configuration surface.

### Claim 7: "The GitHub default" is offered as a distinct, named third option alongside Lite and Balanced for the enterprise-level setting, implying a GitHub-chosen baseline that is not itself simply "Lite" or "Balanced"
- **Evidence**: Parenthetical enumeration of the enterprise setting's options.
- **Confidence**: emerging (the option is named but its actual behavior — whether it is a fixed value, a rolling default GitHub can change over time, or something else — is not explained)
- **Quote**: "one default review effort (i.e., Lite, Balanced, or the GitHub default)"
- **Our assessment**: This is novel to the corpus: no prior source names a "GitHub default" as a selectable value distinct from an explicit Lite/Balanced choice. It reads as an escape hatch letting enterprises defer to whatever GitHub currently ships as its own default (likely Lite, per `docs-github-copilot-code-review-skills-mcp-tier.md` Claim 9's "Low[/Lite] remains a fast, cost-efficient default"), rather than pinning to a specific named tier that could become the "wrong" choice if GitHub changes its own default later. The source does not confirm this interpretation explicitly — flagged as an open question for the Assayer.

### Claim 8: Despite the changelog's title referencing "more ways to request" reviews, the entry introduces no new review-trigger mechanism (no comment-based trigger, no API/programmatic request path, no automation-workflow change) — the only "request"-adjacent change is the personal default-effort setting applying to manually requested reviews
- **Evidence**: Full-text reading of both sections; absence of any trigger-mechanism content beyond the three PR-lifecycle events (Claim 4, which already existed conceptually as "automatic review") and the existing manual "Reviewers" request path (already documented by `docs-github-copilot-code-review-effort-levels-ga.md` Claim 3).
- **Confidence**: settled (absence-of-claim assessment based on direct reading of the complete source text)
- **Quote**: (no direct quote; this is the Miner's synthesis from the absence of any trigger-mechanism language in the full verbatim text — see Concrete Artifacts)
- **Our assessment**: This directly addresses the Prospector's triage question ("What new request mechanisms... are introduced?"). The answer is: none beyond what August 7's changelog already established (manual request via "Reviewers," per-review effort choice). The "more ways to request" framing in the title refers to the *configuration* of who/what triggers automatic review (Claims 3–4) and *how effort defaults to a personal preference* (Claim 5), not to a new triggering channel like a PR/issue comment command. Teams expecting a comment-triggered code-review request (analogous to `docs-github-copilot-automations-comment-trigger.md`'s comment-triggered automations) will not find one here.

## Concrete Artifacts

### Changelog Full Text (verbatim, September 23, 2026, curl-extracted)

```
Title: More ways to request and configure Copilot code reviews
Published: September 23, 2026 (1 minute read)
Source: https://github.blog/changelog/2026-09-23-copilot-code-review-more-ways-to-request-and-configure-reviews/
Tags: copilot

GitHub Copilot code review now offers additional personal configurations to
an expanded set of Copilot plans and an enterprise-level default setting.
These improvements are now generally available:

  - A dedicated personal settings page for automatic review and your
    default review effort
  - An enterprise-wide default review effort setting for organization-owned
    repositories

--- SECTION: ⚙️ Manage your personal review settings ---

Previously, personal Copilot code review settings were available only with
Copilot Pro, Pro+, and Max on the "Copilot features" page. They covered a
single automatic review setting without separate controls for draft pull
requests or new pushes.

Under your profile → Copilot settings, a dedicated "code review" page under
Copilot is now available on every Copilot plan, including Copilot Business
and Copilot Enterprise. From this page you can:

  - Turn on automatic reviews from Copilot, which will trigger when you
    create a pull request, coauthor a pull request, or move a pull request
    out of draft state.
  - Turn on automatic review for new pushes and for draft pull requests you
    create or coauthor.
  - Set your default review effort, shown today as Lite or Balanced.

Your default effort applies to reviews you request, including reviews
configured to automatically review your pull request. When manually
requesting a review from Copilot via the pull request page under
"Reviewers", you can still select a different review effort before
requesting.

--- SECTION: 🏢 Set an enterprise default review effort ---

Authorized enterprise administrators can now set one default review effort
(i.e., Lite, Balanced, or the GitHub default) for the whole enterprise. The
default applies to organization-owned repositories through inheritance.
Organizations and repositories can still set their own overrides.
```

### Effort-Level Precedence Chain (updated to September 23, 2026)

```
Precedence (most specific wins for a given review):

1. Per-review practitioner choice (GA Aug 7, 2026)
   → Selected when manually requesting the review via "Reviewers"; applies
     to that review only.

2. Personal default effort (NEW, GA Sept 23, 2026)
   → Applies to reviews the practitioner themselves requests, including
     auto-triggered reviews of their own PRs, when no explicit per-review
     choice is made. Configured under profile → Copilot settings → code
     review.

3. Repository-level override (existed since June 2, 2026 preview,
   repository settings → Copilot → Code review → Review effort level)

4. Organization-level default (GA Aug 7, 2026,
   organization settings → Copilot → Copilot code review)
   → Applied when a repository has not configured its own effort level.

5. Enterprise-level default (NEW, GA Sept 23, 2026: Lite, Balanced, or
   "the GitHub default")
   → Applies to organization-owned repositories through inheritance when
     no org- or repo-level override is set.

NOTE: The source does not state the precedence between layer 2 (personal
default) and layers 3-5 explicitly for the case of a self-authored PR in a
repository/org/enterprise that has also set its own default. Layers 1 and
5 (and the org/repo layers between them) are confirmed by direct quotes;
the exact position of layer 2 relative to layers 3-4 is the Miner's
placement based on scope language ("reviews you request"), not a stated
precedence rule.
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-effort-levels-ga.md` (issue #2585):
  - That source's "Effort-Level Configuration Hierarchy" artifact documented three
    tiers: per-review choice → repository override → organization default. This
    source's Claim 6 adds a fourth, top-most tier (enterprise default) above the
    organization default, and Claim 5 adds a personal-default layer scoped to
    self-requested reviews. The combined five-entry precedence chain is captured
    in this note's Concrete Artifacts above.
  - That source's Claim 3 (per-review practitioner choice via "Reviewers") is
    directly reaffirmed, not superseded, by this source's Claim 5 quote: "you can
    still select a different review effort before requesting."
  - That source's Claim 6 (plan availability: Pro, Pro+, Max, Business, Enterprise
    for Lite/Balanced generally) is refined by this source's Claim 2: plan
    availability *for the personal settings page specifically* was narrower
    (Pro/Pro+/Max only) until this September 23 update extended it to Business
    and Enterprise — a distinction the August 7 note's plan-availability claim did
    not surface, since it covered the effort-level feature broadly rather than the
    personal-settings UI specifically.

- **Extends** `docs-github-copilot-code-review-config-controls.md` (issue #1168):
  - That source's Claim 2 documented org-level runner-configuration lock enforcement
    as a governance pattern where org defaults can override repo-level settings while
    repos retain some autonomy absent a lock. This source's Claim 6 shows GitHub
    applying the same additive, override-preserving governance shape (new top-level
    default; existing lower levels keep override rights) to the review-effort
    setting instead of the runner setting — a second instance of the same governance
    pattern rather than the same mechanism.

- **Extends** `docs-github-copilot-code-review-progress-tracking-smart-commits.md`
  (issue #3560, the September 18, 2026 predecessor entry in the same weekly cadence
  of Copilot code review changelogs):
  - That source covered review *output* changes (overview-comment restructuring,
    auto-resolution enhancements, smart-commit batching). This source, five days
    later, covers review *configuration and governance* changes exclusively — the
    two entries are adjacent in the same ongoing changelog cadence but address
    non-overlapping product surfaces (output UX vs. settings/governance). No
    claim-level overlap.

- **Corroborates** `docs-github-copilot-global-model-policy-ga.md` (issue #2992):
  - That source documented an enterprise/org model-enablement policy where an
    enterprise-set default is inherited by organizations and can be overridden at
    lower levels. This source's Claim 6 (enterprise default review effort,
    inherited by organization-owned repositories, with org/repo override rights
    preserved) is a structurally identical governance pattern applied to a
    different setting (review effort vs. model enablement). Together these two
    sources establish "enterprise default with inheritance and override rights at
    lower levels" as a recurring GitHub governance design pattern across at least
    two distinct Copilot configuration surfaces — worth naming as a general pattern
    in Ch02 rather than describing each instance in isolation.

- **Contradicts**: None found. The personal-default and enterprise-default additions
  are purely additive to the existing per-review/repo/org hierarchy; nothing in this
  source states or implies that a prior layer (per-review choice, repo override, org
  default) stops working or changes behavior. No contradiction issue filed.

- **Novel**:
  - **Enterprise-level default review effort**, the first governance tier above
    organization-level in the effort-level hierarchy.
  - **"The GitHub default" as a named, selectable enterprise option** distinct from
    an explicit Lite/Balanced choice.
  - **Personal default review effort**, a practitioner-scoped setting distinct from
    admin-controlled org/repo defaults, applying specifically to reviews the
    practitioner themselves requests or that auto-trigger on their own PRs.
  - **Business/Enterprise plan parity for personal review settings**, closing a
    plan-tier gap that previously left Business/Enterprise practitioners without
    any self-service automatic-review controls.
  - **Named three-condition automatic-review trigger list** (create PR, coauthor
    PR, move PR out of draft) as a single enumerated set — previously implied by
    the existence of "automatic review" but not stated as a specific three-item
    list in any prior corpus source.
  - **Split automatic-review toggles** for new pushes vs. draft PRs, replacing a
    single combined toggle.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Update the review-effort-level precedence
  material (built from `docs-github-copilot-code-review-skills-mcp-tier.md` and
  `docs-github-copilot-code-review-effort-levels-ga.md`) to the five-layer chain in
  this note's Concrete Artifacts: per-review choice → personal default → repo
  override → org default → enterprise default. Flag the unresolved
  personal-vs-repo/org precedence question (Claim 5) rather than asserting a
  precedence order the source does not state. Also worth naming the recurring
  "enterprise default with inheritance and lower-level override rights" pattern
  (see Cross-References → Corroborates) as a general GitHub governance design
  observed across both model policy and review-effort configuration.
- **Chapter 05 (Team Adoption)**: Note that Business/Enterprise-plan practitioners
  now have the same personal automatic-review self-service controls Pro/Pro+/Max
  users already had (Claim 2) — relevant for any adoption checklist that assumed
  automatic-review configuration was admin-only for enterprise fleets. Also add the
  enterprise-default-effort setting as a new pre-deployment governance decision:
  platform/security teams standardizing review depth across many organizations can
  now set one enterprise floor instead of coordinating per-organization defaults.
- **Chapter 01 (Daily Workflows)**: Clarify that "the automatic review toggle" is
  now two independent toggles (new pushes vs. draft PRs, Claim 3), and that
  practitioners can set a personal default effort level that applies to
  self-requested reviews (Claim 5) — update any walkthrough describing automatic
  review as a single on/off setting.

## Extraction Notes

1. **WebFetch summarized rather than quoted verbatim; verified via direct curl
   instead**: An initial WebFetch call returned an accurate-in-substance but
   AI-summarized paraphrase of the page (e.g., it rendered "coauthor a pull
   request" content correctly but not word-for-word, and it did not preserve the
   "GitHub default" phrase). All quotes in this note are instead taken from a
   direct `curl` of the raw HTML at the canonical (trailing-slash) URL — the bare
   URL from the issue body returns an HTTP 301 redirect to
   `.../more-ways-to-request-and-configure-reviews/` — with tags stripped and
   entities unescaped programmatically, then spot-checked by eye against the
   parsed text above.

2. **No linked documentation pages to follow**: Unlike the August 7, 2026 changelog
   (`docs-github-copilot-code-review-effort-levels-ga.md`), which linked to a
   substantive "About GitHub Copilot code review" conceptual docs page, this
   changelog's article body contains no links to `docs.github.com` beyond
   site-wide privacy-policy/terms-of-service boilerplate (checked directly in the
   raw HTML). There was no substantive linked page to follow per MINER.md §1.

3. **Source is very short (~230 words, "1 minute read")**: All content was
   exhausted across eight claims. This is a thinner source than the June 2 or
   August 7 code-review changelogs, consistent with it being an incremental
   configuration-surface update rather than a new capability announcement.

4. **Open precedence question flagged, not resolved**: Claim 5 and the Concrete
   Artifacts precedence chain explicitly flag that the source does not state how
   a personal default effort interacts with a conflicting repo/org/enterprise
   default for a self-authored PR. This is a genuine gap in the source, not an
   extraction failure — the Assayer should not expect a citable quote resolving it.

5. **No contradictions to file**: All claims in this source are additive to the
   existing corpus (new governance tiers, new plan availability, new toggle
   granularity). No existing source note makes a claim this source would refute.
   No contradiction issue required.
