---
source_url: https://vercel.com/changelog/authenticate-vercel-flags-with-openid-connect-by-default
source_type: blog-post
title: "Vercel Flags no longer requires SDK Keys for Vercel deployments"
author: Luis Meyer (Vercel)
date_published: 2026-06-24
date_extracted: 2026-07-24
last_checked: 2026-07-24
status: current
confidence_overall: settled
issue: "#2202"
---

# Vercel Flags no longer requires SDK Keys for Vercel deployments

> A short Vercel changelog entry: new projects using Vercel Flags now get a
> short-lived OIDC token automatically at runtime instead of requiring a
> manually-configured SDK Key or `FLAGS` environment variable, with SDK Keys
> remaining required for a named set of cases (cross-project access,
> non-Vercel runtimes, custom auth).

## Source Context

- **Type**: blog-post (Vercel Changelog, `vercel.com/changelog`, published
  June 24, 2026; a single-author changelog entry, not a full product-
  announcement blog post). Two days after Vercel's main Flags-adjacent
  announcement (`blog-vercel-flags-platform-native-feature-flags.md`,
  published June 22, 2026), and post-dates that note's GA claim (Vercel
  Flags went GA in April 2026 per that note's Claim 12).
- **Author credibility**: Luis Meyer, credited as "Software Engineer" at
  Vercel — a named first-party employee byline (with a linked social
  handle), rather than the unattributed "Vercel" or dual-named-author
  bylines seen on the main product-announcement posts in this corpus. This
  is standard for changelog-entry granularity: a specific engineer
  documenting a specific shipped change, not a marketing/product team
  authoring a launch narrative.
- **Scope**: Covers exactly one narrow authentication-configuration change
  to Vercel Flags: new projects deployed on Vercel no longer need an SDK
  Key or `FLAGS` environment variable, because the Vercel adapter now
  receives a short-lived OIDC token automatically at runtime. Also covers
  the local-development credential workflow (`vercel link` / `vercel env
  pull`) and three named cases where SDK Keys are still required. Does
  NOT cover: the mechanics of OIDC token issuance or verification (no
  federation-rule, issuer, or token-lifetime detail is given, unlike the
  much more detailed mechanism description in
  `blog-anthropic-workload-identity-federation.md`); pricing; a rollout
  or migration timeline for extending this to existing projects; or any
  metrics on adoption, incident reduction, or configuration-error rates
  the change is meant to address.

## Extracted Claims

### Claim 1: New Vercel Flags projects no longer need to configure an SDK Key or the `FLAGS` environment variable, because the Vercel adapter automatically receives a short-lived OIDC token at runtime inside a Vercel deployment
- **Evidence**: Direct, first-party statement of a specific configuration-default change, describing both the old requirement (SDK Key / `FLAGS` env var) and the new mechanism (automatic short-lived OIDC token) explicitly.
- **Confidence**: settled (first-party changelog description of a named, shipping default-behavior change)
- **Quote**: "New projects using Vercel Flags no longer need to configure SDK Keys or the FLAGS environment variable when evaluating flags inside a Vercel deployment. At runtime, the Vercel adapter automatically receives a short-lived OIDC token, so authentication is handled for you with zero configuration."
- **Our assessment**: This is Vercel applying the same short-lived-OIDC-token-replaces-static-key pattern documented elsewhere in the corpus for cross-organization credential exchange (Anthropic's Workload Identity Federation, Vercel's own Connect product) to a *first-party, single-vendor, internal* authentication boundary instead: a Vercel deployment authenticating to Vercel's own Flags backend. No federation-rule, issuer-trust, or token-verification detail is given — this is a much shallower description than the WIF or Connect mechanism write-ups, appropriate to a short changelog entry rather than a technical deep-dive.

