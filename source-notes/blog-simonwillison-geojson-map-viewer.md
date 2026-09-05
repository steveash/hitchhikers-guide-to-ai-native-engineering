---
source_url: https://simonwillison.net/2026/Sep/1/geojson/
source_type: blog-post
title: "GeoJSON Map Viewer"
author: Simon Willison
date_published: 2026-09-01
date_extracted: 2026-09-05
last_checked: 2026-09-05
status: current
confidence_overall: anecdotal
issue: "#3245"
---

# GeoJSON Map Viewer

> A short practitioner report in which Simon Willison, while helping someone
> map local political boundaries, asked GPT-5.6-Sol for "suggestions of
> tools" and got a proactively built tool instead of a recommendation list,
> then iterated on it with Claude Code for web and Fable 5.1, while using
> ChatGPT Work as a separate conversational data-extraction step to source
> the actual GeoJSON boundary data from government sources.

## Source Context

- **Type**: blog-post (Willison "notes" format — short first-person practitioner
  report, under 200 words of original prose plus a screenshot/demo of the
  deployed tool; no linked GitHub repo, transcript, or PR was found in the
  post for this specific tool).
- **Author credibility**: Simon Willison is the creator of Django, the `llm`
  CLI, and Datasette, and a `trusted-feed` source already extensively used in
  this corpus (`blog-simonwillison-liteparse-browser.md`,
  `blog-simonwillison-datasette-1-0a33.md`, and dozens of others). This is a
  first-person account of his own tool-building session with a publicly
  deployed, checkable artifact (`tools.simonwillison.net/geojson`).
- **Scope**: Covers exactly one tool-building session: the motivating
  real-world task (mapping political boundaries for the Granada Community
  Services District and the Midcoast Community Council), the sequence of AI
  models used to build the map-viewer tool, the separate use of ChatGPT Work
  to extract boundary GeoJSON from government data, and the finished tool's
  feature set and privacy stance. Does NOT cover: any transcript of the
  Claude Code / Fable 5.1 iteration sessions, the prompts used during that
  iteration (only the GPT-5.6-Sol and ChatGPT Work prompts are quoted), the
  tool's source code, or any discussion of accuracy/validation of the
  extracted government boundary data.

## Extracted Claims

