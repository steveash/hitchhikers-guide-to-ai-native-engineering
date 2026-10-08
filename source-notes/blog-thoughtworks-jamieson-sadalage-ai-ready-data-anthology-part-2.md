---
source_url: https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/ai-ready-data-part-2
source_type: blog-post
title: "AI-ready data: The anthology - Part 2 of 2"
author: Anne Jamieson, Pramod Sadalage (Thoughtworks)
date_published: 2026-10-06
date_extracted: 2026-10-08
last_checked: 2026-10-08
status: current
confidence_overall: anecdotal
issue: "#3990"
---

# AI-ready data: The anthology - Part 2 of 2

> Part 2 operationalizes Part 1's data prerequisites with five short, analogy-driven claims: API-vs-SQL access is governance vs. flexibility, vector/RAG needs machine-ready documents, lineage and observability are complementary, batch comes before real-time, and a "new employee" test checks readiness.

## Source Context

- **Type**: blog-post
- **Author credibility**: Anne Jamieson and Pramod Sadalage of Thoughtworks. Sadalage is also a co-author of the Aug 2026 "Making Your Data Ready for Agentic AI" piece. The article carries a disclaimer that opinions are the authors' own and not Thoughtworks' positions.
- **Scope**: Covers API vs. SQL data access, unstructured/vector data, lineage vs. observability, a vector/RAG readiness audit, and batch-before-real-time sequencing. It has no metrics, client cases, code or tooling. Each section pairs a short claim with an extended analogy (transit/driving, detective, smartwatch, auditor, drive-in restaurant). The analogies are illustration, not evidence, and were not extracted as claims.

## Extracted Claims

### Claim 1: API vs. SQL access for AI is a governance-versus-flexibility trade-off
- **Evidence**: Assertion by analogy (public transit vs. driving). No measurements or incidents.
- **Confidence**: anecdotal
- **Quote**: "This battle of the TLAs (three-letter acronyms) is really a question of governance versus flexibility."
- **Our assessment**: The trade-off is reasonable and matches common practice. The article offers no data on how often hallucinated SQL or injection occurs, and it does not mention intermediate options such as a semantic layer, which the Fowler note covers.

### Claim 2: API access costs more setup and latency but is more secure, because it goes through defined endpoints
- **Evidence**: Asserted without examples.
- **Confidence**: anecdotal
- **Quote**: "Accessing data via APIs typically requires more setup and results in higher latency, but it is a more secure approach as it leverages tools to access the data via defined endpoints."
- **Our assessment**: A plausible default, but "more secure" depends on how the endpoints are scoped. Broad endpoints erode the benefit (compare the tool-sprawl point in the Fowler note).

### Claim 3: Direct SQL access needs relational understanding by the AI and adds hallucination and SQL-injection risk
- **Evidence**: Asserted. The risks are named but not quantified.
- **Confidence**: anecdotal
- **Quote**: "it requires less setup as the AI can directly access the underlying data, but it can introduce additional risks like hallucinations and SQL injection."
- **Our assessment**: The risk is real. The only mitigation offered is the analogy to a driver's licence: permissions on the types of queries that can be executed. No concrete controls are given, such as read-only roles, query allow-lists or row-level security.

### Claim 4: Vectorizing unstructured data has three named challenges: freshness, permission carry-through, and context loss from chunking
- **Evidence**: Asserted, with no examples or tooling.
- **Confidence**: anecdotal
- **Quote**: "In the breakdown to smaller units, there is a high risk of separating the context from a given datapoint."
- **Our assessment**: The three challenges are the useful content here. The note's own statement of the other two: vectors must be kept up to date as source data changes, and source permissions may be hard to enforce in the AI system. The Fowler note has the concrete fix for freshness (see Cross-References).

### Claim 5: Metadata is the "red string" that links disparate sources and gives context to individual pieces
- **Evidence**: Detective analogy only.
- **Confidence**: anecdotal
- **Quote**: "In a data ecosystem, that red string is metadata linking disparate data sources."
- **Our assessment**: Consistent with Part 1's metadata/catalogue claim. The article also notes that only relevant information should be presented, which is an unelaborated hint at retrieval filtering.

### Claim 6: Lineage and observability are complementary: each makes the other useful
- **Evidence**: Smartwatch/medical-history analogy. The analogy's point is that monitoring without a historical baseline has no reference point, and history without fresh data goes unnoticed.
- **Confidence**: anecdotal
- **Quote**: "Lineage answers “How did we get here?”, and observability asks, “How are we doing right now?”."
- **Our assessment**: A neat, citable framing of two terms that are often conflated. It stays at the level of definition and gives no implementation guidance. The Fowler note's agentic-lineage claim (reasoning traces) is much more specific.

