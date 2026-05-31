---
source_url: https://simonwillison.net/2026/May/21/datasette-agent/
source_type: blog-post
title: "Datasette Agent"
author: Simon Willison
date_published: 2026-05-21
date_extracted: 2026-05-31
last_checked: 2026-05-31
status: current
confidence_overall: emerging
issue: "#1011"
---

# Datasette Agent

> The first-party announcement of Datasette Agent — an extensible, plugin-based
> conversational SQL agent for Datasette — establishes a composable capability
> pattern: a core agent handles SQL querying across hundreds of LLM backends, and
> independently-installable plugins add tools (visualization, image generation, code
> execution) without modifying core agent code.

## Source Context

- **Type**: blog-post (Simon Willison's short-form "beat" announcement post at
  simonwillison.net, referencing the official Datasette project blog announcement.
  The post links to a live demo at agent.datasette.io and a demo video; both the
  simonwillison.net post and the Datasette project blog were fetched for this note.)
- **Author credibility**: Simon Willison is the creator of Datasette and the `llm`
  Python CLI. He is the primary developer of Datasette Agent and all three launch
  plugins. This is first-party project announcement documentation — authoritative for
  the platform's capabilities, architecture, and design intent. He has a track record
  of shipping working alpha tooling rapidly in the Datasette ecosystem (cf.
  `blog-simonwillison-datasette-llm-limits.md`, `blog-simonwillison-datasette-agent-charts.md`).
  No vendor affiliation.
- **Scope**: Covers the initial release of Datasette Agent as a platform: core
  architecture, plugin extension model, model support, three launch plugins (with brief
  descriptions), a live demo, and future plans (Datasette Cloud integration, "Claw"
  personal assistant). Does NOT cover: internal agent implementation details, tool
  selection logic, error handling, performance benchmarks, multi-turn conversation
  design, plugin API versioning, or production deployment experience at scale.

## Extracted Claims

### Claim 1: Datasette Agent is an open source plugin for Datasette providing an extensible AI assistant for conversational querying of SQLite databases

- **Evidence**: First-party announcement from the tool's creator, with a live demo
  at agent.datasette.io providing behavioral verification. The Datasette project blog
  describes it as "an open source plugin for Datasette that provides an extensible AI
  assistant for interacting with your SQLite databases."
- **Confidence**: settled (first-party creator-authored announcement; live demo
  confirms the system exists and functions)
- **Quote**: "an open source plugin for Datasette that provides an extensible AI
  assistant for interacting with your SQLite databases."
  *(Source: Datasette project blog announcement, datasette.io/blog/2026/datasette-agent)*
- **Our assessment**: Datasette Agent is the convergence of Willison's multi-year
  LLM library work with the Datasette data platform. The conversational SQL pattern —
  natural language in, SQL query out, prose synthesis back — is the core agent loop.
  The "extensible" framing is load-bearing: extensibility via plugins is explicitly
  called out as the defining design principle, not just an add-on.

### Claim 2: Datasette Agent is built on the LLM Python library, giving it access to hundreds of tool-calling models from frontier vendors and open-weights models through a single interface

- **Evidence**: First-party Datasette blog announcement, which names the model
  abstraction mechanism (the LLM library) and lists example vendor categories.
  Consistent with the LLM library's documented capabilities in
  `blog-simonwillison-llm031.md` and `blog-simonwillison-llm032a0.md`.
- **Confidence**: settled (first-party; consistent with existing corpus documentation
  of the LLM library)
- **Quote**: "support for hundreds of different tool-calling models - from frontier
  vendors like OpenAI, Anthropic and Google Gemini"
  *(Source: Datasette project blog announcement, datasette.io/blog/2026/datasette-agent)*
- **Our assessment**: The LLM library's plugin architecture (llm-gemini, llm-lmstudio,
  etc.) is what gives Datasette Agent multi-model support without per-model integration
  work. The agent inherits the full LLM library model catalog automatically, including
  any future models added via LLM plugins. This decouples agent capability from
  model vendor choices — a significant architectural leverage point.

### Claim 3: The live demo runs on Gemini 3.1 Flash-Lite, chosen for its combination of speed, cost-effectiveness, and SQLite query generation reliability

