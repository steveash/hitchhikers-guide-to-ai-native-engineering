---
source_url: https://www.latent.space/p/the-website-of-the-future
source_type: blog-post
title: "The Website of the Future May Assemble Itself for Every Visitor"
author: Richard MacManus (Latent Space)
date_published: 2026-07-02
date_extracted: 2026-07-20
last_checked: 2026-07-20
status: current
confidence_overall: anecdotal
issue: "#2064"
---

# The Website of the Future May Assemble Itself for Every Visitor

> A dedicated Latent Space profile of Adobe Principal Scientist Carlos
> Sanchez's "agentic sites" concept — real-time, intent-personalized page
> assembly demonstrated at AIEWF 2026 — covering the retrieval-grounded
> architecture, stated latency/cost targets, and Sanchez's own framing of
> the open questions around agent-facing commerce (WebMCP, MCP Apps, A2A).

## Source Context

- **Type**: blog-post — a standalone, dedicated article (not a conference
  round-up), built around a single interview subject (Sanchez) and
  structured with four named subheadings ("From personalized components to
  personalized pages," "AI makes it easier to build, but harder to choose,"
  "A web built for humans — and agents," "Whither websites?").
- **Author credibility**: Richard MacManus is the named byline; per the
  article's own metadata he founded ReadWriteWeb (2003–2012) and writes
  "Now at https://www.latent.space." He reports as first-person
  interviewer/observer throughout ("he told Latent Space after his
  session," "he told me"). Latent Space (swyx) is a `trusted-feed` source
  in this repo's scanning configuration. Claims in the article are a mix
  of (a) MacManus's paraphrase of what he watched Sanchez demonstrate live
  at AIEWF, and (b) direct quotes captured during the session and in a
  follow-up interview. This is first-hand conference/interview journalism
  about a single vendor's own, self-reported, not-yet-broadly-deployed
  product — not an independently verified benchmark or customer case
  study.
- **Scope**: Covers only Sanchez/Adobe's "agentic sites" concept — the
  interpretive architecture (intent signals → intent category → LLM page
  assembly from existing content), stated engineering targets (latency,
  cost), deployment status (not yet broadly shipped to production customer
  sites), and Sanchez's own framing of open questions about serving human
  vs. agent visitors (WebMCP, MCP Apps, A2A, "agentic commerce" as
  non-uniform delegation). Does not cover: benchmark data, named customer
  deployments, adoption numbers, competitor approaches, or any technical
  detail beyond what Sanchez stated in his session and follow-up
  interview.

## Extracted Claims

### Claim 1: Adobe's "agentic site" interprets a visitor's intent, retrieves relevant material from the company's existing content, and composes a personalized page in real time — branded internally as "audience of one"
- **Evidence**: MacManus's description of Sanchez's AIEWF demonstration, corroborated by a direct Sanchez quote defining the "audience of one" term.
- **Confidence**: anecdotal (single vendor's own description of its own unreleased product demo, no independent verification)
- **Quote**: "Sanchez demonstrated what Adobe calls an “agentic site” — a web experience that interprets a visitor’s intent, retrieves relevant material from the company’s existing content, and composes a personalized page in real time." / "“We call this ‘audience of one,’ because the idea is to personalize the site in real time based on the user accessing it and what the user is doing,” Sanchez said."
- **Our assessment**: This is the article's core architectural claim and the same pattern already captured briefly (as "agentic sites") in `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 11, but with substantially more mechanistic detail here: intent signals come from browsing behavior and search queries, are grouped into an intent category, and an LLM assembles the page from that category — not a single black-box "generate a page" call.

### Claim 2: The system's content generation is retrieval-grounded — it draws exclusively from the site's existing content corpus rather than having the LLM invent an entire experience from scratch
- **Evidence**: MacManus's direct characterization of the architecture, stated plainly rather than paraphrased from a Sanchez quote.
- **Confidence**: anecdotal (author's architectural description of a vendor demo, not an independently audited system design)
- **Quote**: "The idea is that the site’s existing content is the grounding corpus. Adobe’s system retrieves from that material rather than asking an LLM model to invent an entire experience from scratch."
- **Our assessment**: This is a specific, actionable architectural choice — retrieval-over-generation as a brand-safety/consistency mechanism — that is new to the corpus for the web-personalization domain. It is also consistent with (not contradicting) the brand-guideline caution Sanchez separately voiced at the same conference, captured in `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 11 ("You cannot just generate the whole site... because the result may stray outside the brand's guidelines") — that dispatch quote doesn't appear in this article, but the retrieval-grounding design described here is the concrete mechanism that would produce exactly the brand-guideline safety that quote describes. See Cross-References.

### Claim 3: In a live demo, a visitor showing interest in camping received a coffee-machine site whose copy, product selection, and supporting content had been reorganized around making coffee outdoors
- **Evidence**: MacManus's direct account of a specific demonstrated example from Sanchez's session.
- **Confidence**: anecdotal (single demo example, not a controlled test or customer deployment)
- **Quote**: "In one example, a visitor interested in camping received a version of a coffee-machine site whose copy, product selection and supporting content had been reorganized around making coffee outdoors."
- **Our assessment**: This is the concrete artifact that makes "agentic site" tangible rather than abstract — the same product page reorganized around a detected use-case/intent rather than swapped for a different predefined variant, which the article explicitly distinguishes from traditional segment-based personalization (see Claim 4).

### Claim 4: Sanchez frames this as a categorically different approach from traditional web personalization, which has been limited to selecting from a predefined set of options (e.g., audience segments or purchase-based recommendations)
- **Evidence**: MacManus's own framing, drawn from his background "managing websites in the dot-com period," contrasting historical personalization with Sanchez's demo.
- **Confidence**: anecdotal (author's editorial framing, not a formal industry survey of personalization approaches)
- **Quote**: "But up till now, that’s typically meant selecting from a predefined set of options. A retailer might recommend an item based on a previous purchase, or place a visitor into one of several audience segments — that’s been the extent of personalization."
- **Our assessment**: Useful framing for the guide because it names the specific prior-generation baseline (predefined-option selection / segment bucketing) that "agentic sites" claims to move beyond (full page assembly from a generative/retrieval pipeline, not a menu of pre-built variants).

### Claim 5: Sanchez insists real-time agentic page generation is not speculative — it is already technically possible today, not a future capability
- **Evidence**: Direct quote from Sanchez in his post-session follow-up interview with MacManus.
- **Confidence**: anecdotal (single vendor spokesperson's assertion about their own unreleased product's readiness)
- **Quote**: "“Many people don’t even think it’s possible to generate a web page on the fly,” he told Latent Space after his session. “People think it is future-looking. No, you can do this. It’s not the future, it’s the present now.”"
- **Our assessment**: This is a stronger, more emphatic restatement of the same "It's not the future, it's the present now" framing already captured in `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 11 ("This is now possible. It's only going to get better..."), independently corroborating that this is Sanchez's stable talking point across at least two separate MacManus interactions at the same conference, not a one-off quote.

### Claim 6: Adobe targets page generation latency of no more than one to two seconds, and evaluates candidate models for speed as well as accuracy
- **Evidence**: Direct Sanchez quote from his AIEWF session, describing an internal engineering constraint.
- **Confidence**: emerging (a stated engineering target from the team building the system, more concrete/verifiable than a general opinion, though still self-reported and unaudited)
- **Quote**: "“We don’t want the site generation to take more than one or two seconds.”"
- **Our assessment**: This is a concrete, actionable latency budget for any team considering a similar real-time LLM-assembly pattern — new to the corpus's coverage of user-facing (not backend-agent) latency constraints, and useful as a benchmark figure for Chapter guidance on real-time generative UI.

### Claim 7: Adobe estimates current per-page inference cost at roughly one to two cents, and expects this to fall substantially over time
- **Evidence**: Direct Sanchez quotes giving a specific cost figure and forward-looking expectation.
- **Confidence**: emerging (a stated cost figure from the team building the system; concrete and falsifiable, though self-reported and not independently audited)
- **Quote**: "He estimated the current inference cost at “one to two cents per page.”" / "“But our point is also this is only going to get cheaper,” he said. “This is where we are today. In six months, who knows where we’re going to be.”"
- **Our assessment**: A concrete unit-economics data point for real-time, per-visitor generative content — useful for any guide discussion of whether/when agentic personalization is economically viable versus static content, though it should be flagged as a single vendor's internal estimate rather than a published cost-accounting methodology.

### Claim 8: Adobe has not yet broadly deployed agentic sites on production customer sites — the company is pitching the concept to customers and seeking willing experimentation partners
- **Evidence**: MacManus's direct statement of deployment status.
- **Confidence**: anecdotal (status report from the vendor's own spokesperson/author observation, no customer names given)
- **Quote**: "Adobe has not yet broadly deployed these experiences on production customer sites. Sanchez said the company is presenting the concept to customers and looking for organizations willing to experiment."
- **Our assessment**: Important caveat for the guide: despite the "it's the present now, not the future" framing (Claim 5), this is explicitly pre-production/early-access, not a shipped, adopted capability with measured outcomes. Any guide reference to "agentic sites" should carry this status caveat.

### Claim 9: Sanchez identifies commerce as the most obvious initial use case for agentic sites because personalization there connects directly to conversion, but argues the pattern generalizes to any site with a large matrix of user types or personas
- **Evidence**: Direct Sanchez quote given in response to a question about applicability beyond retail.
- **Confidence**: anecdotal (single practitioner's stated opinion about generalizability, no non-retail example given)
- **Quote**: "“It could work for other things — anything that needs more conversion and has a big matrix of user types or personas,” he told me."
- **Our assessment**: A specific, testable generalization claim (applicability gated on "big matrix of user types or personas") rather than a vague "this could work anywhere" — useful as a scoping heuristic for guide readers evaluating whether agentic-site patterns fit their own domain.

### Claim 10: Sanchez frames the core uncertainty around agentic sites as a "what to build" problem rather than a "can we build it" problem, and describes Adobe's own approach as building first and finding customers second
- **Evidence**: Direct Sanchez quotes from the follow-up interview.
- **Confidence**: anecdotal (single vendor spokesperson's characterization of his own team's process)
- **Quote**: "“With AI, it’s very easy to build things, but it’s hard to know what to build,” he said. “We build things and then we find the customers.”"
- **Our assessment**: This exact "easy to build things, but hard to know what to build" line is word-for-word identical to the quote already extracted in `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 11, independently confirming it as Sanchez's stable framing across the two MacManus pieces. The addition here — "We build things and then we find the customers" — is new and is a specific, somewhat unusual admission of build-first/find-customers-second process for a vendor pitching a still-undeployed product.

### Claim 11: Sanchez states that "agentic commerce" is not a single interaction pattern — different transaction types warrant different levels of automation, from a personal agent autonomously reordering a commodity to a human wanting to visually inspect a purchase like a jacket before deciding
- **Evidence**: MacManus's paraphrase of Sanchez's framing plus the article's own worked examples.
- **Confidence**: anecdotal (author's synthesis of Sanchez's remarks, illustrated by author-supplied examples rather than a direct Sanchez quote for the specific toilet-paper/jacket contrast)
- **Quote**: "Also, not every transaction will work the same way. A personal agent might autonomously reorder toilet paper, while a person buying a jacket may still want to inspect the product and make the final choice through a visual interface. That means websites will need to support different levels of delegation and involvement, rather than treating “agentic commerce” as a single interaction pattern."
- **Our assessment**: A useful, concrete conditioning variable for any guide discussion of "agentic commerce" — the delegation level should vary by transaction type/stakes, not be treated as an all-or-nothing site capability. This is a specific claim (not a paraphrase-worthy generality) about how sites should be architected to support a spectrum of autonomy.

### Claim 12: Sanchez names three distinct emerging architectural options for serving agent visitors specifically — WebMCP (structured tools exposed directly to an agent), MCP Apps/generative interfaces (interactive product experiences surfaced inside a chat environment), and an A2A backend (agent-to-agent interaction bypassing the visual site entirely)
- **Evidence**: MacManus's direct enumeration of the three named technologies in the context of Sanchez's session, presented as the live menu of options sites are currently evaluating.
- **Confidence**: anecdotal (author's technology enumeration attributed to the general theme of Sanchez's session and industry context, not a direct Sanchez quote naming all three)
- **Quote**: "Technologies such as WebMCP could allow a site to expose structured tools directly to an agent, while MCP Apps and other generative interfaces could bring interactive product experiences into the user’s chat environment. An A2A backend might allow agents to interact without traversing the conventional visual site at all."
- **Our assessment**: This is a useful taxonomy for the guide — three concretely named, non-overlapping architectural patterns for the same underlying problem (serving non-human, agent visitors). WebMCP is independently documented in `blog-google-io-2026-developer-keynote.md` Claim 8 (Chrome 149 origin trial, browser-native structured tool exposure) and A2A is independently documented in `blog-google-a2a-collaborative-agents.md` (Claim 8 names "agentic commerce" specifically as an emerging A2A use case) — this article corroborates both from the demand side (a site owner's perspective on why they'd adopt these) rather than the supply side (the protocol vendors' own announcements).

### Claim 13: Sanchez expects most sites will need to serve both human and agent visitors simultaneously, since a delegated personal agent can arrive carrying a far richer expression of user preference than a site could infer from cookies or browsing history — but is uncertain whether this means one unified site or two separate experiences
- **Evidence**: MacManus's framing plus a direct Sanchez quote acknowledging the "blurry" line between one vs. two site versions.
- **Confidence**: anecdotal (single practitioner's stated uncertainty, no resolved architecture or example given)
- **Quote**: "The agent could arrive carrying a much richer expression of the user’s preferences than the destination site could infer from cookies or recent browsing behavior." / "“Whether it’s going to be two versions [of a website] or not, that may be blurry,” he said. “But obviously, you’re going to have to target both.”"
- **Our assessment**: Notable because Sanchez explicitly declines to predict the resolved architecture ("that may be blurry") even while asserting the requirement is certain ("you're going to have to target both") — this is a specific, quotable instance of high confidence in the problem's existence paired with low confidence in the solution shape, useful to the guide as an honest signal of where the field genuinely hasn't settled.

## Concrete Artifacts

```
Source: Latent Space, "The Website of the Future May Assemble Itself for
Every Visitor" (Richard MacManus, 2026-07-02)
URL: https://www.latent.space/p/the-website-of-the-future

Stated engineering targets (Sanchez, AIEWF session):
  - Page generation latency target: "no more than one or two seconds"
  - Current inference cost estimate: "one to two cents per page"
    (expected to decrease; no fixed timeline given beyond "in six months,
    who knows where we're going to be")

Demonstrated examples (Sanchez's AIEWF session, per MacManus's account):
  1. Visitor interest signal: camping → coffee-machine site's copy,
     product selection, and supporting content reorganized around
     outdoor coffee preparation
  2. Open-ended query interface: user enters "Europe AI conferences" →
     page composed specifically around that request

Architecture pipeline (as described by MacManus/Sanchez):
  visitor browsing behavior + search queries (intent signals)
    -> grouped into an intent category (exploring / researching /
       preparing to purchase)
    -> LLM assembles a page from the site's EXISTING content corpus
       (retrieval-grounded, not generated from scratch)

Named agent-facing web architecture options (article's "A web built for
humans — and agents" section):
  - WebMCP: site exposes structured tools directly to an agent
  - MCP Apps / generative interfaces: interactive product experiences
    surfaced inside the user's chat environment
  - A2A backend: agents interact directly, bypassing the visual site

Deployment status: not yet broadly deployed on production customer
sites; Adobe is pitching the concept to customers and seeking
experimentation partners (as of article publication, 2026-07-02).
```

## Cross-References

- **Corroborates**:
  - `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 11
    (Sanchez's "agentic sites" demo and "This is now possible... it's only
    going to get better/cheaper/faster" framing, and his "With AI, it's
    very easy to build things, but it's hard to know what to build"
    quote): this article's Claim 5 ("It's not the future, it's the
    present now") and Claim 10 (the identical "easy to build things, hard
    to know what to build" sentence) independently confirm these are
    Sanchez's stable, repeated talking points across two separate
    MacManus interactions at the same conference — corroborating rather
    than merely repeating the dispatch note's brief single-claim coverage.
  - `blog-google-io-2026-developer-keynote.md` Claim 8 (WebMCP as a
    proposed open web standard for browser-native agent tool exposure,
    Chrome 149 origin trial): this article's Claim 12 independently
    corroborates WebMCP's relevance from the demand side — a site owner
    (Sanchez/Adobe) naming WebMCP as one of the live options for exposing
    structured tools to agent visitors, not just Google's own supply-side
    standard announcement.
  - `blog-google-a2a-collaborative-agents.md` Claim 8 (A2A named as an
    emerging protocol for "agentic commerce," letting agents negotiate
    deals and execute purchases): this article's Claim 12 corroborates
    A2A's applicability to commerce/web-visitor use cases from a different
    vendor's (Adobe's) perspective, framed as a backend option that lets
    agents "interact without traversing the conventional visual site at
    all."

- **Contradicts**: None filed. This article's retrieval-grounded
  architecture (Claim 2 — "Adobe's system retrieves from that material
  rather than asking an LLM model to invent an entire experience from
  scratch") is consistent with, not contradictory to, the brand-guideline
  caution Sanchez voiced at the same conference and captured in
  `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 11
  ("You cannot just generate the whole site... because the result may
  stray outside the brand's guidelines") — the retrieval-grounding design
  described here is a plausible mechanism for exactly that brand-safety
  constraint, not a competing claim about it. Per MINER.md §4a, this is
  a conditioning/extension relationship, not a contradiction to file.

- **Extends**:
  - `blog-latentspace-aiewf-autoresearch-agency-dispatch.md`: that note's
    Claim 11 is a brief, single-claim mention of "agentic sites" within a
    seven-speaker conference round-up (no architecture, no numbers, no
    deployment status). This article is the dedicated, deeper follow-up
    the dispatch note's own Cross-References/Guide Impact sections
    anticipated — it supplies the retrieval-grounding architecture
    (Claim 2), concrete demo examples (Claim 3), latency/cost targets
    (Claims 6-7), deployment status (Claim 8), and the three-technology
    agent-facing taxonomy (Claim 12) that the dispatch note did not have
    room to cover.

- **Novel**:
  - The full intent-signal → intent-category → LLM-assembly pipeline
    description (Claim 1) and the explicit retrieval-grounding design
    rationale (Claim 2) — the dispatch note named "agentic sites" but did
    not describe the mechanism.
  - Concrete latency (1-2 seconds) and cost (1-2 cents/page) engineering
    targets (Claims 6-7) — no prior corpus source gives numeric targets
    for real-time, per-visitor generative web content.
  - The three-way agent-facing architecture taxonomy — WebMCP / MCP Apps
    / A2A backend as named alternatives for the same problem (Claim 12) —
    new to the corpus as an explicit comparison from a site-owner's
    (rather than protocol-vendor's) perspective.
  - The toilet-paper-vs-jacket delegation-spectrum framing for "agentic
    commerce" (Claim 11) — new, concrete illustration of why agentic
    commerce isn't a single interaction pattern.
  - Sanchez's explicit uncertainty about whether serving human and agent
    visitors requires one unified site or two separate experiences
    (Claim 13) — new to the corpus as a named open architectural question.

## Guide Impact

- **Chapter 02 (Architecture Patterns) or Chapter 04 (Practical
  Engineering)**: Add the retrieval-grounded, intent-signal-to-LLM-
  assembly pipeline (Claim 1-2) as a concrete architecture pattern for
  teams building personalized/generative web experiences — specifically
  the design choice to ground page assembly in an existing, approved
  content corpus rather than open-ended generation, citing this source
  alongside the brand-guideline caution already sourced from
  `blog-latentspace-aiewf-autoresearch-agency-dispatch.md`. Include the
  stated latency (1-2 seconds) and cost (1-2 cents/page) targets (Claims
  6-7) as a starting benchmark for teams scoping similar real-time
  generative UI work, with the caveat that these are one vendor's
  self-reported, pre-production estimates (Claim 8), not audited
  production metrics.

- **Chapter 03 (Agent Orchestration) or a Tool Use section**: Add the
  three-way agent-facing architecture taxonomy (Claim 12: WebMCP, MCP
  Apps/generative interfaces, A2A backend) as a decision framework for
  teams deciding how to expose a site or service to agent visitors, not
  just human visitors — this is the first corpus source to frame these
  three technologies as competing/complementary options from a single
  site owner's adoption perspective, cross-referencing the underlying
  protocol-specific detail already in `blog-google-io-2026-developer-
  keynote.md` and `blog-google-a2a-collaborative-agents.md`.

- **Chapter 01 (Foundations) or wherever "agentic commerce" is
  discussed**: Add Sanchez's delegation-spectrum framing (Claim 11) as a
  corrective to any guide language that treats "agentic commerce" as a
  single capability — the guide should note that appropriate automation
  level varies by transaction stakes/type (commodity reorder vs.
  considered purchase), per this source.

## Extraction Notes

- **Fetch method**: WebFetch's summarized response was not used for
  quoted material — an initial WebFetch call returned a paraphrased,
  condensed version of the article (compressed section headers, shortened
  quotes) that did not match verbatim-quoting requirements. The raw HTML
  was instead fetched directly via `curl` with a browser user-agent,
  the article body was isolated from the `class="body markup"` container,
  HTML tags were stripped, and HTML entities were unescaped
  programmatically. All `Quote` fields above were copied from that raw,
  unescaped text, including the source's original smart-quote characters.
  Publication date (2026-07-02T21:25:14+00:00) and author name (Richard
  MacManus) were confirmed from the page's embedded JSON-LD metadata,
  independent of the article body text.
- **Full source read**: The entire article was read in full across all
  four named sections, from the opening dot-com-era personalization
  framing through the closing "Whither websites?" section. No linked
  sub-pages within the article body were substantive enough to warrant
  following (the article does not link out to Sanchez's own writing, a
  recorded talk, or an Adobe product page for "agentic sites").
- **Confidence rationale**: Rated `anecdotal` overall — every claim
  traces to a single vendor spokesperson's (Sanchez's) own description of
  an unreleased, not-yet-broadly-deployed product demo, relayed by one
  attendee/interviewer, with no customer names, adoption data, or
  independently verifiable benchmarks. Claims 6 and 7 (the stated
  latency and cost targets) are individually rated `emerging` rather than
  `anecdotal` because they are concrete, falsifiable engineering figures
  from the team that built the system, rather than general opinion or
  prediction — but the overall note confidence stays `anecdotal` given
  the single-source, pre-production nature of the whole piece.
- Cross-references verified: `blog-latentspace-aiewf-autoresearch-agency-
  dispatch.md`, `blog-google-io-2026-developer-keynote.md`, and
  `blog-google-a2a-collaborative-agents.md` were each re-read in full
  before citing; claim numbers were confirmed against each note's actual
  `### Claim N` headings, not guessed.
- No contradiction filed: the retrieval-grounding architecture described
  here is a plausible supporting mechanism for, not a conflicting claim
  against, the brand-guideline caution captured in the existing dispatch
  note — see Cross-References — Contradicts above for the reasoning.
