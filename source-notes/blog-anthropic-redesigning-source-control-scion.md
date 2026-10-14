---
source_url: https://www.anthropic.com/engineering/redesigning-source-control
source_type: blog-post
title: "Redesigning source control at Anthropic"
author: Nick G. and the Anthropic source control team
date_published: 2026-10-13
date_extracted: 2026-10-14
last_checked: 2026-10-14
status: current
confidence_overall: anecdotal
issue: "#4097"
---

# Redesigning source control at Anthropic

> Anthropic's first-party account of replacing git with an in-house, always-online, server-centric VCS (Scion) once merges grew from ~2,500/day to 30,000+/day, with vendor-reported infrastructure results and observations on how a seven-person team worked with Claude to build it.

## Source Context

- **Type**: blog-post (anthropic.com/engineering, published Oct 13, 2026)
- **Author credibility**: Written by "Nick G. and the source control team" (seven named-by-initial/first-name engineers). Primary source, first-hand operators of the system. Single-organization, internal workload; no code, benchmarks, or third-party validation published.
- **Scope**: Covers why git stops fitting at Anthropic's monorepo scale, Scion's principles and architecture (changesets, derived data, tiered daemon/cache/server), results, and lessons about agent-assisted development (team size, human role, testing, monitoring, merge queues). Does NOT cover Antique (code review) in depth, does not publish the protocol, and explicitly says Scion is not offered externally.

## Extracted Claims

### Claim 1: At Anthropic the bottleneck has moved from writing code to developer infrastructure built for human scale
- **Evidence**: Self-reported merge-rate growth: ~2,500 changes merged/day in May 2026 to 30,000+/day by September (chart of merges per day, Jan–Sep 2026).
- **Confidence**: anecdotal
- **Quote**: "The bottleneck, now, is all of the developer infrastructure built for human scale: source control, builds, and CI."
- **Our assessment**: Strong framing, consistent with the CI-side account in `blog-anthropic-ci-test-impact-analysis-scaling.md`. Applies to an extreme-volume vendor; treat as a leading indicator rather than a general finding.

### Claim 2: Removing a bottleneck immediately raises code output, so demand for merging is effectively unbounded
- **Evidence**: Authorial assertion backed by the 10x+ merge growth.
- **Confidence**: anecdotal
- **Quote**: "the latent demand for merging code is practically infinite, and every bottleneck we remove immediately leads to a further increase in the amount of code we produce."
- **Our assessment**: Plausible induced-demand dynamic; no data on quality or value of the added merges is given.

### Claim 3: Git's decentralized, offline-capable design mismatches a workload where nearly all clients are always-online agents and jobs
- **Evidence**: ~100 GB main-branch history, >25 GB compressed working copy, ~25M CI checkouts/day (>600 PB/day if fetched naively); several hundred internal git mirrors at peak; seeds drifting from tip; partial clones breaking diff/blame.
- **Confidence**: anecdotal
- **Quote**: "we were using git as a centralized system with one authoritative copy, but nearly all of our clients were agents and jobs that are online by definition."
- **Our assessment**: Credible for their scale. The post concedes git is "the right design" for the vast majority of repositories, so this is not an anti-git general claim.

### Claim 4: Scion is built on six design principles (always-online clients, client-server asymmetry, source control as API, horizontal scalability with no packfiles, cheap lock-free server-side commits, optional sparse working copy)
- **Evidence**: Architecture description; prior art acknowledged (Google Piper, Meta Sapling).
- **Confidence**: emerging
- **Quote**: "The working copy is optional, and sparse by design."
- **Our assessment**: Useful checklist for what "agent-facing infrastructure" means for the VCS layer. Not independently verifiable (closed system).

### Claim 5: Exposing all source-control queries as an API lets CI and tools skip local repos and enables tooling like automated bisect and revert
- **Evidence**: Description of CI jobs asking the server for merge-base diffs; examples of bisect/revert pipelines.
- **Confidence**: anecdotal
- **Quote**: "Many internal tools, such as our automated bisect and revert pipelines, wouldn’t be practical at scale without this cheap, programmatic access to source control."
- **Our assessment**: A concrete case of "give agents/tools a query API instead of a filesystem copy." No measurements specific to this effect.

### Claim 6: Server-side changesets plus recursively-defined derived data remove packfiles, locks, and ref contention
- **Evidence**: Changesets are write-ahead-log entries storing changed files vs. first parent and content-addressed blob pointers; blame, path history, and commit-graph skip lists are "derived data" computed from parents; ref moves are a compare-and-swap on a single Spanner row.
- **Confidence**: anecdotal
- **Quote**: "Each type of derived data is defined recursively, so its value for a changeset is computed from its values for that changeset’s parents."
- **Our assessment**: Design detail, interesting but infrastructure-specific; relevant to guide mostly as evidence for how far agent-scale redesign goes.

