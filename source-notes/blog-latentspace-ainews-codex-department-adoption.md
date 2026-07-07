---
source_url: https://www.latent.space/p/ainews-openai-reports-median-internal
source_type: blog-post
title: "[AINews] OpenAI reports median internal Codex output tokens grew 56x in Research, 32x in Customer Support, 27x in Engineering, and 13x in Legal since November 2025."
author: swyx / smol.ai (AINews aggregation, published under Latent Space)
date_published: 2026-06-26
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: emerging
issue: "#1613"
---

# [AINews] OpenAI reports median internal Codex output tokens grew 56x in Research, 32x in Customer Support, 27x in Engineering, and 13x in Legal since November 2025.

> A daily AI-news aggregation digest (covering 6/24-6/25/2026) leading with
> OpenAI Economic Research's internal telemetry showing median Codex output
> tokens among active internal users grew 13x-56x by department over the
> seven months from November 2025 to June 2026, framed by OpenAI and outside
> commentators as evidence that real agent adoption depends on organizational
> readiness (review loops, tooling, persistent workflows), not just having
> unlimited access to the tool.

## Source Context

- **Type**: blog-post (daily news-aggregation digest, "AINews" — a section of
  Latent Space / smol.ai, published 2026-06-26 for the 6/24-6/25 news cycle,
  with the OpenAI internal-adoption item as the lead story rather than one
  item among many). Editorially, this is a curated roundup written and
  lightly synthesized by the AINews/swyx editorial process, built around a
  short block of direct excerpt/paraphrase from OpenAI's own reporting plus
  named Twitter/X reactions, not first-party interviewing.
