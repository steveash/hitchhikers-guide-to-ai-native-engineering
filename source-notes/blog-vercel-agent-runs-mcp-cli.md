---
source_url: https://vercel.com/changelog/agent-runs-vercel-mcp-cli
source_type: blog-post
title: "Agent Runs now available in the Vercel MCP and CLI"
author: Melkey Moksyakov, Allen Zhou, Josh Souphanthong, Brooke Mosby (Vercel)
date_published: 2026-07-03
date_extracted: 2026-08-01
last_checked: 2026-08-01
status: current
confidence_overall: emerging
issue: "#2393"
---

# Agent Runs now available in the Vercel MCP and CLI

> Vercel changelog announcing four new Vercel MCP tools and four parallel
> CLI commands that let a developer — or a coding agent itself, via
> `--json`/markdown CLI output — query `eve`'s automatically-captured
> Agent Runs observability data (run listings, metadata, and full traces
> with reasoning/tool-calls/token usage) without opening the web dashboard.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`; a
  "1 min read" feature announcement of four short paragraphs, two bulleted
  tool/command lists, and two install-command snippets). Two linked docs
  pages were followed per MINER.md §1: `vercel.com/docs/agent-resources/vercel-mcp/tools`
  (the "Agent Runs Observability Tools" reference section, containing full
  parameter tables and sample prompts for all four tools) and
  `vercel.com/docs/eve/observability` (the underlying Agent Runs dashboard
  and OpenTelemetry-export documentation that this changelog's new
  MCP/CLI tools expose programmatic access to). A third linked page,
  `vercel.com/docs/cli`, is a generic CLI landing page not specific to
  Agent Runs and was not followed; `eve.dev` and `eve.dev/templates` are
  marketing/template pages outside this issue's triage scope (MCP/CLI tool
  mechanics) and were not followed.
- **Author credibility**: First-party Vercel product-team announcement,
  credited to four named individuals (Melkey Moksyakov, Allen Zhou, Josh
  Souphanthong, Brooke Mosby) verified directly in the page's raw HTML
  byline. No customer quotes, adoption metrics, or independent benchmarks
  appear anywhere in the source or the two linked docs pages — this is
  first-party documentation of a shipping feature, not third-party
  reporting or validation.
- **Scope**: Covers four new Vercel MCP tools and four parallel CLI
  subcommands for querying Agent Runs (eve's automatically-captured
  observability data) — what each tool/command does, its parameters, and
  installation. Does **not** cover: pricing for Agent Runs or the new
  tools, a GA/beta status for the feature (no beta or experimental label
  appears anywhere in the changelog or the linked MCP-tools reference
  page — unlike several other Vercel sources in this corpus, e.g.
  `blog-vercel-workflow-sdk-payload-compression.md`'s explicit "beta" SDK
  version), how Agent Runs data is stored or how long it is retained, or
  any named customer/production usage of the new tools.

## Extracted Claims

### Claim 1: Coding agents (not just human developers) can now inspect eve's automatically-captured Agent Runs observability data via the Vercel MCP and CLI
- **Evidence**: The changelog's opening two sentences, addressed to "your agent" rather than to a human developer.
- **Confidence**: settled (first-party, unambiguous first-party feature description)
- **Quote**: "Your agent can now inspect Agent Runs via the Vercel MCP and CLI for eve, the open-source agent framework."
- **Quote (auto-ingestion)**: "eve traces are automatically ingested when deployed to Vercel and available as Agent Runs."
- **Our assessment**: The framing — "your agent can now inspect" rather than "you can now view" — is the load-bearing detail: this changelog explicitly targets a coding agent as the consumer of the observability data, not only a human reading a dashboard. Combined with Claim 4's "coding agents without MCP access can call the CLI directly to debug their own runs," this positions Agent Runs as infrastructure for an agent to self-debug its own prior production runs, a distinct pattern from the human-facing dashboards documented elsewhere in the corpus (see Cross-References → Novel).

### Claim 2: Four new Vercel MCP tools expose Agent Runs data — listing projects with run activity, listing runs, inspecting one run's metadata, and retrieving a run's full trace
- **Evidence**: A bulleted tool list in the changelog, with fuller descriptions and full parameter tables confirmed in the linked `vercel-mcp/tools` reference page's "Agent Runs Observability Tools" section.
- **Confidence**: settled (first-party API reference with named tools and parameter tables)
- **Quote**: "`list_agent_run_projects`: Find projects in a team with Agent Runs activity. `list_agent_runs`: List recent runs for a project. `get_agent_run`: Inspect metadata, lifecycle events, usage, and subagent data. `get_agent_run_trace`: Retrieve trace data for a run, including turns, messages, reasoning, tool calls, token usage, and tool input/output."
- **Our assessment**: The four tools form a clear drill-down hierarchy — find the project, list its runs, inspect one run's metadata, then pull its full trace — mirroring how a human would navigate the Agent Runs dashboard (Claim 8) but exposed as discrete, individually-callable MCP tools rather than a single UI flow. `get_agent_run`'s inclusion of "subagent data" confirms the underlying eve runtime tracks subagent relationships within a run, not just top-level turns.

### Claim 3: Four parallel Vercel CLI commands mirror the four MCP tools — listing projects, listing runs, inspecting a run, and fetching a trace
- **Evidence**: A bulleted CLI command list immediately following the MCP tool list in the changelog.
- **Confidence**: settled (first-party command reference)
- **Quote**: "`vercel agent-runs projects`" / "`vercel agent-runs list`" / "`vercel agent-runs inspect <runId>`" / "`vercel agent-runs trace <runId>`"
- **Our assessment**: The 1:1 mapping between the four MCP tools and four CLI subcommands (projects↔list_agent_run_projects, list↔list_agent_runs, inspect↔get_agent_run, trace↔get_agent_run_trace) means a developer or agent gets the same four operations regardless of which interface it has access to — the changelog does not describe any capability available in one interface but not the other.

### Claim 4: Every Agent Runs CLI subcommand supports `--json` for machine-readable output, and traces render as markdown when piped, specifically so that coding agents without MCP access can debug their own runs directly through the CLI
- **Evidence**: A dedicated sentence following the CLI command list, framed as the rationale for the dual-format output design.
- **Confidence**: settled (first-party design rationale, explicit and unambiguous)
- **Quote**: "Every CLI subcommand supports `--json` for machine-readable output, and traces render as markdown when piped, so coding agents without MCP access can call the CLI directly to debug their own runs."
- **Our assessment**: This is the most concrete statement in the source of the CLI-as-fallback-interface design: the changelog explicitly anticipates that some coding agents run in environments without MCP access (e.g., a CLI-only harness) and designs the CLI's own output formatting — JSON for programmatic parsing, markdown when piped — around that agent-as-consumer use case rather than only a human terminal user. "To debug their own runs" reinforces Claim 1's self-debugging framing: the agent calling the CLI and the agent whose run is being inspected can be the same agent.

### Claim 5: Vercel suggests developers interact with Agent Runs data conversationally, asking a coding agent natural-language questions that the agent then answers by calling the new MCP tools or CLI
- **Evidence**: A dedicated sentence in the changelog, immediately preceding the installation instructions.
- **Confidence**: settled (first-party usage guidance)
- **Quote**: "Ask your coding agent questions like &quot;Show me the latest production Agent Runs for my project&quot; or &quot;Update skills based on recent runs&quot;."
- **Our assessment**: The second example prompt — "Update skills based on recent runs" — is notable beyond simple debugging: it implies a workflow where an agent reads its own or a fleet's recent Agent Runs, extracts a pattern (e.g., a repeated failure mode or missing knowledge), and then edits its own skill files in response, closing an observe-then-self-correct loop without a human manually reviewing traces first. The changelog does not elaborate on this workflow further or provide a worked example of it.

### Claim 6: `get_agent_run_trace` accepts a `maxFieldLength` parameter (default 8000 characters, 0 to disable) that truncates individual string fields in the returned trace
- **Evidence**: The parameter table for `get_agent_run_trace` in the linked `vercel-mcp/tools` reference page.
- **Confidence**: settled (first-party API parameter documentation)
- **Quote**: "`maxFieldLength` | number | No | 8000 | Maximum length for individual string fields in the returned trace. Use 0 to disable truncation."
- **Our assessment**: This parameter matters specifically because trace data returned by this tool (reasoning, tool inputs/outputs, message content) is itself model-generated text that could be arbitrarily long — a truncation default protects against a single `get_agent_run_trace` call flooding the calling agent's own context window with an oversized trace payload. This is a concrete, tool-level instance of the general "results returned to an agent must themselves be context-budgeted" concern documented elsewhere in the corpus (see Cross-References).

### Claim 7: The Agent Runs MCP tools support flexible time-range filtering via named preset periods (from 5 minutes to 90 days) or explicit `from`/`to` timestamps, and `list_agent_runs` additionally supports pagination and server-side title search
- **Evidence**: The shared `period`/`from`/`to` parameter definitions repeated across all four tools' parameter tables, plus `list_agent_runs`-specific `page`, `pageSize`, and `search` parameters, in the linked `vercel-mcp/tools` reference page.
- **Confidence**: settled (first-party API parameter documentation)
- **Quote**: "Preset time range. Supports `5m`, `15m`, `1h`, `6h`, `12h`, `1d`, `3d`, `7d`, `14d`, `30d`, and `90d`. Ignored when both `from` and `to` are provided."
- **Quote (list_agent_runs pagination)**: "`pageSize` | number | No | - | Number of runs per page. The dashboard endpoint caps this at 100."
- **Our assessment**: The `pageSize` cap of 100 and the note that this is "the dashboard endpoint" specifically indicates the new MCP tools/CLI commands are a thin programmatic wrapper around the same backend endpoints the existing Agent Runs web dashboard already calls, rather than a separately-built data path — consistent with Claim 8/9's description of the dashboard as the pre-existing observability surface this changelog is adding query access to.

### Claim 8: The Agent Runs dashboard — the pre-existing UI surface this changelog's MCP/CLI tools now expose programmatically — appears automatically for eve projects with no instrumentation file required, and shows run-level (triggers, token usage, duration) and turn-level (timings including skill loads, tool calls with arguments/results, reasoning, token counts) detail
- **Evidence**: The "Agent Runs" section of the linked `vercel.com/docs/eve/observability` documentation page, describing the dashboard the new tools query.
- **Confidence**: settled (first-party documentation of a described-as-already-shipping dashboard feature)
- **Quote**: "This is the primary observability surface for eve, and it appears automatically for eve projects, with no instrumentation file required."
- **Quote (turn detail)**: "Timings for each step in the turn, including skill loads and individual tool calls."
- **Our assessment**: "No instrumentation file required" is the key architectural claim underlying Claim 1's "eve traces are automatically ingested" — a developer deploying an eve agent to Vercel gets this observability surface passively, without writing any tracing/logging code, distinct from the opt-in OpenTelemetry export path described in Claim 10. This zero-instrumentation default is the same "automatic inheritance from the underlying platform" pattern already documented for eve's Workflow SDK compression benefit (see Cross-References).

### Claim 9: Because Agent Runs capture is always-on, Vercel states that deployers whose agents process personal, sensitive, or regulated data may be legally required to disclose this capture in their own privacy materials
- **Evidence**: An explicit compliance caveat immediately following the dashboard description in the linked `vercel.com/docs/eve/observability` documentation page.
- **Confidence**: settled (first-party, explicit self-disclosed compliance obligation, not a marketed capability)
- **Quote**: "As the deployer, where your agent processes personal, sensitive, or regulated data, you may be required to disclose this capture as required by applicable laws and in your privacy materials."
- **Our assessment**: This is a self-disclosed limitation/obligation of the kind MINER.md flags as high-value — Vercel is naming a real compliance burden its own always-on, no-opt-out-mentioned observability default creates for anyone deploying an eve agent that touches regulated data (e.g., healthcare, financial, or PII-handling agents). Neither this page nor the changelog describes an opt-out mechanism for Agent Runs capture, so a team building such an agent must treat "Agent Runs will capture this" as the default and plan disclosure accordingly, not assume capture is conditional on consent being configured.

### Claim 10: For teams wanting AI SDK OpenTelemetry spans in an external observability backend beyond the Agent Runs dashboard, eve auto-discovers an `agent/instrumentation.ts` file and runs it at server startup with no separate toggle
- **Evidence**: The "Export AI SDK spans with OpenTelemetry" subsection of the linked `vercel.com/docs/eve/observability` documentation page.
- **Confidence**: settled (first-party mechanism description)
- **Quote**: "eve auto-discovers `agent/instrumentation.ts` and runs it at server startup before any agent code. Its presence enables telemetry, and there is no separate toggle."
- **Our assessment**: This confirms Agent Runs (Claims 1-9) and OpenTelemetry export are two independent, non-exclusive observability paths for the same eve deployment — Agent Runs is the always-on, zero-configuration default (Claim 8), while OpenTelemetry export is an opt-in path activated purely by a file's presence (no config flag), for teams that want AI SDK spans in a separate backend as well. The changelog's new MCP/CLI tools query Agent Runs specifically; this note found no indication they also expose OpenTelemetry-exported data.

## Concrete Artifacts

### New Vercel MCP tools and CLI commands (verbatim, from the changelog)

```
Source: https://vercel.com/changelog/agent-runs-vercel-mcp-cli

