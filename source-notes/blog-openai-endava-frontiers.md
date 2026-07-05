---
source_url: https://openai.com/index/endava-frontiers
source_type: blog-post
title: "How Endava is redesigning software delivery around AI agents"
author: OpenAI (customer-story vertical; interview subject Matthew Cloke, CTO, Endava)
date_published: 2026-06-04
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: anecdotal
issue: "#1545"
---

# How Endava is redesigning software delivery around AI agents

> A short OpenAI customer-story interview with Endava's CTO Matthew Cloke describing how the ~11,000-person IT services/consulting firm made ChatGPT Enterprise and Codex its enterprise AI platform, embedded AI throughout its "DavaFlow" delivery lifecycle, watched the adoption bottleneck migrate from engineering into requirements/business analysis, and expanded usage beyond engineering into legal, PM, and commercial teams — with no quantitative metrics beyond headcount and a qualitative results/lessons list.

## Source Context

- **Type**: blog-post (OpenAI customer-story page, `openai.com/index/`, ~700 words; auto-discovered via the `openai-news` trusted feed, published Thu, 04 Jun 2026 per the feed entry)
- **Author credibility**: House-authored OpenAI customer-story copy built around a single interview with Matthew Cloke, Endava's CTO. This is a vendor case study — OpenAI selected the customer, framed the narrative, and chose which quotes to publish — not an independent report or a piece with disclosed methodology. Cloke is a credible primary-source voice for what happened inside Endava (he is the CTO), but the piece is promotional in structure (a "Results at a glance" bullet list with no numbers, a "Lessons learned" list, a closing call to action) and contains zero named metrics beyond the ~11,000-person headcount figure.
- **Scope**: Covers Endava's platform decision (ChatGPT Enterprise + Codex as sole enterprise AI platform), the "AI-native" mindset framing, the observation that the engineering-adoption bottleneck shifted upstream to requirements/business analysis/planning, the "DavaFlow" delivery-lifecycle branding, adoption spreading to legal/PM/commercial teams (with one concrete anecdote — a pricing app replacing a spreadsheet exercise), a qualitative results list, a six-item lessons-learned list, and a forward-looking "orchestration" framing for what's next. Does NOT cover: any quantitative outcome metric (no percentages, no time savings, no cost figures), the DavaFlow lifecycle's actual phases or tooling, how legal/PM/commercial workflows are technically implemented, or any detail on how "AI fluency" is measured for hiring/promotion.

## Extracted Claims

