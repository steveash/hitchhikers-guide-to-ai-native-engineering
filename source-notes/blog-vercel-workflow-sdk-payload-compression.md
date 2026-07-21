---
source_url: https://vercel.com/changelog/workflow-sdk-now-compresses-run-and-step-payloads
source_type: blog-post
title: "Workflow SDK now compresses run and step payloads"
author: Pranay Prakash (Head of Workflows, Vercel)
date_published: 2026-06-22
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: emerging
issue: "#2099"
---

# Workflow SDK now compresses run and step payloads

> Vercel's Workflow SDK 5 beta now applies zstd compression to all run,
> hook, and step inputs/outputs before persisting them, with the vendor
> quoting up to 85% storage savings for AI-conversation-shaped JSON and a
> demonstration workflow shrinking from 52 MB to 10 MB — a benefit that
> flows through automatically to eve, Vercel's durable-agent framework
> built on the same SDK, with no code changes required.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`;
  a "1 min read" feature announcement of roughly 120 words of prose plus
  two embedded before/after dashboard screenshots).
- **Author credibility**: Pranay Prakash, credited by title as "Head of
  Workflows" at Vercel (per the byline's role label and linked Twitter/X
  profile `twitter.com/pranaygp`). This is a first-party product-leadership
  announcement of a feature in the product he owns, not third-party
  reporting or independent benchmarking.
- **Scope**: Covers what compression is applied (zstd, on run/hook/step
  inputs and outputs), when it applies (automatically, only when it
  reduces size), the headline savings figure (up to 85% for AI-conversation
  JSON) with one concrete before/after example, that the benefit
  propagates to eve without code changes, and the SDK version required
  (`workflow@5.0.0-beta.19`+). Does **not** cover: the compression level or
  any tuning parameters, whether/how compression interacts with
  pause-and-resume durability (does a paused workflow's persisted state
  get decompressed transparently on resume, or does resume logic need to
  account for it?), any added CPU/decompression latency, dollar-cost
  pricing impact, a GA/stable-release timeline (the SDK is at v5 beta), or
  any named customer or production-scale deployment. This gap matters
  because one of the three Prospector triage comments on this issue named
  exactly this ("how compression interacts with step-state serialization
  and resumability") as the "key question" this source would need to
  answer to justify a medium/high-priority extraction — it does not answer
  it, and neither of the two linked docs pages I followed (see Extraction
  Notes) fill that gap either.

## Extracted Claims

### Claim 1: Workflow SDK 5 beta now compresses all run, hook, and step inputs and outputs using zstd
- **Evidence**: The changelog's opening sentence, the first substantive content on the page.
- **Confidence**: settled (first-party, unambiguous feature description)
- **Quote**: "The Workflow SDK 5 beta now compresses all run, hook, and step inputs and outputs with zstd."
- **Our assessment**: This is a storage-layer (at-rest) compression feature applied to the durable-execution state Workflow SDK persists for pause/resume — a different mechanism from in-context-window compaction (see Cross-References → Novel), which manages what's fed back to the model rather than what's written to a data store.

### Claim 2: Compression is applied conditionally and automatically — small payloads are left uncompressed, larger ones are compressed before being persisted
- **Evidence**: Second sentence of the changelog, describing the activation logic.
- **Confidence**: settled
- **Quote**: "Compression kicks in automatically, but only when it helps. Small payloads stay as-is, larger ones get compressed before they're persisted."
- **Our assessment**: This is a sensible default (compression overhead isn't worth paying on tiny payloads) but the source gives no size threshold, so a practitioner can't predict from this text alone which of their own workflow payloads will actually be compressed.

### Claim 3: Compressed payloads use less storage and are faster to read/write, with the largest savings — up to 85% — for JSON payloads typical of AI conversations
- **Evidence**: The changelog's headline benefit statement, immediately following the activation-logic sentence.
- **Confidence**: emerging (a specific, quantified vendor claim with no stated methodology — no sample size, payload-shape distribution, or measurement procedure given for how "up to 85%" was derived)
- **Quote**: "Compressed payloads use less storage and are faster to read and write, so your workflows run faster and cost less. The savings are largest for JSON payloads typical of AI conversations, where storage size and cost can drop by up to 85%."
- **Our assessment**: The "faster to read and write" claim is notable because it asserts a speed benefit, not just a storage-cost benefit — compression normally trades CPU time for size, so a net speed win implies the I/O/storage-write savings outweigh the added compress/decompress CPU cost for these payload shapes. The source doesn't explain the mechanism (e.g., faster because less data crosses the network to the storage backend), but Claim 5 below shows a paired example consistent with the speed claim.

### Claim 4: A demonstration workflow's stored payload dropped from 52 MB uncompressed to roughly 10 MB with zstd compression
- **Evidence**: Two captioned before/after screenshots of Vercel's own workflow-observability dashboard, embedded directly in the changelog.
- **Confidence**: emerging (a single vendor-supplied example, not a distribution or benchmark suite)
- **Quote**: "One typical Workflow, run and stored without compression (52 MB):" / "The same Workflow, run and stored with zstd compression (10 MB):"
- **Our assessment**: 52 MB → 10 MB is roughly an 81% reduction, close to but somewhat below the "up to 85%" headline figure — consistent with "up to" being a ceiling rather than a typical result. I opened both embedded images directly (not just their captions) to check for additional detail: both show a Vercel dashboard trace view for a workflow named `timingWorkflow`, with a "Storage" field reading 52 MB (before, run `wrun_01KVKDA886NXYNQ5H3NKN0YXSJ`) and 10 MB (after, run `wrun_01KVKDA6P0B7QG88AWQ9HBJTHR`) — see Concrete Artifacts for the full field values, including a workflow-duration difference the changelog's prose does not mention.

### Claim 5: The same before/after example's total workflow run duration also dropped, from 45.29s to 37.96s
- **Evidence**: The "Duration" field visible in the two embedded dashboard screenshots (not stated anywhere in the changelog's prose).
- **Confidence**: anecdotal (a single paired data point read directly off a screenshot, not asserted as a benchmark result by the source's own text, and not corrected for any other variable that might differ between the two runs)
- **Quote**: (no direct quote; this is a numeric reading from an embedded image, not text — see paraphrase above and exact field values in Concrete Artifacts)
- **Our assessment**: This is the most concrete evidence in the source for the "workflows run faster" half of Claim 3's prose — a ~16% reduction in total run duration (45.29s → 37.96s) alongside the storage drop. But it's one paired example from what looks like a purpose-built timing demo (a workflow literally named `timingWorkflow`, composed of ~50 uniform `recordStep` spans), not a controlled benchmark — the source doesn't state whether the two runs were otherwise identical (same infrastructure load, same data, no other variable) or repeated to check variance.

### Claim 6: eve, Vercel's durable-agent framework built on the Workflow SDK, automatically inherits the compression benefit for conversation history and session state, with no code changes required
- **Evidence**: The changelog's third paragraph, explicitly naming eve as a downstream beneficiary.
- **Confidence**: settled (first-party statement of how the vendor's own two products relate)
- **Quote**: "Since eve builds durable agents on the Workflow SDK, the same compression now applies to the conversation history and state it persists for every session. That means eve agents store less and run faster, with no code to change."
- **Our assessment**: This is the detail that makes the change relevant beyond Workflow SDK users specifically — any team running eve-based agents gets this storage/speed benefit passively by virtue of the underlying SDK upgrade, without touching their own agent code. Neither the changelog nor eve's own introduction docs page (which I also read; see Extraction Notes) states whether this requires eve itself to be updated to a version that pulls in `workflow@5.0.0-beta.19`+, or whether it's automatic for all eve deployments regardless of pinned SDK version — a real ambiguity in "no code to change" that a practitioner evaluating this would need to check directly.

### Claim 7: The feature requires updating to `workflow@5.0.0-beta.19` or later
- **Evidence**: The changelog's closing call-to-action line.
- **Confidence**: settled (explicit version requirement, unambiguous)
- **Quote**: "Update to `workflow@5.0.0-beta.19` or later and learn more in the [documentation]."
- **Our assessment**: This confirms the feature ships inside a pre-1.0 beta line of the SDK (Workflow SDK 5 beta), not a stable/GA release — relevant context for how much production weight to put on this today versus treating it as a beta capability that could still change before GA.

## Concrete Artifacts

### Full changelog body text (verbatim, extracted from raw page HTML/RSC payload)

```
The Workflow SDK 5 beta now compresses all run, hook, and step inputs and
outputs with zstd.

