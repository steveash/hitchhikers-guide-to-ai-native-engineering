---
source_url: https://newsletter.pragmaticengineer.com/p/building-codex-with-tibo-sottiaux
source_type: blog-post
title: "Building Codex with Tibo Sottiaux"
author: Gergely Orosz (The Pragmatic Engineer), interviewing Tibo Sottiaux (OpenAI)
date_published: 2026-09-09
date_extracted: 2026-09-10
last_checked: 2026-09-10
status: current
confidence_overall: emerging
issue: "#3353"
---

# Building Codex with Tibo Sottiaux

> A podcast-episode write-up (12 numbered "Takeaways") in which Tibo Sottiaux —
> one of Codex's original engineers, now head of OpenAI's Core Products &
> Platform org — gives the builder's-side rationale for Codex's technical
> design: why it's written in Rust, why it's open source, why the harness is
> deliberately kept "slightly ahead" of the model and shrinks as models
> improve, and how OpenAI's own engineers use Codex for code review,
> maintenance, and rearchitecture internally.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter/podcast show-notes
  page, Substack; published September 9, 2026). This is not a full written
  transcript — the newsletter publishes audio/video (YouTube, Apple,
  Spotify) plus a "Takeaways from the conversation" section (12 numbered,
  paragraph-length summaries, several containing embedded direct quotes and
  one embedded verbatim tweet) and a timestamped table of contents. The
  entire page (confirmed via raw HTML: `expose_paywall_content_to_search_engines`
  is true, and no `data-testid="paywall"` element wraps this section) is
  freely accessible — unlike several other Pragmatic Engineer posts already
  in this corpus (e.g. `blog-pragmaticengineer-orosz-slow-down-speed-up.md`,
  `blog-pragmaticengineer-bun-rust-rewrite.md`), this one is not metered or
  gated.
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager and
  author of The Pragmatic Engineer, already a trusted, heavily-corroborated
  corpus author (see `survey-pragmaticengineer-ai-tooling-2026.md` and the
  many `blog-pragmaticengineer-orosz-*` notes). The interviewee, Tibo
  Sottiaux, is named in the piece as one of the engineers who created Codex
  and now heads OpenAI's Core Products & Platform org (which includes
  Codex) — a first-party, named, on-the-record technical source describing
  his own team's design decisions, not a third-party analyst.
- **Scope**: Covers why Codex is written in Rust, why it's open source and
  the tradeoffs of that choice, why Codex supports non-OpenAI models, a
  prediction about cloud development environments, how the harness and
  model co-evolve, how deeply Codex is integrated into OpenAI's own internal
  systems, a prediction about the automation of code review, and OpenAI's
  internal experience with AI-driven maintenance and rearchitecture. It also
  covers two non-technical items (a career anecdote about a cancelled Google
  project, and Sottiaux's own account of a "ChatGPT before ChatGPT" project
  at Google DeepMind) and closes with Sottiaux's reflection on "being in the
  zone" versus using agents to gather decision-making data faster. Does
  **not** cover: a line-by-line technical architecture walkthrough, specific
  code/config examples, the "SDLC behind Codex" or "Merge: ChatGPT + Codex"
  segments named in the timestamps (these were evidently discussed in the
  audio/video but are not written out in the takeaways text — see Extraction
  Notes), or any quantitative usage/adoption metrics (contrast
  `blog-openai-codex-knowledge-work.md`, which is metrics-heavy but has no
  builder-side design rationale).

## Extracted Claims

