---
source_url: https://blog.jetbrains.com/ai/2026/09/building-a-rag-pipeline-for-semantic-code-search-a-developer-diary-and-field-notes/
source_type: blog-post
title: "Building a RAG Pipeline for Semantic Code Search: A Developer Diary and Field Notes"
author: Adam Malek and Ashot Kazaryan (JetBrains)
date_published: 2026-09-17
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: emerging
issue: "#3535"
---

# Building a RAG Pipeline for Semantic Code Search: A Developer Diary and Field Notes

> First-party JetBrains engineering diary (Part 1 of a series) on building JetBrains
> Context, a production semantic code search system for AI coding agents — covering
> language-aware structural chunking, binary-quantized vector storage, and a
> privacy-preserving architecture that stores only coordinates, not source code.

## Source Context

- **Type**: blog-post (developer diary / field notes, JetBrains AI blog, published
  2026-09-17; Part 1 of a multi-part series, with storage, millisecond-latency
  querying, agent integration, and continuous evaluation explicitly named as
  subjects of upcoming parts)
- **Author credibility**: First-party JetBrains engineers (Adam Malek, Ashot
  Kazaryan) describing the design of JetBrains Context, a shipped product
  ("public preview, included with a JetBrains license" per the article).
  JetBrains has deep, decades-long authority on language-aware code parsing —
  the article explicitly leverages JetBrains' existing "Code Engine" parser
  infrastructure (the same parsing technology behind IntelliJ IDEA's static
  analysis) rather than building code-awareness from scratch. This is a
  production system account, not a research prototype description, and the
  article cites the IntelliJ IDEA monorepo itself (over a million files) as a
  concrete scale reference. No independent, non-JetBrains verification of the
  claims was located.
- **Scope**: Covers why keyword/grep search is insufficient for agents doing
  conceptual code search, the case against fixed-size and whole-file chunking,
  JetBrains' language-aware structural chunking approach (reusing JetBrains'
  existing code parsers), binary quantization of embedding vectors and Hamming
  distance for comparison, path-abbreviation for long file paths in embedding
  input, and a privacy architecture that stores only coordinates/metadata (not
  source code) using an open-weight embedding model run on JetBrains-operated
  infrastructure. Does NOT cover (deferred to later parts of the series):
  storage engine implementation, query-time latency architecture, incremental
  index freshness/re-indexing cadence as code changes, evaluation methodology,
  or how agents consume/rank the retrieved results (reranking, citation,
  fallback behavior). No cost-per-query or infrastructure-cost figures are
  given.

## Extracted Claims

### Claim 1: Keyword search and grep are fundamentally limited for agentic code search because they require the agent to already know the exact text to search for, whereas conceptual/abstract queries have no fixed vocabulary
- **Evidence**: Direct problem statement with a concrete illustrative example (session-token-refresh code that need not contain the word "refresh").
- **Confidence**: emerging (practitioner architectural rationale motivating a shipped product; not an independently measured comparison)
- **Quote**: "an agent looking for where session tokens get refreshed cannot rely on the code helpfully containing the word 'refresh'"
- **Our assessment**: This is a clean, concrete illustration of the well-known keyword-vs-semantic gap, applied specifically to the agentic-coding-tool context rather than general search. It directly motivates why JetBrains built a dedicated semantic index rather than relying on grep alone — but it does not engage with the alternative of an agent doing broader agentic filesystem traversal (reading surrounding files, following call chains) instead of a single grep call, which is the approach Claude Code takes (see Cross-References/Contradicts below).

### Claim 2: Fixed-size chunking of code produces semantically incoherent groupings — unrelated code fragments (e.g., an import statement and unrelated function content) end up chunked together, causing retrieval mistakes
- **Evidence**: Direct problem statement under the article's discussion of chunk-size decisions.
- **Confidence**: emerging (practitioner rationale; no quantified retrieval-accuracy comparison between fixed-size and structure-aware chunking is given)
- **Quote**: "Unrelated code pieces would be grouped together, for example, an import statement and some function content, leading to mistakes during retrieval."
- **Our assessment**: This is a specific, concrete failure mode (not a generic "chunking matters" statement) and is directly actionable: teams building code-RAG systems should chunk on syntactic/semantic boundaries (declarations), not fixed character or line counts. Whole-file embedding is described elsewhere in the article as the opposite-direction failure (returns whole files, defeating the goal of finding a specific snippet), though no verbatim quote for that specific framing was captured — this is the Miner's synthesis of the surrounding argument, not a direct quote.

