---
source_url: https://cursor.com/blog/git-at-any-scale
source_type: blog-post
title: "Git at any scale"
author: Vicent Martí (Cursor)
date_published: 2026-08-18
date_extracted: 2026-08-23
last_checked: 2026-08-23
status: current
confidence_overall: emerging
issue: "#2884"
---

# Git at any scale

> Cursor's engineering deep-dive into why Git repository *hosting* is hard at
> scale (packfile internals defeat networked filesystems, GitHub's Spokes
> uses 3-phase-commit replication with latency/throughput tradeoffs that
> worsen as replica count grows), and the write-ahead-log-in-S3 architecture
> ("Continuity") Cursor built instead — closing with an explicit claim that
> agent-driven development ("more code, more PRs, more CI runs") motivated
> building a new hosting platform ("Origin").

## Source Context

- **Type**: blog-post (Cursor official engineering blog, published August 18,
  2026, 27-minute read). Auto-discovered via the trusted `cursor-blog` RSS
  feed, so it already passed the "is this author worth listening to?"
  pre-screen.
- **Author credibility**: Byline is Vicent Martí; no formal bio or role is
  given on the page itself. The one internal signal of prior git-hosting
  pedigree is an aside referencing "my former mentor Shawn Pearce" (Shawn
  Pearce is a well-known JGit/Gerrit maintainer with a long history in Git
  tooling), which suggests real domain background, but this is inferred from
  a passing mention, not a stated credential. The piece is written as a
  first-person technical narrative (design history + architecture
  description), not third-party reporting.
- **Scope**: Covers Git *server-side hosting* infrastructure specifically —
  why packfiles make networked/distributed filesystems fail, GitHub's
  historical evolution (NFS/GFS/DRBD → RPC-based single-machine hosting →
  Spokes), and Cursor's own replacement architecture ("Continuity"). It does
  NOT cover client-side git performance, git UX, or how individual coding
  agents issue git commands — those are out of scope. The post is also,
  explicitly, a lead-in to marketing Cursor's "Origin" git hosting product;
  the technical history sections read as disinterested engineering writing,
  but the closing section and the unaudited throughput numbers should be
  read with that commercial framing in mind.

## Extracted Claims

### Claim 1: Git's on-disk packfile format — objects placed with no correlation to their logical graph position, heavily delta-compressed against other objects in the same pack — is why hosting Git on a networked/distributed filesystem breaks down, independent of the DAG-level (i.e. commit/tree/blob graph) distribution question
- **Evidence**: Technical explanation of packfile internals: object placement is optimized purely for pack size, not locality, so most objects are stored only as a delta against another object in the pack, and reading any one object requires "random walk" disk access.
- **Confidence**: settled — this is a description of well-documented Git internals, not a novel empirical claim.
- **Quote**: "There is no correlation between the layout of objects in the DAG and the way they're placed in a _packfile_. The key heuristic used when generating _packfiles_ is minimizing their size; objects are placed randomly throughout the pack, they are compressed, and crucially they're rarely stored whole. Most objects are stored as a delta on top of another object in the same packfile."
- **Our assessment**: This is the load-bearing technical premise for everything that follows in the post (why NFS/GFS/DRBD failed, why Spokes works at the packfile level rather than the filesystem level). It's a solid, verifiable claim about Git's on-disk format, not an opinion.

### Claim 2: GitHub's early attempts to scale Git hosting by distributing the *filesystem* underneath repositories (NFS, then GFS, then DRBD) each failed operationally, not just performance-wise
- **Evidence**: First-person historical account of GitHub's infrastructure evolution, framed as direct experience/institutional memory rather than external reporting.
- **Confidence**: settled (as a historical account) — presented as first-hand narrative, not sourced to public GitHub engineering blog posts within this article.
- **Quote**: "They all hit a wall. They were _terrible_ to operate day to day, and they didn't make up for it with good performance."
- **Our assessment**: Consistent with the packfile mechanics in Claim 1 — a random-access-heavy workload on a networked filesystem is a known anti-pattern, so the operational failure is plausible. We can't independently verify the NFS-specific claim ("It was slow, and it was buggy") since no incident data or citation is given.

