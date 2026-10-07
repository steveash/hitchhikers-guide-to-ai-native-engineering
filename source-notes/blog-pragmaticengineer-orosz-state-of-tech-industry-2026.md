---
source_url: https://newsletter.pragmaticengineer.com/p/the-state-of-the-tech-industry-in
source_type: blog-post
title: "The state of the tech industry in 2026"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-10-06
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: emerging
issue: "#3953"
---

# The state of the tech industry in 2026

> Orosz's LDX3 keynote summary is a one-stop snapshot of what changed (agents write the code, parallel sessions, fading IDE, custom harnesses), what broke (code review, quality, capacity) and what stayed the same (teams, planning, tests) as of October 2026 — mostly synthesizing and linking his earlier single-topic pieces, plus new GitHub/Linear/Factory AI data.

## Source Context

- **Type**: blog-post (written summary of a 29-minute keynote at LDX3 New York to 2,000+ engineering leaders; video free, slides paid)
- **Author credibility**: Gergely Orosz, ex-Uber engineering manager and author of The Pragmatic Engineer; for this piece he visited OpenAI and Anthropic, spoke to Ramp, Uber and others, and obtained unpublished data from GitHub, Factory AI and Linear. Most claims are his observations from interviews, not measurements he ran.
- **Scope**: Trends in "AI labs, VC-funded startups and Big Tech" (his words). Skews toward the most AI-forward companies; he does not cover regulated or legacy enterprises. The full-text body was readable; only slides and the "bonus content" are paywalled. Charts (GitHub, Linear, Factory AI, Uber) are images, so exact values are not extractable beyond what the text states.

## Extracted Claims

### Claim 1: Practically nobody writes code by hand anymore among the most productive engineers; this solidified after models improved at the end of 2025
- **Evidence**: Anecdotal/observational — Orosz's own interviews ("Nearly all of the most productive software engineers I've met"); the "death of coding by hand" debate sparked by the Rails creator.
- **Confidence**: emerging
- **Quote**: "Nearly all of the most productive software engineers I’ve met – who were hand-writing code a year ago – no longer write the code by hand and also run several parallel agents."
- **Our assessment**: Directionally well supported by other notes in the corpus, but the sample is the AI-forward tail. A reader commenter asks exactly this (new products vs. maintenance, long-term quality, incentives), and Orosz does not answer in the article body.

### Claim 2: Running 5-10 parallel agent sessions per engineer is increasingly common, with cognitive overhead as the limit
- **Evidence**: Three named practitioners: Boris Cherny (Claude Code), Peter Mattis (Cockroach Labs), Dima Zaytsev (Linear).
- **Confidence**: emerging
- **Quote**: "I find my cognitive overhead is about 5-10 agent sessions concurrently."
- **Our assessment**: Consistent number across three independent practitioners. Zaytsev's "5-10 (literally) worktrees locally that I rotate between" gives a concrete mechanism (git worktrees + round-robin). Human attention, not tooling, is the stated ceiling.

### Claim 3: Agent-authored PRs grew ninefold in eight months and exceeded human-authored PRs on GitHub in August 2026
- **Evidence**: Unpublished GitHub data (chart image); Orosz's extrapolation.
- **Confidence**: emerging (single vendor-provided chart, not independently verifiable)
- **Quote**: "there were more agent-authored PRs in August 2026 on GitHub than human-authored ones!"
- **Our assessment**: Strong headline but definitions of "agent-authored" are not given. Note an internal date slip in the source: it says "as of today (October 2025)" in the PR-volume estimate (75M+/month vs 25M in Dec 2023), which should be 2026; treat that estimate ("probably") with caution.

### Claim 4: Agents now create more issues than humans (Linear), and skills usage is mainstream (Factory AI)
- **Evidence**: Linear chart: more agent-created than human-created issues since July. Factory AI: 83% of users use skills, up 2.5x from February.
- **Confidence**: emerging (vendor data)
- **Quote**: "83% of Factory AI users use skills, up 2.5x from February."
- **Our assessment**: The 83% is a statement in a chart caption; Factory AI users are a self-selected, agent-heavy population. Also states companies are "building their own agent skills repositories for all staff to create, share, and evaluate."

### Claim 5: The IDE is fading — new agentic products dropped the editor, and the IDE should evolve into a monitoring and validation interface
- **Evidence**: Dated product timeline (Antigravity 2.0 May 2026, Codex Feb 2026, Cursor relaunch April 2026, JetBrains Air); Yegge's 8-level AI-usage ladder; Kent Beck quote.
- **Confidence**: emerging
- **Quote**: "Antigravity 1.0 was the last IDE released, based on a VS Code fork."
- **Our assessment**: The product timeline is checkable and useful. Orosz's own hedge ("I wonder if what is really happening is the IDE evolving into something different") is the more defensible reading than "IDE is dead". His addition that IDEs must become "a validation and verification interface" is an opinion, not data.