Vercel MCP tools:
- list_agent_run_projects: Find projects in a team with Agent Runs activity.
- list_agent_runs: List recent runs for a project.
- get_agent_run: Inspect metadata, lifecycle events, usage, and subagent data.
- get_agent_run_trace: Retrieve trace data for a run, including turns,
  messages, reasoning, tool calls, token usage, and tool input/output.

Vercel CLI commands:
- vercel agent-runs projects
- vercel agent-runs list
- vercel agent-runs inspect <runId>
- vercel agent-runs trace <runId>

Every CLI subcommand supports --json for machine-readable output, and
traces render as markdown when piped, so coding agents without MCP
access can call the CLI directly to debug their own runs.

Ask your coding agent questions like "Show me the latest production
Agent Runs for my project" or "Update skills based on recent runs".

Install:
  npx add-mcp https://mcp.vercel.com
Or upgrade the CLI:
  npm i -g vercel@latest
```

### `list_agent_run_projects` parameter table (verbatim, from `vercel.com/docs/agent-resources/vercel-mcp/tools`)

```
Source: https://vercel.com/docs/agent-resources/vercel-mcp/tools#agent-runs-observability-tools

List projects in a Vercel team that have Agent Runs observability data for
eve agents. The response includes run counts and average duration rollups
for each project.