### Claim 3: After giving up on filesystem-level distribution, GitHub built an RPC system so repositories could live on dedicated fileservers reached remotely from the Rails app — which improved horizontal scalability but did not fix availability or performance for the busiest repos
- **Evidence**: Historical narrative, no citation to external source.
- **Confidence**: settled (as historical account, unverified against a primary GitHub source within this article).
- **Quote**: "Eventually, the systems engineers at GitHub bit the bullet and gave up distributing the filesystem. They started developing an RPC system so that repositories could live on dedicated fileservers, and updated the Rails app to do all operations remotely. This provided a good chunk of horizontal scalability, but didn't fix their availability, nor the performance for the busiest repositories."
- **Our assessment**: Plausible intermediate step between filesystem distribution and Spokes; explains why Spokes (Claim 4) was needed even after the RPC system shipped.

### Claim 4: GitHub's Spokes system (~2013) became the industry-standard approach by making three specific design choices — operate at the packfile level (not the raw filesystem, not "distribute Git itself"), store real Git repos on local NVMe disks, and keep replicas consistently synced
- **Evidence**: Named system, approximate year, explicit enumeration of design choices.
- **Confidence**: settled — Spokes is a real, publicly known GitHub system; the three-part characterization is the author's summary of it.
- **Quote**: "It doesn't distribute Git itself; it works at the packfile level. It stores all data as actual Git repositories on local NVMe disks. It replicates the Git data, but keeps all copies consistently in sync."
- **Our assessment**: Useful frame — it names the specific layer (packfile) at which most successful Git-hosting-at-scale systems operate, which is the same layer Cursor's own Continuity (Claim 6) operates at.

### Claim 5: Spokes' three-phase-commit (3PC) consensus replication has two costs that get *worse*, not better, as you add replicas — push latency is bound by the slowest replica in the cluster, and push throughput degrades as replica count increases
- **Evidence**: Direct technical critique of the consensus mechanism's scaling properties.
- **Confidence**: settled — this is a standard, well-understood property of synchronous quorum/consensus replication (tail latency and throughput degrade with more voting members), not a novel finding.
- **Quote**: "the latency of every step is bound by the slowest of all the servers in the cluster" ... "The more replicas you add to a cluster, the worse push throughput gets."
- **Our assessment**: This is the article's central argument for why a non-consensus architecture (Continuity) is preferable for large replica counts. The critique is technically sound in general (it's a known consensus tradeoff) but the article gives no Spokes-specific benchmark numbers to back the magnitude of the degradation.

### Claim 6: Consensus-replicated systems like Spokes require an external database that tracks exactly where every repository lives, which adds an availability dependency and forces operators to treat individual repositories as "pets," not fungible "cattle"
- **Evidence**: Architectural critique of the operational model created by needing a routing/location database plus per-repo checksums.
- **Confidence**: settled (as an architectural tradeoff description).
- **Quote**: "you need to know exactly where every repository is. This adds a dependency (and a potential availability issue) on an external database" ... "You have to treat repositories as pets, not cattle."
- **Our assessment**: Reasonable critique of routing-table-based architectures in general; directly motivates Continuity's design choice (Claim 7) to make the write-ahead log itself the source of truth instead of a separate location database.

### Claim 7: Cursor's "Continuity" replaces consensus-based replica sync with a write-ahead log (WAL) stored in S3-compatible object storage as the sole source of truth; pushes are never acknowledged until fully persisted to the WAL, which forces all pushes to be linearizable
- **Evidence**: First-party architecture description of Cursor's own system.
- **Confidence**: emerging — this is a first-party, technically detailed disclosure of a system Cursor built and is now productizing, but it is not independently audited or benchmarked by a third party within this article.
- **Quote**: "The core primitive behind it is a write-ahead log, which we store in S3-compatible object storage." ... "We never acknowledge a push until it has been fully persisted." ... "This forces all pushes to be linearizable."
- **Our assessment**: Architecturally this sidesteps the 3PC latency/throughput problem in Claim 5 by removing peer-to-peer consensus entirely — durability is delegated to S3, and on-disk Git replicas become disposable. This is a real and coherent design pattern (log-as-source-of-truth, disk-as-cache), not just marketing language, but we have no independent verification of its correctness under real failure conditions (e.g., S3 partial outages, WAL replay bugs).

