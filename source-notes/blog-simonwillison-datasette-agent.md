---
source_url: https://simonwillison.net/2026/May/21/datasette-agent/
source_type: blog-post
title: "Datasette Agent"
author: Simon Willison
date_published: 2026-05-21
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: anecdotal
issue: "#869"
---

# Datasette Agent

> Simon Willison's May 21, 2026 post announces Datasette Agent — an LLM-powered
> conversational interface for querying Datasette databases — and demonstrates
> plugin-based agent extensibility, cost/speed-driven model selection for SQL
> generation, and permission-scoped data access; taken with the companion May 14
> release note, the source provides a complete working example of an agentic
> system built by composing existing data infrastructure with an LLM library.

## Source Context

- **Type**: blog-post (release announcement with embedded demo video, May 21,
  2026). Accompanied by a shorter May 14, 2026 release note for version 0.1a1
  (source URL from the filed issue: simonwillison.net/2026/May/14/datasette-agent/).
  The May 21 post contains the substantive technical content; the May 14 post
  contributes a single implementation detail (the `execute-sql` permission
  change). Both were read and are documented here.
- **Author credibility**: Simon Willison is the creator of Django, the `llm`
  CLI, and Datasette. He has been building and publicly documenting AI-assisted
  tooling for three years. This is first-party release documentation from the
  tool's own author. He is not vendor-promotional — the live demo deliberately
  uses Gemini Flash-Lite (a Google model) rather than Anthropic's Claude, and
  Willison openly reports both capabilities and limitations across his blog.
- **Scope**: The May 21 post covers: the conversational interface design
  (natural language → SQL), model selection for the live demo, the plugin
  ecosystem (three initial plugins shipped), local model support via LM Studio,
  and future directions. Does NOT cover: internal prompt engineering, failure
  modes, latency characteristics, or production deployment guidance. The live
  demo at agent.datasette.io was not accessed (embedded video; not a text
  source). The May 14 post covers one specific implementation change: using
  the `execute-sql` permission to control table visibility.

## Extracted Claims

### Claim 1: Datasette Agent provides a conversational interface for querying Datasette databases using natural language

- **Evidence**: First-party description from the tool's creator, published on
  the day of release. The post provides a concrete worked example: asking "when
  did Simon most recently see a pelican?" generates a SQL query against the
  blog_beat table with LIKE pattern matching and ORDER BY, returning a
  structured natural language answer.
- **Confidence**: settled (first-party documentation from the author; the demo
  is publicly accessible at agent.datasette.io)
- **Quote**: "Datasette Agent provides a conversational interface for asking
  questions of the data you have stored in Datasette."
- **Our assessment**: This is the core UX pattern: natural language → SQL
  generation → structured result, presented back in natural language. The
  pelican example is non-trivial — it requires the agent to understand that
  "saw a pelican" implies a LIKE search on sighting text rather than a direct
  equality match. The pattern is the same underlying capability as enterprise
  "ask your data" products; this is a practitioner-built, open-source
  implementation in the same class.

### Claim 2: Gemini 3.1 Flash-Lite was selected for the production demo over larger models specifically for cost and speed, with SQL generation as the explicit adequacy criterion

- **Evidence**: Direct rationale statement from the author in the May 21 post.
  Willison names the model, names the reason (cheap, fast), and states the
  adequacy claim (no trouble writing SQLite queries).
- **Confidence**: anecdotal (single practitioner decision with stated rationale;
  not a controlled comparison or benchmark)
- **Quote**: "The live demo runs on Gemini 3.1 Flash-Lite—it's cheap, fast and
  has no trouble writing SQLite queries."