Parameter    | Type   | Required | Default    | Description
teamId       | string | Yes      | -          | The team ID to list projects for. Team IDs start with 'team_'. Can be found by reading .vercel/project.json (orgId) or using the list_teams tool.
environment  | string | No       | production | Agent run environment, usually production or preview
period       | string | No       | -          | Preset time range: 5m, 15m, 1h, 6h, 12h, 1d, 3d, 7d, 14d, 30d, 90d. Ignored when both from and to are provided.
from         | string | No       | -          | Start time as ISO 8601, Unix seconds, Unix milliseconds, or a relative duration like 12h. Must be used with to.
to           | string | No       | -          | End time as ISO 8601, Unix seconds, Unix milliseconds, a relative duration like 1h, or now. Must be used with from.

Sample prompt: "Which projects in my team have Agent Runs in the last 24 hours?"
```

### `list_agent_runs` and `get_agent_run` parameter tables (verbatim)

```
Source: https://vercel.com/docs/agent-resources/vercel-mcp/tools#agent-runs-observability-tools

list_agent_runs
List Agent Runs for a Vercel project. The response includes summaries,
status, model, trigger, token usage, time series, and pagination metadata
for eve agent activity.

Parameter  | Type   | Required | Default | Description
teamId     | string | Yes | - | The team ID to list Agent Runs for.
projectId  | string | Yes | - | The project ID to list Agent Runs for. Project IDs start with 'prj_'.
environment| string | No | production | Agent run environment, usually production or preview
period/from/to | (same as above)
page       | number | No | 1 | Page number
pageSize   | number | No | - | Number of runs per page. The dashboard endpoint caps this at 100.
search     | string | No | - | Server-side title search for Agent Runs

