---
source_url: https://vercel.com/changelog/project-scoped-tokens
source_type: blog-post
title: "Project-scoped Tokens"
author: Dominic Sciascia, Mark Roberts, Bel Curcio (Vercel)
date_published: 2026-07-30
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#3028"
---

# Project-scoped Tokens

> Vercel changelog announcement: Vercel Access Tokens can now be scoped to a
> single project, restricting the token to reading and writing only that
> project's resources and denying any request against another project, a
> user-level resource, or a team-level resource — a further narrowing of the
> token-scoping model beyond the team-scoped tokens Vercel shipped in 2022.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published July 30, 2026; a very short feature-announcement entry — the
  entire article body is approximately 150 words, one short paragraph plus a
  five-step "how to create one" list, with no FAQ, code example, or API
  reference section attached, unlike several longer Vercel changelog entries
  already in this corpus, e.g. `blog-vercel-ai-gateway-api-key-budgets.md`).
- **Author credibility**: First-party Vercel product announcement, listing
  three named authors with public profile links (Dominic Sciascia, Mark
  Roberts, Bel Curcio), consistent with Vercel's changelog byline convention.
  Mark Roberts is also a listed co-author on `blog-vercel-ai-gateway-api-key-budgets.md`.
  Vercel operates the Access Tokens / REST API product being described, so
  the scoping mechanics and creation steps are authoritative first-party
  documentation of a shipping capability, not third-party reporting or a
  customer anecdote.