### Claim 2: The `FLAGS` environment variable and SDK Key were previously mandatory manual configuration steps for evaluating Vercel Flags inside a Vercel deployment, and this change eliminates that configuration step for new projects specifically
- **Evidence**: Implicit in the "no longer need to configure" framing — establishes that a manual credential-configuration step existed before this change and was a new-project onboarding requirement.
- **Confidence**: settled (first-party statement of a prior requirement being removed)
- **Quote**: (no direct quote beyond Claim 1's quote, which covers this point; see paraphrase above)
- **Our assessment**: This is the same "eliminate a manual credential-provisioning step for new workloads" framing documented for Anthropic's WIF (`blog-anthropic-workload-identity-federation.md` Claim 4: WIF "eliminates the need to create, rotate, or leak static... credentials"), but scoped much more narrowly — Vercel Flags removes a single environment-variable/SDK-Key setup step for one specific product, not a platform-wide credential architecture change.

### Claim 3: For local development, the equivalent credential-free workflow is to link the project with `vercel link` and pull credentials with `vercel env pull`
- **Evidence**: Direct instruction given as the local-development counterpart to the automatic runtime OIDC token (which only applies inside an actual Vercel deployment, not on a developer's own machine).
- **Confidence**: settled (first-party, specific CLI-command instruction)
- **Quote**: "For local development, link your project with vercel link and pull credentials with vercel env pull. That's it."
- **Our assessment**: This clarifies an important scope boundary implicit in Claim 1: the "zero configuration" property is specifically a *deployed-on-Vercel-runtime* property (the OIDC token is issued to the deployment itself), not a universal claim — a developer's local machine still needs an explicit credential-pull step, just a simpler one (two CLI commands) than manually copying an SDK Key into a `.env` file.

### Claim 4: This authentication change applies only to new projects — existing projects and all previously-issued SDK Keys continue to work unaffected
- **Evidence**: Direct, explicit scope-limitation statement.
- **Confidence**: settled (first-party, explicit non-breaking-change / migration-scope statement)
- **Quote**: "Existing projects and all SDK Keys are unaffected. This change only applies to new projects, and SDK Keys remain fully supported and are still required for:"
- **Our assessment**: Unlike Anthropic's WIF announcement, which frames API-key/WIF coexistence as an explicit incremental-migration path with an implied trajectory toward full WIF adoption (`blog-anthropic-workload-identity-federation.md` Claim 10, and that note's Guide Impact section explicitly cautioning "Do NOT frame this as 'API keys are still fine'"), this Vercel changelog entry gives no equivalent forward-looking migration guidance for *existing* projects — it states the new default applies only going forward, with no stated plan, timeline, or recommendation for existing projects to adopt OIDC-based auth. This is a narrower, more mechanical scope statement than a migration-path narrative.

### Claim 5: SDK Keys remain required for three specific cases: cross-project flag access, non-Vercel runtimes, and custom authentication setups
- **Evidence**: A named, enumerated list of exceptions to the new OIDC-by-default behavior.
- **Confidence**: settled (first-party, specific enumerated list of exception cases)
- **Quote**: "SDK Keys remain fully supported and are still required for: Cross-project flag access, Non-Vercel runtimes, Custom authentication setups"
- **Our assessment**: This enumerated exception list is the most concrete architectural detail in the entry — it tells us the automatic OIDC token is scoped to "this specific Vercel deployment reading its own project's flags," and breaks down as soon as the access pattern crosses a project boundary, leaves Vercel's own runtime, or requires an authentication scheme Vercel doesn't manage itself. This mirrors the general pattern (seen for WIF and for Vercel Connect) that automatic, ambient, ephemeral credentials work well for the common case but do not eliminate the need for explicit standing credentials in cross-boundary or non-standard scenarios — the entry doesn't reason about *why* these three cases need SDK Keys, but the boundary makes architectural sense: an OIDC token scoped to "this deployment, this project" cannot by itself authorize reading a *different* project's flags, prove identity outside Vercel's own infrastructure, or satisfy an organization's own custom auth policy.

## Concrete Artifacts

### Full changelog entry body (verbatim)

```
New projects using Vercel Flags no longer need to configure SDK Keys or the
FLAGS environment variable when evaluating flags inside a Vercel deployment.
At runtime, the Vercel adapter automatically receives a short-lived OIDC
token, so authentication is handled for you with zero configuration.

For local development, link your project with vercel link and pull
credentials with vercel env pull. That's it.

Existing projects and all SDK Keys are unaffected. This change only applies
to new projects, and SDK Keys remain fully supported and are still required
for:
- Cross-project flag access
- Non-Vercel runtimes
- Custom authentication setups

Read the Vercel Flags documentation to get started.

Source: https://vercel.com/changelog/authenticate-vercel-flags-with-openid-connect-by-default
Published: June 24, 2026. Author: Luis Meyer (Software Engineer, Vercel).
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-flags-platform-native-feature-flags.md`,
`blog-anthropic-workload-identity-federation.md`,
`blog-vercel-enterprise-apps-and-agents.md`,
`blog-anthropic-zero-trust-ai-agents.md`, and
`blog-anthropic-enterprise-managed-auth.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited below was located
and confirmed against that note's own numbered `### Claim N:` headings in
document order before writing this section.

- **Corroborates**:
  - `blog-anthropic-workload-identity-federation.md` Claim 3 ("WIF replaces
    static API keys with short-lived, scoped credentials issued at request
    time") and Claim 4 (eliminates the need to "create, rotate, or leak"
    static credentials): this source's Claim 1 (automatic short-lived OIDC
    token replacing a manually-configured SDK Key / `FLAGS` env var) is the
    same short-lived-OIDC-token-over-static-key architectural pattern,
    independently applied by a second vendor (Vercel, to its own first-party
    Flags product) rather than Anthropic's cross-organization Claude
    Platform access. Two independent vendors converging on ephemeral,
    automatically-issued OIDC tokens as the new default for eliminating
    static-key configuration strengthens the case that this is becoming an
    industry-standard pattern rather than a single-vendor design choice.
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 4 (Vercel Connect:
    "Instead of storing a secret, an agent requests short-lived credentials
    as it works... Tokens are granted per task rather than once and forever,
    and expire when the task is complete."): this source describes the same
    vendor (Vercel) applying an architecturally similar short-lived-
    credential philosophy to a different product (Flags evaluation, not
    third-party SaaS connector access) and a different boundary (Vercel
    deployment → Vercel's own Flags backend, not agent → external system).
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 12 ("Static API keys and
    shared service-account passwords are no longer a legitimate Foundation
    posture — short-lived tokens are now the minimum baseline"; quoted in
    that note as "Static API keys and shared service-account passwords are
    among the first things an attacker with model-assisted code analysis
    will find; they are no longer a legitimate entry point, not even at
    Foundation. Short-lived, narrowly-scoped tokens issued by an identity
    provider are the new baseline."): this is the *normative* claim that
    Claim 1's "Our assessment" is gesturing at. The Vercel changelog shows a
    vendor shipping exactly the posture the zero-trust framework prescribes
    as the minimum baseline — replacing a static SDK Key that "can be grepped
    out of a lockfile" with an automatically-issued short-lived token — so
    this note is not just a second vendor happening to share a pattern with
    WIF, but a concrete product-level instance of an explicitly-stated
    industry baseline. `blog-anthropic-enterprise-managed-auth.md` already
    builds a three-tier convergence around exactly this zero-trust Claim 12
    (Guide Impact → Chapter 03: "Platform-level: WIF", "Connector-level:
    enterprise-managed auth", "Spec-level: zero-trust framework (short-lived
    tokens as minimum baseline everywhere)"); this Vercel Flags note is a
    clean fourth, product-level data point in that same convergence — a
    single vendor's own sub-product defaulting to short-lived OIDC tokens
    rather than static keys.

- **Contradicts**: None identified as a MINER.md §4a contradiction.

- **Extends**:
  - `blog-vercel-flags-platform-native-feature-flags.md`: that note's June
    22, 2026 product announcement documents Vercel Flags' evaluation model,
    dashboard sync, Precompute, CLI, and internal v0 usage in depth, but does
    not mention SDK Keys, the `FLAGS` environment variable, or any
    authentication mechanism at all — authentication is entirely absent from
    that note's Extracted Claims. This source, published two days later,
    fills that specific gap with a first-party statement that (at least as
    of June 24, 2026) SDK Keys were the prior default authentication
    mechanism for new projects, now superseded by automatic OIDC for the
    common case.
  - `blog-anthropic-workload-identity-federation.md`: that note documents
    WIF as a cross-organization credential-federation architecture (external
    OIDC-compliant identity providers — AWS IAM, GCP, Azure, Kubernetes,
    GitHub Actions, Okta — federating into the Claude Platform, with
    federation rules, service accounts, and fine-grained scopes as named
    configurable primitives). This source describes a narrower, single-
    vendor case: Vercel's own deployment runtime issuing an OIDC token to
    Vercel's own Flags backend, with none of WIF's configurable federation-
    rule or scope machinery described or apparently needed, because both
    ends of the credential exchange are already Vercel-operated. This is a
    useful contrast for the guide: the "automatic, zero-configuration OIDC"
    pattern is simplest when a single vendor controls both the token issuer
    and the token verifier (this source); cross-organization credential
    federation (WIF) necessarily requires the additional configuration
    surface of federation rules and identity-provider trust that this
    single-vendor case doesn't need.

- **Novel**:
  - **First-party, single-vendor "zero configuration" OIDC default for a
    specific SaaS-platform sub-product** (Claim 1): no prior corpus source
    documents a vendor eliminating a manually-configured static credential
    for one of its own products (Flags) by having its own deployment
    runtime and its own backend service exchange an OIDC token with no
    federation-rule or identity-provider configuration required from the
    customer at all. This is architecturally simpler than WIF or Connect
    (both of which retain configurable federation/authorization surfaces)
    because it is a wholly-Vercel-to-Vercel credential exchange.
  - **Named enumeration of when a "zero configuration" default still
    requires a fallback static credential** (Claim 5): the three named
    exceptions (cross-project access, non-Vercel runtimes, custom auth) are
    a concrete, specific boundary condition for an automatic-credential
    default that no other corpus source enumerates this precisely for any
    other product.

## Guide Impact

- **Chapter 02 (Harness Engineering) / Chapter 06 (Security Threat Model) —
  ambient platform credentials as a narrower case of short-lived-token
  auth**: Add this source as a concrete, narrow example of the short-lived-
  OIDC-token pattern (already documented at cross-organization scale via
  `blog-anthropic-workload-identity-federation.md`) applied within a single
  vendor's own platform: no static key to provision, rotate, or leak for
  the common case, at the cost of the mechanism only working when both
  ends of the exchange are controlled by the same vendor. Frame this as a
  spectrum: single-vendor ambient OIDC (this source) requires the least
  configuration but is the least portable; cross-organization OIDC
  federation (WIF) requires more configuration (federation rules, scopes)
  but works across arbitrary identity providers and API boundaries. Note
  the three named exception cases (Claim 5) as the guide's concrete example
  of where "zero configuration" auth defaults break down: crossing a
  project boundary, leaving the vendor's own runtime, or needing a custom
  auth scheme. Frame this against the zero-trust baseline explicitly, not
  just as a two-vendor (WIF/Connect) pattern: `blog-anthropic-zero-trust-
  ai-agents.md` Claim 12 states that static keys are "no longer a legitimate
  Foundation posture" and short-lived tokens are "the new baseline," and
  `blog-anthropic-enterprise-managed-auth.md` already frames a three-tier
  convergence (Platform/Connector/Spec-level) around that claim. This Vercel
  Flags change is a concrete product-level data point that the baseline is
  showing up as a shipped default in commodity developer tooling, not only
  in security-framework prescriptions — a useful "the industry norm is
  already the product default" example for the guide.

- **Chapter 05 (Team Adoption) — migration-scope caution**: Contrast this
  source's bare "this change only applies to new projects" scope statement
  (Claim 4) with WIF's more deliberate incremental-migration framing
  (`blog-anthropic-workload-identity-federation.md` Claim 10 and Guide
  Impact, which explicitly warns against treating key/OIDC coexistence as
  a permanent policy). This source gives existing-project teams no
  equivalent nudge to adopt the new default — the guide should note that
  vendor changelog entries scoped to "new projects only" may require teams
  to proactively check whether an existing project could benefit from a
  newer default, since the vendor is not surfacing a migration path here.

## Extraction Notes

1. **Source is a short changelog entry, not a full blog post.** The entire
   body is three short paragraphs plus a three-item list — verified in full
   against the raw page HTML (fetched via `curl` with a browser user agent;
   the site is a Next.js app with article text present in an escaped
   Contentful-style JSON payload embedded in the page). Every quoted phrase
   in this note was located character-for-character in that raw HTML.
   Given the source's length, five claims is the full set of distinct,
   substantive statements available — MINER.md's "aim for 5-15 claims"
   guidance assumes a longer source; this entry does not contain enough
   distinct content to support more without inventing claims not actually
   present in the text.
2. **No sub-pages followed beyond the linked docs page.** The changelog
   entry links to `https://vercel.com/docs/flags` ("Read the Vercel Flags
   documentation to get started"). That page was fetched and found to be a
   generic product-overview page (last updated June 16, 2026, before this
   June 24, 2026 changelog entry) that does not mention OIDC, SDK Keys, or
   the `FLAGS` environment variable at all — it was not a substantive
   companion page and contributed no additional claims.
3. **No metadata beyond byline and publish/modify timestamps available.**
   The raw HTML confirms `datePublished: 2026-06-25T00:00+02:00` (rendered
   in the article as "24 Jun 2026" in the reader's local time zone) and
   `dateModified: 2026-06-25T10:00:14.112Z`; author confirmed as Luis Meyer,
   "Software Engineer," via embedded JSON-LD person data.
4. **No contradiction issues filed.** No claim in this source materially
   opposes any existing source note; see Cross-References → Contradicts.
5. **Confidence calibration: settled.** All five claims are direct,
   unambiguous, first-party statements about a specific, narrow, already-
   shipped default-behavior change, with no marketing framing, no anecdotal
   internal-usage narrative, and no unverified metric or projection —
   unlike several other Vercel announcement posts in this corpus (e.g.
   `blog-vercel-flags-platform-native-feature-flags.md`,
   `blog-vercel-enterprise-apps-and-agents.md`) that mix settled product-
   mechanism claims with anecdotal dogfooding narratives or marketing
   framing and are rated "emerging" overall as a result. This entry
   contains no such anecdotal or marketing content to weigh down the
   overall rating.
