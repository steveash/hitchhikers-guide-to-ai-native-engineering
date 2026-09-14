---
source_url: https://vercel.com/changelog/deploy-cursor-origin-repositories-with-vercel-in-public-beta
source_type: blog-post
title: "Deploy Cursor Origin repositories with Vercel in public beta"
author: Cody Wong, Tom Knickman (Vercel); contributor Eric Dodds
date_published: 2026-08-17
date_extracted: 2026-09-14
last_checked: 2026-09-14
status: current
confidence_overall: emerging
issue: "#3435"
---

# Deploy Cursor Origin repositories with Vercel in public beta

> Vercel's changelog announces that Origin — Cursor's newly-named git forge,
> marketed as "a git forge for the agentic era" — can now be connected to
> Vercel as a fourth git-provider option, wired into Vercel's existing
> preview/production deployment pipeline with no Origin-specific behavior:
> the linked documentation shows this is a standard git-provider
> integration (RBAC-gated connect flow, same automatic-deployment rules as
> GitHub/GitLab/Bitbucket), not a provenance-tracking or
> agent-generated-code-detection feature, despite the "Origin" framing the
> Prospector's triage comments speculated might imply.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published August 17, 2026; a ~120-word feature announcement with one
  embedded screenshot and a link to full documentation). Per MINER.md §1,
  this note follows the changelog's own "Git integration documentation"
  link to `/docs/git/vercel-for-origin` in full, since the changelog states
  only that the connection exists and what triggers deployments, without
  describing the connect flow, permissions, or management/disconnection
  path. A second page, the Origin product marketing page at
  `cursor.com/origin`, was also fetched (not a changelog-embedded link, but
  the docs page's own in-line link identifying what "Origin" is) to resolve
  what Origin actually is, since neither the changelog nor the docs page
  defines it beyond "Cursor's Git platform."
- **Author credibility**: First-party Vercel changelog entry with two named
  authors (Cody Wong, Tom Knickman) and one named contributor (Eric Dodds),
  all presented as Vercel staff. Vercel operates the deployment platform
  being described, so the connection mechanics and deployment-trigger rules
  documented here are authoritative first-party documentation of a shipping
  beta capability. The "Origin" product itself is Cursor's, not Vercel's —
  this source describes Vercel's side of the integration only; no Cursor
  employee or Cursor-side documentation is quoted in the changelog itself
  (the `cursor.com/origin` marketing page was independently fetched to
  cross-check the product description, not sourced from Vercel's post).
- **Scope**: Covers how to connect an Origin team/repository to Vercel, the
  RBAC role required to do so, the deployment-trigger rules (preview vs.
  production), and how to manage or disconnect the integration. Does NOT
  cover: pricing, any Origin-specific build/runtime behavior distinct from
  other git providers, how many teams have adopted the integration, any
  named customer using it, or any detail on what "Cursor Origin" repository
  provenance means beyond "a repository hosted on Origin" (see Claim 6 and
  Extraction Notes for why this matters against the triage comments' framing).

## Extracted Claims

### Claim 1: Vercel now supports connecting Origin repositories as a git-provider integration, with pull requests automatically generating Preview deployments and merges to the production branch triggering Production deployments
- **Evidence**: The changelog's opening two sentences, the entirety of the feature's functional description in the announcement itself.
- **Confidence**: settled (first-party feature announcement, unambiguous)
- **Quote**: "You can now connect Origin repositories to Vercel. Once connected, pull requests on Origin will automatically generate Preview deployments on Vercel, and merging will trigger a Production deployment."
- **Our assessment**: This is functionally identical to Vercel's existing GitHub/GitLab/Bitbucket integrations (PR → Preview, merge-to-production-branch → Production) — the changelog frames Origin as a new item in an existing category (supported git providers) rather than a novel deployment mechanism. The docs page (Claim 5) confirms this explicitly by stating the same automatic-deployment rules that apply to other providers apply here.

### Claim 2: Origin is Cursor's git platform/forge, marketed independently by Cursor as "a git forge for the agentic era" and positioned as infrastructure for code that moves faster than traditional version control was built to handle
- **Evidence**: Vercel's docs page identifies Origin by a one-line definition and links to `cursor.com/origin`; the linked Cursor marketing page supplies the product's own tagline and positioning copy, verified directly against the page's raw HTML meta tags and body text.
- **Confidence**: settled (both the identifying statement and the tagline are directly quoted, unambiguous first-party product descriptions)
- **Quote**: "[Origin](https://cursor.com/origin) is Cursor's Git platform." (Vercel docs, `/docs/git/vercel-for-origin`) — "A git forge for the agentic era." (Cursor, `cursor.com/origin`, page `<meta name="description">` and Open Graph/Twitter description tags) — "Code is moving faster than any infrastructure was built to handle." / "Origin was designed for this moment." (Cursor, `cursor.com/origin`, page body copy)
- **Our assessment**: This is a new corpus data point: Cursor has a named, separately-branded git-hosting product ("Origin"), distinct from the Cursor IDE/editor and from Cursor's Cloud Agents product already documented in `blog-cursor-self-hosted-cloud-agents.md`. The "agentic era" framing positions Origin as infrastructure purpose-built for high-velocity, agent-generated commit volume — a claim consistent with the broader corpus theme that agent-generated code changes the shape of engineering infrastructure (higher PR/commit throughput, see Claim 8 in `blog-cursor-vercel-queues.md` on Vercel's own PR-throughput metrics), but Cursor's marketing page gives no concrete mechanism for how Origin is architecturally different from a conventional git forge (e.g., GitHub) beyond this tagline — no scaling numbers, no named customer, no technical detail were found on the page.

### Claim 3: Connecting Origin to Vercel requires the Owner or Member role on the Vercel team, and can be initiated from four distinct entry points — team Git settings, project Git settings, the "Continue with Origin" option in new-project creation, or Origin's own Apps tab (a bidirectional connection)
- **Evidence**: The docs page's "Connect Origin to Vercel" section states the RBAC prerequisite directly and enumerates the four connection paths, one of which (Origin's Apps tab) is described as initiated from the Origin side rather than the Vercel side.
- **Confidence**: settled (first-party documentation of a specific, checkable prerequisite and enumerated UI paths)
- **Quote**: "You need the Owner or Member role on a Vercel team to connect an Origin team." — "You can also connect Vercel to a repository from within Origin by adding Vercel in the repo's Apps tab." (changelog)
- **Our assessment**: The bidirectional-initiation detail (connect from Vercel's side via Git settings/new-project flow, or from Origin's side via its Apps tab) means the integration is symmetric rather than Vercel-only tooling bolted onto Origin — consistent with Origin being treated as a first-class git provider rather than a one-way import source. The RBAC gate (Owner/Member, not Viewer) is a standard permission-boundary detail worth carrying forward for any guide content that touches team-admin setup steps.

### Claim 4: Both Vercel's integration and Origin itself are in beta — Vercel's side is "public beta," Origin itself is in "early beta" — and Origin repositories are private-only, explicitly excluded from deployment on a Vercel Hobby (free) team
- **Evidence**: Direct status/policy statement in both the changelog and the docs page, stated as a standalone caveat rather than buried in prose.
- **Confidence**: settled (first-party statement of feature maturity and a specific plan-tier restriction)
- **Quote**: "Vercel's integration is in public beta and Origin is in early beta. Origin repositories are subject to Vercel's existing private repository policy." (changelog) — "Origin is available from Cursor as a research preview. All Origin repositories are private and cannot be deployed from a Vercel Hobby team." (docs page)
- **Our assessment**: Two independent beta labels stack here — Vercel's integration (public beta) sits on top of a product (Origin) that is itself pre-GA ("early beta" per Vercel's changelog, "research preview" per the docs page — two different maturity labels for the same underlying product, which is itself worth noting as an inconsistency between the changelog and docs page). The Hobby-tier exclusion means this integration is not usable for evaluation on a free Vercel account — a practitioner would need at least a paid Vercel team to test it, which caps how broadly this can be tried before committing to a paid tier.

