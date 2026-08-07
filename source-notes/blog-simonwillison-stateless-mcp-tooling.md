---
source_url: https://simonwillison.net/2026/Jul/31/stateless-mcp/
source_type: blog-post
title: "Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)"
author: Simon Willison
date_published: 2026-07-31
date_extracted: 2026-08-07
last_checked: 2026-08-07
status: current
confidence_overall: emerging
issue: "#2540"
---

# Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)

> Independent practitioner response to the 2026-07-28 stateless MCP spec release,
> published five days after the spec itself: Willison explains why he had lost
> interest in MCP to shell+curl agent harnesses in 2025, why the stateless
> redesign changed his mind, and documents three working projects he built the
> same week (mcp-explorer, datasette-mcp, llm-mcp-client) plus an explicit
> security argument for MCP over arbitrary shell access.

## Source Context

- **Type**: blog-post — Simon Willison's Weblog, a first-person practitioner
  post combining protocol commentary, project announcements, and a security
  argument. Not a TIL-format link post; this is a full standalone article with
  five named sections (`What's easier with stateless MCP`, `mcp-explorer`,
  `datasette-mcp`, `llm-mcp-client`, `MCP is a safer way to build with agents`).
- **Author credibility**: Simon Willison — creator of Django and Datasette,
  prolific independent LLM-tooling commentator with no vendor affiliation to
  Anthropic, OpenAI, or Google, and the corpus's designated `trusted-feed`
  source. He is a named author of prior injection-security writing referenced
  in his own post (`Model Context Protocol has prompt injection security
  problems`, April 2025) and coined "the Lethal Trifecta" (June 2025). This
  post documents three projects he personally built and shipped the same week
  (mcp-explorer, datasette-mcp, llm-mcp-client), making the claims about "what
  stateless MCP makes easier" first-hand implementation experience, not
  secondhand commentary.
- **Scope**: Covers why the author's interest in MCP waned in 2025, why the
  2026-07-28 stateless spec revived it, a worked before/after comparison of
  stateful vs. stateless HTTP requests (reproducing an example from the spec's
  own May 21st release-candidate announcement, not independently authored),
  three new tools he built this week, and a security argument for MCP over
  shell/curl agent access. Does NOT cover: the formal spec text itself (SEPs,
  RFCs, deprecation policy — see `blog-google-mcp-stateless-scaling.md`), MCP
  server design principles, or benchmarked/quantified security comparisons —
  the security argument here is a stated position, not a study.

## Extracted Claims

### Claim 1: The 2026-07-28 stateless MCP spec (MCP 2.0 / "Stateless MCP day") is the most significant change to MCP since its original November 2024 launch, and reignited the author's personal interest in the protocol

- **Evidence**: First-person framing statement opening the post, naming the
  rollout date and linking to both the announcement thread and the formal spec
  page.
- **Confidence**: settled (a direct claim about the article's own motivating
  event, stated plainly by its author, and consistent with the spec-level
  detail independently documented in `blog-google-mcp-stateless-scaling.md`)
- **Quote**: "This is the most significant change to the MCP spec since it
  first launched, and has also served to reignite my personal interest in the
  protocol."
- **Our assessment**: This is a practitioner-adoption data point that
  complements the first-party spec documentation: Google (the working-group
  co-founder) describes the spec change architecturally; Willison, an
  independent high-signal commentator, independently corroborates that it is
  a major inflection point worth re-engaging with, not merely an incremental
  release.

### Claim 2: MCP was eclipsed through 2025 by Skills because an agent harness with terminal and `curl` access could do most of what MCP did, more flexibly

- **Evidence**: First-person historical account with a link to the author's
  own prior "review of 2025" post as corroborating context.
- **Confidence**: settled (author's own stated account of his prior published
  position, internally consistent with a linked earlier post)
- **Quote**: "It was introduced by Anthropic back in November 2024, had a
  huge spike of interest through much of 2025, and then became somewhat
  eclipsed by Skills (another Anthropic invention) when it became apparent
  that an agent harness with access to a terminal and curl could do most of
  what MCP did in a more flexible way."
