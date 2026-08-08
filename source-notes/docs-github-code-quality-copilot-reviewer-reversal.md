---
source_url: https://github.blog/changelog/2026-08-07-github-code-quality-no-longer-adds-copilot-as-a-reviewer
source_type: docs
title: "GitHub Code Quality no longer adds Copilot as a reviewer"
author: GitHub (official changelog)
date_published: 2026-08-07
date_extracted: 2026-08-08
last_checked: 2026-08-08
status: current
confidence_overall: settled
issue: "#2565"
---

# GitHub Code Quality No Longer Adds Copilot as a Reviewer

> GitHub's August 7, 2026 changelog entry reversing an 18-day-old default: enabling
> GitHub Code Quality no longer auto-creates a ruleset that requests Copilot code
> review on every pull request, every push, and every draft PR. GitHub disabled the
> three settings it had turned on, left user-edited rulesets untouched, and
> attributes the reversal directly to user feedback that "adding a reviewer should
> be your choice."

## Source Context

- **Type**: docs (GitHub official product changelog; marked "Retired" status on the
  page itself; ~1 minute read, two sections plus a short intro)
- **Author credibility**: GitHub's own changelog team, describing a first-party
  product behavior change to GitHub Code Quality and its interaction with Copilot
  code review. Authoritative for the fact of the change, the exact ruleset name,
  the three settings involved, and the stated rationale. Not authoritative for how
  many repositories were affected, how much user pushback there was, or whether
  this reversal reflects a broader pattern in how GitHub handles opt-out AI
  defaults — the source states the "why" only in the vendor's own words.
- **Scope**: Covers exactly one behavior change — automatic Copilot reviewer
  assignment via a GitHub-managed ruleset created when Code Quality is enabled.
  Does NOT cover: what GitHub Code Quality is as a product beyond this ruleset
  interaction, whether other Code Quality behaviors changed, or details of the
  "configuring automatic code review by Copilot" documentation it links to (not
  fetched — see Extraction Notes).

## Extracted Claims

### Claim 1: Enabling GitHub Code Quality no longer automatically creates a ruleset requesting Copilot code review on pull requests
- **Evidence**: Direct statement in the changelog's opening line, backed by the
  page's own "Retired" status label marking the old behavior as discontinued.
- **Confidence**: settled (first-party product changelog describing current
  behavior)
- **Quote**: "Enabling GitHub Code Quality on a repository no longer creates a
  ruleset that automatically requests a code review from GitHub Copilot on your
  pull requests."
- **Our assessment**: This is a straightforward default-behavior removal. The
  practical effect: teams enabling Code Quality today get no automatic Copilot
  review unless they explicitly configure it — a change from the July 20, 2026
  GA behavior. For Ch05 (Team Adoption): any onboarding checklist or runbook
  written between July 20 and August 7, 2026 that assumed "enabling Code Quality
  gets you automatic Copilot review for free" is now stale.

### Claim 2: The automatic-reviewer behavior was introduced when GitHub Code Quality became generally available on July 20, 2026, and was reversed just 18 days later
- **Evidence**: The changelog explicitly dates the original behavior's
  introduction to the Code Quality GA date and frames this entry as a reversal of
  that specific decision.
- **Confidence**: settled (dates stated directly in the source)
- **Quote**: "When Code Quality became generally available on July 20, 2026,
  enabling it created a repository ruleset named Code Quality Copilot review for
  default branch that targeted your default branch."
- **Our assessment**: An 18-day turnaround from GA to reversal is fast even by
  GitHub's own changelog cadence (compare to the multi-week gaps between
  incremental Copilot code review changes in `docs-github-copilot-code-review-config-controls.md`
  and `docs-github-copilot-code-review-skills-mcp-tier.md`). This is worth noting
  as a data point on how quickly a vendor will unwind an opt-out AI default once
  it draws pushback — the decision-to-reversal cycle here is measured in days,
  not months.

### Claim 3: GitHub attributes the reversal directly to user feedback that adding an automatic reviewer should be a choice, not a default
- **Evidence**: Explicit first-person statement in the changelog, phrased as a
  direct response to user sentiment rather than an internal engineering decision.
