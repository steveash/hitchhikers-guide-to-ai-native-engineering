---
source_url: https://vercel.com/changelog/deploy-node-servers-with-zero-configuration
source_type: blog-post
title: "Deploy Node servers with zero configuration"
author: Ricardo Gonzalez, Jeff See (Vercel)
date_published: 2026-06-23
date_extracted: 2026-07-23
last_checked: 2026-07-23
status: current
confidence_overall: settled
issue: "#2171"
---

# Deploy Node servers with zero configuration

> Vercel now detects a raw `server.ts`/`server.js` entrypoint (any file that
> calls `.listen()`) at the project root or `src/`, and deploys it as a
> Vercel Function with no configuration file — generalizing a zero-config
> detection pattern previously limited to Express, Koa, and NestJS to any
> Node HTTP server. The linked runtime docs and pricing pages reveal the two
> load-bearing details the changelog itself omits: captured servers lose the
> `/api`-handler convenience helpers (`request.query`, `request.cookies`,
> `request.body`), and all such backends bill under Active CPU pricing,
> whose three-metric mechanics (Active CPU, Provisioned Memory, Invocations)
> are documented in a separate, earlier Vercel post this changelog links to
> only as "Fluid compute with Active CPU pricing."

## Source Context

- **Type**: blog-post (Vercel product changelog, `vercel.com/changelog`, a
  ~110-word entry with one embedded code sample; no explicit publish date is
  rendered on the page itself — the June 23, 2026 date comes from the
  Prospector's triage comment, sourced from Vercel's Atom feed metadata,
  `https://vercel.com/atom`). Per MINER.md §1, this note follows all three
  links the changelog itself provides inline: `/docs/functions/runtimes/node-js`
  (linked twice, as "Node.js server" and "Node.js runtime on Vercel"),
  `/fluid` (linked as "Fluid compute"), and `/blog/introducing-active-cpu-pricing-for-fluid-compute`
  (linked as "Active CPU pricing"). The last of these was followed because
  the changelog's one pricing sentence ("Backends on Vercel are powered by
  Fluid compute with Active CPU pricing") gives no mechanism or numbers
  itself, and that dedicated pricing post — directly linked from the
  changelog, not a page found one level deeper — is the only place in the
  source family where the actual rates and billing metrics appear.
- **Author credibility**: First-party Vercel changelog entry, byline
  "Ricardo Gonzalez, Jeff See" (extracted from the page's embedded author
  metadata; not stated in the visible article body itself). Vercel operates
  the platform and runtime being described, so the detection mechanism,
  request/response object behavior, and pricing model are authoritative
  first-party documentation of a shipping capability, not third-party
  reporting. No customer, benchmark, or named production deployment is
  cited anywhere in the changelog or its three directly-linked pages
  (the one anonymous testimonial in Claim 9 names a job title, not a
  customer or company).
- **Scope**: Covers the detection rule for a zero-configuration Node.js
  server deployment (`server.{js,cjs,mjs,ts,cts,mts}` at project root or
  `src/`), the CLI commands that pick it up (`vc dev`, `vc deploy`), the
  request/response object differences versus Vercel's existing `/api`
  function-handler convention, and the Fluid-compute/Active-CPU pricing
  model all such backends run under. Does NOT cover: how this interacts
  with build configuration beyond package-manager lock-file detection,
  concurrent-connection or throughput limits for a captured server (the
  `/docs/functions/limitations` page was not re-fetched for this note —
  see `blog-vercel-websocket-support-public-beta.md` for those numbers,
  which apply to Functions generally), or any named customer using this
  specific capability.

## Extracted Claims

### Claim 1: Vercel now detects a standalone Node.js HTTP server entrypoint (`server.ts`/`server.js` at the project root or in `src/`) and deploys it as a Vercel Function with zero configuration files, generalizing a pattern that previously required a recognized framework
- **Evidence**: The changelog's opening two sentences, corroborated by the runtime docs page's dedicated "Deploy a Node.js server" section, which lists the exact accepted filenames.
- **Confidence**: settled (first-party, unambiguous feature description; the runtime docs page is a standing reference page rather than a beta-flagged announcement)
- **Quote**: "You can now deploy a Node.js server to Vercel with zero configuration. Vercel detects a server.ts file at the project root or at src/server.ts and deploys it as a Node.js application, in addition to existing zero-configuration backends like Express, Koa, and NestJS" (changelog); "Vercel looks for a server entrypoint in the project root or the src/ directory: server.{js,cjs,mjs,ts,cts,mts} [or] src/server.{js,cjs,mjs,ts,cts,mts}" (`/docs/functions/runtimes/node-js`)
- **Our assessment**: The changelog's own framing ("in addition to existing zero-configuration backends like Express, Koa, and NestJS") is the key scoping detail — Vercel already had zero-config detection for those three frameworks before this change. The new capability is not "zero-config deployment" itself but generalizing detection away from a fixed framework allow-list to any code that calls `.listen()` (Claim 2), which is a materially different (and broader) detection mechanism.

