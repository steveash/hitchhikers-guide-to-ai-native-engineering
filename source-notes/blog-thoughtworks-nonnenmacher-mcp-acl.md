---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/your-agent-skill-not-anti-corruption-layer
source_type: blog-post
title: "Your agent skill is not an anti-corruption layer"
author: Fabian Nonnenmacher (Thoughtworks)
date_published: 2026-06-12
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: emerging
issue: "#1612"
---

# Your agent skill is not an anti-corruption layer

> A Domain-Driven Design (DDD) critique of using MCP as a universal integration
> adapter for agents: MCP's frictionless adoption is a superpower for local,
> individual-developer use, but the same property — exposing raw upstream API
> schemas directly to the agent's system prompt — turns the agent into a DDD
> "conformist" at enterprise scale, creating context bloat, silent breakage on
> upstream API changes, and cross-system semantic confusion. The recommended
> fix is to build domain-specific tools (an anti-corruption layer, ACL) in the
> agent's own ubiquitous language, using native agent-framework capabilities and
> production-tested protocols (REST/GraphQL/gRPC) rather than treating MCP
> itself as the ACL.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published June 12, 2026; auto-discovered
  via the trusted `thoughtworks` RSS feed)
- **Author credibility**: Fabian Nonnenmacher, writing on Thoughtworks' official
  insights blog. The article itself does not state a title or years of experience
  for the author (WebFetch of the article returned no title/credentials field).
  The Prospector's triage comments assert he is a "Thoughtworks principal," but
  that credential was not independently verified against the article page itself
  and should be treated as unconfirmed. Thoughtworks as a publisher carries
  general credibility in software architecture consulting (the same firm behind
  Martin Fowler's writing and the Technology Radar), which is the primary basis
  for treating this as a substantive architectural argument rather than casual
  commentary.
- **Scope**: Covers the application of DDD concepts (bounded context, ubiquitous
  language, conformist pattern, anti-corruption layer) to the specific question
  of whether MCP should be an agent's default integration mechanism for external
  enterprise systems. Uses a Jira MCP server and a multi-system travel-booking
  example ("reservation" meaning something different in flight, hotel, and
  expense-compliance systems) as running illustrations. Does NOT cover: MCP
  protocol internals, specific token/cost measurements, security/auth mechanisms,
  or a comparison against Anthropic's own MCP server design guidance (see
  Cross-References below) — the article does not engage with or cite
  Anthropic's MCP production guidance directly.

## Extracted Claims

### Claim 1: MCP's frictionless adoption is a superpower for individual developers, but the same property creates architectural debt when scaled to enterprise-grade agent systems
- **Evidence**: Author's own framing of MCP's core strength and its scaling failure, illustrated with the practice of adding a Jira MCP server via a one-click VS Code connection or a few lines in a local `mcp.json` configuration file.
- **Confidence**: emerging (architectural argument from a credible publisher, not a measured study)
- **Quote**: "MCP's biggest strength is its frictionless adoption." / "For individual developers, however, it's a superpower." / "It feels like magic. But when we try to scale this 'local coding agent' pattern to enterprise-grade AI applications, we run straight into architectural debt."
- **Our assessment**: This is the article's central thesis and the frame for every claim that follows. The distinction it draws — MCP-for-individual-velocity vs. MCP-for-enterprise-integration — is a genuine conditioning variable the guide should preserve rather than flatten into a blanket "MCP good" or "MCP bad" recommendation.

### Claim 2: A bounded context defines an explicit boundary within which one domain model and one shared "ubiquitous language" apply
- **Evidence**: Standard DDD framing, attributed in the article to Eric Evans, applied to the Jira example: a team's internal definition of "User Story" differs from Jira's generic "Issue."
- **Confidence**: settled (this is established DDD theory, not a novel claim by the author — the novelty is in the application to agent architecture)
- **Quote**: "A bounded context delimits the applicability of a particular model so that team members have a clear and shared understanding" (attributed to Eric Evans in the article) / "Inside this boundary, all terms, definitions and rules form a ubiquitous language"
- **Our assessment**: This is the load-bearing theoretical framework for the rest of the article. It is worth citing as background/definition rather than as a contested claim — DDD's bounded-context concept is decades-old and widely accepted in software architecture; what's new here is using it to reason about agent/MCP integration.