- **Evidence**: Author's direct statement with explicit reasoning. The model choice
  is stated as a practical decision, not just a capability demonstration.
- **Confidence**: anecdotal (single practitioner choice; but the reasoning — cheap,
  fast, reliable SQL — is generalizable selection criteria for conversational SQL
  agents)
- **Quote**: "The live demo runs on Gemini 3.1 Flash-Lite—it's cheap, fast and has
  no trouble writing SQLite queries."
  *(Source: simonwillison.net/2026/May/21/datasette-agent/)*
- **Our assessment**: The three-criteria model selection heuristic (cost, speed, SQL
  reliability) is architecturally significant for SQL agents. Not all frontier models
  generate reliable SQLite syntax — Willison's selection explicitly names SQL reliability
  as a distinct capability criterion, not just general intelligence. This is a rare
  explicit statement of what "good enough" means for a production SQL agent demo: not
  "most capable model," but "cheapest model that reliably writes correct SQLite."

### Claim 4: Datasette Agent requires reliable tool calls and SQLite SQL generation as minimum model capabilities; recent open-weights models increasingly meet this bar

- **Evidence**: Author's explicit statement of requirements paired with an observation
  about recent open-weights capability trajectory.
- **Confidence**: emerging (first-party technical requirement claim; the open-weights
  capability assertion is qualitative and not benchmarked, though from a highly
  credible practitioner who has tested multiple models)
- **Quote**: "Datasette Agent needs reliable tool calls and the ability for a model
  to produce SQL queries that run against SQLite." and "The open weight models released
  in the past six months are increasingly able to handle that."
  *(Source: simonwillison.net/2026/May/21/datasette-agent/)*
- **Our assessment**: This is the most operationally useful claim for practitioners
  choosing a backend model for SQL agents. The binary threshold — reliable tool calls
  + SQLite SQL generation — is a clearer specification than high benchmark scores. The
  trajectory assertion about open-weights models is significant: it suggests SQL agents
  are approaching commodity model territory for local deployment. The local model
  example in the post (Gemma 4 26B via LM Studio) supports the assertion.

### Claim 5: Extensibility via plugins is Datasette Agent's core architectural feature, following the same plugin model as the rest of Datasette

- **Evidence**: Author's explicit characterization, with the three launch plugins as
  concrete instantiations of the pattern. The Datasette blog also states "Plugins are
  easy to build. The README includes detailed documentation" — actively inviting
  community extension.
- **Confidence**: settled (first-party; three working plugins confirm the extension
  model is real, not aspirational)
- **Quote**: "My favorite feature of Datasette Agent is that, like the rest of
  Datasette, it's extensible using plugins."
  *(Source: simonwillison.net/2026/May/21/datasette-agent/)*
- **Our assessment**: The plugin extension model is the architectural story of this
  release. Three independently-shipped plugins demonstrate that the extension interface
  works in practice — this is not a hypothetical design. Each plugin adds a distinct
  capability class (visualization, image generation, code execution) without modifying
  the core agent. The low friction claim ("Plugins are easy to build") suggests the
  extension interface is stable enough for community adoption at launch.

### Claim 6: Three plugins shipped at launch — datasette-agent-charts (Observable Plot charts), datasette-agent-openai-imagegen (ChatGPT Images 2.0), and datasette-agent-sprites (Fly Sprites code execution) — demonstrating three distinct agent output modalities

- **Evidence**: First-party descriptions of three released plugins from the
  announcement post. Each plugin is named and described with its specific
  implementation.
- **Confidence**: settled (first-party announcement; plugins are released and named
  with specific implementations identified)
- **Quote**:
  - "datasette-agent-charts, shown in the video, adds charts to Datasette Agent, powered by Observable Plot."
  - "datasette-agent-openai-imagegen adds an image generation tool to Datasette Agent using ChatGPT Images 2.0."
  - "datasette-agent-sprites provides tools for executing code in a Fly Sprites persistent sandbox."
  *(Source: simonwillison.net/2026/May/21/datasette-agent/)*
- **Our assessment**: The three plugins represent three distinct agent output modalities
  beyond text: structured visualization (charts), generative imagery, and code execution
  with state persistence. datasette-agent-sprites is particularly notable — Fly Sprites
  is a persistent sandbox, meaning execution state carries across tool calls within a
  session. This enables agentic workflows that mix SQL querying with computation (query
  data → compute → return result), not just retrieval. The three plugins together
  demonstrate that the plugin architecture supports diverse capability classes.