### Claim 2: Detection works by capturing the `server.listen()` call during module startup and routing requests to the server through an internal port — the port number passed to `.listen()` is only meaningful for local development and does not expose a public port on Vercel
- **Evidence**: A direct mechanism description on the runtime docs page, the first technical detail beyond the changelog's announcement text.
- **Confidence**: settled (first-party architectural/mechanism description of a shipping detection rule)
- **Quote**: "Call server.listen() during module startup. Vercel uses that call to detect the HTTP server, then routes incoming requests to the server through an internal port. The port you pass to listen() is only used when you run the file locally and does not expose a public port on Vercel."
- **Our assessment**: This is the load-bearing mechanism the "zero configuration" framing rests on — detection is a runtime capture of the `.listen()` call, not a build-time config flag or framework-specific adapter. Practically, this means any code path that eventually calls `.listen()` on an HTTP server object qualifies, regardless of what routes to it internally, which is why Express/Koa/NestJS (all of which call `.listen()` under the hood) already worked before this change and a raw `node:http` server now works identically.

### Claim 3: Node.js servers captured via this mechanism receive plain Node.js `IncomingMessage`/`ServerResponse` objects and do NOT receive the convenience helper properties (`request.query`, `request.cookies`, `request.body`) that Vercel adds to its existing `/api`-directory function handlers
- **Evidence**: An explicit contrast statement on the runtime docs page, placed directly after the server-capture code example.
- **Confidence**: settled (first-party statement of a specific, easy-to-miss behavioral difference between two deployment conventions on the same platform)
- **Quote**: "Captured Node.js servers receive standard Node.js IncomingMessage and ServerResponse objects. They do not include the helper properties added to /api function handlers, such as request.query, request.cookies, and request.body."
- **Our assessment**: This is a concrete migration gotcha the changelog itself never mentions: a team moving an existing `/api/*.ts` handler (which relies on Vercel's `request.query`/`request.cookies`/`request.body` helpers, themselves documented later on the same page) into a captured `server.ts` will lose those helpers silently unless they bring their own parsing (e.g., via Express or manual `URL`/body parsing, as shown in the docs' own `server.ts` example, which manually constructs a `URL` from `request.url` and `request.headers.host`). This directly answers the Prospector's "key question" about how the new model differs from the existing Function-based model: the difference isn't just deployment detection, it's a different request/response object shape.

### Claim 4: To deploy a captured Node.js server alongside a separate frontend framework (e.g., a Next.js app) within the same Vercel project, teams must use a different product — Services — rather than the server-capture pattern directly
- **Evidence**: A single scoping sentence on the runtime docs page, placed immediately after the request/response-object distinction.
- **Confidence**: settled (first-party statement of a scope boundary for the feature)
- **Quote**: "To deploy a Node.js server alongside a frontend such as a Next.js app within the same project, use Services."
- **Our assessment**: This caps the "zero configuration" framing to a single-backend-per-project scenario. A common real-world shape — a Next.js frontend plus a standalone Node API server in the same repo/project — is explicitly routed to a different, unelaborated product (Services) rather than being solved by server capture itself; this source does not describe how Services works, so it should be treated as a named gap, not a documented capability.

