---
source_url: https://vercel.com/changelog/bun-runtime-now-supports-large-functions-and-extended-max-duration
source_type: blog-post
title: "Bun runtime now supports large functions and extended max duration"
author: Florentin Eckl (Vercel)
date_published: 2026-08-24
date_extracted: 2026-09-22
last_checked: 2026-09-22
status: current
confidence_overall: emerging
issue: "#3613"
---

# Bun runtime now supports large functions and extended max duration

> Vercel's Bun runtime gains parity with Node.js and Python on two beta
> capabilities — uncompressed package sizes up to 5GB (from a 250MB
> standard ceiling) and function durations up to 1800s/30 minutes (from an
> 800s GA ceiling) — both gated behind Fluid compute, Pro/Enterprise plans,
> and (for duration) specific Bun runtime versions, with Secure Compute and
> Static IPs excluded during the beta.

## Source Context

- **Type**: blog-post (Vercel product changelog, `vercel.com/changelog`, a
  ~150-word entry with two embedded code samples, published August 24,
  2026). Per MINER.md §1, this note follows the changelog's own links in
  full: `/docs/functions/runtimes/bun` (the "Bun runtime" link), and both
  beta-specific documentation links the changelog names explicitly —
  `/docs/functions/limitations#large-functions-beta` and
  `/docs/functions/configuring-functions/duration#extended-max-duration-beta`.
  These three pages carry nearly all of the mechanism and eligibility
  detail the changelog itself compresses into two sentences.
- **Author credibility**: First-party Vercel changelog entry, byline
  "Florentin Eckl" (rendered directly in the page's markdown output, unlike
  some other Vercel changelog entries in this corpus where the byline is
  only recoverable from embedded metadata — see
  `blog-vercel-zero-config-node-servers.md` Extraction Notes for a
  contrasting case). Vercel operates the Functions platform and Bun runtime
  being described, so the size/duration limits, eligibility rules, and
  configuration mechanics are authoritative first-party documentation of a
  shipping beta capability, not third-party reporting. No customer,
  benchmark, or named production deployment of large Bun functions or
  extended-duration Bun functions is cited anywhere in the changelog or its
  three directly-linked pages.
- **Scope**: Covers the two beta capabilities (large functions; extended
  max duration) as they apply to the Bun runtime specifically, including
  enrollment/opt-in mechanics, the `vercel.json` and code-level
  configuration required, supported runtime-version gating, and stated
  exclusions (Secure Compute, Static IPs). Does NOT cover: benchmarked
  cold-start or execution-speed differences for large Bun functions,
  pricing for the additional package size or duration (beyond the general
  Active CPU/Provisioned Memory model already documented in
  `blog-vercel-zero-config-node-servers.md`), a GA date for either beta, or
  any comparison of Bun's large-function/extended-duration behavior against
  Node.js's or Python's beyond the shared limits table.

## Extracted Claims

### Claim 1: The Bun runtime on Vercel Functions now supports two betas — large functions (up to 5GB uncompressed package size) and extended max duration (up to 30 minutes) — that previously ran on Node.js and Python only
- **Evidence**: The changelog's opening sentence, corroborated by the Bun runtime docs page's own "Feature support" section stating both betas explicitly.
- **Confidence**: settled (first-party, unambiguous feature-availability statement, consistent across the changelog and the standing runtime docs page)
- **Quote**: "The Bun runtime on Vercel Functions now supports larger package sizes up to 5GB uncompressed and extended max duration for up to 30 minutes, two betas that previously ran on Node.js and Python only." (changelog) — "Vercel Functions using the Bun runtime support large functions with uncompressed bundles up to 5 GB and extended max duration up to 30 minutes. Both features are in beta." (`/docs/functions/runtimes/bun`)
- **Our assessment**: The framing "previously ran on Node.js and Python only" is the key scoping detail — this is a parity announcement, not a new capability class. The Functions Limits table (Claim 4) confirms large functions were already supported on `nodejs` and `python` runtimes before this change, with `bun` now added as a third supported runtime.

