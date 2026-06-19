---
source_url: https://simonwillison.net/2026/Jun/11/datasette/
source_type: blog-post
title: "datasette 1.0a33"
author: Simon Willison
date_published: 2026-06-11
date_extracted: 2026-06-19
last_checked: 2026-06-19
status: current
confidence_overall: anecdotal
issue: "#1216"
---

# datasette 1.0a33

> A short annotated-release-notes post that introduces two distinct signals: the `?_extra=` composable API pattern extended to all three Datasette page types (tables, rows, queries), and a concrete planning/implementation cross-model split — Claude Fable 5 in Claude Code for architecture, GPT-5.5 xhigh in Codex Desktop for code — producing a published interactive API explorer tool that Willison frames as evidence that "API explorer tools are almost free to build now."

## Source Context

- **Type**: blog-post (simonwillison.net, annotated-release-notes format; tagged `annotated-release-notes 55`, `datasette 1,519`, `ai-assisted-programming 390`, `projects 538`. Short-form release announcement with personal technical commentary; links to a full Datasette project blog post at `datasette.io/blog/2026/api-extras/` for deeper documentation.)
- **Author credibility**: Simon Willison is the creator of Datasette, Django, and the `llm` Python CLI. He is the primary developer of Datasette and the author of this feature (`?_extra=` was his own design decision from 2023). This is first-party project announcement documentation — he is describing his own design choices in his own tool. He is a trusted-feed source in this corpus (`blog-simonwillison-datasette-agent.md`, `blog-simonwillison-datasette-llm-limits.md`, `blog-simonwillison-liteparse-browser.md`, `blog-simonwillison-fable-relentlessly-proactive.md`). No vendor affiliation with Anthropic or OpenAI.
- **Scope**: The simonwillison.net post is a short annotated release note covering: (1) Datasette 1.0a33 release, (2) extension of the `?_extra=` pattern to query and row pages, (3) the AI-assisted API explorer tool he built to demonstrate it. The datasette project blog post (`datasette.io/blog/2026/api-extras/`, which returned HTTP 500 at extraction time but was accessible via targeted fetch) provides the technical depth: the verbosity problem the pattern solves, the URL parameter syntax, and the list of available extras. Does NOT cover: internal Datasette implementation details, migration guidance for existing API clients, performance benchmarks for the extras mechanism, or detailed comparison between Claude Fable 5 and GPT-5.5 on this task.

## Extracted Claims

### Claim 1: Datasette 1.0a33 extends the `?_extra=` JSON API pattern from table pages to cover query and row pages, completing its coverage across all three Datasette page types

