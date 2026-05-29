---
source_url: https://simonwillison.net/2026/May/20/datasette-agent-charts/
source_type: blog-post
title: "datasette-agent-charts 0.1a1"
author: Simon Willison
date_published: 2026-05-20
date_extracted: 2026-05-29
last_checked: 2026-05-29
status: current
confidence_overall: emerging
issue: "#984"
---

# datasette-agent-charts 0.1a1

> A brief release announcement for datasette-agent-charts, a Datasette plugin
> adding Observable Plot charting to the Datasette Agent system — notable for
> its permission-gated capability pattern (checking `execute-sql` before column
> discovery) and its composable plugin architecture that extends agent tools
> without modifying core agent code.

## Source Context

- **Type**: blog-post (a "beat" — Simon Willison's short-form release
  announcement format; the post links to the GitHub release at
  `https://github.com/datasette/datasette-agent-charts/releases/tag/0.1a1`,
  which contains the full release notes. Both pages were read.)
- **Author credibility**: Simon Willison is the creator of Datasette and the
  plugin's author. This is first-party release documentation — the release
  notes and README are authoritative for the tool's capabilities. The
  `0.1a1` version string signals early alpha. Willison has a track record of
  shipping functional alpha tooling quickly in the Datasette ecosystem (cf.
  `blog-simonwillison-datasette-llm-limits.md`). No vendor affiliation.
- **Scope**: Covers four specific changes in the 0.1a1 release: color
  improvements for bar/waffle charts, `execute-sql` permission checking,
  interactive tooltips, and a waffleY bug fix. The README documents the
  `render_chart` tool's full parameter schema. Does NOT cover: production
  deployment experience, performance under load, or how datasette-agent
  decides when to call render_chart vs. returning raw query results.

## Extracted Claims

### Claim 1: datasette-agent-charts extends datasette-agent with Observable Plot visualization via a `render_chart` tool that accepts SQL queries and structured chart configuration

- **Evidence**: GitHub README description and tool definition, authored by the
  plugin creator. The README is first-party documentation for what the plugin
  provides.