### Claim 7: Natural language questions are translated to SQL, executed against the database, and synthesized into prose responses — demonstrated by a pelican sighting query against personal blog data

- **Evidence**: Demo transcript from the article — a concrete question/answer pair
  showing the full agent loop against real data.
- **Confidence**: anecdotal (single demo example; but demonstrates the core agent
  loop with a realistic multi-entity query)
- **Quote**: "The most recent sighting of a pelican by Simon was recorded on May 20,
  2026. The observation included a California Brown Pelican, along with a Common Loon,
  Canada Goose, Striped Shore Crab, and a California Sea Lion."
  *(Agent response to "when did Simon most recently see a pelican?", source:
  simonwillison.net/2026/May/21/datasette-agent/)*
- **Our assessment**: The demo uses Willison's personal blog data (a backup with
  nature observation records). The query requires: (1) understanding that "Simon"
  refers to the blog owner, (2) identifying the relevant table and columns, (3)
  generating a SQL filter for pelican-related entries, (4) ordering by date, and
  (5) synthesizing multiple associated records into prose. The response includes
  companion species observed alongside the pelican — enriching the answer beyond
  the literal question. This is a meaningful demo for the guide: it shows the value
  of natural language over SQL for exploratory personal data queries.

### Claim 8: Local model deployment is supported via uvx with the llm-lmstudio backend, enabling Datasette Agent to run entirely on local hardware

- **Evidence**: A concrete command-line example in the post for running the agent
  with LM Studio and a specific open-weights model (Gemma 4 26B).
- **Confidence**: settled (the command is concrete, first-party, and executable)
- **Quote**: (no direct prose quote about local deployment; see Concrete Artifacts
  for the verbatim command)
- **Our assessment**: The presence of a working local model deployment command signals
  that Datasette Agent can run with complete data privacy — no query data leaves the
  local machine. For organizations with sensitive data in Datasette, local model
  deployment is the path to conversational SQL without data exposure concerns. The
  specific model (Gemma 4 26B A4B) is a recent open-weights model consistent with
  Claim 4's assertion that recent models meet the tool-call + SQLite bar.

### Claim 9: Datasette Agent will be integrated into Datasette Cloud for hosted users

- **Evidence**: Direct statement from the project creator in the announcement.
- **Confidence**: emerging (future plan stated by the creator; not yet shipped as
  of the announcement date)
- **Quote**: "We'll also be rolling out Datasette Agent for users of Datasette Cloud."
  *(Source: simonwillison.net/2026/May/21/datasette-agent/)*
- **Our assessment**: Datasette Cloud is the hosted version of Datasette. This
  integration would bring the agent to users who don't self-host, potentially making
  Datasette Agent the default conversational query interface for Datasette Cloud. For
  practitioners evaluating Datasette Cloud, this signals that conversational querying
  is the product direction.

### Claim 10: Willison plans to use Datasette Agent to build a personal AI assistant called "Claw" — a system built around data imported from multiple parts of his digital life

- **Evidence**: Author's stated personal use plan in the announcement.
- **Confidence**: anecdotal (stated intent, not completed work at time of announcement)
- **Quote**: "I'm excited to use Datasette Agent to build my own Claw—a personal AI
  assistant built around data imported from different parts of my digital life"
  *(Source: simonwillison.net/2026/May/21/datasette-agent/)*
- **Our assessment**: "Claw" is described as a personal AI assistant — conceptually a
  queryable personal data layer spanning multiple sources (calendar, iNaturalist, blog
  posts, etc.), with Datasette Agent as the conversational SQL interface. This differs
  from vector-search RAG: SQL over structured imports gives exact answers rather than
  semantically similar documents. The Claw concept connects to Willison's existing
  personal data infrastructure (see `blog-simonwillison-inat-sightings.md`), which
  builds exactly the kind of structured personal data that Claw would query.

## Concrete Artifacts

### Local Model Deployment Command (verbatim from simonwillison.net/2026/May/21/datasette-agent/)