Sample prompt: "Show me the latest production Agent Runs for my project"

get_agent_run
Get detailed metadata for a single eve Agent Run, including events,
workflow metadata, usage, and subagent breakout data. Use list_agent_runs
first if you need to find a run ID.

Parameter | Type | Required | Default | Description
teamId, projectId, runId (Yes), environment, period/from/to (as above)

Sample prompt: "Inspect Agent Run wrun_123 for my project"
```

### `get_agent_run_trace` parameter table (verbatim)

```
Source: https://vercel.com/docs/agent-resources/vercel-mcp/tools#agent-runs-observability-tools

Get the trace for a single eve Agent Run, including turns, messages,
reasoning, tool calls, token usage, and tool input or output when
available. Use this tool to debug exact agent behavior in production.

Parameter       | Type   | Required | Default | Description
teamId, projectId, runId (Yes), environment, period/from/to (as above)
maxFieldLength  | number | No | 8000 | Maximum length for individual string fields in the returned trace. Use 0 to disable truncation.

Sample prompt: "Show me the tool calls and messages from Agent Run wrun_123"
```

### Agent Runs dashboard description and compliance caveat (verbatim, from `vercel.com/docs/eve/observability`)

```
Source: https://vercel.com/docs/eve/observability#agent-runs

Open your project in the Vercel dashboard and go to Agent Runs. This is
the primary observability surface for eve, and it appears automatically
for eve projects, with no instrumentation file required.