- **Confidence**: settled (first-party release documentation; the tool
  definition is authoritative for the plugin's interface)
- **Quote**: "Observable Plot charts for Datasette agent"
  *(Source: GitHub README, https://github.com/datasette/datasette-agent-charts)*
- **Our assessment**: This is the foundational claim of the plugin: it adds
  a dedicated visualization capability to datasette-agent rather than having
  the agent return raw data and let the UI handle rendering. The LLM chooses
  chart type, axes, and color encoding — the plugin handles Observable Plot
  rendering. This is a significant design choice: the LLM controls the visual
  specification, not just the data query.

### Claim 2: The `render_chart` tool encodes the full visual specification as structured LLM-callable parameters: database, SQL query, chart type, x/y axis columns, optional color column, title, and axis labels

- **Evidence**: GitHub README tool definition listing all parameters with their
  descriptions. The parameter list is authoritative for what the agent can
  specify.
- **Confidence**: settled (first-party README from the tool's author)
- **Quote**: (no direct prose quote; see Concrete Artifacts for the tool
  definition)
- **Our assessment**: The tool schema forces the LLM to specify the complete
  visual encoding — not just the data. The `color` field (optional) is
  particularly significant: when the LLM provides it, the plugin uses the
  categorical `observable10` color scheme; when absent, the plugin applies
  magnitude-based sequential shading (see Claim 4). This means the LLM's
  decision about whether to include a color column has a concrete effect on
  how the chart renders.

### Claim 3: The plugin gates visualization on the `execute-sql` Datasette permission before running column-discovery queries

- **Evidence**: Release note from the GitHub release page, confirmed by two
  independent WebFetch requests returning identical wording.
- **Confidence**: settled (first-party release note from the tool's author)
- **Quote**: "Now checks `execute-sql` permission before running the query to
  find the column names."
  *(Source: GitHub release notes, https://github.com/datasette/datasette-agent-charts/releases/tag/0.1a1)*
- **Our assessment**: This is the most architecturally significant change in
  0.1a1. The plugin's chart-rendering flow involves a preliminary query to
  discover column names before constructing the visualization query. Prior to
  this fix, that column-discovery query ran without checking whether the
  requesting actor had SQL execution rights. The fix makes the plugin
  permission-aware: an actor without `execute-sql` cannot trigger even the
  column-name lookup. For practitioners building agent plugins that access
  restricted data, this is a concrete example of the "check permissions before
  any query, including discovery queries" principle.

### Claim 4: Bar and waffle charts without a color column use sequential magnitude-based shading; text-value color columns use the `observable10` categorical color scheme

- **Evidence**: Release note from the GitHub release page, confirmed verbatim
  on both the GitHub release page and the blog post.
- **Confidence**: settled (first-party release note)
- **Quote**: "Bar and waffle charts without a color column are shaded by
  magnitude with a sequential color scheme; color columns holding text values
  use the `observable10` categorical scheme."
  *(Source: GitHub release notes, https://github.com/datasette/datasette-agent-charts/releases/tag/0.1a1)*
- **Our assessment**: This is a semantic color assignment rule: the plugin
  infers which color scheme to use based on whether a color column was
  provided and whether its values are numeric or textual. Sequential schemes
  (light-to-dark gradients) convey magnitude; categorical schemes (distinct
  hues) convey nominal categories. The plugin encodes this convention without
  requiring the LLM to specify it — the LLM decides *whether* to use a color
  column, and the plugin decides *how* to color it. This matches Observable
  Plot's own design conventions.

### Claim 5: Charts include interactive tooltips for agent-generated visualizations

- **Evidence**: Release note from the GitHub release page.
- **Confidence**: settled (first-party release note)
- **Quote**: "Charts now display interactive tooltips."
  *(Source: GitHub release notes, https://github.com/datasette/datasette-agent-charts/releases/tag/0.1a1)*
- **Our assessment**: Interactive tooltips add hover-based data point inspection
  to agent-generated charts — a standard data visualization UX pattern applied
  to LLM-generated output. For practitioners building agent tools that produce
  visual output, this demonstrates that "agent-generated" and "interactive" are
  not mutually exclusive. The chart is a rendered Observable Plot, so standard
  Observable Plot tooltip behavior applies.

### Claim 6: The `waffleY` chart type was previously inaccessible to the agent because it wasn't included in the agent's tool description — a bug where chart type support and agent awareness were out of sync

- **Evidence**: Release note from the GitHub release page.
- **Confidence**: settled (first-party release note)
- **Quote**: "Fixed a bug where `waffleY` charts were not being communicated to
  the agent."
  *(Source: GitHub release notes, https://github.com/datasette/datasette-agent-charts/releases/tag/0.1a1)*
  *(Note: the issue tracker link appended to the original text was `#2`; the
  core quote is reproduced verbatim above without the GitHub issue reference.)*
- **Our assessment**: This bug class — a capability exists in the rendering
  pipeline but is not declared in the agent's tool description — is easy to
  introduce when tool definitions are maintained separately from rendering
  logic. The agent could not call `render_chart` with `chart_type: waffleY`
  because the valid values in the tool description didn't include it. For
  practitioners: tool schema declarations and tool implementations must be kept
  in sync; the LLM can only request capabilities it has been told about.

### Claim 7: datasette-agent-charts installs as a standard Datasette plugin alongside datasette-agent, following Datasette's composable plugin model

- **Evidence**: GitHub README installation instructions.
- **Confidence**: settled (first-party README documentation)
- **Quote**: "datasette install datasette-agent-charts"
  *(Source: GitHub README, https://github.com/datasette/datasette-agent-charts)*
- **Our assessment**: The plugin is a separate installable package rather than
  a built-in datasette-agent feature. This mirrors how datasette-llm-limits is
  separate from datasette-llm (see `blog-simonwillison-datasette-llm-limits.md`
  Claim 2). Visualization is an opt-in capability: datasette-agent deployments
  without this plugin cannot generate charts. For practitioners, this means
  agents can be deployed with a minimal capability surface (just SQL querying)
  and extended with visualization only when needed.

### Claim 8: The plugin supports six chart types: barX, barY, line, dot, areaY, and waffleY

- **Evidence**: GitHub README `render_chart` tool definition listing valid
  `chart_type` values.
- **Confidence**: settled (first-party README from the tool's author)
- **Quote**: (no direct prose quote; see Concrete Artifacts for the tool
  definition)
- **Our assessment**: The six types cover the most common analytical chart
  forms: horizontal bars (barX), vertical bars (barY), line charts for time
  series, scatter plots (dot), area charts (areaY), and waffle charts for
  proportional data (waffleY). All are Observable Plot mark types. The LLM
  must select from this enumerated list — there is no free-text chart type
  parameter. Constraining the LLM to a fixed enum prevents hallucinated chart
  types that the rendering pipeline cannot handle.

## Concrete Artifacts

### `render_chart` Tool Definition (from GitHub README)

The tool the agent calls to generate charts:

```
Tool: render_chart
Parameters:
  database  — the database to query
  sql       — SQL query whose results become chart data
  chart_type — one of: barX, barY, line, dot, areaY, waffleY
  x         — column name for the x axis
  y         — column name for the y axis
  color     — (optional) column name for color encoding
  title     — (optional) chart title
  x_label   — (optional) x axis label
  y_label   — (optional) y axis label
```

*Source: GitHub README, https://github.com/datasette/datasette-agent-charts,
read 2026-05-29. Parameter names and descriptions are as rendered by WebFetch
from the repository's README; the exact YAML/JSON tool schema was not exposed
in the rendered page.*

### Installation Command (verbatim from README)

```
datasette install datasette-agent-charts
```

*Source: GitHub README, https://github.com/datasette/datasette-agent-charts*

### Release Notes (verbatim from GitHub release 0.1a1)

```
• More color! Bar and waffle charts without a color column are shaded by
  magnitude with a sequential color scheme; color columns holding text values
  use the observable10 categorical scheme. #2

• Now checks execute-sql permission before running the query to find the
  column names.

• Charts now display interactive tooltips.

• Fixed a bug where waffleY charts were not being communicated to the agent.
```

*Source: GitHub release page, https://github.com/datasette/datasette-agent-charts/releases/tag/0.1a1,
released 2026-05-20 by @simonw, commit 4492ca4e163dbf84164c95eab4a88c032a0b97b6*

### Example Agent Prompt (verbatim from README)

```
"Draw a bar chart of downloads over time"
```

*Source: GitHub README, https://github.com/datasette/datasette-agent-charts*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-llm-limits.md` Claim 2: That note documents
    the three-package composable stack for LLM cost governance (datasette-llm +
    datasette-llm-accountant + datasette-llm-limits). datasette-agent-charts
    follows the same composable plugin model: datasette-agent is the base layer,
    and datasette-agent-charts is an opt-in extension. Both demonstrate
    Datasette's architectural pattern of building LLM capabilities as independent,
    installable plugin layers rather than baking them into a monolithic agent.

  - `blog-simonwillison-datasette-llm-limits.md` Claim 7: That note documents
    0.1a0 alpha status for datasette-llm-limits. This source is at 0.1a1 — same
    alpha lifecycle stage. Both are early alpha releases from the same ecosystem
    with provisional configuration schemas. Together they show Willison's practice
    of shipping minimal viable alpha releases quickly and iterating in public.

- **Contradicts**: None identified. No existing corpus note makes claims about
  datasette-agent-charts, Observable Plot integration for agent tools, or the
  specific patterns documented here that would conflict with these findings.

- **Extends**:
  - `blog-simonwillison-datasette-llm-limits.md` overall: That note documents
    the cost-governance layer of Datasette's LLM plugin ecosystem. This source
    documents the visualization layer of the same ecosystem. Together, they
    show the breadth of what Willison is building: an incrementally composable
    LLM-powered data platform where each plugin addresses a distinct concern
    (cost governance, visualization, etc.) as a separate installable unit.

  - `blog-simonwillison-datasette-blog-codex-session.md` overall: That note
    documents a Codex Desktop session building Datasette blog infrastructure.
    This source shows the same Datasette ecosystem gaining LLM-driven
    visualization capabilities. Together they bracket the scope of Willison's
    concurrent Datasette work: AI-assisted infrastructure development (the
    Codex session) and AI-powered data querying and visualization (datasette-agent
    + datasette-agent-charts).

- **Novel**:
  - **First corpus source documenting Observable Plot integration for
    agent-generated visualization**: No existing corpus note describes a pattern
    where an LLM specifies chart type, axis columns, and color encoding via a
    structured tool call, and a rendering pipeline produces an interactive
    Observable Plot chart. This is a distinct agent output pattern — not
    text, not raw data, but a rendered interactive visualization.
  - **First corpus documentation of permission-gating a visualization capability
    at the column-discovery level**: The `execute-sql` check before running the
    column-name lookup (not just the data query) is a specific, non-obvious
    implementation detail. Prior corpus notes on agent permissions (e.g.,
    enterprise agent notes) discuss permission gating at an abstract level;
    this is a concrete example of gating even the preparatory queries that
    support a capability.
  - **First corpus example of a tool description/implementation sync bug class**:
    The `waffleY` omission demonstrates a specific bug pattern: a chart type
    is implemented in the rendering layer but not declared in the LLM tool
    description, making it invisible to the agent. This bug class is
    generalizable to any multi-layer agent tool architecture.
  - **First documented `render_chart` tool schema for agent-driven charting**:
    The combination of SQL + chart_type enum + axis columns + optional color
    as a structured LLM-callable tool is a concrete, reusable pattern for
    agent visualization capabilities.

## Guide Impact

- **Chapter 03 (Agent Tool Design — structured output tools)**: Add the
  `render_chart` tool schema as a reference example for designing agent tools
  that combine data access (SQL query) with structured output specification
  (chart type + encoding). The key design choice — using a fixed chart_type
  enum rather than free-text — prevents hallucinated chart types and is
  worth highlighting. The LLM controls the full visual specification within
  a constrained, validated parameter set.

- **Chapter 04 (Agent Permissions — gating discovery queries)**: Add the
  `execute-sql` permission check before column-name discovery as a concrete
  example of the "check permissions before any query, including preparatory
  queries" principle. The guide should note that agent tools often make
  preliminary queries (schema inspection, column listing, metadata lookup)
  before the primary query — all of these should be permission-gated, not
  just the final data query.

- **Chapter 04 (Composable Plugin Architecture)**: Add datasette-agent +
  datasette-agent-charts as a reference example of the composable plugin
  extension pattern: the base agent provides SQL querying; visualization is
  a separate, installable capability. The guide should present this alongside
  the datasette-llm-limits pattern (from `blog-simonwillison-datasette-llm-limits.md`)
  as two examples of the same Datasette plugin architecture applied to
  different concerns (visualization vs. cost governance).

- **Chapter 03 (Agent Tool Implementation — schema/implementation sync)**:
  Add the `waffleY` bug (tool not described to agent) as a documented failure
  mode. The guide should recommend that agent tool implementations include
  automated tests that verify every enumerated tool parameter value is
  both implemented in the rendering layer AND declared in the tool description
  passed to the LLM. A value present in one place but not the other silently
  degrades capability.

## Extraction Notes

- **Very thin primary source**: The blog post at simonwillison.net is a "beat"
  in Simon Willison's format — a brief release announcement that links to the
  GitHub release. Total blog post content is minimal. The substantive release
  notes are at the GitHub release page, and the tool schema is in the README.
  Both were fetched separately.
- **Quote sourcing**: The four release-note bullet points were obtained
  independently from both the blog post and the GitHub release page via
  WebFetch, returning consistent wording on both fetches of each URL. The
  WebFetch model refused to reproduce the full page verbatim but confirmed
  the bullet-point wording character-for-character on repeated queries. The
  README tool definition parameters were obtained from the GitHub repository
  page; the exact internal tool schema format (JSON/YAML) was not exposed in
  the rendered page.
- **Related source note not yet merged**: Issue #869 (datasette-agent 0.1a1)
  had miner PRs opened (#881, #918) but no source note exists in the current
  `source-notes/` directory. Cross-references to datasette-agent core
  capabilities cannot be cited to a specific claim number in a corpus note
  since that note is not present. If the datasette-agent source note is merged
  in the future, Claim 3 (permission gating) and Claim 7 (plugin installation)
  in this note should be updated to cross-reference it.
- **No contradictions filed**: No existing corpus note makes claims about
  datasette-agent-charts, Observable Plot visualization for agents, or the
  specific patterns documented here. No contradiction issue required.
- **Alpha version caveat**: Both the blog post title ("0.1a1") and the GitHub
  release label ("Pre-release") confirm this is early alpha software. The
  `render_chart` parameter schema may change before a stable release.
  Practitioners should treat the tool definition as illustrative of the
  pattern, not as a stable API contract.