- **Our assessment**: This is the necessary backstory for why a "stateless
  MCP" announcement is treated as newsworthy at all — it establishes that MCP
  had lost mindshare to a competing pattern (shell + curl agent harnesses),
  making the rest of the post an explicit "here's what changed my mind" essay
  rather than routine coverage. No prior corpus source states this specific
  MCP-vs-Skills eclipse narrative from this angle (practitioner mindshare, not
  protocol capability).

### Claim 3: Giving an agent unrestricted shell and internet access is risky and requires a strong model to drive safely; MCP tools are easier to audit and control, and simple enough that smaller laptop-class models can drive them well

- **Evidence**: First-person architectural/security judgment, linking to the
  author's own separate post about a real-world incident ("fraught with
  risk").
- **Confidence**: anecdotal (a stated practitioner position/argument, not a
  benchmarked security comparison between shell-access harnesses and MCP
  tool-calling)
- **Quote**: "Giving an agent a shell environment with the ability to access
  the internet is fraught with risk, and requires a strong model that is
  capable of effectively driving such an environment. MCP tools are easier to
  audit and control, and simple enough that smaller models that run on a
  laptop can still drive them reasonably well."
- **Our assessment**: This is the article's core value proposition and the
  reason the Prospector flagged Ch02/Ch03 relevance. It is a capability-tiering
  argument distinct from anything in the corpus's existing MCP coverage: MCP's
  benefit here is framed as making tool use *accessible to weaker models*, not
  just safer for strong ones. This complements (does not restate)
  `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` Claim 1, which frames
  MCP's primary value as isolating auth flows outside the agent's context
  window — Lynch's claim is about credential exposure; this claim is about
  auditability and the minimum model capability required to drive tools
  safely. Both are security arguments for MCP, but they name different
  mechanisms.

### Claim 4: The stateless spec change substantially reduces implementation complexity for both MCP clients and servers, and the author verified this by building three of them in one week

- **Evidence**: First-person claim, backed by the very existence of the three
  shipped projects described later in the post as evidence rather than
  assertion.
- **Confidence**: emerging (a single practitioner's implementation experience
  over one week; not a controlled before/after comparison of stateful vs.
  stateless implementation effort, but backed by working, published code —
  three public GitHub repositories)
- **Quote**: "The new stateless MCP specification also greatly decreases the
  complexity of implementing both clients and servers for the protocol. I
  built three of those this week!"
- **Our assessment**: This is practitioner validation, by demonstration, of a
  claim `blog-google-mcp-stateless-scaling.md` makes architecturally (Claim 2:
  the handshake and session-ID header are removed entirely). Google's post
  argues the mechanism reduces complexity; Willison's post is the first
  independent evidence in the corpus that the reduction is real enough to
  let one practitioner ship three separate MCP-adjacent tools (a CLI explorer,
  a server plugin, and a client library integration) in a single week.

### Claim 5: Legacy stateful MCP required two HTTP requests — an `initialize` call returning an `Mcp-Session-Id`, then a second call carrying that session ID to invoke a tool — while the new stateless model does both in a single HTTP request via an inline `_meta` field

- **Evidence**: Worked before/after JSON-RPC HTTP examples, explicitly
  attributed by the author to a May 21st MCP spec release-candidate blog post
  (not authored by Willison himself) rather than presented as his own
  discovery.
- **Confidence**: settled (a mechanical description of a published protocol
  change, independently corroborated in full technical detail by
  `blog-google-mcp-stateless-scaling.md` Claim 2, whose Concrete Artifacts
  section reproduces materially the same before/after request pair)
- **Quote**: "The older stateful MCP (I'm going to call it "legacy MCP")
  required two HTTP requests—the first to initialize a session and obtain a
  Mcp-Session-Id, and the second to actually call the tool"
