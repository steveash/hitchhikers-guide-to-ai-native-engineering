---
source_url: https://simonwillison.net/2026/Sep/9/blender-viewer/
source_type: blog-post
title: ".blend URL Viewer"
author: Simon Willison
date_published: 2026-09-09
date_extracted: 2026-09-14
last_checked: 2026-09-14
status: current
confidence_overall: anecdotal
issue: "#3428"
---

# .blend URL Viewer

> Simon Willison reuses a pre-existing, self-vibe-coded browser tool (a
> client-side `.blend` file viewer built on the experimental `jsblender`
> npm package and Three.js, with no server-side conversion step) to display
> a new Blender model. That model was produced by chaining two separate
> frontier-model products end to end: ChatGPT Images 2.5 generates a themed
> reference image, which is then handed to Codex (GPT-6 Astra, high
> reasoning) along with a re-invocation of the self-authored `blender-local`
> skill documented in `blog-simonwillison-blender-coding-agents-macos.md`,
> producing an editable, frame-animated `.blend` scene in 17m51s.

## Source Context

- **Type**: blog-post (Willison's main weblog "Tool" category post — short,
  first-person, links out to the live tool, a GitHub project repo, and a
  ChatGPT share link rather than containing extended prose itself).
- **Author credibility**: Simon Willison is a `trusted-feed` source already
  extensively used in this corpus (creator of Django, Datasette,
  `sqlite-utils`, the `llm` CLI). This post is a first-person account of a
  tool Willison built and a project he ran himself, with the live tool, its
  full client-side source, and the generated project's GitHub repository
  all linked as primary evidence — stronger sourcing than a purely
  descriptive post.
- **Scope**: Covers a single practitioner's single ad hoc session (one
  image-generation prompt, one Blender-modeling prompt) and one
  previously-built personal tool. Does not cover: the tool's own
  build/authoring process (that predates this post and isn't described
  here), reliability across repeated runs, other 3D file formats, or any
  systematic evaluation of `jsblender` or the modeling agent. This is a
  short anecdotal tool-announcement post, not a benchmark or a tutorial.

## Extracted Claims

### Claim 1: The `.blend URL Viewer` renders Blender scenes directly in the browser by parsing `.blend` files entirely client-side, using the experimental `jsblender` npm package for parsing and Three.js for WebGL rendering — no server-side conversion step is involved
- **Evidence**: Direct inspection of the live tool's page source at
  `tools.simonwillison.net/blender-viewer`: its module script imports
  `FontLoader`, `NURBSCurve`, `RoomEnvironment`, and `OrbitControls` from
  `three@0.180.0` (fetched from `cdn.jsdelivr.net`) and loads parsing
  primitives from `https://esm.sh/jsblender@0.0.4?bundle` — all resolved
  live in the browser via an `importmap`, with no build step or bundled
  local copy.
- **Confidence**: anecdotal (single tool instance; no data on `jsblender`'s
  adoption or correctness outside this one tool)
