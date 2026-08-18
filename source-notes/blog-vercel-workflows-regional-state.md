---
source_url: https://vercel.com/changelog/configure-where-run-state-lives-in-vercel-workflows
source_type: blog-post
title: "Configure where run state lives in Vercel Workflows"
author: Nathan Rajlich, Pranay Prakash (Vercel; contributors: Karthik Kalyanaraman, Peter Wielander, Ben Sabic)
date_published: 2026-07-20
date_extracted: 2026-08-18
last_checked: 2026-08-18
status: current
confidence_overall: emerging
issue: "#2767"
---

# Configure where run state lives in Vercel Workflows

> Vercel Workflows now pins each run's state, queue dispatch, and output
> streams to a single "home" region — the region the run starts in by
> default, or an explicit region chosen via a new `region` option to
> `start()` — with automatic failover to the next closest region during a
> regional incident and no code changes required for existing workflows.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`; a
  short feature announcement of six paragraphs, one bash install command,
  and one TypeScript code example). I followed the changelog's own linked
  page, `vercel.com/docs/workflows` (its "Multi-region" section is the
  only place the full mechanism — automatic pinning rules, the `region`
  option's exact semantics, and version/migration behavior — is
  documented in full; the changelog prose alone is much thinner). I also
  checked `vercel.com/docs/workflows/pricing`, linked from the docs page's
  own "Resources" section, specifically to see whether it documents a
  cost difference by region for workflow state — it does not (see
  Extraction Notes).
- **Author credibility**: First-party Vercel product-team announcement.
  Byline names (Nathan Rajlich, Pranay Prakash) and three named
  contributors (Karthik Kalyanaraman, Peter Wielander, Ben Sabic) were
  confirmed directly in the page's raw HTML. Pranay Prakash is the same
  Vercel "Head of Workflows" byline that authored the compression
  changelog already in this corpus
  (`blog-vercel-workflow-sdk-payload-compression.md`), giving this source
  the same first-party-product-owner credibility level as that note. No
  customer quotes, adoption metrics, or independent benchmarks appear
  anywhere in the changelog or the linked docs page.
- **Scope**: Covers what "home region" state placement means for a
  Workflows run (state, queue dispatch, output streams), the two ways a
  run's region is chosen (automatic pinning to the starting region, or
  explicit selection via the `region` option), regional failover during
  incidents, the version requirement, and migration semantics for
  existing runs and workflows. Does **not** cover: a list of which Vercel
  Function regions support this feature, any quantified latency or
  cost figures for cross-region vs. same-region execution, a GA/stable
  release timeline (the required SDK version, `workflow@5.0.0-beta.33`,
  is itself a pre-1.0 beta), or how regional state placement interacts
  with the storage-layer compression documented in
  `blog-vercel-workflow-sdk-payload-compression.md`. Unlike that
  compression changelog, this source never names `eve` (Vercel's
  durable-agent framework) — it speaks generally of "agents built on
  Workflows" — so any inference that this benefit reaches eve specifically
  is this note's own inference, not a source statement (flagged in Claim
  2's assessment).

## Extracted Claims

### Claim 1: Vercel Workflows now keeps each run's state, queue dispatch, and output streams in a single home region — the region the run starts in by default, or an explicit target region
- **Evidence**: The changelog's opening sentence, the first substantive content on the page.
- **Confidence**: settled (first-party, unambiguous feature description)
- **Quote**: "Vercel Workflows now keeps each run's state, queue dispatch, and output streams in a single home region: the region where the run starts by default, or any target region you choose."
- **Our assessment**: This names three distinct data surfaces bundled into one "home region" — persisted state, queue message dispatch, and output streams — rather than treating them as independently configurable. A practitioner cannot, per this sentence, pin state to one region while dispatching queue messages from another; all three move together.

### Claim 2: A run keeps its home region for its entire lifetime, so an agent serving a user in a given region executes, checkpoints, and streams output from that same region
- **Evidence**: The changelog's second paragraph, using a concrete worked example (a user in Sydney).
- **Confidence**: settled (first-party mechanism description with a named illustrative example)
- **Quote**: "A run keeps its home region for its lifetime, so for agents built on Workflows, the whole loop stays near the user: an agent serving someone in Sydney executes, checkpoints its progress, and streams output from Sydney."
- **Our assessment**: This is the closest the source comes to a latency justification for the feature — "the whole loop stays near the user" — but it is asserted narratively, not quantified (no latency figures, before/after comparison, or benchmark anywhere in the source or the linked docs page). The source says "agents built on Workflows" generically; it does not name `eve` here, unlike the compression changelog's explicit "eve builds durable agents on the Workflow SDK" framing. Since eve is documented elsewhere in the corpus as built on the Workflow SDK (`blog-vercel-workflow-sdk-payload-compression.md` Claim 6), eve-based agents almost certainly inherit this regional-pinning behavior, but that inheritance is our inference, not a statement in this source.

### Claim 3: During a regional incident, workflow traffic fails over to the next closest region
- **Evidence**: The changelog's second paragraph, immediately following the Sydney example, as a standalone sentence.
- **Confidence**: emerging (a specific operational-resilience claim stated as a single sentence with no further mechanism detail anywhere in the changelog or the linked `vercel.com/docs/workflows` page, which documents automatic pinning and explicit region selection in detail but never uses the words "incident," "failover," or "outage")
- **Quote**: "During a regional incident, workflow traffic fails over to the next closest region."
- **Our assessment**: This is the single least-elaborated claim in the source — it states failover happens but gives no detail on what "next closest" means operationally (geographic proximity? a fixed fallback list per region? does the run's *state* also move, or only new *traffic*?), what happens to in-flight runs during the incident, or whether failover is automatic and silent or requires any customer action. The `vercel.com/docs/workflows` "Multi-region" section — which is otherwise the fuller technical treatment of this same feature — does not mention failover at all, which is a real gap between the changelog's operational-resilience framing and the only linked documentation available to verify it.

### Claim 4: The feature requires updating to `workflow@5.0.0-beta.33` or later
- **Evidence**: The changelog's version-requirement sentence, immediately preceding the install command.
- **Confidence**: settled (explicit version requirement, unambiguous, corroborated verbatim in the linked docs page's "Version and migration" subsection)
- **Quote**: "To get started, update the Workflow SDK to `workflow@5.0.0-beta.33` or later:"
- **Our assessment**: Like the compression feature documented in `blog-vercel-workflow-sdk-payload-compression.md` (which required `workflow@5.0.0-beta.19`+), this feature ships inside the same pre-1.0 Workflow SDK 5 beta line — the version number climbing from `.19` to `.33` between the two changelogs (June 22 to July 20, 2026) is itself evidence of an actively-iterating beta, not a stable release train.

### Claim 5: Existing workflows automatically pick up regional placement on their next run, with no migration or code changes required
- **Evidence**: The changelog's penultimate paragraph, a standalone sentence following the code example.
- **Confidence**: settled (first-party statement, unambiguous)
- **Quote**: "Existing workflows pick up regional placement on their next run, with no migration or code changes."
- **Our assessment**: "On their next run" is the key qualifier — this describes new runs created after the SDK upgrade adopting regional pinning automatically, not existing in-flight or already-completed runs being retroactively relocated. This reading is confirmed by the linked docs page's more explicit statement (Claim 8 below) that upgrading the SDK does not migrate runs created before the upgrade.

### Claim 6: To pin a run to a specific region explicitly, pass a `region` option to the `start()` function
- **Evidence**: The changelog's code example, immediately following the install instructions.
- **Confidence**: settled (first-party code example, verified verbatim against the changelog's raw HTML)
- **Quote**: (no direct prose quote; see the code example itself, extracted verbatim in Concrete Artifacts)
- **Our assessment**: The example passes `{ region: 'sfo1' }` as the third argument to `start()`, alongside the workflow function and its input array — this is an explicit, per-call override of the default automatic pinning behavior described in Claim 7, not a global or per-workflow-file configuration setting.

### Claim 7: By default, Workflows pins a run to the region of the function that started it, with two concrete deployment-topology consequences: single-region deploys keep every run in that one region, and multi-region deploys pin each run to the region that served the triggering user
- **Evidence**: The "Automatic region pinning" subsection of the linked `vercel.com/docs/workflows` page.
- **Confidence**: settled (first-party documentation, more detailed than the changelog itself)
- **Quote**: "By default, Workflows pins a run to the region of the function that started it. No configuration needed:"
- **Quote (single-region consequence)**: "Deploy your app to a single region and every run lives in that region."
- **Quote (multi-region consequence)**: "Deploy your app to multiple regions and each run is pinned to the region that served the user who triggered it."
- **Our assessment**: This is the docs page's fuller version of Claim 2's Sydney example, restated as a general rule rather than a single illustrative case — and it clarifies that the "near the user" latency benefit is contingent on the *application itself* already being deployed to multiple regions. A single-region deployment gets no per-user regional benefit from this feature; every run simply lives in that one region regardless of where the triggering user is.

### Claim 8: The `region` option controls where a run's data is stored and dispatched from, but does not deploy the application's code to that region; step execution instead follows wherever Vercel Functions for the app are deployed
- **Evidence**: The paragraph immediately following the code example in the linked `vercel.com/docs/workflows` page's "Explicit region selection" subsection.
- **Confidence**: settled (first-party documentation, an explicit and specific caveat)
- **Quote**: "The `region` option controls where the run's data is stored and where its queue messages are dispatched from. It does not deploy your code to that region. For step execution to happen in the selected region, deploy your app there."
- **Quote (mismatch behavior)**: "If you deploy your app to a region other than the requested one, the run's data stays in the requested region while its steps execute in the nearest deployed region."
- **Our assessment**: This is the single most practically important caveat in the source and is absent from the changelog entirely — a developer who reads only the changelog's `{ region: 'sfo1' }` example could reasonably assume this pins *execution* to `sfo1`, when it actually only pins *state storage and queue dispatch* there. Getting execution to also happen in that region requires a separate step: configuring Vercel Function regions via the `regions` key in `vercel.json` or the Function Regions project setting. Misreading this distinction could lead a team to believe they've achieved regional data residency or co-located compute when they have only pinned the data layer.

### Claim 9: A run's region is locked at creation and cannot be changed; runs created by the Workflow SDK's 4.x release line always live in `iad1`; and upgrading the SDK does not retroactively migrate runs created before the upgrade
- **Evidence**: The "Version and migration" subsection of the linked `vercel.com/workflows` docs page.
- **Confidence**: settled (first-party documentation, specific and unambiguous)
- **Quote**: "Multi-region requires `workflow` version `5.0.0-beta.33` or later. Runs created by the 4.x release line always live in `iad1`. Workflows locks each run's region at creation. To run in a different region, start a new run. Upgrading the SDK does not migrate runs created before the upgrade."
- **Our assessment**: This is the source's most precise statement of what Claim 5's "no migration ... required" actually means in practice: no migration happens automatically, and none is offered — a run's region assignment is permanent for that run's life, and the only way to relocate a workload to a different region is to start an entirely new run. This also reveals that every run created on the pre-multi-region 4.x SDK line was implicitly single-region (`iad1`, Vercel's US East region) by default, a detail neither the changelog nor the rest of the docs page states explicitly elsewhere.

## Concrete Artifacts

### Full changelog body text (verbatim, extracted from raw page HTML, character-verified via `curl` against the embedded article markup — not trusted from an initial WebFetch pass, per MINER.md §2a)

```
Source: https://vercel.com/changelog/configure-where-run-state-lives-in-vercel-workflows
Published: 2026-07-20
Authors: Nathan Rajlich, Pranay Prakash
Contributors: Karthik Kalyanaraman, Peter Wielander, Ben Sabic

