---
source_url: https://simonwillison.net/2026/Jul/21/nativ/
source_type: blog-post
title: "Nativ: Run AI models locally on your Mac"
author: Simon Willison (link post about Prince Canuma's Nativ)
date_published: 2026-07-21
date_extracted: 2026-07-26
last_checked: 2026-07-26
status: current
confidence_overall: emerging
issue: "#2242"
---

# Nativ: Run AI models locally on your Mac

> Simon Willison's three-paragraph link post introduces Nativ, a macOS desktop app by
> Prince Canuma (creator of the MLX-VLM library) that wraps MLX in a chat interface plus a
> localhost API server. Following the linked project site and GitHub README — required
> reading, since the blog post itself is thin — reveals a more substantive tool than the
> post alone suggests: a dual OpenAI- and Anthropic-compatible local server, a curated
> three-model partner library spanning three different vendors, GUI-exposed advanced
> inference controls (KV-cache quantization, prefix caching, speculative decoding), and an
> explicit "100% open source" positioning against "proprietary shells built on top of
> open-source engines they don't own."

## Source Context

- **Type**: blog-post (simonwillison.net "Link Blog" entry, ~120 words, published 2026-07-21
  at 2:22pm; sourced via Hacker News per the post's "via" link). Willison's own text is a
  brief endorsement, not an evaluation — no benchmarks, no hands-on quality assessment, no
  screenshots described in his prose.
- **Author credibility**: Simon Willison is the creator of Django and one of the most
  widely-cited independent LLM-tooling commentators in this corpus's trusted-feed list. He
  has no vendor affiliation with Nativ or Prince Canuma's projects; his endorsement here is
  personal enthusiasm ("I'm really excited about his new project") rather than an in-depth
  review. Prince Canuma, the developer, is independently credible in this domain as the
  author of MLX-VLM, an existing, widely-used library for running vision-LLMs on Apple
  Silicon via MLX.
- **Scope**: This note extracts from three sources reached by following links per
  MINER.md §1 (the blog post itself was too thin to stand alone): (1) Willison's blog post,
  (2) the Nativ project landing page (blaizzy.github.io/nativ/), and (3) the Nativ GitHub
  README (github.com/Blaizzy/nativ). Covers: what Nativ is, its feature set, its local API
  server (endpoints, default port, auth), its curated model library, its coding-agent
  integrations, and its open-source positioning. Does NOT cover: independent hands-on
  quality testing of Nativ (no corpus source has used it yet), performance benchmarks
  against LM Studio or Ollama, or download/adoption numbers.

## Extracted Claims

### Claim 1: Nativ wraps MLX-VLM in a full macOS desktop application, offering both a chat interface and a localhost API server for accessing models — similar in shape to LM Studio
- **Evidence**: Willison's direct characterization, drawing an explicit comparison to LM
  Studio (an existing local-inference app).
- **Confidence**: settled (the app's basic shape — chat UI plus local server — is
  independently confirmed by the GitHub README and landing page)
- **Quote**: "I'm really excited about his new project, which wraps MLX in a full macOS
  desktop application. It's similar in shape to LM Studio, providing both a chat interface
  and a localhost API server for accessing models."
- **Our assessment**: The LM Studio comparison is a useful orientation point for readers
  already familiar with that tool, but as Claims 4–6 below show, Nativ's local server
  surface (dual OpenAI/Anthropic compatibility, named coding-agent integrations, advanced
  inference controls) is more elaborated than a bare "chat + server" description conveys.

### Claim 2: Nativ auto-detects and lists MLX models already present in the user's Hugging Face cache directory
- **Evidence**: Willison's direct first-person observation of the app's behavior on his own
  machine.
- **Confidence**: anecdotal (single practitioner's first-run observation; not independently
  reproduced by another corpus source)
- **Quote**: "The app picked up MLX models I had already tried that were present in my
  Hugging Face cache directory, which was a nice touch."
- **Our assessment**: This is a small but concrete UX detail: Nativ avoids re-downloading
  models a user has already fetched via other MLX tooling (e.g., `mlx_vlm` directly, or
  another MLX-based app), reducing duplicate multi-gigabyte downloads. It is a specific,
  checkable claim about cache-directory interoperability, not a vague usability assertion.

### Claim 3: Prince Canuma, Nativ's developer, previously created the MLX-VLM Python library, an established tool for running vision-LLMs via MLX on a Mac
- **Evidence**: Willison's direct attribution, given as context for why he trusts the new
  project.
- **Confidence**: settled (MLX-VLM is a verifiable, existing GitHub project;
  github.com/Blaizzy/mlx-vlm is linked directly from the post)
- **Quote**: "Prince Canuma is the developer behind the excellent [MLX-VLM] Python library
  for running vision-LLMs using MLX on a Mac."
- **Our assessment**: This is the credibility anchor for the rest of the post: Nativ is not
  a first-time author's untested project but a second product from someone with a track
  record in the exact technical domain (MLX-based vision-LLM inference) that Nativ builds
  on. `mlx-vlm` itself was already referenced (without a source note) as the library
  Ronacher's `pi-ds4`/`ds4.c` ecosystem discussion implicitly sits alongside — this source
  is the first in the corpus to document Canuma and MLX-VLM directly.

### Claim 4: Nativ's local server exposes both OpenAI-compatible and Anthropic-compatible API endpoints simultaneously, at a default address of `http://127.0.0.1:8080`, configurable via a Developer page
- **Evidence**: Verbatim README documentation, including a worked `curl` example and an
  explicit endpoint list.
- **Confidence**: settled (official project documentation with a specific, checkable
  default port and endpoint paths)
- **Quote**: "By default, the app exposes its server at `http://127.0.0.1:8080`. You can
  change the host and port in the Developer page, which also lists every available endpoint
  and lets you copy URLs directly." / "The server includes: OpenAI-compatible
  `/v1/chat/completions`, `/v1/responses`, `/v1/models`, image, and audio routes.
  Anthropic-compatible `/v1/messages` and token-counting routes. `/health`, `/metrics`,
  cache statistics, cache reset, and model unload endpoints."
- **Our assessment**: Dual OpenAI- and Anthropic-compatible surfaces on a single local
  server is not documented elsewhere in this corpus's local-inference coverage — every
  other local-serving tool this corpus has captured (`litert-lm serve` in
  `blog-google-gemma-4-12b-laptop-ai-edge.md` Claim 6/7, Ollama/LM Studio in
  `blog-jetbrains-air-acp-local-models.md` Claim 5) is described as OpenAI-compatible only.
  Anthropic-compatible endpoints matter specifically for tools built against the Anthropic
  Messages API (e.g., Claude Code when pointed at a custom base URL) — Nativ's README names
  Claude Code explicitly among its supported integrations (Claim 6), and the dual-protocol
  server is the mechanism that makes that specific integration possible without a
  translation shim.

### Claim 5: Nativ's local server optionally requires an API key (Bearer-token auth) to protect its management endpoints, generated at first launch
- **Evidence**: README installation walkthrough and API-usage example.
- **Confidence**: settled (documented, specific auth mechanism)
- **Quote**: "Optionally generate an API key to protect the server's management endpoints."
  / "If you enabled a server API key, also send it as a Bearer token: `-H 'Authorization:
  Bearer your-api-key'`"
- **Our assessment**: This is a concrete security-relevant detail absent from the blog post
  itself: a localhost server with no auth by default is a reasonable choice for a
  single-user desktop tool, but the optional API key is what makes it safe to expose the
  server's management endpoints (which include cache reset and model unload — not just
  inference) on a shared or multi-user machine.

### Claim 6: Nativ names five specific coding-agent integrations it can serve as a local model backend for: Codex, Claude Code, Pi, Hermes, and OpenCode
- **Evidence**: Both the landing page ("Your tools. Your models... Pi, Codex, Claude Code,
  Hermes, OpenCode... One model server. Every coding agent.") and the README feature table
  ("Coding-tool integrations: Configure and launch Codex, Claude Code, Pi, Hermes, and
  OpenCode against models served by Nativ.") name the identical five-tool list.
- **Confidence**: settled (named, specific, and consistent across two independent pages of
  the same project's own documentation)
- **Quote**: "Configure and launch Codex, Claude Code, Pi, Hermes, and OpenCode against
  models served by Nativ."
- **Our assessment**: This is a materially different integration list from the
  `litert-lm serve` list in `blog-google-gemma-4-12b-laptop-ai-edge.md` Claim 6 (OpenClaw,
  Hermes, OpenCode, Pi, Continue, Aider, Open WebUI). The two lists overlap on Hermes, Pi,
  and OpenCode but diverge elsewhere: Nativ names Codex and Claude Code explicitly (plausible
  given its Anthropic-compatible endpoint from Claim 4) but not Continue, Aider, OpenClaw, or
  Open WebUI; Google's list names Continue, Aider, and OpenClaw but not Codex or Claude Code.
  Neither this source nor the Google source explains why each vendor curated a different
  subset — likely reflecting which tools each team actually tested rather than a technical
  incompatibility with the omitted tools.

### Claim 7: Nativ's landing page curates exactly three "partner" models at launch, one each from Google, Cohere, and Liquid AI, with a stated recommendation mechanism ("Nativ recommends the right partner model for your hardware")
- **Evidence**: Verbatim landing-page model table.
- **Confidence**: settled (specific, named models with specific size/context figures, from
  the project's own marketing page)
- **Quote**: "Run standout open models from Google, Cohere, and Liquid AI. Nativ recommends
  the right partner model for your hardware." — table: "Gemma 4 E2B Instruct / Google /
  128k / 10.28 GB / VISION + AUDIO", "North Mini Code / Cohere / 500k / 19.38 GB / CODE +
  TOOLS", "LFM2.5-VL 1.6B / Liquid AI / 128k / 3.20 GB / VISION + LANGUAGE"
- **Our assessment**: A three-model, three-vendor curated launch library is a specific
  design choice worth noting against `blog-ronacher-local-models-focus-polish.md` Claim 1's
  diagnosis that local setup requires the user to choose among an overwhelming model/engine/
  quantization matrix. Nativ's curation narrows model choice to three pre-vetted options
  with an automatic hardware-fit recommendation, rather than exposing the full Hugging Face
  MLX catalog by default (though the browsable library is also available — see Concrete
  Artifacts). None of the three named models (Gemma 4 E2B, North Mini Code, LFM2.5-VL 1.6B)
  has a dedicated source note elsewhere in this corpus; Cohere's North Mini Code and Liquid
  AI's LFM2.5-VL are new model names to the corpus.

### Claim 8: Nativ's README and landing page explicitly position the project as "100% open source" and MIT-licensed, in direct contrast to competing local-AI apps described as "proprietary shells built on top of open-source engines they don't own"
- **Evidence**: The landing page's dedicated "Manifesto" section, framed as a first-person
  philosophy statement.
- **Confidence**: anecdotal (a values/positioning statement by the project's own author, not
  an empirical or technical claim; the specific competitors being described as "proprietary
  shells" are not named)
- **Quote**: "The other 'local AI' apps you've heard of? They're proprietary shells built on
  top of open-source engines they don't own. They keep the UI closed, add a paywall, and
  hope you don't look under the hood. We built in the open. The desktop app is open too.
  Every line. Every model loader. Every telemetry chart. You can read it, fork it, or send a
  pull request tonight. No VC roadmap. No enterprise tier. No dark pattern that turns your
  prompts into training data. Just software made by researchers and hackers, for researchers
  and hackers."
- **Our assessment**: This is a pointed, unprompted competitive claim — the manifesto
  implicitly targets tools like LM Studio (which Willison's own post compares Nativ to in
  Claim 1, and which is proprietary/closed-source) without naming them. It is also a
  values-alignment echo of Armin Ronacher's hyperscaler-independence framing in
  `blog-ronacher-local-models-focus-polish.md` Claim 14 ("a hammer that's locked behind a
  subscription in a data center in another country does not qualify" as local) — both treat
  full openness (weights, engine, *and* application code) as the meaningful bar for "local,"
  not merely on-device execution. See Cross-References for the specific contrast this draws
  with `blog-google-gemma-4-12b-laptop-ai-edge.md`'s closed-source Gallery/Eloquent apps.

### Claim 9: Nativ exposes GUI-level advanced inference controls, including sampling parameters, thinking budgets, structured output, KV-cache quantization, prefix caching, and speculative decoding
- **Evidence**: README feature table entry.
- **Confidence**: settled (a specific, named list of inference-tuning controls documented
  in the project's own README feature table)
- **Quote**: "Advanced inference controls: Tune sampling, thinking budgets, structured
  output, KV-cache quantization, prefix caching, and speculative decoding."
- **Our assessment**: This is a level of inference-engine-tuning exposed through a desktop
  GUI that is not documented for any other local-model app in this corpus — the JetBrains
  Air and Google litert-lm notes describe local serving as effectively a black box (point a
  harness at an endpoint), while Nativ's README claims user-facing controls over
  optimization techniques (speculative decoding, prefix caching, KV-cache quantization) that
  are normally engine-internal implementation details. Whether these controls are genuinely
  useful/discoverable in practice, or mostly power-user knobs most users will ignore, is not
  evaluable from this source — no corpus source has hands-on tested the GUI.

### Claim 10: Nativ bundles its own relocatable Python distribution and an embedded `mlx-vlm` server via a component called `NativServerKit`, which owns the server lifecycle; the SwiftUI application layer adds model discovery, chat, analytics, configuration, integrations, logs, menu-bar controls, and software updates around that runtime
- **Evidence**: README architecture description and accompanying diagram.
- **Confidence**: settled (specific architecture description from the project's own
  documentation, naming the component and its responsibilities)
- **Quote**: "Nativ is a native macOS workspace for running AI models locally on Apple
  silicon. It bundles an [`mlx-vlm`] server, finds compatible models in your Hugging Face
  cache (honoring `HF_HUB_CACHE` and `HF_HOME`), and wraps the whole experience in a polished
  SwiftUI app." / "`NativServerKit` owns the embedded Python distribution and server
  lifecycle. The app adds model discovery, chat, analytics, configuration, integrations,
  logs, menu bar controls, and software updates around that runtime."
- **Our assessment**: This architecture is the harness-owns-the-lifecycle pattern that
  `blog-ronacher-local-models-focus-polish.md` Claim 12 describes for `pi-ds4` (compiles,
  starts, and manages a local inference server automatically, with "no knobs"). Nativ
  applies the same pattern but as a general-purpose desktop app rather than a coding-agent
  extension: bundling a relocatable Python distribution inside a native Swift app removes
  the "install Python, install the right package versions" step entirely for end users. This
  is a second, independent instance of the "harness/app owns the local inference lifecycle"
  design pattern first documented via `pi-ds4`.

### Claim 11: Nativ's dashboard surfaces live performance telemetry — tokens/sec, memory pressure, thermal state, and time-to-first-token — plus system-level CPU, GPU, unified memory/swap, and disk monitoring
- **Evidence**: Landing page feature description and README feature table.
- **Confidence**: settled (specific, named metrics listed in the project's own
  documentation; not independently verified by a third party running the app)
- **Quote**: "Live tokens/sec, memory pressure, thermal state, and time-to-first-token. The
  details developers want." / "System monitor: Inspect live per-core CPU load, GPU
  utilization, unified memory and swap pressure, disk throughput, capacity, and SMART
  health."
- **Our assessment**: This is a direct answer to the operational-visibility gap
  `blog-ronacher-local-models-focus-polish.md` Claims 3–4 describe for local inference in
  coding-agent contexts (no way to distinguish a slow-but-working model from a dead
  connection). Surfacing time-to-first-token and thermal state directly in the app UI gives
  a user a way to see *why* a local model is slow (thermal throttling vs. memory pressure vs.
  genuinely long generation) that a bare API endpoint would not expose. This does not
  resolve Ronacher's specific tool-parameter-streaming gap (not mentioned anywhere in Nativ's
  documentation), but it addresses the adjacent "is this actually working?" visibility
  problem at the application level rather than the protocol level.

## Concrete Artifacts

### Nativ localhost API server — verbatim `curl` example and endpoint list (from GitHub README)

```
Default endpoint: http://127.0.0.1:8080 (configurable via the Developer page)

curl http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "your-model-id",
    "messages": [{"role": "user", "content": "Why is the sky blue?"}],
    "stream": false
  }'

With API key: -H 'Authorization: Bearer your-api-key'

Endpoints:
- OpenAI-compatible: /v1/chat/completions, /v1/responses, /v1/models, image and audio routes
- Anthropic-compatible: /v1/messages, token-counting routes
- System: /health, /metrics, cache statistics, cache reset, model unload

Source: github.com/Blaizzy/nativ README, "Use Nativ as a local API server" section
```

### Nativ launch partner-model library (verbatim table, from blaizzy.github.io/nativ/)

```
MODEL                  CREATOR     CONTEXT   SIZE      TYPE
Gemma 4 E2B Instruct    Google      128k      10.28 GB  VISION + AUDIO
North Mini Code         Cohere      500k      19.38 GB  CODE + TOOLS
LFM2.5-VL 1.6B          Liquid AI   128k      3.20 GB   VISION + LANGUAGE

Source: blaizzy.github.io/nativ/ landing page, "Partner Models" section
```

### Nativ "manifesto" — full verbatim open-source positioning statement (from blaizzy.github.io/nativ/)

```
$ cat philosophy.txt
The other "local AI" apps you've heard of? They're proprietary shells built on
top of open-source engines they don't own. They keep the UI closed, add a
paywall, and hope you don't look under the hood.

We built in the open. The desktop app is open too. Every line. Every model
loader. Every telemetry chart. You can read it, fork it, or send a pull
request tonight.

No VC roadmap. No enterprise tier. No dark pattern that turns your prompts
into training data. Just software made by researchers and hackers, for
researchers and hackers.

// Community owned. MIT licensed. Free forever.

Source: blaizzy.github.io/nativ/ landing page, "Manifesto" section
```

### Nativ architecture diagram (verbatim mermaid source, from GitHub README)

```
flowchart LR
    A["Nativ · SwiftUI app"] --> B["NativServerKit"]
    B --> C["Bundled mlx-vlm server"]
    C --> D["MLX runtime"]
    D --> E["Local models · Apple unified memory"]
    F["Apps and coding agents"] -->|"localhost API"| C

Source: github.com/Blaizzy/nativ README, "How it works" section
```

### Full feature table (verbatim, from GitHub README)

```
Local chat and vision    — Streaming conversations, image attachments, reasoning
                            output, response metrics, and persistent chat history.
Model library             — Discover installed MLX models, browse and download
                            compatible models from Hugging Face with fit warnings
                            for your memory, inspect capabilities, switch models,
                            or remove old ones.
Performance analytics     — Track request volume, token usage, time to first
                            token, decode speed, model performance, and recent
                            activity.
System monitor            — Inspect live per-core CPU load, GPU utilization,
                            unified memory and swap pressure, disk throughput,
                            capacity, and SMART health.
Local APIs                — OpenAI-compatible chat, Responses, image, audio, and
                            model endpoints, plus Anthropic Messages endpoints.
Coding-tool integrations  — Configure and launch Codex, Claude Code, Pi, Hermes,
                            and OpenCode against models served by Nativ.
Developer workspace       — Set the server host and port, add a Hugging Face
                            token for gated models, inspect runtime details, copy
                            endpoint URLs, search and filter live server logs,
                            and monitor server health.
Menu bar controls         — Start or stop the server, change the loaded model,
                            check serving statistics, open the main app without
                            breaking focus, or pin multiple live CPU, GPU, and
                            RAM percentages and mini graphs.
Advanced inference        — Tune sampling, thinking budgets, structured output,
controls                    KV-cache quantization, prefix caching, and
                            speculative decoding.

Source: github.com/Blaizzy/nativ README, "What Nativ can do" section
```

## Cross-References

- **Corroborates**:
  - `blog-google-gemma-4-12b-laptop-ai-edge.md` Claim 6/7 (`litert-lm serve` as a named
    local OpenAI-compatible server bridging to coding-agent tools, with specific default
    port and endpoint documentation): Nativ's Claim 4 is a second, independent instance of
    the same general pattern — a polished, vendor-or-developer-owned local server exposing a
    fixed default port and documented endpoints as a drop-in replacement for a cloud API base
    URL. Both sources corroborate that "point your existing coding-agent config at a local
    OpenAI-compatible endpoint" is becoming a common integration path across independently
    built tools (Google's official `litert-lm` CLI vs. Canuma's independent desktop app).
  - `blog-jetbrains-air-acp-local-models.md` Claim 5 (Ollama/LM Studio as local model
    runners connected to JetBrains Air via an ACP-compatible agent): confirms LM Studio and
    similar chat+server local apps are an established category Willison's comparison (Claim
    1) correctly situates Nativ within.

- **Extends**:
  - `blog-ronacher-local-models-focus-polish.md` Claim 1 (local model setup requires
    choosing an inference engine, model, quantization, template, context size, and JSON
    configs across layers) and Claim 8 ("runnable vs. finished" — the local model community
    optimizes for making models run, not for a finished UX): Nativ's curated three-model
    library (Claim 7), bundled Python runtime with zero manual setup (Claim 10), and GUI
    performance telemetry (Claim 11) are a concrete, independent-developer answer to exactly
    this diagnosed gap — collapsing engine/quantization/config selection into "pick one of
    three recommended models." This is the same structural fix Ronacher's Claim 9 prescribes
    ("pick a winner hard... polish the hell out of it"), but applied by an independent
    open-source developer building a general-purpose app rather than a narrow, single-model
    engine like `ds4.c`.
  - `blog-ronacher-local-models-focus-polish.md` Claim 12 (pi-ds4 as a harness that owns the
    entire local inference server lifecycle — compiling, starting, choosing quantization,
    managing leases — with "no knobs" by design): Nativ's `NativServerKit` (Claim 10) is a
    second, independent instance of the same "app owns the inference lifecycle" pattern,
    though Nativ takes the opposite stance on knobs — it explicitly exposes advanced
    inference controls (Claim 9: KV-cache quantization, prefix caching, speculative decoding)
    rather than hiding them. The two projects agree on hiding *setup* complexity but disagree
    on hiding *tuning* complexity from the user.
  - `blog-ronacher-local-models-focus-polish.md` Claim 6 (the local inference ecosystem is
    fragmented across llama.cpp, Ollama, LM Studio, MLX, Transformers, vLLM): Nativ is a
    concrete, newly-documented addition to the MLX branch of that fragmented landscape —
    confirming the ecosystem has not consolidated, but is still producing new entrants nine
    months after Ronacher's diagnosis.

- **Contrasts** (not a contradiction): `blog-google-gemma-4-12b-laptop-ai-edge.md` (Google
  AI Edge Gallery and Google AI Edge Eloquent — two closed-source, vendor-built macOS apps
  for local Gemma 4 inference, positioned via marketing claims like a "60%+ jump in overall
  quality" with no disclosed methodology). Nativ's manifesto (Claim 8) draws exactly the
  contrast this pairing illustrates without naming Google specifically: a "proprietary shell
  built on top of open-source engines" description that fits Gallery/Eloquent's closed-app
  wrapping of an open Gemma 4 model reasonably well. This is not a factual contradiction —
  both sets of apps genuinely exist and do what they claim — but a values/positioning
  divergence in how the same underlying problem (local model setup friction) gets solved:
  Google's approach is a closed, polished, vendor-owned app; Nativ's is an open, polished,
  community-owned app. No contradiction issue filed per MINER.md §4a — this is a business
  model / licensing difference, not an empirical disagreement that would change guide advice
  about local-model *capability*, though it is directly relevant to guide advice about
  local-tooling *selection criteria* (open-source auditability vs. vendor backing).

- **Novel**:
  - **Dual OpenAI- and Anthropic-compatible local API surface on a single server** (Claim
    4): no other corpus source documents a local inference server exposing both API
    protocols simultaneously; existing local-serving coverage is OpenAI-compatible only.
  - **Optional Bearer-token auth for a local desktop inference server's management
    endpoints** (Claim 5): not documented for any other local-serving tool in the corpus.
  - **A curated, cross-vendor (Google/Cohere/Liquid AI) three-model launch library with an
    automatic hardware-fit recommendation** (Claim 7): a distinct model-curation UX pattern
    not documented elsewhere; North Mini Code (Cohere) and LFM2.5-VL (Liquid AI) are new
    model names to the corpus.
  - **GUI-exposed advanced inference controls (KV-cache quantization, prefix caching,
    speculative decoding, thinking budgets) in a consumer desktop app** (Claim 9): a level of
    user-facing inference tuning not documented in any other local-model app covered by this
    corpus.
  - **An open-source local-AI app's manifesto explicitly critiquing "proprietary shells
    built on top of open-source engines they don't own"** (Claim 8): a new, pointed
    articulation of the open-vs-closed local-tooling divide, distinct from Ronacher's
    hyperscaler-independence framing (which targets cloud subscription lock-in, not
    closed-source local apps specifically) and directly relevant as a contrast point against
    the closed-source Google Gallery/Eloquent apps.

## Guide Impact

- **Chapter on Local vs. Hosted Inference / Model Selection**: Claims 4, 7, and 10 together
  give a third data point (alongside `pi-ds4`/`ds4.c` and Google's `litert-lm`/Gallery/
  Eloquent) for how the local-inference ecosystem is closing Ronacher's diagnosed
  setup-complexity gap: a curated model library plus a bundled, self-managing runtime. The
  guide's local-inference section should note that "download an app, pick a recommended
  model" is now a viable on-ramp for MLX-based local inference on macOS specifically — not
  just the narrow, single-model engines (`ds4.c`) or first-party vendor tooling
  (`litert-lm`) previously documented, but also independent community/open-source apps.
- **Chapter on Harness Engineering (Local Model Integration)**: Claim 4's dual OpenAI-/
  Anthropic-compatible server is a specific, checkable detail worth adding wherever the
  guide discusses pointing existing coding-agent harnesses at local models: an
  Anthropic-compatible local endpoint means tools built specifically against the Anthropic
  Messages API (not just generic OpenAI-compatible clients) can also be redirected to a
  local model without a translation proxy.
- **Chapter on Community and Open-Source Model/Tooling Strategy**: Claim 8's manifesto is a
  citable example of the open-vs-vendor-controlled tension already present in
  `blog-ronacher-local-models-focus-polish.md` Claim 14, now expressed specifically about
  *application* openness (not just model-weight or inference-engine openness) — worth
  including if the guide discusses selection criteria for local-AI tooling beyond raw
  capability (auditability, forkability, absence of a "dark pattern that turns your prompts
  into training data").

## Extraction Notes

- **The blog post alone was insufficient for a substantive note**: Willison's post is ~120
  words across three short paragraphs. Per MINER.md §1 ("If it links to related pages...
  follow up to 5 linked pages that seem substantive"), two linked pages were followed: the
  Nativ project landing page (blaizzy.github.io/nativ/) and its GitHub repository/README
  (github.com/Blaizzy/nativ). Both were fetched via direct `curl` (not the WebFetch
  summarizer) and HTML-tag-stripped, or read as raw Markdown, to obtain character-for-character
  text for `Quote` fields. The Hacker News discussion thread linked as "via" was not followed
  — it is community discussion of the tool, not primary documentation, and MINER.md's
  sub-page guidance targets substantive linked *content* pages.
- **Willison's own post's three sentences are individually quoted in Claims 1–3**; all
  remaining claims (4–11) are sourced from the project's own landing page and README, not
  from Willison's prose, and are clearly marked as such in each Evidence/Quote field.
- **No independent hands-on verification possible**: this note documents what Nativ's own
  documentation claims about itself (architecture, feature list, API surface). No corpus
  source — including this one — has actually run Nativ and verified these claims
  empirically (e.g., whether the "advanced inference controls" are functional and effective,
  whether the dual-protocol server correctly implements both API specs end-to-end). This is
  flagged explicitly in each relevant claim's confidence/assessment rather than treating
  vendor documentation as equivalent to independent verification.
- **Confidence rationale**: Rated `emerging` overall. Most individual claims are graded
  `settled` because they describe specific, checkable facts from the project's own official
  documentation (default port, endpoint paths, named integrations, feature list) rather than
  vague marketing language — comparable in kind to how `blog-google-gemma-4-12b-laptop-ai-edge.md`
  treats Google's own CLI documentation. However, the overall grade is `emerging` rather than
  `settled` because: (a) this is a brand-new tool (first corpus mention) with no independent
  usage or benchmark data yet, unlike an established product; and (b) Claim 8's manifesto and
  the general "polished, finished" framing are the project's own self-description, not a
  third party's assessment — Willison's post itself does not evaluate quality, depth, or
  reliability, only shape and one cache-detection anecdote.
- **No contradictions filed**: The contrast with `blog-google-gemma-4-12b-laptop-ai-edge.md`
  (open vs. closed local-AI app philosophy) is a business-model/positioning difference, not
  an empirical disagreement about a shared factual claim — per MINER.md §4a guidance, this
  does not meet the bar for a contradiction issue. Checked against
  `blog-ronacher-local-models-focus-polish.md`, `blog-jetbrains-air-acp-local-models.md`,
  `blog-google-gemma-4-12b-laptop-ai-edge.md`, `blog-simonwillison-mlx-audio.md`, and
  `blog-latentspace-osman-local-ai-catching-up.md` before writing; no material contradiction
  found in any of them.
