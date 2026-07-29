---
source_url: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
source_type: blog-post
title: "Bringing MCP 2026-07-28 to Claude"
author: Anthropic (no individual byline)
date_published: 2026-07-28
date_extracted: 2026-07-29
last_checked: 2026-07-29
status: current
confidence_overall: emerging
issue: "#2289"
---

# Bringing MCP 2026-07-28 to Claude

> First-party Anthropic announcement of the fifth Model Context Protocol spec
> release — moves MCP's core transport from a bidirectional stateful protocol
> to a stateless request/response model (enabling serverless/edge deployment),
> graduates MCP Apps and a new Tasks framework into a versioned extensions
> system, hardens authorization around production OAuth 2.0/OIDC, previews
> private-network MCP tunnels, and reports 400M monthly SDK downloads and
> 950+ directory servers.

## Source Context

- **Type**: blog-post (official claude.com/blog, July 28, 2026; no individual
  byline — published as Anthropic; product/spec announcement)
- **Author credibility**: First-party Anthropic content on the same publishing
  channel as "Building agents that reach production systems with MCP,"
  "Centrally manage authorization for MCP connectors," and "Observability for
  developers building connectors." The protocol-level claims (stateless core,
  extensions framework, auth alignment) are verifiable against the public spec
  at `modelcontextprotocol.io/specification/2026-07-28`. The ecosystem
  statistics (400M downloads, 950+ servers) and partner quotes are
  Anthropic-reported and vendor-supplied respectively — not independently
  audited.
- **Scope**: A short (~5 minute) recap-and-announcement post covering the
  MCP 2026-07-28 spec release, the three headline protocol changes, four
  Claude-platform-level features tied to the spec (MCP Apps, enterprise-managed
  auth, connector observability, MCP tunnels), ecosystem scale figures, and six
  partner testimonials. Does NOT cover implementation details for building a
  stateless MCP server, migration steps for existing stateful servers, or the
  full extensions-framework versioning mechanics — for those, the post points
  readers to the spec itself (`modelcontextprotocol.io/specification/2026-07-28`)
  and the SDK docs.

## Extracted Claims

### Claim 1: MCP 2026-07-28 is the fifth spec release of the Model Context Protocol, and its headline change is moving the core protocol to a stateless model while hardening authorization and graduating official extensions
- **Evidence**: Opening framing sentence of the post.
- **Confidence**: settled (verifiable spec-version fact; the release itself is a
  first-party, checkable artifact at the spec URL)
- **Quote**: "The fifth spec release of the Model Context Protocol, MCP
  2026-07-28, is live today. The latest spec moves MCP to a stateless core,
  while hardening authorization and graduating official extensions."
- **Our assessment**: This is the thesis sentence for the whole post and the
  correct one-line summary for the guide: MCP 2026-07-28 = stateless core +
  auth hardening + extension graduation. Practitioners tracking MCP as a
  moving target should treat "fifth spec release" as a versioning cue — the
  protocol has now iterated five times, and this release is a breaking change
  to the transport model (stateful → stateless), not an additive one.

### Claim 2: The stateless core moves MCP from a bidirectional stateful protocol to a request/response model, enabling MCP servers to deploy on serverless and edge infrastructure
- **Evidence**: First-party protocol description, corroborated by four
  independent partner quotes describing the same architectural shift from
  their own deployment perspective (Claim 7).
- **Confidence**: settled (concrete, testable protocol-level claim; corroborated
  by multiple named engineering leaders describing their own migration)
- **Quote**: "MCP moves from a bidirectional stateful protocol to a
  request/response model. Servers can now deploy on serverless and edge
  infrastructure."
