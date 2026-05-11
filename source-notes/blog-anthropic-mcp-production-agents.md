---
source_url: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
source_type: blog-post
title: "Building agents that reach production systems with MCP"
author: Anthropic (no individual byline)
date_published: 2026-04-22
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: settled
issue: "#349"
---

# Building agents that reach production systems with MCP

> First-party Anthropic post making the case for MCP as the standard integration
> layer for production cloud agents — contrasts three approaches (direct API calls,
> CLI, MCP), establishes five MCP server design principles, and documents two
> token-efficiency patterns (tool search, programmatic tool calling) with
> quantified reductions of 85%+ and ~37% respectively.

## Source Context

- **Type**: blog-post (official claude.com/blog, April 22, 2026; no individual
  byline — published as Anthropic)
- **Author credibility**: First-party Anthropic content on claude.com — the same
  publishing channel as "Multi-agent coordination patterns" and "Harnessing
  Claude's Intelligence." Represents Anthropic's recommended production practice
  for MCP integration. The download statistic (300M/month) is a verifiable
  adoption signal; the design principles and efficiency metrics are first-party
  Anthropic guidance.
- **Scope**: Covers how to connect agents to production systems using MCP —
  specifically the choice between three integration approaches, five design
  principles for MCP server authors, and two context-efficiency patterns for
  MCP clients. Does NOT cover MCP configuration for specific platforms (see
  `docs-ghaw-mcps.md`), pricing of MCP calls, multi-agent safety, or
  CLAUDE.md authoring. The post is addressed to developers building or exposing
  MCP servers, not just to practitioners consuming existing ones.

## Extracted Claims

### Claim 1: Agents are only as useful as the systems they can reach

- **Evidence**: Opening thesis of the post; frames the entire article.
- **Confidence**: settled (first-party framing; logically inescapable — an
  isolated agent that cannot read or write production state cannot perform
  production work)
- **Quote**: "Agents are only as useful as the systems they can reach."
- **Our assessment**: This is the most quotable single-sentence framing in the
  post and a useful anchor for Ch02 and Ch03. It reframes agent capability from
  "what can the model do?" to "what systems can it touch?" The practical
  implication: harness engineering is integration engineering first. Model
  intelligence is necessary but not sufficient.

### Claim 2: Direct API calls create an M×N integration problem — each agent–service pair requires bespoke auth handling, tool descriptions, and edge case management

- **Evidence**: First-party problem framing with a named failure pattern. The
  post describes agents calling APIs "either by writing code that issues HTTP
  requests inside a code-execution sandbox, or through a generic function-calling
  tool."
- **Confidence**: settled (structural problem description; M×N is a well-understood
  scaling failure mode in integration engineering)
- **Quote**: "With no common layer between agents and services, each agent–service
  pair becomes a bespoke integration with its own auth handling, tool descriptions,
  and edge cases—the M×N integration problem."
- **Our assessment**: The M×N framing is the motivation for the entire MCP
  ecosystem. Before MCP, each agent team had to solve auth, discovery, and
  semantic description for every external system independently. The cost scales
  quadratically: M agents × N services = M×N independent integration problems.
  MCP converts this to M+N: each service writes one MCP server; each agent
  writes one MCP client. This is the correct motivating framing for Ch02's
  coverage of external system integration.

### Claim 3: CLI-based integration hits hard limits with cloud-hosted platforms that don't expose a container

- **Evidence**: First-party description of CLI limitations. Described as "fast,
  lightweight, and leans on pre-existing tooling" but constrained.
- **Confidence**: settled (structural limitation — cloud-hosted platforms do not
  provide shell access to CI/production environments)
- **Quote**: "CLIs hit hard limits reaching mobile, web, or cloud-hosted platforms
  that don't expose a container."
- **Our assessment**: This is an important constraint for practitioners moving
  from local-development agent use (where CLI works well) to production cloud
  agent deployment. Claude Code CLI works in local development because the host
  environment provides a shell; production cloud agents running headlessly cannot
  rely on the same assumption. The CLI approach also has a credential problem
  (disk-based credentials work locally; cloud-hosted agents need programmatic
  auth). This claim explains why the guide's advice about MCP for production
  harnesses does not contradict the guide's advice about CLI tools for local
  development.

