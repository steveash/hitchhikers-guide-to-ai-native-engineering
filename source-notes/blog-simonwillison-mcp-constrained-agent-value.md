---
source_url: https://simonwillison.net/2026/Sep/20/hn-49779718/
source_type: blog-post
title: "Comment: MCP was always a bad idea?"
author: Simon Willison
date_published: 2026-09-20
date_extracted: 2026-09-28
last_checked: 2026-09-28
status: current
confidence_overall: anecdotal
issue: "#3762"
---

# Simon Willison on MCP was always a bad idea?

> Simon Willison's Hacker News comment (cross-posted to his blog) rebuts a
> viral "delete your MCP servers" post by naming the specific axis that
> decides whether MCP is worth using: not integration ergonomics, but how
> constrained/multi-tenant the agent needs to be — full-network terminal
> agents don't need MCP, but access control, auth isolation, connection UI,
> and audit logging still do.

## Source Context

- **Type**: blog-post — a "Comment" entry on Simon Willison's blog, which
  auto-publishes his own Hacker News comments as short standalone posts
  linking back to the originating thread. The blog entry itself is thin:
  one paragraph, a four-item bulleted list, and a closing sentence (~120
  words total). Per MINER.md §1, two linked pages were followed because the
  blog entry is unintelligible without them: (1) the Hacker News thread it
  was posted to (`news.ycombinator.com/item?id=49779329`, 330 comments,
  titled "MCP was always a bad idea?"), which contains Willison's comment
  in its original context plus substantive practitioner replies; and (2)
  the article the thread discusses, Maharshi Patel's "Why MCP Was Always a
  Bad Idea" (`maharship.com/blog/why-mcp-was-always-a-bad-idea/`, published
  2026-09-14), which is the target of Willison's rebuttal.
- **Author credibility**: Simon Willison — creator of Django and Datasette,
  prolific and widely-cited AI tooling commentator, no vendor affiliation.
  Already well-represented in this corpus (see Cross-References). The
  underlying article's author, Maharshi Patel, is a named individual blogger
  (maharship.com, personal/portfolio site) with no stated MCP or Anthropic
  affiliation; the piece is opinion/argument, not a vendor announcement or
  measurement study.
- **Scope**: Covers when MCP's architectural value holds versus when it's
  unnecessary overhead, framed narrowly around one variable — agent
  autonomy/network access level. Does NOT cover MCP protocol internals,
  performance/token-cost tradeoffs (covered elsewhere in corpus), or a
  full rebuttal of Patel's context-bloat argument — Willison's comment does
  not address context bloat at all, only the "agents don't need MCP anymore"
  conclusion.

## Extracted Claims

### Claim 1: Full-blown terminal agents with unfettered internet access have almost no reason to use MCP — they should just call APIs directly
- **Evidence**: Author's stated position, presented as the concession point in his own rebuttal (he opens by agreeing with this much of the critique before drawing his distinction).
- **Confidence**: anecdotal
- **Quote**: "Sure, there's almost no reason to use MCPs if you are running a full-blown terminal agent (Claude Code, Codex, Meta Muse, OpenClaw etc) with unfettered internet access - just let it call APIs directly."
- **Our assessment**: This is a significant concession from one of the most-cited pro-MCP voices in the corpus, and narrows the scope of every other pro-MCP claim in the corpus (e.g. `blog-anthropic-mcp-production-agents.md` Claim 4, "MCP is the recommended integration layer for production cloud agents") to a specific deployment shape: constrained, non-terminal, often multi-tenant agents. It does not contradict Claim 4 there — "production cloud agents" in that Anthropic post are exactly the constrained case Willison is carving MCP's remaining value out for — but it does mean neither source should be read as a blanket endorsement of MCP for coding-agent-style deployments.

### Claim 2: Operating anything less permissive than a fully unfettered terminal agent requires control over exactly which external services the agent can access
- **Evidence**: First of four numbered constraints in the author's list, offered without elaboration or metrics.
- **Confidence**: anecdotal
- **Quote**: "Control over exactly which external services it can access"
- **Our assessment**: This restates an access-control argument for MCP as a mediating layer rather than raw network access. It's consistent with, but less concrete than, `docs-ghaw-mcp-gateway-reference.md`'s guard-policy and container-isolation mechanisms (Claims 4, 5, 10), which are an actual implementation of "control over which services an agent can reach."