### Claim 3: Exposing raw upstream MCP tool schemas directly to an agent turns the agent into a DDD "conformist" — it adopts the upstream system's domain model wholesale instead of maintaining its own
- **Evidence**: Author's core architectural diagnosis, naming the DDD "conformist" integration pattern as the failure mode of naive MCP use.
- **Confidence**: emerging (conceptual/architectural claim, not measured)
- **Quote**: "The downstream system completely conforms to the upstream system's domain model."
- **Our assessment**: This is the single most citable line in the article for a guide audience — it names the anti-pattern precisely in DDD vocabulary. The claim is that an agent wired directly to an off-the-shelf MCP server does not get to define its own vocabulary or validation rules; it inherits whatever the upstream API author decided to expose.

### Claim 4: Off-the-shelf MCP servers expose far more tools than a given agent needs, inflating context window size and token cost
- **Evidence**: Jira MCP server example — the server's generic tool surface vs. a specific coding agent's actual needs.
- **Confidence**: emerging (illustrative example, no token measurements in this article)
- **Quote**: "An off-the-shelf Jira MCP server typically exposes dozens of generic tools" while "Your specific coding agent might only ever need two or three of them."
- **Our assessment**: This corroborates the token-cost mechanism independently measured in `blog-bswen-mcp-token-cost.md` (Claim 1: every MCP server loads all its tool definitions into the system prompt before any work begins). Nonnenmacher's claim is qualitative/architectural (tool bloat as a symptom of missing bounded-context discipline); Bswen's is quantitative (specific token counts per server). Together they make a stronger combined case than either alone.

### Claim 5: An upstream API change can silently alter the tool schemas passed to the agent, and the agent's application code has no way to catch the breaking change
- **Evidence**: Author's stated architectural risk of direct MCP-to-upstream coupling.
- **Confidence**: emerging (architectural risk claim, not an observed incident)
- **Quote**: "An upstream API change can instantly alter the tool schemas passed to your agent. Your application code won't catch this breaking change."
- **Our assessment**: This is a specific, falsifiable-in-principle risk claim distinct from the token-bloat claim: it is about correctness and silent failure, not cost. The mechanism is plausible — if tool schemas are pulled live from the upstream MCP server rather than pinned/versioned, there is no contract boundary at which a breaking change would be caught before it reaches the agent's context. The guide should flag this as a case for pinning/versioning MCP tool schemas even when using MCP, independent of whether a full ACL is built.

