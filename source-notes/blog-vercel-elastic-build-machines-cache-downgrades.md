---
source_url: https://vercel.com/changelog/elastic-build-machines-now-use-turborepo-cache-hits-to-prevent-downgrades
source_type: blog-post
title: "Elastic build machines now use Turborepo cache hits to prevent downgrades"
author: Mehul Kar, Anthony Shew (Vercel)
date_published: 2026-08-24
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: settled
issue: "#3637"
---

# Elastic build machines now use Turborepo cache hits to prevent downgrades

> A three-paragraph Vercel changelog entry announcing that Elastic build
> machines now read Turborepo cache-hit signals before right-sizing a
> project's build machine, so that a fast warm-cache build no longer causes
> the *next* (potentially cold-cache) build to be starved of CPU/memory by
> an autoscaler that mistook low resource usage for low resource need. The
> changelog itself gives only the "what" and a one-sentence "why"; the
> linked `/docs/builds/managing-builds#elastic-build-machines` page supplies
> the load-bearing mechanism detail this note extracts — the build-machine
> tier table, the cost/speed tradeoff Elastic is optimizing, the CPU-minute
> billing formula, and when Vercel recommends pinning a fixed machine type
> instead of using Elastic autoscaling.

## Source Context

- **Type**: blog-post (Vercel product changelog, `vercel.com/changelog`, a
  three-paragraph entry with no code sample; auto-discovered via the
  trusted `vercel` Atom feed, published August 24, 2026). Per MINER.md §1,
  this note follows the changelog's one substantive link — "Learn more in
  the build documentation" — which resolves to
  `https://vercel.com/docs/builds/managing-builds#elastic-build-machines`,
  because the changelog gives no detail on how Elastic sizing actually
  works, what the machine tiers are, or how the feature is billed, and
  that docs page is the only place in the source family where those
  mechanics are documented.
