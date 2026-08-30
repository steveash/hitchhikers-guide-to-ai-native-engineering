---
source_url: https://vercel.com/changelog/server-timing-header
source_type: blog-post
title: "Server-Timing response headers will pass through to the client"
author: Tim Caswell, Steven Salat (Vercel)
date_published: 2026-07-30
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: settled
issue: "#3060"
---

# Server-Timing response headers will pass through to the client

> A short Vercel changelog entry: starting August 10, 2026, Vercel's CDN
> stops stripping the `Server-Timing` response header and instead passes it
> through to the client, making backend metrics (e.g. database query time,
> cache hits) visible in the browser's network panel and via the
> `PerformanceServerTiming` Performance API — a default-behavior change that
> teams wanting the old stripping behavior must explicitly opt out of via a
> `vercel.json` header-delete transform.

## Source Context

- **Type**: blog-post (Vercel product changelog, `vercel.com/changelog`; a
  four-paragraph, ~90-word feature announcement with two embedded code
  blocks — one example header value, one `vercel.json` opt-out config).
- **Author credibility**: First-party Vercel changelog entry, credited to
  two named individuals (Tim Caswell, Steven Salat), verified directly in
  the page's byline markup. This is an infrastructure/CDN behavior-change
  announcement from the platform operator itself — not third-party
  reporting, and there are no customer quotes, benchmarks, or adoption
  figures anywhere in the source.
- **Scope**: Covers exactly one CDN behavior change (Server-Timing header
  pass-through) and its single documented opt-out mechanism. Does **not**
  cover: how to *set* the `Server-Timing` header from application code
  (e.g. in a Vercel Function or Edge Middleware) — the source assumes the
  application already emits the header and only addresses the CDN's prior
  stripping behavior; any security or information-disclosure guidance
  about what a team should or shouldn't put in `Server-Timing` values now
  that they reach the client by default; pricing or plan-tier
  applicability; or a rollout/migration timeline beyond the single
  August 10, 2026 cutover date.

## Extracted Claims

### Claim 1: On August 10, 2026, Vercel's CDN stops stripping the Server-Timing response header and begins passing it through to the client by default
- **Evidence**: The changelog's opening sentence, stating the effective date and the specific mechanism (CDN-level stripping) being removed.
- **Confidence**: settled (first-party, unambiguous statement of a dated infrastructure behavior change)
- **Quote**: "On August 10, 2026, Vercel's CDN will stop stripping the Server-Timing response header and begin passing it through to the client."
- **Our assessment**: This is a silent default-behavior change for every app on Vercel that already emits a `Server-Timing` header from its own code, not an opt-in feature — any such header value that was previously invisible to the client becomes client-visible on that date unless a team explicitly configures the opt-out (Claim 4). Teams should audit, before the cutover, whether their `Server-Timing` values (or any custom labels/descriptions in them) contain information they did not intend to expose to end users — the source itself does not raise this consideration.

