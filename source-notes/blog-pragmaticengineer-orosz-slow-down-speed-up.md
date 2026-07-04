---
source_url: https://newsletter.pragmaticengineer.com/p/slow-down-to-speed-up
source_type: blog-post
title: "Slow down to speed up: so much has changed in 6 months' time"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-06-23
date_extracted: 2026-07-04
last_checked: 2026-07-04
status: current
confidence_overall: emerging
issue: "#1493"
---

# Slow down to speed up: so much has changed in 6 months' time

> A six-month "what's changed" retrospective (November 2025 → June 2026) built around Orosz's Craft
> Conference keynote: new insider detail on the Meta/Instagram account-takeover outage's organizational
> root cause, vendor data (Linear, Cursor) quantifying the jump in AI-authored code volume and the
> corresponding drop in human code review, and a company-by-company survey (Anthropic, OpenAI, Google,
> Uber, startups, Cisco, JPMorgan Chase) of how engineering orgs have restructured around agentic coding.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter, Substack; published June 23, 2026). Written
  companion/expansion of a Craft Conference keynote titled "Slow Down to Speed Up," delivered in
  Budapest three weeks prior. The post is a metered paywall: the first four of five listed sections —
  "Meta: 'AI psychosis' in effect?", "Everything's changed in six months," "How are tech companies
  changing how they work?", and the heading (but not body) of "Industry trends" — are freely
  accessible. The remaining sections ("Industry trends" body, "Trends across software," "Advice for
  software engineers and engineering leaders," and "Feedback") are gated behind "This post is for paid
  subscribers" and were not accessible to this extraction.
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager and author of The Pragmatic
  Engineer, described elsewhere in this corpus as a ~750k+ subscriber engineering newsletter (see
  `survey-pragmaticengineer-ai-tooling-2026.md`). This post draws on Orosz's own direct conversations
  with Meta/Instagram engineers, a March 2026 podcast interview with Boris Cherny (creator of Claude
  Code), a February 2026 Pragmatic Summit talk by Tibo Sottiaux (head of engineering, Codex, OpenAI),
  Orosz's own prior deep dive on Uber's AI developer infrastructure, and named third-party vendor data
  (Linear, Cursor). This is a higher-synthesis piece than a single-source interview: it aggregates
  several first-party accounts Orosz collected directly, plus quoted outside commentators (Simon
  Willison, DHH).
- **Scope**: Covers the Meta outage's newly reported organizational cause, aggregate industry metrics
  on AI-authored code volume and review practices, and per-company summaries of how Anthropic, OpenAI,
  Google, Uber, startups, and "traditional" companies (Cisco, JPMorgan Chase) have restructured
  engineering workflows around agents. Does NOT cover (in the accessible portion): the "Industry
  trends" bullet list itself, quality-degradation trends ("Trends across software"), or the
  prescriptive "Advice" section — all paywalled.

## Extracted Claims

### Claim 1: The Meta/Instagram account-takeover outage was caused not just by an architectural gap but by AI-generated, AI-reviewed code shipping through a security org gutted by layoffs and forced reassignment to AI-labeling work
- **Evidence**: Orosz reports direct conversations with Meta/Instagram engineers conducted in the two days between the outage's disclosure and the Craft Conference keynote.
- **Confidence**: emerging (first-party sourcing — Orosz states he spoke directly with Meta/Instagram engineers — but attributed to unnamed sources, not documents or named individuals)
- **Quote**: "Engineers at the company there told me this disaster was caused by AI-generated, AI-reviewed code, along with layoffs, and by forced reassignments from Integrity teams and elsewhere onto AI labeling and related duties."
- **Our assessment**: This is genuinely new information, not previously in the corpus. `failure-meta-ai-instagram-account-takeover.md` (sourced from Simon Willison summarizing 404 Media) documents the *mechanism* of the failure (a support bot with no ownership verification, one-shot account recovery) but has no information on *why* that gap existed or *how* the specific change shipped. This source adds the missing organizational cause: the change was itself AI-generated and AI-reviewed, with no human in the loop, at a company that had simultaneously stripped headcount from the org responsible for catching exactly this kind of regression. This reframes the incident from "a bot had a a dangerous capability" to "a bot had a dangerous capability, and the org that should have caught the change enabling it had been hollowed out."

### Claim 2: Meta's Integrity/security-adjacent teams suffered outsized headcount cuts relative to the rest of the org — Instagram design -44%, Developer Documentation and Support -95%, Trust and Safety -50% to labeling and layoffs
- **Evidence**: Orosz reports these as follow-up details learned after publishing a prior deep dive on the same incident, sourced to internal Meta/WhatsApp/Instagram contacts.
- **Confidence**: anecdotal (specific percentages attributed to internal sources, not to a public Meta disclosure or leaked document; the "goes beyond 'just' labeling" framing for the ADO group is Orosz's own characterization, not a quoted figure)
- **Quote**: "Instagram's design team suffered a 44% cut in headcount during layoffs" and "The Developer Documentation and Support team had a full 95% headcount reduction during layoffs."
- **Our assessment**: These are concrete, checkable-in-principle numbers (unlike vague "layoffs happened" framing) and they corroborate Claim 1's structural argument: it is not merely that *a* team was cut, but that specifically the review/documentation/trust functions were cut hardest while AI labeling absorbed the reassigned staff. Treat as anecdotal pending independent confirmation — no public Meta HR disclosure is cited.

### Claim 3: DHH (creator of Ruby on Rails) reports that his own resistance to AI-written code, expressed as recently as summer 2025, was based on model capability limits that have since been resolved
- **Evidence**: Direct quote from David Heinemeier Hansson, dated by Orosz to January 2026.
- **Confidence**: anecdotal (single practitioner's self-reported before/after account; no independent verification of the underlying capability change, though DHH is a named, identifiable, technically credible source)
- **Quote**: "Just [in] summer 2025, I spoke with Lex Fridman about not letting AI write any code directly, but it turns out part of this resistance was simply based on the models not being good enough at the time! I spent more time rewriting what it wrote, than if I'd done it from scratch. That has now flipped."
- **Our assessment**: Notable because DHH is an outspoken, historically AI-skeptical voice — a reversal from him carries more weight than the same claim from an AI-tool vendor. The claim is self-report only (no benchmark, no diff of DHH's own repos before/after), so treat the *direction* (capability crossed a threshold that changed his cost-benefit calculus) as credible while treating the specific "now flipped" framing as anecdotal.

### Claim 4: Simon Willison (creator of Django) dates the inflection point in agent usefulness to models released in November 2025
- **Evidence**: Direct quote, dated by Orosz to May 2026.
- **Confidence**: anecdotal (single practitioner's periodization, though it is a specific, falsifiable claim about timing rather than a vague "AI got better")
- **Quote**: "The models released in November 2025 elevated agents to being genuinely useful. We've had six months to get used to that idea now; it's no wonder companies are beginning to spend real money on this technology."
- **Our assessment**: This gives the corpus a specific inflection date (November 2025, i.e. the Opus 4.5 / GPT-5.4 generation named later in the same article) that multiple independent voices in this piece (DHH, Willison, the Linear/Cursor data) converge on. Useful as a periodization anchor for the guide: sources dated before November 2025 describe a materially different agent-capability regime than sources dated after.

### Claim 5: Teams using AI agents now ship 5x as many pull requests as they did two years ago, per Linear's own product data
- **Evidence**: A chart sourced to Linear, comparing PR counts for teams using AI agents with Linear vs. teams that don't.
- **Confidence**: emerging (named vendor, first-party usage data, but Linear is not a neutral third party — it is measuring usage of features it sells, and the comparison groups' selection method is not described)
- **Quote**: "Teams using agents now ship 5x as many pull requests as two years ago."
- **Our assessment**: A 5x PR-volume increase is a large, specific, checkable-in-principle claim, but it says nothing about PR *size* or *quality* in isolation — Claim 6 (PR size up 3x) means part of this "more PRs" trend is also "much bigger PRs," so the two stats should be read together, not as independent signals of pure throughput growth.

### Claim 6: Developers using AI harnesses are producing roughly 2.5x as much code as 18 months prior, and the size of individual pull requests is up roughly 3x over the same period, per Cursor's own usage data
- **Evidence**: Two charts sourced to Cursor: average lines of code added per user (rising from 3,500/month in January 2025 to 8,600/month by the article's June 2026 publication), and average PR size over the same 18-month window.
- **Confidence**: emerging (named vendor, first-party usage telemetry; Cursor is measuring its own users, which selects for engineers already comfortable with AI-heavy workflows, and no denominator/methodology for "average" is given)
- **Quote**: "Devs using AI harnesses are producing 2.5x as much code versus 18 months ago." and "The size of pull requests is up 3x versus 18 months ago."
- **Our assessment**: Consistent with Claim 5's PR-count growth, but the combination (more PRs, each 3x bigger) implies review load per reviewer has grown far faster than headcount could plausibly have scaled — which sets up Claim 7's finding that human review is the variable that gave way under that load, not review capacity.

### Claim 7: Cursor's own data shows a sharp rise in code changes being accepted with no human review at all, beginning around February 2026, coinciding with the Opus 4.7 / GPT-5.5 model generation
- **Evidence**: A chart sourced to Cursor showing the share of changes accepted without human review over time, with an inflection point dated to February 2026.
- **Confidence**: emerging (named vendor, first-party data with a specific dated inflection point tied to named model releases, but correlation with model launch dates is Orosz's inference, not a causal claim Cursor itself makes in the cited chart)
- **Quote**: "Data from Cursor shows a big jump in changes being accepted without human review from around February this year, when Opus 4.7 and GPT 5.5 launched" and "We're seeing a lot more code generated, and less of it than ever being reviewed by devs."
- **Our assessment**: This is the article's central empirical finding and the one most in tension with the rest of the corpus's verification-rigor guidance — see Cross-References/Contradicts below. Orosz explicitly links this trend to the Meta outage: "As per my discussions with Meta engineers, these kinds of AI-generated, AI-reviewed pull requests [at Meta, they're called diffs] are what caused the most recent, embarrassing outage at Instagram" — tying Claim 1's incident directly to this industry-wide review-erosion trend rather than treating Meta as an isolated case.

### Claim 8: At Anthropic, per creator-of-Claude-Code Boris Cherny (March 2026), PRDs have been replaced by prototypes, roughly 100% of Claude Code's own codebase was AI-generated, and 70-90% of code company-wide was Claude-generated
- **Evidence**: Orosz's written summary of specifics Cherny shared on the Pragmatic Engineer podcast in March 2026, presented as a bulleted list in the article.
- **Confidence**: emerging (specific, named-individual, on-the-record figures from the tool creator himself; self-reported by the company building the tool, so treat percentages as directional rather than externally audited)
- **Quote**: "Product requirement documents (PRDs) are dead & prototypes have replaced them inside Anthropic", "~100% of Claude Code was generated by Claude in March", and "~70-90% of code inside Anthropic was generated by Claude"
- **Our assessment**: The PRD-to-prototype shift is a concrete process claim (not just a code-generation percentage) that's actionable for a harness/workflow chapter: it implies Anthropic's own internal spec-writing step has been replaced by generating a working prototype directly, rather than a document describing one. The 70-90% company-wide figure is a wide range, suggesting either high variance across teams or imprecision in Cherny's own estimate — cite it as a range, not a point figure.

### Claim 9: Boris Cherny personally runs roughly five agents in parallel and ships 20-30 pull requests per day; Claude Cowork was built in 10 days
- **Evidence**: Same March 2026 podcast summary as Claim 8.
- **Confidence**: anecdotal (a single named individual's own personal workflow and a single product's build timeline — high-signal because Cherny is the creator of the tool in question, but not representative of typical usage)
- **Quote**: "He personally runs ~5x agents parallel, and ships 20–30 PRs/day" and "Claude Cowork – another billion-dollar product in terms of revenue potential – was built in just 10 days"
- **Our assessment**: Treat this as an upper-bound/power-user data point, not a typical-engineer baseline — it corroborates the general "parallel agent orchestration" pattern documented elsewhere in the corpus but should not be cited as what an average team should expect to achieve.

### Claim 10: OpenAI's Codex team has largely stopped writing code by hand, uses a tiered AI-code-review system where only higher-risk changes get human review, and treats "Taste" as a core skill for the role
- **Evidence**: Orosz's written summary of details shared by Tibo Sottiaux (head of engineering, Codex, OpenAI) at The Pragmatic Summit in February 2026, presented as a bulleted list.
- **Confidence**: emerging (named individual, named team, specific process description; self-reported by the team building the product, not independently audited)
- **Quote**: "AI code review for all code changes. With a tiered approach, some changes can be merged with just AI review, and more important ones need an extra human review", "Code isn't really written by hand anymore on the Codex team, and is also less common on other teams too", and "'Taste' is becoming a core skill for working at the company"
- **Our assessment**: The tiered-review model (some changes: AI-only; higher-stakes changes: AI + human) is a concrete, risk-stratified alternative to the all-or-nothing review erosion described in Claim 7 — it's an explicit design for *which* changes get human eyes, rather than human review simply falling off across the board. This is a useful counter-pattern for the guide to cite alongside Claim 7's warning: risk-tiering review effort, rather than uniformly reducing it, is what a deliberate response looks like.

### Claim 11: OpenAI's Codex team runs multiple agents in parallel per developer, to the point that developers physically prop laptop lids open so background agents don't get suspended by sleep mode
- **Evidence**: Same February 2026 Pragmatic Summit summary as Claim 10.
- **Confidence**: anecdotal (specific, vivid, and highly plausible behavioral detail, but a single secondhand description of team habits, not measured data)
- **Quote**: "Most devs run several agents in parallel, often walking around with their laptop lids open, so the machine doesn't enter sleep mode and suspend agents"
- **Our assessment**: This is a concrete, quotable artifact of what "parallel agent orchestration" looks like as lived practice, distinct from the abstract claim that people "run multiple agents." It's a small but telling operational detail — worth citing verbatim in a guide section on parallel-agent workflows precisely because it's so specific and unglamorous (a physical workaround for a laptop's power-management default fighting against a new work pattern).

### Claim 12: Google's Gemini is considered less capable at coding than Claude or Codex, as acknowledged by Google's own CEO, and this gap may be slowing Google's internal AI-adoption relative to Anthropic and OpenAI
- **Evidence**: Orosz's own assessment, referencing an acknowledgment from Google's CEO (not directly quoted).
- **Confidence**: anecdotal (the "hurting AI adoption compared to other companies" causal link is explicitly Orosz's own inference, not a data point)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Should be cited as Orosz's own interpretation, not as a Google-sourced admission of an adoption gap — the underlying "less capable" acknowledgment is attributed to Google's CEO, but the causal inference about adoption speed is the author's own analysis layered on top.

### Claim 13: Uber has built an extensive suite of in-house AI developer-infrastructure tools — MCP Gateway, Agent Builder, an AIFX command-line tool, a background-agent system called Minion, a risk-stratified PR triage tool called Code Inbox (with Smart Assignments and Risk Profiles features), an AI code review tool called uReview, and migration tools called Autocover and Shepherd — because no off-the-shelf tooling met their requirements
- **Evidence**: Orosz references his own prior in-depth reporting on Uber's AI developer infrastructure, summarizing the tool inventory with captioned screenshots in this article.
- **Confidence**: anecdotal (named company, named internal tools, but this article only summarizes/references a prior deep dive rather than presenting new primary evidence; the "couldn't find anything that worked up to requirements" framing is Orosz's own characterization)
- **Quote**: "Uber built all the tools above because they needed new, better ways to integrate AI agents into the developer workflow, but couldn't find anything that worked up to requirements."
- **Our assessment**: This is the most extensive named-company AI-tooling inventory in this article and is genuinely new to this corpus — no existing source note documents Uber's specific tool names (MCP Gateway, Agent Builder, AIFX, Minion, Code Inbox, uReview, Autocover, Shepherd) at this level of granularity. The pattern — a large company concluding it must build custom review/risk-triage tooling rather than buy it — is directly relevant to any guide discussion of build-vs-buy for AI-native developer infrastructure at scale. Because this article only summarizes a prior Orosz deep dive on Uber (not independently fetched here), treat the tool inventory as accurate-per-Orosz but not independently verified against Uber's own documentation.

### Claim 14: Startups are integrating AI agents into their workflows more directly but less elaborately than large companies, commonly wiring agents into Slack so developers can trigger bugfixes or small feature work directly from chat
- **Evidence**: Orosz's own summary of conversations with several unnamed startups conducted in preparation for the keynote.
- **Confidence**: anecdotal (unnamed companies, small and unspecified sample size, author's own characterization of a pattern across conversations)
- **Quote**: "I also noticed most startups are heavily integrating AI agents into Slack, so devs can kick off bugfixes or small feature requests straight from the chat tool."
- **Our assessment**: Directionally consistent with the general "startups adopt faster, less formally" pattern seen elsewhere in the corpus (e.g. the higher small-company Claude Code adoption rate in `survey-pragmaticengineer-ai-tooling-2026.md` Claim 6), but here the specific integration point named is Slack-as-trigger-surface rather than IDE/CLI-based usage — a distinct pattern worth naming separately.

### Claim 15: "Traditional" (non-tech-native) companies are adopting AI developer tools at meaningful scale — Cisco had roughly 18,000 developers using Codex for complex migrations, code review, and refactoring as of February 2026, and JPMorgan Chase built a multi-agent framework using specialized labeling agents plus judge agents to aggregate and rank annotation results
- **Evidence**: Orosz's summary of details shared by Laura Tacho at The Pragmatic Summit in San Francisco, presented as two distinct company examples.
- **Confidence**: anecdotal (secondhand, conference-talk-sourced figures for two named companies; no independent confirmation from Cisco or JPMorgan Chase)
- **Quote**: "In February, 18,000 Cisco developers used Codex for complex migrations, code review, and refactoring." and "JP Morgan Chase built a multi-agent framework for annotation, using multiple specialized agents to label customer interaction data, and judge agents to aggregate and rank results."
- **Our assessment**: Both are genuinely new named-company data points for this corpus — no existing source note documents Cisco's or JPMorgan Chase's AI-tooling adoption at this level of specificity. The "judge agents to aggregate and rank results" detail from JPMorgan Chase is a concrete example of a multi-agent evaluator/aggregator pattern (agents judging other agents' output) distinct from a simple single-agent pipeline, worth citing in any guide discussion of multi-agent architectures for data-labeling or annotation tasks.

## Concrete Artifacts

```
Section headings, in order (verbatim from the article's table of contents;
sections 1-3 fully accessible, remainder paywalled):

1. Meta: "AI psychosis" in effect?
2. Everything's changed in six months
3. How are tech companies changing how they work?
4. Industry trends [heading accessible; body paywalled]
5. Trends across software [paywalled]
6. Advice for software engineers and engineering leaders [paywalled]
7. Feedback [paywalled]

Source: newsletter.pragmaticengineer.com/p/slow-down-to-speed-up
```

```
Anthropic (Boris Cherny, March 2026 podcast, as summarized by Orosz):
- He personally runs ~5x agents parallel, and ships 20-30 PRs/day
- Product requirement documents (PRDs) are dead & prototypes have replaced
  them inside Anthropic
- ~100% of Claude Code was generated by Claude in March
- ~70-90% of code inside Anthropic was generated by Claude
- Claude Cowork - another billion-dollar product in terms of revenue
  potential - was built in just 10 days

OpenAI Codex team (Tibo Sottiaux, February 2026 Pragmatic Summit, as
summarized by Orosz):
- A "fix this" button integrated into the internal OpenAI mobile app makes
  one-shot fixes to bug reports, which devs review and can merge
- AI code review for all code changes, with a tiered approach: some changes
  merge with just AI review, more important ones need an extra human review
- Most devs run several agents in parallel, often walking around with their
  laptop lids open, so the machine doesn't enter sleep mode and suspend agents
- Code isn't really written by hand anymore on the Codex team, and is also
  less common on other teams too
- "Taste" is becoming a core skill for working at the company
- Codex improves itself: it runs its own test suite, runs improvement tasks
  overnight, and during team meetings it takes actions on topics discussed

Uber's named internal AI developer-infrastructure tools (as referenced by
Orosz, summarizing his own prior Uber deep dive):
- MCP Gateway
- Agent Builder (a no-code experience to build agents)
- AIFX (command line interface)
- Minion (background agents)
- Code Inbox, with Smart Assignments and Risk Profiles features
- uReview (AI code review tool, with usefulness ratings on AI comments)
- Autocover and Shepherd (for large-scale migrations)

Source: newsletter.pragmaticengineer.com/p/slow-down-to-speed-up
```

## Cross-References

- **Corroborates**:
  - `failure-meta-ai-instagram-account-takeover.md` Lesson 1 and Lesson 4: that note documents the
    architectural failure (no ownership verification, no human-in-the-loop for credential changes) and
    argues security review must evaluate blast radius per-capability, independent of model "safety."
    Claim 1 here supplies the missing organizational-cause half of the same incident: the specific
    change that exploited the architectural gap was itself AI-generated and AI-reviewed, shipped by an
    org stripped of the headcount that would normally catch it. The two notes describe the same
    incident from complementary angles (architecture vs. organizational cause) and should be read
    together.
  - `blog-pragmaticengineer-hightower-infrastructure-ai.md` Claim 4 (Kelsey Hightower's warning that
    "agents run loose on raw infra" without guardrails will cause damage at scale): Claim 13 here (Uber
    building an entire in-house tool suite — Code Inbox's Risk Profiles, uReview — specifically to
    triage and constrain AI-generated changes) is a concrete, large-company instance of exactly the
    guardrail-building Hightower's practitioner intuition calls for. Hightower supplies the warning;
    Uber's tool suite is the empirical response.
  - `survey-pragmaticengineer-ai-tooling-2026.md` Claim 6 (startups hit 75% Claude Code adoption vs.
    enterprise procurement lag): Claim 14 here (startups wiring agents directly into Slack for
    lightweight triggering) is consistent with that survey's finding that small companies adopt AI
    tooling faster and less formally than large ones — this article adds a specific integration pattern
    (chat-triggered agent work) to that general adoption-speed finding.

- **Contradicts**:
  - Filed as contradiction issue **#1510** — Claim 7 here (Cursor data showing a sharp, recent rise in
    AI-generated changes accepted with *no* human review, which Orosz directly links to the Meta
    outage) materially opposes `blog-pragmaticengineer-erez-cicd.md` Claim 10 (Robert Erez's prediction
    that AI code generation will shift CI/CD's optimization target toward *more and slower* tests as
    agents write more code). Both sources are from the same publication, six days apart; one is a
    forward-looking prediction from a CD-platform practitioner, the other is Orosz's own empirical
    synthesis of vendor data plus a production incident showing the opposite is currently happening.
    See issue #1510 for full framing; no verdict is asserted in this note — that is for human/Smith
    resolution per `CONTRADICTIONS.md`.

- **Extends**:
  - `survey-pragmaticengineer-ai-tooling-2026.md`: that February 2026 survey captured tool-adoption
    frequency and role-based usage patterns via a 906-respondent self-report survey. This June 2026
    article extends the same publication's coverage with company-specific process detail (Anthropic's
    PRD-to-prototype shift, OpenAI's tiered review, Uber's tool suite) that the survey's aggregate
    percentages could not capture, and adds four months of additional adoption runway.
  - `blog-pragmaticengineer-hightower-infrastructure-ai.md` Claim 1 (the imperative-to-declarative
    infrastructure paradigm shift as an analogy for AI's effect on software development, from a June 3
    2026 companion piece in the same newsletter): this article's Claim 4 (Willison dating the
    inflection point to November 2025 models) gives Hightower's more abstract historical analogy a
    specific date to anchor to.

- **Novel**:
  - **First corpus documentation of Uber's specific AI developer-infrastructure tool names** (MCP
    Gateway, Agent Builder, AIFX, Minion, Code Inbox with Smart Assignments/Risk Profiles, uReview,
    Autocover, Shepherd) — Claim 13.
  - **First corpus data point on Cisco's and JPMorgan Chase's AI-tooling adoption** — Claim 15,
    including the "judge agents to aggregate and rank results" multi-agent evaluator pattern at
    JPMorgan Chase.
  - **First corpus figure quantifying the organizational cause of the Meta/Instagram outage** beyond
    the architectural failure already documented — Claims 1 and 2.
  - **First corpus vendor-data quantification of the human-review drop-off as agents write more code**
    (Cursor's "no human review" inflection point dated to February 2026, tied to named model releases)
    — Claim 7.

## Guide Impact

- **Chapter on Tool Use & Agent Permissions / Security & Safety (wherever `failure-meta-ai-instagram-account-takeover.md`
  is currently cited)**: Update the Meta case study to include the organizational-cause detail from
  Claim 1 (AI-generated, AI-reviewed code shipped through a security org stripped of headcount) so the
  guide's lesson is not just "don't grant one-shot irreversible capabilities to a bot" but also "don't
  simultaneously strip the review capacity that would catch a bad change before it ships an
  irreversible capability." The two failure modes compounded, and the guide should say so explicitly
  rather than presenting only the architectural half.

- **Chapter on Verification / Code Review practices**: Add Claim 7 (Cursor's dated no-human-review
  inflection point, explicitly linked by Orosz to the Meta outage) as the empirical counter-example to
  cite alongside any recommendation that assumes review rigor naturally increases as AI writes more
  code. Pair with the filed contradiction (#1510) against `blog-pragmaticengineer-erez-cicd.md` Claim
  10 — the guide should present Erez's prediction and Orosz's empirical finding together, not cite
  either in isolation as settled.

- **Chapter on Verification / Code Review practices**: Add Claim 10 (OpenAI Codex team's tiered
  AI-review model — some changes AI-only, higher-risk changes get AI + human review) as a named,
  concrete risk-stratification pattern, distinct from and preferable to the uniform review-erosion
  described in Claim 7. This gives the guide a positive pattern to recommend, not just a negative trend
  to warn against.

- **Chapter on Team Adoption / Harness Engineering — build vs. buy for AI dev infrastructure**: Add
  Claim 13 (Uber's from-scratch tool suite: MCP Gateway, Agent Builder, Code Inbox, uReview, etc.) as a
  concrete case study for when a large organization concludes off-the-shelf tooling doesn't meet its
  needs for triaging and reviewing AI-generated changes at scale, and what categories of tooling it
  ends up building (gateway/routing, no-code agent builder, background-agent execution, risk-stratified
  PR triage, AI code review, migration automation).

- **Chapter on Team Adoption — enterprise/"traditional company" adoption patterns**: Add Claim 15
  (Cisco's 18,000-developer Codex usage, JPMorgan Chase's multi-agent annotation framework with judge
  agents) as evidence against any guide framing that assumes only tech-native companies adopt AI
  developer tooling at scale — non-tech-native large enterprises are running meaningful production
  usage as of early 2026.

## Extraction Notes

- **Paywall**: The article is metered. Sections 1-3 ("Meta: 'AI psychosis' in effect?," "Everything's
  changed in six months," "How are tech companies changing how they work?") are fully accessible,
  including body text, and are the basis for all 15 claims above. Section 4's heading ("Industry
  trends") is visible but its body content, plus the entirety of "Trends across software," "Advice for
  software engineers and engineering leaders," and "Feedback," are gated behind "This post is for paid
  subscribers" and were not extractable. The Prospector's triage comments referenced "individual
  productivity is up, but team productivity's flat, tokenmaxxing and tooling adoption, vanishing middle
  management, CEOs and CTOs back to coding" as topics in the (paywalled) "Trends" section summary line
  — that summary line itself is visible in the article's table-of-contents preview (see Source Context)
  but the supporting body text is not, so no claims were extracted from it beyond what's already quoted
  in the table-of-contents line.
- **Verification method**: The article was fetched twice via WebFetch (once for a general summary, once
  for targeted verbatim-quote extraction) and the two passes returned inconsistent figures for the same
  data points (e.g., one pass mischaracterized the Cursor lines-of-code stat). To resolve this, the raw
  page HTML was fetched directly and parsed into plain text locally, and every quote in this note was
  verified against that raw-text extraction rather than against either WebFetch summary. This is flagged
  because it demonstrates WebFetch's AI-processing layer can introduce quote drift between calls on the
  same URL — future extractions of paywalled/metered content should verify against raw HTML when
  precision matters.
- **Contradiction filed**: Issue #1510, per Claim 7 vs. `blog-pragmaticengineer-erez-cicd.md` Claim 10.
  See Cross-References → Contradicts above.
- **Cross-reference verification**: All cited claim/lesson numbers (`failure-meta-ai-instagram-account-takeover.md`
  Lessons 1 and 4; `blog-pragmaticengineer-hightower-infrastructure-ai.md` Claim 4;
  `survey-pragmaticengineer-ai-tooling-2026.md` Claim 6; `blog-pragmaticengineer-erez-cicd.md` Claim 10)
  were verified by re-reading each cited note in full before inclusion.
- **Not independently fetched**: Orosz's prior deep dive on Uber's AI developer infrastructure (referenced
  but not linked with a separate URL extractable from this article) was not independently fetched for
  this note — Claim 13 and its artifacts are based solely on this article's summary of that prior
  reporting.