### Claim 3: JetBrains chunks code using its existing language-aware "Code Engine" parsers rather than building new tokenization/parsing logic — reusing infrastructure originally built for IDE features
- **Evidence**: Direct statement naming the reused infrastructure and the motivation (handling per-language quirks and conventions).
- **Confidence**: settled (first-party architectural description of a shipped system's implementation choice)
- **Quote**: "we at JetBrains have developed parsers that are smart enough to adjust for the various quirks, irregularities, conventions, and nuances of specific languages"
- **Our assessment**: This is a notable structural advantage specific to JetBrains as a vendor — most RAG-for-code implementations (e.g., generic embedding pipelines built on tree-sitter or regex-based heuristics) do not have decades of existing per-language parser infrastructure to reuse. This claim is a reminder that "language-aware chunking" is not a single technique but a spectrum of implementation quality, and JetBrains' approach sits at the high-investment end because the parsers already existed for other purposes (IDE inspections, refactoring, static analysis).

### Claim 4: When chunking, syntactic elements that are semantically bound to a declaration — leading documentation, annotations, visibility modifiers, and keywords, as well as trailing closing syntax — are kept attached to that declaration's chunk rather than split off
- **Evidence**: Direct rule statement describing what the structure-aware chunker preserves.
- **Confidence**: settled (concrete implementation rule from a shipped chunking system)
- **Quote**: "Prefixes such as documentation, annotations, visibility modifiers, and keywords are kept together with the declaration; suffixes (usually closing syntax) remain associated with the construct they close."
- **Our assessment**: This is a genuinely reusable, concrete rule for anyone building a code-chunking pipeline: chunk boundaries should be defined by the full syntactic span of a declaration (doc comment through closing brace), not just its "body." A chunk that drops the docstring or the visibility modifier loses meaning that a human reader would consider part of the same unit.

### Claim 5: JetBrains' structure-aware chunking approach bears similarity to the academic cAST algorithm (Zhang et al., 2025)
- **Evidence**: Direct citation naming the comparable published algorithm.
- **Confidence**: settled (direct citation in the source)
- **Quote**: "The algorithm bears some similarities to cAST, authored by Zhang et al. in 2025."
- **Our assessment**: This citation situates JetBrains' approach within existing published research on structure-aware code chunking rather than presenting it as a wholly novel invention — useful for readers who want to compare implementations or read the underlying academic work (cAST) directly.

### Claim 6: File paths can dominate an embedding if included verbatim, so long paths are abbreviated with a rule that preserves the start (module context) and end (filename) while eliding the middle
- **Evidence**: Direct statement of the truncation rule, motivated by the scale of the IntelliJ IDEA monorepo (over a million files, implying very long, deeply nested paths).
- **Confidence**: settled (concrete implementation rule from a shipped system, with a stated scale justification)
- **Quote**: "Keep the longest prefix that still fits, elide what falls between into '…', and if even parent-plus-filename is too long, keep only the name itself."
- **Our assessment**: This is a specific, non-obvious engineering detail: naively embedding full file paths in a monorepo can let path tokens overwhelm the semantic signal from the actual code content. The chosen heuristic (prefix + elided middle + filename, degrading to filename-only) is a concrete, adoptable pattern for any team embedding code from a large or deeply-nested repository. The stated scale trigger — "the IntelliJ IDEA monorepo runs to over a million files" — is itself a useful data point for what "large enough to need this" looks like.

### Claim 7: JetBrains chose binary quantization for embedding vectors — reducing each vector from 32-bit floats to a single bit per dimension, a 32x storage reduction — and compares vectors using Hamming distance instead of cosine similarity
- **Evidence**: Direct statement of the storage reduction factor and the alternate comparison metric, plus a worked Hamming-distance example ("10110100 and 10010110. They differ in two positions, so the distance between them is two").
- **Confidence**: settled (concrete implementation decision with a stated, checkable ratio)
- **Quote**: "32 times smaller than the same vector in 32-bit floats"
- **Our assessment**: This is a specific, reusable engineering tradeoff for any team scaling vector search across a large codebase: binary quantization plus Hamming distance (computed via XOR and a popcount, described as "costs in the order of a hundred instructions") is dramatically cheaper to store and compare than float vectors with cosine similarity, at the cost of ranking precision (see Claim 8).

### Claim 8: Binary quantization costs some retrieval recall/ranking precision compared to unquantized vectors, but JetBrains judges this acceptable for agent use because agents examine multiple candidate results rather than relying on a single top-ranked result the way a human UI would
- **Evidence**: Direct statement that quantization "still costs a few points of recall against the unquantized vector," paired with the stated justification that ranking degradation is far less consequential when the consumer is an agent rather than a human reading a short results list.
- **Confidence**: emerging (practitioner judgment call defended by reasoning, not by a measured agent-outcome study comparing quantized vs. unquantized retrieval in production)
- **Quote**: "a ranking degradation that would be plainly visible in a three-result UI built for humans is mostly invisible"
- **Our assessment**: This is a notable, generalizable argument about how retrieval quality bars should differ for agent-consumed vs. human-consumed search results: an agent that reads several candidate chunks anyway is more tolerant of a candidate ranking 4th instead of 1st than a human scanning a three-result list. This is a useful counterpoint for any RAG system design discussion that assumes human-UI-grade ranking precision is required — for agentic consumers, a cheaper, lossier retrieval mechanism may be an acceptable and worthwhile tradeoff. The claim is not independently measured in this article, so it should be treated as a design rationale rather than a validated result.

### Claim 9: JetBrains Context stores no source code in its index — only coordinates and metadata — and reconstructs the displayed snippet locally, on the user's machine, from their own checkout
- **Evidence**: Direct architectural/privacy statement.
- **Confidence**: settled (concrete, stated architectural guarantee for a shipped product)
- **Quote**: "No content, no copy of the source code itself, is saved. What a search returns is coordinates, and the snippet you see is assembled on your machine, from your checkout, using them."
- **Our assessment**: This is a specific and verifiable privacy architecture claim, not a vague "we care about privacy" statement — it names exactly what is and isn't persisted (coordinates/metadata vs. source text) and where reconstruction happens (client-side, from the user's own checkout). This is directly comparable to Cursor's client-side indexing rationale in `blog-cursor-fast-regex-search.md` (Claim 9: privacy as one of three reasons for local, client-side indexing) — both vendors independently converge on keeping code content off a shared/server-side store, though via different mechanisms (JetBrains stores no content at all in the index; Cursor keeps the whole index client-side).

