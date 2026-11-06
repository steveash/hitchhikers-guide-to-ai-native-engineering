---
source_url: https://blog.jetbrains.com/ai/2026/11/building-a-rag-pipeline-for-semantic-code-search-a-developer-diary-and-field-notes-part-2/
source_type: blog-post
title: "Building a RAG Pipeline for Semantic Code Search: A Developer Diary and Field Notes (Part 2: Storage, Search, and Agent Tooling)"
author: Eduard Gurskiy and Evgeny Abramov (JetBrains)
date_published: 2026-11-05
date_extracted: 2026-11-06
last_checked: 2026-11-06
status: current
confidence_overall: emerging
issue: "#4556"
---

# Building a RAG Pipeline for Semantic Code Search — Part 2: Storage, Search, and Agent Tooling

> First-party JetBrains account of the storage and retrieval layer of Air Context (a production code-RAG system): filtered ANN strategies, Merkle-tree incremental indexing, local+remote cascade search, reranking, a capped-step retrieval sub-agent, and relevance-tiered result formatting — all design description, with no published recall/latency/cost numbers.

## Source Context

- **Type**: blog-post (JetBrains AI blog, 2026-11-05; Part 2 of a series; follows `blog-jetbrains-rag-semantic-code-search.md`, which covered chunking/parsing/vectorization)
- **Author credibility**: JetBrains engineers describing a shipped system ("Air Context is in public preview and already included with your JetBrains AI subscription"). Vendor-authored; no independent verification. Note the product is called "Air Context" here, whereas Part 1 called it "JetBrains Context".
- **Scope**: Covers storage (ANN, filtering, incremental indexing, sharding, local indexes) and retrieval (reranking, agentic search, result formatting). Does NOT cover evaluation: the author explicitly defers "does any of this actually help the agent?" to Part 3. The only number anywhere is a teaser: "agents with Air Context needed up to 70% fewer turns to solve a task" (unsubstantiated in this post). Embedded diagrams, if any, are not extractable as text.

## Extracted Claims

### Claim 1: Approximate (ANN) search combined with an exact pass over the shortlist works better than ANN alone
- **Evidence**: Practitioner report; no recall figures.
- **Confidence**: anecdotal
- **Quote**: "We found that a hybrid approach, in which we also employ exact search over a more limited vector space following the initial ANN search, works remarkably well."
- **Our assessment**: Standard retrieve-then-rescore pattern; plausible but unmeasured here.

### Claim 2: Filters (repo, branch, subfolder, permissions) must be deterministic and cannot be left to similarity search; combining filters with HNSW is "genuinely hard"
- **Evidence**: Technical argument about graph connectivity.
- **Confidence**: settled (well-known ANN property)
- **Quote**: "the moment you constrain traversal to nodes that satisfy a predicate, the graph can become disconnected and the walk can miss valid candidates."
- **Our assessment**: Sound and generally accepted in vector-DB engineering.

### Claim 3: Of three filtered-ANN strategies, bundling metadata in the index is the best general-purpose choice for ACL-constrained code search; pre-filter suits narrow filters; post-filter is weakest
- **Evidence**: Design reasoning; names Qdrant and turbopuffer as index-integrated filtering stores and pgvector iterative-scan as a post-filter mitigation. No benchmark.
- **Confidence**: emerging
- **Quote**: "Post-filtering is considered to be the weakest of the three strategies."
- **Our assessment**: Pre-filter: "100% recall relative to the filter" but falls back to exact search, good for "a single small repo or a narrow subfolder". Bundled: "For a production codebase RAG with real ACL requirements, this would be a balanced choice." Likely generalizes to any multi-tenant/permissioned retrieval, but conclusion is conditioned on ACL needs and filter selectivity (a conditioning variable, not a contradiction).

### Claim 4: Indexing must be incremental; each snapshot is clustered into a Merkle tree mirroring the directory structure, with unchanged subtrees relinked and embeddings deduplicated by chunk-content hash
- **Evidence**: Architecture description. Phrased conditionally ("Ideally, we'd want... we would only index the changed code"), so it is unclear how fully this is realized.
- **Confidence**: emerging
- **Quote**: "New revisions are diffed from the top down, and entire unchanged subtrees are linked to the new snapshot as-is, without any reindexing."
- **Our assessment**: This is the first concrete answer in the corpus to the index-staleness objection raised by Anthropic (see Cross-References). However, no freshness lag (time from commit to searchable) is reported.