Vercel Workflows now keeps each run's state, queue dispatch, and output
streams in a single home region: the region where the run starts by
default, or any target region you choose.

A run keeps its home region for its lifetime, so for agents built on
Workflows, the whole loop stays near the user: an agent serving someone
in Sydney executes, checkpoints its progress, and streams output from
Sydney. During a regional incident, workflow traffic fails over to the
next closest region.

To get started, update the Workflow SDK to workflow@5.0.0-beta.33 or
later:

  pnpm i workflow@beta

import { start } from 'workflow/api';
import { myWorkflow } from '@/workflows/my-workflow';

const run = await start(myWorkflow, [input], { region: 'sfo1' });

Existing workflows pick up regional placement on their next run, with no
migration or code changes.

Learn more in the Workflows documentation.
```

### `vercel.com/docs/workflows` "Multi-region" section (verbatim, extracted from raw page HTML, character-verified via `curl`)

```
Source: https://vercel.com/docs/workflows#multi-region

Workflows runs in every Vercel Function region. When a run starts,
Workflows pins it to a single region and keeps its state, queue
dispatch, and streams there for the run's lifetime. This avoids
cross-region round trips on the hot path and contains the blast radius
of a regional event to the runs pinned there.

Reads, hook resumes, and stream consumers can come from anywhere. The
platform routes them to the run's region automatically.