- **Evidence**: First-party release announcement from the tool's creator. The `?_extra=` pattern was originally introduced in Datasette 1.0a3 (released 2023-08-09) and previously applied only to table pages. The 1.0a33 release extends it to query pages and row pages.
- **Confidence**: settled (first-party release documentation from the tool's creator; the changelog and documentation are authoritative)
- **Quote**: (no direct verbatim prose quote available; the post describes this extension alongside a link to the updated documentation)
- **Our assessment**: This is an incremental but significant completeness fix: the pattern was previously inconsistent — table pages supported extras but query and row pages did not. Extending coverage to all three page types allows clients to write uniform API calls regardless of which page type they are requesting. For API design: consistency across endpoint families reduces client complexity and removes awkward "this only works for tables" carve-outs from documentation. The companion datasette project blog post (`datasette.io/blog/2026/api-extras/`) provides the technical depth that the simonwillison.net post does not.

### Claim 2: The `?_extra=` pattern addresses the API verbosity problem — Datasette normally returns more JSON than clients need, wasting SQL queries to generate unused data

- **Evidence**: The datasette project blog post (`datasette.io/blog/2026/api-extras/`) states the motivation explicitly. Multiple extras are SQL-backed: fetching them when clients don't need them wastes database queries.
- **Confidence**: settled (first-party rationale from the tool's creator; the SQL-backed extras mechanism is Willison's own design)
- **Quote**: "Datasette usually returns more JSON than the client needs, often wasting SQL queries to generate data that is not used."
  *(Source: datasette project blog, datasette.io/blog/2026/api-extras/, read 2026-06-19)*
- **Our assessment**: The verbosity problem is a classic API design tension: returning everything by default reduces friction for simple clients but penalizes clients that only need a subset of the response. The `?_extra=` solution is opt-in enrichment rather than opt-out reduction — clients request the extras they need. This is architecturally similar to GraphQL's field selection mechanism but without requiring a schema query language. For practitioners designing JSON APIs: the query-parameter-as-field-selector pattern (`?_extra=field`) is a lower-friction alternative to full GraphQL for APIs where response verbosity and SQL cost are real concerns.

### Claim 3: The `?_extra=` mechanism works by appending one or more `?_extra=<name>` parameters to a Datasette JSON URL; each extra adds a corresponding key to the JSON response

- **Evidence**: The datasette project blog provides a concrete URL example demonstrating the multi-extra pattern. The interactive explorer at `tools.simonwillison.net/datasette-extras-explorer` shows checkboxes for ~30 named extras.
- **Confidence**: settled (first-party; the URL pattern and mechanism are authoritative from the tool's creator)
- **Quote**: (no direct prose quote; see Concrete Artifacts for the verbatim URL example)
- **Our assessment**: The additive URL parameter approach (`?_extra=count&_extra=count_sql&_extra=expandable_columns`) is a zero-breaking-change extension mechanism: existing clients that don't add the parameter receive the same response they always did. New clients that want enriched responses add the parameters they need. This backward compatibility property makes `?_extra=` a safer API evolution pattern than versioning or default-response changes. The named-extra registry (shared across all page types) also means client code can use the same extra names regardless of whether it is querying a table, a row, or a query result.

### Claim 4: Willison built an interactive API explorer for the `?_extra=` pattern using a cross-model planning/implementation split: Claude Fable 5 in Claude Code for the plan, GPT-5.5 xhigh in Codex Desktop for the implementation

- **Evidence**: Willison's direct statement in the post describing the tool-building workflow. The resulting tool is publicly deployed and verifiable at `tools.simonwillison.net/datasette-extras-explorer`.
- **Confidence**: anecdotal (first-person practitioner account; the tool's existence is publicly verifiable but the model split is self-reported)
- **Quote**: "I had Claude Fable 5 in Claude Code (for the plan) and GPT-5.5 xhigh in Codex Desktop (for the implementation) build me this custom extras API explorer"
- **Our assessment**: This is the most significant signal in the post from a workflow patterns perspective. Willison explicitly divided the task by role: Claude Fable 5 handled architectural planning (deciding what the explorer should do and how it should be structured); GPT-5.5 xhigh handled implementation (writing the actual code). The two models ran in different tools (Claude Code vs. Codex Desktop), so the split is also an environment split. Prior in-corpus Willison examples used a cross-model pattern for verification (GPT-5.5/Codex auditing a Claude Code build in `blog-simonwillison-liteparse-browser.md` Claim 11); this is the first in-corpus example of a planning/implementation division of labor across vendor models, not just verification.

### Claim 5: Willison chose the cross-model split because "API explorer tools are almost free to build now," illustrating capability-driven development — the perceived cost drop changes what's worth building

- **Evidence**: Willison's explicit framing in the post — the cross-model build was motivated by the low perceived cost of the task, not by a technical requirement for two models.
- **Confidence**: anecdotal (practitioner opinion from a high-signal author; the completed tool confirms the task was viable but doesn't measure effort independently)
- **Quote**: "Because API explorer tools are almost free to build now"
- **Our assessment**: This is the strongest guide-relevant claim in the source. The statement is not about Datasette's API — it is about what AI-assisted development has done to the economics of interactive tooling. An API explorer requires: a URL input, a checkbox panel showing available options, live preview of JSON responses, and UI state management. Without AI assistance, this would take a frontend developer hours or days. With AI assistance (planning + implementation across two models), Willison framed it as a near-zero-cost task. The implication is directly capability-driven: the tool class is not new; what is new is that the cost of building one has dropped far enough to make it worth building ad hoc for a release announcement. Compare `blog-simonwillison-liteparse-browser.md` Claim 12 ("blast radius" framing for vibe-coded browser apps): both posts document Willison shipping browser tools rapidly with minimal human review because the cost and risk are low.

### Claim 6: The resulting extras explorer tool (`tools.simonwillison.net/datasette-extras-explorer`) provides an interactive, self-documenting demonstration of the `?_extra=` pattern — URL input, extras checkboxes, and live JSON preview

- **Evidence**: The post includes a screenshot of the tool and provides its URL. The tool is publicly deployed and accessible.
- **Confidence**: settled (the tool exists at the stated URL and the screenshot confirms its structure)
- **Quote**: (no direct prose quote; the post describes it as a "custom extras API explorer")
- **Our assessment**: The interactive explorer serves a documentation purpose that static docs cannot: a developer can enter any Datasette URL and immediately see which extras are available and what they add to the response. This makes the `?_extra=` pattern self-discoverable — a developer who hasn't read the docs can explore the available extras by checking boxes and watching the JSON change. The tool was built specifically to make the API more accessible, not as a standalone product. For practitioners: "build the interactive demo" is now a viable documentation strategy for any feature that benefits from visual exploration. The tooling cost to do so is near zero with AI assistance.

### Claim 7: The `?_extra=` pattern is now formally documented in the Datasette JSON API documentation

- **Evidence**: The simonwillison.net post states the pattern "is also now documented" and links to `docs.datasette.io/en/latest/json_api.html#json-api-extra`.
- **Confidence**: settled (the post links to the documentation; the documentation URL is verifiable)
- **Quote**: (no direct verbatim quote; paraphrase: the post states the pattern is now documented)
- **Our assessment**: Documentation completeness is a precondition for the pattern being adoptable. Before this release, `?_extra=` was available only on table pages and had limited documentation. The 1.0a33 release simultaneously extends coverage (to queries and rows) and completes the documentation — making the pattern coherent enough to recommend and adopt consistently. The interactive explorer complements the documentation by making the pattern explorable without reading the docs.

### Claim 8: GPT-5.5 xhigh (Codex Desktop) was used for the implementation role while Claude Fable 5 (Claude Code) was used for planning — Willison does not provide a rationale for the specific model-tool assignments

- **Evidence**: The post states the assignment but provides no explanation of why Fable handled planning vs. implementation, or why GPT-5.5 xhigh was chosen for implementation.
- **Confidence**: anecdotal (practitioner choice; no rationale given)
- **Quote**: (same as Claim 4 — "I had Claude Fable 5 in Claude Code (for the plan) and GPT-5.5 xhigh in Codex Desktop (for the implementation)")
- **Our assessment**: The absence of a stated rationale means we can't extract a "use Fable for planning, GPT-5.5 for implementation" principle from this single data point. It may reflect subscription availability (Willison uses both Claude Code and Codex Desktop), tool preference, or deliberate experimentation. What we can state is that the pattern is consistent with Willison's documented multi-model habits: he regularly uses Claude and GPT-5.5 in complementary roles within the same project (`blog-simonwillison-liteparse-browser.md` Claim 11, `blog-simonwillison-gpt55-codex-plugin.md` overall). The trend — multiple models, different roles, same project — is the extractable pattern, not the specific model-to-role assignment.

## Concrete Artifacts

### `?_extra=` URL Pattern (from datasette project blog, datasette.io/blog/2026/api-extras/)

```
# Basic pattern: append one or more ?_extra= parameters to any Datasette JSON URL
# Each extra adds a corresponding key to the JSON response object

# Example with multiple extras on a table page:
/fixtures/facetable.json?_size=1&_facet=state&_extra=count&_extra=count_sql&_extra=expandable_columns&_extra=facet_results

# Extras available (partial list visible in explorer screenshot, ~30 total):
# all_columns, column_types, columns, count, count_sql,
# custom_table_templates, database, database_color, expandable_columns,
# facet_results, foreign_key_tables, metadata, private, query
```

*Source: datasette project blog (datasette.io/blog/2026/api-extras/) and
tools.simonwillison.net/datasette-extras-explorer screenshot, referenced in
simonwillison.net/2026/Jun/11/datasette/*

### Cross-Model Planning/Implementation Split (from simonwillison.net/2026/Jun/11/datasette/)

```
Task: Build an interactive ?_extra= API explorer for Datasette

Planning model:        Claude Fable 5 in Claude Code
Implementation model:  GPT-5.5 xhigh in Codex Desktop
Output:                Interactive web tool at tools.simonwillison.net/datasette-extras-explorer

Tool UI elements:
  - URL input (e.g. https://latest.datasette.io/fixtures/facetable.json)
  - "Explore" button
  - Left panel: checkboxes for each available extra
  - Right panel: live JSON response showing requested extras

Willison's framing: "Because API explorer tools are almost free to build now"
```

*Source: Simon Willison, simonwillison.net/2026/Jun/11/datasette/, 2026-06-11*

### `?_extra=` Design Rationale and Documentation Links

```
Problem:    "Datasette usually returns more JSON than the client needs, often
             wasting SQL queries to generate data that is not used."
Solution:   Opt-in enrichment via ?_extra= query parameters

Page type coverage as of Datasette 1.0a33 (June 11, 2026):
  - Table pages:  supported since 1.0a3 (2023-08-09)
  - Query pages:  added in 1.0a33 (2026-06-11)
  - Row pages:    added in 1.0a33 (2026-06-11)

Documentation: https://docs.datasette.io/en/latest/json_api.html#json-api-extra
Explorer:      https://tools.simonwillison.net/datasette-extras-explorer
```

*Source: datasette project blog (datasette.io/blog/2026/api-extras/) and
simonwillison.net/2026/Jun/11/datasette/*

## Cross-References

- **Corroborates**:
  - **`blog-simonwillison-liteparse-browser.md` Claim 11**: That claim documents Willison's first in-corpus "cross-model verification" pattern: Claude Code built a browser app; GPT-5.5/Codex audited the implementation by describing what it found. This source documents a different use of the same cross-model habit: Claude Fable 5 planned the architecture; GPT-5.5 xhigh implemented it. Both posts from Willison show the same multi-vendor, complementary-role pattern in practice. The two posts together establish that Willison's cross-model habit is not limited to verification — it extends to planning/implementation division.
  - **`blog-simonwillison-gpt55-codex-plugin.md` overall**: That post documents Willison using Claude Code + GPT-5.5/Codex on the same project (Claude Code explored the OAuth flow; GPT-5.5 provided the subscription access route). This source is a third instance of the pattern (Claude for one role, GPT-5.5 for another, same project). Three examples from one practitioner establish this as a consistent workflow habit, not a one-off experiment.
  - **`blog-simonwillison-liteparse-browser.md` Claim 12**: That claim identifies the "blast radius" framing for when vibe coding is acceptable: static site, in-browser only, no data transfer. The extras explorer (a static browser tool with no server-side data processing) fits all three conditions. This source's "almost free to build" claim is the economic complement to LiteParse's blast-radius argument: the tool is cheap to build AND safe to ship without code review.
  - **`blog-simonwillison-datasette-agent.md` overall**: That note documents the Datasette Agent platform and the broader Datasette LLM ecosystem as of May 2026. This source adds a new capability in the same ecosystem (JSON extras extension) one month later. Together they trace the Datasette platform's evolution: conversational SQL querying (Datasette Agent, May 2026) + enriched JSON API (extras extension, June 2026) as parallel tracks.

- **Extends**:
  - **`blog-simonwillison-datasette-blog-codex-session.md` overall**: That note documents Willison building Datasette blog infrastructure in a single Codex Desktop session (May 2026). This source is a second instance of Willison using Codex Desktop for Datasette work (June 2026). Both posts show Codex Desktop as his consistent tool for Datasette coding tasks; this post adds the detail that GPT-5.5 xhigh was the specific model used for implementation.
  - **`blog-simonwillison-datasette-llm-limits.md` overall**: Another short Datasette release announcement from Willison (May 2026). This source is a later release in the same project. Together these release notes trace Willison's Datasette alpha cadence: LLM limits plugin (May 2026) → Datasette Agent (May 2026) → 1.0a33 extras extension (June 2026).
  - **`blog-simonwillison-fable-relentlessly-proactive.md` overall**: Published the same day (June 11, 2026). That note documents a Fable 5 autonomous debugging session on Datasette Agent; this note documents Willison using Fable 5 for API explorer planning on the same day. Both posts show concurrent Datasette work with AI assistance, documenting Willison's June 11, 2026 AI-assisted Datasette development activity from two different angles.

- **Contradicts**: None identified. The cross-model pattern in this source (planning/implementation split) complements rather than contradicts the verification pattern in `blog-simonwillison-liteparse-browser.md` — they are different use cases for the same multi-vendor habit. No contradiction issue required.

- **Novel**:
  - **Planning/implementation cross-model split (Fable for planning, GPT-5.5 for implementation)**: Prior in-corpus examples document cross-model *verification* (Claude builds, GPT-5.5 audits). This is the first in-corpus documentation of a *planning/implementation split* across vendor models on the same task. The division of roles is architectural (who decides what to build) vs. technical (who writes the code), not just quality-assurance.
  - **"API explorer tools are almost free to build now"**: The explicit framing of AI assistance as a cost threshold change for a specific tool category is novel. Prior corpus sources document AI-assisted workflows; this source documents the economic implication — that the cost drop changes what is worth building. This is a concrete example of capability-driven development applied to developer tooling.
  - **`?_extra=` composable API pattern as an API design technique**: The three-page-type extras registry (shared names across table, query, row pages; opt-in via URL parameter; each extra adds one JSON key) is a specific, named API design pattern not documented elsewhere in the corpus. The combination of backward compatibility (no parameter = same response as before) + opt-in enrichment + SQL-cost reduction is a coherent API design philosophy.

## Guide Impact

- **Chapter 02 (Harness Engineering — Cross-Model Workflow Patterns)**: Add the planning/implementation cross-model split as a distinct pattern from cross-model verification (already documented from `blog-simonwillison-liteparse-browser.md`). The guide should distinguish three cross-model use cases: (1) planning in one model/tool, implementing in another (this source); (2) implementing in one model, verifying in another (`blog-simonwillison-liteparse-browser.md` Claim 11); (3) exploring an unfamiliar codebase in one model, building with another (`blog-simonwillison-gpt55-codex-plugin.md`). Three documented examples from the same practitioner establish this as a real, reproducible pattern family. Cite this source for case (1).

- **Chapter 03 (Capability-Driven Development)**: Willison's "API explorer tools are almost free to build now" is one of the most direct in-corpus articulations of capability-driven development. Use it to illustrate the threshold-change argument: the tool class (interactive API explorers) is not new; what changed is that AI assistance dropped the cost below the "worth building" threshold for a short release announcement. Previously, building an interactive API explorer would require dedicated frontend engineering time. Now it requires a planning prompt and an implementation session. This changes product/documentation strategy: interactive exploration is now viable for any feature that benefits from it. Cite Claim 5.

- **Chapter 05 (API Design — Composable Optional Extras Pattern)**: The `?_extra=` design is a concrete practitioner-tested solution to the API verbosity problem. Add as a reference for API designers: "Opt-in enrichment via query parameters allows API clients to request only the data they need, reducing both response payload size and unnecessary database queries. Datasette's `?_extra=` pattern (`?_extra=count&_extra=foreign_key_tables`) applies this across all page types in a shared extras registry, providing backward compatibility (default response unchanged) while supporting progressive discovery. The pattern is complementary to but lower-friction than GraphQL field selection." Cite Claims 1–3 and the Concrete Artifacts URL example.

- **Chapter 02 (Harness Engineering — AI-Assisted Documentation Tooling)**: The extras explorer is a concrete example of using AI assistance to build self-documenting tooling for APIs. The guide should note that for any API feature that benefits from interactive exploration, AI now makes it viable to build the explorer as part of the release, not as a separate project. The extras explorer makes the `?_extra=` pattern discoverable without reading the docs — a qualitatively different documentation strategy than static reference pages. Cite Claim 6.

## Extraction Notes

- **Primary source (simonwillison.net)**: Short annotated-release-notes format. WebFetch returned summaries rather than verbatim text due to copyright limitations. Key quotes were extracted via multiple targeted fetch requests and cross-checked for consistency. The two principal quotes ("Because API explorer tools are almost free to build now" and "I had Claude Fable 5 in Claude Code (for the plan) and GPT-5.5 xhigh in Codex Desktop (for the implementation) build me this custom extras API explorer") are consistent across multiple independent fetches and are assessed as reliably verbatim. The Assayer should spot-check these against the live URL.
- **Secondary source (datasette project blog)**: The datasette.io/blog/2026/api-extras/ URL returned HTTP 500 when fetched directly, but was accessible via targeted WebFetch. The technical details (verbosity problem quote, URL example, page type coverage, documentation link) were retrieved in a separate targeted fetch and attributed to that secondary source explicitly in Concrete Artifacts.
- **Fragment URL**: The issue body includes `#atom-everything` (an Atom feed anchor). `source_url` uses the canonical page URL without the fragment, consistent with prior Willison source notes in this corpus.
- **Two cross-references verified**:
  - `blog-simonwillison-liteparse-browser.md` Claim 11 confirmed at lines 97–101 of that note (GPT-5.5/Codex audit — "Describe the difference between how the node.js CLI tool runs and how the web/ version runs").
  - `blog-simonwillison-liteparse-browser.md` Claim 12 confirmed at lines 104–108 of that note ("blast radius for any bugs is almost non-existent... static in-browser web application hosted on GitHub Pages").
- **Confidence set to `anecdotal`**: The tool-building workflow claims (cross-model split, "almost free" framing) are first-person practitioner observation from a single project. The API design claims (Datasette 1.0a33 extension, `?_extra=` mechanism) are settled from first-party release documentation but are Datasette-specific, not general API design evidence. The overall note is anecdotal because the most guide-relevant claims (capability cost threshold, model role assignment) come from one practitioner's single project account.
- **No contradiction issue filed**: The cross-model patterns in this note complement rather than contradict existing corpus notes. No existing note makes incompatible claims about cross-model planning/implementation splits or the `?_extra=` API pattern.