- **Confidence**: anecdotal (vendor's own characterization of "what users told
  us" — no survey data, ticket counts, or community-thread citations given)
- **Quote**: "You told us that adding a reviewer should be your choice, so we've
  reversed that."
- **Our assessment**: This is the single clearest sentence in the source and the
  one most relevant to the guide: it's a vendor explicitly naming "opt-in vs.
  opt-out for AI touching a critical workflow (PR review)" as the friction point
  that caused a reversal. No metrics back the claim of user complaint volume, but
  the reversal itself — GitHub actually rolled back a GA default — is a stronger
  signal than the sentence alone. For Ch05: use this as a concrete, dated example
  of the opt-in-not-opt-out principle for AI review tooling, not just a
  guideline the guide asserts on its own authority.

### Claim 4: GitHub disabled three specific ruleset settings that had been auto-enabled: automatic review requests, review-on-push, and review-on-draft-PR
- **Evidence**: Changelog explicitly names and describes each of the three
  settings under "What we've turned off."
- **Confidence**: settled (specific configuration facts stated in the source)
- **Quote**: "We've disabled the three settings we enabled in that ruleset:
  Automatically request Copilot code review, which requested a Copilot review on
  every pull request. Review new pushes, which requested another review each
  time you pushed to a pull request. Review draft pull requests, which requested
  a review before you marked a pull request ready."
- **Our assessment**: This is the precise mechanism, not just the headline. Teams
  auditing PR automation should know these are the exact three ruleset toggles
  to check for if they suspect stale auto-review configuration in older
  repositories (enabled between July 20 and August 7, 2026). For Ch02 (Harness
  Engineering): this maps directly onto the ruleset-based configuration surface
  documented for Copilot code review — "Automatically request Copilot code
  review" is the same setting named in the re-enablement instructions (Claim 6
  below), confirming it's a stable, user-facing ruleset toggle rather than an
  internal-only flag.

### Claim 5: GitHub only reverted rulesets that still matched what it originally created — rulesets a user had already edited were left untouched
- **Evidence**: Explicit statement distinguishing GitHub-created, unmodified
  rulesets from user-edited ones.
- **Confidence**: settled (stated directly in the source)
- **Quote**: "We only change the ruleset where it still matches what we created.
  If you've edited it, we leave it as you set it, and we never touch a ruleset
  you wrote yourself."
- **Our assessment**: This is a notable operational detail: the rollback logic
  is conservative and diff-aware rather than a blanket "delete every matching
  ruleset name" sweep. It implies GitHub tracks provenance (did we create this,
  or did the user modify it) at the individual ruleset level. For Ch02: this is
  a good example of a vendor treating auto-generated configuration as owned by
  the vendor only until a human touches it — a pattern worth citing when the
  guide discusses how harness-generated config (CI files, rulesets, hook
  definitions) should interact with human edits during vendor-side changes.

### Claim 6: The disabled ruleset is not deleted — it remains in the repository with the three settings off, and users can delete it manually if they want
- **Evidence**: Explicit statement in the "What we've turned off" section.
- **Confidence**: settled (stated directly in the source)
- **Quote**: "The ruleset stays in your repository with these settings off, so
  you can delete it whenever you want."