```bash
uvx --prerelease=allow \
  --with datasette-agent --with llm-lmstudio \
  datasette --internal internal.db --root \
  -s plugins.datasette-llm.default_model lmstudio/google/gemma-4-26b-a4b \
  data.db
```

*Source: simonwillison.net/2026/May/21/datasette-agent/, 2026-05-21.
Runs Datasette Agent locally using LM Studio as the model backend with
`google/gemma-4-26b-a4b`. `--internal internal.db` provides the agent's internal
state database; `--root` enables root-user access; the `-s` flag sets the default
LLM model for the datasette-llm plugin; `data.db` is the SQLite database to query.*

### Three Launch Plugins (verbatim descriptions from simonwillison.net/2026/May/21/datasette-agent/)

```
1. datasette-agent-charts
   "datasette-agent-charts, shown in the video, adds charts to Datasette Agent, powered by Observable Plot."

2. datasette-agent-openai-imagegen
   "datasette-agent-openai-imagegen adds an image generation tool to Datasette Agent using ChatGPT Images 2.0."

3. datasette-agent-sprites
   "datasette-agent-sprites provides tools for executing code in a Fly Sprites persistent sandbox."
```

### Demo Conversation Excerpt (from simonwillison.net/2026/May/21/datasette-agent/)

```
User query: "when did Simon most recently see a pelican?"

Agent response: "The most recent sighting of a pelican by Simon was recorded on May 20, 2026.
The observation included a California Brown Pelican, along with a Common Loon, Canada Goose,
Striped Shore Crab, and a California Sea Lion."
```

