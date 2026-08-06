---
source_url: https://cursor.com/blog/vercel
source_type: blog-post
title: "How Vercel used Cursor to build Queues"
author: "Cursor Team (vendor case study; named practitioners: Joe Haddad — Distinguished Engineer, Marcos Grappeggia — Product Manager, both at Vercel; quoting Vercel CTO Malte Ubl)"
date_published: 2026-07-28
date_extracted: 2026-08-06
last_checked: 2026-08-06
status: current
confidence_overall: emerging
issue: "#2521"
---

# How Vercel used Cursor to build Queues

> A named-practitioner customer case study documenting how Vercel built Queues, a durable event streaming system, entirely with Cursor across three architectural rewrites — with agent-led end-to-end testing against real AWS infrastructure, six-cycle context compaction without information loss, engineer-driven model switching via parallel planning agents, Slack-initiated Cloud Agent delegation, and expansion of Cursor use to product managers shipping features without engineering resources.

## Source Context

- **Type**: blog-post (vendor case study published on Cursor's blog, July 28, 2026; ~5 min read; seven named sections with attributed pull-quotes from two named Vercel practitioners — Joe Haddad, Distinguished Engineer, and Marcos Grappeggia, Product Manager — plus one attributed quote from Vercel CTO Malte Ubl embedded in body text)
- **Author credibility**: Byline is "Cursor Team" (vendor-authored), but the substantive claims are attributed to named Vercel employees, not anonymized. Haddad is introduced as "one of Vercel's longest-tenured engineers," having "spent the last seven years building Vercel's core infrastructure and now works primarily on critical backend systems" — this gives his quotes practitioner weight on a project (Queues) he personally led. Grappeggia is named as a Product Manager providing the non-engineering-adoption angle. Malte Ubl is named as Vercel's CTO, and the "iteration velocity" philosophy is attributed to him as an internally coined phrase, not sourced from an external interview. This is a vendor case study (Cursor benefits commercially from favorable coverage of Vercel's usage), so treat quantitative claims as self-reported and emerging rather than externally audited.
- **Scope**: Covers the build of Vercel Queues (a durable event streaming system) entirely with Cursor across three rewrites; Haddad's harness-vs-model preference and model-switching workflow; Cursor's context compaction reliability over long sessions; Cloud Agents and Slack-initiated delegation; agent-led end-to-end testing against real AWS services (DynamoDB, Kinesis) with fault injection; stacked-PR code review; Vercel's engineering-velocity metrics (PR throughput, cycle time, resources per feature, hours saved) among "heaviest Cursor users"; and PM adoption of Cursor for product understanding, analytics, and quick fixes. Does NOT cover: cost/pricing, model names used beyond "Claude," "Opus," "GPT," and "GPT-5.4," the specific metric baseline period, team size, or any details on Queues' technical architecture beyond "durable event streaming system."

## Extracted Claims

### Claim 1: Vercel Queues, "one of Vercel's most important new infrastructure products," was built entirely with Cursor across three separate architectural rewrites, each refining the design based on internal dogfooding
- **Evidence**: Named artifact (Queues) with a stated build history (three rewrites) and stated rationale (learning from internal dogfooding), attributed to Haddad and his team.
- **Confidence**: anecdotal (single named project, single company, self-reported by the team that built it)
- **Quote**: "Haddad and his team built the product entirely with Cursor across three separate rewrites, each one refining the architecture based on what the team learned from internal dogfooding."
- **Our assessment**: "Entirely with Cursor" is a strong claim for a "durable event streaming system" — mission-critical infrastructure, not a prototype or internal tool. The three-rewrite detail is notable: it frames AI-assisted infrastructure building as an iterative architecture-discovery process (build, dogfood, learn, rebuild) rather than a single linear implementation. No detail is given on what changed between rewrites or how much of each rewrite was agent-authored vs. human-authored, so "entirely with Cursor" should be read as "Cursor was used throughout the build," not as a precise measurement of AI-authored code share.

