---
source_url: https://simonwillison.net/2026/May/21/datasette-agent/
source_type: blog-post
title: "Datasette Agent"
author: Simon Willison
date_published: 2026-05-21
date_extracted: 2026-05-23
last_checked: 2026-05-23
status: current
confidence_overall: emerging
issue: "#869"
---

# Datasette Agent

> Simon Willison's May 2026 post documenting the first release of Datasette Agent —
> a concrete, working production example of an LLM agent that translates natural
> language into SQLite queries, with plugin-based extensibility, permission-scoped
> table access, and multi-provider model flexibility; the most specific real-world
> implementation of a database agent pattern in the current corpus.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, May 21, 2026; supplemented by
  the May 14, 2026 release note at `https://simonwillison.net/2026/May/14/datasette-agent/`)
- **Author credibility**: Simon Willison is the creator of Datasette and the
  `llm` Python library, widely recognized as a high-signal practitioner and
  commentator in the LLM tooling space. He is speaking from direct implementation
  experience — he built, deployed, and is operating Datasette Agent himself. The
  live demo at agent.datasette.io is publicly accessible, making claims about
  the system's behavior verifiable. This is not a vendor post or speculative
  architecture discussion — it documents a shipped 0.1a1 release.
- **Scope**: Covers the first working release of Datasette Agent: its core
  natural language → SQLite translation capability, model selection rationale
  (Gemini Flash-Lite for cost/speed), three shipped plugins extending the agent
  with charts/image-generation/code-sandbox, the `execute-sql` permission system
  for table-level access control, multi-provider flexibility via the `llm` library
  (including local models), and future plans (Datasette Cloud rollout, personal
  assistant "Claw," Claude Artifacts plugin). Does NOT cover the internal
  prompt/tool design in detail, failure modes of the SQL generation, or
  performance benchmarks.

## Extracted Claims

### Claim 1: Datasette Agent translates natural language questions into SQLite queries as a conversational interface over existing data

- **Evidence**: First-party description from the author who built the system; live
  demo available at agent.datasette.io. The post includes a concrete example:
  asking "when did Simon most recently see a pelican?" yields a generated SQL
  query over the blog_beat table with LIKE pattern matching and ORDER BY, returning
  a result from May 20, 2026.
- **Confidence**: settled (the system is live and publicly accessible; the author
  built it; the SQL generation is demonstrable)
- **Quote**: "Datasette Agent provides a conversational interface for asking
  questions of the data you have stored in Datasette."
- **Our assessment**: This is the clearest corpus example of the NL→SQL agent
  pattern in a working, deployed system. Unlike theoretical agent architectures,
  this is Willison's actual tool processing real queries against his own data.
  The approach — use an LLM to generate SQL, execute against real data, return
  structured results — is the most common "database agent" design, and this note
  provides a concrete reference implementation.

### Claim 2: Gemini 3.1 Flash-Lite was selected for the production demo for cost and speed, not capability — it is sufficient for SQLite query generation

- **Evidence**: Direct author statement explaining the model choice for the live demo.
  The selection criterion is explicitly cost/speed, not maximum capability, with
  the specific assertion that Flash-Lite is adequate for this task.