### Claim 1: Codex was deliberately built in Rust — not Python or TypeScript, the languages AI models were then strongest at writing — because the team designed from the start for Codex instances to run at millions-of-machines cloud scale, prioritizing performance, security, and efficiency over near-term AI-code-generation ease
- **Evidence**: Author's summary of Sottiaux's stated design rationale (Takeaway 4), framed by Orosz as consistent with a separate performance-engineering commentator's (Casey Muratori's) general point about architecting for performance upfront.
- **Confidence**: emerging (named, first-party rationale from one of the system's original engineers, but presented as Orosz's paraphrase of Sottiaux rather than a direct quote of Sottiaux's own words)
- **Quote**: "Codex is built using Rust, even though the AI models were much better at writing Python and TypeScript at the time. The Codex team had a vision of Codex instances running on millions of cloud machines, which meant performance, security, and engineering for efficiency and scale were the first design principles. This led to Rust, despite AI models then not being the strongest at writing Rust."
- **Our assessment**: This is a genuinely counter-intuitive design choice worth flagging: the team optimized for the *target system's* runtime properties (performance/security/scale) over the *AI-authoring pipeline's* near-term convenience (models write worse Rust than Python/TS), betting that model capability in the chosen language would catch up before scale requirements became a problem. This is a distinct, harder-to-find data point than the general "choose your target language for its own merits" advice — it's a specific account of a team knowingly accepting worse initial AI-assistance quality as the cost of the right long-term system properties.

### Claim 2: Sottiaux states that a Google DeepMind team he was part of, including himself, built a "ChatGPT-like" conversational-LLM product roughly a year before ChatGPT launched (internally called "LMChat" and then another codename), but Google was too nervous to ship it and DeepMind was blocked from releasing products that could disrupt Google's core business
- **Evidence**: A verbatim, embedded X (Twitter) post from Sottiaux's own account (@thsottiaux), quoted in full within the article, replying to another user's recollection of the same project.
- **Confidence**: anecdotal (a single named individual's own retrospective social-media post about an unreleased internal project; no independent corroboration, no named product documentation, and Google itself has not confirmed this account in the source)
- **Quote**: "@_chenglou I was part of that team. Basically ChatGPT one year before it came out. Called LMChat and then another codename. Google was too nervous to release it and DeepMind was blocked from shipping products that could disrupt Google. I think about this a lot."
- **Our assessment**: This is a striking, specific claim (a named internal codename, a specific causal account of *why* it wasn't shipped — organizational risk-aversion and internal product cannibalization concerns, not a technical failure) from someone who says he was personally on the team. It is unverifiable from this source alone — there is no public record cited for "LMChat" beyond Sottiaux's own tweet — but it is a first-party claim from a named, identifiable industry figure, not an anonymous rumor. Treat the *existence* of an internal pre-ChatGPT conversational LLM effort as plausible (consistent with widely-reported industry accounts of Google's LLM research predating ChatGPT) but the specific "blocked from shipping products that could disrupt Google" causal framing as Sottiaux's own interpretation, not a documented internal decision record.

### Claim 3: Sottiaux says he was drawn to join OpenAI in 2023 specifically because he learned ChatGPT — despite its scale of popularity — was built and maintained by a team of only around 20 engineers, and he wanted an environment where Research and Product collaborated more closely than he'd experienced at Google
- **Evidence**: Author's summary of Sottiaux's stated motivation for leaving Google for OpenAI (Takeaway 3).
- **Confidence**: anecdotal (a single individual's self-reported reason for a career move, reported secondhand by the interviewer rather than as a direct quote)
- **Quote**: "When he learned in 2023 that ChatGPT was built and maintained by around 20 engineers – despite its massive popularity – he was very surprised and wanted to join."
- **Our assessment**: A specific, checkable-in-principle organizational data point (team size for a product at ChatGPT's scale as of 2023) that is consistent with other small-team narratives already in this corpus for high-leverage AI products (e.g., this echoes the general pattern, documented elsewhere for Claude Cowork and other Anthropic products, that headline consumer AI products are frequently built by disproportionately small teams). Treat the specific "~20 engineers" figure as Sottiaux's own recollection, not an audited headcount record.

### Claim 4: Codex is released as open source, which Sottiaux frames as bringing trust and an energizing community of outside contributors, but with the specific, less-discussed downside that the Codex team's own work sometimes gets copied and shipped in competing tools before Codex itself ships it
- **Evidence**: Author's summary of Sottiaux's stated view on the tradeoffs of Codex's open-source model (Takeaway 5), explicitly contrasted by the author with Claude Code's closed-source model.
- **Confidence**: anecdotal (a named individual's characterization of his own team's tradeoff, including an admitted downside — the kind of self-critical detail that is more credible than an unqualified positive framing, but still a single first-party account with no named example of the "copied and released first" scenario)
- **Quote**: "Tibo says the upsides are trust and the community of contributors who are an energizing influence. A less discussed downside of open source is that the Codex team's work sometimes gets copied and released in other tools before Codex. Tibo told me this stings, but it's the price of working in the open."
- **Our assessment**: The "stings, but it's the price of working in the open" framing is a candid acknowledgment of a real cost of open-sourcing a competitive product, not just a marketing-friendly "open source is good" claim — this is the kind of qualified tradeoff statement worth citing precisely because it names a genuine downside rather than presenting the decision as costless. This directly corroborates and adds a first-party voice to the open-vs-closed tooling distinction already in the corpus (see Cross-References: `blog-simonwillison-crawshaw-devtools-open-source.md`), which treats Codex's open-source status as a given fact enabling downstream personalization, without previously having the Codex team's own account of *why* they chose it or *what it costs them*.

### Claim 5: Sottiaux frames Codex's support for non-OpenAI models as a direct consequence of being open source — even if Codex were locked to one model, its open-source nature means anyone could fork the harness and change a few lines to add another model — and states his own belief in "winning by letting users use the best models," with the Codex team itself trying other models in the same harness
- **Evidence**: Author's summary of Sottiaux's stated rationale for multi-model support (Takeaway 6), explicitly contrasted with Claude Code being usable only with Anthropic's own models.
- **Confidence**: emerging (a named individual's stated product philosophy, corroborated by the observable, checkable fact that Codex is in fact open source and multi-model — the causal claim "open source is why we support other models" is Sottiaux's own framing, not independently verified)
- **Quote**: "Being open source means that even if Codex were locked down to a model, anyone could still fork the harness and change a few lines of code to support a different model. Tibo believes in winning by letting users use the best models; the Codex team themselves also try other models in the same harness."
- **Our assessment**: This is a specific mechanism claim (open-sourcing removes the *option* of a hard model lock-in, because a fork would trivially route around it) rather than just a restatement of "Codex supports multiple models." It also adds a previously undocumented detail to this corpus: the Codex team itself dogfoods competing models inside its own harness, which is a concrete practitioner behavior (evaluating frontier competitors' models using your own tooling) distinct from a customer-facing feature claim.

### Claim 6: Sottiaux predicts a resurgence of fully cloud-orchestrated development machines — cloud development environments (CDEs), which never gained adoption outside large tech companies because of setup costs — because AI agents like Codex can now handle the configuration and keep a cloud environment in sync with a developer's local machine setup
- **Evidence**: Author's summary of a forward-looking prediction attributed to Sottiaux (Takeaway 7).
- **Confidence**: anecdotal (a single named individual's prediction about a technology trend, not a documented or already-observed adoption shift)
- **Quote**: "Tibo predicts a resurgence of fully cloud-orchestrated machines, where agents like Codex can configure and stay in sync with your local machine setup."
- **Our assessment**: A specific, falsifiable prediction (CDE adoption returning, driven by agents solving the historical setup-cost barrier) worth tracking against future sources on cloud/remote dev environments — this corpus already has substantial material on remote-sandboxed coding agents (e.g. `blog-pragmaticengineer-orosz-ramp-inspect.md`'s Inspect platform, which spins up sandboxed remote environments in under 5 seconds specifically to solve local concurrency limits), which is a live, concrete instance of exactly the "agent-configured cloud environment" pattern Sottiaux is predicting will spread more broadly, rather than a hypothetical.

### Claim 7: The Codex harness is deliberately kept "always slightly ahead" of OpenAI's latest model, supplying the model with "crutches" — guardrails, safety, efficiency, steerability, and a developer message injected into context at the start of each turn — and as models improve, some of these crutches are discarded and the harness shrinks; this has been the harness-and-model development cycle to date
- **Evidence**: Author's summary of Sottiaux's stated description of the harness/model relationship (Takeaway 8).
- **Confidence**: emerging (a named, first-party engineering description of an internal development process, not independently verifiable from outside the company, but specific and mechanistic rather than a vague "we iterate" claim)
- **Quote**: "The harness provides the model with crutches: guardrails, safety, efficiency, steerability, and the developer message injected into context at the start of each turn. As models improve, some 'crutches' are discarded and the harness shrinks. This has been the development cycle between Codex and OpenAI's new models to date."
- **Our assessment**: This is the single most guide-relevant and novel claim in the source: a named engineering leader's explicit mental model for how a coding-agent harness and its underlying model are meant to co-evolve — the harness compensates for a specific, enumerated list of current model weaknesses (safety, efficiency, steerability, guardrails), and the harness's job is to make itself progressively smaller as the model needs fewer crutches, not to accumulate features indefinitely. This gives a concrete criterion for evaluating harness design decisions ("is this a permanent capability, or a crutch that should be removed once the model no longer needs it?") that is not phrased this way anywhere else currently identified in this corpus (see Cross-References — no existing note uses "crutch" framing for harness/model co-evolution).

### Claim 8: Codex is integrated by default into nearly every internal OpenAI system — Slack, every document, and all code — to the point that Sottiaux's own advice to a new team member asking for pointers is "have you asked Codex?"; new hires are reportedly surprised they can ask it who is working on something or why a decision was made, and the team deliberately works in public channels and open documents with broad permissions to make this possible
- **Evidence**: Author's summary of Sottiaux's direct answer to a question about advice for new Codex team joiners (Takeaway 9).
- **Confidence**: emerging (a named individual's first-party description of his own team's internal information-access norms and his own stated advice; not independently audited, but specific about the permissions/culture mechanism that makes it possible, not just the outcome)
- **Quote**: "I asked Tibo what pointers he'd give a new joiner on the Codex team. His answer: 'have you asked Codex?' At OpenAI, it's plugged into Slack, every document, and all code, by default. New starters are surprised about being able to ask it anything, including who's working on something, or why a decision was made. The team purposely work in public channels and open documents with broad permissions."
- **Our assessment**: The load-bearing detail here is not "Codex has broad access" (a capability claim) but "the team purposely works in public channels and open documents with broad permissions" (an organizational/cultural precondition claim) — Sottiaux is describing a deliberate default-to-open information-sharing norm that Codex's usefulness as an institutional-memory tool depends on, not just a technical integration. This is a concrete, actionable pattern for any guide section on making an internal agent broadly useful: the bottleneck is as much about what information the organization chooses to make broadly visible as it is about the agent's technical connectors.

### Claim 9: Sottiaux believes correctness checks and security reviews will be automated by AI, and argues that discussions about the *intent* of code do not need to happen inside a code review — since code review is mostly about correctness, information exchange, and a forcing function for conversations that should have happened earlier — and that, with AI code review, intent conversations are probably best had before the code is written
- **Evidence**: Author's summary of Sottiaux's stated view on the future of code review (Takeaway 10), explicitly linked by the author to a separate same-week Pragmatic Engineer article on code review.
- **Confidence**: emerging (a named engineering leader's stated belief about where code review's remaining human value lives, consistent with — not contradicting — a broader, better-evidenced industry pattern already in this corpus)
- **Quote**: "Tibo believes that discussion about the intent of code doesn't have to happen inside a code review, which is mostly about correctness, information exchange, and providing a forcing function for conversations that should've happened sooner. With AI code review, conversations about what the system should do still matter, and are probably best had before the code is written."
- **Our assessment**: This directly corroborates and adds a named OpenAI voice to `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 10 (some teams already replacing implementation review with upfront plan review, e.g. the `/grill-me` skill) — Sottiaux's framing gives the underlying *reason* that source's practitioners give for the shift: code review was historically overloaded as a catch-all forcing function for correctness checking *and* intent-alignment *and* information-sharing, and as AI absorbs the correctness-checking role, the remaining human-necessary conversation (intent/what-the-system-should-do) is better moved earlier rather than left inside the review step. This is a diagnosis of *why* review is restructuring, complementing that other source's evidence of *that* it is restructuring.

### Claim 10: Sottiaux reports that dependency upgrades at OpenAI can now be handled by a model "blasting through the codebase" within a couple of hours, and rearchitecting a system for new tradeoffs — work that used to take years — can now take days at most, though he explicitly caveats that code quality, good abstractions, and good test suites greatly affect how easy or difficult a given codebase change is to make
- **Evidence**: Author's summary of Sottiaux's stated view on maintenance/rearchitecture cost (Takeaway 11).
- **Confidence**: emerging (a named engineering leader's characterization of his own organization's internal experience, but no specific named project, dollar figure, or before/after measurement is given — less concrete than, e.g., the Bun rewrite's or Asana's fully quantified case studies)
- **Quote**: "Maintenance tasks like dependency upgrades can be handled by a model blasting through the codebase within a couple of hours. Meanwhile, re-architecting for new tradeoffs that used to take years can now take days, at most. Tibo adds a caveat: quality code, good abstractions, and good test suites greatly affect how easy — or not — a codebase change is to make."
- **Our assessment**: This corroborates, at the level of a qualitative directional claim rather than a quantified case study, the specific quantified precedents already in this corpus: `blog-anthropic-code-migration-playbook.md`'s and `blog-pragmaticengineer-bun-rust-rewrite.md`'s accounts of large migrations compressing from years to days/weeks. The explicit caveat — that pre-existing code quality, abstractions, and test coverage are what determine how much this compression is achievable — is consistent with `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 1's framing (Orosz: "a thoroughly-tested project is required to pull it off") and with `blog-openai-asana-codex-case-study.md`'s implicit precondition (a single, well-scoped dependency removal). Sottiaux's version states the precondition explicitly and generally rather than deriving it from a single case study, which is a useful, higher-level articulation of the same pattern multiple case studies in this corpus independently illustrate.

### Claim 11: Sottiaux says the experience of staying "in the zone" for long, late coding sessions is being replaced by treating code as one tool among several for solving problems; he still opens an editor and writes some code because it feels good, but values agents primarily because they let him gather decision-relevant data in about a minute, replacing what used to be a "gut call"
- **Evidence**: Author's summary of a reflective, informal exchange between Sottiaux and Orosz during the interview (Takeaway 12).
- **Confidence**: anecdotal (a single individual's personal account of how his own relationship to coding has changed; explicitly framed by the author as informal, nostalgic conversation rather than a technical or organizational claim)
- **Quote**: "These days, Tibo has adapted, like most people at OpenAI. He still opens an editor and writes a little code because it feels nice, but says that an upside of AI agents is being able to gather more data faster – meaning there's less need for the lengthy coding sessions of yore. Instead of making gut calls, he can fire off an agent and get the data within a minute to make much better decisions with."
- **Our assessment**: This reframes "agent as productivity multiplier" specifically as "agent as a fast decision-support/data-gathering tool," distinct from either "agent writes my code for me" or "agent replaces my job" framings more commonly seen elsewhere in the corpus. The mechanism named — firing off an agent to get data in a minute rather than making a gut call — is a specific, personal workflow claim (not an organizational policy or a measured outcome) and should be read as illustrative color from one senior engineering leader, not as a general practitioner recommendation.

## Concrete Artifacts

```
Source: https://newsletter.pragmaticengineer.com/p/building-codex-with-tibo-sottiaux

Episode timestamps (verbatim from the article's "Timestamps" section):
00:00 Intro
07:21 Working at Google
12:41 What drew Tibo to OpenAI
15:19 The early days of Codex
18:20 Why Codex was built in Rust
21:15 Why Codex is open source
25:50 Codex plays nice with other models: why?
32:09 How the harness works
36:44 Harness and model improvements
41:19 The SDLC behind Codex
46:39 Code reviews at Codex
52:09 Maintenance and architecture
56:43 How AI tools expand what engineers can do
1:02:30 The Merge: ChatGPT + Codex
1:07:16 How Tibo uses Codex and ChatGPT
1:10:44 Advice for engineers who want to work in AI
```

```
Source: https://newsletter.pragmaticengineer.com/p/building-codex-with-tibo-sottiaux
Speaker: Tibo Sottiaux (@thsottiaux on X), embedded verbatim tweet quoted in
the article in reply to @_chenglou's recollection of the same Google project

"@_chenglou I was part of that team. Basically ChatGPT one year before it
came out. Called LMChat and then another codename.

Google was too nervous to release it and DeepMind was blocked from shipping
products that could disrupt Google.

I think about this a lot."
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-pragmaticengineer-orosz-slow-down-speed-up.md`,
`blog-pragmaticengineer-orosz-code-review-approaches.md`,
`blog-pragmaticengineer-bun-rust-rewrite.md`,
`blog-pragmaticengineer-orosz-ramp-inspect.md`,
`blog-simonwillison-crawshaw-devtools-open-source.md`,
`blog-openai-asana-codex-case-study.md`, and
`blog-openai-codex-knowledge-work.md` were re-read directly and claim numbers
below were confirmed against those notes' numbered `### Claim N:` headings in
document order.

- **Corroborates**:
  - `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 10 (OpenAI's
    Codex team runs a tiered AI-code-review system, and code is "not really
    written by hand anymore" on the team) — this source's Claim 9 (Sottiaux's
    own stated view that correctness/security review will be automated and
    intent discussion should move earlier) is the same named individual's
    underlying rationale for the practice that source only described from
    the outside (via a February 2026 conference-talk summary). This source
    is a second, more recent (September 2026), directly-interviewed account
    from Sottiaux himself, six months after that conference talk.
  - `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 6
    (blast-radius risk tiering "is the approach that Anthropic and OpenAI
    follow, which I confirmed by talking with both companies") — this
    source's Claim 9 gives the OpenAI/Codex team's own stated philosophical
    justification (intent conversations belong before code is written, not
    inside review) for why a tiered/restructured review process makes sense,
    complementing that source's confirmation that the practice exists.
  - `blog-simonwillison-crawshaw-devtools-open-source.md` Claim 9 (Codex is
    open source, unlike closed-source Claude Code, which determines whether
    users can personalize the agent via source-level skills) — this source's
    Claim 4 and Claim 5 supply, for the first time in this corpus, the
    Codex team's own first-party rationale for *why* they chose to open
    source Codex (trust, community contribution, enabling multi-model
    support) and the specific cost they say they bear for it (competitors
    sometimes ship copied work first) — that other note establishes the
    open/closed fact and one downstream consequence (personalizability);
    this source explains the original decision and names a cost that note
    does not mention.
  - `blog-pragmaticengineer-orosz-ramp-inspect.md` Claim 9 (Ramp's Inspect
    platform is built on OpenCode, an open-source, HTTP-addressable,
    model-agnostic harness, chosen partly *because* open-sourcing removes
    single-vendor lock-in) — this source's Claim 5 (Sottiaux: open-sourcing
    Codex means the harness could always be forked to support another model
    even if formally locked down) describes the identical mechanism — open
    sourcing a harness structurally prevents durable single-model lock-in —
    from the vendor's own side rather than a downstream adopter's side.
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 1 (Orosz: "a
    thoroughly-tested project is required to pull off" a fast AI-driven
    rewrite) and this source's own Claim 10 (Sottiaux: quality code, good
    abstractions, and good test suites determine how easy a codebase change
    is to make) state the identical precondition — pre-existing code/test
    quality gates how much maintenance/rearchitecture speedup is achievable
    — from two different named practitioners (Jarred Sumner via Orosz's
    framing; Tibo Sottiaux directly) describing two different companies.

- **Contradicts**: None identified. No claim in this source was found to
  materially oppose an existing corpus source note's claim about the same
  situation. The "harness shrinks as models improve" claim (Claim 7) and
  the "quality code/abstractions/tests determine ease of change" caveat
  (Claim 10) are both consistent with, not in tension with, existing corpus
  material on harness engineering and large-scale migrations.

- **Extends**:
  - `blog-openai-codex-knowledge-work.md` (OpenAI's own usage-telemetry
    report on Codex's growth among non-developer "knowledge workers") — that
    source documents *what* Codex usage looks like in aggregate; this source
    adds the builder's-side design rationale (Rust, open source, harness
    philosophy) that the usage-telemetry report does not cover at all. The
    two sources are complementary rather than overlapping.
  - `blog-openai-asana-codex-case-study.md` and
    `blog-openai-loveholidays-codex-case-study.md` (both OpenAI customer
    case studies documenting *externally observed outcomes* of using Codex
    for migrations and self-service platforms) — this source extends those
    with the *internal, first-party* account of OpenAI's own team using
    Codex for maintenance and rearchitecture (Claim 10), giving the guide
    both an OpenAI-internal and an external-customer data point for the
    same "AI drastically cuts maintenance/rearchitecture time" claim.
  - `blog-pragmaticengineer-orosz-ramp-inspect.md` Claim 8 (Ramp: "the only
    constraint on agents' ability is model intelligence, not missing tools
    or access") — this source's Claim 7 (the harness supplies "crutches"
    that are discarded as the model improves) is a compatible but more
    specific model: rather than asserting model intelligence is *already*
    the sole constraint, Sottiaux describes an explicit, ongoing handoff
    process by which the harness's role recedes over time as the model
    closes specific, named gaps (safety, efficiency, steerability,
    guardrails) — a mechanism for *how* an organization gets from "tooling
    is the bottleneck" to "model intelligence is the bottleneck," which
    Ramp's claim asserts as an end state without describing the transition.

- **Novel**:
  - **The "harness provides crutches that shrink as the model improves"
    framing** (Claim 7) is new to this corpus as an explicit mental model
    for harness/model co-evolution, naming specific crutch categories
    (guardrails, safety, efficiency, steerability, the injected developer
    message).
  - **A first-party, named account of why Codex is written in Rust**
    (Claim 1) despite AI models being weaker at Rust than Python/TypeScript
    at the time — a specific instance of choosing a target system's runtime
    properties over the AI-authoring pipeline's near-term convenience.
  - **Sottiaux's own account of an unreleased, pre-ChatGPT "ChatGPT-like"
    project at Google DeepMind** ("LMChat," Claim 2), sourced to his own
    verbatim X post — new to this corpus and worth flagging as
    unverified-but-first-party if the guide ever discusses the history of
    conversational-LLM products.
  - **"Purposely work in public channels and open documents with broad
    permissions" as the organizational precondition for a broadly-useful
    internal agent** (Claim 8) — a specific cultural/permissions claim,
    distinct from a technical-integration claim, not previously phrased
    this way in this corpus.

## Guide Impact

- **Chapter on Harness Engineering / Agent Architecture**: Add Claim 7 (the
  harness supplies enumerated "crutches" — guardrails, safety, efficiency,
  steerability, injected developer message — that are discarded as the
  underlying model improves, causing the harness to shrink over time) as a
  named design philosophy and evaluation heuristic for harness features:
  when adding a harness capability, ask whether it is a permanent
  requirement or a crutch that should be planned for removal as models
  improve. This is more specific than the corpus's existing generic
  "harness compensates for model weaknesses" framing.
- **Chapter on Verification / Code Review practices**: Add Claim 9
  (Sottiaux's own rationale — correctness/security review is automatable,
  and intent conversations are better held before code is written) as a
  named OpenAI-internal voice supporting the already-documented shift
  toward upfront plan review (`blog-pragmaticengineer-orosz-code-review-approaches.md`
  Claim 10) and blast-radius tiering (`blog-pragmaticengineer-orosz-code-review-approaches.md`
  Claim 6, `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 10) —
  this source supplies the *reasoning*, those supply the *evidence of
  adoption*.
- **Chapter on Large-Scale Refactoring and Migrations**: Add Claim 10
  (dependency upgrades in hours, rearchitecting in days rather than years,
  explicitly conditioned on pre-existing code quality/abstractions/test
  coverage) as a second, OpenAI-internal, qualitative data point alongside
  the corpus's existing quantified case studies (Bun rewrite, Asana Enzyme
  removal), reinforcing that the "quality codebase as precondition" caveat
  recurs across independently-sourced accounts from different companies.
- **Chapter on Tool Design / Build vs. Open Source**: Add Claims 4 and 5
  (Codex team's own stated rationale for open-sourcing — trust, community,
  removing durable model lock-in — and the named cost they say they bear —
  competitors sometimes ship copied work first) as the first first-party,
  vendor-side account in this corpus of *why* a major coding-agent vendor
  chose to open source their product and what tradeoff they say it costs
  them, complementing the downstream-consequence framing already in
  `blog-simonwillison-crawshaw-devtools-open-source.md`.

## Extraction Notes

- **Not paywalled**: unlike several other Pragmatic Engineer sources already
  in this corpus, this page is fully accessible. This was confirmed by
  fetching the raw HTML directly via `curl` (not through WebFetch's
  AI-summarization layer, which on an initial pass returned a condensed,
  non-verbatim summary) and checking for the `data-testid="paywall"` marker
  used to bound paywalled sections in sibling notes (e.g.
  `blog-pragmaticengineer-orosz-code-review-approaches.md`,
  `blog-pragmaticengineer-bun-rust-rewrite.md`) — no such marker wraps the
  "Takeaways," "Timestamps," or "References" sections used in this note. All
  quotes above were copied character-for-character from that raw-HTML
  extraction (tags stripped, HTML entities unescaped locally), not
  reconstructed from any AI-generated summary, per MINER.md §2a.
- **This source is a "Takeaways" write-up, not a full transcript.** The page
  states "See the episode transcript at the top of this page" and lists
  16 timestamped segments, but no line-by-line spoken transcript is present
  in the page's text content — only the 12 numbered takeaway paragraphs
  (which is where all claims in this note are drawn from) and the
  timestamp list itself. Three timestamped segments — "The SDLC behind
  Codex" (41:19), "The Merge: ChatGPT + Codex" (1:02:30), and "How Tibo uses
  Codex and ChatGPT" (1:07:16) — are named in the timestamps but have no
  corresponding written takeaway paragraph, meaning whatever was discussed
  in the audio/video at those points is not represented in this note. If a
  full transcript becomes available (e.g. via YouTube captions), it should
  be mined separately rather than assumed to be covered here.
- No sub-pages were followed. The article's "Mentions during the episode"
  reference list links to a prior Pragmatic Engineer deep dive ("How Codex
  is built"), a companion piece already in this corpus
  (`blog-pragmaticengineer-orosz-slow-down-speed-up.md`), an OpenAI cookbook
  page, and general reference links (X profiles, python.org, rust-lang.org)
  — none were substantive enough sub-pages to warrant independent
  extraction beyond what MINER.md §1 requires, and the one genuinely
  substantive linked deep dive ("How Codex is built") is not yet in this
  corpus and would be a candidate for its own separate source-submission
  issue rather than being folded into this note.
- No contradictions were identified or filed; see Cross-References
  `Contradicts` above.
