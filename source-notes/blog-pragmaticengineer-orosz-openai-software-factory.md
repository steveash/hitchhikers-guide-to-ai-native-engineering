---
source_url: https://newsletter.pragmaticengineer.com/p/openai-software-factory
source_type: blog-post
title: "Inside OpenAI's agentic software factory"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-09-15
date_extracted: 2026-09-16
last_checked: 2026-09-16
status: current
confidence_overall: emerging
issue: "#3480"
---

# Inside OpenAI's agentic software factory

> First-hand, on-site dispatch from Gergely Orosz's return visit to OpenAI, quoting seven named engineering leaders (Venkat Venkataramani, Sulman Choudhry, Andrew Ambrosino, Joe Gershenson, Akshay Nathan, Ahmed Ibrahim, Steve Coffey) on how Codex displaced nearly every other internal tool in under a year, a 9-step "agentic software factory" pipeline spanning context-gathering through agentic deploy and incident response, and the infrastructure strain (10x load growth in six months) that rapid agent-driven code output is putting on CI/CD, version control, and mobile release pipelines — with the free preview cutting off at the start of section 4 of 7, leaving billion-user-scale infra, API reliability, and "how the job is changing" entirely paywalled.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter, Substack, paid tier; published September 15, 2026). The free preview covers the first three of seven announced sections in full (Codex adoption; death of the IDE/PR rethinking; the agentic software factory pipeline) before the paywall cuts in one sentence into section 4 ("How engineering tooling & practices are changing"). Sections 5-7 (scaling to a billion users, API reliability/performance, and how the software engineering job is changing) are entirely behind the paywall with no visible teaser content beyond the top-of-post one-line summaries.
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager who runs The Pragmatic Engineer, the largest paid technology newsletter on Substack, and is already a trusted, heavily-corroborated corpus author (`blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`, `blog-pragmaticengineer-orosz-inside-anthropic.md`, `blog-pragmaticengineer-bun-rust-rewrite.md`, `blog-pragmaticengineer-orosz-ramp-inspect.md`). This is first-hand reporting: Orosz states he "visited one of the world's leading frontier labs" and interviewed seven named people on the record — Venkat Venkataramani (VP of Engineering, Applied Infra), Sulman Choudhry (Head of Engineering, ChatGPT), Andrew Ambrosino (Lead, Desktop), Joe Gershenson (Lead, Core Agent team), Akshay Nathan (Engineering Lead, Productivity), Ahmed Ibrahim (Engineer, Codex), and Steve Coffey (Engineer, Responses API). The article explicitly frames itself as a return visit ("Plenty has changed since I visited OpenAI's headquarters last year"), referencing the same reporting relationship as `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md` (June 30, 2026) and paralleling the structure of `blog-pragmaticengineer-orosz-inside-anthropic.md` (July 28, 2026), which explicitly promised "a later article, we'll compare findings from Anthropic and OpenAI" — this appears to be that promised OpenAI-focused follow-up, or a close successor to it.
- **Scope**: The free preview substantively covers: (1) Codex/ChatGPT Work's near-total displacement of other internal tools since ~January 2026, including adoption drivers (desktop app, `/goal` long-running tasks, role-specific plugins, embedded domain experts); (2) the death of the IDE and the infrastructure strain (10x load growth) forcing a rethink of PRs, code review, and mobile deployment; (3) the 9-step "agentic software factory" pipeline from human-defined outcome through agentic code review, agentic deploy, production observation, and automated incident response (Sevbot). It does NOT substantively cover section 4 ("How engineering tooling & practices are changing" — cut off after one introductory sentence) or sections 5-7 (scaling to a billion users, API reliability/performance, and "how the software engineering job is changing" — named only in the seven-item top-of-post summary list, zero body content visible).

## Extracted Claims