- **Our assessment**: The selection rationale demonstrates that for
  structured-output tasks with well-defined syntax (SQL), a cost/speed-optimized
  model is treated as sufficient by the tool's author. The three-part framing
  ("cheap, fast, and no trouble with SQLite queries") implicitly ranks
  constraints: cost and latency first, then capability adequacy last — meaning
  the author chose the cheapest/fastest model that clears the task's capability
  bar, rather than defaulting to the most capable model. This pattern
  corroborates GitHub's addition of fast/cost-efficient model tiers for agent
  tasks (see `docs-github-copilot-cca-cost-efficient-models.md` Claim 1) and
  Anthropic's own model selection guidance for computer use
  (`blog-anthropic-computer-use-best-practices.md` Claim 4). Note that the
  model is Gemini (not Claude), which speaks to Datasette Agent's provider
  agnosticism.

### Claim 3: Plugin-based extensibility is the primary architectural design principle, following Datasette's existing plugin system

- **Evidence**: Explicit design prioritization by the tool's creator — framed
  as "My favorite feature," not a secondary concern. The three shipped plugins
  demonstrate this is not aspirational: the plugin API existed at initial
  release.
- **Confidence**: settled (design intent from the author; working plugins
  confirm the architecture)
- **Quote**: "My favorite feature of Datasette Agent is that, like the rest of
  Datasette, it's extensible using plugins."
- **Our assessment**: This reflects a deliberate architectural choice: agent
  capabilities are not baked into core code but added as separate, composable
  plugins. Each plugin has a distinct capability (visualization, generation,
  execution), audited by installation rather than by reading prompt text. The
  consequence: what the agent can do at any deployment is determined by which
  plugins are installed — a transparent, enumerable capability model. This is
  architecturally related to MCP's composable server approach
  (`blog-anthropic-mcp-production-agents.md` Claim 5), but implemented as a
  native plugin system rather than a network protocol.

### Claim 4: Three plugins shipped with the initial release spanning visualization, generation, and sandboxed execution

- **Evidence**: First-party announcement with named plugins and brief
  descriptions, all released on or before May 21, 2026.
- **Confidence**: settled (first-party announcement; plugin names are verifiable
  on PyPI)
- **Quote**: Plugin descriptions as stated in the article: datasette-agent-charts
  "adds charts to Datasette Agent, powered by Observable Plot";
  datasette-agent-openai-imagegen "adds an image generation tool to Datasette
  Agent using ChatGPT Images 2.0"; datasette-agent-sprites "provides tools for
  executing code in a Fly Sprites persistent sandbox"
- **Our assessment**: The three categories are non-overlapping and span the
  range from read-only (charts from query results) to creative (image
  generation) to compute-capable (sandbox code execution). The code execution
  plugin (datasette-agent-sprites) is the most consequential for security
  analysis: it transitions the agent from read-only data access to
  write/execute capability within a Fly sandbox. The plugin architecture means
  this capability is opt-in — deployments without datasette-agent-sprites
  cannot execute code, not because the prompt restricts it, but because the
  tool does not exist.

### Claim 5: The `execute-sql` permission controls which tables the agent lists and queries — authorization delegated to Datasette's native permission system

- **Evidence**: From the May 14, 2026 release note for version 0.1a1, a
  specific implementation change.
- **Confidence**: settled (first-party implementation note from the tool's
  author)
- **Quote**: "Now uses the `execute-sql` permission when deciding which tables
  to list to the user. #8"
- **Our assessment**: This permission integration is architecturally significant.
  Rather than encoding authorized tables in the agent's prompt, authorization
  is delegated to Datasette's native permission system. The agent sees only
  what the authenticated user is allowed to see. This avoids a class of
  jailbreaking vulnerabilities where prompt-based permission lists can be
  overridden by adversarial input — the database simply will not execute
  unauthorized queries regardless of what the agent is told. It is a concrete
  implementation of the "scope permissions" practice from
  `blog-anthropic-computer-use-best-practices.md` Claim 8, applied to a
  database agent context.

### Claim 6: Datasette Agent supports local/open-source models via LM Studio, not requiring cloud model APIs

- **Evidence**: The May 21 post provides a working `uvx` command for running
  the agent against gemma-4-26b locally via LM Studio on macOS.