- **Confidence**: emerging (author's operational assessment; no benchmark comparison
  with other models; single practitioner's judgment based on observed behavior)
- **Quote**: "The live demo runs on Gemini 3.1 Flash-Lite—it's cheap, fast and
  has no trouble writing SQLite queries."
- **Our assessment**: This is high-value model-selection evidence for SQL generation
  agents. The implicit claim is that writing correct SQLite queries does not require
  frontier-scale reasoning — a lightweight, cheap, fast model is sufficient. This
  is consistent with the heuristic across the corpus that task-appropriate model
  selection beats always defaulting to the largest model. The "no trouble writing
  SQLite queries" framing is an operational assessment, not a benchmark — practitioners
  should verify for their schema complexity and query types.

### Claim 3: Plugin-based extensibility is the primary architectural pattern for extending agent capabilities — capabilities are added as plugins, not baked into core

- **Evidence**: Three shipped plugins demonstrated at launch: datasette-agent-charts
  (Observable Plot visualizations), datasette-agent-openai-imagegen (ChatGPT Images
  2.0 image generation), datasette-agent-sprites (Fly Sprites persistent code
  sandbox). Each plugin adds new tools to the agent's tool-calling repertoire.
- **Confidence**: emerging (design is demonstrated with working examples; the
  long-term viability of the plugin architecture is not yet proven at scale)
- **Quote**: "datasette-agent-charts...adds charts to Datasette Agent, powered by
  Observable Plot."
- **Our assessment**: The plugin model inverts the usual agent design: instead of
  adding capabilities to the agent directly, the agent's capabilities expand
  through the same plugin mechanism as Datasette itself. This makes the capability
  surface open-ended — any third-party developer could add tools to the agent.
  The pattern mirrors how Datasette's existing ecosystem (hundreds of plugins)
  works, suggesting that meeting users where they are (in the existing plugin
  model) lowers adoption friction for contributors.

### Claim 4: The `execute-sql` permission system controls which tables the agent can list to the user

- **Evidence**: May 14, 2026 release note (0.1a1 changelog): "Now uses the
  `execute-sql` permission when deciding which tables to list to the user. #8"
  This is a concrete implementation change, not a design description.
- **Confidence**: settled (release changelog entry; specific, verifiable behavior
  change in a named version)
- **Quote**: "Now uses the `execute-sql` permission when deciding which tables to
  list to the user. #8" (from https://simonwillison.net/2026/May/14/datasette-agent/)
- **Our assessment**: This is the most specific permission-system claim in the
  corpus for a database agent. The agent respects existing Datasette permission
  semantics — tables a user cannot `execute-sql` against are not exposed to the
  agent. This means the agent inherits the host system's access controls rather
  than adding a parallel permission layer, which is sound security design: no new
  permission surface, same controls as the underlying tool. The `#8` reference to
  a GitHub issue indicates this was not the initial design but a deliberate
  post-launch correction — an important signal that access-scoping for database
  agents is an easy thing to get wrong on first implementation.

### Claim 5: Reliable tool calling and SQLite query generation are the minimum model requirements for running Datasette Agent

- **Evidence**: Direct statement of the technical prerequisites for a model to work
  with the agent. The constraint is stated as a capability threshold, not a
  recommendation.
- **Confidence**: settled (author-stated requirement from the developer who built
  the system; logically derivable from the agent's operation)
- **Quote**: "Datasette Agent needs reliable tool calls and the ability for a model
  to produce SQL queries that run against SQLite."
- **Our assessment**: This two-part requirement is the minimum viability bar for
  any SQL generation agent: (1) the model must support structured tool calling
  (not just text generation), and (2) the model must produce syntactically correct
  SQLite. The emphasis on "reliable" tool calls — not just "some" tool calls — is
  important: sporadic tool call support produces inconsistent agent behavior.
  This requirement explicitly excludes models that produce SQL but in the wrong
  dialect (e.g., PostgreSQL-only syntax), or models that can use tools but
  generate hallucinated column names.

### Claim 6: The same agent works with local/open-source models via the `llm` library's provider abstraction, not just cloud APIs

- **Evidence**: Working command-line example provided in the post for running
  Datasette Agent against gemma-4-26b-a4b in LM Studio. The integration is via
  `llm-lmstudio` plugin, using the `llm` library's provider abstraction.
- **Confidence**: emerging (command shown; presumably works given Willison's
  publication standard; not independently verified)
- **Quote**: (no direct quote for this claim; see Concrete Artifacts for the
  verbatim command)
- **Our assessment**: Provider flexibility at the command-line level (swap
  `lmstudio/google/gemma-4-26b-a4b` for another model string to change providers)
  is a strong design property for an agent system. It means practitioners in
  privacy-sensitive or air-gapped environments can run the same agent locally.
  The constraint is that the local model must still meet Claim 5's minimum
  requirements — reliable tool calls and SQLite generation. Not all local models
  will qualify.

### Claim 7: Datasette Agent wraps an existing data exploration tool rather than building a new data layer — integration is the pattern, not greenfield construction

- **Evidence**: The agent is built as a Datasette plugin (not a standalone application),
  meaning it operates entirely within Datasette's existing data model, permission
  system, and plugin ecosystem. The agent does not replicate or replace Datasette —
  it adds a conversational interface on top.
- **Confidence**: settled (design is inherent in the architecture; the author is
  Datasette's creator and is explicitly layering the agent capability onto the
  existing tool)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is the "wrap an existing tool" integration pattern
  rather than the "build an agent with tools" pattern. Rather than defining
  tool schemas that replicate what Datasette already does (serving data, enforcing
  permissions, managing plugins), the agent plugin simply gains access to Datasette's
  native runtime. The advantage: the agent inherits all existing Datasette
  functionality (authentication, access control, performance) without re-implementing
  it. The pattern is directly applicable to practitioners who want to add LLM
  agents to existing data infrastructure — rather than building an agent with
  database-connection tools, build the agent as a plugin to the existing data platform.

### Claim 8: Future agent applications include a personal AI assistant ("Claw") and a Claude Artifacts alternative, both built on the same plugin infrastructure

- **Evidence**: Author's stated future plans in the post. The personal assistant
  ("Claw") and the Claude Artifacts plugin are named as next projects.
- **Confidence**: anecdotal (stated intention; not yet shipped; single practitioner's
  roadmap)
- **Quote**: "I've been exploring my own take on the Claude Artifacts, which is
  shaping up nicely as a plugin."
- **Our assessment**: The personal assistant extension is notable for what it implies
  about the pattern: the same agent infrastructure (llm library + Datasette +
  plugin system) is intended to serve as a general-purpose personal AI substrate,
  not just a database query tool. A Claude Artifacts alternative as a plugin
  suggests the author sees plugin-based extensibility as a path to feature parity
  with hosted AI products — self-hosted, composable, under user control. This is
  consistent with Willison's broader "local-first LLM tooling" perspective.

## Concrete Artifacts

### Core Natural Language → SQL Query Example

```
Source: Simon Willison's Weblog, May 21, 2026 (agent.datasette.io live demo)

User question: "when did Simon most recently see a pelican?"

Generated SQL (against blog_beat table):
  SELECT title, commentary, created
  FROM blog_beat
  WHERE beat_type = 'sighting'
    AND (title LIKE '%pelican%' OR commentary LIKE '%pelican%')
  ORDER BY created DESC
  LIMIT 5

Result: Most recent sighting — May 20, 2026 (California Brown Pelican)

Note: SQL reconstructed from WebFetch extraction; may not be character-for-character
verbatim from the source page.
```

### Command to Run Against Local Models (LM Studio)

```bash
# Source: Simon Willison's Weblog, May 21, 2026
# Runs Datasette Agent against gemma-4-26b-a4b via LM Studio locally

uvx --prerelease=allow \
  --with datasette-agent --with llm-lmstudio \
  datasette --internal internal.db --root \
  -s plugins.datasette-llm.default_model lmstudio/google/gemma-4-26b-a4b \
  data.db
```

### Three Shipped Plugins at 0.1a1 Launch

```
Source: Simon Willison's Weblog, May 21, 2026

1. datasette-agent-charts
   "adds charts to Datasette Agent, powered by Observable Plot"
   — Visualization plugin: agent can generate data visualizations alongside query results

2. datasette-agent-openai-imagegen
   "adds an image generation tool...using ChatGPT Images 2.0"
   — Image generation plugin: agent can generate images in response to prompts

3. datasette-agent-sprites
   "provides tools for executing code in a Fly Sprites persistent sandbox"
   — Code execution plugin: agent can execute code in a persistent sandbox environment
```

### execute-sql Permission Integration (May 14 Release Note)

```
Source: https://simonwillison.net/2026/May/14/datasette-agent/ (release 0.1a1 changelog)
Published: May 14, 2026

Changelog entry:
  "Now uses the execute-sql permission when deciding which tables to list to the user. #8"

Interpretation: The agent respects Datasette's existing execute-sql permission system
when building the list of tables it presents to the user. Tables the user cannot
execute SQL against are not surfaced to the agent.
```

### Model Requirements (Minimum Viability Bar)

```
Source: Simon Willison's Weblog, May 21, 2026

Minimum requirements for a model to work with Datasette Agent:
  1. Reliable tool calls — model must support structured tool-calling (not text-only)
  2. SQLite query generation — model must produce syntactically correct SQLite

"Datasette Agent needs reliable tool calls and the ability for a model to produce
SQL queries that run against SQLite."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 1: "Agents are only as useful
    as the systems they can reach." Datasette Agent is a concrete implementation
    of this principle — the agent's value derives entirely from its ability to
    reach the Datasette data infrastructure. The integration-first design (plugin
    into Datasette, inherit its permissions) is the practical answer to the question
    that claim raises.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5: "The bottleneck has shifted
    from code generation to verification." In the SQL generation context, query
    execution IS verification — the query either returns correct results or not.
    Datasette Agent's pattern makes this concrete: the agent generates SQL and
    the database engine verifies it by running it. No separate verification step
    is required.

- **Extends**:
  - `blog-anthropic-mcp-production-agents.md`: That post establishes MCP as the
    preferred integration layer for production agents connecting to external systems.
    Datasette Agent demonstrates an alternative integration path: Python plugin +
    `llm` library, not MCP. Both patterns are valid; this source extends the
    integration pattern space with a non-MCP concrete example. Practitioners
    connecting agents to existing Python-based tools now have both options documented
    in the corpus.

- **Contradicts**: None found. No existing source note makes a materially opposing
  claim to those extractable from this post.

- **Novel**:
  - **Concrete deployed NL→SQL agent with a real example**: No prior corpus source
    documents a working, publicly accessible database agent with a specific SQL
    generation example. This is the first concrete reference implementation.
  - **execute-sql permission for table-level agent access control**: No other
    corpus source describes a database-native permission system (reuse existing
    SQL execution permissions) for scoping what an LLM agent can see. This is
    a distinct pattern from the general "scope permissions" advice in
    `blog-anthropic-computer-use-best-practices.md` — it's table-level, reuses
    existing controls, and requires no new permission layer.
  - **Plugin-based agent extensibility as an architectural pattern**: The pattern
    of agents that gain new tools through the host system's plugin mechanism
    (rather than having tools baked in) is not documented elsewhere in the corpus.
  - **Model selection by task sufficiency (Flash-Lite for SQL generation)**:
    The explicit "cheap, fast, and no trouble writing SQLite queries" framing is the
    first corpus example of selecting a small/cheap model specifically because it is
    sufficient for a structured-output task, with cost/speed as the tiebreaker.
  - **Wrap-existing-tool integration pattern (plugin to existing data platform)**:
    No other corpus source demonstrates building an agent as a plugin to an existing
    data platform (inheriting auth, permissions, ecosystem) rather than building
    the agent with database-access tools from scratch.

## Guide Impact

- **Ch02 (Tool Use & Agentic Systems) — Integration Patterns**: Add the
  "plugin-to-existing-platform" integration pattern (Claim 7) as a distinct
  alternative to the MCP-or-custom-tool pattern documented in
  `blog-anthropic-mcp-production-agents.md`. When an existing tool has a
  plugin/extension mechanism, building the agent as a plugin (and inheriting
  the tool's auth, permissions, and ecosystem) can be significantly lower cost
  than exposing the tool via MCP or custom API wrappers.

- **Ch03 (Tool Use — model selection)**: Add Claim 2 as a concrete example of
  task-appropriate model selection: Gemini 3.1 Flash-Lite was sufficient for
  SQLite generation. The guide should update any general "use a capable model"
  advice to note that for structured-output tasks (SQL, JSON, simple code
  generation), lightweight models may suffice and reduce cost/latency
  significantly. Pair with the "minimum model requirements" framing from Claim 5.

- **Ch03 (Tool Use — permission scoping)**: Add Claim 4 (execute-sql permission
  for table-level access control) as a concrete permission-scoping example.
  The broader lesson: when integrating an LLM agent into an existing system,
  prefer reusing the system's native permission model over adding a new agent-specific
  permission layer. This prevents permission drift and reduces the attack surface.

- **Ch04 (Common Patterns — plugin extensibility)**: Add Claim 3 as the reference
  example for plugin-based agent extensibility. The pattern — agent tools are
  added as plugins, not baked into core — creates an open-ended capability surface
  and mirrors ecosystem patterns practitioners already know from non-AI plugin
  systems (WordPress plugins, Datasette plugins, VS Code extensions).

- **Ch06 (Model Selection — cost/speed vs. capability tradeoffs)**: Add Claim 2
  as the primary example of "model sufficiency" rather than "model maximality"
  in model selection for SQL agents. Recommend that practitioners identify the
  minimum model requirements for their task (Claim 5: reliable tool calls +
  dialect-correct SQL) and test lightweight models before defaulting to frontier
  models.

## Extraction Notes

- **Two source URLs**: The issue body lists the May 14 release note URL
  (`https://simonwillison.net/2026/May/14/datasette-agent/`), but the
  Prospector's triage comment explicitly directs extraction to the May 21 post
  (`https://simonwillison.net/2026/May/21/datasette-agent/`). The May 21 post
  contains the substantive content; the May 14 release note is a one-sentence
  changelog. Both were fetched; Claim 4 is exclusively from the May 14 note;
  all other claims are from the May 21 post.
- **WebFetch limitation**: The WebFetch tool processes HTML through an AI model
  before returning content, so quotes marked as verbatim are those the WebFetch
  model enclosed in quotation marks. The SQL query in Concrete Artifacts was
  stated as a generated example by the WebFetch extraction model and is likely
  reconstructed rather than character-for-character from the post. It is marked
  accordingly in the artifact.
- **Live demo not fetched**: The live demo at agent.datasette.io and embedded
  video were not accessible via WebFetch. Plugin pages and linked repositories
  were not fetched (within the 5-link budget, the substantive content was
  concentrated in the main post). Practitioners wanting to verify SQL generation
  behavior should consult the live demo directly.
- **Pre-release software**: This is version 0.1a1 — alpha quality. Claims about
  architecture and design patterns are reliable; claims about specific behavior
  may change in future releases. Confidence is calibrated as `emerging` overall.
- **No contradictions filed**: No existing corpus source makes an opposing claim.
  The closest potential tension — MCP as the standard integration layer vs.
  plugin/llm-library integration — is not a contradiction because both patterns
  are complementary; no corpus source claims MCP is the *only* valid approach.