### Claim 2: Large functions raise the standard 250MB uncompressed package-size limit to 5GB; extended max duration raises the 800-second generally-available ceiling to 1800 seconds — both specifically for Pro and Enterprise teams
- **Evidence**: The changelog's second sentence, stating both numeric deltas directly.
- **Confidence**: settled (first-party statement of specific before/after numbers)
- **Quote**: "Large functions raise the standard 250MB package size limit to 5GB, and extended max duration raises the generally available 800-second ceiling to 1800 seconds for Pro and Enterprise teams."
- **Our assessment**: Note the asymmetry in the changelog's own wording — "for Pro and Enterprise teams" is attached grammatically only to the duration clause, but the linked limitations page's duration table (Claim 5) confirms Hobby is excluded from the extended-maximum tier entirely (no value given, just "-"), while the large-functions eligibility section (Claim 4) states no plan restriction at all — large functions is not stated anywhere as Pro/Enterprise-only, only as excluded for Secure Compute/Static IPs projects (Claim 7). This is a real asymmetry between the two betas, not just a wording artifact: duration is plan-gated, large functions on Bun is not, based on all three pages fetched for this note.

### Claim 3: Both betas require Fluid compute to be enabled
- **Evidence**: A direct prerequisite statement in the changelog, corroborated by the Functions Limits page's separate statement that large functions specifically require Fluid compute with Active CPU enabled.
- **Confidence**: settled (first-party statement of a shared prerequisite, corroborated across two pages)
- **Quote**: "Both features require Fluid compute to be enabled." (changelog) — "Large functions require fluid compute with Active CPU enabled. Fluid compute is enabled by default for new projects." (`/docs/functions/limitations`)
- **Our assessment**: This ties both betas to the same Fluid-compute prerequisite already documented for WebSockets (`blog-vercel-websocket-support-public-beta.md` Claim 9) and zero-config Node servers (`blog-vercel-zero-config-node-servers.md` Claim 5) — a project created before April 23, 2025 (the date Fluid compute became the default for new projects, per that WebSocket note) may need to explicitly enable Fluid compute before either Bun beta will work, on top of any beta-specific opt-in.

### Claim 4: New Vercel projects are automatically eligible for the large-functions beta; existing projects created before July 2026 must explicitly opt in by setting the `VERCEL_SUPPORT_LARGE_FUNCTIONS=1` environment variable and redeploying — and even in an eligible project, the beta path is only used for functions that actually exceed the standard 250MB limit
- **Evidence**: The changelog states the opt-in mechanic and cutoff date; the Functions Limits page's dedicated "Enable large functions" subsection gives the full mechanics, including the variable's dual-purpose (`1` to enable, `0` to disable) and the "only for functions that exceed the standard limit" behavior.
- **Confidence**: settled (first-party statement of a specific, dated eligibility rule with concrete configuration steps)
- **Quote**: "New projects are enrolled in the large functions beta automatically, while existing projects created before *July 2026* opt in by adding `VERCEL_SUPPORT_LARGE_FUNCTIONS=1` as an environment variable in your project settings, then redeploying." (changelog) — "New projects are eligible for large functions by default. For existing projects, opt in by setting the `VERCEL_SUPPORT_LARGE_FUNCTIONS` environment variable. The environment variable always takes precedence over the project default. Set it to `1` to enable support for large functions, or `0` to disable, for both new and existing projects. In eligible projects, Vercel only uses the large functions beta for Functions that exceed the standard bundle size limit. Functions that fit within the standard limit continue to use the standard path." (`/docs/functions/limitations`)
- **Our assessment**: The "only uses the beta path when a function actually exceeds the standard limit" detail is not in the changelog at all — it means enabling `VERCEL_SUPPORT_LARGE_FUNCTIONS=1` is safe to leave on broadly (it doesn't change behavior for functions that already fit under 250MB), which is a materially different risk profile than a project-wide behavior switch. This is also the first source in the corpus to document large functions as supported on three runtimes together (`nodejs`, `bun`, `python`, per the Limits page's "Supported runtimes" list) rather than Bun in isolation.