### Claim 6: Most mid-sized-and-larger companies have built their own agent harness/platform
- **Evidence**: A list of ~20 named internal harnesses; Ramp Inspect case study.
- **Confidence**: emerging
- **Quote**: "most mid-sized-and-above companies have built their own agent harnesses, at this point!"
- **Our assessment**: The names list is concrete and useful as a census. "Most" is asserted from a survivorship-biased set of companies Orosz covers.

### Claim 7: Development work increasingly starts in Slack and runs in cloud agents, and "agentic software factories" are being built widely
- **Evidence**: Examples: "@Codex, implement this" (OpenAI), "@Claude build this" (Anthropic), "@Linear work on this"; reader feedback to the OpenAI factory deepdive.
- **Confidence**: anecdotal
- **Quote**: "Coding agents work really well when deeply integrated into a company’s stack, when the Slack agent kicks off a coding agent that runs in the cloud."
- **Our assessment**: Pattern (chat trigger → cloud sandbox agent → PR) is consistent with the Ramp and OpenAI notes.

### Claim 8: Migrations that took years now take weeks or months
- **Evidence**: Anthropic Bun Zig→Rust in 11 days (est. 1.5 engineering-years); OpenAI Python→Rust API ~5 months; Airbnb 3,500 test files in 6 weeks; Asana 4,000 test files in 2 weeks; Uber 600,000 JUnit 4 tests / 15M LOC in 4 months.
- **Confidence**: emerging (company-reported, estimates of counterfactual are the companies' own)
- **Quote**: "We’re seeing many migrations that would have taken years to complete, now taking mere weeks or months:"
- **Our assessment**: Counterfactual durations are estimates. The Bun case is detailed elsewhere including 19 regressions and a $165K token bill, which tempers the headline. The prediction "no excuse to delay any longer" for refactors is Orosz's inference.

### Claim 9: AI cost is a major engineering concern; model routing and open models cut per-token cost 50%+ (Uber)
- **Evidence**: Uber chart: token usage up but costs flat since May; Bloomberg corroboration; Databricks chart of cost levers.
- **Confidence**: emerging
- **Quote**: "lower-cost models and smart routing account for the majority of cost savings at most companies."
- **Our assessment**: Actionable and specific: "If you’re only doing two things, consider those techniques." (model routing and lower-cost models).

### Claim 10: Projects are staffed by one or two engineers, yet team structure still matters (two-pizza teams at Anthropic)
- **Evidence**: Katelyn Lesse (Claude Platform) quoted twice.
- **Confidence**: anecdotal
- **Quote**: "On an individual project, you often cannot have more than two people working on it."
- **Our assessment**: Not a contradiction with "teams are still important" — the unit is project-per-1-2-engineers inside a team that still owns software and on-call ("We still have two-pizza teams."). Worth presenting as a conditioning pair in the guide.

### Claim 11: Human code review has become "theater"; AI-only review is rising
- **Evidence**: An anonymous mid-sized-startup engineer; Orosz's observation that audience reacted strongly; Linear chart of AI-only reviews rising; GitHub charts of exponential growth in lines of code and commits.
- **Confidence**: emerging
- **Quote**: "Everyone is playing the theater of doing reviews"
- **Our assessment**: One anonymous source plus Orosz's generalization ("at most companies"). The same author's code-review-approaches note gives more nuanced responses (risk tiering, plan review). Treat "reviews are dead" as a symptom report, not a recommendation.

### Claim 12: Quality and reliability are declining, and personal focus/productivity suffer from context switching
- **Evidence**: Mario Zechner quote; Dima Zaytsev on expectation creep; link to "Are AI agents actually slowing us down?".
- **Confidence**: anecdotal
- **Quote**: "There’s lots of context switching: there’s always another agent that waits on your response."
- **Our assessment**: Zaytsev's point that "the expectation has become that everyone works on parallel things" is a notable second-order effect: productivity gains get absorbed as raised workload. Zechner's "98% uptime" is opinion; no measurement offered.

### Claim 13: Compute capacity (GPUs, memory, now CPUs) is a real constraint
- **Evidence**: Orosz's earlier reporting, rumors of regions not accepting tenants, prepaying for capacity coming online in December.
- **Confidence**: anecdotal
- **Quote**: "The best time to secure more CPU capacity is most certainly right now."
- **Our assessment**: Peripheral to the guide's engineering-practice scope; relevant only to agent-fleet planning (cloud agents are CPU-hungry).

### Claim 14: Tests and validation remain essential; effort goes into validating agent output
- **Evidence**: Jarred Sumner (Bun/Anthropic); Orosz's company conversations.
- **Confidence**: emerging
- **Quote**: "You need to have a way to trust your code, and tests are probably the best way to."
- **Our assessment**: Sumner says AI writes the tests too and test-writing time is roughly equal to code time as pre-AI. Matches the inside-anthropic and bun-rust notes.

### Claim 15: Non-engineers are not shipping production code; engineers still decide what is released
- **Evidence**: Orosz asked AI labs, startups and other companies; found none.
- **Confidence**: anecdotal (absence-of-evidence from a limited sample; he did not say how many companies)
- **Quote**: "I can report that I did not find any single company where PMs/designers/non-technical people ship to production!"
- **Our assessment**: Useful boundary condition; the finding is a negative from an unspecified sample. Prototyping and agent-made bugfixes routed to developer review are the observed pattern.

### Claim 16: Classic practices (tracer bullets, unit tests, upfront architecture, design patterns) work well with agents, and complex projects still get lengthy planning
- **Evidence**: Matt Pocock's tracer-bullet finding; Lesse on Managed Agents planning (docs back two years).
- **Confidence**: emerging
- **Quote**: "In general, I’m noticing that “old” best practices are helpful when building better software when working with AI."
- **Our assessment**: Corroborated by the Pocock and inside-anthropic notes; supports guide advice to front-load design for hard-to-reverse work.

### Claim 17: Predictions — cloud agents dominate, engineers stop reading the code, new agent-aware internal infra (CI/CD with agentic evals, deploy, observability), a "golden age" of migrations
- **Evidence**: Forecast, grounded in Ramp's Inspect and Charity Majors' framing.
- **Confidence**: anecdotal (predictions)
- **Quote**: "What would it take for you to be comfortable shipping code without you reading it and understanding it? Because that is engineering."
- **Our assessment**: Majors' question is the most useful reframing: define the evidence needed to ship unread code (as Ops/QA already do). Orosz himself says timing is uncertain ("this year, next year, or further in the future").

### Claim 18: Domain expertise and AI positivity become hiring/market-value criteria; specializations, juniors and team sizes shrink
- **Evidence**: Titus Winters quote; a Series D Director of Engineering; links to his job-market deepdive.
- **Confidence**: anecdotal
- **Quote**: "When intelligence becomes commonplace, wisdom and charisma become much more important."
- **Our assessment**: Winters' intelligence/wisdom/charisma frame supports guide emphasis on domain context as the human contribution. Hiring claims are anecdotal and out of the guide's core scope.

## Concrete Artifacts

```
Steve Yegge's levels of AI usage (as listed in the article, quoted from a Pragmatic Engineer podcast):
1. No AI usage
2. AI agent in the IDE, with strict permissions
3. AI agent in the IDE, with “YOLO” mode (permissions off)
4. AI agent in the IDE, no longer looking at the code, but interacting with the agent
5. CLI-first: abandoned the IDE
6. Running several agents in parallel
7. Running 10+ agents
8. Built a custom agent orchestrator to run 30+ (or 100+) agents
```

```
Named internal harnesses (article, section "#7 Everyone is building their own harness/agent platform"):
Ramp (Inspect), Stripe (Minions), Uber (Minion), Block (Goose), Shopify (River),
Google (Agent Smith), Meta (Devmate), Amazon (Kiro + Crew), Dropbox (Nova), Spotify (Honk),
DoorDash (Flux), Grab (LLM-Kit), WorkOS (Horizon), Hubspot (Crucible),
Monzo (Agent Chip), Sierra (Pinecone), Harvey (Spectre), Browserbase (bb)
```

```
Migration data points (article, section "#10 Migrations no longer take years"):
Anthropic  Bun Zig -> Rust            11 days   (vs est. 1.5 engineering years)
OpenAI     API layer Python -> Rust   ~5 months (vs several years)
Airbnb     3,500 e2e test files Enzyme -> React Testing Library   6 weeks
Asana      4,000 e2e test files Enzyme -> React Testing Library   2 weeks (vs est. five years)
Uber       600,000 JUnit 4 tests, 15M LOC -> JUnit 5               4 months
```

```
Product timeline for the fading IDE (article, section "#6 The fading IDE"):
Nov 2025  Antigravity 1.0 (last major VS Code-fork IDE)
Feb 2026  Codex launches as non-IDE
Apr 2026  Cursor relaunches without IDE interface (legacy fork maintained for enterprises)
May 2026  Antigravity 2.0 moves away from IDE concept
          JetBrains pivoting to JetBrains Air (agentic development environment)
```

```
Data points (charts from GitHub / Linear / Factory AI; values per article text):
- Agent-authored PRs: ninefold increase in eight months; > human-authored in Aug 2026
- Agent-created issues > human-created in Linear since July 2026
- Factory AI: 83% of users use skills, 2.5x since Feb 2026
- Uber per-token costs down 50%+ (open models + routing); total cost flat since May
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 1 (GitHub PR volume growth, accelerating from end of 2025) and Claim 2 (humans reviewing the AI's review); this article's "theater" framing is the symptom, that note documents responses.
  - `blog-pragmaticengineer-orosz-ramp-inspect.md` Claim 5 (Ramp's reasons for building its own harness include local tools being limited to one or two concurrent sessions) supports Claim 6 above.
  - `blog-pragmaticengineer-orosz-openai-software-factory.md` Claim 9 (OpenAI shipped a non-IDE Codex app betting agents make IDEs matter less) and Claim 10 (~10x load increase on dev infrastructure) corroborate the IDE and GitHub-load points.
  - `blog-pragmaticengineer-orosz-pocock-ai-skills.md` Claim 8 ("leading words" such as tracer bullets) is the source of this article's tracer-bullet claim.
  - `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 1 (Managed Agents needed typical pre-AI upfront planning) and Claim 3 (two years pre-AI vs six months) back the "planning still happens" point; Claim 10 (fanning out to many Claudes) backs parallel-agent use.
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 1 (11 days vs 1-2 years) and Claim 11 (19 known regressions) — same migration, more detail.
  - `blog-pragmaticengineer-orosz-engineering-leader-career-break.md` is the source for the career-break aside (its Claim 1).
- **Contradicts**: None found. Apparent tension between "1-2 engineers per project" (Claim 10) and "teams still matter" is a conditioning difference (project staffing vs. ownership/on-call), within the same source; no contradiction issue filed.
- **Extends**: `blog-pragmaticengineer-orosz-slow-down-speed-up.md` (the six-months-ago snapshot; this is the October update), and `survey-pragmaticengineer-ai-tooling-2026.md` (tooling adoption) with GitHub/Linear/Factory AI data. The 8-level Yegge ladder is a usable maturity scale.
- **Novel**: GitHub agent-PR vs human-PR crossover (Aug 2026); Linear agent-created issues crossover and AI-only-review trend; Factory AI skills adoption (83%); the IDE-retreat product timeline; the named-harness census; "non-engineers not shipping to production" negative finding; Zaytsev's workload-expectation-creep observation; Majors' "shipping code you haven't read" framing.

## Guide Impact

- **Ch02 (AI-native workflows)**: Add Yegge's 8-level ladder as a maturity framing and the 5-10 parallel-session / git-worktree-rotation pattern with "cognitive overhead" as the stated limit (Claims 1, 2, Artifacts). Add a note that the IDE role is shifting to monitoring/validation (Claim 5) — present as a trend with the dated product timeline, not a prescription.
- **Ch03 (verification/validation)**: Cite Sumner (tests ≈ same effort as code, AI writes them) and Orosz's observation that validation of agent output is where companies are investing (Claim 14); pair with Majors' "what would it take to ship unread code" as a framing question.
- **Ch04 (team structures/planning)**: Use Claim 10 and 16 to state that team ownership, on-call and upfront planning for complex work persist; 1-2 engineers per project is the observed staffing unit.
- **Ch05 (harnesses/platforms)**: Use the named-harness census and the Slack → cloud agent pattern (Claims 6, 7) as evidence that custom harnesses are the norm among larger companies; add cost levers (model routing, open models, Claim 9).
- **Ch06 (review/testing)**: Cite the "theatrical review" symptom (Claim 11) as motivation for risk-tiered review and AI-only review, while linking to the code-review-approaches note for the responses. Add the caution that quality/reliability complaints (Claim 12) are anecdotal.
- **Guide-wide caveat**: Most numbers are single-vendor charts and counterfactual estimates; label them as such.

## Extraction Notes

- Read the full article body via direct fetch (the page text was complete through the comments section). The video and paid slides were not accessible. Did not follow the many linked deepdives; instead, cross-referenced the existing corpus notes for them.
- All quotes were copied from the fetched page text; curly apostrophes preserved.
- Source-internal oddity: "as of today (October 2025)" in section #3 is presumably a typo for 2026.
- Two reader comments (on novelty of "no hand-written code" sample, and on rework/waste measurement) raise legitimate questions about sampling bias and unmeasured rework; not part of the article's claims.
