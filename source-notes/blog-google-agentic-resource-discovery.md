---
source_url: https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/
source_type: blog-post
title: "Announcing the Agentic Resource Discovery specification"
author: Junjie Bu (Senior Staff Software Engineer) and Srinivas Krishnan (Distinguished Software Engineer), Google Developers Blog
date_published: 2026-06-17
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: emerging
issue: "#1638"
---

# Announcing the Agentic Resource Discovery specification

> Google announces Agentic Resource Discovery (ARD), an open, v0.9-draft standard
> for publishing (Catalogs), finding (Registries), and cryptographically verifying
> agent-callable capabilities — MCP servers, A2A agents, OpenAPI tools, and other
> catalogs — across organizational domain boundaries, with a commercial
> implementation shipping as Agent Registry inside Google Cloud's Gemini
> Enterprise Agent Platform.

## Source Context

- **Type**: blog-post (official Google Developers Blog, developers.googleblog.com,
  published June 17, 2026). Auto-discovered via the trusted `google-developers` feed.
  Followed two linked pages for additional technical grounding: the rendered
  specification site (agenticresourcediscovery.org) and the spec's GitHub
  repository (github.com/ards-project/ard-spec).
- **Author credibility**: Junjie Bu (Senior Staff Software Engineer) and Srinivas
  Krishnan (Distinguished Software Engineer) are named Google staff writing on
  Google's own developer blog, announcing a Google-backed open specification.
  This is first-party vendor content for a brand-new, jointly-governed standard —
  the spec explicitly credits the "AI Catalog Working Group under the Linux
  Foundation" as a foundational input, so it is not solely a Google-internal
  proposal, but Google is the party publishing and productizing it first (via
  Agent Registry). Treat architectural claims as an accurate description of what
  the spec proposes; treat "solves cross-organization discovery" framing as
  vendor-optimistic until independent adopters and interoperability data exist.
- **Scope**: Covers the motivating problem (fragmented, siloed per-platform tool
  registries), the two-layer Catalog + Registry architecture, the discovery flow
  (registry search vs. direct fetch), the cryptographic trust/verification layer,
  supported capability types (MCP servers, A2A agents, OpenAPI tools, nested
  catalogs), and Google's own commercial implementation (Agent Registry in Gemini
  Enterprise Agent Platform). Does NOT cover: the detailed JSON schema of
  `ai-catalog.json` or the trust-manifest wire format (these live in the spec's
  `spec/schemas/` directory, not reproduced in the blog post or its landing page),
  pricing for Agent Registry, or any independent third-party implementation
  reports (none exist yet — the GitHub repo is at v0.9-draft with 356 stars / 45
  forks / 26 open issues at time of extraction).

## Extracted Claims

### Claim 1: ARD frames agent tool/capability discovery across organizations as three unanswered questions — where a capability lives, which to use, and how to verify it's safe
- **Evidence**: Stated as the article's problem framing, opening thesis for why a new
  standard is needed.
- **Confidence**: settled (the three-question framing is a clear, internally
  consistent restatement of the discovery problem; it is a rhetorical framing
  device rather than an empirical claim)
- **Quote**: "Where does the right capability live? Which capability should I
  actually use? And how do I verify it's safe to connect to?"
- **Our assessment**: This is a clean three-part decomposition of the discovery
  problem (locate → select → verify) that maps directly onto the two mechanisms
  ARD proposes: Catalogs/Registries answer "locate," and the cryptographic trust
  layer answers "verify." "Select" (which capability to use among matches) is
  the least developed part of the announcement — the post does not describe a
  ranking or selection mechanism beyond "plain-language intent" query matching.

### Claim 2: Existing tool/agent registries today are fragmented and siloed within individual platforms, which is the specific gap ARD is positioned to close
- **Evidence**: Direct problem statement in the article, contrasting current state
  with the proposed cross-organization standard.
- **Confidence**: emerging (accurate high-level characterization of a real
  ecosystem fragmentation problem — e.g., MCP marketplaces, A2A agent cards, and
  vendor-specific tool directories each operate independently today — but no
  survey data or count of existing siloed registries is cited)
- **Quote**: "While many platforms already feature custom registries to manage
  these capabilities, they remain fragmented and siloed within specific
  ecosystems."
- **Our assessment**: This is the direct motivation for a cross-org standard
  rather than a per-platform one. It implicitly acknowledges that ARD is not
  filling an empty niche — platform-specific registries already exist (MCP
  registries, agent marketplaces) — but that none of them interoperate across
  organizational boundaries. Whether ARD actually displaces or supplements those
  existing siloed registries is not addressed in the post.