### Claim 8: Continuity treats on-disk Git repository replicas as a disposable "warm cache," not the source of truth — which lets replica count scale independently per repository (from hundreds of replicas for a hot monorepo down to a single replica, or zero via garbage collection, for an idle repo) without a routing database
- **Evidence**: Architecture description plus a worked example of the resulting operational behavior (garbage collection and lazy rematerialization from the WAL).
- **Confidence**: emerging — first-party design claim, plausible given Claim 7's WAL-as-source-of-truth premise, but unverified for the "millions of tiny repositories" case in practice.
- **Quote**: "We treat repositories like a warm cache on disk, but the source of truth is always the write-ahead log in S3." ... "A large monorepo can be deployed across hundreds of replicas to serve all the load from its CI jobs. Millions of tiny repositories created by agents can be served with one replica each; we don't need more than one to ensure availability, because S3 is the source of truth. In fact, an idle repository doesn't even need that: when a replica hasn't received traffic for a while, we garbage collect it from the node's disk, and simply materialize it again from the WAL the next time a fetch comes in."
- **Our assessment**: This is the claim most directly relevant to agent-native workflows — it explicitly names "millions of tiny repositories created by agents" as a distinct scaling case the architecture was designed for, separate from monorepo scaling. Worth flagging: the claim gives no data on how many such repos Cursor is actually hosting, or how the "garbage collect + rematerialize from WAL" path performs under real fetch latency requirements.

