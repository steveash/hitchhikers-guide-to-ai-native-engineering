---
source_url: https://newsletter.pragmaticengineer.com/p/inside-anthropic
source_type: blog-post
title: "How building software is changing at Anthropic"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-07-28
date_extracted: 2026-07-29
last_checked: 2026-07-29
status: current
confidence_overall: emerging
issue: "#2296"
---

# How building software is changing at Anthropic

> First-hand, on-site dispatch from Gergely Orosz's visit to Anthropic's San Francisco office, quoting four named engineers (Katelyn Lesse, Jarred Sumner, Thariq Shihipar, David Hershey) on the six-month build of Claude Managed Agents, the process/PRD story behind it, and a cluster of day-to-day engineering-practice changes (verification-heavy time split, AI code review and security scanning, automated OSS maintenance, system-prompt shrinkage, no-token-budget culture) — largely corroborating and adding organizational narrative to claims the corpus already has in more technical/quantitative form, with the article's "Team-level changes" section (design cadence, project counts, two-engineer team caps) cut off by paywall.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter, Substack, paid tier; published July 28, 2026). The free preview covers roughly the first three of four announced sections in full (Claude Managed Agents case study, the Bun Rust rewrite, changing engineering practices) before the paywall cuts in one paragraph into section 4 ("Team-level changes"). The article states explicitly it is the first of a two-part series ("In this article and in an upcoming follow-up, I'll share what I learned... In a later article, we'll compare findings from Anthropic and OpenAI").
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager who runs The Pragmatic Engineer, the largest paid technology newsletter on Substack, and is already a trusted, corroborated corpus author (`blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`, `blog-pragmaticengineer-bun-rust-rewrite.md`, `survey-pragmaticengineer-ai-tooling-2026.md`). This is first-hand reporting: Orosz physically visited Anthropic's San Francisco HQ and interviewed four named people on the record — Katelyn Lesse (Head of Engineering, Claude Platform), Jarred Sumner (creator of Bun, now at Anthropic working on Bun and Claude Code), Thariq Shihipar (Claude Code engineering and education), and David Hershey (Applied AI, works with customers including Cursor, Cognition, and Perplexity — not directly quoted in the free preview). This is the same reporting trip referenced retrospectively; it is a separate, later, and more Anthropic-specific visit than the June 30, 2026 three-company piece already in the corpus.
- **Scope**: The free preview substantively covers: (1) the Claude Managed Agents case study (planning process, PRD, internal-customer-first rollout, mid-project re-architecture, six-month timeline); (2) the Bun Zig-to-Rust rewrite (framed here primarily through Jarred Sumner's own words on trust, code review, security scanning, fanning-out-work, and Bun's OSS maintenance automation — distinct emphasis from the metrics-heavy primary source already in the corpus); (3) "Changing engineering practices" (AI-lab-specific culture: parallel agents, no token budgets, fluid prototyping; verification-vs-implementation time split; AI code review/testing; system-prompt shrinkage; HTML-over-Markdown). It does NOT substantively cover section 4, "Team-level changes" — only a one-paragraph teaser list is visible before the paywall (design cadence, project counts per team, a stated maximum of two engineers per project, and a "still the same" list). Also does not cover the article's own later teasers ("Changing the 'standout' software engineer archetype," "Will AI replace software engineering?") beyond their one-line headline framings, which appear only in the top-of-article summary list, not as expanded sections in the free content.

## Extracted Claims

### Claim 1: Claude Managed Agents — the Claude Platform team's most complex project of the past year — took about six months from idea to its April launch, and required "typical pre-AI"-style upfront architecture planning rather than jumping straight to prototyping

- **Evidence**: First-person account from Katelyn Lesse, Head of Engineering for Claude Platform, describing why this specific project needed more planning than others her team ships.
- **Confidence**: emerging (single named, senior, on-the-record source; consistent with an independent report of the same project from an earlier Orosz article — see Cross-References)
- **Quote**: "The Claude Platform team's most complex project in the past year was building Claude Managed Agents, a pre-built harness for production agents that runs in the cloud on infrastructure managed by Anthropic, or on your team's own infrastructure, with any sandbox you choose. The project took around six months from idea until launch in April."
- **Quote** (planning): "There are products you can jump straight to prototyping, but then there are ones where you need to start by architecting it properly. For example, if we build a TypeScript CLI – which is pretty trivial for what needs to be built – we could go straight to prototyping. But with Claude Managed Agents, we needed to first figure out what we are doing. [...] Our planning process looked more like a typical pre-AI planning process."
- **Our assessment**: This is a useful counterweight to any guide narrative that AI-native planning is uniformly "just-in-time" or lighter-weight — Lesse's own framing is explicitly conditional: trivial/prototypable projects go straight to building, but complex infrastructure projects still warrant upfront architecture work resembling pre-AI process. This nuances (does not contradict) `blog-anthropic-ai-native-engineering-org.md` Claim 3's "JIT planning" framing from Fiona Fung — both sources are from Anthropic, both post-date widespread agentic coding adoption, and both describe planning intensity as scaling with project complexity/coordination needs, not disappearing outright. Worth flagging in the guide as two data points on the same axis (trivial/fast-moving work → JIT; complex/cross-team infrastructure → still close to traditional upfront planning) rather than as competing claims.