- **Our assessment**: A minor but practical detail for anyone auditing rulesets
  post-change: `Code Quality Copilot review for default branch` will still show
  up in a repository's ruleset list, just with all three settings disabled — it
  is not silently removed. Teams scripting ruleset audits (e.g., "flag any
  ruleset with 0 active rules") should account for this ghost ruleset rather
  than assuming its presence implies active enforcement.

### Claim 7: Copilot code review itself is unchanged by this update, and teams can manually re-enable automatic review at the repository or organization level at any time
- **Evidence**: Explicit statement in the "How to keep automatic Copilot code
  review" section, with a named setting and a link to setup documentation.
- **Confidence**: settled (stated directly in the source)
- **Quote**: "Copilot code review itself hasn't changed, and you can turn it back
  on at any time. Add or edit a ruleset that enables Automatically request
  Copilot code review for the branches you choose, at either the repository or
  organization level."
- **Our assessment**: This confirms the change is scoped narrowly to the
  Code-Quality-driven auto-creation of the ruleset, not to Copilot code review
  as a capability. Teams that want the old default-on behavior back can
  explicitly configure the same "Automatically request Copilot code review"
  ruleset setting themselves — the org-level option is notable since it lets a
  platform team restore fleet-wide automatic review as a deliberate policy
  decision rather than an implicit side effect of enabling Code Quality. This
  aligns with the org-level ruleset governance surface documented in
  `docs-github-copilot-code-review-config-controls.md` (that note's Claims 1-3
  cover org-level runner defaults and locks; this source confirms the reviewer
  ruleset setting is likewise configurable at the org level, not just per-repo).

### Claim 8: Copilot code review continues to bill to a user's Copilot plan regardless of whether it was triggered automatically or manually re-enabled
- **Evidence**: Explicit statement at the end of the "How to keep automatic
  Copilot code review" section.
- **Confidence**: settled (stated directly in the source)
- **Quote**: "Copilot code review continues to bill to your Copilot plan."
- **Our assessment**: This is a reassurance that the billing model established
  in `docs-github-copilot-code-review-actions-billing.md` (AI Credits + Actions
  minutes) is unaffected by this reversal — the change is purely about the
  trigger mechanism (automatic-by-default vs. explicit opt-in), not about cost
  or the underlying agentic architecture. For Ch05 TCO discussions: no billing
  model update needed from this source.

### Claim 9: This change applies specifically to GitHub Code Quality on GitHub Enterprise Cloud and GitHub Team
- **Evidence**: Explicit scope statement at the end of the changelog entry.
- **Confidence**: settled (stated directly in the source)
- **Quote**: "This change applies to Code Quality on GitHub Enterprise Cloud and
  GitHub Team."
- **Our assessment**: Narrows the audience: teams on other GitHub plans, or
  using Copilot code review through mechanisms other than GitHub Code Quality
  (e.g., manually requesting a Copilot review, or the ruleset-based setup
  documented in the config-controls note), are unaffected because they were
  never subject to the Code-Quality-driven auto-creation behavior in the first
  place. For Ch05: scope any guide callout to Enterprise Cloud / Team customers
  using Code Quality specifically, not Copilot code review users generally.

## Concrete Artifacts

### Source text (verbatim, August 7, 2026 changelog entry)

```
GitHub Code Quality no longer adds Copilot as a reviewer
Status: Retired
Published: August 7, 2026 · 1 minute read
Source: https://github.blog/changelog/2026-08-07-github-code-quality-no-longer-adds-copilot-as-a-reviewer

Enabling GitHub Code Quality on a repository no longer creates a ruleset that
automatically requests a code review from GitHub Copilot on your pull requests.
In repositories that already have that ruleset, we've turned off the settings
we enabled.

When Code Quality became generally available on July 20, 2026, enabling it
created a repository ruleset named Code Quality Copilot review for default
branch that targeted your default branch. You told us that adding a reviewer
should be your choice, so we've reversed that.

--- What we've turned off ---

We've disabled the three settings we enabled in that ruleset:

- Automatically request Copilot code review, which requested a Copilot review
  on every pull request.
- Review new pushes, which requested another review each time you pushed to a
  pull request.
- Review draft pull requests, which requested a review before you marked a
  pull request ready.

We only change the ruleset where it still matches what we created. If you've
edited it, we leave it as you set it, and we never touch a ruleset you wrote
yourself. The ruleset stays in your repository with these settings off, so you
can delete it whenever you want.

--- How to keep automatic Copilot code review ---

Copilot code review itself hasn't changed, and you can turn it back on at any
time. Add or edit a ruleset that enables Automatically request Copilot code
review for the branches you choose, at either the repository or organization
level. For the steps, see configuring automatic code review by Copilot.
Copilot code review continues to bill to your Copilot plan.

This change applies to Code Quality on GitHub Enterprise Cloud and GitHub Team.

Tags: application security, copilot
```

### Ruleset settings table (from source)

```
Ruleset name (GitHub-created): "Code Quality Copilot review for default branch"

Setting                                    | Prior state | New state | Effect when on
------------------------------------------ | ----------- | --------- | -----------------------------------------
Automatically request Copilot code review  | ON (auto)   | OFF       | Copilot review requested on every PR
Review new pushes                          | ON (auto)   | OFF       | New review requested on every push to a PR
Review draft pull requests                 | ON (auto)   | OFF       | Review requested before marking PR ready

Reversal scope: only rulesets unmodified since GitHub created them.
User-edited rulesets: left untouched (not reverted).
Ruleset deletion: not automatic — remains in repo, disabled, until user deletes it.
Manual re-enable: same "Automatically request Copilot code review" setting,
configurable at repository or organization level.
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-config-controls.md` (issue #1168):
  That note documents the June 12, 2026 addition of org-level runner defaults
  with lock enforcement, content exclusion, and unlimited instruction files as
  governance layers for Copilot code review. This source confirms that the
  reviewer-assignment ruleset setting ("Automatically request Copilot code
  review") is itself configurable at repository *or* organization level — the
  same two-tier governance pattern that note documents for runners. This source
  adds a new governance-relevant fact that note didn't cover: GitHub Code
  Quality, when enabled, used to *auto-create* this ruleset on your behalf
  rather than requiring an admin to configure it explicitly. That auto-creation
  behavior is now removed, meaning the reviewer ruleset is an entirely
  admin-initiated governance surface going forward — no implicit default from
  enabling Code Quality.
- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md` (issue #1052):
  That note's Claim 14 documents the per-repository "review effort level" (tier)
  setting as an admin-controlled, not practitioner-controlled, configuration.
  This source's ruleset-based reviewer-assignment setting is a second
  admin-controlled configuration surface for the same feature (whether Copilot
  reviews at all vs. how deeply it reviews). Together the two notes establish
  that "does Copilot review this PR" and "how thoroughly does Copilot review
  this PR" are two independently admin-configured questions.
- **Contradicts**: None found. No existing source note claims that Code Quality
  auto-enables Copilot review as a permanent or currently accurate default —
  this is the first note documenting the auto-enable behavior at all (it
  existed only from July 20 to August 7, 2026 and no prior source-note issue
  covered Code Quality's Copilot-reviewer ruleset during that window). No
  contradiction issue to file.
- **Novel**: This is the first corpus source to document GitHub Code Quality's
  ruleset-based interaction with Copilot code review at all — no prior note
  discusses the `Code Quality Copilot review for default branch` ruleset, its
  three settings, or GitHub Code Quality as a product distinct from Copilot
  code review itself. It's also the first corpus source documenting a GitHub
  changelog entry that reverses a prior GA default within less than three
  weeks, explicitly citing user feedback as the cause — a useful concrete
  example of vendor responsiveness (or at least stated responsiveness) to
  opt-out AI complaints. `docs-ghaw-code-quality-monitoring.md` uses the phrase
  "code quality monitoring" but refers to a distinct GitHub Agentic Workflows
  example pattern, not the GitHub Code Quality product feature this source
  covers — the naming overlap is coincidental, not a cross-reference.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add this as a dated, concrete example for the
  "default to opt-in, not opt-out, for AI in critical workflows" guidance.
  Specifics to cite: GitHub Code Quality auto-added Copilot as a PR reviewer
  from GA (2026-07-20) until reversal (2026-08-07); GitHub's own stated reason
  was "adding a reviewer should be your choice." If the guide has an onboarding
  checklist for teams enabling GitHub Code Quality, remove any assumption that
  automatic Copilot review comes bundled — it must now be explicitly configured
  via the "Automatically request Copilot code review" ruleset setting at repo
  or org level.
- **Chapter 02 (Harness Engineering)**: When documenting the Copilot code
  review configuration surface (extending `docs-github-copilot-code-review-config-controls.md`),
  note that the reviewer-assignment ruleset is a distinct configuration axis
  from tier/skills/MCP/content-exclusion, and that GitHub-authored config
  (auto-created rulesets) is now scoped to be reverted only while it remains
  byte-for-byte GitHub's own default — once a human edits it, GitHub will not
  touch it again. Cite this as a model for how a harness/platform team's own
  auto-generated config should relate to vendor-side rollbacks.

## Extraction Notes

- WebFetch's first pass through a summarizing model returned only paraphrased
  content. To satisfy the verbatim-quote requirement, I fetched the raw page
  HTML directly (via `curl` with a browser user agent) and extracted the
  `<article>` content, stripping tags. All quotes above are copied verbatim
  from that extracted text and cross-checked against the WebFetch summary for
  consistency; no discrepancies found.
- The source links to a separate "configuring automatic code review by
  Copilot" documentation page for setup steps. That page was not fetched — it
  likely contains the detailed ruleset-configuration UI walkthrough referenced
  in Claim 7. If a future source note is filed for that page, it should extend
  this note's Claim 7 and Claim 9.
- The source is short (~1 minute read, two sections). All substantive claims
  were extracted; there was no additional depth to mine beyond the two
  sections and the closing scope/billing lines.
- No sub-pages beyond the single linked "configuring automatic code review by
  Copilot" doc were identified as worth following (the page has no other
  substantive outbound content links).