### Claim 9: Continuity sustains up to 120 pushes/second on standard S3 storage while compacting and replicating, and over 300 pushes/second on S3 Express One Zone, where the ceiling is set by Git's own on-disk compaction speed rather than the storage layer
- **Evidence**: Vendor-reported throughput numbers; no benchmark methodology (cluster size, repo size/shape, hardware, measurement window) is disclosed in the passages retrieved.
- **Confidence**: anecdotal — single-source, unaudited vendor performance numbers with no disclosed methodology.
- **Quote**: "we can sustain up to 120 pushes/s while compacting and replicating" ... "we can ingest more than 300 pushes/s"
- **Our assessment**: These are the headline performance numbers of the post but are the least verifiable claims in it — no comparison baseline (e.g., Spokes' own push throughput under 3PC) is given, so "faster than Spokes" is implied but not directly demonstrated with matched benchmarks. Treat as a vendor-reported ceiling, not an independently confirmed figure.

### Claim 10: The post explicitly frames agent-driven development as having made Git hosting reliability *harder*, citing "more code, more PRs, more CI runs" as the motivating pressure behind building a new hosting platform ("Origin")
- **Evidence**: Closing-section framing statement, presented without supporting metrics (no agent-specific commit/PR/CI volume data given).
- **Confidence**: anecdotal — a motivational/marketing claim, not a measured one.
- **Quote**: "Agents have fundamentally changed the way we work with software, and in many ways they've made this situation worse. More code, more PRs, more CI runs."
- **Our assessment**: This is the article's explicit tie-back to AI-native engineering, but it's asserted rather than evidenced — no numbers on how much agent adoption increased PR/commit/CI volume at Cursor or its customers. Directionally consistent with `blog-cursor-agent-swarm-model-economics.md` Claim 4 (see Cross-References), which *does* quantify a related but distinct throughput pressure.

### Claim 11: The article frames three possible Git-hosting scaling strategies "in increasing order of complexity" — distribute the filesystem, distribute the packfiles, or distribute Git itself — but only the first two are explored in the retrieved content; "distribute Git itself" is named and never elaborated
- **Evidence**: Direct textual/structural observation of the essay's own stated framework versus its actual content.
- **Confidence**: settled — this is a direct observation about the article's structure, not an inference.
- **Quote**: "There are broadly three possible approaches to accomplish this, in increasing order of complexity: distribute the filesystem, distribute the packfiles, or distribute Git itself."
- **Our assessment**: Worth flagging explicitly: readers should not treat this post as an exhaustive survey of Git-hosting-at-scale strategies. The unaddressed third approach ("distribute Git itself") is conceptually adjacent to Cursor's own from-scratch, non-Git version-control system for agent swarms described in `blog-cursor-agent-swarm-model-economics.md` Claim 4 — but this article never draws that connection or elaborates on the option at all.

### Claim 12: The article asserts, without citation, that "the average repository for an enterprise company is now a massive monorepo"
- **Evidence**: Unsupported industry-trend assertion used to justify why per-repository replica scaling (rather than sheer repo count) matters most.
- **Confidence**: anecdotal — no data, survey, or citation backs this claim.
- **Quote**: "The average repository for an enterprise company is now a massive monorepo"
- **Our assessment**: Should be treated as rhetorical framing rather than a measured industry fact. It sits in tension with Claim 8's own example of "millions of tiny repositories created by agents" — the article wants both a monorepo-scaling story and a many-tiny-repos-scaling story to be true simultaneously, and doesn't reconcile which is more representative of "the average" case.

## Concrete Artifacts

```
Packfile internals (why networked filesystems fail for Git), from the article:

"There is no correlation between the layout of objects in the DAG and the
way they're placed in a packfile. The key heuristic used when generating
packfiles is minimizing their size; objects are placed randomly throughout
the pack, they are compressed, and crucially they're rarely stored whole.
Most objects are stored as a delta on top of another object in the same
packfile."

"This kind of random walk across gigabytes of data, which must happen for
every single Git operation performed on a repository, just doesn't play
well with a networked filesystem (whether it replicates at the file or at
the block level)."
```

```
Spokes' three defining design choices (GitHub, ~2013), from the article:

"It doesn't distribute Git itself; it works at the packfile level. It
stores all data as actual Git repositories on local NVMe disks. It
replicates the Git data, but keeps all copies consistently in sync."

Structural costs of Spokes' 3PC consensus as replica count grows:
- "the latency of every step is bound by the slowest of all the servers
  in the cluster"
- "The more replicas you add to a cluster, the worse push throughput
  gets"
- "you need to know exactly where every repository is. This adds a
  dependency (and a potential availability issue) on an external
  database"
- "You have to treat repositories as pets, not cattle"
```

```
Continuity (Cursor's replacement architecture) — WAL-in-S3 design and
measured throughput, from the article:

"The core primitive behind it is a write-ahead log, which we store in
S3-compatible object storage."
"We never acknowledge a push until it has been fully persisted."
"This forces all pushes to be linearizable."
"We treat repositories like a warm cache on disk, but the source of
truth is always the write-ahead log in S3."

Throughput:
- S3 Standard: "we can sustain up to 120 pushes/s while compacting and
  replicating"
- S3 Express One Zone: "we can ingest more than 300 pushes/s"
  (bottleneck stated as Git's own on-disk compaction speed, not storage)

Replica scaling behavior:
"A large monorepo can be deployed across hundreds of replicas to serve
all the load from its CI jobs. Millions of tiny repositories created by
agents can be served with one replica each; we don't need more than one
to ensure availability, because S3 is the source of truth. In fact, an
idle repository doesn't even need that: when a replica hasn't received
traffic for a while, we garbage collect it from the node's disk, and
simply materialize it again from the WAL the next time a fetch comes
in."
```

```
Closing motivation for "Origin" (Cursor's git hosting platform), from the
article's final section:

"Agents have fundamentally changed the way we work with software, and in
many ways they've made this situation worse. More code, more PRs, more
CI runs. Version control is at the core of all of this, and it is
possibly the hardest thing to change overnight."

"Origin is not an experiment; it is the result of many decades of
experience building these same systems, from people who deeply
understand the magnitude of the challenges involved."
```

## Cross-References

- **Corroborates**: `docs-ghaw-guides-using-at-scale.md` Claim 3 (sparse
  `checkout:` on large monorepos cuts checkout time from tens of minutes to
  seconds) corroborates, at a different layer, that monorepo scale is a real
  friction point for agent-driven Git workflows — that note covers
  client-side checkout cost, this one covers server-side hosting/replication
  cost, but both point at the same underlying problem (Git's assumptions
  strain at monorepo scale).
- **Contradicts**: None found. No existing source note makes a claim about
  Git server-hosting architecture, packfile replication, or consensus vs.
  WAL tradeoffs that this post disagrees with.
- **Extends / distinguishes from**: `blog-cursor-agent-swarm-model-economics.md`
  Claim 4 describes a *different* Cursor system: a from-scratch version
  control system built to replace Git entirely inside a single agent swarm's
  working tree, because "Git/Cargo's coarse locks are unworkable" at
  swarm-internal contention levels — reaching roughly 1,000 commits/second
  for that swarm's own commit stream. This article's "Continuity" is not
  that system: it is a server-side replication/hosting layer that still
  stores and serves real Git packfile repositories, measured in pushes/second
  across a hosting fleet (120–300/s), not commits/second inside one
  contended working tree. This directly answers the Prospector's triage
  question ("How does it differ from the custom VCS work documented in
  Cursor's agent-swarm post?") — the two are complementary systems at
  different layers (intra-swarm working-tree coordination vs. fleet-wide Git
  hosting), not the same system described twice, and their throughput
  numbers are not directly comparable units.
- **Novel**: The packfile-internals explanation (Claim 1), the Spokes 3PC
  cost analysis (Claim 5–6), and the WAL-in-S3 hosting architecture
  (Claims 7–9) are all new to the corpus — no existing source note covers
  Git server-hosting architecture, packfile replication mechanics, or
  consensus-vs-log-based replication tradeoffs at all.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The existing "Git Worktrees for
  Parallel Work" section (guide/02-harness-engineering.md, ~line 1288)
  covers *local*, single-machine worktree isolation for parallel agent
  sessions — a client-side concern. This source is entirely about
  server-side Git hosting infrastructure (packfile replication, push
  throughput at a fleet level) and does not change that section's advice.
  It would only become guide-relevant if the guide adds a section on
  operational symptoms of agent-driven Git load at the hosting-platform
  level (e.g., "if your team is hitting Git hosting throughput ceilings
  because of agent-driven PR/commit volume, here's what's actually
  happening under the hood") — and even then, the specific throughput
  numbers (120/300 pushes/s) should be cited as vendor-reported and
  unaudited (Claim 9), not as settled benchmarks.
- **Chapter 05 (Team Adoption)**: The chapter already frames agents as
  "throughput infrastructure" (~line 1337) and discusses review-throughput
  bottlenecks. This source's Claim 10 (agents increase PR/commit/CI volume
  enough to stress Git hosting itself) is a plausible extension of that
  framing but is asserted, not measured, in this source — recommend NOT
  citing it as evidence of a real infrastructure bottleneck without a more
  quantified source; it's better used as a "watch for this" flag than a
  settled recommendation.

## Extraction Notes

- Fetched via `WebFetch`, which returns AI-summarized/paraphrased content
  rather than raw HTML, so this note was built from eight separate
  targeted fetches, each asking for verbatim text of a specific section
  (opening/thesis, three-approaches framing, Spokes history and design,
  3PC drawbacks, Continuity architecture and metrics, the "millions of
  tiny repositories" paragraph in full context, packfile internals, and
  the Origin/agents closing section). Every `Quote` field above was cross-
  checked against these targeted verbatim fetches, not the initial
  one-shot summary fetch.
- The article is a single long-form post (27-minute read), not a docs tree
  with linked sub-pages — there were no substantive linked sub-pages to
  follow per MINER.md §1.
- Two explicit gaps in the source itself, both called out above: the
  "distribute Git itself" third scaling approach (Claim 11) is named but
  never elaborated in the retrieved content, and no author bio/credential
  statement is given beyond the byline and one aside referencing a "former
  mentor" (Claim/Source Context notes).
- No contradiction with any existing source note was found, so no
  contradiction issue was filed per MINER.md §4a.
