---
source_url: https://claude.com/resources/articles/skills-over-mcp-tasks-and-more
source_type: blog-post
title: "MCP servers can now ship skills, run tasks, and more with Claude"
author: Anthropic (no individual byline)
date_published: 2026-11-24
date_extracted: 2026-11-26
last_checked: 2026-11-26
status: current
confidence_overall: emerging
issue: "#4964"
---

# MCP servers can now ship skills, run tasks, and more with Claude

> Anthropic announces Skills over MCP (public beta) and GA of Tasks and Elicitation, shifting the "Skills vs MCP" framing toward servers that bundle procedural guidance with their tools.

## Source Context

- **Type**: blog-post (vendor product update, category "Product updates", 6 min read)
- **Author credibility**: Anthropic, the creator of MCP and Claude/Claude Code; authoritative on what ships in its own products, but this is an announcement with no code, config, or measurements beyond one figure that is repeated from earlier material.
- **Scope**: Covers Skills over MCP, Tasks, Elicitation, File Uploads, plan availability, and a recap of MCP improvements (tool search, stateless spec, Enterprise Managed Auth, MCP Apps). Does not give protocol detail, versioning semantics for server-shipped skills, or any measurements of context cost. Partner examples are vendor-reported.

## Extracted Claims

### Claim 1: Tool names and descriptions say what a server can do, not how to handle specific use cases; Skills over MCP lets servers publish that "how" alongside tools
- **Evidence**: Design rationale stated by the vendor; customer examples (Shopify, HubSpot, Atlassian, Carta) but no detail or metrics.
- **Confidence**: emerging
- **Quote**: "Tool names and descriptions tell Claude what a server can do, but don't cover how to handle specific use cases."
- **Our assessment**: Plausible and consistent with the skills/MCP complementarity argument. The gap it names (procedural knowledge absent from tool schemas) is real, but there is no evidence yet on how much it improves task success.

### Claim 2: Server-shipped skills load only when needed, so context use stays low
- **Evidence**: Assertion only; no token figures for server-shipped skills.
- **Confidence**: anecdotal
- **Quote**: "Claude loads a skill only when it's needed, keeping context use low."
- **Our assessment**: Matches progressive-disclosure design of local skills. Unquantified here; do not carry the local-skill token budget figures over to this mechanism without measurement.

### Claim 3: Skills ship and update with the server, so users have nothing separate to install
- **Evidence**: Stated mechanism; versioning, pinning, and trust model are not described.
- **Confidence**: emerging
- **Quote**: "Skills update with the server, so developers can ship tools and guidance together and users have nothing separate to install."
- **Our assessment**: Real distribution advantage (tools and guidance cannot drift apart). The flip side, not discussed in the post, is that skill text now arrives from a remote server and can change without user action. That is a trust and prompt-injection surface worth flagging for Ch06.

### Claim 4: Skills can cover best practices, step-by-step workflows, or account/organization-tailored playbooks
- **Evidence**: Listed use categories; examples are Shopify (store design/updates), HubSpot (onboarding), Atlassian (org context), Carta (equity issuance from an uploaded document, "coming soon").
- **Confidence**: anecdotal
- **Quote**: "Skills can cover best practices, step-by-step workflows, or even playbooks tailored to a user's account or organization."
- **Our assessment**: "Tailored to a user's account" implies skills can be dynamic per user, which differs from static file-based skills. Mechanism unspecified.

### Claim 5: Skills over MCP is in public beta with plan-dependent availability
- **Evidence**: Availability statement.
- **Confidence**: settled (as a statement of the 2026-11-24 rollout)
- **Quote**: "Skills over MCP is in public beta in Claude and Claude Code, on by default for Pro, Max, and Ultra plans and available to Team plans once an admin enables it. Coming soon to Enterprise."
- **Our assessment**: Time-sensitive; guide text should state the date and avoid presenting it as universally available.

### Claim 6: Tasks let servers run long operations, even full agent loops, while Claude keeps working and collects the result later
- **Evidence**: Mechanism description; ZoomInfo cited for deeper account/contact research "that previously took several prompts" (vendor-reported).
- **Confidence**: emerging
- **Quote**: "With Tasks, servers can run operations that take time, or even full agent loops, while Claude keeps working and picks up the result when it's ready."
- **Our assessment**: Moves MCP from synchronous request/response toward delegation to a server-side agent. The "full agent loops" wording means a server can itself be an agent, which raises the nested-agent cost/observability questions the post does not address.

### Claim 7: Tool calls previously had to finish before Claude could proceed
- **Evidence**: Framing statement describing prior behavior.
- **Confidence**: settled
- **Quote**: "Tool calls used to have to finish before Claude could move on."
- **Our assessment**: Accurate baseline for synchronous MCP tool calls; helps decide when to use Tasks (slow operations) versus a plain tool call.

### Claim 8: Elicitation lets a server pause mid-call to ask the user for sign-off via a form or link, then resume
- **Evidence**: Mechanism plus examples: Supabase confirms costs before creating a paid project and before running destructive SQL; Railway asks before removing a service; GitHub has users type a repository's name before an agent deletes it.
- **Confidence**: emerging
- **Quote**: "With Elicitation, a server can pause to ask the user for input through a form or link, then continue where it left off."
- **Our assessment**: Concrete, reusable human-in-the-loop pattern: put the confirmation gate in the server, at the point of the costly/destructive action, rather than relying on the client's permission prompts. The GitHub "type the repo name" example is the familiar typed-confirmation pattern applied to agents. Examples are vendor-reported.