*Query executed against Willison's personal blog backup database at agent.datasette.io,
using Gemini 3.1 Flash-Lite.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-agent-charts.md` Claim 7: "datasette-agent-charts
    installs as a standard Datasette plugin alongside datasette-agent, following
    Datasette's composable plugin model." This source is the platform announcement that
    frames datasette-agent-charts as one of three plugins in the extensible ecosystem.
    The plugin installation claim in the charts note is confirmed by this source's
    broader architecture description.
  - `blog-simonwillison-datasette-llm-limits.md` Claim 2: The three-layer composable
    plugin stack (datasette-llm + datasette-llm-accountant + datasette-llm-limits)
    applies the same additive plugin composition principle as the datasette-agent
    plugin ecosystem. Both demonstrate Datasette's architectural pattern of building
    LLM capabilities as independently-installable layers.
  - `blog-simonwillison-llm031.md` overall: Datasette Agent is built on the `llm`
    Python library. Claim 2 of this source confirms the multi-model abstraction that
    `llm 0.31` provides is what gives Datasette Agent "hundreds of different
    tool-calling models."

- **Extends**:
  - `blog-simonwillison-datasette-agent-charts.md` overall: That note is a deep dive
    into the charts plugin within the ecosystem. This source provides the full platform
    context that the charts note lacked: core agent architecture, the plugin extension
    model, multi-model support, and the other two launch plugins. Together they form
    a complete picture of the Datasette Agent ecosystem at launch.
  - `blog-simonwillison-inat-sightings.md` overall: That note documents Willison's
    iNaturalist sightings tool — personal data infrastructure built around nature
    observation data. Claim 10 of this source (Claw personal AI) is the stated next
    step in the same trajectory: the iNaturalist infrastructure (data pipeline) combined
    with Datasette Agent (conversational SQL layer) is exactly the architecture Claw
    would use. The two notes bracket the data collection side (inat-sightings) and the
    query/assistant side (Datasette Agent) of Willison's personal AI stack.
  - `blog-simonwillison-datasette-blog-codex-session.md` overall: That note documents
    a Codex Desktop session building Datasette's blog infrastructure. Both sources
    show concurrent May 2026 work expanding the Datasette ecosystem.

- **Novel**:
  - **First corpus source documenting Datasette Agent as a platform**: The charts note
    (issue #984) documented one plugin in isolation without the platform context. This
    is the first in-corpus documentation of the agent's core architecture, multi-model
    support, and plugin extension model as a unified platform.
  - **First corpus documentation of model selection criteria for SQL agents**: Claim 3
    states a three-criteria heuristic for SQL agent model selection (cheap + fast +
    reliable SQLite). Prior corpus notes on model selection focus on general capability;
    this source specifies SQL query generation as a distinct capability criterion.
  - **First corpus example of stateful sandboxed code execution as an agent plugin**:
    The datasette-agent-sprites plugin (Fly Sprites persistent sandbox) introduces a
    new capability pattern: stateful code execution as an agent tool, distinct from
    retrieval or generation tools. The persistent sandbox means execution state carries
    across tool calls within a session.
  - **"Claw" personal AI architecture**: The "personal AI built around data from
    different parts of my digital life" framing connects SQL-queryable personal data
    stores to the personal AI assistant pattern. This is the first corpus source to
    name and describe this specific architecture (structured SQL retrieval over personal
    data imports vs. vector-search RAG).

- **Contradicts**: None identified. All existing corpus notes covering the Datasette
  LLM ecosystem are complementary. No contradiction issue required.

## Guide Impact

- **Chapter 02 (Harness Engineering — agent architecture and extensibility)**: Add
  Datasette Agent as a reference implementation of the composable plugin extension
  pattern. The key design principle: the core agent handles SQL querying and
  conversation loop; additional capabilities are separately-installable plugins that
  do not modify core agent code. Three working plugins confirm this is a real pattern,
  not a hypothetical design. Cite Claim 5 and the launch plugins summary in Concrete
  Artifacts. Pair with `blog-simonwillison-datasette-agent-charts.md` for the detailed
  plugin implementation story (permission gating, tool schema design).

- **Chapter 02 (Harness Engineering — model selection for SQL agents)**: Add Claim 3's
  model selection heuristic as a concrete example of capability-specific model choice.
  The guide should note that "reliable SQLite SQL generation" is a distinct capability
  criterion for SQL agents, not just general intelligence. Cite Claim 4 for the
  additional point that recent open-weights models increasingly meet this bar — local
  deployment of SQL agents is approaching commodity status.

- **Chapter 03 (Safety and Verification — tool permissions)**: This source provides
  the platform context for the datasette-agent-charts note's permission-gating claim
  (that note's Claim 3: `execute-sql` check before column discovery). The guide should
  reference both sources together: this note for the overall plugin architecture,
  the charts note for the specific permission enforcement pattern within plugins.

- **Chapter 04 (Context Engineering — personal data and SQL retrieval)**: Add the
  Claw personal AI concept (Claim 10) as an example of the "SQL over personal data
  stores" retrieval architecture. The agent-as-personal-assistant pattern provides
  exact answers from structured data imports, distinct from semantic RAG retrieval.
  Cite alongside `blog-simonwillison-inat-sightings.md` to show the full stack:
  data collection infrastructure (inat-sightings) + conversational SQL layer
  (Datasette Agent).

## Extraction Notes

- **Two primary sources fetched**: The simonwillison.net post and the Datasette
  project blog announcement were both fetched independently. The simonwillison.net
  post contains the local model command, the pelican demo response, the model choice
  rationale, and the plugin descriptions verbatim. The Datasette blog contributed
  the platform description, multi-model count, and plugin-building invitation.
- **Live demo not fully extracted**: agent.datasette.io is a live, interactive demo
  requiring a browser session; its conversation transcript beyond the pelican example
  could not be fetched via WebFetch. The pelican Q&A is the only verbatim conversation
  excerpt available.
- **Video not watched**: The announcement includes a demo video. The video content
  beyond the pelican example was not directly accessible.
- **Three plugins not deeply extracted**: datasette-agent-charts is covered in detail
  in `blog-simonwillison-datasette-agent-charts.md`. datasette-agent-openai-imagegen
  and datasette-agent-sprites were not separately fetched for this note — the brief
  descriptions from the announcement are sufficient for the claims and guide impact
  assessments.
- **Fragment URL**: The issue body URL includes `#atom-everything`. The `source_url`
  uses the canonical URL without the fragment, consistent with prior Willison source
  notes in this corpus.
- **No contradictions filed**: No existing corpus note makes claims about Datasette
  Agent's core platform that conflict with this source. No contradiction issue required.
- **datasette-agent-charts cross-reference verified**: Claim 7 in `blog-simonwillison-datasette-agent-charts.md` confirmed at lines 141–153 of that note ("datasette-agent-charts installs as a standard Datasette plugin alongside datasette-agent, following Datasette's composable plugin model."). The cross-reference resolves correctly.