### Claim 5: Origin-connected repositories follow the same automatic-deployment trigger rules as any other Vercel git integration — non-production-branch pushes and pull requests create Preview deployments (with PR status/URL updates), and pushes or merges to the configured production branch create Production deployments and update production domains
- **Evidence**: The docs page's dedicated "Automatic deployments" section, stated in general terms not specific to Origin (i.e., presented as Vercel's standard git-integration behavior that Origin now participates in).
- **Confidence**: settled (first-party description of an existing, general deployment-trigger mechanism now extended to a new provider)
- **Quote**: "Pushes to a branch other than your production branch create preview deployments. Pull requests create preview deployments, and Vercel updates the pull request with the deployment status and preview URL. Pushes and merges to your production branch create production deployments and update your production domains."
- **Our assessment**: This section contains no Origin-specific caveats or exceptions — it reads as boilerplate shared across Vercel's git-provider docs pages, reinforcing Claim 1's read that Origin is being onboarded as a peer to GitHub/GitLab/Bitbucket, not as a differently-behaved deployment source. If Origin's "agentic era" positioning (Claim 2) implied something like automatic detection of agent-authored commits, differentiated review gating, or provenance-based deployment policy, none of that surfaces anywhere in this documentation.

### Claim 6: The integration is fully manageable and reversible — teams can view/reconnect Origin teams from Vercel's team Git settings, manage repository access or uninstall from Origin's side ("Manage on Cursor"), and disconnect an individual project's Origin repository from that project's Git settings
- **Evidence**: The docs page's "Manage the Origin connection" section, describing three distinct management actions and where each is performed.
- **Confidence**: settled (first-party operational documentation of a standard connect/manage/disconnect lifecycle)
- **Quote**: "To view or reconnect your Origin teams, open your Vercel team's Git settings and find Origin. To change repository access or uninstall the Vercel app, select Manage on Cursor. To disconnect an Origin repository from a Vercel project, open the project's Git settings and select Disconnect under Connected Git Repository."
- **Our assessment**: Notable structural detail: repository-access management lives on Origin's side ("Manage on Cursor"), not Vercel's — Vercel's settings only expose reconnect and disconnect actions, not granular repo-access control. This mirrors the GitHub-App permission model (where a connected GitHub App's repo access is managed from GitHub, not from the third-party tool), suggesting Vercel built the Origin integration as a conventional OAuth-app/GitHub-App-style connector rather than something Origin-bespoke.