### Claim 3: Catalogs are self-published capability descriptions hosted under an organization's own domain, and domain ownership itself is the cryptographic trust root
- **Evidence**: Direct architectural definition of the "Catalog" half of the
  two-layer model.
- **Confidence**: settled (clearly and specifically stated architectural design
  choice, unambiguous in the source)
- **Quote**: "Catalogs: To make resources discoverable, an organization publishes
  a catalog describing its available capabilities. Because these catalogs are
  hosted directly under the organization's own domain, ownership of that domain
  serves as the cryptographic foundation for identity and trust."
- **Our assessment**: This is the single most consequential design decision in
  the spec: instead of a centralized issuing authority (a certificate authority
  for agent capabilities, or a single blessed marketplace), trust derives from
  the same primitive the web already relies on — domain ownership (implicitly,
  something like a `.well-known/ai-catalog.json` path, matching the pattern
  used by `robots.txt` and OAuth's `.well-known` discovery documents). This
  makes ARD adoption incremental (any org that owns a domain can publish a
  catalog with no registration step) at the cost of inheriting all of the
  web's existing domain-security weaknesses (typosquatting, domain takeover,
  expired-domain reuse) as attack surface for capability discovery.

### Claim 4: Registries are third-party federated search engines that crawl and index published Catalogs — not a single central directory
- **Evidence**: Direct architectural definition of the "Registry" half of the
  two-layer model.
- **Confidence**: settled (clearly stated architectural design choice)
- **Quote**: "Registries act as search engines for the agentic web. They crawl
  published catalogs, index their contents, and make them searchable."
- **Our assessment**: The "search engines for the agentic web" framing is a
  deliberate analogy to how the web itself decoupled publishing (any domain can
  host a page) from discovery (search engines crawl and rank independently).
  Applied to agent capabilities, this means no single vendor needs to run "the"
  registry — multiple competing or specialized registries can each crawl the
  same universe of Catalogs, similar to how multiple search engines index the
  same web. This is corroborated by the spec site's explicit statement (see
  Extraction Notes) that ARD is "not... a central catalog" and instead enables
  "distributed, community-specific indexing services with independent trust
  policies."

### Claim 5: Agents can discover a capability via a registry's plain-language intent search, or bypass search entirely and fetch a known partner's catalog directly
- **Evidence**: Direct description of the two supported discovery paths.
- **Confidence**: settled (clearly stated as the two supported flows)
- **Quote**: "When a client agent needs a capability, it can either query an ARD
  registry using a plain-language intent (which can actively crawl and index
  these catalogs), or it can completely bypass search and directly fetch a
  catalog from a known partner's domain."
- **Our assessment**: The direct-fetch path is important for pre-established
  B2B/partner relationships — an enterprise that already knows it wants to
  connect to a specific named partner's capabilities does not need to route
  through a third-party registry at all, avoiding both the latency and the
  trust dependency on a registry operator. The registry-search path is for the
  open-ended "what's available for this task" case. This two-path design
  mirrors the direct-API-call vs. discovery-service split already documented
  for MCP server connections generally.

### Claim 6: A publisher's cryptographic identity is verified before a client connects, regardless of whether the capability was found via registry search or direct fetch
- **Evidence**: Direct description of the trust/verification mechanism, described
  as intended "for production environments."
