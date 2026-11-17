---
source_url: https://simonwillison.net/2026/Nov/15/datasette/
source_type: blog-post
title: "datasette 1.0a43"
author: Simon Willison
date_published: 2026-11-15
date_extracted: 2026-11-17
last_checked: 2026-11-17
status: current
confidence_overall: anecdotal
issue: "#4765"
---

# datasette 1.0a43

> A release "beat" whose one AI-relevant sentence says the maintainer is "leaning hard into Claude Fable 5.2" to work through the Datasette 1.0 milestone (53% complete); the linked GitHub advisory documents a private-stored-query exposure bug found by an internal permissions audit.

## Source Context

- **Type**: blog-post (annotated release note / "beat"). Also read: the GitHub advisory GHSA-mw6v-83vp-7c4c (fetched via `gh api`) and the Datasette changelog page (the 1.0a43 section only lists headings in the text extraction; the advisory supplied the security detail).
- **Author credibility**: Simon Willison is the creator and maintainer of Datasette; first-party statement about his own workflow.
- **Scope**: Covers release contents (streaming output renderers, security fixes, UI work, CSS view transitions). Does NOT describe how the model is used, which tasks are delegated, review process, or any metrics. The AI-usage evidence is a single sentence.

## Extracted Claims

### Claim 1: The maintainer is using a frontier model (Claude Fable 5.2) heavily to burn down the Datasette 1.0 milestone
- **Evidence**: First-party one-sentence statement; milestone progress figure (53%) given, but no before/after rate, task breakdown, or review process.
- **Confidence**: anecdotal
- **Quote**: "I've been leaning hard into Claude Fable 5.2 to help knock things off the 1.0 milestone"
- **Our assessment**: A credible datapoint that a mature OSS maintainer uses a frontier model against a defined milestone (a bounded, issue-tracked backlog) rather than ad-hoc. The 53% figure is not tied to AI contribution, so it cannot be read as a productivity result. Earlier series notes show multi-model usage (see Cross-References), so "Fable 5.2" here is one tool among several.

### Claim 2: A security bug (private stored queries exposed) was serious enough for a GitHub advisory, even though it exposes text rather than execution
- **Evidence**: Post text plus the advisory: the `?owner_id=` filter on query list pages caused the "private queries are only visible to their owner" rule to be evaluated as if the request came from the named actor, so unauthenticated clients could list another actor's private queries (name, title, description, SQL) given a known or guessed actor ID.
- **Confidence**: settled (first-party disclosure)
- **Quote**: "private stored queries could be exposed, granting access to the title and SQL of the query (but not allowing that query to be executed)"
- **Our assessment**: Same bug class as earlier notes: an authorization rule whose actor/subject was confused by a request parameter. Impact is bounded (advisory: it "does not by itself let them run SQL or read tables that they do not already have permission to access") but SQL text can leak schema and literals.

### Claim 3: The bug was introduced with a feature (stored queries, 1.0a31) and found by an internal permissions audit
- **Evidence**: Advisory text: introduced in 1.0a31 when stored queries shipped; fixed in 1.0a43 by giving the owner filter its own SQL parameter so it no longer changes which actor the privacy rule is evaluated against. Stable 0.65.x is not affected. Credit line states discovery source.
- **Confidence**: settled (advisory), though the advisory does not say whether the audit used coding agents.
- **Quote**: "Found during an internal audit of Datasette's permissions system." (advisory GHSA-mw6v-83vp-7c4c, Credit section)
- **Our assessment**: Consistent with the audit practice described in the 1.0a39 note, but the advisory does not say agents performed this one; do not over-attribute. Notable lifecycle: new feature -> vulnerable for roughly five months (1.0a31 on 2026-05-28 to 1.0a43 on 2026-11-15, per the changelog index) -> found by audit.

### Claim 4: The fix pattern is to separate the filter parameter from the identity used for authorization
- **Evidence**: Advisory "Patches" section; mitigation for those unable to upgrade is to reject `owner_id` query strings at the proxy.
- **Confidence**: settled
- **Quote**: "The owner filter now uses its own SQL parameter and no longer changes which actor the privacy rule is evaluated against."
- **Our assessment**: A transferable review checklist item for agent-written code: user-supplied filter parameters must never feed the principal used in permission evaluation.

### Claim 5: Streaming support for output renderers is the biggest 1.0 item in the release
- **Evidence**: Post describes `Response.stream()`; built-in CSV/TSV export now uses it.
- **Confidence**: settled (release fact)
- **Quote**: "plugins can register themselves as capable of streaming every row in a table in one go via the new Response.stream() method"
- **Our assessment**: Product detail; no AI-engineering pattern stated. Triage said to treat as supporting only.

## Concrete Artifacts

```
Advisory GHSA-mw6v-83vp-7c4c (affected request shapes, verbatim):
/-/queries.json?owner_id=alice
/<database>/-/queries.json?owner_id=alice
```

```
Advisory workaround (verbatim): "configure the proxy in front of Datasette to reject requests to `/-/queries` and `/<database>/-/queries` (with or without `.json`) that include an `owner_id` query string parameter."
```

The CSS view-transition snippet in the post was deliberately not extracted (product detail per triage).

## Cross-References

- **Corroborates**: `blog-simonwillison-datasette-1-0a39.md` Claim 3 (first dedicated coding-agent security audit) and Claim 13 (audit as an ongoing practice): this advisory's "internal audit of Datasette's permissions system" credit is consistent with continued auditing, though agent involvement is not stated here. `blog-simonwillison-datasette-1-0a39.md` Claim 7 (permission-check gaps reachable through query parameters) is the same bug class.
- **Contradicts**: none.
- **Extends**: `blog-simonwillison-datasette-1-0a33.md` Claim 4 (Claude Fable 5 used for planning in a cross-model split): this adds a later first-party statement of heavy Fable 5.2 use on the milestone. `blog-simonwillison-datasette-0-65-5.md` Claim 9 (a bug survived the internal multi-model audit): another permission-check bug in the same series. Earlier 1.0a39/1.0a41 notes say nothing about AI-assisted development in the release posts themselves.
- **Novel**: The explicit milestone-driven AI usage statement in a release beat, and the owner_id actor-confusion bug class with its advisory.

## Guide Impact

- **Chapter 01**: Optional single-sentence datapoint (anecdotal) that a maintainer targets a model at an issue-tracker milestone; do not cite it for productivity claims.
- **Chapter 06**: The advisory's root cause (request filter parameter overriding the principal in an authorization check) could be an example in a review checklist for agent-generated access-control code, alongside the 0.65.5 note. Low priority.
- No change recommended for Ch05; the source contains no team-adoption content.

## Extraction Notes

- The blog post is short and was read in full (fetched raw HTML). The advisory was read in full; the changelog 1.0a43 body text did not render in extraction, so changelog details were not used.
- No contradiction found, so no contradiction issue filed.
- Evidence for the AI-usage claim is one sentence; confidence kept at anecdotal.
