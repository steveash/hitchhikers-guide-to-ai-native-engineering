---
source_url: https://openai.com/index/scaling-git-at-openai
source_type: blog-post
title: "Scaling Git at OpenAI"
author: Aaron Friel, Taylor Blau, Ted Nyman (OpenAI)
date_published: 2026-11-02
date_extracted: 2026-11-23
last_checked: 2026-11-23
status: current
confidence_overall: anecdotal
issue: "#4909"
---

# Scaling Git at OpenAI

> OpenAI's first-party account of Pando, a Git-protocol-compatible backend that coordinates writes per branch (causal consistency) and serves reusable, cached packfiles, built because Codex-driven parallel work overloaded the monorepo's Git infrastructure; all production numbers are vendor-reported.

## Source Context

- **Type**: blog-post (openai.com/index, Engineering, published Nov 2, 2026)
- **Author credibility**: Three OpenAI Members of Technical Staff, including Taylor Blau (known Git upstream contributor). First-party operators of the system; no independent verification.
- **Scope**: Why the monorepo's Git service failed under agent-scale concurrency, two modeled alternatives (3PC, WAL), Pando's design (ref versions, trunk-only advertisement, packfile reuse via `packfile-uri`, LSM-style compaction), how it was built with Codex and migrated, and upstream Git contributions. Does not give production benchmark methodology; the three-architecture comparison is an interactive simulation, not production data. The closing "What's next" section was not captured in extraction.

## Extracted Claims

### Claim 1: Codex-driven parallelism overloaded the monorepo's Git serving layer
- **Evidence**: First-party description; reliability "at times falling below 90%" with slow fetches/pushes and failed merges. No time series or methodology.
- **Confidence**: anecdotal
- **Quote**: "One engineer now has several changes ready for CI at once, and each push can set several jobs fetching the same commit."
- **Our assessment**: Concrete causal mechanism (multiplied branches × CI fetch fan-out). Plausible and consistent with Anthropic's Scion account; the <90% figure is unquantified.

### Claim 2: Keep the Git protocol and client; rebuild only the backend
- **Evidence**: Design decision; Pando "now powers all development in OpenAI's monorepo" without changing how engineers use Git.
- **Confidence**: anecdotal
- **Quote**: "We met these goals while retaining compatibility with the Git protocol and client, enabling both our engineers and agents to seamlessly adopt Pando into their existing workflows."
- **Our assessment**: Directly opposite design choice to Anthropic's Scion (new VCS). Not a contradiction (different constraints) but a useful fork-in-the-road for the guide.

### Claim 3: Per-branch independent write coordination lets unrelated pushes proceed in parallel, at the cost of cross-ref point-in-time consistency
- **Evidence**: Design: each push stores an immutable pack in a blob store and records a "ref version" in a metadata store; only the ref pointer is contended, guarded by compare-and-swap-like operation.
- **Confidence**: anecdotal
- **Quote**: "The tradeoff is that a reader looking at several branches can see them at different points of time."
- **Our assessment**: Clearly stated tradeoff; the authors argue "users and agents are agnostic to the global ordering of ref updates". Reasonable but an untested assumption for agents that reason across multiple branches.

### Claim 4: Reusing packfiles across fetches, instead of per-client packs, scales reads
- **Evidence**: Pando serves stored packs via `packfile-uri` (inline pack empty), regional caches, consistent hashing to "Express" pack servers; >99% cache hit; clone/fetch saturate 10 Gbps links on standard cloud VMs (stated as validated).
- **Confidence**: anecdotal
- **Quote**: "A client may download some objects it already has, but the server can serve the same bytes to many clients with little computation."
- **Our assessment**: Sound trade (bandwidth for CPU) and fits fan-out of CI jobs fetching the same commit.

### Claim 5: Advertising only a trunk branch on push keeps advertisements small and packs reusable, but makes stacked/repeated branch pushes larger
- **Evidence**: With millions of branches ref advertisement can exceed 100 MiB; in OpenAI's monorepo median push pack <20 KiB, p99 <3 MiB.
- **Confidence**: anecdotal
- **Quote**: "This causes successive branch pushes to be larger, containing potentially-redundant objects, and uses additional client bandwidth."
- **Our assessment**: Explicit, quantified tradeoff — rare in vendor posts. Relevant to agents that push the same branch repeatedly or stack branches.

### Claim 6: Conventional scaling patterns (3PC replication, WAL-in-blob-store manifest) bottleneck on a single coordination point
- **Evidence**: Modeled (not necessarily deployed) designs; simulation with 1,000 clients each pushing to a distinct branch, hardware commodity→premium. Results are only in an interactive widget, not in text.
- **Confidence**: anecdotal
- **Quote**: "Waiting for a quorum puts replica disk performance and communication latency on the push path."
- **Our assessment**: Simulation authored by the system's builders; treat as illustration, not benchmark. Authors note they "relaxed repository-wide consistency for three-phase commit" in the simulation.

### Claim 7: LSM-style compaction of per-push packs makes fetch planning sub-linear in how far behind a client is
- **Evidence**: L0 packs per push, geometric "covers" up to L4 in the monorepo; without it a client would download tens of thousands of packs daily; packs at all levels retained.
- **Confidence**: anecdotal
- **Quote**: "Each day, a client would need to download tens of thousands of packfiles to catch up their trunk."
- **Our assessment**: Detailed, technically coherent; no before/after numbers.