Compression kicks in automatically, but only when it helps. Small payloads
stay as-is, larger ones get compressed before they're persisted.

Compressed payloads use less storage and are faster to read and write, so
your workflows run faster and cost less. The savings are largest for JSON
payloads typical of AI conversations, where storage size and cost can drop
by up to 85%.

One typical Workflow, run and stored without compression (52 MB):
[screenshot: Vercel dashboard, workflow "timingWorkflow", run
wrun_01KVKDA886NXYNQ5H3NKN0YXSJ, Storage 52 MB, Duration 45.29s / field
shows "45s", Created "3m ago", Completed "2m ago", Expiry "in 30d",
Status "Completed"]

The same Workflow, run and stored with zstd compression (10 MB):
[screenshot: same dashboard, workflow "timingWorkflow", run
wrun_01KVKDA6P0B7QG88AWQ9HBJTHR, Storage 10 MB, Duration 37.96s / field
shows "38s", Created "3m ago", Completed "2m ago", Expiry "in 30d",
Status "Completed"]

Since eve builds durable agents on the Workflow SDK, the same compression
now applies to the conversation history and state it persists for every
session. That means eve agents store less and run faster, with no code to
change.

Update to workflow@5.0.0-beta.19 or later and learn more in the
documentation.

Author: Pranay Prakash (Head of Workflows)
Published: 22 Jun 2026
```

Source: `vercel.com/changelog/workflow-sdk-now-compresses-run-and-step-payloads`,
body text located inside the page's embedded Next.js RSC/Contentful
richtext JSON payload via raw HTML fetch, cross-checked against a
WebFetch-rendered pass. The two screenshot field values (run IDs,
storage, duration, timestamps) were read directly from the embedded PNG
images, not from any caption text, since the changelog prose does not
state them.

### Linked pages followed (no compression-specific content found)

```
https://workflow-sdk.dev/v5/docs/getting-started
  — a framework-selection landing page (14 framework cards: Next.js,
    Vite, React Router, Astro, Express, Fastify, Hono, Nitro, Nuxt,
    SvelteKit, TanStack Start, Python (Beta), NestJS (Experimental));
    no mention of compression, zstd, or payload storage.