### Claim 5: Vector ingestion is decoupled from HNSW build; at most one index build per shard runs at a time, and a snapshot is searchable only once its index is ready
- **Evidence**: Design description; HNSW construction named as "one of the primary CPU bottlenecks".
- **Confidence**: emerging
- **Quote**: "This keeps the database instances stable, as a snapshot only becomes searchable once its index is ready."
- **Our assessment**: Implies freshness lag by design (new snapshot not searchable until build completes); the post doesn't quantify it, and doesn't say what is served in the interim.

### Claim 6: Scaling is by shards (primary + read-only replicas, geo-distributed), with each customer pinned to exactly one shard via application-side routing
- **Evidence**: Architecture description.
- **Confidence**: emerging
- **Quote**: "each customer is pinned to exactly one shard, with a simple application-side routing layer directing each transaction to the right shard based on the customer identifier."
- **Our assessment**: Useful reference for multi-tenant isolation; no scale numbers given.

### Claim 7: A local on-device index (USearch) shares the server's metadata model, enabling cascade indexing and a two-stage local+remote search merged by a reranker
- **Evidence**: Architecture description.
- **Confidence**: emerging
- **Quote**: "Search becomes a two-stage process. First, it runs against the remote index, and then it runs against the local one, using a reranker that merges the top candidates from both sources into a single result list."
- **Our assessment**: Addresses unpushed-code relevance (pre-push work is irrelevant to others' branches). Note the order stated is remote then local, not local-first. Corroborates Cursor's client-side-index freshness rationale for local edits.

### Claim 8: Post-processing (dedupe, grouping by file, result-count cutoff, reranking) is cheap relative to search because it runs over a few dozen candidates; a slower cross-encoder/LLM reranker is affordable only on that shortlist
- **Evidence**: Design reasoning.
- **Confidence**: emerging
- **Quote**: "Each of these steps is cheap compared to the search itself, because each one runs over a few dozen candidates rather than the whole codebase."
- **Our assessment**: Sensible. Stronger LLM-based rerank (JointRank, ICTIR '25) "delivered a noticeable improvement in search quality, but at the price of significantly higher resource use and slower searches" — and was apparently not adopted. No numbers.

### Claim 9: A dedicated code-retrieval agent, implemented as a sub-agent with a capped step budget, improved search quality over single-shot retrieval
- **Evidence**: Design description; the author doesn't quantify the improvement. Cites Claude Code custom sub-agents as precedent.
- **Confidence**: anecdotal
- **Quote**: "We cap the number of steps it can take so that exploration never runs away with the budget."
- **Our assessment**: Pairs semantic retrieval with agentic tool orchestration — notably it keeps embedding retrieval as one tool inside an agent rather than replacing grep/read. Claimed sub-agent benefits (isolated context, cheaper/faster model, read-only tools, parallelism) are generic and unmeasured.

### Claim 10: Sub-agents keep the main agent's context small, can run on a cheaper model, and can be restricted to read-only tools
- **Evidence**: Assertion citing established pattern.
- **Confidence**: settled (consistent with multiple corpus sources)
- **Quote**: "When a sub-agent does the reading, only its conclusion comes back, so the main agent’s context stays small and focused."
- **Our assessment**: Matches Anthropic's subagent description in the corpus.

### Claim 11: Search results should carry detail proportional to assessed relevance — full chunk + line numbers above a threshold, minimal file-name/partial snippet below
- **Evidence**: Design decision; stated tradeoff between saving follow-up calls and polluting context.
- **Confidence**: emerging
- **Quote**: "The strategy we have adopted is to match the level of details to the assessed relevance of each result."
- **Our assessment**: A concrete, reusable tool-output design rule for any search/retrieval tool. No ablation reported; threshold value not given.

### Claim 12: The author concedes frontier-model agents are increasingly adept at navigating large codebases and that the value of semantic search is an open question, deferred to the next post
- **Evidence**: Author's own framing; teaser metric "up to 70% fewer turns" without methodology.
- **Confidence**: anecdotal
- **Quote**: "After all, agents, especially when using frontier models, have become increasingly adept at navigating large codebases."
- **Our assessment**: Notably candid; the central empirical question remains unanswered in the published parts. Treat "70% fewer turns" as unverified marketing until Part 3 shows methodology.

## Concrete Artifacts

No code or configs are published. Design summary as stated by the author (paraphrased structure; quoted fragments verbatim):

```
Storage:  ANN (HNSW/IVF) + exact pass over small candidate set
Filtering: three strategies — pre-filter / metadata bundled in index / post-filter
Incremental: snapshot -> Merkle tree of directory structure; unchanged subtrees relinked;
             embeddings deduped by chunk content hash
Build:    vectors written first; HNSW built async after snapshot fully stored;
          "at most one index build at a time per shard"
Scale:    shards (primary + read-only replicas); customer pinned to one shard
Local:    USearch on-device; same metadata model as server -> cascade indexing
Search:   remote index, then local index; reranker merges top candidates
Post:     dedupe, group by file, cutoff, rerank
Agentic:  retrieval sub-agent, capped steps, search+read tools
Format:   detail level matched to relevance score threshold
```
(Source: JetBrains AI blog, Part 2 — summary table by the Miner.)

## Cross-References

- **Contradicts:** `blog-anthropic-large-codebase-best-practices.md` (Claim 2: agentic search instead of RAG; Claim 4: no embedding pipeline or centralized index to maintain). Already filed as contradiction issue #3546 (closed; no C-NNN entry found in CONTRADICTIONS.md at time of writing, so no new issue filed). Part 2 is the installment Part 1's note predicted would address staleness: it offers Merkle-tree incremental relinking and local indexes, but quantifies no freshness lag, and concedes frontier agents navigate large repos well. This partially answers Anthropic's staleness objection in design but not in measured evidence. No verdict is picked here.
- **Corroborates**:
  - `blog-cursor-fast-regex-search.md` (Claim 8: index anchored to a git commit and updated incrementally; Claim 9: client-side indexing for freshness) — Claim 7 above shows the same local-index rationale for unpushed changes.
  - `blog-anthropic-large-codebase-best-practices.md` (Claim 12: subagents split exploration from editing) — Claims 9–10 above.
- **Extends**: `blog-jetbrains-rag-semantic-code-search.md` (Part 1; Claim 14 there commits to storage, querying, and agent integration in later parts — this delivers storage and partial agent integration; evaluation is still pending). Also extends Cursor Claim 10 (semantic and regex search complementary): here the retrieval agent orchestrates embedding search alongside other search/read tools.
- **Novel**: (a) three-way filtered-ANN comparison with an ACL-driven recommendation; (b) Merkle-tree snapshot clustering with chunk-hash dedup for code indexes; (c) build/ingest decoupling with one-build-per-shard; (d) remote+local two-stage search with reranker merge; (e) relevance-tiered result formatting rule; (f) customer-to-shard pinning for isolation.

## Guide Impact

- **Ch04 (context engineering)**: Add relevance-tiered result formatting (Claim 11) as a design rule for retrieval tool outputs: full chunk for high-score hits, file name only for low-score. Cite as `emerging`. Add the retrieval-as-sub-agent pattern with step cap (Claims 9–10) next to the Anthropic subagent material.
- **Ch04 / Ch02**: In wherever the guide discusses RAG vs. agentic search (flagged pending #3546), note that JetBrains now has a published incremental-freshness design (Claim 4), but with no measured freshness or benefit data; keep the position "debated". Revisit when Part 3 (evaluation, "up to 70% fewer turns") is published — file it as a follow-up source.
- **Ch02 (harness engineering)**: Reference the local+remote cascade (Claim 7) as a topology option for search tooling that must see unpushed code.
- **Evidence-grade caution**: Any guide text citing this source must label it design description, not measured results.

## Extraction Notes

- WebFetch returned HTTP 403; the page was retrieved with curl (HTTP 200) into an isolated directory and converted to text, so quotes were copied from the full article text. Curly apostrophes in the source were preserved.
- Source read fully; no sub-pages followed (JointRank/ICTIR '25, USearch, Qdrant, turbopuffer are mentioned but not load-bearing). Triage comments' stated "Merkle-tree snapshots" etc. all confirmed in text; the claim that "post-filtering is weakest for ACL-constrained code search" is slightly narrower than the source, which calls it weakest in general.
- Cross-reference claim numbers verified against the cited notes' headings. The Anthropic note's Claim 2/4 and Cursor Claims 8–10 match their headings.
- Confidence set `emerging`: first-party, concrete architecture, but vendor-authored, unmeasured, with several statements written conditionally ("Ideally, we'd want").