### Claim 6: Naive MCP integration makes it dangerously easy to skip proper system design and let raw, uncurated upstream data structures dictate the agent's cognitive model
- **Evidence**: Author's summary framing of the cumulative risk of Claims 3-5.
- **Confidence**: emerging (author's synthesis/opinion, not independently measured)
- **Quote**: "It makes it dangerously simple to skip proper system design and let raw, uncurated upstream data structures dictate your agent's cognitive model."
- **Our assessment**: This is the article's strongest normative claim and the one most likely to be cited as a soundbite. "Cognitive model" is doing real work here — the claim is not just about cost or fragility but about the agent's reasoning being shaped by whatever vocabulary the upstream API happens to use, rather than by a deliberately designed domain vocabulary.

### Claim 7: The same term can mean fundamentally different things across bounded contexts, and connecting those contexts without translation traps the agent in a linguistic contradiction
- **Evidence**: A travel-booking illustration: "reservation" has different meanings and lifecycles in a flight-booking system, a hotel system, and an expense-compliance engine.
- **Confidence**: emerging (illustrative example, not a documented production incident)
- **Quote**: "Trying to connect them forces the agent into a linguistic trap" because "reservation" triggers different error states and operational rules in each system.
- **Our assessment**: This is the clearest concrete illustration of "semantic risk" in the article — a term that means one thing in bounded context A and another in bounded context B produces agent confusion when both are exposed through the same MCP-mediated vocabulary without a translation layer reconciling them. This is a specific, reusable example for a guide chapter on tool/context design.

### Claim 8: The recommended fix is to build domain-specific tools — an anti-corruption layer — in the agent's own ubiquitous language, using native agent-framework capabilities and production-tested protocols instead of raw MCP passthrough
- **Evidence**: Author's prescriptive recommendation, naming Pydantic AI as an example framework and REST, GraphQL, and gRPC as example production protocols.
- **Confidence**: emerging (architectural recommendation, not benchmarked against the MCP-only alternative in this article)
- **Quote**: "you can model the tool interfaces entirely in the agent's internal, specialized vocabulary" / "By using robust data-validation, you can decorate your interfaces with rich metadata" / "your native agent tools can communicate directly with enterprise systems using established, production-tested protocols"
- **Our assessment**: This is the article's positive proposal, mirroring classic DDD anti-corruption-layer design: define your own model and language, validate inputs against it, and translate at the boundary rather than importing the upstream model wholesale. Framework-specific (Pydantic AI is named as one option, not the only one). The claim that REST/GraphQL/gRPC are more "production-tested" than MCP for this purpose is asserted, not evidenced with a comparative reliability study.

### Claim 9: MCP is not to be abandoned outright — a custom internal MCP server can itself serve as the ACL, and the choice is a tipping point between prioritizing flexibility (early/exploratory) vs. reliability (production)
- **Evidence**: Author's closing qualification, directly answering "should we remove MCP from our toolbox?"
- **Confidence**: emerging (author's own hedge/qualification on the article's main argument)
- **Quote**: "you could build a custom internal MCP server to act as your ACL" / "MCP's undisputed superpower is speed of adoption" / "At that tipping point, your priority must shift from flexibility to reliability."
- **Our assessment**: This qualification is important and easy to miss if only Claims 1-8 are cited: the article is not "never use MCP for enterprise systems," it is "don't let an off-the-shelf/upstream MCP server's raw schema become your agent's domain model — if you use MCP at all in production, wrap it in a boundary you designed." This nuance matters for how the guide frames the recommendation — it is about where the ACL lives, not about banning a specific protocol.

## Concrete Artifacts

```
Article structure (in order), Fabian Nonnenmacher, Thoughtworks Insights,
"Your agent skill is not an anti-corruption layer," June 12, 2026:

1. Where MCP shines: Fast adoption
2. A quick DDD refresher: Bounded contexts
3. The conformist agent
4. The enterprise challenge: context translation
5. The better way: domain specific tools as your ACL
6. Should we remove MCP from our toolbox?
```

```
DDD vocabulary applied to agent/MCP architecture (as used in the article):

- Bounded context   → the boundary within which one domain model + ubiquitous
                       language applies (e.g., a team's own definition of
                       "User Story" vs. Jira's generic "Issue")
- Conformist pattern → downstream system fully adopts the upstream model
                       ("The downstream system completely conforms to the
                       upstream system's domain model.")
- Anti-corruption
  layer (ACL)        → "A translating layer created between two contexts.
                       The downstream system refuses to be polluted by the
                       upstream model."
- Applied claim      → an agent wired directly to a raw MCP server is
                       architecturally a conformist to the upstream system,
                       not a bounded context with its own ACL
```

## Cross-References

- **Contradicts**: `blog-anthropic-mcp-production-agents.md` Claim 4 and Claim 5.
  That note (first-party Anthropic guidance, issue #349) states MCP "is the
  recommended integration layer for production cloud agents" and recommends
  building remote MCP servers as the standard production integration pattern
  ("Build remote servers so agents can use your system wherever they run").
  This Thoughtworks source argues the opposite emphasis for the same
  production/enterprise context: that raw MCP-server integration (even a
  well-designed one) risks making the agent a DDD conformist to upstream
  schemas, and that production systems should instead build domain-specific
  tools as an anti-corruption layer using native framework capabilities and
  REST/GraphQL/gRPC, with MCP relegated to local/individual-developer use (or,
  at most, wrapped behind a custom-built internal MCP server that itself acts
  as the ACL). Notably, Anthropic's Claim 6 ("group tools around intent, so
  the agent can accomplish a task in a couple of calls") addresses a very
  similar symptom (tool bloat / exhaustive API mirrors) but proposes fixing it
  through better MCP *server design*, not by moving the integration outside
  MCP entirely. This is a genuine disagreement about the recommended default
  integration architecture for production/enterprise agent systems, not a
  small-scale-vs-large-scale conditioning variable — both sources are
  explicitly discussing production/enterprise-grade systems. Filed as
  contradiction issue #1625 (see also `**Contradicts**` note there); do not
  treat either side as the guide's settled position until that issue is
  resolved and a `C-NNN` entry is appended to CONTRADICTIONS.md.

- **Corroborates**: `blog-bswen-mcp-token-cost.md` Claim 1 and Claim 2. Bswen
  measured that every connected MCP server loads its full tool definitions
  into the system prompt before any user input, at roughly 5-7k tokens per
  server. Nonnenmacher's Claim 4 (off-the-shelf servers expose "dozens of
  generic tools" vs. the two or three an agent actually needs) is the
  qualitative/architectural version of the same observation — Bswen supplies
  the quantitative token cost, Nonnenmacher supplies the DDD explanation for
  *why* it happens (no bounded-context discipline constraining what gets
  exposed).

- **Corroborates**: `blog-anthropic-maccoss-developer-onboarding.md` Claim 11.
  MacLean's post describes MCP servers (a C# visual-diff server, a Python
  data-aggregation server) built and used successfully for a single academic
  lab's own operational needs — exactly the "individual developer / small
  team, local, self-built" context Nonnenmacher's Claim 1 concedes is MCP's
  "superpower." This is consistent, not contradictory: MacLean's MCP servers
  are custom-built for the lab's own needs (arguably already function as
  their own ACL) rather than raw off-the-shelf third-party servers wired
  directly into a large enterprise agent deployment, which is the specific
  pattern Nonnenmacher's critique targets.

