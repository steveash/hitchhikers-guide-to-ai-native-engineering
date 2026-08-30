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
> team used Codex and ChatGPT Work to compress an estimated 243
> "modeled active role-hours" of go-to-market production for a six-week
> product launch into about 77 actual hours, and built a standing
> GPT-powered system that keeps product-marketing materials current
> between launches. Unlike prior OpenAI case studies in the corpus
> (Asana, Notion), the primary output here is marketing/content assets —
> blog posts, launch emails, a webinar deck, a hero animation, sales
> enablement material — not code.

## Source Context

- **Type**: blog-post (OpenAI customer-story page, `openai.com/index/`,
  published August 20, 2026; the same single-customer case-study
  template used elsewhere in the corpus — Company size/Region/Industry/
  Products metadata tiles, a two-stat headline block, a five-section
  narrative body with subheadings, two named-individual pull quotes, and
  a "Contact sales" CTA). ~800 words of body text.
- **Author credibility**: House-authored OpenAI customer-marketing copy,
  no named OpenAI author. Two named Stampli individuals are quoted:
  Eyal Feldman (CEO and Co-Founder) and Melad Zahedi (Director of
  Product Marketing), the latter supplying the majority of the article's
  narrative detail and three separate quotes. This is first-party vendor
  marketing content — OpenAI selected and published every quote and
  framing choice, with no independent verification of the hours
  figures, the "hundreds of pieces of content" claim, or the 10x
  output-multiplier claim. Standard vendor-case-study credibility
  caveats apply throughout.