- **Author credibility**: swyx (Shawn Wang) co-founded Latent Space, already
  a corroborated corpus author (`blog-latentspace-databricks-agent-clouds.md`,
  `blog-latentspace-ainews-meta-harness-summer.md`). The lead item's
  underlying numbers trace to "OpenAI Economic Research" and link out to
  OpenAI's own post at `https://openai.com/index/how-agents-are-transforming-work/`
  (Twitter reference: `https://x.com/OpenAI/status/2070196105745518913`);
  that primary OpenAI URL returned HTTP 403 to both `curl` and WebFetch
  during this extraction (see Extraction Notes), so this note relies on
  AINews's excerpt/paraphrase of the primary source rather than the primary
  source directly. AINews itself is an aggregation product ("We checked 12
  subreddits, 544 Twitters and no further Discords") — value is in curation
  and framing, not original reporting.
- **Scope**: Covers, in order: (1) the OpenAI internal Codex department-growth
  story as a standalone lead item; (2) an "AI Twitter Recap" spanning open
  coding models (GLM-5.2, Ornith-1.0, Liquid LFM2.5-230M), agents in
  production (Google Gemini 3.5 Flash computer use, agent infrastructure
  startups, the OpenAI story restated in context), evaluation/reward-hacking
  concerns (Cursor's benchmark-contamination research, Meta's Autodata),
  and open-ecosystem economics (Hugging Face $100M ARR, Common Crawl, local
  inference tooling); (3) a policy/access-control section (Fable 5 rumor
  correction, the Anthropic/Alibaba distillation dispute); (4) an "AI
  Reddit Recap" covering several open-weight model releases. Does NOT cover:
  OpenAI's own stated measurement methodology for the department multipliers
  (not disclosed in the accessible portion of either this digest or the
  linked primary post) — see Extraction Notes on the paywall boundary.

## Extracted Claims

### Claim 1: OpenAI's internal Codex usage grew sharply and unevenly across departments over seven months, with Research growing the most (56x) and Legal growing the least but still substantially (13x)
- **Evidence**: OpenAI Economic Research's own reported internal telemetry, quoted/paraphrased in the digest and restated in the article's own headline.
- **Confidence**: emerging (first-party vendor telemetry about the vendor's own workforce, relayed via a third-party aggregator rather than read from OpenAI's primary post directly, since that URL 403'd during this extraction; no disclosed sample size, cohort definition, or measurement methodology for any of the four multipliers)
- **Quote**: "Research saw the biggest jump: by June 2026, median use was 56 times higher than in November 2025. Customer Support rose 32 times and Engineering rose 27 times, while Legal grew more gradually but still reached 13 times its November level."
- **Our assessment**: This is the article's central, most specific, and most guide-relevant claim: a same-company, same-tool, cross-department comparison showing non-engineering functions (Research, Customer Support) growing usage faster than Engineering itself. Directionally plausible and specific enough to be falsifiable (four named departments, four named multipliers, a seven-month window), but it is self-reported internal telemetry from the vendor whose product is being measured, with zero disclosed methodology — treat the relative ordering (Research > Customer Support > Engineering > Legal) as more reliable than the precise multipliers themselves.

### Claim 2: Before this growth, OpenAI's own employees were substantially underusing Codex despite having unlimited internal access — spending less than 10% of their tokens on it through August 2025
- **Evidence**: OpenAI's own reported baseline figure, quoted in the digest.
- **Confidence**: emerging (same self-reported-telemetry caveats as Claim 1)
- **Quote**: "Through August 2025, the average OpenAI worker spent less than 10% of their tokens on Codex…"
- **Our assessment**: This baseline figure is what makes Claim 1's growth multipliers meaningful rather than an artifact of a tiny denominator inflating the ratios — it establishes that as of August 2025, Codex was a minority share of OpenAI's own internal token spend even with unlimited access, which the digest's own editorializing (Claim 5 below) treats as evidence that access alone does not drive adoption. Still, "10% of tokens" is a token-share metric, not a user-count or task-count metric, so it cannot be directly compared to the "56x more tokens" growth figure in Claim 1 without knowing what the Nov 2025 per-user token baseline was.

### Claim 3: The digest frames the growth as part of a broader trend of token usage expanding beyond coding tasks specifically
- **Evidence**: The digest's own framing sentence introducing the OpenAI figures.
- **Confidence**: anecdotal (single-sentence editorial framing, not itself a measured claim)
- **Quote**: "OpenAI Economic Research is reporting that token usage for everything outside coding is exploding"
- **Our assessment**: This is the digest's interpretive gloss on Claim 1's numbers, not a separate data point — it reads Research/Customer Support/Legal growth as evidence that Codex (nominally a coding tool) is being used by OpenAI's own staff for non-coding knowledge work. This is consistent with, and adds an internal-adoption data point to, the general "coding agents are becoming general knowledge-work tools" thesis already in `blog-openai-codex-knowledge-work.md`.

### Claim 4: OpenAI states that over the last six months Codex usage "deepened and intensified," with agents changing work "in every department" through longer-running, more cross-functional tasks
- **Evidence**: OpenAI's own framing, quoted in the digest.
- **Confidence**: anecdotal (a vendor's own qualitative characterization of its product's internal impact, not a measured claim distinct from Claim 1's numbers)
- **Quote**: "OpenAI said agents are changing work "in every department," with Codex used for longer-running, more cross-functional tasks."
- **Our assessment**: This is OpenAI's own qualitative narrative layered on top of the quantitative growth figures (Claim 1) — "longer-running, more cross-functional tasks" is asserted, not itself quantified anywhere in the accessible portion of this source. Treat as the vendor's interpretive framing of its own numbers rather than independent evidence of task duration or cross-functionality.

### Claim 5: External commentators (@gdb, @reach_vb, @eliebakouch) read the internal growth as being especially concentrated in research teams and tied to specific usage patterns — "skills" and running concurrent agents
- **Evidence**: Named Twitter/X reactions, paraphrased by the digest.
- **Confidence**: anecdotal (Twitter reactions to a vendor's self-reported figures, no independent data of their own)
- **Quote**: "External commentary from @gdb, @reach_vb, and @eliebakouch emphasized growth in internal token consumption—especially by research teams—and patterns like skills and concurrent agents."
- **Our assessment**: @gdb is Greg Brockman (OpenAI President), so this "external" commentary is itself partly an OpenAI insider amplifying the company's own figures, not a fully independent check. The "skills and concurrent agents" mechanism named here is asserted without elaboration in the accessible text — it points at *how* usage may have intensified (per-task tool/skill usage, running multiple agents at once) but supplies no measurement of either.

### Claim 6: The digest's own editorial takeaway is that the growth pattern argues against a "capability alone drives adoption" narrative — real adoption requires organizational readiness (review loops, tooling, persistent workflows)
- **Evidence**: The digest's closing synthesis sentence for this section.
- **Confidence**: anecdotal (editorial interpretation, not a separate measured finding)
- **Quote**: "The practical takeaway is less "agents are magical" and more that real adoption is emerging where organizations can support review loops, tooling, and persistent workflows."
- **Our assessment**: This is the most guide-actionable single sentence in the source: it explicitly connects Claim 2 (OpenAI staff underused Codex for months despite unlimited access) to a causal claim about *why* — access without supporting organizational infrastructure (review loops, tooling, persistent workflows) does not translate into adoption. This is an assertion, not something the digest demonstrates with evidence beyond the OpenAI numbers themselves, but it is a specific, checkable thesis (adoption lags access until organizational scaffolding exists) that other sources in the corpus could be checked against.

### Claim 7: Agent-infrastructure startups are increasingly optimizing specifically for long-running, persistent agents rather than interactive chat latency — illustrated by Sail ($80M raised, claiming "10x more intelligence per dollar" for patient workloads) and Hyperagent (each agent gets its own persistent cloud machine with browser/code execution)
- **Evidence**: Digest paraphrase of startup announcements, presented in the same "Agents in Production" section as the OpenAI story.
- **Confidence**: anecdotal (vendor self-description of funding and product positioning, no independent verification of the "10x more intelligence per dollar" claim or of Hyperagent's specific architecture)
- **Quote**: "Sail launched with $80M raised to provide low-cost inference and sandboxes for agents that run days or weeks, claiming "10x more intelligence per dollar" for patient workloads. Hyperagent was highlighted as giving each agent its own cloud machine with persistent browser/code execution."
- **Our assessment**: This is adjacent infrastructure context for Claim 1/4's "longer-running, cross-functional tasks" framing — if OpenAI's own internal usage is genuinely shifting toward longer-running agent tasks, a parallel wave of infrastructure startups building specifically for multi-day/multi-week agent execution (rather than chat-turn latency) is a consistent, corroborating market signal, though neither company's technical claims are independently verified here.

### Claim 8: LangChain's "Fleet" framing draws an explicit line between when to use general-purpose chat versus specialized persistent agents
- **Evidence**: Digest paraphrase of LangChain's product positioning.
- **Confidence**: anecdotal (single vendor's own framing of when its product applies, no independent test)
- **Quote**: "LangChain's Fleet framing drew a useful distinction: use general-purpose chat when work ends with an answer; use specialized agents when the work has a repeatable shape and durable context."
- **Our assessment**: A crisp, quotable heuristic ("work ends with an answer" vs. "repeatable shape and durable context") for a decision practitioners face constantly — whether a given task belongs in an ad hoc chat session or a dedicated persistent agent. It is vendor framing rather than an empirical finding, but the heuristic itself is specific enough to be directly usable in guide text on task/tool selection.

### Claim 9: Google made computer use a first-class, built-in capability of Gemini 3.5 Flash across browser, desktop, and mobile, with explicit safety controls (user confirmation for sensitive actions, automated task stopping)
- **Evidence**: Digest paraphrase of Google's own launch announcement (@Google, @GoogleDeepMind, @googledevs), plus a cited developer quickstart from @_philschmid.
- **Confidence**: emerging (first-party vendor product announcement, relayed via aggregator paraphrase rather than read from Google's own post directly)
- **Quote**: "Google made computer use a first-class built-in capability in Gemini 3.5 Flash across browser, desktop, and mobile... Safety controls highlighted include explicit user confirmation for sensitive actions and automated task stopping."
- **Our assessment**: This directly updates `blog-simonwillison-gemini35-flash-pricing.md` Claim 8, which documented Gemini 3.5 Flash as explicitly *lacking* computer use at its May 19, 2026 GA launch ("It mostly has the same set of platform features as the previous Gemini 3.5 series, albeit with no computer use."). This June 26, 2026 item reports computer use has since been added as a first-class capability — a ~5-week-later product update, not a factual disagreement about the same point in time. See Cross-References for why this is not filed as a contradiction.

## Concrete Artifacts

```
Source: "[AINews] OpenAI reports median internal Codex output tokens grew
56x in Research, 32x in Customer Support, 27x in Engineering, and 13x in
Legal since November 2025.", Latent Space/AINews, 2026-06-26

Median internal Codex output-token growth by department, Nov 2025 -> Jun 2026:
  Research            56x
  Customer Support     32x
  Engineering          27x
  Legal                13x

Baseline: "Through August 2025, the average OpenAI worker spent less than
10% of their tokens on Codex" (despite unlimited internal access)
```

```
Source: same digest, "Agents in Production" section, 2026-06-26

Agent infra startups optimizing for long-running/persistent agents:
  Sail       — $80M raised; low-cost inference + sandboxes for agents
               running days/weeks; claims "10x more intelligence per dollar"
  Hyperagent — each agent gets its own persistent cloud machine with
               browser/code execution
  LangChain Fleet — chat vs. specialized-agent selection heuristic:
    "use general-purpose chat when work ends with an answer; use
    specialized agents when the work has a repeatable shape and
    durable context"
```

## Cross-References

- **Corroborates**: `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`
  Claim 10 ("At OpenAI, more than 95% of non-engineers use Codex, not
  ChatGPT") — both sources describe the same population (OpenAI's own
  internal staff) adopting Codex heavily outside pure software engineering.
  That note's figure is a single-snapshot share-of-tool-choice statistic
  with zero visible supporting detail (paywalled beyond a one-line teaser);
  this source adds a quantified, department-by-department growth trajectory
  (Claim 1) over a seven-month window that is directionally consistent with
  — and considerably more granular than — the 95% figure, though neither
  source discloses a shared methodology, so they should be cited as two
  independent, mutually-reinforcing but not strictly reconcilable data
  points about the same underlying phenomenon (internal OpenAI staff
  increasingly choosing Codex over other tools/ChatGPT), not as a single
  unified statistic.
- **Extends**: `blog-openai-codex-knowledge-work.md` — that note documents
  Codex's *external, worldwide* user-base shift toward knowledge workers
  (Claim 2: "knowledge workers now represent about 20 percent of Codex
  users and are adopting it more than 3 times as fast as developers") and
  task-category growth (Claim 4). This source supplies the internal
  mirror-image of that same thesis — OpenAI's *own* Research, Customer
  Support, and Legal departments (not just external non-developer
  customers) ramping Codex usage faster in several cases than Engineering
  itself. Same underlying "coding agent becomes general knowledge-work
  tool" thesis, different (internal vs. external) population — not a
  restatement of the same number.
- **Extends / updates (not a contradiction)**: `blog-simonwillison-gemini35-flash-pricing.md`
  Claim 8 states Gemini 3.5 Flash launched (2026-05-19) explicitly without
  computer use. This source's Claim 9 (2026-06-26, ~5 weeks later) reports
  Google has since added computer use to Gemini 3.5 Flash as a first-class
  capability. **No contradiction issue filed**: per MINER.md §4a, this is a
  conditioning-variable difference (product state at two different points
  in time, with the later date self-evidently superseding the earlier one
  for any "does 3.5 Flash support computer use today" guide question), not
  a genuine dispute between two sources about the same fact at the same
  time — there is nothing for a human to adjudicate. Any guide text citing
  the earlier note's "no computer use" claim as current should be updated
  to reflect this later addition.
- **Contradicts**: None rising to a genuine, adjudicable disagreement (see
  the Gemini 3.5 Flash item above, which is a timeline update rather than a
  contradiction).
- **Novel**: The department-by-department internal Codex token-growth
  multipliers (Claim 1) and the pre-growth internal token-share baseline
  (Claim 2) are new to the corpus — no existing source note quantifies
  OpenAI's own internal cross-departmental agent-adoption rate. The
  "organizational readiness over raw capability" thesis (Claim 6) is also a
  new, specific framing not previously stated this directly elsewhere in
  the corpus. Sail, Hyperagent, and LangChain's Fleet framing (Claims 7-8)
  are new named entities/products to the corpus.

## Guide Impact

- **Chapter 02 (Adoption Patterns) / Chapter 03 (Adoption Velocity &
  Cross-Functional Deployment)**: Cite Claim 1 (56x/32x/27x/13x
  department growth) alongside `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`
  Claim 10 as two independent, internal-OpenAI data points that
  non-engineering functions (especially Research and Customer Support) are
  now growing agentic-tool usage faster than engineering itself inside the
  vendor's own walls — a specific, quantified counter-example to any guide
  framing that treats "coding agents" as an engineering-only tool category.
  Caveat both as self-reported vendor telemetry with no disclosed
  methodology.
- **Chapter 04/05 (Productivity & Measurement / Success Metrics for
  Enterprise Deployment)**: Cite Claim 2 + Claim 6 together as a specific,
  named counter-example to an "access alone drives adoption" assumption:
  OpenAI's own staff had unlimited access to Codex for months and still
  used it for less than 10% of their tokens (Claim 2) until, per the
  digest's own framing, organizational scaffolding (review loops, tooling,
  persistent workflows) caught up (Claim 6). If the guide has or plans
  adoption-measurement guidance, this pairs well as a "give people the
  tool" vs. "build the workflow that makes the tool useful" example.
- **Chapter 02 (Harness Engineering) / Chapter 04 (Workflows)**: Claim 8
  (LangChain's chat-vs-specialized-agent heuristic — "work ends with an
  answer" vs. "repeatable shape and durable context") is a specific,
  quotable decision rule the guide could use directly in any section
  advising when to reach for an ad hoc chat session versus standing up a
  dedicated persistent agent.
- **Chapter 04 (if it discusses model/tool capability tables)**: Update any
  guide text drawing on `blog-simonwillison-gemini35-flash-pricing.md` to
  reflect that Gemini 3.5 Flash gained computer use after its initial GA
  launch (Claim 9) — the "no computer use" fact from that note is now
  stale as of this source's June 26, 2026 report.

## Extraction Notes

- The primary source OpenAI links to (`https://openai.com/index/how-agents-are-transforming-work/`)
  returned HTTP 403 to both `curl` (with a browser user-agent) and WebFetch
  during this extraction, consistent with the Cloudflare-style bot
  protection already documented for the OpenAI domain in
  `blog-openai-codex-knowledge-work.md`'s Extraction Notes. This note
  therefore relies on AINews's excerpt/paraphrase of that primary post
  rather than the primary post itself; a future Miner pass that retrieves
  the primary post (e.g., via a Wayback Machine snapshot, following that
  earlier note's precedent) could raise this note's confidence from
  `emerging` toward `settled` if the excerpted figures match verbatim.
- WebFetch's summarizing model initially declined to reproduce article text
  citing the page's paywall notice, even though the paywall in fact sits
  well past (~76KB into the HTML, after the Ornith-1.0 discussion) the
  lead OpenAI story and the full "AI Twitter Recap" and "AI Reddit Recap"
  sections. The page was re-fetched via `curl` with a browser user-agent
  (HTTP 200) and the pre-paywall HTML (identified via the
  `data-testid="paywall"` marker) was stripped to plain text for verbatim
  quoting, following the same recovery method documented in
  `blog-latentspace-ainews-meta-harness-summer.md`'s Extraction Notes.
- The paywall genuinely does cut the article off mid-way through the "AI
  Reddit Recap" section: the "Ornith-1.0 released on Hugging Face" item is
  the last fully-readable item before the paywall marker. Everything after
  that point (if any further Reddit items existed) was not read and is not
  claimed to have been.
- Sections read in full but not extracted as standalone claims (judged
  off-topic for the Prospector's stated chapter relevance — adoption
  patterns and cross-functional deployment — or already well-covered
  elsewhere in the corpus): the GLM-5.2/Ornith-1.0/Liquid open-model
  coding-benchmark items; Cursor's benchmark-hacking/reward-hacking
  research post; Meta's Autodata synthetic-data framework; Hugging Face's
  $100M ARR milestone and Common Crawl's June 2026 archive; the Fable 5
  rumor-correction and Anthropic/Alibaba distillation-dispute policy
  section; and the full "AI Reddit Recap" (Nemotron-TwoTower, Qwen-
  AgentWorld, Unlimited-OCR, Ornith-1.0 community reception). None of these
  directly bear on the department-level internal-adoption story this issue
  was triaged for, though a future Miner pass focused on eval-integrity or
  synthetic-data chapters could revisit the Cursor benchmark-hacking and
  Autodata items specifically.
- The three Prospector triage comments on this issue are duplicate/repeated
  triage passes on the same source (consistent chapter guidance across all
  three: adoption velocity, cross-functional deployment, productivity
  measurement); all three were read and reconciled into the single
  extraction above.
- Overall confidence rated **emerging**: the core claim (Claim 1) is
  first-party vendor telemetry about the vendor's own internal workforce —
  stronger than a third-party survey in principle, since OpenAI has direct
  access to its own product analytics — but it is unaudited, self-reported,
  relayed through an aggregator rather than read from the primary source
  directly (which 403'd), and discloses no methodology. This falls short of
  "settled" but above purely anecdotal single-user testimony.
