---
source_url: https://vercel.com/changelog/sign-jwts-from-your-functions-without-managing-private-keys
source_type: blog-post
title: "Sign JWTs from your Functions without managing private keys"
author: Marc Greenstock, Lakshay Bhushan, Luc Leray, Dima Voytenko, Yvonne Zhou, Jeff Pope (Vercel)
date_published: 2026-08-18
date_extracted: 2026-09-15
last_checked: 2026-09-15
status: current
confidence_overall: emerging
issue: "#3456"
---

# Sign JWTs from your Functions without managing private keys

> Vercel changelog announcing Vercel KMS — a managed asymmetric-signing service
> that lets a Vercel Function sign JWTs and raw messages using a deployment's
> ambient OIDC token, so no private key material ever lives in code or
> environment variables, with public verification via per-issuer OIDC
> discovery/JWKS endpoints that any external relying party can use with
> standard libraries.

## Source Context

- **Type**: blog-post (Vercel product changelog, `vercel.com/changelog`; a
  short feature-announcement entry — one intro paragraph, a capability list,
  three code samples, a best-practice note, and a beta-status disclaimer). Per
  MINER.md §1, five linked first-party docs pages were followed because the
  changelog entry itself is thin relative to the feature's actual surface
  area: `vercel.com/docs/kms` (the product overview page, read in full),
  `vercel.com/docs/kms/concepts/authentication` (read in full),
  `vercel.com/docs/kms/concepts/key-rotation` (read in full),
  `vercel.com/docs/kms/quickstart` (read in full), and
  `vercel.com/docs/kms/concepts/project-grants` (read in full). All five were
  fetched via the same `text/markdown` content-negotiation approach as the
  main changelog page (see Extraction Notes) and confirmed self-consistent
  with the changelog and with each other everywhere they overlap.
- **Author credibility**: First-party Vercel product-team announcement,
  credited to six named engineers (Marc Greenstock, Lakshay Bhushan, Luc
  Leray, Dima Voytenko, Yvonne Zhou, Jeff Pope) in the changelog byline — a
  larger credited team than the single-author changelog entries elsewhere in
  this corpus (e.g. `blog-vercel-flags-oidc-default-auth.md`), consistent
  with KMS being a new product surface rather than a configuration-default
  tweak to an existing one. No independent third-party benchmark, customer
  story, or adoption metric appears anywhere in the source family — this is
  vendor documentation of a shipping (beta) feature, not independent
  reporting.
- **Scope**: Covers creating and rotating KMS issuers and signing keys (RSA,
  ECDSA, EdDSA), signing JWTs with custom claims and TTL or raw messages via
  `@vercel/kms`, per-environment project grants, claims-schema validation,
  public OIDC-discovery/JWKS verification, the two-tier signing-vs-management
  authorization split, and staged key rotation. Does **not** cover: pricing
  rates or platform limits in detail (the docs page defers to a separate
  `/docs/kms/pricing` page, not fetched — out of scope for a changelog-
  anchored note), the full `@vercel/kms` SDK reference (`/docs/kms/ts-sdk-
  reference`, not fetched), Connect grants in mechanistic detail (`/docs/kms/
  concepts/connect-grants`, referenced but not fetched — the fifth-page
  budget was spent on `project-grants` instead, judged more central to the
  "no private key management" headline claim), or any production usage
  evidence, GA timeline, or independent security review of the service.

## Extracted Claims

