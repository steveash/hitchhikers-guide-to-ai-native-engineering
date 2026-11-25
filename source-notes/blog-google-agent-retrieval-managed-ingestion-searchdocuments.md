---
source_url: https://developers.googleblog.com/from-files-to-cited-answers-in-one-api-call-managed-ingestion-and-searchdocuments-in-agent-retrieval/
source_type: blog-post
title: "From Files to Cited Answers in One API Call: Managed Ingestion and SearchDocuments in Agent Retrieval"
author: "Yingxin Jiang, Kaz Sato (Google)"
date_published: 2026-11-24
date_extracted: 2026-11-25
last_checked: 2026-11-25
status: current
confidence_overall: anecdotal
issue: "#4946"
---

# From Files to Cited Answers in One API Call: Managed Ingestion and SearchDocuments in Agent Retrieval

> Google vendor guide to a Public Preview managed document/video ingestion pipeline plus a one-call `SearchDocuments` API that returns page- or timestamp-cited segments — a concrete "buy, not build" option for agent retrieval, backed only by self-reported single-run timings.

## Source Context

- **Type**: blog-post (vendor how-to / product announcement, Google Developers Blog)
- **Author credibility**: A Google Software Engineer and a Staff Developer Advocate, writing about their own product. Authoritative on API shape; not independent on performance or on the build-vs-buy conclusion.
- **Scope**: Agent Retrieval (formerly Vector Search 2.0) data stores, `importDocuments`, `documents:search`, filters, reranking, video search with audio mode, production notes. Public Preview, v1beta REST, regions us-east4 / europe-west4 only. Does NOT report recall/precision, cost at scale, or comparisons with other managed or DIY pipelines.

## Extracted Claims

### Claim 1: Managed ingestion removes the hand-built parse → chunk → embed → store → learn-schema pipeline for files
- **Evidence**: Product description plus a Python/REST walkthrough (data store creation, import, search). Authority of the vendor; no independent measurement.
- **Confidence**: emerging
- **Quote**: "Managed ingestion builds the pipeline for you: point a data store at files in Cloud Storage, and the service parses, segments, and embeds them with Gemini Embedding 2."
- **Our assessment**: Plausible and consistent with the general trend of platforms absorbing RAG plumbing. The cost is coupling to one vendor's segmentation/embedding choices; the post offers the Collection escape hatch (Claim 7) to mitigate.

### Claim 2: A single `SearchDocuments` call, with no Collection/vector-field/task-type/output-field arguments, is enough for retrieval, and hybrid search runs automatically for documents
- **Evidence**: API example: `text_query` + `top_k` only; response shown.
- **Confidence**: emerging
- **Quote**: "SearchDocuments takes a data store and a text query. You don't pass a Collection name, a vector field, a task type, or output fields, and hybrid search (semantic + full-text) runs automatically for documents."
- **Our assessment**: A narrow tool surface is good for agent tool design (fewer parameters for the model to get wrong). Hybrid-by-default matches the semantic+keyword fusion described in the Bayer/PRINCE note, but here the weighting is not tunable in the shown API.

### Claim 3: Retrieval results should carry provenance (source URI plus page range or time range) so agents can cite where an answer came from
- **Evidence**: Documented result schema (`unstructuredDetails.pageRange`, `videoDetails.startOffset/endOffset`, `document.content.gcsUri`) and example output.
- **Confidence**: emerging
- **Quote**: "Every result carries its source file URI and a page range for documents, or a start and end time for videos, so your agent can cite exactly where an answer came from."
- **Our assessment**: The main transferable pattern. Citation metadata produced at ingestion time (not reconstructed after generation) makes grounding and human verification cheap. Segment-level provenance only; it does not guarantee the model quotes faithfully.

### Claim 4: Segmentation mode determines citation granularity — page segmentation gives one page per result; chunk segmentation (100–500 tokens, default) returns the page range each chunk spans
- **Evidence**: Config example (`page_segmentation_config`) and documented behavior.
- **Confidence**: emerging
- **Quote**: "Two segmentation modes are available. Chunk segmentation (the default) splits text into chunks of 100 to 500 tokens and works with layout parsing, which also detects tables and headings."
- **Our assessment**: Useful design knob: citation precision trades off against chunk coherence. The post gives no data on which mode retrieves better.