- **Confidence**: emerging (the mechanism is stated architecturally — "verifiable
  trust metadata" attached by publishers — but the blog post and its linked
  landing page do not describe the specific cryptographic scheme, key
  distribution, or revocation model; those details are said to live in the
  spec's schema files, not examined directly in this extraction)
- **Quote**: "For production environments, the discovery layer allows publishers
  to attach verifiable trust metadata. Whether found via search or direct fetch,
  this enables the client agent or registry to actively confirm the publisher's
  true cryptographic identity before connecting to the endpoint."
- **Our assessment**: This is ARD's answer to the "how do I verify it's safe to
  connect to" question from Claim 1, and it is the direct architectural
  countermeasure to the impersonation-style attack documented in
  `blog-anthropic-zero-trust-ai-agents.md` Claim 6 (the first documented
  in-the-wild malicious MCP server impersonated a legitimate email service).
  Under ARD, a client verifying "true cryptographic identity" tied to domain
  ownership before connecting would, in principle, prevent an attacker-hosted
  catalog from being mistaken for a trusted partner's — but only as strong as
  the underlying domain security (see Claim 3's assessment) and only if clients
  actually perform the verification step rather than treating it as optional.

### Claim 7: Catalog entries can describe heterogeneous, cross-protocol capability types — MCP servers, A2A agents, OpenAPI tools, or other nested catalogs — under one discovery format
- **Evidence**: Direct enumeration of supported capability types in a catalog
  entry.
- **Confidence**: settled (clearly enumerated in the source)
- **Quote**: "The catalog describes the provider's available capabilities, which
  can include things like MCP servers, A2A agents, OpenAPI tools, or even other
  nested catalogs."
- **Our assessment**: ARD is explicitly positioned as a discovery layer that sits
  above existing protocols rather than replacing any of them — an agent still
  speaks MCP to an MCP server or A2A to an A2A agent once it has located and
  verified the endpoint; ARD only solves "how did the agent learn this endpoint
  exists and that it's trustworthy." The "nested catalogs" option means a large
  organization could publish one root catalog that references department- or
  product-line-specific sub-catalogs, giving the model a tree structure similar
  to DNS delegation.

### Claim 8: Once a capability is selected, the client agent dynamically loads it and invokes it using its own native protocol — ARD does not define a new calling convention
- **Evidence**: Direct description of the runtime connection step, the final
  stage of the discovery-to-use flow.
- **Confidence**: settled (clearly stated in the source)
- **Quote**: "The client agent dynamically loads the selected capability,
  interacts with it using its native protocol or API, and returns the result to
  the user."
- **Our assessment**: This confirms ARD's scope boundary: it governs discovery
  and trust verification only, handing off to whatever protocol the discovered
  resource actually speaks (MCP, A2A, OpenAPI) for the actual invocation. This
  is corroborated directly by the spec site's own negative scoping statement
  (see Extraction Notes): ARD explicitly disclaims being "an execution runtime...
  or replacement for MCP, Skills, or API runtimes."

### Claim 9: Google is productizing ARD as "Agent Registry" inside its Gemini Enterprise Agent Platform, framed as the trust/governance layer for enterprises adopting the open spec at scale
- **Evidence**: Direct statement of Google's own commercial implementation of the
  open specification it is simultaneously announcing.
- **Confidence**: emerging (first-party claim about Google's own commercial
  offering; "trust, govern, and operationalize... at scale" is vendor framing
  with no usage or adoption data provided in the post)
- **Quote**: "Agent Registry ensures enterprises can trust, govern, and
  operationalize that promise at scale."
- **Our assessment**: This is a familiar open-standard-plus-commercial-product
  pattern (comparable to Kubernetes/GKE or OpenTelemetry/Cloud Trace): Google
  publishes an open, Linux-Foundation-linked spec while simultaneously shipping
  the first hosted implementation of the registry half of the architecture.
  Organizations adopting ARD's Catalog format are not required to use Google's
  Agent Registry — any conforming registry can crawl their catalog — but Google
  is positioned as the reference commercial operator at launch.

### Claim 10: The spec is Apache 2.0 licensed and explicitly built on a pre-existing, Linux-Foundation-governed "AI Catalog" data model, not authored from scratch by Google alone
- **Evidence**: Direct licensing and provenance statement, naming the
  contributing working group.
- **Confidence**: settled (verifiable licensing and attribution statement)
- **Quote**: "The Agentic Resource Discovery specification is licensed under
  Apache 2.0 and is built upon the foundational AI Catalog data model. We are
  grateful to the AI Catalog Working Group under the Linux Foundation"
- **Our assessment**: This attribution matters for assessing how "open" the
  standard really is at launch: it is not a unilateral Google format, but
  extends an existing Linux Foundation working group's data model. This gives
  ARD more of a multi-stakeholder governance starting point than a typical
  single-vendor "open-source but vendor-controlled" spec, though the GitHub
  repository's stated status (v0.9-draft, maintainer-based governance for
  normative changes — see Extraction Notes) shows the standard is still early
  and not yet stabilized.

## Concrete Artifacts

```
Agentic Resource Discovery (ARD) — Two-Layer Architecture
Source: developers.googleblog.com, "Announcing the Agentic Resource Discovery
specification," Google (Junjie Bu, Srinivas Krishnan), June 17, 2026

LAYER 1 — CATALOGS (publishing)
  - Organization publishes an `ai-catalog.json`-style catalog under its own domain
  - Domain ownership = cryptographic trust root (no central issuing authority)
  - Entries can describe: MCP servers | A2A agents | OpenAPI tools | nested catalogs

LAYER 2 — REGISTRIES (discovery)
  - Third-party federated "search engines for the agentic web"
  - Crawl published catalogs, index contents, make them searchable
  - Multiple independent/competing registries can coexist (no single directory)

DISCOVERY FLOW
  1. Client agent needs a capability
  2a. EITHER: query a Registry with a plain-language intent
  2b. OR: bypass search, direct-fetch a known partner's catalog from their domain
  3. Verify: publisher's cryptographic identity confirmed via attached trust
     metadata, before connecting (production environments)
  4. Client agent dynamically loads the selected capability
  5. Client agent invokes it using ITS OWN native protocol (MCP/A2A/OpenAPI) —
     ARD does not define a new invocation protocol

COMMERCIAL IMPLEMENTATION (Google)
  - Agent Registry, inside Gemini Enterprise Agent Platform
  - Positioned as: hosted discovery + governance + secure resource management

LICENSING / GOVERNANCE
  - Apache 2.0
  - Built on the AI Catalog data model (Linux Foundation AI Catalog Working Group)
  - Repo (github.com/ards-project/ard-spec) status at extraction: v0.9 (Draft)
```

```
ARD explicit non-goals (from agenticresourcediscovery.org, "About" section)
Source: agenticresourcediscovery.org (linked from the announcement)

"An agentic resource is any external capability an AI client can call on to do
a task — an agent, MCP server, Skill, Canvas, Plugin, API, or workflow —
anything that can be represented as an AI Catalog entry."

ARD is explicitly framed as NOT:
  - an execution runtime
  - a single central catalog
  - a replacement for MCP, Skills, or API runtimes
It is scoped as a discovery layer only, enabling distributed,
community-specific indexing services with independent trust policies.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 2 (the M×N integration
    problem: "each agent–service pair becomes a bespoke integration with its
    own auth handling, tool descriptions, and edge cases"): ARD's framing of
    today's registries as "fragmented and siloed within specific ecosystems"
    (Claim 2 here) is the discovery-layer analog of the same M×N pattern — just
    as MCP standardizes the agent-to-single-service connection, ARD is pitched
    as standardizing agent-to-many-organizations discovery, one layer up the
    stack.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 6 (tool poisoning / the
    first documented in-the-wild malicious MCP server impersonated a legitimate
    email service): ARD's cryptographic publisher-verification step (Claim 6
    here) is a direct architectural countermeasure to exactly this class of
    impersonation attack, applied at discovery time rather than after a
    connection is already configured.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 19 ("identity-based
    isolation is the primary control for resource boundaries... every
    workload carries its own cryptographic identity"): ARD's domain-ownership-
    as-identity model (Claim 3 here) is a parallel application of the same
    cryptographic-identity-over-network-trust principle, but applied to
    organizations/publishers in a discovery context rather than to individual
    workloads in a runtime context.

- **Extends**:
  - `blog-anthropic-mcp-production-agents.md`: That note documents how to
    design and consume an individual MCP server once an agent already knows
    its address (remote-server design, intent-grouped tools, tool search for
    context efficiency). This source covers the layer that precedes all of
    that — how an agent finds and trust-verifies the server's address in the
    first place, across organizational boundaries the MCP post does not
    address. Read together: ARD answers "how do I find and trust this MCP
    server," and the MCP production-agents post answers "what do I do once
    I'm connected to it."

- **Contradicts**: No material contradictions identified with existing corpus
  source notes. ARD's domain-ownership trust model and the zero-trust eBook's
  "hardware-bound credentials, expiring tokens, cryptographic identity" test
  (`blog-anthropic-zero-trust-ai-agents.md` Claim 4) are complementary rather
  than conflicting — ARD addresses discovery-time publisher trust, the eBook
  addresses runtime credential/session trust; nothing in this source disputes
  the eBook's guidance or vice versa.

- **Novel**:
  - **Catalog + Registry federation as a named cross-organization discovery
    architecture**: no prior corpus source documents a proposal for discovering
    agent capabilities across organizational domain boundaries; prior notes on
    MCP and A2A cover connecting to a system whose address is already known.
  - **Domain ownership as the cryptographic trust root for agent capability
    discovery**: distinct from the certificate-authority and workload-identity
    patterns documented in `blog-anthropic-workload-identity-federation.md` and
    `blog-anthropic-zero-trust-ai-agents.md` — those govern identity between a
    workload and a known platform; ARD governs identity between a discovering
    agent and a previously-unknown publisher, using the web's existing
    domain-trust primitive instead of a new PKI.
  - **Nested catalogs and cross-protocol capability enumeration** (MCP servers,
    A2A agents, OpenAPI tools, and other catalogs all describable in one
    format) is new to the corpus as an explicit design goal.
  - **Linux Foundation AI Catalog Working Group** as a named multi-stakeholder
    governance body for agent discovery standards — first appearance in the
    corpus.

## Guide Impact

- **Chapter 04 (Context Engineering — tool discovery)**: Add ARD's Catalog +
  Registry model as an early-stage (v0.9-draft) proposal for cross-organization
  tool/capability discovery, distinct from within-a-single-agent tool-loading
  optimizations already documented (tool search, `allowed:` filtering — see
  `blog-anthropic-mcp-production-agents.md` Claim 10 and `docs-ghaw-mcps.md`
  Claim 3). Frame it explicitly as "discovery across organizations you haven't
  already configured," not a replacement for those existing within-harness
  context-management techniques.

- **Chapter 02 (Harness Engineering — tool integration)**: Note ARD as a
  specification to watch, not yet to build on for production systems: single
  primary vendor push (Google) plus one industry working group, v0.9-draft
  status, no independent implementations or interoperability reports in this
  source. Recommend re-checking `last_checked` before citing this as settled
  guidance in the guide.

- **Chapter 06 (Security — trust and verification)**: Add domain-ownership-based
  publisher verification (Claim 6) as a concrete, named implementation pattern
  for the "verify provenance before connecting" principle already established
  by `blog-anthropic-zero-trust-ai-agents.md` (Phase 2: "Run/host the MCP server
  yourself... cryptographically sign it yourself"). ARD proposes a federated
  alternative to self-hosting-and-signing: trust a publisher's catalog based on
  their domain's cryptographic identity, verified at discovery time. Flag the
  same weakness this note raises: this trust model inherits all of the web's
  existing domain-security attack surface (typosquatting, domain takeover,
  expired-domain reuse) as a discovery-time risk.

## Extraction Notes

- **WebFetch returns AI-summarized content, not raw HTML**: developers.googleblog.com
  is rendered through an AI-summarization layer in this environment. Six
  targeted WebFetch calls were made against the announcement URL, each asking
  for a specific short passage verbatim (the three-question framing, the
  Catalog definition, the Registry definition, the discovery-flow sentences,
  the protocol/license sentences, and the runtime/commercial-implementation
  sentences) to maximize quote fidelity, following the same methodology used
  in `blog-anthropic-agent-identity-access-model.md` and
  `blog-anthropic-mcp-production-agents.md`. Quotes above were each returned
  consistently as short, self-contained sentences and are treated as verbatim;
  they should be spot-checked against the source URL before being cited
  directly in the guide.
- **Followed two linked pages**: the rendered specification landing page
  (agenticresourcediscovery.org) and the spec's GitHub repository
  (github.com/ards-project/ard-spec), both linked from the announcement's
  "Get Started" section. Neither page's underlying JSON schema files
  (`spec/schemas/`) were opened directly — the repository README references
  their existence (CDDL, JSON Schema, and OpenAPI formats) but does not
  reproduce them, and this extraction did not fetch the schema files
  themselves. A future source note mining the spec repository directly could
  extract the actual `ai-catalog.json` schema and trust-manifest wire format,
  which are not available from the blog post or landing page alone.
- **Publication date**: the article carries no visible byline date in the
  rendered page content the Prospector's triage comment could confirm ("unknown");
  a targeted WebFetch call against the announcement page returned June 17, 2026
  as the publication date. This is used as `date_published` above but was not
  independently corroborated against a second source (e.g., an archived page
  snapshot or RSS feed timestamp), so treat it as reasonably but not certainly
  accurate.
- **No contradictions filed**: reviewed all existing corpus notes on MCP, A2A,
  agent identity, and zero-trust security (`blog-anthropic-mcp-production-agents.md`,
  `blog-anthropic-zero-trust-ai-agents.md`, `blog-anthropic-agent-identity-access-model.md`,
  `blog-anthropic-workload-identity-federation.md`, `blog-google-adk-kotlin-android-agents.md`).
  No material contradiction found — see Cross-References above.
- **Overall confidence rated "emerging"**: the architectural claims (Catalog/
  Registry split, domain-ownership trust root, discovery flow, capability
  types) are clearly and consistently stated in the source and are individually
  rated "settled" as accurate descriptions of what the spec proposes. The note's
  overall confidence is "emerging" rather than "settled" because the standard
  itself is a v0.9-draft with a single primary commercial backer, no
  independent adopters, no interoperability test results, and no production
  deployment data — this is a proposal announcement, not a validated pattern.