### Claim 1: At OpenAI, Codex (and later Codex plus ChatGPT Work) went from a "nice-to-have" tool to the backbone of nearly everything at the company within about a year, with the shift concentrated starting around January 2026
- **Evidence**: Author's own framing after the visit, corroborated by named engineer Andrew Ambrosino's direct quote about the change.
- **Confidence**: emerging (first-hand reporter synthesis plus a named, on-the-record engineer's framing of the same shift)
- **Quote**: "The big theme of the past months has been that everything is now a coding agent. Whether the visible code is your output or not, agents write your artifacts. Think of it like this: your entire life is via software. You have these powerful tools (agents) in your computer, and the ability to loop and reason and write code is the ability to do everything."
- **Our assessment**: This is a strong, specific articulation of a "coding agent as universal work interface" thesis — not just "developers use agents more" but a claim that non-code artifacts (documents, spreadsheets, presentations) are now routed through a coding-agent harness by default. It sets up the concrete adoption data in Claim 2 and is consistent with the broader "agent as default work surface" framing already in `blog-openai-agents-transforming-work.md` Claim 1 ("Agentic AI changes the unit of knowledge work from single interactions to delegated, long-horizon tasks").

### Claim 2: Non-engineering departments (finance, recruitment, legal) at OpenAI went from ~0% Codex usage to 90% usage within a four-month period, and now almost all OpenAI employees use Codex and ChatGPT Work weekly
- **Evidence**: A department-level adoption chart sourced and captioned by Orosz directly from OpenAI's own public post, described in the article's prose.
- **Confidence**: emerging (first-party vendor chart, reproduced and narrated by an independent reporter who had it explained to him during the visit, rather than only read cold off the OpenAI blog)
- **Quote**: "In a four-month period, non-engineering orgs like finance, recruitment, and legal went from ~0% usage of Codex to 90% usage. Now, almost all OpenAI employees use Codex and ChatGPT Work weekly."
- **Our assessment**: This is the same underlying chart and telemetry already extracted in `blog-openai-agents-transforming-work.md` (the article's own image caption credits "Source: OpenAI" linking to `openai.com/index/how-agents-are-transforming-work`), so it is not independent corroboration of the 90% figure — it is the same first-party number relayed through a second venue. Its value is context: it also substantiates, for the first time with visible detail, the previously paywalled teaser in `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md` Claim 10 ("more than 95% of non-engineers use Codex, not ChatGPT" — stated there as a headline-only, unelaborated figure). The two numbers (95% vs. 90%) are close but not identical, and likely reflect different snapshots or slightly different cohort definitions (the June article's figure was framed as "non-engineers using Codex over ChatGPT" specifically, while this article's 90% is department-level Codex-usage-share from the chart) — worth flagging in the guide as "same directional claim, two close-but-not-identical numbers from the same underlying trend," not as a discrepancy to resolve.

### Claim 3: OpenAI's internal version of Codex is meaningfully more advanced than the external product because it is plugged into nearly every internal system — Git, Slack, Notion, Databricks, Datadog, and internal logs — a pattern Orosz explicitly compares to Ramp's internal Inspect agent
- **Evidence**: Author's own aside, drawing an explicit parallel to a separate company he had previously reported on.
- **Confidence**: emerging (reporter's own comparative observation, informed by two separate on-site visits to two different companies)
- **Quote**: "Caveat: OpenAI's internal version of Codex is a lot more advanced than its external counterpart because it's plugged into pretty much every OpenAI system – similar to how Ramp's Inspect AI agent has been wired up."
- **Our assessment**: This is a useful, explicit, cross-company pattern claim from the same reporter: internal deployments of a company's own coding agent routinely outstrip the external product in context/integration depth. This directly extends `blog-pragmaticengineer-orosz-ramp-inspect.md` (Ramp's internal Inspect agent) by explicitly naming it as the comparison point — the guide should treat "internal agent deployments are wired into far more systems than the external product" as a now twice-observed pattern from the same credible reporter, not a one-off.

### Claim 4: A `/goal` setting for long-running Codex tasks drove adoption from 60% to 90% between April and May 2026, and shifted usage toward fewer, much longer-running agent threads that themselves spin off sub-agents
- **Evidence**: Direct quote from Andrew Ambrosino, Lead of Desktop, describing the mechanism and its effect on how people work.
- **Confidence**: emerging (single named, senior, on-the-record source describing a specific shipped feature and a dated adoption jump)
- **Quote**: "The number one thing that is changing is that people are starting to use threads for much longer, and this longer usage has been a breakthrough. It's surprising to see the sheer length of time that people spend on a thread – even days! They often set a goal and then have the model crank. Codex being good at longer-running tasks seems to cause people to do fewer things in parallel. This is because a long-running agent often spins off other agents to do other things, reducing the surface area that you, as a human, have to manage."
- **Our assessment**: The "fewer things in parallel, because the single long-running agent spins off its own sub-agents" framing is a specific and somewhat counterintuitive nuance — it suggests that as agent autonomy over longer horizons improves, the locus of parallelism shifts from "the human juggling several top-level agent sessions" (the pattern documented elsewhere in the corpus, e.g. `blog-openai-codex-knowledge-work.md` Claim 6's ~50%-of-users-running-parallel-tasks figure) to "one agent orchestrating its own sub-agents," with the human managing a smaller surface area. This is worth flagging as a claim about how parallelism itself is being restructured, not just increasing in volume — a distinction the guide's harness-engineering chapters should preserve.

### Claim 5: OpenAI's Codex/Productivity team attributes rapid non-engineering adoption partly to an "awareness gap" rather than a capability gap — the underlying capability existed before most users discovered applicable use cases, and discovery now spreads primarily through word-of-mouth between teammates
- **Evidence**: Direct quote from Akshay Nathan, Engineering Lead, Productivity team.
- **Confidence**: emerging (single named, on-the-record source's framing, consistent with the broader adoption-curve pattern described elsewhere in the article)
- **Quote**: "For a long time, we had a 'capability overhang': the models were capable but the products didn't fully bring that out. Now, we're seeing an awareness gap. Some people have figured out they can use Codex to monitor Slack, update Airtable, or create onboarding materials. But many others still use it for one task and then discover more uses from teammates via word-of-mouth. But there's still so much more, under the surface, that you can do with Codex."
- **Our assessment**: The "capability overhang → awareness gap" framing is a specific, named two-stage model of adoption bottlenecks that is novel to the corpus in this exact terminology. It implies that once a coding-agent product crosses a usability threshold, the binding constraint on further adoption becomes internal word-of-mouth discovery of use cases rather than product capability — a distinct claim from, but consistent with, the "role-specific plugins accelerate adoption" mechanism described in Claim 6 below (plugins are one deliberate response to exactly this awareness gap).

### Claim 6: OpenAI accelerated non-engineering adoption by having teams build and distribute role-specific and team-specific plugins/skills rather than relying on a generic, one-size-fits-all coding agent
- **Evidence**: Direct quote from Andrew Ambrosino explaining the product rationale.
- **Confidence**: emerging (single named, on-the-record source describing a deliberate product strategy)
- **Quote**: "If you build a product that can do anything, teams need a way to make it their own. You can't just give everyone an empty box. Skills and plugins let teams adapt the agent to their work. Sometimes, we also need a new app capability, like a browser that the agent can use alongside those skills. But the same building blocks already cover a lot of different roles."
- **Our assessment**: This is a concrete product-design claim relevant to harness engineering: a maximally general agent still needs role-specific "skins" (skills/plugins) to reach non-technical adopters, even when the underlying model and tool primitives are shared across roles. It is a practical counterpoint to any guide framing that suggests a single generic harness configuration is sufficient once model capability is high enough.

### Claim 7: Non-technical departments at OpenAI now embed domain experts directly onto engineering teams (e.g., for ChatGPT Work), because the model has become "smarter" than developers in some non-engineering domains and developers alone cannot encode the necessary domain "taste" into the harness
- **Evidence**: Author's own synthesis from the visit, presented as an organizational observation rather than attributed to a single named quote.
- **Confidence**: anecdotal (reporter's synthesis of what he observed/was told, not a single direct quote or a measured organizational statistic)
- **Quote**: "The models have become 'smarter' than developers in some domains, so devs cannot channel 'taste' into the harness in those areas. So, people who are domain experts are onboarded onto engineering teams."
- **Our assessment**: Orosz's own aside flags this as "a decades-old best practice for building quality products" being "rediscovered" in an AI context — worth preserving that self-aware framing in the guide so this isn't presented as a novel AI-era invention. The underlying claim (domain expertise must be embedded directly in the team building the harness, not routed through a developer intermediary, once the model exceeds developer domain knowledge) is a concrete, guide-relevant staffing implication for teams building agent products for non-engineering users.

### Claim 8: OpenAI is now so dependent on Codex and ChatGPT Work for internal work that during even minor outages, internal colleague alerts to the Codex/Work teams arrive at the same time as, or before, automated monitoring alerts
- **Evidence**: Author's own observation/summary from the visit.
- **Confidence**: anecdotal (reporter's characterization, not tied to a specific named quote or incident count)
- **Quote**: "This is so much the case that in the event of even a minor outage, internal messages from colleagues alert the Codex and Work teams at the same time as – or before – automated alerts."
- **Our assessment**: This is a vivid, falsifiable-in-principle organizational signal of total internal dependency on a single harness — human-reported outage detection outpacing automated monitoring is a distinctive claim (most organizations would expect the reverse). It corroborates, from OpenAI's side, the same total-dependency pattern quantified in `blog-openai-agents-transforming-work.md` Claim 2 (Codex = 99.8% of weekly company-wide output tokens at OpenAI) — this article supplies the qualitative, human-behavior evidence for what that post supplies as a raw percentage.

### Claim 9: Despite internal doubt in December 2025 about whether a standalone Codex desktop app made sense (with Antigravity's VS Code fork raising the question of whether OpenAI should fork an IDE too), the team shipped the app on a bet that AI agents would make IDEs matter less — a bet the team now considers vindicated by falling IDE usage since January
- **Evidence**: Direct quote from Andrew Ambrosino describing the internal debate and decision, with the author's own follow-up observation that IDE usage has since declined.
- **Confidence**: emerging (single named, senior, on-the-record source's account of an internal product decision, with the outcome corroborated by the reporter's own stated observation of usage trends during the visit)
- **Quote**: "In December 2025, we weren't entirely sure if we would release the Codex app. We had the Codex CLI as a terminal, and there are large, feature-rich IDEs out there. So, would there be space for a dev tool that is between a terminal and an IDE? In my head, there was this future where it would not work out, and be the kind of 'misfit' like the iPad was. [...] Also, don't forget that in November, Antigravity came out as a VS Code fork. This added to the feeling that perhaps we should have also forked VS Code for the Codex app. But still, we dismissed the temptation and went with our gut feeling that as AI agents get better, IDEs will matter less."
- **Our assessment**: This is a concrete, dated internal product-strategy decision (Dec 2025 desktop-app go/no-go, explicitly considered and rejected the "fork an IDE" alternative that a competitor took) with a stated rationale (agents will make IDE feature-richness matter less over time) that the article's own later reporting (IDE usage down since January) treats as vindicated. It is a useful, named data point for any guide discussion of whether coding-agent products should be built as IDE forks versus a distinct terminal/app-native surface — OpenAI's Codex team explicitly considered and rejected the IDE-fork path that Antigravity took.

### Claim 10: Rapid Codex-driven code output has caused roughly a 10x increase in load on some of OpenAI's development-infrastructure systems within about six months — growth Venkat Venkataramani says would normally take two to three years at most companies — forcing continuous, month-over-month infrastructure scaling work
- **Evidence**: Direct quote from Venkat Venkataramani, VP of Engineering, Applied Infra.
- **Confidence**: emerging (single named, senior infrastructure leader's on-the-record account, internally consistent with the article's broader "software factory" load narrative)
- **Quote**: "The number of pull requests (PRs) per engineer is growing like a hockey stick (at a very high, accelerating rate). Every part of the build-test-deploy pipeline is seeing dramatically more load. We're talking about roughly a 10x increase in load on some systems. At most companies, that kind of growth might happen over two or three years. At OpenAI, we see it in about six months. [...] Every month, we wake up to a new set of infrastructure scaling challenges to solve. Just when we think we've created enough capacity for the next phase of growth, the model unlocks another wave of capabilities, which creates a new set of bottlenecks somewhere else in the system."
- **Our assessment**: This is a specific, quotable, dated infrastructure-load figure from the leader directly responsible for it — a strong candidate for a guide section on the operational/infrastructure consequences of high agent-driven code velocity, distinct from (and more infrastructure-specific than) the corpus's existing coverage of individual-developer or team-level productivity gains. The "every month, a new bottleneck" framing is a useful caveat against treating any single infrastructure investment as a one-time fix for agent-driven load growth.

### Claim 11: Venkat Venkataramani argues that core software-engineering primitives — code review and pull requests specifically — "make less and less sense" in their traditional form at agent-driven velocity, and describes OpenAI's response as agentic code review by multiple domain-specialist agents plus an agentic deploy step that "handholds" changes to production and builds its own monitoring dashboards
- **Evidence**: Direct quote from Venkat Venkataramani.
- **Confidence**: emerging (single named, senior infrastructure leader describing both a stated philosophy and shipped/in-progress systems built to implement it)
- **Quote**: "The question we ought to ask ourselves in the middle of all this development acceleration is how do we reimagine many things we took for granted. For example, how do we reimagine the CI (continuous integration) and CD (continuous deployment) process? What does observability mean in this world, and how should people interact with pull requests? If you ask me, the way we do code review today makes less and less sense, and the same is true for pull requests. We're now seeing agentic code reviews that look at code changes through a series of different lenses. In the past, it would have been impractical for a cloud infrastructure engineer and a security engineer to review every single code change. With agents, that becomes possible. We can rethink how code is deployed with agents, too. We are building an agent that 'handholds' a change all the way to production — whether it's a code change or a change behind a feature flag. It observes the relevant monitoring graphs, but can also build its own dashboard to monitor important signals. More of our code changes are going to production with this kind of agent monitoring."
- **Our assessment**: The "multiple domain-specialist review agents, each simulating a different infrastructure/security specialist's perspective" pattern is a concrete, named architecture for agentic code review that is more specific than generic "AI code review" claims elsewhere in the corpus (e.g., `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 7-8's single-reviewer Claude Code Review at Anthropic/Bun). Orosz's own skeptical aside is worth preserving: "I was skeptical about the claim that an agent that's told to be a cloud infra specialist would produce a different review from a generic agent. However, all Codex agents have full access to OpenAI's code and docs, so this 'cloud infra expert' agent likely has gathered a lot of context... The important thing is how these 'domain specialist' agents are set up, the context they have access to, and how they focus only on their own domain to make best use of their limited context window." This caveat — that the value of a "specialist" agent persona comes from scoped context and focus, not some inherent domain knowledge the base model lacks — is a useful, generalizable harness-design point independent of OpenAI specifically.

### Claim 12: OpenAI classifies code changes by risk level and lets low-risk-classified areas of the codebase auto-approve PRs without human review, while high-risk changes get stricter gates (more AI reviews, mandatory human review after agents finish)
- **Evidence**: Author's own summary of the risk-classification mechanism described during the visit, following directly from Venkataramani's account of agentic code review.
- **Confidence**: emerging (specific, describable mechanism attributed to the same reporting context as the directly-quoted material around it, though not itself a direct quote)
- **Quote**: "Code changes are classified by risk. High-risk changes can be sent through stricter processes; for example, they might invoke more AI code reviews, or mandate that a human reviews it after the AI agents finish. Low-risk changes follow an easier path; areas of the codebase can opt in to an agent that will auto-approve low risk PRs, removing human acceptance as a bottleneck and improving velocity."
- **Our assessment**: This is a concrete, actionable governance pattern — risk-tiered review intensity with an opt-in auto-approve path for low-risk code areas — that is more operationally specific than the "auto-merge" material already in the corpus. It directly parallels Jarred Sumner's forward-looking auto-merge prediction in `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 12 ("another Claude with a fresh context window judges if it's simple and low blast-radius → if it is: auto-merge!"), except OpenAI's version is described as already opt-in-deployed for some codebase areas rather than a near-term prediction — worth flagging in the guide as evidence that risk-tiered auto-merge/auto-approve has moved from "predicted" (Anthropic/Bun, July 2026) to "shipped in at least some form" (OpenAI, by September 2026) within about two months, across two different labs.

### Claim 13: Native mobile app deployment (iOS/Android) is becoming an increasingly painful bottleneck relative to backend/web deployment because Apple's and Google's manual app-store review processes have not sped up even as code-generation velocity has increased dramatically — a problem Sulman Choudhry compares to Facebook's mobile-release-velocity breakthrough in the 2010s
- **Evidence**: Direct quote from Sulman Choudhry, Head of Engineering for ChatGPT, drawing on his prior experience at Facebook.
- **Confidence**: emerging (single named, senior, on-the-record source with directly relevant prior-company experience, describing a structural constraint that is independently verifiable — app store review processes are public policy, not an internal OpenAI claim)
- **Quote**: "Back in the 2010s, Facebook had a pretty important breakthrough in how to ship native mobile code faster. App Store releases went from monthly to bi-weekly to weekly. At the same time, experimentation and feature flags let teams ship code before it was ready to launch, then turn features on remotely when they were. That model brought a lot more velocity to mobile. In the age of Codex, I think we're hitting the next version of this problem. Code generation is getting dramatically faster, but getting that code into users' hands on native mobile is not. For Codex in particular, where usage is heavily mobile-first, that gap is already becoming painful for us and users. I expect the pressure here to increase quickly. If software can be written in minutes, waiting days or weeks to get it onto a phone starts to look increasingly absurd."
- **Our assessment**: This identifies a structural bottleneck to AI-driven velocity gains that is external to any individual company's engineering practices — app-store review latency is fixed by Apple/Google policy, not solvable by better internal tooling. It's a useful, concrete caveat for any guide claim that agent-driven code velocity translates directly and proportionally into faster user-facing release cadence: for mobile specifically, it does not, and the gap is widening rather than narrowing as code-generation speed increases. Orosz's own closing aside reinforces this: "There's some irony in how shipping a native iOS or Android app has the exact same challenges today as in 2008, when the App Store was launched. In 18 years, not much has changed!"

### Claim 14: OpenAI's "agentic software factory" is a named, described 9-step pipeline — from a human defining the desired outcome, through Codex gathering context from company-wide systems, implementation, CI with a "perf harness," multi-agent domain-specialist code review, agentic deploy with self-built dashboards, production observation, continuous performance-regression feedback via "Perf Factory," and automated incident response via "Sevbot" — with the explicit long-term goal of a "per-change autonomous SRE"
- **Evidence**: Author's structured walkthrough of the pipeline as described directly by Venkat Venkataramani, illustrated with a named diagram ("OpenAI's 'agentic software factory'") comparing it to the traditional software development pipeline.
- **Confidence**: emerging (detailed, named, multi-step process description attributed to a senior engineering leader with direct visibility into it; internally consistent with the more granular claims — Claims 10-12 — describing individual pipeline stages)
- **Quote**: "The idea of a 'software factory' is similar to a physical factory where robots and humans produce autos together. In the software context, it is AI agents and humans producing software. Some manufacturing sites are fully automated 'dark factories' where illumination isn't needed because there are no humans. Could the same fully automated process emerge in software engineering? At OpenAI today, there's a 'software factory' running and it's all built around Codex."
- **Our assessment**: The "dark factory" framing — an explicit, named end-state aspiration (full automation with no humans required) rather than merely "AI-assisted development" — is a clear, quotable articulation of where OpenAI's infrastructure leadership says this pipeline is heading, useful for framing a guide discussion of the trajectory (not just the current state) of agentic software delivery. The pipeline's step-by-step structure (see Concrete Artifacts) is the most complete, named, end-to-end agentic-SDLC description currently in the corpus from a single company.

### Claim 15: Sevbot, OpenAI's Codex-built internal incident-response agent, currently collects incident context, proposes (but never autonomously executes) mitigations, and answers on-call engineers' questions in Slack — with human on-call duty still required today, but OpenAI's stated goal is for Sevbot to eventually handle "routine" outages autonomously so no one is woken up outside working hours
- **Evidence**: Author's description of Sevbot's current capabilities and OpenAI's stated goal for it, in the context of the pipeline's final ("respond to outages") stage.
- **Confidence**: anecdotal (a named tool with current-state capabilities described in the article, but the "no humans woken up" outcome is an explicitly stated future goal, not a current reality — "as of now, oncall duty is not a thing of the past at the company")
- **Quote**: "OpenAI's goal is to get to the point where Sevbot can take autonomous action when mitigating some outages. The dream is that no humans be woken up outside of their working hours during an outage because Sevbot can handle 'routine' outages autonomously, with humans reviewing its actions when they return to work. But as of now, oncall duty is not a thing of the past at the company."
- **Our assessment**: The article is explicit and self-aware about the capability/goal gap here — Sevbot today is a context-gathering and human-advising agent, not an autonomous incident-mitigator, and the reporter preserves that distinction rather than conflating current state with stated ambition. This is a useful, honestly-caveated data point for a guide section on agentic incident response: even at a frontier lab with an otherwise highly automated pipeline, autonomous execution of production mitigations is explicitly not yet trusted, only proposal and advisory functions are.

## Concrete Artifacts

### Interviewees (verbatim, from the article's introduction)

```
Source: https://newsletter.pragmaticengineer.com/p/openai-software-factory

"To learn more, I talked with seven engineering leaders and engineers there:
Venkat Venkataramani (VP of Engineering, Applied Infra), Sulman Choudhry
(Head of Engineering, ChatGPT), Andrew Ambrosino (Lead, Desktop), Joe
Gershenson (Lead, Core Agent team), Akshay Nathan (Engineering Lead,
Productivity), Ahmed Ibrahim (Engineer, Codex) and Steve Coffey (Engineer,
Responses API)."
```

Joe Gershenson, Ahmed Ibrahim, and Steve Coffey are named but not directly quoted anywhere in the free-preview portion of this article — their contributions likely appear in the paywalled sections 4-7.

### Article structure (from the top-of-post "we cover" summary, all visible pre-paywall)

```
Source: https://newsletter.pragmaticengineer.com/p/openai-software-factory

1. Codex takes over at OpenAI.
   [SUBSTANTIVELY COVERED IN FREE PREVIEW — see Claims 1-9]
2. Death of the IDE & pull requests.
   [SUBSTANTIVELY COVERED IN FREE PREVIEW — see Claims 9-13]
3. OpenAI's agentic software factory.
   [SUBSTANTIVELY COVERED IN FREE PREVIEW — see Claims 14-15]
4. How engineering tooling & practices are changing.
   [PAYWALLED — one introductory sentence only, no substantive content]
5. Engineering for a billion users: how OpenAI scales up its infra.
   [PAYWALLED — teaser only: "They buy first and take it in-house later.
   Also, geographic infra distribution, capacity planning tactics and
   challenges."]
6. Making OpenAI's API more reliable and performant.
   [PAYWALLED — teaser only: "CPUs are becoming a bottleneck, doing slower
   deployments on purpose, and solving load challenges."]
7. How the software engineering job is changing.
   [PAYWALLED — teaser only: "Engineering specializations are disappearing,
   judgment and agency are more important, and it only takes one or two
   engineers for previously 'impossible' rewrites and migrations to
   succeed."]

Paywall cutoff point (verbatim, end of free content):
"Unsurprisingly, Codex is changing how easy it is to build internal tools
and having an impact on standard engineering practices like debugging.
Here's what I gathered from talking with folks at OpenAI.

This post is for paid subscribers"
```

### OpenAI's 9-step "agentic software factory" pipeline (extracted from article body)

```
Source: https://newsletter.pragmaticengineer.com/p/openai-software-factory
Speaker: Venkat Venkataramani, VP of Engineering, Applied Infra (pipeline
description); named tools per step as stated in the article.

1. Human builder defines the desired outcome (engineer or PM specifies the
   problem; judgment/prioritization/taste increasingly central to this role)
2. Codex gathers context — Git/GitHub, Slack, Notion, internal data
   (Databricks, Datadog, internal logs), and internal Codex "skills" (some
   maintained by Codex itself); OpenAI has moved documentation into source
   code specifically to make it easier for agents to find
3. Codex implements code changes and self-verifies against the goal
4. Build & test, then CI — agent babysits the PR until CI is green,
   including a new "perf harness" that routes problematic PRs to a
   "Synthetics A/B framework" for performance-impact evaluation
5. Agentic code review — multiple domain-specialist review agents (e.g. a
   "cloud infra specialist" persona) instead of one generic reviewer;
   changes are risk-classified, with low-risk areas eligible for
   agent-auto-approval and high-risk changes gated by more AI review and/or
   mandatory human review
6. Agentic deploy — after human approval, a dedicated agent "handholds" the
   change (including feature-flagged changes) to production: locates the
   flag, understands the change, decides success/failure signals, and
   builds its own monitoring dashboard
7. Production observation — the agent's own self-built dashboards plus
   OpenAI's existing internal observability stack (logs, metrics, traces,
   wide events)
8. "Perf Factory" — agents sift alerts/dashboards, de-duplicate signals,
   identify real latency regressions, root-cause them, and propose fixes,
   extending the loop into continuous post-deploy improvement
9. "Sevbot" (incident response, built on Codex) — wakes on incident
   detection, collects context, proposes (never autonomously executes)
   mitigations, answers on-call questions in Slack; an engineer must tell
   it to apply a mitigation. Long-term goal: autonomous handling of
   "routine" outages so no one is paged outside working hours; not yet the
   case today.
```

### Codex adoption timeline (extracted from article body and chart caption)

```
Source: https://newsletter.pragmaticengineer.com/p/openai-software-factory
Chart caption: "Codex usage since August 2025 at OpenAI by department.
Source: OpenAI" (linking to openai.com/index/how-agents-are-transforming-work)

- Feb 2026: Codex desktop app ships for Mac
- Mar 2026: Codex desktop app ships for Windows
- Feb-Apr 2026: ~40% adoption among non-engineering teams despite an
  interface still described as "hostile to non-technical users" (showed
  code on-screen)
- Apr-May 2026: /goal setting (long-running task goals) ships; adoption
  among the relevant cohort rises from 60% to 90%
- Jul 2026: ChatGPT Work launches (built on the Codex harness)
- "Now" (article present, ~Sep 2026): non-engineering orgs (finance,
  recruitment, legal) at ~90% usage, up from ~0% four months prior; almost
  all OpenAI employees use Codex/ChatGPT Work weekly
```

## Cross-References

- **Corroborates**: `blog-openai-agents-transforming-work.md` Claim 2 and Claim 5 — this article's Claim 2 (non-engineering orgs ~0% to 90% in four months) reproduces the same underlying OpenAI department-adoption chart and telemetry that source documents in more numeric detail (majority-Codex crossover dates, >85% average output-token share). Not independent corroboration of the number itself (same first-party source), but independent narrative confirmation via on-site interviews that the trend the chart shows is one OpenAI's own engineers describe consistently when asked directly.
- **Corroborates**: `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md` Claim 10 — that June 30, 2026 article's paywalled teaser ("more than 95% of non-engineers use Codex, not ChatGPT") is now substantively confirmed in direction and rough magnitude by this article's visible, sourced 90% figure (Claim 2), roughly 2.5 months later. Flag the close-but-not-identical numbers (95% vs. 90%) as likely different snapshot dates or cohort definitions rather than a discrepancy requiring resolution — see Claim 2's assessment.
- **Corroborates**: `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 14 — that article documents Anthropic engineers describing "no token budget, usage not tracked" as a distinctive AI-lab norm; this article's opening line makes the identical claim about OpenAI: "It's rare to work with an unlimited token budget, but at OpenAI, that's what all engineers, researchers, finance colleagues, and marketing folks do." This is genuine independent corroboration — two different companies, confirmed by the same reporter across two separate visits — that unlimited/untracked token budgets are a shared norm at frontier AI labs specifically, not an Anthropic-specific culture choice. The guide should treat "no token budget" as a lab-wide pattern (with the same generalizability caveat already flagged in the Anthropic note: this likely does not transfer to organizations that must track AI spend).
- **Extends**: `blog-pragmaticengineer-orosz-ramp-inspect.md` — this article's Claim 3 explicitly names Ramp's Inspect agent as the comparison point for "internal agent deployments are more deeply wired into company systems than the external product," directly linking the two source notes via the reporter's own stated analogy rather than an inferred similarity.
- **Extends**: `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 12 (Jarred Sumner's predicted near-future auto-merge gated by a fresh-context-window Claude judging blast radius) — this article's Claim 12 describes a similar risk-tiered auto-approval mechanism as already opt-in-deployed for low-risk codebase areas at OpenAI, suggesting the pattern predicted at Anthropic/Bun in July 2026 has a working analogue at OpenAI by September 2026. Not confirmed to be the same mechanism or maturity level — flagged as a parallel development worth tracking, not a verified match.
- **Extends**: `blog-openai-codex-knowledge-work.md` Claim 6 (~50% of Codex users running more than one task simultaneously) — this article's Claim 4 adds a nuance not present in that source: as long-running single-thread tasks (via `/goal`) become more capable, some users report doing *fewer* things in parallel themselves, because a single long-running agent now spins off its own sub-agents rather than the human managing several top-level parallel sessions. This is a distinct claim about *where* parallelism is occurring (agent-orchestrated vs. human-orchestrated), not a contradiction of the ~50%-parallel-usage figure.
- **Novel**: The full 9-step "agentic software factory" pipeline as a single named, end-to-end structure (Claim 14) — no existing corpus source describes a comparably complete, named agentic SDLC pipeline from a single company, spanning context-gathering through deploy, observation, performance regression response, and incident response. Also novel: the "capability overhang" vs. "awareness gap" two-stage adoption-bottleneck framing (Claim 5); the December 2025 Codex-desktop-app go/no-go decision and its explicit rejection of the IDE-fork path taken by Antigravity (Claim 9); the mobile app-store review bottleneck as a structural (non-OpenAI-specific) constraint on translating agent velocity into release velocity (Claim 13); Sevbot as a named, capability-scoped incident-response agent (Claim 15); risk-tiered code-review/auto-approval with domain-specialist reviewer agents (Claims 11-12).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Cite the 9-step agentic software factory pipeline (Claim 14, Concrete Artifacts) as the corpus's most complete single-company reference architecture for an end-to-end agentic SDLC — useful as a structural template even where individual steps (e.g., agentic deploy with self-built dashboards) are not yet broadly replicable elsewhere. Add Claim 11's caveat (domain-specialist review agents derive their value from scoped context and focus, not inherent domain knowledge the base model lacks) as a concrete design principle for any multi-agent review architecture the guide recommends.
- **Chapter 02 (Harness Engineering — Risk-Tiered Automation)**: Add Claim 12 (risk-classified auto-approval for low-risk PRs, stricter gates for high-risk changes) alongside `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 12's Bun/Anthropic auto-merge prediction as two labs' converging approaches to reducing human-review bottleneck at agent-driven PR volume — useful as a "risk-tiering, not blanket automation" pattern for teams considering auto-merge.
- **Chapter 04/05 (Team & Org Adoption)**: Add Claim 5 (capability overhang vs. awareness gap) and Claim 6 (role-specific plugins/skills as the deliberate response) as a concrete, named adoption-bottleneck framework distinct from the corpus's existing "adoption curve" material — useful for teams past the initial rollout stage wondering why usage has plateaued despite continued capability improvements. Add Claim 7 (embedding domain experts directly on engineering teams once the model exceeds developer domain knowledge) as a staffing implication for teams building agent products for non-engineering users.
- **Chapter 06 (Cost/Efficiency and Infrastructure)**: Add Claim 10 (10x infrastructure load growth in six months, "every month a new bottleneck") as a concrete, dated infrastructure-scaling data point for any guide section on the operational costs of high agent-driven code velocity — distinct from and complementary to the corpus's existing individual/team productivity-focused coverage. Add Claim 13 (mobile app-store review as a structural, non-tooling-solvable bottleneck) as an explicit caveat against assuming agent-driven code velocity translates proportionally into user-facing release velocity across all platforms.
- **Chapter 04 (Context Engineering)**: Add Claim 3 (internal agent deployments wired into far more systems — Git, Slack, Notion, Databricks, Datadog — than the external product) as a second data point (after Ramp's Inspect) for the pattern that a company's most capable internal agent deployment is defined primarily by breadth of system integration, not model choice.
- **Chapter 03 (Safety and Verification)**: Add Claim 15 (Sevbot: proposes but never autonomously executes incident mitigations; human on-call still required "as of now") as a concrete, currently-in-production example of a frontier lab deliberately withholding autonomous execution authority from an otherwise highly capable agent in a high-blast-radius domain (production incident response), even while automating most of the surrounding pipeline.

## Extraction Notes

- **Paywall boundary verified via raw HTML, not WebFetch summarization**: consistent with the pattern already documented in this same author's prior source notes (`blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`, `blog-pragmaticengineer-orosz-inside-anthropic.md`), an initial `WebFetch` pass returned a shortened, paraphrased summary of the article rather than verbatim text. The full free-preview content was instead retrieved via `curl` with a browser user-agent (HTTP 200), the `available-content` div isolated from the surrounding page chrome, and converted to flat text with `html2text`. The paywall boundary (`"This post is for paid subscribers"`) was located precisely in that flat text, immediately after one introductory sentence of section 4 ("How engineering tooling & practices are changing"). All quotes above were copied character-for-character from this raw-HTML-derived text, not from the earlier `WebFetch` summary.
- No sub-pages were followed. The article's only outbound links relevant to its claims are: (1) the author's own prior visit report (`https://newsletter.pragmaticengineer.com/p/san-francisco-is-back`), referenced only as "last year's visit" context and not itself re-fetched since it predates the corpus's coverage window and is not the subject of this issue; (2) the OpenAI chart source (`openai.com/index/how-agents-are-transforming-work`), already fully extracted as `blog-openai-agents-transforming-work.md`; (3) the Ramp Inspect reference (`newsletter.pragmaticengineer.com/p/why-ramp-built-inspect`), already fully extracted as `blog-pragmaticengineer-orosz-ramp-inspect.md`. None required re-fetching per MINER.md's "follow up to 5 linked pages" guidance, since both are already fully represented in the corpus.
- No contradiction found requiring an issue filing. The closest candidate — this article's ~90% non-engineering-department Codex-adoption figure (Claim 2) versus the prior article's paywalled ">95% of non-engineers" teaser (`blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md` Claim 10) — was evaluated against MINER.md §4a's bar and does not qualify as a contradiction: both numbers point the same direction, are close in magnitude, and most plausibly reflect different snapshot dates (the June article's teaser vs. this September article's chart) or slightly different cohort definitions ("non-engineers using Codex over ChatGPT" vs. department-level "Codex usage" share) rather than a disagreement about the same measured fact. Captured as a **Corroborates** cross-reference instead, with the numeric difference flagged explicitly so a future guide citation does not present both as if they were the identical statistic.
- This article is very likely the OpenAI-focused follow-up piece explicitly promised in `blog-pragmaticengineer-orosz-inside-anthropic.md`'s Extraction Notes ("a later article, we'll compare findings from Anthropic and OpenAI"), though this specific article does not itself contain a side-by-side Anthropic/OpenAI comparison in its free-preview content — such a comparison, if it exists, would likely be in the paywalled sections or a further follow-up piece. Future Prospector triage should watch for a dedicated comparison article from the same author/venue.
- Confidence is set to `emerging` overall: the visible, substantiated portion of the article (Codex adoption mechanics, the death-of-the-IDE/PR-rethinking narrative, and the full agentic-software-factory pipeline — Claims 1-15) rests on seven named, on-the-record, senior engineers and leaders at a single frontier lab, comparable in authority to this same author's Anthropic and June three-company dispatches already in the corpus. It is not rated `settled` because: (a) it is first-hand reporting from named sources at one company describing that company's own practices, not independently audited or cross-validated by a third party beyond the reporter's own credibility; (b) several claims (7, 8, 15) are the reporter's own synthesis or characterization rather than direct quotes; (c) more than half of the article's announced content (sections 4-7, including the article's own promised "how the job is changing" section) is entirely paywalled and unavailable for this extraction. Individual claims are rated at the appropriate level within the note; most are `emerging` (named, on-record, but single-company/single-source), with a few `anecdotal` where the claim is reporter synthesis or an explicitly-stated future goal rather than current, demonstrated fact.
