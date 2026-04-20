---
source_url: https://cursor.com/blog/fast-regex-search
source_type: blog-post
title: "Fast Regex Search: Indexing Text for Agent Tools"
author: Cursor Engineering Team (Anysphere)
date_published: 2026-03-23
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#179"
---

# Fast Regex Search: Indexing Text for Agent Tools

> Cursor's engineering team explains why regex search is now a critical agent operation
> requiring dedicated indexing infrastructure — tracing the 50-year arc from `grep`
> through trigrams, suffix arrays, and sparse N-grams to their client-side production
> implementation, and framing local search indexes for agents as the exact analogue of
> LSP indexes IDEs built for Go-To-Definition.

## Source Context

- **Type**: blog-post (engineering deep-dive, Cursor's official blog, published 2026-03-23)
- **Author credibility**: First-party from the Cursor / Anysphere engineering team. Cursor
  is a production AI coding IDE serving enterprise-scale customers; the 15-second latency
  figure comes from their own telemetry. The post does not name individual authors but
  represents the team that built and ships this indexing system. Claims are grounded in
  a real production deployment; the historical background (Zobel 1993, Russ Cox's Google
  Code Search, Nelson Elhage's livegrep, GitHub's Project Blackbird) is academically
  traceable, adding credibility to the technical narrative.
- **Scope**: Covers why regex search is now a critical agent operation; the history of
  text indexing approaches and their tradeoffs for code search; Cursor's specific
  implementation choices (sparse N-grams, client-side storage, memory-mapped lookup
  tables, git-anchored freshness); and performance results for large codebases. Does NOT
  cover semantic (embedding-based) search in depth — the post explicitly treats that as
  a complementary system. Does NOT provide code or exact implementation benchmarks beyond
  qualitative comparisons.

## Extracted Claims

### Claim 1: Regex search is now a critical agent operation whose latency scales with codebase size, unlike most other agent actions

- **Evidence**: Cursor's own telemetry: "We routinely see `rg` invocations that take more
  than 15 seconds" in enterprise monorepos. This latency is particularly damaging because
  human-in-the-loop agentic sessions depend on agent turn-around — a 15-second stall per
  grep call compounds across a multi-step investigation. The post explicitly singles out
  grep as "one of the few agent operations whose latency scales with the size and
  complexity of the code."
- **Confidence**: emerging (first-party production telemetry; not independently verified,
  but the 15-second figure is specific and plausible for Chromium-scale codebases)
- **Quote**: "We routinely see `rg` invocations that take more than 15 seconds" and "grep
  is one of the few agent operations whose latency scales with the size and complexity of
  the code."
- **Our assessment**: This is the core motivating claim. Most harness performance literature
  focuses on token cost or context window management; latency of individual tool calls is
  underrepresented. A 15-second grep stall per agent turn is a real UX failure for
  interactive agentic sessions. The "scales with codebase size" characterization is
  important: the problem is not a fixed overhead but a variable one — enterprises with
  large monorepos are disproportionately affected, exactly the customers where AI coding
  tools have the most value.

### Claim 2: The right mental model is that agents need the same codebase indexes IDEs built for Go-To-Definition, but for grep

- **Evidence**: Structural argument framed across the blog post. IDEs invest heavily in
  syntactic indexes (AST-based go-to-definition, find-all-references via LSP) so that
  navigation is fast regardless of codebase size. Agents "love to use grep" the same way
  IDEs use Go-To-Definition — as the primary navigation primitive. The post draws the
  explicit analogy: "matching regular expressions is now a critical part of agentic
  development, and we believe it's crucial to target it explicitly" in the same way IDE
  tooling targeted symbol navigation.
- **Confidence**: emerging (analytical framing, not a measured claim; widely consistent
  with how agents are observed to use search tools)
- **Quote**: "Matching regular expressions is now a critical part of agentic development,
  and we believe it's crucial to target it explicitly."
- **Our assessment**: This framing is the single most portable insight for harness
  engineers. The IDE-to-agent analogy is practically actionable: before agents, the
  tooling community invested decades in making IDEs fast; now the same investment is
  needed for agent tools. Any harness author building or selecting search tooling should
  ask "does this behave like grep (O(n) over the codebase) or like an IDE index (O(log n)
  regardless of size)?" This claim directly supports a Ch02 harness engineering principle.