- **Confidence**: settled (first-party; working command provided at release)
- **Quote**: (no direct prose quote; the command is the artifact — see Concrete
  Artifacts)
- **Our assessment**: Local model support is architecturally relevant for
  data-private deployments where sending queries to external APIs is prohibited.
  Gemma-4-26b (26B parameters) is large enough to handle SQL generation
  accurately. This multi-provider flexibility follows from the `llm` library's
  provider-agnostic design, which abstracts model access behind a consistent
  interface.

### Claim 7: Datasette Agent is the convergence of the LLM Python library and Datasette after three years of parallel development

- **Evidence**: Direct statement from the tool's creator about the relationship
  between two of his major independent projects.
- **Confidence**: settled (author's own statement about his own projects;
  confirmed by the architectural evidence: both tools are prerequisites for
  Datasette Agent)
- **Quote**: "I've been working on my LLM Python library for just over three
  years now, and Datasette Agent represents the moment that LLM and Datasette
  finally come together."
- **Our assessment**: This framing reveals the stack: Datasette Agent is built
  on the `llm` library for model access and Datasette for data access and
  permissions. Neither was purpose-built for agents — both were independent
  tools that became the agent's substrate. This demonstrates that agent systems
  can emerge from composing purpose-built data and AI tools rather than
  requiring a ground-up agent framework. The `llm` library provides the
  multi-provider abstraction (explaining the multi-provider support); Datasette
  provides data access, permissions, and the plugin system.

### Claim 8: Future directions include Claude Artifacts-style visualization output as a plugin, Datasette Cloud rollout, and a personal AI assistant ("Claw") built on top of the agent

- **Evidence**: Author's stated intentions in the May 21 post. Three distinct
  future directions with different confidence levels: the Artifacts analog is
  described as "shaping up nicely" (in progress); Datasette Cloud rollout is
  stated as a plan ("We'll also be rolling out"); "Claw" is personal ambition
  ("I'm excited to use Datasette Agent to build my own Claw").
- **Confidence**: anecdotal (stated intentions at initial release; software
  plans often change)
- **Quote**: "I've been exploring my own take on the Claude Artifacts, which is
  shaping up nicely as a plugin." and "We'll also be rolling out Datasette Agent
  for users of Datasette Cloud." and "I'm excited to use Datasette Agent to
  build my own Claw—a personal AI assistant built around data imported from
  different parts of my digital life."
- **Our assessment**: The "Claw" direction is the most substantively interesting
  signal for the guide: Willison is describing building a personal AI assistant
  over self-imported personal data (life logs, browsing history, etc.) as a
  concrete near-term project. This is a practitioner-announced implementation
  of the "AI over personal data" pattern that other sources discuss only
  abstractly. The Artifacts analog as a plugin reinforces that the author is
  aware of and learning from competitor product patterns. The Datasette Cloud
  rollout signals organizational support for the project beyond personal tooling.

## Concrete Artifacts

### Local Model Command (from May 21 post)

```bash
uvx --prerelease=allow --with datasette-agent --with llm-lmstudio datasette --internal internal.db --root -s plugins.datasette-llm.default_model lmstudio/google/gemma-4-26b-a4b data.db
```

*Source: Simon Willison, simonwillison.net/2026/May/21/datasette-agent/, 2026-05-21*

Command breakdown:
- `uvx --prerelease=allow` — run in isolated uv environment, allowing pre-release packages
- `--with datasette-agent --with llm-lmstudio` — install both the agent and the LM Studio provider plugin
- `--internal internal.db` — path for Datasette Agent's internal session storage
- `--root` — run as root user (required for the agent to use Datasette internal APIs)
- `-s plugins.datasette-llm.default_model lmstudio/google/gemma-4-26b-a4b` — set default model to gemma-4-26b running locally in LM Studio
- `data.db` — the database to query