### Claim 1: Vercel KMS lets a Vercel Function sign JWTs and arbitrary messages using managed asymmetric keys, authenticated by the deployment's own Vercel OIDC token, so private keys never live in the function's code or environment variables
- **Evidence**: Direct first-party statement of the feature's core mechanism, corroborated identically in the docs overview page's opening paragraph.
- **Confidence**: settled (unambiguous, first-party description of a named, shipping mechanism, consistent across two independently-fetched pages)
- **Quote**: "Vercel KMS lets you sign JWTs and arbitrary messages from your Vercel Functions using managed asymmetric signing keys, so private keys never live in your code or environment variables. Your function authenticates with its Vercel OIDC token, and the private key stays inside Vercel's key management service while verifiers use only the public key."
- **Quote (docs overview, corroborating)**: "You sign JWTs and messages by calling the KMS signing API from your Vercel Functions, and Vercel publishes the matching public keys so any relying party can verify the result. Your private keys never leave Vercel, so you avoid storing signing material in environment variables."
- **Our assessment**: This is the same "ambient deployment OIDC token replaces a manually-configured static credential" pattern already documented twice elsewhere in this corpus for Vercel's own products (`blog-vercel-flags-oidc-default-auth.md` Claim 1, `blog-vercel-github-tools-eve.md` Claim 5), but applied to a materially different credential type: those two cases eliminate a *bearer token or PAT* a deployment would otherwise need to authenticate *itself* to a backend; this case eliminates the *private signing key* a deployment would otherwise need to hold in order to mint credentials *for others* to verify. See Cross-References → Novel.

### Claim 2: Verification requires no contact with Vercel at all — every KMS issuer publishes a public JWKS and an OpenID Connect Discovery document at stable, predictable URLs, so any standard OIDC or JOSE library can verify a signed token with no Vercel-specific code
- **Evidence**: Direct statement of the verification-side architecture, with the exact endpoint URL patterns given, corroborated by a working code sample using the third-party `jose` library and repeated near-verbatim on two further docs pages (authentication, quickstart).
- **Confidence**: settled (first-party, with runnable third-party-library code, consistent across four independently-fetched pages)
- **Quote**: "Verify signed tokens anywhere. Each issuer publishes a public OpenID Connect Discovery document at `https://kms.vercel.com/<issuerId>/.well-known/openid-configuration` and a JWK set at `https://kms.vercel.com/<issuerId>/jwks.json`, so any standard OIDC or JOSE library can validate tokens without Vercel-specific code."
- **Quote (verification code, verbatim)**: "const issuer = 'https://kms.vercel.com/123e4567-e89b-42d3-a456-426614174000';\nconst jwks = createRemoteJWKSet(new URL(`${issuer}/jwks.json`));\n\nconst { payload } = await jwtVerify(token, jwks, { issuer });"
- **Our assessment**: This is the architecturally significant half of the feature that the changelog headline ("without managing private keys") undersells: it is not just that Vercel manages the *signing* side for you, but that the *verifying* side can be any arbitrary third party — a partner API, a customer's own backend, an open-source library consumer — with zero Vercel account, API key, or SDK dependency, purely because JWKS/OIDC-discovery are open, standardized formats. This is a stronger claim than the ambient-OIDC patterns in `blog-vercel-flags-oidc-default-auth.md` and `blog-vercel-github-tools-eve.md`, both of which are Vercel-to-Vercel (or Vercel-to-GitHub-via-Connect) exchanges; here the relying party can be a system Vercel has no relationship with at all.

### Claim 3: KMS authorizes two different classes of operation with two different credential types — signing requests use a short-lived deployment OIDC token, while management operations (such as staging or activating a key during rotation) use a longer-lived Vercel access token
- **Evidence**: Direct statement of the authorization-boundary design, with a runnable `curl` example showing the access-token header for a management call.
- **Confidence**: settled (first-party, explicit architectural statement with a concrete example)
- **Quote**: "KMS authorizes requests differently depending on what you are doing. Signing is authorized with a short-lived deployment OIDC token, management operations are authorized with a Vercel access token, and relying parties verify signatures against the issuer's published JWKS without authenticating at all."
- **Quote (management call, verbatim)**: "curl -X POST \\\n  \"https://api.vercel.com/v1/kms/issuers/f47ac10b-58cc-4372-a567-0e02b2c3d479/keys\" \\\n  -H \"authorization: Bearer $VERCEL_TOKEN\" \\\n  -H \"content-type: application/json\" \\\n  -d '{ \"activation\": \"automatic\" }'"
- **Our assessment**: This three-way split (ephemeral OIDC for the high-frequency, per-request signing path; a standing access token for the low-frequency, human-or-CI-triggered management path; no authentication at all for the high-frequency, externally-triggered verification path) is a deliberately different credential lifetime for each access pattern's actual risk/frequency profile, rather than a single uniform auth mechanism applied everywhere. It is a concrete illustration of matching credential lifetime to operation frequency and blast radius, a design principle implicit but not spelled out this explicitly in the corpus's other OIDC-pattern sources.