## Concrete Artifacts

### Full changelog text (verbatim, `vercel.com/changelog/deploy-cursor-origin-repositories-with-vercel-in-public-beta`, published 17 Aug 2026, retrieved via the page's markdown alternate and diff-checked against WebFetch output)

```
Deploy Cursor Origin repositories with Vercel in public beta

Published: August 17, 2026 | Authors: Cody Wong, Tom Knickman | Contributors: Eric Dodds

You can now connect Origin repositories to Vercel.

Once connected, pull requests on Origin will automatically generate Preview
deployments on Vercel, and merging will trigger a Production deployment.

[screenshot: vercel.com/new project-creation screen]

You can connect Origin through Team settings, Project settings, or by
clicking "Continue with Origin" when creating a new project.

You can also connect Vercel to a repository from within Origin by adding
Vercel in the repo's Apps tab.

Vercel's integration is in public beta and Origin is in early beta. Origin
repositories are subject to Vercel's existing private repository policy.

Learn more about connecting Origin in the Git integration documentation.
```

### Docs page frontmatter and connect-flow steps (verbatim, `/docs/git/vercel-for-origin`, `last_updated: 2026-08-14`)

```
summary: Connect Origin to Vercel to create automatic Preview and Production
Deployments from your repositories.

To connect Origin and import a repository:
1. From the Vercel dashboard, select New Project.
2. Select Continue with Origin.
3. Choose the Origin team to connect. Its repositories become available to
   the Vercel team currently selected in the dashboard.
4. Select an Origin repository from the list.
5. Review the project settings. If Vercel does not detect the framework,
   select a Framework Preset.
6. Select Deploy.
```

### Origin product marketing copy (verbatim, `cursor.com/origin`, meta tags and body copy)

```
<meta name="description" content="A git forge for the agentic era.">
<meta property="og:title" content="Cursor · Origin">
<meta property="og:description" content="A git forge for the agentic era.">

Body copy: "Code is moving faster than any infrastructure was built to
handle. Origin was designed for this moment."
"Early beta now available on all paid plans."
```

## Cross-References