The overview shows:
- Runs over time, broken down by trigger (such as Slack and HTTP).
- Token usage over the same window, split into input, output, and cached
  tokens.
- A table of runs with the triggering message, trigger type, tokens in
  and out, turn count, duration, and time.

Select a run to drill into it. The run detail shows its model, trigger,
and deployment, then a per-turn breakdown with:
- Timings for each step in the turn, including skill loads and
  individual tool calls.
- Input and Output for the turn.
- Reasoning the model produced along the way.
- Tool Calls made during the turn, with their arguments and results.
- Input, cached, and output token counts for the turn.

Because this view is always on, it is the fastest way to confirm an
agent is running in production and to inspect what happened on any given
session.

As the deployer, where your agent processes personal, sensitive, or
regulated data, you may be required to disclose this capture as required
by applicable laws and in your privacy materials.

Export AI SDK spans with OpenTelemetry
eve auto-discovers agent/instrumentation.ts and runs it at server
startup before any agent code. Its presence enables telemetry, and
there is no separate toggle.
```

## Cross-References

### Cross-reference verification notes
`blog-latentspace-vercel-andrew-qu-eve.md`, `blog-vercel-workflow-sdk-payload-compression.md`,
`blog-vercel-ai-sdk-7-release.md`, `blog-ghaw-agent-observability.md`, and
`blog-anthropic-connector-observability.md` were re-read (in full, or via
their numbered `### Claim N:` headings for the two longest notes) during
this extraction per MINER.md §4b, and every claim number cited below was
located and confirmed against that note's own numbered claims in document
order before writing this section.

- **Corroborates**:
  - `blog-latentspace-vercel-andrew-qu-eve.md` Claim 8 ("If you deploy eve
    to Vercel, you get observability and evaluations out of the box"):
    that claim, from Vercel's own Chief of Software, asserted observability
    as a batteries-included benefit of eve without describing its
    mechanism. This source is the first in the corpus to supply that
    mechanism in concrete technical detail — the always-on, no-instrumentation
    Agent Runs dashboard (Claim 8 here) plus the new MCP/CLI query layer on
    top of it (Claims 1-7). "Evaluations" (the other half of that claim) is
    not addressed anywhere in this source.
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't
    optional when you're running dozens of AI agents"): a second,
    independent vendor (Vercel, via eve) arrives at the same operating
    principle — production agent observability is treated as a default,
    not an opt-in feature a team must build themselves. The architectures
    differ substantially: GitHub's pattern (that note's Claims 2-3) is
    three purpose-built *agents* (Metrics Collector, Portfolio Analyst,
    Audit Workflows) that actively analyze other agents' runs and can raise
    issues autonomously; this source's pattern is passive, automatic trace
    capture exposed for query, with no autonomous analysis or remediation
    agent described anywhere in this source.
  - `blog-anthropic-connector-observability.md` Claim 3 (per-tool error
    breakdowns as a debugging primitive for MCP connector developers):
    both sources document a vendor shipping structured, tool-call-level
    debugging detail (that source: per-tool error rates for a *connector*;
    this source: per-turn tool calls with arguments and results for an
    *agent run*, Claim 8 here) as a named observability feature, though for
    different subjects (a deployed MCP server vs. a deployed agent) and at
    different granularity (aggregate error rates vs. individual-call trace
    detail).

- **Contradicts**: None identified as a MINER.md §4a contradiction. No
  claim in this source opposes any existing corpus note.