### Claim 7: A tiered daemon → cache → server protocol over immutable content-addressed objects delivers large efficiency gains
- **Evidence**: Vendor-reported: cache hit rates over 99% per tier; infrastructure 200x smaller (CPU+memory) than prior git mirrors; checkouts "two orders of magnitude faster" (seconds vs. minutes); 25% CI CPU capacity win.
- **Confidence**: anecdotal
- **Quote**: "Our Scion infrastructure footprint is now 200x smaller than our previous git mirroring infrastructure in terms of CPU and memory requirements."
- **Our assessment**: Impressive but self-reported, with no methodology or baseline detail (mirror fleet had become a strained baseline). Cite as vendor-reported.

### Claim 8: Claude rewrote a handwritten ingestion pipeline prototype to use 20x less memory and run 4x faster
- **Evidence**: Single anecdote about an early internal snapshot of Claude Mythos Preview, given no further instructions, preserving "implicit invariants around ingestion ordering and data structures."
- **Confidence**: anecdotal
- **Quote**: "it produced a version that consumed 20x less memory and was 4x faster, while preserving all of the implicit invariants around ingestion ordering and data structures."
- **Our assessment**: Vendor self-report of an unreleased model; one data point, no verification method described. Do not generalize to released models.

### Claim 9: A seven-person team built and migrated to Scion and Antique in five months while merge volume rose 10x
- **Evidence**: Team and timeline stated; "half a dozen related systems" also built.
- **Confidence**: anecdotal
- **Quote**: "A team of seven people built both Scion and Antique (our code review tool, which we could easily write a whole other blog post about), not to mention half a dozen related systems, and fully migrated to them in five months."
- **Our assessment**: Notable team-size/pace claim, but the team is at an AI lab with token spend the authors say exceeds what other businesses would spend, which limits transferability.

### Claim 10: The engineer's role shifted to telling the agent "no" — preventing agents from violating system constraints and from over-engineering in response to adversarial review
- **Evidence**: Two examples: systems brute-forcing "when a change merged to main" by linearly reading the commit log instead of asking the code review tool; an adversarial review that was overly defensive about trusting another internal service, leading Claude to add excessive validation.
- **Confidence**: anecdotal
- **Quote**: "Very often, we found that the role of the engineers was to tell Claude “no.”"
- **Our assessment**: Specific, useful failure modes (shortcut-seeking against architecture; adversarial review myopia). Corroborates the need for human design-level judgment.

### Claim 11: Human review shifted from reading every line to examining intent, while every change request is still reviewed
- **Evidence**: Authorial statement about the team's practice; semantic approval constraints in code review distinguish comment-only from sensitive logical changes.
- **Confidence**: anecdotal
- **Quote**: "Our team members still review every change request for the system, but they now examine the intent of the change as opposed to reading every line of code."
- **Our assessment**: Notable review-practice data point; supported by extensive hermetic simulation/fuzzing (Claim 12) as compensating controls. Single team.

### Claim 12: Cheap code generation yielded unusually thorough testing: hermetic simulations, fuzzing, rate limiting, and agent-discovered optimizations
- **Evidence**: Authors' assertion; example of an algorithmic optimization to ancestry queries that missed an index, which "would have taken an expert days or weeks."
- **Confidence**: anecdotal
- **Quote**: "Scion is among the most well-tested and well-defended codebases we have ever worked on."
- **Our assessment**: Plausible "spend the saved effort on verification" pattern; no defect or coverage metrics given.

### Claim 13: Directory-level permissions and semantic approval constraints let a monorepo protect sensitive code without losing monorepo benefits
- **Evidence**: Feature description only.
- **Confidence**: anecdotal
- **Quote**: "It supports rich access control on repositories, as well as the ability to apply permissions to individual directories in order to protect the most sensitive code without losing the benefits of a monorepo."
- **Our assessment**: Capability description with no operating detail; mainly signals the direction for agent-scale governance.

### Claim 14: Per-component "superfan" Claude agents in Slack monitor telemetry and catch subtle issues that traditional alerts miss
- **Evidence**: Examples: scion-daemon, scion-cache, and Antique merge queue superfans with access to telemetry and logs; traditional alerts kept alongside.
- **Confidence**: anecdotal
- **Quote**: "we created Slack channels where we tasked Claude with being obsessively focused on the health of a single component."
- **Our assessment**: A concrete monitoring pattern; no detection-rate data. Pairs with the long-lived monitoring session in the CI test-impact note.