### Claim 2: Haddad believes the harness matters more than the underlying model, and did not perceive a step-change in model capability ("the AGI moment") until using frontier models inside Cursor specifically
- **Evidence**: Two named pull-quotes from Haddad, both drawing an explicit contrast between model capability and harness/platform quality.
- **Confidence**: anecdotal (single practitioner's subjective framing)
- **Quote**: "Cursor offers the best harness, and the platform has the smoothest developer experience of anything I've tried." ... "I didn't feel the AGI moment with Opus or GPT until I used it in Cursor. After that, my expectations for coding agents were raised so high that using those models in other coding harnesses became untenable."
- **Our assessment**: This is a strong, specific articulation of the "harness matters more than model" thesis already well-represented in the corpus (see Cross-References). The "AGI moment" framing is notable because it locates the perceived capability jump not at a model release but at the intersection of a specific model and a specific harness — implying the same model underperforms in a lesser harness. This is a testable, falsifiable claim in principle (does the same model produce materially worse outcomes in a different harness?) but the post provides no controlled comparison, only Haddad's retrospective impression.

### Claim 3: Haddad frequently switches between Claude and GPT-5.4 depending on task fit, and uses parallel planning agents across models to decide which model to commit to for a given piece of work
- **Evidence**: Named quote plus a described workflow (fire off parallel planning agents, review each plan, commit to the strongest).
- **Confidence**: anecdotal (single practitioner's workflow description)
- **Quote**: "I was a steady Claude user through Opus 4.5, but when GPT-5.4 came out I started shifting more of my work over." (Article text, not in quotation marks: "Whenever he starts on a new problem space, Haddad uses Cursor to compare which model performs best. He'll fire off parallel planning agents, review each plan, and then commit to the strongest one for that leg of work.")
- **Our assessment**: The parallel-planning-agent-as-model-selection workflow is the concrete mechanism behind the more general "model switching" claim in the Prospector's triage notes. It is a specific, reusable pattern: rather than picking a model by reputation or benchmark, generate competing plans from multiple models for the same problem and let a human judge the plan quality before committing execution resources. This shifts model selection from a static, per-organization policy decision to a per-task, per-session evaluation — notable because it requires a harness that makes running multiple models on the same prompt cheap and low-friction.

### Claim 4: Cursor's context compaction retained critical session details (test procedures, previously-created resources) across six or more compaction cycles, where other harnesses Haddad tried lost this information
- **Evidence**: Named quote plus contrastive framing against unnamed "other coding agent harnesses Haddad tried."
- **Confidence**: anecdotal (single practitioner's comparative impression; no named comparison harness, no measurement of what "compact itself six times over" quantifies in tokens or turns)
- **Quote**: "I could actually let Cursor run and compact itself six times over without any issues." ... "Without Cursor, even the best models struggle with context management. That causes them to stop prematurely or forget key details during their work."
- **Our assessment**: This is the most guide-relevant technical claim in the source, but it is qualitative and comparative without naming the comparison harness or quantifying "issues." The body text adds specificity: in other harnesses Haddad tried, "models would lose critical details during compaction, forgetting how to run tests or failing to reference resources they had created earlier in the session" — this is a concrete failure mode (losing test procedures and created-resource references) that matches the "architectural why is the first thing compaction destroys" pattern documented elsewhere in the corpus. The claim is consistent with, but does not independently verify, Cursor's own published mechanism for improved compaction (see Cross-References — Extends).

### Claim 5: Cursor's Cloud Agents let Haddad delegate work to run asynchronously in the background while he worked on other tasks, and he frequently starts Cloud Agents directly from Slack conversations so they inherit discussion context
- **Evidence**: Described workflow with a supporting quote on cloud agent dependability.
- **Confidence**: anecdotal (single practitioner's workflow description)
- **Quote**: "Cursor's cloud agents are dependable and strongly sandboxed. This makes the cloud experience much more useful because agents can accomplish real work without constantly escalating to the user."
- **Our assessment**: The Slack-initiated Cloud Agent pattern ("He frequently kicks off agents directly in Slack conversations so they have context on an issue he's already been discussing with coworkers") is structurally the same engineer-initiated Slack-to-agent handoff pattern documented at Faire (see Cross-References — Corroborates), giving two independent named-practitioner accounts of the same invocation pattern. The "dependable and strongly sandboxed" framing is offered as the reason escalation-free autonomous execution is trustworthy — sandboxing is presented as a precondition for delegation confidence, not just a security feature.

### Claim 6: Agent-led end-to-end testing against real AWS infrastructure — connecting to DynamoDB and Kinesis, injecting faults, and simulating bugs across hundreds of stacked PRs — was "a significant part of meeting our quality bar" for Queues
- **Evidence**: Named quote plus body-text description of the specific testing pattern and named AWS services.
- **Confidence**: anecdotal (single project, single team, self-reported quality outcome — no defect rate, incident count, or independent quality measurement given)
- **Quote**: "Cursor's harness allowed agents to ground themselves in production AWS environments with real resources. Agent-led testing was a significant part of meeting our quality bar with Vercel Queues."
- **Our assessment**: This is the most operationally specific claim in the source: "Engineers would instruct agents to work on the Queues API, connect to AWS, read side effects from DynamoDB and Kinesis, inject faults, simulate bugs, and verify results." This describes agents performing verification against live cloud infrastructure and side effects (not mocks or unit tests) as a named quality-assurance mechanism for a "mission-critical" system, repeated "across each leg of work and hundreds of stacked PRs." No detail is given on the sandboxing/isolation boundary for testing against "production AWS environments with real resources" — a question the guide should flag rather than assume is safely scoped, since fault injection and bug simulation against production-adjacent infrastructure carries real blast-radius risk if isolation is imperfect.

### Claim 7: Cursor's integrated code review lets Haddad review agent-generated code inline and break work into stacked PRs his team can review incrementally
- **Evidence**: Body-text description of the review workflow, motivated by the fact that "every change goes through deep review" for critical backend infrastructure.
- **Confidence**: anecdotal (single practitioner's workflow description)
- **Quote**: (no direct quote for this specific claim; see paraphrase in Our assessment) — the article states: "Cursor's integrated review experience lets him review agent-generated code inline, iterate with the agent, and then break work into stacked PRs that his team can review incrementally."
- **Our assessment**: This pairs the "hundreds of stacked PRs" testing claim (Claim 6) with the review mechanism that makes that volume reviewable: decomposing agent output into stacked, incrementally-reviewable PRs rather than large monolithic changes. This is consistent with the stacked-PR pattern already documented at Faire (see Cross-References), giving a second named-practitioner account of stacked PRs as the delivery unit for agent-generated infrastructure code specifically (not just application feature code).

### Claim 8: Among Vercel's "heaviest Cursor users," PR throughput increased 54%, PR cycle time decreased 89%, resources allocated per feature dropped 27%, and this works out to 104 hours saved per developer annually — measured against Vercel's existing engineering-velocity metrics
- **Evidence**: Named quantitative metrics, explicitly scoped to "power users" / "heaviest Cursor users," tied to Vercel's pre-existing tracked metrics ("PR velocity, time to first review, time to merge, and number of review cycles before merge").
- **Confidence**: emerging (specific named metrics tied to metrics Vercel says it already tracks organization-wide, which is stronger grounding than a metric invented for the case study; but self-reported, no baseline period defined, no comparison group, and explicitly scoped to power users rather than all Cursor users at Vercel)
- **Quote**: "Among Vercel's Cursor power users, PR throughput is up 54%, PR cycle time is down 89%, and resources allocated per feature dropped 27%. That works out to 104 hours saved per developer annually."
- **Our assessment**: The explicit "power users" / "heaviest Cursor users" scoping (repeated three times in the article) is an important caveat the guide should preserve: these are not average or organization-wide figures, so the numbers describe an upper bound achieved by the most engaged users, not a typical or expected result of adopting Cursor. The 89% cycle-time decrease is a large figure without a stated baseline (89% of what starting cycle time?). The "104 hours saved per developer annually" figure is derived ("that works out to"), not independently measured — its derivation method (from which of the three percentage figures, over what assumed working-hours base) is not shown in the source.

### Claim 9: Vercel's engineering-metrics philosophy — "Iteration velocity solves all known software problems" — is a phrase CTO Malte Ubl coined internally, and is the stated reason Vercel tracks PR velocity, time to first review, time to merge, and review-cycle count
- **Evidence**: Named attribution to Vercel's CTO, presented as the rationale for the specific metrics the company tracks.
- **Confidence**: anecdotal (a stated organizational philosophy, not an empirical claim; presented as internally coined, not externally sourced or fact-checked in this piece)
- **Quote**: "The philosophy behind focusing on these metrics comes from Vercel's CTO, Malte Ubl, who coined the phrase internally: 'Iteration velocity solves all known software problems.'"
- **Our assessment**: This is a leadership-level framing claim rather than a technical one: it asserts that fast iteration is the dominant lever for software quality/outcomes, which is why Vercel measures PR-cycle metrics as its primary engineering health signal. The claim is presented at face value with no supporting argument or evidence in the article — it functions as an organizational mission statement that justifies why the case study's chosen metrics (PR throughput, cycle time) are the ones Vercel considers meaningful, rather than an independently supportable general claim about software engineering.

### Claim 10: Vercel has expanded Cursor adoption beyond engineering to product managers, with PM Marcos Grappeggia using it for cross-repository product understanding, product-analytics queries against the data warehouse, and shipping small fixes that would otherwise sit in engineering backlogs
- **Evidence**: Named PM with three specific, distinct use cases described in the article's structured list, plus a closing attributed quote.
- **Confidence**: anecdotal (single named non-engineer, single company; no measurement of how many PMs at Vercel use Cursor or how much engineering time this has actually offloaded)
- **Quote**: "PMs are using Cursor to ship features and fix bugs without requiring resources from other parts of the business."
- **Our assessment**: The three named use cases are concretely differentiated, not generic: (1) "Understanding the product" — Grappeggia "loads multiple repositories into a multi-root workspace and queries across all of them" to answer customer feature-support questions live in meetings, with lift estimates, "without interrupting an engineer"; (2) "Product analytics" — using "data warehouse CLIs and MCPs" with Cloud Agents running "long durations" for analyses the data team lacks bandwidth for; (3) "Shipping quick changes" — one-shotting small bugs that "would otherwise sit in P2 backlogs indefinitely," with a named example (a polling bug in the Vercel CLI's project-linking flow) that "engineering wouldn't have gotten to for weeks." This is a specific, checkable instance of the broader "AI coding tools expand who can ship code" narrative, distinguished from generic "non-engineers can code now" claims by naming the exact mechanisms (multi-repo workspace queries, data-warehouse MCP integration, one-shot bug fixes) rather than asserting the outcome alone.

## Concrete Artifacts

### Headline metrics (article callout boxes, repeated at top and bottom of page)

```
Source: "How Vercel used Cursor to build Queues" (Cursor blog, Jul 28, 2026)
Scope: "Vercel's Cursor power users" / "heaviest Cursor users" — NOT org-wide average

  54%     Increase in PR throughput
  89%     Decrease in PR cycle time
  27%     Decrease in resources allocated per feature
  104 hrs Saved per developer annually

Vercel Queues: "Product built entirely with Cursor"
Vercel is described in the page metadata as: "a Cloud Infrastructure company
in North America."
```

### Agent-led AWS testing pattern (Building Vercel Queues with Cursor section)

```
Source: "How Vercel used Cursor to build Queues" (Cursor blog, Jul 28, 2026)

"Engineers would instruct agents to work on the Queues API, connect to AWS,
read side effects from DynamoDB and Kinesis, inject faults, simulate bugs,
and verify results. Haddad would repeat this pattern across each leg of
work and hundreds of stacked PRs."

Named AWS services touched by agents: DynamoDB, Kinesis
Verification actions performed by agents: connect, read side effects,
  inject faults, simulate bugs, verify results
Delivery unit: stacked PRs (hundreds, across the Queues build)
```

### Vercel's tracked engineering-velocity metrics (Measuring impact section)

```
Source: "How Vercel used Cursor to build Queues" (Cursor blog, Jul 28, 2026)

"Vercel tracks engineering velocity and quality through a few key metrics:
PR velocity, time to first review, time to merge, and number of review
cycles before merge."

Attributed philosophy (Malte Ubl, Vercel CTO, internally coined):
"Iteration velocity solves all known software problems."
```

### PM use cases (Expanding beyond engineering section, verbatim list structure)

```
Source: "How Vercel used Cursor to build Queues" (Cursor blog, Jul 28, 2026)
Named PM: Marcos Grappeggia, Product Manager, Vercel

1. Understanding the product.
   "Grappeggia loads multiple repositories into a multi-root workspace and
   queries across all of them. When a customer asks whether Vercel supports
   a specific feature, he can get an answer in the same meeting, along with
   an estimate of how much lift a change would require, without
   interrupting an engineer."

2. Product analytics.
   "PMs use Cursor with data warehouse CLIs and MCPs to dig into product
   usage patterns. Cloud agents can run for long durations to develop
   complex analyses that Vercel's data team doesn't have bandwidth for."

3. Shipping quick changes.
   "PMs use Cursor to one-shot small bugs and improvements that would
   otherwise sit in P2 backlogs indefinitely. A polling bug in the Vercel
   CLI's project linking flow was a quick fix implemented with Cursor that
   engineering wouldn't have gotten to for weeks."
```

## Cross-References

### Cross-reference verification notes
`blog-cursor-faire-cloud-agents.md`, `blog-cursor-cloud-agent-lessons.md`,
`blog-cursor-composer-self-summarization.md`, `blog-cursor-better-models-ambitious-work.md`,
`blog-latentspace-vercel-andrew-qu-eve.md`, and `blog-anthropic-vlasenko-pm-agent-orchestration.md`
were re-read in full during this extraction per MINER.md §4b, and every claim
number cited below was located and confirmed against that note's own numbered
claims in document order before writing this section.

- **Corroborates**:
  - `blog-cursor-faire-cloud-agents.md` Claim 4 (Faire's Slack-to-PR pattern: "You can see the message, kick off @cursor in the same context, and you get a PR a few minutes later") — this source's Claim 5 (Haddad "frequently kicks off agents directly in Slack conversations so they have context on an issue he's already been discussing with coworkers") is a second, independent named-practitioner account of the same engineer-initiated Slack-thread-as-context invocation pattern, at a different company. Both are engineer-initiated (contrast with Amplitude's fully automated Slack-monitoring pipeline referenced in the Faire note).
  - `blog-cursor-faire-cloud-agents.md` Claim 6 (Faire's stacked-PR delivery: plan mode → step-by-step plan → cloud agent → five stacked PRs in two hours) — this source's Claim 7 (Haddad's "integrated review experience... break work into stacked PRs that his team can review incrementally") is a second named-practitioner account of stacked PRs as the review/delivery unit for agent-generated code, here applied to "hundreds of stacked PRs" for infrastructure work rather than a single internal tool.
  - `blog-cursor-cloud-agent-lessons.md` (Josh Ma, Cursor engineering) general framing that environment quality and durable execution underpin cloud agent reliability — this source's Claim 5 ("Cursor's cloud agents are dependable and strongly sandboxed") is a customer-side practitioner endorsement of the reliability properties that source describes from the infrastructure-builder side (Temporal-based durable execution, past "two 9s" reliability). Neither source names the other's specific mechanism (Temporal is not mentioned in this case study), so this is corroboration of the outcome (dependability), not verification of the mechanism.
  - `blog-cursor-better-models-ambitious-work.md` Claim 4 (task-category distribution shifting toward documentation, architecture, and code review as AI-generated code volume rises) — this source's emphasis on "deep review," inline agent-code review, and stacked-PR decomposition for a "critical backend" system is a concrete instance of the code-review-burden growth that study documents at the aggregate behavioral-data level; this case study supplies the qualitative practitioner workflow (why and how review is structured) that the aggregate study cannot show.

- **Extends**:
  - `blog-cursor-composer-self-summarization.md` Claim 2 (trained self-summarization reduces compaction error 50% vs. a prompt-engineered baseline on CursorBench) and Claim 7 (the DOOM benchmark: 170-turn session, 100k+ tokens compressed to ~1,000 tokens of preserved critical information) — this source's Claim 4 (Haddad: "I could actually let Cursor run and compact itself six times over without any issues," contrasted with other harnesses where agents "forgot key details" and "stop[ped] prematurely") is real-world practitioner evidence consistent with the internal-benchmark claims in the self-summarization post. Neither source states that the self-summarization training technique is specifically what Haddad experienced — this case study does not name the underlying mechanism — so this is presented as consistent, not as direct confirmation that the trained self-summarization feature is what Haddad is describing.
  - `blog-anthropic-vlasenko-pm-agent-orchestration.md` (a non-technical PM at Mythical Games using 15+ parallel Claude Code subagents to ship a production iOS app solo) — this source's Claim 10 (Grappeggia, a Vercel PM, using Cursor for product understanding, analytics, and shipping small fixes without engineering resources) extends the "non-engineers building/shipping with AI coding tools" pattern to a different vendor (Cursor vs. Claude Code) and a different scope (targeted PM workflows integrated into an existing engineering org, vs. one person building a standalone app end-to-end). Together, two independent vendor case studies (Anthropic, Cursor) document non-engineers using coding-agent tooling to ship real, shipped work rather than prototypes.

- **Complicates (same company, different product team, risk of conflation)**:
  - `blog-latentspace-vercel-andrew-qu-eve.md` documents Vercel Chief of Software Andrew Qu's account of `eve`, Vercel's own framework for *building* agents (used by Vercel's customers and internally, e.g., for v0). This source documents a *different* Vercel team (Haddad's infrastructure/backend engineering group) using *Cursor*, a third-party vendor tool, to build Queues. These are not the same initiative and should not be merged in the guide: this source is about Vercel as a *customer* of an external coding-agent product; the Qu interview is about Vercel as a *builder* of its own agent framework. Both are true simultaneously and are not in tension, but a reader skimming both notes could easily conflate "Vercel's agent tooling" as a single effort. The guide should keep these explicitly separate when citing either.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No claim in this source directly opposes a claim in an existing corpus note.

- **Novel**:
  - **Agent-led fault injection and bug simulation against real (non-mocked) AWS infrastructure as a named quality-assurance mechanism for mission-critical infrastructure** (Claim 6): no other corpus source documents an agent both writing infrastructure code and independently exercising fault-injection/bug-simulation testing against live cloud service side effects (DynamoDB, Kinesis) as part of meeting a stated "quality bar." This is a more aggressive verification pattern than the video-demo (Faire/Playground) or CI-based verification patterns already in the corpus.
  - **Parallel planning agents across models as a live, per-task model-selection mechanism** (Claim 3): existing corpus sources document model switching as a general capability or a routing/classifier decision; this source is the first to describe an engineer manually firing off competing planning agents on different models for the same problem and choosing execution based on plan quality, rather than relying on a router or a fixed per-organization model policy.
  - **A named CTO-level engineering philosophy ("Iteration velocity solves all known software problems") explicitly given as the stated rationale for a company's chosen engineering metrics** (Claim 9): no other corpus source attributes a specific coined internal phrase to a named CTO as the justification for which velocity metrics a company tracks.
  - **"Power users" as an explicit, repeated scoping qualifier on headline productivity metrics** (Claim 8): several other corpus case studies (Faire, PayPal, NAB) report headline percentage or multiplier metrics without a stated user-segment scope; this source is explicit and repeated ("Cursor power users," "heaviest Cursor users") that its 54%/89%/27%/104-hours figures describe the most engaged user segment, not an org-wide or median outcome — a scoping discipline worth calling out as a positive example when the guide discusses how to read vendor-reported productivity metrics.

## Guide Impact

- **Chapter 03 (Model Selection)**: Add Claim 3's parallel-planning-agent workflow ("fire off parallel planning agents, review each plan, and then commit to the strongest one for that leg of work") as a concrete, reusable model-selection heuristic distinct from router-based or fixed-policy approaches already covered. Frame it as a per-task evaluation technique available to engineers working in harnesses that make multi-model plan generation cheap, rather than a universal recommendation — it trades extra planning-stage cost for reduced risk of committing execution budget to the weaker model.

- **Chapter 02 (Working with AI Agents — verification)**: Add Claim 6 (agent-led fault injection and bug simulation against real AWS infrastructure) as a new, more aggressive point on the corpus's verification-pattern spectrum, alongside the Faire Playground video-demo pattern and CI-based verification. Explicitly flag the open question this source does not answer: what isolation/blast-radius controls bound "production AWS environments with real resources" during fault injection — the guide should not present this pattern as safe-by-default without that detail, and should note it as a gap in the sourced evidence rather than assume best practice was followed.

- **Chapter 04 (Evaluation and Measurement)**: Use Claim 8 as a worked example of how to read vendor-reported productivity metrics: note the explicit "power users only" scoping as something practitioners should look for (and demand) in any productivity claim, contrasted with case studies elsewhere in the corpus that report headline multipliers without stating whether they describe average or best-case users. Pair with Claim 9 (Ubl's "iteration velocity" philosophy) as an example of a named organizational rationale for choosing PR-cycle metrics specifically as the primary engineering-health signal, which the guide's measurement chapter can present as one defensible metric philosophy among others (not the only correct one).

- **Chapter 05 (Team Adoption)**: Add Claim 10 (Grappeggia's three PM use cases: multi-repo product-understanding queries, data-warehouse analytics via MCP, one-shot small-bug fixes) as a second, differently-scoped corpus example of non-engineer adoption of coding-agent tooling — narrower in scope than the solo-app-building PM case in `blog-anthropic-vlasenko-pm-agent-orchestration.md`, but embedded inside an existing engineering organization rather than operating independently. Recommend the guide present both as points on a spectrum: PM-augments-existing-engineering-team (this source) vs. PM-replaces-need-for-engineering-team-on-a-project (Vlasenko/Mythical Games case).

- **Chapter 01 (Daily Workflows)**: Add Claim 5's Slack-initiated Cloud Agent pattern as a second named-practitioner confirmation (alongside Faire) of engineer-initiated, conversation-context-as-agent-context invocation — strengthening this as a recurring, cross-company workflow pattern worth naming explicitly rather than treating as one company's idiosyncratic habit.

## Extraction Notes

1. **WebFetch's AI-summarized pass under-quoted the source**: An initial WebFetch call returned a clean-looking set of quotes and section summaries, but a follow-up verification pass (per MINER.md §2a) surfaced that at least one quote had been silently trimmed (the "of anything I've tried" clause was dropped from Haddad's first quote in the initial summary) and one pull-quote's full text ("Cursor's cloud agents are dependable and strongly sandboxed. This makes the cloud experience much more useful...") had been shortened. Per the same pattern documented in `blog-latentspace-vercel-andrew-qu-eve.md`'s Extraction Notes, I fetched the raw page directly via `curl` with a browser user agent, stripped HTML tags with a Python script, and located every quote in this note character-for-character in that raw-text capture before using it. All `Quote` fields in this note were verified against that raw capture, not against either WebFetch pass.
2. **One passage of ambiguous attribution was deliberately excluded from quoted claims**: immediately following the pull-quote block in the "Building Vercel Queues with Cursor" section, the raw text contains an unattributed sentence — "Cursor's intelligent context management allowed agents to remember every resource created, side effects observed, and test run across long sessions with multiple compaction events." — that appears to be narrative body copy (likely written by the Cursor Team byline) rather than a Haddad quote, since it follows the "Joe Haddad / Distinguished Engineer, Vercel" attribution line for the *preceding* quote and is not itself set off with quotation marks or a new attribution. I did not attribute this sentence to Haddad in any claim above; it is folded into Claim 4's "Our assessment" as supporting body-text detail, not presented as a direct quote.
3. **No sub-pages followed**: the article is a single self-contained page with no inline links to other Vercel or Cursor documentation, technical deep-dives on Queues' architecture, or the underlying methodology for the headline metrics. MINER.md §1's "follow up to 5 linked pages" guidance did not apply — there were no substantive linked pages present.
4. **No independent verification of quantitative claims possible**: all metrics (54%, 89%, 27%, 104 hours) are self-reported by Vercel via a vendor (Cursor) case study, with no baseline period, comparison group, or methodology disclosed. Treated as `emerging` rather than `settled` throughout, consistent with how the corpus treats other vendor case-study metrics (Faire, PayPal, NAB).
5. **No contradictions filed**: this source's claims are additive to and consistent with the existing corpus. No claim here opposes a claim in `blog-cursor-faire-cloud-agents.md`, `blog-cursor-cloud-agent-lessons.md`, `blog-cursor-composer-self-summarization.md`, `blog-cursor-better-models-ambitious-work.md`, or `blog-latentspace-vercel-andrew-qu-eve.md`.