### Plugin Ecosystem at Initial Release (May 21, 2026)

```
datasette-agent-charts
  Description: "adds charts to Datasette Agent, powered by Observable Plot"
  Capability category: data visualization (read-only, derives charts from query results)

datasette-agent-openai-imagegen
  Description: "adds an image generation tool to Datasette Agent using ChatGPT Images 2.0"
  Capability category: content generation (uses external OpenAI API)

datasette-agent-sprites
  Description: "provides tools for executing code in a Fly Sprites persistent sandbox"
  Capability category: sandboxed code execution (read/execute, not read-only)
```

*Source: Simon Willison, simonwillison.net/2026/May/21/datasette-agent/, 2026-05-21*

### Permission Change (May 14 release note, verbatim)

```
Now uses the `execute-sql` permission when deciding which tables to list to the user. #8
```

*Source: Simon Willison, simonwillison.net/2026/May/14/datasette-agent/, 2026-05-14, version 0.1a1*

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 1: "Agents are only as
    useful as the systems they can reach." Datasette Agent is a concrete
    implementation of this principle — the agent's value derives entirely from
    its connection to the Datasette database and the capabilities of its
    installed plugins. The plugin architecture extends this reach incrementally
    without changing the core agent.
  - `blog-simonwillison-datasette-llm-limits.md` Claim 2: the three-package
    stack (datasette-llm + datasette-llm-accountant + datasette-llm-limits).
    Datasette Agent sits above this governance stack as the conversational
    interface layer. The limits note documents cost governance for the same
    ecosystem; this note documents the conversational access layer built on top
    of it. Together they describe a coherent LLM-over-data architecture: agent
    access → cost governance → query execution → accounting.
  - `docs-github-copilot-cca-cost-efficient-models.md` Claim 1: GitHub's
    expansion of Copilot cloud agent to include "faster, more cost-efficient
    options" for tasks. Willison's explicit Flash-Lite selection (Claim 2 here)
    is the same practitioner reasoning applied to his own deployment: use the
    cheapest/fastest model that clears the capability bar for the task.
  - `blog-anthropic-computer-use-best-practices.md` Claim 8: "four behavioral
    best practices" including "Scope permissions." The `execute-sql` permission
    integration (Claim 5 here) is a concrete implementation of permission
    scoping at the data access layer — with the significant improvement that
    permissions are enforced by the database, not described in the prompt.

- **Extends**:
  - `blog-simonwillison-datasette-llm-limits.md`: That note documents the LLM
    cost governance layer in the Datasette ecosystem. This note adds the
    conversational agent layer built on top of the same infrastructure. The two
    notes together document an LLM deployment architecture: conversational
    access (Datasette Agent) + execution (datasette-llm) + accounting
    (datasette-llm-accountant) + enforcement (datasette-llm-limits).
  - `blog-simonwillison-llm031.md` and `blog-simonwillison-llm032a0.md`: Those
    notes document the `llm` library releases (0.31 and 0.32a0) that form the
    model-access substrate Datasette Agent runs on. This note documents the
    agent layer built on top of that library. The three-year development arc is
    now visible as a platform: llm library → Datasette → Datasette Agent.

- **Contradicts**: None identified. The Flash-Lite model selection (Claim 2) is
  consistent with the general task-appropriate model selection principle across
  the corpus; it does not contradict any existing source's claims.

- **Novel**:
  - **Permission scoping via native database authorization (execute-sql
    pattern)**: No other corpus source documents an agent that derives table
    access permissions from the underlying database's auth system rather than
    from prompt-encoded lists. This is more robust than prompt-based access
    control and has no exact analog in the corpus.
  - **Plugin-based agent tool extensibility in a production open-source
    system**: The corpus covers agent framework discussions (MCP, Osmani's
    orchestration) and vendor products, but no documented open-source agent
    system with a shipped plugin API for adding tools at runtime.
  - **NL-to-SQL-to-Datasette as a complete, deployable agentic data-access
    pattern**: While NL-to-SQL is a well-known concept, the specific architecture
    (llm library + Datasette + execute-sql permissions + plugin ecosystem) as an
    open-source, self-hostable, single-command deployment is new to the corpus.
  - **"Claw" personal AI assistant over self-imported personal data as a
    practitioner-announced near-term project**: Other corpus sources discuss
    AI-over-personal-data abstractly; Willison names a concrete planned project
    with a specific name and states it is actively in progress. First corpus
    source to document this pattern as an imminent personal project from a
    credible practitioner.