### Claim 1: Willison built the tool to solve a real, specific need — mapping local political boundaries for two community organizations — not as a demo or experiment
- **Evidence**: Direct first-person statement of motivation at the top of the post.
- **Confidence**: settled (first-party statement of the author's own motivation)
- **Quote**: "I was helping Natalie gather some maps of local political boundaries (for the Granada Community Services District and the Midcoast Community Council) and found a need to display some GeoJSON files on a map and export that as a PNG."
- **Our assessment**: This is a "personal, situated" tool in the sense already
  documented in `blog-simonwillison-rss-vibe-coded-apps.md` (Claim 2) — built
  for a specific real task (helping someone with community-org boundary
  maps), not for a general audience, then published to his tools portfolio
  as a side effect rather than the goal. The motivation is concrete and
  falsifiable (a named need: display + PNG export), which is stronger
  grounding than "I wanted to try X."

### Claim 2: When Willison asked GPT-5.6-Sol for "suggestions of tools," the model proactively built a working tool rather than recommending existing ones
- **Evidence**: Direct first-person statement describing the model's behavior as a departure from what was asked.
- **Confidence**: anecdotal (single practitioner observation, single interaction; no comparison to how other models responded to the same prompt)
- **Quote**: "I asked GPT-5.6-Sol for suggestions of tools and it proactively built one."
- **Our assessment**: This is a genuinely novel claim in this corpus — no
  existing source note documents a model reinterpreting a request for
  *suggestions* as an instruction to *build*. It's a small but concrete data
  point about model agency/initiative in GPT-5.6-Sol (part of the GPT-5.6
  Sol/Terra/Luna lineup documented in `blog-simonwillison-gpt56-sol-launch.md`,
  which covers pricing/caching but says nothing about behavioral tendencies).
  Whether this generalizes (does GPT-5.6-Sol reliably over-deliver on
  ambiguous requests, or was this a one-off) cannot be determined from a
  single anecdote, and the post gives no indication of the exact prompt
  wording beyond "suggestions of tools."

### Claim 3: The finished tool was produced through a three-stage, cross-vendor pipeline: GPT-5.6-Sol builds a first version, then Claude Code for web and Fable 5.1 iterate on it to completion
- **Evidence**: Direct first-person statement giving the full model sequence.
- **Confidence**: anecdotal (single project, self-reported)
- **Quote**: "After some iterations using Claude Code for web and Fable 5.1 we got to this finished tool."
- **Our assessment**: This is a different cross-model shape than the
  planning/implementation split documented in
  `blog-simonwillison-datasette-1-0a33.md` (Claim 4: Fable 5 plans, GPT-5.5
  implements) — here a GPT-family model produces the *first working version*
  unprompted, and Claude-family tools (Claude Code for web, Fable 5.1) handle
  all subsequent refinement. Combined with the 1.0a33 note, this is now two
  distinct in-corpus shapes of cross-vendor collaboration on the same kind of
  task (build a small tool): "Claude plans, GPT implements" and "GPT
  originates, Claude refines." Neither post explains why the roles were
  assigned that way, so we should not over-generalize a "which vendor for
  which role" rule from either single example — the extractable pattern is
  that practitioners are fluidly mixing vendors within one small project, not
  a fixed division of labor.

### Claim 4: Willison used ChatGPT Work as a separate, conversational step to extract real government boundary GeoJSON data, independent of the tool-building pipeline
- **Evidence**: The post is explicit that ChatGPT Work (not the tool-building models) was the one used for data sourcing, with specific verbatim prompts given.
- **Confidence**: anecdotal (single practitioner, two specific data-extraction requests)
- **Quote**: "I want a polygon that represents the exact boundary of the El Granada GCSD"
- **Our assessment**: This decouples two AI-assisted tasks that could easily
  be conflated: *building the viewer tool* (GPT-5.6-Sol → Claude Code →
  Fable 5.1) and *sourcing the data to view* (ChatGPT Work). The data-sourcing
  task is a natural-language-to-structured-geodata extraction problem —
  asking a conversational model to locate and return a specific
  administrative boundary as GeoJSON, rather than manually finding and
  parsing a government shapefile or GIS portal. This is a concrete example of
  "ask the model to go find and structure a specific piece of public data"
  as a data-acquisition technique, distinct from code generation.

### Claim 5: The second ChatGPT Work extraction request combined two named jurisdictions/data sources into a single ask
- **Evidence**: Second verbatim prompt quoted in the post, naming a specific organization and a nearby city for geographic disambiguation.
- **Confidence**: anecdotal (single example)
- **Quote**: "Get me a GeoJSON file for the boundary (or boundaries if that makes sense) for the MCC - Midcoast Community Council - that operates near Half Moon Bay CA"
- **Our assessment**: Notably, the prompt itself hedges on cardinality
  ("or boundaries if that makes sense") — Willison lets the model decide
  whether the entity has one boundary or several, rather than asserting it
  upfront. This is a small but reusable prompting habit for data-extraction
  tasks where the requester doesn't know the shape of the answer in advance:
  state the ambiguity explicitly rather than guessing a schema.

### Claim 6: The finished tool processes all GeoJSON data client-side, with no server-side transfer of the user's data
- **Evidence**: Direct statement of the tool's privacy/architecture stance, presumably on the tool's own page rather than the blog post body.
- **Confidence**: settled (a verifiable architectural claim about the deployed tool at tools.simonwillison.net/geojson)
- **Quote**: "Your GeoJSON stays in this browser."
- **Our assessment**: This is the same "blast radius" justification already
  documented at length in `blog-simonwillison-liteparse-browser.md` (Claim
  12): a static, browser-only tool with no server-side data handling has
  near-zero blast radius, which is Willison's recurring stated basis for
  shipping small tools without a security review or even reading the
  generated code closely. The GeoJSON viewer is architecturally identical in
  this respect (client-side only, no backend), even though this post does
  not explicitly restate the "I haven't reviewed this code" framing the way
  the LiteParse post does.

### Claim 7: The tool supports pasting arbitrary GeoJSON objects (Feature, FeatureCollection, or Geometry) and adjusting fill color/opacity before rendering on an interactive OpenStreetMap base layer
- **Evidence**: Feature description, apparently from the tool's own page/metadata rather than Willison's blog prose.
- **Confidence**: settled (directly checkable against the live tool)
- **Quote**: "Paste GeoJSON objects (Feature, FeatureCollection, or Geometry) into the editor, adjust fill color and opacity, and render the features directly on the map."
- **Our assessment**: This is a fairly standard GeoJSON-viewer feature set;
  the significance is not the feature list itself but that this is the kind
  of narrowly-scoped, single-purpose utility that is now cheap enough to
  build ad hoc for a one-off personal need (mapping two specific community
  organizations' boundaries) and still worth publishing generally, echoing
  the "tools are basically free to build now" framing in
  `blog-simonwillison-datasette-1-0a33.md` (Claim 5).

## Concrete Artifacts

```
Tool: GeoJSON Map Viewer
URL:  https://tools.simonwillison.net/geojson
Source post: https://simonwillison.net/2026/Sep/1/geojson/ (2026-09-01)

Build pipeline (as stated by Willison):
  1. GPT-5.6-Sol       — asked for "suggestions of tools"; proactively built one
  2. Claude Code for web — iteration
  3. Fable 5.1            — iteration
  Result: "finished tool"

Separate data-sourcing step (ChatGPT Work):
  Prompt 1: "I want a polygon that represents the exact boundary of the El Granada GCSD"
  Prompt 2: "Get me a GeoJSON file for the boundary (or boundaries if that makes sense)
             for the MCC - Midcoast Community Council - that operates near Half Moon Bay CA"

Motivating task: mapping boundaries for the Granada Community Services District
                 and the Midcoast Community Council, for "Natalie"

Privacy stance: "Your GeoJSON stays in this browser."
```
*Source: simonwillison.net/2026/Sep/1/geojson/, via targeted WebFetch queries
against the live page (2026-09-05); the raw HTML was not fetched directly via
curl for this note, so quotes should be spot-checked by the Assayer against
the live URL.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-rss-vibe-coded-apps.md` Claim 2 (vibe-coded tools
    trend "more personal, more situated"): this tool was built for one
    specific, named real-world need (two community organizations' boundary
    maps) and only secondarily published as a general-purpose tool — a
    direct instance of the "personal, situated" pattern that source names in
    the abstract.
  - `blog-simonwillison-liteparse-browser.md` Claim 12 (blast-radius
    justification for shipping unreviewed browser-only vibe-coded tools):
    the GeoJSON viewer's stated "Your GeoJSON stays in this browser"
    architecture matches the same static/client-side/no-data-transfer
    profile that Claim 12 identifies as justifying minimal review.

- **Contradicts**: None identified. No existing source note makes a claim
  about model behavior, cross-model tool-building sequencing, or
  data-extraction prompting that this source opposes.

- **Extends**:
  - `blog-simonwillison-datasette-1-0a33.md` Claim 4 (cross-model
    planning/implementation split: Fable 5 plans, GPT-5.5 implements): this
    source documents a second, differently-shaped cross-vendor pipeline for
    building a small tool (GPT-5.6-Sol originates a working build
    unprompted; Claude Code for web and Fable 5.1 handle all iteration
    afterward). Together the two posts show Willison mixing vendors within a
    single small project in more than one arrangement, rather than a fixed
    "which vendor does which job" rule.
  - `blog-simonwillison-liteparse-browser.md` (overall — full workflow
    documentation of a browser-tool build): this source is much thinner (no
    transcript, no prompt sequence for the Claude Code / Fable 5.1 iteration
    stage, no linked repo), but adds the ChatGPT Work data-extraction step as
    a task type not covered by the LiteParse post, which is about a PDF
    parsing library, not conversational geodata extraction.

- **Novel**:
  - **Model proactively building a tool when only "suggestions" were
    requested** (Claim 2): no existing corpus source documents a model
    reinterpreting a request for recommendations as an instruction to build.
  - **Conversational natural-language-to-GeoJSON extraction from government
    sources via ChatGPT Work** (Claims 4-5): no existing corpus source
    documents using a chat model to locate and structure a specific public
    administrative boundary as geodata, as distinct from code generation or
    general data lookup.

## Guide Impact

- **Chapter 04 (practical workflows / tool-building)**: Add Claim 2 (a model
  proactively building a tool instead of listing suggestions) as a
  documented instance of model-initiative behavior worth flagging to
  practitioners — when asking a model for "suggestions" or "options," be
  aware some models may skip the recommendation step and just build
  something, which is useful when a working artifact is welcome but could
  be surprising or wasteful in other contexts (e.g., a quick exploratory
  question where you didn't want an artifact at all).
- **Chapter 04 (practical workflows / cross-model tool-building)**: Add this
  source alongside `blog-simonwillison-datasette-1-0a33.md` as a second data
  point for a "cross-vendor within one small project" workflow section:
  present both the "plan in Claude, implement in GPT" shape and the
  "GPT originates, Claude iterates" shape as two observed variants, with the
  explicit caveat (from both sources) that neither post gives a rationale
  for the specific vendor-to-role assignment, so this should be presented as
  "practitioners mix vendors fluidly," not a prescriptive rule.
- **Chapter 04 (data extraction / context engineering)**: Add the ChatGPT
  Work GeoJSON-extraction prompts (Claims 4-5) as a concrete example of using
  a conversational model to acquire and structure a specific piece of public
  geodata from natural-language description alone, including the "or X if
  that makes sense" hedge as a reusable technique for signaling schema
  ambiguity to the model rather than guessing cardinality upfront.

## Extraction Notes

- **Source is thin**: This is one of Willison's shortest "notes"-format
  posts — well under 200 words of original prose. There is no linked GitHub
  repository, Claude Code transcript, or PR for this specific tool (unlike
  `blog-simonwillison-liteparse-browser.md`, which links a full transcript
  and repo). The claims extracted here are therefore all first-person,
  self-reported, single-instance observations with no independent
  verification path beyond the deployed tool itself
  (`tools.simonwillison.net/geojson`), which confirms the tool's existence
  and feature set but not the build process narrative.
- **WebFetch declined full verbatim reproduction** on the first request
  (citing copyright), consistent with prior notes' experience with this
  source (`blog-simonwillison-datasette-mcp-02.md`,
  `blog-simonwillison-datasette-1-0a33.md`). Quotes in this note were
  obtained via a second, narrower WebFetch request asking for specific
  short (under-30-word) attributed passages rather than the full post; the
  quotes returned were internally consistent (a follow-up spot-check request
  reproduced the same wording), but — unlike the datasette-mcp-02 note —
  the raw HTML was not independently fetched via `curl` for this note, so
  the Assayer should treat quote fidelity here as somewhat lower-confidence
  than notes that cross-checked against raw HTML, and spot-check directly
  against the live URL.
- **No linked sub-pages followed**: the post does not link to a GitHub repo,
  transcript, or the government data sources used by ChatGPT Work. The tool
  itself (`tools.simonwillison.net/geojson`) is the only linked artifact, and
  its feature-description text (Claim 7) and privacy statement (Claim 6)
  were the two additional facts recoverable from a live-page fetch beyond
  the blog post prose itself.
- **No contradictions found**: checked against all Willison notes referenced
  in the Prospector's triage comments (`blog-simonwillison-datasette-mcp-02.md`,
  `blog-simonwillison-rss-vibe-coded-apps.md`) plus
  `blog-simonwillison-liteparse-browser.md` and
  `blog-simonwillison-datasette-1-0a33.md` for related cross-model and
  blast-radius claims; none disagree with anything in this source.
- **Confidence set to `anecdotal`**: every claim in this note is a
  single-practitioner, single-instance, self-reported account with no
  transcript or repo to verify the build-process narrative against (only the
  finished tool and its stated feature set are independently checkable).
  This is a lower evidentiary bar than the fuller `blog-simonwillison-liteparse-browser.md`
  or `blog-simonwillison-datasette-1-0a33.md` reports, which at least link a
  transcript or a companion technical blog post.
