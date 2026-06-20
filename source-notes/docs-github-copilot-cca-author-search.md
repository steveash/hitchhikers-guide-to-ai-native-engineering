---
source_url: https://github.blog/changelog/2026-06-18-copilot-authored-pull-requests-now-included-in-author-searches
source_type: docs
title: "Copilot-authored pull requests now included in author searches"
author: GitHub (official changelog)
date_published: 2026-06-18
date_extracted: 2026-06-20
last_checked: 2026-06-20
status: current
confidence_overall: settled
issue: "#1235"
---

# Copilot-Authored Pull Requests Now Included in Author Searches

> GitHub's June 18, 2026 changelog documenting that `author:` PR searches now return
> both human-authored and Copilot cloud agent–opened pull requests together, with
> "username with Copilot" attribution in the global PR dashboard and a July 16, 2026
> expansion to REST API and GraphQL API.

## Source Context

- **Type**: docs (GitHub official changelog, June 18, 2026; ~100 words of primary content)
- **Author credibility**: GitHub engineering team announcing a production feature change.
  Authoritative for: the feature's existence, the `author:` search behavior change, the
  "username with Copilot" attribution format in search results, the platform availability
  timeline, and the July 16 API rollout date. Not credible for: how the feature interacts
  with third-party PR management tools that filter by author, whether this applies to PRs
  created via non-CCA Copilot paths (e.g., Copilot CLI auto-complete that drafts code but
  the developer opens the PR), or how historical CCA PRs (created before June 18) appear
  in searches.
- **Scope**: The change to how GitHub's `author:` PR search handles Copilot cloud
  agent–opened PRs: inclusion of CCA-opened PRs in author results, the "username with
  Copilot" display format, the effect on default views like "Created by me," and the
  platform rollout timeline (UI/Mobile now; REST API/GraphQL July 16, 2026). Does NOT
  cover: behavior with non-CCA Copilot contributions, organization-level search
  restrictions, search result ranking, or whether the feature is configurable per
  repository or organization.

## Extracted Claims

### Claim 1: The `author:` PR search filter now includes PRs opened by Copilot cloud agent on the user's behalf

- **Evidence**: Official GitHub product changelog announcement, June 18, 2026. This is
  the primary feature change described in the source, returned verbatim across two
  independent WebFetch calls.
- **Confidence**: settled (product fact; announced in official changelog, available now
  on GitHub.com UI and GitHub Mobile)
- **Quote**: "Searching for pull requests using `author:` now shows pull requests opened
  by Copilot cloud agent on the user's behalf."
- **Our assessment**: This closes a meaningful discoverability gap. Before this update,
  a developer who invoked Copilot cloud agent to open PRs would not see those PRs when
  filtering by `author:@me` — the PR was opened by @copilot, not the user directly.
  After this change, `author:@me` returns both directly-authored and CCA-opened PRs.
  The implication: GitHub has decided that CCA invocation is the user's act of authorship,
  even when the agent performs the mechanical PR-open step. This is consistent with the
  dual-attribution design in the same-day release notes change
  (`docs-github-copilot-release-notes-pr-credit.md`).

### Claim 2: `author:@me` on github.com/pulls now returns a combined view of human-authored and Copilot-opened pull requests

- **Evidence**: Specific example provided in the changelog, appearing consistently across
  two WebFetch calls.
- **Confidence**: settled (concrete specific example from official changelog)
- **Quote**: (no direct quote; WebFetch returned a paraphrase — Assayer should verify
  exact wording against live URL)
- **Our assessment**: `author:@me` on github.com/pulls is the canonical daily-workflow
  PR discovery path for most developers. Making this the specific example in the
  changelog signals that GitHub is targeting the highest-frequency developer workflow,
  not an edge-case search pattern. A developer who navigates to github.com/pulls and
  applies the default `author:@me` filter will now see all PRs they are responsible for
  — whether opened directly or via CCA — without any additional configuration.

### Claim 3: Default views like "Created by me" automatically include Copilot cloud agent–opened pull requests

- **Evidence**: Stated in the changelog as part of the feature description; consistent
  across both WebFetch calls.
- **Confidence**: settled (product feature description in official changelog)
- **Quote**: (no direct quote; WebFetch returned a paraphrase — Assayer should verify
  exact wording against live URL)
- **Our assessment**: This is the highest-impact part of the change. "Created by me" is
  the default landing state of the GitHub PR interface at github.com/pulls — it requires
  no explicit search syntax. Any developer who navigates to the PR dashboard using
  default settings will now see CCA-opened PRs surfaced automatically. This reduces the
  likelihood that CCA-opened PRs go untracked simply because they were not in the
  default view. The change requires no user action or opt-in.

### Claim 4: The global pull requests dashboard displays CCA-authored PRs with "username with Copilot" attribution

- **Evidence**: Stated in changelog; consistent across both WebFetch calls as the
  attribution format in the global PR dashboard.
- **Confidence**: settled (product feature description from official changelog)
- **Quote**: (no direct quote; WebFetch returned a paraphrase — Assayer should verify
  exact wording against live URL)