### Claim 3: Operating a constrained agent requires a way to handle authentication that doesn't allow the agent to directly access API keys
- **Evidence**: Second of four numbered constraints, asserted without elaboration.
- **Confidence**: settled
- **Quote**: "A way to handle authentication that doesn't allow the agent to directly access API keys"
- **Our assessment**: This is the same core argument Willison made three months earlier quoting Sean Lynch (`blog-simonwillison-sean-lynch-mcp-auth-gateway.md` Claim 1: "MCP's primary architectural value over skills/CLI is isolating auth flows outside the agent's context window"), now restated in his own words in a different debate. Two independent framings from the same author, months apart, in response to different critiques, converging on the same claim raises this from a one-off anecdote to a settled position for Willison specifically. It's also corroborated architecturally by `blog-anthropic-agent-identity-access-model.md` Claim 8 (credentials "injected at the network boundary at request time — never attached to individual users").

### Claim 4: Operating a constrained agent requires a sensible UI to allow users to connect and authenticate further services
- **Evidence**: Third of four numbered constraints, asserted without elaboration or example.
- **Confidence**: anecdotal
- **Quote**: "A sensible UI to allow users to connect and authenticate further services"
- **Our assessment**: This is the one constraint in Willison's list that is genuinely novel to the corpus — prior MCP-and-auth notes (Sean Lynch, Anthropic agent identity) focus on where credentials live and how they're isolated, not on the end-user-facing connection experience. No existing source note documents MCP's role in providing a standardized "connect your account" UI pattern comparable to OAuth consent screens.

### Claim 5: Operating a constrained agent requires strong audit logging for what the agent is doing
- **Evidence**: Fourth of four numbered constraints, asserted without elaboration.
- **Confidence**: settled
- **Quote**: "Strong audit logging for what's going on"
- **Our assessment**: Directly corroborated by `blog-anthropic-agent-identity-access-model.md` Claim 10 ("Agent actions are logged through a dual audit trail — Claude's own audit log plus each connected system's native logs") and by `docs-ghaw-mcp-gateway-reference.md` Claim 9 (gateway-level OpenTelemetry with a 10-test compliance suite). Both show concrete first-party implementations of exactly the audit-logging value Willison asserts abstractly here — the claim is well supported elsewhere in the corpus even though this source offers no specifics of its own.

### Claim 6: MCP makes all four of the above (access control, auth isolation, connection UI, audit logging) so much easier to provide than building them ad hoc
- **Evidence**: Author's summary conclusion tying the four bullets together; no comparison data against a non-MCP baseline.
- **Confidence**: anecdotal
- **Quote**: "MCP makes all of that so much easier to provide."
- **Our assessment**: This is the load-bearing claim and it's the weakest-supported one in the post — "easier" is asserted, not demonstrated, and Willison doesn't address the context-bloat and maintenance costs that the article he's rebutting (and `blog-bswen-mcp-token-cost.md`, `source-notes/blog-thoughtworks-nonnenmacher-mcp-acl.md`) document as real costs of choosing MCP. We buy the directional claim (a standard protocol is easier than four bespoke ad hoc systems) but flag that "easier" here is relative to building the same four things from scratch, not relative to skipping them or using a lighter-weight pattern (e.g. a REST gateway with OIDC).

### Claim 7: Believing MCP is obsolete because full coding agents don't need it overlooks the other kinds of systems people build with agents
- **Evidence**: Author's closing framing/thesis statement.
- **Confidence**: anecdotal
- **Quote**: "Thinking MCP is obsolete because full coding agents don't need it misses out on all of the other things we might want to build."
- **Our assessment**: This is the cleanest one-line summary in the corpus of the "coding-agent-shaped thinking distorts general agent architecture advice" failure mode — worth quoting directly in the guide as a caution against generalizing from terminal-coding-agent experience (Claude Code, Codex) to all agent system design.