https://eve.dev/docs/introduction
  — eve's product introduction. Confirms the durability relationship to
    Workflow SDK: "eve uses the open-source Workflow SDK to make
    sessions durable, resumable, and crash-safe. eve handles that
    machinery so your tools focus on the work itself." No mention of
    compression, zstd, or storage-size figures anywhere on the page.
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-websocket-support-public-beta.md`, `blog-vercel-ai-gateway-api-key-budgets.md`,
`blog-vercel-enterprise-apps-and-agents.md`, `blog-langchain-harness-memory.md`, and
`research-wasnotwas-context-compaction.md` were re-read in full during this
extraction (MINER.md §4b); every claim number cited below was located and
confirmed against that note's own numbered `### Claim N:` headings in
document order before writing this section.

- **Corroborates**: None identified. No existing corpus note makes a claim
  about storage-layer compression of durable-execution or agent-run state,
  so there is nothing for this source to directly corroborate.

- **Contradicts**: None identified. This source makes no claim that
  conflicts with any existing corpus note.

- **Extends**:
  - `blog-vercel-websocket-support-public-beta.md`, `blog-vercel-ai-gateway-api-key-budgets.md`,
    and `blog-vercel-enterprise-apps-and-agents.md`: all three document other
    Vercel platform primitives relevant to AI-agent infrastructure
    (persistent-connection hosting, LLM-spend budgeting, enterprise
    access/credential governance). This source extends that same vendor's
    platform-documentation family to a fourth surface — durable-execution
    storage cost — and, like the WebSocket note, originates from a short
    first-party changelog entry whose real substance required following
    linked pages (though here, unlike the WebSocket case, the linked pages
    added no further mechanism detail; see Extraction Notes).
  - `blog-langchain-harness-memory.md` Claim 6 ("Using a stateful API
    (OpenAI Responses API or Anthropic server-side compaction) is 'mildly
    bad' — state is stored on the vendor's server"): this source's Claim 6
    is a concrete instance of exactly the pattern Chase describes — eve
    agents' "conversation history and state" persisted server-side by
    Vercel's Workflow SDK, on Vercel's infrastructure, is state stored on
    the vendor's server. This isn't a contradiction (Vercel doesn't argue
    against Chase's framing, and Chase's post doesn't mention Vercel or
    Workflow SDK), but it is a concrete example a guide chapter citing
    Chase's argument could point to as an instance of the pattern.
  - `research-wasnotwas-context-compaction.md` Claim 2 (LLM-summary context
    compaction costs "~$0.40 and burns ~21 turns of cached throughput"):
    both sources address the cost of long AI-conversation histories, but at
    different layers — the wasnotwas note covers *in-context-window*
    compaction (shrinking what's re-sent to the model, which costs LLM
    tokens/cache-turns to perform), while this source covers *at-rest*
    storage compression of state that's persisted outside the context
    window for durability/resume, which costs CPU to compress/decompress
    but no LLM tokens. A practitioner optimizing agent-infrastructure cost
    may need both levers, and they are not substitutes for each other.

- **Novel**:
  - **Storage-layer (at-rest) compression of durable-execution/agent state**
    (Claims 1-4, 6) is a mechanism not previously documented in this corpus.
    Every prior corpus source touching "the cost of long AI conversations"
    addresses it either as an in-context-window token/compaction problem
    (`research-wasnotwas-context-compaction.md`) or a prompt-cache-hit-rate
    problem (`blog-anthropic-prompt-caching-everything.md`) — both are about
    what's sent to or cached in front of the model. This source is the first
    to document compressing what's written to a persistence layer for
    pause/resume durability, a distinct concern.
  - **A platform-level compression benefit that propagates transparently to
    a downstream framework built on the same primitive, with the vendor's
    own "no code to change" framing** (Claim 6): no prior corpus source
    documents this specific inheritance pattern (framework B, built on
    infrastructure A, silently gains a cost/performance improvement when A
    is upgraded, without B's own maintainers or B's users doing anything).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: When discussing durable/stateful
  agent execution (pause, resume, crash recovery — the pattern eve and
  Workflow SDK implement), add a note that the storage cost of persisting
  verbose AI-conversation JSON for durability can be substantial in
  practice (this source's own demo: 52 MB for one workflow run) and that
  platform-level transparent compression (zstd, here) is one lever for
  that cost — distinct from, and complementary to, in-context-window
  compaction (`research-wasnotwas-context-compaction.md`), which addresses
  a different layer of the same underlying "conversations get expensive to
  carry around" problem. Flag the open question this source leaves
  unanswered (Claim 6's assessment): whether eve users need to take any
  action themselves to receive this benefit, since "no code to change"
  is stated but not fully specified.
- **Chapter 04 (Context Engineering)**: One Prospector triage comment
  suggested this chapter as relevant; on reading the source in full, we
  think that's a weaker fit than Chapter 02. Context engineering concerns
  what's inside the model's context window; this source's compression
  operates on state persisted *outside* the context window for durability
  purposes, and is never re-read into the context window in compressed
  form (it would be decompressed on read). We recommend Chapter 02 as the
  primary fit and would not add this to Chapter 04 without a source that
  more directly connects storage compression to context-window content.

## Extraction Notes

1. **WebFetch output checked against raw HTML, not trusted directly.**
   An initial WebFetch pass gave an accurate-reading paraphrase, and a
   second pass (explicitly asked for verbatim reproduction) produced text
   very close to but not guaranteed identical to source wording. Per
   MINER.md §2a, every `Quote` field in this note was instead verified
   against the changelog's raw HTML, fetched directly via `curl` and
   located inside the page's embedded Contentful richtext JSON payload —
   the same technique used in `blog-vercel-websocket-support-public-beta.md`.
2. **Both embedded screenshot images were opened and read directly**, not
   just their text captions — this surfaced the workflow-duration figures
   (45.29s → 37.96s, Claim 5) and exact dashboard field values (run IDs,
   "Storage", "Duration", "Expiry") that the changelog's prose does not
   state anywhere. This is concrete evidence the changelog text alone
   would not have surfaced.
3. **Two linked pages followed per MINER.md §1** — the changelog's own
   `Workflow SDK` link (`workflow-sdk.dev/v5/docs/getting-started`) and
   `eve` link (`eve.dev/docs/introduction`) — specifically because one
   Prospector triage comment on this issue asked whether "the linked docs
   elaborate" on data structures, compression/resumability interaction, or
   broader applicability beyond Vercel. Neither page mentions compression,
   zstd, or payload storage at all; the getting-started page is a
   framework picker and the eve introduction covers durability generally
   without this specific detail. This gap is called out explicitly in
   Source Context and is not filled anywhere in the source family I could
   find.
4. **This issue carried three separate Prospector triage comments** with
   differing novelty assessments (low / high / low-medium) and differing
   recommendations (skip unless there's deeper context / extract due to
   quantified evidence / extract only if linked docs elaborate). I treated
   this as a signal to extract carefully but not pad: the source is
   genuinely short (a "1 min read" changelog), so this note has 7 claims
   rather than the 5-15 MINER.md suggests as typical — the shortfall is a
   property of the source's length, not of extraction depth. Every
   substantive sentence and both images in the source are represented
   above.
5. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts.
6. **Confidence calibration: emerging.** Individual mechanism claims
   (Claims 1, 2, 6, 7) are rated "settled" because they are unambiguous
   first-party descriptions of a shipping (if beta) capability. The
   note's overall confidence is "emerging" rather than "settled" because
   the headline quantified claims (85% savings, the 52 MB→10 MB example,
   and the 45.29s→37.96s duration figures I read from the screenshots) are
   all vendor-self-reported, drawn from a single demonstration workflow
   rather than a disclosed methodology or independent benchmark, and the
   underlying SDK is itself still at v5 beta with no GA date given.