Automatic region pinning
By default, Workflows pins a run to the region of the function that
started it. No configuration needed:
- Deploy your app to a single region and every run lives in that region.
- Deploy your app to multiple regions and each run is pinned to the
  region that served the user who triggered it.

Explicit region selection
To pin a run to a specific region, pass the region option to start():

  import { start } from 'workflow/api';
  import { myWorkflow } from '@/workflows/my-workflow';

  const run = await start(myWorkflow, [input], { region: 'sfo1' });

The region option controls where the run's data is stored and where its
queue messages are dispatched from. It does not deploy your code to
that region. For step execution to happen in the selected region,
deploy your app there. To do this, configure Function regions through
the regions key in vercel.json or the Function Regions project setting.
If you deploy your app to a region other than the requested one, the
run's data stays in the requested region while its steps execute in the
nearest deployed region.

Version and migration
Multi-region requires workflow version 5.0.0-beta.33 or later. Runs
created by the 4.x release line always live in iad1. Workflows locks
each run's region at creation. To run in a different region, start a
new run. Upgrading the SDK does not migrate runs created before the
upgrade.
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-workflow-sdk-payload-compression.md`, `blog-vercel-agent-runs-mcp-cli.md`,
`blog-latentspace-vercel-andrew-qu-eve.md`, and `blog-cursor-vercel-queues.md` were
re-read (in full, or checked via targeted grep for "region"/"durab" where noted below)
during this extraction per MINER.md §4b, and every claim number cited below was
located and confirmed against that note's own numbered `### Claim N:` headings in
document order before writing this section. `blog-latentspace-vercel-andrew-qu-eve.md`
contains no mention of "region" or "durab" anywhere (checked via grep) and is not
cited below for that reason.