### Claim 5: Node.js server deployments run on Fluid compute under Active CPU pricing, meaning teams are billed only for the time the server actively uses CPU, not for the time it sits idle waiting on I/O
- **Evidence**: The changelog's closing sentence, expanded with mechanism and numbers on the separately-linked Active CPU pricing post.
- **Confidence**: settled (first-party pricing-model statement, corroborated with concrete rates in a dedicated pricing announcement)
- **Quote**: "Backends on Vercel are powered by Fluid compute with Active CPU pricing." (changelog) — "You pay CPU rates only when your code is actively using CPU." (`/blog/introducing-active-cpu-pricing-for-fluid-compute`)
- **Our assessment**: For a Node backend serving an AI workload (an agent's tool-execution API, an MCP server, an inference proxy) with bursty, I/O-bound request patterns, this is a materially different cost model from a dedicated always-on process billed by wall-clock uptime — the server can sit "warm" between requests without accruing CPU charges during the idle stretches. This corroborates and extends `blog-vercel-websocket-support-public-beta.md` Claim 3, which documents the same idle-time-free billing applied to persistent WebSocket connections specifically, but without the rate/mechanism detail this source's linked pricing post supplies (Claim 6-7 below).

### Claim 6: Active CPU pricing charges three separate, independently-metered dimensions — Active CPU time (~$0.128/hour), Provisioned Memory (~$0.0106/GB-hour, described as "less than 10% of Active CPU" rate), and per-invocation count — replacing a flat memory-allocation-times-wall-time charge
- **Evidence**: A dedicated "The Active CPU pricing model" section on the linked pricing post, enumerating each metric with its definition and starting rate.
- **Confidence**: settled (first-party pricing documentation with specific numeric rates)
- **Quote**: "Active CPU reflects the compute time your code is actively executing on a virtual CPU (vCPU)... Pricing starting at at $0.128 per hour" / "Provisioned Memory covers the memory required to keep a function alive while it's running... billed at a much lower rate (less than 10% of Active CPU)... Pricing starting at at $0.0106 per GB-Hour" / "Invocations are counted per function call (just like in traditional serverless) and remain part of the overall pricing"
- **Our assessment**: This is the concrete mechanism behind the changelog's one-line pricing claim (Claim 5) — a practitioner estimating the cost of running a Node backend for an agent workload on Vercel needs these three rates, not just the qualitative "pay for what you use" framing. The worked example in the same post ("A function running on a Standard machine size at 100% active CPU would now cost ~$0.149 per hour... Previously, this would have cost $0.31842 per hour") gives a concrete before/after comparison for a fully-CPU-saturated function — the savings case is strongest for idle-heavy workloads, not this saturated-CPU example, which the post itself frames as illustrating the new metric structure rather than the headline savings case.

### Claim 7: Vercel states Fluid compute was already the default AI compute model on its platform prior to Active CPU pricing, powering "over one trillion invocations" and delivering "up to 90% cost savings" through shared compute across concurrent workloads, before Active CPU pricing was layered on top for further idle-time savings
- **Evidence**: The pricing post's "From serverless to Fluid compute" section, presented as background/context for why Active CPU pricing was introduced.
- **Confidence**: emerging (vendor-reported adoption and savings figures with no independent verification or named customer breakdown; the underlying mechanism — sharing compute across concurrent invocations — is architecturally coherent, but the specific percentages are unverified vendor claims)
- **Quote**: "Fluid became the default for AI on Vercel, powering over one trillion invocations. Teams saw up to 90% cost savings by sharing compute across workloads intelligently."
- **Our assessment**: "Over one trillion invocations" is presented without a time window or customer breakdown, and "up to 90%" is a best-case figure, not a typical or median outcome — both should be read as marketing-scale claims that establish Fluid's adoption is real and large, not as a specific, reproducible savings guarantee for any given workload.

### Claim 8: Fluid compute's core mechanism is running multiple concurrent invocations on a single warm instance rather than spinning up a dedicated instance per request, which the vendor states eliminates cold starts and reuses otherwise-idle time
- **Evidence**: Direct architectural description on both the Fluid compute marketing page and the pricing post.
- **Confidence**: settled (first-party architectural description of the platform's shipping compute model, consistent across two separate pages from the same vendor)
- **Quote**: "Fluid runs many requests on a single instance and bills only the CPU you actually use, never the time spent waiting... Fluid runs invocations concurrently. Overall cloud resources provisioned are dramatically reduced while invocations are kept alive in-memory." (`/fluid`) — "Instead of spinning up a separate instance for each invocation, Fluid compute intelligently orchestrates compute across invocations. Multiple concurrent requests can share the same underlying resources, eliminating cold starts and reusing idle time." (pricing post)
- **Our assessment**: This is the underlying mechanism claim that both the idle-time-free billing (Claim 5) and the cold-start elimination depend on — a single instance handling multiple concurrent requests only works for workloads where the runtime can safely interleave execution (I/O-bound work waiting on external calls, which the pricing post explicitly names AI inference and agent workloads as examples of, not CPU-bound work that would contend for the same vCPU).

### Claim 9: An unnamed customer ("Lead Fullstack developer," no company identified) is quoted claiming in-function concurrency cut their compute costs by over 50% "with zero code changes"
- **Evidence**: A pull-quote on the Fluid compute marketing page, attributed only to a job title, not a name or company.
- **Confidence**: anecdotal (single, anonymous, unattributable testimonial — no company name, no way to independently verify the workload, baseline, or measurement methodology)
- **Quote**: "By leveraging in-function concurrency, we were able to share compute resources between invocations, cutting costs by over 50% with zero code changes." — Lead Fullstack developer
- **Our assessment**: This carries far less evidentiary weight than the named, attributed customer testimonials documented elsewhere in the corpus (e.g., Brex/Money Forward/Notion in `blog-cursor-self-hosted-cloud-agents.md`) — there is no company, no name, and no way to check the claim against any other source. Treat as illustrative marketing copy, not as independent validation of the "up to 90%" or "over 50%" savings figures elsewhere in this source family.

## Concrete Artifacts

### Full changelog text (verbatim, `vercel.com/changelog/deploy-node-servers-with-zero-configuration`)

```
You can now deploy a Node.js server to Vercel with zero configuration.
Vercel detects a server.ts file at the project root or at src/server.ts and
deploys it as a Node.js application, in addition to existing
zero-configuration backends like Express, Koa, and NestJS:

// server.ts
import { createServer } from 'node:http'

const server = createServer((req, res) => {
  res.end('Hello from Node.js on Vercel!')
})

server.listen(process.env.PORT ?? 3000)

Vercel CLI can handle local development and deployment:

# Run the server locally
vc dev

# Create a deployment
vc deploy

Both commands pick up server.ts automatically, with no configuration files
required.

Backends on Vercel are powered by Fluid compute with Active CPU pricing.
Learn more about the Node.js runtime on Vercel.

Authors: Ricardo Gonzalez, Jeff See
```

### Server entrypoint detection rules and fuller example (verbatim, `/docs/functions/runtimes/node-js`)

```
Vercel looks for a server entrypoint in the project root or the src/
directory:
  server.{js,cjs,mjs,ts,cts,mts}
  src/server.{js,cjs,mjs,ts,cts,mts}

// server.ts
import { createServer } from 'node:http';

const server = createServer((request, response) => {
  const url = new URL(
    request.url ?? '/',
    `http://${request.headers.host ?? 'localhost'}`
  );

  if (request.method === 'GET' && url.pathname === '/health') {
    response.writeHead(200, { 'Content-Type': 'application/json' });
    response.end(JSON.stringify({ status: 'ok' }));
    return;
  }

  response.writeHead(200, { 'Content-Type': 'text/plain' });
  response.end('Hello from Node.js on Vercel');
});

