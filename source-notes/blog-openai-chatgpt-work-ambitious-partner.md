---
source_url: https://openai.com/index/chatgpt-for-your-most-ambitious-work
source_type: blog-post
title: "ChatGPT is now a partner for your most ambitious work"
author: OpenAI
date_published: 2026-07-09
date_extracted: 2026-07-26
last_checked: 2026-07-26
status: current
confidence_overall: emerging
issue: "#2244"
---

# ChatGPT is now a partner for your most ambitious work

> OpenAI's launch post for "ChatGPT Work," a new agent mode built on Codex
> technology and the newly-released GPT‑5.6 model that can gather
> information across a user's connected apps, stay with a project for
> hours by breaking it into steps, and produce finished artifacts (docs,
> slides, sheets, and interactive "Sites"). The post also announces the
> Codex desktop app merging into a unified ChatGPT desktop app (with a
> built-in browser and Computer Use), the sunsetting of the standalone
> Atlas browser, and four named enterprise customer testimonials
> (Zapier, RingCentral, Virgin Atlantic, NVIDIA) alongside two internal
> OpenAI adoption anecdotes (sales, finance).

## Source Context

- **Type**: blog-post (OpenAI "Product" news vertical, `openai.com/index/`,
  published July 9, 2026; a full product-launch page, not a short
  announcement — includes a customer-testimonial carousel, a "From goals
  to real outcomes across every team" tabbed section (Sales / Marketing /
  Finance / Business Operations / Data Analytics / Engineering), a
  dedicated security/governance section, and a pricing/availability
  section).
- **Author credibility**: House-authored OpenAI product announcement, no
  named individual author. Contains four named external customer quotes
  (Angela Ferrante, Zapier; Vaneet Seth, RingCentral; Nathan Bolt, Virgin
  Atlantic; Will Daney, NVIDIA) attributed by name and title, plus two
  unattributed internal-OpenAI anecdotes (sales, finance) with no named
  individual. This is first-party vendor marketing copy for a new paid
  product tier — every customer quote is OpenAI-selected and
  OpenAI-published, with no independent verification of the outcomes
  described. Standard vendor-launch-post credibility caveats apply
  throughout.
- **Scope**: Covers the ChatGPT Work product launch (what it is, how it's
  powered, how to use it), four named external customer testimonials with
  specific claimed outcomes, two internal-OpenAI adoption anecdotes, the
  Codex/ChatGPT desktop-app merger and Atlas browser sunset, a new "Sites"
  public-beta feature, Scheduled Tasks and Computer Use capabilities,
  security/governance controls (Compliance API, Auto-review, admin spend
  controls), and rollout/pricing/availability. Does NOT cover: any
  quantified success/failure rate for ChatGPT Work tasks, pricing dollar
  figures (usage-based, tied to Codex's existing usage structure but no
  numbers given), a technical description of how GPT‑5.6 differs from
  prior models, or methodology for any of the customer-testimonial claims
  (e.g., how "seven figures in potential sales" was calculated for
  Zapier).

## Extracted Claims

### Claim 1: ChatGPT Work is a new agent mode that gathers information across a user's connected apps and workflows, produces finished materials (slides, sheets, docs, Sites), and can stay with complex, multi-hour projects by breaking them into smaller steps and completing them independently
- **Evidence**: Product description in the post's opening framing paragraph.
- **Confidence**: emerging (a specific, checkable product-capability claim,
  though "stay with complex projects for hours" and "completing them
  independently" are not quantified or demonstrated with a worked example
  in the post itself)
- **Quote**: "Introducing ChatGPT Work, an agent in ChatGPT that helps you take on more ambitious tasks. It can gather information across your apps and workflows to create finished materials like sheets, slides, docs, and web apps, and stay with complex projects for hours by breaking them into smaller steps and completing them independently."
- **Our assessment**: This is the post's core product claim and reads as a
  direct extension of the "unit of knowledge work" thesis already
  documented from OpenAI in `blog-openai-agents-transforming-work.md`
  Claim 1 (agentic AI shifts work from short chatbot interactions to
  delegated, long-horizon tasks) — ChatGPT Work is that thesis turned into
  a shipped consumer/enterprise product surface rather than an internal
  usage pattern. No task-success-rate or failure-mode data accompanies the
  claim.