### Claim 8: In practice, MCP's Tools capability accounts for the overwhelming majority of real-world MCP usage, while Resources, Prompts, and especially Elicitation see little to no adoption
- **Evidence**: Willison's own follow-up reply later in the same Hacker News thread, made in response to a commenter (`kaoD`) who linked the MCP spec to dispute the "MCP is just Tool Use" framing.
- **Confidence**: anecdotal
- **Quote**: "The spec describes Resources, Prompts, Tools, and Elicitation. In practice, I believe Tools represent 95%+ of what people actually use MCP for. I've not seen an MCP with Resources or Prompts that seems to have widespread use of those features, and I don't think I've ever seen anything implement Elicitation."
- **Source location**: Hacker News thread `item?id=49779329`, reply by `simonw` to `kaoD`, same page as the primary comment.
- **Our assessment**: This is a specific, falsifiable-sounding claim about spec-versus-practice gap that isn't in the blog post itself but directly extends it — it's Willison qualifying his own "MCP makes it easier" argument (Claim 6) by conceding that most of the protocol's surface area is unused in practice. No existing corpus source documents which parts of the MCP spec (Tools/Resources/Prompts/Elicitation) actually see adoption; this is new, even though it's a single practitioner's impression rather than measured data ("I believe", "I've not seen").

### Claim 9: A concrete production pattern validating Willison's access-control and audit constraints: a fleet of sandboxed coding agents can be given MCP tools against a virtual, non-existent filesystem, keeping the agents fully unaware of and unable to reach the real cloud credentials behind it
- **Evidence**: A named practitioner's (`prescriptivist`) first-hand description of a running system, posted as a reply to Willison's comment in the same HN thread.
- **Confidence**: anecdotal
- **Quote**: "I have a fleet of sandboxed Claude Code instances running and they share files with each other. The files are stored on AWS but they don't have access to AWS at all -- they can't see the access keys. In fact they don't know the files are on AWS. Instead they have a set of MCP tools for listing/uploading/downloading from an internal, virtual filesystem with a special URI handler (ie agentfiles://somefile.json) and the outer orchestrator of the Claude Code instances takes the MCP requests and does the actual file manipulation on Claude's behalf. The LLM seems to adapt quite well to this strange, arbitrary filesystem and I get to keep these agents fully compartmentalized. And I have tool request logs and logs in the outer orchestrator for full auditing of the agents. MCP is a really natural fit for this kind of stuff."
- **Source location**: Hacker News thread `item?id=49779329`, reply by `prescriptivist`, first-level reply to Willison's top comment.
- **Our assessment**: This is the single most concrete artifact in the whole thread — a named, specific architecture (custom `agentfiles://` URI scheme, MCP as the compartmentalization boundary between coding agents and real AWS credentials) that is a direct, working instance of Claim 2 (access control) and Claim 5 (audit logging) rather than an abstract assertion of them. Worth extracting as a pattern example even though it's a single anonymous HN commenter's unverified self-report, not a vendor or named-company case study.

### Claim 10: A competing view from the same thread: MCP's real niche is narrower than either "always use it" or "always skip it" — it fits problems too constrained for direct agent+curl access but not so open that a full agentic client makes more sense, and SaaS-to-SaaS integration is where that niche concentrates
- **Evidence**: A separate commenter's (`socketcluster`) framing, with a direct reply from `anon84873628` narrowing it further to SaaS-to-SaaS integration specifically.
- **Confidence**: anecdotal
- **Quote**: "MCP definitely has its niche in certain environments. It's good for a specific kind of constrained problem; not so constrained that you could solve the problem with just Node.js + fetch call to LLM API but not so open that you'd want to let the AI agent directly invoke any service it wants over the web."
- **Source location**: Hacker News thread `item?id=49779329`, top-level comment by `socketcluster`; reply by `anon84873628`: "That niche environment is all SaaS-to-SaaS integrations. The client doesn't want to have users struggling to get every integration working on their platform. The service providers don't want to have to support non-standarized behavior by every client."
- **Our assessment**: This sharpens Willison's "constrained agent" framing (Claim 1) into a specific deployment shape — third-party-to-third-party integrations where neither side controls the other's harness — rather than leaving "constrained" undefined. It's a useful complement, not a contradiction: Willison names the *properties* a constrained deployment needs (auth isolation, audit logging, etc.); this thread exchange names *where* those deployments concentrate (SaaS-to-SaaS). Elsewhere in the same comment (a separate paragraph, not part of the quoted passage above), `socketcluster` also states a preference for "SKILL.md + curl" as the general mechanism for agent tool calling over MCP, calling MCP "niche" — consistent with the same claim, paraphrased here rather than spliced into the quote above since the two passages are not adjacent in the source. Both are anecdotal HN-thread opinions, not measured claims.