server.listen(Number(process.env.PORT ?? 3000));

To use ES modules in JavaScript, name the file server.mjs or set "type":
"module" in package.json.

Other Vercel Function formats, such as a Web Handler (GET, POST, and other
method exports), the fetch Web Standard export, or a Node.js (request,
response) handler, do not need server.listen().

Source: https://vercel.com/docs/functions/runtimes/node-js
```

### Active CPU pricing model and worked example (verbatim, `/blog/introducing-active-cpu-pricing-for-fluid-compute`)

```
Fluid compute now charges based on three key metrics, each designed to
reflect actual resource usage:

Active CPU reflects the compute time your code is actively executing on a
virtual CPU (vCPU). It's measured in milliseconds, calculated as the number
of vCPUs allocated multiplied by the time they're actively used. Pricing
starting at at $0.128 per hour

Provisioned Memory covers the memory required to keep a function alive
while it's running. It's measured in GB-hours and billed at a much lower
rate (less than 10% of Active CPU), thanks to Fluid's ability to reuse
memory across multiple concurrent invocations. Pricing starting at at
$0.0106 per GB-Hour

Invocations are counted per function call (just like in traditional
serverless) and remain part of the overall pricing

This pricing model in action:
A function running on a Standard machine size at 100% active CPU would now
cost ~$0.149 per hour (1 Active CPU GB-Hour + 2 GB of provisioned memory).
Previously, this would have cost $0.31842 per hour (1.7 GB Memory ×
$0.18).

Source: https://vercel.com/blog/introducing-active-cpu-pricing-for-fluid-compute
```

### Servers vs. Serverless vs. Fluid comparison table (verbatim, `/fluid`)

```
Features          | Servers               | Serverless             | Fluid
------------------|------------------------|-------------------------|---------------------------
Cold start handling | Not applicable       | Cold starts             | Cold-start prevention
Scaling           | Manual scaling         | Auto-scaling            | Efficient auto-scaling
Concurrency       | Horizontal             | Vertical                | Horizontal & vertical
Operational overhead | High maintenance    | Minimal, inefficient    | Minimal, optimized
Pricing model     | Upfront cost per server | Pay-as-you-go model    | Pay-as-you-compute
CPU efficiency    | High efficiency        | I/O bound inefficiency  | Optimized I/O efficiency

