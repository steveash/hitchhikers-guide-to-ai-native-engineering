---
source_url: https://simonwillison.net/2026/Sep/7/equal-earth/
source_type: blog-post
title: "Tool: Mercator ↔ Equal Earth"
author: Simon Willison
date_published: 2026-09-07
date_extracted: 2026-09-11
last_checked: 2026-09-11
status: current
confidence_overall: anecdotal
issue: "#3374"
---

# Tool: Mercator ↔ Equal Earth

> A one-paragraph "beat" post in which Willison has GPT-6 Astra (medium) in ChatGPT Work
> build a D3/Canvas map-projection-morphing tool in a single delegation, adding a new
> data-point to the corpus: continued cross-vendor vibe coding (ChatGPT, not Claude) applied
> to a geospatial visualization task, plus a concrete generated-code artifact that reveals
> how the model chose to approximate the transition (linear blend of raw projected
> coordinates, not a true equal-area interpolation).

## Source Context

- **Type**: blog-post (Simon Willison's blog; a "beat" — his shortest post format, used for
  link/tool drops rather than long-form essays). The entire body text is one sentence plus
  an embedded demo video; there is no extended commentary, workflow narration, or reflection.
- **Author credibility**: Simon Willison is the creator of Django, maintainer of 200+ tools
  at tools.simonwillison.net, and a `trusted-feed` source in this repo (see
  [[blog-simonwillison-vibe-coding-agentic-engineering]] and
  [[blog-simonwillison-liteparse-browser]] for his established credibility as a first-person
  AI-tooling practitioner). This post is far thinner than his typical workflow write-ups —
  it is a link-blog entry, not an essay — but the linked artifact (the deployed tool itself)
  is publicly inspectable and was read directly for this note.
- **Scope**: Covers a single act of tool creation — an interactive Mercator↔Equal Earth map
  projection morph — built by GPT-6 Astra (medium) in ChatGPT Work, in one shared
  conversation. Does NOT cover: the underlying prompt(s) used, any iteration or debugging
  narrative, code review practices, or general reflections on the vibe-coding practice
  (unlike [[blog-simonwillison-vibe-coding-agentic-engineering]] or
  [[blog-simonwillison-liteparse-browser]], which document full workflows). The ChatGPT
  share link referenced in the post (`chatgpt.com/share/6a9ee520-...`) renders its
  conversation content via client-side JavaScript that could not be extracted through
  automated fetching for this note (see Extraction Notes).

## Extracted Claims

### Claim 1: Willison used GPT-6 Astra at "medium" reasoning effort — not a high/max tier — to generate a complete interactive D3 visualization in a single delegation
- **Evidence**: Direct statement in the post body naming the specific model and tier used for this task.
- **Confidence**: anecdotal (single example, self-reported)
- **Quote**: "I got curious about the Equal Earth map projection that was recently voted on at the UN so I had GPT-6 Astra (medium) in ChatGPT Work build me this animated transition between Mercator and Equal Earth using D3."
- **Our assessment**: This is a small but concrete data point that "medium" reasoning effort is treated by Willison as sufficient for a self-contained, moderately technical visualization task (custom map-projection math plus Canvas animation loop), rather than reaching for a "high" or "max" tier. It's consistent with the cost/quality tradeoff pattern documented in [[blog-simonwillison-astra-pelican-comparison-grid]] Claim 4 (Astra's "low" tier already outperforming competitors on a simpler visual task), suggesting Astra's lower reasoning tiers are being treated by Willison as production-viable for scoped generative-visualization work, not just cheap toys.

