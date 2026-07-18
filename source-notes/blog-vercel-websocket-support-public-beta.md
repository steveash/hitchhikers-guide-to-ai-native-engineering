---
source_url: https://vercel.com/changelog/websocket-support-is-now-in-public-beta
source_type: blog-post
title: "WebSocket support is now in Public Beta"
author: Matthew Stanciu, Mark Glagola, Ethan Niser, Casey Gowrie (Vercel)
date_published: 2026-06-22
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: emerging
issue: "#1999"
---

# WebSocket support is now in Public Beta

> Vercel Functions can now serve persistent WebSocket connections in Public
> Beta, explicitly naming "interactive AI streaming" as a target use case;
> the linked documentation reveals the load-bearing mechanics the changelog
> itself omits — a connection is pinned to one Function instance and its
> lifetime is capped by that Function's maximum duration (300s on Hobby;
> up to 800s GA / 1800s beta on Pro and Enterprise), reconnects are not
> guaranteed to land on the same instance, and Socket.IO's default
> long-polling transport must be explicitly disabled to work at all.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published June 22, 2026; a ~150-word, "1 min read" feature announcement
  with one embedded code sample). Per MINER.md §1, this note follows the
  changelog's own "Read the documentation" link to
  `/docs/functions/websockets` in full, since that page contains nearly all
  of the mechanism detail — the changelog itself states only that
  WebSockets exist and follow "the same limits and pricing" as other
  Function invocations, without saying what those limits are. A second
  linked page, `/docs/functions/limitations`, was also followed
  specifically to resolve the concrete maximum-duration numbers the
  Prospector's triage comment flagged as the "key question" (connection
  duration limits), since neither the changelog nor the WebSockets doc
  page states them directly — both only link to the limitations page's
  `#max-duration` anchor.