Source: https://vercel.com/fluid
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-websocket-support-public-beta.md`, `blog-vercel-enterprise-apps-and-agents.md`,
and `blog-cursor-self-hosted-cloud-agents.md` were re-read in full during
this extraction (MINER.md §4b), and every claim number cited below was
located and confirmed against that note's own numbered `### Claim N:`
headings in document order before writing this section.

- **Corroborates**:
  - `blog-vercel-websocket-support-public-beta.md` Claim 3 ("WebSocket
    connections... follow the same limits and pricing as other Function
    invocations. With Active CPU pricing, billing only applies to the time
    your Function spends processing messages, not idle connection time"):
    that note documents the same idle-time-free billing principle applied
    to persistent WebSocket connections specifically, but explicitly did
    not have rate or mechanism detail beyond the qualitative billing rule.
    This source's Claim 6 (the three-metric breakdown: Active CPU
    $0.128/hour, Provisioned Memory $0.0106/GB-hour, Invocations) is the
    first corpus documentation of the actual numbers behind that shared
    billing model — both notes describe the same underlying pricing
    system, at different levels of mechanism detail.

- **Contradicts**: None identified. This source makes no claim that
  conflicts with any existing corpus note on Vercel infrastructure, pricing,
  or deployment models.

- **Extends**:
  - `blog-vercel-websocket-support-public-beta.md`: extends that note's
    passing mention of Active CPU pricing into the full three-metric
    pricing model with concrete rates and a worked cost example (Claim 6),
    and extends the "Fluid compute" infrastructure family this corpus has
    now documented for two separate product surfaces (WebSocket connection
    hosting; standalone Node server hosting) to a third: zero-configuration
    detection of a raw Node HTTP server as a deployable unit, independent of
    any specific framework (Claim 1-2).
  - `blog-vercel-enterprise-apps-and-agents.md`: that note documents
    identity/access/credential governance products (Passport, Connect,
    Enterprise Managed Users, BYOC) for apps and agents deployed on Vercel;
    this source documents a different layer of the same platform — how a
    backend process itself gets detected and deployed, and how it is
    billed — neither note's claims overlap or conflict, but both describe
    infrastructure a team would need to reason about when choosing Vercel
    to host an agent's backend/tool-execution server.
  - `blog-cursor-self-hosted-cloud-agents.md`: that note documents an
    inference-cloud/execution-on-prem split for coding agents, where a
    self-hosted worker process is the customer-controlled execution
    surface. This source is unrelated to that split (it describes a
    fully Vercel-hosted server, not a customer-premises worker), but is
    relevant to the same general question of "where does an agent's
    backend/tool-execution process run and what does it cost" — a team
    evaluating Vercel-hosted vs. self-hosted execution for an agent backend
    would weigh this source's Active CPU pricing model against Cursor's
    self-hosted-worker cost-avoidance model as two different answers to a
    similar infrastructure question.

- **Novel**:
  - **Runtime detection of a raw `.listen()` call as the zero-configuration
    trigger, independent of any framework** (Claims 1-2): no prior corpus
    source documents a serverless/FaaS platform detecting an arbitrary Node
    HTTP server by capturing its `server.listen()` call at runtime, as
    distinct from framework-specific adapters (Express, Koa, NestJS) or a
    build-time configuration file.
  - **Explicit request/response object degradation when moving from a
    platform's convenience-handler convention to a captured raw server**
    (Claim 3): a new, concrete migration gotcha not documented elsewhere in
    the corpus — moving from Vercel's `/api`-handler convention to a
    captured `server.ts` silently drops `request.query`/`request.cookies`/
    `request.body` helpers.
  - **The three-metric Active CPU pricing breakdown with specific rates and
    a worked before/after cost comparison** (Claim 6): the first corpus
    source to give concrete dollar figures ($0.128/hour Active CPU,
    $0.0106/GB-hour Provisioned Memory, and a $0.149-vs-$0.31842-per-hour
    worked example) for Vercel's Fluid compute billing model.

## Guide Impact