- **Extends**: `docs-ghaw-mcps.md`. That note documents gh-aw's four MCP
  server types (stdio, Docker, HTTP, registry) and its read-only policy for
  custom MCP servers, enforced by convention rather than protocol. Nonnenmacher's
  Claim 9 concession — that a custom-built internal MCP server can serve as a
  proper ACL — implies that gh-aw's Docker/registry containerized custom
  server types are a plausible substrate for building exactly that kind of ACL,
  provided the server author designs its tool surface around the agent's own
  vocabulary rather than mirroring an upstream API. gh-aw's docs do not
  currently frame server design in DDD terms; this source could inform future
  guidance on custom MCP server design for that platform.

- **Novel**: The DDD (bounded context / conformist pattern / anti-corruption
  layer) vocabulary applied specifically to agent-to-MCP integration is new to
  the corpus. No other source note frames the MCP tool-bloat, schema-fragility,
  or cross-system semantic-confusion problems using this theoretical
  architecture-design vocabulary — prior sources (Bswen, Anthropic) describe
  the same symptoms (token cost, schema mirroring) but propose fixes at the
  protocol/config level (tool search, `allowed:` filters, server-count pruning,
  intent-grouped tool design) rather than at the domain-modeling level
  (build your own vocabulary and validate at the boundary).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The guide currently (via
  `blog-anthropic-mcp-production-agents.md`) recommends MCP as the standard
  production integration layer, with design principles for MCP *server*
  authors. This source provides a competing recommendation for MCP *client*-side
  architecture: rather than wiring an agent directly to an off-the-shelf
  upstream MCP server, build domain-specific tools in the agent's own
  vocabulary (an ACL) and reserve MCP for exploration or for internally-built
  servers that already function as an ACL. Recommend adding a `**Debated:**`
  block once contradiction issue #1625 is resolved, rather than presenting
  either recommendation as settled.

- **Chapter 04 (Context Engineering)**: Claim 4 (tool bloat from off-the-shelf
  MCP servers) should be added as architectural context for the existing
  token-cost material from `blog-bswen-mcp-token-cost.md` — the guide can now
  explain both *how much* raw MCP integration costs (Bswen's numbers) and
  *why* it happens from a system-design perspective (Nonnenmacher's bounded-context
  argument).

- **Chapter 06 (Security Threat Model, if this is the chapter covering
  integration risk)**: Claim 5 (silent breaking changes from upstream schema
  drift) and Claim 7 (cross-system term collisions) should be added as two
  specific, concrete integration-risk scenarios distinct from the security
  literature's usual focus on prompt injection and credential handling — these
  are correctness/reliability risks introduced by architecture choices, not
  adversarial attacks.

## Extraction Notes

- The source is a JavaScript-rendered Thoughtworks blog page. WebFetch returns
  AI-generated summaries of the rendered content rather than raw HTML/text, so
  four separate targeted fetches were performed (one general overview, then
  three section-scoped fetches asking for short, exact quoted fragments) to
  maximize verbatim quote fidelity. Quotes used in this note appeared
  consistently in quotation marks across fetches when re-requested for the
  same section, which is the same verification approach used in
  `blog-anthropic-mcp-production-agents.md` and `blog-cursor-cloud-agent-lessons.md`
  for the same JS-rendering / summarization limitation. No independent means
  of diffing against raw page HTML was available in this environment.
- The article does not name or engage with Anthropic's own MCP production
  guidance (`blog-anthropic-mcp-production-agents.md`) at all — the
  contradiction identified above is structural (both sources address the same
  question) rather than a direct rebuttal by either author.
- The author's credentials ("Thoughtworks principal") appear only in the
  Prospector's triage comments, not in content independently confirmed from
  the article itself via WebFetch. Treat that specific credential as
  unverified; the `Author credibility` field above reflects only what could be
  confirmed.
- No code examples, terminal transcripts, or metrics were found in the source
  — it is a conceptual/architectural argument piece, not an implementation
  report. This is reflected in the `emerging` (not `settled` or purely
  `anecdotal`) confidence_overall rating: the DDD theory underpinning it is
  settled, but its specific application to MCP/agent architecture is a new,
  unmeasured argument from a single author/publisher.
- Filed contradiction issue #1625 against `blog-anthropic-mcp-production-agents.md`
  per MINER.md §4a before opening this PR.
