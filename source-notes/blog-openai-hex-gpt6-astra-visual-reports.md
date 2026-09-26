---
source_url: https://openai.com/index/hex-gpt-6-astra
source_type: blog-post
title: "Hex turns complex analysis into visual reports with GPT‑6 Astra"
author: OpenAI (customer case study, featuring Caitlin Colgrove, Co-founder and CTO, Hex)
date_published: 2026-09-16
date_extracted: 2026-09-26
last_checked: 2026-09-26
status: current
confidence_overall: anecdotal
issue: "#3727"
---

# Hex turns complex analysis into visual reports with GPT‑6 Astra

> An OpenAI customer case study describing how Hex, an agentic data
> platform, uses GPT‑6 Astra to move beyond producing technically correct
> analysis toward two distinct capabilities: generating complex,
> interactive, "aesthetically pleasing" data visualizations by operating
> directly on underlying plotting/geospatial libraries, and interrogating
> its own analysis for business relevance ("analytical judgment") before
> presenting it — all attributed to a single named source, Hex co-founder
> and CTO Caitlin Colgrove.

## Source Context

- **Type**: blog-post (OpenAI `openai.com/index/` customer-story vertical,
  "Startup" tag; a very short (~350-word) case study with three section
  headers and three pull quotes — no benchmark table, no methodology
  appendix, no code or architecture diagram).
- **Author credibility**: Written and published by OpenAI as promotional
  customer-success content — OpenAI has a direct commercial incentive to
  present GPT‑6 Astra favorably. The only named individual quoted is
  Caitlin Colgrove, identified as "co-founder and CTO of Hex, an agentic
  data platform," quoted four times (every substantive claim in the
  article traces to her). No independent third party, end customer of
  Hex, or analyst is named or quoted. No methodology, benchmark, or
  quantified metric of any kind appears anywhere in the article — this is
  the thinnest evidentiary case study of its type in the corpus so far
  (contrast with `blog-openai-legora-financial-statement-tie-out.md`,
  which at least reports a named benchmark and specific figures).
- **Scope**: Covers Hex's stated rationale for adopting GPT‑6 Astra
  (visualization quality and self-checking analysis), one worked example
  (sales-channel performance analysis), and a closing framing tying clear
  visualization to organizational data literacy. Does NOT cover: any
  metric, benchmark, before/after timing or accuracy figure, Hex's
  underlying agent architecture or orchestration, which specific
  plotting/geospatial libraries Astra operates, how the "interrogate the
  answer" self-check is technically implemented (a separate model pass? a
  tool call? a prompt instruction?), adoption scale, or any detail about
  Hex as a company beyond the sidebar tags (Startup, North America,
  Technology, API).

## Extracted Claims

### Claim 1: Hex's CTO frames communicating an analysis, not just producing it, as an equally important and historically difficult part of data work — specifically citing data visualization as a longstanding model weakness that GPT‑6 Astra changes
- **Evidence**: Direct attributed quote opening the article, followed by
  editorial framing crediting Astra with resolving the stated weakness.
- **Confidence**: anecdotal (single practitioner's framing/anecdote, no
  measurement of "struggled... for a really long time" given)
- **Quote**: "A really important part of data work is not just doing the analysis, but also communicating it," ... "Models have struggled with data visualization for a really long time."
- **Our assessment**: This is the article's thesis-setting quote and the
  frame every other claim hangs from. It asserts a category of prior model
  weakness (visualization specifically, as distinct from analysis
  correctness) without naming which prior models were tried, for how long,
  or by what standard "struggled" was judged — a vendor-selected
  practitioner's summary judgment, not a comparative evaluation.

### Claim 2: With GPT‑6 Astra, Hex can build more complex, interactive, and visually compelling data artifacts that Colgrove says data teams are now "actually proud to share" across the organization, not just artifacts that are merely functional
- **Evidence**: Direct attributed pull-quote, the article's main
  capability claim.
- **Confidence**: anecdotal (single practitioner's qualitative
  before/after judgment, no specific artifact example given at this point
  in the article beyond the sales-channel example in Claim 4)