### Claim 5: Metadata filters and document scoping narrow retrieval before ranking, using the same paths returned in results
- **Evidence**: A single anecdotal test: a "page-1" filter on a CEO-quote query.
- **Confidence**: anecdotal
- **Quote**: "In our test, searching \"What did the CEO say about AI?\" with the page-1 filter returned the CEO quotes from the headline page of five different earnings releases."
- **Our assessment**: Illustrates structural filtering as a retrieval lever, but the post's exemplar is one hand-picked query.

### Claim 6: Turning on a reranker fixed a hybrid-search failure on a headcount query
- **Evidence**: One query ("How many employees does Alphabet have?"), before/after comparison, no aggregate metrics, no baseline beyond plain hybrid search.
- **Confidence**: anecdotal
- **Quote**: "For \"How many employees does Alphabet have?\", plain hybrid search returned two balance sheet pages among the top five, which don't mention employees at all."
- **Our assessment**: Consistent with the reranking step in the Bayer/PRINCE note, but a single cherry-pickable example. Not evidence of general improvement.

### Claim 7: The managed data store sits on top of an ordinary Collection, so direct control remains available when needed
- **Evidence**: Architectural statement; "Architecture Summary" section (decision table rendered as an image, not extractable).
- **Confidence**: emerging
- **Quote**: "The backing Collection is still a regular Agent Retrieval Collection, so you can query it directly whenever you need full control."
- **Our assessment**: A good "layered escape hatch" design: high-level default, low-level fallback. The rule of thumb below is the post's decision guidance.

### Claim 8: Rule of thumb — if data is files, use a data store; drop to the Collection only when needed
- **Evidence**: Authorial recommendation; no comparative data.
- **Confidence**: anecdotal
- **Quote**: "The rule of thumb: If your data is files, let a data store ingest them and search with SearchDocuments. Drop down to the Collection only when you need control the data store doesn't give you."
- **Our assessment**: Vendor-interested default. Reasonable for prototypes; production teams should check schema control, data residency (two preview regions), and lock-in.

### Claim 9: Video can be searched by visuals and, with audio mode enabled, by what was said, without transcripts; queries returned in 0.3–0.5 s
- **Evidence**: Five Google sample videos (~19 min), one scene query ("Cucumbers being sorted by a machine"), and an audio-on vs audio-off comparison on keynote statements; latency self-reported.
- **Confidence**: anecdotal
- **Quote**: "Searches returned in 0.3 to 0.5 seconds."
- **Our assessment**: Small, vendor-chosen dataset; single run. Interesting for multimodal agent context, but no accuracy figures.

### Claim 10: Vendor-reported ingestion timing: 18 PDFs searchable in about 9 minutes
- **Evidence**: Self-reported test on public Alphabet investor PDFs.
- **Confidence**: anecdotal
- **Quote**: "In our tests, 18 Alphabet investor PDFs went from a public Cloud Storage bucket to searchable, page cited results in about 9 minutes"
- **Our assessment**: Record as a vendor claim only. No file sizes/pages given, no variance.

### Claim 11: Production considerations: video imports are slow, preview is free during preview, cleanup of the backing Collection is manual, reranking is not available for video
- **Evidence**: Authorial operational notes with measured durations.
- **Confidence**: emerging
- **Quote**: "Importing our five videos into two data stores took 20 to 45 minutes."
- **Our assessment**: Honest caveats worth preserving: import is asynchronous (long-running operation) so agents must not assume freshly added files are searchable; orphaned Collections are a cost/hygiene hazard; "managed ingestion itself incurs no separate charge during Public Preview (billing will start at GA)" means cost is not yet known.

### Claim 12: Managed ingestion does not change what good retrieval needs, only who builds it
- **Evidence**: Concluding statement.
- **Confidence**: emerging
- **Quote**: "Managed ingestion doesn't change what good retrieval needs: well-segmented content, good embeddings, and the right filters."
- **Our assessment**: A fair framing: the quality levers (segmentation, embeddings, filters, reranking) remain; they are now configuration, not code.