### Claim 11: The article Willison is rebutting argues that improving agent competency at using `--help` to discover CLIs and writing ad hoc scripts against documented APIs has made most remote MCP servers unnecessary, since they mostly just wrap APIs that already exist
- **Evidence**: Direct extraction from the target article, Maharshi Patel's "Why MCP Was Always a Bad Idea" (maharship.com, 2026-09-14), which is what Willison's comment is responding to.
- **Confidence**: anecdotal
- **Quote**: "But even better than that, the LLMs have figured out how to use the --help command to discover CLIs, so they no longer need MCP servers to access many services available through documented APIs or CLIs. Most remote-service MCP servers ultimately wrap APIs that already exist."
- **Source location**: maharship.com/blog/why-mcp-was-always-a-bad-idea/, "Surprise, Surprise, the Big Labs Were Right" section.
- **Our assessment**: This is the specific claim Willison's whole comment is aimed at rebutting, and it's important context for why his rebuttal is framed the way it is: Patel's argument is scoped to "agents with terminal access," which is exactly the case Willison concedes in Claim 1. Read together, the two pieces mostly talk past each other on the constrained-agent case — Patel's article never addresses multi-tenant, access-controlled, or audited deployments at all, which is Willison's whole point.

### Claim 12: The same article proposes that documentation-serving MCP servers can be replaced by simple HTTP content-negotiation headers — `Accept: text/markdown` for machine-readable docs and a proposed `Accept-Language`-based mechanism for language/framework-specific examples — and cites this as already shipping at real companies
- **Evidence**: A named, quoted exchange between a Vercel engineer and Shopify's CEO, presented by the article as evidence the pattern is gaining real adoption.
- **Confidence**: emerging
- **Quote**: "Malte Ubl (@cramforce): Request to harnesses: I love that you now send “Accept: text/markdown”. Next thing is: Put the programming language you prefer into the Accept-Language header." / "Tobi Lutke (@tobi): Great idea. Will support this on Shopify docs."
- **Source location**: maharship.com/blog/why-mcp-was-always-a-bad-idea/, "Some Real Examples" section.
- **Our assessment**: Novel to the corpus — no existing source note documents content-negotiation headers (`Accept: text/markdown`, proposed `Accept-Language` for code examples) as a lightweight alternative to a documentation MCP server. This is a genuinely different integration pattern from either "build an MCP server" or "let the agent curl the API," and is concrete enough (named companies, a quoted commitment from Shopify) to be worth prospecting as its own source if a primary write-up of the "Accept: text/markdown" convention exists.

## Concrete Artifacts

```
Simon Willison's four-constraint list (verbatim, simonwillison.net/2026/Sep/20/hn-49779718/):

  1. Control over exactly which external services it can access
  2. A way to handle authentication that doesn't allow the agent to
     directly access API keys
  3. A sensible UI to allow users to connect and authenticate further
     services
  4. Strong audit logging for what's going on
```

```
prescriptivist's production pattern (HN thread item?id=49779329, reply to
Willison's comment) — MCP as a compartmentalization boundary:

  - Fleet of sandboxed Claude Code instances share files with each other
  - Files physically live on AWS; agents have no AWS access and don't
    know AWS is involved
  - Agents call MCP tools against a virtual filesystem with a custom URI
    scheme: agentfiles://somefile.json
  - An outer orchestrator receives the MCP requests and performs the
    real file manipulation on the agent's behalf
  - Tool request logs (agent side) + orchestrator logs (real-system side)
    give full audit coverage
```