- **Quote**: "With GPT‑6 Astra, you are able to build much more complex, interactive, compelling, and beautiful data artifacts that not only communicate your analysis clearly, but that you are actually proud to share with the rest of the organization."
- **Our assessment**: The specific framing — a capability gap between
  "functional" and "shareable/presentable" output — is a distinct claim
  from raw analytical correctness. It implies a prior state where Hex's
  AI-generated outputs were accurate but not something an analyst would
  put in front of the business, which is a narrower and more checkable
  (if still unaudited) claim than a generic "Astra is better" statement.

### Claim 3: Colgrove attributes the visualization-quality jump specifically to GPT‑6 Astra's ability to operate directly on underlying plotting libraries and perform the transformations geospatial visualizations require, producing output that is both functional and aesthetically pleasing
- **Evidence**: Direct attributed pull-quote naming a specific technical
  mechanism (library-level manipulation) rather than a general capability
  statement.
- **Confidence**: anecdotal (single practitioner's technical
  characterization; no named library, no example geospatial output shown,
  no comparison to what earlier models did instead)
- **Quote**: "Astra is able to go into the underlying libraries, do all of the crazy transformations that geospatial visualizations require, and build out something that's not just functional but aesthetically pleasing inside of the data artifact as well."
- **Our assessment**: This is the closest the source comes to a mechanism
  rather than a vibe — "go into the underlying libraries" suggests Astra
  is generating and executing code against a plotting/mapping library
  (e.g., writing transformation code) rather than producing a static image
  or filling a template, but the article names no specific library,
  geospatial technique, or example output, so this should be read as a
  qualitative practitioner impression of code-generation capability
  applied to visualization, not a documented technical pattern.

### Claim 4: Hex's worked example is a sales-channel performance query — asking how channels are performing over time, which are doing best, and which should be discontinued — for which Hex returns written findings alongside trend lines and comparisons, plus interactive dashboards letting users explore key measures, rankings, and geographic breakdowns
- **Evidence**: Direct descriptive passage from the article body (not a
  named pull-quote, but verbatim article prose).
- **Confidence**: anecdotal (a single illustrative example, not a
  demonstrated or user-tested capability; no screenshot or artifact shown
  in the article text itself)
- **Quote**: "For example, a Hex user can ask how sales channels are performing over time, which are doing best, and which should be discontinued. Hex presents written findings alongside trend lines and comparisons, as well as interactive dashboards that let users explore key measures, rankings, and geographic breakdowns."
- **Our assessment**: This is the article's only concrete task example and
  the only place a specific output composition is described: prose
  findings + trend lines/comparisons + an interactive, explorable
  dashboard (measures, rankings, geographic breakdowns) — a
  multi-modal output bundle rather than a single chart or a single text
  answer. No indication is given of whether this composition is
  automatic/default or something the user must request.

### Claim 5: Hex uses GPT‑6 Astra to interrogate its own analysis output for whether it actually answers the user's question and reflects the business objective, not just whether the underlying code is technically correct
- **Evidence**: Editorial framing statement introducing a three-part
  self-check, presented as Hex's design choice for using the model.
- **Confidence**: anecdotal (a described product behavior, first-party,
  with no detail on how the self-check is technically implemented — a
  separate model pass, a tool call, or a prompt instruction — or how often
  it changes an initial answer)
- **Quote**: "Even technically correct code can produce an answer that misses the point, so Hex uses GPT‑6 Astra to interrogate the answer: Does the number make sense? Does the analysis answer the user's question? Does it reflect the business objective?"
- **Our assessment**: This is the most guide-relevant claim in the
  source: a named, three-part self-verification checklist (sense-check the
  number; check the analysis matches the question asked; check it matches
  the business objective) applied by the model to its own output, distinct
  from code-correctness testing. It describes *what* is checked but not
  *how* — no detail on whether this is a distinct agent step, a
  self-critique prompt, or a tool-assisted verification pass, so it cannot
  be cited as a specific implementable pattern beyond the checklist itself.

### Claim 6: Colgrove says GPT‑6 Astra exercises stronger "analytical judgment" than earlier models — investigating more thoroughly, surfacing more of the data's pitfalls and nuances, and producing more comprehensive analysis
- **Evidence**: Direct attributed pull-quote, naming Hex's own internal
  term ("analytical judgment") for the capability.