### Claim 2: The purpose of pass-through is to let `Server-Timing` report backend metrics like database query time and cache hits, visible in the browser's network panel and as `PerformanceServerTiming` entries through the Performance API
- **Evidence**: The changelog's second paragraph, naming the two client-side surfaces (network panel, Performance API) where the data becomes visible.
- **Confidence**: settled (first-party statement of intended use and the two specific browser surfaces affected)
- **Quote**: "Use Server-Timing to report backend metrics like database query time and cache hits. These values appear in the browser's network panel and as PerformanceServerTiming entries through the Performance API."
- **Our assessment**: This positions Server-Timing as a browser-visible, human/tooling-facing latency-breakdown mechanism — distinct from server-side observability (traces, OTel spans) that only the operator sees. For an AI-native application on Vercel (e.g. one where a page's initial render depends on an LLM call), this is a mechanism to expose a coarse backend timing breakdown (e.g. `llm;dur=1200,cache;dur=4`) directly in the requesting browser's own dev tools and Performance API, without needing a separate observability backend to inspect that specific request.

### Claim 3: The example Server-Timing value format given combines multiple named, described, timed segments in one header using semicolon-delimited key-value pairs per entry
- **Evidence**: A standalone code block immediately following the purpose statement, presented as a representative example value.
- **Confidence**: settled (first-party example of the header's expected format, matching the general `Server-Timing` HTTP spec's metric-list syntax)
- **Quote**: `Server-Timing: db;desc="Database";dur=53,cache;desc="Cache";dur=4.2`
- **Our assessment**: The example encodes two metrics (`db`, `cache`) each with a human-readable `desc` and a `dur` in milliseconds — this is the standard `Server-Timing` header grammar (per the linked MDN reference), not a Vercel-specific extension. Worth preserving verbatim in the guide as a copy-pasteable example of the header shape practitioners would emit from application code.

### Claim 4: Teams that want to preserve the prior stripping behavior must add an explicit `response.headers` "delete" transform for the `server-timing` key in `vercel.json`
- **Evidence**: The changelog's third paragraph plus a complete, runnable `vercel.json` code block showing the opt-out configuration.
- **Confidence**: settled (first-party, complete, runnable opt-out configuration)
- **Quote**: "If you want to keep the current behavior, where the header is stripped from every response, you can add a transform in vercel.json:"
- **Our assessment**: The opt-out is per-project, explicit, and requires editing `vercel.json` — there is no dashboard toggle or account-level setting mentioned anywhere in the source. A team with many Vercel projects that all currently rely on implicit stripping would need to add this block to each project's `vercel.json` individually before August 10, 2026, or accept the new pass-through default.

### Claim 5: The `response.headers` "delete" transform used to opt out is a general-purpose `vercel.json` mechanism (documented on the linked "transform object definition" reference page), not a Server-Timing-specific feature
- **Evidence**: The changelog links directly to `vercel.com/docs/project-configuration/vercel-json#transform-object-definition`, a `type: reference` docs page whose own "Transform examples" section shows the identical `response.headers` + `delete` + `target.key` pattern used generically (its worked example removes a `x-custom-header` from both request and response), and whose "Transform object definition" table documents three transform types (`request.query`, `request.headers`, `response.headers`, `request.path`) and three ops (`append`, `set`, `delete`).
- **Confidence**: settled (first-party reference documentation, directly linked from the changelog, cross-checked against its own worked example)
- **Quote**: "`op` ... These specify the possible operations:- `append` appends `args` to the value of the key, and will set if missing- `set` sets the key and value if missing- `delete` deletes the key entirely if `args` is not provided; otherwise, it will delete the value of `args` from the matching key" (from `/docs/project-configuration/vercel-json#transform-object-definition`)
- **Our assessment**: This confirms the changelog's opt-out snippet is an instance of Vercel's existing, general edge-transform system (also usable for request headers, query parameters, and path rewriting) rather than a bespoke mechanism invented for this change — a practitioner who already uses `vercel.json` transforms for other header manipulation does not need to learn a new mechanism to opt out of Server-Timing pass-through.

## Concrete Artifacts

### Example Server-Timing header value (verbatim, from the changelog body)

```
Server-Timing: db;desc="Database";dur=53,cache;desc="Cache";dur=4.2

Source: https://vercel.com/changelog/server-timing-header
```

### Opt-out configuration to restore pre-August-10 stripping behavior (verbatim, from the changelog body)

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/(.*)",
      "transforms": [
        {
          "type": "response.headers",
          "op": "delete",
          "target": {
            "key": "server-timing"
          }
        }
      ]
    }
  ]
}

Source: https://vercel.com/changelog/server-timing-header
```

### General-purpose header-delete transform pattern (verbatim, from the linked `vercel.json` reference page's "Transform examples" section — not Server-Timing-specific, shown to confirm the mechanism is a pre-existing general one)

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/home",
      "transforms": [
        {
          "type": "request.headers",
          "op": "delete",
          "target": {
            "key": "x-custom-header"
          }
        },
        {
          "type": "response.headers",
          "op": "delete",
          "target": {
            "key": "x-custom-header"
          }
        }
      ]
    }
  ]
}

Source: https://vercel.com/docs/project-configuration/vercel-json#transform-object-definition
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-ai-sdk-7-release.md`, `docs-ghaw-open-telemetry-attributes.md`,
and `blog-vercel-web-analytics-cli.md` were re-read (via their full text or
their numbered `### Claim N:` heading list) during this extraction per
MINER.md §4b, and every claim number cited below was located and confirmed
against each note's own numbered claims in document order before writing
this section. A `Server-Timing`-specific text search across all files in
`source-notes/` returned no matches, confirming this topic is new to the
corpus.

- **Corroborates**: None found at the claim level — no existing corpus note
  documents client-visible backend-timing headers specifically. The closest
  thematic overlap is `blog-vercel-ai-sdk-7-release.md` Claim 10 (AI SDK 7's
  observability redesign: `@ai-sdk/otel`, Node.js tracing-channel emission)
  and `docs-ghaw-open-telemetry-attributes.md`'s full attribute inventory —
  both document *server-side* telemetry surfaces (traces/spans an operator
  configures a backend to receive), which is a different audience and
  transport than this source's *client-visible*, per-request header
  mechanism. They are complementary observability layers, not overlapping
  claims about the same mechanism.

- **Contradicts**: None identified.

