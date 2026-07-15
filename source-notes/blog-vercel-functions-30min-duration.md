---
source_url: https://vercel.com/changelog/vercel-functions-can-now-run-up-to-30-minutes
source_type: blog-post
title: "Vercel Functions can now run up to 30 minutes"
author: Florentin Eckl, Craig Andrews, Casey Gowrie, Tiago Ventura Loureiro (Vercel)
date_published: 2026-06-15
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: settled
issue: "#1891"
---

# Vercel Functions can now run up to 30 minutes

> Vercel Functions on Node.js/Python runtimes can now be configured to run up
> to 30 minutes (1800s) for Pro/Enterprise teams, more than 2x the previous
> 800-second general-availability ceiling — but this is a beta capability
> with real constraints (per-function config only, restricted runtime
> versions, no Secure Compute/Static IP support, and a still-unchanged 300s
> default), and Vercel's own documentation directs workloads needing truly
> unbounded duration to a separate product, Vercel Workflows, rather than to
> this feature.

## Source Context

- **Type**: blog-post (Vercel changelog entry, `vercel.com/changelog`,
  published June 15, 2026; ~1-minute read per the page's own estimate).
  Per MINER.md §1, this note also follows the changelog's only substantive
  outbound link — "Learn more about configuring max duration for Vercel
  Functions in the documentation" — to the dedicated reference page
  `vercel.com/docs/functions/configuring-functions/duration` (last updated
  July 1, 2026, i.e. after the changelog itself), which supplies most of the
  constraint-level detail in this note (runtime list, duration-limits table,
  Secure Compute exclusion, HTTP/1.1 keepalive caveat, Vercel Workflows
  pointer) that the changelog omits entirely.
- **Author credibility**: First-party Vercel changelog post, four named
  authors (Florentin Eckl, Craig Andrews, Casey Gowrie, Tiago Ventura
  Loureiro) plus a "+2" indicator of additional unnamed authors, consistent
  with Vercel's changelog byline convention seen in
  `blog-vercel-ai-gateway-api-key-budgets.md`. Vercel operates the Functions
  product being described, so the mechanics (duration ceilings, runtime
  support, billing model, configuration syntax) are authoritative first-party
  documentation of a shipping/beta platform capability, not third-party
  reporting.
- **Scope**: Covers execution-duration configuration for Vercel Functions
  specifically (the `maxDuration` setting, its ceilings by plan, and the
  beta "extended max duration" capability). Does NOT cover Vercel AI Gateway
  (a separate product; see `blog-vercel-ai-gateway-api-key-budgets.md` and
  `blog-vercel-ai-gateway-production-index-may2026.md`), Vercel Sandbox
  (covered in `blog-anthropic-claude-managed-agents-selfhosted.md`), pricing
  beyond the general Active CPU billing description, or memory/concurrency
  configuration (covered by sibling docs pages not fetched for this note).

## Extracted Claims

### Claim 1: Vercel Functions on Node.js and Python runtimes now support execution durations up to 30 minutes for Pro and Enterprise teams, more than double the previous 800-second limit
- **Evidence**: Direct statement in the changelog's opening paragraph, with the exact prior ceiling (800 seconds) and prior beta-vs-GA framing corroborated by the linked reference page's "Duration limits" table (Concrete Artifacts).
- **Confidence**: settled (first-party description of a shipping/beta platform feature, with the base fact — the general-availability 800s ceiling being superseded by an 1800s beta ceiling — corroborated across both the changelog and the reference doc)
- **Quote**: "Vercel Functions using the Node.js and Python runtimes now support execution durations up to 30 minutes for Pro and Enterprise teams, more than 2x the previous 800 second limit."
- **Our assessment**: "More than 2x" is arithmetically precise — 1800/800 = 2.25x — not a rounded marketing figure. The Prospector's triage comment guessed the prior limit was "implied 15 minutes"; the actual prior GA ceiling, confirmed directly against the reference doc, is 800 seconds (13.3 minutes), and the *new* ceiling (1800s = 30 minutes) is what's being announced. This is a meaningful ceiling increase for any serverless-deployed agent workflow that previously had to fit inside a 13.3-minute window.

### Claim 2: Vercel explicitly frames the extended duration as targeting AI workloads: long LLM reasoning and tool calls, multi-minute streaming AI responses, document/media processing, OCR, web scraping/browser automation, and complex workflow or queue-handler steps
- **Evidence**: The changelog's bulleted use-case list, presented immediately after the headline duration announcement as the rationale for the feature.
- **Confidence**: settled (first-party statement of the vendor's own stated use cases for the feature — these are asserted rationale, not measured outcomes from customers)
- **Quote**: "Use longer-running Functions for work that needs more time to finish, including: Long LLM reasoning and tool calls; AI responses that stream for several minutes; Document and media processing; OCR and extraction; Web scraping and browser automation; Complex Workflow steps or Queue handlers."
- **Our assessment**: "Long LLM reasoning and tool calls" is listed first, ahead of the more generic web-scraping/document-processing use cases — a signal that AI agent workloads are Vercel's primary framing for why this ceiling needed to move, not an incidental beneficiary. This directly targets the same problem space as `blog-anthropic-harness-long-running.md` (multi-hour agent builds) but from the infrastructure-provider side rather than the model-builder side.

### Claim 3: Fluid Compute's Active CPU billing charges only while a function's code is actively executing, and pauses while the function is waiting on I/O such as AI model calls, database queries, or third-party APIs
- **Evidence**: Direct statement in the changelog, presented as the reason long-running functions remain "cost-efficient" under Fluid Compute; independently restated (word-for-word on the billing mechanism) in the linked reference doc's "Consequences of changing the maximum duration" section.
- **Confidence**: settled (first-party billing-mechanism description, consistent across two pages of the same source family)
- **Quote**: "Fluid Compute keeps long-running work cost-efficient. Active CPU billing only applies while your code is executing, and pauses while your Function is waiting on I/O such as AI model calls, database queries, and third-party APIs."
- **Our assessment**: This is the load-bearing economic fact that makes a 30-minute ceiling practical rather than merely a bigger risk surface: an LLM-reasoning function that spends 25 of its 30 minutes waiting on model API responses is not billed for CPU time during that wait. Without this detail, a reader might assume "30-minute function" implies "30 minutes of billed compute," which the source explicitly refutes. This should be paired with any guide advice about long-running serverless AI workflows — the ceiling is a wall-clock/timeout limit, not (primarily) a cost limit.

### Claim 4: Extended max duration (above 800 seconds) is a beta capability, available only for six specific runtime versions, and can only be configured per-function — project-level defaults above 800 seconds are not yet supported
- **Evidence**: The reference doc's dedicated "Extended max duration Beta" section, naming the exact runtime list and the per-function-only configuration constraint explicitly.
- **Confidence**: settled (first-party documentation of specific, falsifiable beta constraints — an exact runtime-version list and an explicit "not yet supported" statement about project-level defaults)
- **Quote**: "Pro and Enterprise teams can set individual Vercel Functions using supported Node.js and Python runtime versions to run for up to 30 minutes. During the beta, durations above 800 seconds must be configured for each function in code or in vercel.json. Project-level defaults above 800 seconds are not supported yet." followed by the runtime list: "nodejs20.x nodejs22.x nodejs24.x python3.12 python3.13 python3.14"
- **Our assessment**: This is the single most operationally important constraint a practitioner would miss by reading only the changelog (which does not mention the runtime restriction, the per-function-only requirement, or the beta status of durations above 800s at all — the changelog presents `maxDuration = 1800` as a simple opt-in with no caveats). A team on an older Node.js runtime, or one hoping to raise the project-wide default past 800s in one dashboard edit, would hit an undocumented (from the changelog's perspective) wall without reading the reference page.

### Claim 5: Secure Compute and Static IPs do not support durations above 800 seconds during the beta
- **Evidence**: A standalone constraint sentence in the reference doc's "Extended max duration" section, immediately following the supported-runtimes list.
- **Confidence**: settled (first-party documentation of a specific product-feature incompatibility)
- **Quote**: "Secure Compute and Static IPs do not support durations above 800 seconds during the beta."
- **Our assessment**: This is a concrete, easy-to-miss incompatibility for any team that has already adopted Vercel's Secure Compute (private networking) or Static IP features for outbound calls to allowlisted internal services or partner APIs — a common pattern for AI agents that need to reach an internal database or partner API by IP allowlist. Such a team cannot combine that networking setup with the new 30-minute ceiling until the beta constraint lifts.

### Claim 6: For long-running request handlers holding a client connection open, Vercel sends HTTP/2 keepalive PING frames while the response is idle, but HTTP/1.1 has no equivalent mechanism, so HTTP/1.1 clients or intermediate network layers may still close idle connections — Vercel recommends streaming progress or heartbeat data instead
- **Evidence**: A dedicated paragraph in the reference doc, presented as guidance for functions that stay open over an HTTP connection during long executions.
- **Confidence**: settled (first-party technical guidance describing a specific protocol-level limitation and its recommended mitigation)
- **Quote**: "For long-running request handlers that keep a client connection open over HTTP/2, Vercel sends connection-level HTTP/2 PING frames while the response is idle. HTTP/1.1 does not have an equivalent protocol frame, so HTTP/1.1 clients and intermediate network layers may still close idle connections. For those cases, stream progress or heartbeat data while work is running."
- **Our assessment**: This is a subtle but important gotcha for the "AI responses that stream for several minutes" use case named in Claim 2: simply raising `maxDuration` to 1800 does not guarantee a client stays connected for the full window if the connection goes idle (e.g., during a long silent LLM reasoning phase with no token output) and the client or an intermediary is on HTTP/1.1 or otherwise doesn't respect HTTP/2 PING frames. Practitioners building long-running streaming AI endpoints on Vercel should emit periodic heartbeat/progress data rather than relying on the raised duration ceiling alone to keep the connection alive.

### Claim 7: The default maximum duration remains 300 seconds (5 minutes) for every plan tier, including Pro and Enterprise — the increase applies only to the configurable ceiling a team can opt into, not to what a function gets without explicit configuration
- **Evidence**: The reference doc's "Duration limits" table, which lists "Default: 300s (5 minutes)" for Hobby, Pro, and Enterprise alike, distinct from each tier's "Maximum" and "Extended maximum" columns (Concrete Artifacts).
- **Confidence**: settled (first-party table of exact default/maximum/extended-maximum values per plan tier)
- **Quote**: (table data extracted verbatim — see Concrete Artifacts; no single prose sentence states this claim, so no inline quote is given per MINER.md §2a's guidance to avoid splicing non-adjacent text into a fabricated quote)
- **Our assessment**: This is a detail the changelog's framing could cause a reader to miss — "Vercel Functions can now run up to 30 minutes" describes the new *ceiling*, not a new default. A function deployed with no `maxDuration` set still terminates at 300 seconds regardless of plan tier; a team must explicitly set `maxDuration` (and, per Claim 4, do so per-function rather than at the project level) to access anything beyond 300s, let alone the extended 1800s ceiling.

### Claim 8: Hobby-tier accounts have no extended-duration option at all — their maximum duration is capped at 300 seconds with no path to the 800s or 1800s ceilings available to Pro/Enterprise
- **Evidence**: The reference doc's "Duration limits" table, which lists Hobby's "Maximum" as 300s (identical to its Default) and shows no value in its "Extended maximum" column, in contrast to Pro and Enterprise, which both show "800s" as Maximum and "1800s (30 minutes) Beta" as Extended maximum.
- **Confidence**: settled (first-party table listing exact per-tier limits)
- **Quote**: (table data extracted verbatim — see Concrete Artifacts)
- **Our assessment**: This is a concrete plan-tier gate relevant to any guide advice about prototyping long-running AI agent workflows on Vercel's free/Hobby tier: the 30-minute (or even the 800-second) ceiling is unavailable there entirely, so a team validating a long-running agent pattern on Hobby before upgrading would hit the 300-second wall regardless of how they configure `maxDuration`.

### Claim 9: For workloads that need genuinely unbounded execution time, Vercel's own documentation directs teams to a different product — Vercel Workflows — which allows code to pause, resume, and maintain state for minutes to months, rather than to raising a Function's `maxDuration`
- **Evidence**: A direct pointer at the end of the reference doc's "Duration limits" section, positioned immediately after the duration-limits table as the documented alternative once a workload exceeds even the extended 1800s ceiling.
- **Confidence**: settled (first-party documentation explicitly scoping what this feature is not for, and naming the product that is)
- **Quote**: "For workloads that require unlimited execution time, use Vercel Workflows, which allow your code to pause, resume, and maintain state for minutes to months without duration limits."
- **Our assessment**: This is the most important scoping fact for guide purposes: the 30-minute extended duration is explicitly *not* Vercel's answer to unbounded agent execution — it is a wider but still-bounded ceiling for functions that need "more time," while genuinely long-running or resumable work (the kind of multi-hour-to-multi-day agent orchestration this corpus's harness-design sources describe) is meant to run on the separate Workflows product instead. A guide reader evaluating Vercel for a long-running agent deployment should treat Functions' 30-minute ceiling as an upper bound for request/response-shaped work, not as a general-purpose long-running-agent host, and should evaluate Vercel Workflows separately for anything that might need to run longer or survive a restart.

## Concrete Artifacts

### `maxDuration` configuration examples (verbatim, changelog + reference doc; both give the identical example)

```typescript
// app/api/long-task/route.ts (Next.js App Router)
export const maxDuration = 1800; // 30 minutes
export async function POST(request: Request) {
  return Response.json({ ok: true });
}
```

```json
// vercel.json (other runtimes/frameworks)
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/long-task.py": { "maxDuration": 1800 }
  }
}
```

Source: https://vercel.com/changelog/vercel-functions-can-now-run-up-to-30-minutes (both snippets appear verbatim on this page); identical snippets also appear on https://vercel.com/docs/functions/configuring-functions/duration

### Supported runtimes for extended max duration (verbatim list, reference doc)

```
nodejs20.x
nodejs22.x
nodejs24.x
python3.12
python3.13
python3.14
```

Source: https://vercel.com/docs/functions/configuring-functions/duration, "Extended max duration Beta" section

### Duration limits table (verbatim, reference doc)

| Plan | Default | Maximum | Extended maximum |
|---|---|---|---|
| Hobby | 300s (5 minutes) | 300s (5 minutes) | - |
| Pro | 300s (5 minutes) | 800s | 1800s (30 minutes) Beta |
| Enterprise | 300s (5 minutes) | 800s | 1800s (30 minutes) Beta |

Note accompanying the table: "The 800 second maximum is generally available for Pro and Enterprise teams."

Source: https://vercel.com/docs/functions/configuring-functions/duration, "Duration limits" section

### HTTP keepalive caveat (verbatim, reference doc)

```
"For long-running request handlers that keep a client connection open over
HTTP/2, Vercel sends connection-level HTTP/2 PING frames while the response
is idle. HTTP/1.1 does not have an equivalent protocol frame, so HTTP/1.1
clients and intermediate network layers may still close idle connections.
For those cases, stream progress or heartbeat data while work is running."
```

Source: https://vercel.com/docs/functions/configuring-functions/duration, paragraph following the "Extended max duration Beta" section

## Cross-References

### Cross-reference verification notes
`blog-anthropic-harness-long-running.md`, `blog-vercel-ai-gateway-api-key-budgets.md`,
`blog-vercel-ai-gateway-production-index-may2026.md`, and
`blog-anthropic-claude-managed-agents-selfhosted.md` were re-read directly
(MINER.md §4b) and the claim numbers cited below were confirmed against
each note's own numbered `### Claim N:` headings in document order before
writing this section.

- **Corroborates**:
  - `blog-vercel-ai-gateway-api-key-budgets.md` (Source Context and
    frontmatter): both notes describe first-party Vercel infrastructure
    products aimed at the same underlying customer (teams running AI
    workloads on Vercel), reinforcing that Vercel is actively building out
    multiple layers of AI-workload-specific platform capability
    (cost-governance on AI Gateway; execution-duration ceilings on
    Functions) rather than treating either as a one-off feature.

- **Contradicts**: None identified. No claim in this source materially
  opposes an existing source note's claim on the same topic (see
  **Extends** below for the one nuance worth flagging, which is a
  conditioning/scoping distinction rather than an opposing factual claim).

- **Extends**:
  - `blog-anthropic-harness-long-running.md` Claim 8 (Opus 4.6 sustains
    "coherent building for 2+ hours without intermediate checkpoints") and
    Claim 12 (that harness was built on the Claude Agent SDK, not a
    serverless deployment target): this source adds the infrastructure-side
    ceiling that a team deploying an equivalent long-running generator
    agent as a Vercel Function would face. Even after this change, Vercel
    Functions' extended maximum (1800s / 30 minutes, Claim 1) remains well
    short of the 2+ hour single-generator run Opus 4.6 demonstrated —
    meaning a Vercel-Functions-hosted deployment of that pattern would still
    need to decompose the run (or move to Vercel Workflows, Claim 9) even
    though the *model* no longer requires sprint decomposition for context
    reasons. This is a concrete, previously-undocumented-in-corpus
    illustration of infrastructure ceilings and model-capability ceilings
    moving independently: `blog-anthropic-harness-long-running.md` Claim 13
    argues harness complexity "moves" rather than shrinks as models improve;
    this source shows one concrete place it moves *to* — from
    context-management scaffolding toward infrastructure-deployment
    scaffolding (splitting a run across multiple bounded Function
    invocations, or using a different product entirely) once the model
    itself is no longer the binding constraint.
  - `blog-anthropic-claude-managed-agents-selfhosted.md` (Claim 8 and the
    provider-comparison Concrete Artifacts table): that note documents
    Vercel Sandbox as one of four self-hosted sandbox providers for
    Anthropic's Claude Managed Agents, distinct from Vercel Functions (the
    product this source covers). Together the two notes show Vercel
    offering at least two separate compute surfaces relevant to AI agent
    deployment — ephemeral sandboxed tool execution (Vercel Sandbox, VM-based,
    millisecond startup, firewall credential injection) and
    request/response serverless compute with an extended duration ceiling
    (Vercel Functions, this source) — that a team evaluating Vercel as an
    agent-hosting platform would need to choose between or combine,
    depending on whether the workload is "run untrusted/generated code"
    (Sandbox) or "run a long-lived request handler" (Functions).

- **Novel**:
  - **A quantified, per-plan-tier serverless execution-duration ceiling for
    AI workloads, with explicit beta constraints** (Claims 1, 4, 5, 7, 8):
    no existing corpus source documents specific numeric duration limits
    (300s/800s/1800s), plan-tier gating, or runtime-version restrictions for
    a serverless AI-agent deployment target — this is new infrastructure-
    constraint data for any guide section reasoning about "can I deploy a
    long-running agent as a serverless function, and for how long."
  - **The Active CPU billing pause-during-I/O-wait mechanism specifically
    tied to AI model calls** (Claim 3): while Fluid Compute's Active CPU
    billing model is not new to Vercel as a concept, no existing corpus
    source documents it in the specific context of long-running AI/LLM
    calls as the named I/O-wait case.
  - **The HTTP/1.1-vs-HTTP/2 keepalive gap for long-idle streaming
    responses** (Claim 6): a protocol-level operational detail not
    documented anywhere else in this corpus, directly relevant to any team
    building long-running streaming AI endpoints.
  - **Vercel Workflows as the documented "graduate to this when Functions'
    ceiling isn't enough" product** (Claim 9): the corpus has no prior
    source documenting Vercel Workflows' pause/resume/state-for-months
    capability or its explicit positioning relative to Vercel Functions.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Vercel Functions' extended
  30-minute duration (Claim 1) as a concrete, current serverless-deployment
  constraint for teams considering Vercel as a host for long-running agent
  workflows (LLM reasoning chains, streaming responses, tool-call loops —
  Claim 2's named use cases). Pair this immediately with Claim 9's scoping
  fact (Vercel's own docs point to the separate Vercel Workflows product for
  anything needing to exceed 30 minutes or survive a restart) so the guide
  does not imply Functions alone solves unbounded agent execution — and with
  the `blog-anthropic-harness-long-running.md` cross-reference (Extends,
  above) illustrating a specific case (a 2+ hour Opus 4.6 generator run)
  that already exceeds this infrastructure ceiling even though the model no
  longer needs sprint decomposition for its own reasons.

- **Chapter 02 (Harness Engineering)**: Add the beta constraints (Claim 4:
  restricted runtime versions, per-function-only configuration, no
  project-level default above 800s; Claim 5: incompatible with Secure
  Compute/Static IPs) as practical checklist items for any team evaluating
  this feature today — these are the kind of details that change a "yes,
  Vercel supports 30-minute functions" answer into "yes, but only for these
  six runtime versions, configured individually, and not if you also need
  Secure Compute."

- **Chapter 04 (Cost Engineering at Scale)**: Add Claim 3 (Active CPU
  billing pauses during I/O wait, including AI model calls) as a
  cost-model correction: a long-duration ceiling does not imply
  proportionally higher billed cost for AI workloads that spend most of
  their wall-clock time waiting on model responses rather than executing
  code.

- **Chapter 05 (Team Adoption)**: Add Claim 6 (HTTP/1.1 clients/intermediaries
  may close idle long-running connections despite the raised duration
  ceiling) as an implementation gotcha for teams building customer-facing
  streaming AI features — the duration ceiling and connection persistence
  are two separate concerns that must both be handled.

## Extraction Notes

1. **Fetched via direct HTTP for both pages, not WebFetch's summarized
   output.** An initial WebFetch pass on the changelog returned a
   reasonable-looking summary, but per the pattern documented in
   `blog-vercel-ai-gateway-api-key-budgets.md` and
   `blog-vercel-ai-gateway-production-index-may2026.md` (both of which
   found WebFetch paraphrasing or fabricating wording on Vercel pages), this
   note instead retrieved the changelog and its linked reference doc via
   direct `curl` requests, stripped markup with a Python script, and read
   the resulting plain text in full. Every `Quote` field in this note is
   taken from that locally-parsed verbatim text.
2. **One linked page followed, per MINER.md §1.** The changelog's only
   substantive outbound link — "Learn more about configuring max duration
   for Vercel Functions in the documentation" — points to
   `vercel.com/docs/functions/configuring-functions/duration`. That page was
   fetched and is the source of most Claims 4-9 and the duration-limits
   table; it was last updated July 1, 2026, two weeks after the changelog,
   and is treated as the more current and complete statement of the
   feature's constraints where it adds detail the changelog omits entirely
   (which is most of the beta-specific detail).
3. **No contradiction issues filed.** Cross-referenced against all Vercel,
   harness-design, and long-running-agent notes currently in the corpus;
   found no claim here that materially opposes an existing note's claim in
   a way that would drive different guide advice (see Cross-References →
   Contradicts).
4. **Confidence calibration: settled.** Nearly every claim is a first-party,
   non-interpretive description of a shipping or beta product feature's
   exact mechanics (duration ceilings, runtime support, billing model,
   protocol behavior), verified verbatim against directly-fetched raw HTML
   rather than an AI-summarized intermediate, and internally consistent
   across the changelog and reference doc everywhere they overlap. The beta
   status of the 1800s ceiling itself (Claim 4) means the *specific numeric
   ceiling and constraints* could change before General Availability — this
   is noted in the claims themselves rather than lowering the overall
   confidence rating, since the claims accurately describe the feature's
   state as documented at time of extraction (2026-07-15).