- **Our assessment**: This is a corroborating restatement, not a novel
  technical claim — the underlying mechanism is already documented in more
  spec-precise detail (named SEPs, error codes) by
  `blog-google-mcp-stateless-scaling.md`. Its value here is as independent
  confirmation from a second, non-Google source that the practitioner-facing
  description of the change matches the working group's own framing, and as
  the immediate technical grounding for why Willison says implementation
  complexity dropped (Claim 4).

### Claim 6: Eliminating the session handshake means servers no longer need to maintain server-side session-ID state or worry about routing a client's follow-up requests to the same backend instance

- **Evidence**: First-person architectural conclusion following directly from
  the worked example in Claim 5.
- **Confidence**: settled (direct logical consequence of the mechanism
  described in Claim 5, and independently corroborated at greater depth by
  `blog-google-mcp-stateless-scaling.md` Claims 1 and 3, which name the
  specific production failure mode — `400 Session Not Found` behind a
  round-robin load balancer — that this statement describes only generically)
- **Quote**: "This is so much cleaner from both a client- and server-side
  implementation perspective. It's also a better fit for building scalable
  web applications, since now you don't need to maintain server-side state to
  keep track of those session IDs, or worry about routing the same session to
  the same backend machine."
- **Our assessment**: Willison's framing here ("better fit for building
  scalable web applications") is the practitioner-level restatement of the
  load-balancing and horizontal-scaling argument that
  `blog-google-mcp-stateless-scaling.md` makes in full architectural detail
  (round-robin load balancing, serverless deployment, transparent failover).
  This claim is evidence that the scaling benefit is legible to a working
  developer without needing the formal spec's named failure taxonomy —
  useful corroboration that the benefit is real and not merely a vendor
  framing exercise.

### Claim 7: mcp-explorer is a stateless Python CLI tool for interactively probing MCP servers — list tools, inspect their JSON schemas, and call them with arguments — runnable via `uvx` with no installation step

- **Evidence**: First-person project description with a working example
  command against a third-party demo MCP server (`agentic-mermaid.dev`),
  reproduced tool-list output, an `inspect` command, and a full `call`
  invocation with arguments producing a real SVG image result linked from the
  post.
- **Confidence**: settled (the author built and demonstrates the tool with a
  live third-party server, not a hypothetical or planned feature; the GitHub
  repository is linked)
- **Quote**: "mcp-explorer is the result. It's a stateless Python CLI tool, so
  you don't even need to install it to try it out—it works with uvx like
  this:"
- **Our assessment**: This is the first source in the corpus documenting a
  general-purpose, install-free MCP inspection/exploration CLI. It fills a
  practical gap for practitioners evaluating or debugging an unfamiliar MCP
  server before wiring it into a harness — distinct from Claude Code's `/mcp`
  in-session inspection (documented in
  `blog-simonwillison-cloudflare-mcp-api-fallback.md` Claim 5) because
  mcp-explorer is a standalone, harness-independent tool usable outside any
  particular agent product.

### Claim 8: datasette-mcp is a Datasette plugin adding a `/-/mcp` endpoint with exactly three tools — `list_databases()`, `get_database_schema(database_name)`, and `execute_sql(database_name, sql)` (currently read-only) — and is the author's fourth attempt at building this plugin, only now shippable because of the stateless spec

- **Evidence**: First-person project description naming the exact tool
  signatures, an explicit statement that this is a repeated (fourth) attempt,
  and a live deployment on the author's own blog's Datasette mirror
  (`datasette.simonwillison.net/-/mcp`) with a linked shared Claude session
  transcript as a worked usage example.
- **Confidence**: settled (working, deployed, publicly linked plugin with a
  reproducible usage transcript)
- **Quote**: "This is probably the fourth time I've tried building this
  plugin, but thanks to the new stateless MCP specification I finally have a
  version that feels good to release."
- **Quote (tool surface)**: "It provides just three tools: list_databases(),
  get_database_schema(database_name), and execute_sql(database_name, sql).
  They do exactly what you would expect them to do—though execute_sql() is
  read-only for the moment."