### Claim 10: JetBrains runs its own open-weight embedding model on JetBrains-operated GPU infrastructure rather than calling a third-party embedding API
- **Evidence**: Direct statement about the embedding model deployment choice, presented as part of the same privacy-architecture discussion as Claim 9.
- **Confidence**: settled (stated infrastructure/vendor choice for a shipped product)
- **Quote**: (no direct quote captured for this specific sentence; per the source's "Protecting source code" section, described in Miner's paraphrase as "an open-weight embedding model, running on GPUs we operate" — see Extraction Notes for why this is not presented as a verbatim quote)
- **Our assessment**: Running an open-weight model in-house rather than sending code to a third-party embedding API is a second, independent privacy control layered on top of the coordinates-only storage design in Claim 9 — even the act of *computing* the embedding does not send code to an external vendor. This is a concrete data point for any team evaluating build-vs-buy tradeoffs for code-embedding infrastructure in regulated or IP-sensitive environments.

### Claim 11: For search to be usable interactively, results must return within a couple of seconds at most, or users abandon the tool
- **Evidence**: Direct statement of the latency requirement as a design constraint.
- **Confidence**: emerging (stated as a general UX principle motivating design decisions; no specific measured abandonment-rate data given)
- **Quote**: "users will give up if they are not provided with results within a couple of seconds at most"
- **Our assessment**: This latency bar is stated as a design constraint rather than a measured outcome, but it is a useful, concrete number for the guide's discussion of retrieval-system UX requirements — a couple of seconds is a tight bar for a full RAG pipeline (embed query, search index, retrieve/rerank, assemble snippet) and explains why the storage/comparison optimizations in Claims 6–8 (path truncation, binary quantization) matter: every millisecond of index-scan cost compounds against this ceiling.

### Claim 12: At JetBrains' operating scale, a few million code chunks produce an index on the order of tens of gigabytes
- **Evidence**: Direct scale statement.
- **Confidence**: settled (stated concrete figure for the described system)
- **Quote**: "a few million chunks add up to tens of gigabytes of index"
- **Our assessment**: This is a concrete, checkable data point for anyone estimating storage requirements for a similarly-scoped code-RAG system — millions of chunks (implying tens-of-thousands to low-hundred-thousands of files, given typical chunk-per-file counts) map to tens of gigabytes even after the 32x binary-quantization storage reduction (Claim 7). Without quantization, the same index would plausibly run into the terabyte range, underscoring why the storage optimization was treated as a first-order design concern rather than an afterthought.