## Concrete Artifacts

Data store creation (verbatim from source, abridged to the config body):

```python
session.post(
    f"{PARENT}/dataStores",
    params={"data_store_id": "investor-reports"},
    json={
        "document_type": "UNSTRUCTURED",
        "processing_config": {
            "unstructured_processing_config": {
                # One segment per page, so results carry page numbers
                "segmentation_config": {"page_segmentation_config": {}},
                "parsing_config": {"digital_parsing_config": {}},
            }
        },
        # Metadata you can filter on and return in search
        "document_metadata_schema": {
            "schema": {
                "type": "object",
                "properties": {
                    "doc_type": {"type": "string"},
                    "year": {"type": "integer"},
                },
            }
        },
    },
)
```

Search call and cited result (from the post):

```python
response = session.post(
    f"{PARENT}/dataStores/investor-reports/documents:search",
    json={
        "text_query": {"text": "How much did Google Cloud revenue grow?"},
        "top_k": 5,
    },
).json()
```
```json
{
  "document": {
    "name": ".../dataStores/investor-reports/documents/2022-annual-report",
    "content": {"gcsUri": "gs://.../2022_alphabet_annual_report.pdf"}
  },
  "unstructuredDetails": {
    "contentSnippet": "... Google Cloud revenues increased $7.1 billion from 2021 to 2022 ...",
    "pageRange": {"startPage": "68", "endPage": "68"}
  }
}
```

Reranking toggle and video config:

```python
"ranking_spec": {"reranking_spec": {"enabled": True}}
```
```
"document_type": "VIDEO",
"processing_config": {
    "video_processing_config": {
        "segmentation_config": {"fixed_window_config": {"segment_duration": "20s"}},
        "embedding_config": {"audio_mode": "ENABLED"},
    }
},
```

Availability (from "Requirements & Next Steps"): us-east4 or europe-west4 only; v1beta REST; Python SDK planned; grant `roles/vectorsearch.serviceAgent` to the Agent Retrieval service agent.

Vendor-reported measurements: ~9 min for 18 PDFs; 0.3–0.5 s per video query; 20–45 min to import five videos into two data stores; ~20 min data-store deletion; default video segment 30 s (10–20 s precise, up to 80 s for thematic context).

## Cross-References

- **Corroborates**: `blog-fowler-bayer-prince-agentic-rag.md` — Claim 6 (hybrid semantic + keyword retrieval followed by a reranker) and Claims 10–11 (grounding with citations to source documents and pages). This post offers the same pattern as a managed product.
- **Contradicts**: None found.
- **Extends**: `blog-thoughtworks-penumarthi-jev-rag-pipelines.md` — its Claim 2 lists ingestion as a RAG stage with cost; this post is a platform-level way to remove that stage. `blog-jetbrains-rag-semantic-code-search.md` — Claims 2–3 show a bespoke chunking pipeline built for code; this post is the generic-document counterpoint (managed chunking, no structure-aware code parsing).
- **Novel**: Managed ingestion as a build-vs-buy option; citation metadata (page range / time range) as a first-class result field; audio-aware video retrieval for agents; the "high-level data store over regular Collection" escape-hatch design.

## Guide Impact

- **Chapter 04 (context engineering)**: Where retrieval-as-a-tool is discussed, add this as an example of a narrow, citation-returning retrieval tool and of managed ingestion as an alternative to custom pipelines. Flag all performance figures as vendor-reported, single-run, preview-stage.
- **Chapter 02 (harness/tools)**: Optional: note the "one call, few parameters" tool shape as a tool-design example; async ingestion implies freshness caveats.

## Extraction Notes

- Fetched and read the full page HTML as text; the page has no sub-pages worth following (references link to Google Cloud docs and notebooks, not read).
- Several figures in the post (the "Before/After" and "Architecture Summary" diagrams, filter examples, audio comparison) are images/embeds and not extractable; claims relying on them are limited to surrounding text.
- All evaluations are anecdotal; no recall/precision numbers. Public Preview — not GA.