### Claim 4: MCP is the recommended integration layer for production cloud agents, providing authentication, discovery, and rich semantics as a standardized protocol

- **Evidence**: First-party recommendation. The post explicitly frames MCP as
  the solution to the M×N problem for cloud-scale production use.
- **Confidence**: settled (first-party Anthropic recommendation)
- **Quote**: "MCP provides the common layer as a protocol. The agent connects to
  a server that exposes your system's capabilities, with auth, discovery, and rich
  semantics standardized."
- **Quote (adoption signal)**: "The MCP SDKs recently surpassed 300 million
  downloads a month, up from 100 million at the start of the year, with strong
  adoption across enterprises and popular agentic platforms."
- **Our assessment**: The 300M/month download figure is a meaningful adoption
  signal — it shows MCP is not a niche protocol but an increasingly universal
  integration standard. The 3× growth in 2026 alone (100M to 300M by April)
  suggests the ecosystem is in rapid acceleration. For practitioners evaluating
  whether to build MCP integrations: the size of the MCP ecosystem directly
  reduces the bespoke-per-server cost. A service with an existing MCP server is
  immediately usable by any MCP-compatible agent without additional integration
  work.

### Claim 5: Build remote MCP servers (not local stdio servers) for production cloud agents that need to scale and operate continuously

- **Evidence**: First-party design guidance. The post notes "Production agents
  increasingly run in the cloud, so they can scale and operate continuously."
- **Confidence**: settled (first-party recommendation; logically follows from
  the cloud-agent deployment model)
- **Quote**: "Build remote servers so agents can use your system wherever they run."
- **Our assessment**: This is the key design choice separating development-time
  MCP use from production MCP use. Local stdio servers (e.g., the `uvx`-invoked
  Serena server in `docs-ghaw-mcps.md`) are appropriate for local developer
  workflows where the agent runs on the same machine. Production cloud agents
  — running in a managed harness, GitHub Actions, or a serverless environment —
  cannot invoke local processes. Remote HTTP-based MCP servers are the correct
  target architecture for any team deploying agents into production. This claim
  explains why the cloud-deployment pattern requires different MCP architecture
  than the local-development pattern.

### Claim 6: Group tools around user intent, not API endpoints — fewer, well-described tools outperform exhaustive API mirrors

- **Evidence**: First-party design principle.
- **Confidence**: settled (first-party guidance; consistent with tool design
  principles documented in `blog-anthropic-seeing-like-an-agent.md`)
- **Quote**: "Fewer, well-described tools consistently outperform exhaustive API
  mirrors."
- **Quote (mechanism)**: "group tools around intent, so the agent can accomplish
  a task in a couple of calls."
- **Our assessment**: This is the primary MCP server design principle in the post
  and the most actionable for practitioners building MCP servers. The intuition
  is: APIs are designed for programmatic clients that compose many small calls;
  MCP tools are designed for language model clients that reason about what they
  want to do. An API endpoint like `GET /repos/{owner}/{repo}/issues/{id}` is
  appropriate for a programmatic client; an MCP tool like `get_github_issue` with
  a description of what it returns is appropriate for an LLM. The principle
  "group around intent" means: design tools around the goals a user would
  express ("search for this Notion page"), not around the API operations that
  implement the goal ("call search_pages with query parameter"). This aligns
  with `blog-anthropic-seeing-like-an-agent.md`'s "see like an agent" principle
  — design tools the way the model reasons, not the way APIs expose.

### Claim 7: For services with hundreds of distinct operations, expose a thin "code orchestration" interface instead of intent-grouped tools — let the agent write scripts against a sandbox

- **Evidence**: First-party design guidance with named examples (Cloudflare, AWS,
  Kubernetes).
- **Confidence**: settled (first-party recommendation with concrete examples)
- **Quote**: "If your service requires hundreds of distinct operations, such as
  Cloudflare, AWS, or Kubernetes, an intent-grouped toolset likely won't cover it.
  Instead, expose a thin tool surface that accepts code: the agent writes a short
  script, your server runs it in a sandbox against your API, and only the result
  returns."