- **Our assessment**: The "username with Copilot" format in search results parallels the
  "by @[user] with @copilot" attribution pattern introduced the same day for generated
  release notes (`docs-github-copilot-release-notes-pr-credit.md` Claim 2). Both
  surfaces use a "human with Copilot" conjunction — the human requester is named first,
  the agent second — establishing human-primary attribution across both live search and
  historical release records. This is a cross-surface design consistency that teams can
  rely on when building processes for AI-contribution auditing.

### Claim 5: The feature is available on GitHub.com UI and GitHub Mobile as of June 18, 2026, with REST API and GraphQL API support scheduled for July 16, 2026

- **Evidence**: Explicit platform availability and rollout timeline in the changelog;
  consistent across both WebFetch calls.
- **Confidence**: settled (concrete date and platform scope stated in official changelog)
- **Quote**: (no direct quote; dates and platform scope appeared consistently across
  both fetches as paraphrases — Assayer should verify against live URL)
- **Our assessment**: The staggered rollout matters for practitioners building automated
  tooling. Any script or integration that queries PRs by author via the REST API or
  GraphQL API will NOT see CCA-opened PRs in those results until July 16, 2026. Tooling
  built to audit or report on CCA contributions using the API should note this cutover
  date. The UI change (June 18) and the API change (July 16) have a ~28-day gap during
  which the behavior is inconsistent between surfaces.

### Claim 6: The feature eliminates the need for multiple queries to locate all PRs the user is responsible for

- **Evidence**: Feature description in the changelog describing the practical benefit;
  consistent across both WebFetch calls.
- **Confidence**: settled (product description from official changelog)
- **Quote**: (no direct quote; WebFetch returned a paraphrase — Assayer should verify
  against live URL)
- **Our assessment**: Before this change, a developer with high CCA usage needed two
  separate searches: one for directly-authored PRs and one for CCA-opened PRs. The
  consolidation into a single `author:` query is a meaningful friction reduction for
  developers who regularly use Copilot cloud agent across multiple repositories or tasks.
  It also reduces the chance that CCA-opened PRs accumulate unreviewed — they now surface
  in the same query context as all other open work.

## Concrete Artifacts

### Platform Rollout Summary (from changelog, June 18, 2026)

```
Feature: Copilot-authored PRs included in author searches
Published: 2026-06-18
Source: github.blog/changelog/2026-06-18-copilot-authored-pull-requests-now-included-in-author-searches

Primary behavior change:
  BEFORE: author:@me on github.com/pulls → returns only directly-authored PRs
  AFTER:  author:@me on github.com/pulls → returns directly-authored + CCA-opened PRs

Attribution format in global PR dashboard:
  "username with Copilot"

Default views affected:
  "Created by me" (github.com/pulls default) — now includes CCA-opened PRs

Platform rollout:
  Available now (June 18, 2026):
    ✅  GitHub.com UI
    ✅  GitHub Mobile

  Scheduled (July 16, 2026):
    🔜  REST API
    🔜  GraphQL API

Labels: client apps, collaboration tools, copilot
```

### CCA PR Discoverability Path (synthesized from corpus)

```
CCA PR lifecycle — discoverability (as of June 18, 2026):

Step 1 — Invocation
  Developer invokes CCA via UI, REST API, or GitHub Actions
  Source: docs-github-copilot-cca-rest-api-tasks.md

Step 2 — PR creation
  CCA "works in the background in its own development environment, where it
  can make and validate code changes, then open a pull request."
  (quote from docs-github-copilot-cca-rest-api-tasks.md Claim 2)

Step 3 — Discovery (POST-June 18, 2026)
  author:@me on github.com/pulls → developer sees their CCA-opened PR
  Default "Created by me" view → developer sees their CCA-opened PR
  Attribution in results: "username with Copilot"

Step 4 — Historical record (POST-June 18, 2026)
  Generated release notes → "by @[username] with @copilot"
  Source: docs-github-copilot-release-notes-pr-credit.md

Step 5 — API queries (POST-July 16, 2026)
  REST API author: filter → includes CCA-opened PRs
  GraphQL API author: filter → includes CCA-opened PRs
```

## Cross-References

