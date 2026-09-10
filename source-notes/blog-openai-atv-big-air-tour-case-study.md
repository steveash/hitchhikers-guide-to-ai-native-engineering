---
source_url: https://openai.com/index/atv-big-air-tour
source_type: blog-post
title: "ATV Big Air Tour turned 3 days of work into 3 hours with ChatGPT"
author: OpenAI
date_published: 2026-09-02
date_extracted: 2026-09-10
last_checked: 2026-09-10
status: current
confidence_overall: anecdotal
issue: "#3352"
---

# ATV Big Air Tour turned 3 days of work into 3 hours with ChatGPT

> OpenAI customer case study on a two-person small business (ATV Big Air
> Tour, a live motorsports touring show) using ChatGPT Work for three
> distinct recurring workflows: daily automated fact-checking of event
> listings across ~30 publications, multimodal photo-to-spreadsheet
> merchandise inventory and reordering, and a daily "answer engine
> optimization" (AEO) audit of the company website's AI-discoverability.
> All outcomes are self-reported by one of the two co-founders.

## Source Context

- **Type**: blog-post (OpenAI "Product" news vertical, `openai.com/index/`,
  a short customer-case-study page — four sections, each built around one
  workflow vignette plus a closing framing paragraph). Structurally the
  same short-case-study genre as
  `blog-openai-nvidia-chatgpt-work-case-study.md` and
  `blog-openai-ringcentral-case-study.md` (no product-feature
  walkthrough, no pricing/availability section, no security/governance
  section — pure customer narrative).
- **Author credibility**: House-authored OpenAI customer-marketing
  content, no named individual author on the OpenAI side. All claims are
  attributed to one named source: Larissa Guetter, co-founder of ATV Big
  Air Tour (her business partner and co-founder, Derek Guetter, is named
  and pictured but not quoted). This is first-party vendor marketing
  copy for a paid product tier (ChatGPT Work) — the customer was
  OpenAI-selected and OpenAI-published, with no independent verification
  of any time-savings or analytics figures. Standard vendor-case-study
  credibility caveats apply, compounded here by the fact that the sole
  source of every claim is a single individual with no second
  named perspective (unlike case studies with multiple named employees,
  e.g. NVIDIA's two-vignette piece).
- **Scope**: Covers three recurring ChatGPT Work workflows at a
  two-person small business — event-listing fact-checking/correction,
  merchandise inventory-and-reorder planning from photos, and daily AEO
  website auditing — plus one self-reported website-traffic metric. Does
  NOT cover: any ChatGPT Work product-feature detail (no mention of
  Scheduled Tasks, Connectors, Compliance API, or GPT‑5.6 by name, unlike
  the ChatGPT Work launch post), any detail on how the "scheduled
  briefing" or "daily automation" is technically configured (prompt
  text, connectors used, or trigger mechanism), pricing, or any failure
  mode / limitation encountered with the tool.

## Extracted Claims

### Claim 1: A two-person company can use ChatGPT Work to take on tasks that would otherwise require a larger team, according to the company's co-founder
- **Evidence**: Direct named quote, presented as the article's lead
  testimonial.
- **Confidence**: anecdotal (single self-reported characterization from
  the customer being profiled)
- **Quote**: "We’re a team of two, but using ChatGPT Work lets us compete with businesses that have much bigger budgets and teams. It helps us do the work of multiple team members."
- **Our assessment**: A generic "force multiplier" framing, same shape as
  Will Daney's "It feels like I have a team working for me" quote in
  `blog-openai-nvidia-chatgpt-work-case-study.md` Claim 9 and the broader
  testimonial pattern documented across the corpus's OpenAI
  customer-story genre. Its value here is context, not novelty: it is
  the first source in the corpus with this framing applied to a
  two-person, non-tech, live-events small business rather than an
  enterprise knowledge worker.

### Claim 2: A scheduled ChatGPT Work briefing now performs daily fact-checking of event listings across roughly 30 online publications, a task that previously consumed a full workday every week
- **Evidence**: Narrative description plus a direct named quote.
- **Confidence**: anecdotal (single self-reported time estimate, no
  measurement methodology given for either the "full workday" baseline
  or the automated version)