- **Corroborates**: None identified. No existing corpus note makes a claim about
  geographic/regional placement of durable-execution state, so there is nothing
  in the corpus for this source to directly corroborate.

- **Contradicts**: None identified. This source makes no claim that conflicts
  with any existing corpus note.

- **Extends**:
  - `blog-vercel-workflow-sdk-payload-compression.md` Claims 1 and 7 (Workflow
    SDK 5 beta compresses all run/hook/step inputs and outputs with zstd;
    required `workflow@5.0.0-beta.19`+): this source documents a second,
    independent configuration axis for the same underlying persisted-state
    layer that compression note's Claims 1-4 describe — *where* that state
    lives geographically (this source), versus *how much space* it occupies
    once compressed (that source). The two features shipped roughly a month
    apart in the same beta SDK line (`.19` then `.33`), but this source's
    changelog and the `vercel.com/docs/workflows` page I followed do not
    state whether regional placement and payload compression interact (e.g.,
    whether a compressed payload's storage location is affected by the
    `region` option) — an open question neither source answers.
  - `blog-vercel-agent-runs-mcp-cli.md` Claim 8 ("[the Agent Runs dashboard]
    appears automatically for eve projects, with no instrumentation file
    required") and the compression note's Claim 6 (eve inherits the
    compression benefit "with no code to change"): both describe eve
    passively inheriting a platform-level Workflow SDK capability with zero
    developer action. This source's Claim 5 ("Existing workflows pick up
    regional placement on their next run, with no migration or code changes")
    uses near-identical "no code changes" language, extending that recurring
    "automatic inheritance from the underlying platform" pattern to a third
    distinct Workflow SDK capability. Unlike those two sources, however, this
    changelog never names `eve` explicitly (see Claim 2's assessment) — the
    inheritance is inferred by this note from eve's documented dependency on
    the Workflow SDK, not stated here.
  - `blog-cursor-vercel-queues.md` Claim 1 (Vercel Queues, "a durable event
    streaming system," was built as Vercel's own infrastructure product):
    this source's Claim 1 names "queue dispatch" as one of the three data
    surfaces pinned to a run's home region, which is a concrete, regionally-scoped
    consumer of the Queues infrastructure that Queues note documents being
    built. Neither source states that Workflows' queue dispatch specifically
    runs on Vercel Queues (the compression note and this one both link a
    separate `vercel.com/docs/queues` page that I did not follow, as it was
    outside this issue's triage scope), so this is a plausible architectural
    connection, not a confirmed one.

- **Novel**:
  - **Explicit, per-run geographic placement of durable-execution state**
    (Claims 1, 6, 7) is a mechanism not previously documented in this corpus.
    Every prior corpus source touching Vercel's Workflow SDK persistence
    layer addresses payload size (compression) or observability (Agent
    Runs), not the geographic region the persisted data lives in.
  - **A stated data/compute decoupling caveat**, where a configuration option
    controls data residency but not code execution location, requiring a
    second, separate configuration mechanism (Function regions) to align the
    two (Claim 8): no prior corpus source documents this specific
    data-vs-compute placement distinction for a durable-execution platform.
  - **An explicit, vendor-stated regional-failover claim for a durable
    execution platform with no supporting mechanism detail** (Claim 3): no
    prior corpus source makes an operational-resilience/incident-failover
    claim for AI-agent infrastructure state; this is also the single
    thinnest-evidenced claim in this note (see Claim 3's assessment and
    Extraction Notes).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: When discussing durable/stateful
  agent execution (pause, resume, crash recovery — already touched via
  `blog-vercel-workflow-sdk-payload-compression.md`), add regional state
  placement as a third configurable dimension of that same persistence
  layer (alongside compression and observability capture). Specifically
  flag Claim 8's data-vs-compute distinction as a concrete gotcha worth
  naming explicitly: setting `{ region: 'sfo1' }` on `start()` pins where
  an agent's state and queue messages live, not where its code actually
  runs — a team building a distributed, multi-region agent deployment
  needs to configure Function regions separately to get co-located
  compute, or their "regional" agent will still execute from wherever
  its app happens to be deployed.
- **Chapter 03 (Infrastructure & Deployment)**: Add Claim 9's migration
  semantics (region locked at creation; no automatic migration; the only
  path to a different region is starting a new run) as a concrete
  planning consideration for any team relying on Vercel Workflows for
  agent state and later needing to relocate workloads — this is not a
  live-migration capability, and teams should not assume upgrading the
  SDK retroactively moves existing runs' data.
- We do **not** recommend citing Claim 3 (regional failover) in the guide
  as a settled operational-resilience guarantee without a stronger
  source: it is a single unelaborated sentence in a first-party changelog,
  not corroborated by the fuller `vercel.com/docs/workflows` page, which
  documents the rest of this feature in detail but never mentions
  failover, incidents, or outages at all (see Claim 3's assessment).

## Extraction Notes

1. **WebFetch output checked against raw HTML, not trusted directly.**
   An initial WebFetch pass on the changelog URL returned an accurate-reading
   but reworded paraphrase (e.g., "Vercel Workflows now maintains run state...
   within a single home region" rather than the source's actual "keeps each
   run's state..."), and a follow-up WebFetch pass hit an internal
   copyright-length guardrail that truncated quotes to ~125 characters and
   refused to reproduce full paragraphs verbatim. Per MINER.md §2a, every
   `Quote` field in this note was instead verified against the changelog's
   raw HTML, fetched directly via `curl` with a browser user-agent and
   located character-for-character inside the page's rendered article markup
   — the same raw-HTML-verification technique documented in
   `blog-vercel-workflow-sdk-payload-compression.md`'s and
   `blog-cursor-vercel-queues.md`'s Extraction Notes. The same technique was
   applied to the linked `vercel.com/docs/workflows` page.
2. **One linked page followed per MINER.md §1** — `vercel.com/docs/workflows`,
   specifically because the changelog's own prose (six short paragraphs) does
   not explain the automatic-pinning default, the data-vs-compute distinction
   for the `region` option, or the migration/version-locking semantics; all
   of that (Claims 7-9) came from the docs page's "Multi-region" section. A
   second linked page, `vercel.com/docs/workflows/pricing`, was checked
   specifically to see whether it documents any region-dependent cost for
   Workflows state storage or dispatch — every "region" hit on that page
   traced to unrelated site-navigation links for general Vercel Function
   regional-pricing pages, not to any Workflows-specific regional cost
   content, so no claim about cost tradeoffs is included in this note. This
   is a real gap: neither the changelog, the linked docs page, nor the
   linked pricing page states whether choosing a non-default region costs
   more, less, or the same as the default.
3. **Failover claim (Claim 3) is corroborated only by the changelog itself,
   not by the fuller docs page.** I specifically searched the full raw text
   of `vercel.com/docs/workflows` for "failover," "incident," and "outage"
   after finding the failover sentence in the changelog, and found no match
   for any of those terms anywhere on that page. I flagged this gap
   explicitly in Claim 3 and in Guide Impact rather than treating the
   changelog's single sentence as sufficient to recommend the guide state
   regional failover as a settled capability.
4. **Three separate Prospector triage comments were filed on this issue**,
   with differing chapter recommendations (Ch01/Ch02, then Ch02/Ch03, then
   Ch02 alone) but a consistent, correct summary of the source's core claims
   in the third comment (region affinity, latency via the Sydney example,
   failover, and "no code changes"). I verified all four of that comment's
   "key claims to extract" directly against the raw source text before
   including them here; none were fabricated by the triage step.
5. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts.
6. **Confidence calibration: emerging.** Individual mechanism claims (Claims
   1, 4, 5, 6, 7, 8, 9) are rated "settled" because they are unambiguous,
   internally consistent first-party descriptions of a shipping (if beta)
   capability, cross-verified between the changelog and the linked docs
   page via raw HTML. The note's overall confidence is "emerging" rather
   than "settled" because: (a) the underlying SDK is still at v5 beta
   (`5.0.0-beta.33`) with no GA date given anywhere in the source family;
   (b) the regional-latency benefit (Claim 2) and the failover claim (Claim
   3) are both asserted narratively with no quantified metric, benchmark, or
   named customer evidence; and (c) no independent verification, third-party
   usage report, or production case study of this specific feature exists
   anywhere in the current corpus.