### Claim 8: Reported production results: median push latency down ~5x (~80%), ~1 PB/day, 57 TB in one hour with >99% from local cache
- **Evidence**: Vendor-reported. Note the intro says "nearly 5x" and the body says "nearly 80%"; these are arithmetically equivalent (an 80% reduction is a 5x speedup), so not an inconsistency despite the triage flag, though phrasing differs. No baseline or measurement window.
- **Confidence**: anecdotal
- **Quote**: "Pando has served more than 57 terabytes of Git packs in a single hour, with more than 99% of those bytes from local disk cache."
- **Our assessment**: Cite as vendor-reported. "Petabyte per day with just a handful of CPU cores" is for a single repository per the authors.

### Claim 9: Pando was built with Codex in 10 weeks: one engineer designed the core, teams of agents implemented it
- **Evidence**: Self-report. Validation: conformance test suite against standard Git behavior, deterministic simulation testing, Lean/TLA+ formal models written by agents, multi-hundred-hour continuous agent sessions, round-the-clock red-teaming agents.
- **Confidence**: anecdotal
- **Quote**: "The core of Pando was designed by a single engineer, implemented by teams of agents, and deployed by a handful of engineers."
- **Our assessment**: Parallels Anthropic's Scion account (small team, agent-built, heavy simulation testing). The conformance suite "so agents could test their changes against standard Git behavior" is a reusable pattern: an executable spec for agents.

### Claim 10: Migration used a read/write-through proxy, phased client rollout via a Git CLI wrapper, and Codex skills to migrate developer checkouts
- **Evidence**: Self-report: hundreds of integrations (APIs, webhooks, repo downloads) migrated; OpenAI Git build shipped to dev machines and ChatGPT desktop app.
- **Confidence**: anecdotal
- **Quote**: "As a result, developers could simply ask Codex to migrate their development environments and services."
- **Our assessment**: Concrete example of agent-assisted internal migration via skills; no adoption or failure data.

### Claim 11: Upstream Git contributions: packfile-uri fixes, tracing, parallel pack download/indexing, and "explicit haves" enabling `--force-with-lease`
- **Evidence**: Described fixes for concurrent downloads, interrupted-transfer cleanup, resume; several "already in upstream Git", others in OpenAI's public repo.
- **Confidence**: anecdotal (verifiable via public patch tracker, not checked)
- **Quote**: "Several of these improvements are already in upstream Git, and many others in our public repository."
- **Our assessment**: Verifiable in principle; lowers the "vendor lock-in" concern of the design.

## Concrete Artifacts

```
Pando design summary (from "Architecting Pando" / "Scaling pushes" sections)
- Push: pack stored as immutable blob; metadata store records
  ref version = {new tip, pack, earlier ref versions pack depends on}
- Only contended key: ref pointer (compare-and-swap-like)
- Advertise on push: designated trunk branch only (by default)
- Fetch: map haves/wants -> ref versions -> stored packs; deliver via
  packfile-uri with an empty inline packfile
- Compaction: L0 per push, geometric covers up to L4 in monorepo
Reported numbers (vendor-reported): median push pack <20 KiB, p99 <3 MiB;
ref advertisement can exceed 100 MiB at millions of branches;
cache hit >99%; 57 TB packs/hour; ~1 PB/day; build time 10 weeks;
production traffic since April 2026.
```

## Cross-References

- **Corroborates**: `blog-anthropic-redesigning-source-control-scion.md` Claim 3 and Claim 6: agent-scale concurrency breaks Git-era infrastructure, and ref moves reduce to a compare-and-swap on a single key (Scion uses a single Spanner row; Pando a ref pointer). Claim 7 there reports >99% cache hit rates per tier, similar to Pando's >99%.
- **Contradicts**: None filed. Choices differ (Anthropic replaced Git; OpenAI kept the protocol/client, see Scion Claim 16 on Scion not being a general Git replacement), but these are different constraints, not opposing claims.
- **Extends**: `blog-google-abfs-massive-git-repositories.md` Claim 2 and Claim 7: ABFS addresses cold-start of many parallel workspaces on the client/filesystem side; Pando addresses the server side of the same fan-out (many pushes, many fetches of the same commit).
- **Novel**: Causal-consistency ref versions with trunk-only advertisement; explicit quantified tradeoff (larger stacked-branch pushes); packfile-uri-only serving with LSM-style compaction; conformance suite + formal models (Lean/TLA+) as agent validation for a greenfield infrastructure system.

## Guide Impact

- **Chapter 01**: Where concurrent sessions/worktrees are discussed, add a note that many parallel agent branches and CI fetches can overload the Git server side, citing this source (vendor-reported) alongside the Scion note.
- **Chapter 02**: Add "executable conformance suite against reference behavior" as a harness pattern for agents building compatible reimplementations (Claim 9).
- **Chapter 05**: Add the migration pattern (write-through proxy, CLI wrapper phased rollout, Codex skills to migrate checkouts) as a team-adoption example (Claim 10), flagged as self-reported.

## Extraction Notes

- Read the full article body via direct HTML fetch (WebFetch only returned a summary). Interactive simulation widgets contain no extractable result numbers. The final "What's next" section text was not captured. No sub-pages followed.
- Triage comments flagged a "5x vs 80%" inconsistency; these are equivalent, recorded in Claim 8.
- The article mentions models "GPT-6 Astra" and "Daybreak-capable models" without elaboration.
- All claim cross-reference numbers were checked against the numbered headings in the cited notes.
