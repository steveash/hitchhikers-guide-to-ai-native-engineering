---
source_url: https://developers.googleblog.com/a2ui-and-mcp-apps/
source_type: blog-post
title: "A2UI + MCP Apps: Combining the best of declarative and custom agentic UIs"
author: Google A2UI Team, Ido Salomon (MCP Apps Co-creator), Liad Yosef (MCP Apps Co-creator)
date_published: 2026-06-17
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: emerging
issue: "#1610"
---

# A2UI + MCP Apps: Combining the best of declarative and custom agentic UIs

> Google's A2UI team and the MCP Apps co-creators lay out three concrete
> architectural patterns for combining declarative UI (A2UI's JSON payload
> rendered by native host components) with custom iframe UI (MCP Apps),
> each with a worked demo, a MIME-type-level implementation mechanism, and
> an explicit trade-off framing between design consistency/security and
> creative/client-side-logic freedom.

## Source Context

- **Type**: blog-post (official Google Developers Blog, published June 17,
  2026). Co-authored by the "Google A2UI Team" plus Ido Salomon and Liad
  Yosef, both individually credited as "MCP Apps Co-creator."
- **Author credibility**: First-party from the teams that built both halves
  of the integration being described — the A2UI protocol team at Google and
  the co-creators of the MCP Apps extension to Model Context Protocol. This
  is the canonical source for how these two specific technologies are
  intended to interoperate, not a third-party integration guide. Each of
  the three patterns links to a runnable demo application and a sample-code
  repository (`github.com/a2ui-project/a2ui` and `github.com/google/A2UI`),
  which is stronger evidence than prose description alone.
- **Scope**: Covers three architectural patterns for combining A2UI (a
  declarative, JSON-based UI protocol at `a2ui.org`) with MCP Apps (an
  iframe-based custom-UI extension to MCP at
  `modelcontextprotocol.io/extensions/apps/overview`): (1) serving A2UI
  payloads directly over MCP, (2) embedding an MCP App inside an A2UI
  component, (3) embedding an A2UI renderer inside an MCP App. Does NOT
  cover: A2UI's full component catalog or schema spec, MCP Apps' security
  model in general (only the state-sync mechanics relevant to hybrid use),
  performance/latency of any pattern, or non-Google client implementations
  (React/Flutter/Angular rendering is asserted but not demonstrated in this
  post).

## Extracted Claims

### Claim 1: MCP Apps and A2UI represent a fundamental trade-off between iframe-based creative freedom and declarative-JSON-based design/security consistency

- **Evidence**: The post's framing section contrasts the two technologies
  directly, citing specific failure modes of each (fragmented UX and
  performance/security hurdles for MCP Apps; restriction to a fixed
  component library for A2UI).
- **Confidence**: settled (first-party framing from the creators of both
  technologies; each technology's own limitation is stated by its own team,
  not attributed to the other side)
- **Quote**: "**Model Context Protocol (MCP) Apps** offer creative freedom within an iframe using standard web technologies. However, this reliance on iframes for these applications can lead to a fragmented user experience, characterized by aesthetic inconsistencies like clashing design systems or redundant scrollbars, while simultaneously presenting notable hurdles in both *computational performance* and *security encapsulation*."
- **Quote (A2UI side)**: "**Agent-to-User Interface (A2UI)** utilizes a declarative framework. Instead of sending raw HTML, CSS, and JavaScript, [A2UI] employs a JSON payload to define what to render, allowing the host application to handle the presentation through its native components. ... While this ensures consistent design and enhanced security, developers are restricted to a specific component library."
- **Our assessment**: This is a clean, self-critical framing from both
  technologies' own maintainers — useful because it is not a vendor
  comparing itself favorably to a competitor, but two Google-affiliated
  teams naming their own respective weaknesses before proposing to combine
  them. It corroborates and sharpens `blog-anthropic-mcp-production-agents.md`
  Claim 8, which introduces "MCP Apps" as a protocol extension letting "a
  tool return an interactive interface, such as a chart, form, or
  dashboard" but does not discuss iframe drawbacks or contrast it with a
  declarative alternative. This post is the first source in the corpus to
  name the specific iframe failure modes (design-system clashes, redundant
  scrollbars, performance/security overhead) that motivate a declarative
  alternative.