### Claim 13: JetBrains Context is shipped as a public preview product included with a JetBrains license, not a research prototype
- **Evidence**: Direct product-status statement (captured via targeted fetch, not independently re-verified against raw HTML — see Extraction Notes).
- **Confidence**: settled (product-status fact about the vendor's own shipped offering)
- **Quote**: (no direct quote captured; product status described by the fetch tool as "public preview, included with JetBrains license" — treated as paraphrase pending verbatim confirmation, see Extraction Notes)
- **Our assessment**: The shipped/public-preview status matters for how the guide should frame this source: these are documented decisions behind a product real users can install today, not a lab exercise. This raises the practical stakes of Claims 1–12 relative to a purely theoretical RAG-for-code writeup.

### Claim 14: This article is Part 1 of a multi-part series; JetBrains explicitly commits to covering storage efficiency, millisecond-latency querying, agent integration, and continuous result evaluation in subsequent parts
- **Evidence**: Direct closing statement naming the deferred topics.
- **Confidence**: settled (explicit statement of the source's own scope and roadmap)
- **Quote**: "how to store them efficiently, how to create a system that can answer a query in milliseconds, how we can continuously evaluate our results"
- **Our assessment**: This tells the guide (and future Miners) exactly what is *not yet* covered by this installment and should be treated as an open question rather than settled: index freshness/staleness as code changes (central to the Anthropic contradiction filed alongside this note — see Cross-References), how agents actually consume and rank results (reranking, citation, fallback on empty results), and evaluation methodology. Follow-up source submissions should be filed once JetBrains publishes the storage and agent-integration installments, since those are the parts most likely to bear on the RAG-vs-agentic-search contradiction below.

## Concrete Artifacts

```
JetBrains Context: Chunking and Vectorization Design (Part 1, Sept 2026)

CHUNKING:
  Mechanism:   Reuses JetBrains "Code Engine" language-aware parsers
  Boundary:    Syntactic declaration span (function, class, etc.)
  Preserved:   Prefixes (docs, annotations, visibility modifiers, keywords)
               kept with declaration; suffixes (closing syntax) kept with
               the construct they close
  Rejected approaches:
    - Fixed-size chunking: groups unrelated code (e.g. import + unrelated
      function body) into one chunk, causing retrieval mistakes
    - Whole-file embedding: returns entire files, defeats snippet-level
      retrieval goal (Miner's synthesis of surrounding argument, not a
      direct quote)
  Related academic work: cAST (Zhang et al., 2025) — "bears some
  similarities"

PATH HANDLING (for monorepos, e.g. IntelliJ IDEA: 1M+ files):
  Rule: "Keep the longest prefix that still fits, elide what falls between
         into '…', and if even parent-plus-filename is too long, keep only
         the name itself."

VECTORIZATION:
  Quantization: 32-bit float → 1 bit per dimension (32x storage reduction)
  Comparison:   Hamming distance (XOR + popcount) instead of cosine
                similarity on float vectors
                Example given: 10110100 vs 10010110 → Hamming distance 2
                Cost: "in the order of a hundred instructions" per comparison
  Tradeoff:     "a few points of recall" lost vs. unquantized vectors;
                judged acceptable because agents read multiple candidates
                rather than relying on a single top result

SCALE (JetBrains' own reported figures):
  Latency bar:  results within "a couple of seconds at most"
  Index size:   "a few million chunks add up to tens of gigabytes of index"

PRIVACY ARCHITECTURE:
  Stored:    coordinates + metadata only — no source code content
  Snippet:   assembled client-side, from the user's own local checkout
  Embedding: computed with an open-weight model run on JetBrains-operated
             GPUs (not a third-party embedding API)

PRODUCT STATUS: JetBrains Context, public preview (per source)
SERIES STATUS: Part 1 of 4+; upcoming parts cover storage, millisecond
               query latency, continuous evaluation, and (per the
               Prospector's triage) agent integration
PREVIOUS POST IN JETBRAINS AI BLOG: "Our First Moves to Get AI Spend Under
               Control" (Aug 2026)

Source: JetBrains AI blog, "Building a RAG Pipeline for Semantic Code
Search: A Developer Diary and Field Notes," 2026-09-17
```

## Cross-References

- **Contradicts**: `blog-anthropic-large-codebase-best-practices.md` (Claims 2
  and 4) — Anthropic's post states that agentic search (filesystem
  traversal + grep, no embedding index) is the *correct* architecture for
  large, fast-moving codebases specifically because embedding-based RAG
  indexes go stale ("By the time a developer queries the index, it reflects
  the codebase as it existed days, weeks, or even hours ago") and require an
  embedding pipeline that cannot keep pace with commit velocity ("There's no
  embedding pipeline or centralized index to maintain as thousands of
  engineers commit new code"). This JetBrains source reaches the opposite
  architectural conclusion for a comparably large monorepo (IntelliJ IDEA,
  over a million files): that grep/keyword search is insufficient for
  abstract/conceptual queries and a purpose-built RAG index is necessary
  ("To reason through abstract domains, the agent needs the ability to
  search for code by meaning... This is where retrieval-augmented generation
  (RAG) comes into the picture" — captured via targeted fetch, treated as
  paraphrase pending verbatim confirmation). Critically, this Part 1
  installment does **not** engage with or rebut Anthropic's staleness
  argument at all — index freshness/incremental updates are explicitly
  deferred to a later part of the series (Claim 14). **Filed as contradiction
  issue #3546** (see `CONTRADICTIONS.md` once resolved); do not cite either
  source's position as the guide's settled recommendation on agent code
  search architecture until that issue is resolved. A follow-up source
  submission should be filed once JetBrains publishes the storage/freshness
  installment of this series, since that installment is most likely to
  directly address (or fail to address) Anthropic's core objection.

- **Corroborates**:
  - `blog-cursor-fast-regex-search.md` (Claim 9: client-side indexing for
    privacy, latency, and freshness; Claim 10: semantic and regex search
    are complementary with different staleness tolerances) — both this
    source's coordinates-only/local-reconstruction architecture (Claim 9
    above) and Cursor's fully local index are independently-arrived-at
    privacy architectures for code search infrastructure serving AI agents.
    Where they differ: Cursor frames semantic and lexical (regex) search as
    permanently complementary tools with different jobs; this JetBrains
    installment frames semantic search as necessary to replace grep for
    abstract queries but has not yet (as of Part 1) stated whether it
    intends grep/lexical search to remain in the toolset alongside RAG.
  - `blog-cursor-fast-regex-search.md` (Claim 12: search latency degrades
    agent "investigation" workflows) — this source's stated "couple of
    seconds at most" ceiling (Claim 11 above) is a concrete, independently
    stated latency bar that corroborates Cursor's broader claim that search
    latency is a first-order UX concern for agentic code search, not a
    background optimization.

- **Extends**: `docs-github-copilot-semantic-issue-search.md` (Claim 1: a
  purpose-built "semantic issues index" as new Copilot infrastructure) —
  that source documents semantic indexing applied to GitHub *issue* text;
  this source documents semantic indexing applied to *code* content, with
  substantially more implementation depth (chunking strategy, vectorization,
  storage optimization) than the brief GitHub changelog entry provides. Both
  corroborate that dedicated semantic indexes (distinct from generic
  full-text/keyword search) are becoming standard infrastructure investments
  across vendors (GitHub for issues, JetBrains and, per
  `blog-anthropic-large-codebase-best-practices.md`'s framing of the
  alternative, implicitly Cursor for code — though Cursor's own source note
  describes lexical rather than semantic indexing as its primary
  investment).

- **Novel**: The following are new to the corpus:
  - A concrete, worked example of language-aware structural code chunking
    (prefix/suffix attachment rules, Claim 4) with a named comparison to
    published academic work (cAST, Claim 5).
  - Binary quantization (32-bit float → 1 bit, Hamming distance instead of
    cosine similarity) as a production vector-storage optimization for code
    embeddings, including the explicit design argument that reduced ranking
    precision matters less for agent consumers than for human-facing UIs
    (Claims 7–8). No prior corpus source discusses vector quantization for
    code search.
  - The file-path-truncation heuristic for embedding inputs in
    deeply-nested monorepos (Claim 6) — a specific, previously undocumented
    engineering detail.
  - A coordinates-only, no-source-code-content index architecture with
    client-side snippet reconstruction (Claim 9) — a distinct privacy
    mechanism from Cursor's "keep the whole index local" approach.
  - Concrete index-size-at-scale figures (tens of gigabytes for a few
    million chunks, Claim 12) — the corpus previously had no code-RAG
    storage-scale reference point.

## Guide Impact

- **Ch03 (Retrieval & Context)**: Add JetBrains' structure-aware chunking
  rules (Claim 4: prefix/suffix attachment to declarations) and the
  fixed-size-chunking failure mode (Claim 2) as concrete guidance for teams
  building or evaluating code-RAG chunking strategies. Add the file-path
  truncation heuristic (Claim 6) as a specific, non-obvious detail for large
  monorepos. Flag the RAG-vs-agentic-search architectural question as
  **debated pending contradiction issue #3546** rather than presenting
  either Anthropic's or JetBrains' position as settled guidance.

- **Ch04 (Agentic Workflows / Context Engineering)**: Add the "ranking
  precision matters less for agent consumers than human UIs" argument
  (Claim 8) as a specific, citable design principle when discussing
  retrieval-quality tradeoffs for agent-facing (vs. human-facing) search
  systems. Add the "couple of seconds" latency ceiling (Claim 11) alongside
  Cursor's 15-second-grep-stall finding (`blog-cursor-fast-regex-search.md`)
  as concrete numbers for the guide's discussion of tool-latency budgets in
  agentic sessions.

- **Ch02 (Harness Engineering) or a Privacy/Data-Governance section**: Add
  the coordinates-only index + client-side snippet reconstruction + in-house
  open-weight embedding model architecture (Claims 9–10) as a concrete
  reference architecture for teams that need code-search infrastructure but
  cannot send source code to a third-party API for privacy, IP, or
  compliance reasons.

- **Follow-up mining**: Flag this as an active series — later installments
  (storage, millisecond query latency, agent integration, continuous
  evaluation) should be submitted as sources once published, since the
  storage/freshness installment in particular is likely to bear directly on
  contradiction issue #3546.

## Extraction Notes

- WebFetch on this URL returns a lossy, heavily summarized rendering rather
  than the raw article text (consistent with the experience documented in
  `blog-anthropic-large-codebase-best-practices.md`'s Extraction Notes). A
  first full-article fetch produced only a ~200-word bullet summary. To
  recover quote-accurate text, five additional targeted fetches were made,
  each asking for short (1–2 sentence) verbatim quotes on specific
  sub-topics (keyword-search limitations, chunking strategy, quantization,
  privacy, metrics, path truncation, cAST comparison, series roadmap).
- A final targeted fetch was performed to adversarially re-verify each
  candidate quote against the source text, asking the tool to confirm
  YES/NO whether each string appeared character-for-character and to supply
  the correction if not. Ten of eleven candidate quotes were confirmed
  verbatim; one (the "no content... is saved" privacy quote) was corrected
  to add a trailing clause ("...from your checkout, using them.") that the
  original candidate had dropped — the corrected version is what appears in
  Claim 9 above. This verification pass could not be run for Claims 10 and
  13 (the embedding-model-hosting detail and the "public preview" product
  status) because they surfaced only as paraphrase in the fetch responses
  and no exact candidate sentence was available to submit for verification;
  both are flagged inline as paraphrase-pending-confirmation rather than
  presented as direct quotes, per the Miner quoting rules.
  Whole-file-embedding as a rejected chunking approach (mentioned in Claim 2
  and the Concrete Artifacts block) is the Miner's synthesis of the
  surrounding argument rather than a captured quote, and is labeled as such.
- The article's embedded diagrams (a RAG pipeline flowchart, a vector-space
  visualization, and a path-truncation diagram, per one fetch's description)
  could not be extracted as text content — only the surrounding prose was
  available.
- No sub-pages or linked prior posts were fetched beyond noting the
  existence of the previous JetBrains AI blog post ("Our First Moves to Get
  AI Spend Under Control," Aug 2026) and the cited academic reference
  (cAST, Zhang et al. 2025); neither was read in full for this note, since
  neither was load-bearing for the claims extracted here. A follow-up
  Miner pass could read the cAST paper directly if the guide wants deeper
  technical grounding on the chunking algorithm.
- **Confidence rationale**: Set to `emerging` overall rather than `settled`
  because, while several individual claims describe concrete, checkable
  facts about a shipped product (settled-level confidence per-claim), the
  source's central architectural thesis — that RAG/semantic indexing is
  necessary for agentic code search — is asserted without engaging the
  staleness/maintenance-cost objection raised by a comparably authoritative
  first-party source (Anthropic), and the series itself is incomplete
  (freshness handling, evaluation, and agent-integration details are not
  yet published). The note should be revisited once later parts of the
  series are available.
- A contradiction with `blog-anthropic-large-codebase-best-practices.md`
  was identified during cross-referencing (Cross-References → Contradicts)
  and filed as issue #3546 per MINER.md §4a before this source note was
  opened. No verdict has been assigned; this note does not pick a side.