### Claim 2: More than 5 million people use Codex every week, and more than 1 million of them now use it for work outside software development
- **Evidence**: OpenAI's own stated usage figures in the post's second
  paragraph.
- **Confidence**: emerging (specific, falsifiable absolute numbers; the
  5-million-weekly-users figure exactly matches the figure already in the
  corpus from six weeks earlier, and the >1-million-non-developer figure is
  a new absolute count where the prior source gave only a percentage)
- **Quote**: "More than 5 million people use Codex every week. Although it began as a coding agent for developers, more than 1 million people now use it for work outside software development, showing how its capabilities can support a wider range of tasks."
- **Our assessment**: The 5M weekly-user figure is an exact restatement of
  `blog-openai-codex-knowledge-work.md` Claim 1 ("Codex now has more than
  5 million weekly active users"), five weeks after that report's June 2,
  2026 publication, with no growth delta given — either the figure is
  stale/reused marketing copy, or weekly-user growth has plateaued at
  "more than 5 million" in OpenAI's public messaging (the post gives no
  way to distinguish these). The >1M-non-developer figure is new and more
  concrete than the earlier post's "20% of users are knowledge workers"
  framing (`blog-openai-codex-knowledge-work.md` Claim 2) — if 20% of "more
  than 5 million" were the basis, that would be roughly 1M, so the two
  figures are numerically consistent with each other, suggesting the >1M
  count in this post is likely a restatement of the same underlying share
  rather than independent new growth.

### Claim 3: ChatGPT Work is powered by GPT‑5.6, described as OpenAI's latest frontier model and "state of the art at reasoning through multi-step tasks and creating materials that follow your templates and reference files," rolling out the same day as this post
- **Evidence**: Direct product-positioning statement naming the underlying
  model.
