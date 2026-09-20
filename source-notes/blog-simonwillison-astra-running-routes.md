---
source_url: https://simonwillison.net/2026/Sep/12/astra-running-routes/
source_type: blog-post
title: "Generating running routes with GPT-6 Astra and ChatGPT Work"
author: Simon Willison
date_published: 2026-09-12
date_extracted: 2026-09-20
last_checked: 2026-09-20
status: current
confidence_overall: anecdotal
issue: "#3577"
---

# Generating running routes with GPT-6 Astra and ChatGPT Work

> Simon Willison's short hands-on report of a single 27-minute ChatGPT Work
> (GPT-6 Astra, Max reasoning) session that turned a one-line natural-language
> prompt into 5K/10K running-route recommendations — chaining Nominatim
> (geocoding) and Overpass (OSM road/trail extraction) with local route
> calculation, then rendering the result as a self-contained, tile-free D3/SVG
> map via the "visualize" skill. The post's real payload is a named failure
> mode: after the session compacted, Willison could not retrieve the Python
> code the agent had already run, which he generalizes into a concrete
> requirement for any LLM system that uses context compaction.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, a short "notes" post, ~230
  words of prose plus an embedded screenshot and two blockquotes — published
  12th September 2026, 11:56pm).
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI and an already heavily-used `trusted-feed` source in this corpus
  (e.g. `blog-simonwillison-gpt6-astra-launch.md`,
  `blog-simonwillison-astra-pelican-comparison-grid.md`). This post is
  first-person, hands-on: Willison ran the session himself, on his own real
  address, and reports his own attempt (and failure) to retrieve the
  underlying code afterward. It is a single-session anecdote, not a
  benchmark or a systematic evaluation.
- **Scope**: Covers one ChatGPT Work session (GPT-6 Astra, Max reasoning)
  performing a geospatial tool-orchestration task, the specific tools it
  self-reported using, the output artifacts produced (embedded map, GPX,
  GeoJSON), a UI transparency limitation Willison hit when trying to inspect
  the underlying code, and detail on the "visualize" skill that rendered the
  map (drawn from the post's own inline blockquote of that skill's docs, and
  independently confirmed against the live skill-documentation page for this
  note). Does **not** cover: Astra's general benchmark performance (see
  `blog-simonwillison-gpt6-astra-launch.md`), routing-algorithm correctness
  or quality evaluation of the generated routes, cost/token accounting for
  the session, or any comparison against other models/harnesses performing
  the same task.

## Extracted Claims

### Claim 1: A single ChatGPT Work (GPT-6 Astra, Max) session ran for 27 minutes and produced exactly the requested output — an embedded map visualization plus downloadable GPX and GeoJSON files — from a one-sentence natural-language prompt
- **Evidence**: Willison's own first-person account of running the session and inspecting its output.
- **Confidence**: anecdotal (single practitioner, single session, no replication)
- **Quote**: "It worked for 27 minutes and produced exactly what I'd asked for, as both an embedded visualization and downloadable GPX file and GeoJSON files."
- **Our assessment**: A concrete, dated data point for how long a "Max" reasoning-effort ChatGPT Work session ran unattended on a moderately complex, multi-tool geospatial task, and that it converged on a directly usable result on the first attempt (no retry or correction mentioned). One data point only — no cost, token, or failure-rate information accompanies it, so it should not be read as a general throughput claim for this task class.

### Claim 2: The prompt Willison used was a single, unelaborated natural-language sentence naming the task, the user's location, and the data source, with no instructions about tools, APIs, or methodology
- **Evidence**: The exact prompt text, reproduced verbatim as a blockquote in the post.
- **Confidence**: settled (directly quoted user input, not an interpretation)
- **Quote**: "I live at <my address>. Figure out 5K and 10K running routes from me that loop from my house. Use OSM data."
- **Our assessment**: The only explicit methodological instruction in the prompt is "Use OSM data" — the choice of Nominatim for geocoding, Overpass for road/trail extraction, and local route calculation (Claim 3) was left entirely to the agent. This is a useful concrete example of how little scaffolding a Max-effort agent session needed to correctly select and chain a specific real-world API toolchain from an open-ended data-source constraint.

