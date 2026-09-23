---
source_url: https://newsletter.pragmaticengineer.com/p/windows-and-ai
source_type: blog-post
title: "How will AI change operating systems? Part 2: Windows"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-09-22
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: emerging
issue: "#3633"
---

# How will AI change operating systems? Part 2: Windows

> Orosz's reporting on Microsoft's plan to make Windows "agent-friendly" —
> based on interviews with the Windows team — documenting new OS-level
> agent-identity primitives (Entra ID agent accounts, Defender agent
> scanning), an MCP tool discovery/proxy layer (On Device Agent Registry),
> a graduated-isolation sandboxing system for agent tools (Microsoft
> Execution Containers), and Windows ML, a new ONNX-based hardware-agnostic
> layer for running local models across GPU/NPU/CPU.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter, Substack; published
  2026-09-22). Second part of a two-part series on OS-level AI change (Part 1
  reportedly covered Ubuntu/Linux; not fetched, out of scope for this note).
- **Author credibility**: Gergely Orosz, an established, frequently-corroborated
  source already well represented in this corpus (e.g.
  `blog-pragmaticengineer-orosz-inside-anthropic.md`,
  `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`,
  `survey-pragmaticengineer-ai-tooling-2026.md`). This piece is based on direct
  interviews the author conducted with three named Microsoft staff: Pavan
  Davuluri (EVP, Windows and Devices), Scott Hanselman (VP, Microsoft CoreAI
  and GitHub), and Logan Iyer (CVP, Windows Platform and Developer). This
  makes the OS-feature claims first-party-sourced-through-a-journalist rather
  than independently verified reporting — the underlying technology
  descriptions originate with Microsoft, filtered through Orosz's
  interviewing and framing, not through Orosz's own testing.