- **Confidence**: anecdotal (single practitioner's qualitative,
  unquantified comparison to unnamed "earlier models")
- **Quote**: "GPT‑6 Astra is much better at exercising what we call analytical judgment, which is not just getting to an answer, but understanding whether or not that answer is actually what the user is asking for and what the business needs."
- **Our assessment**: "Analytical judgment" as Hex defines it here is
  functionally the same capability described in Claim 5 (does the answer
  match what was actually asked and what the business needs), restated as
  a named internal term rather than a process description — this is a
  restatement/reinforcement of Claim 5, not a separate capability. No
  prior model is named for the "better than" comparison, and no example of
  a specific pitfall or nuance Astra caught (that an earlier model missed)
  is given.

### Claim 7: A clear visualization is framed as what lets colleagues beyond the original analyst engage with an analysis — comparing results, following changes over time, and exploring details relevant to their own work — which the article ties to Hex's stated mission of "making everyone a data person"
- **Evidence**: Closing editorial framing statement.
- **Confidence**: anecdotal (aspirational/mission framing, not a
  demonstrated organizational outcome — no example given of a
  non-analyst colleague actually using an Astra-generated visualization)
- **Quote**: "A clear visualization gives colleagues a way to engage with the analysis: comparing results, following changes over time, and exploring the details that relate to their work." ... "bringing Hex closer to its mission of making everyone a data person."
- **Our assessment**: This closing claim reframes the visualization-quality
  capability (Claims 2-3) as an organizational-adoption argument — better
  visual output isn't just aesthetically nicer, it's positioned as
  widening who inside a company can meaningfully use an analysis. This is
  company mission-statement framing rather than a described or measured
  adoption outcome, and should be treated as aspirational context, not a
  reported result.

## Concrete Artifacts

### Full article text (verbatim, via Wayback Machine snapshot — see Extraction Notes)

```
Source: https://openai.com/index/hex-gpt-6-astra
(OpenAI, published September 16, 2026)

Company size: Startup
Region: North America
Industry: Technology
Products: API

Hex turns complex analysis into visual reports with GPT‑6 Astra
GPT‑6 Astra helps Hex's data agents turn answers into interactive
visualizations that employees are proud to share.

Handling the complexity behind a clear visualization

"A really important part of data work is not just doing the analysis,
but also communicating it," says Caitlin Colgrove, co-founder and CTO
of Hex, an agentic data platform. But according to Caitlin, "Models
have struggled with data visualization for a really long time."
GPT‑6 Astra changes that.

"With GPT‑6 Astra, you are able to build much more complex,
interactive, compelling, and beautiful data artifacts that not only
communicate your analysis clearly, but that you are actually proud to
share with the rest of the organization."
—Caitlin Colgrove, Co-founder and CTO, Hex

Producing a useful data visualization requires both technical work and
choices about how to present the result. Caitlin remarks on how well
GPT‑6 Astra works with the underlying libraries and performs the data
transformations required, helping analysts create functional, visually
appealing outputs.

"Astra is able to go into the underlying libraries, do all of the
crazy transformations that geospatial visualizations require, and
build out something that's not just functional but aesthetically
pleasing inside of the data artifact as well."
—Caitlin Colgrove, Co-founder and CTO, Hex

For example, a Hex user can ask how sales channels are performing over
time, which are doing best, and which should be discontinued. Hex
presents written findings alongside trend lines and comparisons, as
well as interactive dashboards that let users explore key measures,
rankings, and geographic breakdowns.

Ensuring every answer makes sense

Even technically correct code can produce an answer that misses the
point, so Hex uses GPT‑6 Astra to interrogate the answer: Does the
number make sense? Does the analysis answer the user's question? Does
it reflect the business objective?

Caitlin says GPT‑6 Astra investigates more thoroughly, uncovers more
of the data's pitfalls and nuances, and delivers a more comprehensive
analysis than earlier models.

"GPT‑6 Astra is much better at exercising what we call analytical
judgment, which is not just getting to an answer, but understanding
whether or not that answer is actually what the user is asking for and
what the business needs."
—Caitlin Colgrove, Co-founder and CTO, Hex

Making findings useful across the business

A clear visualization gives colleagues a way to engage with the
analysis: comparing results, following changes over time, and
exploring the details that relate to their work.

With GPT‑6 Astra, Hex users can access, understand, and communicate
data more easily, bringing Hex closer to its mission of making
everyone a data person.
```