### Claim 9: Tasks and Elicitation are GA in Claude and Claude Code for Pro/Max/Ultra, rolling out to Team and Enterprise
- **Evidence**: Availability statement.
- **Confidence**: settled (as rollout statement)
- **Quote**: "Tasks and Elicitation are now generally available in Claude and Claude Code for Pro, Max, and Ultra plans, and rolling out to Team and Enterprise organizations."
- **Our assessment**: Updates the status of elicitation, which the April 2026 note described as an early extension.

### Claim 10: File Uploads sends files to servers without passing them through the context window
- **Evidence**: Feature description; not yet shipped ("rolling out soon").
- **Confidence**: emerging
- **Quote**: "The File Uploads extension sends PDFs, spreadsheets, and images to a server without passing them through the context window."
- **Our assessment**: A context-engineering win in principle (bulk data bypasses context). Not yet available, so treat as announced, not proven.

### Claim 11: Tool search can cut tool-definition context by over 85% in multi-server setups
- **Evidence**: A single figure with no methodology; the same 85% figure appears in the April 2026 Anthropic note.
- **Confidence**: emerging
- **Quote**: "Tool search loads tool definitions only when needed, which can cut the context they use by over 85% in multi-server setups."
- **Our assessment**: Self-reported by the same vendor, so it is not independent corroboration of the earlier note. Hedged with "can".

### Claim 12: The latest MCP spec is stateless and supported across Claude products; Enterprise Managed Auth and MCP Apps extensions exist
- **Evidence**: Listed as improvements, no detail.
- **Confidence**: emerging
- **Quote**: "The latest MCP spec is stateless and supported across Claude products, making it easier to build servers and maintain their reliability as they grow."
- **Our assessment**: Corroborates the Google note on the stateless spec; Anthropic confirms client-side support. Enterprise Managed Auth ("lets admins authorize supported servers once, so users connect automatically") is new to the corpus.

### Claim 13: These features are open MCP spec/extensions, so any compatible client can support them
- **Evidence**: Statement; docs linked for each feature.
- **Confidence**: emerging
- **Quote**: "These features are part of the open MCP spec and its extensions, so a server that supports them works in any compatible client, not just Claude."
- **Our assessment**: Server-shipped skills are therefore not Claude-lock-in in principle, but actual client support elsewhere is unverified.

### Claim 14: Ecosystem scale figures
- **Evidence**: Vendor statistics, no sourcing.
- **Confidence**: anecdotal
- **Quote**: "MCP now sees over 700 million monthly SDK downloads, and there are over 10,000 MCP connectors for Claude."
- **Our assessment**: Adoption signal only; low value for guide advice.

## Concrete Artifacts

No code, config, or transcripts in the source. Availability matrix (source, 2026-11-24):

```
Feature            Status        Plans
Skills over MCP    public beta   Pro/Max/Ultra default-on; Team via admin enable; Enterprise coming soon
Tasks              GA            Pro/Max/Ultra; rolling out to Team and Enterprise
Elicitation        GA            Pro/Max/Ultra; rolling out to Team and Enterprise
File Uploads       rolling out soon   Pro/Max/Ultra and eligible Team/Enterprise
```

Elicitation gating examples named in the source: Supabase (cost before paid project; destructive SQL), Railway (removing a service), GitHub (user enters repo name before deletion).

## Cross-References

- **Corroborates**: `blog-anthropic-mcp-production-agents.md` Claim 12 (skills and MCP are complementary: MCP gives tool access, skills give procedure) and Claim 10 (tool search 85%+ reduction; same vendor). `blog-google-mcp-stateless-scaling.md` Claim 2 and Claim 3 (stateless spec), Claim 7 (stateless elicitation via MRTR) and Claim 8 (Tasks extension graduating to first-class feature).
- **Contradicts**: No direct contradiction filed. Tension to note: `blog-french-owen-coding-agents-feb-2026.md` Claim 2 (skills are cheap, MCP calls are expensive) supports preferring skills over MCP; this post reframes them as bundled, with MCP servers carrying the skills. Claims differ in context (local-skill vs MCP cost framing) rather than opposing, so no contradiction issue was filed.
- **Extends**: `blog-anthropic-mcp-production-agents.md` Claim 8 (elicitation was an early extension; now GA) and Claim 12 (adds the shipping mechanism). `blog-anthropic-claude-code-skills-lessons.md` (skills design) now has a server-distributed delivery path.
- **Novel**: Skills over MCP as a delivery mechanism; Tasks that can wrap full agent loops; Enterprise Managed Auth; File Uploads extension; GA/rollout dates and plan matrix.

## Guide Impact

- **Chapter 04**: The "prefer Skills over MCP whenever both can do the job" guidance (sourced from the French-Owen note) should be qualified: when a server ships its own skills, the choice is no longer either/or. Add the date-stamped caveat that this is public beta. Do not extend the per-skill token budget table to server-shipped skills; the source gives no figures.
- **Chapter 02**: Add Tasks as the option for long-running or agent-loop tool work (versus synchronous tool calls), and Elicitation as the server-side mid-call confirmation mechanism; note plan availability.
- **Chapter 06**: Recommend elicitation gates before spending money or destructive operations (typed-confirmation pattern); flag that server-shipped skills are remotely updatable instructions, so treat them as a trust boundary (our inference, not stated in source).

## Extraction Notes

- Read the full article text (fetched directly). Linked docs pages (Skills over MCP, Tasks, Elicitation, File Uploads) were not followed; protocol-level detail is therefore absent from this note.
- All customer examples are vendor-reported and unverified. Triage comments' suggested questions (versioning vs local install, when to use Tasks, what to gate) are only partly answerable from the post; the post does not discuss versioning or context-cost measurements.
