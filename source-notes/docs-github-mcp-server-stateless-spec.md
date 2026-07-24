---
source_url: https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification
source_type: docs
title: "GitHub MCP Server supports the next MCP specification"
author: GitHub (official changelog)
date_published: 2026-07-23
date_extracted: 2026-07-24
last_checked: 2026-07-24
status: current
confidence_overall: emerging
issue: "#2192"
---

# GitHub MCP Server supports the next MCP specification

> GitHub's July 23, 2026 changelog announcing that the GitHub MCP Server already
> implements the upcoming MCP protocol release (final spec ships July 28, 2026),
> which drops the stateful `initialize`/session handshake in favor of a stateless
> core — documenting three concrete server-side changes (Redis session removal,
> header-based auth instead of payload inspection, and a reworked stdio
> elicitation flow) plus the arrival of an official MCP conformance test suite.

## Source Context

- **Type**: docs (GitHub official product changelog, July 23, 2026; short —
  "2 minute read" — four-section post: opening/what's changing, GitHub MCP
  Server implementation changes, elicitation upgrade, and a closing pointer to
  conformance-suite resources)
- **Author credibility**: GitHub engineering team announcing production
  behavior of the GitHub MCP Server, the first-party MCP server GitHub ships
  for its own platform. Authoritative for what GitHub's server does today and
  which upstream spec changes it tracks ahead of the official release.
  Authoritative-by-reference, not first-party, for the underlying MCP
  specification itself — the protocol-level claims (stateless core, session
  removal, conformance suite) originate with the MCP steering spec (see the
  linked Release Candidate post, cross-referenced below) and this changelog
  reports GitHub's implementation of them ahead of the July 28, 2026 general
  release.
- **Scope**: What changes in the next MCP spec (statelessness, removed
  `initialize`/session handshake, parallel handshakes, elicitation
  multi-round-trip support) and the three specific things GitHub changed in
  its own MCP Server to adopt it early (Redis session removal, no more deep
  packet inspection, reworked stdio elicitation). Does NOT cover: the MCP
  spec's Extensions framework, authorization hardening, or feature lifecycle
  policy (those are in the linked Release Candidate post, not this
  changelog); migration steps for third-party MCP server authors beyond "tier
  1 SDKs already shipped beta support"; or any gh-aw/Copilot-specific
  configuration changes resulting from this spec bump.

## Extracted Claims

### Claim 1: The MCP protocol goes stateless on July 28, 2026, and the GitHub MCP Server already supports the latest spec ahead of that official release

- **Evidence**: Opening sentence of the changelog, stating both the date and
  GitHub's early-adopter position.
- **Confidence**: settled (specific date, first-party statement of GitHub's
  own server behavior)
- **Quote**: "The MCP protocol is going stateless on 28th July 2026, and the
  GitHub MCP Server supports the latest spec ahead of the official release."
- **Our assessment**: This is the load-bearing fact for the whole post: a
  concrete date for a protocol-level architecture change, and a signal that
  practitioners running the GitHub MCP Server are already on the new
  behavior, not waiting for a future upgrade. For Ch02 (Harness Engineering):
  any documentation or configuration guidance for the GitHub MCP Server
  written before July 2026 should be checked against this transition —
  session-based assumptions (e.g., about `initialize` handshakes) may no
  longer hold.

### Claim 2: The new stateless core is specifically framed as a scaling improvement for MCP deployments

- **Evidence**: Direct statement in the "what's changing" section.
- **Confidence**: settled (first-party framing of the design rationale)
- **Quote**: "The new stateless core means MCP deployments are now easy to
  scale."
- **Our assessment**: This is the architectural motivation, not just a
  protocol trivia point: statelessness at the protocol layer removes the
  need for sticky sessions or a shared session store behind a load balancer,
  which is precisely the deployment pattern that stateful `initialize`
  handshakes made awkward. For Ch02: this reframes MCP server deployment
  guidance — horizontal scaling behind a standard load balancer becomes the
  default expectation for remote MCP servers built against the new spec,
  rather than something requiring session-affinity workarounds.

### Claim 3: Sessions and the `initialize` handshake are both removed, letting clients connect faster and complete handshakes in parallel

- **Evidence**: Direct statement describing the specific protocol elements
  eliminated and their effect on connection speed.