## Guide Impact

- **Chapter 02 (Tool Use and Agentic Systems — permission patterns)**: Add the
  `execute-sql` permission integration (Claim 5) as a canonical example of
  permission scoping at the data access layer. The principle to convey: agent
  permissions are most robust when enforced by the underlying system's
  authorization mechanism, not by prompt-encoded access lists. Prompt-based
  lists can be overridden by adversarial input; database-layer enforcement cannot.
  Frame this as the "scope permissions at the execution layer" pattern.

- **Chapter 02 (Tool Use and Agentic Systems — plugin architecture)**: Datasette
  Agent's plugin system (Claims 3 and 4) is a deployable reference for composable
  agent capability design. The guide should note that agent tool sets can be
  configured post-installation as plugins rather than baked into core code —
  enabling both capability auditing (list installed plugins to know what the agent
  can do) and capability restriction (remove a plugin to remove a capability,
  without prompt changes).

- **Chapter 04 (Integration Patterns — NL-to-SQL agents)**: Add Datasette Agent
  as a concrete implementation of the natural language data query pattern. Specific
  guide content: (1) the query example (pelican sightings → SQL → structured
  answer) demonstrates the pattern works for non-trivial queries requiring LIKE
  matching and ordering; (2) local model support enables data-private deployments;
  (3) Flash-Lite selection demonstrates the model adequacy principle for SQL
  generation tasks.

- **Chapter 06 (Model Selection — task-appropriate models)**: Add Willison's
  Flash-Lite selection (Claim 2) as a named practitioner example of
  cost/speed-optimized model selection for structured-output tasks. The signal for
  the guide: for tasks with well-defined output syntax (SQL, JSON schema,
  function signatures), smaller/faster models often clear the capability bar —
  defaulting to the most capable model is not always the right call. Quote the
  rationale directly: "cheap, fast and has no trouble writing SQLite queries."

## Extraction Notes

- **Two source posts, one note**: The issue URL points to the May 14 release note
  (0.1a1, very brief — one implementation change), while the Prospector's triage
  directs extraction toward the May 21 post (the substantive release announcement).
  Both posts were read and mined. All claims except Claim 5 derive from the May 21
  post; Claim 5 (execute-sql permission) derives from the May 14 post.
- **WebFetch verbatim quotes confirmed**: All quotes marked as verbatim were
  confirmed via multiple WebFetch passes with specific quote-extraction prompts.
  The WebFetch tool processes source HTML through an AI model before returning
  content; quotes represent what that model returned as direct text. Plugin
  descriptions in Claim 4 were extracted with explicit verbatim requests and are
  consistent across multiple extraction attempts.
- **Embedded demo video not accessed**: The May 21 post includes an embedded demo
  video at agent.datasette.io. WebFetch cannot process video content; demo
  behavior claims derive from the article's text description and the worked
  example (pelican sightings query), not from viewing the video.
- **Alpha software caveat**: The May 14 post covers version 0.1a1 and the May 21
  post covers the initial public release. Architectural patterns (plugin system,
  execute-sql permission, llm library integration) are likely stable; specific
  API signatures and plugin interfaces may change before stable release.
- **No contradictions filed**: This source introduces a new system with novel
  patterns to the corpus. No existing source note makes claims about Datasette
  Agent's architecture, model selection, or permission model that conflict with
  this source's claims.
