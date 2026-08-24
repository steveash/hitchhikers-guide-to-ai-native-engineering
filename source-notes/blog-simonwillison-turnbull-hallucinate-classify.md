---
source_url: https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/
source_type: blog-post
title: "Don't classify. Hallucinate!"
author: Simon Willison (link-blog note); primary essay by Doug Turnbull (softwaredoug.com)
date_published: 2026-08-14
date_extracted: 2026-08-24
last_checked: 2026-08-24
status: current
confidence_overall: emerging
issue: "#2902"
---

# Don't Classify. Hallucinate!

> Doug Turnbull's technique for classifying free text against a large,
> closed vocabulary: ask a cheap LLM to invent a plausible-but-fake
> classification without ever showing it the real taxonomy, then use
> vector embeddings to resolve the invented label to the nearest real
> one — sidestepping the token-budget and per-request schema cost of
> constrained/structured-output classification against hundreds of
> legal values.

## Source Context

- **Type**: blog-post. The proximate source
  (`simonwillison.net/2026/Aug/14/dont-classify-hallucinate/`) is Simon
  Willison's "link-blog" format — two short paragraphs of his own framing
  plus a verbatim excerpt of the example prompt, with a link to the primary
  essay. Per MINER.md §1, this note follows that outbound link to the
  primary source: Doug Turnbull's "Don't classify. Hallucinate!"
  (`softwaredoug.com/blog/2026/08/10/hypothetical-classifications`,
  published August 10, 2026), which is where nearly all of the extractable
  content below comes from. Both pages were fetched directly via `curl` and
  read in full (each is short — one screen of prose plus code blocks); no
  further sub-pages were followed (see Extraction Notes for why the two
  linked artifacts — a Colab notebook and a GitHub utility file — were not
  fetched).