### Claim 3: Trigram decomposition (Zobel et al., 1993) is the canonical approach to indexing text for regex search — and the 3-character choice is a principled tradeoff

- **Evidence**: Historical citation to Zobel et al. 1993 academic work, popularized for
  code search by Russ Cox in Google Code Search. The reasoning is concrete: bigrams
  (2-char) create massive posting lists (too many results per query); quadgrams (4-char)
  require billions of index keys (too many index entries). Trigrams balance both. The
  query process: decompose the regex into trigram sets → load relevant posting lists →
  intersect lists to find candidate documents → perform actual regex match only on the
  resulting subset.
- **Confidence**: settled (academically grounded, independently deployed in Google Code
  Search, sourcegraph/zoekt, and other production systems)
- **Quote**: N/A (described in prose; the 1993 paper is attributed to Zobel et al.)
- **Our assessment**: The trigram approach is well-established and the tradeoff explanation
  (bigrams vs. quadgrams) is clear and teachable. The key insight for practitioners is
  that the index does not replace the regex match — it eliminates candidate documents so
  the expensive scan only touches a small subset. This is the "filter first, match second"
  pattern that appears in many database query optimizations.

### Claim 4: Suffix arrays (Nelson Elhage's livegrep approach) offer efficient binary search for literal matches but scale poorly for dynamic updates

- **Evidence**: Description of the livegrep architecture: a sorted array of all string
  suffixes (as offsets, not full strings, so compressed) enables binary search for
  literal patterns and character ranges. However, the implementation requires
  "concatenating the entire codebase into a single string" and dynamic updates are "very
  expensive." Used by livegrep for the Linux kernel (a relatively static, large codebase
  where batch rebuilds are acceptable).