- **Chapter 02 (Harness Engineering / Infrastructure)**: Add zero-config
  `server.ts` deployment (Claim 1-2) as a concrete, low-friction option for
  hosting an agent's backend/tool-execution HTTP server (e.g., an MCP
  server, an agent-to-browser streaming endpoint, a webhook receiver) on
  Vercel without adopting a specific framework or writing a Vercel-specific
  handler — any code that calls `.listen()` qualifies. Pair this with the
  request/response-object gotcha (Claim 3): teams migrating an existing
  `/api`-handler-based agent backend to a captured `server.ts` will lose
  `request.query`/`request.cookies`/`request.body` and need to handle
  parsing themselves (as the docs' own example does, manually constructing
  a `URL` from `request.headers.host`).

- **Chapter 04 (Cost Engineering at Scale)**: Add the three-metric Active
  CPU pricing breakdown (Claim 6: $0.128/hour Active CPU, $0.0106/GB-hour
  Provisioned Memory, per-invocation charges) as concrete reference numbers
  for estimating the cost of running an I/O-bound AI backend (agent
  orchestration, inference proxying, MCP servers) on Vercel — the pricing
  model is explicitly designed to reward idle-heavy, bursty workloads like
  AI inference (Claim 7's "high idle time, like AI inference" framing) over
  CPU-saturated ones, which should inform whether Vercel's compute model is
  a good cost fit for a given agent-backend workload shape versus a
  dedicated always-on server or a self-hosted execution model (see
  `blog-cursor-self-hosted-cloud-agents.md`).

## Extraction Notes

1. **Changelog page verified via raw HTML, not WebFetch summarization
   alone**, per MINER.md §2a. The changelog's `<article>` HTML was fetched
   directly via `curl` and stripped of markup with a plain-text extraction
   pass; the resulting ~110-word article text was compared against the
   Prospector's triage summaries and matches. All three linked pages
   (`/docs/functions/runtimes/node-js`, `/fluid`,
   `/blog/introducing-active-cpu-pricing-for-fluid-compute`) were fetched
   and extracted the same way. Every `Quote` field in this note is taken
   from one of these directly-fetched raw HTML sources, not from a
   summarized intermediate.
2. **All three of the changelog's own linked pages were followed, per
   MINER.md §1.** The changelog contains three distinct outbound links
   (`/docs/functions/runtimes/node-js`, linked twice; `/fluid`;
   `/blog/introducing-active-cpu-pricing-for-fluid-compute`) — all were
   fetched and read in full. The Active CPU pricing post was followed
   specifically because neither the changelog's pricing sentence ("Fluid
   compute with Active CPU pricing") nor the `/fluid` marketing page itself
   gives concrete rates — the dedicated pricing post was the only place in
   the source family where the three-metric breakdown and dollar figures
   (Claim 6) appear.
3. **No author byline is visible in the changelog's rendered article text.**
   "Ricardo Gonzalez, Jeff See" was recovered from the page's embedded
   author-metadata block (a Twitter/X profile link with `rel="author"`
   attributes near a byline element), not from the visible changelog prose
   itself, which is unsigned. Flagging this so the Assayer can verify the
   byline extraction independently if needed.
4. **No numeric limits (concurrent connections, request size, execution
   duration) were re-verified for this specific feature.** The
   `/docs/functions/limitations` page was not re-fetched for this note,
   since `blog-vercel-websocket-support-public-beta.md` already documents
   the general Function duration-limit table (300s Hobby / up to 1800s
   Pro-Enterprise beta) that would apply to any Vercel Function, including
   a captured Node server; this note does not repeat those figures to avoid
   re-asserting an unverified-for-this-context claim, and points to that
   note instead.
5. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts.
6. **Confidence calibration: settled.** Individual claims are rated
   "settled" (Claims 1-6, 8) because they are unambiguous, first-party
   descriptions of already-shipped, non-beta capabilities (neither the
   changelog nor the linked runtime docs page marks this feature "beta,"
   unlike several other Vercel features documented elsewhere in the corpus
   — e.g., WebSockets and Enterprise Managed Users, both explicitly
   Beta/Private Beta), verified against directly-fetched raw HTML. Claim 7
   is rated "emerging" (unverified, best-case adoption/savings figures) and
   Claim 9 "anecdotal" (a single anonymous, unattributable testimonial).
   The note's overall confidence is "settled" because the core capability
   this issue was filed to document — zero-config server detection and its
   concrete behavioral differences from the existing `/api`-handler model —
   rests entirely on unambiguous, non-beta, first-party technical
   documentation; the two lower-confidence claims (7, 9) are supporting
   context from a linked page, not the source's central contribution.