- **Confidence**: emerging (a specific, dated model-release claim; the
  "state of the art" superlative is OpenAI's own unaudited claim)
- **Quote**: "To better manage these tasks, ChatGPT Work is powered by our latest frontier model, GPT‑5.6, which is also rolling out today. GPT‑5.6 makes ChatGPT state of the art at reasoning through multi-step tasks and creating materials that follow your templates and reference files."
- **Our assessment**: This confirms the same GPT‑5.6 GA release date (July
  9, 2026) already documented independently in
  `blog-simonwillison-gpt56-ga-launch.md`, corroborating that date from the
  vendor's own announcement rather than only a third-party writeup. The
  "follow your templates and reference files" framing is new
  product-specific detail not present in Willison's more benchmark-focused
  coverage.

### Claim 4: Customer testimonial — Zapier's Head of Enterprise Marketing used ChatGPT Work to build a repeatable lead-review system that traced customer touchpoints across CRM, email, and other tools, producing a weekly executive dashboard that "revealed seven figures in potential sales"
- **Evidence**: Named customer testimonial (Angela Ferrante, Head of
  Enterprise Marketing at Zapier), presented in a testimonial carousel.
- **Confidence**: anecdotal (single named individual, vendor-selected and
  vendor-published testimonial; "seven figures in potential sales" is not
  defined — unclear if this means identified pipeline, closed revenue, or
  an estimate, and no measurement methodology is given)
- **Quote**: "Used ChatGPT Work to build a repeatable system for reviewing thousands of leads each month. It traced customer touchpoints across Zapier's CRM, email, and other tools, found where follow-ups broke down, and generated a weekly executive dashboard that highlighted missed pipeline and revealed seven figures in potential sales."
- **Our assessment**: Concrete and specific (named company, named role,
  named mechanism: cross-tool touchpoint tracing plus a recurring
  dashboard), but a single hand-picked customer story with an ambiguous
  headline number, in the same genre as the Notion, GroundVue, and Proaction
  vignettes already in the corpus (`blog-openai-notion-codex-case-study.md`,
  `blog-openai-codex-knowledge-work.md` Claims 8-9). Novel to the corpus:
  first Zapier-specific case study.

### Claim 5: Customer testimonial — RingCentral's R&D Efficiency Manager used ChatGPT Work to turn manual monthly launch checks into a repeatable workflow that flags missing steps, blockers, and unclear ownership across release plans, Jira tasks, and go-to-market schedules, letting him scale from supporting one product manager to supporting roughly 50
- **Evidence**: Named customer testimonial (Vaneet Seth, R&D Efficiency
  Manager at RingCentral).
- **Confidence**: anecdotal (single named individual, vendor-selected
  testimonial; the "one → roughly 50 product managers" figure is a
  striking specific ratio but self-reported with no supporting detail on
  role scope or hours worked)
- **Quote**: "Used ChatGPT Work to turn manual monthly launch checks into a repeatable workflow. It reviewed release plans, Jira tasks, and go-to-market schedules, flagged missing steps, blockers, and unclear ownership, and produced source-backed reports naming owners and next steps, allowing him to go from supporting one product manager to supporting roughly 50 product managers."
- **Our assessment**: The "1 → 50" scaling ratio is the most dramatic
  individual-productivity claim in the post and would be a strong data
  point for a Ch01/Ch05 "force multiplier" discussion if independently
  corroborated — but it is a single self-reported claim with no detail on
  what "supporting" a product manager entails before vs. after, so treat
  as illustrative anecdote only, not a benchmarkable multiplier.

### Claim 6: Customer testimonial — Virgin Atlantic's Head of Digital Products used ChatGPT Work to research and compare the airline's passenger experience against competitors for a five-year plan, reducing "weeks of analysis to hours"
- **Evidence**: Named customer testimonial (Nathan Bolt, Head of Digital
  Products at Virgin Atlantic).
- **Confidence**: anecdotal (single named individual, vendor-selected
  testimonial; "weeks of analysis to hours" is a self-reported estimate
  with no baseline definition of what the prior manual process entailed)
- **Quote**: "Used ChatGPT Work to compare the airline's passenger experience with competitors as the airline developed its five-year plan. He gave ChatGPT a customer journey to evaluate and a list of competing airlines, then asked it to research what each airline offered, assess where Virgin led or lagged, and build a dataset his team could review and refine—reducing weeks of analysis to hours and helping the team decide where to invest over the next five years."
- **Our assessment**: A clean example of agent-driven competitive research
  compressing a multi-week analyst task into hours, structurally similar
  to `blog-openai-codex-knowledge-work.md` Claim 8 (GroundVue: "tasks that
  once took days or weeks now take minutes") — both are OpenAI-selected
  "days/weeks → hours/minutes" testimonials with no independent time
  measurement. Treat the pattern (not the specific ratio) as the
  repeatable signal: multiple independent OpenAI case studies converge on
  "long-horizon research/analysis tasks compress dramatically," which is
  worth noting as a recurring vendor narrative even though no single
  instance is independently verifiable.

### Claim 7: Customer testimonial — NVIDIA's Go-to-Market Manager used ChatGPT Work to automate GTC conference preparation, replacing an Excel-based workflow that previously consumed about 40% of his pre-event time, and to synthesize hundreds of post-event session transcripts and customer-meeting notes so the team's two-week review could focus on discussing findings rather than assembling data
- **Evidence**: Named customer testimonial (Will Daney, Go-to-Market
  Manager at NVIDIA).
- **Confidence**: anecdotal (single named individual, vendor-selected
  testimonial; the "~40% of pre-event time" figure is a specific,
  quantified self-estimate, more concrete than Claims 4-6's vaguer
  time-savings language)
- **Quote**: "Used ChatGPT Work to automate preparation for GTC (NVIDIA's global conference), replacing an Excel workflow that consumed about 40% of his pre-event time. ChatGPT tracked which customer accounts had registered, what meetings were planned, and how field sales teams were preparing; afterward, it synthesized hundreds of session transcripts and customer-meeting notes to assess whether GTC met its goals, allowing the team to spend its two-week review discussing the findings instead of assembling the data."
- **Our assessment**: The most operationally specific of the four
  testimonials — it names the artifact being replaced (an Excel workflow),
  a quantified time-share (~40% of pre-event time), and a before/after
  description of what a fixed two-week review period is now spent doing
  (discussing findings vs. assembling data). Still a single self-reported,
  vendor-selected account, but the "same time budget, different activity
  mix" framing is a more falsifiable claim shape than a raw multiplier.

### Claim 8: Nearly 100% of teams inside OpenAI, including non-technical departments like Finance and Sales, now use ChatGPT Work and Codex; internally, ChatGPT Work compressed a sales discovery-to-proof-of-concept process from weeks to 24 hours, and reduced finance's month-end close and forecasting from days to hours
- **Evidence**: Two unattributed internal-OpenAI anecdotes (sales,
  finance), plus a company-wide adoption superlative.
- **Confidence**: anecdotal for the two workflow anecdotes (no named
  individual, no measurement methodology); the "nearly 100% of teams"
  figure is emerging (a specific, if unaudited, internal-adoption
  superlative consistent with prior OpenAI internal-telemetry claims)
- **Quote**: "Nearly 100% of teams inside OpenAI, including finance and sales, now use ChatGPT Work and Codex to move faster, take on harder tasks, and spend more time with customers." ... "In sales, ChatGPT Work turned a discovery conversation into a tailored proof of concept for a mission-critical problem within 24 hours—a process that normally takes weeks." ... "In finance, ChatGPT Work reduced month-end close and forecasting from days to hours by helping teams find source data, move it into Excel or Sheets, reconcile it, create slides, and verify the results."
- **Our assessment**: The "nearly 100% of teams" figure directly
  corroborates and updates `blog-openai-agents-transforming-work.md`
  Claim 2 (Codex reached 99.8% of weekly company-wide output tokens at
  OpenAI as of ~June 25, 2026) and Claim 5 (every department had crossed
  over to majority-Codex usage by ~April 2026) — this post, two weeks
  later, restates the same near-total internal-adoption picture in
  qualitative "nearly 100% of teams" language rather than the earlier
  post's precise token-share percentage. The sales (weeks→24 hours) and
  finance (days→hours) anecdotes are new, specific internal-workflow
  detail not present in the June 25 post, which reported adoption
  percentages and growth multipliers but no internal workflow narratives.

### Claim 9: The standalone Codex desktop app is merging into a new unified ChatGPT desktop app (Chat, Work, and Codex modes, available on every plan including Free), and OpenAI will begin sunsetting the standalone Atlas browser, migrating its users to ChatGPT
- **Evidence**: Direct product-restructuring announcement.
- **Confidence**: settled (an unambiguous, dated product-discontinuation
  and consolidation announcement from the vendor itself)
- **Quote**: "Starting today, the Codex app is merging with the new ChatGPT desktop app." ... "We'll begin sunsetting the standalone Atlas browser, and will share information with users about how to transition to ChatGPT." ... "In the ChatGPT desktop app, Chat, Work, and Codex are available on every plan, including Free."
- **Our assessment**: This is a concrete, checkable product-lifecycle
  event — the guide's corpus should treat any prior reference to "the
  Atlas browser" as describing a product being wound down as of this post
  (July 9, 2026), and any reference to "the Codex desktop app" as
  describing a product being folded into the unified ChatGPT desktop app
  going forward. Existing Codex-app references elsewhere in the corpus
  predate this consolidation and should be read as describing the
  pre-merger standalone app.

### Claim 10: ChatGPT Work introduces "Sites," a public-beta feature letting users turn work or ideas into an interactive site or web app, testable inside ChatGPT and shareable via URL, with OpenAI able to update the Site automatically as underlying information changes
- **Evidence**: Direct feature description in the "Create slides, sheets,
  docs, and Sites" section.
- **Confidence**: emerging (a specific, named, dated feature launch; no
  usage data since it launched the same day as the post)
- **Quote**: "We're also introducing Sites in ChatGPT in public beta. With Sites, you can turn your work or ideas into an interactive site or web app and share it with your team or publicly through a URL. Sites are useful when you want to create things like live dashboards, project trackers, launch calendars, prototypes, internal portals, and interactive reports. You can test the Sites you build right inside ChatGPT and bring fresh web context into your project, too. ChatGPT can also update them as the underlying information changes."
- **Our assessment**: Novel to the corpus — no existing OpenAI source note
  documents a "publish a live, auto-updating web app directly from a chat
  agent" feature. This is architecturally adjacent to Claude's Artifacts
  and to `blog-anthropic-claude-managed-agents.md`-style hosted-agent
  output, but the "auto-updates as underlying information changes"
  behavior (implying a persistent, agent-maintained live site rather than
  a static generated artifact) is a distinct capability worth flagging for
  a future comparison if a Claude-side equivalent is mined.

### Claim 11: Scheduled Tasks let ChatGPT Work perform an action once, repeat it on a schedule, or monitor for changes and trigger on an event, using connected apps and the built-in browser — named examples include weekly Slack-update summarization into a recurring meeting agenda, daily dashboard-change monitoring and reporting, and updating a presentation when new feedback arrives by email
- **Evidence**: Direct feature description with four named example use
  cases, in the "Delegate repetitive tasks" section.
- **Confidence**: emerging (a specific, named feature with concrete
  example use cases, but no usage or reliability data)
- **Quote**: "Scheduled Tasks let you ask ChatGPT to perform an action once, repeat it on a schedule or when an event occurs, or monitor for changes over time." ... "Review new Slack updates each week and refresh a recurring meeting agenda. Check websites and dashboards each morning, summarize what changed, and send a report. Monitor new customer feedback and turn recurring themes into prioritized product ideas. Update a presentation when new feedback arrives by email."
- **Our assessment**: This is the same "Scheduled Tasks" capability name
  already present in the corpus for other agent products (see
  Cross-References — Anthropic's Cowork and GitHub Copilot CLI both have
  similarly-named scheduled/triggered task features); this post confirms
  OpenAI has shipped an equivalent capability under ChatGPT Work, with the
  event-triggered ("or when an event occurs") variant being a slightly
  broader claim than pure time-based scheduling. No detail is given on
  trigger latency, reliability, or failure handling.

### Claim 12: On desktop, Computer Use lets ChatGPT Work operate the user's computer in the background — clicking, typing, and moving files across apps, tools, and the browser — either as a one-time task or as part of a Scheduled Task
- **Evidence**: Direct feature description in the "Get work done faster
  across the web and your desktop apps" section.
- **Confidence**: emerging (a specific, named feature confirming OpenAI has
  shipped background/unattended Computer Use as part of a mainstream
  consumer+enterprise product, not just a research preview)
- **Quote**: "On desktop, Computer Use lets ChatGPT use your computer on your behalf to execute tasks in the background across your apps, tools, and browser—clicking, typing, and moving files where they need to go. You can use it for a one-time task or as part of a Scheduled Task when recurring work includes steps on your computer."
- **Our assessment**: Confirms that OpenAI's Computer Use capability
  (previously more research/preview-flavored) is now integrated directly
  into the mainstream ChatGPT Work product and combinable with Scheduled
  Tasks for unattended, recurring, GUI-level automation. This combination
  (background GUI automation + recurring schedule) is a meaningfully
  higher-autonomy capability than either feature alone and is the kind of
  concrete capability detail the Prospector's triage flagged as the "key
  question" to look for.

### Claim 13: Enterprise/Edu admins get a Compliance API for visibility into ChatGPT Work conversations and actions at scale, and an "Auto-review" feature that uses OpenAI's most advanced models to review important actions involving connected tools/APIs before they happen, to help prevent unauthorized sharing of sensitive information
- **Evidence**: Direct feature description in the "Security and governance
  for organizations" section.
- **Confidence**: emerging (specific, named governance features; no
  detail on Auto-review's false-positive/false-negative rate, latency
  added to task execution, or which "important actions" trigger it)
- **Quote**: "The Compliance API provides visibility into ChatGPT Work conversations and actions at scale to support enterprise oversight." ... "Auto-review adds another layer of protection by using our most advanced models to review important actions involving connected tools and APIs before they happen, helping prevent unauthorized sharing of sensitive information."
- **Our assessment**: A model-reviewing-a-model governance pattern
  (Auto-review) is a concrete, guide-relevant control worth flagging for
  Ch03 (Verification) — using a separate model pass to gate "important
  actions" before execution is a specific architectural pattern, not just
  a policy statement, though the post gives no detail on what counts as
  an "important action" or how the review model's judgment is itself
  audited or overridden.

## Concrete Artifacts

```
Source: OpenAI, "ChatGPT is now a partner for your most ambitious work,"
https://openai.com/index/chatgpt-for-your-most-ambitious-work (July 9, 2026)

Headline usage figures:
  >5,000,000   weekly Codex users (matches blog-openai-codex-knowledge-work.md
               Claim 1, no growth delta given five weeks later)
  >1,000,000   Codex users doing work outside software development

Model: GPT-5.6 (rolling out same day as ChatGPT Work; matches GA date in
blog-simonwillison-gpt56-ga-launch.md)

Customer testimonials (all first-time in corpus):
  Zapier        — Angela Ferrante, Head of Enterprise Marketing
                  lead-review system; "seven figures in potential sales"
  RingCentral    — Vaneet Seth, R&D Efficiency Manager
                  launch-check automation; scaled 1 -> ~50 supported PMs
  Virgin Atlantic — Nathan Bolt, Head of Digital Products
                  competitive research; "weeks of analysis to hours"
  NVIDIA         — Will Daney, Go-to-Market Manager
                  GTC conference prep automation; ~40% of pre-event time
                  previously spent in Excel eliminated

Internal OpenAI anecdotes (unattributed):
  Sales:   discovery conversation -> tailored proof-of-concept, weeks -> 24 hours
  Finance: month-end close + forecasting, days -> hours
  Adoption: "nearly 100% of teams inside OpenAI" now use ChatGPT Work + Codex

Product/feature launches in this post:
  - ChatGPT Work (agent mode; web, mobile, desktop)
  - Sites (public beta) — interactive site/web app generation, auto-updating
  - Scheduled Tasks — one-time / recurring / event-triggered automation
  - Computer Use (desktop) — background GUI automation, combinable with
    Scheduled Tasks
  - Compliance API + Auto-review (enterprise governance)
  - Codex desktop app merges into unified ChatGPT desktop app
    (Chat/Work/Codex on every plan, including Free)
  - Atlas standalone browser: sunsetting begins
  - Existing ChatGPT desktop app renamed "ChatGPT Classic"

Rollout: Pro/Enterprise/Edu (web, mobile) today; Plus/Business "over the
next few days." Desktop app (all plans, incl. Free) available globally
today for Mac and Windows. Usage follows "the same usage structure as
Codex" (no dollar pricing disclosed in this post).
```

## Cross-References

- **Corroborates**:
  - `blog-openai-codex-knowledge-work.md` Claim 1 (5M+ weekly Codex users,
    June 2, 2026) — this post restates the identical "more than 5 million"
    figure five weeks later with no growth delta, suggesting either
    reused marketing copy or a genuine plateau in the public-facing
    headline number (see Claim 2's assessment).
  - `blog-openai-agents-transforming-work.md` Claim 2 (Codex = 99.8% of
    weekly company-wide output tokens at OpenAI, ~June 25, 2026) and
    Claim 5 (every OpenAI department crossed over to majority-Codex usage
    by ~April 2026) — this post's Claim 8 ("nearly 100% of teams inside
    OpenAI... use ChatGPT Work and Codex") restates the same near-total
    internal-adoption picture in qualitative form, two weeks later, with
    two new concrete workflow anecdotes (sales, finance) not present in
    the earlier post.
  - `blog-simonwillison-gpt56-ga-launch.md` — independently confirms the
    July 9, 2026 GA date for GPT‑5.6 from the vendor's own announcement,
    corroborating Willison's third-party writeup with the primary source.
- **Contradicts**: None identified.
- **Extends**:
  - `blog-openai-notion-codex-case-study.md`,
    `blog-openai-codex-knowledge-work.md` Claims 8-11 (GroundVue, Proaction,
    Inoue, Luke Xing case studies) — this post adds four more named
    customer testimonials (Zapier, RingCentral, Virgin Atlantic, NVIDIA)
    to the corpus's growing set of OpenAI-selected customer vignettes,
    all following the same "days/weeks of manual work -> hours" narrative
    shape. The pattern across five-plus independent OpenAI case studies is
    itself now a notable corpus feature: OpenAI consistently frames agent
    value via before/after time-compression anecdotes from a single named
    individual, never via aggregate cross-customer outcome data.
  - `blog-anthropic-bryant-cowork-sales.md`, `blog-anthropic-cowork-marketing-ops.md`,
    `blog-addyosmani-loop-engineering.md`, `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`
    (all document "Scheduled Tasks" or equivalent recurring/triggered
    automation features in other agent products) — this post's Claim 11
    confirms OpenAI has shipped a directly comparable capability under the
    same feature name ("Scheduled Tasks") in ChatGPT Work; a future guide
    section comparing scheduled-agent-task implementations across
    Anthropic Cowork, GitHub Copilot CLI, and ChatGPT Work would draw on
    all of these.
  - `blog-anthropic-dispatch-computer-use.md`, `blog-anthropic-computer-use-best-practices.md`
    (Anthropic's Computer Use documentation) — this post's Claim 12
    confirms OpenAI now ships an equivalent background/unattended
    Computer Use capability as a mainstream product feature (not a
    research preview), giving the corpus a same-era comparison point
    between the two labs' Computer Use productization.
- **Novel**:
  - "Sites" (Claim 10) — the first source in the corpus describing an
    agent product that generates a live, auto-updating, shareable
    interactive web app/site directly from a chat interface, distinct from
    one-off code-generation or static-artifact patterns already documented.
  - The Codex-desktop-app-into-ChatGPT-desktop-app merger and Atlas
    browser sunset (Claim 9) — the first source in the corpus documenting
    this specific product consolidation; any future extraction citing "the
    Codex app" or "the Atlas browser" as separate products should be
    checked against this July 9, 2026 announcement date.
  - Auto-review (Claim 13) — the first source in the corpus naming a
    dedicated "model reviews agent's important actions before execution"
    governance feature by name, as a shipped enterprise control rather
    than a general best-practice recommendation.
  - The >1,000,000-non-developer-Codex-users absolute figure (Claim 2) —
    more concrete than the percentage-only figures in prior OpenAI posts.

## Guide Impact

- **Chapter 04 (Agentic Workflows / Context Engineering)**: Claim 1
  (ChatGPT Work staying with multi-hour projects by self-decomposing into
  steps) and Claim 11 (Scheduled Tasks with time- and event-based
  triggers) are citable, dated examples of a major vendor shipping
  long-horizon, self-decomposing task delegation as a mainstream product
  feature — pair with the delegation-depth statistics already sourced
  from `blog-openai-agents-transforming-work.md` Claim 3 as a
  "here's the product, here's the usage data" pairing from the same
  vendor.
- **Chapter 03 (Verification)**: Claim 13's Auto-review pattern (a
  separate model pass gating "important actions" before execution) is a
  concrete, named example of a model-reviews-agent-action verification
  architecture worth citing if the chapter discusses automated
  pre-execution review gates — flag that no false-positive/negative data
  or trigger-scope detail is disclosed.
- **Chapter 05 (Team Adoption)**: The four new customer testimonials
  (Claims 4-7) and two internal-OpenAI anecdotes (Claim 8) add five more
  data points to the corpus's "days/weeks of manual work compressed via
  an agent" case-study genre — useful as illustrative examples of the
  *shape* of adoption stories vendors tell, but none should be cited as a
  benchmarkable, reproducible productivity multiplier given the single-source,
  self-reported, vendor-selected nature of every testimonial in this genre.
- **Chapter 02 (Harness Engineering)**: Claim 12's Computer Use +
  Scheduled Task combination (background GUI automation on a recurring
  trigger) is worth noting where the guide discusses the boundary between
  API/tool-call-based agent action and direct GUI automation — this is a
  concrete example of a major vendor shipping the GUI-automation path as a
  first-class, schedulable capability rather than a fallback.
- No chapter should cite the >5M-weekly-Codex-users figure (Claim 2) as
  evidence of *recent* growth — it is identical to the figure already in
  the corpus from five weeks earlier with no stated delta, so it should be
  treated as a restated baseline, not new growth evidence.

## Extraction Notes

- The live OpenAI URL returned an HTTP 403 (Cloudflare bot-challenge page,
  `<meta http-equiv="refresh" content="360">` holding page) to both
  `WebFetch` and direct `curl` with a browser user-agent — the same access
  pattern already documented for `openai.com/index/` posts in
  `blog-openai-agents-transforming-work.md` and
  `blog-openai-chatgpt-adoption-signals.md`, and anticipated by the
  Prospector's second triage comment on this issue ("Article is protected
  by Cloudflare and content could not be directly inspected").
- Unlike those two prior notes (which used the `r.jina.ai` reader proxy),
  this extraction used the Internet Archive Wayback Machine, whose
  availability API returned a snapshot from July 25, 2026
  (`http://web.archive.org/web/20260725042659/https://openai.com/index/chatgpt-for-your-most-ambitious-work/`,
  crawled one day before extraction, sixteen days after publication). The
  `WebFetch` tool refused to fetch `web.archive.org` URLs directly, so the
  snapshot was retrieved with `curl` (browser user-agent) and its HTML
  stripped to plain text locally. All quotes above were checked against
  that stripped text, which preserved full prose, headings, testimonial
  text, and bullet lists.
- The post's several embedded interactive elements — a tabbed "From goals
  to real outcomes across every team" section (Sales/Marketing/Finance/
  Business Operations/Data Analytics/Engineering) and a
  Revenue-forecast-planner/Event-operations-dashboard/Product-launch-hub
  visual showcase — rendered in the extracted text only as tab labels and
  one visible example prompt (the Sales tab's "[Example prompt: Create an
  automation that monitors for new account activity and updates this site
  every day at 8am]"); the Marketing, Finance, Business Operations, Data
  Analytics, and Engineering tabs' example content did not resolve as
  visible text in the flattened HTML (likely loaded via client-side tab
  interaction not captured by a static snapshot). No content was
  fabricated to fill this gap — only the Sales tab's content is cited
  above (implicitly, via the broader sales anecdote in Claim 8, which is
  drawn from a separate paragraph, not the tab).
- No footnote/citation markers requiring resolution were found in this
  post, unlike the `[1]`/`[2]`-style unresolved footnote markers flagged
  in `blog-openai-agents-transforming-work.md` and
  `blog-openai-chatgpt-adoption-signals.md`.
- No contradiction with any existing source note was found during
  cross-referencing (see Cross-References -> Contradicts), so no
  contradiction issue was filed per MINER.md §4a.
- The Prospector's triage comments (three, apparently from repeated triage
  runs) ranged from "low novelty... marketing content" to "medium
  novelty," with the most recent flagging the Cloudflare access barrier.
  On full reading via the Wayback snapshot, this source contains
  substantially more concrete, extractable, guide-relevant detail than
  the low-novelty assessment anticipated — four named customer
  testimonials with specific (if unverified) metrics, a confirmed product
  consolidation (Codex app -> ChatGPT desktop app, Atlas sunset), and
  several named feature launches (Sites, Auto-review) not previously in
  the corpus. Recommend future Prospector triage of Cloudflare-blocked
  OpenAI posts default toward "let the Miner attempt a Wayback/proxy
  fetch before downgrading novelty," since the inability to read the page
  directly during triage appears to correlate with under-estimating
  novelty here.