- **Confidence**: emerging (description of an existing production system; tradeoffs are
  stated by Cursor's team, not independently measured in the post)
- **Quote**: (paraphrased) requires single concatenated string; dynamic updates "very
  expensive" compared to inverted-index approaches.
- **Our assessment**: Suffix arrays are the right choice for very large, stable corpora
  where you want fast literal substring search and can afford periodic rebuilds. For
  agent workflows where files change frequently (the agent is writing code), the rebuild
  cost is prohibitive. The tradeoff space (suffix array vs. trigram index) maps cleanly
  to batch-rebuild vs. incremental-update use cases — relevant for harness authors
  choosing or building search backends.

### Claim 5: GitHub's Project Blackbird augments trigram entries with 8-bit bloom filters to achieve "3.5-gram" effective precision — but bloom filter saturation degrades performance at scale

- **Evidence**: Technical description of Blackbird's two bloom filter types: `locMask`
  (position information, mod 8) and `nextMask` (probabilistic encoding of characters
  following each trigram). By encoding information about the character *after* a trigram,
  queries can behave like quadgram queries (filtering by adjacency) while the index only
  stores trigrams. The drawback: bloom filters have fixed bit-width; as the codebase grows,
  bits saturate and the filters become useless — all candidates pass the filter and you
  are back to scanning.
- **Confidence**: emerging (described by Cursor's team; the Blackbird project is real but
  not fully publicly documented; the saturation failure mode is a known bloom filter property)
- **Quote**: (described in post prose; no direct quote available)
- **Our assessment**: The bloom filter augmentation is a clever engineering trick but has
  a fundamental scaling limit that Cursor explicitly chose to avoid. The saturation problem
  is worth understanding as a general principle: probabilistic data structures have failure
  modes that emerge at scale, and a system that works for GitHub's own codebase may not
  work for a large enterprise monorepo. The architectural lesson: optimize for the worst-
  case codebase size, not the median.

### Claim 6: Sparse N-grams (used in GitHub Code Search and ClickHouse) extract variable-length segments deterministically based on character-pair weights — reducing false positives and query-time lookups

- **Evidence**: Algorithm description: assign a weight to each character pair using a
  deterministic function (e.g., CRC32 hash or frequency-based weighting). Extract an
  N-gram boundary wherever the edge weights exceed all interior weights of the segment.
  This produces variable-length n-grams with fewer redundant entries than trigrams. Two
  operational modes: `build_all` (index all possible sparse n-grams at write time) and
  `build_covering` (at query time, extract only the minimal set of n-grams needed to
  cover the query). Frequency-based weighting assigns high weights to rare character
  pairs — this means queries involving rare substrings (e.g., a distinctive function
  name) reduce to very few posting list lookups.
- **Confidence**: emerging (described with algorithmic specificity; deployed in production
  at GitHub Code Search and ClickHouse as corroborating implementations)
- **Quote**: N/A (described in post prose)
- **Our assessment**: Sparse N-grams are the most sophisticated approach in the post's
  taxonomy and the one Cursor chose. The frequency-based weighting is particularly elegant:
  it automatically gives better performance for the searches that matter most in code
  (rare identifiers, specific error messages) and is less optimal for common tokens —
  exactly the right distribution. The two-mode design (`build_all` vs. `build_covering`)
  separates index construction cost from query cost, allowing tuning of each independently.

### Claim 7: Cursor's implementation uses local client-side storage with two files — a postings file and a memory-mapped lookup table — for minimal memory overhead and fast binary-search queries

- **Evidence**: Technical architecture description. File 1: sequential posting lists
  flushed to disk during index construction. File 2: N-gram hashes and their file offsets,
  stored as a sorted hash table and memory-mapped (not fully loaded into memory). Queries
  binary-search the memory-mapped lookup table to find the offset, then read directly from
  the postings file at that offset. Hash collisions broaden posting lists but never produce
  false negatives (you may scan more candidates but never miss a true match).
- **Confidence**: emerging (first-party description of production implementation; not
  independently verified)
- **Quote**: N/A (architecture described in post prose)
- **Our assessment**: The two-file design is a practical engineering choice: the postings
  file can be large (sequential disk I/O is cheap) while the lookup table is small enough
  to memory-map (fast random access). The "no false negatives" guarantee from hash
  collisions is the correct invariant — you want to be able to omit candidates but not
  miss true matches. This is the same contract as trigram-based search generally: the
  index reduces the candidate set, and the final match is the truth function.

### Claim 8: The index is anchored to a git commit and updated incrementally for agent writes — solving the freshness problem without full rebuilds

- **Evidence**: Architecture description: "Index pinned to Git commit; user/agent changes
  layered on top for rapid updates." The layered approach means the committed codebase
  provides the stable base index, and any file the agent has written or modified during
  the session is tracked separately. This ensures the agent's own writes are immediately
  searchable without waiting for a full reindex.
- **Confidence**: emerging (described as part of the production implementation; mechanism
  is architecturally sound)
- **Quote**: "Index pinned to Git commit; user/agent changes layered on top for rapid
  updates."
- **Our assessment**: The git-anchoring approach elegantly separates the "codebase as
  committed" from "codebase as the agent currently sees it." This is directly relevant
  to agentic workflows where the agent writes a file, then immediately needs to search
  that file. Without this layering, an agent could write a file and then fail to find it
  with grep — a confusing state. The commit-anchor also means index state is reproducible:
  the same commit always produces the same base index.

### Claim 9: Client-side (local) indexing is preferred over server-side for three reasons: no network latency, immediate agent-write freshness, and data privacy

- **Evidence**: Explicit architectural rationale from the post. (1) Latency: "avoiding
  network roundtrips preserves one of the fastest tokens per second" rates — the post
  implies that the model's inference speed is now fast enough that tool latency (not model
  latency) is the bottleneck. (2) Freshness: agent writes are immediately visible to the
  local index; server-side would require syncing. (3) Privacy: code never leaves the
  client for indexing purposes.