- **Extends**:
  - `blog-vercel-workflow-sdk-payload-compression.md` Claim 6 ("Since eve
    builds durable agents on the Workflow SDK, the same compression now
    applies to the conversation history and state it persists for every
    session... with no code to change"): this source's Claim 8 ("appears
    automatically for eve projects, with no instrumentation file required")
    is the same "eve inherits a platform-level capability automatically,
    with zero code changes" pattern, now documented for observability
    capture rather than storage compression — the two sources together
    show this "automatic inheritance" design recurring across at least two
    distinct eve/Vercel platform features.
  - `blog-vercel-ai-sdk-7-release.md` Claim 10 (AI SDK 7's observability
    redesign: telemetry moved to a separate opt-in `@ai-sdk/otel` package,
    plus native Node.js tracing-channel emission): that note documents a
    generic, opt-in-registration OpenTelemetry layer for any AI SDK
    application. This source's Claim 10 shows the specific hook (eve's
    auto-discovered `agent/instrumentation.ts`) that an eve deployment uses
    to plug into that same `@ai-sdk/otel` layer for external-backend
    export — while Claim 8's Agent Runs dashboard is a separate,
    always-on, zero-instrumentation path that does not require
    `@ai-sdk/otel` at all. The two notes together clarify that eve
    deployments have two independent, non-exclusive observability paths,
    a distinction neither note alone fully states.
  - `blog-anthropic-connector-observability.md`: that note documents a
    human-facing web dashboard (Organization settings → Directory) for
    MCP connector developers, with no MCP-tool or CLI query access
    described anywhere in that source — a developer must open the Claude
    web UI to see connector metrics. This source extends the observability
    corpus with a case where the equivalent data (run/trace metrics) is
    additionally exposed through machine-callable interfaces (MCP tools,
    CLI with `--json`/markdown output) explicitly designed for a coding
    agent to query directly, not only through a web dashboard.