- **Confidence**: settled (specific protocol-level claim, first-party)
- **Quote**: "Sessions and `initialize` are both removed, so you can connect
  to servers faster."
- **Quote (parallel handshakes)**: "Clients can also complete the handshake
  in parallel."
- **Our assessment**: Removing the stateful handshake is the specific
  mechanism behind the "easy to scale" claim in Claim 2 — no server-side
  session object to create, store, or route back to on every request. The
  parallel-handshake capability is a secondary client-side benefit: a client
  connecting to multiple MCP servers no longer needs to serialize the
  connection setup for each one. For Ch02: document that MCP client code
  written against the old spec's sequential-`initialize`-then-connect
  pattern can be simplified once servers are on the new spec.

### Claim 4: Remote MCP servers under the new spec will increasingly support features like elicitation via multi-round-trip HTTP requests rather than a persistent session

- **Evidence**: Statement connecting the protocol change to a specific
  capability (elicitation) that benefits from it.
- **Confidence**: emerging (forward-looking claim — "you'll see more" — about
  ecosystem-wide server behavior, not a settled fact about a shipped
  implementation beyond GitHub's own server)
- **Quote**: "You'll see more remote servers supporting features like
  elicitation thanks to multi round-trip requests."
- **Our assessment**: This connects the stateless architecture to a
  practical capability: elicitation (server pausing mid-tool-call to ask the
  user for input) no longer depends on a long-lived session object to
  correlate the follow-up request with the original call — each round trip
  can be a discrete, stateless HTTP exchange. This is the same elicitation
  feature documented as a first-party protocol extension in
  `blog-anthropic-mcp-production-agents.md` Claim 8; this source adds that
  the new stateless transport is what makes elicitation practical for
  *remote* (not just stdio) MCP servers at scale.

### Claim 5: GitHub removed Redis-backed session storage from the GitHub MCP Server, eliminating database reads and writes on `initialize`

- **Evidence**: First of three GitHub MCP Server implementation changes,
  under the "GitHub MCP Server Implementation" heading.
- **Confidence**: settled (specific, concrete first-party implementation
  change)
- **Quote**: "Removed Redis sessions: Database writes on `initialize` are
  gone, and database reads are gone."
- **Our assessment**: This is the single most concrete infrastructure-impact
  claim in the post: GitHub's own MCP Server had a Redis dependency
  specifically to persist session state across the `initialize` handshake,
  and the stateless spec let them delete it. For Ch02 (Harness Engineering):
  this is a directly citable example of the abstract "easy to scale" claim
  (Claim 2) translating into a real infrastructure simplification — one
  fewer stateful dependency (Redis) to provision, scale, and fail over for a
  production MCP server. Practitioners building their own remote MCP servers
  against the new spec should expect to be able to drop similar
  session-store dependencies.

### Claim 6: The new spec lets MCP servers read required values from HTTP headers instead of inspecting the request payload

- **Evidence**: Second of three GitHub MCP Server implementation changes.
- **Confidence**: settled (specific first-party implementation detail)
- **Quote**: "In the new spec we can do that from HTTP headers guaranteed to
  be present. That means no more inspecting the payload."
- **Our assessment**: This is a narrower, more mechanical change than Claims
  2-3, but operationally relevant: server implementations that previously had
  to parse and inspect the request body to extract routing/identity
  information can now rely on values being present in headers instead. For
  server authors this is a simplification (no payload parsing needed before
  routing); for anyone reasoning about MCP server security surface, moving
  required values into headers is also a smaller change to the trust
  boundary than deep-inspecting arbitrary payload content. For Ch02: note as
  a secondary implementation simplification alongside the Redis removal —
  not as significant as Claim 5's infrastructure change, but relevant to
  practitioners implementing their own MCP servers against the new spec.

### Claim 7: The GitHub MCP Server's stdio implementation now handles URL-based elicitation for user login as a separate HTTP request per step, with a Go SDK wrapper maintaining backward compatibility for old and new clients

- **Evidence**: Third of three GitHub MCP Server implementation changes,
  under an "Upgraded elicitation" subsection.
- **Confidence**: settled (specific first-party implementation detail,
  including the backward-compatibility mechanism)
- **Quote**: "Our stdio MCP server uses URL elicitation for easy user login.
  In the new protocol version, each step is a separate HTTP request."
- **Quote (backward compatibility)**: "To make this work with old and new
  clients, the Go SDK provides a wrapper that makes both mechanisms work."
- **Our assessment**: This is the concrete example of Claim 4's abstract
  "elicitation via multi-round-trip requests" applied to GitHub's own stdio
  server: user login via URL elicitation used to depend on a stateful
  session correlating each step; now each step is an independent HTTP
  request. The explicit statement that the Go SDK wraps both the old and new
  mechanism is operationally important — it means GitHub MCP Server clients
  do not need to upgrade in lockstep with the server to keep login working.
  For Ch02: cite this as a concrete worked example of what "elicitation
  under the new spec" looks like in a shipped server, useful alongside the
  more abstract elicitation description in
  `blog-anthropic-mcp-production-agents.md` Claim 8.

### Claim 8: All tier 1 MCP SDKs preserved backward compatibility and had already shipped beta support for the new spec at the time of this post

- **Evidence**: Statement made in the context of explaining why elicitation
  continues to work for existing clients.
- **Confidence**: emerging (first-party changelog assertion about the state
  of the broader SDK ecosystem, not independently verified against each
  SDK's own release notes)
- **Quote**: "Since all tier 1 SDKs have preserved backwards compatibility
  and they have all already shipped beta support, you don't need to do
  anything to maintain support."
- **Our assessment**: This is the practitioner-facing reassurance in the
  post: existing MCP client code using a tier-1 SDK should continue working
  against the GitHub MCP Server without changes, because the SDKs
  themselves already have beta support for the new spec and preserved
  compatibility with the old one. For Ch02: this is useful "no action
  required" guidance for teams already using a tier-1 MCP SDK, but it is
  worth flagging as unverified beyond this one changelog's assertion — teams
  should confirm their specific SDK's changelog rather than relying on this
  blanket statement alone.

### Claim 9: MCP now includes an official conformance test suite, and strict validation from that suite helps agents verify their own work

- **Evidence**: Closing section of the changelog, introducing the
  conformance suite and its stated purpose.
- **Confidence**: settled (first-party statement that the suite exists and
  is officially part of MCP; "helps agents verify their work" is a framing
  claim rather than an independently measured outcome)
- **Quote**: "In addition, MCP added official conformance tests. Strict
  validation helps agents to verify their work."
- **Our assessment**: This is new infrastructure for the ecosystem, not just
  a GitHub MCP Server change: an official test suite that any MCP server or
  client implementation can run against to check spec conformance. The
  "helps agents to verify their work" framing suggests these tests are meant
  to be usable by an agent (e.g., Copilot) itself, not only by human
  developers running a test harness. For Ch03 (Safety and Verification):
  document the conformance suite as a concrete verification mechanism for
  any team building or auditing a custom MCP server — a testable spec
  compliance bar distinct from the deeper gateway-level compliance testing
  already documented in `docs-ghaw-mcp-gateway-reference.md` Claim 11
  (that gateway's own three-level, 11-suite conformance framework is a
  different, gh-aw-specific test surface, not the general MCP conformance
  suite this post refers to).

### Claim 10: Verifying an MCP implementation against the new spec means giving an agent access to the conformance suite, the draft spec documentation, and any tier 1 SDK implementation

- **Evidence**: Closing instructional sentence pointing practitioners at the
  specific resources to use for verification.
- **Confidence**: settled (first-party, explicit instruction)
- **Quote**: "To use this, point Copilot at your codebase and provide access
  to: The conformance suite, The draft spec documentation, Any tier 1 SDK
  implementation."
- **Our assessment**: This is a concrete, actionable verification recipe:
  rather than manually cross-checking a custom MCP server implementation
  against the spec text, the post recommends pointing an agent (Copilot,
  named explicitly) at the codebase together with the three reference
  resources and letting the agent do the conformance check. This is a
  specific instance of the broader "agent as spec-conformance verifier"
  pattern — using an LLM with tool/file access to a formal spec, a
  conformance suite, and a reference implementation as a verification
  harness, rather than only as a code-writing tool. For Ch03: cite as a
  concrete example of agent-assisted conformance verification, distinct
  from agent-assisted code review or test-writing.

## Concrete Artifacts

### Changelog Text (reconstructed from targeted verbatim-quote fetches)

```
Title: GitHub MCP Server supports the next MCP specification
Published: July 23, 2026 · 2 minute read
Source: https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification

--- OPENING ---
"The MCP protocol is going stateless on 28th July 2026, and the GitHub MCP
Server supports the latest spec ahead of the official release."

--- WHAT'S CHANGING ---
"The new stateless core means MCP deployments are now easy to scale."
"Sessions and `initialize` are both removed, so you can connect to servers
faster."
"Clients can also complete the handshake in parallel."
"You'll see more remote servers supporting features like elicitation thanks
to multi round-trip requests."

--- GITHUB MCP SERVER IMPLEMENTATION (three changes) ---
1. Removed Redis sessions:
   "Database writes on `initialize` are gone, and database reads are gone."
2. Avoided deep packet inspection:
   "In the new spec we can do that from HTTP headers guaranteed to be
   present. That means no more inspecting the payload."
3. Upgraded elicitation:
   "Our stdio MCP server uses URL elicitation for easy user login. In the
   new protocol version, each step is a separate HTTP request."
   "To make this work with old and new clients, the Go SDK provides a
   wrapper that makes both mechanisms work."
   "The GitHub MCP server uses the official Go SDK."

--- COMPATIBILITY ---
"Since all tier 1 SDKs have preserved backwards compatibility and they have
all already shipped beta support, you don't need to do anything to maintain
support."

--- CLOSING / CONFORMANCE ---
"In addition, MCP added official conformance tests. Strict validation helps
agents to verify their work."
"This is a huge boost to all tiers of the official SDK, and to bespoke
clients and servers too, because AI assisted development is much easier to
verify with these tests."
"To use this, point Copilot at your codebase and provide access to: The
conformance suite, The draft spec documentation, Any tier 1 SDK
implementation."

Related link: MCP Release Candidate announcement
(https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)
```

*Source: reconstructed from multiple targeted WebFetch passes against the
changelog URL, each requesting short (under-40-word) verbatim quotes on a
specific sub-topic to maximize fidelity — see Extraction Notes.*

### Cross-Reference: MCP Release Candidate Post (linked from this changelog)

```
Source: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
(the upstream MCP spec post this GitHub changelog implements ahead of
schedule; followed as a substantive linked page per MINER.md §1)

"MCP is now stateless at the protocol layer"
"The `Mcp-Session-Id` header and the protocol-level session that came with
it are also removed"
"a Standards Track SEP can no longer reach Final status until a matching
scenario lands in the conformance suite"
"The feature lifecycle policy gives every feature an Active, Deprecated,
and Removed lifecycle with at least twelve months between deprecation and
removal"
"The release candidate is locked as of May 21, 2026. The final specification
will be published on July 28, 2026."
```

*Source: WebFetch summary of the linked MCP steering blog's release
candidate post. This is provided as corroborating context for Claims 1-3 —
it confirms the `Mcp-Session-Id` header (not just the `initialize` call) is
also removed, and that the spec ships a formal feature lifecycle policy
(Active/Deprecated/Removed, minimum 12-month deprecation window) not
mentioned in the GitHub changelog itself. This lifecycle-policy detail is
noted here for completeness but is out of scope for this note's Claims,
since it is not something the GitHub changelog itself asserts.*

## Cross-References

- **Extends**:
  - `docs-ghaw-mcps.md` Claim 2 (four MCP server types — stdio, Docker,
    HTTP, registry — with distinct trust and isolation profiles): this
    source's Redis-session-removal (Claim 5) and stdio elicitation rework
    (Claim 7) are concrete evidence that the underlying MCP transport layer
    itself is changing shape independent of gh-aw's server-type taxonomy.
    The stdio type in `docs-ghaw-mcps.md` is unaffected in kind (it's still
    a local process), but a stdio server built against the new spec (like
    GitHub's own) now handles elicitation as discrete HTTP requests rather
    than through a persistent session — an internal implementation change
    that gh-aw's stdio configuration schema does not need to know about, but
    that MCP server authors do.
  - `docs-ghaw-mcp-gateway-reference.md` Claim 9 (OpenTelemetry integration
    at the gateway level, with 10 T-OTEL compliance test cases) and Claim 11
    (three-level, 11-suite gh-aw MCP Gateway conformance framework): this
    source's Claim 9 (an official, protocol-level MCP conformance suite)
    is a distinct, upstream-of-gh-aw testing surface. The gh-aw gateway
    spec's conformance framework tests gh-aw's own gateway implementation
    against gh-aw's own requirements; the conformance suite this changelog
    describes tests any MCP server or client against the general MCP spec.
    A gh-aw MCP Gateway implementation could conceivably need to pass both:
    the general MCP conformance suite (protocol-level) and gh-aw's own
    T-CFG/T-PTL/T-ISO/etc. suites (gateway-implementation-level).
  - `blog-anthropic-mcp-production-agents.md` Claim 8 (MCP Apps and
    elicitation as the first official protocol extensions, with elicitation
    described as letting "your server pause mid-tool call to ask the user
    for input"): this source's Claims 4 and 7 add the transport-level detail
    that elicitation's mid-tool-call round trips are what the stateless
    spec's "multi round-trip requests" and GitHub's own separate-HTTP-request
    stdio rework are built to support efficiently at scale — the April 2026
    post named elicitation as a capability; this July 2026 post describes
    the protocol-level plumbing (statelessness) that makes it practical for
    *remote* servers, not just local stdio ones.
  - `blog-anthropic-mcp-production-agents.md` Claim 5 (production MCP
    servers should be remote/HTTP, not local stdio, because "production
    agents increasingly run in the cloud, so they can scale and operate
    continuously"): this source's Claim 2 ("the new stateless core means MCP
    deployments are now easy to scale") is the protocol-level change that
    directly supports that April 2026 recommendation — a stateless remote
    MCP server no longer needs sticky-session infrastructure to scale
    horizontally, removing one of the operational costs of following the
    "build remote servers" guidance.

- **Corroborates**:
  - `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` Claim 1 (MCP's
    primary value over skills/CLI is isolating the auth flow outside the
    agent's context window, "potentially out of the harness completely"):
    this source's Claim 6 (reading required values from HTTP headers
    instead of inspecting the payload) and Claim 7 (URL-based elicitation
    for login, handled server-side) are concrete implementation evidence
    consistent with Lynch's framing — the GitHub MCP Server's own
    authentication/login flow lives in server-side HTTP mechanics, not in
    anything the agent's context window needs to see or hold.

- **Contradicts**: None identified. No existing source note asserts that MCP
  will remain stateful, that `initialize`/session handshakes are permanent,
  or that Redis-backed session storage is required for MCP servers. The
  transition documented here (stateful → stateless) is a forward-looking
  spec change with a stated future effective date (July 28, 2026), not a
  disagreement with any prior source's description of the *current* (prior
  to that date) stateful protocol. No contradiction issue filed.

- **Novel**:
  - **Concrete date for the MCP stateless transition** (Claim 1): no
    existing source note documents July 28, 2026 as the date the MCP spec
    goes stateless, or that GitHub's own MCP Server was already running
    ahead of that date.
  - **Redis session removal as a specific, named infrastructure change**
    (Claim 5): no existing source note documents that a production MCP
    server (GitHub's) had a Redis dependency for session state, or that the
    new spec allowed removing it entirely.
  - **Header-based vs. payload-inspection value extraction** (Claim 6): this
    specific mechanical detail of the new spec is not documented elsewhere
    in the corpus.
  - **Official, protocol-level MCP conformance test suite** (Claim 9): no
    existing source note documents a general MCP conformance suite distinct
    from platform-specific compliance testing (e.g., the gh-aw MCP Gateway's
    own T-CFG/T-PTL/etc. suites in `docs-ghaw-mcp-gateway-reference.md`).
  - **Agent-assisted conformance verification recipe** (Claim 10): the
    specific instruction to point an agent (Copilot) at a codebase plus the
    conformance suite, draft spec, and a tier-1 SDK implementation as a
    verification method is new to the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the MCP statelessness transition as a dated fact practitioners
  should account for** (Claim 1): any guide language describing MCP's
  `initialize`/session handshake as foundational should be updated to note
  that the spec went stateless on July 28, 2026, and that the GitHub MCP
  Server adopted the change ahead of that date.
- **Cite the Redis-removal example as concrete evidence for the "build
  remote servers, they'll scale more easily" guidance** (Claim 5, extending
  `blog-anthropic-mcp-production-agents.md` Claim 5): when explaining why
  the new spec eases horizontal scaling of remote MCP servers, use GitHub's
  own Redis-session removal as the worked example — a named infrastructure
  dependency a production MCP server no longer needs.

### Chapter 03: Safety and Verification

- **Add the official MCP conformance suite as a verification resource**
  (Claim 9): distinct from gh-aw's own gateway conformance testing
  (`docs-ghaw-mcp-gateway-reference.md` Claim 11), this is a general,
  spec-level conformance suite any MCP server or client author can run.
  Document it as a first checkpoint for teams building or auditing custom
  MCP servers.
- **Add the agent-assisted conformance-check recipe as a concrete
  verification pattern** (Claim 10): "point an agent at your codebase plus
  the conformance suite, spec docs, and a reference SDK" is a specific,
  actionable instance of using an agent as a verifier rather than only as an
  implementer — worth citing alongside other agent-as-verifier patterns in
  the guide.

## Extraction Notes

1. **WebFetch on this page returns AI-summarized/paraphrased content, not
   raw HTML, and the underlying model in one pass explicitly declined to
   reproduce full body text verbatim for copyright reasons.** To get
   fair-use-length, verbatim quotes for every Claim above, five separate
   targeted WebFetch passes were made, each requesting short (under
   ~40-word) exact quotes on a specific named sub-topic (stateless core;
   sessions/initialize removal; parallel handshakes; Redis removal; header
   vs. payload inspection; elicitation; conformance tests; the July 28 date;
   the stdio elicitation rework; backward compatibility; the closing
   Copilot-verification instruction). Quotes that appeared consistently
   across passes are treated as accurate; none of the quotes above were
   reconstructed or spliced from non-adjacent sentences.
2. **One quote (the closing "point Copilot at your codebase..." instruction,
   Claim 10) was independently re-verified with a follow-up fetch** because
   its first appearance, out of context, read as though it might be
   boilerplate from an unrelated part of the page (e.g., a PR-review widget)
   rather than article body content. A targeted follow-up fetch confirmed it
   is part of the article's closing section, immediately following the
   conformance-suite sentence (Claim 9), not page chrome.
3. **The linked "MCP Release Candidate announcement" page was followed** per
   MINER.md §1 (up to 5 substantive linked pages) and is reproduced under
   Concrete Artifacts as corroborating context. Its claims about the
   `Mcp-Session-Id` header removal, the Standards Track SEP conformance-suite
   gating rule, and the feature lifecycle policy are NOT elevated to numbered
   Claims in this note, because this note's scope is what the GitHub
   changelog itself asserts; they are recorded for a future Miner pass that
   might mine the MCP steering blog directly as its own source.
4. **Only two of the three "Existing notes that overlap" cited across the
   three separate Prospector triage comments were substantively
   cross-referenced in depth** (`docs-ghaw-mcps.md`,
   `docs-ghaw-mcp-gateway-reference.md`,
   `blog-anthropic-mcp-production-agents.md`,
   `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`); `docs-ghaw-web-search.md`,
   `blog-addyosmani-loop-engineering.md`, and
   `blog-anthropic-admin-analytics-cost-controls.md` were checked and found
   to have no substantive overlap with this source's specific protocol-level
   claims (statelessness, Redis removal, conformance testing) beyond generic
   "MCP exists" context, so they are not cited above.
5. **No contradictions to file.** Reviewed CONTRADICTIONS.md and the
   cross-referenced source notes above; no existing claim asserts MCP
   statefulness is permanent or that Redis-backed sessions are required. No
   contradiction issue filed.
6. **Confidence rated `emerging` overall**, not `settled`, despite most
   individual claims being rated `settled` for what GitHub's own changelog
   asserts about GitHub's own server: the underlying protocol change has not
   yet shipped as of the source's publication date (final spec: July 28,
   2026) or as of this extraction (July 24, 2026), and this note relies on
   WebFetch-summarized reconstructions of a changelog page rather than raw
   HTML, with no independent confirmation from the MCP spec repository
   itself beyond the one linked Release Candidate post.