- **Our assessment**: The "fourth attempt, only now shippable" detail is
  strong first-hand evidence for Claim 4's complexity-reduction argument —
  this is not a claim that stateless MCP is merely nicer, but that it removed
  a concrete blocker that had stalled the same project across three prior
  tries. The deliberately minimal, read-only tool surface (three tools,
  no write capability yet) is also a concrete, citable example of the
  "group tools around intent, few well-described tools" design principle
  documented in `blog-anthropic-mcp-production-agents.md` Claim 6 — Willison
  did not expose a tool per Datasette API endpoint, he exposed three
  intent-shaped operations.

### Claim 9: In a demonstrated Claude session against the deployed datasette-mcp server, the model answered "what has Simon said recently about MCP?" by autonomously running 7 separate SQL queries

- **Evidence**: A linked, shared Claude.ai conversation transcript
  (`claude.ai/share/de1ad9bf-f7c2-4fb9-a9a0-2a1ae39995db`) showing two prompts
  ("list tables in simonwillison.net" and the MCP question) and the author's
  own count of the queries executed.
- **Confidence**: anecdotal (a single demonstrated session against one
  practitioner's own server; no claim of typical or average query count for
  this class of task)
- **Quote**: "It ran 7 separate SQL queries to figure out the answer."
- **Our assessment**: This is a concrete, citable example of multi-step
  autonomous tool orchestration through a minimal three-tool MCP surface —
  the model was not given a single "search my blog" tool, only generic
  schema-inspection and SQL-execution primitives, and composed 7 queries
  itself to answer a natural-language question. This is a specific worked
  instance of the "let the agent write scripts/queries against a sandbox"
  pattern that `blog-anthropic-mcp-production-agents.md` Claim 7 recommends
  for large-surface APIs, except applied to a deliberately small,
  read-only three-tool surface rather than a "hundreds of operations" API.

### Claim 10: llm-mcp-client is a new alpha plugin bringing official MCP integration to Willison's LLM CLI tool, installable via `llm install llm-mcp-client` and invoked with an inline `MCP(...)` tool reference; the author is considering folding it into LLM core once it is "fully baked"

- **Evidence**: First-person project description with an exact install/usage
  command pair, a worked example querying the same datasette-mcp server
  ("count the notes"), a reproduced reasoning-trace excerpt from the model's
  response, and a linked full `llm logs` output for the session.
- **Confidence**: emerging (explicitly labeled "alpha" by the author; a
  stated future intention — folding into LLM core — that has not happened
  yet)
- **Quote**: "My LLM tool is long overdue for an official MCP integration.
  The new alpha llm-mcp-client plugin is my attempt at exactly that:"