### Claim 4: KMS supports two policy kinds that separate signing-only access from provisioning access: a project grant lets a Vercel deployment sign with its own OIDC token, scoped to one team, one project, and specific environments, and confers "signing access only, never provisioning"; a Connect grant lets Vercel Connect provision and sign with an issuer on behalf of the team
- **Evidence**: Direct statement on the authentication concepts page, elaborated with the full field list and verification logic on the dedicated project-grants page.
- **Confidence**: settled (first-party, consistent across two independently-fetched pages, with an explicit field table)
- **Quote**: "A policy is the rule that authorizes signing for an issuer. KMS supports two policy kinds: Project grant (project-grant): lets a Vercel deployment sign with its OIDC token, scoped to a project and its environments. It confers signing access only, never provisioning. Connect grant (connex-grant): lets Vercel Connect provision and sign with the issuer on behalf of your team, identified by a Connect client ID."
- **Quote (project-grant verification logic, verbatim)**: "When a deployment signs, KMS verifies its Vercel OIDC token, issued by `https://oidc.vercel.com`, and checks that: `owner_id` matches both the issuer's owning team and the grant's `teamId`. `project_id` matches the grant's `projectId`. `environment` is one of the grant's `environments`. If any check fails, KMS rejects the signing request."
- **Our assessment**: This directly ties the new KMS product into the existing Vercel Connect architecture already documented in this corpus (`blog-vercel-enterprise-apps-and-agents.md` Claims 4-7, `blog-vercel-github-tools-eve.md` Claim 5): a deployment's own OIDC token is deliberately restricted to signing-only, while any *provisioning* of new issuers or keys on a team's behalf is routed through Connect specifically — the same "provisioning is a distinct, more privileged operation than day-to-day use" separation Connect already enforces for GitHub App management in the eve/GitHub-tools integration. See Cross-References → Extends.

