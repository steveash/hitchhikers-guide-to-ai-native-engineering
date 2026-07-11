---
source_url: https://openai.com/index/preply
source_type: blog-post
title: "How Preply combines AI and human tutors to personalize learning"
author: OpenAI (customer-story vertical; quoted subjects Dmytro Voloshyn — Co-founder & CTO of Preply, Emily Stott — Staff Product Manager at Preply, Michelle Garcia Ramos — Spanish tutor on Preply)
date_published: 2026-06-12
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: emerging
issue: "#1755"
---

# How Preply combines AI and human tutors to personalize learning

> An OpenAI customer-story case study describing Preply's "Lesson Insights" feature — an
> OpenAI-API-powered pipeline that transcribes 1:1 language lessons and generates
> structured, personalized post-lesson feedback and homework — plus company-wide
> ChatGPT Enterprise and Codex adoption figures, a six-item quantified results block,
> and a three-item "Leadership lessons" / three-item "Tips" list, all explicitly framed
> around augmenting rather than replacing human tutors.

## Source Context

- **Type**: blog-post (OpenAI customer-story page, `openai.com/index/preply`, ~900 words,
  published June 12, 2026; auto-discovered via the `openai-news` trusted feed).
- **Author credibility**: House-authored OpenAI customer-story copy built around quotes
  from three named Preply subjects: Dmytro Voloshyn (Co-founder & CTO), Emily Stott (Staff
  Product Manager), and Michelle Garcia Ramos (a Spanish tutor on the platform). Preply is
  described in the article as "the world's largest marketplace for online language
  learning, connecting more than 100,000 expert tutors with learners across more than 180
  countries." This is a vendor case study — OpenAI selected the customer, chose which
  quotes and metrics to publish, and frames the narrative promotionally (a stat block, a
  "Results at a glance" section, a "Leadership lessons" list, a "Tips" list, a closing
  "Contact sales" call to action) — not an independent report with disclosed measurement
  methodology. The three named individuals are credible primary-source voices for what
  happened inside Preply, but no metric in the article states a measurement window, sample
  definition, or survey instrument.
- **Scope**: Covers the Lesson Insights feature (what it generates, when, and how it feeds
  a downstream self-learning exercise engine), Preply's ChatGPT Enterprise company-wide
  rollout and weekly-active-usage growth, Preply's internal use of custom GPTs and Codex
  for engineering, a six-metric "Results at a glance" block, a single tutor's before/after
  account of AI-assisted lesson prep, a three-item leadership-lessons list, a three-item
  tips list, and forward-looking product plans. Does NOT cover: the model(s) or prompts
  used to generate Lesson Insights, transcription/privacy architecture beyond "with
  learner consent," how tutors or students can correct or dispute AI-generated feedback,
  any error/failure-mode data, cost or contract terms, or a technical description of the
  "self-learning exercise engine" the insights feed into.

## Extracted Claims

### Claim 1: Preply designed Lesson Insights to strengthen, not replace, the tutor-learner relationship by automating the administrative overhead around lessons rather than the lessons themselves
- **Evidence**: Narrator (OpenAI-authored) framing statement introducing the feature, followed by a description of what the feature actually automates.
- **Confidence**: emerging (a stated product-design intent, corroborated by the concrete feature description that follows it in the same source, but still a single vendor-published account)
- **Quote**: "Preply saw an opportunity to use AI to strengthen—not replace—the relationship between tutors and learners. The result was Lesson Insights, an OpenAI API-powered experience that transforms every lesson into a personalized learning journey."
- **Our assessment**: This is the article's thesis statement, and unlike similarly-worded aspirational framing in other OpenAI customer stories (e.g. BBVA's "anticipating the needs of every client," see Cross-References), it is backed by a specific, checkable mechanism in the same source: Lesson Insights automates post-lesson administrative writing (notes, feedback summaries), not the 1:1 teaching interaction itself (Claim 4). The "augment, don't replace" framing should be read as a design choice about *which* task got automated (admin work, not the live lesson), not as evidence about downstream labor-market effects on tutors generally.