- **Scope**: Covers exactly one capability — restricting a Vercel Access
  Token's read/write access to a single named project at creation time — and
  the UI steps to create one. Does NOT cover: pricing, an API/CLI method for
  creating a project-scoped token programmatically (the article only
  describes the Dashboard "Account Tokens page" flow), token lifetime
  limits, whether project-scoped tokens can be listed or audited separately
  from other tokens, rate limits, or any interaction with team-scoped tokens
  once a project-scoped token exists. The linked `Vercel Access Tokens` and
  `Vercel API` references in the article point to
  `vercel.com/docs/rest-api#authentication` and `vercel.com/docs/api`
  respectively; neither of those pages contains additional prose about
  project-scoped tokens specifically — both surfaced only as inbound-link
  listings pointing back to this same changelog entry (see Extraction
  Notes). A separate, considerably older Vercel changelog entry,
  "Access tokens can now be scoped to teams" (dated 15 Mar 2022, discovered
  via the REST API docs page's own backlink list), documents team-level
  token scoping as a prior, coarser-grained step in the same feature
  lineage; it is used here only for the single dated fact in Claim 5, not
  as a fully mined companion source.

## Extracted Claims

### Claim 1: A project-scoped token can only read and write resources belonging to the single project it is scoped to; any request against a different project, a user-level resource, or a team-level resource is denied
- **Evidence**: Direct statement of the access-control mechanism in the article's opening definitional paragraph.
- **Confidence**: settled (first-party description of a shipping, non-beta platform capability, verified against raw page HTML — see Extraction Notes)
- **Quote**: "A project-scoped token can only read and write resources belonging to a project that the token is scoped to. Requests to any other project, a user-level resource, or a team-level resource will be denied."
- **Our assessment**: This is a hard-deny, not a soft-warn, access boundary — the language is unconditional ("will be denied"), with no mention of an override, an admin-approval path, or a grace period, unlike some other credential-governance features in this corpus that ship with soft caps or propagation delays (contrast `blog-vercel-ai-gateway-api-key-budgets.md` Claim 2's "soft cap, not a hard limit"). The three named excluded scopes (other project, user-level, team-level) matter because they establish that a project-scoped token is strictly narrower than every other existing Vercel token scope, not just narrower than an unscoped token — it cannot even reach the user's own account-level resources or other team-level resources the user/team can otherwise access.

### Claim 2: The stated purpose of project-scoped tokens is to ensure jobs, tools, or workflows granted such a token can only ever touch the one project they are scoped to
- **Evidence**: A single explanatory sentence immediately following the access-denial rule, framing the *why* rather than repeating the mechanism.
- **Confidence**: settled (first-party statement of design intent for a shipping feature)
- **Quote**: "This ensures jobs, tools, or workflows only ever access the projects they are scoped to."
- **Our assessment**: The three named consumers — "jobs, tools, or workflows" — are non-human/automated callers, not individual developers browsing the dashboard. This framing positions the feature specifically as a machine-credential control: the target use case is a CI job, a third-party integration, or an agent/automation that needs Vercel API access to exactly one project's resources and nothing else. This is a narrower and more specific framing than the general "least-privilege access" language used in the page's `<meta name="description">` tag (not itself a quotable body claim, but consistent framing).

### Claim 3: Creating a project-scoped token requires drilling down through a team-scoped selector to a specific project inside the Account Tokens page, then setting an expiration before the token is created and shown exactly once
- **Evidence**: The article's five-step ordered list under the "Creating a project-scoped token" heading.
- **Confidence**: settled (first-party description of a shipping UI flow)
- **Quote**: "Open the Scope dropdown and select the team that owns the project, then click the team to drill into its list of projects" / "Select the project you want the token to be limited to" / "Choose an expiration and click Create" / "Make a note of the token created as it will not be shown again"
- **Our assessment**: The creation flow itself reveals the underlying data model: scope selection is a two-step drill-down (team, then project within that team), meaning a project-scoped token is always created in the context of a specific team's project — there is no team-independent, cross-team project selector shown. The mandatory expiration step ("Choose an expiration and click Create") means an indefinite/non-expiring project-scoped token is not offered as a default path in this flow, though the article does not state whether "no expiration" is one of the selectable options (contrast the AI Gateway budget feature's explicit `none` refresh-period option, `blog-vercel-ai-gateway-api-key-budgets.md` Claim 6) — this is a genuine gap in what the source discloses, not a claim we can make either way. The one-time-display rule ("will not be shown again") is the same secret-hygiene pattern common to nearly all bearer-token issuance flows and is not specific to project scoping.

### Claim 4: Project-scoped tokens are a further narrowing of a token-scoping model whose previous coarsest step was scoping a token to a team, a capability Vercel shipped over four years earlier
- **Evidence**: A separate Vercel changelog entry, "Access tokens can now be scoped to teams," dated 15 Mar 2022, discovered via the REST API docs page's backlink list of changelog entries referencing that page — not linked directly from the project-scoped-tokens article itself.
- **Confidence**: settled (first-party changelog dates from the same publisher, both independently fetched and verified)
- **Quote**: "Access tokens used in the CLI and for authenticating APIs can now be scoped to specific Teams." (from the 15 Mar 2022 entry, not the source under review for this issue)
- **Our assessment**: This establishes a timeline for Vercel's token-scoping granularity: unscoped account tokens, then team-scoped tokens (2022), then project-scoped tokens (2026) — each step narrowing the blast radius of a leaked or misused token by one organizational level. This is background context discovered while investigating this source's linked pages, not itself part of the source under review; it is included here because it directly bears on how novel the July 2026 feature actually is (an incremental narrowing of an existing scoping axis, not a first-of-its-kind access control), which affects the Guide Impact framing below.

## Concrete Artifacts

### Full article text (verbatim, from the changelog page's rendered article body)

```
You can now create Vercel Access Tokens that are limited to a project to
authenticate and use the Vercel API.

A project-scoped token can only read and write resources belonging to a
project that the token is scoped to. Requests to any other project, a
user-level resource, or a team-level resource will be denied. This ensures
jobs, tools, or workflows only ever access the projects they are scoped to.

Creating a project-scoped token

Navigate to the Account Tokens page, found under the Settings area of your
Account.

1. Enter a descriptive token name
2. Open the Scope dropdown and select the team that owns the project, then
   click the team to drill into its list of projects
3. Select the project you want the token to be limited to
4. Choose an expiration and click Create
5. Make a note of the token created as it will not be shown again

Source: https://vercel.com/changelog/project-scoped-tokens (published 30 Jul 2026)
```

### Page metadata (verbatim)

```
<title>: Project-scoped Tokens - Vercel
<meta name="description">: Create Vercel access tokens scoped to a project.
Project-scoped tokens limit API access to a project's resources, so any
tool or workflow gets least-privilege access.

Authors (byline, with linked GitHub profiles): Dominic Sciascia
(github.com/duhminick), Mark Roberts, Bel Curcio
Published: <time dateTime="2026-07-30T00:00+00:00">30 Jul 2026</time>

Source: https://vercel.com/changelog/project-scoped-tokens
```

## Cross-References

### Cross-reference verification notes
`blog-anthropic-workload-identity-federation.md`,
`blog-anthropic-agent-identity-access-model.md`,
`blog-vercel-enterprise-apps-and-agents.md`, and
`blog-vercel-ai-gateway-api-key-budgets.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited below was located
and confirmed against that note's own numbered `### Claim N:` headings in
document order before writing this section.

- **Corroborates**:
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 6 (Vercel Connect
    scopes external-provider credentials down to a single API request —
    e.g. a GitHub token restricted to one repository, read-only, for one
    call — with the framing "Least privilege becomes the shape of the
    request"): this source's project-scoped token (Claim 1 here) is the
    same least-privilege-by-scoping philosophy applied one layer up, at the
    Vercel platform's own first-party Access Token / REST API layer rather
    than at externally-connected third-party systems via Connect. Both are
    Vercel narrowing a credential's reach to the smallest unit that still
    lets the intended job/tool/workflow function — Connect at per-request
    granularity for external connectors, project-scoped tokens at
    per-project granularity for the Vercel API itself.
  - `blog-anthropic-workload-identity-federation.md` Claim 3 ("WIF replaces
    static API keys with short-lived, scoped credentials issued at request
    time"): the *scoping* half of that principle (narrow the credential to
    only what is needed) is corroborated here, though the *ephemeral* half
    is not — this source's tokens are long-lived, user-created bearer
    tokens with a configurable expiration, not short-lived tokens issued
    per request. Project-scoped tokens narrow the "what can this credential
    reach" axis without changing the "how long does this credential live"
    axis that WIF and Vercel Connect (Claim 4/5 in
    `blog-vercel-enterprise-apps-and-agents.md`) both address.
  - `blog-anthropic-agent-identity-access-model.md` Claim 4 ("Agent identity
    replaces the question 'what can this user do?' with 'what can this
    agent do in this compartment?'"): this source's stated purpose (Claim 2
    here — "jobs, tools, or workflows only ever access the projects they
    are scoped to") is a narrower, credential-level instance of the same
    compartment-scoping logic: a project is the compartment, and the token
    is the mechanism that confines a non-human caller to it.

- **Contradicts**: None identified. No existing corpus source makes a
  claim about Vercel Access Token scoping that this source disagrees with;
  this is a straightforward, non-overlapping extension of Vercel's existing
  token-scoping surface (see Claim 4 and Extends below).

- **Extends**:
  - `blog-vercel-enterprise-apps-and-agents.md` and
    `blog-vercel-ai-gateway-api-key-budgets.md`: both document distinct
    Vercel credential-governance dimensions — Connect's per-request scoped
    credentials for third-party connectors, and AI Gateway API keys' dollar
    budgets for cost governance. This source adds a third, independent
    Vercel credential-governance dimension for a different credential type
    entirely (the general-purpose Vercel Access Token used for the Vercel
    REST API/CLI, not an AI Gateway key or a Connect-brokered third-party
    credential) and a different axis (project-level access scope, not
    request-level scope or dollar spend).
  - This source's own discovered prior entry ("Access tokens can now be
    scoped to teams," 2022): project-scoped tokens are a direct, one-step
    narrower extension of that existing team-scoping axis for the same
    Vercel Access Token product, four years later (Claim 4).

- **Novel**:
  - **Project-level scoping for Vercel's own general-purpose Access
    Tokens**: no prior corpus source documents Vercel Access Tokens (the
    credential used for direct Vercel REST API/CLI calls) being scopable to
    a single project; prior corpus coverage of Vercel credential scoping
    (`blog-vercel-enterprise-apps-and-agents.md`) is specific to Vercel
    Connect's third-party-connector credentials, a structurally different
    product and credential type.
  - **Explicit denial of user-level and team-level resource access from a
    project-scoped token**: the specific three-way exclusion list (other
    project, user-level, team-level) is a level of access-boundary
    precision not previously documented for this credential type in the
    corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add project-scoped Vercel Access
  Tokens as a concrete, low-effort credential-scoping option for any
  harness/CI job that only needs Vercel API access to one project — e.g. a
  deployment-status check, a project-specific automation, or an agent tool
  that manages a single project's environment variables or deployments.
  Frame it as complementary to, not a replacement for, Vercel Connect's
  per-request scoping (`blog-vercel-enterprise-apps-and-agents.md` Claim
  6): project-scoped tokens are the right tool when the caller needs
  standing (if expiring) access to one project via the Vercel API/CLI
  itself, whereas Connect is the right tool when an agent needs short-lived,
  per-task credentials for a *third-party* connected system (GitHub, Slack,
  Snowflake, etc.).
- **Chapter 06 (Security & Threat Model)**: Add the explicit deny-list
  (other projects, user-level resources, team-level resources) as a
  concrete example of stating an access boundary in terms of what is
  excluded, not just what is included — useful phrasing for practitioners
  documenting their own scoped-credential boundaries. Note the open
  question this source does not answer (Claim 3's assessment): whether a
  non-expiring project-scoped token is selectable, or whether some
  expiration is always mandatory — this is a real gap for any team using
  this feature that wants to reason about the credential's maximum
  possible lifetime, and should be verified directly in the product before
  the guide asserts either way.

## Extraction Notes

1. **WebFetch summarization discarded; verified against raw HTML.** An
   initial WebFetch pass returned a plausible-sounding but subtly
   restructured summary (e.g., compressing the five creation steps into a
   four-step paraphrase and attributing a slightly different sentence
   structure to the core access-denial rule). Per MINER.md §2a, this note
   discards that WebFetch output entirely; every `Quote` field above was
   independently located character-for-character in the page's raw HTML
   (fetched directly via `curl`, since the site is a Next.js app whose
   article text is embedded in escaped form in the rendered HTML) before
   being used here.
2. **Two inline-linked pages checked, per MINER.md §1; neither added
   substantive content.** The article inline-links "Vercel Access Tokens"
   (`vercel.com/docs/rest-api#authentication`) and "Vercel API"
   (`vercel.com/docs/api`). Both were fetched; neither page's own body text
   discusses project-scoped tokens beyond listing "Project-scoped Tokens"
   as one of several changelog entries that link back to that docs page
   (an auto-generated "mentioned in" backlink list, not original prose).
   No further sub-pages were followed from either.
3. **One additional page discovered and partially used for a single dated
   fact (Claim 4), not fully mined.** While checking the REST API docs
   page's backlink list, a separate, much older Vercel changelog entry,
   "Access tokens can now be scoped to teams" (15 Mar 2022), was found and
   fetched to confirm its date and one sentence, since it directly
   contextualizes how incremental this July 2026 feature is. That older
   entry was not itself deeply mined (no separate `### Claim` entries
   beyond Claim 4's single fact, no Concrete Artifacts drawn from it) — if
   a future issue targets that page specifically, it should get its own
   full extraction pass rather than relying on this note's partial use.
4. **Source is genuinely thin.** The full article body is approximately
   150 words: one two-sentence definitional paragraph and a five-step
   creation list, with no code examples, no API/CLI syntax for
   programmatic creation, no FAQ, and no named customer or usage data. This
   is a materially shorter source than most Vercel changelog entries
   already in this corpus (contrast `blog-vercel-ai-gateway-api-key-budgets.md`,
   which links to a much longer technical reference page with API
   examples). Four claims were extracted directly from the source itself
   (Claims 1-3, drawn from its two paragraphs and one list) plus one
   claim drawn from a discovered related page (Claim 4); this falls short
   of MINER.md's "aim for 5-15 claims" guidance because the source does not
   contain more extractable material, not because of a shallow read — both
   inline links and the docs page's backlink list were checked for
   additional substance and none was found.
5. **No contradiction issues filed.** This feature does not conflict with
   any existing corpus claim about Vercel or Anthropic credential scoping;
   it is a straightforward, narrower addition to Vercel's existing
   token-scoping surface (see Cross-References → Contradicts).
6. **Confidence calibration: settled.** Every claim is a first-party,
   unambiguous description of a shipping (non-beta) platform capability,
   verified against directly-fetched raw HTML rather than an AI-summarized
   intermediate. The note is rated "settled" rather than "emerging" despite
   its thinness because there is no beta/private-beta qualifier on this
   feature (contrast the "emerging" rating on
   `blog-vercel-enterprise-apps-and-agents.md`, where three of four
   products are Beta or Private Beta) and no interpretive or forward-looking
   claim is made anywhere in this note.