### Claim 2: Managed Agents still used a traditional PRD, written as a Google Doc, specifically because coordinating a large number of interested parties (a Product Manager, a Tech Lead, other business teams, other cloud providers, and an internal sandboxing team) required a persistent, shared artifact

- **Evidence**: First-person account of the project's kickoff process and why the PRD format was retained.
- **Confidence**: emerging (specific, named process detail from a senior engineering leader)
- **Quote**: "In the end, it was the Product Manager and the Tech Lead on our API Agents team who decided to pull the trigger and kick off this project. We'd get in a room, go through it, and get aligned. But it wasn't just us: we'd have to align with teams around the business, other cloud providers, and other engineering teams. For example, we have a sandboxing team inside of the Platform org: and so this team was consulted on the design of Managed Agents, given this product would spawn a lot of sandboxes. [...] Just like before, we had a PRD, it was a Google Doc. We used a Google Doc because we needed to coordinate all interested people. This has not gone away."
- **Our assessment**: The explicit rationale — "we needed to coordinate all interested people" — isolates *why* PRDs persist in an AI-native org even as other planning rituals compress: the artifact's job is cross-team human coordination, not specifying implementation detail to be typed out by an engineer. This is a sharper, more specific claim than a generic "PRDs are still useful" statement, and it should be read alongside Fung's JIT-planning claim as identifying the boundary condition where formal planning docs remain load-bearing: multi-team, multi-stakeholder infrastructure work, not single-team feature work.

### Claim 3: Katelyn Lesse estimates that a project of Managed Agents' complexity would have taken roughly two years pre-AI, versus the six months it actually took