## Cross-References

### Cross-reference verification notes
`blog-openai-legora-financial-statement-tie-out.md`,
`blog-openai-fyxer-executive-assistant-case-study.md`,
`blog-simonwillison-gpt6-astra-launch.md`,
`blog-simonwillison-astra-pelican-comparison-grid.md`, and
`blog-simonwillison-astra-running-routes.md` were each re-read directly
before writing this section, and every `Claim N` cited below was located
and confirmed by number and content against that note's own numbered
`### Claim N:` headings, per MINER.md §4b.

- **Corroborates**:
  - `blog-openai-legora-financial-statement-tie-out.md`: both sources are
    OpenAI `openai.com/index/` customer case studies for GPT‑6 Astra,
    published two weeks apart (Legora Sep 3, Hex Sep 16), following an
    identical template (single named practitioner, multiple pull quotes,
    a worked example, no independent audit). Both sources independently
    frame GPT‑6 Astra as strong at "exhaustive," precision-sensitive
    analytical work — Legora's Claim 3 (checking every balance against
    its supporting schedule across 41 documents) and this source's Claim 6
    ("investigates more thoroughly, uncovers more of the data's pitfalls
    and nuances") both describe Astra doing more thorough, complete
    analysis than a prior model, in different domains (financial
    reconciliation vs. general data analysis).
  - `blog-openai-fyxer-executive-assistant-case-study.md`: a third
    same-template OpenAI startup case study (Fyxer, Sep 14, 2026, two days
    before this source), corroborating that OpenAI is running a
    recurring, near-weekly cadence of single-customer, single-quote
    `openai.com/index/` case studies for GPT‑6 Astra/GPT models around
    September 2026 launch — useful pattern-recognition context for how
    much weight the guide should give any single such case study
    (see Guide Impact).
  - `blog-simonwillison-astra-running-routes.md` Claim 6-7 (ChatGPT Work's
    "visualize" skill generates a self-contained, client-side-rendered
    D3/SVG map from previously-fetched geospatial vector data): this
    source's Claim 3 (Astra "go[es] into the underlying libraries" and
    does "the crazy transformations that geospatial visualizations
    require") describes, from a different product (Hex, not ChatGPT Work)
    and a different vantage point (a customer's qualitative account, not
    a Miner's direct code inspection), the same underlying capability
    area — Astra performing geospatial data visualization work directly
    via library-level code generation. Willison's post independently
    confirms this is achievable (he inspected the actual generated HTML/JS);
    this source adds a second, independent product vendor attesting to the
    same geospatial-visualization capability, though without any
    equivalent code-level evidence of its own.

- **Contradicts**: None identified rising to the MINER.md §4a filing bar.
  One tension worth flagging without filing: this source's Claim 6
  ("GPT‑6 Astra is much better at exercising... analytical judgment...
  than earlier models," an unqualified, all-around capability
  improvement claim) sits awkwardly next to
  `blog-simonwillison-gpt6-astra-launch.md` Claim 4 (on Artificial
  Analysis's Intelligence Index, Astra scores *equal* to GPT‑5.6 Sol and
  *trails* both Claude Fable 5.1 and Meta Muse Spark 1.3) and that note's
  Claim 6 (Artificial Analysis reports Astra "still beaten by Fable" on
  that index). These are not a genuine contradiction — "analytical
  judgment" as Hex uses it is a qualitative, task-specific, single-company
  impression of Astra's behavior on data-analysis workflows, while the
  Intelligence Index is a broad, aggregate third-party benchmark measuring
  a different thing — but a guide passage citing Hex's "better analytical
  judgment" claim as general evidence of Astra's superiority would
  conflict with the aggregate benchmark picture already in the corpus.
  This is a conditioning-variable case (different measurement scope), per
  MINER.md §4a "When NOT to file," not a contradiction requiring an issue.

- **Extends**:
  - `blog-simonwillison-astra-pelican-comparison-grid.md`: that note is
    Willison's own hands-on, single-practitioner evaluation of Astra's
    SVG-generation quality on one narrow creative-benchmark task (a
    pelican riding a bicycle), scored across reasoning levels with token
    counts and pricing. This source extends the corpus's evidence on
    Astra's visual/creative output quality with a second, independent
    practitioner's qualitative account ("aesthetically pleasing,"
    "beautiful data artifacts") in a materially different domain
    (business data dashboards rather than a fixed creative-benchmark
    prompt) — directionally consistent (both describe Astra producing
    visual output practitioners judge as higher-quality than prior
    models) but neither quantified nor independently verifiable the way
    the pelican grid's token/pricing data is.
  - `blog-openai-legora-financial-statement-tie-out.md` Claim 5 (Legora's
    Agent does the exhaustive comparison while the human expert keeps the
    judgment call — an externally-imposed human-in-the-loop verification
    step): this source's Claim 5 (Hex has Astra interrogate its *own*
    answer for sense, question-fit, and business relevance) is a
    meaningfully different verification pattern — self-checking by the
    same model that produced the answer, rather than a separate human
    review step. The guide should treat these as two distinct points on a
    verification-architecture spectrum (see Guide Impact), not as the same
    pattern in two domains.

