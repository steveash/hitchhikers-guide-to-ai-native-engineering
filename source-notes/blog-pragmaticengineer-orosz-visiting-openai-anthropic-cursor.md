---
source_url: https://newsletter.pragmaticengineer.com/p/impressions-from-visiting-openai
source_type: blog-post
title: "Impressions from visiting OpenAI, Anthropic, & Cursor"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-06-30
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: emerging
issue: "#1531"
---

# Impressions from visiting OpenAI, Anthropic, & Cursor

> First-hand dispatch from on-site visits to OpenAI, Anthropic, and Cursor documenting cloud agents as an industry mega-trend that all three companies (plus at least one independent tool builder) converged on separately, with concrete new operational details — Anthropic's six-month "Claude Managed Agents" build, OpenAI's Ona acquisition and open Cloud Agents team hiring, and Cursor's "confess" pattern and node-termination challenges — though the article's headline claims about non-developer Codex adoption (95%+) and a Coinbase per-token cost case study sit entirely behind the paywall beyond a one-line teaser.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter, Substack, paid tier; ~850-word free preview of a longer paid article, published June 30, 2026)
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager who runs The Pragmatic Engineer, the largest paid technology newsletter on Substack. He is already a trusted, corroborated corpus author (`survey-pragmaticengineer-ai-tooling-2026.md`, `blog-pragmaticengineer-erez-cicd.md`, `blog-pragmaticengineer-hightower-infrastructure-ai.md`, `blog-pragmaticengineer-orosz-slow-down-speed-up.md`). This article is first-hand reporting, not survey data or aggregation: Orosz physically visited the San Francisco offices of OpenAI, Anthropic, and Cursor in late June 2026 and spoke directly with named engineers (David Hershey, Anthropic Applied AI; Katelyn Lesse, head of engineering for Claude Platform; Andrew Ambrosino, first engineer on the Codex team; Sualeh Asif, Cursor cofounder and Chief Product Officer), plus a private AI builders event with independent tool-builder Peter Steinberger.
- **Scope**: Covers cloud-agent infrastructure convergence across three named companies, one named independent tool-builder's parallel convergence on the same solution, Orosz's own four-factor hypothesis for why cloud agents are emerging now, and a one-line teaser each for two further trends (non-developer Codex adoption; per-token cost optimization with a Coinbase case study). Does NOT cover: the detailed non-developer-adoption narrative, the Coinbase case study, or the "engineers building agent-execution environments" trend — all three are named only in the four-bullet "We cover" teaser list and their substantive sections are paywalled. The free content cuts off mid-sentence in the second of four announced sections, immediately after Andrew Ambrosino is introduced and before he says anything.

## Extracted Claims

