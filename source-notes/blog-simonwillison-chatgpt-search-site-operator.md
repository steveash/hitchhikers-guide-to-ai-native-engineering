---
source_url: https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/
source_type: blog-post
title: "ChatGPT search now uses the site:operator at scale"
author: Simon Willison
date_published: 2026-08-20
date_extracted: 2026-08-28
last_checked: 2026-08-28
status: current
confidence_overall: emerging
issue: "#3016"
---

# ChatGPT Search Now Uses the site:operator at Scale

> A short Willison link-blog post relaying third-party telemetry from GEO
> ("Generative Engine Optimization") vendor Promptwatch: ChatGPT Search's use
> of the `site:` operator jumped roughly 46x overnight on August 8, 2026,
> coinciding with a vague OpenAI announcement about GPT-5.6 Sol, while
> Reddit's share of ChatGPT citations collapsed days later — behavioral
> evidence of an opaque, unannounced system-prompt or tool-schema change that
> practitioners can only infer from the outside.

## Source Context

- **Type**: blog-post (Willison "note" format — a short link-blog post
  built around quoting and annotating a third-party vendor's data page,
  rather than Willison's own experiment or benchmark. The post itself is
  five short paragraphs plus two blockquotes.)
- **Author credibility**: Simon Willison is a heavily-cited, high-signal
  independent commentator on practical LLM tooling already present
  throughout this corpus (see e.g. `blog-simonwillison-opus47-system-prompt.md`,
  `blog-simonwillison-llm032.md`). For this specific post, Willison is not
  the primary data source — he is relaying and lightly interpreting data
  published by Promptwatch, a GEO analytics vendor whose own claimed
  methodology is "over 26 billion data points" collected from "the actual
  user interfaces of major AI platforms." Willison explicitly flags the
  limits of his own knowledge here ("I am hampered by OpenAI's decision to
  actively obscure their system prompts") and frames his `search(query,
  recency, domains)` tool-shape claim as an inference from "poking at
  ChatGPT," not a confirmed fact.
- **Scope**: Covers two linked but distinct observations — (1) a sudden
  spike in ChatGPT Search's use of the `site:` operator on August 8, 2026,
  and (2) a subsequent sharp drop in Reddit's share of ChatGPT Search
  citations starting August 14, 2026, with a slower, more gradual decline
  in Reddit's share of Google's AI Overviews and AI Mode citations over the
  same general window for comparison. It does NOT cover the underlying
  mechanism (OpenAI has not disclosed a system-prompt or tool-schema
  change), does NOT cover other chat products' search behavior in detail
  (Claude and Gemini are named as also tracked by Promptwatch but no data
  for them is quoted), and does NOT independently verify Promptwatch's
  raw data collection methodology.

## Extracted Claims

### Claim 1: GEO ("Generative Engine Optimization") is an emerging practice area — the chatbot-search equivalent of SEO
- **Evidence**: Author's own framing, describing Promptwatch as part of this space.
- **Confidence**: emerging
- **Quote**: "Promptwatch is part of the emerging \"GEO\" space, for Generative Engine Optimization - the chatbot version of SEO, where companies offer tools and consulting to help your site increase its presence in replies to prompts inside tools like ChatGPT."
- **Our assessment**: This is a naming/framing claim rather than a data claim, but it is useful corpus context: it establishes that a vendor market already exists around influencing LLM-search citation behavior, analogous to traditional SEO. Worth treating as directional color rather than a settled taxonomy — the term "GEO" is Promptwatch's positioning, relayed uncritically by Willison.

### Claim 2: Promptwatch tracks chatbot search/citation behavior via automation across ChatGPT, Claude, and Gemini, and publishes aggregate reports as content marketing that nonetheless appear to give credible signal about otherwise-invisible product changes
- **Evidence**: Willison's own assessment of the vendor's output, not an endorsement of their raw methodology.
- **Confidence**: emerging
- **Quote**: "The Promptwatch product uses automation to track responses to prompts across end-user chat products like ChatGPT, Claude, and Gemini. They publish aggregate reports on this as part of their own content marketing strategy, which do seem to provide credible hints as to otherwise invisible design changes to those products."
- **Our assessment**: Willison is explicit that this is a vendor with a commercial incentive to publish attention-grabbing data (content marketing), while also judging the specific data credible. This is a second-hand, single-source credibility judgment — useful as a data point but not independent confirmation. Practitioners should treat Promptwatch's numbers as suggestive telemetry, not verified ground truth.

### Claim 3: The share of ChatGPT Search "fanout" queries containing the `site:` operator held steady around 0.3-0.5% for weeks, dipped to 0.15% August 3-5, then jumped to 16-17% on August 8, 2026
- **Evidence**: Quoted directly from Promptwatch's data page, as relayed by Willison; corroborated with more precise figures on the Promptwatch page itself (see Claim 4).
- **Confidence**: emerging
- **Quote**: "The percentage of all ChatGPT Search fanout queries that contain the site:operator, per day. The share hovered between 0.3% and 0.5% for weeks, dipped briefly to 0.15% on August 3 to 5 (consistent with a staged rollout or pre-launch experiment), then jumped to 16-17% on August 8."
- **Our assessment**: The brief dip immediately before the jump is a specific enough pattern (not just a step change) to be a plausible staged-rollout signature, as Willison/Promptwatch note. This is the single strongest piece of quantitative evidence in the post; it is telemetry from one vendor's tracking panel, not an OpenAI-disclosed figure, so the precision (down to fractions of a percent) should be read as "this vendor's sample showed," not as OpenAI's own reported metric.

### Claim 4: Promptwatch's own data page states the site:operator jump was from 0.37% to 16.8% of fanout queries — roughly a 46x increase within a single day — and that average searches per ChatGPT response nearly doubled at the same time
- **Evidence**: Direct text from the linked Promptwatch data page (promptwatch.com/data/chatgpt-site-operator-fanouts), followed as a substantive linked source per MINER.md §1.
- **Confidence**: emerging
- **Quote**: "On August 8, 2026, ChatGPT Search changed how it searches the web overnight. Fanout queries using the site:operator (searches scoped to a specific domain) jumped from 0.37% to 16.8% of all fanout queries, a roughly 46x increase in share within a single day."
- **Our assessment**: This is the precise version of Claim 3's rounded "0.3-0.5% → 16-17%" range quoted in Willison's post — both describe the same underlying dataset. The companion figure (average fanout searches per response, 1.08 → 1.83) is new information not mentioned in Willison's post at all; it suggests the change is not just "more `site:`-scoped queries" but "more searches overall per answer," which is a broader behavioral shift than the operator-usage number alone implies.

### Claim 5: The site:operator shift correlates with an OpenAI announcement on August 6, 2026 about "updating GPT-5.6 Sol in Chat to be more reliable with facts and provide more focused answers" — vague wording that does not disclose a search-tool change
- **Evidence**: Quoted OpenAI announcement text, relayed via Willison's post; Willison explicitly characterizes the announcement as "somewhat vague."
- **Confidence**: emerging
- **Quote**: "For Plus and Pro users, we're updating GPT‑5.6 Sol in Chat to be more reliable with facts and provide more focused answers."
- **Our assessment**: The two-day gap between this announcement (Aug 6) and the observed behavior jump (Aug 8) is consistent with a staged rollout, but OpenAI's own language gives no indication that search/citation behavior specifically was the mechanism — "more reliable with facts" could describe many implementation choices. The correlation is plausible but not confirmed causation; this is exactly the kind of opaque-behind-the-scenes-change problem the post is about.

### Claim 6: Willison infers, from his own probing of ChatGPT rather than any disclosed documentation, that the underlying search tool likely has a shape like `search(query, recency, domains)` rather than one that encourages a literal `site:` operator in the query string
- **Evidence**: Author's own investigation ("from poking at ChatGPT"), explicitly caveated as inference rather than confirmed fact, attributed to OpenAI's practice of not publishing system prompts/tool schemas.
- **Confidence**: anecdotal
- **Quote**: "Once again I am hampered by OpenAI's decision to actively obscure their system prompts, but from poking at ChatGPT I believe their latest search tool has a shape like `search(query, recency, domains)` rather than encouraging a `site:` operator directly."
- **Our assessment**: This is the most speculative claim in the post — a single practitioner's best guess at an internal tool signature based on black-box interaction, not a leaked schema or documented API. It should be treated as a hypothesis worth testing, not a fact. It does, however, illustrate a repeatable practitioner technique: inferring tool/parameter shape by observing model output patterns when direct documentation is withheld.

### Claim 7: Reddit's share of ChatGPT Search citations held steady near 3.8% from mid-July through early August 2026, then collapsed to under 1% starting August 14, 2026
- **Evidence**: Promptwatch follow-up report (Aug 18), linked and summarized by Willison; direct figures pulled from the Promptwatch page itself as a followed substantive link.
- **Confidence**: emerging
- **Quote**: "Reddit held a steady 3.8% share of ChatGPT Search citations from July 18 through August 7, 2026. On August 14 that share collapsed to under 1%, and it has stayed there: the August 14-17 average is 0.5%, a 86% drop."
- **Our assessment**: Notably, this is a second, separate step-change six days after the `site:` operator jump (Aug 8), not the same event — Promptwatch's own page states "The slide started earlier: on August 8 ... Reddit's share fell from the high 3s to the mid 2s," then collapsed further on Aug 14. That two-stage pattern (partial decline Aug 8, near-total collapse Aug 14) suggests at least two separate changes to ChatGPT's search/citation behavior within a single week, not one single rollout.

### Claim 8: Willison attempted to verify whether ChatGPT's system prompt was updated to discourage Reddit sourcing, but could not confirm this via the most thorough public leaked-system-prompt archive he knows of
- **Evidence**: Author's own attempted verification, explicitly described as unsuccessful, against a named external resource (a GitHub repo of leaked system prompts).
- **Confidence**: anecdotal
- **Quote**: "My own attempts to ascertain if the system prompt has been updated to discourage Reddit sourcing have been unsuccessful - the most thorough leaked system prompt collection I know of doesn't yet show any relevant changes."
- **Our assessment**: This is an honest negative result, not a confirmed absence of change — a leaked-prompt archive can lag behind an actual change, or the mechanism could be a retrieval/ranking change rather than a system-prompt instruction at all (which a prompt leak would never surface regardless of freshness). Practitioners should not read "the leaked prompts don't show it" as evidence the underlying mechanism isn't a prompt change — it is only evidence that this particular archive hasn't captured one yet.

### Claim 9: Reddit's citation share in Google's AI Overviews and AI Mode declined much more gradually over a comparable window than its collapse in ChatGPT Search
- **Evidence**: Promptwatch page data (from the Reddit-citations follow-up page), giving percentage-point figures for two Google surfaces.
- **Confidence**: emerging
- **Quote**: "Reddit averaged 2.37% of AI Overview citations during the first seven days and 2.10% during the final seven. That is a 11.3% relative decline over the period." / "Reddit averaged 2.22% of AI Mode citations during the first seven days and 1.54% during the final seven, a 30.5% relative decline."
- **Our assessment**: This is not quoted or referenced in Willison's own post text at all — it's additional context found only by following the Promptwatch link per MINER.md §1. It's a useful contrast: ChatGPT's Reddit-citation drop is abrupt (single-day collapse, 86% relative decline) while Google's two AI surfaces show smaller, gradual declines (11-31% relative) over a similar window. This supports reading the ChatGPT change as a discrete rollout event rather than a shared industry-wide drift away from Reddit as a source.

## Concrete Artifacts

### Promptwatch's recommendations for site operators (from the site:operator data page, promptwatch.com/data/chatgpt-site-operator-fanouts)
```
- Treat your domain as retrieval surface
- Ensure crawlability and indexing
- Monitor for behavior shifts before rewriting strategy
```

### Fanout-queries-per-response data (Promptwatch, same page)
```
"ChatGPT Search held steady at about 1.08 fanout queries per response for
weeks, then jumped to about 1.83 on August 8 and has stayed there."
```

### Promptwatch stated methodology (appears on both linked data pages)
```
"We collect millions of prompt responses, citations, and click data from
the actual user interfaces of major AI platforms: over 26 billion data
points and growing."
```

### Full timeline reconstructed from the post + both linked Promptwatch pages
```
Jul 18 - Aug 7, 2026:  site:operator share steady ~0.3-0.5%;
                       Reddit citation share steady ~3.8% (ChatGPT Search)