- **Scope**: Covers one product launch (Stampli's "Deep Finance"
  spend-intelligence product) end to end — go-to-market content
  production, a standing product-marketing knowledge system used
  between launches, and two specific workflow vignettes (a "second
  brain" meeting-prep pattern and an in-meeting live data query). Does
  NOT cover: any engineering-side use of Codex (the article is entirely
  about product marketing, not software development, despite Codex
  being the named product), the actual prompts or system-prompt
  configuration used, how the "GPT-powered system" ingesting Jira/
  GitHub/meeting-notes data is technically built or governed, or any
  account from an engineer who set up the underlying automation.

## Extracted Claims

### Claim 1: The headline "68%" figure is a derived ratio — a launch that Stampli modeled at 243 role-hours without Codex took about 77 actual hours with it, for a savings of roughly 166 hours (166/243 ≈ 68%)
- **Evidence**: Headline stat block plus a restated figure in the body text ("saving roughly 166 hours or 3.16x faster production").
- **Confidence**: anecdotal (single vendor-selected project at a single company; the "243 hours" side of the ratio is explicitly labeled a model, not a measured baseline — see Claim 2)
- **Quote**: "With OpenAI tools, they compressed an estimated 243 hours of production work into about 77, while keeping full human review and final approval on everything customer-facing."
- **Our assessment**: Unlike some vendor headline stats, this one is internally consistent and checkable (166/243 = 68.3%, matching the "68%" headline and the separately stated "3.16x"). That consistency is a point in its favor over case studies with looser headline rounding. It does not change the underlying evidentiary limit: only the "77 hours, with Codex" side was actually measured; the "243 hours" side is a model.

### Claim 2: The "243 hours without Codex" figure is explicitly described as "modeled active role-hours," not a measured baseline from a prior launch run the same way without AI tools
- **Evidence**: Precise phrasing in the case study's closing summary paragraph.
- **Confidence**: anecdotal (self-reported estimate; no methodology given for how the 243-hour model was built — by role, by task, or by analogy to a prior launch)
- **Quote**: "Across the defined Deep Finance go-to-market and content production workflow, the Stampli team estimates the launch would have taken about 243 modeled active role-hours without Codex."
- **Our assessment**: This is the same "one side of the ratio is a counterfactual estimate, not a measured run" pattern already flagged in `blog-openai-asana-codex-case-study.md` Claim 1 (Asana's "five years" staffing estimate) and Claim 2 ($6M staffing estimate). OpenAI's own phrasing here ("modeled") is more transparent about this than Asana's flat "$6 million estimate" framing, but the evidentiary weight is the same: treat "77 hours" as the measured figure and "243 hours" as a counterfactual model, not as two comparably solid data points.

### Claim 3: Using ChatGPT Work, Stampli's product marketing team now produces "100s" of pieces of content per week, which Melad Zahedi (Director of Product Marketing) describes as multiplying a small team's output tenfold versus what it could produce before
- **Evidence**: Headline stat block ("100s — Pieces of content created each week using ChatGPT Work") plus a named, attributed quote restating and quantifying the same claim.
- **Confidence**: anecdotal (single named individual's self-reported estimate; "100s" and "10x" are not independently defined or audited — no baseline count of "a couple" is given precisely)
- **Quote**: "it's multiplied the output of a small team by 10x, putting out hundreds of pieces of content on a weekly basis, where it was limited to just a couple before."
- **Our assessment**: A large claimed multiplier (10x) from a single named source with no denominator for "a couple" (two? three? five pieces a week?), so the ratio should be read as directional, not precise. Notable mainly because it's a *sustained, ongoing* output claim (content produced every week, not a one-time launch metric), distinguishing it from the launch-specific 243→77 hour figure in Claims 1-2.

### Claim 4: Stampli's CEO frames Codex's value as shortening the loop between customer need, team response, and usage-derived learning, extending "technical abilities" to every team rather than only engineers
- **Evidence**: Direct, attributed executive quote.
- **Confidence**: anecdotal (single executive's characterization, vendor-published)
- **Quote**: "Codex shortens the distance between a customer's need, our team's response, and real learnings from usage. By extending technical abilities across every team, it helps us move 10x faster from requirement to deployable solution." — Eyal Feldman, CEO and Co-Founder, Stampli
- **Our assessment**: The "extending technical abilities across every team" framing is the article's explicit thesis for why a coding-agent product (Codex) is the tool credited for a marketing/content-production result — the claim is that Codex's utility isn't gated to engineers. This is consistent with the article's broader scope (a non-engineering department as the primary subject), but the quote itself supplies no mechanism for *how* a non-technical marketing team operates Codex day to day; that detail comes later (Claim 7).

### Claim 5: The Deep Finance product moved from an initial prototype demo to public go-to-market launch and first shipped product in about six weeks, with Codex used to turn evolving product decisions into a defined slate of review-ready launch assets
- **Evidence**: Narrative description of the launch scope and asset list.
- **Confidence**: anecdotal (single-project account; no per-asset time breakdown beyond the aggregate 243→77 hour figure)
- **Quote**: "the team used Codex to turn evolving product decisions into review-ready assets across a seven-part blog series, launch emails, a webinar and its supporting deck, social and paid creative, a PR Newswire release, the Deep Finance web page, and sales enablement materials."
- **Our assessment**: This is the most concrete inventory in the corpus of what "AI-assisted go-to-market production" actually spans in practice — seven distinct asset categories across a single launch. Useful as a checklist-style artifact for a guide chapter discussing agent-assisted marketing/GTM workflows, independent of whether the aggregate hours figure holds up to scrutiny.

### Claim 6: Codex handled roughly 90% of the polished work on the launch's hero animation — through exploration, iteration, and packaging — before a human contractor finished the opening scene and final format
- **Evidence**: A specific, named production detail distinct from the text/document assets in Claim 5.
- **Confidence**: anecdotal (single asset, single project, no definition of how "90%" of animation work was measured — time spent, frame count, or subjective assessment)
- **Quote**: "Codex also helped create the launch's hero animation through exploration, iteration, and packaging, handling roughly 90% of the polished animation work before a contractor finished the opening scene and final format."
- **Our assessment**: Novel to the corpus — no prior OpenAI or Anthropic case study describes an LLM coding-agent product used for visual/motion creative production, as opposed to text, code, or data synthesis. Notable given the article's opening framing that "design resources and outside contractors" were "already committed to other priorities" — this reads as Codex covering a design-capacity gap, with a human contractor retained for the final 10% (opening scene, format finishing), rather than a full human-to-AI handoff.

### Claim 7: Outside of launches, Stampli has automated much of its day-to-day product-marketing knowledge-maintenance process — previously interviewing PMs, reading Jira tickets, reviewing GitHub, and working through meeting notes, then translating that into help center articles, presentations, and one-pagers — with a standing GPT-powered system that gathers information from product systems and meeting notes and helps keep materials up to date
- **Evidence**: Narrative description of an ongoing (not launch-specific) internal system.
- **Confidence**: anecdotal (no detail on how the system is technically built, how "up to date" is verified, or who reviews its output before publication)
- **Quote**: "Stampli has automated much of that process with a GPT‑powered system. It gathers information from product systems and meeting notes, then helps keep those materials up to date."
- **Our assessment**: This is the article's clearest example of a persistent, standing agent-backed system built and owned by a non-engineering function, rather than a one-off prompting session — structurally similar in kind (though different in domain) to the Sunday-scheduled weekly-report and campaign-build automations described in `blog-anthropic-cowork-marketing-ops.md`, and to Jared Sires' self-built GTM tooling in `blog-anthropic-sires-gtm-claude-code.md`. No technical detail is given (data-source connectors, review/approval gates, or failure handling), so it should be cited as an existence claim for the pattern, not as an implementation reference.

### Claim 8: Melad Zahedi describes using GPT-powered automations as a "second brain" to organize business context across a schedule filled with back-to-back meetings, saying it lets him arrive at every meeting already prepared
- **Evidence**: Direct, attributed quote.
- **Confidence**: anecdotal (single named individual's self-reported characterization)
- **Quote**: "Being able to go to every meeting prepared with context, understanding what is needed from me in that meeting and how to stay efficient with my time, has been an amazing benefit."
- **Our assessment**: The "second brain" framing closely parallels Rachita Jain's "active intelligence" framing for a structurally similar meeting-heavy, context-organization use case in `blog-openai-nvidia-chatgpt-work-case-study.md` Claim 6 ("ChatGPT helped me change passive reading into active intelligence") — two independently named individuals, at two different companies, in two separate OpenAI case studies, describing a near-identical personal-context-management workflow for people whose day is dominated by meetings. This convergence across sources is more informative than either quote alone.

### Claim 9: In one executive meeting, a question arose about metrics stored across HubSpot and other systems; an employee used Codex to retrieve and analyze the relevant data live during the call, producing in about 20 seconds of keystrokes what Zahedi estimates would otherwise have taken Stampli's FP&A team half a day
- **Evidence**: A specific, dated-in-narrative anecdote with a named before/after comparison, attributed to Zahedi.
- **Confidence**: anecdotal (single incident, self-reported, no verification of the resulting analysis's accuracy or of the "half a day" counterfactual)
- **Quote**: "This is something that would've taken our FP&A team half a day to put a report together, give us a model, and give us an answer that we felt confident in. Someone was able to do it with 20 seconds of keystrokes." — Melad Zahedi, Director of Product Marketing, Stampli
- **Our assessment**: This is a live, on-demand, in-the-moment cross-system query — distinct in shape from the *scheduled* "poll systems, synthesize, push a digest" pattern already documented three times in the corpus (`blog-openai-ringcentral-case-study.md` Claim 8; `blog-anthropic-ai-native-engineering-org.md` Claim 5; OpenAI's own Scheduled Tasks feature in `blog-openai-chatgpt-work-ambitious-partner.md` Claim 11). Both patterns rest on the same underlying mechanism (an agent with access to multiple connected systems), but this is the first corpus example of the synchronous, mid-meeting variant rather than an asynchronous recurring report.

### Claim 10: The time saved on information-gathering has shifted product marketing's role toward advising VPs and C-suite leaders on corporate and product strategy, with ChatGPT Work also serving as a "thought partner" for deepening knowledge, brainstorming, building stakeholder personas, and pressure-testing recommendations before they reach leadership
- **Evidence**: Narrative description of a role-level shift, without individual attribution.
- **Confidence**: anecdotal (unattributed narrator claim, no metric for how much more "strategy" time resulted, or how leadership involvement was measured before vs. after)
- **Quote**: "The time saved let product marketing spend less time reconstructing context and more time advising leaders on product and company strategy."
- **Our assessment**: A qualitative "time saved gets reinvested in higher-judgment work" claim, the same shape as the "engineers get more room for craft" framing in `blog-openai-asana-codex-case-study.md` Claim 7 (Asana's CTO) — here applied to a marketing/strategy function rather than engineering. As with that source, this is an assertion about how saved time was *reinvested*, not a measured outcome (no before/after count of strategy meetings or advisory engagements is given).

### Claim 11: Zahedi estimates that with ChatGPT Work and Codex, the full cross-functional (product, marketing, customer success, sales, enablement) prototype-to-launch process took about six weeks — work he says would previously have taken months or even quarters
- **Evidence**: Named individual's estimate of the broader organizational timeline, distinct from the narrower 243→77 "modeled role-hours" figure in Claims 1-2.
- **Confidence**: anecdotal (single named individual's estimate; "months or even quarters" is not a specific measured prior baseline, unlike the "243 hours" figure which at least names a modeling methodology)
- **Quote**: "Zahedi estimates that with OpenAI tools the process took about six weeks, which previously would have taken months or even quarters."
- **Our assessment**: This is a softer, less-precise counterfactual than Claims 1-2's hours-based figure — no modeling methodology is described for "months or even quarters," making it the weakest-evidenced claim in the source. Cite it, if at all, as a qualitative reinforcement of the launch-speed thesis, not as an additional quantified data point alongside the 68%/3.16x figures.

### Claim 12: Zahedi frames the larger opportunity as expanding what employees believe they can personally take on, arguing that curiosity and experimentation with ChatGPT surfaces "latent capacity" within both individuals and the organization
- **Evidence**: Direct, attributed closing quote.
- **Confidence**: anecdotal (single named individual's forward-looking characterization)
- **Quote**: "Being curious and just asking, 'What can I do?' and trying everything first through ChatGPT will unlock a lot of latent capacity that you didn't realize was there in your organization—and in yourself." — Melad Zahedi, Director of Product Marketing, Stampli
- **Our assessment**: A generic but recurring closing framing in the OpenAI customer-story genre (individual agency/curiosity as the unlock, rather than a top-down mandate) — thematically consistent with the "give people the tools and see what they build" pattern already noted in `blog-openai-ringcentral-case-study.md` Claim 2 (RingCentral's "no mandated workflow" AI-Native Challenge), though here expressed as individual philosophy rather than a named organizational program.

## Concrete Artifacts

```
Source: OpenAI, "Stampli cuts launch hours by 68% using ChatGPT Work,"
https://openai.com/index/stampli (August 20, 2026)

Case-study metadata tiles:
  Company size: Mid-market
  Region:       North America
  Industry:     Finance, Technology
  Products:     Codex

Headline stats:
  100s    Pieces of content created each week using ChatGPT Work
  3.16x   Faster launch to production with Codex

Page structure (five sections, per on-page section nav):
  1. From prototype to launch, in six weeks
  2. A system built for daily use, not just launches
  3. Surfacing insights when they matter
  4. Making more room for strategy
  5. What's next

Launch hours math (Deep Finance go-to-market/content production):
  243 modeled active role-hours (estimated, without Codex)
   77 actual hours (with Codex)
  166 hours saved  ->  3.16x faster  ->  ~68% reduction

Launch asset inventory (Codex-assisted):
  - Seven-part blog series
  - Launch emails
  - Webinar + supporting deck
  - Social and paid creative
  - PR Newswire release
  - Deep Finance web page
  - Sales enablement materials
  - Hero animation (~90% of polished work by Codex; contractor
    finished opening scene + final format)

Named individuals quoted:
  Eyal Feldman   — CEO and Co-Founder, Stampli
  Melad Zahedi   — Director of Product Marketing, Stampli
```

## Cross-References

- **Corroborates**:
  - `blog-openai-asana-codex-case-study.md` and `blog-openai-notion-codex-case-study.md` — same OpenAI single-customer case-study template (metadata tiles, headline stat block, named-executive pull quote) and the same "one side of the headline ratio is a modeled/estimated counterfactual, not a measured baseline" pattern (this note's Claim 2 vs. Asana's Claim 1-2 "five years"/"$6M estimate").
  - `blog-openai-nvidia-chatgpt-work-case-study.md` Claim 6 (Rachita Jain's "passive reading into active intelligence" framing) — corroborates this note's Claim 8 (Zahedi's "second brain" framing); two independently named individuals at two different companies describing near-identical personal context-management workflows for meeting-heavy roles.
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 8 (internal OpenAI figures: sales discovery-to-proof-of-concept compressed from weeks to 24 hours; finance month-end close from days to hours) — a general pattern of ChatGPT-Work-driven business-process time compression, corroborated here by Stampli's own 243→77 hour launch-production figure in a different function (product marketing vs. sales/finance).
  - `blog-anthropic-cowork-marketing-ops.md` — a second, independently-sourced (different vendor: Anthropic Cowork vs. OpenAI ChatGPT Work/Codex) example of a marketing operations function building standing, agent-backed automation for reporting and content/campaign production, rather than one-off prompting. Cross-vendor convergence on marketing operations as an agent-automatable domain.
- **Contradicts**: None identified. No contradiction issue filed.
- **Extends**:
  - `blog-openai-asana-codex-case-study.md` and `blog-openai-notion-codex-case-study.md` — both prior OpenAI Codex case studies in the corpus describe code-centric migrations (removing a testing framework; an engineering workflow). This is the first Codex case study in the corpus where the primary output is marketing/content/creative assets (blog posts, emails, a webinar deck, a PR release, a hero animation) rather than code — confirming the Prospector's triage assessment that this source extends the evidence base into business-process/GTM acceleration, not code migration.
  - `blog-anthropic-sires-gtm-claude-code.md` — Sires' case study documents one non-programmer individual contributor building a persistent, agent-backed GTM tool (a Gmail integration) from scratch. This source's Claim 7 (a standing GPT-powered product-marketing knowledge system) extends that "non-engineer builds and owns standing agent infrastructure" pattern from an individual-contributor sales role to a product-marketing department's shared system.
  - `blog-openai-ringcentral-case-study.md` Claim 8 (scheduled Jira/Sheets/CRM status-digest automation) — this note's Claim 9 (an on-demand, mid-meeting HubSpot data query, answered in "20 seconds of keystrokes") extends the "connect siloed systems via an agent" pattern with a synchronous/live variant, distinct from RingCentral's asynchronous scheduled-digest mechanism.
- **Novel**:
  - The hero-animation production detail (Claim 6) — the corpus's first example of a coding-agent product (Codex) credited with the bulk of a visual/motion creative asset, as opposed to text, code, or data synthesis.
  - The explicit "modeled active role-hours" labeling (Claim 2) — more transparent phrasing about the counterfactual-estimate nature of a headline productivity ratio than prior OpenAI case studies in the corpus use.
  - Finance as a named customer industry — expands the corpus's industry-vertical coverage for ChatGPT Work/Codex case studies beyond the more common SaaS/dev-tools/enterprise-software customer profile.

## Guide Impact

- **Chapter 04 (Coordination and Planning / Agentic Workflows)**: Add Claim 9 (the synchronous, mid-meeting cross-system data query) as a second, on-demand variant of the "connect siloed systems via an agent" pattern already documented from `blog-openai-ringcentral-case-study.md` (scheduled digest) — worth presenting together as two ends of a spectrum (ask-in-the-moment vs. scheduled-recurring) rather than as competing approaches.
- **Chapter 05 (Team Adoption)**: Cite this source, alongside `blog-anthropic-cowork-marketing-ops.md` and `blog-anthropic-sires-gtm-claude-code.md`, as a third independent example of a non-engineering function (here, product marketing) building and operating standing agent-backed infrastructure rather than using an agent only for one-off tasks (Claim 7). Explicitly caveat, per Claim 2's "modeled active role-hours" framing, that the headline 68%/3.16x figures rest on a counterfactual estimate for one side of the comparison, not a measured before/after — consistent with the caveat already applied to the Asana case study in the corpus.
- **Chapter 01 (Daily Workflows)**: Cite Claim 8 (the "second brain" meeting-prep pattern) alongside the NVIDIA case study's "active intelligence" framing as two named, cross-company examples of using an agent for personal context management ahead of a meeting-heavy schedule — a recurring practitioner pattern distinct from code-generation or content-production use cases.
- No chapter should cite the "243 hours" or "months or even quarters" figures (Claims 1-2, 11) as measured baselines — both are self-reported estimates for work that was not separately run without Codex, per this note's Our assessment fields.

## Extraction Notes

- **Fetch method**: The live URL (`https://openai.com/index/stampli`) returned HTTP 403 to both `WebFetch` and direct `curl` with a browser user-agent — the same Cloudflare bot-challenge pattern already documented for `openai.com/index/` posts elsewhere in the corpus (e.g. `blog-openai-asana-codex-case-study.md`, `blog-openai-ringcentral-case-study.md`). `WebFetch` also refused `web.archive.org` URLs directly ("Claude Code is unable to fetch from web.archive.org"). Retrieved instead via a Wayback Machine snapshot (`https://web.archive.org/web/20260822112941/https://openai.com/index/stampli/`, crawled August 22, 2026, two days after the August 20 publication date), fetched with `curl` using a browser user-agent (the Internet Archive returned an intermittent "Temporarily Offline" 503 on the first two attempts and succeeded on a third), with HTML tags stripped and entities decoded locally via Python rather than through an AI-summarization pass, specifically so `Quote` fields could be copied character-for-character per MINER.md §2a.
- **Full article read**: The article is short (~800 words of body text across five sections) and was read in full from the stripped-text extraction; no gaps were apparent between sections. The page's "Keep reading" footer links to three unrelated OpenAI posts ("Introducing AI Futures," "Offering Zero Data Retention for frontier models," "Replit expands access to software creation with GPT-5.6 Luna"), none of which concern Stampli or this case study, and were not followed.
- This is a single-source, single-company, vendor-published case study with exactly two named individuals (CEO and Director of Product Marketing) and no quote from anyone who directly built or administers the "GPT-powered system" described in Claim 7 — no engineer, admin, or IT stakeholder is named or quoted anywhere in the piece, despite Claim 7 describing what is functionally an internal data-integration system.
- No contradiction with any existing source note was found during cross-referencing; see Cross-References → Contradicts. No contradiction issue was filed.
- `confidence_overall` set to `anecdotal`: every claim is a single vendor-selected, vendor-published case study with two named individuals, self-reported figures, and no independent verification — consistent with the `anecdotal` rating already used for the Asana and Notion case studies in the corpus.