- **Extends**: `blog-vercel-web-analytics-cli.md` Claim 9 ("The dashboard
  and CLI are complementary... Use `vercel metrics` for custom filtering,
  grouping, aggregations, calendar buckets, JSON output, and agent
  workflows") documents one Vercel-operator-facing telemetry surface
  (aggregate Web Analytics queryable via CLI/agent); this source documents
  a distinct, per-request, client-facing surface (a single response's own
  backend-timing breakdown, visible directly in that request's browser dev
  tools). Both extend the corpus's picture of where Vercel exposes
  performance data, but at different granularities (aggregate,
  cross-request analytics vs. single-request, client-visible timing) and to
  different audiences (an operator/agent querying historical data vs.
  whichever client is currently receiving the response).

- **Novel**:
  - **Client-visible, per-request backend-timing headers as a CDN default**
    (Claim 1): no existing corpus source documents a platform changing a
    header-stripping default such that backend timing metadata becomes
    visible to the requesting browser by default.
  - **The specific `Server-Timing` value format and its two client-side
    consumption points** (Claims 2-3): the `desc`/`dur` metric-list syntax
    and the `PerformanceServerTiming`/network-panel visibility are new to
    the corpus.
  - **The general-purpose `vercel.json` transform mechanism (`append`/
    `set`/`delete` across `request.query`, `request.headers`,
    `response.headers`, `request.path`)** (Claim 5): not previously
    documented in the corpus's Vercel coverage; this is the first source
    note to extract the transform system's operation semantics.

## Guide Impact

- **Chapter 02 (Harness Engineering) or wherever the guide discusses
  observability for AI-native web applications on Vercel**: Note this as a
  default-behavior change practitioners should audit before/around August
  10, 2026 — any Vercel-hosted app already emitting a `Server-Timing`
  header from application code (e.g., to report an LLM call's duration
  alongside a database or cache lookup) will have that data become visible
  in every client's browser dev tools starting that date, unless the
  `vercel.json` opt-out (Claim 4, Concrete Artifacts) is added first. This
  is a concrete, low-effort mechanism for surfacing a single request's
  backend timing breakdown (e.g., `llm;dur=1200,cache;dur=4`) directly to
  a developer inspecting network requests in-browser, without standing up
  a separate observability backend for that specific debugging need —
  complementary to, not a replacement for, server-side tracing/OTel setups
  like those documented in `docs-ghaw-open-telemetry-attributes.md`.

- **Chapter 06 (Security / Threat Model), if the guide covers information
  disclosure via response headers**: Flag that `Server-Timing` values are
  now client-visible by default on Vercel, so any backend metric label or
  description a team places in that header (e.g., a cache-key hint, an
  internal service name in a `desc` field) is exposed to any client that
  can see response headers, not just to the operator's own tooling — the
  source itself gives no guidance on this and the guide would be adding
  original caution not present in the changelog.

## Extraction Notes

1. **WebFetch returned an AI-summarized abstract, not verbatim text; raw
   HTML fetched and parsed instead.** An initial WebFetch pass produced a
   clean but paraphrased summary (e.g., "Vercel's CDN will cease stripping
   the Server-Timing header," which does not appear verbatim on the page —
   the actual wording is "will stop stripping"). Per MINER.md §2a, the page
   was re-fetched directly via `curl` with a browser user-agent
   (385KB raw HTML), and the article's body text was located inside an
   embedded Next.js/Contentful rich-text JSON payload in the page source
   (a `"nodeType":"document"` block containing the article's paragraphs and
   embedded code blocks as structured, unambiguous plain-text `"value"`
   fields). Every `Quote` field in this note's Claims 1-4 is copied
   character-for-character from that JSON payload, not from the WebFetch
   summary pass.
2. **One linked page followed.** Per MINER.md §1, the changelog's own
   in-text link to `/docs/project-configuration/vercel-json#transform-object-definition`
   was followed (fetched via WebFetch, ~83KB of returned Markdown) because
   it is the authoritative documentation for the exact mechanism (`op:
   "delete"`) used in the changelog's own opt-out example, and gave the
   general transform-type/op vocabulary extracted in Claim 5. The two MDN
   links in the changelog's "Related Resources" (Server-Timing header spec,
   `PerformanceServerTiming` API, and the Performance API/Server Timing
   guide) are external, non-Vercel reference material explaining the
   underlying web platform feature rather than anything Vercel-specific;
   they were not followed as separate substantive pages, since the
   changelog's own text (Claims 1-3) already states what a practitioner
   needs to know about the header's purpose and format without requiring
   the MDN specification text itself.
3. **Byline authors and publish date verified independently of WebFetch.**
   "Tim Caswell" and "Steven Salat" were located directly in the raw HTML's
   author byline markup (`aria-label="Tim Caswell"`, `aria-label="Steven
   Salat"`), and the publish date (`datePublished":"2026-07-30T08:00-04:00`)
   was located in a JSON-LD block in the same raw HTML fetch — both
   independently of the WebFetch summary pass.
4. **Source is intentionally thin; five claims reflects the source's actual
   depth, not a shortened extraction.** The changelog itself is four short
   paragraphs (~90 words) with two code blocks; there is no additional
   first-party prose, no customer/production evidence, and no discussion
   of security or information-disclosure implications of the default
   change. Claim 5 required following the one linked reference page to
   avoid treating the opt-out mechanism as unexplained boilerplate. No
   sixth or later claim was manufactured to hit a target count.
5. **No contradiction issues filed.** Cross-referenced against all
   Vercel-authored notes already in the corpus and the two
   observability/telemetry notes checked above; no claim here opposes an
   existing corpus note (see Cross-References → Contradicts).
6. **Confidence calibration: settled.** All five claims are first-party,
   unambiguous, checkable statements about a shipping CDN behavior change,
   its example header format, and its documented opt-out mechanism —
   cross-verified against the linked reference page for Claim 5. There is
   no marketing narrative, no experimental/beta caveat, and no unverified
   adoption or customer claim to discount against, so the note is rated
   "settled" overall.