Aug 3-5, 2026:         site:operator share dips to 0.15% (staged-rollout signature)
Aug 6, 2026:           OpenAI announces "updating GPT-5.6 Sol in Chat to be
                       more reliable with facts and provide more focused answers"
Aug 8, 2026:           site:operator share jumps to 16-17% (0.37% -> 16.8%,
                       ~46x) overnight; fanout searches/response nearly double
                       (1.08 -> 1.83); Reddit citation share also begins
                       falling ("high 3s to mid 2s")
Aug 14, 2026:          Reddit citation share collapses further to under 1%
                       in ChatGPT Search
Aug 14-17, 2026:       Reddit citation share averages 0.5% (86% relative drop
                       from the Jul 18-Aug 7 baseline)
Aug 18, 2026:          Promptwatch publishes Reddit-citation follow-up report
Aug 20, 2026:          Willison's post (this source) published
```

## Cross-References

- **Corroborates**: None found. No existing source note in this corpus
  covers GEO, Promptwatch, ChatGPT Search's citation/query behavior, or
  the `site:` operator topic (verified via `grep -ril` across
  `source-notes/` for "GEO", "generative engine optimization",
  "site:operator", "promptwatch" — no matches prior to this note).

- **Contradicts**: None identified.

- **Extends**: `blog-simonwillison-opus47-system-prompt.md` (Willison
  diffing Anthropic's published system-prompt archive to detect behavioral
  changes between Claude Opus 4.6 and 4.7) shares the same underlying
  practitioner pattern this post exhibits — inferring an opaque vendor's
  internal instruction changes from external observation — but uses a
  fundamentally different method. That note's technique works because
  Anthropic *publishes* its chat system prompts, letting Willison diff
  exact text; this post's technique is forced to rely on third-party
  behavioral telemetry (Promptwatch) and his own black-box probing
  precisely because, per Claim 6/Claim 8 above, OpenAI does not publish
  its system prompts or tool schemas and the community leaked-prompt
  archive he checked hadn't caught the change. Worth citing together as
  two ends of the same "reverse-engineering opaque LLM product behavior"
  spectrum: disclosed-artifact diffing (Anthropic) vs. inferred-from-
  telemetry probing (OpenAI).

- **Novel**: This is the first source note in the corpus to name GEO
  (Generative Engine Optimization) as a vendor category, the first to cite
  Promptwatch as a data source, and the first to document a concrete,
  dated, quantified behavioral change in a deployed chat product's search
  tool usage (the Aug 8, 2026 `site:` operator spike) plus a related
  citation-source shift (the Reddit citation collapse) inferred entirely
  from external telemetry rather than vendor disclosure.

## Guide Impact

- **Chapter 05 (Observability — understanding opaque model/product
  behavior)**: Add this as a citable example of a repeatable practitioner
  technique: when a vendor won't disclose a system-prompt or tool-schema
  change, third-party behavioral telemetry (query-pattern tracking,
  citation-share tracking) can surface the *fact* of a change and roughly
  *when* it happened, even without confirming the *mechanism*. Explicitly
  flag the limits demonstrated here: Willison's own tool-shape guess
  (Claim 6) and his inability to confirm a system-prompt cause via a
  leaked-prompt archive (Claim 8) — the technique detects change, it does
  not reliably explain it.
- **Chapter 02/03 (content and tooling strategy under LLM-mediated
  search)**: If the guide discusses building content or tools that need to
  be discoverable by AI systems, this source is a citable, dated data
  point that chat-product search behavior can change abruptly (46x shift
  in a day) and that a small vendor market (GEO, exemplified by
  Promptwatch) already exists to track and advise on this. Recommend
  Promptwatch's own guidance ("treat your domain as retrieval surface,"
  "ensure crawlability and indexing," "monitor for behavior shifts before
  rewriting strategy") be presented as vendor-sourced and unverified
  rather than settled practice.
- **Chapter 01 (fundamentals) / Chapter 05**: If the guide discusses
  citation/sourcing behavior of chat products (e.g., which domains get
  cited, how that affects trust in AI-generated answers), the Reddit
  citation collapse (Claim 7, Claim 9) is a concrete, comparative example:
  the same source-type's citation share can move abruptly on one platform
  (ChatGPT: 86% relative drop in days) while shifting only gradually on
  another (Google AI Overviews/AI Mode: 11-31% relative decline over a
  similar window) — evidence that citation behavior is platform-specific
  and not simply tracking Reddit's own actual content quality or
  popularity.

## Extraction Notes

- Fetched three sources: the Willison blog post itself (full text and all
  hyperlinks extracted), and both linked Promptwatch data pages
  (`/data/chatgpt-site-operator-fanouts` and
  `/data/reddit-citations-are-dropping-in-chatgpt`), followed as
  substantive linked pages per MINER.md §1. Did not follow the OpenAI
  announcement page (its relevant sentence is already quoted verbatim
  inside Willison's post, Claim 5) or the GitHub leaked-system-prompts
  repository (Claim 8 only needs Willison's negative-result statement
  about it, not the repo contents itself).
- The Willison post itself is short (five paragraphs); roughly half of
  this note's quantitative claims (Claim 4, the fanout-searches-per-
  response figure, all of Claim 9, and the Promptwatch recommendations in
  Concrete Artifacts) come from the two linked Promptwatch pages rather
  than the blog post text itself. Reading past the post into both linked
  data pages was necessary to avoid a shallow extraction, consistent with
  the pattern documented in `blog-simonwillison-llm-gemini-033.md`'s
  Extraction Notes (reading past a thin "beat"-format post into its linked
  substantive source).
- No contradiction requiring MINER.md §4a filing was found — the
  differing decline shapes between ChatGPT and Google's AI surfaces
  (Claim 9) are a genuine platform-conditioning difference reported by the
  same source (Promptwatch), not two sources disagreeing about the same
  fact, so no contradiction issue was filed.
- Considered filenames matching corpus convention
  (`blog-simonwillison-<topic>.md`); confirmed no existing file uses this
  slug via `ls source-notes/ | grep -i simonwillison`.
- Cross-reference verification performed: `blog-simonwillison-opus47-system-prompt.md`
  frontmatter and Claims 1-2 (its diff-based system-prompt-change
  methodology) confirmed by direct read before citing in Cross-References
  above. Corpus-wide `grep -ril` for "GEO", "generative engine
  optimization", "site:operator", and "promptwatch" across `source-notes/`
  returned no matches prior to this note, confirming the "Corroborates:
  None found" and "Novel" claims above.