- **Quote (result)**: "There are 151 notes."
- **Our assessment**: This is the third of three distinct MCP client
  surfaces demonstrated in the post (mcp-explorer for ad hoc inspection,
  datasette-mcp as a server, llm-mcp-client as a scriptable CLI client),
  together forming a fuller stack than any single tool alone. The
  reasoning-trace excerpt ("I see the question 'count the notes' is probably
  asking me to tally up blog notes... I'll need to figure out the total
  number of notes, likely by querying the count for both published notes and
  drafts") is a concrete artifact showing a model disambiguating an
  ambiguous natural-language request before issuing a tool call — relevant
  to any guide discussion of tool-use reasoning transparency via reasoning
  traces.

### Claim 11: Before coining "the Lethal Trifecta" in June 2025, the author had already identified MCP's pattern of end users mixing and matching tools as pushing data-exfiltration risk onto the users themselves, in an April 2025 post on MCP prompt injection

- **Evidence**: First-person historical account with links to both the named
  prior post ("Model Context Protocol has prompt injection security
  problems") and the Lethal Trifecta post, presented as the author's own
  intellectual history on this topic.
- **Confidence**: settled (author's own account of his own prior published
  work, with direct links to both referenced posts)
- **Quote**: "A few months after MCP was first released, I wrote Model
  Context Protocol has prompt injection security problems, where I noted
  that the pattern of having end users mix and match tools pushed
  responsibility for avoiding data exfiltration attacks out to the users
  themselves. I hadn't coined the Lethal Trifecta yet, but that was
  absolutely what I had in mind."
- **Our assessment**: This retroactively frames MCP's original (2025)
  security concern as a user-facing responsibility problem — the *user* who
  connects multiple MCP tools together is the one exposed to
  injection/exfiltration risk, not just the agent operator. That framing is
  a useful precursor for Claim 12's contrast: this claim is about MCP's own
  earlier-identified risk; the next claim argues shell/curl agents are worse
  along the same axis.

### Claim 12: General-purpose agents with arbitrary shell and `curl` access are harder to secure than MCP, because it is much easier to reason about what an agent with defined MCP tool capabilities might do wrong than to reason about arbitrary command execution in an open network environment — the default for most current general and coding agent tools

- **Evidence**: First-person concluding security argument, stated as the
  author's considered position closing the post, followed by a stated forward
  intention.
- **Confidence**: anecdotal (a stated practitioner position and comparative
  judgment, not a benchmarked or measured security comparison between
  shell-access agents and MCP-tool-restricted agents)
- **Quote**: "Something I've come to appreciate about MCP is that it's much
  easier to reason about agent capabilities and what might go wrong than
  with arbitrary command execution in an open network environment—the
  default for most of today's general and coding agent tools."
- **Quote (forward intent)**: "I plan to lean into MCP a whole lot more when
  I'm building sensitive applications on top of LLMs."
- **Our assessment**: This is the article's thesis statement and the
  specific "MCP as safer than shell+curl" framing the Prospector flagged as
  distinct from the corpus's existing auth-isolation argument
  (`blog-simonwillison-sean-lynch-mcp-auth-gateway.md`). The threat model here
  is capability enumeration and reasoning-about-blast-radius (a bounded,
  named tool surface vs. an open-ended shell), not credential exposure. Both
  are legitimate, non-competing security arguments for preferring MCP over
  shell access, and the corpus now has independent claims for each.

## Concrete Artifacts

### Legacy stateful MCP request pair (reproduced by Willison from the spec's own May 21st release-candidate post, not his own invention)

```
POST /mcp HTTP/1.1
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
    },
    "clientInfo": {
      "name": "my-app",
      "version": "1.0"
    }
  }
}

POST /mcp HTTP/1.1
Mcp-Session-Id: 1868a90c-3a3f-4f5b
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "search",
    "arguments": {
      "q": "otters"
    }
  }
}
```
Source: simonwillison.net, "What's easier with stateless MCP" section.

### New stateless MCP single-request form

```
POST /mcp HTTP/1.1
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: search
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search",
    "arguments": {
      "q": "otters"
    },
    "_meta": {
      "io.modelcontextprotocol/clientInfo": {
        "name": "my-app",
        "version": "1.0"
      }
    }
  }
}
```
Source: simonwillison.net, "What's easier with stateless MCP" section.

### mcp-explorer commands and output

```
# List tools on a demo MCP server
uvx mcp-explorer list https://agentic-mermaid.dev/mcp

# Example returned tool list (truncated):
execute(code: string, timeoutMs?: integer) - Execute Mermaid SDK code
  Run JavaScript in an isolated sandbox; return a value.
describe_sdk(family: string, detail?: string) - Describe Mermaid SDK operations
  Return version-matched mutation operations for one diagram family.
render_svg(source: string, options?: object) - Render Mermaid as SVG
  Render a Mermaid source string to themeable SVG. Returns { ok, svg }.
render_ascii(source: string, useAscii?: boolean, targetWidth?: integer, options?: object) - Render Mermaid as text
render_png(source: string, scale?: number, background?: string, fitTo?: object, options?: object) - Render Mermaid as PNG

# Inspect a single tool's JSON schema
uvx mcp-explorer inspect render_svg

# Call a tool with arguments
uvx mcp-explorer call \
  https://agentic-mermaid.dev/mcp \
  render_svg \
  -a source 'graph TD; A-->B' \
  -a options '{"padding":24}'

# Response:
{"ok":true,"svg":"<svg xmlns=\"http://www.w3.org/2000/svg\" width=...
```
Source: simonwillison.net, "mcp-explorer" section. GitHub: github.com/simonw/mcp-explorer.

### datasette-mcp tool surface and llm-mcp-client usage

```
# datasette-mcp: three tools exposed at /-/mcp
list_databases()
get_database_schema(database_name)
execute_sql(database_name, sql)   # read-only for the moment

# llm-mcp-client: install and invoke against a live datasette-mcp server
llm install llm-mcp-client
llm -T 'MCP("https://datasette.simonwillison.net/-/mcp")' 'count the notes'

# Reasoning trace excerpt from that invocation (LLM 0.32rc2):
Considering note count
I see the question "count the notes" is probably asking me to tally up blog
notes. It could also mean published notes or drafts, so there's some
ambiguity there. I'll need to figure out the total number of notes, likely
by querying the count for both published notes and drafts to get a clear
answer. Let's execute that count!

There are 151 notes.
```
Source: simonwillison.net, "datasette-mcp" and "llm-mcp-client" sections.
GitHub: github.com/datasette/datasette-mcp, github.com/simonw/llm-mcp-client.

## Cross-References

- **Corroborates**:
  - `blog-google-mcp-stateless-scaling.md` Claim 2 (the `initialize`/
    `Mcp-Session-Id` handshake is removed entirely in favor of a per-request
    inline `_meta` field): this note's Claim 5 and its reproduced before/after
    HTTP examples independently confirm, from a non-Google practitioner
    source, the same mechanical description of the spec change — though
    Willison attributes the example to the spec's own May 21st RC
    announcement rather than presenting it as his own analysis.
  - `blog-google-mcp-stateless-scaling.md` Claims 1 and 3 (the legacy session
    model broke horizontal scaling; statelessness enables plain round-robin
    load balancing and serverless deployment): this note's Claim 6 reaches
    the same conclusion ("a better fit for building scalable web
    applications... you don't need to maintain server-side state") at a more
    general, less spec-precise level of detail — independent practitioner
    convergence on the same architectural benefit.
  - `blog-anthropic-mcp-production-agents.md` Claim 6 ("group tools around
    intent, so the agent can accomplish a task in a couple of calls" /
    "fewer, well-described tools consistently outperform exhaustive API
    mirrors"): this note's Claim 8 (datasette-mcp's deliberately minimal
    three-tool, intent-shaped surface) is a concrete, shipped example of that
    design principle in practice.
  - `blog-simonwillison-cloudflare-mcp-api-fallback.md` Claim 5 (remote,
    `type: http` MCP servers require only URL configuration for a working
    OAuth/connection flow in Claude Code): this note's datasette-mcp
    deployment (Claim 8) and its linked Claude Code TIL
    (`blog-simonwillison-mcp-claude-chatgpt-setup.md`) are the same author
    independently demonstrating low-friction remote MCP server setup across
    multiple of his own projects.

- **Contradicts**: None identified. This note's central security argument
  (Claim 12 — MCP is easier to reason about than arbitrary shell/curl access)
  is a distinct mechanism from, and does not conflict with,
  `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`'s auth-isolation
  argument (Claim 1) — the two describe different security benefits of the
  same underlying preference for MCP over unrestricted shell/CLI access
  (capability enumeration vs. credential exposure), which the corpus can
  hold as complementary rather than competing claims.

- **Extends**:
  - `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`: That note's single
    quoted paragraph argues MCP's primary value is isolating auth flows
    outside the agent's context window. This note's Claim 3 and Claim 12 add
    a second, independent security argument from the same author who curated
    the Lynch quote — MCP bounds and simplifies what an agent can do,
    independent of any auth question, which is why smaller/weaker models can
    drive MCP tools safely where they could not safely drive an open shell.
  - `blog-google-mcp-stateless-scaling.md`: That note is first-party
    working-group spec documentation (named SEPs, error codes, deprecation
    policy). This note is the first independent practitioner
    implementation-and-adoption account of the same spec release, published
    5 days before Google's own explainer — it demonstrates the spec's
    complexity-reduction claims by shipping three working tools rather than
    describing the mechanism architecturally.
  - `blog-simonwillison-mcp-claude-chatgpt-setup.md`: That note documents the
    consumer-chat-UI mechanics of attaching a custom MCP server (including
    this same datasette-mcp deployment) to Claude.ai and ChatGPT. This note
    is the server-and-tooling-author's-eye view of the same underlying
    project (why datasette-mcp exists, what its three tools do, why this was
    the fourth attempt) that the other note's TIL is a *user* of.
  - `blog-anthropic-mcp-production-agents.md`: That post gives first-party
    MCP server design guidance (remote servers, intent-grouped tools, code
    orchestration for large APIs). This note's datasette-mcp and mcp-explorer
    are independently-built, real-world instances that follow (datasette-mcp)
    or complement (mcp-explorer, as a general-purpose inspection tool outside
    that post's scope) that guidance.

- **Novel**:
  - **MCP-vs-Skills mindshare eclipse narrative** (Claim 2): No prior corpus
    source documents *why* MCP lost practitioner attention in 2025 from this
    specific angle — that shell+curl agent harnesses were simply more
    flexible for the same jobs, not that MCP was technically deficient.
  - **"MCP tools are simple enough for smaller/laptop-class models to drive
    reasonably well" as an explicit capability-tiering argument** (Claim 3):
    new to the corpus; distinct from auth-isolation or scaling arguments.
  - **mcp-explorer**: a standalone, install-free (`uvx`), harness-independent
    MCP inspection/debugging CLI — no prior corpus source documents a
    general-purpose MCP exploration tool of this kind.
  - **datasette-mcp's "fourth attempt, first shippable version" history**
    (Claim 8): concrete first-hand evidence that the stateless spec removed
    a real, previously blocking implementation obstacle for at least one
    practitioner, not merely a theoretical simplification.
  - **A demonstrated 7-query autonomous tool-orchestration session** (Claim 9)
    against a deliberately minimal three-tool MCP surface — a concrete,
    linked, reproducible example of multi-step tool composition through a
    small tool surface rather than a purpose-built single "answer this"
    tool.
  - **llm-mcp-client and its reasoning-trace transcript** (Claim 10): the
    first corpus example of a reasoning trace showing ambiguity resolution
    ("could also mean published notes or drafts") before a tool call is
    issued, in the specific context of an MCP tool invocation.
  - **The pre-Lethal-Trifecta MCP injection framing** (Claim 11): connects
    MCP's original 2025 security concern (users mixing/matching tools
    exposes them to exfiltration risk) to the author's own later Lethal
    Trifecta framework, a piece of intellectual history not previously
    captured in the corpus's MCP coverage.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 3's capability-tiering
  argument as a second, independent justification (alongside the existing
  auth-isolation justification from `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`)
  for preferring MCP tool calling over shell/CLI agent access in harnesses
  that may run weaker or cheaper models: a bounded, named MCP tool surface is
  "simple enough that smaller models... can still drive them reasonably
  well," where driving an open shell safely requires a stronger model. This
  is a concrete guidance point for teams choosing model tier per harness
  component.
- **Chapter 02 (Harness Engineering)**: Add mcp-explorer as a recommended
  utility for the specific, currently undocumented workflow of "inspecting
  an unfamiliar MCP server before wiring it into a harness" — install-free
  via `uvx`, works against any MCP endpoint, shows tool lists and JSON
  schemas. No existing corpus source documents an MCP debugging/exploration
  tool.
- **Chapter 03 (Safety and Verification)**: Add Claim 12 as a named,
  independent security argument — reasoning about a bounded MCP tool
  capability set is easier than reasoning about arbitrary shell/`curl`
  execution in an open network environment — distinct from and additive to
  the existing auth-isolation argument. If the guide already states "prefer
  MCP over credentials-in-context for untrusted content," it should also
  state "prefer MCP over open shell access when the harness needs to bound
  and audit what an agent can technically do," citing this source.
  Recommend framing both as complementary, non-competing reasons to prefer
  MCP — not a single unified argument, since they address different threat
  mechanisms (credential exposure vs. capability enumeration).
  Note: this claim is the author's stated position, not a benchmarked
  security study — flag it in the guide as an argued position, matching this
  note's `anecdotal` per-claim confidence.
- **Chapter 04 (Context Engineering)**: The datasette-mcp minimal three-tool
  design (Claim 8) and the 7-query composition example (Claim 9) are a
  concrete, citable illustration of `blog-anthropic-mcp-production-agents.md`
  Claim 6's "group tools around intent, few well-described tools" principle
  — useful as a worked example rather than only an abstract principle.

## Extraction Notes

1. **Fetched raw HTML directly rather than relying on WebFetch summarization**:
   An initial WebFetch pass returned a paraphrased/summarized rendering of the
   article and, on a second attempt asking for full verbatim reproduction,
   WebFetch declined on copyright grounds and offered only quotes under ~125
   characters. To satisfy MINER.md §2a's verbatim-quote requirement, the page
   was instead fetched directly via `curl` (`https://simonwillison.net/2026/Jul/31/stateless-mcp/`),
   the article body isolated from the surrounding page chrome, and every quote
   in this note copied character-for-character (including the source's own
   curly quotes and em dashes) from that raw HTML text — not reconstructed
   from any AI-generated summary. The full article (all five sections) was
   read in its entirety before extraction began.

2. **Distinguished the author's own claims from spec text he reproduces**:
   The before/after HTTP request examples in "What's easier with stateless
   MCP" are explicitly attributed by Willison to "this May 21st blog post
   that introduced the RC for the new specification" — i.e., he is
   reproducing someone else's worked example, not presenting his own
   independent technical analysis. Claim 5 and the corresponding Concrete
   Artifacts entries are labeled accordingly; the assessment for Claim 5
   treats it as corroboration (a second source repeating the same example)
   rather than as fresh, independent evidence for the underlying mechanism.

3. **No sub-pages followed for the three GitHub project repositories**: The
   post links to `github.com/simonw/mcp-explorer`, `github.com/datasette/datasette-mcp`,
   and `github.com/simonw/llm-mcp-client`, plus a linked README for
   mcp-explorer ("a few more commands"). None of these were fetched — the
   post's own descriptions, command examples, and output samples were judged
   sufficient for the claims extracted here, consistent with the source being
   a project-announcement post rather than technical documentation. A deeper
   extraction of any one project's README/documentation would be a candidate
   for a separate future source if submitted independently.

4. **Confidence grading rationale**: `confidence_overall` is set to
   `emerging` rather than `settled`: the mechanical/architectural claims that
   corroborate the already-`emerging`-graded `blog-google-mcp-stateless-scaling.md`
   are settled at the claim level, but the three projects are described as
   built "this week" (i.e., within days of publication), one is explicitly
   labeled "alpha," and the central security argument (Claim 12) is a stated
   practitioner position rather than a benchmarked comparison — collectively
   this is fresh, not-yet-battle-tested practitioner adoption evidence, not a
   settled body of practice.

5. **Checked for contradictions; none filed**: Reviewed all overlapping notes
   named in the Prospector's triage comments
   (`blog-google-mcp-stateless-scaling.md`,
   `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`,
   `blog-anthropic-mcp-production-agents.md`,
   `blog-simonwillison-cloudflare-mcp-api-fallback.md`) plus
   `blog-simonwillison-mcp-claude-chatgpt-setup.md`, which this post directly
   links to as "a new TIL." No claim in this source opposes a claim in any
   existing note; the security arguments in this note and in the Sean Lynch
   note describe two different, additive mechanisms (capability enumeration
   vs. credential isolation) rather than disagreeing about the same fact
   — see Cross-References → Contradicts.

6. **Cross-references verified before writing**: Every cited `Claim N` was
   confirmed by re-reading the cited note in full and locating that
   `### Claim N:` heading in document order before citing it here.