```
Maharshi Patel's counter-proposal to MCP for documentation serving
(maharship.com/blog/why-mcp-was-always-a-bad-idea/, "Some Real Examples"):

  - Servers honor `Accept: text/markdown` and return rendered Markdown
    instead of HTML
  - Proposed extension: agents send preferred programming language via
    `Accept-Language`, so docs sites serve language-specific examples
  - Cited as already committed to by Shopify (per Tobi Lütke's reply to
    Vercel's Malte Ubl on social media)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` Claim 1 ("MCP's
    primary architectural value over skills/CLI is isolating auth flows
    outside the agent's context window") and Claim 3 (a pure "auth
    gateway" MCP would still be worth having): this source's Claim 3 here
    is the same author restating the identical position, three months
    later, in response to a completely different critique. Two
    independent framings converging on the same core argument strengthens
    it from "one Willison post" to "Willison's consistent position."
  - `blog-anthropic-agent-identity-access-model.md` Claim 8 (credentials
    "injected at the network boundary at request time — never attached to
    individual users") corroborates this source's Claim 3 (auth without
    exposing API keys to the agent) with a first-party production
    architecture (Claude Tag/Cowork identity model).
  - `blog-anthropic-agent-identity-access-model.md` Claim 10 ("Agent
    actions are logged through a dual audit trail") and
    `docs-ghaw-mcp-gateway-reference.md` Claim 9 (gateway-level
    OpenTelemetry with a 10-test compliance suite): both corroborate this
    source's Claim 5 (strong audit logging) with concrete implementations
    of what Willison only asserts abstractly.
  - `docs-ghaw-mcp-gateway-reference.md` Claims 4, 5, and 10 (guard
    policy integrity levels, precedence algorithm, and four-property
    container isolation) corroborate this source's Claim 2 (control over
    which external services an agent can access) with an actual
    enforcement mechanism.

- **Contradicts**: None requiring a new contradiction issue. This source
  is directly relevant to the open, unresolved contradiction in **issue
  #1625** ("MCP for production/enterprise integration: recommended
  standard vs. anti-pattern," Side A: `blog-anthropic-mcp-production-agents.md`
  Claim 4 "MCP is the recommended integration layer for production cloud
  agents" vs. Side B: `blog-thoughtworks-nonnenmacher-mcp-acl.md`, MCP as
  a universal-adapter anti-pattern). This source doesn't resolve #1625 —
  it adds a conditioning variable neither side of that contradiction
  states explicitly: whether the calling agent is a "full-blown terminal
  agent with unfettered internet access" (Willison's Claim 1 — MCP largely
  unnecessary here) or a constrained/multi-tenant/user-facing system
  (Willison's Claims 2-6 — MCP's value concentrates here). Per MINER.md
  §4a this reads as a conditioning variable, not a fresh contradiction, so
  no new issue was filed; the Assayer/Smith should consider citing this
  source when #1625 is resolved, since it suggests the "recommended vs.
  anti-pattern" framing itself may be the wrong axis. Separately, within
  this source's own linked context (not a corpus source-note conflict):
  the article Willison is rebutting, Maharshi Patel's "Why MCP Was Always
  a Bad Idea" (Claim 11 here), argues the opposite conclusion — that
  agents' growing CLI/API competency makes most MCP servers unnecessary —
  but scopes that argument to terminal-agent deployments, which is exactly
  the case Willison concedes in Claim 1. The two pieces mostly talk past
  each other rather than genuinely disagreeing on the constrained-agent
  case.