### Claim 5: KMS signing keys support RS256/RS384/RS512, the PS* and ES* algorithm families, and default to RS512; KMS does not support symmetric (HS*) keys; and an issuer's key can either be generated by KMS itself ("vercel-origin") or imported as an existing PEM private key ("external-origin"), with the external option named specifically for cases where another party (e.g. a GitHub App) generates the key pair and keeps the public half
- **Evidence**: Direct, itemized statement on the docs overview's "KMS primitives" section.
- **Confidence**: settled (first-party, specific and itemized algorithm/origin list)
- **Quote**: "Signing keys: The key material an issuer signs with. KMS supports RS256, RS384, RS512, the PS* and ES* families, and defaults to RS512. KMS does not support symmetric (HS*) keys."
- **Quote (key origin)**: "Key origin: KMS can generate the key for you (a vercel-origin issuer), or you can import an existing PEM private key (an external-origin issuer). Import a key when the other side generates the key pair and keeps your public key, such as a GitHub App."
- **Our assessment**: The explicit exclusion of symmetric (HS*) algorithms is a meaningful design constraint worth flagging: KMS is architected exclusively around the asymmetric sign-with-private/verify-with-public split that makes the "verify anywhere with no Vercel contact" property (Claim 2) possible — a symmetric HMAC key would require the verifier to hold the same secret as the signer, which would defeat the entire "verifiers use only the public key" premise. The external-origin/GitHub-App example is a concrete, named use case connecting this feature to exactly the credential architecture already documented in `blog-vercel-github-tools-eve.md` (Vercel Connect "manages the GitHub App for you, which means you never register an app or handle a private key" — that note's Claim 5), suggesting KMS may be positioned as infrastructure other Vercel products build on, not only a standalone developer-facing feature.

### Claim 6: A project grant can constrain which claims a project is allowed to request, and an issuer can separately define a JSON Schema that validates every token it signs, regardless of which grant authorized the request
- **Evidence**: Brief statement on the authentication concepts page, cross-referenced to a dedicated (unfetched) "Claims" page.
- **Confidence**: settled (first-party statement of a named capability, though the mechanism's detail lives on a page this note did not fetch)
- **Quote**: "A policy can also define KMS-owned tokenClaims, and an issuer can define a claims schema that validates every token it signs. See Claims."
- **Our assessment**: This is a two-layer claims-control model — grant-level constraint on what a *given caller* may request, plus issuer-level schema validation applied to *every* signed token regardless of caller — that the source only gestures at without giving the JSON Schema syntax or an example. Flagged here as a claim worth a lower-confidence caveat: the *existence* of the two-layer model is settled (stated plainly), but its exact enforcement mechanics are not verifiable from the pages this note fetched, since `/docs/kms/concepts/claims` was not one of the five linked pages followed (see Extraction Notes and Source Context → Scope).

### Claim 7: Key rotation moves through three named stages — staging a pending key (added to the JWKS immediately but not yet signing), activating it (becomes the active signer, either automatically once the JWKS CDN cache has had time to invalidate, or manually on demand), and retiring the previous key after a configurable grace period — all without changing the issuer's ID or JWKS URL, so relying parties never need to update anything
- **Evidence**: Direct, itemized statement of the three-stage model, with a full explanation of the automatic-vs-manual activation choice and the grace-period configuration.
- **Confidence**: settled (first-party, detailed mechanism description with two runnable `curl` examples)
- **Quote**: "Rotating an issuer's key moves through three stages: Stage a pending key: KMS creates a new signing key and immediately adds its public key to the issuer's published JWKS... Activate: the pending key becomes the active signer and KMS starts signing new tokens with it... Retire the previous key: when the new key activates, the previously-active key stops signing but stays in the JWKS for a grace period so already-issued tokens keep verifying."
- **Quote (grace period)**: "You control the grace period with `revokePreviousAfterHours`, the number of hours after activation that the previous key keeps verifying. It defaults to 1 hour, and you should set it to at least the longest lifetime of the tokens you have signed. Set it to 0 to retire the previous key immediately at activation."
- **Our assessment**: This is a concrete, reusable operational pattern independent of Vercel specifically: the core problem — how do you rotate a signing key without invalidating tokens that are still "in flight" and without requiring every relying party to coordinate the exact moment of cutover — is solved here by (a) publishing the new public key *before* using it, to let CDN/client caches catch up, and (b) keeping the *old* public key published for a bounded grace period *after* it stops signing, sized to the longest-lived token still in circulation. The explicit warning to set the grace period to at least the longest token TTL is the kind of self-disclosed operational detail (get this wrong and rotation silently breaks already-issued tokens) worth surfacing directly to readers designing their own credential-rotation schemes, not just Vercel KMS users.

### Claim 8: Vercel recommends creating a separate issuer per project and per environment (e.g. distinct issuers for production, preview, and development) rather than sharing one issuer across projects or environments, in order to keep each issuer's signing surface and published JWKS scoped to the smallest audience and limit blast radius
- **Evidence**: Stated as an explicit best practice in both the changelog and the docs overview, with the same three justifications repeated in near-identical language.
- **Confidence**: settled (first-party, explicit and repeated best-practice recommendation)
- **Quote (changelog)**: "As a best practice, create a separate issuer per project and environment. Isolating issuers keeps each token audience distinct, scopes signing access to exactly one project and environment, and lets you rotate or revoke keys for one without affecting the others."
- **Quote (docs overview)**: "Create a separate issuer for each project and each environment... Scoping issuers this way: Keeps each issuer's signing policy limited to the smallest surface. Isolates each published JWKS, so a relying party can trust one project and environment at a time. Limits blast radius, and lets you rotate or revoke one issuer's keys without affecting the others."
- **Our assessment**: This mirrors the same "narrow scope by default" instinct already documented for Vercel Connect's per-request credential scoping (`blog-vercel-enterprise-apps-and-agents.md` Claim 6: a GitHub token request "can be restricted to a named repository and specific permissions... for that one call") and for project grants generally (Claim 4 above) — a consistent Vercel-wide design posture of defaulting new credential/access primitives to the narrowest reasonable scope rather than a shared, broadly-provisioned default.

### Claim 9: `signToken` and `signMessage` resolve the calling function's OIDC token at call time, which requires an active request context — the SDK explicitly warns against calling them at the module top level, and the quickstart's own example calls `signToken` inside a Next.js route handler specifically for this reason
- **Evidence**: An explicit warning callout on both the authentication concepts page and the quickstart tutorial, in near-identical wording, plus the quickstart's own code sample structure (the `signToken` call is inside `export async function GET()`, not at module scope).
- **Confidence**: settled (first-party, explicit self-disclosed constraint stated as a warning callout on two independently-fetched pages)
- **Quote (authentication page)**: "The @vercel/kms SDK resolves the function's OIDC token for you through @vercel/oidc. Because the token is resolved at call time, call signToken and signMessage inside an active request context, not at the module top level."
- **Quote (quickstart warning callout, verbatim)**: "⚠️ Warning: signToken resolves the function's OIDC token at call time, which requires an active request context. Call it inside a route handler or Server Component, not at the module top level."
- **Our assessment**: This is exactly the kind of specific, checkable "this looks like it should work but has a sharp edge" constraint that MINER.md flags as high-value: a developer refactoring `signToken` into a shared helper initialized once at module load (a common pattern for e.g. database clients or SDK instances) would silently break, because the OIDC token that authorizes the signing call is tied to the *request's* execution context, not the module's. The source states this as a hard requirement (not a performance tip), twice, independently.

### Claim 10: Vercel KMS is currently in public beta, available on all pricing plans, with features and behavior subject to change before general availability, and is billed per signing operation with no separate per-key or per-issuer charge
- **Evidence**: An explicit beta-status disclaimer in the changelog, corroborated by the docs overview's pricing summary.
- **Confidence**: settled (first-party, explicit status and billing-model statement, though the underlying GA timeline and detailed rate table are not given)
- **Quote (changelog)**: "Vercel KMS is in beta and available on all plans. Features and behavior may change before general availability. Usage is subject to the Beta Agreement."
- **Quote (docs overview, pricing)**: "KMS is billed per signing operation, with no per-key or per-issuer charge. For the full rate table, limits, and how to stop being billed, see Pricing and Limits."
- **Our assessment**: Per-signing-operation billing (rather than per-key, per-issuer, or a flat platform fee) means the cost model scales directly with how often a deployment mints tokens, which matters for any usage pattern that signs a fresh short-TTL token per request rather than reusing one across many requests — a cost dimension worth flagging for any guide discussion of adopting this pattern at scale, even though this note did not fetch the actual rate table (`/docs/kms/pricing`, out of the five-page budget).

## Concrete Artifacts

### Signing a token inside a Vercel Function (verbatim, from the changelog)

```
Source: https://vercel.com/changelog/sign-jwts-from-your-functions-without-managing-private-keys

import { signToken } from '@vercel/kms';

export async function GET() {
  // Sign a short-lived JWT with your claims.
  const token = await signToken({
    issuerId: '123e4567-e89b-42d3-a456-426614174000',
    claims: { sub: 'user_123', scope: 'read:data' },
    ttl: 300,
  });

  // Send the signed token as a Bearer credential to the downstream API.
  const res = await fetch('https://api.example.com/data', {
    headers: { Authorization: `Bearer ${token}` },
  });

  return new Response(await res.text(), { status: res.status });
}
```

### Verifying a token with a standard JOSE library (verbatim, from the changelog; identical example repeated on the authentication and quickstart docs pages)

```
Source: https://vercel.com/changelog/sign-jwts-from-your-functions-without-managing-private-keys

import { createRemoteJWKSet, jwtVerify } from 'jose';

const issuer = 'https://kms.vercel.com/123e4567-e89b-42d3-a456-426614174000';
const jwks = createRemoteJWKSet(new URL(`${issuer}/jwks.json`));

const { payload } = await jwtVerify(token, jwks, { issuer });
```

### Setting up an issuer and granting project access from the CLI (verbatim, from the changelog)

```
Source: https://vercel.com/changelog/sign-jwts-from-your-functions-without-managing-private-keys

vercel kms add my-issuer --algorithm ES256
vercel kms add-grant 123e4567-e89b-42d3-a456-426614174000 --project my-app --environment production
```

### Staging and activating a rotated key via the management API (verbatim, from the key-rotation docs page)

```
Source: https://vercel.com/docs/kms/concepts/key-rotation

curl -X POST \
  "https://api.vercel.com/v1/kms/issuers/f47ac10b-58cc-4372-a567-0e02b2c3d479/keys" \
  -H "authorization: Bearer $VERCEL_TOKEN" \
  -H "content-type: application/json" \
  -d '{ "activation": "automatic", "revokePreviousAfterHours": 24 }'

curl -X POST \
  "https://api.vercel.com/v1/kms/issuers/f47ac10b-58cc-4372-a567-0e02b2c3d479/keys/<keyId>/activate" \
  -H "authorization: Bearer $VERCEL_TOKEN" \
  -H "content-type: application/json" \
  -d '{ "revokePreviousAfterHours": 24 }'
```

### Public discovery/verification endpoint URL patterns (verbatim, from the docs overview and authentication pages)

```
Source: https://vercel.com/docs/kms and https://vercel.com/docs/kms/concepts/authentication

Issuer URL:          https://kms.vercel.com/<issuerId>
JWKS:                https://kms.vercel.com/<issuerId>/jwks.json
OpenID configuration: https://kms.vercel.com/<issuerId>/.well-known/openid-configuration
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-flags-oidc-default-auth.md`, `blog-vercel-github-tools-eve.md`,
`blog-vercel-enterprise-apps-and-agents.md`, `blog-anthropic-workload-
identity-federation.md`, and `blog-anthropic-zero-trust-ai-agents.md` were
re-read (in full, or via their numbered `### Claim N:` heading list) during
this extraction per MINER.md §4b, and every claim number cited below was
located and confirmed against that note's own numbered claims in document
order before writing this section.

- **Corroborates**:
  - `blog-vercel-flags-oidc-default-auth.md` Claim 1 ("At runtime, the
    Vercel adapter automatically receives a short-lived OIDC token, so
    authentication is handled for you with zero configuration") and
    `blog-vercel-github-tools-eve.md` Claim 5 (Vercel Connect "mints
    short-lived GitHub tokens at runtime so no personal access token lives
    in your environment"): this source's Claim 1 and Claim 9 are a third,
    independent instance of the same Vercel-wide pattern — a deployment's
    ambient OIDC token replaces a static credential a developer would
    otherwise configure — now applied to authorizing a *signing* operation
    rather than authenticating a *read/write* API call. Three products
    (Flags, GitHub Tools via Connect, and now KMS) converging on the same
    "deployment OIDC token, zero stored secret" default strengthens the case
    that this is now Vercel's platform-wide baseline for new features, not a
    one-off.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 12 ("Static API keys and
    shared service-account passwords are... no longer a legitimate
    Foundation posture — short-lived tokens are now the minimum baseline"):
    KMS's entire premise (Claim 1: "private keys never live in your code or
    environment variables") is a product-level instance of that prescribed
    baseline, extended from *bearer tokens* (the examples that note and
    `blog-vercel-flags-oidc-default-auth.md`'s Cross-References focus on) to
    *asymmetric private signing-key material* specifically — a credential
    type none of the corpus's prior OIDC-pattern sources address.
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 6 (Vercel Connect
    scopes a GitHub token request "at the level of an individual request...
    restricted to a named repository and specific permissions... for that
    one call"): this source's Claim 8 (one issuer per project and
    environment, to keep signing surface and JWKS audience minimal) is the
    same narrow-scope-by-default instinct applied to a different credential
    primitive (a signing issuer, not a per-call token grant).

- **Contradicts**: None identified as a MINER.md §4a contradiction. No claim
  in this source opposes any existing corpus note.

- **Extends**:
  - `blog-vercel-flags-oidc-default-auth.md`: that note's Guide Impact
    section explicitly frames Vercel Flags' ambient-OIDC pattern as
    "simplest when a single vendor controls both the token issuer and the
    token verifier" (a wholly Vercel-to-Vercel exchange) and contrasts it
    with cross-organization federation (WIF), which needs configurable
    federation rules because the verifier is a different organization. This
    source's Claim 2 breaks that dichotomy: KMS is a single-vendor (Vercel)
    *issuer*, but the *verifier* can be any arbitrary third party with no
    Vercel relationship at all, using only a public JWKS/OIDC-discovery
    document — a third point on that note's single-vendor-to-cross-
    organization spectrum that neither of the two prior corpus examples
    (ambient Flags OIDC, WIF federation) occupies: Vercel-controlled issuance
    paired with completely open, vendor-agnostic verification.
  - `blog-vercel-github-tools-eve.md` Claim 5 (Vercel Connect mints GitHub
    tokens and "also manages the GitHub App for you, which means you never
    register an app or handle a private key") and Claim 4's "external-origin
    issuer" concept (Claim 5 in this note): this source's project-grant/
    Connect-grant split (Claim 4) and its named external-origin use case
    ("import a key when the other side generates the key pair and keeps
    your public key, such as a GitHub App") directly ties KMS into the same
    Connect-managed-credential architecture that note documents for GitHub
    App private keys specifically — suggesting KMS may function as shared
    infrastructure underneath multiple Vercel products' "no private key
    management" claims, not a standalone feature.
  - `blog-anthropic-workload-identity-federation.md`: that note documents
    WIF as *inbound* federation — external OIDC-compliant identity providers
    (AWS IAM, GCP, GitHub Actions, Okta, etc.) proving identity *to* the
    Claude Platform so it can issue short-lived Claude API access. This
    source is architecturally the mirror image: a Vercel deployment's own
    OIDC identity authorizes it to have Vercel *mint outbound, externally-
    verifiable credentials* (signed JWTs) that a completely separate,
    unrelated system then trusts. Both use OIDC as the trust mechanism, but
    WIF is "let me in using my external identity" while KMS is "let me issue
    credentials that establish identity for someone else to verify" — a
    useful contrast for any guide section explaining OIDC's two distinct
    roles (as a *relying-party* credential and as an *issuing* mechanism) in
    agent/service infrastructure.

- **Novel**:
  - **A managed signing service that turns a deployment's ambient identity
    into the ability to mint externally-verifiable credentials, without the
    deployment or its operator ever holding key material** (Claims 1, 2): no
    prior corpus source documents a platform letting a workload become an
    *issuer* of cryptographically verifiable tokens for arbitrary third-party
    consumption, as opposed to consuming or presenting credentials issued by
    someone else. This is a structurally different capability from every
    other OIDC-pattern source in the corpus, which are all about a workload
    authenticating *itself* to some backend.
  - **A two-tier, per-operation-type authorization split (ephemeral OIDC for
    signing, standing access token for management, no auth for verification)
    matched to each operation's actual frequency and risk profile** (Claim
    3): no prior corpus source states this three-way credential-lifetime-by-
    operation-type design this explicitly.
  - **A CDN-cache-aware, three-stage key-rotation protocol with a
    token-lifetime-driven grace period, designed specifically so relying
    parties never need to coordinate a cutover moment** (Claim 7): this is a
    concrete, reusable rotation mechanism (stage → activate → retire-with-
    grace-period) not documented for any other credential system in the
    corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering) / Chapter 06 (Security and Threat
  Model) — ambient OIDC extended to asymmetric signing-key management**: Add
  this source as a fourth data point (alongside `blog-vercel-flags-oidc-
  default-auth.md`, `blog-vercel-github-tools-eve.md`, and the WIF/zero-trust
  sources) in the "static credentials → short-lived OIDC-backed identity"
  convergence already tracked in the guide, but flag it as a *qualitatively
  different* instance rather than a repeat: prior examples eliminate a
  standing bearer token a deployment needs to authenticate itself; this one
  eliminates a standing *private signing key* a deployment needs in order to
  issue credentials others will trust, and the resulting verification step
  needs no relationship with Vercel at all (Claim 2). Recommend the guide
  distinguish OIDC's two roles explicitly — "proving who I am to someone
  else" (WIF, Connect, ambient Flags auth) versus "authorizing me to mint
  credentials that establish identity for a third party" (this source) — per
  Cross-References → Extends.

- **Chapter 08 (Operations) or wherever credential-rotation guidance lives**:
  Add Claim 7's three-stage rotation protocol (stage a pending key → activate
  once caches have invalidated → retire the previous key after a
  `revokePreviousAfterHours` grace period sized to the longest outstanding
  token TTL) as a concrete, vendor-agnostic reference pattern for how to
  rotate *any* signing/verification key pair without breaking tokens already
  in circulation — useful even for teams not using Vercel KMS specifically,
  as a template for designing their own token-issuance rotation.

- **Chapter 03 (Safety and Verification) or wherever self-disclosed vendor
  constraints are tracked**: Add Claim 9 (the OIDC-token-at-call-time
  constraint that breaks if `signToken`/`signMessage` are hoisted to module
  scope) as another concrete example — alongside the token-staleness gap
  already tracked from `blog-vercel-github-tools-eve.md` Claim 7 — of a
  "looks like ordinary code, breaks in a specific execution-context way"
  pitfall that a team adopting Vercel's ambient-credential patterns should
  check for explicitly rather than discover in production.

## Extraction Notes

1. **Raw content fetched via markdown content-negotiation, cross-checked
   against a WebFetch pass that produced a restructured, non-verbatim
   summary.** An initial `WebFetch` call against the changelog URL returned
   a response with invented section headings not present in the source
   ("Overview," "Key Capabilities," "Best Practices," "Availability") and
   reworded sentences presented without quotation marks. While spot-checking
   showed the *substance* of that WebFetch output was not factually wrong,
   its structure and exact wording were the summarizing model's own
   reconstruction, not the source's actual text — unsuitable for the
   character-for-character `Quote` requirement in MINER.md §2a. This note
   discarded the WebFetch output entirely and instead fetched the page via
   `curl` with an `Accept: text/markdown` header, which the site honors via
   content negotiation (confirmed by a `200` response and clean, unprocessed
   markdown matching the page's actual structure, headings, and code blocks).
   Every `Quote` field in this note was located character-for-character in
   that raw markdown capture (or the equivalent raw markdown capture of each
   linked docs page, fetched the same way). Future extractions of Vercel
   pages should prefer this content-negotiation approach over `WebFetch`'s
   default summarization for any page where verbatim quoting matters.
2. **Five linked pages followed per MINER.md §1**: `vercel.com/docs/kms`
   (product overview — supplied Claims 1, 5, 8, 10), `vercel.com/docs/kms/
   concepts/authentication` (supplied Claims 2, 3, 4, 6, 9), `vercel.com/
   docs/kms/concepts/key-rotation` (supplied Claim 7), `vercel.com/docs/kms/
   quickstart` (supplied Claim 9 corroboration and the quickstart code
   structure), and `vercel.com/docs/kms/concepts/project-grants` (supplied
   Claim 4's full field table and verification logic). Two further linked
   pages — `/docs/kms/concepts/connect-grants` and `/docs/kms/concepts/
   claims` — were not fetched; the five-page budget was spent on the pages
   judged most central to the changelog's headline claim (no private key
   management) rather than on Connect-grant provisioning mechanics or the
   claims-schema syntax. Claim 6 is flagged with a lower-confidence caveat on
   its mechanism detail specifically because of this gap.
3. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts.
4. **Confidence calibration: emerging.** Individual claims are rated
   "settled" because they are unambiguous, first-party statements about a
   named, shipping (beta) feature, cross-checked across five independently-
   fetched pages that agree with each other everywhere they overlap. The
   note's overall confidence is "emerging" rather than "settled" because:
   (a) the feature is explicitly in public beta with "features and behavior
   may change before general availability" (Claim 10) stated by the vendor
   itself; (b) this is a single-vendor documentation family with no
   independent security review, benchmark, or named production customer
   anywhere in the source set; and (c) the feature shipped less than a month
   before extraction (2026-08-18 vs. this note's 2026-09-15 extraction
   date), leaving no track record of how the beta-to-GA transition affects
   any of the documented mechanics.
