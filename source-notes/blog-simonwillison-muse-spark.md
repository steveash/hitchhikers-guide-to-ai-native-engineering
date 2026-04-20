---
source_url: https://simonwillison.net/2026/Apr/8/muse-spark/
source_type: blog-post
title: "Meta's new model is Muse Spark, and meta.ai chat has some interesting tools"
author: Simon Willison
date_published: 2026-04-08
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: anecdotal
issue: "#169"
---

# Meta's new model is Muse Spark, and meta.ai chat has some interesting tools

> Simon Willison's hands-on exploration of meta.ai's 16-tool commercial harness documents
> two vendor-convergence data points relevant to harness engineering: the file-editing
> primitives (view/insert/str_replace) independently match Claude's text editor tool API
> shape, and `subagents.spawn_agent` appearing as a first-class tool in a major commercial
> product further validates sub-agent delegation as a stable harness primitive.

## Source Context

- **Type**: blog-post (link-blog + hands-on exploration; ~800 words plus tool list and
  test results; Willison's recurring pelican SVG benchmark applied to Muse Spark)
- **Author credibility**: Simon Willison is the creator of Django, a prolific open-source
  engineer, and one of the most widely-cited commentators on LLM tooling. His recurring
  pelican-on-a-bicycle SVG test is an informal but consistent cross-model benchmark. He
  documents what the model actually does, not what vendors claim it does — his observations
  are practitioner-grade anecdote, not vendor marketing. He has no affiliation with Meta.
  Claims should be treated as accurate first-person observation, not controlled evidence.
- **Scope**: Covers one model (Muse Spark), one interface (meta.ai chat via
  Facebook/Instagram login), one session's worth of tool discovery. Does NOT cover:
  API access (private preview at time of writing), model benchmark methodology, detailed
  performance comparisons, or any practitioner workflow experience with the model. The
  post is a first-impression exploration, not a production evaluation. The key signal is
  the tool list itself and Willison's cross-vendor pattern observation.

## Extracted Claims

### Claim 1: Meta's Muse Spark is hosted rather than open-weights, marking a significant shift from Meta's prior model release strategy

- **Evidence**: Willison states directly: "API access currently limited to select users
  via private preview." The model is accessible via meta.ai chat but not via open weights
  or a public API at time of publication.
- **Confidence**: settled (factual statement; corroborated by Meta's own announcement)
- **Quote**: "Meta announced Muse Spark, their first model since Llama 4 nearly a year
  prior. The model is hosted rather than open-weights."
- **Our assessment**: The strategic shift matters to the harness engineering picture: Meta
  joining the hosted-model tier (alongside Anthropic, OpenAI, Google) means the major AI
  vendors are all now competing on agentic tool surface, not just model weights. For
  practitioners, the tool API design choices made by commercial hosts are the relevant
  signal — not the model weights themselves.

### Claim 2: The file-editing tool API in meta.ai (container.view / container.insert / container.str_replace) matches the pattern of Claude's text editor tool, suggesting cross-vendor convergence on a common primitive

- **Evidence**: Willison's direct observation of the tool list returned by the model when
  asked about its capabilities. He explicitly flags the pattern match: "container.view,
  container.insert, and container.str_replace enable file editing, mirroring patterns in
  Claude's text editor tool commands." The three-function API surface (view, insert,
  str_replace) is the same decomposition Claude uses.
- **Confidence**: anecdotal (single author's direct observation; no controlled comparison
  or official vendor confirmation of intentional alignment)
- **Quote**: "container.view, container.insert, and container.str_replace enable file
  editing, mirroring patterns in Claude's text editor tool commands"
- **Our assessment**: This is the most harness-engineering-relevant signal in the post.
  When two major AI vendors independently arrive at the same three-function decomposition
  for file editing (view / insert / str_replace), it is evidence that this API shape is
  a natural fit for the task — not an arbitrary design choice. For practitioners designing
  custom harnesses with file-editing tools, this convergence is a signal to adopt the same
  decomposition rather than inventing a different primitive set. The str_replace pattern
  in particular (replace a specific string rather than rewrite the whole file) reduces
  token cost and avoids full-file overwrites — the vendors may have converged here because
  the practical advantages forced the same solution.

### Claim 3: `subagents.spawn_agent` appearing as a first-class tool in meta.ai's commercial product further validates sub-agent delegation as a standard harness primitive

- **Evidence**: Tool list returned by the model: "`subagents.spawn_agent` spawns
  independent agents for research, analysis, or delegation, returning text responses."
  This is a first-party commercial product (meta.ai), not a research prototype.
- **Confidence**: anecdotal (single commercial product; no usage metrics, failure modes,
  or practitioner experience report)
- **Quote**: "`subagents.spawn_agent` spawns independent agents for research, analysis,
  or delegation, returning text responses"
- **Our assessment**: The signal here is vendor adoption, not practitioner experience.
  When Claude Code (Task tool), GitHub Agentic Workflows (spawn patterns), and now meta.ai
  (`subagents.spawn_agent`) all surface sub-agent delegation as a named first-class tool,
  the pattern has graduated from practitioner experiment to commercial standard. This does
  not tell us how well `subagents.spawn_agent` works in meta.ai, but it does tell us that
  every major hosted AI platform now exposes sub-agent spawning as a core capability.
  Practitioners designing harnesses should treat sub-agent delegation as a supported
  primitive, not an advanced hack.

### Claim 4: meta.ai exposes 16 tools across 6 categories, constituting a full-featured commercial AI harness reference architecture

- **Evidence**: The model itself enumerated its full tool suite when asked. Categories:
  Browse & Search (3 tools), Meta Content Search (2 tools), Image Generation (1 tool),
  Code Execution (1 tool), File & Web Artifacts (4 tools), Visual Analysis (1 tool),
  Sub-agents (1 tool), Account Linking (1 tool). Full list documented in Concrete
  Artifacts below.
- **Confidence**: settled (first-party disclosure; the model listed its own tools)
- **Quote**: (see full tool list in Concrete Artifacts)
- **Our assessment**: The 16-tool taxonomy is a useful reference for practitioners
  designing harnesses. It represents what Meta's team decided was the right set of
  primitives for a general-purpose AI assistant at commercial scale. The categories
  (search, code execution, file operations, visual analysis, sub-agents, account linking)
  are a vendor's answer to "what tools should a capable AI harness provide?" Notably
  absent: any explicit memory/persistence tool (context is presumably managed through
  the container filesystem). This is one data point in an emerging design space, not a
  normative specification.

### Claim 5: The Python execution environment in meta.ai is sandboxed with a specific, stable library set and persistent `/mnt/data/` storage

- **Evidence**: Tool description: "Python 3.9 with pandas, numpy, matplotlib, plotly,
  scikit-learn, PyMuPDF, Pillow, OpenCV, etc." with file persistence at `/mnt/data/`.
  Willison confirmed Python 3.9.25 and SQLite 3.34.1 via direct testing.
- **Confidence**: settled (Willison directly verified the runtime version)
- **Quote**: "container.python_execution provides 'Python 3.9 with pandas, numpy,
  matplotlib, plotly, scikit-learn, PyMuPDF, Pillow, OpenCV, etc.' with file persistence
  at `/mnt/data/`"
- **Our assessment**: The persistence path (`/mnt/data/`) and the fixed library set are
  the practically relevant facts. Practitioners designing data analysis pipelines on
  meta.ai's platform can plan around this library set. The Python 3.9 runtime is notably
  older than current (3.12+), which may constrain newer syntax or library versions. For
  harness designers: providing a persistent storage path as part of the execution
  environment spec is a concrete pattern worth adopting when designing custom code
  execution tools.

### Claim 6: `container.visual_grounding` provides multi-mode object localization — bounding boxes, point coordinates, and counts — as a first-class AI harness tool

- **Evidence**: Willison tested all three output modes. Point mode returned pixel
  coordinates. Bounding box mode returned normalized 0-1000 coordinates showing nested
  relationships (face inside raccoon, eyes inside face). Count mode returned JSON with
  object names, locations, and counts (e.g., 12 raccoon whiskers, 8 paw claws, 3 trash
  items). He generated a custom HTML visualization of the point results.
- **Confidence**: anecdotal (single session, specific image type)
- **Quote**: "Bounding Box Mode: Provided normalized 0-1000 coordinate boxes around
  detected objects, showing nested relationships"
- **Our assessment**: The three-format output (bbox/point/count) is a thoughtful API
  design — different downstream uses need different representations of the same
  localization result. The ability to get nested bounding boxes (face inside raccoon,
  eyes inside face) is non-trivial. For harness designers: visual grounding as a tool
  primitive — returning structured localization data rather than embedding it in prose —
  is the right pattern for interoperability with downstream code.

### Claim 7: Meta's proprietary content search tools (meta_1p.content_search) provide semantic access to the user's Instagram/Threads/Facebook posts as harness context

- **Evidence**: Tool description: "semantic search across Instagram, Threads, and
  Facebook posts" for content the user can view, created since January 1 2025, with
  parameters including `author_ids`, `key_celebrities`, `commented_by_user_ids`, and
  `liked_by_user_ids`.
- **Confidence**: settled (first-party tool description; no independent testing of the
  search quality)
- **Quote**: "meta_1p.content_search enables 'Semantic search across Instagram, Threads,
  and Facebook posts' for content the user can view created since January 1, 2025"
- **Our assessment**: This is a vendor-specific context-enrichment pattern: using the
  platform's proprietary data as harness context. It is architecturally analogous to how
  an enterprise AI assistant might search internal Slack/email/calendar data. For
  harness designers: the meta_1p pattern (platform-native semantic search returning
  structured posts with social graph parameters) illustrates how context tools can
  combine retrieval with social relationship filtering. The January 2025 cutoff is a
  practical constraint worth noting — pre-2025 content is not accessible.

### Claim 8: Muse Spark achieves benchmark parity with frontier models using "over an order of magnitude less compute" than Llama 4 Maverick

- **Evidence**: Meta's own claim quoted in the blog post. Artificial Analysis
  independently scored Muse Spark at 52 on their composite benchmark, behind only
  Gemini 3.1 Pro, GPT-5.4, and Claude Opus 4.6.
- **Confidence**: anecdotal (Meta's self-reported efficiency claim; benchmark score is
  third-party but single measurement)
- **Quote**: "achieving 'same capabilities with over an order of magnitude less compute
  than our previous model, Llama 4 Maverick'"
- **Our assessment**: The efficiency claim is vendor-stated and should be treated with
  skepticism until independently replicated. The Artificial Analysis ranking (52nd
  overall, top 4) is more credible as a third-party measurement but benchmark selection
  matters. For practitioners: the practical takeaway is that Meta's hosted model is
  competitive with current frontier models, not that the efficiency claim is verified.
  The relevance to harness engineering is limited — model capability matters for output
  quality, but harness design decisions are largely model-agnostic at this tier.

## Concrete Artifacts

### Full 16-Tool Suite (meta.ai, April 2026)

As enumerated by the model when asked directly:

```
Browse & Search:
  browser.search         — web searches via undisclosed engine
  browser.open           — loads full pages from search results
  browser.find           — pattern matching against retrieved content

Meta Content Search:
  meta_1p.content_search — semantic search across Instagram/Threads/Facebook
                           (user-accessible content, since 2025-01-01)
                           params: author_ids, key_celebrities,
                                   commented_by_user_ids, liked_by_user_ids
  meta_1p.meta_catalog_search — Meta product catalog search

Image Generation:
  media.image_gen        — text-to-image; modes: "artistic" / "realistic"
                           formats: "square" / "vertical" / "landscape"

Code Execution:
  container.python_execution — Python 3.9.25 sandbox
                               libs: pandas, numpy, matplotlib, plotly,
                                     scikit-learn, PyMuPDF, Pillow, OpenCV
                               persistence: /mnt/data/
                               also: SQLite 3.34.1 available

File & Web Artifacts:
  container.create_web_artifact — HTML+JS sandboxed iframes (html/svg kinds)
  container.view                — view file contents
  container.insert              — insert content into file
  container.str_replace         — replace string in file
  container.file_search         — search uploaded files, extract passages
  container.download_meta_1p_media — retrieve media from Meta sources
                                     params: post_id / catalog_search_citation_id

Visual Analysis:
  container.visual_grounding   — object localization
                                 params: object_names, image_path, format_type
                                 format_type: "bbox" | "point" | "count"
                                 bbox: normalized 0-1000 coordinate boxes
                                 point: pixel-level coordinates
                                 count: JSON {name, location, count}

Sub-agents:
  subagents.spawn_agent        — delegate to independent agents
                                 returns: text response

Account Linking:
  third_party.link_third_party_account — Google Calendar / Outlook Calendar
                                         Gmail / Outlook
```

*Source: Willison, simonwillison.net/2026/Apr/8/muse-spark/ — model self-enumeration*

### File-Editing API Convergence: Claude vs. meta.ai

```
Claude text editor tool (Anthropic):    meta.ai container tools (Meta):
  str_replace_editor view              →  container.view
  str_replace_editor str_replace       →  container.str_replace
  str_replace_editor insert            →  container.insert
  str_replace_editor create            →  (container.create_web_artifact / implicit)
```

Willison's observation: these tools are "becoming a common pattern across any
file-equipped agent harness."

*Source: Willison, simonwillison.net/2026/Apr/8/muse-spark/*

### Visual Grounding Output Examples (raccoon image test)

```json
// Count mode output (partial)
{
  "raccoon_whiskers": {"count": 12, "locations": [...]},
  "paw_claws":        {"count": 8,  "locations": [...]},
  "trash_on_head":    {"count": 3,  "locations": [...]},
  "eyes":             {"count": 2,  "locations": [...]},
  "ears":             {"count": 2,  "locations": [...]}
}

// Bounding box output shows nested containment:
// face bbox ⊂ raccoon bbox
// eyes bbox ⊂ face bbox
// hat components overlap with raccoon bbox
```

*Source: Willison, simonwillison.net/2026/Apr/8/muse-spark/*

## Cross-References

- **Corroborates**:
  - **blog-addyosmani-code-agent-orchestra** (Claim 3 — subagents via the Task tool
    validate parallel decomposition): Osmani documents Claude Code's Task tool as the
    sub-agent spawning primitive; meta.ai's `subagents.spawn_agent` is a second
    independent commercial implementation of the same pattern. Together they confirm
    sub-agent delegation is not Claude-specific but a cross-platform harness primitive.
  - **blog-addyosmani-code-agent-orchestra** (Claim 11 — five patterns to adopt; git
    worktrees, subagents, quality gates): The meta.ai tool suite's architecture aligns
    with several of these patterns: sub-agent spawning, code execution sandbox, file
    editing — the same primitives Osmani recommends practitioners build into their
    harnesses are what Meta shipped commercially.
  - **discussion-hn-kiln-orchestration** (Claim 4 — one worktree per issue for
    isolation): The container-based isolation in meta.ai (each session gets its own
    `/mnt/data/` sandbox) is the commercial implementation of the same isolation
    principle Kiln applied at the git worktree level.

- **Contradicts**: None. No existing source note makes claims that conflict with this
  source's observations. The sub-agent and file-editing patterns documented here
  corroborate rather than contradict existing notes.

- **Extends**:
  - **blog-simonwillison-glm51**: Same author, same pelican test methodology, different
    model. The GLM-5.1 note covers open-weights model access; this note covers a
    hosted commercial harness. Together they show Willison's consistent cross-model
    evaluation approach, making his observations comparable across posts.
  - **blog-addyosmani-code-agent-orchestra**: Osmani's post describes sub-agent patterns
    and file-editing as practitioner recommendations. This source provides a commercial
    vendor data point: Meta independently shipped the same primitives at production scale,
    which moves the patterns from "practitioner best practice" toward "emerging industry
    standard."

- **Novel**:
  - **Cross-vendor tool API convergence on view/insert/str_replace**: No existing source
    in the corpus documents two major AI vendors (Anthropic and Meta) independently
    converging on the same file-editing tool API decomposition. This is the first
    cross-vendor convergence evidence in the corpus.
  - **`subagents.spawn_agent` as a named commercial tool**: While sub-agent patterns are
    covered in Osmani and Kiln, no existing note documents a major commercial AI platform
    (not a research prototype or community tool) exposing sub-agent spawning as a named
    first-class tool. This is new.
  - **meta_1p social context tools**: No existing note covers social media content
    (Instagram/Threads/Facebook posts) as a harness context source. This is a
    vendor-specific pattern but illustrates a broader class: platform-native data as
    AI tool context.
  - **container.visual_grounding with three output modes**: Multi-mode structured object
    localization (bbox/point/count) as a tool primitive is not described elsewhere in
    the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — Tool Design)**: The view/insert/str_replace
  convergence is the strongest argument in the corpus for recommending this specific
  API decomposition when building custom file-editing tools. Currently the chapter
  describes what Claude Code's text editor tool does; this source adds the data point
  that Meta arrived at the same decomposition independently. Recommend updating to say:
  "The view/insert/str_replace decomposition has emerged independently across multiple
  AI vendors. When designing custom file-editing tools for your harness, this API shape
  is a natural fit — not an arbitrary Claude-specific choice."

- **Chapter 02 (Harness Engineering — Tool Taxonomy)**: The meta.ai 16-tool suite is
  a concrete commercial reference for "what tools does a general-purpose AI harness
  need?" The taxonomy (search, code execution, file operations, visual analysis,
  sub-agents, account linking) is a vendor's answer to this question. The guide can
  reference it alongside Claude Code's built-in tools as a cross-vendor benchmark for
  harness completeness.

- **Chapter 01 (Daily Workflows) or Chapter 02 (Multi-agent primitives)**: The
  `subagents.spawn_agent` commercial release is a data point for the claim that
  sub-agent delegation is now a stable harness primitive rather than an advanced
  experiment. Updating the chapter to note that meta.ai, Claude Code (Task tool), and
  GitHub Agentic Workflows all expose sub-agent spawning as a named first-class tool
  would strengthen the recommendation to design for sub-agent patterns from the start.

## Extraction Notes

- **Thin source with two high-signal observations**: As the Prospector correctly
  assessed, this is a product announcement + exploration post with narrow practitioner
  signal. The value is concentrated in (1) the file-editing API convergence observation
  and (2) the `subagents.spawn_agent` commercial confirmation. The 16-tool taxonomy is
  a useful reference artifact but not a deep analytical finding.
- **No sub-pages followed**: The post does not link to sub-pages with substantive
  content. The meta.ai interface itself is the source, and Willison's tool list
  enumeration is the primary artifact.
- **Tool list is self-reported by the model**: The 16-tool list came from asking the
  model to describe its capabilities. This is a direct disclosure, not reverse-engineered
  — but it may not reflect all tools available or may include tools not yet fully
  deployed. Treat as accurate at time of writing (April 8, 2026).
- **Benchmark claims**: The Artificial Analysis score (52) and Meta's efficiency claim
  ("order of magnitude less compute") are included for completeness but are not the
  focus of this extraction. Benchmark comparisons age quickly; the structural observations
  (tool design, API shape) are more durable.