- **Our assessment**: This is the single most consequential change in the
  release for server operators. Under the prior stateful/bidirectional model,
  an MCP server had to maintain a long-lived session/connection per client —
  which rules out (or complicates) serverless and edge deployment, where
  compute is spun up per-request and does not persist connection state between
  invocations. A stateless request/response model removes that constraint:
  an MCP server becomes "a first-class HTTP workload" (Netlify's phrasing,
  Claim 7) that can scale the same way any other stateless HTTP API scales.
  This directly extends `blog-anthropic-mcp-production-agents.md` Claim 5
  ("build remote servers, not local stdio servers, for production") — this
  post narrows *what kind* of remote server is now recommended: a stateless
  HTTP one, deployable on serverless/edge infra rather than a
  long-lived-connection remote server.

### Claim 3: MCP Apps and a new Tasks framework now ship under a versioned extensions framework, giving developers a formal path to add capabilities like interactive UIs and long-running work without changing the core protocol
- **Evidence**: First-party protocol description of the extensions mechanism.
- **Confidence**: emerging (a newly-formalized mechanism; "Tasks" is a
  previously undocumented capability in our corpus, and "versioned extensions
  framework" implies a maturation step whose long-term stability is unproven)
- **Quote**: "MCP Apps and Tasks now ship under a versioned extensions
  framework, giving developers a formal path to add capabilities like
  interactive UIs and long-running work without changing the core protocol."
- **Our assessment**: This is a meaningful maturation from what
  `blog-anthropic-mcp-production-agents.md` documented in April 2026, where
  MCP Apps was described as "the first official protocol extension" (singular,
  standalone). By July, MCP Apps has been joined by a second extension
  (Tasks, for long-running work) and both now live under a formal versioning
  scheme. The practical implication for server authors: protocol capabilities
  can now evolve independently of the core spec's release cadence, via
  extension version bumps, rather than requiring a full spec revision. "Tasks"
  itself — a framework for long-running work — is new to our corpus; no prior
  source documents how MCP represents or tracks long-running (non-request/response)
  operations, which is a notable gap given the core protocol is now explicitly
  request/response (Claim 2). Tasks appears to be the mechanism for handling
  work that doesn't fit a single synchronous request/response cycle under the
  new stateless core.

### Claim 4: Authorization now aligns with production OAuth 2.0 and OIDC deployments, letting MCP servers connect to enterprise identity systems like Entra or Okta without workarounds
- **Evidence**: First-party protocol description of the auth-hardening change.
- **Confidence**: settled (concrete alignment claim against well-known external
  standards — OAuth 2.0, OIDC — and named identity providers)
- **Quote**: "Authorization now aligns with production OAuth 2.0 and OIDC
  deployments, so MCP servers connect to enterprise identity systems like
  Entra or Okta without workarounds."
- **Our assessment**: This is a protocol-level claim distinct from — and
  broader than — the enterprise-managed auth *feature* documented in
  `blog-anthropic-enterprise-managed-auth.md` (June 18, 2026), which covers
  Anthropic's specific admin-provisioning product built on the
  Enterprise-Managed Authorization MCP extension. This claim says the core
  MCP auth model itself now aligns with standard OAuth 2.0/OIDC flows,
  independent of any one vendor's provisioning UI. "Without workarounds" is a
  pointed phrase — it implies that prior MCP spec versions required
  non-standard adaptations to fit into existing enterprise IdP deployments
  (Entra, Okta), and this release removes that friction at the protocol level.
  This also complements the CIMD (Client ID Metadata Documents) mechanism
  documented in `blog-anthropic-mcp-production-agents.md` Claim 9 — CIMD
  handles dynamic client registration for cloud-hosted agents; this broader
  OAuth 2.0/OIDC alignment is the surrounding protocol-level compatibility
  claim that makes CIMD-based auth interoperate cleanly with enterprise IdPs.

### Claim 5: MCP has surpassed 400M monthly SDK downloads, a 4x increase in 2026, and Claude's connector directory now lists over 950 MCP servers used by millions of people every day
- **Evidence**: First-party Anthropic-reported ecosystem scale statistics.
- **Confidence**: emerging (first-party, unaudited figures; no methodology
  given for how "monthly SDK downloads" or "used by millions… every day" are
  measured)
- **Quote**: "MCP recently surpassed 400M monthly SDK downloads, a 4x increase
  this year."
- **Quote (directory size)**: "Claude now lists over 950 MCP servers in the
  connectors directory, used by millions of people every day."
- **Our assessment**: These figures continue a growth trajectory already in
  our corpus: `blog-anthropic-mcp-production-agents.md` Claim 4 reported 300M
  monthly downloads in April 2026, up from 100M at the start of the year — so
  "4x increase this year" (100M → 400M) is consistent with that April data
  point (100M → 300M by April → 400M by July). The directory-size figure is
  more striking: `blog-anthropic-connector-observability.md` Claim 5 reported
  "over 300 third-party connectors" in the directory as of June 8, 2026; this
  post reports "over 950" seven weeks later, more than tripling in under two
  months. That is a very steep jump for a directory count and is worth
  treating with caution — it may reflect a broader denominator (all MCP
  servers vs. only third-party ones), a batch onboarding event, or simply
  rapid real growth; the post does not clarify. Not a contradiction (both are
  point-in-time counts from the same Anthropic directory, at different dates),
  but the magnitude of the jump should be flagged rather than repeated
  uncritically as a smooth trend line.

### Claim 6: MCP tunnels (research preview) connect Claude to MCP servers inside a private network without exposing them to the public internet
- **Evidence**: First-party feature description, explicitly labeled a research
  preview (earliest-stage availability tier).
- **Confidence**: anecdotal (research-preview stage; no customers or usage
  data cited, no technical detail on the tunneling mechanism)
- **Quote**: "MCP tunnels (research preview) connect Claude to MCP servers
  inside a private network without exposing them to the public internet."
- **Our assessment**: This is new to our corpus — no prior source documents a
  mechanism for reaching private-network MCP servers from Claude without
  public exposure. It's notable in tension with Claim 2 (stateless core
  enabling serverless/edge deployment): tunnels address the opposite
  deployment shape — MCP servers that deliberately stay off the public
  internet (internal tooling, on-prem systems, VPC-only services) but still
  need to be reachable by Claude. Together, Claims 2 and 6 suggest MCP 2026-07-28
  is trying to serve both ends of the deployment spectrum: public
  serverless/edge servers (stateless core) and private network-isolated
  servers (tunnels). Research-preview status means this is not yet
  production-ready; practitioners should not build critical infrastructure on
  it without expecting API/behavior changes.