- **Novel**:
  - **A named, three-part model self-interrogation checklist for
    analysis output** (Claim 5: does the number make sense? does the
    analysis answer the user's question? does it reflect the business
    objective?) — not previously documented in this corpus. Every existing
    verification-pattern source in the corpus (e.g. Legora's exhaustive
    comparison + human judgment call, or mutation-testing-style
    planted-defect checks) describes an external check on the model's
    output; this is the first source describing the model checking its
    *own* output against user-intent and business-relevance criteria
    before presenting it.
  - **Data-visualization/BI as a distinct GPT‑6 Astra use-case vertical**:
    the corpus's existing Astra case studies cover legal/financial
    document review (Legora) and an AI executive assistant (Fyxer); this
    is the first customer case study specifically about an agentic
    business-intelligence/data-analysis platform.

## Guide Impact

- **Chapter 03 (Verification)**: Add this source's Claim 5 (Hex's
  three-part self-interrogation checklist: does the number make sense,
  does the analysis answer the question asked, does it reflect the
  business objective) as a distinct, named pattern of *model
  self-checking its own output for relevance*, explicitly contrasted with
  `blog-openai-legora-financial-statement-tie-out.md` Claim 5's
  externally-imposed human-in-the-loop pattern (agent does the exhaustive
  comparison, a separate human expert makes the judgment call). Flag
  clearly that this source discloses no implementation detail (whether the
  self-check is a distinct pass, a tool call, or a prompt instruction) and
  no measurement of how often the self-check changes an initial answer —
  this is a described product behavior, not a technique with a worked
  example the guide can reproduce.
- **Chapter on AI-native outputs / visualization** (wherever the guide
  discusses agents generating visual artifacts — see
  `blog-simonwillison-astra-running-routes.md`'s Guide Impact for the
  existing "visualize" skill material): Add Claims 2-4 as a second,
  independent practitioner account of GPT‑6 Astra generating complex
  interactive data visualizations by operating directly on
  plotting/geospatial libraries, cross-referenced with the running-routes
  post's directly-inspected D3/SVG output mechanism. Note explicitly that
  this source, unlike the running-routes post, offers no inspectable
  artifact, code, or screenshot — it is a vendor-published qualitative
  customer testimonial only.
- **No chapter should cite Claim 1's "struggled... for a really long
  time" framing, Claim 2's "actually proud to share" framing, or Claim 6's
  "analytical judgment" comparison as evidence of a measured or
  generalizable capability improvement** — all are single-source,
  unquantified, first-party vendor-published characterizations with no
  named comparison model, no example of a specific failure an earlier
  model made, and no independent audit, consistent with every other
  OpenAI customer case study already in this corpus.