- **Our assessment**: This is the most novel design pattern in the post. For
  large-surface APIs, instead of trying to enumerate intent-groups (which would
  require hundreds of tools), expose one or two tools that accept arbitrary code
  and execute it sandboxed against the API. The agent writes the orchestration
  logic; the MCP server handles execution and security. This pattern is only
  viable when the MCP server can safely sandbox arbitrary code — which requires
  careful implementation. It is architecturally aligned with the "programmatic
  tool calling" efficiency pattern (Claim 12) and with the dynamic tool generation
  pattern documented in `blog-anthropic-claude-managed-agents.md` Claim 9 (where
  General Legal's agent codes up tools on the fly). The tradeoff: more agent
  flexibility at the cost of more server-side security burden.

### Claim 8: MCP Apps (interactive interfaces returned by tools) and elicitation (server-initiated user input mid-tool-call) are the first official protocol extensions enabling richer human-in-the-loop patterns

- **Evidence**: First-party protocol description. These are described as "official
  protocol extension[s]."
- **Confidence**: emerging (described as the "first" extension; protocol extensions
  are newer than the core protocol)
- **Quote (MCP Apps)**: "MCP Apps is the first official protocol extension and
  lets a tool return an interactive interface, such as a chart, form, or dashboard."
- **Quote (elicitation)**: "Elicitation lets your server pause mid-tool call to
  ask the user for input. Form mode sends a simple schema and the client renders
  a native form—use it to request a missing parameter, confirm a destructive
  action, or disambiguate options."
- **Our assessment**: These two extensions move MCP from a pure read/execute
  protocol toward a richer human-in-the-loop protocol. MCP Apps enables rich
  output (dashboards, forms) rather than only text/structured data returns.
  Elicitation enables confirmation gates and parameter disambiguation without
  requiring the agent to handle all input-gathering through the conversation.
  The "confirm a destructive action" use case for elicitation is particularly
  relevant for Ch03 (Safety and Verification): it provides a protocol-level
  mechanism for human approval of high-risk tool calls, distinct from the
  agent-level pattern of asking permission in conversation. For practitioners
  building MCP servers that expose write operations, elicitation is the
  correct protocol mechanism for approval gates — not agent-side prompting.

### Claim 9: Standardized OAuth with CIMD (Client ID Metadata Documents) makes MCP auth practical for cloud-hosted agents without manual client registration

- **Evidence**: First-party protocol description.
- **Confidence**: emerging (described as "the latest MCP spec" — this is a
  recent addition, not a foundational protocol feature)
- **Quote**: "Standardized auth makes MCP practical for cloud-hosted agents. If
  your server requires OAuth, the latest MCP spec supports CIMD (Client ID
  Metadata Documents) for client registration."
- **Our assessment**: CIMD is the MCP-native answer to the credential management
  problem for cloud agents. Without it, each OAuth-protected MCP server requires
  manual client registration, which doesn't scale when agents connect to many
  services. CIMD standardizes the registration flow so agents can authenticate
  dynamically without pre-registered credentials. This is complementary to the
  GitHub Actions OIDC pattern documented in `docs-ghaw-mcps.md` Claim 4 — OIDC
  is the right auth pattern for gh-aw-specific deployments; CIMD is the right
  pattern for general MCP-over-OAuth in production. For Ch02: document both auth
  patterns — OIDC for GitHub-hosted agents, CIMD for general cloud agents.

### Claim 10: Tool search defers loading all tool definitions into context and cuts tool-definition tokens by 85%+ while maintaining high selection accuracy

- **Evidence**: First-party quantified efficiency claim.
- **Confidence**: emerging (first-party claim with a specific metric; no
  methodology details or independent replication cited)
- **Quote**: "Tool search defers loading all tools into context, rather than
  loading them upfront...tool search tends to cut tool-definition tokens by 85%+
  while maintaining high selection accuracy."
- **Our assessment**: The 85%+ token reduction is the most striking quantitative
  claim in the post. The mechanism: instead of loading all tool definitions into
  the system prompt at session start, the agent issues a search to find relevant
  tools and loads only those. This directly addresses the problem documented in
  `blog-bswen-mcp-token-cost.md` (MCP tool definitions loaded upfront consume
  thousands of tokens per server before any work begins). The "high selection
  accuracy" qualifier is important — the pattern is only practical if the search
  mechanism reliably surfaces the right tools. For Ch04: tool search is the
  architectural solution to the MCP token cost problem, complementing the
  server-count pruning (`blog-bswen-mcp-token-cost.md` Claim 4) and the `allowed:`
  filter discipline (`docs-ghaw-mcps.md` Claim 3). Three levers in descending
  granularity: prune which servers you use → restrict which tools per server are
  allowed → defer loading tool definitions until needed via search.

### Claim 11: Programmatic tool calling — processing tool results in a code-execution sandbox rather than returning them raw — reduces token usage by roughly 37% on complex multi-step workflows

- **Evidence**: First-party quantified efficiency claim.
- **Confidence**: emerging (first-party claim with specific metric; no methodology
  details)
- **Quote**: "Programmatic tool calling processes tool results in a code-execution
  sandbox, rather than returning them raw to the model...reduces token usage by
  roughly 37% on complex multi-step workflows."
- **Our assessment**: This pattern is the MCP-server equivalent of the
  code-execution filtering pattern documented in `blog-anthropic-harnessing-claude-intelligence.md`
  Claim 3 — where giving the agent a REPL to filter its own tool outputs lifted
  BrowseComp from 45.3% to 61.6%. In the MCP context, the pattern means the agent
  writes code to process tool results (filter, aggregate, transform) in a sandbox
  before the processed result enters context, rather than returning the full raw
  result for the agent to reason about in text. For large API responses (e.g.,
  a GitHub search returning 50 issues with full metadata), this is a significant
  context saving. For Ch04: document programmatic tool calling as the
  "post-fetch" equivalent of tool search's "pre-fetch" optimization.

### Claim 12: Skills and MCP are complementary — MCP provides tool access to external systems, skills teach the procedural knowledge of how to use those tools effectively

- **Evidence**: First-party architectural principle.
- **Confidence**: settled (first-party definitional distinction)
- **Quote**: "Skills and MCP are complementary. MCP gives an agent access to
  tools and data from external systems, while skills teach an agent the procedural
  knowledge of how to use those tools to accomplish real work."
- **Our assessment**: This is the clearest first-party statement of the
  skills-vs-tools distinction for practitioners. Skills are not a substitute
  for MCP integration — they teach the workflow patterns on top of the tool access
  MCP provides. A practitioner who builds an MCP server for their CI system still
  needs a skill (or CLAUDE.md instructions) that teaches the agent how to use
  that server effectively for a given workflow. For Ch02: frame skills + MCP as
  the two-layer architecture — MCP is the data/action layer; skills are the
  knowledge layer on top of it.

## Concrete Artifacts

### Three Integration Approaches Comparison

```
# Integration approach comparison
# Source: "Building agents that reach production systems with MCP," Anthropic, April 22, 2026

DIRECT API CALLS
  Mechanism: Agent writes HTTP requests in code sandbox or uses generic function-calling tool
  Weakness:  M×N integration problem — each agent–service pair is bespoke (own auth, tool
             descriptions, edge cases)
  When OK:   Simple, one-off integrations; when no MCP server exists

CLI-BASED
  Mechanism: Agent runs command-line tools in a shell
  Strength:  Fast, lightweight, leverages existing tooling
  Weakness:  Hard limits with mobile, web, or cloud-hosted platforms that don't expose a container
             Relies on disk-based credentials (bad for cloud-hosted agents)
  When OK:   Local development workflows where agent runs on same machine as tools

MCP
  Mechanism: Agent connects to server exposing system capabilities via standardized protocol
  Strength:  Auth, discovery, and rich semantics standardized; solves M×N → M+N
  Downloads: 300M/month (April 2026), up from 100M at start of year
  When recommended: Production cloud agents
```

### MCP Server Design Principles

```
# Five design principles for MCP server authors
# Source: "Building agents that reach production systems with MCP," Anthropic, April 22, 2026

1. BUILD REMOTE SERVERS
   "Build remote servers so agents can use your system wherever they run."
   — Production agents run in cloud; local stdio servers don't reach them.

2. GROUP TOOLS AROUND INTENT
   "Fewer, well-described tools consistently outperform exhaustive API mirrors."
   "group tools around intent, so the agent can accomplish a task in a couple of calls."
   — Design for what users want to DO, not for what the API CAN DO.

3. DESIGN FOR CODE ORCHESTRATION (for large-surface APIs)
   "If your service requires hundreds of distinct operations, such as Cloudflare, AWS, or
   Kubernetes, an intent-grouped toolset likely won't cover it. Instead, expose a thin
   tool surface that accepts code: the agent writes a short script, your server runs it
   in a sandbox against your API, and only the result returns."

4. IMPLEMENT MCP APPS + ELICITATION (for interactive workflows)
   MCP Apps: "lets a tool return an interactive interface, such as a chart, form,
              or dashboard."
   Elicitation: "lets your server pause mid-tool call to ask the user for input.
                 Form mode sends a simple schema and the client renders a native
                 form—use it to request a missing parameter, confirm a destructive
                 action, or disambiguate options."

5. USE STANDARDIZED OAUTH/CIMD
   "Standardized auth makes MCP practical for cloud-hosted agents. If your server
   requires OAuth, the latest MCP spec supports CIMD (Client ID Metadata Documents)
   for client registration."
```

### MCP Client Token-Efficiency Patterns

```
# Two context-efficiency patterns for MCP clients
# Source: "Building agents that reach production systems with MCP," Anthropic, April 22, 2026

TOOL SEARCH (pre-fetch optimization)
  Mechanism: Defer loading all tool definitions upfront; search to find relevant tools
             at query time; load only selected tool definitions.
  Savings:   "tool search tends to cut tool-definition tokens by 85%+ while
              maintaining high selection accuracy"

PROGRAMMATIC TOOL CALLING (post-fetch optimization)
  Mechanism: Process tool results in a code-execution sandbox before returning to model,
             rather than returning raw results for in-context reasoning.
  Savings:   "reduces token usage by roughly 37% on complex multi-step workflows"

Combined: use both patterns for maximum context efficiency in MCP-heavy workflows.
```

### MCP Ecosystem Closing Principle

```
# Source: "Building agents that reach production systems with MCP," Anthropic, April 22, 2026

"Every integration built on MCP strengthens the ecosystem: fewer edge cases to solve alone,
fewer bespoke integrations to maintain."
```

## Cross-References

- **Corroborates**:
  - `blog-bswen-mcp-token-cost.md` Claim 1 ("Every MCP server loads all its tool
    definitions before you type anything"): the tool search pattern (Claim 10 here)
    is the first-party architectural solution to exactly the upfront-loading problem
    Bswen documented. Bswen measured the cost (85%+ of context budget in heavy
    configs); this post documents the fix (tool search defers loading). The two
    notes together form the complete problem-solution pair for the MCP token cost
    problem.
  - `blog-anthropic-harnessing-claude-intelligence.md` Claim 3 (code-execution
    filtering lifted BrowseComp from 45.3% to 61.6%): the programmatic tool calling
    pattern here (Claim 11, ~37% token reduction) is the MCP-server-side version
    of the same pattern. In `harnessing-claude-intelligence`, the agent uses a REPL
    to filter its own tool outputs. Here, the MCP server processes results in a
    sandbox before they return to the agent. Both patterns reduce the token cost
    of large tool responses via code-based filtering. Together they establish
    code-based result processing as a first-class context management pattern at
    both the harness level and the MCP server level.
  - `docs-ghaw-mcps.md` Claim 3 (the `allowed:` field restricts tool definitions
    loaded into context): the `allowed:` filter and the tool search pattern here
    are complementary approaches to the same goal — reduce the number of tool
    definitions the agent loads at any given time. The `allowed:` field prunes at
    the per-server level (only listed tools' definitions appear in the system
    prompt); tool search prunes at the session-start level (no tool definitions
    load upfront; only selected tools load at query time). Ch04 should document
    all three levers: server count pruning (Bswen), `allowed:` filter (gh-aw), and
    tool search (this post).
  - `blog-anthropic-seeing-like-an-agent.md` Claim 1 and the "see like an agent"
    meta-principle: the "group tools around intent, not endpoints" principle here
    (Claim 6) is the MCP-server application of the same design philosophy. Thariq
    Shihipar's post documents the principle for tool design in Claude Code; this
    post applies it to MCP server design. Both sources agree: tool design should
    match how the model reasons about tasks, not how the underlying API exposes
    operations.
  - `blog-anthropic-claude-managed-agents.md` Claim 9 (dynamic tool generation —
    the agent codes up new tools on the fly): the code orchestration pattern here
    (Claim 7) is the MCP-server-side architecture that enables this behavior.
    General Legal's agent "codes up any tool it needs on the fly" because the
    underlying harness exposes a sandboxed code execution surface — precisely the
    pattern this post recommends for large-surface APIs ("expose a thin tool
    surface that accepts code").
  - `blog-anthropic-claude-managed-agents.md` Claim 11 (Blockit's integration
    pattern): the Blockit testimonial explicitly confirms the pattern this post
    recommends — "MCP made it simple to connect external systems like meeting
    notetakers, CRMs, etc." Blockit used MCP for external systems and custom
    tools for proprietary data, the two-layer architecture Claim 12 here describes.

- **Extends**:
  - `docs-ghaw-mcps.md`: That note covers MCP *configuration* in the gh-aw platform
    (how to wire up servers to workflows). This post covers MCP *server design*
    (how to build servers that agents can use effectively). Together they give the
    complete picture: design good servers (this post), then configure them correctly
    (gh-aw docs). The remote server recommendation here (Claim 5) explains why gh-aw
    supports HTTP MCP server types as first-class citizens alongside local stdio.
  - `blog-bswen-mcp-token-cost.md`: Bswen documents the problem (token cost of
    upfront tool loading) and a server-count mitigation. This post adds two
    architectural solutions: tool search (pre-fetch deferral) and programmatic tool
    calling (post-fetch processing). Together, the corpus now has a three-layer
    mitigation strategy for MCP token overhead.
  - `blog-anthropic-harnessing-claude-intelligence.md` Claim 13 (tool search
    enables dynamic tool discovery without breaking cache): that note documents
    tool search as a *cache-preservation* mechanism. This post documents it as a
    *token-reduction* mechanism (85%+ cut). The two benefits are additive and
    complementary — tool search is both cache-preserving and context-efficient.
    Together they make a strong case for tool search as the default pattern for
    MCP-heavy harnesses.

- **Contradicts**: None identified. The remote-server recommendation here (Claim 5)
  does not contradict `docs-ghaw-mcps.md`'s coverage of stdio and Docker container
  servers — those apply to gh-aw's specific runner environment, while this post
  addresses general production cloud agent deployment. The difference is a
  conditioning variable (platform-specific vs. general), not a contradiction.

- **Novel**:
  - **M×N integration problem named**: No prior corpus source frames the motivation
    for MCP using the M×N → M+N reduction. This is the most concise and principled
    statement of why MCP exists.
  - **Remote-vs-local MCP server distinction**: No prior corpus source explicitly
    states "build remote servers" as the production design principle. Docs-ghaw-mcps
    covers four server types for a specific platform; this post establishes the
    general recommendation for production cloud agents.
  - **Code orchestration pattern**: The "expose a thin tool surface that accepts
    code" pattern for large-surface APIs (Cloudflare, AWS, Kubernetes) is new to
    the corpus. No prior source describes delegating API orchestration logic to
    agent-written code executed in a server-side sandbox.
  - **MCP Apps and elicitation as protocol extensions**: These are the first
    documented official MCP protocol extensions in our corpus. Elicitation's
    "confirm a destructive action" use case is a new protocol-level safety
    primitive not documented in any other source note.
  - **CIMD for dynamic client registration**: The CIMD OAuth extension is new to
    the corpus as a cloud agent authentication mechanism.
  - **85%+ and ~37% token reduction metrics**: The specific efficiency claims for
    tool search and programmatic tool calling are quantified here for the first
    time in the corpus. Bswen documented the token cost problem with measurements;
    this post documents the solution with efficiency metrics.
  - **Skills + MCP two-layer architecture**: The explicit framing — MCP as data/
    action layer, skills as procedural knowledge layer on top — is stated precisely
    here for the first time. Both elements existed in prior notes but the
    complementary two-layer architecture was not named.
  - **MCP ecosystem network effects**: "Every integration built on MCP strengthens
    the ecosystem: fewer edge cases to solve alone, fewer bespoke integrations to
    maintain." The ecosystem-strengthening framing as a reason to adopt MCP is new
    to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the M×N → M+N framing (Claim 2) as
  the canonical motivation for MCP in production harnesses. Currently the guide
  lacks a principled justification for choosing MCP over direct API calls; this
  post provides it. Also add the three-approach decision framework (Claims 2-4)
  as a decision table: direct API calls for simple one-offs, CLI for local
  development, MCP for production cloud agents.

- **Chapter 02 (Harness Engineering)**: Add the remote-vs-local MCP server
  distinction (Claim 5) as an explicit design requirement for production deployments.
  Practitioners moving from local Claude Code workflows (where stdio MCP servers
  work fine) to cloud-deployed agents must understand that their server architecture
  must change — not just their configuration.

- **Chapter 02 (Harness Engineering)**: Document the Skills + MCP two-layer
  architecture (Claim 12) explicitly: MCP is the integration layer (what can the
  agent touch?); skills are the knowledge layer (how should it use those tools?).
  This frames the two-layer design as a first-class architectural pattern, not an
  incidental combination.

- **Chapter 03 (Safety and Verification)**: Add elicitation (Claim 8) as a
  protocol-level safety primitive for write-capable MCP servers. For any MCP tool
  that performs destructive operations, the "confirm a destructive action" elicitation
  pattern provides a human-approval gate at the protocol level — complementary to
  Safe Outputs (for gh-aw) and agent-level approval-seeking (for general harnesses).

- **Chapter 04 (Context Engineering / Tool Choice)**: Add the three-lever MCP
  token management framework, citing all three sources:
  1. Server count pruning (3-6 essential servers) — `blog-bswen-mcp-token-cost.md` Claim 4
  2. Per-server tool filtering (`allowed:` field) — `docs-ghaw-mcps.md` Claim 3
  3. Tool search (85%+ upfront token reduction) — Claim 10 here
  Also add programmatic tool calling (Claim 11, ~37% reduction on complex workflows)
  as the post-fetch complement to tool search's pre-fetch optimization.

- **Chapter 04 (Context Engineering)**: Tool search (Claim 10) should be cited
  alongside `blog-anthropic-harnessing-claude-intelligence.md` Claim 13 to give
  both the cache-preservation benefit and the token-reduction benefit. Tool search
  is a dual-purpose pattern: it defers loading tool definitions (saving upfront
  tokens) AND avoids busting the cache by keeping the tool list in the cached
  prefix stable. The two benefits together make a strong case for tool search as
  the default for any MCP-heavy harness.

- **Chapter N (MCP Server Design)** — if such a chapter or section exists or is
  planned: The five design principles (Claims 5-9) are a complete first-party
  framework for practitioners building MCP servers. The "group around intent"
  principle (Claim 6), the code orchestration pattern (Claim 7), and MCP Apps +
  elicitation (Claim 8) together cover the range from small-surface to
  large-surface to interactive server designs.

## Extraction Notes

1. **No individual byline**: The post is published on claude.com/blog with no
   named author. Treated as first-party Anthropic guidance with the same authority
   as other Anthropic blog posts on this channel.

2. **WebFetch returns summarized content**: The claude.com blog is a JavaScript-
   rendered SPA. WebFetch AI-summarizes the rendered content. Three separate fetches
   were performed with targeted prompts to maximize verbatim quote fidelity. All
   quotes in this note were extracted from WebFetch responses and compared across
   fetches for consistency. The efficiency metrics (85%+, ~37%) appeared consistently
   across all fetches and are treated as accurate.

3. **Protocol extension maturity**: MCP Apps and elicitation are described as "the
   first official protocol extension" — this phrasing suggests they are relatively
   new additions to the MCP spec. The `emerging` confidence assigned to Claim 8
   reflects this maturity uncertainty. Practitioners should verify current spec
   status before implementing.

4. **CIMD maturity**: Similarly described as "the latest MCP spec" feature, indicating
   recent addition. Assigned `emerging` confidence in Claim 9.

5. **No tool search methodology details**: The 85%+ figure comes without methodology
   details — what workload, how many tools, what selection mechanism. Treat as a
   directional signal, not a precise measurement. The "high selection accuracy" qualifier
   is also unquantified.

6. **Code orchestration examples (Cloudflare, AWS, Kubernetes)** are named but not
   linked to specific existing MCP server implementations. These are illustrative examples
   of the pattern, not endorsements of specific servers.

7. **No contradictions to file**: Reviewed all existing source notes covering MCP
   (docs-ghaw-mcps, blog-bswen-mcp-token-cost, blog-anthropic-claude-managed-agents).
   The remote-server vs. local-server difference between this post and docs-ghaw-mcps
   is a conditioning variable (production cloud vs. gh-aw platform-specific), not a
   contradiction. No contradiction issue filed.