- **Author credibility**: First-party Vercel changelog entry, byline Mehul
  Kar and Anthony Shew (both named in the page's markdown-rendered byline,
  `**Published:** August 24, 2026 | **Authors:** Mehul Kar, Anthony Shew`).
  Anthony Shew is also the byline on `blog-vercel-remote-cache-purge.md`,
  another Vercel Remote-Cache/Turborepo-adjacent changelog entry already in
  this corpus. Vercel operates both the Elastic build machine product and
  Turborepo, so this is authoritative first-party documentation of a
  shipping autoscaling behavior, not third-party reporting or a customer
  anecdote. No named customer, incident, or measured failure count (e.g.,
  "N builds failed from underprovisioning before this fix") is given
  anywhere in either page — the failure mode motivating the change is
  described only as a hypothetical ("could leave... without enough
  resources"), not a documented incident.
- **Scope**: Covers the new cache-hit-aware downgrade-prevention logic for
  Elastic build machines, and, via the linked docs page, the surrounding
  Elastic build machine feature: the five build-machine tiers and their
  specs, how Elastic decides machine size ("balance between speed and
  price"), the CPU-minute billing model, and guidance on when to pin a
  fixed machine type instead of using Elastic. Does NOT cover: the actual
  algorithm/heuristic Elastic uses to read "cache hits" (e.g., whether it
  checks Turborepo's local `.turbo` cache, the Remote Cache, or both; what
  hit-rate threshold triggers non-downgrade behavior), any metrics on how
  often downgrades previously caused build failures, rollout timeline or
  opt-out mechanism (the changelog states none is needed/available), or
  whether this cache-awareness applies to non-Turborepo monorepo tools.

## Extracted Claims

### Claim 1: Elastic build machines now factor Turborepo cache-hit data into the downgrade decision, so a build with a warm cache no longer causes the machine tier to be downgraded
- **Evidence**: The changelog's lead sentence, stated as new shipping behavior.
- **Confidence**: settled (first-party description of a shipping autoscaling change)
- **Quote**: "Elastic build machines now consider Turborepo cache hits when deciding whether to use a smaller build machine. A warm-cache build no longer triggers a downgrade."
- **Our assessment**: This is a narrow, specific autoscaler fix: previously, Elastic's sizing decision apparently used *only* recent build resource usage (see Claim 4: "auto-scale based on your recent build durations") as its signal, which a warm Turborepo cache would deflate — a fast, low-CPU warm-cache build looks like a project that needs a smaller machine, even though the next build might hit a cold cache and need the original capacity. Adding cache-hit state as a second input is a plausible, low-risk fix for that specific mis-signal, but the source gives no detail on the actual decision rule (e.g., is it binary hit/no-hit, or a hit-ratio threshold?).

### Claim 2: The problem this fixes is that a warm-cache build's lower CPU/memory usage could cause Elastic to downgrade the machine tier, leaving a subsequent cold-cache build without enough resources to complete
- **Evidence**: The changelog's explicit rationale paragraph, presented as the mechanism being fixed.
- **Confidence**: settled (first-party statement of the bug/gap being addressed)
- **Quote**: "A warm-cache build can use less CPU and memory than the same build with a cold cache. Downgrading based on that lower usage could leave a later cold-cache build without enough resources to complete successfully."
- **Our assessment**: This names a concrete failure mode for autoscaled build infrastructure: optimizing machine size off of the *most recent* observed usage is unsafe when that usage is itself an artifact of a transient cache state (a warm cache) rather than the project's true steady-state resource need. This is a general lesson for any cache-aware autoscaler, not just Turborepo/Vercel specifically — an agent-driven CI system that scales compute off of recent build telemetry could hit the identical failure mode if it doesn't distinguish "fast because cached" from "fast because small."

### Claim 3: The fix applies automatically to all builds on Elastic build machines, with no developer action, configuration, or opt-in required
- **Evidence**: The changelog's closing paragraph, stated as a deployment/rollout fact.
- **Confidence**: settled (first-party statement of rollout scope)
- **Quote**: "This change applies automatically to all builds using Elastic build machines. No action is required."
- **Our assessment**: Consistent with how Vercel has framed other autoscaling/infrastructure changes in this corpus (e.g., Elastic itself being default-on for new Pro/Enterprise teams per Claim 9) — capacity-management logic is treated as a platform-managed default, not a per-project tunable. There is no stated opt-out, so teams cannot revert to the old downgrade behavior even if they wanted to (no use case for wanting the old behavior is discussed, but the absence of an escape hatch is worth noting for teams that pin machine types for predictability — see Claim 7).

### Claim 4: Elastic build machines auto-scale per project based on that project's recent build durations, ranging from 4 to 30 vCPUs and 8 to 60 GB memory with auto-scaled disk
- **Evidence**: The docs page's build-machine tier table plus explicit prose describing the auto-scaling input signal.
- **Confidence**: settled (first-party spec table and auto-scaling description)
- **Quote**: "For Pro and Enterprise customers, Elastic build machines auto-scale based on your recent build durations."
- **Our assessment**: This confirms the pre-existing signal Elastic used before this changelog's fix was "recent build durations" — i.e., wall-clock time, not a direct CPU/memory utilization metric. That framing sharpens Claim 1/2: a warm-cache build finishes faster (shorter duration), and if duration alone drove the downgrade decision, a fast cached build would look like a candidate for a smaller machine regardless of why it was fast. The new cache-hit signal is layered on top of this existing duration-based heuristic rather than replacing it (the source doesn't say the duration signal was removed).

### Claim 5: Elastic's stated design goal is balancing speed against price — assigning larger machines only to builds that are genuinely CPU/memory-bound, and smaller machines to builds that wouldn't benefit, so teams don't pay for unused compute
- **Evidence**: The docs page's explanatory paragraph immediately under the "Elastic build machines" heading.
- **Confidence**: settled (first-party framing of the feature's design intent)
- **Quote**: "With Elastic, Vercel evaluates each project individually and assigns the build machine that best fits its actual workload. The goal is a balance between speed and price: builds that genuinely benefit from more vCPUs and memory get larger machines automatically, while builds that don't get, smaller machines so you aren't paying for compute you won't use."
- **Our assessment**: This is the cost-efficiency framing that makes the changelog's fix necessary in the first place — Elastic actively tries to downsize machines to save money, which is precisely the behavior that needed the cache-hit guardrail from Claim 1 so it doesn't downsize based on a misleading fast-because-cached signal. (Note: the quoted sentence contains an apparent copy-edit slip in the source itself — "while the builds that don't get, smaller machines" — reproduced here verbatim per MINER.md §2a rather than corrected.)

### Claim 6: Elastic reduces cost specifically because many projects don't fully utilize a Turbo machine's 30 vCPUs, and it auto-upgrades CPU/memory-bound projects (heavy bundling, expensive type checking) to larger machines so they finish sooner
- **Evidence**: The docs page's two-bullet elaboration ("Optimized bills" / "Faster builds where it matters") under "In practice, this means:".
- **Confidence**: settled (first-party elaboration of the mechanism from Claim 5)
- **Quote**: "Optimized bills. Many projects don't fully utilize a Turbo machine's 30 vCPUs. Elastic detects this and assigns a smaller machine, reducing your build minute costs without making builds noticeably slower." ... "Faster builds where it matters. Projects that are CPU- or memory-bound (heavy bundling, expensive type checking) are auto-upgraded to a larger machine so they finish sooner."
- **Our assessment**: This names the two concrete named workload types Elastic optimizes for: bundling and type checking as CPU/memory-bound examples on the "needs more machine" side, with no named example given for the "needs less machine" side beyond "many projects." The claim that upgrading doesn't come with a corresponding "noticeably slower" downside statement for the downsizing path is asserted, not measured, in this source.

### Claim 7: Elastic reassignment is continuous and automatic as a project changes over time, requiring no manual benchmarking or tier selection by the developer
- **Evidence**: The docs page's third "In practice" bullet ("No manual tuning").
- **Confidence**: settled (first-party description of ongoing reevaluation behavior)
- **Quote**: "No manual tuning. You don't need to benchmark each project or guess the right tier. The assignment is reevaluated as your project changes over time, so it stays right-sized as your codebase grows."
- **Our assessment**: This positions Elastic as a continuously-adaptive default rather than a one-time sizing decision made at project setup — relevant to any guide discussion of infrastructure that supports growing, agent-generated codebases, where build resource needs may shift as an agent adds dependencies or restructures a monorepo over time without a human proactively re-benchmarking build infra.

### Claim 8: Vercel recommends pinning a fixed (non-Elastic) build machine type only when a team wants a guaranteed machine size on every build, or when a project has unusual resource patterns already manually tuned for
- **Evidence**: The docs page's "When to choose a fixed machine type instead" section, presented as explicit guidance.
- **Confidence**: settled (first-party guidance/recommendation)
- **Quote**: "Elastic is the right choice for most projects. You may want to pin a project to a specific build machine type if: You want to guarantee a specific machine size on every build. A project has unusual resource patterns that you've already manually tuned for."
- **Our assessment**: This is Vercel's own stated exception list to an Elastic-by-default recommendation — notably, "predictability" (guaranteed sizing) is framed as the main reason to opt out of an auto-scaling system, which is a recognizable tradeoff pattern (autoscaling optimizes average cost/throughput; fixed provisioning optimizes worst-case predictability) that shows up broadly in infrastructure design, not just build machines.

### Claim 9: Elastic build machines are billed by CPU minute (build minutes × vCPU cores used), starting at $0.0035 per CPU minute, and are the default machine type for new Pro and Enterprise teams
- **Evidence**: The docs page's billing paragraph with a worked example, plus the earlier auto-scaling paragraph's default-on statement.
- **Confidence**: settled (first-party pricing and default-configuration documentation)
- **Quote**: "Elastic build machines are also billed by CPU minute, starting at $0.0035 per CPU minute. A CPU minute is one minute of build time multiplied by the number of vCPU cores used. For example, if a build takes 3 minutes and Elastic assigns the Standard machine (4 vCPUs), you're billed for 3 minutes × 4 cores = 12 CPU minutes." ... "New Pro and Enterprise accounts use Elastic machines by default."
- **Our assessment**: This makes the cost stakes of Claim 1's fix concrete: because billing is CPU-minutes (duration × vCPU count), a machine downgrade genuinely lowers cost per build, which is exactly why Elastic is incentivized to downgrade aggressively — and exactly why an under-provisioning failure from an incorrect downgrade (Claim 2) isn't just a reliability bug, it's the direct result of the same cost-optimization logic the feature is designed to perform. The two goals (minimize CPU-minute cost, avoid resource-starved failures) are in tension, and this changelog entry is Vercel adding one additional signal (cache hits) to resolve that tension more accurately.

## Concrete Artifacts

```
Build machine tier table (verbatim, from /docs/builds/managing-builds#build-machines):

| Build machine type | Number of vCPUs | Memory (GB) | Disk size (GB) |
| ------------------ | --------------- | ----------- | -------------- |
| Basic              | 2               | 8           | 32              |
| Standard            | 4               | 8           | 32              |
| Enhanced           | 8               | 16          | 64              |
| Turbo              | 30              | 60          | 64              |
| Elastic            | 4-30            | 8-60        | Auto-scaled     |

Source: https://vercel.com/docs/builds/managing-builds#build-machines
```

```
Changelog announcement (verbatim, full text of the markdown-served version
fetched via `Accept: text/markdown`):

"Elastic build machines now consider Turborepo cache hits when deciding
whether to use a smaller build machine. A warm-cache build no longer
triggers a downgrade.

A warm-cache build can use less CPU and memory than the same build with a
cold cache. Downgrading based on that lower usage could leave a later
cold-cache build without enough resources to complete successfully.

This change applies automatically to all builds using Elastic build
machines. No action is required. Learn more in the build documentation."

Source: https://vercel.com/changelog/elastic-build-machines-now-use-turborepo-cache-hits-to-prevent-downgrades
Published: August 24, 2026. Authors: Mehul Kar, Anthony Shew.
```

```
CPU-minute billing worked example (verbatim, from /docs/builds/managing-builds#build-machines):

"Basic is included with Hobby. For paid teams, Basic usage is billed at
$0.0035 per CPU minute, or $0.007 per build minute. Elastic build machines
are also billed by CPU minute, starting at $0.0035 per CPU minute. A CPU
minute is one minute of build time multiplied by the number of vCPU cores
used. For example, if a build takes 3 minutes and Elastic assigns the
Standard machine (4 vCPUs), you're billed for 3 minutes × 4 cores = 12 CPU
minutes."

Source: https://vercel.com/docs/builds/managing-builds#build-machines
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-remote-cache-purge.md` and `blog-cursor-vercel-queues.md` were
re-read in full during this extraction per MINER.md §4b. Neither note
numbers a claim that this note cites by number — both are referenced below
by section/claim content, not by an invented claim number where the
correspondence is topical rather than a direct citation.

- **Corroborates**: `blog-vercel-remote-cache-purge.md` Claim 3 (Vercel
  automatically expires Remote Cache artifacts after 7 days "to avoid
  unbounded cache growth") — both sources independently show Vercel/
  Turborepo caching infrastructure (Remote Cache artifacts there, build
  machine sizing here) being tuned with automatic, no-developer-action
  safety defaults (automatic expiry there; automatic cache-aware
  downgrade-prevention here) rather than requiring manual intervention.
  Both are also authored/co-authored by Anthony Shew, giving a consistent
  first-party voice across two Turborepo/Vercel build-cache-adjacent
  changelog entries in the corpus.
- **Contradicts**: None found. No existing source note makes a claim about
  Elastic build machine sizing, CPU-minute billing, or cache-aware
  autoscaling that this source disagrees with.
- **Extends**: `blog-vercel-remote-cache-purge.md` — that note documents
  the Turborepo/Vercel Remote Cache's retention, permissions, and what
  counts as a cacheable artifact (including console logs); this note adds
  a previously-uncovered layer of the same cache ecosystem: how cache
  *hit/miss state* feeds back into build-machine capacity decisions, not
  just what gets cached or how long it's retained. `docs-ghaw-cache-memory-
  reference.md` documents a structurally different cache (GitHub Actions
  Cache used for agent session/memory persistence, 10GB/LRU) — this note's
  build-machine-sizing cache-awareness is a distinct application of "cache
  state as an infrastructure signal," worth distinguishing rather than
  conflating: that note's cache holds agent memory across runs, this
  source's cache (Turborepo) holds build artifacts, and only this source
  documents cache state being read by an *autoscaler* to size compute.
- **Novel**: The specific failure mode this changelog fixes — an
  autoscaler downgrading compute capacity based on a transient warm-cache
  speedup, then starving a subsequent cold-cache run — is new to the
  corpus. No existing source discusses cache-hit state as an input to a
  build-infrastructure autoscaling decision, or the general "fast because
  cached, not fast because small" mis-signal risk for any usage-based
  autoscaler. The CPU-minute billing formula and the five-tier build
  machine spec table (Claim 9, Concrete Artifacts) are also not documented
  elsewhere in the corpus.

## Guide Impact

- **No direct match in the current chapter structure.** The guide's actual
  chapters (`00-principles`, `01-daily-workflows`, `02-harness-engineering`,
  `03-verification`, `04-context-engineering`, `05-team-adoption`,
  `06-security-threat-model`) do not include a build-infrastructure,
  CI-capacity, or infrastructure-cost chapter — the Prospector's second
  triage comment referenced "Ch03 (Build infrastructure for agents)" and
  "Ch04 (Reliability & observability patterns)," but those titles do not
  match the actual `guide/03-verification.md` and `guide/04-context-
  engineering.md` files (see Extraction Notes). I did not force this
  source into either chapter on that basis.
- **Chapter 02 (Harness Engineering), `## CI` section**: This section
  currently only shows an example CLAUDE.md snippet describing what a
  project's CI does (e.g., "GitHub Actions (`test.yml`): runs on push and
  PRs"). If the guide ever expands this section to discuss the
  infrastructure *behind* agent-triggered CI/build load (relevant as
  agents increasingly generate the commits and PRs that trigger builds),
  Claim 2's general lesson is the concrete, reusable point to add: an
  autoscaler that sizes compute off of recent build duration/usage alone
  can under-provision a subsequent run if that usage was artificially low
  due to a warm cache, not a genuinely smaller workload — a caution
  applicable to any team building or configuring cache-aware autoscaling
  for agent-driven build pipelines, not just Vercel customers.
- This source is a minor, standalone data point rather than one that
  changes an existing recommendation — recommend holding it for a future
  chapter on build/CI infrastructure economics if one is added, rather
  than forcing a citation into an unrelated section now.

## Extraction Notes

- **Two triage comments on this issue disagree, and neither fully matches
  the actual guide structure.** The first triage comment lists "Relevant
  chapters: Ch02 (Harness Engineering)" only. The second lists "Ch03
  (Build infrastructure for agents), Ch04 (Reliability & observability
  patterns)" — chapter titles that do not exist in `guide/`; the actual
  `03-verification.md` and `04-context-engineering.md` cover different
  topics. I flagged this inconsistency here rather than silently picking
  one triage comment's framing, and based Guide Impact on the guide's
  actual on-disk chapter structure instead of either comment's chapter
  labels.
- **WebFetch's AI-summarized pass materially reworded the source.** An
  initial WebFetch call against the changelog URL returned a paraphrased,
  restructured version (different headings, invented section titles like
  "Technical Rationale," and a compressed/altered rendering of the core
  quote) rather than the source's actual wording. Per MINER.md §2a, I
  fetched the page directly via `curl` instead. The page serves a clean
  first-party markdown version when requested with an `Accept:
  text/markdown` header (Vercel's own `<link rel="alternate"
  type="text/markdown">` tag points at the same URL), which was used as
  the ground truth for every quote in this note; I cross-checked it
  against the raw HTML's Open Graph/meta description tags (which
  paraphrase the same two-sentence mechanism) as a consistency check, not
  as a quote source.
- **One linked page followed per MINER.md §1**: the docs page
  `/docs/builds/managing-builds`, fetched via the same markdown content
  negotiation. Other links on that docs page (e.g., to `/docs/pricing`,
  `/docs/cli/deploy`, `/docs/rest-api`) were not followed, since they cover
  billing/CLI/API surfaces orthogonal to this issue's specific "cache-hit
  aware downgrade prevention" topic; the "Elastic build machines" and
  "Build machines" sections of the docs page that were followed already
  contain the load-bearing tier, billing, and design-rationale detail.
- **No contradiction with existing source notes was found** during
  cross-referencing (MINER.md §4a), so no contradiction issue was filed.
- The changelog itself gives no measured before/after data (e.g., number
  of builds previously failed to under-provisioning) — this is graded
  `settled` because it is first-party documentation of shipping platform
  behavior, not because the *motivating problem's* prevalence is
  independently verified.