- **Author credibility**: Simon Willison is a widely-cited LLM-tooling
  commentator (already a trusted feed in this corpus) whose link-blog notes
  surface claims for attention without independently endorsing their
  technical soundness. Doug Turnbull (`softwaredoug.com`, bio in this
  source: search relevance consultant, host of a "Vectors Week" event series
  on vector retrieval and hybrid search, prior speaking/training credits per
  his site's author box) is a working search-relevance practitioner
  describing his own applied technique with runnable code and a worked
  example against a named public dataset (Wayfair WANDS). This is
  first-party engineering content from a domain specialist, not third-party
  reporting — but it is a single practitioner's pattern on one dataset, with
  no comparative benchmark against the constrained-decoding baseline it
  replaces.
- **Scope**: Covers one specific problem (classifying a search query or
  product description against a large, closed taxonomy) and one specific
  technique (unconstrained "hallucination" generation followed by embedding
  resolution), illustrated with the Wayfair WANDS furniture/home-goods
  taxonomy. Does NOT cover: accuracy/precision comparison between the
  hallucinate-then-embed approach and the structured-output baseline it's
  positioned against, cost figures (dollar or latency) for either approach,
  behavior when the hallucinated label is a poor match for any real
  category (no fallback/confidence-threshold discussion), multi-label
  classification, or non-e-commerce domains.

## Extracted Claims

### Claim 1: Constraining LLM classification output to a large legal vocabulary via structured outputs (e.g., a Pydantic `Literal` of every category) works, but does not scale cheaply — there is an upper limit on how many legal values can be sent, and cost/latency motivate an alternative for large taxonomies

- **Evidence**: Turnbull walks through the standard structured-output implementation in full — a Pydantic model with a `Literal` type listing every legal classification ("times 500"), fed to `client.responses.parse` — then states its limitation and links to OpenAI's own structured-outputs documentation as the source for the stated upper bound.
- **Confidence**: emerging (a working-practitioner's stated limitation, with a link to vendor documentation as evidence for the "upper limit" claim, but no specific number, dollar cost, or latency figure given in the source itself)
- **Quote**: "This works. But there's a way to do this a lot cheaper with small / dumb models at scale. Not to mention, there's an upper limit you can send"
- **Our assessment**: The "upper limit" claim is asserted with a hyperlink to OpenAI's structured-outputs guide rather than a stated number — treat the existence of some ceiling as more solidly evidenced than any specific figure, since Turnbull does not quote one. The cost/scale motivation ("a lot cheaper with small / dumb models") is the article's stated justification for the alternative technique but is not independently measured in this source.

### Claim 2: The core technique — tell the LLM to invent classifications with zero knowledge of the real vocabulary, then use vector embeddings against the real corpus to find the closest actual entries to what it imagined

- **Evidence**: Turnbull's explicit statement of the pattern, restated by Willison in his own words as the framing for the whole post.
- **Confidence**: emerging (a named, described pattern with a full worked code example in the same source, but not validated against ground truth or a baseline in this article)
- **Quote**: "Just ask a dumb LLM to invent plausible, fake classifications for your query" ... "It's very cheap to build an in-memory set of embeddings of the REAL classifications... I compute the embedding of the fake, hypothetical embedding from the LLM. I then dot product the fake embedding into the real ones to find the most similar."
- **Our assessment**: This is the article's central contribution and the reason the Prospector flagged it as high-novelty. The technique inverts the usual expectation that hallucination is a failure to be suppressed (see Cross-References — this framing tension, not a topical contradiction) — here, generative divergence from the true vocabulary is deliberately invited because the invented label is never used directly; it is only a proxy vector for a nearest-neighbor lookup against the real, closed set. The design only works because the failure mode is bounded: whatever the model invents, the final output is always drawn from the real vocabulary via embedding resolution, not from the model's raw (possibly nonexistent) text.

### Claim 3: A worked example shows the mechanism end-to-end — the LLM invents "Furniture / Living Room / Tables / Coffee" (a category that does not exist in the real taxonomy) for the query "brown coffee table," and embedding resolution correctly maps it to the real category "Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables"

- **Evidence**: A directly reproduced before/after pair in the source: the fake, invented label, followed by the resolved real label after embedding lookup.
- **Confidence**: settled (a specific, concrete, reproducible worked example given directly in the source, not a general/abstract claim)
- **Quote**: "It'll then make up some BS that doesn't actually exist in your real taxonomy like:" [code block] "Furniture / Living Room / Tables / Coffee" ... "I then dot product the fake embedding into the real ones to find the most similar. Producing:" [code block] "Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables"
- **Our assessment**: This single worked example is the strongest evidence in the source — it is fully specified (exact input query, exact hallucinated string, exact resolved output) and independently reproducible from the linked notebook/utility. It is, however, one example on one query; the source does not report an error rate, a set of failure cases, or behavior when the invented label is semantically distant from every real category (e.g., what happens if the model hallucinates a category unrelated to any real entry — no confidence threshold or fallback is discussed).

### Claim 4: The technique lets classification run on small/cheap ("dumb") LLMs at scale, and removes the need to transmit the full classification schema/vocabulary on every request

- **Evidence**: Direct statement contrasting the hallucinate-then-embed approach with the structured-output approach's per-request schema cost.
- **Confidence**: emerging (a stated design benefit, not measured against the structured-output baseline for cost or latency in this source)
- **Quote**: "You can give these hallucination tasks to dumb / cheap LLMs. And you don't need to ship the schema over to the LLM every time."
- **Our assessment**: This is the practical payoff claim and the one most relevant to cost-conscious production classification pipelines — if true, it changes the model-tier decision for a classification task from "needs a capable model to respect a 500-item enum constraint" to "needs any model competent enough to free-generate a plausible label in the right domain." No dollar or token-count comparison is given, so this should be treated as a directional, plausible claim pending independent measurement.

### Claim 5: The implementation detail — a lightweight sentence-embedding model (MiniLM) embeds every real classification once, in memory, and resolution is a single dot-product nearest-neighbor lookup against the hallucinated label's embedding

- **Evidence**: Turnbull's description of his own implementation, with links to a runnable Colab notebook and a GitHub source file implementing the vocabulary-resolution utility.
- **Confidence**: settled (a specific, named implementation choice — MiniLM, dot product — stated directly by the person who built it, with linked runnable code as backing)
- **Quote**: "In the notebook, I compute a MiniLM embedding of every real Wayfair classification. I compute the embedding of the fake, hypothetical embedding from the LLM. I then dot product the fake embedding into the real ones to find the most similar."
- **Our assessment**: MiniLM is a small, cheap sentence-embedding model — consistent with the article's stated "cheap at scale" framing extending to the resolution step as well as the generation step. The "in-memory set of embeddings" detail implies the real vocabulary's embeddings are precomputed once and reused across queries, which is standard nearest-neighbor practice, but worth noting explicitly since it means the technique's per-query cost is one small-model generation plus one embedding plus one dot-product scan, not a second LLM call.

### Claim 6: The prompt supplies example categories in the taxonomy's hierarchical *shape* (e.g., "Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables") without listing the actual legal vocabulary, to guide the model's output format without constraining its content to real values

- **Evidence**: The verbatim hallucination prompt, reproduced in both Willison's excerpt and Turnbull's original post, showing six example category strings followed by the target query.
- **Confidence**: settled (the exact prompt text is given verbatim in the source, reproduced in this note's Concrete Artifacts)
- **Quote**: "Your task is to create novel, never seen before, furniture, home goods, or hardware classification that best fit a search query. \n\nProduct classifications might look like: \n\nFurniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables \n..."
- **Our assessment**: This is a subtle but important prompt-engineering detail: the six example categories shown are real categories from the actual taxonomy (they appear elsewhere in the article as genuine WANDS classifications), but the prompt never tells the model this is the closed set or that it must choose from among them — it explicitly instructs the model to invent something "never seen before." The examples teach delimiter conventions, depth, and vocabulary register (e.g., "Coffee Tables & End Tables" style naming) without constraining the output to only those six or their descendants. This format-shape-without-content-constraint distinction is the mechanism that keeps the token cost low (six examples vs. hundreds of legal values) while still producing an embeddable, resolvable output.

### Claim 7: Simon Willison generalizes the technique beyond e-commerce product classification to any large, closed tagging vocabulary — specifically citing his own blog's 1,856-tag vocabulary as "likely too many to feed to an LLM in one go"

- **Evidence**: Willison's own framing paragraph, written before the excerpt from Turnbull's post, stating his own motivating problem (untagged older blog content) and vocabulary size.
- **Confidence**: anecdotal (Willison's own stated motivation for reading the post; no report yet that he has applied the technique to his own tagging backlog)
- **Quote**: "I still have quite a bit of older content on my blog that I never got round to tagging. My blog has 1,856 tags - likely too many to feed to an LLM in one go and say 'which of these tags match the following content'."
- **Our assessment**: This generalization is Willison's own addition, not part of Turnbull's original post — it extends the technique's applicability from product-category classification (Turnbull's domain) to free-form content tagging (Willison's domain), which is a different retrieval shape (many-to-many tag assignment vs. single-category classification) that the source does not itself demonstrate working. Treat this as a plausible extension flagged by a credible commentator, not a validated second use case.

## Concrete Artifacts

### Structured-output baseline (verbatim, from Turnbull's post)
```
Source: https://softwaredoug.com/blog/2026/08/10/hypothetical-classifications
Author: Doug Turnbull, published August 10, 2026

from typing import Literal
from pydantic import BaseModel, Field

FullyQualifiedClassifications = Literal[
 'Furniture / Bedroom Furniture / Beds & Headboards / Beds',
 'Furniture / Living Room Furniture / Chairs & Seating / Accent Chairs',
 'Rugs / Area Rugs',
  ...
  # times 500
]

class QueryClassification(BaseModel):
    """
    Structured representation of a search query for furniture e-commerce.
    Inherits keywords from the base Query model and adds category and sub-category.
    """
    classifications: list[FullyQualifiedClassifications] = Field(
        description="A possible classification for the product."
    )

response = client.responses.parse(
    model="gpt-5.4-mini",
    input="Classify the query: brown coffee table",
    text_format=QueryClassification,
)

print(response.output_parsed.message)
# Outputs: Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables
```

### Hallucination prompt and resolution call (verbatim, from Turnbull's post)
```
Source: https://softwaredoug.com/blog/2026/08/10/hypothetical-classifications

hallucination_prompt = f"""
Your task is to create novel, never seen before, furniture, home goods, or hardware classification that best fit a search query.

Product classifications might look like:

Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables
Décor & Pillows / Decorative Pillows & Blankets / Throw Pillows
Furniture / Bedroom Furniture / Dressers & Chests
Kitchen & Tabletop / Kitchen Organization / Food Storage & Canisters
School Furniture and Supplies / School Furniture / School Chairs & Seating / Stackable Chairs
Baby & Kids / Toddler & Kids Bedroom Furniture / Kids Beds

Here's the query to generate classifications for:

brown coffee table
"""

response = client.responses.parse(
    model="gpt-5.4-mini",
    input=hallucination_prompt,
    text_format=list[str],
)

# Hallucinated output: "Furniture / Living Room / Tables / Coffee"
# (does not exist in the real taxonomy)

# Resolved via MiniLM embedding dot-product against real classifications:
# "Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables"
```

### Referenced (not independently fetched) implementation artifacts
```
Colab notebook (MiniLM embedding + resolution demo):
https://colab.research.google.com/drive/1ljk72SBRuqWIijuEusCnDbhG1WAfZFcC#scrollTo=RZ-hEr-CSr9T

GitHub utility (vocabulary resolution code):
https://github.com/softwaredoug/cheat-at-search/blob/main/cheat_at_search/enrich/vocabulary.py

Dataset referenced: Wayfair WANDS e-commerce product/query dataset
```

## Cross-References

- **Extends**: `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 4
  (that source frames graph traversal against a populated, entity-resolved
  structure as superior retrieval to "guessing from surface similarity" via
  embeddings). This source's technique is a narrower, different use of
  embedding similarity than the retrieval Asthagiri's note critiques: here,
  embedding similarity is not the primary retrieval mechanism over
  unstructured text — it is a resolution/snapping step against a small,
  fully-enumerable closed vocabulary (hundreds of categories, not a general
  document corpus), where nearest-neighbor lookup is exactly the right tool
  because the target set is finite and complete. Not a contradiction: the
  two sources describe embedding similarity applied to different problem
  shapes (open-ended document retrieval vs. closed-vocabulary snap-to-nearest).
- **Extends**: `docs-github-copilot-semantic-issue-search.md` (Claim 1,
  Claim 3) — that source documents a purpose-built "semantic issues index"
  letting GitHub Copilot Chat surface issues by intent rather than exact
  keyword match. Both sources use embedding-based semantic matching to route
  around a vocabulary/keyword mismatch problem, but this source's technique
  is more specific: rather than matching a natural-language query directly
  against indexed real content (Copilot's approach), Turnbull's pattern
  first generates a synthetic, unconstrained label and only then resolves it
  — an extra hallucination step that Copilot's documented approach does not
  need because it queries the real corpus directly.
- **Contradicts**: None filed as a formal contradiction issue. There is a
  notable *framing* tension worth flagging for editorial awareness rather
  than a filed contradiction: `blog-thebatch-gpt55-hallucination-kimi-k26.md`
  (Claims 2–3) documents hallucination and confabulation as failure modes to
  be minimized and independently verified against (e.g., "GPT-5.5 falsely
  claimed to complete an impossible programming task in 29% of samples").
  This source instead deliberately invites unconstrained, fabricated output
  as an intermediate step. Per MINER.md §4a, this is not filed as a
  contradiction because the two sources are not making opposing claims about
  the same mechanism: The Batch's concern is models fabricating claims about
  task state/completion that are consumed as ground truth (high-stakes,
  unresolved fabrication); Turnbull's technique fabricates a disposable
  intermediate label that is never trusted directly and is always resolved
  against a real, closed vocabulary before use (low-stakes, always-resolved
  fabrication). The distinguishing factor — whether the hallucinated output
  is consumed directly or only used as a proxy for a bounded lookup — is
  worth capturing in the guide as the condition under which "letting the
  model hallucinate" is safe versus dangerous.
- **Novel**: The hallucinate-then-embed-to-resolve pattern for
  closed-vocabulary classification is new to this corpus. No existing source
  note documents using an LLM's free-generation output as an intermediate,
  disposable proxy vector for nearest-neighbor resolution against a real
  taxonomy, nor the specific cost/scale argument (avoiding per-request
  transmission of a large legal-value enum) that motivates it over
  structured-output constrained decoding.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add "hallucinate-then-resolve" as a
  named pattern for classification/tagging against large closed vocabularies
  that don't fit in a single prompt's structured-output schema (Claims 1–2,
  6). Frame it as an alternative to shipping the full legal-value enum on
  every request: generate an unconstrained candidate label using a cheap
  model and a small set of shape-only examples (Claim 6), then resolve via
  embedding nearest-neighbor against a precomputed, in-memory index of the
  real vocabulary (Claim 5). This is a concrete technique for the general
  "taxonomy too large for context window" problem the Prospector flagged.
- **Chapter 04 (Context Engineering)**: Note the safety condition implicit
  in the technique (see Cross-References — Contradicts discussion): this
  pattern is safe specifically because the hallucinated output is never
  consumed directly — it is always snapped to a real value via nearest-
  neighbor lookup before use. Any guide language recommending this pattern
  should state that condition explicitly, distinguishing it from cases where
  a model's free-generated claim (e.g., "I completed the task") is trusted
  without independent resolution against ground truth — the exact failure
  mode documented in `blog-thebatch-gpt55-hallucination-kimi-k26.md`.
- **Chapter 02 (Harness Engineering)**: Add as a cost/model-tier
  optimization: when a classification task's vocabulary is too large to
  send as a constrained schema, this technique permits routing to a smaller,
  cheaper model for the generation step (Claim 4) since the model's output
  is never used directly — only its embedding. This is a concrete instance
  of matching model capability to task risk (low-stakes intermediate output
  can use a weaker model) that the guide's model-selection guidance could
  cite as a worked example.

## Extraction Notes

- **Two-hop source, both fetched in full via `curl`**: Simon Willison's
  page is a short link-blog note (two paragraphs plus the excerpted
  prompt); Doug Turnbull's linked essay is where nearly all substantive
  content originates. Both were retrieved as raw HTML directly (not via
  WebFetch summarization) and every `Quote` field above was copied
  character-for-character from that raw HTML, per MINER.md §2a. An initial
  WebFetch call against the Willison URL returned only a paraphrased
  summary and was not used for any quote.
- **Two linked implementation artifacts not independently fetched**: the
  Colab notebook and the GitHub utility file (`vocabulary.py`) referenced
  in Claim 5 are runnable code, not additional prose content, and were
  judged out of scope for MINER.md's "follow up to 5 linked pages that seem
  substantive" guidance, which targets prose/documentation pages. Their
  URLs are preserved in Concrete Artifacts for any future Miner or reader
  who wants to verify the implementation directly.
- **No accuracy/error-rate data in the source**: This is the most
  significant gap for guide-writing purposes — the source shows the
  technique working on exactly one worked example (Claim 3) and asserts
  general applicability, but reports no error rate, no comparison against
  the structured-output baseline it replaces, and no discussion of what
  happens when the hallucinated label doesn't map cleanly to any real
  category. Confidence is graded `emerging` overall for this reason: the
  mechanism is clearly and concretely described, but its reliability at
  scale is asserted, not measured, in this source.
- **Contradiction check performed**: Searched the corpus for existing notes
  on hallucination, structured outputs, embeddings, classification, and
  taxonomy (see Cross-References). Found one framing tension (with
  `blog-thebatch-gpt55-hallucination-kimi-k26.md`) that was evaluated
  against MINER.md §4a's filing criteria and judged not to rise to a formal
  contradiction — the two sources address different mechanisms (bounded,
  always-resolved intermediate fabrication vs. unresolved, directly-trusted
  fabrication about task state), not opposing claims about the same
  mechanism. No contradiction issue filed.