### Claim 5: Durations above 800 seconds must be configured per-function (in `vercel.json` or in code), not as a project-level default, and are only supported on specific runtime versions — for Bun, versions `1.x` and `1.4.x`
- **Evidence**: The changelog states the per-function requirement directly; the Configuring Maximum Duration docs page's "Extended max duration Beta" section gives the full supported-runtime-version list and the code/`vercel.json` mechanics.
- **Confidence**: settled (first-party statement of a specific configuration constraint and an explicit version allowlist)
- **Quote**: "Durations above 800 seconds are set per function in `vercel.json` rather than as a project-level default" (changelog) — "During the beta, durations above 800 seconds must be configured for each function in code or in vercel.json. Project-level defaults above 800 seconds are not supported yet. Extended max duration is supported for the following runtimes during the beta: nodejs20.x, nodejs22.x, nodejs24.x, Bun 1.x and 1.4.x, python3.12, python3.13, python3.14." (`/docs/functions/configuring-functions/duration`)
- **Our assessment**: The docs page also gives a Next.js App Router path the changelog omits entirely — for Next.js App Router functions on a supported Node.js or Bun runtime, `maxDuration` is set as an exported constant in the route file itself (`export const maxDuration = 1800;`), not only via `vercel.json`. A team running Bun through Next.js App Router (rather than the standalone `Bun.serve()` pattern the changelog's own code sample shows) would use this different configuration surface, which the changelog's single `vercel.json` example doesn't cover.

### Claim 6: For long-running request handlers held open over HTTP/2, Vercel sends connection-level `PING` frames to keep the connection alive during idle stretches; HTTP/1.1 has no equivalent mechanism, so HTTP/1.1 clients or intermediate network layers may still close idle connections, and the docs recommend streaming progress or heartbeat data as a mitigation
- **Evidence**: A dedicated callout note in the "Extended max duration Beta" section of the Configuring Maximum Duration docs page — not mentioned anywhere in the changelog itself.
- **Confidence**: settled (first-party operational caveat specific to the extended-duration beta)
- **Quote**: "For long-running request handlers that keep a client connection open over HTTP/2, Vercel sends connection-level HTTP/2 PING frames while the response is idle. HTTP/1.1 does not have an equivalent protocol frame, so HTTP/1.1 clients and intermediate network layers may still close idle connections. For those cases, stream progress or heartbeat data while work is running."
- **Our assessment**: This is a load-bearing caveat the changelog omits entirely: a 30-minute `maxDuration` configured on the Vercel side does not guarantee a 30-minute connection in practice — if the client or any intermediary network hop is HTTP/1.1, or otherwise doesn't respect HTTP/2 keepalive PINGs, the connection can still be silently dropped well before the function-side duration limit is reached. For an AI use case this would plausibly serve (e.g., a long-running agent task streaming incremental output over 10-30 minutes), an implementer relying solely on the extended `maxDuration` without also implementing application-level heartbeat/progress streaming risks a connection that looks like it should work but doesn't, depending on the client stack — a genuinely non-obvious constraint an implementer would only find by reading this specific docs page, not the changelog.

### Claim 7: During the beta, both large functions and extended max duration are unavailable for projects using Secure Compute or Static IPs
- **Evidence**: Stated once in the changelog as a shared caveat; corroborated separately for each beta in the two linked docs pages.
- **Confidence**: settled (first-party statement of a specific, named exclusion, corroborated across three pages)
- **Quote**: "During the beta, these features are unavailable on projects using Secure Compute or Static IPs." (changelog) — "Large functions are not yet supported for projects using Secure Compute or Static IPs." (`/docs/functions/limitations`) — "Secure Compute and Static IPs do not support durations above 800 seconds during the beta." (`/docs/functions/configuring-functions/duration`)
- **Our assessment**: This is the same exclusion already documented for the general extended-duration beta in `blog-vercel-websocket-support-public-beta.md` Claim 4 ("Secure Compute and Static IPs do not support durations above 800 seconds during the beta"), now confirmed to apply identically to the large-functions beta as well and to the Bun runtime specifically — a team that has adopted Secure Compute or Static IPs for network-security reasons (e.g., calling a database or internal API from an allowlisted IP) cannot combine that with either Bun beta during the beta period, a real architectural tradeoff for security-conscious deployments wanting large or long-running Bun functions.

### Claim 8: The Bun framework preset detects a project via a `Bun.serve()` call made once during module startup in a `server.ts`/`server.js` entrypoint (or `src/` equivalent), and routes incoming requests to it through a Vercel Function — the `port`/`hostname` options passed to `Bun.serve()` only apply to local development, not the public Vercel endpoint
- **Evidence**: The Bun runtime docs page's "Deploy with the Bun framework preset" section, describing the detection mechanism directly.
- **Confidence**: settled (first-party architectural/mechanism description of a shipping detection rule)
- **Quote**: "Call Bun.serve() once during module startup. Vercel uses that call to detect the server, then routes incoming requests through a Vercel Function... The port and hostname options only apply when you run the server locally. They don't configure the public endpoint on Vercel. Unix sockets and HTML imports in routes are not supported."
- **Our assessment**: This mirrors the `.listen()`-capture detection mechanism already documented for Node.js server deployment in `blog-vercel-zero-config-node-servers.md` Claim 2 — the same runtime-capture pattern (call a framework's server-start function once at module load; Vercel intercepts it) is used for Bun's `Bun.serve()` as for Node's `server.listen()`. This confirms the pattern generalizes across at least two runtimes on the platform, not just Node.js.

### Claim 9: A separate, `/api`-directory deployment model exists for Bun (`api/server.ts`, calling `Bun.serve()` in that single file) that only requires setting the `bunVersion` in `vercel.json` — it does not use the Bun framework preset, does not require a `bun.lock` file, and only routes requests for that specific `/api/server` path, unlike the framework preset which can coexist with a frontend but claims the whole project
- **Evidence**: The Bun runtime docs page's "Deploy a Bun server from `/api`" section, explicitly contrasting this path with the framework-preset path.
- **Confidence**: settled (first-party statement of a second, narrower deployment model with an explicit contrast to the first)
- **Quote**: "Create api/server.ts to deploy a native Bun server as one Vercel Function. Vercel serves the function at /api/server, so you can add it to a project that also contains a frontend... This deployment model only requires the bunVersion configuration shown above. It doesn't use the Bun framework preset or require bun.lock. Unlike the preset, it only sends requests for /api/server to this server."
- **Our assessment**: This is the Bun-runtime answer to the gap `blog-vercel-zero-config-node-servers.md` Claim 4 named for Node.js server capture — that note found that combining a captured `server.ts` with a separate frontend (e.g., Next.js) in the same project required an unelaborated product called "Services." For Bun specifically, this docs page instead describes a direct, documented mechanism (`api/server.ts`) for coexisting with a frontend in the same project, without needing to reach for Services — a materially more complete answer for Bun than what the corpus currently has for Node's general server-capture path.

### Claim 10: The Bun runtime is generally faster than Node.js for CPU-bound tasks and provides Node.js API compatibility, but the docs explicitly caveat that Node.js may still be faster for some specific operations, and recommend Node.js over Bun when a project needs automatic source maps for debugging or request metrics on the `node:http`/`node:https` modules
- **Evidence**: The Bun runtime docs page's "Performance considerations," "Feature support," and "When to use Bun" sections, stated as direct vendor guidance rather than universal claims.
- **Confidence**: emerging (a vendor's own qualified performance/tradeoff guidance, explicitly hedged with "performance varies by workload" rather than presented as a benchmark-backed universal claim)
- **Quote**: "Bun is generally faster than Node.js, especially for CPU-bound tasks. Performance varies by workload, and in some cases Node.js may be faster depending on the specific operations your function performs." / "The main differences relate to automatic source maps, bytecode caching, and request metrics on the node:http and node:https modules." / "Consider using Node.js instead if: ...You need automatic source maps for debugging [or] You need request metrics on the node:http or node:https modules."
- **Our assessment**: This is notably even-handed for vendor documentation — Vercel is not universally pitching Bun as a strict upgrade over Node.js, and names two concrete, operational reasons (debugging via source maps; request-level observability on the raw HTTP modules) a team might deliberately choose Node.js over Bun despite the raw-speed framing. For an AI-native engineering team choosing a runtime for an agent backend or tool-execution server, loss of request metrics on `node:http`/`node:https` is a concrete observability tradeoff worth weighing against Bun's CPU-bound speed and zero-config TypeScript support, not a reason to default to Bun uncritically.

## Concrete Artifacts

### Full changelog text (verbatim, `vercel.com/changelog/bun-runtime-now-supports-large-functions-and-extended-max-duration`, retrieved via the page's markdown endpoint)

```
# Bun runtime now supports large functions and extended max duration

**Published:** August 24, 2026 | **Authors:** Florentin Eckl

---

The Bun runtime on Vercel Functions now supports larger package sizes up to
5GB uncompressed and extended max duration for up to 30 minutes, two betas
that previously ran on Node.js and Python only.

Large functions raise the standard 250MB package size limit to 5GB, and
extended max duration raises the generally available 800-second ceiling to
1800 seconds for Pro and Enterprise teams. Both features require Fluid
compute to be enabled. New projects are enrolled in the large functions beta
automatically, while existing projects created before July 2026 opt in by
adding VERCEL_SUPPORT_LARGE_FUNCTIONS=1 as an environment variable in your
project settings, then redeploying. Durations above 800 seconds are set per
function in vercel.json rather than as a project-level default:

vercel.json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "server.ts": {
      "maxDuration": 1800
    }
  }
}

The server.ts entry point serves the long-running route with Bun:

server.ts
Bun.serve({
  routes: {
    "/": () => Response.json({ success: true })
  }
});

During the beta, these features are unavailable on projects using Secure
Compute or Static IPs.

Read the large functions and extended max duration documentation.

Source: https://vercel.com/changelog/bun-runtime-now-supports-large-functions-and-extended-max-duration
```

### Bun framework-preset deployment example (verbatim, `/docs/functions/runtimes/bun`)

```typescript
// server.ts
Bun.serve({
  routes: {
    '/health': () => Response.json({ status: 'ok' }),
  },
  fetch() {
    return new Response('Hello from Bun on Vercel');
  },
});
```

### Bun `/api`-directory deployment example (verbatim, `/docs/functions/runtimes/bun`)

```typescript
// api/server.ts
Bun.serve({
  fetch(request) {
    const url = new URL(request.url);

    return Response.json({
      message: 'Hello from Bun on Vercel',
      pathname: url.pathname,
    });
  },
});
```

### `bunVersion` configuration (verbatim, `/docs/functions/runtimes/bun`)

```json
// vercel.json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "bunVersion": "1.4.x"
}
```

### Node.js/Bun/Python duration limits table (verbatim, `/docs/functions/limitations#max-duration`)

```
|            | Default          | Maximum | Extended maximum        |
| ---------- | ----------------- | ------- | ------------------------ |
| Hobby      | 300s (5 minutes) | 300s (5 minutes) | -               |
| Pro        | 300s (5 minutes) | 800s    | 1800s (30 minutes) Beta  |
| Enterprise | 300s (5 minutes) | 800s    | 1800s (30 minutes) Beta  |

"The 800 second maximum is generally available for Pro and Enterprise teams.
The 1800 second extended maximum is in beta. Values above 800 seconds require
function-level configuration and are only supported for specific Node.js,
Bun, and Python runtime versions. Secure Compute and Static IPs do not
support durations above 800 seconds during the beta."

Source: https://vercel.com/docs/functions/limitations
```

### Extended max duration: Next.js App Router configuration (verbatim, `/docs/functions/configuring-functions/duration#extended-max-duration-beta`)

```typescript
// app/api/long-task/route.ts
export const maxDuration = 1800; // This function can run for a maximum of 30 minutes

export async function POST(request: Request) {
  return Response.json({ ok: true });
}
```

### Extended max duration: supported runtime-version allowlist (verbatim, `/docs/functions/configuring-functions/duration#extended-max-duration-beta`)

```
Extended max duration is supported for the following runtimes during the beta:

- nodejs20.x
- nodejs22.x
- nodejs24.x
- Bun 1.x and 1.4.x
- python3.12
- python3.13
- python3.14

Source: https://vercel.com/docs/functions/configuring-functions/duration
```

### HTTP/2 PING keepalive caveat (verbatim, `/docs/functions/configuring-functions/duration#extended-max-duration-beta`)

```
For long-running request handlers that keep a client connection open over
HTTP/2, Vercel sends connection-level HTTP/2 PING frames while the response
is idle. HTTP/1.1 does not have an equivalent protocol frame, so HTTP/1.1
clients and intermediate network layers may still close idle connections.
For those cases, stream progress or heartbeat data while work is running.

Source: https://vercel.com/docs/functions/configuring-functions/duration
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-websocket-support-public-beta.md` and
`blog-vercel-zero-config-node-servers.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited above and below was
located and confirmed against that note's own numbered `### Claim N:`
headings in document order before writing this section.

- **Corroborates**:
  - `blog-vercel-websocket-support-public-beta.md` Claim 4 (the identical
    Node.js/Python duration table: "Hobby | 300s ... Pro | 300s default,
    800s maximum, 1800s (beta) extended maximum"): this source's own copy of
    the same table (Concrete Artifacts, and Claim 5 here) now explicitly
    adds Bun as a third row-applicable runtime alongside Node.js and Python,
    and both sources independently document the same Secure Compute/Static
    IPs exclusion for durations above 800 seconds (this note's Claim 7
    corroborates that note's Claim 4's parenthetical on the same exclusion).
  - `blog-vercel-websocket-support-public-beta.md` Claim 9 (Fluid compute
    required, default for new projects since April 23, 2025): this source's
    Claim 3 states the same Fluid-compute prerequisite for both Bun betas,
    without restating the April 23, 2025 default-enrollment date itself —
    that date is carried forward from the WebSocket note rather than
    re-verified in this extraction.

- **Contradicts**: None identified. This source makes no claim that
  conflicts with any existing corpus note on Vercel infrastructure,
  runtimes, or beta-feature eligibility rules.

- **Extends**:
  - `blog-vercel-zero-config-node-servers.md` Claim 2 (Node.js server
    detection via capturing a `.listen()` call at module startup) and
    Claim 4 (combining a captured server with a separate frontend requires
    the unelaborated "Services" product): this source's Claim 8 documents
    the same runtime-capture detection pattern applied to Bun's
    `Bun.serve()` instead of Node's `server.listen()`, confirming the
    pattern generalizes across runtimes. This source's Claim 9 additionally
    gives a more complete answer than the Node.js note has for coexisting
    with a frontend in one project — Bun's `api/server.ts` path is
    documented in full, where the Node.js note could only point at the
    unelaborated "Services" product as a gap.
  - `blog-vercel-websocket-support-public-beta.md` Claim 4: extends the
    corpus's existing Node.js/Python duration-limit table to explicitly
    include Bun as a third supported runtime for both the 800s GA ceiling
    and the 1800s beta ceiling, and adds the specific Bun runtime-version
    gating (`1.x` and `1.4.x`) that note did not need to cover.

- **Novel**:
  - **The large-functions beta itself** (5GB uncompressed package size,
    Claims 1-2, 4): no prior corpus source documents Vercel's large-function
    package-size beta for any runtime — this is the first corpus note to
    cover it, via its Bun-runtime enablement.
  - **HTTP/2 PING keepalive vs. HTTP/1.1 idle-connection-drop risk for
    long-duration functions** (Claim 6): a new, concrete operational caveat
    for the extended-max-duration beta not present in
    `blog-vercel-websocket-support-public-beta.md`, which documents
    WebSocket connection lifetime limits but not this HTTP/1.1-vs-HTTP/2
    keepalive distinction for long-running HTTP request/response handlers
    specifically.
  - **`VERCEL_SUPPORT_LARGE_FUNCTIONS` environment-variable opt-in mechanic,
    including its "only affects functions that already exceed the standard
    limit" scoping** (Claim 4): a new, concrete configuration detail not
    documented elsewhere in the corpus.
  - **Vendor-stated tradeoffs for choosing Node.js over Bun** (Claim 10):
    the first corpus source to document Vercel's own hedged guidance on
    when *not* to default to Bun (loss of automatic source maps and
    `node:http`/`node:https` request metrics), distinct from the
    Bun-vs-Node.js rewrite-performance claims covered elsewhere in the
    corpus by `blog-pragmaticengineer-bun-rust-rewrite.md` and
    `blog-simonwillison-rewriting-bun-rust.md`, both of which discuss Bun's
    own internal Zig-to-Rust rewrite rather than a hosting platform's
    runtime-choice guidance for applications built on Bun.

## Guide Impact

- **Chapter 05 (Infrastructure & Deployment)**: Add Vercel's Bun runtime as
  a viable option for hosting compute-intensive agent backends or
  tool-execution servers where CPU-bound performance matters (Claim 10),
  now with beta parity to Node.js/Python on package size (5GB, Claim 2) and
  duration (1800s/30min, Claim 2). Explicitly carry forward the two
  eligibility gates the changelog compresses: large functions require no
  plan tier but do require Fluid compute and (for existing pre-July-2026
  projects) an explicit `VERCEL_SUPPORT_LARGE_FUNCTIONS=1` opt-in (Claim 4);
  extended duration is Pro/Enterprise-only and requires per-function
  `vercel.json` or in-code configuration on a supported Bun version
  (`1.x`/`1.4.x`, Claim 5) — there is no project-level default above 800s
  during the beta.
- **Chapter 05 (Infrastructure & Deployment)**: Add the HTTP/2-PING-vs-
  HTTP/1.1 caveat (Claim 6) as a specific pitfall for any team relying on
  the extended 1800s duration ceiling for a long-running streamed agent
  task — the platform-side duration limit does not guarantee the
  client-side connection survives that long if the client or an
  intermediate network layer is HTTP/1.1; recommend application-level
  heartbeat/progress streaming as the documented mitigation, not reliance
  on `maxDuration` alone.
- **Chapter 06 (Constraints & Tradeoffs)**: Add Vercel's own hedged
  Bun-vs-Node.js guidance (Claim 10) as a concrete decision point — Bun is
  not a strict upgrade; teams needing automatic source-map-based debugging
  or `node:http`/`node:https`-level request metrics should stay on Node.js
  even when Bun's CPU-bound speed would otherwise be attractive for an
  agent workload.

## Extraction Notes

1. **Changelog and all three linked docs pages verified via each page's raw
   markdown endpoint, not WebFetch summarization alone**, per MINER.md §2a.
   The changelog and `/docs/functions/runtimes/bun`,
   `/docs/functions/limitations`, and
   `/docs/functions/configuring-functions/duration` were each fetched
   directly via `curl` with `Accept: text/markdown` against their canonical
   URLs (these Vercel pages expose a markdown alternate at the same path).
   An initial WebFetch pass on the changelog was compared against this raw
   markdown and found to match closely but was not used as a quote source;
   every `Quote` field in this note is taken from the directly-fetched raw
   markdown, not a summarized intermediate.
2. **Three of the changelog's linked pages were followed, per MINER.md §1.**
   The changelog links `/docs/functions/runtimes/bun` (as "Bun runtime"),
   `/docs/functions/limitations#large-functions-beta` (as "large
   functions"), and
   `/docs/functions/configuring-functions/duration#extended-max-duration-beta`
   (as "extended max duration") — all three were fetched and read in full,
   since the changelog itself gives only the headline numbers and one
   `vercel.json`/`Bun.serve()` example, while the eligibility mechanics
   (opt-in variable, runtime-version allowlist, HTTP/2 keepalive caveat,
   plan-tier gating) live only in the linked pages.
3. **The `/docs/fluid-compute` page was also fetched** to verify the Fluid
   compute prerequisite (Claim 3) and confirm Bun is listed among Fluid
   compute's supported runtimes (`Node.js, Python, Edge, Bun, Rust`,
   per that page's "Available runtime support" section) — not quoted
   directly in a claim since the changelog and limitations page already
   state the Fluid-compute requirement for these two betas specifically,
   but used to confirm no contradiction exists between the general
   Fluid-compute runtime-support list and this source's Bun-specific
   claims.
4. **Existing Bun-related corpus notes are about Bun's own internal
   rewrite, not Vercel's hosting of it** — `blog-pragmaticengineer-bun-rust-rewrite.md`,
   `blog-simonwillison-rewriting-bun-rust.md`,
   `blog-simonwillison-bun-webview-json-api.md`, and
   `blog-simonwillison-claude-code-bun-in-rust.md` were checked by filename
   and found to concern Bun's Zig-to-Rust rewrite and Bun-as-a-local-dev-tool
   use cases, not Vercel's Bun runtime as a serverless hosting target. No
   claim in this note overlaps with or needs reconciling against those
   notes beyond the passing mention in Claim 10's "Our assessment."
5. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts.
6. **Confidence calibration: emerging.** Individual claims are rated
   "settled" (Claims 1-9) because they are unambiguous, first-party
   descriptions of a shipping-but-beta capability's documented mechanics
   (opt-in variables, version allowlists, exclusion lists), verified
   against directly-fetched raw markdown rather than a summarized
   intermediate. Claim 10 is rated "emerging" because it is explicitly
   hedged vendor guidance ("performance varies by workload") rather than a
   benchmark-backed claim. The note's overall confidence is "emerging"
   rather than "settled" because both headline capabilities this issue was
   filed to document — large functions and extended max duration — are
   themselves still in Beta with no GA date given anywhere in the source
   family, and no named customer, production deployment, or independent
   benchmark validates either capability at scale for the Bun runtime
   specifically; every claim here is the vendor's own pre-GA documentation
   of how the features are designed to behave, not observed production
   behavior.