- **Confidence**: emerging (design rationale stated; the claim that model inference is now
  faster than tool I/O is directionally credible for current frontier models)
- **Quote**: "Avoiding network roundtrips preserves one of the fastest tokens per second
  rates" (paraphrased); privacy and freshness cited as explicit advantages.
- **Our assessment**: The "model inference is now the fast part; tool latency is the
  bottleneck" framing is significant. It inverts the common assumption that model
  inference is the limiting factor in agent turn-around time. If frontier models generate
  tokens fast enough that grep latency dominates, then harness performance investment
  should shift from context optimization (reducing tokens) to tool latency optimization
  (making tools faster). This is an important architectural signal for Ch02.

### Claim 10: Semantic (embedding-based) search and regex (index-based) search are complementary tools with different failure modes — one is not a substitute for the other

- **Evidence**: The post explicitly distinguishes the two: "We don't have to continuously
  update our semantic index because re-computing the embeddings for a file after it is
  modified does not cause the new embedding to significantly displace itself." By contrast,
  regex indexes must reflect exact character-level changes immediately. The two address
  different query types: semantic search for conceptual retrieval ("what code handles
  authentication?"), regex for deterministic text matching ("find all uses of
  `parseConfig`").
- **Confidence**: settled (complementarity of the two approaches is architecturally clear;
  neither can replicate the other's query semantics)
- **Quote**: "We don't have to continuously update our semantic index because re-computing
  the embeddings for a file after it is modified does not cause the new embedding to
  significantly displace itself."
- **Our assessment**: This claim contains an important practical implication for semantic
  index freshness: embedding-based indexes tolerate moderate staleness because the
  embedding space changes slowly with code changes. Regex indexes cannot tolerate staleness
  at all — a renamed function breaks regex search immediately. The two freshness
  requirements are fundamentally different, which is why they need separate indexing
  infrastructure. Harness authors who treat semantic search as a drop-in replacement for
  grep will hit this mismatch.

### Claim 11: Word-based tokenized inverted indexes — the foundation of search engines like ElasticSearch — fail for code search because programming language tokenization is too complex

- **Evidence**: Historical context: early GitHub code search "required a very complex
  tokenizer for programming languages, and a very large ElasticSearch cluster." The word-
  token approach that works well for natural language documents (split on whitespace and
  punctuation) fails for code because identifiers, operators, and delimiters create
  ambiguous token boundaries across languages.
- **Confidence**: settled (the GitHub early approach is a documented public failure; the
  structural reason for the failure is well-understood)
- **Quote**: (paraphrased from post): required "a very complex tokenizer for programming
  languages, and a very large ElasticSearch cluster"
- **Our assessment**: This is historical context rather than a primary claim, but it
  establishes why purpose-built code indexing (trigrams, suffix arrays) is necessary
  rather than an engineering preference. General-purpose search infrastructure should not
  be assumed to work for code search without validation. Teams building internal search
  tooling should treat code search as a distinct problem from document search.

### Claim 12: Grep latency compounds worst in agent "investigation" phases — the bottleneck appears most during bug root-cause analysis, not during code generation

- **Evidence**: Performance comparisons show: "Investigation in Chromium: substantial time
  reduction primarily during search phases." The post describes refactoring tasks also
  improving when grep latency disappears, but emphasizes the investigation (multi-grep,
  exploratory search) use case as the primary target. Investigation tasks are grep-heavy
  because the agent does not know where to look and must search broadly before narrowing.
- **Confidence**: emerging (qualitative performance comparison shown in visuals; no
  quantitative numbers published in the accessible text)
- **Quote**: "Investigation tasks: Grep overhead significantly reduced (visual comparison
  across chromium and cursor projects)"
- **Our assessment**: The investigation-task focus aligns with the Prospector's triage
  observation that ripgrep searches stall "human-in-the-loop agentic sessions." The
  worst case is the agent doing a broad exploratory search over a large codebase to
  understand an unfamiliar system — exactly the onboarding or debugging scenario where
  a human would most want fast answers. A 15-second grep in that context breaks the
  cognitive flow of both the agent and the human watching it.

## Concrete Artifacts

### Text Indexing Approach Taxonomy for Code Search

```
# Approaches to indexing text for regex search (from Cursor's survey, March 2026)

APPROACH 1: Inverted Index (word-based, search engine foundation)
  Mechanism:  Tokenize documents; map token → posting list of doc IDs
  Code search failure: Programming language tokenization too complex
  Prior attempt: GitHub early code search (required large ElasticSearch cluster)
  Status: Not recommended for code search

APPROACH 2: Trigram Inverted Index (Zobel et al., 1993; Russ Cox / Google Code Search)
  Mechanism:  Every overlapping 3-char sequence → posting list
  Tradeoff:   Bigrams: posting lists too large; quadgrams: too many index keys
  Query:      Decompose regex → trigram set → intersect posting lists → regex match on subset
  Deployed:   google/codesearch, sourcegraph/zoekt
  Status:     Production-proven baseline

APPROACH 3: Suffix Array (Nelson Elhage / livegrep)
  Mechanism:  Sorted array of all string suffix offsets; binary search for matches
  Advantages: Fast literal match; compact (offsets only, not full strings)
  Drawbacks:  Requires single concatenated codebase string; dynamic updates "very expensive"
  Deployed:   livegrep (Linux kernel search)
  Status:     Good for large, stable corpora; poor for frequently-changing codebases

APPROACH 4: Trigram + 8-bit Bloom Filters (GitHub Project Blackbird)
  Mechanism:  Augment each trigram posting list with two 8-bit masks:
                locMask: position information (mod 8)
                nextMask: probabilistic bloom filter for next character
  Benefit:    Achieves ~3.5-gram effective precision while indexing trigrams
  Drawback:   Bloom filter saturation degrades to scanning with large datasets
  Status:     Innovation but has fundamental scaling limit

APPROACH 5: Sparse N-grams (GitHub Code Search, ClickHouse)
  Mechanism:  Assign weight to each character pair (CRC32 or frequency-based)
              Extract n-gram boundary when edge weight exceeds all interior weights
              → variable-length segments with fewer redundant entries
  Modes:
    build_all:      Index all possible sparse n-grams (write-time)
    build_covering: Extract minimal n-grams needed (query-time)
  Frequency weighting: Rare char pairs → high weight → fewer query lookups for rare strings
  Advantage:  Rarer substrings produce fewer posting list lookups (fast for identifiers)
  Status:     Current state-of-the-art; chosen by Cursor
```

### Cursor's Production Index Architecture

```
# Cursor client-side index implementation (as of March 2026)

STORAGE: Two-file design
  File 1 (postings.bin):   Sequential posting lists, flushed to disk during construction
  File 2 (lookup.mmap):    Sorted hash table: n-gram hash → file offset in postings file
                           Memory-mapped (not fully loaded into RAM)

QUERY PROCESS:
  1. Binary search on memory-mapped lookup table → posting list offset
  2. Direct disk read at returned offset → candidate document set
  3. Regex match against actual file content (filter, not oracle)
  4. Hash collisions: may broaden candidate set; never cause false negatives

FRESHNESS MODEL:
  Base:    Index anchored to current git commit
  Layer:   Agent writes tracked separately (immediate freshness for in-session changes)
  Update:  Full rebuild at commit; incremental for agent file changes

DEPLOYMENT: Local / client-side
  - No network roundtrip (latency preservation)
  - Immediate visibility of agent writes
  - Code never leaves client for indexing
```

### Mental Model: IDE Index Analogy

```
# IDE indexes → Agent indexes (conceptual mapping)

TRADITIONAL IDE:
  Problem:    "Go to definition" requires symbol lookup across entire codebase
  Solution:   Build AST + symbol index; O(log n) lookup regardless of codebase size
  Protocol:   Language Server Protocol (LSP) standardizes this for many tools
  Result:     Fast symbol navigation even in 500K-file monorepos

AGENT WORKFLOWS:
  Problem:    grep (regex search) requires linear scan across entire codebase
  Solution:   Build text index (trigrams / sparse n-grams); O(log n) candidate reduction
  Protocol:   Not yet standardized — each tool builds its own
  Result:     Fast regex search even in 500K-file monorepos

KEY INSIGHT: Agents "love to use grep" the same way IDEs depend on Go-To-Definition.
Both require the same solution: build a purpose-built index for the primitive operation.
```

## Cross-References

- **Corroborates**:
  - **blog-ccunpacked-claude-code-architecture** (issue #22): The Grep tool appears in
    the ccunpacked tool taxonomy (File Operations category, alongside FileRead, FileEdit,
    FileWrite, Glob, NotebookEdit). This fast-regex-search post provides the production
    motivation for why Grep needs to be fast — specifically, that without indexing, Grep
    is O(n) over the codebase and becomes a 15-second stall at enterprise scale. The two
    sources are complementary: ccunpacked documents that Grep exists as a tool; this note
    explains why making it fast is an active engineering priority.
  - **blog-cursor-cursorbench** (issue #160): CursorBench's ablation experiment (removing
    the semantic search tool) found semantic search mattered most for "repository-grounded
    Q&A on larger codebases." This fast-regex-search post confirms that large codebases
    are also where regex search latency is the most acute (15-second `rg` calls in
    enterprise monorepos). Both sources independently confirm that codebase scale is the
    critical variable for search performance, and both highlight the complementary nature
    of semantic (embedding) vs. lexical (regex) search.
  - **blog-addyosmani-code-agent-orchestra** (no issue number): Osmani's Claim 5 states
    "the bottleneck has shifted from code generation to verification." This post makes a
    parallel claim at the tool level: within a single agent turn, the bottleneck has
    shifted from model inference to tool latency (grep in particular). Both sources point
    to the same insight from different angles — the model generating text is no longer the
    slow part of the system.

- **Contradicts**: None identified. The claim that regex and semantic search are
  complementary (not competing) is internally consistent with every other source note that
  discusses context retrieval.

- **Extends**:
  - **blog-cursor-cursorbench** (issue #160): The cursorbench post shows semantic search
    matters more for large codebases (ablation result). This post extends that finding
    with the mechanism: large codebases are precisely where unindexed regex search becomes
    a 15-second blocking operation, making the performance case for both indexing approaches
    strongest at scale. The two together make a complete picture of search infrastructure
    requirements for large-codebase agentic work.
  - **blog-ccunpacked-claude-code-architecture** (issue #22): The ccunpacked note
    documents the Grep tool as part of the File Operations tool category. This note
    provides the production engineering rationale for *why* Cursor invested in optimizing
    what looks like a simple utility tool — regex search latency is a first-order agent
    performance concern, not a background optimization.

- **Novel**: The following are completely new to our corpus:
  - **Regex search latency as a named harness engineering concern**: No existing source
    note identifies grep/regex latency as a first-class problem for agentic workflows.
    The 15-second figure is the first concrete measurement of this overhead in the corpus.
  - **The IDE-to-agent index analogy**: No existing source articulates the principle that
    agents need search indexes equivalent to what IDEs built for symbol navigation. This
    framing is portable and actionable for any harness author evaluating search tooling.
  - **The complete taxonomy of code search indexing approaches**: Trigrams, suffix arrays,
    bloom-filter augmentation, and sparse n-grams are not discussed in any other source
    note. This is the only source providing depth on the technical options.
  - **Client-side indexing rationale**: The privacy/latency/freshness tradeoff for
    deploying search indexes locally vs. server-side is not covered elsewhere in the corpus.
  - **Tool latency as the new bottleneck**: The claim that model inference speed has
    increased to the point where tool latency (not model latency) is the limiting factor
    in agent turn-around is new to the corpus and significant for harness design priorities.
  - **Semantic index freshness tolerance**: The observation that embedding-based indexes
    can tolerate staleness (because embeddings change slowly with code changes) while
    regex indexes cannot is new and practically important.

## Guide Impact

- **Chapter 02 (Harness Engineering — Tool Performance)**: Add a dedicated section on
  search tool performance as a harness engineering concern. The headline claim is concrete
  and surprising: at enterprise scale, grep latency (15+ seconds) is a first-order UX
  problem for agentic workflows, not a background optimization. The recommendation for
  Ch02: when selecting or building a code search tool for an agent harness, evaluate
  whether it uses an index (O(log n) query) or scans (O(n) query) — the difference
  materializes at the scale where AI coding tools are most valuable.

- **Chapter 02 (Harness Engineering — IDE-to-Agent Analogy)**: Use the IDE index analogy
  as a mental model for harness design more broadly. IDEs invested decades in purpose-built
  indexes (AST, symbols, go-to-definition via LSP) so that navigation primitives became
  fast. Agents need the same investment: indexing grep, watching file changes, caching
  semantic embeddings. Harness design is building the "IDE layer" for the agent — not just
  providing raw filesystem access.

- **Chapter 04 (Context Engineering — Tool Selection)**: Cite Claim 10 (semantic and regex
  search are complementary with different freshness requirements) as a tool selection
  principle. Teams choosing between embedding-based and regex search for their agents
  should deploy both and route queries appropriately. Regex search is required for
  deterministic lookups (exact identifier, specific string); semantic search is required
  for conceptual queries ("find authentication code"). The staleness tolerance difference
  (embedding indexes can lag; regex indexes cannot) is a concrete architectural design
  constraint.

- **Chapter 04 (Context Engineering — Bottleneck Analysis)**: The "tool latency is now
  the bottleneck, not model inference" claim belongs in any section on optimizing agent
  turn-around time. Context window optimization (reducing tokens) may yield diminishing
  returns if grep latency is the dominant factor per turn. Harness authors should profile
  their agents to understand where time is actually spent before investing in optimization.

- **Chapter 02 or Appendix (Technical Reference — Search Indexing)**: The taxonomy of
  search index approaches (trigrams, suffix arrays, bloom filter augmentation, sparse
  n-grams) is the right reference material for teams building their own search backends.
  The tradeoff table — dynamic updates, bloom filter saturation, false-positive rate,
  query complexity — provides the selection framework. Sparse N-grams with frequency-based
  weighting is the current recommended approach for agent search backends.

## Extraction Notes

- The blog post is fully accessible at cursor.com/blog/fast-regex-search (no paywall).
  Two separate fetches were performed to ensure completeness; both were consistent and
  cross-corroborating.
- The post includes performance comparison visuals (screenshots of agent workflows with
  and without the index) that were not extractable as text. The post describes them as
  showing "substantial time reduction primarily during search phases" for investigation
  tasks in Chromium-scale codebases and the cursor codebase itself. No quantitative
  numbers (exact ms savings) are given in the text.
- No individual authors are named on this post (attributed to Cursor Engineering Team);
  this reduces the ability to assess individual credibility but the first-party production
  context establishes sufficient credibility.
- The history of text indexing approaches in the post is accurate and traceable: Zobel
  et al. 1993 is a real academic reference; Russ Cox's Google Code Search is documented
  in his public writings; Nelson Elhage's livegrep is an open-source project; GitHub's
  Project Blackbird is documented in GitHub engineering posts; ClickHouse's sparse n-gram
  use is part of their full-text search documentation. The historical grounding raises
  confidence that the technical claims are accurately represented.
- The post's framing (50-year arc from grep through to agent tools) is pedagogically
  compelling and suggests this was written as much for developer education as for product
  announcement. The educational framing is a quality signal — the team had to understand
  the history well to explain it accurately.
- No contradictions to file: no existing source note makes claims about code search
  indexing or regex search tool performance that this source would contradict.