- **Extends**:
  - `blog-bswen-mcp-token-cost.md` (context-bloat measurements): Patel's
    article (Claim 11 area, "The MCP Industrial Complex" section, not
    separately extracted as a numbered claim here since Patel isn't the
    issue's source) names context bloat as a driver of the current
    anti-MCP backlash — the same problem Bswen measured concretely.
    Willison's rebuttal doesn't dispute the context-bloat cost; it argues
    the four listed benefits can be worth that cost for constrained
    deployments. Together the two notes frame context-bloat-vs-control as
    the real tradeoff, rather than "MCP good" vs. "MCP bad."
  - `docs-ghaw-mcp-gateway-reference.md` and `docs-ghaw-mcps.md`: gh-aw's
    actual gateway implementation (containerized isolation, guard
    policies, OIDC auth, OpenTelemetry) is a concrete, already-documented
    instantiation of exactly the four constraints Willison lists
    abstractly in this post.

- **Novel**:
  - The "full-blown terminal agent with unfettered internet access" vs.
    "less YOLO" framing (Claim 1) as the deciding variable for MCP
    adoption — no existing corpus note frames the MCP-vs-direct-API
    decision as a function of agent autonomy/network-access level rather
    than integration mechanics or organizational scale.
  - The "sensible UI to connect and authenticate services" constraint
    (Claim 4) — end-user-facing connection UX is not addressed by any
    existing MCP-and-auth note in the corpus, which focus on where
    credentials live rather than how a human grants access in the first
    place.
  - Willison's spec-vs-practice usage breakdown (Claim 8: Tools ~95%+,
    Resources/Prompts rarely used, Elicitation essentially unimplemented)
    — no existing source quantifies which parts of the MCP spec actually
    see real-world adoption.
  - The `agentfiles://` virtual-filesystem pattern (Claim 9) — a specific,
    named architecture for using MCP as a hard compartmentalization
    boundary between sandboxed coding agents and real cloud credentials,
    not documented elsewhere in the corpus.
  - The `Accept: text/markdown` / `Accept-Language` content-negotiation
    alternative to documentation MCP servers (Claim 12) — a distinct third
    option (neither "build an MCP server" nor "let the agent call the raw
    API") not documented anywhere else in the corpus.

## Guide Impact

- **Ch04 (Architecture & Design)**: The guide currently has an open,
  unresolved tension (issue #1625) between "MCP is the recommended
  integration layer" and "MCP is an anti-pattern for production
  integration." Recommend adding Willison's conditional framing as a
  clarifying axis once #1625 is resolved: the decision isn't MCP-good vs.
  MCP-bad in the abstract, it's whether the agent is a full-network
  terminal agent (skip MCP, call APIs/CLIs directly — Claim 1) or a
  constrained/multi-tenant/user-facing agent (MCP's value is access
  control + auth isolation + connection UI + audit logging — Claims 2-6),
  independent of whether the org considers itself "production."
- **Ch05 (Integration Patterns)**: Add the `agentfiles://` virtual
  filesystem pattern (Claim 9, Concrete Artifacts) as a worked example of
  "MCP as compartmentalization boundary" alongside the more abstract
  auth-isolation claim already in `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`.
  Also worth a short mention of the `Accept: text/markdown` /
  `Accept-Language` content-negotiation pattern (Claim 12) as an emerging
  lower-overhead alternative to documentation-serving MCP servers,
  flagged as `emerging` confidence pending a primary source.

## Extraction Notes

- The issue's source URL (`simonwillison.net/2026/Sep/20/hn-49779718/`) is
  a thin "Comment"-type blog entry — Willison's blog auto-publishes his
  own Hacker News comments. Read alone, it's one paragraph and four
  bullets with no elaboration. Per MINER.md §1, followed both linked
  pages: the Hacker News thread itself (`news.ycombinator.com/item?id=49779329`,
  330 comments — read the first ~40 comments in depth, not skimmed) and
  the article the thread discusses (`maharship.com/blog/why-mcp-was-always-a-bad-idea/`).
  Both were necessary to make sense of what Willison's four bullets are
  actually arguing against and what "the other things we might want to
  build" (Claim 7) refers to.
- Claims 8-12 are drawn from the linked HN thread and article rather than
  the blog post's own text. They're included because MINER.md instructs
  following substantive linked pages and extracting claims from them, and
  because the blog post's four-bullet list is too thin on its own to
  reach the 5-15 claim target with genuine depth. All are attributed by
  commenter handle and location so the Assayer can verify them against
  the live thread.
- Did not extract individual claims from every reply in the 330-comment
  thread — selected the replies that were direct responses to Willison's
  comment (prescriptivist, and Willison's own follow-up to kaoD) plus one
  adjacent sub-thread (socketcluster/anon84873628) that most sharply
  contests Willison's framing. A large fraction of the remaining thread is
  repetitive "MCP vs. Unix pipes" commentary that doesn't add claims
  beyond what's captured here.
- The Hacker News thread and the maharship.com article are both live and
  were fetched directly (not paywalled). No sub-pages beyond these two
  were followed — the MCP spec URL one commenter links
  (`modelcontextprotocol.io/specification/2026-07-28`) was not fetched
  since it's a protocol reference document already covered by
  `docs-ghaw-mcp-gateway-reference.md` and would not add claims specific
  to this issue's source.