- **Quote**: "The URL must permit cross-origin fetches. jsblender 0.0.4 is primarily validated against Blender 5.x files."
- **Our assessment**: A genuinely novel-to-corpus technical pattern: a full
  binary 3D-scene-format parser and renderer running as static
  client-side JavaScript, with its core parsing dependency at version
  `0.0.4` (pre-1.0, explicitly scoped to "primarily validated against
  Blender 5.x") loaded live from a public ESM CDN rather than vendored or
  pinned via a lockfile. This is convenient for a personal tool shipped in
  an afternoon, but it means the tool's correctness and availability are
  coupled to an unaudited, early-stage third-party package's CDN uptime
  and future releases at the exact pinned version string — see Claim 6.

### Claim 2: The tool's own stated scope is to view Blender scenes by pasting a URL — either a directly CORS-accessible file URL or a GitHub repository link — and it renders mesh geometry with materials, lighting, and optional saved camera positions, plus interactive orbit, wireframe, and model-fitting controls
- **Evidence**: The post's own descriptive dek line, published directly
  under the post title.
- **Confidence**: anecdotal (tool's own self-description, not independently
  verified feature-by-feature against every claimed capability)
- **Quote**: "View Blender .blend files directly in your browser by pasting a URL to a CORS-accessible file or GitHub repository link. The viewer renders mesh geometry with materials, lighting, and optional saved camera positions from Blender 5.x files, and provides interactive orbit controls, wireframe mode, and model fitting capabilities."
- **Our assessment**: A concrete example of a narrow, single-purpose
  personal utility (view one file format, from a URL, in a browser) built
  to solve exactly the sharing problem the post itself demonstrates:
  turning an agent-generated binary artifact into something viewable
  without asking the recipient to install Blender.

### Claim 3: To route around CORS restrictions when fetching a binary file directly off GitHub, the viewer automatically rewrites `github.com/.../blob/...` file-page URLs into `cdn.jsdelivr.net/gh/...` CDN URLs before fetching
- **Evidence**: Direct inspection of the tool's `normalizeURL()` function in
  its client-side source, which pattern-matches `github.com` blob URLs
  (owner/repo/blob/ref/path) and rewrites them to jsDelivr's GitHub CDN
  mirror.
- **Confidence**: anecdotal (single tool's implementation choice)
- **Quote**: "jsDelivr is usually convenient and CORS-friendly for public repositories."
- **Our assessment**: A small, reusable, generalizable pattern for any
  browser-based tool that needs to fetch public-repo binary assets by URL:
  GitHub's own file-serving endpoints are not reliably CORS-enabled for
  arbitrary binary content, so routing through a public CDN mirror of the
  repo is a pragmatic workaround rather than requiring a custom proxy
  server.

### Claim 4: Willison did not build this viewer for this post — it is a pre-existing personal tool ("vibe-coded", in his own framing) that he simply pointed at a new model, illustrating opportunistic reuse of a previously self-built utility for an unplanned purpose
- **Evidence**: Author's direct statement introducing the tool in this post.
- **Confidence**: anecdotal
- **Quote**: "I already had this vibe-coded Blender viewing experiment lying around, so I added that to my tools collection and now you can use it to see my Pluribus blender model in your browser"
- **Our assessment**: This corroborates the pattern already documented in
  `blog-simonwillison-rss-vibe-coded-apps.md` — Willison maintains an
  ever-growing personal "tools collection" (`tools.simonwillison.net`) of
  small, quickly-built utilities that get reused opportunistically well
  after their original purpose. Here the reuse is concrete: a tool
  originally built for *some* earlier Blender-viewing need is repurposed,
  unmodified, to showcase an unrelated new model.

### Claim 5: The new model was produced by chaining two separate frontier-model products across modalities — first generating a themed reference image with ChatGPT Images 2.5, then handing that image to Codex (GPT-6 Astra, "high" reasoning) with an instruction to build a matching editable Blender model using a previously self-authored local skill
- **Evidence**: The post's own sequential narration of the two prompts and
  the explicit hand-off between them ("Then, just to see what would
  happen, I pasted that image into Codex...").
- **Confidence**: anecdotal (single example, one practitioner, one project)
- **Quote**: "Generate a photo of a faberge egg that's themed after the TV show Pluribus - research first"
- **Our assessment**: A concrete text-to-image-to-3D-agent pipeline: an
  image-generation model supplies a visual target, and a separate coding
  agent is then asked to reverse-engineer that target into editable 3D
  geometry via its scripting interface to a desktop application. Unlike
  the earlier TIL's prompts (pure natural-language creative direction,
  e.g. "add a lot of flair"), this session's Blender prompt is grounded by
  an actual reference image rather than by an unconstrained textual
  description — a meaningfully different, more constrained input modality
  for the same underlying skill.

### Claim 6: The image-grounded Blender-modeling prompt explicitly re-invoked the previously self-authored `blender-local` skill by name, reusing the identical `SKILL.md` file (same GitHub path) documented in the earlier TIL post — direct, first-hand evidence for that earlier post's claim that the skill was reused in later sessions
- **Evidence**: The prompt text names the skill directly, and the post's
  "the skill file" link points at the exact same file path,
  `github.com/simonw/gpt-6-astra-blender-pelican-bicycle/blob/main/outputs/blender-local/SKILL.md`,
  already extracted in `blog-simonwillison-blender-coding-agents-macos.md`
  (Claim 7, Concrete Artifacts).
- **Confidence**: anecdotal (one additional confirmed reuse instance; still
  not a sustained-use track record, and the linked file shows no evidence
  of having been updated since its original authoring)
- **Quote**: "Use your blender local skill to create a blender model of this faverge egg"
- **Our assessment**: This is the single highest-value cross-reference in
  this note (see Cross-References → Extends). The earlier TIL post
  asserted the skill "has since [been] used for further Blender
  experiments" but gave no specifics; this post is one of those specific
  instances, with a linked, verifiable prompt and output. It does not,
  however, show the skill being *updated* with anything learned from this
  new session (e.g., no new lessons about jeweled/ornamental geometry or
  procedural-material authoring appear to have been folded back into the
  `SKILL.md`) — so it confirms reuse but not iterative improvement of the
  skill file itself.

### Claim 7: The image-grounded Blender-modeling session, run at "high" reasoning effort, took 17 minutes 51 seconds and produced multiple `.blend` files as output
- **Evidence**: Author's direct elapsed-time statement, and the linked
  GitHub deliverables directory
  (`github.com/simonw/vibe-coded-blender-projects/tree/main/pluribus-faberge-egg/deliverables`),
  which contains two `.blend` files (`Pluribus_Jeweled_Egg.blend`,
  `Pluribus_Jeweled_Egg_v1.blend`, both roughly 7.5MB) plus a `.blend1`
  backup file and three PNG renders.
- **Confidence**: anecdotal (single session, single project, no
  repeated-trial variance data)
- **Quote**: "It churned away for 17m51s and built me several .blend files."
- **Our assessment**: Directionally consistent with the earlier TIL's
  finding that later, more visually complex turns take longer (that
  post's three turns ran 2m39s / 3m51s / 5m59s at "Medium" reasoning for a
  simpler creative-direction task). This session, at "High" reasoning and
  reconstructing a specific ornamental reference image rather than
  following open-ended creative instructions, took roughly 3-7x longer
  than any single turn in that earlier session — but the two are not a
  controlled comparison (different task, different reasoning tier, single
  data points each), so treat this only as a second order-of-magnitude
  anchor (tens of minutes, not seconds) rather than a validated scaling
  curve.

### Claim 8: The generated deliverable is a reproducible, editable, frame-animated Blender scene rather than a static render — the project's own README documents a lid-opening animation driven by frame number and a named rotation-constrained object, organized into named collections, with materials built procedurally rather than from external texture files
- **Evidence**: Direct text from the deliverables directory's `README.md`
  (fetched from
  `raw.githubusercontent.com/simonw/vibe-coded-blender-projects/main/pluribus-faberge-egg/deliverables/README.md`).
- **Confidence**: anecdotal (single generated artifact, self-documented by
  the same session that produced it — not independently verified by
  opening the `.blend` file in Blender)
- **Quote**: "Scrub between frames 1–80 to preview the lid opening."
- **Our assessment**: This is a materially more sophisticated output than
  the earlier TIL's three pelican-bicycle scenes, which were static
  single-frame renders. Here the agent produced a parametric,
  frame-driven animation rig (an object literally named "LID HINGE •
  rotate local X to open" with its X-rotation keyframed from 0° to −28°)
  from a single still reference image — evidence that the underlying
  skill/workflow generalizes from "build a static scene matching a
  description" to "build an animated, riggable mechanism matching an
  image," though again from a single example.

### Claim 9: The project preserves the first modeling pass as a separate file alongside the final version, mirroring the "don't overwrite, keep every iteration" artifact-preservation pattern already documented for this same skill/workflow in the earlier TIL post
- **Evidence**: The deliverables README's "Files" list, which explicitly
  labels one of the two `.blend` files as a preserved earlier draft.
- **Confidence**: anecdotal
- **Quote**: "Pluribus_Jeweled_Egg_v1.blend — preserved first modeling pass."
- **Our assessment**: Directly corroborates
  `blog-simonwillison-blender-coding-agents-macos.md` (Claim 4), where each
  of the three pelican-bicycle turns was saved to a distinct, non-
  overwritten `.blend`/script pair rather than mutating one file in place.
  Two independent sessions of the same practitioner's same workflow both
  show this non-destructive, keep-every-draft file-naming discipline —
  worth treating as a recurring (if still anecdotal, n=2) practice rather
  than a one-off.

## Concrete Artifacts

GitHub-URL-to-CDN rewrite, from the viewer's client-side source
(`tools.simonwillison.net/blender-viewer`):

```js
function normalizeURL(input) {
  const u = new URL(input.trim());

  // Normal GitHub file page:
  // https://github.com/owner/repo/blob/ref/path/file.blend
  if (u.hostname === "github.com") {
    const parts = u.pathname.split("/").filter(Boolean);
    const blobIndex = parts.indexOf("blob");
    if (blobIndex === 2 && parts.length >= 5) {
      const owner = parts[0];
      const repo = parts[1];
      const ref = parts[3];
      const path = parts.slice(4).join("/");
      // jsDelivr is usually convenient and CORS-friendly for public repositories.
      return `https://cdn.jsdelivr.net/gh/${owner}/${repo}@${ref}/${path}`;
    }
  }
  return u.href;
}
```

Live-resolved dependency import map, from the same page's `<script
type="importmap">` (no local install, no lockfile — every load resolves
against these exact CDN URLs):

```json
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.180.0/examples/jsm/"
  }
}
```
```js
import * as THREE from "three";
import { FontLoader } from "three/addons/loaders/FontLoader.js";
import { NURBSCurve } from "three/addons/curves/NURBSCurve.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { /* parsing primitives */ } from "https://esm.sh/jsblender@0.0.4?bundle";
```

Deliverables directory listing (via GitHub API,
`simonw/vibe-coded-blender-projects/pluribus-faberge-egg/deliverables`):

```
Pluribus_Jeweled_Egg.blend        7,621,564 bytes  (finished editable scene)
Pluribus_Jeweled_Egg.blend1       7,604,022 bytes  (Blender auto-backup)
Pluribus_Jeweled_Egg.png          3,903,585 bytes  (1440x1800 studio render)
Pluribus_Jeweled_Egg_ThreeQuarter.png  1,979,271 bytes
Pluribus_Jeweled_Egg_v1.blend     7,528,955 bytes  (preserved first modeling pass)
README.md                             1,485 bytes
egg_preview.png                   1,035,793 bytes  (first-pass preview)
```

Full deliverables `README.md` (verbatim, fetched from
`raw.githubusercontent.com/simonw/vibe-coded-blender-projects/main/pluribus-faberge-egg/deliverables/README.md`):

```markdown
# PLURIBUS — Jeweled Desert Egg

