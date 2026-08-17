---
source_url: https://simonwillison.net/2026/Aug/7/pdfs-are-terrible/
source_type: blog-post
title: "The Tokenpocalypse Is Here: Companies Are Scrambling To Stop Spending So Much on AI"
author: Simon Willison (link-blog commentary), quoting/linking 404 Media (Joseph Cox, reporting)
date_published: 2026-08-07
date_extracted: 2026-08-17
last_checked: 2026-08-17
status: current
confidence_overall: emerging
issue: "#2743"
---

# Simon Willison on Accenture's Leaked "PDFs Are a Token Chewer" Audio

> Simon Willison's link-blog post reproduces leaked-audio dialogue from an internal
> Accenture meeting (via a paywalled 404 Media investigation) in which Accenture's own
> leadership identifies PDF-to-markdown conversion by non-engineering staff, not
> engineer-driven coding agents, as one of the company's biggest sources of AI token
> consumption.

## Source Context

- **Type**: blog-post (Simon Willison link-blog entry, posted 7th August 2026, tagged
  `pdf`, `markdown`, `ai`, `generative-ai`, `llms`, `ai-misuse`). The post is short (one
  framing sentence, a three-paragraph blockquote, one closing comment) and links out to
  a 404 Media investigative article, "The Tokenpocalypse Is Here: Companies Are
  Scrambling To Stop Spending So Much on AI," published 24th June 2026 and mostly
  paywalled (`post-access-paid` class; only the first five paragraphs are freely
  readable — see Extraction Notes).
- **Author credibility**: Simon Willison is the creator of Django and one of the
  highest-signal independent LLM-tooling commentators tracked in this corpus (see
  `blog-simonwillison-james-shore-maintenance-costs.md` and others); his link-blog
  functions as a curation signal in its own right. The primary reporting is by 404
  Media, an investigative outlet already corroborated elsewhere in this corpus (see
  Cross-References) for leaked internal corporate material (Slack chats, dashboards,
  emails, and — in this piece — meeting audio recordings). The specific individuals
  quoted (Justice Kwak, Accenture's agentic AI strategy lead, and Stuart Henderson,
  Accenture's client group lead) are named and titled, which raises the evidentiary bar
  above an anonymous leak, though 404 Media's own sourcing chain (audio obtained from an
  unnamed source) cannot be independently verified by this extraction.
- **Scope**: Covers a single named company's (Accenture's) internal token-consumption
  behavior and its self-diagnosis of the cause (non-engineer document workflows, not
  agentic coding). It does not cover other companies, does not give quantitative token
  or dollar figures for this specific anecdote (contrast the dashboard figures in
  `blog-fowler-fragments-2026-07-06.md` Claim 14, which come from a different part of
  the same underlying token-cost-crisis reporting wave), and does not describe what
  remediation, if any, Accenture adopted.

## Extracted Claims

### Claim 1: Accenture's own internal data shows non-engineers, not engineers, are the primary drivers of the company's AI token consumption
- **Evidence**: Direct quote attributed by name and title to Justice Kwak, Accenture's
  agentic AI strategy lead, from leaked internal meeting audio, reproduced by Willison
  from the (otherwise paywalled) 404 Media article and independently confirmed present
  in 404 Media's own freely-readable preview paragraphs.
- **Confidence**: emerging
- **Quote**: "We're seeing from some of the data internally at least that it's actually
  not our engineers that are driving the token consumption. It's a lot of the
  non-engineers that are doing some of those behaviors [...] you were talking about,"
  Justice Kwak, Accenture's agentic AI strategy lead, said [...]
- **Our assessment**: This is a specific, named-individual, named-company data point
  that directly corroborates and adds primary-source depth to
  `blog-fowler-fragments-2026-07-06.md` Claim 15, which had already summarized this
  same underlying finding secondhand via Fowler's paraphrase. We buy it as company-level
  self-reported evidence (Accenture's own internal telemetry, as characterized by its
  own strategy lead) but not as a generalizable industry claim — it is one consultancy's
  internal mix of engineering vs. non-engineering AI usage, which will vary heavily by
  company and workforce composition.

