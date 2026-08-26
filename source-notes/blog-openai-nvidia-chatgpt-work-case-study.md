---
source_url: https://openai.com/index/nvidia/chatgpt-work
source_type: blog-post
title: "How NVIDIA scales expertise with ChatGPT Work"
author: OpenAI
date_published: 2026-08-18
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: anecdotal
issue: "#2966"
---

# How NVIDIA scales expertise with ChatGPT Work

> A short, two-vignette OpenAI customer case study on NVIDIA's internal use
> of ChatGPT Work: a Go-to-Market Strategist who automated GTC-conference
> prep into a twice-weekly workflow he shares (and colleagues customize)
> across regions, and a Solutions Architect who uses ChatGPT Work to
> distill dozens of weekly external AI updates into a handful of
> actionable signals and to prototype ideas in days instead of weeks. Adds
> quantified hours-saved and workflow-sharing detail to the same Will
> Daney/NVIDIA testimonial already in the corpus, plus one entirely new
> named case (Rachita Jain).

## Source Context

- **Type**: blog-post (OpenAI "Product" news vertical, `openai.com/index/`,
  a short customer-case-study page — three sections: two named-individual
  vignettes and a closing "What's next" framing paragraph. Substantially
  shorter and narrower than OpenAI's general ChatGPT Work launch post
  (`blog-openai-chatgpt-work-ambitious-partner.md`) — no product-feature
  description, no pricing/availability section, no security/governance
  section.
- **Author credibility**: House-authored OpenAI customer-marketing
  content, no named individual author. Contains two named
  NVIDIA-employee quotes (Will Daney, Go-To-Market Strategist; Rachita
  Jain, Solutions Architect) attributed by name and title. This is
  first-party vendor marketing copy — both testimonials are
  OpenAI-selected and OpenAI-published, with no independent verification
  of the hours-saved or timeline figures. Same standard vendor-case-study
  credibility caveats as the rest of the corpus's OpenAI customer-story
  genre apply.
- **Scope**: Covers two individual NVIDIA employees' workflows built on
  ChatGPT Work (event-prep automation; AI-industry-monitoring and rapid
  prototyping) and a short closing statement about NVIDIA's plan to scale
  these patterns org-wide. Does NOT cover: any ChatGPT Work product
  feature detail (no mention of Codex, Scheduled Tasks, Connectors,
  GPT‑5.6, or Compliance API by name), NVIDIA-wide adoption metrics
  (headcount, percentage of employees using ChatGPT Work, or a
  company-wide token/usage figure), pricing, or any detail on how the
  workflows are technically implemented (no data-source, API, or
  scheduling-mechanism specifics — the article explicitly avoids
  granular technical detail).

## Extracted Claims

### Claim 1: NVIDIA frames its ChatGPT Work adoption as helping knowledge workers spend less time assembling information and more time acting on it
- **Evidence**: The article's own opening framing sentence.
- **Confidence**: anecdotal (a vendor-authored thesis statement, not a
  measured claim)
- **Quote**: "At NVIDIA, ChatGPT Work is helping knowledge workers spend less time assembling information and more time acting on it."
- **Our assessment**: A generic framing sentence that restates the
  same "gather information → produce finished work" thesis already
  documented in `blog-openai-chatgpt-work-ambitious-partner.md` Claim 1;
  it adds no new evidence on its own, but sets up the two vignettes that
  follow, which do add new detail.

### Claim 2: Will Daney (Go-To-Market Strategist at NVIDIA, supporting global sales/business development/product leadership around NVIDIA's GTC conference) turned a manual, spreadsheet-based GTC-prep process that previously consumed about 40% of his time into an automated ChatGPT Work process that runs twice a week, saving about 16 hours per week across the 12-week GTC planning cycle
- **Evidence**: Named customer testimonial, with a specific quantified
  time-savings figure (hours/week) in addition to the percentage-of-time
  figure.
- **Confidence**: anecdotal (single named individual, vendor-selected
  and vendor-published testimonial; "about 16 hours per week" is a
  self-reported estimate with no measurement methodology given)
- **Quote**: "Previously, preparing for GTC required extensive work in spreadsheets: assembling account lists, tracking registrations, and helping teams identify the actions needed to create a productive experience for customers and partners. During the lead-up to the event, Will estimates that manual analysis consumed about 40% of his time. Today, he has turned much of that work into an automated ChatGPT Work process that runs twice a week. Across the 12-week GTC planning cycle, the workflow saves about 16 hours per week."
- **Our assessment**: This is the same underlying Will Daney/NVIDIA GTC
  case already captured in `blog-openai-chatgpt-work-ambitious-partner.md`
  Claim 7 (~40% of pre-event time previously spent in an Excel workflow),
  but this article adds three pieces of quantified detail the earlier
  post lacked: (a) an absolute hours-saved figure (~16 hours/week), (b)
  an explicit run cadence ("runs twice a week"), and (c) the 12-week
  planning-cycle window the hours figure is scoped to. The earlier post
  described *what* was replaced (an Excel workflow) and gave only the
  40% figure; this post quantifies the resulting savings. Treat "about
  16 hours per week" as a self-reported estimate layered on the same
  40%-of-time baseline, not as independent new evidence of a different
  or larger effect.

### Claim 3: Because Daney owns the ChatGPT Work workflow himself, he can adapt it as the event changes without waiting on a new tool to be purchased, implemented, and maintained — and he has shared the underlying process with colleagues supporting GTC events in San Jose, Taipei, Europe, and Washington, DC, who have customized it for their local needs
- **Evidence**: The article's own narrative description of workflow
  ownership and cross-region sharing.
- **Confidence**: anecdotal (a single individual's self-reported account
  of internal workflow-sharing, no detail on how many colleagues adopted
  it, how much customization was needed, or any outcome data from the
  regional variants)
- **Quote**: "And because he owns the workflow, he can adapt it as the event changes without waiting for a new tool to be purchased, implemented, and maintained. He can also share the underlying process with teams in other regions. Colleagues supporting events in San Jose, Taipei, Europe, and Washington, DC have received his ChatGPT workflows and customized them for their local needs."
- **Our assessment**: Novel to the corpus — no existing OpenAI customer
  case study documents a named, geography-specific pattern of an
  individual-built ChatGPT Work workflow being handed off and
  locally customized by peers across multiple sites. This is a concrete
  instance of bottom-up, practitioner-owned workflow propagation (as
  opposed to a centrally procured and IT-deployed tool), which is a
  distinct organizational-scaling pattern from the aggregate adoption
  statistics elsewhere in the corpus (e.g., "nearly 100% of teams inside
  OpenAI... use ChatGPT Work," `blog-openai-chatgpt-work-ambitious-partner.md`
  Claim 8) — those are usage-penetration numbers, whereas this is a
  peer-to-peer knowledge-transfer mechanism.

### Claim 4: Daney describes the key benefit as being able to take a workflow he already built and re-run/automate it for each new event with little to no overhead
- **Evidence**: Direct named quote.
- **Confidence**: anecdotal (single self-reported characterization)
- **Quote**: "With ChatGPT, I think the real key is that I'm able to take a workflow I've already developed and I'm able to automate it event over event with little to no overhead." —Will Daney, Go-To-Market Strategist at NVIDIA
- **Our assessment**: Reinforces Claim 3's "workflow reuse without
  re-procurement" framing in the subject's own words; consistent
  in shape (though more specific in mechanism) with the broader
  "days/weeks of manual work compressed via an agent" testimonial genre
  already noted as a recurring OpenAI narrative pattern in
  `blog-openai-chatgpt-work-ambitious-partner.md`'s Cross-References →
  Extends section.

### Claim 5: Rachita Jain, a Solutions Architect on NVIDIA's AI operations team (within NVIDIA's marketing organization), built a ChatGPT Work workflow that reviews trusted external AI-industry sources alongside internal context, identifies meaningful overlap, and distills roughly 25–40 external AI updates per week into 5–8 actionable signals
- **Evidence**: Named customer testimonial with specific quantified
  input/output volumes.
- **Confidence**: anecdotal (single named individual, vendor-selected
  testimonial; the 25–40 → 5–8 figures are self-reported with no stated
  measurement window or definition of what counts as an "actionable
  signal")
- **Quote**: "Rachita built a workflow with ChatGPT Work that reviews trusted external sources alongside internal context, identifies meaningful areas of overlap, and surfaces insights that can inform action. Each week, it distills roughly 25–40 external AI updates into 5–8 actionable signals."
- **Our assessment**: Entirely new named case to the corpus — no
  existing OpenAI customer story documents a competitive-intelligence /
  industry-monitoring use case (continuously triaging external AI news
  against internal priorities) with this specific input/output
  compression ratio. This is a distinct workflow shape from the
  event-logistics automation (Claim 2) and the research-compression
  testimonials already in the corpus (Virgin Atlantic, GroundVue) — it's
  a recurring filtering/triage pipeline rather than a one-off analysis
  task.

### Claim 6: Jain describes the biggest problem she's solving as information overload from a fast-moving AI industry, and says ChatGPT changed her process from passive reading into "active intelligence"
- **Evidence**: Two direct named quotes.
- **Confidence**: anecdotal (single self-reported characterization)
- **Quote**: "ChatGPT helped me change passive reading into active intelligence"
- **Quote (problem framing)**: "I think the biggest problem I'm trying to solve is information overload, because everything is moving so fast. It's getting harder by the day to keep track of all the changes. And with ChatGPT, it becomes much simpler." —Rachita Jain, Solutions Architect at NVIDIA
- **Our assessment**: The "passive reading → active intelligence" framing
  is a distinctive, quotable phrase for describing an information-triage
  (as opposed to task-execution) agent use case; worth flagging as a
  concrete example if the guide ever discusses agent-assisted
  environmental scanning / competitive intelligence as its own workflow
  category.

### Claim 7: The same ChatGPT Work environment that supports Jain's monitoring workflow also supports her broader building process — starting from an idea, exploring approaches, working through a codebase, and debugging — without continually switching between disconnected tools; in one case she went from idea to working prototype in about 3–5 days, versus an estimated 2–3 weeks if she had built the same components manually across separate tools
- **Evidence**: Named testimonial describing a specific prototyping
  timeline comparison.
- **Confidence**: anecdotal (single self-reported instance, "estimated
  2–3 weeks" is a counterfactual estimate rather than a measured
  baseline)
- **Quote**: "The same environment supports the broader building process. Rachita can begin with an idea, explore possible approaches, work through a codebase, debug problems, and refine the result without continually moving between disconnected tools. Initiatives that might once have remained side projects can develop into working products within days. In one case, she moved from idea to working prototype in about 3–5 days, compared with an estimated 2–3 weeks if she had built the components manually across separate tools."
- **Our assessment**: This is the closest thing in this article to a
  harness-engineering claim rather than a pure knowledge-work claim — the
  stated benefit is explicitly attributed to *tool consolidation* (not
  "continually moving between disconnected tools"), which is a
  more specific mechanism than the vague "agent is a force multiplier"
  framing found elsewhere. Still a single, self-reported, uncontrolled
  comparison (estimated vs. actual timeline), so the 3–5 days vs. 2–3
  weeks ratio should be treated as illustrative, not benchmarkable.

### Claim 8: NVIDIA's stated forward strategy is to scale its proven ChatGPT Work workflows across functions and regions by turning specialized knowledge into reusable processes, while deliberately keeping "the people closest to the work" in control of how those processes evolve
- **Evidence**: The article's own closing "What's next" framing
  paragraph.
- **Confidence**: anecdotal (a forward-looking, vendor-authored strategy
  statement, not a reported outcome)
- **Quote**: "The next opportunity is to scale what's already working. By turning specialized knowledge into reusable workflows, teams across NVIDIA can adapt proven processes across functions, events, and regions—while keeping the people closest to the work in control of how those processes evolve."
- **Our assessment**: This is a specific, named organizational-scaling
  philosophy — decentralized ownership of AI-built workflows, propagated
  peer-to-peer and locally adapted, rather than centrally standardized
  and IT-mandated — that is directly evidenced by Claim 3's concrete
  San Jose/Taipei/Europe/DC example. It stands in contrast to the more
  typical "roll out a standardized tool company-wide" adoption narrative
  and is worth flagging as a distinct scaling pattern for a guide chapter
  on org-level AI-native adoption strategy.

### Claim 9: The article closes by restating Daney's "force multiplier" quote as evidence that the scaling opportunity is already visible in practice: "ChatGPT has really been a force multiplier for me personally. It feels like I have a team working for me. It's helped me get out of the weeds and focus more on the work that matters."
- **Evidence**: Direct named quote, placed in the closing section as
  supporting evidence for Claim 8's forward-looking strategy statement.
- **Confidence**: anecdotal (single self-reported characterization)
- **Quote**: "ChatGPT has really been a force multiplier for me personally. It feels like I have a team working for me. It's helped me get out of the weeds and focus more on the work that matters."
- **Our assessment**: "Force multiplier" and "like I have a team working
  for me" are common framings already present elsewhere in the corpus's
  OpenAI/Anthropic customer-testimonial genre (see Cross-References);
  this instance's news value is structural, not lexical — OpenAI chose to
  close the piece by looping back to Daney's individual outcome as the
  proof point for the company-wide scaling claim in Claim 8, rather than
  citing an aggregate NVIDIA-wide metric.

## Concrete Artifacts

```
Source: OpenAI, "How NVIDIA scales expertise with ChatGPT Work,"
https://openai.com/index/nvidia/chatgpt-work (published 2026-08-18, per
the openai-news RSS feed entry that surfaced this issue; no publication
date was visible in the extracted page body itself).

Section structure (3 sections, in order):
  1. Freeing teams to focus on customers   (Will Daney vignette)
  2. Finding the signal in a fast-moving industry (Rachita Jain vignette)
  3. What's next                            (closing scaling statement)

Will Daney (Go-To-Market Strategist, NVIDIA):
  - Prior process: manual spreadsheet work (account lists, registration
    tracking, action identification) for GTC conference prep
  - Prior time cost: ~40% of his time during GTC lead-up
  - New process: automated ChatGPT Work workflow, runs 2x/week
  - Savings: ~16 hours/week across a 12-week GTC planning cycle
  - Workflow shared/customized by colleagues in: San Jose, Taipei,
    Europe, Washington DC

Rachita Jain (Solutions Architect, NVIDIA AI operations team, within
NVIDIA's marketing organization):
  - Workflow: reviews trusted external AI-industry sources + internal
    context, surfaces overlap/actionable insight
  - Volume: ~25-40 external AI updates/week -> 5-8 actionable signals/week
  - Prototyping: idea -> working prototype in ~3-5 days
    (vs. an estimated 2-3 weeks building components manually across
    separate tools)

No OpenAI product/feature names besides "ChatGPT Work" appear in the
article (no Codex, Scheduled Tasks, Connectors, GPT-5.6, or Compliance
API mentions). No NVIDIA-wide adoption metric (headcount or % of
employees) is given.
```

## Cross-References

- **Corroborates**:
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 7 — the same
    Will Daney / NVIDIA GTC testimonial (this article restates the ~40%
    pre-event-time figure) with three new quantified details layered on
    top: an absolute hours-saved figure (~16 hrs/week), an explicit
    twice-weekly run cadence, and the 12-week cycle window (see Claim 2
    above).
  - `blog-openai-chatgpt-work-ambitious-partner.md`'s general "days/weeks
    of manual work compressed via an agent" testimonial pattern (noted in
    that note's Cross-References → Extends) — this article's Claim 7
    (3-5 days vs. an estimated 2-3 weeks) is another instance of the same
    narrative shape from a different named individual.
- **Contradicts**: A minor, non-material inconsistency: this article
  identifies Will Daney's title as "Go-To-Market Strategist at NVIDIA,"
  while `blog-openai-chatgpt-work-ambitious-partner.md` Claim 7 (a
  different OpenAI-published post, dated July 9, 2026, about the same
  named individual and the same GTC workflow) identifies him as
  "Go-to-Market Manager, NVIDIA." Both posts otherwise describe the same
  person and the same workflow, so this reads as OpenAI's own internal
  inconsistency in how it captions the same customer across two
  marketing posts, not a substantive factual disagreement — it does not
  rise to a guide-impacting contradiction per MINER.md §4a (no guide
  advice would differ depending on which title is correct), so no
  contradiction issue was filed. Noted here as a data-quality flag: this
  article's title for Daney should not be treated as more authoritative
  than the July 9 post's without further verification.
- **Extends**:
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 8 ("nearly
    100% of teams inside OpenAI... use ChatGPT Work") — that claim is an
    aggregate internal-OpenAI adoption statistic; this article's Claim 3
    (Daney's workflow physically handed off to and customized by
    colleagues in four regions) is a customer-side example of the
    *mechanism* by which adoption might spread inside a large
    organization — peer-to-peer workflow sharing rather than a
    top-down mandate — which the earlier post does not describe for any
    customer.
  - `blog-latentspace-khemani-unpacking-chatgpt-work.md` Claim 7 (the
    apps/skills/app-templates plugin architecture, including
    "app templates for organization-specific configuration") — this
    article's Claim 3 (regional colleagues receiving and customizing
    Daney's workflow) is a real-world, named example of the kind of
    workflow reuse and local adaptation that app templates are designed
    to support, though this article never names "app templates" or any
    other product mechanism explicitly, so the connection is inferential,
    not confirmed by the source.
- **Novel**:
  - Rachita Jain's competitive-intelligence/industry-monitoring workflow
    (Claims 5-6) — a filtering/triage use case (many external inputs
    distilled into few actionable signals on a recurring cadence) not
    previously documented in the corpus's OpenAI customer-story set,
    which has so far focused on event logistics, sales pipeline review,
    launch-checklist automation, and competitive research (singular
    reports), not continuous external-signal triage.
  - The named, geography-specific workflow-sharing detail (Claim 3: San
    Jose, Taipei, Europe, Washington DC) — the first source in the corpus
    to document a specific, named cross-region propagation path for a
    single individual's self-built ChatGPT Work workflow.
  - The "keeping the people closest to the work in control" scaling
    philosophy (Claim 8) — a distinct, explicitly named organizational
    stance on how to scale agent-built workflows (decentralized
    ownership) not previously articulated in the corpus's OpenAI
    customer-story or launch-post material, which otherwise emphasizes
    company-wide adoption percentages and centrally announced feature
    rollouts.

## Guide Impact

- **Chapter 05 (Team Adoption / Scaling AI-native orgs)**: Add Claim 3
  and Claim 8 as a concrete, named counter-example to the
  centrally-mandated-tool-rollout adoption pattern — NVIDIA's own framing
  is "keep the people closest to the work in control," evidenced by a
  named individual's workflow spreading peer-to-peer across four
  regions with local customization rather than being standardized top
  down. Pair with `blog-openai-chatgpt-work-ambitious-partner.md`
  Claim 8's aggregate "nearly 100% of teams" figure as a "here's the
  percentage, here's one mechanism that might produce it" pairing.
- **Chapter 01 (Agent Patterns)**: Add Claim 5 (Jain's 25-40 → 5-8
  weekly triage workflow) as a named example of a recurring
  information-filtering agent pattern, distinct from the
  one-off-analysis and task-automation patterns already documented from
  other OpenAI customer stories — useful if the guide categorizes agent
  use cases by workflow shape (one-off task vs. recurring triage
  pipeline vs. GUI/browser automation).
- **Chapter 02 (AI-Native Patterns) / harness-consolidation discussion**:
  Add Claim 7's specific mechanism claim (fewer context switches between
  disconnected tools shortens idea-to-prototype time, 3-5 days vs. an
  estimated 2-3 weeks) as one more data point for a discussion of
  environment consolidation as a stated driver of agent-assisted
  build-speed gains — flag it as a single self-reported, uncontrolled
  comparison, not a benchmark.
- No chapter should treat the ~16-hours/week or 25-40→5-8 figures as
  independently verified productivity multipliers; both are
  single-source, self-reported, vendor-selected testimonials with no
  measurement methodology disclosed, consistent with every other
  OpenAI customer-story figure already flagged this way in the corpus.

## Extraction Notes

- **Fetch method**: The live `openai.com/index/nvidia/chatgpt-work` URL
  returned an HTTP 403 to `WebFetch` (the same Cloudflare bot-challenge
  pattern already documented for `openai.com/index/` posts elsewhere in
  the corpus, e.g. `blog-openai-chatgpt-work-ambitious-partner.md`). A
  Wayback Machine snapshot exists
  (`http://web.archive.org/web/20260818231550/https://openai.com/index/nvidia/chatgpt-work`,
  timestamped the same day as the RSS-feed publication date) but
  `WebFetch` explicitly refused `web.archive.org` URLs ("Claude Code is
  unable to fetch from web.archive.org"), and direct `curl` to
  `web.archive.org` from this environment's network sandbox failed to
  connect (connection refused on port 80). Extraction instead used the
  `r.jina.ai` reader-proxy path against the live URL (the same
  fallback used successfully in
  `blog-latentspace-khemani-unpacking-chatgpt-work.md`), issuing five
  separate, narrowly scoped `WebFetch` prompts explicitly requesting
  character-for-character verbatim reproduction of each section (Will
  Daney's quotes/figures; Rachita Jain's quotes/figures; the title,
  intro, headings, and closing section; product/tool-name and
  technical-detail check; and finally the full verbatim text of both
  named-individual sections) before finalizing any `Quote` field, per
  MINER.md §2a. Cross-checking the independently-fetched full-section
  passes against the earlier narrower passes showed no discrepancies in
  wording.
- **Full article read**: The article is short (three sections, roughly
  600 words of body text) and was read in full via the fetch passes
  above; no linked sub-pages were found within the article body to
  follow.
- **Publication date**: No publication date was visible in the extracted
  page body itself. The 2026-08-18 date used in this note's frontmatter
  is taken from the Prospector's triage comment on issue #2966, which
  cites the `openai-news` RSS feed entry ("Published: Tue, 18 Aug 2026
  00:00:00 GMT") — consistent with the Wayback Machine's closest snapshot
  timestamp of the same date.
- A minor title inconsistency for Will Daney between this post and
  `blog-openai-chatgpt-work-ambitious-partner.md` was found during
  cross-referencing and is recorded under Cross-References → Contradicts
  above; it was judged not to meet the MINER.md §4a bar for filing a
  contradiction issue (no guide advice turns on which title is correct).
  No other contradiction with any existing source note was found.