- **Evidence**: First-person estimate from the project's engineering lead, offered as a direct before/after comparison.
- **Confidence**: anecdotal (single practitioner's retrospective estimate, not a measured or controlled comparison — there is no actual pre-AI version of this exact project to compare against)
- **Quote**: "Katelyn emphasized that pre-AI, a project like this would have probably been in the realm of two years. Managed Agents is one of the biggest projects the Claude Platform team has built, and more complex than it looks: for example, adding support for running agents on AWS, GCP and Azure."
- **Our assessment**: A ~4x compression estimate (24 months to 6 months) for a large, multi-cloud infrastructure project is a specific, quotable calibration point, but should be presented in the guide as a single practitioner's retrospective judgment rather than a measured benchmark — there is no counterfactual project to check it against. It is directionally consistent with, but a different order of magnitude than, the Bun rewrite's ~30x compression (a year to 11 days) documented elsewhere in this same article and in the corpus's existing Bun sources — a useful illustration that AI-driven speedups vary enormously by project type (a well-tested, single-owner mechanical port compresses far more than a novel, multi-stakeholder infrastructure build with real architectural uncertainty).

### Claim 4: Internal cross-team collaboration on Managed Agents became more fluid than pre-AI norms — teams exchanged working components and stub services to iterate on interfaces together, rather than exchanging fully-specified requirements documents in sequence

- **Evidence**: First-person account contrasting the pre-AI and current collaboration pattern between the Platform team and the Claude Code team during the internal "spike" (see Claim 5).
- **Confidence**: emerging (specific, named process comparison from a senior engineering leader)
- **Quote**: "Pre-AI, we might have hit the Claude Code team up with a bunch of big requirements documents, and they would have then hit us back with another set of documents. Now it was much easier: someone on our team built a few components, took it over to the Claude Code team, and they started to hack around it. We could figure out how this component plugs into this part of their product, and the other way around. It was just a faster and easier process, getting this first internal version of the product up and running." / "Back in the day, you'd have to come with a fully spec'd interface to use. Now, we could do it a lot more fluidly: we could stand up a stub service that shadowed traffic to start with, and iron out the interfaces with the Claude Code team as we went."
- **Our assessment**: This describes a shift in the *medium* of cross-team coordination — from documents-as-interface-contracts to working code (stub services, shadowed traffic) as the interface-negotiation mechanism. It is a concrete, cross-team-scoped complement to Fung's `blog-anthropic-ai-native-engineering-org.md` Claim 3 (JIT planning: "discussions in PRs or prototypes" replacing design docs) — that claim describes a single team's planning ritual; this claim describes the analogous shift specifically for *interface negotiation between two teams*, with a named mechanism (stub service + shadowed traffic) not present in the Fung source.

### Claim 5: Managed Agents was re-architected mid-project — decoupling the "brain" (Claude and its harness), the "hands" (sandboxes/tools), and the "session" (event log) — based on what the team learned while building an internal spike (a Claude Code mobile backend) for the Claude Code team

- **Evidence**: First-person account naming the specific trigger (learnings from the Claude Code "spike") for a mid-project architectural change, with an accompanying figure captioned "High-level architecture of Claude Managed Agents after the re-architecture."
- **Confidence**: emerging (specific first-party account of the sequencing and cause of the re-architecture; the resulting architecture itself is independently documented in more technical depth elsewhere — see Cross-References)
- **Quote**: "The platform team ended up re-architecting Managed Agents based on learnings from the Claude Code 'spike.' Re-architecting meant decoupling the 'brain' of Claude and its harness from the 'hands' (sandboxes & tools that perform actions) and the 'session' (the log of events). Each became an interface that made few assumptions about each other."
- **Our assessment**: This adds a piece of the causal/sequencing story that Anthropic's own engineering blog post does not tell: `blog-anthropic-scaling-managed-agents.md` (Claim 2, Claim 3) explains *what* the session/harness/sandbox decoupling is and the "pets vs. cattle" motivation, but frames it as a retrospective architectural philosophy rather than dating it to a specific internal spike. This source corroborates the same three-way decoupling from an independent, external-reporter vantage point and adds the trigger: the re-architecture happened *because of* building the Claude Code mobile backend as an internal customer first, not as an upfront design decision. Treat the architecture details themselves as corroboration (already settled in the corpus via the engineering post), and the sequencing/causal story as this source's novel contribution.

### Claim 6: Two examples of hard infrastructure problems surfaced by internal dogfooding during Managed Agents' build: reliability/scalability (losing agent state entirely if the sandbox connection dropped) and credentials/access control

- **Evidence**: First-person, named list of the two hardest problems the team hit during internal dogfooding.
- **Confidence**: anecdotal (brief, unelaborated list from the project lead; no metrics or specific incident accounts given)
- **Quote**: (no direct quote; see paraphrase in Our assessment) — the article states, attributed to the section on internal dogfooding: "Reliability and scalability: these are really hard to do well for agents because if connection to the sandbox is lost, the whole agent dies and you lose state" and "Credentials and access control: also hard and problematic, especially when first building the service" as two bulleted findings following the sentence "Internal 'dogfooding' helped surface hard problems to solve."
- **Our assessment**: Both problems are already well-documented in the corpus in much greater technical depth — the credential/access-control problem is the entire subject of `blog-anthropic-scaling-managed-agents.md` Claim 7 (the vault + MCP-proxy pattern, motivated by the exact same failure mode: "any untrusted code that Claude generated was run in the same container as credentials"), and the reliability/state-loss problem is the subject of that same source's Claim 3 ("pets vs. cattle") and is illustrated concretely by `failure-decker-4hr-session-loss.md`. This claim's value is narrow but real: it is independent, first-party confirmation that these two specific problems were the ones internal dogfooding actually surfaced (as opposed to being framed only retrospectively in the engineering blog post) — i.e., dogfooding is shown here as the *discovery* mechanism, not just background context.

### Claim 7: Jarred Sumner frames the core trust problem of high-velocity AI-driven merging as "how do you merge 100+ PRs a day, and make sure the code works?" and names automated code review, security scanning, and fuzz testing as the three pillars of his answer

- **Evidence**: First-person framing from Sumner, followed immediately by the three-item list.
- **Confidence**: emerging (specific first-party framing and named practice list; the "100+ PRs a day" figure is stated as a round description of pace, not an audited count)
- **Quote**: "I think a lot about trust when you merge a lot of code. How do you merge 100+ PRs a day, and make sure the code works? At this pace, you need to trust the code without the ability to read it all yourself."
- **Our assessment**: This is a compact, quotable framing of the verification-bottleneck problem — trust, not throughput, is the binding constraint once code generation is cheap — that corroborates the corpus's existing "bottleneck shift" thesis (`blog-anthropic-ai-native-engineering-org.md` Claim 1: "Verification, code review, and security took their place"). Sumner's version is notable for naming a third pillar (fuzz testing, Claim 9 below) beyond the code-review/security pairing that dominates the rest of the corpus's coverage of this shift.

### Claim 8: Jarred Sumner states Claude's automated code review "catches bugs that would take me an hour of closely reading the code to figure out," with an explicit cost caveat

- **Evidence**: First-person, specific practitioner endorsement with a named cost caveat.
- **Confidence**: anecdotal (single practitioner's subjective assessment; no bug count or false-positive/negative rate given)
- **Quote**: "Code review: it needs to be really good and automated. I'm clearly tooting our own horn here, but I find Claude's code review to be really good. Claude's code review catches bugs that would take me an hour of closely reading the code to figure out. The caveat is that it's expensive!"
- **Our assessment**: Sumner flags his own conflict of interest explicitly ("I'm clearly tooting our own horn here") — a useful piece of epistemic honesty the guide should preserve when citing this quote, since Sumner is both an Anthropic employee and a heavy user of the product he is praising. The cost caveat ("it's expensive") is the more novel and useful half of the claim for practitioners: it is a rare acknowledgment from an enthusiastic adopter that automated code review has a real, unstated dollar cost that should factor into adoption decisions, not just a capability one.

### Claim 9: The Bun Rust rewrite's post-merge hardening included 11 runs of the Claude Security Scanner and Claude-written fuzzers targeting Bun's parsers

- **Evidence**: First-person, specific named-tool account from Sumner.
- **Confidence**: settled (specific figure, independently corroborated by a second source describing the same event — see Cross-References)
- **Quote**: "Security scanning: for this Rust rewrite we did 11 runs of the Claude Security Scanner. Fuzz testing: we've also been doing different types of fuzzing (fuzz testing), where we had Claude write a fuzzer for things like parser fuzzing."
- **Our assessment**: This is independent corroboration — not new information — of a figure already in the corpus: `blog-pragmaticengineer-bun-rust-rewrite.md`'s Concrete Artifacts section (drawn from Sumner's own bun.com post) states "11 rounds of Claude Code Security review; 24/7 coverage-guided fuzzing across all Bun parsers (~100 billion executions, ~15 PRs from bugs found)" for the same rewrite. The "11" figure matching exactly across Sumner's own written blog post and his separate verbal account to Orosz is a small but genuine confidence-raising signal — it means the number was consistent across two independent tellings months apart, not a one-off misstatement.

### Claim 10: Jarred Sumner names "fanning out work to many Claudes at the same time" as a distinct, generalizable working pattern he now applies beyond the Bun rewrite, and considers it underused

- **Evidence**: First-person description of a named personal working pattern, with an explicit claim about its general applicability and adoption rate.
- **Confidence**: anecdotal (single practitioner's self-assessment of a personal workflow; "underused" is his own subjective judgment, not a measured adoption statistic)
- **Quote**: "A new approach I'm using is fanning out a lot of the work to many Claudes at the same time. I did this with the Bun rewrite, but I use it for other work. This approach works very well for me, and I feel it's pretty underused."
- **Our assessment**: This is Sumner's own framing of parallel-agent fan-out as a reusable *practice* (something he now reaches for on other work), distinct from the corpus's existing coverage of the Bun rewrite's parallel-agent *mechanics* (the specific 64-instance, 4-worktree, implementer/reviewer/fixer harness documented in `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 6-7). The "pretty underused" self-assessment is a useful practitioner signal that fan-out-style parallel agent orchestration, despite being demonstrated at spectacular scale in the Bun case study, may not yet be common even among sophisticated AI-native practitioners.

### Claim 11: The Bun open-source project runs an automated maintenance pipeline where filed issues trigger an automatic reproduction attempt, a fix-and-PR attempt in a separate container, and PRs are auto-rejected unless they include a test that fails without the patch and passes with it

- **Evidence**: First-person, specific, multi-step description of a shipped automation pipeline for an actively maintained open-source project.
- **Confidence**: emerging (specific, named process description from the practitioner who set it up; not independently verified against the actual Bun repository's CI configuration, but specific enough to be falsifiable/replicable)
- **Quote**: "Every time someone files an issue, Claude runs to try and reproduce the issue. If it succeeds, it starts another container, which then tries to fix the issue and submit a PR. [...] The agent tasked with submitting a PR has to write a test that fails in the system version (the one without the patch) of Bun, and passes in the debug build with the patch, before it is allowed to submit a PR [...] There are other automations, like if there is no test, the PR is auto-rejected; all linters are run: Claude Code review is run, CodeRabbit's code review is run, and the agents go back and forth on the GitHub pull request [...] a lot of GitHub activity is Claude talking to Claude!"
- **Our assessment**: This is a novel, concrete, end-to-end example of "automate the boring stuff" applied to open-source maintenance specifically — distinct from the corpus's existing coverage of the Bun rewrite (a one-time migration project). The "fails without the patch, passes with the patch" gate is a specific, reusable regression-test discipline that is stricter than "add a test" — it requires demonstrating the bug existed and is fixed, not just that some test exists. The dual code-review layer (Claude Code review + CodeRabbit) running on the same PR is also a concrete example of using two independent automated reviewers rather than one, which corroborates the corpus's broader "multiple independent reviewers catch more" pattern (`blog-pragmaticengineer-bun-rust-rewrite.md` Claim 7's adversarial-reviewer design) applied here to ongoing maintenance rather than a single migration.

### Claim 12: Jarred Sumner predicts near-term auto-merge of low-risk PRs on Bun, gated by a second Claude instance with a fresh context window judging blast radius, replacing the current human "press merge" step

- **Evidence**: First-person forward-looking prediction from the practitioner running the automation pipeline described in Claim 11.
- **Confidence**: anecdotal (explicit prediction, not a shipped feature — Sumner frames it as "within a few months, I expect," not as something already running)
- **Quote**: "Today, a person presses 'merge' but within a few months, I expect: Automated reviewer LGTMs → another Claude with a fresh context window judges if it's simple and low blast-radius → if it is: auto-merge!"
- **Our assessment**: The "fresh context window" detail is the load-bearing mechanism: the auto-merge gate is not the same Claude instance that reviewed the code approving its own review, but a separate instance without exposure to the PR's back-and-forth discussion, judging only simplicity and blast radius. This is architecturally consistent with the adversarial-reviewer-isolation pattern already documented in the corpus (`blog-pragmaticengineer-bun-rust-rewrite.md` Claim 7 — reviewers receive only the diff, not the implementer's reasoning) applied one step further down the pipeline, to the merge decision itself rather than just the review.

### Claim 13: Thariq Shihipar states the Claude Code team deleted 80% of the system prompt because the model got smarter, and separately reports a personal, team-observed preference for HTML output over Markdown

- **Evidence**: First-person account from Thariq Shihipar, framed as an example of the team "revisit[ing] any assumptions you have made because it can change with a new model generation."
- **Confidence**: settled (specific figure, independently corroborated by a second on-the-record account from the same named engineer in a separate venue — see Cross-References)
- **Quote**: "The thing with agents is that you have to revisit any assumptions you have made because it can change with a new model generation. For that reason, we deleted 80% of the Claude Code system prompt recently because the model has gotten smarter." / "Using HTML is another assumption we needed to re-examine. HTML is one of those things which Claude is a lot smarter at than many of us expected. I've started preferring HTML as an output format over Markdown, and see this being used by others on the Claude Code team. HTML can convey much richer information compared to markdown, HTML documents are easier to read and share."
- **Our assessment**: The 80% figure independently matches `blog-simonwillison-cat-thariq-fireside-chat.md` Claim 2, where Thariq gave the same figure in a July 21, 2026 conference talk ("we were over-constraining Claude... removing examples was extremely helpful"). Two on-the-record statements from the same named engineer, a week apart, in two different venues (a conference Q&A and a one-on-one interview), citing the identical "80%" figure, is strong corroboration that the number is a real, stable internal figure rather than an off-the-cuff estimate. The HTML-over-Markdown preference corroborates `blog-simonwillison-html-effectiveness.md` Claim 1, which is built entirely around the same Thariq Shihipar's argument and companion page — this is now a third independent surfacing of the same practitioner's HTML claim.

### Claim 14: Anthropic engineers described a set of AI-lab-specific working norms as unusual relative to Big Tech and most startups — running 3-10 parallel AI agents as routine, no token budgets or usage tracking/leaderboards, and very high individual autonomy to prototype

- **Evidence**: Orosz's own synthesis of what he observed across his conversations at Anthropic, presented as a named list of "AI lab-specific practices."
- **Confidence**: anecdotal (reporter's synthesis of a site visit and conversations with a handful of named engineers at one company; not a survey or measured comparison against other companies)
- **Quote**: "Everyone runs multiple AI agents all the time. Running 3-10 parallel agents is a given. Folks I talked with had their agents running in the background or cloud." / "No token budget, usage not tracked. One major difference between AI labs and everyone else is that there really is no token limit or token leaderboards that promote tokenmaxxing; people already use agents all the time." / "Very high autonomy. Work is becoming more structured inside AI labs, but there's still massive autonomy compared to Big Tech and most startups. When everyone has unlimited tokens, it's pretty easy to prototype any idea."
- **Our assessment**: This is a useful explicit naming of a resource-constraint difference that likely explains why some Anthropic-sourced practices in the corpus (e.g., Sumner's 64-parallel-agent Bun rewrite, or Fung's near-100%-Claude-assisted-commit rate in `blog-anthropic-ai-native-engineering-org.md` Claim 11) may not transfer directly to token-budget-constrained organizations. The guide should flag this explicitly whenever citing Anthropic-internal practices as generalizable benchmarks: Anthropic engineers operate without the token-cost friction that most adopting organizations will still face, which is itself a confound on how directly their reported workflow patterns generalize.

### Claim 15: The article's paywalled "Team-level changes" section is teased as covering more ongoing/less upfront design, more concurrent projects per team, and a stated maximum of two engineers per project — with "still the same" items listed as two-pizza teams, the continued importance of planning, PRD relevance for complex projects, context-switching difficulty, and a roughly unchanged coding-vs-testing time ratio

- **Evidence**: Stated only in the article's top-of-post teaser/summary list; the corresponding body section ("4. Team-level changes") is cut off by the paywall one sentence after its heading, before any elaboration.
- **Confidence**: anecdotal (headline teaser only — no supporting detail, examples, or named sources for any of these specific sub-claims are visible in the readable portion)
- **Quote**: "Team-level changes. Design is more ongoing and less upfront, teams work on more projects, a maximum of two engineers per project, and more." / "Still the same: two-pizza teams, planning is important, PRDs are relevant in complex projects, context switching is a challenge, the ratio of time spent on coding vs testing not changing that much."
- **Our assessment**: Treat this as a headline pointer, not evidence — we have one summary sentence per sub-claim and zero elaboration, examples, or attribution to a named speaker. The "two-pizza teams... still the same" framing is directionally consistent with `blog-anthropic-ai-native-engineering-org.md`'s general picture of an org that preserves some traditional structures (Claim 10's "keep the team flat as possible" principle) while changing others, but this article gives no detail on *how* Anthropic's two-pizza teams operate differently (or don't) post-AI-adoption. Do not cite the "maximum of two engineers per project" or "more ongoing design" claims as substantiated findings — flag for a follow-up extraction if the paid content becomes accessible, consistent with how `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md`'s Extraction Notes handled the same publication's paywall pattern.

## Concrete Artifacts

### Interviewees (verbatim, from the article's introduction)

```
Source: https://newsletter.pragmaticengineer.com/p/inside-anthropic

"Thanks to Anthropic for showing me inside their lab in San Francisco. I talked
with four people:

Katelyn Lesse, Head of Engineering for Claude Platform, whose organization owns
the infrastructure that Claude runs on

Jarred Sumner, creator of Bun, now at Anthropic on Bun and Claude Code

Thariq Shihipar, who works across Claude Code engineering and education

David Hershey, at Anthropic's Applied AI organization in a role resembling a
sales engineer, working with customers like Cursor, Cognition, and Perplexity"
```

David Hershey is named but not directly quoted anywhere in the free-preview portion of this article.

### Article structure (from the top-of-post "we cover" summary, all visible pre-paywall)

```
Source: https://newsletter.pragmaticengineer.com/p/inside-anthropic

1. Complex & long: Claude Managed Agents.
   [SUBSTANTIVELY COVERED IN FREE PREVIEW — see Claims 1-6]
2. Twelve-month project done in 11 days: Bun rewrite to Rust.
   [SUBSTANTIVELY COVERED IN FREE PREVIEW — see Claims 7-13, mostly corroborating
   existing corpus coverage of the same rewrite]
3. Changing engineering practices.
   [SUBSTANTIVELY COVERED IN FREE PREVIEW — see Claims 7-14]
4. Team-level changes.
   [PAYWALLED — teaser only, see Claim 15]

Additional headline-only teasers naming two further themes, with zero
corresponding body content visible before the article ends:
  "Still the same: two-pizza teams, planning is important, PRDs are relevant
  in complex projects, context switching is a challenge, the ratio of time
  spent on coding vs testing not changing that much."
  "Changing the 'standout' software engineer archetype? Deep understanding,
  including of a layer below what you work on, is valuable, along with the
  ability to coordinate work."
  "Will AI replace software engineering? The more hands-on software engineers
  get with AI at the lab, the less they fear their jobs are going away."

Paywall cutoff point (verbatim, end of free content, immediately after the
"4. Team-level changes" section heading):
"At Anthropic, there are also changes in how engineering teams operate,
compared to pre-AI.

This post is for paid subscribers
Subscribe
Already a paid subscriber? Sign in"
```

### Claude Managed Agents: process timeline (extracted from article body)

```
Source: https://newsletter.pragmaticengineer.com/p/inside-anthropic
Speaker: Katelyn Lesse, Head of Engineering, Claude Platform

1. Motivation: customers hacking together their own "harness infrastructure"
   after starting with a self-hosted-sandbox API model
2. Planning: "typical pre-AI" upfront architecture planning (not a quick
   prototype); some upfront prototyping/spiking, but mainly for requirements
   understanding, not implementation
3. Kickoff: PM + Tech Lead decide to start the project; a PRD is written as a
   Google Doc, explicitly to coordinate cross-org stakeholders (other business
   teams, other cloud providers, an internal sandboxing team)
4. Internal-customer-first build: team builds a "spike" — the backend for
   Claude Code on the web/mobile — as a stress test of the architecture,
   working fluidly with the Claude Code team via stub services and shadowed
   traffic rather than fully-spec'd interface documents
5. Re-architecture: learnings from the spike trigger a mid-project redesign,
   decoupling "brain" (Claude + harness) / "hands" (sandboxes & tools) /
   "session" (event log) into separate interfaces
6. Hardening: internal dogfooding surfaces two hard problems — reliability/
   state loss on dropped sandbox connections, and credentials/access control
7. Launch: shipped in April 2026, ~6 months after project start; Lesse
   estimates a comparable pre-AI project would have taken ~2 years
8. Scope note: supports running agents on AWS, GCP, and Azure
```

### Bun OSS maintenance automation pipeline (extracted from article body)

```
Source: https://newsletter.pragmaticengineer.com/p/inside-anthropic
Speaker: Jarred Sumner, creator of Bun

1. Issue filed by a user
2. Claude attempts to reproduce the issue
3. If reproduction succeeds: a separate container starts, and Claude attempts
   a fix + PR submission
4. Gate: the PR-submitting agent MUST write a test that (a) fails on the
   unpatched/system build and (b) passes on the debug build with the patch —
   required before the PR can be submitted
5. Additional gates: PRs with no test are auto-rejected; all linters run;
   Claude Code review runs; CodeRabbit's code review runs; agents iterate
   back and forth on the PR thread ("a lot of GitHub activity is Claude
   talking to Claude")
6. Current state: merge is still a manual, human-pressed action
7. Predicted near-future state (Sumner's own words): "Automated reviewer
   LGTMs -> another Claude with a fresh context window judges if it's simple
   and low blast-radius -> if it is: auto-merge!"
```

## Cross-References

- **Corroborates**: `blog-pragmaticengineer-orosz-visiting-openai-anthropic-cursor.md` Claim 3 — that source's June 30, 2026 dispatch already reported "Claude Managed Agents is a large, complex project which her team built over a six-month period," attributed to the same Katelyn Lesse. This article is a return visit that substantially deepens that single sentence into the full process narrative (planning, PRD, internal-customer-first rollout, re-architecture trigger) in Claims 1-6 above.
- **Corroborates**: `blog-anthropic-scaling-managed-agents.md` Claim 2 (three-way session/harness/sandbox virtualization) and Claim 3 (the "pets vs. cattle" coupled-design failure mode) — this article's Claim 5 (re-architecture into brain/hands/session) and Claim 6 (dogfooding surfacing reliability/state-loss and credential problems) independently confirm the same architecture and the same two motivating failure modes from a second, external-reporter source, with the added detail that the re-architecture was triggered specifically by learnings from the Claude Code mobile-backend spike — a sequencing detail the engineering post does not state.
- **Corroborates**: `blog-anthropic-scaling-managed-agents.md` Claim 7 (credential vault + proxy pattern, motivated by "a prompt injection only had to convince Claude to read its own environment") — this article's Claim 6 names "credentials and access control" as one of the two hardest problems dogfooding surfaced, consistent with but less detailed than that source's technical account.
- **Corroborates**: `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 5-7 (the Bun rewrite's $165K cost, 64-instance/11-day/4-worktree scale, and the implementer/adversarial-reviewer/fixer harness) — this article's framing of the same rewrite (Claims 7, 9-10 above) adds new first-person color (the trust/merge-volume framing, the 15%/85% implementation-vs-verification time split, the "fanning out" naming) without contradicting any of the quantitative figures already in the corpus.
- **Corroborates**: `blog-pragmaticengineer-bun-rust-rewrite.md` Concrete Artifacts ("11 rounds of Claude Code Security review; 24/7 coverage-guided fuzzing... ~100 billion executions") — this article's Claim 9 independently reports the same "11" security-scanner-run figure directly from Sumner in a separate, later interview, strengthening confidence in that number via a second independent telling.
- **Corroborates**: `blog-simonwillison-cat-thariq-fireside-chat.md` Claim 2 (Claude Code system prompt reduced 80%, driven by removing examples as models improved) — this article's Claim 13 has Thariq Shihipar independently stating the same "80%" figure to a different interviewer (Orosz) about a week after the fireside chat (July 21, 2026) this article was published (July 28, 2026), corroborating the figure's stability.
- **Corroborates**: `blog-simonwillison-html-effectiveness.md` Claim 1 (Thariq Shihipar's HTML-over-Markdown argument) — this article's Claim 13 is a third independent surfacing of the same named engineer's HTML preference claim.
- **Extends**: `blog-anthropic-ai-native-engineering-org.md` Claim 1 ("Verification, code review, and security took their place" as the bottleneck) — this article's Claim 7 (Sumner's "how do you merge 100+ PRs a day" trust framing) and the 15%/85% implementation-vs-verification split in Claim 7's context corroborate the bottleneck-shift thesis from a second Anthropic team (Bun/Claude Code infrastructure, not the Claude Code product team Fung describes), adding a third named pillar (fuzz testing) alongside code review and security scanning.
- **Extends**: `blog-anthropic-ai-native-engineering-org.md` Claim 3 ("JIT planning... away from design docs toward discussions in PRs or prototypes") — this article's Claim 1 and Claim 2 provide an explicit boundary condition Fung's account does not state as clearly: Lesse frames the choice between JIT-style prototyping and traditional upfront planning as conditional on project complexity and cross-team coordination needs, not as a uniform organizational shift. Complex, multi-stakeholder infrastructure work (Managed Agents) still gets "typical pre-AI planning" and a PRD; simple, single-team work (a "trivial" TypeScript CLI, Lesse's own example) goes straight to prototyping. This should be read as a refinement/conditioning variable on Fung's claim, not a contradiction — both sources are internally consistent with "plan proportionally to actual coordination need," they just illustrate opposite ends of that spectrum.
- **Novel**:
  - **The specific causal sequence for Managed Agents' mid-project re-architecture** (triggered by the internal Claude Code mobile-backend spike, not planned upfront) — no prior corpus source dates or explains *why* the brain/hands/session decoupling happened when it did.
  - **The PRD-as-coordination-artifact rationale** ("we needed to coordinate all interested people") as an explicit, named reason formal planning docs persist for specific project types in an AI-native org — sharper than a generic "PRDs are still useful" claim.
  - **Bun's automated OSS-maintenance pipeline** (issue → auto-reproduction → auto-fix-attempt → mandatory fail-then-pass regression test → dual automated code review → predicted auto-merge) — an end-to-end example of automation applied to ongoing project maintenance, distinct from the corpus's existing one-time-migration-focused Bun coverage.
  - **The 15%/85% implementation-vs-verification time split**, stated as Sumner's own rough accounting of the Rust rewrite specifically in terms of *time*, complementing the corpus's existing *token*- and *role*-based accounting of the same project.
  - **Explicit naming of AI-lab-specific resource norms** (3-10 parallel agents as routine, no token budgets or usage leaderboards) as a distinct organizational condition that likely does not transfer to token-budget-constrained organizations — no prior corpus source names this as an explicit confound on generalizing Anthropic-internal practices.

## Guide Impact

- **Chapter 01/02 (Daily Workflows / Planning)**: Add Claims 1-2 as a conditioning variable on the guide's existing JIT-planning material (from `blog-anthropic-ai-native-engineering-org.md`): planning intensity should scale with project complexity and the number of stakeholders who must coordinate, not disappear uniformly. Cite Lesse's own binary example (trivial CLI → prototype immediately; complex multi-cloud infrastructure → traditional upfront planning + PRD) as the practical heuristic, and her explicit rationale that PRDs persist specifically as a coordination artifact for multi-team alignment, not as a spec for an engineer to type from.
- **Chapter 02 (Harness Engineering — Managed Agent Architecture)**: If the guide cites `blog-anthropic-scaling-managed-agents.md`'s brain/hands/session architecture, add this article's Claim 5 as the sequencing context: the decoupling was not an upfront design choice but emerged from learnings during an internal dogfooding spike (the Claude Code mobile backend). This is a concrete illustration of "build for an internal customer first, let real usage reveal the right architecture" as a development strategy for infrastructure-heavy agent platforms.
- **Chapter 03 (Safety and Verification)**: Add Claim 7 (Sumner's "100+ PRs a day" trust framing) and Claim 9 (11 security-scanner runs + Claude-written fuzzers) as a third named example — alongside Shopify and Fung/Anthropic-Claude-Code-team sources already in the corpus — of a team responding to the verification bottleneck with a specific, named tool stack (code review + security scanning + fuzz testing), not just "we use AI for review" in the abstract.
- **Chapter 04/05 (Team Adoption — Open-Source Maintenance)**: Add the Bun OSS automation pipeline (Claim 11) as a concrete worked example for maintainers of active open-source projects: issue reproduction, gated fix-and-PR submission requiring a fail-then-pass regression test, dual automated review, with human-pressed merge as the only remaining manual gate. This is new to the corpus as an end-to-end maintenance (not migration) automation case study.
- **Chapter 02 (Harness Engineering — System Prompts)**: Add Claim 13 as a second independent confirmation (a week apart, different interviewer) of the 80% Claude Code system-prompt reduction already documented via `blog-simonwillison-cat-thariq-fireside-chat.md`. Two consistent tellings from the same named engineer strengthens this from "reported once" to "a stable, repeatable internal figure."
- **Chapter 05/06 (Team Adoption — Generalizability Caveats)**: Add Claim 14 (3-10 parallel agents as routine, no token budgets) as an explicit caveat wherever the guide cites Anthropic-internal engineering practices (Fung's near-100% Claude-assisted commit rate, Sumner's 64-parallel-agent rewrite, etc.) as adoption benchmarks — Anthropic engineers operate without the token-cost friction most adopting organizations still face, which likely inflates how aggressively they can parallelize relative to a cost-conscious team.

## Extraction Notes

- **Paywall boundary verified via raw HTML, not WebFetch summarization**: An initial WebFetch pass returned a shortened, AI-paraphrased summary rather than verbatim text (consistent with the pattern already noted in `blog-simonwillison-cat-thariq-fireside-chat.md` and `blog-pragmaticengineer-bun-rust-rewrite.md`'s Extraction Notes). The full free-preview text was instead fetched via `curl` with a browser user-agent (HTTP 200), and the `available-content` div was isolated and stripped of markup to produce a flat-text extraction, which is what all quotes above were copied from character-for-character. The paywall boundary (`"This post is for paid subscribers"`) was located precisely in this flat text, immediately after one sentence of section 4 ("Team-level changes"), confirming exactly how much of the article is genuinely free content versus teaser-only.
- **No sub-pages followed**: The article's only substantive outbound content is inline (no linked sub-pages requiring separate extraction per MINER.md's "follow up to 5 linked pages" guidance); it does link to `bun.com/blog/bun-in-rust` (already extracted in full in `blog-pragmaticengineer-bun-rust-rewrite.md`) and to a companion "What can we learn from Bun's rapid Rust rewrite with AI?" Pulse piece (already extracted in the same note), so neither was re-fetched here.
- **This is explicitly the first of a two-part (or more) series**: the article states directly that a follow-up piece will cover OpenAI, and a later piece will compare Anthropic and OpenAI directly. Future Prospector triage should expect at least one, possibly two, follow-up articles from the same author/venue covering the same reporting trip; when those appear, this note's "Team-level changes" gap (Claim 15) should be revisited, since Orosz's own two-part structure suggests deeper team-structure content may appear there rather than behind this specific article's paywall.
- **No contradiction found requiring an issue filing**: The closest candidate — Lesse's "typical pre-AI planning" framing for Managed Agents versus Fung's "JIT planning" framing for the Claude Code team — was evaluated against MINER.md §4a's bar and does not qualify: both sources describe planning intensity as conditional on project type/complexity, and neither claims its own norm is universal within Anthropic. This is captured as an "Extends" cross-reference (a conditioning variable) rather than a contradiction.
- Confidence is set to `emerging` overall: the article contains multiple named, on-the-record, first-hand accounts from senior Anthropic engineers (comparable in authority to `blog-anthropic-ai-native-engineering-org.md`), but a meaningful fraction of its claims are either brief/unelaborated (Claim 6), explicitly self-interested practitioner endorsements (Claim 8), forward-looking predictions rather than shipped facts (Claim 12), or reporter synthesis rather than direct quotes (Claim 14) — and the article's own most structurally-oriented section (team-level changes) is entirely paywalled beyond a teaser. Individual claims are rated at the appropriate level within the note; several (Claims 9, 13) are rated `settled` specifically because they are independently corroborated by a second source, not on this article's authority alone.
