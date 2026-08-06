---
source_url: https://openai.com/index/how-ai-is-expanding-what-people-do-at-work
source_type: blog-post
title: "How AI is Expanding What People Do at Work"
author: OpenAI
date_published: 2026-07-27
date_extracted: 2026-08-06
last_checked: 2026-08-06
status: current
confidence_overall: emerging
issue: "#2522"
---

# How AI is Expanding What People Do at Work

> OpenAI's first "Work at the Frontier" report, analyzing 800,000+
> work-related U.S. ChatGPT messages, introduces "task crossover" — a
> named metric for how often a user's AI-assisted work belongs to a
> different occupation than their own. 43.5% of occupation-specific
> messages fall outside the user's own occupation, with crossover
> concentrated in customer experience, design, and HR, and highest in
> the smallest companies.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`; unsigned,
  house-authored, published under OpenAI's own domain). Framed as the
  first entry in a new recurring series, "Work at the Frontier," and
  summarizes a longer named report, *Work at the Frontier: How AI is
  Expanding What People Do at Work*, which is not itself linked as a
  separate PDF in the fetched page content (contrast with the companion
  *AI Jobs Transition Framework* report, which the post does link to a
  PDF at `cdn.openai.com/pdf/the-ai-jobs-transition-framework_report.pdf`).
- **Author credibility**: First-party OpenAI research/telemetry post, no
  named individual author. The underlying evidence is OpenAI's own
  analysis of ChatGPT message content (occupation inference and task
  classification applied to real user messages), which is vendor-internal
  data OpenAI has direct but unaudited access to — outside readers cannot
  verify the classifier's accuracy or the occupation-inference methodology
  from the blog post alone. The post does disclose its top-level
  methodology (separating "generic" cross-occupation tasks like writing
  and scheduling from occupation-specific tasks, then classifying each
  occupation-specific message by which occupation's typical work it most
  resembles) more explicitly than some other OpenAI adoption posts in the
  corpus, but does not disclose sample selection criteria, the specific
  occupation taxonomy used, or classifier validation.
- **Scope**: Covers "work-related" messages from U.S. ChatGPT users only —
  the post does not state whether this includes Enterprise/Team/API usage
  or is restricted to Individual-plan usage (contrast with
  `blog-openai-chatgpt-adoption-signals.md`, which explicitly scopes
  itself to Individual plans only). Covers seven named occupation groups
  (customer experience, design, engineering, finance, human resources,
  legal, marketing, sales) and their cross-occupation task-sharing
  patterns, plus a company-size breakdown. Does NOT cover: task quality or
  success rates, whether crossover work is done well or poorly, job-title
  or employment-outcome data, non-U.S. usage, or Codex/agentic (vs.
  chatbot) usage specifically.

## Extracted Claims

### Claim 1: 16.8% of work-related ChatGPT messages and 43.5% of occupation-specific messages concern tasks associated with an occupation other than the user's own
- **Evidence**: Analysis of more than 800,000 work-related messages from
  U.S. ChatGPT users, classifying each message as generic (shared broadly
  across occupations, e.g., writing, summarizing, scheduling) or
  occupation-specific, then checking whether occupation-specific messages
  fall inside or outside the user's own occupation.
- **Confidence**: emerging (a large, specific, disclosed-methodology
  statistic, but the underlying occupation-inference and task-classification
  methods are not detailed in the post, and the figures are unaudited
  first-party telemetry)
- **Quote**: "AI changes the work that people do. In an analysis of more than 800,000 messages from U.S. ChatGPT users, our new research suggests that 16.8% of work-related messages and 43.5% of occupation-specific messages are about tasks associated with another occupation."
- **Our assessment**: This is the report's headline statistic and the
  origin of the "task crossover" term used throughout the rest of the
  post. The two-number framing matters: 16.8% is the share across *all*
  work-related messages (including generic ones), while 43.5% is the
  share once generic messages are excluded — the much larger 43.5%
  figure is the more meaningful one for arguing that occupation-specific
  AI use is nearly a coin flip between "your own job's tasks" and
  "someone else's job's tasks," and later claims/quotes in the post
  consistently use this excluded-generic denominator.

### Claim 2: AI is changing not just how work gets done, but who does it — illustrated by a small-business owner drafting copy and reviewing contracts, a salesperson analyzing customer data, and a marketer troubleshooting a website
- **Evidence**: Illustrative examples given in the post's opening framing,
  not a measured statistic.
- **Confidence**: anecdotal (illustrative examples, not sourced to
  specific named users or case studies)
- **Quote**: "A small-business owner can independently draft copy, review a contract, or perform basic financial analysis. A salesperson can use AI to explore a customer dataset that might once have gone to an analyst. A marketer can troubleshoot a website without waiting for a developer. In each case, AI changes not just how work gets done, but who does what."
- **Our assessment**: These are unsourced illustrative vignettes, not
  case studies with named individuals or companies (contrast with
  `blog-openai-codex-knowledge-work.md` Claims 8-11, which name specific
  companies and people). Useful only as framing color for the
  quantitative claims that follow, not as independent evidence.

### Claim 3: Task crossover is highly uneven across occupations — once generic work is excluded, outside-occupation tasks account for 77% of occupation-specific messages from customer experience workers, 75% from designers, 69% from HR workers, 56% from legal workers, and 53% from marketers
- **Evidence**: Per-occupation breakdown of the same message-classification
  methodology used for Claim 1, applied separately to each of five named
  occupation groups.
- **Confidence**: emerging (specific, per-occupation percentages, but same
  undisclosed-methodology caveat as Claim 1)
- **Quote**: "Once generic work is excluded, outside-occupation tasks account for: 77% of occupation-specific messages from customer experience workers[,] 75% from designers[,] 69% from human resources workers[,] 56% from legal workers[,] 53% from marketers"
- **Our assessment**: The magnitude here is striking — for customer
  experience workers, more than three-quarters of their occupation-specific
  AI use is nominally "someone else's job." The post frames this as these
  occupations "borrowing" tasks from other roles, but an equally valid
  reading is that the occupation-classification taxonomy itself may not
  match how these particular roles are actually structured day-to-day
  (i.e., a "customer experience" job may already routinely include tasks
  the classifier labels as belonging to other occupations). The post does
  not address this alternative explanation.

### Claim 4: Marketing and engineering tasks travel farthest across occupations; financial calculation and technology troubleshooting each appear among the three most common outside tasks in all seven other occupation groups studied
- **Evidence**: A task-crossover heatmap (values not recoverable from the
  fetched text — see Extraction Notes) plus the post's own prose summary
  of which task types appear most broadly outside their "home" occupation.
- **Confidence**: anecdotal for the heatmap itself (data not recoverable),
  emerging for the prose-stated finding about financial calculation and
  tech troubleshooting specifically
- **Quote**: "Financial calculation and technology troubleshooting each appear among the three most common outside tasks in all seven other occupation groups in the analysis. Marketing work also travels broadly: creating marketing materials appears across five other groups and is especially prominent among design users."
- **Our assessment**: This is the most concrete "which specific tasks
  cross occupational lines" finding in the post — financial calculation
  and tech troubleshooting are apparently near-universal secondary skills
  that AI now lets any occupation pick up. As with Claim 3's heatmap, the
  underlying cell values were not recoverable from the reader-proxy text
  extraction, so only the prose-stated top-line finding is captured here.

### Claim 5: Design absorbs many outside-occupation tasks (35.2% of designer messages) but rarely exports design work to other occupations (1.7% of other occupations' messages); engineering shows the reverse pattern (18.5% inbound, but engineering accounts for 7.4% of messages from other occupations)
- **Evidence**: Per-occupation inbound/outbound task-share breakdown from
  the same classification methodology.
- **Confidence**: emerging (specific, paired inbound/outbound percentages
  for two named occupations)
- **Quote**: "About 35.2% of messages from designers involve work usually associated with another occupation, while design tasks account for only 1.7% of messages from workers in other fields. Designers draw heavily on outside tasks, but design work itself rarely appears elsewhere. [...] Only 18.5% of engineering messages involve tasks from other fields, but engineering tasks account for 7.4% of messages among workers in other occupations. Engineering is an important source of work that people elsewhere take on, from troubleshooting software to working with technical systems."
- **Our assessment**: This inbound/outbound asymmetry is the report's
  most analytically interesting finding — it distinguishes occupations
  that are net *importers* of outside tasks (design) from occupations
  that are net *exporters* of tasks other people pick up (engineering).
  The engineering-as-exporter finding directly corroborates
  `blog-openai-agents-transforming-work.md` Claim 8 (over one-fourth of
  Codex work done by business-function workers is engineering or coding)
  and `blog-openai-codex-knowledge-work.md` Claim 5 (46% of knowledge
  workers do "code implementation" work weekly) — three independent
  OpenAI analyses, using different products (ChatGPT here vs. Codex in
  the other two) and different time windows, all converge on "engineering
  work leaks into non-engineering roles at a meaningful rate." The 7.4%
  figure here is notably smaller than the Codex-specific ">25%" figure in
  `blog-openai-agents-transforming-work.md` Claim 8, which makes sense
  given Codex is a coding-specific agentic tool and this post measures
  general ChatGPT usage across all task types — the two numbers describe
  the same directional phenomenon at different product-specific
  intensities and should not be conflated as the same statistic.

### Claim 6: Marketing shows bidirectional crossover — marketers spend 24.3% of their messages on outside-occupation tasks, while marketing tasks account for 8.9% of messages from other occupations, the highest outward share of any occupation in the sample
- **Evidence**: Same per-occupation inbound/outbound methodology as
  Claim 5, applied to marketing.
- **Confidence**: emerging (specific paired percentages, with an explicit
  "highest in sample" superlative claim)
- **Quote**: "Marketers devote 24.3% of their messages to tasks associated with other occupations, while marketing tasks account for 8.9% of messages among workers in other fields—the highest outward share in the sample. Marketing workers combine tasks from multiple domains, and marketing work also spreads widely across the organization."
- **Our assessment**: Marketing is positioned as the occupation with the
  most "traffic" in both directions — it both borrows the most (after
  customer experience, design, and HR per Claim 3) and lends out the
  most (more than engineering's 7.4%, per Claim 5). This makes marketing
  the report's clearest example of an occupation becoming a general
  cross-functional connector rather than a specialist silo, though the
  post gives no explanation for why marketing specifically occupies this
  position.

### Claim 7: Task crossover is higher in smaller organizations — outside-occupation task share among average users falls from 18.9% in workspaces with 2-5 seats to 16.3% in workspaces with more than 100 seats, though this pattern does not hold among the heaviest users
- **Evidence**: A company-size breakdown of the outside-occupation task
  share, split between "average users" and "heaviest users" cohorts.
- **Confidence**: emerging (specific percentages tied to named seat-count
  bands, with an explicit caveat that the pattern doesn't replicate for
  heavy users)
- **Quote**: "Among average users, the outside-occupation task share falls from 18.9% for users in workspaces with 2–5 seats to 16.3% for users in workspaces with over 100 seats. Among the heaviest users, we do not see the same monotonic pattern."
- **Our assessment**: The explicit non-replication among heavy users is a
  notable, easy-to-overlook honesty signal — the post could have
  presented only the average-user finding, but instead flags that its
  own pattern breaks down for the sub-population arguably most relevant
  to understanding sustained behavior change. The post's own explanation
  (quoted in Claim 8) is speculative and not tested against the heavy-user
  data.

### Claim 8: Smaller organizations show more task crossover because "the worker closest to the problem is more likely to take on the problem rather than delegate," and AI may function as a generalist tool where specialist resources are scarce
- **Evidence**: The post's own interpretive explanation for the Claim 7
  finding, not itself a separately measured result.
- **Confidence**: anecdotal (an unsourced interpretive claim offered to
  explain a measured pattern, not itself tested)
- **Quote**: "In a large company, employees may have access to specialized teams, established workflows, and internal services. In a smaller organization, the worker closest to the problem is more likely to take on the problem rather than delegate."
- **Additional quote (pull-quote elsewhere on the page)**: "AI may be especially useful as a generalist tool where specialist resources are scarce."
- **Our assessment**: A plausible mechanism (small companies lack
  specialist headcount to delegate to, so the same worker uses AI to
  cover more ground) but not independently verified against, say,
  headcount-per-specialist-function data — it is offered as narrative
  explanation for a real, measured pattern (Claim 7), not itself a
  separately evidenced claim.

### Claim 9: Task crossover and AI usage patterns can serve as an early signal of occupational change, visible in usage data before conventional labor-market statistics or job descriptions catch up
- **Evidence**: The post's closing interpretive framing, tying the
  quantitative findings to a broader claim about the value of usage-data
  analysis for labor-market observation.
- **Confidence**: anecdotal (a framing/thesis claim about the value of the
  data source itself, not a separately measured finding)
- **Quote**: "AI usage data like this is an indicator of where work is shifting. It allows us to see how AI lets workers experiment with new combinations of activities before firms rewrite job descriptions or create new job titles. In that sense, usage patterns may provide an early signal of occupational change that conventional labor-market statistics will capture only later."
- **Our assessment**: This is OpenAI positioning itself (via its access to
  ChatGPT usage logs) as a source of leading-indicator labor-market data,
  ahead of government or survey-based labor statistics — a self-interested
  but not obviously false claim, since usage logs genuinely do update
  faster than annual/quarterly labor surveys. No comparison to any actual
  lagging labor-market statistic is given to substantiate the "early
  signal" framing empirically.

### Claim 10: This report is the first in a new recurring OpenAI series, "Work at the Frontier," intended to provide regular data-driven insights into how AI is changing work, and separately references a companion report, the "AI Jobs Transition Framework," arguing that many jobs are likely to reorganize because their day-to-day tasks could change substantially
- **Evidence**: The post's own framing statement about its series and its
  citation of a separate, linked companion report.
- **Confidence**: settled (a direct, unambiguous self-description by the
  source; the "AI Jobs Transition Framework" is confirmed as a distinct
  linked PDF, not merely referenced by name)
- **Quote**: "Our new report, _Work at the Frontier: How AI is Expanding What People Do at Work_, studies this shift. [...] In our _AI Jobs Transition Framework_, we argue that many jobs are likely to reorganize: these are jobs whose day-to-day tasks could change substantially. This report is the first in our new _Work at the Frontier_ series, which explores how AI is changing work in real time."
- **Our assessment**: This confirms the task-crossover report is meant to
  be read as evidence *for* the separate AI Jobs Transition Framework's
  "jobs will reorganize" thesis, rather than as a standalone finding —
  the two are companion pieces from the same research effort. The AI
  Jobs Transition Framework PDF itself
  (`cdn.openai.com/pdf/the-ai-jobs-transition-framework_report.pdf`) was
  not fetched or extracted for this note; a future source-note extraction
  of that PDF directly would be a natural follow-up, since it appears to
  contain the underlying occupational-reorganization framework this post
  only summarizes.

## Concrete Artifacts

```
Source: OpenAI, "How AI is Expanding What People Do at Work,"
https://openai.com/index/how-ai-is-expanding-what-people-do-at-work
(published per RSS feed metadata: Mon, 27 Jul 2026)