### Claim 7: High data volume and unfettered access do not make an organization RAG-ready, because human-optimized documents are not machine-optimized
- **Evidence**: Assertion plus an auditor analogy (receipts and scrawled calculations vs. bookkeeping software).
- **Confidence**: anecdotal
- **Quote**: "Often, documents that are optimized for human consumption are not optimized for machine consumption."
- **Our assessment**: Directionally right and widely observed. No test or checklist is given beyond the stated attributes in Claim 8, despite the "audit" in the section title.

### Claim 8: AI-ready data for RAG must be hygienic (common formats, minimal missing information) and carry complete context (rich metadata and tagging), which also enables permissions management
- **Evidence**: Asserted via the auditor analogy.
- **Confidence**: anecdotal
- **Quote**: "AI needs to work with data that is hygienic (common formats, minimal missing information) as well as includes complete context (rich metadata and tagging)."
- **Our assessment**: This is the closest the article comes to a checklist. It echoes Part 1's quality claim (consistent nulls and formats) and extends it to document corpora.

### Claim 9: Build a batch AI data platform first, then add real-time ("walk before you run")
- **Evidence**: Assertion; the drive-in analogy illustrates how a stall in a streaming lane raises latency for the whole system.
- **Confidence**: anecdotal
- **Quote**: "“Walk before you run” is apt for developing data platforms."
- **Our assessment**: A sensible sequencing heuristic with no supporting data. It matches the Fowler note's dependency-ordered view (Claim 16 there), though it applies the ordering to batch/real-time rather than to data layers.

### Claim 10: Real-time AI data requires timestamped streams, immediate updates to operational memory, and low-latency serving; otherwise the system acts on stale inputs
- **Evidence**: Asserted.
- **Confidence**: anecdotal
- **Quote**: "Failure to do so risks performing operations with stale inputs."
- **Our assessment**: Three requirements are named: accurate, standard-format timestamps so out-of-order events can be tied to sessions; immediate update of the engine's operational memory; and minimal-latency serving. This is the only claim in the article that reads as a requirements list. It is thin on how to achieve any of them.

### Claim 11: The "new employee" question is a readiness test for AI-ready data
- **Evidence**: Offered as a heuristic, not validated.
- **Confidence**: anecdotal
- **Quote**: "can a new employee understand, find, trust and use the data without asking five people for help?"
- **Our assessment**: A memorable, cheap check, and it is consistent with the agent-readability test in the Xiong/Asthagiri/Kulkarni note (the "agent handed this product cold" test). It is binary and unmeasured.

## Concrete Artifacts

No code, configuration, metrics or transcripts are in the source. The only structured material is the pair of access-mode descriptions and the real-time requirements list (Claims 1-3, 10), in the authors' words:

```
Source: Jamieson & Sadalage, Part 2 (2026-10-06)
API access:  more setup, higher latency, more secure (defined endpoints)
SQL access:  less setup, AI must understand relationships across the data,
             risks: hallucinations, SQL injection
             mitigation named: permissions on the types of queries which can be executed
Real-time requirements: precise standard-format timestamps; immediate update of
             operational memory; minimal-latency serving
```

## Cross-References

- **Corroborates**: `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim 2 (stale data produces confidently wrong outcomes) and Claim 6 (vector index freshness for unstructured data), which cover the same freshness concern with far more specific mechanisms. `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` Claim 2 (temporal validity as a required data property) and Claim 7 (agent-readability test) support Claims 10 and 11 here.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-thoughtworks-jamieson-sadalage-ai-ready-data-anthology.md` Claim 8, which deferred operationalization to Part 2; Claim 3 there (data hygiene) is extended to document corpora in Claim 8 here.
- **Novel**: The explicit API-vs-SQL framing as governance vs. flexibility, the lineage/observability pairing, the batch-before-real-time sequencing, and the "new employee" test. All are asserted without evidence.

## Guide Impact

- **Chapter 04**: If the guide discusses RAG or data readiness, this source can be cited (as anecdotal) for the three vectorization hazards in Claim 4: stale vectors, lost source permissions, and context loss from chunking. Prefer the Fowler note for the freshness mechanism.
- **Chapter 04 / Chapter 06**: The API-vs-SQL trade-off (Claims 1-3) could be a one-line framing for agent data access, with the SQL guardrail point (query-type permissions) linked to Chapter 06. It should not be cited as evidence for the claim that SQL access is riskier.
- **Chapter 02**: The "new employee" test (Claim 11) could be offered as a lightweight readiness heuristic.
- No existing chapter recommendation needs to change on the strength of this source.

## Extraction Notes

- The full article was fetched as HTML and read end to end, including the closing "You need brakes to go fast" section that the Prospector flagged as possibly truncated. The page text is about 12k characters.
- No linked sub-pages were followed. The page links only to Part 1 and a related Thoughtworks piece, both already tracked.
- The Prospector comments variously suggested Ch02, Ch04 and Ch06 as relevant; the Guide Impact section lists the specific places.
- The Prospector asked that anecdotes not be extracted as evidence. They were left out of the claims and mentioned only as the vehicle for each claim.
- Quotes containing curly quotation marks are reproduced as they appear in the source.