- **Quote**: "ChatGPT Work runs this report for me every morning. It finds all the inconsistencies all the way across the internet, so I can ensure all of this information is correct," said Larissa.
- **Our assessment**: This is a recurring, scheduled information-triage
  workflow — structurally the same shape as Rachita Jain's
  25–40-updates-to-5–8-signals workflow in
  `blog-openai-nvidia-chatgpt-work-case-study.md` Claims 5–6, but applied
  to outbound accuracy-monitoring (checking that *other people's*
  listings about the business are correct) rather than inbound
  industry-news triage. This is a distinct sub-pattern: an agent
  continuously monitoring third-party sources for errors about the
  monitoring party itself, then producing a daily report.

### Claim 3: The same ChatGPT Work workflow also drafts correction emails and suggests the correct publication contacts, cutting what the co-founder describes as a normally lengthy process down to minutes
- **Evidence**: Direct named quote.
- **Confidence**: anecdotal (self-reported, no baseline time given for
  "normally" beyond "a lengthy process")
- **Quote**: "Finding the right people and writing each email would normally be a lengthy process, but within minutes, I have the correction requests ready and sent to every publication that needs to update its website."
- **Our assessment**: Extends Claim 2 from pure detection (finding
  inconsistencies) into an action step (drafting outbound corrective
  communication addressed to specific named contacts) within the same
  workflow — a detect-then-act pipeline rather than a report-only
  monitoring tool. Combined with Claim 2, the article gives a concrete
  aggregate figure (Claim 4) for the whole pipeline.

### Claim 4: The full fact-checking-and-correction workflow reduced total weekly review time from around 8 hours to 1 hour
- **Evidence**: The article's own stated aggregate figure for the
  workflow described in Claims 2–3.
- **Confidence**: anecdotal (a specific, quantified before/after figure,
  but self-reported by the single profiled individual with no
  measurement methodology disclosed — same caveat pattern as every other
  hours-saved figure in the corpus's OpenAI customer-story genre, e.g.
  the ~16-hours/week NVIDIA figure in
  `blog-openai-nvidia-chatgpt-work-case-study.md` Claim 2)
- **Quote**: "The ChatGPT workflow reduces total review time from around 8 hours to 1 hour per week and helps ATV Big Air Tour maintain accurate event information, ensuring a painless customer experience and making the tour easier to find."
- **Our assessment**: An 8x reduction on a recurring weekly task,
  comparable in magnitude to the article's headline "3 days to 3 hours"
  merchandise claim (Claim 6) but for a different workflow. Treat as
  illustrative anecdote, not a benchmarkable multiplier — same standard
  caveat the corpus already applies to this genre.

### Claim 5: Uploading photos of merchandise to ChatGPT Work let the co-founder generate an organized inventory spreadsheet, a "visual inventory website," and reorder recommendations in under 15 minutes
- **Evidence**: Narrative description plus a direct named quote.
- **Confidence**: anecdotal (specific self-reported time figure for a
  single workflow run; no detail on how many items/photos were involved,
  what "visual inventory website" means technically, or how accurate the
  generated reorder recommendations were before human review)
- **Quote**: "I’m still in shock at how painless this process is now. I used to dread it before!"
- **Our assessment**: This is a multimodal (image-input) workflow —
  distinct from the text/document-centric workflows dominant elsewhere
  in the corpus's OpenAI customer-story set (spreadsheets, Jira tickets,
  CRM records, transcripts). No other source note in the corpus
  documents a "photograph physical inventory, get a structured
  spreadsheet + generated micro-site + reorder plan" workflow — novel to
  the corpus (see Cross-References → Novel).

### Claim 6: The end-to-end merchandise inventorying-and-reordering process — from photographing stock to sending the final order to the supplier — dropped from two to three full days to two to three hours
- **Evidence**: The article's own stated aggregate figure, reinforced by
  a direct named quote; this is also the headline claim referenced in
  the article's title.
- **Confidence**: anecdotal (specific quantified before/after range,
  self-reported by the single profiled individual, no measurement
  methodology disclosed; note the co-founder still personally "reviewed
  the recommendations, made adjustments, and sent the final order" —
  the workflow is not claimed to be fully autonomous)