- **Complements** `docs-github-copilot-release-notes-pr-credit.md` (Issue #1220, Claim 2):
  That source documents "by @[requester] with @copilot" attribution in generated release
  notes, also released June 18, 2026. This source documents the same dual-attribution
  principle applied to live PR search results ("username with Copilot"). The two changes
  together appear to be a coordinated rollout — same day, same feature area, same
  attribution design philosophy — applied to two distinct surfaces: release notes
  (historical record) and PR search (operational discovery). Both sources should be cited
  together when discussing how CCA-authored contributions are represented in standard
  GitHub tooling. Neither contradicts the other.

- **Extends** `docs-github-copilot-cca-rest-api-tasks.md` Claim 2 (CCA "make[s] and
  validate[s] code changes, then open[s] a pull request"): That source documents CCA's
  execution model, including the PR it opens as output. This source documents the
  downstream discoverability of that PR: what happens when a developer searches for
  their authored PRs. The full operational sequence across both notes: CCA is triggered
  (via REST API, UI, or Actions) → CCA opens a PR → that PR now appears under the
  developer's `author:@me` search. The notes complement each other without overlap.

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md` (if present — verify
  claim number before citing): Usage metrics APIs track CCA task activity at the org or
  team level; author search is the individual developer's analogous mechanism for their
  own work. Together they enable oversight at different scopes: organizational aggregate
  (metrics API) and personal (author search). Cross-reference by section name pending
  verification of exact claim numbers in that note.

- **Contradicts**: None identified. No existing corpus source claims that CCA-opened PRs
  should remain invisible to `author:` searches. The dual-attribution pattern is
  consistent with the release notes note and with GitHub's broader design philosophy
  documented in related sources. No contradiction issue filed.

- **Novel**:
  - **First corpus source establishing that GitHub's PR search treats CCA invocations
    as the human requester's authorship**: Prior notes document how CCA creates PRs but
    no prior source establishes that those PRs appear under the invoking user's
    `author:` search. This is the first affirmation in the corpus that GitHub maps CCA
    invocations to the invoking user's identity for search purposes, not the agent's.
  - **Staggered API rollout (UI now, REST/GraphQL July 16)**: No prior corpus source
    documents a CCA-related feature with explicitly different UI and API availability
    dates. This matters for practitioners building automated tooling that queries PRs
    by author via the API — the behavior change is not yet live in API queries as of
    extraction date.
  - **"Created by me" default view inclusion**: The default view change requires no
    user action and affects every developer who uses the standard github.com/pulls
    landing page. No prior corpus source documents a default view change that
    automatically incorporates CCA-authored content.

## Guide Impact

- **Chapter 01 (Daily Workflows — AI-Assisted Development Patterns)**:
  Add: Developers using Copilot cloud agent should know their CCA-opened PRs are now
  visible in `author:@me` searches and the "Created by me" default view on github.com/pulls.
  This eliminates the previous friction where CCA PRs were invisible in a developer's
  default PR view. Recommend using a single `author:@me` query (or the default view) to
  manage all open work — no need for separate CCA-specific bookmarks or filters.

- **Chapter 02 (Tool Integration — Copilot Cloud Agent Workflows)**:
  Add: When documenting the CCA PR lifecycle, note that the resulting PR appears in the
  invoking developer's `author:` searches. For automated tooling that queries PRs via
  the REST API or GraphQL API, note the July 16, 2026 cutover date — the API does not
  reflect the new CCA-inclusive behavior until that date. Any reporting scripts written
  before July 16 that rely on `author:` to find CCA PRs must be tested against the API
  after the rollout date.

- **Chapter 04 (Quality and Oversight — Tracking AI-Assisted Contributions)**:
  Add: The "username with Copilot" attribution in PR search results, combined with the
  "by @[user] with @copilot" format in release notes (documented in
  `docs-github-copilot-release-notes-pr-credit.md`), provides team leads with a
  consistent, GitHub-native mechanism to identify and audit AI-assisted contributions
  across both live dashboards (PR author search) and historical records (release notes).
  Teams building AI contribution review processes can rely on these surfaces rather than
  custom labeling schemes — GitHub is building the attribution infrastructure at the
  platform level.

## Extraction Notes

1. **Very brief source (~100 words)**: This is a concise changelog announcement. All
   extractable claims are covered in 6 items. The source is short but its implications
   for daily developer workflow and automated tooling are significant.

2. **Verbatim quote confidence**: Two independent WebFetch calls were made to the source
   URL. Claim 1's quote ("Searching for pull requests using `author:` now shows pull
   requests opened by Copilot cloud agent on the user's behalf.") appeared verbatim and
   consistently across both calls and is presented as a verbatim quote with high
   confidence. All other specific details (attribution format, platform timeline, default
   view behavior) were returned as paraphrases by the WebFetch AI layer, not as
   character-for-character copies. These are marked "(no direct quote; WebFetch returned
   a paraphrase)" per MINER.md §2a. The Assayer should spot-check Claims 3, 4, 5, and
   6 against the live URL.

3. **Same-day coordination with release notes change**: Both this source and
   `docs-github-copilot-release-notes-pr-credit.md` are published June 18, 2026 and
   both address CCA PR attribution. The parallel release appears intentional; both are
   noted under Cross-References without filing a contradiction issue (they do not
   conflict).

4. **API rollout not yet live at extraction date**: The REST API and GraphQL API change
   is scheduled for July 16, 2026 (not yet live as of extraction date June 20, 2026).
   Claims about API behavior (Claim 5) should be treated as forward-looking until July 16.

5. **Scope limited to Copilot cloud agent**: The changelog specifies this applies to PRs
   opened by "Copilot cloud agent." It is not claimed here that PRs reviewed by Copilot
   (but not opened by CCA) appear differently in `author:` search results.

6. **Cross-reference to `docs-github-copilot-cca-usage-metrics-aggregate.md`**: This
   note exists in the corpus (confirmed in source-notes/ listing) but its claim numbers
   were not verified before writing. The cross-reference under Cross-References cites it
   by section intent ("verify claim number before citing") rather than by a specific
   claim number, per MINER.md §4b.