### Claim 2: Pattern 1 (A2UI over MCP servers) lets an MCP server return natively-rendered UI by using the MIME type `application/a2ui+json` on a standard MCP content payload, bypassing MCP Apps' iframe entirely

- **Evidence**: A worked JSON example shows an MCP tool-call response with
  `"type": "resource"` and `"mimeType": "application/a2ui+json"` containing
  an A2UI JSON payload (`createSurface`), linked to a sample "Recipe
  Studio" demo app on GitHub.
- **Confidence**: settled (concrete protocol-level mechanism with a code
  example, not a conceptual description)
- **Quote**: "Instead of an MCP server returning a standard text response or a bundled HTML/JS web app, for an MCP server to return A2UI payloads, it returns a structured JSON payload with a specific MIME type: `application/a2ui+json`."
- **Our assessment**: This is the most concrete, implementable claim in the
  post — a single MIME-type convention is the entire mechanism that lets an
  existing MCP tool or resource response be recognized and natively
  rendered by an A2UI-capable host, with no iframe involved. For
  practitioners already running MCP servers, this is a low-effort upgrade
  path to richer UI: change a response's MIME type and payload shape rather
  than build a new embedding surface. This directly extends the "MCP Apps"
  protocol extension documented in `blog-anthropic-mcp-production-agents.md`
  Claim 8 by giving MCP servers a *non-iframe* alternative for the same
  "return an interactive interface" goal.

### Claim 3: A2UI-over-MCP payloads can be delivered two ways — static via MCP Resources (`resources/read`) for prescriptive, cacheable UI, or dynamic via MCP Tool Calls (`tools/call`) for live, agent-assembled UI — with different ideal use cases for each