### Claim 1: Cloud agents are converging as the next infrastructure mega-trend, arrived at independently by OpenAI, Anthropic, Cursor, and at least one outside tool builder, all reacting to the same problem — locally-run agents straining developer machines
- **Evidence**: First-hand reporting across three company visits plus a private AI builders event; the convergence is presented as an observed pattern across independently-run organizations, not a single company's claim.
- **Confidence**: emerging (first-hand, cross-company observation from a credible reporter; still an early-stage trend by the article's own framing)
- **Quote**: "Suddenly, the same solution of cloud agents has emerged in separate places – at Anthropic and with Peter's OpenClaw – in response to issues caused by locally-running agents. I also learned that cloud agents are becoming a big deal at OpenAI and Cursor, too."
- **Our assessment**: The value of this claim is the independent-convergence framing: four distinct organizations (three large labs plus one independent builder) landed on cloud execution as the answer to the same local-agent pain point without apparent coordination. This corroborates `blog-cursor-cloud-agent-lessons.md` (Cursor's own account of building cloud agents at production scale, 40%+ of internal PRs) and `blog-anthropic-claude-managed-agents.md` (Anthropic's hosted platform announcement) from a third, independent vantage point — a reporter who visited all three and saw the same pattern rather than reading three separate vendor posts.

### Claim 2: The excitement around Anthropic's Claude Slack integration ("Claude Tag") is misdiagnosed by public skeptics — the real appeal isn't the Slack integration itself, it's that the agent no longer needs to run on, or be set up on, a local machine
- **Evidence**: Direct explanation from David Hershey (Anthropic Applied AI) during the office visit, plus Orosz's own synthesis after hearing it, illustrated by Hershey's "Claude playing Pokémon" side project (previously required local machine setup each run; now one Slack command).
- **Confidence**: emerging (single named source's explanation, corroborated by a concrete before/after example)
- **Quote**: "My sense is that the excitement here is less about the Slack integration itself, and more to do with the fact that it's easy to kick off one or more AIs that no longer run on a local machine. You can skip the setup entirely."
- **Our assessment**: This reframes a public debate (was Karpathy's "new paradigm" framing of a Slack integration overhyped?) by identifying the actual mechanism of value: eliminating local environment setup and machine dependency, not the chat surface. This is the same underlying value proposition documented in `blog-cursor-ios-mobile-app.md` Claim 4 (bidirectional local↔cloud handoff) and OpenAI's own Ona acquisition rationale (Claim 4 below) — three different companies' cloud-agent pitches all reduce to the same core benefit: decoupling agent execution from a specific machine and session.

### Claim 3: Anthropic built "Claude Managed Agents" — a hosted service to execute long-running agents on cloud providers — as a large, complex engineering effort spanning six months, and it is currently a major internal focus
- **Evidence**: Direct attribution to Katelyn Lesse, head of engineering for Claude Platform, during the office visit.
- **Confidence**: emerging (single named, senior, on-the-record source; internally consistent with the product's public complexity)
- **Quote**: "Claude Managed Agents is a large, complex project which her team built over a six-month period. It's a hosted service to execute long-running agents on various cloud providers."
- **Our assessment**: This adds an internal-effort data point — a named engineering leader and a six-month build timeline — not present in Anthropic's own product announcement (`blog-anthropic-claude-managed-agents.md`), which describes what the platform does but not who built it or how long it took. The six-month figure is a useful calibration for practitioners estimating what it costs (in-house) to build comparable production agent infrastructure (sandboxing, checkpointing, credential management, multi-agent coordination) — the same infrastructure list documented in `blog-anthropic-claude-managed-agents.md` Claim 1.

### Claim 4: OpenAI acquired Ona (formerly Gitpod) specifically to give Codex agents secure, persistent cloud environments so their most valuable work — now unfolding over hours or days rather than minutes — can continue beyond a single device or session
- **Evidence**: Direct quote from OpenAI's own official acquisition announcement, reproduced in the article.
- **Confidence**: emerging (first-party vendor statement, quoted verbatim by an independent reporter; the underlying rationale — that agent tasks now run long enough to outlast a single session — is consistent with the broader cloud-agent convergence pattern)
- **Quote**: "Ona will help us do that. Its technology provides secure, persistent environments where agents can access the tools, systems, and context they need to make progress over time."
- **Our assessment**: This is the clearest single-sentence statement in the corpus of *why* cloud development environments (CDEs) are being repurposed as agent execution infrastructure: CDEs built for human developers to develop faster "also happen to be the perfect primitive for agents to run in a sandboxed cloud environment" (article's framing). The acquisition is OpenAI's infrastructure answer to the same problem Anthropic solved with Claude Managed Agents (Claim 3) and Cursor solved with its own Cloud Agents product (`blog-cursor-cloud-agent-lessons.md`) — three different build-or-buy paths (build in-house, acquire, build in-house) converging on the same capability.

### Claim 5: OpenAI is actively hiring a dedicated "Cloud Agents team" to build and scale cloud agent orchestration infrastructure, confirming this is a newly prioritized, resourced investment rather than a research bet
- **Evidence**: A live job advertisement quoted in full by the article; corroborated by OpenAI engineers' direct answer to Orosz's question about whether their focus is shifting to cloud-based agents ("it very much is").
- **Confidence**: emerging (primary-source job ad text; direct engineer confirmation during the visit)
- **Quote**: "We are looking for an experienced software engineer to help build and scale our cloud agent platform. You will design and operate systems for orchestrating agents at scale. You will work closely with product engineers on ChatGPT, API, and Codex to define the right abstractions and enable them to ship products quickly. Strong backend or infrastructure experience is important; experience with Python, Rust, distributed systems, cloud infrastructure, or product platforms is especially helpful."
- **Our assessment**: An open req for a dedicated "cloud agent platform" team that serves ChatGPT, API, and Codex simultaneously indicates OpenAI is centralizing cloud-agent orchestration as shared infrastructure across product lines, not building it as a one-off feature inside Codex. This is organizational evidence — headcount investment — that corroborates the Ona acquisition (Claim 4) as a strategic bet rather than an isolated deal.

### Claim 6: Cursor invented a "confess" pattern for cloud agents — since a long-running cloud agent has no human in the loop to interactively surface warnings or errors the way a locally-run agent does, the model is prompted to periodically "confess" problems, which are routed to the infrastructure team to improve the environment
- **Evidence**: Direct explanation from Sualeh Asif (Cursor cofounder, Chief Product Officer) during a one-hour conversation at Cursor's offices.
- **Confidence**: emerging (single named, senior, on-the-record source describing a specific named mechanism)
- **Quote**: "Cursor came up with the idea for the model \"confess\" in regular interviews, and the \"confessions\" are shared with the infra team to improve the agents' environment."
- **Our assessment**: This is a genuinely new operational detail not present in Cursor's own engineering synthesis post (`blog-cursor-cloud-agent-lessons.md`), which covers environment quality, Temporal-based durable execution, and the agent-loop/machine-state/conversation-state decoupling pattern, but does not mention a "confess" mechanism. The "confess" pattern is a concrete, named answer to a problem that source implies but doesn't solve: if environment quality is the primary determinant of cloud agent output quality (`blog-cursor-cloud-agent-lessons.md` Claim 1), and poor environments degrade output "subtly" rather than crashing, you need some channel for the agent itself to report environment friction — "confess" is that channel. Extends rather than corroborates that note.

### Claim 7: Long-running cloud agents introduce genuinely new distributed-systems-style engineering problems that don't exist for local agents — specifically, what happens when a compute node terminates mid-execution and how agent execution migrates to a different node
- **Evidence**: Direct explanation from Sualeh Asif during the same conversation.
- **Confidence**: emerging (single named, senior, on-the-record source)
- **Quote**: "What happens when a node terminates, midway through; how do you move agent execution from one node to the other? There are new, nontrivial engineering challenges the team needs to solve."
- **Our assessment**: This corroborates and extends the reliability story in `blog-cursor-cloud-agent-lessons.md` Claim 3–4 (Cursor's migration from a "work-stealing" architecture at ~1-nine reliability to Temporal-based durable execution at >2 nines, explicitly built to "survive... pod hibernation and resumption"). This article confirms, from Asif directly, that node-termination-and-migration is one of the specific problems that reliability work was solving — the two sources describe the same engineering challenge from the strategy level (this article) and the implementation level (`blog-cursor-cloud-agent-lessons.md`).

### Claim 8: Cursor's iOS app, launched June 29, 2026, is built entirely on cloud agent infrastructure — a deliberate architectural choice, since building software from a phone requires agents that run asynchronously and can iterate toward merge-ready PRs without local intervention
- **Evidence**: Direct quote from Cursor's own iOS launch statement, reproduced in the article.
- **Confidence**: emerging (first-party vendor statement about a shipped, generally-available feature; independently corroborated by a separate corpus source note quoting the identical company statement)
- **Quote**: "Cloud agents run in isolated virtual machines with full development environments to test, verify, and demo work. Since they operate asynchronously with their own tools and resources, cloud agents can run for longer and iterate toward merge-ready PRs without intervention."
- **Our assessment**: This is the same underlying Cursor company statement already extracted in `blog-cursor-ios-mobile-app.md` (Concrete Artifacts, "Cursor iOS App: Feature Matrix"), reached independently by two different miners reading two different source pages about the same launch — strong corroboration that the quote is accurate and that Cursor is explicit about the cloud-agents-as-mobile-foundation architecture. Orosz's framing adds one thing the iOS-app note doesn't: positioning the iOS launch as *evidence for the broader cloud-agent mega-trend*, not just a mobile feature in isolation — "only yesterday... Cursor launched its iOS app that enables the building of software from anywhere," presented as the third data point (after Anthropic and OpenAI) in the same reporting trip.

### Claim 9: Orosz's own hypothesis for why cloud agents are converging as a trend specifically now (not two years ago) rests on four simultaneous factors: models crossing an autonomous-coding capability threshold, maturing agent infrastructure (MCP, skills), larger context windows, and greater cloud GPU capacity
- **Evidence**: Author's own analytical synthesis after the three office visits, presented as an explicit hypothesis ("My hypothesis is that a mix of factors are at play") rather than something any single company told him.
- **Confidence**: anecdotal (explicitly labeled a hypothesis by the author, not a measured finding; each of the four factors is independently plausible but not tested against each other or ranked)
- **Quote**: "Coding models got 'good enough'. Before Opus 4.5 / GPT-5.4, AI models could not really code autonomously, so running them for long tasks was pointless!"
- **Our assessment**: This is the first corpus source to synthesize a single four-factor causal framework for the cloud-agent trend's timing. The context-window factor directly corroborates `blog-anthropic-session-management-1m-context.md` (Anthropic's own 1M-context-window feature, which that note documents as changing session-management strategy) — Orosz cites the same "up to 1 million tokens" context window size as a precondition for agents running "for a longer time." The MCP/skills-maturity factor is consistent with the maturation narrative already documented across multiple corpus sources (e.g., `blog-anthropic-mcp-production-agents.md`). As a hypothesis rather than a finding, treat the four factors as a plausible practitioner-reporter framework, not validated causal evidence.

### Claim 10: OpenAI's own framing states that at OpenAI, more than 95% of non-engineers use Codex rather than ChatGPT, offered by Orosz as a possible signal of broader non-developer coding-harness adoption across the tech industry — but the article's substantive discussion of this claim is entirely paywalled
- **Evidence**: Stated only in the article's four-bullet "We cover" teaser list at the top of the piece; the corresponding body section ("2. Mass adoption of coding harnesses by non-developers?") is cut off by the paywall notice one sentence after naming Andrew Ambrosino, before he says anything.
- **Confidence**: anecdotal (headline statistic with zero visible supporting detail — no stated methodology, sample, or definition of "non-engineer" is given anywhere in the readable portion of the article)
- **Quote**: "Mass adoption of coding harnesses by non-developers. At OpenAI, more than 95% of non-engineers use Codex, not ChatGPT. Is it a sign of things to come across tech?"
- **Our assessment**: Treat this as a headline claim awaiting substantiation, not corroborated evidence — we have literally one sentence and no supporting narrative. It should not be read as directly conflicting with `blog-openai-codex-knowledge-work.md` Claim 2 (OpenAI's own report: "knowledge workers now represent about 20 percent of Codex users" of Codex's *total external user base*) — the two statistics measure different populations (the share of OpenAI's *own internal* non-engineering staff who reach for Codex over ChatGPT, vs. the share of Codex's *external, worldwide* user base that is non-developer). They are not restatements of the same number and are not in tension, but a reader skimming both source notes could easily conflate "95% of non-engineers [at OpenAI] use Codex" with "20% of Codex users are non-developers [worldwide]" — worth flagging explicitly in any guide text that cites either figure, to prevent that conflation.

### Claim 11: A related trend named only in the article's teaser: platform/infrastructure teams are aggressively optimizing spend-per-token because AI usage costs generated by software engineers have grown large enough to justify the effort, illustrated with a Coinbase case study whose details are entirely paywalled
- **Evidence**: Stated only in the four-bullet "We cover" teaser list; no corresponding body section is reached before the paywall cuts the article off.
- **Confidence**: anecdotal (one-sentence teaser only; zero visible supporting detail, no numbers, no mechanism described)
- **Quote**: "Next trend? Companies aggressively optimize spend-per-token. AI spending by software engineers is so high that it makes sense for platform teams to slash per-token cost. A case study from Coinbase."
- **Our assessment**: This Coinbase reference cannot currently be verified against or reconciled with `blog-cursor-coinbase-agent-first-adoption.md` (an existing corpus note on a different, Cursor-published Coinbase case study about organizational redesign and idea-to-production time, published June 23, 2026 — one week before this article). It is unclear from the visible teaser alone whether Orosz is referencing the same Coinbase engagement from a cost angle, a different initiative at Coinbase, or a case study specific to this Pragmatic Engineer piece. Do not assume these are the same case study without reading the paywalled section; flag for a future extraction pass if/when this article's paid content becomes accessible.

### Claim 12: A third trend named only in the teaser: the main task of engineers at Anthropic and Cursor is increasingly to build environments that let agents execute more efficiently, rather than to write code directly — but again, no substantive section on this is reached before the paywall
- **Evidence**: Stated only in the four-bullet teaser list.
- **Confidence**: anecdotal (one-sentence teaser only)
- **Quote**: "Will the main task of engineers be to make agents more efficient? Ever more engineering work is about building environments for agents to execute more efficiently at Anthropic and Cursor."
- **Our assessment**: Directionally, this teaser is already substantiated by content that *is* visible in the free portion of the article — Cursor's node-termination/execution-migration challenge (Claim 7) and Anthropic's six-month Managed Agents build (Claim 3) are both examples of engineers building agent-execution environments rather than product features. The teaser line itself adds no new information beyond what the visible sections already show; it is presented here as the article's own explicit naming of a pattern the guide can otherwise support from Claims 3 and 7 directly.

### Claim 13: Independent tool builder Peter Steinberger converged on cloud agents from outside all three labs — he built "Crabbox" specifically to move his own locally-running OpenClaw agents, which were straining his machine's CPU and slowing down his whole system, into the cloud
- **Evidence**: First-hand account from a private AI builders event Orosz attended, where Steinberger discussed his workflow directly.
- **Confidence**: anecdotal (single independent practitioner's account of his own tool and motivation, relayed secondhand by the reporter who heard the talk)
- **Quote**: "He talked about how he has gotten really tired of having several OpenClaw agents running on his local machine, which heat up the CPU and slow down his whole system. So, he built Crabbox as a way to run OpenClaw agents in the cloud"
- **Our assessment**: This is the corpus's first evidence that the cloud-agent convergence extends beyond well-resourced labs to individual practitioners building their own tooling. The stated motivation — literal hardware strain (CPU heat, system slowdown) from running "several" agents locally at once — is a concrete, physical version of the same problem the labs describe in more abstract infrastructure terms (session management, environment setup, machine dependency). It is independent corroboration, from a different actor with different incentives (personal tooling, not a company product), of the same underlying driver.

## Concrete Artifacts

```
Article structure (from "We cover:" teaser list, all visible pre-paywall):
1. Next mega-trend? Agents running in the cloud to go mainstream.
   [SUBSTANTIVELY COVERED IN FREE PREVIEW — see Claims 1-9]
2. Mass adoption of coding harnesses by non-developers.
   [PAYWALLED — teaser only, see Claim 10]
3. Will the main task of engineers be to make agents more efficient?
   [PAYWALLED — teaser only, see Claim 12]
4. Next trend? Companies aggressively optimize spend-per-token.
   [PAYWALLED — teaser only, see Claim 11]

Paywall cutoff point (verbatim, end of free content):
"At OpenAI, I also met Andrew Ambrosino, who was the first engineer on the
Codex team. Our time together got off to an ideal start, with Andrew saying
he needed to show me something incredible:

This post is for paid subscribers"
```

```
Orosz's four-factor hypothesis for "why cloud agents are suddenly a thing"
(source: article body, section "Why are cloud agents suddenly a thing?")

1. "Coding models got 'good enough'. Before Opus 4.5 / GPT-5.4, AI models
   could not really code autonomously, so running them for long tasks was
   pointless!"
2. "Infra for AI coding agents has matured. Ways of giving more context to
   agents have improved: things like MCP and skills became mainstream and
   better understood."
3. "The context window is bigger. Today's models have context windows of up
   to 1 million tokens, meaning that more complex instructions, code, and
   context can be passed in. It's hard to have agents run for a longer time
   without access to a large context window."
4. "Cloud providers have much more GPU capacity. Every cloud provider has
   been building GPU clusters in the last few years, and now there's enough
   that these AI agents can make use of this infra."
```

```
Cloud agent moves observed at each company (article body, per-company sections):

Anthropic: "Claude Managed Agents" — hosted service, 6-month build,
  led within Claude Platform engineering (Katelyn Lesse).

OpenAI: Acquired Ona (formerly Gitpod, a cloud development environment
  leader) to give Codex "secure, persistent environments"; actively
  hiring a dedicated Cloud Agents platform team.

Cursor: Shipped Cloud Agents (end of 2025); "confess" pattern for
  agent-to-infra-team problem reporting; solving node-termination /
  execution-migration challenges; iOS app (June 29, 2026) built
  entirely on cloud agent infrastructure.

Independent: Peter Steinberger built "Crabbox" to run his own
  locally-strained OpenClaw agents in the cloud.
```

## Cross-References

- **Corroborates**: `blog-anthropic-claude-managed-agents.md` — confirms the existence, purpose, and internal prioritization of Claude Managed Agents from an independent reporter's on-site interview, adding the six-month build timeline and named engineering lead (Katelyn Lesse) that the product-announcement blog post does not include.
- **Corroborates**: `blog-cursor-cloud-agent-lessons.md` — confirms Cursor's cloud-agent reliability challenges (node termination, environment quality) from a second, independent source (Sualeh Asif interview) rather than only Cursor's own engineering blog. See also **Extends** below — this article adds two new named mechanisms (the "confess" pattern; explicit node-termination framing from Asif) not present in that note.
- **Corroborates**: `blog-cursor-ios-mobile-app.md` — quotes the identical Cursor company statement about cloud agents running "in isolated virtual machines with full development environments," reached independently via a different source page, strengthening confidence that the quote is accurate and central to Cursor's own framing of the iOS launch.
- **Corroborates**: `blog-anthropic-session-management-1m-context.md` — Orosz's fourth causal factor (Claim 9) explicitly cites "context windows of up to 1 million tokens" as an enabler of longer-running agents, the same 1M context window feature that source documents from Anthropic's own engineering team.
- **Corroborates (same author)**: `survey-pragmaticengineer-ai-tooling-2026.md` — same author (Orosz), different methodology (survey data vs. first-hand office-visit reporting); both document rapid, ongoing shifts in agentic tooling adoption, though this article is anecdotal/qualitative where the survey note is quantitative.
- **Distinguishes (not a contradiction)**: `blog-openai-codex-knowledge-work.md` Claim 2 — that source's "knowledge workers... about 20 percent of Codex users" (external, worldwide Codex user base) measures a different population than this article's teased "more than 95% of non-engineers [at OpenAI] use Codex, not ChatGPT" (internal OpenAI staff tool choice). Both may be true simultaneously; they are not restatements of one number. Flagged explicitly in Claim 10's assessment to prevent conflation in guide text — no contradiction issue filed, since this is a population/scope difference, not a disagreement on the same fact.
- **Unresolved overlap flagged for future extraction**: `blog-cursor-coinbase-agent-first-adoption.md` — this article's one-line teaser about a Coinbase per-token cost-optimization case study (Claim 11) cannot currently be confirmed as the same or a different engagement from the existing Coinbase/Cursor case study already in the corpus (which covers organizational redesign and idea-to-production time, not per-token cost). Left unresolved because the article's substantive Coinbase section is paywalled; see Claim 11's assessment.
- **Extends**: `blog-cursor-cloud-agent-lessons.md` — adds the "confess" pattern (Claim 6) and explicit node-termination/execution-migration framing (Claim 7) as new operational details layered on top of that note's Temporal/durable-execution architecture story.
- **Extends**: `blog-anthropic-claude-managed-agents.md` — adds internal build-effort context (six months, named engineering lead) not present in the first-party product announcement.
- **Novel**: The "confess" pattern by name (Claim 6); Peter Steinberger's independent "Crabbox" convergence (Claim 13); OpenAI's live Cloud Agents team job requisition as organizational evidence (Claim 5); Orosz's explicit four-factor "why now" causal hypothesis (Claim 9); the specific attribution of Claude Managed Agents to a six-month build under Katelyn Lesse (Claim 3).

## Guide Impact

- **Chapter 01/02 (Foundations / Harness Engineering — cloud agents as infrastructure trend)**: Cite this article as independent, cross-company confirmation (three labs plus one independent builder, via a credible reporter's own site visits) that cloud-hosted agent execution is displacing local-machine agent execution as the default architecture for long-running agent work. Pair with the already-corpus-present `blog-anthropic-claude-managed-agents.md` and `blog-cursor-cloud-agent-lessons.md` for the vendor side, and use this source for the "why now" framing (Claim 9's four factors: model capability, MCP/skills maturity, context window size, GPU capacity).
- **Chapter 02 (Harness Engineering — new failure modes of cloud agents)**: Add the "confess" pattern (Claim 6) and node-termination/execution-migration challenge (Claim 7) as concrete, named engineering problems specific to cloud (vs. local) agent execution, extending the existing Cursor reliability narrative in `blog-cursor-cloud-agent-lessons.md`.
- **Chapter 04/05 (Team/Org Adoption)**: Flag but do not yet cite as settled the non-developer Codex-adoption claim (Claim 10) and the engineers-building-environments claim (Claim 12) — both are headline-only, paywalled claims with zero visible supporting detail. Recommend a follow-up extraction if/when the paid content becomes accessible, since the >95% non-engineer figure would be a strong data point for a "non-developer adoption" section if substantiated.
- **Chapter 06 (Cost/Efficiency)**: Do not cite the Coinbase per-token cost-optimization teaser (Claim 11) without first resolving whether it duplicates or differs from `blog-cursor-coinbase-agent-first-adoption.md`'s existing organizational-redesign case study — flagged as an open item above.

## Extraction Notes

- **Paywall**: This is a paid Pragmatic Engineer post. The free preview covers the first of four announced sections in full (cloud agents mega-trend) plus one introductory sentence of the second section; the remaining three sections (non-developer adoption, engineer-efficiency framing, per-token cost optimization / Coinbase) are entirely behind "This post is for paid subscribers." All quotes in this note are taken from the free-to-read portion only, verified against the raw page HTML (fetched via `curl` with a browser user-agent, HTTP 200, then stripped of markup) rather than relying solely on an LLM-summarized re-read of the page — the raw-HTML pass was necessary because an initial WebFetch-based pass produced two mutually inconsistent renderings of the same "95%" statistic across separate calls (one call reported it "paywalled, no exact match"; another reported it as a confirmed quote), which could not be trusted without independent verification. The raw HTML confirms the 95% line and the Coinbase line both appear only in the pre-paywall "We cover:" teaser bullets, not in any substantiated body section.
- No sub-pages were followed: the article links to an X/Twitter post (Karpathy) and a screenshot image (Crabbox), neither of which is a substantive text source requiring extraction per MINER.md's "follow up to 5 linked pages" guidance — both are illustrations of points already fully stated in the article's own prose.
- No contradiction issue filed. The one candidate tension (Claim 10 vs. `blog-openai-codex-knowledge-work.md` Claim 2) was examined and determined to be a difference in measured population (internal OpenAI staff vs. external worldwide Codex users), not a disagreement about the same fact — see Cross-References.
- Confidence is set to `emerging` overall: the visible, substantiated portion of the article (cloud agents as a converging mega-trend, Claims 1–9) rests on first-hand, named, on-the-record interviews across three separate companies plus an independent builder, which is stronger than typical single-vendor marketing copy. However, three of the article's four headline claims (Claims 10–12) are supported by nothing beyond a one-sentence teaser, which pulls the overall confidence down from "settled." Individual claims are rated at the appropriate level within the note (emerging for the substantiated cloud-agent material, anecdotal for the paywalled teasers).