Headline task-crossover statistics (800,000+ work-related U.S. ChatGPT
messages):
  All work-related messages, outside-occupation share:        16.8%
  Occupation-specific messages only, outside-occupation share: 43.5%

Outside-occupation task share by occupation (occupation-specific
messages only):
  Customer experience:  77%
  Design:                75%
  Human resources:       69%
  Legal:                 56%
  Marketing:              53%

Inbound vs. outbound task-crossover share by occupation:
  Design:      35.2% inbound (outside tasks in designer messages)
                1.7% outbound (design tasks in other occupations' messages)
  Engineering: 18.5% inbound
                7.4% outbound
  Marketing:   24.3% inbound
                8.9% outbound (highest outbound share in the sample)

Cross-occupation "universal" outside tasks:
  Financial calculation and technology troubleshooting — among the top 3
  outside tasks in all 7 other occupation groups studied
  Creating marketing materials — appears across 5 other occupation groups

Company-size effect (average users, outside-occupation task share):
  2-5 seat workspaces:    18.9%
  100+ seat workspaces:   16.3%
  (Pattern does not replicate among heaviest users)

Occupation groups studied (7 named + generic tasks excluded from
occupation-specific analysis): customer experience, design, engineering,
finance, human resources, legal, marketing, sales
```

## Cross-References

### Cross-reference verification notes
`blog-openai-agents-transforming-work.md`, `blog-openai-codex-knowledge-work.md`,
and `blog-openai-chatgpt-adoption-signals.md` were re-read directly
(MINER.md §4b) and the claim numbers cited above were confirmed against
each note's numbered `### Claim N:` headings in document order before
writing this section.

- **Corroborates**:
  - `blog-openai-agents-transforming-work.md` Claim 8 (over one-fourth of
    business-function Codex work is engineering or coding — "Agents can
    lower the cost of moving across task boundaries") and
    `blog-openai-codex-knowledge-work.md` Claim 5 (72% of knowledge
    workers produce artifacts weekly; 46% do code implementation,
    "indicating the boundary between 'developer' and 'knowledge worker'
    tasks has blurred"): this note's Claim 5 (engineering tasks account
    for 7.4% of messages from other occupations) is a third, independent
    OpenAI measurement of the same underlying phenomenon — technical work
    leaking into non-technical roles — using general ChatGPT usage rather
    than Codex-specific usage. Three OpenAI analyses of two different
    products, all converging on the same directional finding, is a
    meaningfully stronger corroboration chain than any single post alone.
  - `blog-openai-codex-knowledge-work.md` Claim 2 (knowledge workers
    adopting Codex "more than 3 times as fast as developers") and
    `blog-openai-agents-transforming-work.md` Claim 7 (non-developer
    Codex growth of 137x/189x/12x across user populations): both describe
    non-technical roles rapidly picking up technical-tool usage: this
    note's overall "task crossover" framing gives that same phenomenon a
    general, product-agnostic name and a general-ChatGPT-usage baseline
    rate (43.5% of occupation-specific messages), rather than a
    Codex-specific adoption-growth number.

- **Contradicts**: None identified. No existing source note makes a
  claim about per-occupation task-crossover rates that this post's
  figures conflict with.

- **Extends**: `blog-openai-chatgpt-adoption-signals.md`, which explicitly
  scopes itself to Individual ChatGPT plans and explicitly states it does
  NOT cover "task-category breakdowns" (that note's Claim 7 and its
  Cross-References section flag this as an intentional scope boundary).
  This report fills exactly the gap that note left open — a task-category,
  cross-occupation breakdown of ChatGPT usage — though this post does not
  itself state whether its "work-related U.S. ChatGPT users" population is
  restricted to Individual plans, spans Enterprise/Team/API usage, or some
  mix; unlike the adoption-signals note, this post gives no explicit
  population-scope disclosure, which should be flagged as an open question
  rather than assumed to match the adoption-signals note's Individual-only
  scope.

- **Novel**:
  - **"Task crossover" as a named, measured metric** (Claim 1) — the
    first source in our corpus to name and quantify how often a worker's
    AI-assisted tasks belong to a different occupation than their own,
    distinct from the corpus's existing developer-vs-knowledge-worker
    adoption-rate framing (which measures *who adopts a tool*, not *whose
    job's tasks a person is doing*).
  - **Per-occupation inbound/outbound task-crossover asymmetry** (Claims
    3, 5, 6) — the first source to distinguish occupations that
    net-import outside tasks (design, customer experience, HR) from
    occupations that net-export tasks other people pick up (engineering,
    and to a lesser extent marketing).
  - **Company-size effect on task crossover** (Claims 7-8) — the first
    source in our corpus tying organizational size specifically to how
    much AI-enabled role-boundary-crossing occurs, as distinct from the
    existing corpus's company-size discussions (which focus on cost
    governance and infrastructure, e.g., the OpenAI investment-management
    post, not task-boundary crossing).

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add Claim 3 (per-occupation
  outside-task shares, especially customer experience at 77% and design
  at 75%) and Claim 7-8 (smaller organizations show more task crossover,
  "the worker closest to the problem is more likely to take on the
  problem rather than delegate") as evidence for a section on how AI
  changes role boundaries within a team or company, particularly for
  smaller engineering organizations where individual contributors are
  already expected to cover more functional ground. Pair with
  `blog-openai-agents-transforming-work.md` Claim 8 and
  `blog-openai-codex-knowledge-work.md` Claim 5 as three independent,
  converging OpenAI data points on technical-work crossover into
  non-technical roles, while flagging that none of the three discloses
  its occupation-classification or task-labeling methodology in enough
  detail for the guide to treat the specific percentages as precise
  benchmarks.
- **Chapter 02 (Harness Engineering)**: Claim 5's finding that engineering
  work is a significant net *exporter* of tasks to other occupations
  (7.4% of other occupations' messages, and the largest source of
  cross-occupation "technology troubleshooting" per Claim 4) reinforces
  the existing guide point (already sourced from
  `blog-openai-agents-transforming-work.md` Claim 8) that harnesses
  should not assume a hard boundary between "developer" and
  "non-developer" users — a growing share of the people running
  engineering-adjacent tasks through AI are not engineers by job title.
- **No chapter should cite the per-occupation or per-company-size
  percentages in this note as precise, reproducible benchmarks.** They
  are unaudited first-party classifier output over an undisclosed sample,
  with no confidence intervals, classifier-accuracy figures, or published
  occupation taxonomy — use them as directional evidence of a real and
  substantial task-crossover phenomenon, not as numbers a reader's own
  organization should expect to replicate.

## Extraction Notes

1. **The live OpenAI URL returned HTTP 403** to both `WebFetch` directly
   and a `curl` fetch with a browser user-agent from Bash (a Cloudflare
   bot-challenge page was returned by `curl`, matching the
   `cf-mitigated: challenge` pattern already documented in
   `blog-openai-agents-transforming-work.md` and
   `blog-openai-managing-ai-investments-agentic-era.md` for other
   `openai.com/index/` posts). The Wayback Machine was not reachable from
   this environment (`web.archive.org` fetches are blocked entirely, not
   just rate-limited). The article was retrieved via the `r.jina.ai`
   reader proxy through `WebFetch`. An initial pass, prompted to
   "extract" the content, returned a visibly restructured summary with
   invented section headings ("Key Statistics," "Core Concept") that do
   not appear on the source page — this was discarded per MINER.md §2a.
   A second pass, explicitly prompted to reproduce the raw page content
   verbatim without summarizing, returned the full article text
   including every paragraph, heading, and bullet list; every `Quote`
   field above was checked against that second, verbatim-reproduction
   fetch. A third, targeted fetch was used to check for a byline,
   publication date, pull-quotes, and linked-report details not covered
   by the first verbatim pass.
2. **No byline or on-page publication date was recoverable** from the
   fetched content — the `date_published` field above (2026-07-27) comes
   from the RSS feed metadata already present in this issue's body
   ("Published: Mon, 27 Jul 2026 03:30:00 GMT," from the `openai-news`
   trusted feed), not from the article page itself.
3. **The task-crossover heatmap's underlying cell values were not
   recoverable** from the reader-proxy text extraction — it rendered as
   an empty table skeleton with row/column labels (the seven occupations)
   but no populated data cells, the same limitation documented for
   embedded charts in `blog-openai-agents-transforming-work.md`
   (Claim 9) and `blog-openai-chatgpt-adoption-signals.md`. Claim 4 above
   is therefore drawn from the post's own prose description of the
   heatmap's findings (which occupation groups the top outside-tasks
   appear in), not the heatmap's actual per-cell values.
4. **The companion "AI Jobs Transition Framework" PDF was not fetched.**
   The post links to it (`cdn.openai.com/pdf/the-ai-jobs-transition-framework_report.pdf`)
   as a separate report this post's findings are meant to support, but
   extracting that PDF's own content was out of scope for this note — see
   Claim 10's "Our assessment" for why a future extraction of that PDF is
   recommended as a follow-up source.
5. **No contradiction with any existing source note was found** during
   cross-referencing (see Cross-References → Contradicts), so no
   contradiction issue was filed per MINER.md §4a.
6. **Population scope is genuinely ambiguous in the source itself** — the
   post says "U.S. ChatGPT users" and "work-related messages" without
   stating whether this spans Individual, Team, Enterprise, and API
   usage, or is restricted like the adoption-signals post to Individual
   plans only. This ambiguity is flagged explicitly in Cross-References →
   Extends rather than silently assumed one way or the other.