- **Author credibility**: First-party Vercel changelog entry with four
  named authors (Matthew Stanciu, Mark Glagola, Ethan Niser, Casey Gowrie),
  all listed as Vercel employees (three with "Software Engineer" job
  titles per the page's embedded JSON-LD metadata). Vercel operates the
  Functions platform being described, so the mechanics documented here
  (instance pinning, duration limits, pricing model, framework support) are
  authoritative first-party documentation of a shipping/beta capability,
  not third-party reporting. No named customer or production deployment is
  cited anywhere in the changelog or the two linked docs pages.
- **Scope**: Covers WebSocket connection handling on Vercel Functions —
  the request lifecycle (HTTP upgrade), instance pinning and multi-tenancy
  under Fluid compute, disconnect/reconnect handling, persistent-state
  guidance, per-framework setup (Node.js: `ws`, Socket.IO, Express, Hono,
  h3, Nitro; Python: FastAPI, `python-socketio`), the Next.js-specific
  workaround, and limits/pricing. Does NOT cover: message size limits
  (no cap is stated anywhere in the source family — see Extraction Notes),
  concurrent-connections-per-instance numbers, any benchmark or
  latency/throughput measurement, or any named production user of the
  feature.

## Extracted Claims

### Claim 1: Vercel Functions can now serve WebSocket connections in Public Beta, with "interactive AI streaming" named explicitly alongside chat and collaborative apps as the target use case
- **Evidence**: The changelog's opening two sentences, the first substantive content on the page.
- **Confidence**: settled (first-party feature announcement, unambiguous)
- **Quote**: "Vercel Functions can now serve WebSocket connections, enabling bidirectional communication between clients and server-side code on Vercel." / "Use WebSockets for realtime features such as interactive AI streaming, chat, and collaborative apps."
- **Our assessment**: This is the entire substance of the changelog's own framing — a platform capability being explicitly pitched at AI streaming use cases is directly relevant to harness/infrastructure decisions, but the changelog alone gives no mechanism detail; everything a practitioner needs to actually evaluate this for an AI streaming workload (Claims 2-10) comes from the linked docs pages, not this announcement text itself.

### Claim 2: A single WebSocket connection is pinned to one Vercel Function instance for the connection's entire lifetime, though Fluid compute lets one instance multiplex many simultaneous connections
- **Evidence**: Direct architectural statement on the WebSockets docs page, the first technical detail beyond the changelog's marketing framing.
- **Confidence**: settled (first-party architectural description of a shipping mechanism)
- **Quote**: "A single WebSocket connection is pinned to one Vercel Function instance. Messages sent over that connection reach the same function instance for the lifetime of the connection, and Fluid compute allows a single function instance to handle multiple WebSocket connections."
- **Our assessment**: This is the load-bearing architectural fact the rest of the source's operational guidance (Claims 4-5) follows from: within a connection's life, routing is sticky (one instance); across reconnects, it is not (Claim 5). A single Fluid-compute instance handling many concurrent WebSocket connections is the multi-tenancy model that makes this economically viable versus one dedicated process per connection.

### Claim 3: WebSocket connections bill under the same Active CPU pricing as other Function invocations — only time spent actively processing messages is charged, not idle connection time
- **Evidence**: Direct pricing statement in the changelog, immediately following the architectural framing.
- **Confidence**: settled (first-party pricing-model description)
- **Quote**: "WebSocket connections run on Fluid compute and follow the same limits and pricing as other Function invocations. With Active CPU pricing, billing only applies to the time your Function spends processing messages, not idle connection time."
- **Our assessment**: This is a materially different cost model from a dedicated WebSocket server (e.g. a long-running Node process on a VM, billed by wall-clock uptime): a Vercel-hosted connection that sits open but idle for minutes between AI-streaming turns costs nothing during the idle stretches. For a chat/streaming AI use case with bursty, human-paced message cadence, this changes the unit economics from "cost scales with connection count × session length" to "cost scales with actual message-processing CPU time" — a relevant data point for anyone comparing managed-WebSocket hosting costs for AI applications.

### Claim 4: A WebSocket connection's maximum lifetime is bounded by its Function's configured maximum duration — connections close when that duration is reached, with concrete platform ceilings of 300s on Hobby and up to 800s (GA) or 1800s (beta, restricted runtimes) on Pro/Enterprise
- **Evidence**: The WebSockets docs page states the closure rule; the linked Functions Limits reference page (`/docs/functions/limitations#max-duration`) supplies the actual numeric bounds via a Node.js/Python duration table, which neither the changelog nor the WebSockets page states directly.
- **Confidence**: settled (first-party documentation combining an explicit behavioral rule with a numeric limits table from the same vendor's reference docs)
- **Quote**: "WebSocket connections close when a Vercel Function reaches its maximum duration." (`/docs/functions/websockets`) — cross-referenced against the limits table: "Hobby | 300s (5 minutes) | 300s (5 minutes) | -" and "Pro | 300s (5 minutes) | 800s | 1800s (30 minutes)" with the note "The 800 second maximum is generally available for Pro and Enterprise teams. The 1800 second extended maximum is in beta. Values above 800 seconds require function-level configuration and are only supported for specific Node.js and Python runtime versions." (`/docs/functions/limitations`)
- **Our assessment**: This directly answers the Prospector's triage "key question" about connection duration constraints — there is no unlimited-duration WebSocket tier. A Hobby-tier deployment gets a hard 300-second ceiling on any single connection regardless of activity; Pro/Enterprise can extend to 800s (GA) or 1800s (still beta, and restricted to specific runtime versions, with Secure Compute/Static IPs explicitly excluded from durations above 800s during the beta). For AI streaming specifically, this means any session expected to run longer than these ceilings (e.g., a long agentic back-and-forth or an extended voice conversation) must be designed around forced disconnection and client-side reconnect (Claim 5's reconnect guidance), not treated as a single unbroken channel — this is a materially different constraint than, e.g., OpenAI's Realtime API sessions, which last "up to 30 minutes" per an ephemeral token model documented in `blog-simonwillison-openai-webrtc-document-context.md` Claim 2 (see Cross-References).

### Claim 5: New WebSocket connections are not guaranteed to reach the same Function instance as prior connections, and a new deployment can split traffic — existing connections stay on the old deployment until they close, while new connections may land on the new one — so durable/shared state must live in an external store, not in-memory
- **Evidence**: A dedicated "Manage persistent state" section on the WebSockets docs page, giving the reconnection and deployment-split behavior together with the recommended mitigation.
- **Confidence**: settled (first-party operational guidance describing a specific distributed-systems constraint of the platform)
- **Quote**: "New WebSocket connections are not guaranteed to reach the same Vercel Function instance. If a client reconnects, it may connect to a different instance. After a new deployment, new connections may reach the new deployment while existing connections remain on the previous deployment until they close." / "Store durable state, presence, counters, rooms, and pub/sub coordination in an external data store instead of relying on in-memory variables. For example, you can use Redis from the Vercel Marketplace to share state across function instances and deployments."
- **Our assessment**: Combined with Claim 2 (sticky-within-connection, not across reconnects) and Claim 4 (connections are forced to close at the duration ceiling), this establishes that any AI streaming application built on this feature must treat every connection as ephemeral by design — a forced disconnect-and-reconnect is a normal, expected event (not a failure mode), and any state that must survive it (conversation history, room membership, in-flight agent task state) has to be externalized from the start rather than retrofitted later. This is a concrete architectural requirement the guide should surface alongside the recommendation to use this feature for AI streaming.

### Claim 6: A WebSocket connection begins as a normal HTTP GET request with an Upgrade header, and passes through the same routing/security pipeline (Routing Middleware, rewrites, Firewall rules, rate limits) as any other request before the upgrade completes — Firewall rules can target the WebSocket path specifically, and rate limits apply per upgrade attempt
- **Evidence**: The "Request lifecycle" section of the WebSockets docs page, stated as a direct architectural/security description.
- **Confidence**: settled (first-party description of the platform's request-handling pipeline)
- **Quote**: "A WebSocket connection starts as an HTTP GET request with an Upgrade header. Before the connection is upgraded, the request goes through the same routing and security controls as other requests to Vercel Functions, including Routing Middleware, rewrites, Firewall rules, and rate limits. You can write Firewall rules that target the WebSocket request path, and rate limits apply to each upgrade request."
- **Our assessment**: This means existing Vercel Firewall/rate-limit configuration extends to WebSocket endpoints without a separate configuration surface — a practitioner who has already rate-limited an HTTP API route can apply the same primitive to the WebSocket upgrade path. Note the scope: rate limits apply "to each upgrade request" (i.e., connection attempts), not to messages sent over an already-established connection — a distinct concern from per-message throughput, which this source does not address.

### Claim 7: WebSocket support spans both Node.js (`ws`, Socket.IO, Express, Hono, h3, Nitro) and Python (FastAPI with `websockets`/`wsproto`/`uvicorn[standard]`, or `python-socketio`) runtimes, and the JavaScript and Python Socket.IO server implementations are protocol-compatible — a client can connect to either
- **Evidence**: Dedicated code-example sections for each runtime/framework combination on the WebSockets docs page, plus an explicit cross-language compatibility statement for Socket.IO.
- **Confidence**: settled (first-party documentation with working code examples for each claimed combination)
- **Quote**: "Python frameworks like FastAPI also work with WebSockets on Vercel Functions." / "You can also use python-socketio for the same rooms, namespaces, and broadcast features as the JavaScript Socket.IO library. The two are protocol-compatible, so clients can connect to either server."
- **Our assessment**: The Python-runtime support is notable for AI streaming specifically, since many AI/ML backend teams run Python services (model inference, agent orchestration) rather than Node — this removes "our backend is Python, not Node" as a blocker to using Vercel's native WebSocket hosting, distinct from a JS-only WebSocket feature that would require a bridging service for Python-based agent backends.

### Claim 8: Next.js — Vercel's own flagship framework — has no native API for handling WebSocket upgrades on Vercel Functions and requires an experimental workaround, unlike Nitro/Nuxt (native support) or Express/Hono/h3 (direct library use)
- **Evidence**: A dedicated "Next.js" subsection on the WebSockets docs page, explicitly naming the gap and the workaround API.
- **Confidence**: settled (first-party statement of a specific framework-support gap, notable because it is self-disclosed about the vendor's own primary framework rather than a third-party framework)
- **Quote**: "Next.js does not expose an API for handling WebSocket upgrades. As a workaround, you can use the experimental_upgradeWebSocket() API:" — followed by a code example importing `experimental_upgradeWebSocket` and `WebSocketData` from `@vercel/functions`.
- **Our assessment**: The word "experimental" in the API name itself signals this is not yet a stable, first-class Next.js integration path, even though Next.js is Vercel's own framework and the one most of its documentation and marketing centers on. Practitioners building an AI-streaming app in Next.js on Vercel should expect to reach for this experimental API rather than a native route-handler pattern — and should treat it as more likely to change than the Nitro/Express/Hono/h3 paths, which use their own frameworks' native WebSocket APIs directly rather than a Vercel-specific experimental shim.

### Claim 9: WebSockets require Fluid compute to be enabled, which has only been the default for new Vercel projects since April 23, 2025 — projects created before that date may need to explicitly enable it
- **Evidence**: The final line of the "Limits and pricing" section on the WebSockets docs page.
- **Confidence**: settled (first-party statement of a specific prerequisite with a stated cutoff date)
- **Quote**: "WebSockets require Fluid compute to be enabled. This is the default for new projects created on or after April 23, 2025."
- **Our assessment**: This is a concrete prerequisite-check practitioners with older Vercel projects need to verify before WebSocket support will work at all — a project created before April 23, 2025 is not guaranteed to have Fluid compute on by default, distinct from the general availability of the WebSocket feature itself (Public Beta as of this June 22, 2026 changelog).

### Claim 10: A Socket.IO client connecting to a Vercel-hosted WebSocket endpoint must explicitly force the WebSocket transport (`transports: ['websocket']`), because Socket.IO's default behavior is to fall back to HTTP long-polling first
- **Evidence**: An inline code comment in the docs page's Socket.IO client example, marked "required" rather than merely suggested.
- **Confidence**: settled (explicit, unambiguous code-level requirement stated by the vendor); the underlying *reason* long-polling is incompatible is our inference, not stated in prose by the source (see Our assessment)
- **Quote**: "transports: ['websocket'], // required — Socket.IO defaults to HTTP long-polling"
- **Our assessment**: The source states this is "required" but does not explain why in prose. Read alongside Claim 5 (new connections are not guaranteed to reach the same instance), the likely mechanism is that Socket.IO's default long-polling transport depends on a sequence of separate HTTP requests being routed to a session-consistent backend, which conflicts with a serverless routing model that does not guarantee instance stickiness across separate requests the way a persistent WebSocket connection does within itself. This is a concrete, easy-to-miss configuration gotcha: a team that adopts Socket.IO's client defaults without this override would see connection failures or silent fallback behavior, not an obvious error pointing at the cause.

## Concrete Artifacts

### Full changelog announcement text (verbatim, `vercel.com/changelog/websocket-support-is-now-in-public-beta`, published 22 Jun 2026)

```
Vercel Functions can now serve WebSocket connections, enabling bidirectional
communication between clients and server-side code on Vercel.

Use WebSockets for realtime features such as interactive AI streaming, chat,
and collaborative apps.

WebSocket connections run on Fluid compute and follow the same limits and
pricing as other Function invocations. With Active CPU pricing, billing only
applies to the time your Function spends processing messages, not idle
connection time.

You can serve WebSocket connections using standard Node.js libraries, with no
additional configuration:

// api/ws.ts
import express from 'express';
import { createServer } from 'http';
import { WebSocketServer } from 'ws';

const app = express();
const server = createServer(app);
const wss = new WebSocketServer({ server });

wss.on('connection', (ws) => {
  ws.on('message', (data) => {
    ws.send(data);
  });
});

export default server;

Higher-level libraries like Socket.IO are also supported.

Read the documentation to get started.

Authors: Matthew Stanciu, Mark Glagola, Ethan Niser, Casey Gowrie
```

### Maximum-duration table for Node.js/Python runtimes (verbatim, `/docs/functions/limitations#max-duration`)

```
|            | Default          | Maximum | Extended maximum   |
| ---------- | ----------------- | ------- | ------------------ |
| Hobby      | 300s (5 minutes) | 300s (5 minutes) | -          |
| Pro        | 300s (5 minutes) | 800s    | 1800s (30 minutes) |
| Enterprise | 300s (5 minutes) | 800s    | 1800s (30 minutes) |

"The 800 second maximum is generally available for Pro and Enterprise teams.
The 1800 second extended maximum is in beta. Values above 800 seconds require
function-level configuration and are only supported for specific Node.js and
Python runtime versions. Secure Compute and Static IPs do not support
durations above 800 seconds during the beta."

"For workloads that require unlimited execution time, use Vercel Workflows,
which allow your code to pause, resume, and maintain state for minutes to
months without duration limits."

Source: https://vercel.com/docs/functions/limitations
```

### Socket.IO client transport override (verbatim, `/docs/functions/websockets`)

```typescript
// client.ts
import { io } from 'socket.io-client';

const socket = io('https://your-domain.com', {
  // Socket.IO appends /socket.io to the path by default,
  // so the full path becomes /api/socket-io/socket.io
  path: '/api/socket-io/socket.io',
  transports: ['websocket'], // required — Socket.IO defaults to HTTP long-polling
});
```

### Next.js experimental WebSocket workaround (verbatim, `/docs/functions/websockets`)

```typescript
// app/api/ws/route.ts
import {
  experimental_upgradeWebSocket,
  type WebSocketData,
} from '@vercel/functions';

export async function GET() {
  return experimental_upgradeWebSocket((ws) => {
    ws.on('message', (data: WebSocketData) => {
      ws.send(data);
    });
  });
}
```

### Recommended client reconnect-with-backoff pattern (verbatim, `/docs/functions/websockets`, "Handle disconnections and reconnects")

```typescript
// client.ts
let socket: WebSocket;
let reconnectDelay = 1000;

function connect() {
  socket = new WebSocket('wss://your-domain.com/api/ws');

  socket.addEventListener('open', () => {
    reconnectDelay = 1000;
  });

  socket.addEventListener('message', (event) => {
    console.log(event.data);
  });

  socket.addEventListener('close', () => {
    setTimeout(connect, reconnectDelay);
    reconnectDelay = Math.min(reconnectDelay * 2, 30000);
  });
}

connect();
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-luke-curley-webrtc.md`, `blog-simonwillison-openai-webrtc-document-context.md`,
`blog-vercel-ai-gateway-api-key-budgets.md`, and `blog-vercel-enterprise-apps-and-agents.md`
were re-read in full during this extraction (MINER.md §4b), and every claim
number cited below was located and confirmed against that note's own
numbered `### Claim N:` headings in document order before writing this
section.

- **Corroborates**:
  - `blog-simonwillison-luke-curley-webrtc.md` Claim 8 ("if I was working at
    OpenAI, I'd start by stream audio over WebSockets. You can leverage
    existing TCP/HTTP infrastructure instead of inventing a custom WebRTC
    load balancer... it's simple, works with Kubernetes, and SCALES"):
    Curley's recommendation was a practitioner's architectural opinion about
    what LLM voice/streaming AI *should* run on. This source is a major
    platform (Vercel) now shipping exactly that transport as a managed,
    natively-billed primitive, with "interactive AI streaming" named as a
    first-class use case in the announcement itself (Claim 1 here). This
    does not corroborate Curley's specific WebRTC-vs-WebSocket technical
    critique (which this source does not engage with at all — it says
    nothing about WebRTC), only his conclusion that WebSockets are a
    practical, infrastructure-friendly choice for streaming AI.

- **Contradicts**: None identified. This source makes no claim that
  conflicts with any existing corpus note; it does not address WebRTC,
  QUIC, or any of the transport-protocol tradeoffs the Curley note covers,
  and does not make claims about model behavior, cost, or capability that
  any Vercel or non-Vercel note contradicts.

- **Extends**:
  - `blog-vercel-ai-gateway-api-key-budgets.md` and
    `blog-vercel-enterprise-apps-and-agents.md`: both document other Vercel
    platform primitives (AI Gateway API-key budgets; Passport/Connect/
    Enterprise Managed Users/BYOC) built on the same Fluid-compute
    infrastructure family. This source extends that same vendor's platform
    documentation to a third product surface — persistent connection
    hosting — and is the first corpus note to document Active CPU pricing
    (mentioned only in passing, without mechanism detail, in the other two
    notes) applied specifically to an idle-vs-active billing split for a
    long-lived connection, rather than a request/response invocation.
  - `blog-simonwillison-openai-webrtc-document-context.md` Claim 2
    (OpenAI's Realtime API: a 60-second ephemeral token to initiate a
    session that then "will last for up to 30 minutes"): both sources
    describe a *bounded-lifetime* real-time connection model for AI
    streaming, but at different layers and with different numbers — OpenAI
    bounds the model-side voice session itself (30 minutes, fixed, not
    configurable by the caller); this source bounds the *hosting
    function's* duration (300s Hobby / up to 1800s beta on Pro+Enterprise,
    configurable by the deployer). A team building a browser-to-agent
    streaming architecture on Vercel that also calls OpenAI's Realtime API
    would need to reason about both ceilings independently — whichever is
    shorter determines when the end-to-end session is forced to reconnect.

- **Novel**:
  - **A serverless/FaaS platform natively hosting persistent, instance-pinned
    WebSocket connections with connection lifetime tied to the platform's
    general Function-duration limits** (Claims 2, 4): no prior corpus source
    documents a serverless compute platform offering managed WebSocket
    hosting with this specific architecture (connection pinned to one
    instance; lifetime bounded by the same duration ceiling as ordinary
    request/response invocations, not a separate connection-specific limit).
  - **Idle-time-free billing for a persistent connection primitive** (Claim
    3): "billing only applies to the time your Function spends processing
    messages, not idle connection time" is a new pricing-model detail for
    this corpus — the closest prior analog (`blog-vercel-ai-gateway-api-key-budgets.md`)
    covers dollar-denominated spend caps on LLM API traffic, not a
    connection-duration-vs-active-processing billing distinction.
  - **Forced-ephemerality-by-design for reconnect/deployment-split behavior**
    (Claim 5): the explicit guidance that new connections may land on a
    different instance or a different deployment than prior connections,
    with external-store state as the stated mitigation, is a new
    operational pattern for this corpus's coverage of real-time AI
    application architecture.
  - **Socket.IO long-polling-fallback incompatibility with per-instance-pinned
    serverless WebSocket routing** (Claim 10): a new, concrete
    framework-configuration gotcha not documented elsewhere in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Vercel's native WebSocket
  Functions as a concrete, managed deployment option for real-time AI
  streaming harnesses (chat UIs, agent-to-browser streaming, collaborative
  AI tools) — corroborating the platform-choice conclusion (though not the
  WebRTC-critique reasoning) already in `blog-simonwillison-luke-curley-webrtc.md`
  Claim 8. Explicitly carry forward the constraint the changelog itself
  omits: connection lifetime is capped by the hosting Function's maximum
  duration (300s on Hobby; up to 800s GA or 1800s beta on Pro/Enterprise —
  Claim 4), so any AI streaming session expected to run longer than that
  must be designed around forced disconnection from the start — client-side
  reconnect-with-backoff (the docs' own snippet, in Concrete Artifacts) and
  externalized session/conversation state (Claim 5), not an assumption of
  one unbroken channel for the life of a user's session.

- **Chapter 02 (Harness Engineering)**: Add the Socket.IO
  `transports: ['websocket']` requirement (Claim 10) as a specific,
  easy-to-miss configuration detail for teams building AI chat/streaming
  UIs on Vercel with Socket.IO — the library's default long-polling
  fallback does not work against Vercel's per-instance-pinned connection
  model, and the failure mode is not self-explanatory from the error
  behavior alone.

## Extraction Notes

1. **WebFetch output verified against raw HTML/markdown, not trusted
   directly.** An initial WebFetch pass on the changelog gave an accurate
   paraphrase but not verbatim text (per MINER.md §2a's caution). This note
   instead retrieved the changelog's raw HTML via `curl`, located the
   article body inside the page's embedded Next.js RSC/Contentful richtext
   JSON payload, and extracted the exact prose and code block from there.
   The linked `/docs/functions/websockets` and `/docs/functions/limitations`
   pages were fetched both via WebFetch and via direct `curl` against each
   page's markdown alternate (`Accept: text/markdown`, which these Vercel
   docs pages expose at their canonical URL); the two outputs were
   diffed and found byte-identical, confirming the WebFetch output for
   those two pages was not paraphrased. Every `Quote` field in this note
   is taken from one of these directly-fetched raw sources.
2. **Two linked pages followed, per MINER.md §1.** `/docs/functions/websockets`
   (the changelog's own "documentation" link) was followed in full, since
   it holds nearly all mechanism detail. `/docs/functions/limitations` was
   also followed specifically because both the changelog and the
   WebSockets doc page state only that WebSocket connections "follow the
   same limits" as other Function invocations without giving numbers, and
   the Prospector's triage comment named the actual duration/size limits as
   the "key question" for this source — the limitations page's `#max-duration`
   table was the only place those numbers appear.
3. **No message-size or per-instance concurrent-connection-count limit
   found anywhere in the source family.** The Prospector's triage question
   asked about "message size caps" specifically; neither the changelog,
   the WebSockets docs page, nor the limitations page states one. This
   should be treated as an open gap, not as evidence that no such limit
   exists — Vercel Functions have general request/response payload-size
   limits (bundle size, memory) documented on the limitations page, but
   none of the concrete artifacts on that page were labeled as applying to
   in-flight WebSocket message payloads specifically, so none are asserted
   as a WebSocket-specific message-size limit in this note.
4. **A hidden, non-malicious Contentful CMS artifact was found and
   decoded, not a prompt injection.** The changelog page's embedded JSON-LD
   author metadata contains a ~430-character run of zero-width Unicode
   characters (U+200B/U+200C/U+200D/U+FEFF) appended to one author's
   `jobTitle` field. Decoded as base-4 digits (one byte per 4 characters),
   it resolves to `{"origin":"contentful.com","href":"/api/blog/edit?...","type":"text","data":"role"}`
   — a known Contentful "live preview" / inspector-mode edit-link encoding
   used by their visual-editing tooling, not an attempt to inject
   instructions into content an LLM might read. Flagging this for
   transparency per the standing instruction to surface suspected prompt
   injection; it had no effect on this extraction, since none of the
   quoted content in this note comes from that field.
5. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts.
6. **Confidence calibration: emerging.** Individual claims are rated
   "settled" because they are unambiguous, first-party descriptions of a
   shipping/beta feature's documented mechanics (duration table, pricing
   rule, code-level requirements), verified against directly-fetched raw
   sources rather than an AI-summarized intermediate. The note's overall
   confidence is "emerging" rather than "settled" because: (a) the
   headline feature itself is explicitly Public Beta with no GA date
   given; (b) the 1800-second extended-duration tier that would matter
   most for long AI streaming sessions is itself still in beta and
   runtime-version-restricted; and (c) no named customer, production
   deployment, or independent benchmark validates any of this at scale —
   every claim here is the vendor's own pre-release documentation of how
   the feature is designed to behave, not observed production behavior.