### Claim 15: Global-lock merge queues stop making sense at agent scale; Anthropic relies on post-merge and pre-deploy testing and agent conflict repair
- **Evidence**: Stated as Anthropic's current practice after being unable to replicate a global repository lock on the merge queue.
- **Confidence**: anecdotal
- **Quote**: "A proper merge queue, for example, doesn’t make much sense at agent scale."
- **Our assessment**: Counter-conventional; accepts concurrent conflicts and relies on Claude to fix them. Risky for teams without Anthropic's testing depth; present as one org's choice, not a recommendation.

### Claim 16: Scion is not a general git replacement; the transferable ideas are server-side RPCs, different negotiation, and composable sparse/shallow features
- **Evidence**: Authors' explicit scoping; expectation that this class of problem becomes common "over the next six to 12 months."
- **Confidence**: anecdotal
- **Quote**: "Scion is by no means a suitable replacement for git for general use."
- **Our assessment**: Honest scoping that should be preserved in any guide citation.

## Concrete Artifacts

Metrics as reported (vendor self-report, Anthropic engineering blog, Oct 13, 2026):

```
Merges/day:            ~2,500 (May 2026) -> 30,000+ (Sept 2026)
Main-branch history:   almost 100 GB; compressed working copy > 25 GB
CI checkouts/day:      ~25 million (naive git fetch: >600 PB/day)
Git mirrors (peak):    several hundred
Cache hit rate:        >99% per tier
Infra footprint:       200x smaller than prior git mirror fleet (CPU, memory)
Checkout time:         two orders of magnitude faster (seconds vs. minutes)
CI CPU capacity:       25% win
Ingestion rewrite:     20x less memory, 4x faster (Claude Mythos Preview)
Team / timeline:       7 people, 5 months
```

Component tiers named in the post: `scn` (client) -> `scion-daemon` (per node) -> `scion-cache` (regional) -> `scion-server` (authoritative; Spanner/cloud storage). Tiering is strictly enforced "to isolate failure domains."

## Cross-References

- **Corroborates**: `blog-anthropic-ci-test-impact-analysis-scaling.md` (Claim 1: CI load growth from agentic coding; Claim 11: plan for exponential load growth) — same pressure from the CI side, this post from the source-control side. `blog-anthropic-claude-oncall-cicd.md` (Claim 16: ~8x code shipped per quarter) — consistent scale-up narrative.
- **Contradicts**: None filed. Tension to note, not a formal contradiction: Claim 15 (no global merge-queue lock) vs. conventional CI-gated merge guidance in the guide; context differs (extreme volume), so it is a conditioning variable.
- **Extends**: `blog-anthropic-large-codebase-best-practices.md` (Claim 1, Claim 15) — that note covers Claude Code usage and rollout in large codebases; this post covers the underlying VCS infrastructure that note does not address.
- **Novel**: Agent-first VCS design (changesets, derived data, tiered checkout protocol), API-first source control for CI, merge-queue rethink, "superfan" component monitors, and the human "tell Claude no" role with concrete failure examples. No existing note covers Scion or Antique.

## Guide Impact

- **Chapter 02**: In the Monorepo Patterns section, add a short note (vendor-reported, citing this source) that at extreme agent scale source control and checkout cost become the bottleneck, and that server-side query APIs plus sparse/virtual checkouts avoid per-job full clones. Keep the author's caveat that this applies only to enormous monorepos.
- **Chapter 05**: Cite the seven-person/five-month migration and "engineers tell Claude no" examples as an anecdotal data point on team shape and the human role; flag that token budget is atypical.
- **Chapter 06**: Cite directory-level permissions and semantic approval constraints (comment-only vs. logic changes) as an example of monorepo governance for agent-written code.
- **Chapter 03**: Cite the 25M checkouts/day, 25% CI CPU win, and post-merge/pre-deploy testing instead of a global merge lock as an example of rethinking CI at agent scale, alongside `blog-anthropic-ci-test-impact-analysis-scaling.md`.

## Extraction Notes

- Read the full article text (fetched raw HTML, stripped to text); quotes copied from that text. Charts/diagrams are images and not captured beyond their captions.
- No sub-pages followed; the post links no substantive further pages on Scion. Antique is mentioned but not detailed.
- All metrics are vendor-reported; no methodology, baselines, or code published. The 20x/4x rewrite concerns an unreleased internal model snapshot.
- No contradiction issue filed; the merge-queue point is context-dependent.