- **Quote**: "Prior to ChatGPT Work, inventorying and reordering merchandise would take me two to three full days. Now it takes me two to three hours."
- **Our assessment**: This is the article's headline metric (referenced
  in the title as "3 days of work into 3 hours"). Structurally identical
  to the "weeks of analysis to hours" and "days or weeks now take
  minutes" testimonial shape already flagged as a recurring OpenAI
  narrative pattern in `blog-openai-chatgpt-work-ambitious-partner.md`
  Claim 6's assessment — this is another independent instance of the
  same shape, this time explicitly retaining a human-review step before
  the final action (sending the order), which is more transparent about
  human-in-the-loop involvement than some other testimonials in the
  genre that describe the before/after purely as time saved.

### Claim 7: The company runs a daily ChatGPT Work automation that audits whether the company website's content (event dates, locations, ticket details) is structured clearly enough for AI-powered search tools and assistants to understand and surface — framed by the co-founder as "answer engine optimization" (AEO) and as her doing the work of her own CMO
- **Evidence**: Narrative description plus two direct named quotes.
- **Confidence**: anecdotal (a specific, named recurring workflow; no
  detail on what the audit actually checks technically — schema markup,
  page structure, robots.txt/AI-crawler access, or something else — the
  article stays at the level of business framing, not implementation)
