---
source_url: https://openai.com/index/ringcentral
source_type: blog-post
title: "How RingCentral builds AI-native work from engineering to ops"
author: OpenAI
date_published: 2026-08-12
date_extracted: 2026-08-21
last_checked: 2026-08-21
status: current
confidence_overall: emerging
issue: "#2837"
---

# How RingCentral builds AI-native work from engineering to ops

> A dedicated OpenAI customer case study (not a testimonial carousel entry)
> describing two RingCentral AI-native initiatives: a company-wide
> "AI-Native Challenge" hackathon that gave every employee ChatGPT Work and
> Codex with no mandated workflow, and the PMO's use of ChatGPT Work to
> build an "operating system for program management" with automated
> cross-tool status reporting.

## Source Context

- **Type**: blog-post (OpenAI customer-story page, `openai.com/index/`,
  published August 12, 2026; formatted as a single-customer case study —
  metadata tiles for Company size/Region/Industry/Products, a two-section
  narrative body, "Contact sales" CTAs — distinct from the
  multi-customer testimonial-carousel format used in
  `blog-openai-chatgpt-work-ambitious-partner.md`).
- **Author credibility**: House-authored OpenAI customer-story copy, no
  named OpenAI author. Contains two named RingCentral quotes (Kira
  Makagon, President & Chief Operating Officer; Vaneet Seth, Senior
  Manager, R&D Efficiency, PMO) and one unnamed attribution ("Engineering
  leader at RingCentral who spearheaded the project"). This is first-party
  vendor marketing copy commissioned/published by OpenAI about a customer
  — every quote and framing choice is OpenAI-selected and OpenAI-published,
  with no independent verification of participation counts, the "operating
  system for program management" characterization, or any other claim in
  the piece. Standard vendor-case-study credibility caveats apply
  throughout.
- **Scope**: Covers two initiatives — (1) the "AI-Native Challenge," a
  company-wide, CEO-office-sponsored hackathon-style program giving every
  employee ChatGPT Work and Codex access with no mandated workflow, and
  (2) the PMO's adoption of ChatGPT Work for status tracking, reporting,
  release governance, and knowledge transfer, including one named
  automation (cross-tool status-notification generation). Does NOT cover:
  any quantified participation count (no percentage or absolute number of
  the "thousands of employees" who completed the challenge), any
  time-savings or productivity metric (unlike
  `blog-openai-chatgpt-work-ambitious-partner.md`'s ~40%/weeks-to-hours
  figures, this piece contains zero numeric outcome claims), technical
  detail on how the Jira/Sheets/CRM automation is built, or any
  engineering-side workflow detail beyond the challenge's existence
  (despite the headline promising "engineering to ops," the engineering
  half is covered only by the Challenge description and one unnamed
  engineering leader's quote — there is no engineering-specific workflow
  detail comparable to the PMO section's status-reporting mechanism).

## Extracted Claims

### Claim 1: RingCentral gives every employee access to ChatGPT Work and Codex regardless of engineering experience, framed by its President & COO as turning "the whole company" into "a product organization"
- **Evidence**: Named executive quote (Kira Makagon, President & Chief
  Operating Officer, RingCentral), presented as the article's opening
  pull quote.
- **Confidence**: anecdotal (single named executive's framing of a
  company-wide policy; no data on actual access-rate or usage-rate across
  the "thousands of employees worldwide" mentioned in the same paragraph)
- **Quote**: "When you put real AI tools in everyone's hands, the whole company becomes a product organization. Every one of our products—including but not limited to our Agentic Voice AI portfolio of AIR, AVA, ACE—gets sharper as we compress the distance between an idea and a shipped feature, and that's exactly what AI-native development lets us do."
- **Our assessment**: A C-suite-level "AI tools for everyone" framing
  consistent with the article's broader "regardless of engineering
  experience" thesis, but it is a strategic statement rather than an
  operational description — it names no mechanism for how "compressing
  the distance between an idea and a shipped feature" actually happens.
  The mechanism is supplied later by Claim 2 (the AI-Native Challenge).

### Claim 2: RingCentral's Office of the CEO sponsored a company-wide "AI-Native Challenge" giving every participant ChatGPT Work and Codex and asking them to build a complete, end-to-end project with no mandated workflow or other constraints
- **Evidence**: Direct description of a named, sponsored internal program.
- **Confidence**: emerging (a specific, named program with a stated
  sponsor and stated design constraint — "no mandated workflow" — though
  no start/end date, duration, or total headcount eligible is given)
- **Quote**: "To encourage AI fluency across a global engineering organization, RingCentral's Office of the CEO sponsored an AI-Native Challenge. Every participant was given ChatGPT Work and Codex, and asked to build a complete, end-to-end project—with no mandated workflow or other constraints."
- **Our assessment**: The "no mandated workflow" design choice is
  notable — this is explicitly an unstructured, bottom-up adoption
  exercise rather than a top-down process rollout, which stands in
  contrast to the more prescriptive, ritual-driven norm changes described
  in `blog-anthropic-ai-native-engineering-org.md` (JIT planning,
  bifurcated code review, three core team principles). RingCentral's
  approach here is closer to "give people the tools and see what they
  build" than to Anthropic's deliberate norm-redesign process.

### Claim 3: Nearly every AI-Native Challenge participant created a working repository, and thousands of employees — including non-technical staff and executives — delivered functioning projects
- **Evidence**: Direct outcome claim for the Challenge, no participation
  denominator given.
- **Confidence**: anecdotal (a specific-sounding outcome claim —
  "thousands of employees" — but with no total headcount, no completion
  rate, and no definition of "functioning project" or "working
  repository," so the claim cannot be checked against a base rate)
- **Quote**: "Nearly every participant created a working repository, and thousands of employees, including non-technical staff and even executives, delivered functioning projects."
- **Our assessment**: "Nearly every participant" combined with an
  unspecified total participant count is a common vendor-case-study
  pattern — it reads as a strong completion-rate claim without being one,
  since we don't know whether "thousands" is out of five thousand
  eligible employees or fifty thousand. The non-technical-staff/executive
  detail is the most concrete part of the claim (it names *who*
  participated beyond engineers), but still self-reported and
  unverifiable.

### Claim 4: The AI-Native Challenge functions as a working model for RingCentral's broader strategy of using AI internally to build products faster for customers, applying the same Codex-enabled approach to accelerate development of its own AI product portfolio (AI Receptionist, AI Virtual Assistant, AI Conversation Expert)
- **Evidence**: Direct statement connecting the internal hackathon to
  RingCentral's external product roadmap.
- **Confidence**: emerging (names three specific shipped products by
  full name and acronym, giving a checkable claim about what RingCentral
  sells, though the causal link from "the Challenge" to "product
  development speed" is asserted, not demonstrated with a before/after
  example)
- **Quote**: "For RingCentral, the challenge is a working model of a broader strategy: using AI internally to build products faster for their customers. The company applies the same Codex-enabled approach to accelerate development of its own AI-powered product portfolio—RingCentral AI Receptionist (AIR), AI Virtual Assistant (AVA), and AI Conversation Expert (ACE)—shortening the distance between an idea and a shipped customer feature."
- **Our assessment**: This is the article's clearest attempt to connect
  an internal-adoption exercise to external product velocity, but it
  gives no worked example (no "feature X shipped in Y time because of
  Codex" case, unlike the specific before/after anecdotes in
  `blog-openai-chatgpt-work-ambitious-partner.md` Claims 4-7). Treat as
  a strategic assertion, not a measured outcome.

### Claim 5: An unnamed RingCentral engineering leader who ran the Challenge frames AI-native development as amplifying engineers rather than replacing them, with humans remaining in the loop for product requirements, business context, architectural decisions, and testing/verification
- **Evidence**: Direct quote, attributed only by role ("Engineering
  leader at RingCentral who spearheaded the project"), not by name.
- **Confidence**: anecdotal (unnamed source, so credibility rests
  entirely on OpenAI's editorial framing rather than an independently
  identifiable individual)
- **Quote**: "The clearest lesson from the challenge was that AI-native development isn't about replacing engineers—it's about amplifying them. AI accelerates the entire development cycle, while humans remain in the loop, guiding product requirements, providing business context, making architectural decisions, and ensuring every outcome is tested and verified."
- **Our assessment**: This "amplify, not replace" framing plus a named
  list of retained-human responsibilities (product requirements, business
  context, architectural decisions, testing/verification) closely
  parallels the human/AI division of labor described in
  `blog-anthropic-ai-native-engineering-org.md` Claim 6 (Claude handles
  style/linting/bug-catching/tests; humans retain legal, security, and
  product-sense judgment) — both sources converge on "the human role
  narrows to judgment and verification, not mechanical output," though
  this RingCentral quote is vaguer (no named mechanism for *how*
  verification happens) and comes from an unnamed source, so it carries
  less individual weight than Fung's first-party account.

### Claim 6: The RingCentral PMO used ChatGPT Work to build "what amounts to an operating system for program management," replacing scattered notes and chat history with AI-powered workflows for status tracking, reporting, release governance, and knowledge transfer
- **Evidence**: Direct description of a department-level tooling
  build-out, following on from the Challenge.
- **Confidence**: emerging (a specific, named set of workflow categories
  — status tracking, reporting, release governance, knowledge transfer —
  though "operating system" is OpenAI's own characterization, not a
  literal product name, and no before/after time or accuracy metric is
  given)
- **Quote**: "The Program Management Office (PMO) has used ChatGPT Work to build what amounts to an operating system for program management, replacing scattered notes and chat history with AI-powered workflows for status tracking, reporting, release governance, and knowledge transfer."
- **Our assessment**: This is the article's most concrete organizational
  claim — naming four specific workflow categories a non-engineering
  department rebuilt around an agent product — but it's a category list,
  not a description of any single workflow's mechanics, except for the
  one worked example in Claim 8.

### Claim 7: Vaneet Seth (Senior Manager, R&D Efficiency, PMO, RingCentral) says ChatGPT Work lets him turn assembled project context directly into "actions and execution"
- **Evidence**: Named individual quote, same person previously quoted in
  `blog-openai-chatgpt-work-ambitious-partner.md` Claim 5 (there titled
  "R&D Efficiency Manager, RingCentral"; here titled "Senior Manager, R&D
  Efficiency, PMO, RingCentral" — a more specific but consistent title
  for the same role).
- **Confidence**: anecdotal (single named individual, vendor-selected
  quote; no specifics on which actions or how execution differs from
  before)
- **Quote**: "ChatGPT brings my project context together. With ChatGPT Work, I can turn that context into actions and execution."
- **Our assessment**: This is a shorter, more abstract restatement from
  the same named source as the "launch-check automation, scaled 1→~50
  supported product managers" claim already in the corpus
  (`blog-openai-chatgpt-work-ambitious-partner.md` Claim 5, published
  July 9, 2026, five weeks earlier). This article does not repeat the
  1→50 figure or the launch-check-automation detail — it instead
  describes a different, newer application (Claim 8's cross-tool status
  reporting). Treat the two articles as complementary snapshots of the
  same person's evolving PMO tooling, not a single restated claim.

### Claim 8: The PMO built an automated status-reporting workflow in ChatGPT Work that generates notifications from issues tracked across Jira, Google Sheets, CRM systems, and other sources, so meetings start with blockers, owners, and actions already defined instead of an open question about what changed
- **Evidence**: Direct description of a named, cross-tool automation with
  a specific before/after framing.
- **Confidence**: emerging (names the specific source systems being
  integrated — Jira, Google Sheets, CRM — and gives a concrete
  before/after behavioral contrast, though no metric for time saved,
  accuracy, or adoption rate is given)
- **Quote**: "One application is automated status reporting: Using ChatGPT Work, the PMO team built workflows that generate notifications from issues tracked across Jira, Google Sheets, CRM systems, and other sources. It's the difference between walking into a meeting asking what changed and walking in with blockers, owners, and actions already defined."
- **Our assessment**: This is the single most concrete, checkable
  artifact in the piece — a named cross-tool automation pattern (poll
  Jira/Sheets/CRM → synthesize → push status notifications) that is
  structurally similar to the "Scheduled Tasks" pattern documented in
  `blog-openai-chatgpt-work-ambitious-partner.md` Claim 11 (dashboard
  monitoring, recurring reports) and to Fung's customer-feedback-channel
  automation in `blog-anthropic-ai-native-engineering-org.md` Claim 5 —
  three independent sources now describe "poll multiple systems on a
  schedule, synthesize, and push a digest" as a recurring, cross-vendor
  agent-automation pattern for reducing manual status-gathering meetings.

### Claim 9: Across engineering and operations, RingCentral's overall pattern is that giving employees room to experiment with AI doesn't just build individual skills — it builds the infrastructure the company runs on
- **Evidence**: The article's closing synthesis statement, tying the
  Challenge (engineering) and PMO automation (ops) sections together.
- **Confidence**: anecdotal (an editorial closing thesis rather than a
  new factual claim — it summarizes Claims 2-8 rather than adding new
  evidence)
- **Quote**: "Across engineering and operations alike, the same pattern holds: giving employees room to experiment with AI doesn't just build individual skills, it builds the infrastructure the company runs on."
- **Our assessment**: This is OpenAI's editorial framing device for the
  piece — "bottom-up experimentation becomes company infrastructure" — and
  is the throughline connecting the unstructured AI-Native Challenge
  (Claim 2) to the PMO's now-institutionalized status-reporting workflow
  (Claim 8). It is a narrative conclusion, not an independently
  verifiable claim.

## Concrete Artifacts

```
Source: OpenAI, "How RingCentral builds AI-native work from engineering
to ops," https://openai.com/index/ringcentral (August 12, 2026)

Case-study metadata tiles (from page header):
  Company size: Enterprise
  Region:       North America
  Industry:     Technology
  Products:     ChatGPT, Codex

Company context (non-AI, background):
  "nearly three decades of innovation in business communications"
  "more than $2.6 billion in annual revenue"
  "thousands of employees worldwide"

Page structure (two sections, per on-page section nav):
  1. "The AI-Native Challenge"
  2. "Running daily PMO operations with ChatGPT Work"

Named individuals quoted:
  Kira Makagon      — President & Chief Operating Officer, RingCentral
  [unnamed]          — "Engineering leader at RingCentral who spearheaded
                        the project"
  Vaneet Seth        — Senior Manager, R&D Efficiency, PMO, RingCentral
                        (same individual as
                        blog-openai-chatgpt-work-ambitious-partner.md
                        Claim 5, titled there "R&D Efficiency Manager")

Named RingCentral AI product portfolio (referenced, not the subject of
the case study itself — RingCentral is a *customer* of ChatGPT Work/Codex,
and separately *builds* these products for its own customers):
  AIR — RingCentral AI Receptionist
  AVA — AI Virtual Assistant
  ACE — AI Conversation Expert

PMO automation pattern (Claim 8):
  Input:  issues tracked across Jira, Google Sheets, CRM systems, "and
          other sources"
  Output: status notifications naming blockers, owners, and actions
  Effect (claimed): meetings start with defined blockers/owners/actions
          instead of an open "what changed" question
```

## Cross-References

- **Corroborates**:
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 5 — the same
    named individual, Vaneet Seth, is quoted in both articles about his
    PMO work at RingCentral with ChatGPT Work. The July 9, 2026 article
    reports a specific outcome metric (launch-check automation scaling
    him from supporting 1 to ~50 product managers); this August 12, 2026
    article does not repeat that figure but describes a related,
    apparently newer automation (Claim 8's Jira/Sheets/CRM status
    reporting). Together they corroborate that Seth's PMO tooling is an
    ongoing, evolving build-out rather than a single one-off automation.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 6 — Fung's
    bifurcated code-review framing (Claude handles mechanical work;
    humans retain judgment on legal, security, and product sense) is
    corroborated in shape (not detail) by this article's Claim 5
    (unnamed RingCentral engineering leader: AI accelerates the
    development cycle, humans stay in the loop for product requirements,
    business context, architectural decisions, and verification). Two
    independent organizations describe the same "humans retain judgment
    and verification, AI handles execution" division of labor.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 5 — Fung's
    customer-feedback-channel automation ("Is there a way to automate
    it?") is structurally corroborated by this article's Claim 8
    (poll multiple systems on a schedule, synthesize, push a digest to
    replace manual status-gathering) — a third independent source (after
    Fung/Anthropic and the Scheduled Tasks feature in
    `blog-openai-chatgpt-work-ambitious-partner.md` Claim 11) describing
    the same "automate the recurring status/digest ritual" pattern.
- **Contradicts**: None identified. (No contradiction issue filed.)
- **Extends**:
  - `blog-openai-chatgpt-work-ambitious-partner.md` — that post's Claim 5
    covered RingCentral only as one of four testimonials in a
    multi-customer product-launch carousel, with a single quantified
    metric (1→~50 PMs) and no detail on the mechanism beyond "launch
    checks." This article is a dedicated single-customer case study
    adding: the company-wide "AI-Native Challenge" program (entirely new
    to the corpus), the Jira/Sheets/CRM status-reporting automation detail
    (new mechanism, not previously described), and named RingCentral
    product context (AIR/AVA/ACE) not present in the earlier post.
  - `blog-bvp-shopify-ai-playbook.md` — both this article's Claim 2 (the
    AI-Native Challenge's "no mandated workflow or other constraints"
    design) and Shopify's Claim 1 (intentional non-standardization on a
    single AI tool) describe large organizations deliberately choosing
    an unstructured, bottom-up adoption path over a top-down mandate —
    though Shopify's is a tooling-choice policy and RingCentral's is a
    one-time internal hackathon design, so this is a thematic parallel,
    not a claim-level match.
- **Novel**:
  - The "AI-Native Challenge" (Claims 2-5) — the first source in the
    corpus describing a CEO-office-sponsored, company-wide, no-mandated-
    workflow internal hackathon as an AI-adoption mechanism, including
    non-technical staff and executives as participants.
  - The single-customer OpenAI case-study page format itself (metadata
    tiles for Company size/Region/Industry/Products) — the corpus's
    first example of this page template, distinct from the multi-customer
    testimonial-carousel format already documented in
    `blog-openai-chatgpt-work-ambitious-partner.md`.
  - The specific Jira/Google Sheets/CRM cross-tool status-notification
    automation (Claim 8) — more implementation detail (named source
    systems) than any prior corpus mention of RingCentral's PMO tooling.

## Guide Impact

- **Chapter 05 (Team Adoption / Practitioner Patterns)**: Add the
  "AI-Native Challenge" (Claim 2) as a named example of bottom-up,
  unstructured adoption ("no mandated workflow or other constraints")
  sponsored at the CEO-office level — a different adoption mechanism
  than the top-down norm-redesign process Anthropic describes in
  `blog-anthropic-ai-native-engineering-org.md`. Flag clearly that no
  participation denominator or completion-rate is given (Claim 3), so
  this should be cited as an illustrative program design, not as
  evidence of a specific adoption rate.
- **Chapter 04 (Agentic Workflows)**: Claim 8's Jira/Google Sheets/CRM
  status-notification automation is a third independent corpus example
  (after Fung's feedback-channel automation and OpenAI's own Scheduled
  Tasks feature) of the "poll multiple systems on a schedule, synthesize,
  push a digest" pattern — worth citing together as a converging,
  cross-vendor agentic-workflow shape if the chapter discusses common
  automation patterns.
- **Chapter 02 (Harness Engineering)**: Claim 5's unnamed-engineering-
  leader framing (AI handles the development cycle; humans retain
  product requirements, business context, architectural decisions, and
  verification) is a weaker, unnamed-source echo of the more detailed,
  first-party division-of-labor claim already in the corpus from Fung
  (`blog-anthropic-ai-native-engineering-org.md` Claim 6) — cite Fung as
  the primary source and this article only as secondary corroboration,
  given the unnamed attribution here.
- No chapter should cite this article for any quantified productivity or
  time-savings figure — unlike
  `blog-openai-chatgpt-work-ambitious-partner.md`, this piece contains no
  percentage, ratio, or before/after time metric anywhere in its body.

## Extraction Notes

- The live URL (`https://openai.com/index/ringcentral`) returned HTTP 403
  to both `WebFetch` and direct `curl` with a browser user-agent, matching
  the Cloudflare bot-challenge pattern the Prospector's second triage
  comment anticipated and that is already documented for other
  `openai.com/index/` posts in `blog-openai-chatgpt-work-ambitious-partner.md`.
- Retrieved via the Internet Archive Wayback Machine
  (`https://web.archive.org/web/20260818034507/https://openai.com/index/ringcentral/`,
  crawled August 18, 2026, six days after publication). The Wayback
  Machine itself returned an intermittent "Temporarily Offline" 503 on
  the first several attempts and succeeded on a later retry; `WebFetch`
  again refused to fetch `web.archive.org` URLs directly (as previously
  documented), so the snapshot was retrieved with `curl` (browser
  user-agent) and its HTML stripped to plain text locally, with HTML
  entities (`&amp;`, curly quotes, etc.) decoded via Python's `html.unescape`
  so extracted quotes preserve the source's exact punctuation and
  typographic characters.
- The stripped text captured the full visible article body (both named
  sections, all three quotes, the metadata tiles) with no gaps — this
  appears to be the complete article; it is a short case-study page
  (roughly 600 words of body text), noticeably thinner than the
  multi-section product-launch post already in the corpus
  (`blog-openai-chatgpt-work-ambitious-partner.md`). This explains the
  lower claim count (9) relative to that longer source (13 claims) —
  the source itself is short, not under-read. Checked the raw HTML for
  any numeric stat tiles or hidden structured-data blocks (a pattern
  other OpenAI case-study pages sometimes use) and found none; the
  article genuinely contains zero quantified outcome metrics.
- No linked sub-pages within the article body were found to follow (the
  only links present are global site navigation and a "Keep reading"
  related-articles module unrelated to RingCentral).
- No contradiction with any existing source note was found during
  cross-referencing (see Cross-References → Contradicts), so no
  contradiction issue was filed per MINER.md §4a.
- Confidence set to `emerging`: two named individuals and one unnamed
  role-attributed source give specific, checkable claims (named program,
  named source systems, named products), but every claim is
  vendor-selected, vendor-published, and contains no independent
  verification, participation denominator, or outcome metric — consistent
  with the `emerging` rating already used for the closely related
  `blog-openai-chatgpt-work-ambitious-partner.md`.