### Claim 2: Preply evaluated multiple AI model providers before selecting OpenAI, citing speed, reliability, and production readiness at global scale as the deciding factors
- **Evidence**: Direct quote from Dmytro Voloshyn, Co-founder & CTO, describing the vendor-selection process and resulting relationship.
- **Confidence**: anecdotal (single executive's account of a vendor selection; no detail on which other providers were evaluated, what specific benchmarks were used, or over what time period)
- **Quote**: "We decided to partner with OpenAI because it provides state-of-the-art models for us, which solve problems for our customers. It's now at the center of our ecosystem and how we operate as a company."
- **Our assessment**: This is standard vendor-selection framing from a company being featured by that same vendor — the claim that OpenAI is now "at the center of our ecosystem" is unsurprising given the source, and no comparative evidence is given for why OpenAI specifically beat other providers on "speed, reliability, and production readiness" (the narrator's paraphrase, not a Voloshyn quote). Treat this as evidence that Preply made OpenAI a deep, cross-functional platform choice (corroborated by internal usage figures in Claims 5–6), not as an independently verified capability comparison.

### Claim 3: Preply ran company-wide ChatGPT Enterprise enablement sessions for more than 600 employees across four cities (New York, Kyiv, London, Barcelona), growing weekly active usage from 60% to 95%
- **Evidence**: Direct narrator statement with specific headcount, city count, and before/after usage percentages.
- **Confidence**: emerging (specific named figures for a company-wide rollout; single company, self-reported, no stated measurement window for the 60%→95% growth)
- **Quote**: "Preply introduced ChatGPT Enterprise across its organization, running company-wide enablement sessions for more than 600 employees across New York, Kyiv, London and Barcelona. Weekly active usage quickly grew from 60% to 95%, helping embed AI into everyday work across teams."
- **Our assessment**: The 95% weekly-active-usage figure matches the headline stat-block number ("95% ChatGPT weekly active usage among Preply employees") and is the highest company-wide ChatGPT Enterprise WAU figure in the corpus's OpenAI customer-story set — higher than BBVA's "70%+ weekly active usage" (`blog-openai-bbva-banking-transformation.md` Claim 2 / Concrete Artifacts), though BBVA's rollout is roughly 150x larger in headcount (100,000 vs. 600+ employees), which likely explains part of the usage-rate gap: a smaller, more centrally-run enablement program is easier to drive to near-universal weekly usage than a 100,000-employee global bank rollout. The two figures should not be cited together as directly comparable evidence of "which company achieved higher adoption" without noting the scale difference.

### Claim 4: Lesson Insights is generated a few minutes before a lesson ends from a consented, transcribed lesson recording, and delivers a five-part structured report (topic summary, grammar corrections, vocabulary highlights, pronunciation feedback, recommended next steps) to the learner and tutor's chat thread within minutes of the lesson ending
- **Evidence**: Direct narrator description of the feature's technical/workflow mechanics, including a bulleted breakdown of report contents.
- **Confidence**: emerging (a specific, concrete workflow description — timing, consent gate, delivery channel, and named report sections — though still self-reported by the vendor with no detail on transcription accuracy or generation-quality safeguards)
- **Quote**: "Lessons take place in the Preply Classroom, and with learner consent, the sessions are recorded and transcribed. Insight generation is scheduled a few minutes before the end of the session, so feedback is ready for the tutor and student to review together. Within minutes of a lesson ending, the learner and their tutor receive a structured, personalized report in their chat thread that includes: A summary of key lesson topics / Grammar corrections and explanations / Vocabulary highlights and translations / Pronunciation feedback / Recommended next steps."
- **Our assessment**: This is the most concrete, technically specific claim in the source and the one most useful for a context-engineering or verification discussion: the system is explicitly timed to complete generation *before* the lesson ends (not after), so the tutor and student can review the AI output together in the same session — a deliberate design choice to keep a human in the loop at the point the AI output is first consumed, rather than delivering it asynchronously and unreviewed. The article gives no detail on what happens if generation isn't ready in time, or what recourse exists if the AI-generated grammar/pronunciation feedback is wrong.

### Claim 5: Lesson Insights output feeds directly into Preply's self-learning exercise engine, which generates personalized homework from what was actually discussed and corrected in that specific lesson
- **Evidence**: Direct narrator statement describing the downstream use of Lesson Insights data.
- **Confidence**: anecdotal (a stated data pipeline with no technical detail on the "self-learning exercise engine" itself, no example of a generated exercise, and no measurement of whether homework generated this way is more effective than generic exercises)
- **Quote**: "Those insights feed directly into Preply's self-learning exercise engine to generate personalized homework—turning every human lesson into structured practice that compounds over time."
- **Our assessment**: This is the clearest description in the source of the "compounding personalization" pattern OpenAI is promoting: each 1:1 lesson's transcript becomes the input for that specific learner's next practice material, rather than lessons and homework being generated from separate, disconnected systems. It is a plausible and specific architecture (lesson-derived context feeding downstream generation) but the claim that this "compounds over time" is asserted, not measured — no data is given on retention or skill-progression outcomes attributable specifically to this feedback loop (as opposed to the general retention figures in Claim 8, which are about engagement with Lesson Insights, not learning outcomes).

### Claim 6: Emily Stott, Staff Product Manager, reports that students repeatedly asked for a tangible sense of progress before Lesson Insights existed, and that the feature now lets Preply convert lesson content and tutor feedback into "highly personalized and targeted practice"
- **Evidence**: Direct quote from Emily Stott describing the product problem Lesson Insights was built to solve.
- **Confidence**: anecdotal (single product manager's characterization of a recurring but unquantified user complaint — no survey data, ticket counts, or churn data cited for the "how am I doing" problem)
- **Quote**: "We were hearing time and time again, 'How am I doing? Am I getting better? What do I get to do next?,' Students wanted a more tangible view of their growth. Now, with Lesson Insights, we're able to understand exactly what you've been talking about, your goals, the topics you've been covering, your tutor's feedback, and convert that into highly personalized and targeted practice."
- **Our assessment**: This grounds Claim 5's "self-learning exercise engine" claim in a named, specific user pain point (repeated "how am I doing" questions) that motivated the feature, which is more evidentiary than a generic "we wanted to improve personalization" justification. Still, "time and time again" is qualitative, not a quantified complaint volume, so this should be cited as the stated product rationale, not as measured user-research evidence.

### Claim 7: Around 94% of Preply engineers use Codex and AI coding assistants for code generation, PR reviews, debugging, and accelerating development workflows
- **Evidence**: Direct narrator statement with a specific adoption percentage and named use cases.
- **Confidence**: emerging (a specific, named engineering-adoption figure; single company, self-reported, no stated measurement window or definition of "use")
- **Quote**: "Around 94% of Preply engineers use Codex and AI coding assistants for code generation, PR reviews, debugging, and accelerating development workflows."
- **Our assessment**: This 94% figure is a near-saturation engineering-adoption number, comparable in kind (though not sourced the same way) to the ChatGPT-Enterprise-wide 95% figure in Claim 3 — together they suggest Preply achieved near-universal adoption across both the general-employee and engineering-specific tool categories, which is a stronger combined adoption signal than either figure alone. Note the phrasing "Codex and AI coding assistants" is ambiguous about whether Codex specifically reaches 94%, or whether 94% is the union of Codex plus any other AI coding tool in use — the source does not disambiguate, so this figure should be cited as "94% of engineers use some combination of Codex and AI coding assistants," not as "94% Codex-specific adoption."

### Claim 8: Dmytro Voloshyn describes Codex as enabling engineers to write code at unprecedented speed, freeing them to focus more on system architecture and customer problems rather than implementation
- **Evidence**: Direct quote from Dmytro Voloshyn describing his own enthusiasm for and framing of Codex's impact on engineering work.
- **Confidence**: anecdotal (single executive's characterization of an org-wide effect, no before/after metric for architecture-time allocation or any measured productivity figure tied specifically to Codex, as distinct from the 94% adoption figure in Claim 7)
- **Quote**: "It's the topic I'm most excited about. Codex helps us write code with a speed that was previously unseen. With such a powerful tool, engineers can focus more on architecture in the system as a whole and solving customers' problems."
- **Our assessment**: This is the same "implementation speed frees engineers for higher-altitude work" framing documented elsewhere in the corpus (e.g., the Notion case study's "spec document" shift, `blog-openai-notion-codex-case-study.md` Claim 8), but here it is asserted at the level of a CTO's general characterization rather than illustrated with a specific feature, time estimate, or before/after example — unlike the Notion source, which anchors an identical claim in one engineer's concrete ported-feature story. This claim should be cited as CTO-level rhetoric about the *category* of benefit, not as a measured or example-grounded instance of it.

### Claim 9: Preply reports six quantified results — 95% ChatGPT weekly active usage among employees, 75% of English-language learners actively using Lesson Insights, 70%+ of tutors using the feature, ~75% of active learners still engaging with Lesson Insights more than a year after adoption, a 4.7/5 satisfaction rating from more than 300,000 ratings, and a 70% product-market-fit score
- **Evidence**: Verbatim "Results" bulleted list, each item with a specific percentage or rating.
- **Confidence**: emerging (six specific, named metrics — the richest quantified block in the article — but no stated measurement methodology, survey instrument, or time window for any of them; "product market fit score" and its "70%" figure are asserted as "significantly above the threshold often associated with strong customer demand" without naming the threshold, methodology, or scoring instrument)
- **Quote**: "95% ChatGPT weekly active usage among Preply employees / 75% of English-language learners actively use Lesson Insights, powered by OpenAI APIs / More than 70% of tutors use the feature / Around 75% of active learners continue engaging with Lesson Insights more than a year after adoption / 4.7/5 satisfaction rating among tutors and students, from more than 300k ratings received directly on the platform / 70% product market fit score, significantly above the threshold often associated with strong customer demand"
- **Our assessment**: The long-run retention figure (~75% of active learners still engaging with Lesson Insights more than a year after adoption) is the single strongest data point in this block for a "durable, not novelty" argument — Emily Stott's own framing of it as evidence against the "AI tools might have an element of novelty" concern (Claim 10) is explicit and reasonable, but it is still a self-reported figure with an undefined "active learner" denominator (active in what sense — logging in, taking lessons, or something else — is not specified). The 4.7/5 rating from 300k+ ratings is a large sample size relative to most anecdotal case-study metrics in the corpus, though the rating instrument itself (what exactly respondents were asked) is not described.

### Claim 10: Emily Stott explicitly frames the long-run engagement data as evidence against the concern that AI-tool enthusiasm is a temporary novelty effect
- **Evidence**: Direct quote from Emily Stott interpreting the retention figure in Claim 9.
- **Confidence**: anecdotal (a single product manager's interpretive framing of the company's own retention statistic, not an independent analysis controlling for other explanations of sustained usage)
- **Quote**: "We know AI-powered tools might have an element of novelty. But if people are coming back and engaging months later, time and time again, that's a very strong signal of value—learners and tutors find value in our solutions."
- **Our assessment**: This is a reasonable interpretive point (novelty effects typically decay, so multi-year sustained engagement is at least consistent with genuine value) but it is not a controlled comparison — the source gives no counterfactual (e.g., retention of a comparable non-AI feature, or a cohort that opted out of Lesson Insights) that would let a reader distinguish "sustained value" from other explanations (e.g., the feature becoming a default/expected part of the product experience that most users simply don't opt out of). Treat as the company's own plausible-but-unverified interpretation of its retention number, not as independently established evidence against novelty effects.

### Claim 11: Michelle Garcia Ramos, a Spanish tutor, reports that Preply's AI feature cut her class-prep and homework-creation time by more than half, from "hours and hours" to less
- **Evidence**: Direct quote from a named tutor describing her own before/after time allocation.
- **Confidence**: anecdotal (single tutor's self-reported time estimate, no measured time-tracking data, no detail on which specific AI feature — Lesson Insights directly, or a related tool — she used for prep)
- **Quote**: "Before I started using Preply's AI feature, I would spend hours and hours prepping for classes and creating homework. But now that time has been cut by more than half."
- **Our assessment**: This is the article's only front-line practitioner (as opposed to executive/PM) account, and it is a concrete, checkable-in-principle claim (halved prep time) rather than vague praise. It corroborates the article's Claim 1 thesis (AI automating administrative overhead, not the teaching itself) with a first-person instance, but as with the Notion and BBVA case studies elsewhere in the corpus, this is a single named individual selected by the vendor for a promotional piece, not a surveyed sample of Preply's 100,000+ tutors.

### Claim 12: Preply names three "Leadership lessons" (treat AI as cultural transformation not a tooling rollout; pick a small number of high-impact use cases rather than many shallow experiments; build vendor partnerships that support rollout and problem-solving) and three "Tips" (make AI a stated company priority; invest in structured enablement; work directly with users — tutors — to build datasets and evaluate prompts)
- **Evidence**: Verbatim bulleted "Leadership lessons" and "Tips" lists, each item with a one-sentence elaboration.
- **Confidence**: anecdotal (vendor-authored/vendor-curated lessons lists; no detail on how these six items were selected or whether other lessons were considered and excluded)
- **Quote**: "Pick high-impact use cases: It's better to go deep on a small number of features with clear user value and measurable impact than many experiments that don't reach quality" and "Work with users: Preply collaborated with tutors to build data sets, evaluate prompts and ensure it had high standards for quality"
- **Our assessment**: This "lessons learned" bulleted-list format is structurally identical to the "Leadership lessons" / "Lessons learned" sections in `blog-openai-bbva-banking-transformation.md` and `blog-openai-endava-frontiers.md` — all three OpenAI customer-story pages use the same template (metrics box, named-executive quotes, results bullets, closing lessons/tips bullets), which is more likely evidence of OpenAI's consistent house editorial framing than three companies independently converging on identical advice. The one item with genuine specificity beyond generic "AI adoption is change management" framing is "Work with users" — naming tutors specifically as the group Preply collaborated with to build training data and evaluate prompts is a concrete practice (domain-expert-in-the-loop dataset/prompt evaluation) not present in the BBVA or Endava lessons lists, which describe leadership training and governance but not frontline-worker involvement in model/prompt evaluation.

## Concrete Artifacts

```
Source: OpenAI, "How Preply combines AI and human tutors to personalize learning,"
https://openai.com/index/preply (published June 12, 2026; retrieved via Wayback
Machine snapshot — see Extraction Notes)

Case-study metadata block:
  Products:     ChatGPT, API, Codex
  Company size: Mid-market
  Region:       Global
  Industry:     Technology, Education

Headline stat block (verbatim, four tiles):
  95%    ChatGPT weekly active usage among Preply employees
  70%+   Tutors actively use AI-powered Lesson Insights
  70%    Product market fit score
  4.7/5  Satisfaction rating for Lesson Insights

"Results at a glance" → "Results:" (verbatim bulleted list, full version):
  - 95% ChatGPT weekly active usage among Preply employees
  - 75% of English-language learners actively use Lesson Insights,
    powered by OpenAI APIs
  - More than 70% of tutors use the feature
  - Around 75% of active learners continue engaging with Lesson Insights
    more than a year after adoption
  - 4.7/5 satisfaction rating among tutors and students, from more than
    300k ratings received directly on the platform
  - 70% product market fit score, significantly above the threshold
    often associated with strong customer demand

"Leadership lessons" (verbatim bulleted list with elaborations):
  - Treat AI as a cultural transformation, not a tooling rollout:
    Adoption accelerates when leadership sets a clear strategy, teams
    are trained to use it, and AI becomes part of everyday work across
    the business
  - Pick high-impact use cases: It's better to go deep on a small
    number of features with clear user value and measurable impact
    than many experiments that don't reach quality
  - Build partnerships: Work with organizations that can support
    rollout, develop teams' knowledge, and collaborate on how to solve
    customers' problems in the best way

"Tips" (verbatim bulleted list with elaborations):
  - Make it a company priority: Preply's adoption of ChatGPT Enterprise
    was reflected in its strategy, roadmaps, and objectives—signaling
    that its use was an expectation, not an experiment
  - Invest in enablement: Structured training, hands-on workshops, and
    internal sessions helped teams move from curiosity to practical
    usage
  - Work with users: Preply collaborated with tutors to build data
    sets, evaluate prompts and ensure it had high standards for quality

Lesson Insights report contents (verbatim bulleted list):
  - A summary of key lesson topics
  - Grammar corrections and explanations
  - Vocabulary highlights and translations
  - Pronunciation feedback
  - Recommended next steps

Closing line: "The future, Preply believes, isn't human or AI. It's
human-led, AI-enabled."
```

## Cross-References

- **Corroborates**:
  - `blog-openai-bbva-banking-transformation.md` and `blog-openai-endava-frontiers.md`:
    all three are OpenAI customer-story pages sharing an identical article template
    (metrics stat block, named-executive quotes, a "Results at a glance" bullet list, a
    closing "Lessons learned"/"Leadership lessons" bullet list). Preply's near-universal
    company-wide ChatGPT Enterprise usage (95% WAU, Claim 3) is directionally consistent
    with BBVA's "70%+ weekly active usage across deployed employees" — both cite very high
    but self-reported weekly-active-usage figures — though Preply's rollout (600+ employees)
    is roughly two orders of magnitude smaller than BBVA's (~100,000 employees), a scale
    difference worth noting whenever these two WAU figures are cited together.
  - `blog-openai-notion-codex-case-study.md` Claim 5 ("Codex's tendency to spend time
    exploring/planning before writing code results in output that matches Notion's
    codebase conventions") and Claim 8 ("Nystrom now spends more of his time writing spec
    documents... than writing code by hand"): Dmytro Voloshyn's Claim 8 here ("engineers
    can focus more on architecture in the system as a whole and solving customers'
    problems") is the same "implementation speed frees engineers for higher-altitude work"
    pattern, but stated at CTO-generalization level rather than illustrated with a specific
    engineer/feature example, which is a meaningfully thinner version of the same claim.
  - `blog-anthropic-human-agent-teams.md`: that first-party Anthropic post (also authored
    by a member of an Education team — Kristen Swanson) frames effective human-agent
    collaboration around shared context, defined roles, and trust-proportional autonomy.
    Preply's Lesson Insights design — generating AI output *before* the lesson ends so the
    human tutor and student review it together in the same session (Claim 4) — is a
    concrete, customer-facing (not internal-engineering) instance of keeping a human
    reviewer in the loop at the point AI output is first consumed, a structurally similar
    design principle applied to a different (education product, not internal-team) context.

- **Contradicts**: None filed. One candidate tension was considered and rejected as a
  conditioning-variable difference, not a factual disagreement: `blog-simonwillison-josh-comeau-course-sales-ai.md`
  reports that free LLM-based tutoring is one factor Comeau blames for depressed sales of
  paid *developer-education video courses* (Comeau's course sales down to roughly ⅓ of a
  typical launch, peers reporting "Revenue down 50%+"), which could superficially read as
  opposing evidence to this source's claim
  that AI strengthens rather than displaces paid human tutoring. The two sources describe
  different markets and different AI roles: Comeau's source describes general-purpose LLM
  chat *substituting for* a paid instructional product (a one-way replacement), while this
  source describes AI *embedded inside* a paid human-tutoring product to reduce the tutor's
  administrative overhead (a complementary integration, not a substitute product). Both
  claims could be true simultaneously in their respective markets — general-purpose LLMs
  eroding demand for static prerecorded courses is not in tension with an AI-augmented
  live-tutoring marketplace retaining engagement — so per MINER.md §4a this was not filed
  as a contradiction.

- **Extends**:
  - `blog-openai-bbva-banking-transformation.md` and `blog-openai-endava-frontiers.md`:
    extends the corpus's small set of OpenAI enterprise customer-story sources with a third
    data point — education/consumer-marketplace rather than banking or IT consulting — and
    with a customer-facing AI feature (Lesson Insights) as the centerpiece, rather than
    purely internal productivity tooling. Neither BBVA's nor Endava's case study centers a
    customer-facing generative-AI product feature the way this source does.
  - `blog-anthropic-human-agent-teams.md`: extends that post's internal, engineering/
    knowledge-work-oriented human-agent-teaming principles to a customer product context —
    a live illustration of "review AI output together with the human before it's acted on"
    applied to end-users (tutors and students) rather than internal Anthropic teams.

- **Novel**:
  - **Timing AI generation to complete before an interaction ends, specifically so a human
    can review the output together with another human in the same session** (Claim 4) — no
    existing corpus source describes this specific timing-for-co-review design pattern; most
    human-in-the-loop patterns documented elsewhere (e.g. `blog-anthropic-human-agent-teams.md`)
    describe asynchronous or internal-team review, not a live, two-party, same-session review
    moment engineered into the product timeline.
  - **A lesson-transcript-to-personalized-homework generation pipeline** (Claim 5) — the
    specific architecture of using a live interaction's own transcript as the direct input
    for that individual's next practice content is new to the corpus's education-adjacent
    sources.
  - **A frontline, non-engineering worker (a tutor) explicitly named as a data-set-building
    and prompt-evaluation collaborator** ("Work with users," Concrete Artifacts) — the BBVA
    and Endava lessons lists both describe leadership training and governance, but neither
    names frontline domain experts as direct collaborators in building training data or
    evaluating prompts; this is a more specific practice than either.
  - **A >1-year post-adoption retention figure explicitly used to argue against a novelty-effect
    explanation** (Claims 9–10) — most adoption metrics elsewhere in the corpus report
    weekly/monthly active usage or point-in-time satisfaction; this is the corpus's first
    OpenAI customer-story source citing a specific long-run (>1 year) retention figure with
    an explicit interpretive claim about durability of value versus novelty.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add the "Work with users" tip (Claim 12 / Concrete
  Artifacts) — Preply collaborating directly with tutors (frontline domain experts, not
  engineers or leadership) to build datasets and evaluate prompts — as a concrete variant
  of "involve the people who will use the tool in building it," worth contrasting with
  BBVA's and Endava's leadership-centric lessons lists, which describe training and
  governance but not frontline-worker involvement in model/prompt evaluation.
- **Chapter 03/07 (Verification / Operations), if discussing human-in-the-loop product
  design**: Add Claim 4 (Lesson Insights generation scheduled to finish *before* the lesson
  ends, so tutor and student review AI output together in the same session) as a concrete,
  specific example of designing an AI feature's timing around a co-review moment, rather
  than delivering AI output asynchronously for unsupervised consumption. This is a more
  specific pattern than the general "keep a human in the loop" guidance already in the
  guide — it names the *mechanism* (timing) that creates the review opportunity.
  Caveat: the source gives no detail on what happens when generation isn't ready in time,
  or what recourse exists for incorrect AI-generated feedback, so this should be cited as a
  design pattern to describe, not as an audited safety mechanism.
- **Chapter 05 (Team Adoption)**: Note the ChatGPT Enterprise weekly-active-usage figures
  (95% at Preply's ~600-employee rollout vs. BBVA's 70%+ at ~100,000 employees) as a data
  point for a "usage-rate benchmarks should be read alongside organization scale" caution —
  if the guide ever compares WAU figures across case studies, it should flag that smaller,
  centrally-run rollouts appear to reach higher usage percentages than very large,
  federated ones, at least in this small sample of vendor-published figures.
- **Chapter 01 (Daily Workflows), if citing engineering-adoption saturation figures**: The
  94% Codex/AI-coding-assistant adoption figure (Claim 7) is a data point for near-universal
  engineering-org adoption, comparable to (though not directly poolable with, given
  different definitions) other high-adoption figures already in the corpus; cite with the
  caveat that "Codex and AI coding assistants" is not disambiguated as Codex-specific usage.

## Extraction Notes

- The live URL (`https://openai.com/index/preply`) returned HTTP 403 to both the WebFetch
  tool and direct `curl` with a browser user-agent (Cloudflare bot-protection challenge
  page), consistent with the OpenAI-domain extraction difficulties already documented in
  `blog-openai-bbva-banking-transformation.md`, `blog-openai-endava-frontiers.md`, and
  `blog-openai-notion-codex-case-study.md`'s Extraction Notes. A direct Wayback Machine
  fetch of the canonical URL also returned a captured Cloudflare challenge page rather than
  the article (the crawler itself was blocked at capture time for that specific snapshot).
  The CDX API (`web.archive.org/cdx/search/cdx?url=openai.com/index/preply`) was queried
  directly to check all captures of this URL, which surfaced one snapshot with HTTP 200 and
  a substantially larger byte count (`20260617030416`, 53,124 bytes, versus ~7,500–7,800
  bytes for the other five `403` captures) — that snapshot was the actual rendered article
  and was fetched with `curl`, then parsed with a local Python script (`re`-based tag
  stripping, script/style removed) rather than through an AI-summarization pass, so that
  every `Quote` field above could be copied character-for-character per MINER.md §2a. Every
  quote was independently re-checked against the extracted plain text before being copied
  into this note.
- The source is short (~900 words) with no linked sub-pages containing further substantive
  content about this case study; the page's "Keep reading" footer links to three unrelated
  OpenAI news posts (a model-behavior-simulation research post, an OpenAI Partner Network
  product announcement, and an OpenAI Academy courses announcement), none of which concern
  Preply and none were followed.
- This is a single-source, vendor-published, three-practitioner case study (one executive,
  one product manager, one tutor). Every claim above should be read with that ceiling in
  mind: OpenAI selected which quotes and metrics to publish, Preply did not publish an
  independent account, and no metric in the piece states a measurement methodology (window,
  sample, or instrument). The quantified "Results" block (Claim 9) is unusually rich for
  this case-study format (six named metrics vs. Endava's zero and BBVA's eight), which is
  why several claims here reach "emerging" rather than "anecdotal" — but even the
  richest-evidenced claims (Claims 3, 4, 7, 9) remain single-company, self-reported figures.
- One contradiction candidate was considered and explicitly rejected (Comeau course-sales
  source) — see Cross-References → Contradicts for the full reasoning; no contradiction
  issue was filed.
- All cross-reference claim numbers cited above (from `blog-openai-bbva-banking-transformation.md`,
  `blog-openai-endava-frontiers.md`, `blog-openai-notion-codex-case-study.md`, and
  `blog-anthropic-human-agent-teams.md`) were verified by re-reading each cited note's actual
  claim numbering and content before writing this note; none were guessed.