### Claim 2: Converting a PDF into images and then into markdown is identified by Accenture leadership, in an internal meeting, as "one of the big token chewers"
- **Evidence**: Direct quote of a leaked-audio exchange between Stuart Henderson
  (Accenture's client group lead) and Justice Kwak, reproduced verbatim by Willison.
- **Confidence**: emerging
- **Quote**: "Stuart Henderson, Accenture's client group lead, interrupts. He jokes he
  hopes Kwak didn't just convert a PDF into images and then into markdown files. 'I'm
  learning that's one of the big token chewers,' Henderson says. 'Turning PDFs into
  markdown: is that right?' That's when Kwak says that's what Accenture's own data
  shows."
- **Our assessment**: This is the single most concrete, actionable data point in the
  source: a specific document-processing pattern (PDF → image → markdown, a workflow
  commonly used to feed scanned/complex PDFs to an LLM) named as a major token sink by
  people with access to Accenture's internal usage data. Worth noting: 404 Media's own
  article summary (meta description and opening paragraph, both freely readable outside
  the paywall) instead describes the behavior as "converting PDFs to presentation
  slides" — a different specific workflow than the "PDF → images → markdown" exchange
  actually quoted in the leaked-audio dialogue. This looks like an inconsistency
  internal to the 404 Media article between its summary framing and its quoted
  transcript, not a disagreement between two of our sources, so it does not rise to a
  MINER.md §4a contradiction — but it means the exact workflow being described ("PDF to
  slides" vs. "PDF to markdown via images") should be treated as imprecisely reported
  rather than settled. See Extraction Notes.

### Claim 3: Simon Willison argues PDFs are a fundamentally poor medium for information transfer, and Accenture's internal token-cost data could help push that argument into wider business adoption
- **Evidence**: Willison's own closing editorial comment on the anecdote.
- **Confidence**: anecdotal (opinion/editorial framing, not a data claim)
- **Quote**: "Maybe if Accenture figure out that PDFs are a _terrible medium for
  communicating information_ they'll be able to push that message out to the rest of
  the business world too!"
- **Our assessment**: This is commentary, not evidence, but it is a useful framing
  device: it reframes a cost-governance anecdote (token spend) as also a
  document/data-format engineering problem — i.e., the fix isn't only "use fewer
  tokens" but "stop feeding LLMs an image-based, non-machine-native format in the first
  place." That reframing is novel to this corpus's token-cost cluster, which has
  otherwise focused on billing models, model selection, and organizational governance
  rather than input-format engineering.

### Claim 4: 404 Media situates the Accenture anecdote within a broader 2026 industry shift away from "uninhibited AI growth," citing GitHub's move to per-token billing, Uber's capping of employee AI tool usage after blowing through its AI budget in four months, and Accenture's own internal mandate that senior staff use AI or risk losing out on promotions
- **Evidence**: 404 Media's own freely-readable lead paragraphs (before the paywall),
  each citing a separate named secondary source (TechCrunch for GitHub's per-token
  billing; Bloomberg and The Information for Uber's usage cap and budget overrun; CNBC
  for Accenture's senior-staff AI mandate).
- **Confidence**: emerging
- **Quote**: "The news highlights a major shift in the tech industry and other companies
  that use AI: the wave of uninhibited AI growth is over. Some AI providers like GitHub
  are now charging customers per token rather than a flat subscription fee, leading some
  companies to burn through their tokens. Uber recently capped employees' use of AI
  tools like Claude Code and Cursor; that came after Uber told employees to use AI as
  much as possible and Uber's CTO said the company had blown its entire AI budget in
  four months. And Accenture itself reportedly started requiring senior staff to start
  using AI or risk losing out on promotions."
- **Our assessment**: This is a tightly-sourced roll-up (three separate outlets, three
  separate named companies) rather than a single anecdote, and it corroborates the
  broader "subscription-to-consumption billing shift" and "adoption-pressure-then-cost-
  panic" narrative already documented at length in
  `blog-thoughtworks-vega-token-billing-lockin.md` (Claim 1) and
  `blog-thoughtworks-kamelman-token-crisis.md` (Claim 3, Claim 4) — see
  Cross-References. The Uber budget-cap detail specifically corroborates
  `blog-thoughtworks-kamelman-token-crisis.md` Claim 2 (Uber's COO stating no
  demonstrated link between token consumption and shipped features) as the same
  underlying Uber cost-control episode viewed from a different secondary source.

### Claim 5: 404 Media explicitly frames the Accenture anecdote as undercutting the narrative that engineer-driven code generation is the primary driver of rising enterprise AI token costs
- **Evidence**: 404 Media's own editorial framing sentence in the freely-readable
  portion of the article.
- **Confidence**: anecdotal (editorial interpretation, not a measured claim)
- **Quote**: "It also undercuts the narrative that superpowered engineers generating
  mountains of code are behind the AI boom. In many cases it is non-technical staff
  burning through tokens for non-specialized tasks."
- **Our assessment**: This is the article's thesis statement, and it is a genuinely
  novel angle for this corpus's token-cost cluster, which has so far discussed
  engineering-side waste patterns in detail (verbose context, retry loops, model
  over-selection — e.g. `blog-thoughtworks-vega-token-billing-lockin.md` Claim 2,
  `blog-thoughtworks-kamelman-token-crisis.md` Claim 8) but has not previously supplied
  a named-company case where the dominant cost driver was explicitly attributed to
  non-engineering staff rather than engineering/agentic workflows. We buy the framing as
  true for Accenture specifically (per its own internal data, as reported), but treat it
  as a single-company data point, not a generalized industry finding — a consultancy
  with a very large non-engineering, document-heavy client-services workforce is a
  plausible outlier case, not necessarily representative of, say, a software product
  company.

### Claim 6: Accenture describes seeing "soaring token spend" broadly (i.e., as an observation from its internal data, not scoped only to the specific PDF-conversion behavior)
- **Evidence**: 404 Media's lead paragraph, attributed to "the audio" without a specific
  named speaker for this particular phrase.
- **Confidence**: anecdotal (unattributed to a specific named speaker within the
  freely-readable text, though sourced to the same leaked-audio recordings as the
  Kwak/Henderson quotes)
- **Quote**: "Across the industry Accenture is seeing 'soaring token spend,' according
  to the audio."
- **Our assessment**: Read alongside Claim 1, this suggests Accenture's internal
  observation spans its own consumption and/or its view of client-industry consumption
  more broadly ("across the industry Accenture is seeing..." is ambiguous between
  "Accenture's own spend" and "the spend Accenture observes across its client base" —
  the freely-readable text doesn't disambiguate). Flagged as a phrase worth verifying
  against the full paywalled article if it becomes accessible.

## Concrete Artifacts

```
Source: Simon Willison, "The Tokenpocalypse Is Here: Companies Are Scrambling To Stop
        Spending So Much on AI" (simonwillison.net, 7th August 2026), quoting a 404
        Media investigation (published 24th June 2026), via leaked internal Accenture
        meeting audio.

Willison's framing sentence:
"There's a fun anecdote from Accenture (apparently via leaked meeting audio recordings)
in this 404 Media piece from June 24th:"

Full blockquoted leaked-audio exchange, as reproduced by Willison:

  "We're seeing from some of the data internally at least that it's actually not our
  engineers that are driving the token consumption. It's a lot of the non-engineers
  that are doing some of those behaviors [...] you were talking about," Justice Kwak,
  Accenture's agentic AI strategy lead, said [...]

  Stuart Henderson, Accenture's client group lead, interrupts. He jokes he hopes Kwak
  didn't just convert a PDF into images and then into markdown files. "I'm learning
  that's one of the big token chewers," Henderson says. "Turning PDFs into markdown:
  is that right?"

  That's when Kwak says that's what Accenture's own data shows.

Willison's closing comment:
"Maybe if Accenture figure out that PDFs are a terrible medium for communicating
information they'll be able to push that message out to the rest of the business
world too!"

---

Source: 404 Media, "The Tokenpocalypse Is Here: Companies Are Scrambling To Stop
        Spending So Much on AI" (404media.co, 24th June 2026) — freely-readable
        preview paragraphs only (article is paywalled `post-access-paid` after this
        point):

"Consulting giant Accenture is trying to figure out how to stop non-technical workers
from blowing through companies' AI token budget on trivial tasks like converting PDFs
to presentation slides, according to leaked audio obtained by 404 Media. Across the
industry Accenture is seeing 'soaring token spend,' according to the audio.

The news highlights a major shift in the tech industry and other companies that use
AI: the wave of uninhibited AI growth is over. Some AI providers like GitHub are now
charging customers per token rather than a flat subscription fee, leading some
companies to burn through their tokens. Uber recently capped employees' use of AI
tools like Claude Code and Cursor; that came after Uber told employees to use AI as
much as possible and Uber's CTO said the company had blown its entire AI budget in
four months. And Accenture itself reportedly started requiring senior staff to start
using AI or risk losing out on promotions.

It also undercuts the narrative that superpowered engineers generating mountains of
code are behind the AI boom. In many cases it is non-technical staff burning through
tokens for non-specialized tasks.

'We're seeing from some of the data internally at least that it's actually not our
engineers that are driving the token consumption. It's a lot of the non-engineers
that are doing some of those behaviors [...] you were talking about,' Justice Kwak,
Accenture's agentic AI strategy lead, said in a recent internal meeting, according to
the audio obtained by 404 Media."

[Article continues behind paywall: "This post is for paid members only."]
```

## Cross-References

### Cross-reference verification notes
`blog-fowler-fragments-2026-07-06.md`, `blog-thoughtworks-vega-token-billing-lockin.md`,
`blog-thoughtworks-kamelman-token-crisis.md`, and `blog-anthropic-prompt-caching-
everything.md` were re-read directly (MINER.md §4b) and the claim numbers cited below
were confirmed against those notes' numbered `### Claim N:` headings in document order.

- **Corroborates / same underlying source as**:
  - `blog-fowler-fragments-2026-07-06.md` Claim 15 ("404 Media separately reported that
    Accenture's biggest token-cost driver was not agentic software engineering but
    non-engineering staff using AI for tasks like converting PDFs into presentation
    slides"). That note's Claim 14 assessment explicitly flagged: "a dedicated 404
    Media source note (if the full paywalled report becomes accessible) could resolve
    the attribution and add substantially more figures." That note's own Concrete
    Artifacts section identifies the underlying piece by name: "404 Media podcast
    referenced: 'The AI Tokenpocalypse Is Here.'" This note is that same underlying
    404 Media investigation, reached via a different secondary source (Willison's
    link-blog) that reproduces verbatim leaked-audio dialogue Fowler's fragment only
    paraphrased — see Claim 1 and Claim 2 above, which supply the primary quotes and
    named speakers (Kwak, Henderson) that Fowler's fragment did not include. This does
    not add the dollar/token figures Fowler's Claim 14 flagged as missing (Claim 14 is a
    different, dashboard-based part of the same reporting wave, not resolved by this
    note), but it does resolve the attribution gap for Claim 15 specifically down to
    named individuals and an exact quoted exchange.
  - `blog-thoughtworks-vega-token-billing-lockin.md` Claim 1 (the shift from flat
    subscription pricing to variable, consumption-based billing) and
    `blog-thoughtworks-kamelman-token-crisis.md` Claim 3 and Claim 4 (Microsoft's Claude
    Code license cancellation and GitHub's usage-based credit pricing): this note's
    Claim 4 independently corroborates the same GitHub per-token billing shift via a
    different secondary citation chain (404 Media → TechCrunch, rather than
    Thoughtworks's own sourcing).
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 2 (Uber COO Andrew Macdonald
    stating there is no demonstrated link between token consumption and shipped
    features): this note's Claim 4 independently corroborates the same Uber
    budget-capping episode via 404 Media's citation of Bloomberg and The Information.

- **Contradicts**: None identified. The internal inconsistency noted in Claim 2 (404
  Media's own article describing the anecdote as "PDF to presentation slides" in its
  summary paragraph vs. "PDF to images to markdown" in the quoted transcript) is
  internal to the single 404 Media article, not a disagreement between two corpus
  sources, so no contradiction issue was filed per MINER.md §4a.

- **Extends**: `blog-fowler-fragments-2026-07-06.md` Claim 15, as described above — from
  a secondhand paraphrase to a primary-source verbatim quote with named speakers.
  `blog-anthropic-prompt-caching-everything.md` (which documents *how* to keep
  agentic-coding token costs down via caching) is extended by this note's observation
  that a comparably large token-cost lever — input document format — sits entirely
  outside the coding-agent context that note addresses; a caching strategy does nothing
  for a workflow that converts a PDF into images and re-sends them as markdown context
  on every use.

- **Novel**: The specific, named-individual confirmation that a consultancy's own
  *internal usage telemetry* attributes majority token consumption to non-engineers
  (Claim 1) is new to this corpus — prior token-cost sources measure consumption in
  aggregate dollars/tokens (Fowler's $5M→$15M→$120M dashboard, Kamelman's AT&T and
  insurer figures) without breaking down the split between engineering and
  non-engineering usage. The specific PDF→image→markdown workflow as a named "token
  chewer" (Claim 2) is also new — no existing note in this corpus names a specific
  document-processing pattern as a major token-cost driver.

## Guide Impact

- **Chapter 02 (Harness Engineering — cost management)**: Add the PDF→image→markdown
  conversion pattern (Claim 2) as a concrete, named example of a non-coding-agent token
  sink, positioned alongside the existing token-budget/cost-governance material sourced
  from `blog-thoughtworks-omahony-feature-token-budgets.md` and
  `docs-ghaw-cost-management.md`. The guide's cost-governance guidance currently centers
  on agent design (retry loops, context management, model routing); this source
  supports adding a note that document-ingestion workflows (PDF handling specifically)
  deserve the same scrutiny, and that "not our engineers" (Claim 1) means cost
  governance needs to reach non-engineering AI users, not just the coding-agent harness.

- **Chapter 04 (Context Engineering)**: Add Willison's framing (Claim 3) that PDFs are a
  poor native input format for LLM context — an image-based, non-machine-native
  document format that forces an expensive image→markdown conversion round-trip — as a
  concrete instance of a broader context-engineering principle: input format choice is
  itself a token-cost lever, not just prompt/context-window management.

- **Chapter 05 (Team Adoption)**: Add the non-engineer-driven consumption pattern (Claim
  1, Claim 5) as a named-company data point for the guide's discussion of scaling AI
  adoption beyond engineering teams — team-adoption guidance should flag that
  document-heavy, non-engineering workflows (client-services, admin, ops) can generate
  outsized token costs relative to coding-agent usage, and that cost governance/training
  needs to extend past the engineering org.

## Extraction Notes

- The 404 Media article is paywalled (`post-access-paid` class) after its first five
  paragraphs. This note draws the freely-readable preview paragraphs directly from
  404 Media's own page (fetched and confirmed via raw HTML, not just Willison's
  reproduction), and draws the Kwak/Henderson dialogue exchange from Simon Willison's
  blockquote, which reproduces text that sits past 404 Media's own paywall cutoff on
  404 Media's site as currently configured. The remainder of the 404 Media article
  (beyond what both sources make available) was not read and is not represented here.
  If the full paywalled 404 Media article becomes accessible, it should be re-mined —
  it likely contains the dollar/token figures and additional named companies that
  `blog-fowler-fragments-2026-07-06.md` Claim 14's assessment flagged as still missing
  from this corpus.
- Did not follow the three secondary links cited in 404 Media's freely-readable preview
  (TechCrunch on GitHub per-token billing, Bloomberg/The Information on Uber's AI
  budget, CNBC on Accenture's senior-staff AI mandate) as separate sources — they are
  represented here only as 404 Media's own citations (Claim 4), not independently
  verified against the original outlets. If any of these becomes a standalone
  guide-relevant claim, it should be mined directly from its primary outlet rather than
  relayed through this note.
- No contradiction issue was filed. See Cross-References → Contradicts for the reasoning
  (the "PDF to slides" vs. "PDF to markdown" discrepancy is internal to the single 404
  Media article, not a disagreement between two corpus sources).