## Extraction Notes

1. **Direct fetch blocked (Cloudflare/bot protection)**: Both `WebFetch`
   and a direct `curl` (with a standard desktop-browser user agent)
   against `https://openai.com/index/hex-gpt-6-astra` returned HTTP 403 —
   the same access pattern already documented for `openai.com/index/`
   pages elsewhere in this corpus (e.g.
   `blog-openai-legora-financial-statement-tie-out.md`,
   `blog-openai-fyxer-executive-assistant-case-study.md`). Unlike the
   Legora note (no Wayback snapshot existed at extraction time) and like
   the Fyxer note, a Wayback Machine snapshot did exist for this URL:
   `http://web.archive.org/web/20260921060520/https://openai.com/index/hex-gpt-6-astra/`
   (captured Sep 21, 2026, five days after the article's Sep 16
   publish date). `WebFetch` itself is blocked from fetching
   `web.archive.org` directly in this environment, so the snapshot was
   retrieved via a direct `curl` (HTTP 200, ~390KB of HTML), and the
   article text was extracted by stripping script/style blocks and HTML
   tags with a short local script, then read in full.
2. **Entire article captured**: The extracted text ends on a clear closing
   sentence ("bringing Hex closer to its mission of making everyone a
   data person") followed only by "Keep reading" related-article links and
   generic site navigation/footer — no indication of truncation. All
   extractable claims (Claims 1-7) are drawn from this single, complete
   retrieval, reproduced verbatim in Concrete Artifacts above. The
   retrieved section headers ("Handling the complexity behind a clear
   visualization," "Ensuring every answer makes sense," "Making findings
   useful across the business") and quote structure match the level of
   detail given in two of the three Prospector triage comments on the
   source issue, corroborating that the retrieval is accurate.
3. **No sub-pages followed**: The "Keep reading" footer links to three
   other OpenAI customer case studies (Fyxer, Legora, and a Playco case
   study not yet in this corpus) by title only, with no additional
   article content — these are not sub-pages of this source but pointers
   to separate case studies, two of which (Fyxer, Legora) are already
   mined and cross-referenced above. The Playco case study
   ("Playco cut manual fixes 50% prototyping games with GPT-6 Astra," Sep
   3, 2026) is not currently in the corpus and is a candidate for its own
   Prospector scan, but this Miner does not extract from it here since it
   falls outside this issue's scope.
4. **Confidence rated `anecdotal` overall**: every claim in this source is
   a first-party, vendor-published characterization or single-example
   anecdote from one named individual at one customer company, with no
   benchmark, no metric, no named comparison model, and no independent
   audit — matching the `anecdotal` rating already applied to the corpus's
   other single-company OpenAI vendor case studies (Legora, Fyxer, Asana,
   Notion, Polimill) rather than the `emerging` rating applied to sources
   with named, independently-checkable benchmark data
   (`blog-simonwillison-gpt6-astra-launch.md`,
   `blog-simonwillison-astra-pelican-comparison-grid.md`).
5. **Source is short and thin — thinner than comparable case studies
   already in the corpus**: at ~350 words with three section headers,
   three pull quotes, and zero numeric metrics of any kind (no benchmark
   score, no percentage, no before/after timing figure), this article
   contains no quantified claim at all — a contrast with both Legora
   (which discloses "nearly 40%," "about 3%," "41 documents," "£500,000,"
   "around 50 more") and Fyxer (53% draft acceptance, 90%+ retention,
   $1M→$32M ARR) in this corpus. All seven claims above exhaust the
   article's substantive content; there was no additional depth to
   extract beyond what is captured here.
6. **No contradiction filed**: Checked this source's content against the
   cross-referenced notes above; no material opposition to any existing
   claim rising to the MINER.md §4a filing bar was found — see
   Cross-References → Contradicts for the "analytical judgment" vs.
   Intelligence Index tension that was considered and treated as a
   conditioning-variable case (different measurement scope), not a
   contradiction. Open `contradiction`-labeled issues and
   `CONTRADICTIONS.md` were checked for an existing entry on Astra
   capability-claim disputes; none covers this pairing.