### Claim 1: Endava defines "AI-native" as making AI the first step in solving a problem, not the last
- **Evidence**: Direct quote from CTO Matthew Cloke describing the company's operating philosophy.
- **Confidence**: anecdotal (single executive's characterization of company culture, no supporting behavioral data beyond the quotes that follow)
- **Quote**: "To be AI-native at Endava, it's about thinking about AI to solve the problem first. It's the first thing you do rather than the last thing that you do."
- **Our assessment**: This is a clean, quotable definition of "AI-native" as a decision-ordering habit (check AI first) rather than a tooling inventory. It is consistent with the corpus's existing framing of AI-native adoption as a mindset/behavior change rather than a software rollout (see Cross-References), but this article does not describe how the habit was instilled or measured — it is asserted, not demonstrated.

### Claim 2: Cloke personally treats an idle background agent as wasted time
- **Evidence**: Direct pull-quote from Cloke, presented as a standalone block quote in the article.
- **Confidence**: anecdotal (single executive's personal working habit)
- **Quote**: "If I don't have an agent running in the background, I somehow think I'm wasting my time."
- **Our assessment**: A vivid, individual-level illustration of the "agent-first" reflex named in Claim 1, and a specific behavioral norm (always have a background agent running) rather than a general sentiment. It parallels — without being identical to — Fiona Fung's "Is there a way to automate it?" reflex in `blog-anthropic-ai-native-engineering-org.md` Claim 5, but Cloke's framing is about constant background-agent utilization as a personal habit, while Fung's is about converting specific recurring manual rituals into scheduled automations. Both are executive-level "always be delegating to an agent" norms from different companies.

### Claim 3: Endava made OpenAI (ChatGPT Enterprise plus Codex) its single enterprise AI platform, rather than adopting AI tools piecemeal
- **Evidence**: Direct statement of the platform decision, attributed to leadership intent ("That mindset led Endava to make OpenAI its enterprise AI platform").
- **Confidence**: anecdotal (a stated platform decision; no detail on selection criteria, prior tools evaluated, or contract scope)
- **Quote**: "That mindset led Endava to make OpenAI its enterprise AI platform, giving employees across the company access to ChatGPT Enterprise and Codex."
- **Our assessment**: This is a single-vendor enterprise platform bet at company scale, which contrasts with the multi-tool policy documented in `blog-bvp-shopify-ai-playbook.md` (Shopify deliberately runs Cursor, Claude Code, GitHub Copilot, and Codex side by side). Endava's single-platform choice and Shopify's multi-tool choice are both plausible strategies for different organizational contexts (consulting/delivery firm needing one platform employees across roles can standardize on, versus a product company optimizing per-task tool fit) — this is a conditioning-variable difference, not a contradiction, so no contradiction issue was filed per MINER.md 4a.

### Claim 4: Once developers adopted AI-assisted coding, the delivery bottleneck moved from engineering output to requirements gathering, business analysis, planning, and stakeholder coordination
- **Evidence**: Direct account of what Endava's software delivery teams observed after early coding-agent adoption, attributed to Cloke.
- **Confidence**: emerging (a specific, named bottleneck-migration claim from a named executive, consistent with independently-sourced convergence elsewhere in the corpus — see Cross-References — though still a single-company anecdote without measurement)
- **Quote**: "As developers started experimenting with AI-assisted coding and agentic workflows, teams quickly realized the bottleneck was no longer engineering output. Requirements gathering, business analysis, planning, and stakeholder coordination all needed to move faster too." — paired with Cloke's own words: "We started to challenge how quickly we could produce requirements and how quickly we could produce the right business solutions for our clients."
- **Our assessment**: This is the single most guide-relevant claim in the article. It is now at least a fourth independent corroboration of the "bottleneck shifts once code generation is no longer the constraint" pattern already established via Osmani (`blog-addyosmani-code-agent-orchestra.md` Claim 5: "The bottleneck is no longer generation. It's verification."), Fung (`blog-anthropic-ai-native-engineering-org.md` Claim 1: verification/code review/security replaced code-writing as the bottleneck), and Shopify (cited in Fung's note as also identifying code review as the post-adoption bottleneck). Endava's variant names a *different* downstream destination — requirements/business-analysis/planning/stakeholder-coordination — rather than verification/code-review. This is not a contradiction (a consulting-delivery firm's bottleneck plausibly differs from a product engineering team's, and both migrations can be true simultaneously — the bottleneck moves to wherever judgment work remains uncompressed), but it is a distinct data point: it extends the "bottleneck migrates upstream, not just downstream to review" observation, which the existing corpus (Osmani, Fung, Shopify) frames primarily as a downstream (verification/review) migration.

### Claim 5: AI is embedded throughout Endava's entire "DavaFlow" delivery lifecycle, from meeting preparation through deployment
- **Evidence**: Direct statement plus a supporting block quote from Cloke.
- **Confidence**: anecdotal (a branded internal methodology name with a sweeping claim of total coverage; no phase-by-phase detail provided)
- **Quote**: "Today, OpenAI technology is embedded throughout the entire DavaFlow lifecycle—from meeting preparation and business planning to product discovery, software engineering, and deployment." followed by the block quote: "There isn't a part of DavaFlow that doesn't use OpenAI technology."
- **Our assessment**: "DavaFlow" is a named, branded internal delivery methodology not previously present anywhere in our corpus. The claim of *total* lifecycle coverage is a strong, unqualified assertion with no supporting detail (no named phases, no per-phase tooling description, no adoption percentage) — the article does not describe what DavaFlow's phases actually are beyond the five named touchpoints in the sentence itself. Treat this as evidence that a phase-by-phase-integrated methodology exists and is branded, not as evidence of depth or effectiveness at any given phase.

### Claim 6: AI adoption expanded beyond engineering into legal, project management, and commercial/sales teams, each with a distinct use case
- **Evidence**: Three named functional use cases: legal teams using AI for research and documentation workflows; project managers using Codex to generate governance reports and summarize engineering progress; commercial teams replacing spreadsheet-heavy planning with lightweight AI-generated applications.
- **Confidence**: anecdotal (named functional categories with no quantitative adoption data, single-company account)
- **Quote**: "Legal teams began using AI to streamline research and documentation workflows. Project managers started using Codex to generate governance reports and summarize engineering progress. Commercial teams replaced spreadsheet-heavy planning exercises with lightweight AI-generated applications."
- **Our assessment**: This is a concrete (if unquantified) account of cross-functional spread beyond engineering, corroborating the general "AI adoption starts in engineering, then spreads to adjacent functions" pattern in the corpus (e.g., the "surrounding work first" adoption pattern cited via `blog-anthropic-cowork-enterprise.md` in `blog-anthropic-building-enterprise-agents.md`'s Cross-References). The specific detail that PMs use *Codex* (a coding-agent product) for non-code artifacts (governance reports, progress summaries) is a notable use-case extension — it is the same tool, repurposed, rather than a separate non-coding product being deployed to PMs.

### Claim 7: A single internal pricing discussion replaced spreadsheet analysis with an AI-generated single-page interactive pricing app, changing the nature of the conversation
- **Evidence**: Named anecdote with a direct quote from Cloke.
- **Confidence**: anecdotal (a single internal anecdote, no detail on what the app did technically, who built it, or how long it took)
- **Quote**: "In one internal pricing discussion, employees skipped spreadsheets entirely and instead built a single-page pricing app teams could interact with immediately." followed by Cloke's quote: "It changed the conversation completely."
- **Our assessment**: This is the article's most concrete, specific artifact — a named example of "commercial teams replaced spreadsheet-heavy planning... with lightweight AI-generated applications" (Claim 6) made tangible. It illustrates the "process compression" pattern already named in `blog-anthropic-building-enterprise-agents.md` Claim 4 (pillar 3: "condensing information-dense processes"), though this anecdote describes a *format* change (spreadsheet → interactive app) rather than a *step-count* reduction, which is a specific mechanism that note's "process compression" pillar does not itself illustrate with an example this concrete.

### Claim 8: Leadership teams use agents for asynchronous, background coordination work — summarizing projects, automating communications, and managing inboxes
- **Evidence**: Direct statement describing a leadership-level usage pattern, without a specific named example or executive attribution beyond the general "leadership teams" framing.
- **Confidence**: anecdotal (a general description with no specific example, metric, or individual attribution)
- **Quote**: "AI agents have also become embedded in day-to-day operations. Leadership teams use agents to summarize projects, automate communications, manage inboxes, and coordinate work asynchronously."
- **Our assessment**: This corroborates Fung's "automate recurring information requests" reflex (`blog-anthropic-ai-native-engineering-org.md` Claim 5 — the customer-feedback-channel-summary example) at the leadership-team level rather than the individual-engineer level, but offers no comparable concrete example (Fung names a specific automated task; this claim stays at the level of category description: "summarize," "automate," "manage," "coordinate").

### Claim 9: Endava has established AI fluency as an explicit part of hiring and promotion expectations company-wide
- **Evidence**: Listed as one of five bullet points under "Results at a glance."
- **Confidence**: anecdotal (a stated policy outcome with no detail on how "AI fluency" is defined, assessed, or weighted in hiring/promotion decisions)
- **Quote**: "Established AI fluency as part of hiring and promotion expectations across the company"
- **Our assessment**: This is a company-wide policy claim (all roles, not just engineering), which is a broader scope than the engineering-specific hiring-philosophy shift Fung describes in `blog-anthropic-ai-native-engineering-org.md` Claim 9 (de-emphasizing raw throughput, prioritizing product sense and systems expertise for the Claude Code engineering team specifically). The two are not directly comparable — different company, different role scope, and Endava's claim gives no detail on *what* fluency criteria changed — but both are examples of AI usage becoming a formal hiring/promotion input rather than an optional skill, worth noting as a second, independent instance of that pattern.

### Claim 10: Endava's next phase of enterprise AI is "orchestration" — combining models, agents, workflows, and human expertise into integrated systems that reshape how the organization operates, with AI becoming "the operating model itself" rather than a productivity layer
- **Evidence**: Forward-looking framing attributed to Endava's stated view as an OpenAI partner, plus a closing quote from Cloke.
- **Confidence**: anecdotal (a forward-looking strategic framing/prediction, not a description of anything currently implemented)
- **Quote**: "As a long-term OpenAI partner, Endava sees the next phase of enterprise AI centered around orchestration—combining models, agents, workflows, and human expertise into integrated systems that fundamentally reshape how organizations operate." followed by: "From reasoning models and Codex agents to automation and enterprise-scale collaboration, Endava believes AI is becoming more than a productivity layer. It's becoming the operating model itself."
- **Our assessment**: This "productivity layer → operating model" framing is aspirational vendor-partner rhetoric (both OpenAI's and Endava's incentive is to describe AI adoption as maximally transformative) rather than a description of a currently operating system. It uses "orchestration" in the organization-of-work sense (combining models/agents/workflows/humans into integrated systems), which is a different sense of the term than the technical "orchestrator mode" (async, goal-handoff usage) defined in `blog-addyosmani-new-software-lifecycle.md` Claim 15 — readers should not conflate the two uses of "orchestration" across these sources.

## Concrete Artifacts

```
Source: OpenAI, "How Endava is redesigning software delivery around AI agents,"
https://openai.com/index/endava-frontiers (published 2026-06-04)

"Results at a glance" (verbatim bullet list, no supporting numbers given):
- Accelerated software delivery by integrating AI agents into engineering workflows
- Expanded AI adoption beyond engineering into legal, finance, and operations teams
- Reduced manual reporting and coordination work through AI-assisted workflows
- Enabled teams to build internal tools and applications without dedicated engineering support
- Established AI fluency as part of hiring and promotion expectations across the company

"Lessons learned from Endava" (verbatim bullet list, framed as principles that
"emerged" as Endava rolled AI out across its 11,000-person global workforce):
- Treat AI adoption as a behavior change, not a software rollout
- Leaders need to actively use AI to drive organization-wide adoption
- Create space for experimentation—even when outcomes are imperfect
- Bring non-technical teams into the process early, not later
- Hands-on experience is the fastest way to overcome skepticism
- Make AI part of everyday workflows, not a separate initiative
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5 and `blog-anthropic-ai-native-engineering-org.md` Claim 1: the "bottleneck moves once engineering output stops being the constraint" thesis. Claim 4 here is a fourth independent account of this pattern, though it names a different downstream location (requirements/business-analysis/planning) than Osmani's and Fung's verification/code-review destination.
  - `blog-anthropic-building-enterprise-agents.md` Claim 1 (the "agentic thinking divide" — organizations that embed AI into workflows/processes vs. those that treat it as incremental improvement): Endava's "make AI part of everyday workflows, not a separate initiative" lesson (Concrete Artifacts, lessons-learned list) and Claim 1 here ("AI to solve the problem first... first thing you do rather than the last thing") are a second, independently-sourced (different vendor, different company) restatement of the identical embedding-vs-bolt-on distinction.
  - `blog-anthropic-building-enterprise-agents.md` Claim 4 (pillar 3, "process compression... while maintaining human oversight"): the pricing-app anecdote (Claim 7 here) is a concrete illustration of process compression that the Anthropic post's own pillar 3 does not itself provide an example for.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 5 (the "always ask if this can be automated" reflex) and Claim 9 (hiring de-emphasizing raw throughput in favor of judgment-heavy profiles): Claims 2, 8, and 9 here are each a company-external, independently-sourced parallel to one of Fung's Anthropic-internal claims — an agent-always-running personal habit, leadership-level task automation, and AI fluency as a formal hiring/promotion input, respectively.

- **Contradicts**: None filed. The one candidate tension — Endava's single-vendor (OpenAI-only) enterprise platform strategy (Claim 3) versus Shopify's deliberate multi-tool policy in `blog-bvp-shopify-ai-playbook.md` — is a conditioning-variable difference (different company type and scale, not opposing evidence about what strategy works), not a factual disagreement that would drive opposite guide advice, so per MINER.md 4a this was not filed as a contradiction issue.

- **Extends**:
  - `blog-anthropic-ai-native-engineering-org.md`: extends Fung's single-organization (Anthropic, ~engineering-team-scale) account of bottleneck migration, automation habits, and hiring-philosophy shift with a second, much larger (11,000-person, non-AI-native-by-default) organization independently reporting parallel patterns.
  - `blog-anthropic-building-enterprise-agents.md`: extends that note's "agentic thinking divide" and "process compression" pillars — both introduced there without a concrete example — with Endava's pricing-app anecdote and lessons-learned list as illustrative material.

- **Novel**:
  - "DavaFlow" as a named, branded, claimed-total-coverage delivery lifecycle (Claim 5) is new to the corpus — no existing source names an internally-branded delivery methodology with this scope of claimed AI integration.
  - The specific bottleneck-migration destination named here (requirements gathering, business analysis, planning, stakeholder coordination) is a new variant of the bottleneck-shift thesis, distinct from the verification/code-review destination the corpus has previously documented (Claim 4).
  - Endava itself, as a large (~11,000-person) IT-services/consulting-delivery firm, is a new organizational category for the corpus — prior enterprise-adoption sources cover product companies (Shopify), a research lab building its own tool (Anthropic/Fung), or unnamed case-study companies (L'Oréal, Lyft, Rakuten in `blog-anthropic-building-enterprise-agents.md`, none with workflow detail). This is the first source with narrative detail specifically about a consulting/delivery-services organization.

## Guide Impact

- **Chapter 05/06 (Team Adoption / Organizational Design)**: Add Claim 4 (bottleneck migrating to requirements/business-analysis/planning/stakeholder coordination) as a fourth data point in the "the bottleneck moves once code generation is no longer the constraint" convergence argument, explicitly noting that this source names a different downstream destination than the verification/code-review destination named by Osmani, Fung, and Shopify — the guide should present bottleneck migration as multi-directional (upstream to specification/planning as well as downstream to review/verification) rather than implying a single universal destination.
- **Chapter 05/06 (Team Adoption)**: Add the "Lessons learned from Endava" six-item list (Concrete Artifacts) as a second, independently-sourced corroboration of "AI adoption is a behavior change, not a software rollout" and "leaders must use AI themselves to drive adoption," alongside the existing `blog-anthropic-building-enterprise-agents.md` "agentic thinking divide" framing — note both sources are vendor-adjacent (one OpenAI customer story, one Anthropic first-party post) and neither provides a measurement methodology.
- **Chapter 05/06 (Team Adoption)**: Add the pricing-app anecdote (Claim 7) as a concrete example for any section discussing "process compression" or spreadsheet-to-app workflow collapse — currently `blog-anthropic-building-enterprise-agents.md`'s process-compression pillar has no worked example; this one is small but specific.
- **Chapter 01 (Daily Workflows)**: Cloke's "always have an agent running in the background" quote (Claim 2) is a quotable executive-level illustration of the "agent-first" personal habit, usable alongside Fung's automation-reflex material, with the caveat that it is a personal anecdote from one executive, not a team-wide measured practice.
- Given the article's thinness (no quantitative outcome data anywhere), none of these claims should be cited as evidence of *effectiveness* — only as evidence that a large, non-tech-native organization reports adopting these patterns and these specific narrative frames.

## Extraction Notes

- The live URL returned HTTP 403 to both the WebFetch tool and direct `curl` with a browser user-agent (Cloudflare-style bot protection, consistent with prior OpenAI-domain extractions in this corpus — see `blog-openai-codex-knowledge-work.md`'s Extraction Notes). Full text was retrieved via the `r.jina.ai` text-extraction proxy (`https://r.jina.ai/https://openai.com/index/endava-frontiers`), which returned clean Markdown matching the page's visible content; no Wayback Machine snapshot was needed for this source.
- The article contains no internal links to other substantive pages (checked both the raw HTML block-page response and the jina-extracted Markdown for outbound URLs) — this is a short, standalone customer-story page. No linked sub-pages were followed because none exist.
- The article is genuinely short (~700 words) and thin on quantitative evidence — every sentence in the article's body is reflected in one of the ten claims above; this is not a case of shallow reading but a source with limited depth. All ten claims are anecdotal or vendor-framed; none rise above `emerging` (Claim 4, on the strength of independent corroboration elsewhere in the corpus, not on this article's own evidentiary weight).
- One of the Prospector's two triage comments on this issue describes Endava as "a 60k+ person consulting and engineering firm," while the article itself states Endava's workforce as "11,000-person global workforce." This note uses the article's own figure (11,000) since that is what the source actually says; the Prospector's larger figure could not be corroborated from this source and may reflect a different (or outdated, or conflated) headcount estimate. Flagging this discrepancy for visibility rather than silently picking one number.
- No contradiction issue was filed. The one candidate tension considered (single-vendor platform choice here vs. Shopify's multi-tool policy) was judged to be a conditioning-variable difference, not a factual disagreement — see Cross-References → Contradicts for full reasoning.
- All cross-reference claim numbers cited above (from `blog-addyosmani-code-agent-orchestra.md`, `blog-anthropic-ai-native-engineering-org.md`, `blog-anthropic-building-enterprise-agents.md`, `blog-addyosmani-new-software-lifecycle.md`, and `blog-bvp-shopify-ai-playbook.md`) were verified by re-reading each cited note's actual claim numbering before writing this note; none were guessed.