- **Quote**: "My goal is to be searchable from AI. The way that people are searching for information is changing, and as a small business, it’s very important for us to be on top of this so we can be seen on the same level as our larger competitors," said Larissa.
- **Our assessment**: Novel to the corpus — no existing source note
  documents a small business running a *recurring, agent-driven* AEO
  self-audit workflow (as opposed to a one-off SEO/AEO explainer or
  a vendor's product-level SEO tooling). This is a concrete example of
  an agent being pointed at the business's own outward-facing surface
  (its website) as the audit target, rather than at internal documents
  or third-party sources.

### Claim 8: One AEO audit run by the company found that ChatGPT could not retrieve about 90% of the website's FAQs, and the same ChatGPT Work automation recommended a fix in addition to surfacing the problem
- **Evidence**: Narrative description of a specific audit finding.
- **Confidence**: anecdotal (a single self-reported audit result with no
  detail on the audit's method, what "could not retrieve" means
  technically, or whether the recommended fix was implemented and
  re-verified)
- **Quote**: "One audit found that ChatGPT could not retrieve about 90% of the site’s FAQs. ChatGPT Work not only surfaced the issue, it recommended a solution."
- **Our assessment**: A concrete, specific finding (not just a vague
  "improved discoverability" claim) — 90% of FAQ content invisible to
  ChatGPT's retrieval is a notably large and specific failure rate for a
  small business to have surfaced on its own. Still single-source and
  unverified (no detail on what the fix was or whether the 90% figure
  changed after remediation), but more falsifiable than most testimonial
  claims in this genre because it names a specific, checkable technical
  symptom (FAQ non-retrievability) rather than a vague time-savings
  estimate.

### Claim 9: Website analytics showed OpenAI-search and AI-user-bot hits rising from 183 to 2,421 across two consecutive 30-day periods — a self-reported 1,223% month-over-month increase, after the co-founder filtered out training bots and other AI platforms
- **Evidence**: The article's own stated analytics figures.
- **Confidence**: anecdotal (a specific, large percentage figure from a
  single small business's own analytics, filtered by the business owner
  herself with an unspecified filtering methodology; no corroborating
  data, no absolute traffic-to-ticket-sales conversion figure, and a
  small base number — 183 to 2,421 hits — that makes the percentage
  figure sensitive to noise)
- **Quote**: "Website analytics showed OpenAI search and user-bot hits rising from 183 to 2,421 across consecutive 30-day periods, a 1,223% month-over-month increase. Larissa filtered the results to exclude training bots and other AI platforms."
- **Our assessment**: This is the article's one quantified outcome metric
  tied directly to the AEO workflow (Claims 7–8), rather than a
  time-savings figure. It is a small-sample traffic metric self-filtered
  by the business owner with no stated methodology for how "OpenAI
  search and user-bot hits" were identified or how "training bots and
  other AI platforms" were excluded — treat the specific percentage as
  illustrative only, not as a benchmarkable AEO-effectiveness figure.

## Concrete Artifacts

```
Source: OpenAI, "ATV Big Air Tour turned 3 days of work into 3 hours with
ChatGPT," https://openai.com/index/atv-big-air-tour (published Sep 2,
2026, per the openai-news RSS feed entry that surfaced this issue).

Business profile: ATV Big Air Tour — a live motorsports touring show
(75-foot ATV jumps), ~26 tour dates across the US, May-November season.
Two co-founders: Larissa Guetter and Derek Guetter (only Larissa is
quoted).

Section structure (4 sections, in order):
  1. (intro, unlabeled) — "team of two" framing quote
  2. Helping fans find accurate event information
     (daily fact-checking automation, ~30 publications)
  3. Using inventory photos to make a merchandise plan
     (photo -> spreadsheet -> reorder workflow)
  4. Becoming her own CMO, and growing with AEO
     (daily AEO audit automation + traffic metric)
  5. Turning days of work into minutes with ChatGPT Work (closing)

Workflow 1 — Event-listing fact-checking:
  - Input: ~30 online publications (event organizers, ticketing teams,
    local media, chambers of commerce)
  - Cadence: daily scheduled briefing ("every morning")
  - Output: inconsistency report + suggested contacts + drafted
    correction emails
  - Time: ~8 hours/week -> ~1 hour/week

Workflow 2 — Merchandise inventory & reorder:
  - Input: photos of physical merchandise, uploaded to ChatGPT Work
  - Output: organized inventory, spreadsheet, "visual inventory
    website," reorder recommendations (generated in <15 minutes)
  - Human step retained: review, adjust, send final order to supplier
  - Time: 2-3 days -> 2-3 hours (end to end)

Workflow 3 — AEO (answer-engine-optimization) audit:
  - Cadence: daily automation
  - Checks: whether event dates/locations/ticket details are clearly
    structured for AI search tools/assistants to parse
  - Finding cited: one audit found ~90% of site FAQs were not
    retrievable by ChatGPT; the automation also recommended a fix
  - Metric cited: OpenAI-search/user-bot hits, 183 -> 2,421 across two
    consecutive 30-day periods (self-filtered to exclude training bots
    and other AI platforms), reported as a 1,223% MoM increase

No ChatGPT Work product/feature names (Scheduled Tasks, Connectors,
Compliance API, GPT-5.6, Codex) appear anywhere in the article body.
Link at the end to a webinar featuring Larissa: "25 jobs small business
does with ChatGPT Work" (https://webinar.openai.com/25-jobs-small-business-does-with-chatgpt-work/)
— not fetched as part of this extraction (webinar page, not text
content; flagged here for a future Miner pass if it becomes relevant).
```

## Cross-References

- **Corroborates**:
  - `blog-openai-nvidia-chatgpt-work-case-study.md` and
    `blog-openai-chatgpt-work-ambitious-partner.md` — same OpenAI
    customer-testimonial genre and "days/weeks of manual work compressed
    via an agent" narrative shape (see that note's Claim 6 assessment,
    and `blog-openai-nvidia-chatgpt-work-case-study.md`'s Cross-References
    → Extends), now with a fourth-plus independent instance (Claim 6
    here: "2-3 days to 2-3 hours").
  - The "force multiplier" / "team of two competing with bigger teams"
    framing in Claim 1 matches the same rhetorical pattern as Will
    Daney's closing quote in
    `blog-openai-nvidia-chatgpt-work-case-study.md` Claim 9 ("It feels
    like I have a team working for me").
- **Contradicts**: None identified against existing source notes.
- **Extends**:
  - `blog-openai-nvidia-chatgpt-work-case-study.md` Claims 5–6 (Rachita
    Jain's recurring external-signal-triage workflow, 25-40 updates ->
    5-8 signals/week) — Claim 2 here is a structurally similar recurring
    scheduled-triage pattern, but pointed outward at third-party sources
    describing the business itself (accuracy monitoring) rather than at
    an industry-news feed (competitive intelligence). Useful as a second
    data point if the guide categorizes agent use cases by workflow
    shape (recurring triage pipeline vs. one-off task vs. GUI automation).
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 11 (Scheduled
    Tasks: "Check websites and dashboards each morning, summarize what
    changed, and send a report") — this article's Workflow 1 (daily
    fact-checking briefing) and Workflow 3 (daily AEO audit) are both
    concrete, named real-world instances of exactly the example use case
    that post describes generically, giving the corpus its first
    small-business, non-enterprise instance of this pattern.
- **Novel**:
  - The photo-to-inventory-spreadsheet-to-reorder workflow (Claim 5) —
    the first source in the corpus documenting a multimodal
    (image-upload) ChatGPT Work workflow; every other OpenAI
    customer-story workflow in the corpus is text/document-centric
    (CRM records, spreadsheets, transcripts, Jira tickets).
  - The recurring self-directed AEO (answer-engine-optimization) audit
    workflow (Claims 7-9) — the first source in the corpus documenting a
    business using an agent to recurrently audit and improve its *own*
    discoverability by other AI systems, including a specific, checkable
    technical finding (90% of FAQs not retrievable by ChatGPT) and a
    self-reported AI-referral-traffic metric. This is a distinct
    guide-relevant category from AI-as-worker (doing tasks) or
    AI-as-search-tool (finding information) — here the business treats
    AI retrieval-quality of its own content as a target to optimize for,
    analogous to SEO but for AI answer engines.
  - The first small-business (two-person, non-tech, live-events)
    customer profile in the corpus's OpenAI ChatGPT Work case-study set,
    which otherwise skews toward large enterprises (NVIDIA, Zapier,
    RingCentral, Virgin Atlantic, Notion, Asana, Samsung).

## Guide Impact

- **Chapter 01 (Agent Patterns / daily workflows)**: Add Claim 2
  (scheduled daily accuracy-monitoring briefing across ~30 external
  sources) and Claim 5 (photo-upload -> structured inventory + reorder
  plan) as two more named examples of recurring, scheduled agent
  workflows outside software engineering — Claim 5 specifically as the
  corpus's first multimodal (image-input) case, useful if the guide
  discusses agent input modalities beyond text/documents.
- **Chapter 05 (Team Adoption / small-team and solo-operator ROI)**: Add
  this whole case study as the corpus's first small-business (two-person)
  ChatGPT Work profile, contrasting with the enterprise-employee
  testimonials that dominate the existing corpus (NVIDIA, Zapier,
  RingCentral). Useful if the guide distinguishes "AI as a force
  multiplier for an individual inside a large org" from "AI as a
  near-complete substitute for hires a small business can't afford" —
  Claim 1's framing ("do the work of multiple team members") is explicit
  about the latter.
- **Chapter 03 or wherever the guide discusses AI-discoverability /
  content strategy (if it exists)**: Add Claims 7-9 as a concrete example
  of "answer engine optimization" (AEO) as a distinct, actionable
  practice — not just a buzzword — including the specific technical
  symptom (90% of FAQs unretrievable by ChatGPT) an agent surfaced on a
  real site. Flag the 1,223% traffic-increase figure (Claim 9) as
  illustrative only, given the small base numbers (183 -> 2,421) and
  undisclosed filtering methodology.
- No chapter should cite the 8-hours-to-1-hour, 2-3-days-to-2-3-hours, or
  1,223%-traffic-increase figures as independently verified productivity
  benchmarks — all are single-source, self-reported figures from the one
  business owner profiled, consistent with every other OpenAI
  customer-story figure already flagged this way in the corpus.

## Extraction Notes

- **Fetch method**: The live `openai.com/index/atv-big-air-tour` URL
  returned an HTTP 403 to both `WebFetch` and a direct `curl` with a
  browser user-agent (the same Cloudflare bot-challenge pattern already
  documented for `openai.com/index/` posts elsewhere in the corpus, e.g.
  `blog-openai-chatgpt-work-ambitious-partner.md` and
  `blog-openai-nvidia-chatgpt-work-case-study.md`). No Wayback Machine
  snapshot existed yet (`archive.org/wayback/available` returned an
  empty `archived_snapshots` object at extraction time — the article was
  published only 8 days before this extraction). Extraction instead used
  the `r.jina.ai` reader-proxy path against the live URL, which returned
  a clean, complete markdown rendering of the full article body in a
  single fetch.
- **Full article read**: The article is short (four sections plus a
  closing paragraph, roughly 550 words of body text) and was read in
  full via the single fetch above; the only outbound link found (a
  webinar registration page) was not followed, since it is a
  registration/marketing page rather than substantive text content — see
  note in Concrete Artifacts.
- No contradiction with any existing source note was found during
  cross-referencing (see Cross-References → Contradicts), so no
  contradiction issue was filed per MINER.md §4a.
- `confidence_overall` is set to `anecdotal` rather than `emerging`
  because every claim in this note traces back to a single named
  individual's self-reported account with no corroborating internal
  metric, third-party verification, or named second perspective — a
  step below case studies in the corpus that include multiple named
  employees or an internal OpenAI-reported adoption statistic alongside
  the customer anecdote.
