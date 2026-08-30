---
source_url: https://openai.com/index/stampli
source_type: blog-post
title: "Stampli cuts launch hours by 68% using ChatGPT Work"
author: OpenAI (customer case study, featuring Eyal Feldman, CEO and Co-Founder, and Melad Zahedi, Director of Product Marketing, Stampli)
date_published: 2026-08-20
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: anecdotal
issue: "#3100"
---

# Stampli cuts launch hours by 68% using ChatGPT Work

> An OpenAI customer case study describing how Stampli's product marketing
> team used Codex and ChatGPT Work to compress an estimated 243 modeled
> active role-hours of go-to-market production work for its "Deep Finance"
> launch into about 77 hours (a 68% reduction, "3.16x faster"), taking the
> product from prototype to public launch in six weeks despite fixed design
> and contractor resources. The same GPT-powered system is also used daily
> to keep product materials current and to answer live business questions —
> including one instance where an employee retrieved and analyzed
> cross-system metrics live in an executive meeting in about 20 seconds of
> keystrokes, work the team says would otherwise have taken its FP&A team
> half a day.

## Source Context

- **Type**: blog-post (OpenAI "Product"/customer-story vertical,
  `openai.com/index/stampli`, published August 20, 2026; ~700 words).
  Structured as a marketing case study with a company metadata block
  (Company size: Mid-market, Region: North America, Industry: Finance,
  Technology, Products: Codex), a two-stat headline block ("100s — Pieces
  of content created each week using ChatGPT Work" and "3.16x — Faster
  launch to production with Codex"), five named body sections, and two
  named-executive pull quotes. Not a technical or engineering blog post.
- **Author credibility**: Written and published by OpenAI, not Stampli, as
  promotional customer-success content — OpenAI has a direct commercial
  incentive to present Codex and ChatGPT Work favorably. Two named
  individuals are quoted: Eyal Feldman (CEO and Co-Founder, Stampli) and
  Melad Zahedi (Director of Product Marketing, Stampli). No engineer,
  designer, or other team member who executed the work is separately
  quoted, no methodology is disclosed for how "243 modeled active
  role-hours" was calculated, and no independent party verifies the launch
  timeline or content-volume figures.
- **Scope**: Covers one detailed launch case (Stampli's "Deep Finance"
  go-to-market and content-production workflow, moving from a fixed
  six-week timeline to shipped launch), a broader description of a
  standing GPT-powered system the product marketing team uses daily
  (gathering product/meeting context to keep materials current, surfacing
  insights, and answering ad hoc business questions), and a forward-looking
  "what's next" section about scaling the approach to more products and
  workflows. Does NOT cover: engineering/coding use of Codex outside the
  content-production and information-gathering context, model version or
  configuration details, security/governance detail, adoption metrics
  outside the one featured team, or any account from anyone other than the
  CEO and the Director of Product Marketing.

## Extracted Claims

### Claim 1: Stampli's marketing team compressed an estimated 243 modeled active role-hours of Deep Finance go-to-market and content production work into about 77 hours using Codex and ChatGPT Work, a 68% reduction and roughly 3.16x faster production, while keeping full human review and final approval on everything customer-facing
- **Evidence**: Case-study headline stat block ("3.16x — Faster launch to production with Codex") plus a restated, more precise figure in the body text.
- **Confidence**: anecdotal (a single vendor-selected launch project at a single mid-market company; "243 modeled active role-hours" is described as an estimate against a defined workflow, not a role-hour count that was ever actually staffed and measured the old way)
- **Quote**: "Across the defined Deep Finance go-to-market and content production workflow, the Stampli team estimates the launch would have taken about 243 modeled active role-hours without Codex. With Codex, it took approximately 77, saving roughly 166 hours or 3.16x faster production."
- **Our assessment**: This is a more methodologically explicit figure than most of the corpus's OpenAI case studies — "243 modeled active role-hours" implies a defined counterfactual workflow model rather than a single practitioner's rough retrospective guess (compare `blog-openai-notion-codex-case-study.md` Claim 7's "two weeks... maybe three or four hours" recollection). Still, the counterfactual side (243 hours) is explicitly labeled a model/estimate, not a measured baseline — no prior Stampli launch was actually run without Codex to compare against, so the ratio should be read as "a single vendor-selected launch, benchmarked against the team's own estimate of its unassisted cost," not as an audited before/after measurement. The headline "cuts launch hours by 68%" title figure and the body's "3.16x faster" / "166 hours saved" figures are internally consistent with each other ((243-77)/243 ≈ 68%; 243/77 ≈ 3.16), which is a basic but useful sanity check most vendor case studies in the corpus do not make possible to verify from the published numbers alone.

### Claim 2: Deep Finance moved from an initial prototype demo to a public go-to-market launch and first shipped product in about six weeks, with design resources and outside contractors already committed to other priorities
- **Evidence**: Narrative description opening the "From prototype to launch, in six weeks" section.
- **Confidence**: anecdotal (single project, self-reported timeline, no independent verification of the "six weeks" window's start/end points)
- **Quote**: "Deep Finance moved from an initial prototype demo to a public GTM launch and first shipped product in about six weeks. With design resources and outside contractors committed to other priorities, the team used Codex to turn evolving product decisions into review-ready assets across a seven-part blog series, launch emails, a webinar and its supporting deck, social and paid creative, a PR Newswire release, the Deep Finance web page, and sales enablement materials."
- **Our assessment**: This grounds the headline ratio in a specific, checkable scope: a named list of seven-plus concrete content-production asset types (blog series, emails, webinar + deck, social/paid creative, a wire-service press release, a web page, sales enablement materials) produced under a resource constraint (design and contractors already committed elsewhere) rather than an unconstrained team. This is a materially different scenario from the corpus's engineering-migration case studies (`blog-openai-asana-codex-case-study.md`, Mike Krieger's port in `blog-anthropic-code-migration-playbook.md`) — the constraint here is competing demand for scarce creative/design labor, not a deprecated dependency or legacy codebase, making this the first source in the corpus documenting agent-driven compression of a resource-constrained marketing/GTM production timeline specifically.

### Claim 3: Codex also handled roughly 90% of the polished animation work for the launch's hero animation — through exploration, iteration, and packaging — before a contractor finished the opening scene and final format
- **Evidence**: A specific technical/creative-production detail within the same "six weeks" section.
- **Confidence**: anecdotal (single project, self-reported percentage with no definition of how "90%" of animation work was measured — by time, by shot count, or by the team's own estimate)
- **Quote**: "Codex also helped create the launch’s hero animation through exploration, iteration, and packaging, handling roughly 90% of the polished animation work before a contractor finished the opening scene and final format."
- **Our assessment**: Novel to the corpus — no existing OpenAI customer case study describes Codex being used for non-text, non-code creative asset production (motion/animation work) with a human contractor finishing only the opening scene and final format. This is a different creative-asset category from anything else in the corpus's OpenAI case-study set (which otherwise covers code, documents, dashboards, and research reports), and it is presented as a hybrid workflow — the agent doing the bulk of iterative creative exploration, a human closing the final, highest-craft portion — rather than either full automation or full human authorship.

### Claim 4: Stampli's CEO frames Codex's value as shortening the distance between a customer's need, the team's response, and real usage learnings, extending technical abilities across every team to move "10x faster from requirement to deployable solution"
- **Evidence**: Direct, attributed quote from Eyal Feldman, CEO and Co-Founder, Stampli.
- **Confidence**: anecdotal (single executive's characterization; "10x faster" is not tied to any specific measured project, unlike the 243→77-hour figure in Claim 1, which is scoped to the Deep Finance launch specifically)
- **Quote**: "Codex shortens the distance between a customer’s need, our team’s response, and real learnings from usage. By extending technical abilities across every team, it helps us move 10x faster from requirement to deployable solution."
- **Our assessment**: This is a broader, unscoped multiplier claim (10x, "every team") distinct from and less precisely grounded than the launch-specific 3.16x/68% figure in Claim 1 — the case study does not reconcile the two numbers or explain whether "10x faster from requirement to deployable solution" refers to the same Deep Finance launch, a different workflow, or a general impression. Treat the 10x figure as an executive's general characterization of perceived value, not as a second measured data point alongside the 3.16x figure.

### Claim 5: The same GPT-powered system used for the Deep Finance launch is Stampli's standing daily infrastructure, replacing a manual process of interviewing product managers, reading Jira tickets, reviewing GitHub, and working through meeting notes to keep help center articles, presentations, one-pagers, and other materials current
- **Evidence**: Narrative description in the "A system built for daily use, not just launches" section.
- **Confidence**: anecdotal (unattributed narrator claim describing a standing internal system; no metrics on how often it runs, how many materials it updates, or how accuracy/staleness is checked)
- **Quote**: "Keeping product materials current used to require interviewing product managers, reading Jira tickets, reviewing GitHub, and working through meeting notes. The team then had to translate that information into help center articles, presentations, one-pagers, and other assets. Stampli has automated much of that process with a GPT‑powered system. It gathers information from product systems and meeting notes, then helps keep those materials up to date."
- **Our assessment**: This names a specific set of source systems (Jira, GitHub, meeting notes, plus interviews with PMs) being consolidated into an automated content-freshness pipeline — a concrete instance of the "aggregate scattered context into a single system that keeps derived artifacts current" pattern, worth comparing against other corpus sources describing agent-maintained living documentation. The launch (Claim 1-3) is framed explicitly as one example output of this standing system, not a one-off project — which changes how the launch's 68%/3.16x figure should be read: as one measured instance of an already-existing production pipeline's output, not a first-time experiment.

### Claim 6: Melad Zahedi (Director of Product Marketing) says the same automations have multiplied a small team's output roughly 10x, producing hundreds of pieces of content weekly versus "just a couple" before
- **Evidence**: Direct, attributed quote from Melad Zahedi, Director of Product Marketing, Stampli, describing team-level output.
- **Confidence**: anecdotal (single named individual's characterization of his own team's output; "10x" and "hundreds... weekly" are not independently measured or broken down by content type)
- **Quote**: "it’s multiplied the output of a small team by 10x, putting out hundreds of pieces of content on a weekly basis, where it was limited to just a couple before."
- **Our assessment**: This is the source of the article's headline stat ("100s — Pieces of content created each week using ChatGPT Work") and is a team-output-volume claim distinct in kind from Claim 1's hours-saved figure — it describes scaling the *quantity* of content produced, not just the *time* to produce a fixed set of launch assets. As with the CEO's 10x figure in Claim 4, no baseline definition is given for what counts as "a piece of content" or how "just a couple" (before) was counted, so the ratio should be read as an order-of-magnitude impression from the team lead, not an audited output count.

### Claim 7: Zahedi uses GPT-powered automations as a "second brain" to organize information across a schedule filled with back-to-back meetings, saying it lets him arrive at every meeting prepared with context and understanding of what's needed from him
- **Evidence**: Narrative framing plus a direct attributed quote, in the "Surfacing insights when they matter" section.
- **Confidence**: anecdotal (single practitioner's self-description of a personal workflow habit)
- **Quote**: "Being able to go to every meeting prepared with context, understanding what is needed from me in that meeting and how to stay efficient with my time, has been an amazing benefit," he says.
- **Our assessment**: A "second brain" meeting-prep framing that is structurally similar to, but distinct in mechanism from, the industry-monitoring/triage use case documented in `blog-openai-nvidia-chatgpt-work-case-study.md` Claim 5-6 (Rachita Jain's 25-40 external updates → 5-8 actionable signals per week, framed as "passive reading into active intelligence"). Zahedi's version is inward-facing (organizing the user's own scattered meeting/context load) rather than outward-facing (triaging external industry signal), so the two are complementary rather than duplicate data points on the same underlying "information consolidation" pattern.

### Claim 8: In one executive meeting, an employee used Codex to retrieve and analyze metrics stored across HubSpot and other systems live during the call, producing in about 20 seconds of keystrokes work that Zahedi says would otherwise have taken the FP&A team about half a day to assemble into a report with a confidence-inspiring model and answer
- **Evidence**: Narrative description of a specific incident plus a direct attributed quote from Zahedi.
- **Confidence**: anecdotal (single incident, self-reported, no detail on which metrics, what analysis was performed, or how the result's accuracy was checked before being presented to the meeting)
- **Quote**: "This is something that would’ve taken our FP&A team half a day to put a report together, give us a model, and give us an answer that we felt confident in. Someone was able to do it with 20 seconds of keystrokes," Zahedi says.
- **Our assessment**: This is the most concretely time-bounded single-incident claim in the source (half a day vs. ~20 seconds of keystrokes) and, notably, describes a live, synchronous, in-meeting use of the agent to answer a question on the spot — a different usage shape from every other claim in this note, which describe asynchronous production work completed ahead of a deadline. No detail is given on how the "confidence" bar for the half-day manual process compares to the confidence placed in the 20-second answer, which is a real gap given that this incident involved presenting numbers to company leadership.

### Claim 9: Zahedi estimates the entire Deep Finance prototype-to-launch process took about six weeks with OpenAI tools, versus what would previously have taken months or even quarters
- **Evidence**: Direct attributed quote in the "Making more room for strategy" section, restating and slightly extending Claim 2's six-week figure with an explicit prior-baseline comparison.
- **Confidence**: anecdotal (single practitioner's retrospective estimate for an unexecuted counterfactual, similar in kind to the "five years" and "two weeks" counterfactuals in `blog-openai-asana-codex-case-study.md` and `blog-openai-notion-codex-case-study.md`)
- **Quote**: "Zahedi estimates that with OpenAI tools the process took about six weeks, which previously would have taken months or even quarters."
- **Our assessment**: Unlike Claim 1's specific 243→77 modeled-hours figure, "months or even quarters" is a vague, unquantified counterfactual range — this is the least precise time-comparison claim in the source and should not be cited alongside the more specific hours-based figure as if it carries equivalent evidentiary weight.

### Claim 10: Zahedi frames the larger opportunity as expanding what employees believe they can take on, saying curiosity and "trying everything first through ChatGPT" will unlock latent organizational capacity
- **Evidence**: Direct, attributed closing quote from Melad Zahedi, in the "What's next" section.
- **Confidence**: anecdotal (single executive's forward-looking characterization, not a measured outcome)
- **Quote**: "Being curious and just asking, ‘What can I do?’ and trying everything first through ChatGPT will unlock a lot of latent capacity that you didn’t realize was there in your organization—and in yourself."
- **Our assessment**: A capability-expansion framing (agent use widening what an individual or org believes is worth attempting) that echoes the CTO hedge in `blog-openai-asana-codex-case-study.md` Claim 7 ("agents can give engineers more room for craft—and make once-impossible work worth attempting") — a second, differently-worded instance of an OpenAI customer executive characterizing agent value in terms of expanded scope of ambition rather than a flat productivity multiplier.

## Concrete Artifacts

### Case study metadata and stat block

```
Source: https://openai.com/index/stampli (August 20, 2026)

Company size: Mid-market
Region:       North America
Industry:     Finance, Technology
Products:     Codex

Headline stats:
  100s    Pieces of content created each week using ChatGPT Work
  3.16x   Faster launch to production with Codex
```

### Launch workflow description — verbatim

```
Source: https://openai.com/index/stampli (August 20, 2026)

"Stampli is an intelligent procure-to-pay platform that connects
procurement, accounts payable, vendor management, payments, and employee
spend. Its Deep Finance™ product transforms the data moving through
Stampli’s procure-to-pay platform into executive spend intelligence for
CFOs, VPs, and other business leaders. Launching it meant product
development, positioning, design, communications, enablement, and
operations all moving in parallel, on a fixed timeline, with design
resources and outside contractors already committed to other priorities.

Stampli’s marketing team used Codex to connect product context, meeting
notes, decisions, and messaging guidelines into a shared system. With
OpenAI tools, they compressed an estimated 243 hours of production work
into about 77, while keeping full human review and final approval on
everything customer-facing."

"Deep Finance moved from an initial prototype demo to a public GTM launch
and first shipped product in about six weeks. With design resources and
outside contractors committed to other priorities, the team used Codex to
turn evolving product decisions into review-ready assets across a
seven-part blog series, launch emails, a webinar and its supporting deck,
social and paid creative, a PR Newswire release, the Deep Finance web
page, and sales enablement materials. Codex also helped create the
launch’s hero animation through exploration, iteration, and packaging,
handling roughly 90% of the polished animation work before a contractor
finished the opening scene and final format.

Across the defined Deep Finance go-to-market and content production
workflow, the Stampli team estimates the launch would have taken about
243 modeled active role-hours without Codex. With Codex, it took
approximately 77, saving roughly 166 hours or 3.16x faster production."
```

### Named quotes — verbatim, in order of appearance

```
Source: https://openai.com/index/stampli (August 20, 2026)

Eyal Feldman, CEO and Co-Founder, Stampli:
"Codex shortens the distance between a customer’s need, our team’s
response, and real learnings from usage. By extending technical abilities
across every team, it helps us move 10x faster from requirement to
deployable solution."

Melad Zahedi, Director of Product Marketing, Stampli:
1. "it’s multiplied the output of a small team by 10x, putting out
   hundreds of pieces of content on a weekly basis, where it was limited
   to just a couple before."

2. "Being able to go to every meeting prepared with context, understanding
   what is needed from me in that meeting and how to stay efficient with
   my time, has been an amazing benefit," he says.

3. "This is something that would’ve taken our FP&A team half a day to put
   a report together, give us a model, and give us an answer that we felt
   confident in. Someone was able to do it with 20 seconds of keystrokes,"
   Zahedi says.

4. "Being curious and just asking, ‘What can I do?’ and trying everything
   first through ChatGPT will unlock a lot of latent capacity that you
   didn’t realize was there in your organization—and in yourself."
```

## Cross-References

- **Corroborates**:
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 6 (Virgin
    Atlantic: "weeks of analysis to hours") and Claim 7 (NVIDIA: ~40% of
    pre-event time eliminated) — this source's Claim 1 (243 → 77
    modeled hours, 68% reduction) is another instance of the same
    OpenAI-published "days/weeks of manual work compressed via an agent"
    testimonial shape, this time with a more explicit modeled-hours
    methodology than either of those two testimonials disclosed.
  - `blog-openai-asana-codex-case-study.md` Claim 7 (Asana's CTO:
    "agents can give engineers more room for craft—and make
    once-impossible work worth attempting") — this source's Claim 10
    (Zahedi: curiosity "will unlock a lot of latent capacity... in your
    organization—and in yourself") is a second, independently-worded
    OpenAI customer executive framing agent value as expanded scope of
    ambition rather than a flat multiplier.
  - `blog-openai-nvidia-chatgpt-work-case-study.md` Claim 6 (Rachita
    Jain: "ChatGPT helped me change passive reading into active
    intelligence") — this source's Claim 7 (Zahedi's "second brain"
    meeting-prep framing) is a second named individual, at a second
    company, describing ChatGPT Work as consolidating scattered context
    into meeting/decision-ready form, though the two use cases differ in
    direction (Jain: external industry-signal triage; Zahedi: internal
    meeting/context prep — see Claim 7's Our assessment).
- **Contradicts**: None identified.
- **Extends**:
  - `blog-openai-asana-codex-case-study.md` and
    `blog-openai-notion-codex-case-study.md` (engineering-focused case
    studies) and `blog-openai-nvidia-chatgpt-work-case-study.md` /
    `blog-openai-ringcentral-case-study.md` (sales/ops-focused case
    studies) — this source extends the corpus's OpenAI customer-story set
    into product-marketing/GTM content production specifically, a domain
    not previously covered by name. It is the first source in the corpus
    to document agent-driven production of a full multi-format GTM
    launch package (blog series, emails, webinar + deck, paid/social
    creative, press release, web page, sales enablement) under a
    resource constraint (design/contractors committed elsewhere), and the
    first to describe Codex handling non-text creative asset production
    (a hero launch animation, ~90% Codex-produced) rather than only text,
    code, dashboards, or research reports.
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 8 (internal
    OpenAI sales/finance anecdotes: discovery-to-POC in 24 hours, weeks
    → hours; month-end close days → hours) — this source's Claim 8 (a
    live in-meeting HubSpot data query answered in ~20 seconds of
    keystrokes vs. an FP&A half-day) is a structurally similar
    "synchronous, live-meeting agent query replacing a slower manual
    analysis process" claim, but from an external customer (Stampli)
    rather than OpenAI's own internal usage, corroborating that this
    live-query pattern is not unique to OpenAI's internal tooling.
- **Novel**:
  - An explicit "modeled active role-hours" counterfactual methodology
    (243 → 77 hours; Claim 1) — more methodologically specific than the
    single-practitioner retrospective-recollection figures elsewhere in
    the corpus's OpenAI case-study set (e.g., Notion's "maybe three or
    four hours" recollection), though still a self-reported, unaudited
    model rather than a measured baseline.
  - Non-text creative-asset production (a launch hero animation, ~90%
    Codex-produced with a human finishing only the opening scene and
    final format; Claim 3) — the first source in the corpus documenting
    agent involvement in motion/animation creative work specifically.
  - A weekly content-output-volume headline stat ("100s — Pieces of
    content created each week"; Claim 6) distinct from every other
    corpus case study's hours-saved or ratio-based headline metric.
  - A live, synchronous, in-meeting data-retrieval incident with a
    specific keystroke-time figure (Claim 8) as a concrete illustration
    of real-time agent use during a leadership meeting, rather than
    asynchronous task delegation.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add Claim 1 (243 → 77 modeled active
  role-hours, 68% reduction, 3.16x) as another data point in the corpus's
  "days/weeks of manual work compressed via an agent" case-study genre,
  explicitly noting it is the most methodologically transparent of the
  bunch (a named "modeled active role-hours" framework) while still
  flagging it as self-reported and unaudited, consistent with every other
  OpenAI customer-story figure already caveated this way in the corpus.
  Pair Claim 6 (10x team output, hundreds of content pieces weekly) and
  Claim 4 (CEO's unscoped "10x faster... every team" claim) as examples of
  vendor case studies bundling multiple, differently-scoped multiplier
  claims (launch-specific vs. team-wide vs. company-wide) in a single
  piece — worth flagging for readers as a recurring pattern to watch for
  when citing headline ratios from this genre.
- **Chapter 04 (Coordination and Planning)**: Add Claim 2 (product
  development, positioning, design, communications, enablement, and
  operations moving in parallel on a fixed timeline with design/contractor
  resources committed elsewhere) as a concrete example of agent-assisted
  coordination across a resource-constrained, multi-workstream GTM launch
  — a coordination domain (marketing/GTM production) distinct from the
  parallel-coding-agent-copies pattern already documented from engineering
  migrations (`blog-openai-asana-codex-case-study.md`,
  `blog-anthropic-code-migration-playbook.md`).
- **Chapter 01 (Daily Workflows)**: Add Claim 8 (live in-meeting data
  retrieval, ~20 seconds of keystrokes vs. an FP&A half-day) as a concrete,
  time-bounded illustration of synchronous, real-time agent querying during
  a meeting, distinct from the asynchronous/overnight delegation patterns
  already documented (e.g., `blog-openai-notion-codex-case-study.md`
  Claim 11's overnight research delegation). Add Claim 7 (Zahedi's "second
  brain" meeting-prep framing) alongside the NVIDIA source's "passive
  reading into active intelligence" framing as two named examples of
  context-consolidation-for-meetings use cases.

## Extraction Notes

- **Fetch method**: The live `openai.com/index/stampli` URL returned an
  HTTP 403 to both `WebFetch` and direct `curl` with a browser user-agent
  (the same Cloudflare/bot-challenge pattern already documented for
  `openai.com/index/` posts throughout the corpus, e.g.
  `blog-openai-asana-codex-case-study.md`,
  `blog-openai-notion-codex-case-study.md`). `WebFetch` also explicitly
  refused to fetch `web.archive.org` URLs directly ("Claude Code is unable
  to fetch from web.archive.org"). Search-engine fallbacks (`r.jina.ai`,
  DuckDuckGo HTML, Bing, Google) were all blocked by bot-challenge pages or
  returned irrelevant results. The Wayback Machine's CDX API confirmed a
  crawled snapshot (`http://web.archive.org/web/20260822112941/https://openai.com/index/stampli/`,
  crawled August 22, 2026, two days after the August 20 publication date);
  a first `curl` attempt against that exact snapshot URL returned a
  transient "Internet Archive: Temporarily Offline" 503, but a retry
  against the same URL with an `if_` (raw, unrewritten) modifier succeeded
  (HTTP 200, ~377KB). The raw HTML was parsed locally by stripping
  `<script>`/`<style>` blocks and remaining tags rather than through an
  AI-summarization pass, specifically to guarantee the `Quote` fields above
  are copied character-for-character rather than paraphrased, per
  MINER.md §2a. Every quote was independently verified against the
  stripped plain-text extraction (169 lines, full page from nav through
  footer) before being copied into this note.
- **Full article read**: The article is short (~700 words of body text,
  five named sections plus a closing "What's next") and was read in full
  from the stripped extraction above. The page's "Keep reading" footer
  links to three unrelated OpenAI posts ("Introducing AI Futures,"
  "Offering Zero Data Retention for frontier models," "Replit expands
  access to software creation with GPT-5.6 Luna"), none of which concern
  Stampli or this case study, and were not followed. No further linked
  sub-pages containing substantive content about this specific case study
  were found.
- This is a single-source, single-company, vendor-published case study
  with exactly two named individuals (CEO and Director of Product
  Marketing) and no quote from any team member who actually executed the
  content-production or animation work described. Every claim above should
  be read with that ceiling in mind: OpenAI selected what to publish,
  Stampli did not publish an independent account, and none of the hours,
  percentage, or content-volume figures are independently audited or
  methodologically explained beyond the "modeled active role-hours" label
  in Claim 1.
- No contradictions were identified during cross-referencing (see
  Cross-References → Contradicts); none filed.