### Cross-reference verification notes
`blog-cursor-vercel-queues.md` and `blog-cursor-self-hosted-cloud-agents.md`
were re-read in full during this extraction (MINER.md §4b); no other
source note references "Cursor Origin," "Origin repositories," or a
Cursor-branded git forge (checked via grep across `source-notes/` for
"Cursor Origin", "Origin repositories", and "cursor.com/origin" — only this
issue's own source matched).

- **Corroborates**: `blog-cursor-vercel-queues.md` (Cursor case study on
  Vercel building Queues with Cursor) documents the Cursor-Vercel
  relationship from the opposite direction — Vercel as a heavy Cursor
  *user* building infrastructure — while this source documents Vercel as
  a deployment *platform* integrating Cursor's own product (Origin). Both
  sources corroborate an active, multi-surface Cursor-Vercel partnership,
  but neither one's claims depend on or verify the other's.

- **Contradicts**: None identified. No existing corpus note makes a claim
  about Cursor Origin, git-forge deployment integrations, or Vercel's
  git-provider RBAC model that this source conflicts with.

- **Extends**: `blog-cursor-self-hosted-cloud-agents.md` documents a
  different Cursor product surface (self-hosted Cloud Agents, for
  background agent execution) with its own enterprise-adoption evidence.
  This source extends the corpus's map of the Cursor product family by
  adding a third named surface (Origin, a git forge) alongside the Cursor
  IDE and Cloud Agents — the three are architecturally distinct products
  under the same vendor, not variations of one feature.

- **Novel**:
  - **Cursor's git-forge product ("Origin") and its own positioning
    tagline** (Claim 2): no prior corpus source documents Origin at all;
    this is the first note to establish what it is and how Cursor markets it.
  - **A deployment platform (Vercel) treating an AI-coding-tool vendor's
    git hosting product as a peer git provider, with no differentiated
    behavior for agent-authored commits** (Claims 1, 5): the absence of
    any provenance-tracking, review-gating, or deployment-policy
    differentiation based on a repository's Origin/agentic-authorship
    status is itself a notable (negative) finding not established
    elsewhere in the corpus — see Extraction Notes for why this matters
    against the Prospector's triage framing.

## Guide Impact

- **Chapter 04 (Tools/Ecosystems)**: Add Cursor Origin as a distinct,
  named product in Cursor's toolset — a git forge, not an IDE feature or
  Cloud Agents variant — currently in early beta/research preview,
  available on paid plans, with a "git forge for the agentic era"
  positioning. Cross-reference alongside existing Cursor coverage
  (`blog-cursor-vercel-queues.md`, `blog-cursor-self-hosted-cloud-agents.md`)
  so the guide's map of the Cursor product family stays complete.
- **Chapter 02 (Harness Engineering) / Chapter 05 (Team Adoption)**: When
  discussing "agent-generated code volume changes engineering
  infrastructure needs" (a theme already present via the Vercel PR-velocity
  metrics in `blog-cursor-vercel-queues.md`), note that this specific
  integration is a data point *against* the idea that platforms are
  building differentiated tooling for agent-authored commits — Vercel's
  Origin integration uses the same Preview/Production trigger rules as any
  other git provider, with no stated agent-provenance or review-policy
  distinction. The guide should not assume "Origin" implies automatic
  agentic-commit detection or governance without evidence, since none was
  found here.

## Extraction Notes

1. **The Prospector's triage "key question" is not answered affirmatively
   by the source, and this note flags that explicitly rather than
   speculating further.** All three triage comments on the issue asked
   variants of "what does 'Cursor Origin' detection enable for deployment
   automation / provenance tracking / agentic workflows" — implicitly
   assuming "Origin" repositories are detected or specially treated by
   Vercel. Reading both the changelog and the full docs page, no such
   mechanism exists: "Origin" is simply the proper name of Cursor's git
   hosting product (analogous to "GitHub" or "GitLab"), and connecting an
   Origin repository to Vercel is a standard git-provider integration with
   no distinct deployment behavior. This is reported as Claim 5/6 and
   flagged prominently in Guide Impact rather than silently omitted, since
   correcting a specific, plausible-sounding misreading in the triage
   record is itself useful signal for the Smith.
2. **Two non-changelog pages followed, per MINER.md §1.** `/docs/git/vercel-for-origin`
   (the changelog's own documentation link) was followed in full. `cursor.com/origin`
   was also fetched — not linked from the changelog, but linked in-line
   from the docs page's own definition of "Origin" — specifically to
   answer what Origin is, since neither Vercel page defines it beyond
   "Cursor's Git platform."
3. **WebFetch output verified against raw HTML/markdown for all three
   pages, per MINER.md §2a.** The changelog and docs page were retrieved
   via `curl` against their markdown alternates (`Accept: text/markdown`)
   and found to match the corresponding WebFetch summaries in substance;
   all `Quote` fields in this note are taken from the directly-fetched raw
   markdown, not from WebFetch's prose summary. The `cursor.com/origin`
   marketing page does not expose a markdown alternate (returns full
   rendered HTML), so its quotes were verified by `grep`-ing the raw HTML
   response directly for the exact quoted strings (meta description, Open
   Graph tags, and body copy), rather than trusting WebFetch's paraphrase.
4. **Source is thin by design (a ~120-word changelog plus a short docs
   page).** This is a feature-announcement changelog, not a technical deep
   dive — six claims fully exhaust the concrete, checkable content across
   both pages. No metrics, named customers, or architecture detail beyond
   what's quoted here exist in the source family. Confidence is rated
   "emerging" overall (not "settled") because both halves of the
   integration — Vercel's side (public beta) and Origin itself (early
   beta / research preview, two different labels used inconsistently
   between the changelog and docs page — see Claim 4) — are explicitly
   pre-GA, and no independent or third-party account of using this
   integration was found.
5. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts.