- **Scope**: This note covers only the free (non-paywalled) portion of the
  article — roughly the first five of eight announced sections: (1) developer
  OS market-share data, (2) agent identity & discovery (Entra ID, Windows
  On Device Agent Registry), (3) agent tool isolation (Microsoft Execution
  Containers), (4) local model support (Windows ML), and the opening sentence
  of (5) agent-building frameworks. Sections 5 (remainder)–8 ("More
  dev-friendly," "Linux on Windows (WSL)," "Windows & hardware") sit behind
  the Pragmatic Engineer paywall and were **not** accessible — see Extraction
  Notes. Does NOT cover: WSL specifics, Windows-on-ARM/NVIDIA hardware
  partnership details, or the agent-building-framework content — these are
  announced in the article's own outline but are paywalled.

## Extracted Claims

### Claim 1: Windows developer market share appears to be declining, with one informal 2026 survey putting it in third place behind Linux and macOS
- **Evidence**: Three data points cited in the article: the 2025 Stack Overflow professional-user survey (49,000 respondents), a 2025 JetBrains "State of Developer Ecosystem" survey (24,500 respondents), and the authors' own September 2026 social-media survey (~10,000 combined responses on X and LinkedIn).
- **Confidence**: anecdotal (the article's own survey is informal, single-choice, and self-selected from the newsletter's readership; the author explicitly flags this limitation)
- **Quote**: "We were surprised to find Windows in third place behind Linux, based on nearly 10,000 combined responses"
- **Our assessment**: The author's own caveat is important and should travel with this claim: "It's very likely that our own social media survey over-indexes on this group!" (VC-funded startups and Big Tech, where Macs are already the norm). This is directional evidence of a trend (Windows losing developer mindshare), not a settled market-share figure. The more rigorous data points (Stack Overflow, JetBrains) show Windows still nominally the most-used single OS but down substantially from its "XP-era peak," with macOS and Linux both gaining.

### Claim 2: Windows gives agentic programs a distinguishable OS-level identity through Entra ID, so agents appear as separate "users" in Task Manager rather than masquerading as the human they act on behalf of
- **Evidence**: Direct product description plus a screenshot example (Task Manager grouping processes under two users: "kirupach," a human, and "V9-G4," an agent).
- **Confidence**: emerging (described as a current Windows capability by named Microsoft executives, but not independently tested by the author; Windows' AI features are described elsewhere in the piece as still "in development" and "available to beta testers")
- **Quote**: "Agent identification is enabled through Entra ID, Microsoft's tool for centralized identity management in Windows. When an agent has a local identity, it acts as if it is another user on the system as visible in the Task Manager."
- **Our assessment**: This is the OS-level analogue of the "agent gets its own identity, not the user's" pattern this corpus already documents at the application layer (Claude Tag's per-channel service accounts — see Cross-References). It is a genuinely different layer of the stack: Entra ID assigns an agent a first-class OS identity visible to any process-level observability tool (Task Manager, presumably Event Viewer/EDR), not just within one vendor's product. If shipped broadly, this could become the substrate that lets *any* Windows-native agent (not just Microsoft's own) be identified and audited consistently — a capability the Claude Tag model can only provide within Anthropic's own product boundary.

### Claim 3: Microsoft Defender is becoming "agent aware," scanning Windows machines for known local agent activity the same way antivirus software scans for viruses
- **Evidence**: Direct statement plus a screenshot of "Microsoft Defender's AI Assets feature."
- **Confidence**: emerging (vendor-described feature, screenshot shown but feature maturity/detection scope not independently verified)
- **Quote**: "That's why Defender, Microsoft's antivirus software, is becoming \"agent aware\" and scanning Windows for known local agent activity like it scans for viruses."
- **Our assessment**: The stated rationale is explicitly security-motivated: the article frames unregistered/impersonating agents as structurally similar to malware ("a rogue agentic application can impersonate a user and not self-register as an agent – which in a sense is how viruses operate by using legitimate OS functionality for illegitimate purposes"). This reframes "does this process have an agent identity" as a detection signal, which is a novel angle not covered elsewhere in this corpus — existing sandboxing/containment sources address *containing* known agents, not *detecting unregistered* ones.

### Claim 4: Windows On Device Agent Registry (ODR) is a centralized, OS-level registry where agents discover and use locally available MCP tools, including built-in connectors for File Explorer and System Settings
- **Evidence**: Direct product description with a worked example (a hypothetical "Photo Organizer Agent" discovering and using a File Explorer MCP connector).
- **Confidence**: emerging (ODR is explicitly stated to be pre-release: "ODR is still in development and available to beta testers, so little is known about its internals")
- **Quote**: "Windows On Device Agent Registry (ODR) is the centralized place where agents register and discover available MCP tools. ODR manages and runs MCP servers locally, and also comes with connectors for core operating system components like the File Explorer or System Settings."
- **Our assessment**: This is an OS vendor building first-party MCP server hosting and discovery directly into the operating system — a different integration point than the many product- or platform-level MCP gateway/registry patterns already in this corpus (e.g. `docs-ghaw-mcp-gateway-reference.md`, `blog-google-mcp-stateless-scaling.md`). If Windows ships built-in MCP connectors for OS primitives (filesystem, settings), it removes the need for third-party developers to build and maintain their own File Explorer/Settings MCP servers — worth flagging as a potential shift in "who owns the MCP server for OS-level capabilities."

### Claim 5: Independent research (Origin Technology) reverse-engineered ODR and found it inserts itself as a proxy between the MCP client and server, rather than acting as a pure registry/discovery service — a claim Microsoft has not confirmed
- **Evidence**: Third-party reverse-engineering research, explicitly flagged by the author as unconfirmed by Microsoft.
- **Confidence**: anecdotal (single third-party research claim, not corroborated by the vendor)
- **Quote**: "By reverse engineering ODR behavior, researchers proved ODR puts itself as a proxy between the MCP client and its server."
- **Quote** (unconfirmed-status caveat, several sentences later in the same section): "However, this proxying behaviour is as yet unconfirmed by Microsoft, so it remains to be seen how they use it."
- **Our assessment**: This is the most security-relevant claim in the readable portion of the article, and the author is careful to flag its unconfirmed status — we should preserve that same caution. If true, ODR sitting in the MCP client-server path as a proxy would give Windows visibility into (and potential control over) all local MCP payloads, which is architecturally significant for the same reason session-scoped credential injection is significant in `blog-anthropic-agent-identity-access-model.md` Claim 8 — a chokepoint that can enforce security policy, but also a new trust dependency. Treat as a plausible-but-unverified architectural detail, not a confirmed Microsoft design decision.

### Claim 6: Microsoft Execution Containers (MXC) is a new, in-development, cross-platform (Windows/Linux/macOS) sandboxing technology for agent tools, configured via JSON containment policies covering network, filesystem, UI, and execution restrictions
- **Evidence**: Direct product description, a worked code example (`spawnSandboxFromConfig()`), and a named example application (OpenClaw for Windows) already using it, plus a screenshot of its Windows settings UI.
- **Confidence**: emerging ("MXC enforcement isn't broadly adopted yet"; described as in-development but already runs cross-platform)
- **Quote**: "Microsoft Execution Containers (MXC) is a new, in-development agent containment technology by Windows. Developers can use MXC to spawn agentic tools in isolated environments called sandboxes, and agent access within the sandbox environment is configured through MXC containment policies."
- **Quote** (cross-platform): "MXC is under development, but already runs on Windows, Linux, and macOS. Developers therefore get a unified way of containing external tools across operating systems."
- **Our assessment**: MXC's design vocabulary maps closely onto the containment framework already documented in `blog-anthropic-how-contain-claude.md` — see Cross-References for the specific correspondence. The notable new fact is that Microsoft is building a cross-OS abstraction (explicitly using macOS's Seatbelt as one of its underlying containment technologies, per the article: "on a Mac, it would use seatbelt, a process containment layer built into the Mac OS") rather than each product/vendor building its own per-OS containment layer, as Anthropic currently does per-product.

### Claim 7: MXC offers five graduated containment levels — process containment, session containment, WSL containers, lightweight Hyper-V containers, and full virtual machines — letting developers trade isolation strength against startup speed and blast radius
- **Evidence**: Explicit enumerated list in the article plus a "Speed versus safety tradeoff" framing paragraph.
- **Confidence**: emerging (described feature of an in-development, not-yet-broadly-adopted technology)
- **Quote**: "Choosing the right level of containment is a trade-off between the blast radius and speed of execution."
- **Our assessment**: This is a striking structural echo of `blog-anthropic-how-contain-claude.md` Claim 15 ("matching isolation strength to user expertise/blast radius is a core design principle") and its three-tier comparison table (gVisor container / OS-level sandbox / full VM). MXC generalizes that idea into five selectable levels exposed as a single OS-level API, rather than three fixed architectures each hard-wired into a specific product. This corroborates, at the OS-vendor level, that graduated (not binary) containment is becoming the industry-standard mental model for agent tool isolation — see Cross-References.

### Claim 8: MXC integrates with Microsoft Intune for enterprise fleet-wide management of agent containment policies, combined with agent identity for centralized control
- **Evidence**: Direct statement of the enterprise management integration.
- **Confidence**: emerging (stated product direction, not yet broadly deployed per Claim 6's "not broadly adopted" caveat)
- **Quote**: "Combined with agent identities, MXC will give enterprises fleet-wide control of their agents. For admins, Microsoft will offer MXC policy management through its Intune product for corporate device fleet management."
- **Our assessment**: This pairs OS-level agent identity (Claim 2) with OS-level containment (Claims 6-7) into a single enterprise governance surface (Intune), which is notable because it's a different administrative layer than the workspace/channel-level governance described for Claude Tag in `blog-anthropic-agent-identity-access-model.md` (Claims 6-7: workspace/channel identity hierarchy). Windows is proposing device-fleet-level governance of *all* agents on a machine, regardless of vendor, via existing enterprise device management tooling IT departments already use.

### Claim 9: Windows ML is a new, hardware-agnostic abstraction layer for running AI models locally, built on the open ONNX runtime, positioned as Microsoft's second attempt after DirectML (2019) and intended to do for AI what DirectX did for graphics
- **Evidence**: Direct product description with an explicit before/after comparison to DirectML.
- **Confidence**: emerging (vendor description of an in-development/newly-available framework; no independent benchmark of Windows ML cited)
- **Quote**: "Windows ML is a hardware-agnostic layer for running AI models locally on Windows. Its goal is to do for AI what DirectX did for computer graphics: abstract away hardware complexity, regardless of the underlying model's architecture."
- **Our assessment**: The two stated improvements over DirectML are concrete and checkable: (1) ONNX-based higher-level abstraction covering GPU+NPU+CPU instead of DirectML's GPU-only, DirectX-12-based low-level API; (2) hardware vendors ship "Execution Providers" (EPs) that Windows ML downloads on demand per the user's actual hardware, avoiding the "six months to get meaningful adoption" driver-update bottleneck DirectML had. This is the most concrete, novel-to-corpus technical claim in the article — no existing source note covers ONNX Runtime, DirectML, or Windows' local-inference hardware abstraction strategy.

### Claim 10: Small Language Models are being embedded directly in Windows/Edge so app developers can call local inference (e.g. sentiment analysis) as a local library, without shipping their own model or calling a cloud API
- **Evidence**: Named example: Aion-1.0-Instruct, built into Microsoft Edge, exposed to web developers via a "Prompt API," with a JavaScript code sample shown (screenshot, not machine-readable text in the fetched portion).
- **Confidence**: emerging (a specific shipped/shipping integration named by the vendor, but the code sample itself was in image form and not independently reproduced here — see Concrete Artifacts)
- **Quote**: "For example, the Aion-1.0-Instruct model is built into Edge, Microsoft's web browser. Accessed through the Prompt API, Aion model allows developers to build apps like sentiment analysis with a few lines of code."
- **Our assessment**: This directly corroborates the general industry direction documented in `blog-fowler-boeckeler-local-models-viability.md` (small/local models becoming practically usable for bounded tasks) but from the opposite end of the stack: instead of a practitioner manually running a downloaded open-weight model in a harness (Böckeler's approach), Microsoft is proposing that the OS/browser itself ships a small model as a system service any app can call like a local library. This removes the RAM/runtime-selection burden Böckeler documents as the core practitioner pain point (Claim 1 and Claim 8 of that note) — at the cost of being locked to whatever model Microsoft embeds.

### Claim 11: A pre-release Surface laptop with an NVIDIA GPU ran the Qwen model locally at roughly 40 tokens/second, hooked up to GitHub Copilot, demonstrated directly to the author by Scott Hanselman
- **Evidence**: First-hand demo witnessed by the author, with a specific named model, hardware, integration point, and throughput figure.
- **Confidence**: anecdotal (single demo, pre-release hardware, one data point, not a systematic benchmark)
- **Quote**: "At Microsoft, Scott Hanselman showed us a pre-release Surface laptop with NVIDIA GPUs running Qwen as a local model, hooked up to GitHub Copilot. This local model churned out tokens at a rate of ~40 tokens per second!"
- **Our assessment**: ~40 tok/s on Qwen is a concrete, citable local-inference throughput data point for a coding-assistant use case, and is broadly consistent with the practitioner-reported feasibility of local coding models in `blog-fowler-boeckeler-local-models-viability.md` (which used Qwen3.6 35B-A3B MoE as its best-performing model, on Apple Silicon rather than NVIDIA). Treat as a vendor demo, not a reproducible benchmark — no context window, quantization level, or task type is given, unlike Böckeler's more rigorous methodology.

## Concrete Artifacts

### MXC containment levels (enumerated in source)
```
Multiple containment levels available in Windows (Microsoft Execution
Containers):
  - Process containment
  - Session containment
  - Running WSL containers
  - Lightweight Hyper-V containers
  - Full virtual machines

Source: "How will AI change operating systems? Part 2: Windows",
Gergely Orosz, The Pragmatic Engineer, 2026-09-22
```

### MXC workflow steps (as described for the OpenClaw for Windows example)
```
1. The policy object specifies how the containerized workload should be
   constrained. It specifies network, UI, filesystem restrictions
2. The createConfigFromPolicy step configures the whole container. It
   takes the containment policy object, the chosen isolation level
   ("process"), and names the container.
3. The app then manipulates what gets executed in the "WHAT RUNS" step
4. Finally, spawnSandboxFromConfig() runs the container and processes
   its output.

Source: "How will AI change operating systems? Part 2: Windows",
Gergely Orosz, The Pragmatic Engineer, 2026-09-22 (describing Microsoft's
worked example for OpenClaw for Windows)
```

### Windows ML vs. DirectML comparison (as stated in source)
```
DirectML (2019, first attempt):
  - Low-level: developers build inference pipelines from simple
    mathematical operations, manage memory layout manually
  - GPU-only (built on DirectX 12)
  - New runtime optimizations required driver updates ("took six months
    to get meaningful adoption")

Windows ML (second attempt):
  - Built on ONNX (Open Neural Network Exchange) format / ONNX runtime
  - Covers GPU, NPU, and CPU from all major vendors
  - Hardware-specific optimization delivered via downloadable "Execution
    Providers" (EPs) per-vendor, certified by Microsoft, loaded on demand
    based on the user's actual hardware (e.g. NVIDIA GeForce RTX ->
    NVIDIA Tensor RTX execution provider)
  - Most execution providers available today are also available on GitHub

Source: "How will AI change operating systems? Part 2: Windows",
Gergely Orosz, The Pragmatic Engineer, 2026-09-22
```

### Article's own outline (for scope tracking — sections 6-8 are paywalled and NOT extracted in this note)
```
1. How many devs use Windows anyway? [extracted: Claim 1]
2. Agent identity & discovery [extracted: Claims 2-5]
3. Isolate agentic tools [extracted: Claims 6-8]
4. Running models locally [extracted: Claims 9-11]
5. Building agents on Windows [only opening sentence readable; PAYWALLED]
6. More dev-friendly [PAYWALLED — not extracted]
7. Linux on Windows (WSL) [PAYWALLED — not extracted]
8. Windows & hardware (ARM, NVIDIA collaboration) [PAYWALLED — not extracted]

Source: "How will AI change operating systems? Part 2: Windows",
Gergely Orosz, The Pragmatic Engineer, 2026-09-22 (article's own numbered
outline)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-how-contain-claude.md` Claim 15 ("Matching isolation
    strength to user expertise is a core design principle...the same
    containment pattern should not be applied across user populations with
    different technical capabilities") and its three-product containment
    comparison table (gVisor container / OS-level sandbox / full VM). MXC's
    five graduated containment levels (Claim 7 here: process → session → WSL
    container → lightweight Hyper-V container → full VM) generalize the same
    "match isolation strength to blast radius/speed tradeoff" principle into
    a single OS-exposed API, rather than three separate product
    architectures. This is independent convergence between Anthropic
    (product-specific) and Microsoft (OS-level, cross-vendor) on graduated
    containment as the right mental model.
  - `blog-anthropic-how-contain-claude.md` Claim 7, which names "Seatbelt on
    macOS, bubblewrap on Linux" as Claude Code's OS-level sandbox
    primitives. This article independently names Seatbelt as one of the
    containment technologies MXC uses on Mac ("on a Mac, it would use
    seatbelt, a process containment layer built into the Mac OS") — two
    independent sources naming the identical underlying macOS primitive as
    the foundation for agent tool containment.
  - `blog-fowler-boeckeler-local-models-viability.md` (Claim 1, Claim 10):
    both sources document local/small models becoming practically viable for
    bounded coding and text tasks in 2026, though via different mechanisms —
    Böckeler manually running downloaded open-weight models in a harness on
    Apple Silicon vs. this article's OS/browser-embedded SLM (Aion-1.0-Instruct
    in Edge) and a GPU-accelerated Qwen demo on a Surface laptop at ~40 tok/s.

- **Extends**:
  - `blog-anthropic-agent-identity-access-model.md`: that note documents
    agent identity at the application/product layer (Claude Tag: per-channel
    service accounts, workspace/channel identity hierarchy, Claim 4's
    reframe from "what can this user do?" to "what can this agent do in this
    compartment?"). This article extends the same underlying idea (agents
    need their own, non-human-impersonating identity) down to the OS layer:
    Entra ID agent accounts visible in Task Manager (Claim 2 here) and
    Defender agent-activity scanning (Claim 3 here) would apply to *any*
    Windows-native agent, not just one vendor's product. Together the two
    sources sketch a layered identity picture: OS-level agent identity
    (Windows/Entra ID) as the substrate, with product-level identity models
    (Claude Tag) as a narrower, product-specific instance running on top.

- **Contradicts**: None identified. No existing source note makes claims
  about Windows-specific agent infrastructure, ONNX/DirectML, or OS-vendor
  MCP registries that this article's claims conflict with.

- **Novel**:
  - **OS-vendor-built MCP discovery/proxy layer (ODR)**: no existing source
    note documents an operating system vendor shipping a built-in MCP server
    registry with connectors for OS primitives (File Explorer, System
    Settings), or the unconfirmed-but-researched claim that it proxies MCP
    traffic (Claims 4-5).
  - **Cross-platform, OS-level agent containment API (MXC)**: existing
    corpus containment sources are all product-specific (Anthropic's three
    products, various sandbox vendors). MXC is novel as an OS-vendor-neutral,
    cross-platform (Windows/Linux/macOS) containment API intended for any
    developer's agent, with Intune-based fleet management (Claim 8).
  - **ONNX Runtime / Windows ML / Execution Providers as a named local-
    inference hardware abstraction strategy**: no existing source note
    covers DirectML, ONNX, or the "Execution Providers downloaded per
    hardware vendor" model (Claim 9).
  - **Windows developer market-share erosion data** (Claim 1): no existing
    source note cites Stack Overflow/JetBrains OS-usage survey data or
    documents Windows possibly falling to third place among developers.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Windows ML / ONNX Runtime
  (Claim 9) as a named option practitioners should be aware of when
  evaluating local-model runtimes on Windows hardware, alongside the
  Apple-Silicon-focused guidance already sourced from
  `blog-fowler-boeckeler-local-models-viability.md`. Currently the guide's
  local-model coverage is Mac-centric; this source is the first Windows-side
  data point. Caveat clearly that Windows ML is newly-positioned/emerging,
  not a mature, independently-benchmarked runtime.

- **Chapter 02 (Harness Engineering) / Chapter 06 (Security & Threat
  Model)**: Add MXC's five-level graduated containment model (Claim 7) as a
  second data point — alongside Anthropic's three-tier product comparison in
  `blog-anthropic-how-contain-claude.md` — for the guide's "match isolation
  level to blast radius and user expertise" containment-design guidance.
  Note explicitly that MXC is Microsoft's in-development, not-yet-broadly-
  adopted OS-level generalization of the same principle, so cite it as
  emerging/directional, not as an established practice to build against yet.

- **Chapter 06 (Security & Threat Model)**: Add OS-level agent identity
  (Entra ID agent accounts, Claim 2; Defender agent-activity scanning,
  Claim 3) as a new detection/observability primitive distinct from the
  product-level agent identity model already documented from
  `blog-anthropic-agent-identity-access-model.md`. Flag the unconfirmed ODR
  proxy claim (Claim 5) explicitly as unverified when citing it — do not
  present it as confirmed Microsoft architecture.

- **Chapter 05 (Team Adoption)**: The Windows developer market-share data
  (Claim 1) is weak/anecdotal evidence and should not be cited as a settled
  fact if used at all — at most, flag as "one newsletter's informal 2026
  survey suggests Windows may be losing developer mindshare to macOS/Linux,"
  with the author's own over-indexing caveat attached.

## Extraction Notes

- **Paywall**: This article is a Pragmatic Engineer "full article" post,
  free through the end of section 4 and the opening sentence of section 5
  ("Besides Windows being agent-friendly, Microsoft is also investing in the
  agent building toolchain to simplify agentic app development by providing
  a rich agent building framework."), after which the page renders a
  paid-subscriber paywall block. Sections 5 (remainder), 6 ("More
  dev-friendly"), 7 ("Linux on Windows (WSL)"), and 8 ("Windows & hardware")
  were **not accessible** and are not covered by this note. The article's
  own numbered outline (reproduced in Concrete Artifacts) names what those
  sections cover, but none of their content was read. If this source is
  revisited by a Pragmatic Engineer subscriber, sections 5-8 (agent
  frameworks, UI/Start-menu decluttering, WSL adoption strategy, Windows-on-
  ARM/NVIDIA hardware partnership) would be worth a follow-up extraction —
  WSL and dev-friendliness in particular map directly to Ch01/Ch02 relevance
  flagged by the Prospector's triage.
- **Fetch method**: WebFetch's AI-summarization returned only a lossy
  summary of the visible content and did not preserve verbatim wording, so
  it was not used for quotes. Instead, the raw article HTML was fetched
  directly via `curl`, the `available-content` div was isolated from the
  HTML (bounded by the point where the DOM's `data-testid="paywall"` block
  begins), and converted to plain text with `html2text`. All quotes in this
  note are copied verbatim from that extracted plain text, which itself is
  a direct rendering of the publisher's own HTML markup (not a model
  paraphrase).
- **Companion Ubuntu article**: The article references "a previous article
  on how the leading Linux distribution, Ubuntu, is changing, thanks to AI,"
  covering GPU/NPU/DPU hardware support and local-first LLMs. This companion
  piece's URL was not given in the visible text (only referenced by title)
  and was not fetched — out of scope for issue #3633, which names only the
  Windows URL. Flagging it as a candidate for a future source-submission
  issue if the Prospector wants OS-level Linux/Ubuntu-AI coverage to match
  this Windows note.
- **Image-only content**: Several data points in the source (the three
  survey charts in section 1, the Task Manager screenshot, the Defender AI
  Assets screenshot, several MXC architecture diagrams, and the Aion/Prompt
  API JavaScript code sample) are presented as embedded images in the
  article, not as machine-readable text. These were not OCR'd or
  transcribed; claims based on them rely on the article's surrounding prose
  description rather than the image content itself. The JavaScript code
  sample for the Prompt API (mentioned in Claim 10) could not be verbatim-
  extracted for this reason and is not reproduced in Concrete Artifacts.
- **No contradiction issues filed**: cross-referencing against the corpus
  found no conflicting claims — see Cross-References.