An editable Blender 5.1 scene modeled from the supplied photograph. The yellow enamel egg, gold scrollwork, pearls, emerald accents, desert cameos, ivory portraits, miniature choir, conductor, and marble pedestal are built as geometry. Human figures and ornamental details are a stylized interpretation of the single view.

## Open the model

Open `Pluribus_Jeweled_Egg.blend` in Blender. The scene is saved in its open presentation pose at frame 80, with studio lighting and a portrait camera ready to render.

- **Frame 80:** open egg.
- **Frame 1:** closed egg.
- Scrub between frames 1–80 to preview the lid opening.
- The object **LID HINGE • rotate local X to open**, in collection **04 • Hinged crown**, controls the upper half and its ornament. Its X rotation is animated from 0° to −28°.
- Major parts are grouped in named collections. Repeated pearls and tiny stones are combined into meshes; they remain editable in Edit Mode.
- All materials are procedural. No external textures are required.

## Files

- `Pluribus_Jeweled_Egg.blend` — finished editable scene.
- `Pluribus_Jeweled_Egg.png` — 1440 × 1800 studio render.
- `Pluribus_Jeweled_Egg_v1.blend` — preserved first modeling pass.
- `egg_preview.png` — first-pass preview.

The reproducible scene-building and polishing scripts are in the adjacent `work` directory.
- `Pluribus_Jeweled_Egg_ThreeQuarter.png` — additional view for inspecting the scene in depth.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-rss-vibe-coded-apps.md` — the "personal tools
    collection, reused opportunistically well after original purpose"
    pattern that post describes in the abstract (Claim about Willison's
    `tools.simonwillison.net` Atom feed) is directly instantiated here:
    the `.blend` viewer is exactly such a tool, built earlier and reused
    for an unrelated new model.
  - `blog-simonwillison-blender-coding-agents-macos.md` (Claim 4) — this
    post's preserved-`v1`-file pattern (Claim 9 above) matches that post's
    non-overwriting, keep-every-turn file discipline.

- **Contradicts**: None found.

- **Extends**:
  - `blog-simonwillison-blender-coding-agents-macos.md` (Claim 7, Claim 9)
    — that note documented the *creation* of the `blender-local` skill and
    Willison's assertion, without a concrete example, that he'd since
    reused it for "further Blender experiments." This post supplies the
    first concrete, independently linkable instance of that reuse (Claim 6
    above): the identical `SKILL.md` file, invoked by name, in a separate
    project weeks later, this time driven by an image rather than by pure
    natural-language description — a materially different and more
    complex input modality (Claim 5, Claim 8) than the original
    scene-from-text-prompt session.
  - `blog-simonwillison-agentsview-custom-model-price.md` — the earlier
    Blender post used AgentsView to estimate the session's API-equivalent
    cost; this post gives no cost figure for the (longer, "high"
    reasoning) image-grounded session, so the cost/reasoning-tier
    relationship for this workflow remains only partially documented
    across the two posts.

- **Novel**:
  - First corpus source describing a client-side, in-browser binary `.blend`
    file parser and WebGL renderer (via the `jsblender` npm package), with
    no server-side conversion step — a technical pattern distinct from
    every other corpus example of agent-generated 3D content, which so far
    only covers *creating* `.blend` files, not building tooling to *view*
    them without the Blender desktop app.
  - First corpus source documenting a GitHub-URL-to-CDN (jsDelivr)
    rewrite as a practical CORS workaround for browser tools fetching
    public-repo binary assets by URL.
  - First corpus source documenting a two-product, cross-modality pipeline
    where one frontier model's image output is used as the direct visual
    reference input to a separate coding agent's 3D-modeling session.
  - First corpus source showing a coding-agent-driven Blender workflow
    producing a frame-animated, riggable mechanism (a hinged lid) rather
    than a static single-frame scene.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Strengthens the existing
  recommendation (informed by `blog-simonwillison-blender-coding-agents-macos.md`)
  about self-authored skills persisting and being reused — this source
  supplies the first *concrete, verifiable* reuse instance rather than
  just the original author's unsubstantiated claim of reuse. If the guide
  cites that earlier post's Claim 9 ("I have since used [it] for further
  Blender experiments"), it should now cite this post alongside it as the
  first-hand confirmation, and can additionally note the reuse held up
  across a materially different input modality (image-grounded vs.
  pure-text prompting) without any changes to the skill file itself.
- **Chapter 01 (Daily Workflows)**: Claim 4's "vibe-coded tool lying
  around, reused for an unrelated new purpose" pattern is a small,
  concrete illustration worth pairing with
  `blog-simonwillison-rss-vibe-coded-apps.md` — building small personal
  utilities has a compounding payoff because they get reused for
  purposes their author didn't originally anticipate.
- **Chapter 06 (Security / Threat Model)**: Claim 1's dependency
  structure (an unpinned-to-lockfile, pre-1.0 (`0.0.4`) third-party
  parsing library, loaded live from a public ESM CDN on every page load,
  with no local vendoring) is a small but genuine supply-chain/
  availability fragility worth a one-line mention if the chapter discusses
  risks specific to quickly-shipped personal/internal tools rather than
  production software — the tool's correctness and uptime are fully
  outsourced to `esm.sh` and `jsdelivr.net` continuing to serve that exact
  version string indefinitely.

## Extraction Notes

- Followed five linked pages beyond the source weblog post itself, within
  MINER.md §1's "up to 5" guidance: the live tool's full page source at
  `tools.simonwillison.net/blender-viewer` (read the client-side JS
  directly, not just rendered output); the GitHub deliverables directory
  listing (via the GitHub contents API); the deliverables `README.md`
  (fetched raw); the pre-existing `SKILL.md` (confirmed identical path to
  the one already fully extracted in
  `blog-simonwillison-blender-coding-agents-macos.md`, so not
  re-transcribed here — see that note for its content); and attempted the
  linked ChatGPT share page for the image-generation prompt, which is
  client-rendered and did not yield conversation text via a direct fetch
  — the image-generation prompt quoted in Claim 5 is instead taken
  verbatim from the blog post's own text, which quotes it directly.
- Did not fetch the `.blend` binary files themselves or the "work"
  directory's scene-building scripts referenced by the README; the
  README's own description was sufficient to document the claims above
  without needing the raw scripts.
- This post is short (under 200 words of original prose); most of the
  evidentiary depth in this note comes from the linked tool's source code
  and the linked GitHub project's README/file listing, not from additional
  prose in the blog post itself. Flagged in case the Assayer expects claim
  density comparable to a long-form article — the claim count here (9) is
  driven by artifact inspection rather than by extended narrative text.