- **Evidence**: A named two-part breakdown ("1. Static Delivery via MCP
  Resources," "2. Dynamic Delivery via MCP Tool Calls") each with its own
  "Ideal use cases" and "Key Benefit" bullet.
- **Confidence**: settled (first-party design guidance with explicit
  use-case guidance for each option)
- **Quote (static)**: "This approach ensures high predictability and efficient caching with zero computational overhead, as it removes the need for real-time UI synthesis by the LLM."
- **Quote (dynamic)**: "Provides architectural versatility, empowering agents to build sophisticated, native-feeling experiences that respond to user objectives."
- **Our assessment**: This static/dynamic split mirrors a pattern already
  in the corpus for MCP resources generally — `docs-ghaw-mcps.md`-style
  static-config-vs-live-tool-call distinctions — but applied specifically
  to UI payload delivery. The static path's "zero computational overhead"
  claim is notable: because the UI is a fixed, cacheable JSON resource
  rather than LLM-synthesized output, a privacy notice or standardized
  settings panel served this way has no per-request LLM cost, unlike a
  dynamically generated card.

### Claim 4: A2UI-over-MCP, A2UI-over-A2A, and (implicitly) A2UI-over-MCP-Tools form a dynamism gradient — MCP Resources are static/prescriptive, MCP Tools are templated/parameter-bound, and A2A is fully generative within the component catalog

- **Evidence**: A dedicated section, "Understanding the differences: A2UI
  over MCP vs. A2UI over A2A," gives three bullet definitions ordered by
  dynamism.
- **Confidence**: settled (first-party explicit comparison table in prose
  form)
- **Quote**: "**A2UI over MCP (Resources):** Static and prescriptive UI. This is the optimal choice for rigid structural requirements such as fixed data entry forms."
- **Quote (2)**: "**A2UI over MCP (Tools):** Templated and dynamic UI based on tool parameters. It can also serve static and prescriptive UI too. The dynamic controls are limited to the tool's input parameters."
- **Quote (3)**: "**A2UI over A2A:** Fully generative and open-ended within the scope of the components in the supported catalogs. The agent has full conversational context and drives UI construction on the fly."
- **Our assessment**: The key constraint buried in this section is that
  MCP-Tools-based dynamic UI is bounded by "the too[l] parameters and the
  prescribed prompt for the backend agent" — i.e., even the "dynamic"
  MCP-tool path is not as open-ended as full A2A because the backend LLM
  driving it only sees what the tool's own parameter schema exposes, not
  the full conversational context an A2A agent would have. Practitioners
  choosing between MCP-Tools-delivered A2UI and A2A-delivered A2UI should
  treat this as a real capability ceiling, not just an implementation
  detail — MCP Tools capped at tool-parameter context is a materially
  smaller UI generation surface than full A2A conversational context.

### Claim 5: Pattern 2 (MCP Apps in A2UI) wraps an MCP App inside a dedicated A2UI "MCP App Component" — a reusable secure iframe wrapper — letting complex state-intensive modules (e.g., a real-time Pong game) sit inside an otherwise-native A2UI surface

- **Evidence**: Description of a custom A2UI component that acts as a
  generalized iframe wrapper, demonstrated with a Pong-game MCP App
  embedded alongside two native A2UI scorecards in a single surface.
- **Confidence**: settled (concrete architecture description with a working
  demo and linked sample code)
- **Quote**: "To achieve this hybrid approach, developers define a custom A2UI component that acts as a secure iframe wrapper (referred to as MCP App Component). This generalized wrapper can hold any standard MCP App and provides a bridged channel for the app to communicate with the outside world."
- **Our assessment**: The architectural insight here is that the wrapper is
  generalized — a single "MCP App Component" type can host *any* MCP App,
  not a bespoke wrapper per app. This means A2UI hosts only need to
  implement iframe-wrapping support once to gain the ability to embed
  arbitrary MCP Apps, rather than needing custom integration work per
  embedded app. This is the pattern's key reusability property and is not
  hedged or qualified in the source.

### Claim 6: State synchronization between a native A2UI surface and an embedded MCP App follows a fixed three-step interception loop (Interception and Conversion → Request Routing → Hydration), with the backend agent tracking only coarse "key-states," not fine-grained micro-state

- **Evidence**: A numbered three-step description of what the post names
  "state synchronization," explicitly contrasted with alternative
  approaches ("Rather than relying on real-time DOM scraping or state
  polling...").
- **Confidence**: settled (first-party protocol description, explicit
  numbered steps, explicit contrast with rejected alternative designs)
- **Quote**: "The A2UI Rendering Engine maintains the state across both the native components and the embedded MCP Apps using a secure, event-driven cycle, which we refer to as **state synchronization**. Rather than relying on real-time DOM scraping or state polling, synchronization follows an explicit interception loop"
- **Quote (key-states)**: "The agent functions as the overarching coordinator, tracking only macro \"key-states\" (such as game score or reservation confirmation) without keeping track of micro-states (such as paddle/ball coordinates or temporary form inputs)."
- **Our assessment**: This is the most architecturally important claim in
  Pattern 2 for practitioners building similar hybrid systems: the design
  explicitly avoids DOM scraping/polling (fragile, high-frequency
  patterns) in favor of an event-driven, tool-call-triggered
  synchronization where the MCP App's own internal `paddle/ball
  coordinates`-style micro-state never leaves the iframe. Only
  agent-relevant coarse state (a score, a confirmation) crosses the
  boundary. This is a concrete, transferable pattern for any system that
  needs to keep an LLM "aware" of an embedded interactive surface's state
  without forcing the LLM to process high-frequency UI events — directly
  relevant to token/context economy for agents supervising live UI.

### Claim 7: Pattern 3 (A2UI inside MCP Apps) bundles the A2UI rendering engine inside the MCP App itself, letting an MCP App provide agent-driven generative UI even when the host application has no native A2UI support

- **Evidence**: Description of the pattern as "a powerful modernization
  bridge," demonstrated with a text-editor MCP App that renders dynamic
  A2UI-delivered editing controls (sliders, parameters) inside its own
  iframe boundary after highlighting text.
- **Confidence**: settled (first-party architecture description with
  worked demo — a generative document editor — and linked sample code)
- **Quote**: "This pattern serves as a powerful modernization bridge, allowing developers to inject dynamic, agent-driven UIs into legacy applications or non-A2UI environments without requiring a complex architectural overhaul."
- **Quote (mechanism)**: "In this pattern, the MCP App bundle contains its own A2UI renderer. To fetch the dynamic A2UI interfaces, the MCP App bridges a tool call to the server to retrieve the A2UI payload, leveraging the A2UI-over-MCP mechanics discussed earlier."
- **Our assessment**: This is explicitly positioned as a legacy-system
  migration path, distinct from Patterns 1 and 2, which assume the host
  already supports A2UI. Pattern 3 requires zero host-side A2UI investment
  — "Legacy applications only need to support a basic MCP App iframe
  container" — pushing all A2UI rendering complexity into the MCP App
  bundle itself. This is the pattern most relevant to organizations with
  existing MCP App infrastructure who want generative UI without a host
  rewrite, at the cost of duplicating the A2UI renderer inside every such
  MCP App rather than sharing one host-level renderer.

### Claim 8: Pattern 3's interaction lifecycle is a five-step loop where local state transitions (e.g., accepting/rejecting a document revision) are handled entirely inside the app sandbox, and only high-level user actions are relayed to the backend agent via `postMessage`

- **Evidence**: A numbered five-step lifecycle (Context Trigger → Event
  Relay → Generative Payload Return → Internal Rendering → Managed
  Communication) plus a full pseudocode HTML/JS example implementing the
  loop.
- **Confidence**: settled (first-party description with matching code
  example — the code and the prose description are internally consistent)
- **Quote**: "High-level user actions are relayed through the bridge for backend processing, while local state transitions—like accepting or rejecting revisions—are managed directly within the app sandbox to maintain security isolation."
- **Quote (event relay mechanism)**: "The App Bridge transmits this event to the host via postMessage, which subsequently routes the context to the backend AI agent."
- **Our assessment**: Pattern 3 uses `postMessage` for the App Bridge
  itself (host↔iframe transport), which is a different transport choice
  than `blog-simonwillison-datasette-apps.md` Claim 2, where Willison
  explicitly moved *away* from `postMessage()` to `MessageChannel()` for
  Datasette Apps specifically because `MessageChannel()` channels
  auto-close on frame navigation, closing a data-exfiltration path. This
  post does not mention that security property or discuss what happens if
  an embedded MCP App navigates away mid-session — see Cross-References
  below for whether this rises to a documented contradiction.

## Concrete Artifacts

### A2UI payload delivered as an Embedded Resource via MCP Tool Call (Pattern 1)

```json
{
  "content": [
    {
      "type": "resource",
      "resource": {
        "uri": "a2ui://dynamic-ui/recipe-card",
        "mimeType": "application/a2ui+json",
        "text": "[
          { "version": "v0.9",
            "createSurface": { ... }
          }
        ]"
      }
    }
  ]
}
```
*Source: developers.googleblog.com/a2ui-and-mcp-apps/, "Under the hood: How it works" section (Pattern 1).*

### State synchronization interception loop (Pattern 2)

```
1. Interception and Conversion:
   MCP App triggers a standard MCP tool call on a key state transition
   (e.g., a point is scored). The A2UI wrapper intercepts this locally,
   maps the JSON arguments into structured A2UI Action context, and
   immediately returns an acknowledgment so the app's local UI loop is
   unblocked.
2. Request Routing:
   Host application packages the converted context as an A2UI Action and
   routes it to the backend AI Agent, which tracks only macro "key-states"
   (e.g., game score, reservation confirmation) — not micro-states (e.g.,
   paddle/ball coordinates, temporary form inputs).
3. Hydration:
   Agent evaluates overall surface state, returns a formatted DataModel
   Update JSON. The A2UI engine updates native components directly and
   pushes the updated resource through the App Bridge to re-hydrate the
   embedded MCP App's internal state.
```
*Source: developers.googleblog.com/a2ui-and-mcp-apps/, "Under the hood: How it works" section (Pattern 2).*

### Pattern 3 pseudocode: MCP App bundling its own A2UI renderer

```html
<html>
<body>

  <div>
    <h3>MCP App (Editor Panel)</h3>
    <p>This text is native to the sandboxed third-party app.</p>

    <!-- A2UI Surface custom element provided by the A2UI SDK -->
    <a2ui-surface surfaceId="recipe-card"></a2ui-surface>
  </div>

  <script>
    // Note: The pseudocode below assumes AppBridge from @modelcontextprotocol/ext-apps
    // and a2uiProcessor from the A2UI SDK are preloaded or inlined.
    const bridge = new AppBridge({ name: 'editor-panel', version: '1.0.0' });

    // Helper to extract and process dynamic A2UI responses from tool results
    function processA2UIResponse(result) {
      const a2uiResource = result?.content?.find(
        c => c.type === 'resource' && c.resource?.mimeType === 'application/a2ui+json'
      );
      if (a2uiResource?.resource?.text) {
        const payload = JSON.parse(a2uiResource.resource.text);
        window.a2uiProcessor.processMessages(payload);
      }
    }

    // 1. Initialize AppBridge and fetch initial controls
    async function initApp() {
      await bridge.connect();

      // Call server tool to load initial layout controls
      const result = await bridge.callServerTool({ name: 'fetch_controls', arguments: {} });
      processA2UIResponse(result);
    }

    // 2. Handle interactive User Actions routed by the A2UI SDK
    window.a2uiProcessor.events.subscribe(async (event) => {
      if (!event.message.userAction) return;
      const action = event.message.userAction;

      // Route the user action directly via the bridge to the MCP Server tool
      const result = await bridge.callServerTool({
        name: action.name,
        arguments: action.context
      });

      // Feed any updated server UI states back to the A2UI processor
      processA2UIResponse(result);
    });

    // Initialize the app on startup
    initApp();
  </script>
</body>
</html>
```
*Source: developers.googleblog.com/a2ui-and-mcp-apps/, "Under the hood: How it works" section (Pattern 3). Copied verbatim including the source's own inline comments.*

### Three-pattern summary

```
Pattern 1 — A2UI over MCP servers
  Mechanism: MCP tool/resource response with mimeType application/a2ui+json
  Bypasses:  MCP App iframe entirely
  Delivery:  Static (MCP Resources) or Dynamic (MCP Tool Calls)
  Best for:  Native rendering of standard UI elements without iframe overhead

Pattern 2 — MCP Apps in A2UI Components
  Mechanism: MCP App wrapped in a reusable A2UI "MCP App Component" (iframe wrapper)
  Sync:      Three-step interception loop (Interception → Routing → Hydration)
  Best for:  Complex, state-intensive modules (games, bespoke validation UIs)
             embedded inside an otherwise-native design system

Pattern 3 — A2UI inside MCP Apps
  Mechanism: A2UI renderer bundled inside the MCP App itself
  Transport: App Bridge over postMessage
  Best for:  Legacy / non-A2UI hosts that only support a basic MCP App iframe
             container, with zero host-side A2UI investment required
```
*Source: developers.googleblog.com/a2ui-and-mcp-apps/, synthesized from the "Conclusion" section's own one-line-per-pattern summary and the three "Under the hood" sections.*

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 8 ("MCP Apps
    (interactive interfaces returned by tools)... is the first official
    protocol extension and lets a tool return an interactive interface,
    such as a chart, form, or dashboard"): this post is a deep dive into
    exactly the extension that claim introduces, and Pattern 1 here (A2UI
    over MCP) documents a *second*, non-iframe mechanism — MIME-typed A2UI
    JSON payloads — for a tool to "return an interactive interface" that
    the Anthropic post does not mention. Together the two notes show there
    are at least two distinct protocol-level mechanisms for MCP tools to
    return rich UI: MCP Apps (iframe) and A2UI-over-MCP (native JSON
    rendering).
  - `blog-simonwillison-datasette-agent-charts.md` Claim 1 (`render_chart`
    tool "extends datasette-agent... via a `render_chart` tool that accepts
    SQL queries and structured chart configuration" — the LLM controls a
    structured visual spec, not raw HTML): this is architecturally the same
    pattern as A2UI-over-MCP (Claim 2 here) at smaller scale — a tool
    response carries a *declarative, structured* specification that a
    fixed host-side renderer turns into UI, rather than returning raw
    markup. Datasette's `render_chart` is a single-purpose, bespoke version
    of the general-purpose A2UI JSON contract this post formalizes.
  - `blog-cursor-canvas.md` Claim 2 ("Cursor renders canvases using a
    React-based UI library with first-party components like tables, boxes,
    diagrams, and charts"): Cursor's canvas architecture — agents compose
    from a fixed palette of first-party components rather than generating
    arbitrary HTML/CSS — is the same declarative-over-freeform trade-off
    A2UI makes (Claim 1 here), applied inside an IDE rather than over MCP.
    Both sources independently arrive at "constrain agent UI output to a
    predefined component catalog" as the design choice that buys
    consistency and safety at the cost of expressiveness.

- **Contradicts**: None filed as a formal contradiction. Claim 8's
  transport choice (App Bridge over plain `postMessage`) sits in tension
  with `blog-simonwillison-datasette-apps.md` Claim 2, where Willison
  deliberately replaced `postMessage()` with `MessageChannel()` specifically
  because "if a page navigates to somewhere else the channel closes
  automatically" — a security property `postMessage()` lacks. However, this
  does not rise to a filable contradiction per MINER.md §4a: the two
  sources address different trust boundaries (Datasette Apps hosts
  arbitrary LLM-generated, potentially adversarial app code and treats
  transport-level exfiltration as an active threat it explicitly tested
  for; this post's MCP Apps are first-party-authored server-provided
  components, and the post does not make any explicit security claim about
  `postMessage` being sufficient that a `MessageChannel()`-based claim
  would rebut). It is a documented gap worth watching, not an opposing
  claim — noting it here so the Smith can decide whether to flag
  `postMessage`-based App Bridges as an area needing the same
  navigation-teardown hardening Datasette Apps applied, if a future source
  makes an explicit claim either way.

- **Extends**:
  - `blog-anthropic-mcp-production-agents.md`: that post names MCP Apps
    and elicitation as MCP's "first official protocol extension[s]" at a
    high level; this post is the detailed architectural companion,
    specifically for combining MCP Apps with A2UI, including protocol-level
    mechanism (MIME type), delivery-mode trade-offs (static vs. dynamic),
    and a state-synchronization protocol not mentioned in the Anthropic
    post at all.
  - `blog-cursor-canvas.md`: extends the "declarative component palette
    for agent UI output" pattern from a single-vendor IDE feature (Cursor
    canvases) to a cross-vendor, protocol-level standard (A2UI transported
    over MCP), with an explicit mechanism for when to break out of the
    palette into custom iframe UI (Pattern 2) that Cursor's canvas post
    does not address at all — Cursor's canvases have no equivalent "escape
    hatch to full custom UI" pattern documented.

- **Novel**:
  - **The `application/a2ui+json` MIME-type convention** for MCP tool/resource
    responses is new to the corpus — no existing note documents a
    MIME-type-based mechanism for MCP UI delivery.
  - **The three-pattern taxonomy itself** (A2UI-over-MCP, MCP-Apps-in-A2UI,
    A2UI-in-MCP-Apps) as a named decision framework for combining
    declarative and iframe-based agentic UI is new to the corpus.
  - **The state-synchronization interception loop** (Interception and
    Conversion → Request Routing → Hydration) with explicit macro
    "key-state" vs. micro-state separation is a new, transferable pattern
    for keeping an LLM aware of embedded interactive UI state without
    high-frequency event processing.
  - **The dynamism gradient across A2UI transports** (MCP Resources:
    static → MCP Tools: templated/parameter-bound → A2A: fully generative)
    is a new comparative framework not present in any existing MCP or A2A
    source note in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Pattern 1 (A2UI over MCP,
  Claim 2) as a concrete, low-effort option for MCP server authors who want
  to return rich UI without building a full MCP App/iframe integration —
  complementary to the existing MCP Apps guidance the guide may pull from
  `blog-anthropic-mcp-production-agents.md`. Specifically note the MIME
  type (`application/a2ui+json`) and the static-vs-dynamic delivery choice
  (Claim 3) as the two design decisions a server author must make.

- **Chapter 02 (Harness Engineering)**: When documenting MCP Apps as an
  interactive-interface mechanism, add the three-pattern decision framework
  (Concrete Artifacts → "Three-pattern summary") as guidance for choosing
  between native declarative rendering, hybrid embedding, and full
  iframe-hosted custom UI, depending on whether the host has A2UI support
  and whether the UI need is state-intensive/custom (Pattern 2) versus
  standard/form-like (Pattern 1).

- **Chapter 04 (Context Engineering)**: Add the state-synchronization
  macro/micro-state distinction (Claim 6) as a pattern for keeping an
  agent's context focused on decision-relevant state ("key-states" like
  score or confirmation) while excluding high-frequency UI micro-state
  (cursor position, paddle coordinates) from ever entering the agent's
  context — a concrete instance of the broader context-economy principle
  applied to agents supervising live embedded UI.

## Extraction Notes

- **WebFetch summarized rather than quoted verbatim**: as with prior
  Google/Anthropic blog extractions in this corpus, an initial WebFetch
  pass returned a paraphrased/restructured summary (with a fabricated
  "Overview" heading not present in the source) rather than the source's
  actual text. All quotes in this note were instead sourced from the raw
  HTML fetched directly via `curl` and converted to Markdown, then verified
  against that raw text line-by-line before being included as quotes. No
  quote in this note is sourced from the WebFetch summary.
- **Full page read**: The entire post was read, including all three
  "Under the hood" sections, all three "Explore the code" linked-guide
  references (not followed — they point to interactive tutorials/live
  demos on `a2ui.org`, not additional prose content), the conclusion, the
  decision-tree image (described but not machine-readable — it is a PNG,
  not extractable as text; the post's own one-line-per-pattern summary in
  the Conclusion section was used as the textual equivalent), and the "Get
  started" links section.
  Images (`table.original.png`, `decision_tree_5.original.png`) could not
  be read as text; their content is not represented in this note beyond
  what the surrounding prose describes.
- **Sample-code repositories were not cloned or read**: the three demo
  repositories under `github.com/a2ui-project/a2ui` and `github.com/google/A2UI`
  are referenced in the post but were not fetched separately — the post's
  own inline code examples (all three of which are reproduced verbatim
  above) were treated as sufficient concrete artifacts for this note. A
  future source-note update could deep-read the sample repos if the guide
  needs implementation-level detail beyond what this post documents.
- **No contradiction issue filed**: reviewed the `postMessage` vs.
  `MessageChannel()` tension against `blog-simonwillison-datasette-apps.md`
  Claim 2 (see Cross-References → Contradicts) and determined it does not
  meet the bar in MINER.md §4a — the two sources describe different trust
  models (first-party MCP App content vs. Datasette's explicitly
  adversarial LLM-generated app threat model) rather than making opposing
  claims about the same conditioning variable.