- **Novel**:
  - **Agent-run observability data exposed for query by the agent itself,
    not only by a human via a dashboard** (Claims 1, 4, 5): no prior corpus
    source documents an agent-observability surface built specifically so
    that a coding agent can query its own (or another agent's) past
    production runs programmatically and act on the result (e.g., "update
    skills based on recent runs," Claim 5) — every other observability
    source in the corpus (`blog-ghaw-agent-observability.md`,
    `blog-anthropic-connector-observability.md`) describes either
    dedicated auditor *agents* analyzing other agents, or a human-facing
    *dashboard*, not a query interface aimed at the subject agent's own
    self-debugging loop.
  - **A CLI-output design (`--json` plus markdown-when-piped) explicitly
    justified as a fallback for agents without MCP access** (Claim 4): no
    prior corpus source documents a CLI tool whose output-format choice is
    explicitly framed around "agents that lack MCP access" as a named
    constraint to design for.
  - **An explicit vendor statement tying an always-on agent-observability
    default to a legal disclosure obligation for personal/sensitive/regulated
    data** (Claim 9): no prior corpus source documents an agent-observability
    feature carrying a stated compliance/privacy-disclosure obligation for
    its deployer. This is a new, concrete data point for any guide
    discussion of agent-platform default behaviors that create downstream
    compliance work for the team adopting them.
  - **A per-call truncation parameter (`maxFieldLength`) on a tool that
    itself returns model-generated trace content back into a calling
    agent's context** (Claim 6): no prior corpus source documents an
    observability-query tool with a context-budget control aimed at
    preventing its own (potentially large) return payload from flooding
    the calling agent's context window.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Agent Runs' MCP tools and CLI
  commands (Claims 1-5, Concrete Artifacts) as a concrete example resolving
  `blog-latentspace-vercel-andrew-qu-eve.md` Claim 8's previously
  unelaborated "observability... out of the box" claim, and specifically
  as an instance of a harness capability the guide does not yet cover:
  observability tooling built so the *agent* — not only a human — can
  query its own production run history to self-debug. Recommend framing
  this alongside the "Update skills based on recent runs" example (Claim
  5) as a named pattern: observe-own-runs → self-correct, distinct from
  the human-in-the-loop dashboards documented elsewhere in the corpus.

- **Chapter 04 (Context Engineering)**: Add the `maxFieldLength` truncation
  parameter (Claim 6) as a concrete example of a tool designer budgeting
  an observability/debugging tool's own return payload against the calling
  agent's context window — relevant to any guide discussion of tools whose
  results can themselves be large enough to need truncation controls,
  distinct from the MCP-server-side token-efficiency patterns
  (`blog-anthropic-mcp-production-agents.md` Claims 10-11) which address
  tool *definitions* and *result processing*, not a single tool's own
  variable-length return payload.

- **Chapter 06 (Security Threat Model)**: Add Claim 9's disclosure
  obligation as a concrete compliance consideration for teams adopting a
  platform with always-on agent-observability capture: if an eve agent
  deployed to Vercel processes personal, sensitive, or regulated data, the
  deployer — not Vercel — may be required to disclose that Agent Runs
  captures it, in their own privacy materials, with no stated opt-out
  mechanism for the capture itself. This is a new, concrete instance of
  the general pattern that a platform's helpful-by-default observability
  can create compliance obligations for its adopters that are easy to
  overlook when the feature reads as a purely positive debugging benefit.

## Extraction Notes

1. **WebFetch output not trusted for quotes; raw HTML fetched and parsed
   instead.** An initial WebFetch pass returned a clean but reworded
   paraphrase (e.g., it rendered Claim 4's quote as "so coding agents
   without MCP access can call the CLI directly to debug their own runs"
   with different surrounding sentence structure than the source). Per
   MINER.md §2a, the changelog's raw HTML was fetched directly via `curl`
   with a browser user-agent, and every `Quote` field in this note was
   located character-for-character in that raw capture (the site is a
   Next.js app; article text appears in escaped form inside an embedded
   Contentful richtext JSON payload, and again in de-tagged rendered HTML)
   before being used here.
2. **Two linked docs pages followed per MINER.md §1**, specifically because
   the changelog's own prose is short (four paragraphs) and the Prospector's
   highest-novelty triage comment asked for "tool names, capabilities...
   MCP vs CLI parity/differences" that only the linked API reference could
   supply in full: `vercel.com/docs/agent-resources/vercel-mcp/tools`
   (fetched in full for its "Agent Runs Observability Tools" section, which
   supplied every parameter table and sample prompt in Claims 2, 6, and 7)
   and `vercel.com/docs/eve/observability` (fetched in full for its "Agent
   Runs" and "Export AI SDK spans with OpenTelemetry" sections, which
   supplied Claims 8-10 and are the source of the "always on... no
   instrumentation file required" and disclosure-obligation claims that do
   not appear in the changelog itself). A third linked page
   (`vercel.com/docs/cli`) is a generic CLI landing page, not specific to
   Agent Runs, and was not followed; `eve.dev` and `eve.dev/templates` are
   product-marketing pages outside this issue's MCP/CLI-mechanics scope and
   were not followed.
3. **No beta/experimental label found.** Neither the changelog nor the
   linked MCP-tools reference page marks Agent Runs, the four MCP tools, or
   the four CLI commands as beta or experimental anywhere in the raw HTML
   (checked via case-insensitive substring search for "beta" across both
   pages) — unlike, e.g., `blog-vercel-workflow-sdk-payload-compression.md`'s
   explicitly beta-versioned SDK. This note treats the feature as shipped/
   generally available on the evidence available, while noting that no
   source in this family states a formal GA declaration either.
4. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts. The nearest
   candidate tension — this source's "agent queries its own runs directly"
   pattern versus `blog-ghaw-agent-observability.md`'s dedicated-auditor-agent
   pattern — is a different architectural approach to the same underlying
   goal (agent-fleet observability), not a factual disagreement about what
   either vendor's system does, so it was not filed.
5. **Confidence calibration: emerging.** Individual claims are rated
   "settled" because they are first-party, unambiguous descriptions of
   named tools/commands with full parameter tables, cross-checked against
   raw HTML across three separately fetched pages. The note's overall
   confidence is "emerging" rather than "settled" because: (a) this is a
   single vendor's own changelog and API reference with no independent
   verification, benchmark, or named customer/production usage evidence
   anywhere in the source family; (b) the feature's stability tier (beta
   vs. GA) is not stated anywhere, so its likelihood of near-term breaking
   changes cannot be assessed from this source alone; and (c) the
   self-debugging and "update skills based on recent runs" usage patterns
   (Claims 1, 4, 5) are described as intended use cases via sample prompts,
   not demonstrated with a worked example or production evidence that a
   coding agent has actually used these tools this way.