### Claim 3: When asked how the route was generated, the agent self-reported a three-step toolchain — Nominatim for address geocoding, Overpass for downloading local OpenStreetMap roads and trails, and local (in-session) route-loop calculation — with no third-party routing/directions API involved
- **Evidence**: The agent's own explanation, given in response to a direct follow-up question and reproduced verbatim.
- **Confidence**: anecdotal (a single self-reported explanation from the model, not independently verified against the actual executed code — which Willison was later unable to retrieve, per Claim 5)
- **Quote**: "I used Nominatim to locate the address and Overpass to download local OpenStreetMap roads and trails, then calculated the loops locally."
- **Our assessment**: This is the concrete tool-orchestration pattern the Prospector flagged as the key extraction target. It's notable that the loop-finding logic itself ("calculated the loops locally") was not delegated to any named external routing service — the agent used Nominatim and Overpass only for data acquisition and then computed the route geometry itself. Because Willison could not later retrieve the code (Claim 5), this claim rests entirely on the model's own self-report and should be treated as testimony about the model's behavior, not as independently verified ground truth about what actually executed.

### Claim 4: Willison flags the ChatGPT UI's failure to expose the actual code and execution detail behind the agent's actions, during the session, as a transparency anti-pattern
- **Evidence**: Willison's own direct editorial statement, made immediately after quoting the agent's tool-use explanation.
- **Confidence**: anecdotal (single practitioner's UX judgment)
- **Quote**: "Frustratingly, the actual code it ran and exact details of what it did weren't visible to me in the ChatGPT UI. I see this lack of transparency is an anti-feature."
- **Our assessment**: This is a specifically-scoped complaint — not "the agent didn't explain itself" (it did, per Claim 3) but "the UI didn't surface the underlying execution artifacts (code, intermediate data) even though they presumably existed." It sets up the more concrete failure in Claim 5, where that missing transparency became unrecoverable.

### Claim 5: After the session's context had been compacted, ChatGPT was unable to produce a copy of the Python code it had already run, which Willison attributes to compaction discarding the pre-compaction text; he generalizes this into a requirement that any LLM system using compaction must both preserve pre-compaction text and expose it via agent tool calls
- **Evidence**: Willison's own account of asking for the code after the fact and being refused/unable to receive it, plus his own stated causal attribution and generalized recommendation.
- **Confidence**: anecdotal (single-session failure observation) for the specific incident; the generalized systems requirement is Willison's own editorial recommendation, not independently tested against other compaction implementations in this post
- **Quote**: "By the time I thought to ask for a copy of the Python code it had used, ChatGPT was unable to provide it. This appears to be because the thread had been compacted. I think any LLM system that uses compaction needs to both preserve the pre-compacted text and make that text available via agent tool calls, to protect against this kind of problem."
- **Our assessment**: This is the source's most guide-relevant claim. It names a specific, reproducible-sounding failure mode (compaction → permanent loss of retrievability for already-executed code) rather than a vague complaint about summarization losing detail, and proposes a concrete two-part fix (preserve pre-compaction text; expose it via tool calls, not just as inert history). Willison hedges the causal attribution with "appears to be" — he did not get an authoritative explanation from OpenAI that compaction was in fact the mechanism, so this should be cited as his plausible inference, not a confirmed root cause.

### Claim 6: The map shown to Willison was produced by ChatGPT Work's "visualize" skill, which wrote a new file at `/workspace/el-granada-5k-share.html` to embed directly into the ChatGPT UI
- **Evidence**: Willison's direct statement, naming both the skill and the exact generated file path, with a link to the skill's own documentation.
- **Confidence**: settled (a specific, named, checkable artifact — file path and skill name — stated directly by the practitioner who observed it)
- **Quote**: "As for displaying the map to me, that used the visualize skill. It created a file called /workspace/el-granada-5k-share.html to embed directly into the ChatGPT UI."
- **Our assessment**: Confirms that ChatGPT Work's in-conversation visualizations are implemented as standalone HTML files written into the session's `/workspace` filesystem and embedded, rather than rendered through some separate charting subsystem. This is architecturally consistent with the persistent `/workspace` filesystem Willison documents independently in his companion post "Understanding ChatGPT Work" (simonwillison.net/2026/Aug/30/understanding-chatgpt-work/): "each session gets its own scratch folder... but each of those are persisted across sessions" — that post is linked from this one as background but is a separate URL, not part of this source, and is cited here only as corroborating context, not as part of this claim's evidentiary basis.

### Claim 7: The generated HTML artifact embeds the full route and road geometry as an inline JSON GeoJSON blob and renders it entirely client-side as an SVG map using D3 (loaded from a CDN), rather than displaying raster map tiles from a mapping service
- **Evidence**: Direct inspection of the linked gist containing the shared HTML (gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480), fetched and read by this Miner. The `<script type="application/json" id="eg-share-data">` element holds the route `LineString` and road-network `Polygon`/`LineString` GeoJSON features; a separate `<script>` block loads `d3@7.9.0` from `cdn.jsdelivr.net` and uses `d3.geoMercator()` and `d3.geoPath()` to project and draw that geometry directly as SVG `<path>` elements at render time, with distinct styling for coastline, trunk roads, and trail/footway/cycleway/bridleway types.
- **Confidence**: settled (directly inspected artifact — this is the actual HTML file Willison shared, not a description of it)
- **Quote**: (no direct quote from the blog post itself for this mechanism; the blog post only shows the opening `<div id="eg-share-loop">` markup and states "The `<script type="application/json">` element contains the full geometry needed to render both the running route and the map itself, using D3." The rendering-logic detail above is the Miner's own direct reading of the linked gist's raw source, not a quoted passage from Willison's prose — see Concrete Artifacts for the extracted code.)
- **Our assessment**: This is a genuinely reusable implementation pattern beyond the specific running-routes task: rather than fetching raster map tiles (which would require a tile-server API key/quota and network access at render time), the skill baked the previously-fetched Overpass vector data directly into the shareable HTML and drew it with D3 at load time. The resulting file is self-contained and works offline once loaded — a concrete example of an agent choosing a "ship the data, not a live dependency" output pattern for a shareable artifact.

### Claim 8: The visualize skill's Content Security Policy allows external resource loading from exactly seven named CDN/font origins, blocking and silently failing on all others
- **Evidence**: Quoted directly in the blog post from the skill's own "External resources" documentation section, and independently confirmed by this Miner by fetching the live documentation page directly.
- **Confidence**: settled (a specific, checkable configuration value, quoted identically in two independently-fetched locations — the blog post's blockquote and the skill-documentation page itself)
- **Quote**: "The CSP allows only cdnjs.cloudflare.com, esm.sh, cdn.jsdelivr.net, unpkg.com, fonts.googleapis.com, fonts.gstatic.com, and fonts.bunny.net. Other origins are blocked and fail silently." (blog post; identical text confirmed present verbatim at codex-tool-reference.simonw.chatgpt.site/skills/visualize, under the "External Resources" heading)
- **Our assessment**: Important caveat on independence: the skill-documentation page this quote is drawn from is not an official OpenAI documentation source — per Willison's separate "Understanding ChatGPT Work" post, that entire site was itself generated by a ChatGPT Work session Willison prompted to "duplicate arguments and tool descriptions where possible" for its own tools and skills, then further prompted to add "full copies of every skill." So this CSP text is the *agent's own reproduction* of its system-provided skill file, not a document OpenAI published directly — both quotes trace back to the same underlying agent-elicited source, not two independent confirmations. Treat the exact allowlist as "very likely accurate, self-consistent across two fetches" rather than "OpenAI-confirmed." The practical takeaway — that a visualization skill's silent CDN allowlist is narrow and fails without an error message — is still a concrete, actionable detail for anyone building or debugging similar in-conversation visualization tooling. "Fail silently" specifically is worth flagging as a debugging trap: a blocked-origin resource load gives no visible error in the rendered output.

### Claim 9: ChatGPT Work's cloud code-execution environment has outbound internet access by default, unlike ChatGPT Chat's, whose container proxy blocks installing packages or reaching external websites/APIs
- **Evidence**: Drawn from Willison's separate, linked companion post "Understanding ChatGPT Work" (simonwillison.net/2026/Aug/30/understanding-chatgpt-work/), read by this Miner as background for how the Nominatim/Overpass calls in Claim 3 were technically possible; not itself part of the running-routes post's own text.
- **Confidence**: anecdotal (a separate first-person practitioner account, not independently verified against OpenAI's own documentation in that post)
- **Quote**: "The code execution environment can now talk to the rest of the internet!" ... "ChatGPT Chat can't do this—if you ask it to install additional software packages or interact with websites or APIs that access will be blocked by the container proxy." (from "Understanding ChatGPT Work," simonwillison.net/2026/Aug/30/understanding-chatgpt-work/ — a different URL from this note's primary source)
- **Our assessment**: This is background context, not a claim of the mined post itself, but it directly explains the precondition that made Claim 3's toolchain (live calls to Nominatim and Overpass, both external HTTP APIs) possible in ChatGPT Work specifically — the same task would not have been achievable in plain ChatGPT Chat per this same companion post. Guide text citing the running-routes example as "an agent calling external APIs" should note this is a ChatGPT-Work-specific (not ChatGPT-Chat-general) capability, per Willison's own separate documentation.

## Concrete Artifacts

Prompt used to start the session (source: blog post, exact text):
```
I live at <my address>. Figure out 5K and 10K running routes from me
that loop from my house. Use OSM data.
```

Agent's self-reported tool-use explanation (source: blog post, exact text):
```
I used Nominatim to locate the address and Overpass to download local
OpenStreetMap roads and trails, then calculated the loops locally.
```

Opening markup of the shared visualization HTML artifact (source: blog
post's reproduced excerpt of `/workspace/el-granada-5k-share.html`):
```html
<div id="eg-share-loop">
  <div class="viz-row"><h3>El Granada harbor loop</h3><span class="text-small">5.1 km</span></div>
  <div id="eg-share-stage"></div>
  <div class="text-small text-muted">Map data © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a></div>
  <style> ... </style>
  <script type="application/json" id="eg-share-data">{"route":{"type":"LineString","coordinates":[[-122.467425,37.4997753], ... </script>
  <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
  <script>
  (() => {
    const root=document.getElementById('eg-share-loop');
```

Client-side D3 rendering logic (source: this Miner's direct fetch of the
full linked gist, gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480,
raw HTML — not reproduced in the blog post itself):
```js
function draw(){
  if(typeof d3==='undefined'){stage.textContent='The map could not load.';return;}
  const w=Math.round(stage.getBoundingClientRect().width);
  if(w<1)return;
  const h=w<480?440:500;
  const projection=d3.geoMercator().fitExtent([[28,36],[w-28,h-36]],data.route);
  const path=d3.geoPath(projection);
  const svg=el('svg',{class:'eg-share-map',viewBox:`0 0 ${w} ${h}`,width:w,height:h, ... });
  ...
  for(const f of data.roads){
    if(f.geometry.type!=='Polygon')continue;
    const fixed=d3.geoArea(f)>2*Math.PI?{...f,geometry:{type:'Polygon',coordinates:[f.geometry.coordinates[0].slice().reverse()]}}:f;
    map.append(el('path',{d:path(fixed),fill:'var(--muted)',opacity:.55,stroke:'none'}));
  }
  ...
}
```

Visualize skill's "External resources" section (source: blog post
blockquote, independently confirmed against
codex-tool-reference.simonw.chatgpt.site/skills/visualize):
```
### External resources
- The CSP allows only cdnjs.cloudflare.com, esm.sh, cdn.jsdelivr.net,
  unpkg.com, fonts.googleapis.com, fonts.gstatic.com, and
  fonts.bunny.net. Other origins are blocked and fail silently.
```

## Cross-References

### Cross-reference verification notes
`blog-openai-chatgpt-work-ambitious-partner.md`,
`blog-simonwillison-datasette-agent.md`, `blog-simonwillison-gpt6-astra-launch.md`,
and `blog-simonwillison-astra-pelican-comparison-grid.md` were each re-read
directly before citing; every `Claim N` reference below was located and
confirmed by number and content against that note's own text, per MINER.md
§4b.

- **Corroborates**:
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 1 ("ChatGPT Work
    is a new agent mode... that can stay with complex, multi-hour projects
    by breaking them into smaller steps and completing them
    independently"): this note's Claim 1 (a 27-minute, unattended,
    multi-tool session converging on the requested output) is a concrete,
    first-person instance of exactly the "stay with a project and break it
    into steps" behavior that announcement post describes only in
    marketing-copy generality.
  - `blog-simonwillison-datasette-agent.md` Claim 6 (three launch plugins
    demonstrating "three distinct agent output modalities," including
    `datasette-agent-charts` for chart rendering as a separate output-layer
    plugin from the core querying agent): this note's Claim 6 (a distinct
    "visualize" skill, separate from the geocoding/routing toolchain,
    responsible specifically for rendering the final HTML/map artifact)
    matches the same general pattern — a dedicated visualization
    tool/skill/plugin handling final-output rendering, decoupled from the
    tools that gathered the underlying data.

- **Contradicts**: None identified rising to the MINER.md §4a filing bar.
  One tension worth flagging without filing: `blog-openai-chatgpt-work-ambitious-partner.md`
  Claim 13 describes an enterprise "Auto-review" feature giving admins
  visibility into ChatGPT Work's actions on connected tools/APIs before
  they happen. This note's Claim 4/5 (an individual user unable to retrieve
  the code an agent had already run, once compacted) describes a different
  audience and a different kind of visibility — admin-level pre-action
  oversight versus an end user's own post-hoc code retrieval — so this is
  not a genuine contradiction (different scope/audience, MINER.md §4a "When
  NOT to file"), but the two sit awkwardly next to each other: an
  enterprise feature exists to review agent actions before they happen,
  while an ordinary user could not review an action's own code after the
  fact.

- **Extends**:
  - `blog-simonwillison-gpt6-astra-launch.md` and
    `blog-simonwillison-astra-pelican-comparison-grid.md`: both existing
    Astra notes in this corpus cover either secondhand benchmark data
    (the launch note, whose Claim 10 states Willison "had not tried it yet
    myself" at time of writing) or a narrow, single-prompt creative
    benchmark (SVG pelican generation). This note extends the corpus's
    Astra coverage with a first-person, real-world, multi-tool agentic task
    (geospatial data lookup, computation, and rendering) rather than a
    static generation or aggregate-score comparison — a different capability
    axis (tool orchestration and session durability) than either prior note
    examines.

- **Novel**:
  - First corpus documentation of the "visualize" skill by name, its
    file-output contract (`/workspace/<title>.html`, embedded inline), and
    its CSP-restricted external-resource allowlist (Claim 6, 8).
  - First corpus documentation of a concrete, named agent-transparency
    failure tied specifically to context compaction discarding
    already-executed code, plus a practitioner's proposed two-part fix
    (preserve pre-compaction text; expose it via tool calls) (Claim 5).
  - First corpus example of an agent-generated shareable artifact that
    embeds previously-fetched vector geodata inline and renders it
    client-side with D3, rather than depending on a live map-tile service
    at view time (Claim 7).

## Guide Impact

- **Chapter on Context Engineering / compaction (Ch04 per this issue's
  triage)**: Add Claim 5 as a concrete, named failure mode for any guide
  discussion of context compaction: compaction can make already-executed,
  successful code permanently unretrievable from the agent's own session,
  not just cause the agent to "forget" earlier conversational detail.
  Recommend citing Willison's proposed mitigation (preserve pre-compaction
  text; expose it via tool calls, not just inert scrollback) as a concrete
  design requirement for any harness that implements compaction, while
  flagging that Willison's causal attribution ("appears to be because the
  thread had been compacted") is his own inference, not an OpenAI-confirmed
  mechanism.

- **Chapter on Delegation & Tool Use (Ch02) / Practical agentic patterns**:
  Add Claim 3 (Nominatim + Overpass + local computation, chosen entirely by
  the agent from a one-line prompt with only a data-source constraint) as a
  concrete example of unsupervised multi-API tool selection succeeding on a
  real task, alongside Claim 9's caveat that this specific toolchain
  required ChatGPT Work's internet-enabled code-execution sandbox
  specifically, not plain ChatGPT Chat.

- **Chapter on Infrastructure & Observability (Ch04)**: Add Claim 4/5
  together as a worked example for why "the agent explained what it did in
  prose" (Claim 3) is not equivalent to "the actual execution is auditable"
  — the prose explanation survived, the underlying code did not. Useful as
  a concrete illustration that harness-level code/tool-call logging,
  independent of the conversation's own compacted history, is what
  auditability actually requires.

- **Do not cite this post as evidence of Astra's general capability or of
  OSM/Overpass/Nominatim routing quality**: per Source Context, this is a
  single, unreplicated session on one address, with no evaluation of route
  quality, safety, or correctness — only that the agent produced *a*
  plausible-looking result Willison accepted at face value.

## Extraction Notes

- **Primary source is short**: the blog post itself is ~230 words of prose
  plus two blockquotes; nine claims were extracted by treating each
  distinct statement (session duration/outcome, the prompt, the
  self-reported toolchain, the transparency complaint, the compaction
  failure and its generalized fix, the visualize skill's file-output
  behavior, and its CSP allowlist) as its own claim, plus one background
  claim (Claim 9) drawn from a directly-linked companion post.
- **Linked pages followed** (within MINER.md §1's "up to 5" budget): (1)
  the companion post "Understanding ChatGPT Work"
  (simonwillison.net/2026/Aug/30/understanding-chatgpt-work/), read in full
  — used only for Claim 9's background context, clearly attributed to its
  own separate URL throughout rather than blended into claims about the
  primary source; (2) the visualize skill's live documentation page
  (codex-tool-reference.simonw.chatgpt.site/skills/visualize), fetched
  directly to independently confirm the CSP quote character-for-character
  before using it in Claim 8; (3) the linked gist containing the full
  shared HTML artifact
  (gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480), fetched raw
  and read in full to extract the D3 rendering mechanism for Claim 7 (a
  detail the blog post itself only partially shows). Not followed: the
  Mastodon/Bluesky/Twitter/newsletter footer links (non-substantive
  author-contact links) and the "OpenAI announced ChatGPT Work" link inside
  the companion post (one level further removed from this source; the
  companion post's own prose was judged sufficient for Claim 9's narrow
  purpose).
- **Important caveat carried through Claim 8 and Source Context**: the
  skill-documentation site quoted for the CSP allowlist
  (codex-tool-reference.simonw.chatgpt.site) was itself built by a ChatGPT
  Work session Willison prompted to reproduce its own tool/skill
  descriptions — per the companion post, "Try to exactly duplicate
  arguments and tool descriptions where possible." This means the CSP text
  is the agent's own self-reported reproduction of its system files, not
  independently-published OpenAI documentation, even though the blog post
  and the skill-documentation page state it identically. Flagged explicitly
  in Claim 8 and reflected in this note's `anecdotal` overall confidence
  rating — the corpus should not treat this skill-file content as
  OpenAI-confirmed until it appears in an official OpenAI documentation
  source.
- **No contradiction meeting the MINER.md §4a filing bar was identified.**
  The one tension noted (enterprise Auto-review oversight vs. an
  individual's inability to retrieve post-hoc code) is documented under
  Cross-References → Contradicts as a scope/audience difference, not filed
  as a formal contradiction issue.