### Claim 2: The task was delegated to ChatGPT/GPT-6 Astra rather than Claude Code, continuing Willison's pattern of cross-vendor tool selection for vibe-coded personal tools
- **Evidence**: The post explicitly names "ChatGPT Work" (OpenAI's product) as the environment, with no Claude/Anthropic tooling involved in this instance.
- **Confidence**: anecdotal
- **Quote**: "...I had GPT-6 Astra (medium) in ChatGPT Work build me this animated transition..."
- **Our assessment**: Willison's corpus consistently shows him picking whichever model/tool is convenient or currently interesting for a given personal project ([[blog-simonwillison-liteparse-browser]] used Claude Code + Opus 4.7 with a GPT-5.5/Codex cross-model audit; this post uses ChatGPT/GPT-6 Astra alone, with no stated cross-model verification step). For the guide, this is a minor but real counter-example to any framing that vibe-coding-with-Claude is the default pattern in the corpus — practitioners route personal, low-stakes tools to whatever model is at hand.

### Claim 3: The published tool documents its own approximation limitation directly in its UI copy — the projection blend is a coordinate-space linear interpolation, not a true equal-area transition
- **Evidence**: Extracted directly from the deployed tool's HTML/JS source at https://tools.simonwillison.net/equal-earth (fetched for this note). The generated code (see Concrete Artifacts) computes intermediate frames by linearly blending the raw Mercator and Equal Earth projection functions' output coordinates for each point, scaled independently, rather than any area-preserving interpolation.
- **Confidence**: anecdotal (single generated artifact, but independently verifiable — the code and its self-disclosed limitation are both publicly inspectable)
- **Quote**: "Intermediate frames blend projected coordinates; they are not equal-area."
- **Our assessment**: This is the most technically interesting extraction from this source. The generated tool is honest about its own approximation in its own UI copy — whether that caveat originated from Willison's prompt, from GPT-6 Astra's own commentary during generation, or from Willison editing the output cannot be determined from the blog post alone (the ChatGPT share link that would clarify this was not accessible — see Extraction Notes). Regardless of origin, it's a good concrete example of a vibe-coded artifact that surfaces its own known limitation to end users rather than silently misrepresenting the geometry — a small but positive UX/honesty pattern worth noting for any guide section on shipping AI-generated tools with known approximations.

### Claim 4: The tool was published under Willison's `tools.simonwillison.net` personal-tools domain rather than embedded inline in the blog post
- **Evidence**: The blog post links out to a separate URL (`tools.simonwillison.net/equal-earth`) rather than embedding the interactive visualization directly in the blog page; the blog post itself only embeds a static video recording of the tool in action.
- **Confidence**: settled (directly observable from the post's structure and the separate tool URL)
- **Quote**: "(no direct quote; see paraphrase in Our assessment)"
- **Our assessment**: This continues the publishing pattern already documented in [[blog-simonwillison-rss-vibe-coded-apps]] Claim 1 and Claim 5 — personal vibe-coded tools accumulate on a dedicated low-friction hosting surface (200+ tools as of that note) with blog posts serving as lightweight announcements/demos rather than the tools' actual home. This entry is a fresh, dated (September 2026) data point confirming that pattern is still active four months after the RSS/vibe-coded-apps post.

### Claim 5: The tool's map projection blend was implemented using D3's low-level "raw" projection functions (`d3.geoMercatorRaw`, `d3.geoEqualEarthRaw`) rather than D3's higher-level projection/interpolation utilities
- **Evidence**: Extracted directly from the deployed tool's source code (see Concrete Artifacts). The `projectionAt(blend)` function calls both raw projection functions per-point inside a custom `d3.geoProjection(...)` callback and linearly interpolates their outputs, rather than using any built-in D3 interpolation helper.
- **Confidence**: anecdotal (single code sample)
- **Quote**: "(no direct quote; see code in Concrete Artifacts)"
- **Our assessment**: This is a specific, verifiable technical choice in the generated code: rather than reaching for a library-level "morph between projections" helper (D3 doesn't ship one), the model composed the transition from D3's primitive raw-projection functions plus a custom scale/translate/clip pipeline, including an explicit epsilon-clamp to avoid Mercator's pole singularity. That's a reasonable and idiomatic use of D3's lower-level API surface for a task the library doesn't directly support out of the box — a small positive signal about GPT-6 Astra's ability to compose correct solutions from a library's primitives rather than only its documented high-level recipes.

## Concrete Artifacts

### Full blog post body text (verbatim, entire post)

```
Source: https://simonwillison.net/2026/Sep/7/equal-earth/
Posted 7th September 2026 at 4:24 pm
Tags: geospatial, d3, vibe-coding, gpt-6-astra

Title: Mercator ↔ Equal Earth

Beat summary (link description):
"View an interactive animated map that morphs between Mercator and Equal
Earth projections using a slider or play button. The visualization
demonstrates how different map projections represent the world, with
controls to blend between the two projection types and observe how they
preserve different geographic properties."

Body:
"I got curious about the Equal Earth map projection that was recently
voted on at the UN so I had GPT-6 Astra (medium) in ChatGPT Work build
me this animated transition between Mercator and Equal Earth using D3."

[Embedded video demo, no additional prose.]
```

### Generated projection-blend logic (verbatim, from the deployed tool's source)

```js
// Source: https://tools.simonwillison.net/equal-earth (view-source, fetched 2026-09-11)
// Built by GPT-6 Astra (medium) per the blog post; this is the actual shipped code.

const eqWidth = d3.geoEqualEarthRaw(Math.PI, 0)[0];
const eqHeight = d3.geoEqualEarthRaw(0, Math.PI / 2)[1];

function projectionAt(blend) {
  const innerWidth = width - 38;
  const innerHeight = height - 90;

  const mercatorScale =
    Math.min(innerWidth, innerHeight) / (2 * Math.PI);

  const equalEarthScale = Math.min(
    innerWidth / (2 * eqWidth),
    innerHeight / (2 * eqHeight)
  );

  const halfHeight =
    (1 - blend) * Math.PI * mercatorScale +
    blend * eqHeight * equalEarthScale;

  return d3.geoProjection((lambda, phi) => {
    // Avoid Mercator's singularities at the exact poles.
    const safePhi = Math.max(
      -Math.PI / 2 + 1e-7,
      Math.min(Math.PI / 2 - 1e-7, phi)
    );
    const a = d3.geoMercatorRaw(lambda, safePhi);
    const b = d3.geoEqualEarthRaw(lambda, phi);

    return [
      (1 - blend) * a[0] * mercatorScale +
        blend * b[0] * equalEarthScale,
      (1 - blend) * a[1] * mercatorScale +
        blend * b[1] * equalEarthScale
    ];
  })
    .scale(1)
    .translate([width / 2, height / 2])
    .precision(0.4)
    .clipExtent([
      [18, height / 2 - halfHeight],
      [width - 18, height / 2 + halfHeight]
    ]);
}
```

### Self-disclosed limitation text shipped in the tool's UI (verbatim)

```
Source: https://tools.simonwillison.net/equal-earth (view-source, fetched 2026-09-11)

"Intermediate frames blend projected coordinates; they are not equal-area.
Mercator is cropped at ±85.05° latitude.
Each endpoint is fitted to the available space."
```

### Stack used (from the tool's source)

```
d3@7.9.0 (CDN: jsdelivr)
topojson-client@3.1.0 (CDN: jsdelivr)
world-atlas@2.0.2 countries-110m.json (CDN: jsdelivr, for land/border geometry)
Canvas 2D rendering (not SVG) via d3.geoPath(projection, ctx)
d3.timer() driving a manual play/pause/reverse animation loop
ResizeObserver for responsive canvas sizing
prefers-reduced-motion respected on initial autoplay decision
```

## Cross-References

- **Corroborates**:
  - [[blog-simonwillison-rss-vibe-coded-apps]] Claim 1 ("Vibe-coding accelerates app
    development to the point where release cadence becomes blog-post-like") and Claim 5
    (abundance of personal vibe-coded tools visible at scale in Willison's own portfolio):
    this post is a fresh, dated instance of exactly that pattern — a small, single-purpose,
    personally-motivated tool, announced in a one-paragraph blog post and hosted on
    `tools.simonwillison.net` rather than as a standalone product.
  - [[blog-simonwillison-astra-pelican-comparison-grid]] Claim 4 (Astra's low reasoning
    tier outperforming competitors on visual-generation tasks at low cost): this post is
    independent anecdotal support that Willison treats Astra's non-maximum reasoning tiers
    as adequate for real visualization work, not just benchmark curiosities.
- **Contradicts**: None identified. Nothing in this source materially opposes an existing
  corpus note.
- **Extends**:
  - [[blog-simonwillison-liteparse-browser]]: That post documents a full, narrated
    Claude-Code-based workflow (notes.md → plan.md, TDD, cross-model audit, deployment
    delegation) for a browser-native tool. This post is the minimal-effort opposite end of
    the same spectrum — a single-shot ChatGPT delegation with zero narrated workflow, no
    stated review step, and no cross-model audit. Read together, they bracket the range of
    documented Willison vibe-coding effort levels, from fully narrated multi-step harness
    engineering to a one-sentence "I had it build me this."
  - [[blog-simonwillison-vibe-coding-agentic-engineering]] Claim 12 territory
    (blast-radius-conditioned acceptability of unreviewed AI code, drawn from
    [[blog-simonwillison-liteparse-browser]]): this tool is another zero-stated-review,
    static/client-side, no-data-transfer artifact, consistent with the same blast-radius
    reasoning, though this post does not itself articulate that reasoning — it simply
    ships the tool.
- **Novel**:
  - The generated-code inspection in Claims 3 and 5 is new to the corpus: this is the
    first source note in this collection to extract and analyze the *actual shipped code*
    of a Willison-vibe-coded tool at the implementation-detail level (specific D3 API
    choices, an explicit numerical-approximation caveat baked into the UI). Prior
    vibe-coding notes on Willison's blog document his prompts and workflow narrative but
    not the generated code's internal technical choices in this depth, because the source
    posts either didn't link a directly-inspectable static artifact or the Miner did not
    fetch it.

## Guide Impact

- **Chapter 03 (AI-native development patterns)**: Add this as a minor supporting example
  under any discussion of vibe-coding effort levels — specifically, that "vibe coding" in
  Willison's own use spans from fully-narrated, multi-step, reviewed harness workflows
  ([[blog-simonwillison-liteparse-browser]]) down to single-sentence, single-model,
  no-narration delegations like this one. If the guide presents a spectrum or maturity
  ladder of vibe-coding effort, this source is a concrete anchor for the "minimal effort"
  end for a small, self-contained visualization tool.
- **Chapter 03 / Chapter 04 (Context Engineering or output verification)**: If the guide
  ever discusses shipping AI-generated tools with known numerical/algorithmic
  approximations, cite the "Intermediate frames blend projected coordinates; they are not
  equal-area" UI copy as a small positive example of surfacing an artifact's own limitation
  to end users rather than silently misrepresenting correctness. This is a narrow,
  single-example data point — not strong enough to generalize into a rule on its own.
- No changes recommended to any existing chapter recommendation; this source is
  incremental corroboration and a minor illustrative example, not grounds for new guidance.

## Extraction Notes

- **This is a "beat" — Willison's shortest post format**: the entire prose body is one
  sentence. This note is necessarily thinner on narrated-workflow claims than notes on his
  longer essays (e.g. [[blog-simonwillison-vibe-coding-agentic-engineering]],
  [[blog-simonwillison-liteparse-browser]]) because there is no narrated workflow to
  extract — Willison did not describe his prompt(s), any iteration, or his review process.
  To reach a substantive claim count, this note supplements the sparse blog text with
  direct inspection of the deployed tool's own source code (fetched via `curl` from
  `tools.simonwillison.net/equal-earth`), which is a legitimate primary artifact linked
  directly from the post.
- **ChatGPT share link could not be extracted**: the post links to
  `https://chatgpt.com/share/6a9ee520-c82c-83ea-8111-2f7050c08638`, which would likely
  contain the actual prompt(s) Willison used and any back-and-forth with GPT-6 Astra.
  That page renders its conversation content via client-side JavaScript/API calls that
  require an authenticated browser session; automated fetching (`curl`, WebFetch) returned
  only the page shell (title, OpenGraph metadata, feature-flag JSON) with no conversation
  text. No claim in this note is based on that page's content. If the Assayer or a future
  Miner has browser-based access, re-checking that link could surface the actual prompt
  wording, which would materially improve this note's Claim 1/2/3 confidence.
  - **Guardian article context** (`theguardian.com/world/2026/sep/04/un-vote-world-map-mercator-equal-earth-africa`,
  linked from the post as the origin of Willison's curiosity) was fetched but not quoted
  in this note — it is background context for why Willison built the tool, not itself a
  claim about AI-native engineering, and quoting it would be outside this note's scope.
- **No sub-pages beyond the tool source and the two linked context articles were
  followed.** The "Recent articles" sidebar links (Navier–Stokes post, Astra pelican
  comparison grid, OpenAI rogue-agent-wikis post) are unrelated recommended-reading widgets,
  not content this post references; the pelican-comparison-grid post is already a separate
  source note in this corpus ([[blog-simonwillison-astra-pelican-comparison-grid]]).
- **Confidence ceiling: anecdotal**: single practitioner, single tool, no narrated
  workflow, no comparison to alternative approaches. The code-inspection claims (3, 5) are
  independently verifiable (the code is public) but still describe only one generated
  artifact.