### Claim 7: Four named partner engineering leaders (Netlify, PostHog, Xero, Zoom) independently describe the same benefit from the stateless core: simpler deployment and scaling on standard HTTP infrastructure, without session-management overhead
- **Evidence**: Four separate, attributed customer quotes converging on the
  same architectural benefit.
- **Confidence**: emerging (vendor-supplied testimonials — genuine named
  individuals and companies, but selected/curated by Anthropic for the
  announcement, not independently sourced)
- **Quote (Netlify — Sean Roberts, VP of Applied AI)**: "The stateless core in
  the 2026-07-28 spec makes MCP a first-class HTTP workload with no session
  management."
- **Quote (PostHog — Paul D'Ambra, Product Engineer)**: "Moving MCP to a
  stateless protocol makes it easier to scale our own service."
- **Quote (Xero — Andrew Goodman, VP of AI)**: "The stateless core in the open
  MCP 2026-07-28 spec reduces the complexity we manage."
- **Quote (Zoom — Ross Mayfield, Head of Product for AI Platform)**: "The new
  MCP spec makes it far easier to deploy and scale MCP servers on standard
  HTTP infrastructure."
- **Our assessment**: Four independent companies describing the identical
  benefit (less session-management complexity, easier scaling on standard
  HTTP infra) is stronger corroboration than a single vendor claim, even
  though all four quotes were curated by Anthropic for the launch post. This
  is real-world validation — from companies operating production MCP
  servers today — that the stateless-core architectural claim (Claim 2)
  translates into an actual operational benefit, not just a theoretical one.
  For the guide, this is citable evidence that migrating an existing stateful
  MCP server to the 2026-07-28 stateless model is a concrete infrastructure
  simplification, not just a spec-compliance exercise.

### Claim 8: MCP Apps let servers render interactive UI directly in the conversation, and Figma reports more builders using its MCP server to bring generated outputs into Figma's canvas for further iteration
- **Evidence**: First-party feature description plus a named partner quote
  describing actual usage.
- **Confidence**: emerging (feature description is settled/verifiable at the
  spec level per Claim 3's extensions framework; the Figma usage claim is a
  vendor-supplied, unquantified anecdote — "more builders," no numbers)
- **Quote (feature)**: "MCP Apps let servers render interactive UI directly in
  the conversation."
- **Quote (Figma — Josh Clemm, VP of Engineering)**: "More builders are using
  our MCP server to bring generated outputs into Figma's canvas, where they
  can explore, riff and refine them."
- **Our assessment**: This corroborates `blog-anthropic-mcp-production-agents.md`
  Claim 8, which quoted the April 2026 post describing MCP Apps as letting "a
  tool return an interactive interface, such as a chart, form, or dashboard."
  The Figma quote is the first concrete named-customer usage example of MCP
  Apps in our corpus — generated design outputs rendered directly into
  Figma's canvas via the MCP server, rather than described only in text. This
  is useful as a citable real-world example of the "interactive interface"
  pattern for Ch02/Ch03 discussions of MCP Apps, beyond the abstract
  chart/form/dashboard description in the April post.

### Claim 9: Intuit frames MCP itself, not just this release, as "the industry standard for connecting AI agents to tools and data," and describes supporting agentic experiences at the scale of 100 million consumers and businesses
- **Evidence**: Named partner quote (Chief Architect and SVP of Engineering).
- **Confidence**: anecdotal (single-company characterization of an entire
  protocol's market position; not an independently verified market-share
  claim)
- **Quote**: "MCP is the industry standard for connecting AI agents to tools
  and data."
- **Our assessment**: This is a strong claim from a single enterprise partner,
  not a neutral market analysis — treat as a testimonial endorsement, not as
  independently verified fact. It's consistent with the ecosystem-scale
  figures in Claim 5 (400M downloads, 950+ directory servers) but doesn't add
  new quantitative evidence on its own. Useful primarily as a citable
  "industry sentiment" data point for the guide's framing of MCP's adoption
  trajectory, alongside — not instead of — the harder download/directory
  numbers.

### Claim 10: The observability dashboard for connector developers (previously announced) and enterprise-managed auth (previously announced) are recapped in this post as part of the same "Claude platform features" set tied to the MCP 2026-07-28 release
- **Evidence**: The post lists "Observability dashboard" and
  "Enterprise-managed auth" among its Claude-platform-level feature bullets,
  alongside MCP Apps and MCP tunnels.
- **Confidence**: settled (these are recaps of features already documented in
  our corpus with full first-party detail — see cross-references below — not
  new claims requiring independent verification here)
- **Quote (observability)**: "Observability for developers building connectors
  gives published connectors in our directory a dashboard showing how they
  perform across Claude product surfaces."
- **Our assessment**: No new information here beyond what
  `blog-anthropic-connector-observability.md` and
  `blog-anthropic-enterprise-managed-auth.md` already document in depth — this
  post's contribution is framing both as part of the coherent MCP 2026-07-28
  release story, alongside the genuinely new items (stateless core, MCP
  tunnels, Tasks framework). Treat this post as the summary/index entry
  pointing to those two more detailed notes, not as a primary source for
  those two features' mechanics.

## Concrete Artifacts

### Three Headline Protocol Changes

```
# MCP 2026-07-28 — three major changes
# Source: "Bringing MCP 2026-07-28 to Claude," Anthropic, July 28, 2026

1. STATELESS CORE
   "MCP moves from a bidirectional stateful protocol to a request/response
   model. Servers can now deploy on serverless and edge infrastructure."

2. STANDARDIZED EXTENSIONS
   "MCP Apps and Tasks now ship under a versioned extensions framework,
   giving developers a formal path to add capabilities like interactive UIs
   and long-running work without changing the core protocol."

3. AUTH HARDENING
   "Authorization now aligns with production OAuth 2.0 and OIDC deployments,
   so MCP servers connect to enterprise identity systems like Entra or Okta
   without workarounds."
```

### Claude Platform Features Tied to This Release

```
# Source: "Bringing MCP 2026-07-28 to Claude," Anthropic, July 28, 2026

MCP APPS:
  "MCP Apps let servers render interactive UI directly in the conversation."

ENTERPRISE-MANAGED AUTH: (recap — see blog-anthropic-enterprise-managed-auth.md)
  Admins provision connectors org-wide via identity provider; users inherit
  access.

OBSERVABILITY DASHBOARD: (recap — see blog-anthropic-connector-observability.md)
  "Observability for developers building connectors gives published
  connectors in our directory a dashboard showing how they perform across
  Claude product surfaces."

MCP TUNNELS (research preview):
  "MCP tunnels (research preview) connect Claude to MCP servers inside a
  private network without exposing them to the public internet."
```

### Ecosystem Scale Figures

```
# Source: "Bringing MCP 2026-07-28 to Claude," Anthropic, July 28, 2026

SDK DOWNLOADS: "MCP recently surpassed 400M monthly SDK downloads, a 4x
                increase this year."
DIRECTORY SIZE: "Claude now lists over 950 MCP servers in the connectors
                 directory, used by millions of people every day."

# Growth trajectory across corpus (same underlying Anthropic metrics, different dates):
#   SDK downloads/month:      100M (start of 2026) -> 300M (Apr 2026) -> 400M (Jul 2026)
#   Directory server count:   300+ third-party connectors (Jun 8, 2026) -> 950+ (Jul 28, 2026)
```

### Partner Testimonials (verbatim, with name and title as given)

```
# Source: "Bringing MCP 2026-07-28 to Claude," Anthropic, July 28, 2026

Figma — Josh Clemm, VP of Engineering:
  "More builders are using our MCP server to bring generated outputs into
  Figma's canvas, where they can explore, riff and refine them."

Intuit — Chris Kasten, Chief Architect and SVP of Engineering:
  "MCP is the industry standard for connecting AI agents to tools and data."

Netlify — Sean Roberts, VP of Applied AI:
  "The stateless core in the 2026-07-28 spec makes MCP a first-class HTTP
  workload with no session management."

PostHog — Paul D'Ambra, Product Engineer:
  "Moving MCP to a stateless protocol makes it easier to scale our own
  service."

Xero — Andrew Goodman, VP of AI:
  "The stateless core in the open MCP 2026-07-28 spec reduces the complexity
  we manage."

Zoom — Ross Mayfield, Head of Product for AI Platform:
  "The new MCP spec makes it far easier to deploy and scale MCP servers on
  standard HTTP infrastructure."
```

### Getting Started Resources

```
# Source: "Bringing MCP 2026-07-28 to Claude," Anthropic, July 28, 2026

Specification: modelcontextprotocol.io/specification/2026-07-28
SDKs:          modelcontextprotocol.io/docs
Connectors directory: claude.ai/directory/connectors
Submission info:      claude.com/docs/connectors/building/submission
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 4 (300M monthly SDK
    downloads, April 2026, up from 100M at start of year): this post's 400M
    figure (July 2026, "4x increase this year") is the next data point in the
    same growth series and is internally consistent with it.
  - `blog-anthropic-mcp-production-agents.md` Claim 8 (MCP Apps as "the first
    official protocol extension," letting a tool "return an interactive
    interface, such as a chart, form, or dashboard"): this post's description
    ("MCP Apps let servers render interactive UI directly in the
    conversation") and the new Figma usage example (Claim 8 here) corroborate
    and add a concrete customer example to the April claim.
  - `blog-anthropic-connector-observability.md` Claim 5 ("over 300 third-party
    connectors… used by millions of people every day," June 8, 2026): this
    post's "millions of people every day" phrasing for the 950+-server
    directory is nearly identical wording, confirming continuity of the same
    usage-scale claim, though the server count jumped substantially (see
    Claim 5 assessment above).
  - `blog-anthropic-enterprise-managed-auth.md` and
    `blog-anthropic-connector-observability.md`: both are recapped as part of
    the MCP 2026-07-28 platform feature set (Claim 10) — this post treats
    them as already-shipped components of the same release story rather than
    introducing new detail about them.

- **Extends**:
  - `blog-anthropic-mcp-production-agents.md` Claim 5 ("build remote servers
    so agents can use your system wherever they run" — the April 2026
    recommendation to move from local stdio to remote MCP servers for
    production): this post narrows that recommendation further — the
    recommended remote-server architecture is now specifically a *stateless*
    HTTP server (Claim 2), which is what makes serverless/edge deployment
    possible. "Remote" (April) → "remote and stateless" (July) is a
    meaningful architectural refinement, not a contradiction.
  - `blog-anthropic-mcp-production-agents.md` Claim 8 (MCP Apps as the "first"
    official extension) and Claim 9 (CIMD as "the latest MCP spec" OAuth
    mechanism): this post shows both have matured — MCP Apps is now one of
    two extensions (joined by Tasks) under a formal versioned extensions
    framework (Claim 3), and the auth story has broadened from a single OAuth
    mechanism (CIMD) to a general claim of OAuth 2.0/OIDC production alignment
    (Claim 4).

- **Contradicts**: None identified. The stateless-core transport change
  (Claim 2) is a breaking protocol change relative to the "bidirectional
  stateful protocol" model implied throughout `blog-anthropic-mcp-production-agents.md`,
  but that April post never claimed the stateful model was permanent — it
  described the protocol as it existed at the time. This is a protocol
  evolution documented across two dated sources, not two sources disagreeing
  about the same point in time. No contradiction issue filed. (The one
  genuinely surprising number — the 300+ → 950+ directory server jump in
  seven weeks, Claim 5 — is flagged as worth watching, not filed as a
  contradiction, since both figures are point-in-time snapshots that could
  both be accurate.)

- **Novel**:
  - **Stateless core as a breaking transport-model change**: No prior corpus
    source documents MCP moving away from a stateful/bidirectional transport.
    This is the first source describing MCP explicitly as request/response
    and citing serverless/edge deployment as the unlocked capability.
  - **Tasks framework**: The first corpus mention of "Tasks" as an MCP
    extension for long-running work. No prior source documents how MCP
    represents work that spans multiple request/response cycles.
  - **Versioned extensions framework**: The first corpus source to describe
    MCP extensions (MCP Apps, Tasks) as living under a formal versioning
    scheme independent of core spec releases.
  - **MCP tunnels (research preview)**: The first corpus source describing a
    mechanism for Claude to reach MCP servers on a private network without
    public internet exposure.
  - **Four independent partner testimonials converging on the same stateless-core
    benefit**: The first instance in our corpus of multiple named companies
    (Netlify, PostHog, Xero, Zoom) independently corroborating the same
    architectural claim about an MCP spec change from their own production
    experience.
  - **Named engineering-leader titles for six MCP ecosystem partners**: First
    corpus record of these specific individuals (Josh Clemm/Figma, Chris
    Kasten/Intuit, Sean Roberts/Netlify, Paul D'Ambra/PostHog, Andrew
    Goodman/Xero, Ross Mayfield/Zoom) as named MCP ecosystem voices.

## Guide Impact

- **Chapter 02 (Harness Engineering — MCP server design)**: Update the
  `blog-anthropic-mcp-production-agents.md`-derived guidance ("build remote
  servers, not local stdio") to specify that as of MCP 2026-07-28, "remote"
  now specifically means a *stateless* HTTP server. Add a note that teams
  running pre-2026-07-28 stateful remote MCP servers face a migration
  decision, not just an optional upgrade — the four partner testimonials
  (Claim 7) are citable evidence that migrating reduces operational
  complexity (no session management) and unlocks serverless/edge deployment.

- **Chapter 02 (Harness Engineering — deployment patterns)**: Add MCP tunnels
  (research preview, Claim 6) as an emerging pattern for reaching
  private-network/on-prem MCP servers from Claude without public exposure.
  Flag explicitly as research-preview / not production-ready given no
  customer validation or technical detail is yet available.

- **Chapter 02 (Harness Engineering — auth)**: Broaden the existing auth
  coverage (CIMD, enterprise-managed auth) with the protocol-level claim that
  MCP 2026-07-28 authorization aligns with standard OAuth 2.0/OIDC production
  deployments generally (Claim 4), not just via Anthropic's specific
  enterprise-managed-auth product. This is the umbrella claim under which
  CIMD and enterprise-managed auth both sit.

- **Chapter 04 (Context Engineering / Tool Integration)**: Note the Tasks
  framework (Claim 3) as an open question for future mining — no source in
  the corpus yet documents how Tasks represents long-running work under a
  request/response core, and this gap should be flagged for a future source
  submission once Anthropic or a third party documents Tasks in more depth.

- **Ecosystem-tracking / stats appendix (if one exists)**: Update MCP
  ecosystem figures to 400M monthly SDK downloads and 950+ directory servers
  (July 2026), citing this post, while flagging the directory-server jump
  (300+ in June to 950+ in July) as a figure to re-verify at the next MCP
  source rather than repeat uncritically.

## Extraction Notes

1. **WebFetch returns AI-summarized content from a JS-rendered SPA**: Like
   prior claude.com/blog extractions in this corpus, this page renders as a
   JavaScript SPA and WebFetch summarizes the rendered content rather than
   returning raw HTML. Three separate targeted fetches were performed
   (general content, partner quotes + stats, remaining feature descriptions +
   getting-started section) to cross-check quote fidelity. All quotes used in
   this note appeared consistently, word-for-word, across the relevant
   fetches.
2. **Short feature-announcement/recap post**: This is a compact (~5 min read)
   announcement rather than a deep technical spec walkthrough. Several items
   (Tasks framework, MCP tunnels, versioned extensions mechanics) are
   mentioned but not explained in depth — the post directs readers to the
   spec itself for details. Claims were exhausted at 10 extractions; deeper
   technical detail on Tasks and the extensions versioning scheme would
   require mining the spec page directly (`modelcontextprotocol.io/specification/2026-07-28`),
   which is out of scope for this note but flagged in Guide Impact as a gap.
3. **Directory-size jump treated as a caution, not a contradiction**: The
   300+ (June 8) → 950+ (July 28) directory server count jump is unusually
   steep for seven weeks. I considered filing a contradiction issue but
   concluded it does not meet the MINER.md §4a threshold — both figures are
   point-in-time counts from the same Anthropic-owned directory at different
   dates, and rapid ecosystem growth (consistent with the 4x SDK download
   growth also reported) is a plausible, if striking, explanation. Flagged in
   Claim 5 and Guide Impact for future re-verification rather than filed as a
   contradiction.
4. **Partner testimonials treated as emerging/anecdotal, not settled**: All
   six partner quotes are vendor-supplied and curated by Anthropic for a
   launch post — genuine named individuals and real companies, but not
   independently sourced or quantified (e.g., "more builders," no numbers).
   Graded emerging/anecdotal accordingly per claim, consistent with how this
   corpus treats similar testimonial content in
   `blog-anthropic-enterprise-managed-auth.md`.
5. **No contradictions filed**: Reviewed against all MCP-related source notes
   in the corpus (`blog-anthropic-mcp-production-agents.md`,
   `blog-anthropic-enterprise-managed-auth.md`,
   `blog-anthropic-connector-observability.md`, `blog-bswen-mcp-token-cost.md`,
   `docs-ghaw-mcps.md`). All differences found are protocol/product evolution
   across dated releases, not disagreements about the same point in time.
