---
source_url: https://simonwillison.net/2026/Jul/21/cat-and-thariq/
source_type: blog-post
title: "A Fireside Chat with Cat and Thariq from the Claude Code team"
author: Simon Willison (transcript of Cat Wu and Thariq Shihipar, Anthropic Claude Code team)
date_published: 2026-07-21
date_extracted: 2026-07-26
last_checked: 2026-07-26
status: current
confidence_overall: emerging
issue: "#2241"
---

# A Fireside Chat with Cat and Thariq from the Claude Code team

> Simon Willison's edited transcript of a fireside chat at AI Engineer World's
> Fair with Cat Wu and Thariq Shihipar (Anthropic's Claude Code team), covering
> the Claude Code system prompt's 80% size reduction, the team's gradual
> handoff of code review to Claude, Claude Tag's 65%-of-PRs multiplayer
> workflow, the credential-injection pattern for agent API access, and how
> Anthropic decides which features to ship.

## Source Context

- **Type**: blog-post (edited interview transcript, published on Simon
  Willison's personal blog; a companion YouTube video of the full session is
  linked but not itself extracted here — extraction is from the transcript
  text only, fetched via raw HTML)
- **Author credibility**: The primary content is not Willison's own
  commentary but a transcript of direct, on-the-record statements from Cat Wu
  and Thariq Shihipar, both named members of Anthropic's Claude Code team,
  at a public conference (AI Engineer World's Fair). Willison hosted the
  session, edited the transcript, and added his own bolded highlights and a
  handful of first-person annotations (clearly distinguishable from the
  Q&A exchanges). This is first-hand primary-source material from the team
  that builds Claude Code — comparable in authority to Anthropic's own
  engineering blog posts, though delivered conversationally rather than as a
  reviewed publication, so figures are less precise (e.g., "roughly," "about")
  than a written postmortem.
- **Scope**: Covers day-to-day workflow changes, product prioritization,
  Claude Tag's multiplayer collaboration model, code review evolution, eval
  methodology, system prompt optimization (the 80% reduction), tool design
  philosophy, auto mode security architecture, credential injection, personal
  side projects (Street Fighter game, climbing trip planner), and closing
  advice on company culture. Does NOT cover: Claude Code's technical
  architecture/source code, pricing, the Fable/Mythos model family in detail
  beyond video editing anecdotes, or any metrics beyond what the two
  speakers state conversationally (no citations to internal dashboards or
  written eval reports).

## Extracted Claims

### Claim 1: Claude Tag now lands 65% of the Claude Code team's product engineering PRs

- **Evidence**: Direct, repeated statement from Cat Wu, specific to "our
  product engineering team," restated a second time in response to a
  clarifying question from Willison about scope.
- **Confidence**: settled (specific first-party figure, restated for
  precision after a direct follow-up question)
- **Quote**: "This is just for our product engineering team — our internal
  version of Claude Tag lands 65% of our product PRs right now. And this is a
  huge shift; this is more than 50% of our PRs."
- **Our assessment**: The follow-up exchange is important: Willison
  explicitly asked "For all of Anthropic, or just for Claude Code?" and Cat
  narrowed the claim to "our product engineering team" — this is not an
  Anthropic-wide figure, and the guide should preserve that scoping rather
  than generalize it. Cat also draws the practical division of labor: "Claude
  Code is still the best place for your most complex tasks, when you're
  interactively iterating with the agent. But Claude Tag is great for having
  it work proactively on your behalf." That division — interactive complex
  work vs. proactive routine work — is a reusable framework for teams
  choosing between an interactive coding agent and a proactive
  channel-embedded one.

### Claim 2: The Claude Code system prompt was reduced by 80% for frontier models, chiefly by removing examples

- **Evidence**: Direct statement from Thariq Shihipar in response to a
  specific question about the 80% figure Willison had heard him mention
  earlier that day.
- **Confidence**: settled (specific, named percentage from the engineer
  directly responsible for the change)
- **Quote**: "One of the patterns we saw is that we were over-constraining
  Claude. The initial, maybe Opus 4-ish models wanted a lot of examples, and
  removing examples was extremely helpful, because it was just more creative
  than the examples we gave it."
- **Our assessment**: This directly contradicts a prompting heuristic Willison
  himself volunteers as one of his "top prompting tips" ("give it examples"),
  and both speakers register surprise at this ("I was surprised to hear that"
  — Thariq). The reduction is explicitly model-capability-dependent, not a
  universal claim: it applies "to Fable 5 or even Opus 4.8," and per Claim 4
  below, older/smaller models still receive the full, example-laden prompt.
  This should be presented in the guide as a frontier-model-specific finding,
  not a blanket "stop using examples" rule.

### Claim 3: Lists of "don't do X and don't do Y" instructions reduce output quality on the latest models; the team now favors context over hard constraints

- **Evidence**: Direct statement from Thariq, elaborated on by Cat with a
  concrete before/after example of a verification instruction.
- **Confidence**: settled (specific, named prompt-engineering principle from
  the team's own before/after example)
- **Quote**: "The other thing we did is try to give it more context and fewer
  'do not do this' instructions, because that's a very strong impulse for
  Claude, and especially if it conflicts with user instructions later on,
  that can be extremely confusing to Claude... So we try to have fewer hard
  constraints, more context, and fewer instructions overall."
- **Quote** (Cat's worked example): "We found a few cases where yes, this
  statement is 90% true, but there's a real 10% of cases where it's not
  true... So we've adjusted our wording from 'always verify, verify, verify'
  to something like: most of the time when you're doing front-end work you
  can't fully understand the experience by hitting the backend endpoints, so
  when you make larger changes to the user experience, please run the app
  locally."
- **Our assessment**: Cat's framing — "you should think about the ways in
  which it could be misinterpreted by a well-intentioned human... and soften
  the prompt so that it's actually 100% accurate" — is a concrete editing
  heuristic: audit each absolute instruction ("always X") for the 10% of
  cases where it's false, and rewrite it as conditional context rather than
  a hard rule. This is a specific, actionable technique distinct from the
  more general "remove examples" finding in Claim 2.

### Claim 4: Claude Code now runs a different system prompt per model, with only the most frontier models receiving the 80%-reduced version

- **Evidence**: Direct statement from Cat in response to Willison's question
  about whether the shorter prompt would work for a cheaper model like Haiku.
- **Confidence**: settled (explicit architectural statement)
- **Quote**: "We actually have a different system prompt per model now, for
  this very reason. It's only our most frontier models that have this 80%
  token decrease — the older models still have the full system prompt."
- **Our assessment**: This is the load-bearing qualifier on Claim 2 — the 80%
  reduction is not a single global prompt change but a per-model-tier
  configuration decision, contingent on a frontier model's judgment being
  reliable enough to fill in what examples used to specify. When Willison
  asks directly whether Fable/Opus are smart enough to write a more detailed
  prompt for Haiku, Cat says plainly: "We haven't been able to eval it — we
  don't have any hard data to show it" — an honest admission of an open
  question, not a claimed capability.

### Claim 5: Code review is splitting into two tiers — human code-owner review for critical areas, and Claude-driven review for "outer layers," reached via a six-plus-month trust-building process

- **Evidence**: Extended exchange between Thariq and Cat describing the
  current state and how they got there, including the specific mechanism for
  building trust (incident review feeding an eval set).
- **Confidence**: settled (detailed first-party process description with a
  named timeframe)
- **Quote**: "For important areas we have code owners. The system prompt is
  an example where we have a code owner — you really need to get their
  approval." (Thariq)
- **Quote** (the trust-building mechanism): "In the beginning we had human
  review for everything, and then increasingly we would say, okay, for code
  changes that touch these files, code review is catching 100% of the issues
  there — so we actually don't need a human manually reviewing those. And
  when we have incident review, we look at the PRs that caused the incident
  and say, okay, how do we update code review to catch that — and we take
  those PRs and add them to an eval set to make sure our future changes to
  code review never regress that metric." (Cat)
- **Our assessment**: The mechanism described — incident review feeds
  concrete failing PRs into a regression eval set for the code-review system
  itself — is the most transferable part of this claim: it turns "we trust
  automated review" from a one-time confidence judgment into a continuously
  regression-tested claim. This is a meaningfully more rigorous trust-building
  process than "we ran it for a while and it seemed fine." Note the tension
  with `blog-anthropic-claudecode-quality-postmortem.md` Claim 7, which
  documents a real April 2026 bug that passed human code review, automated
  code review, unit tests, E2E tests, *and* dogfooding simultaneously — see
  Cross-References below; this is a caveat on the claim's confidence, not a
  contradiction of the same claim.

### Claim 6: Auto mode's Sonnet classifier makes prompt-injection and data-exfiltration risk "far lower than the average human reviewer," according to Cat — a comparative, not absolute, safety claim

- **Evidence**: Direct statement from Cat after Willison presses her on
  whether Anthropic has "mitigated every attack" (her prior sentence).
- **Confidence**: settled as a direct quote; emerging as a safety claim
  (self-reported, comparative, no independently reproducible benchmark cited
  in the transcript itself)
- **Quote**: "It doesn't catch 100% of things — that would be way too strong a
  claim. But for the main categories of risks that we're concerned about,
  like prompt injection and data exfiltration, the risks are far lower than
  the average human reviewer."
- **Our assessment**: Cat is careful to walk back her own prior, stronger
  statement ("we've pretty much mitigated every attack") to this narrower,
  comparative claim once Willison challenges it directly ("That is a big
  claim"). The comparison baseline is explicitly "the average human
  reviewer," not zero risk — this is consistent with, and less absolute than,
  the "not a drop-in replacement for careful human review on high-stakes
  infrastructure" caveat in Anthropic's own auto mode engineering post (see
  Cross-References). No specific false-negative/false-positive numbers are
  given in this transcript; Anthropic says it will "publish some evals in the
  coming weeks."

### Claim 7: Claude Code supports a credential-injection pattern where agents can use an API credential (e.g., Datadog) without ever holding it — a proxy injects it at request time

- **Evidence**: Direct feature description from Cat, framed around a
  concrete named example (Datadog).
- **Confidence**: settled (specific first-party feature description)
- **Quote**: "If you want Claude Code to be able to access Datadog, but you
  don't want Claude Code itself to hold the Datadog credential, you can set
  up our identity and credential management system so that the Datadog
  credentials are only usable by the agent but not accessible by the agent —
  we insert them on the fly when the agent tries to make a Datadog request."
- **Our assessment**: "Usable by the agent but not accessible by the agent"
  is a precise, quotable framing of the injection-at-the-network-boundary
  pattern. This matches — for Claude Code specifically, with a concrete named
  connector (Datadog) — the architecture already documented for Claude Tag's
  channel-scoped credentials in `blog-anthropic-agent-identity-access-model.md`
  Claim 8 ("stored independently and mapped to that channel's identity, then
  injected at the network boundary at request time"). This transcript is the
  first corpus source to confirm the same credential-injection pattern is
  also exposed in Claude Code (not just Claude Tag), and to name a specific
  connector (Datadog) as an example.

### Claim 8: Features ship publicly only after clearing an internal active-user and retention bar with Anthropic employees as the first cohort

- **Evidence**: Direct process description from Cat in response to a
  question about prioritization.
- **Confidence**: settled (specific first-party process description)
- **Quote**: "Before we share our products with everyone in the world, we
  share them with everyone within Anthropic, and with some early customers
  who give us very honest feedback about it... We have an internal bar for
  the number of active users and the amount of retention a feature has to
  have before we share it with the world. Because this bar is very clear,
  every engineer knows what they're trying to hit."
- **Our assessment**: The mechanism Cat names for *why* this works as a
  prioritization filter is notable: "if the feature isn't polished, people
  will churn — and then we shouldn't ship that feature." This reframes
  internal dogfooding (which the team calls "ant fooding" — see Concrete
  Artifacts) from a QA step into the actual shipping gate itself, with
  retention as the pass/fail metric rather than a bug count or a subjective
  go/no-go call.

### Claim 9: Thariq states plainly that "rewrites are now good," reversing decades of software engineering wisdom against rewrites, provided a good test suite exists

- **Evidence**: Direct statement from Thariq in response to a question about
  which piece of conventional software engineering wisdom no longer holds,
  immediately affirmed by Willison ("The worst thing you could do is now
  actually fine!") and elaborated with a concrete example (Bun).
- **Confidence**: emerging (a strong personal position stated plainly, not
  hedged as "sometimes" or "for some codebases"; backed by one named example
  rather than a survey of cases)
- **Quote**: "For me, it's that rewrites are now good."
- **Quote** (continuing after Willison's "The worst thing you could do is now
  actually fine!"): "Exactly. All the Mythical Man-Month stuff — never
  rewrite — I'm pro-rewriting now. If you have a good test suite — and I
  think the rewrite actually forces you to make sure you have a good test
  suite — but I think what people undercount is that a codebase is a spec,
  and maybe it's the only copy of the spec that you have, because no one
  knows every branching part of the codebase."
- **Our assessment**: "A codebase is a spec, and maybe it's the only copy of
  the spec you have" is a compact, quotable justification for treating
  large-scale AI-driven rewrites as spec-extraction exercises rather than
  purely mechanical translations — distinct from (and a good companion
  framing for) the corpus's existing Bun Zig-to-Rust rewrite case study. On
  the specific example: "We rewrote Bun in Rust and it works great — it's
  live for me right now," and in response to Willison's direct follow-up
  ("You're not shipping Claude Code on Bun-in-Rust yet, right?"), Thariq
  confirms: "Internally we have." Willison's own editorial aside notes
  Anthropic "started shipping Claude Code on Bun-in-Rust to everyone on June
  17th" — this independently corroborates the exact date already documented
  in `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 12 (Claude Code
  v2.1.181, released June 17, 2026, as first production consumer of the Rust
  port) from a second, independent source (the Claude Code team itself,
  on the record, a month later).

### Claim 10: Compressed idea-to-ship timelines (six-to-twelve months down to "maybe even a week") are shifting the highest-value engineering skill from execution speed to product/business judgment

- **Evidence**: Direct statement from Cat framing this as "one of the biggest
  shifts we're seeing in the eng skill set."
- **Confidence**: emerging (a directional claim about skill-value shift,
  asserted from the speaker's vantage point inside a fast-moving AI lab —
  not necessarily representative of slower-moving or more regulated
  engineering organizations)
- **Quote**: "The timeline between having an idea and building it is so much
  shorter — it's down from six to twelve months to maybe even a week. That
  means all of us need to have better taste on what is worth building, what
  will actually inflect the businesses we're working on. So it's an increase
  in value on product taste and business sense, and a bit lower on execution
  in most product domains. Of course, for infra there's still a very heavy
  emphasis on making sure all the details are right."
- **Our assessment**: Cat explicitly carves out an exception for
  infrastructure work ("still a very heavy emphasis on making sure all the
  details are right") — the guide should preserve this qualifier rather than
  present the taste-over-execution shift as universal across all engineering
  domains. This corroborates the thesis already documented from a labor-market
  angle in `blog-addyosmani-earning-taste-judgment.md` Claim 1 ("Taste used
  to be a byproduct of the reps. Agents took the reps.") — that note argues
  the *supply* of taste is threatened because junior engineers no longer get
  the reps that used to produce it passively; this transcript corroborates
  from the *demand* side — taste is what's increasingly valuable precisely
  because execution has become cheap and fast.

### Claim 11: When code production accelerates, time spent blocked awaiting someone else's decision becomes a much more visible bottleneck — Willison's own synthesis, not a direct quote from Cat or Thariq

- **Evidence**: This is Willison's own editorial commentary, inserted
  immediately after Cat's answer about the product manager role changing
  ("plugging in whenever there's any kind of gap"), not a quote from either
  speaker.
- **Confidence**: anecdotal (single commentator's inference, though a
  well-known and widely cited practitioner)
- **Quote**: "This reflects something I've noticed: when you can produce code
  so much faster, time spent blocked awaiting a decision from someone else
  becomes a much more notable bottleneck. Engineers who can make product
  decisions can move a whole lot faster, and the cost of getting one of those
  decisions wrong is much less prohibitive."
- **Our assessment**: Flagging the attribution explicitly because MINER.md
  §2a requires quotes be the source's own words — this passage is Willison's
  own words about the interview, not Cat's or Thariq's. It is still worth
  extracting because it names a specific, guide-relevant organizational
  bottleneck (decision latency) as a *consequence* of the other claims in
  this note (faster code production, PMs "plugging in whenever there's any
  kind of gap" per Cat's own words in the same exchange), and because
  Willison's second clause — "the cost of getting one of those decisions
  wrong is much less prohibitive" — gives a concrete reason organizations
  might want to push decision authority down to engineers: mistakes are
  cheaper to reverse when redoing the work is fast.

### Claim 12: The Claude Code team deliberately keeps tool cardinality low, requiring each tool to have a function distinct from every other tool so Claude can reliably choose between them

- **Evidence**: Direct statement from Cat, given as the team's operating
  principle for adding new tools, following Thariq's more general framing
  that tool design is "more of an art... or a biology" than a science.
- **Confidence**: settled (specific first-party design principle)
- **Quote**: "In general as we introduce more tools, we try to keep the
  cardinality pretty low and make sure that every tool we add has a distinct
  function from every other tool, so that Claude can very easily distinguish
  when to call each."
- **Our assessment**: This is a concrete, actionable tool-design heuristic
  for anyone building a custom agent harness with several tools: before
  adding a new tool, check whether its function is genuinely distinct from
  every existing tool, not just usefully specialized. Thariq's parallel
  statement that they "trend towards fewer tools" and specifically "removed
  our grep and other search tools — glob tools — in favor of native bash" is
  a concrete example of consolidation in the same direction. Thariq's
  self-deprecating admission that his own "career peaked" when he introduced
  the ask-user-question tool, and that it is "hard to eval" because it's "more
  of a user preference thing," is a useful acknowledgment that not every tool
  decision is measurable via standard evals.

### Claim 13: The dedicated file-edit tool is kept mainly for UI purposes (so Claude Code can show a deterministic "approve this edit" prompt), not because it's technically necessary for auto-mode users

- **Evidence**: Direct explanation from Cat of why the file-edit tool
  persists despite the team's general preference for fewer, more general
  tools.
- **Confidence**: settled (specific first-party design rationale)
- **Quote**: "The reason we had a dedicated file edit tool was so that we
  could deterministically know that Claude was making a file change, so we
  could show people this nice UI... But for a lot of us who are on auto mode
  right now — hopefully you're not on YOLO mode — I don't think it actually
  matters, and we could probably just remove file edit and be totally fine."
- **Our assessment**: This is a clear example of a tool that exists for a
  UX/observability reason (rendering a deterministic approval prompt) rather
  than a model-capability reason (Claude could edit files via bash/sed just
  as well). For harness designers: a dedicated tool can be justified purely
  by the deterministic hook it gives the surrounding UI, independent of
  whether the underlying model actually needs the narrower interface.

### Claim 14: OpenAI's own GPT-5.6 prompting guidance echoes the "leaner system prompts" finding independently, with quantified numbers Willison quotes directly in his post

- **Evidence**: This is not a claim by Cat or Thariq — it is a passage
  Willison inserts into his own post, quoting OpenAI's published GPT-5.6
  prompting best practices, immediately after the system-prompt-reduction
  discussion (Claims 2–4).
- **Confidence**: settled (verbatim quote of a named, dated, external vendor
  document, as reproduced in this source)
- **Quote**: "Favor leaner prompts. Removing repeated instructions and
  examples and simplifying tool descriptions can improve task performance
  and token efficiency. In a sample of internal coding-agent eval runs,
  configurations with leaner system prompts improved evaluation scores by
  roughly 10–15% while reducing total tokens by 41–66% and cost by 33–67%."
- **Our assessment**: This is cross-vendor corroboration for the same
  directional finding as Claims 2–3 (Anthropic's own 80% system-prompt
  reduction and "remove examples" principle) — OpenAI independently reports
  quantified evaluation-score gains (10–15%) alongside token/cost reductions
  (41–66% tokens, 33–67% cost) from leaner prompts. Note this is OpenAI's
  GPT-5.6 guidance specifically, a different, more recent document than the
  GPT-5.5 prompting guide already in the corpus (`blog-simonwillison-gpt55-prompting-guide.md`)
  — see Cross-References for how the two relate.

## Concrete Artifacts

### Willison's top-level bullet summary (verbatim, from the top of the post)

```
Source: simonwillison.net/2026/Jul/21/cat-and-thariq/

Claude Tag (Claude's new collaborative Slack integration) now lands 65% of
the product engineering PRs for the Claude Code team.

Claude Code ships features to Anthropic employees first, and only ships the
features that demonstrate user retention with that cohort

Critical changes to Claude Code are still reviewed manually, but the team
increasingly relies on automated code review for the "outer layers" of the
product.

Adding examples to a system prompt is no longer best practice for models
like Fable 5 or even Opus 4.8. The Claude Code system prompt recently
reduced in size by 80%.

Likewise, lists of "don't do X and don't do Y" can reduce the quality of
results from the latest models.

Dogfooding inside Anthropic is called "ant fooding".

Anthropic really believe in their auto mode, and see that as an enabling
technology for Claude Tag.

Thariq advises offsetting coding-agent-induced Deep Blue by "being more
ambitious" with the work you take on.

Fable is competent at editing video, and Thariq used it to edit its own
launch video.

Anthropic's culture of working (internally) in public is key to their
success, as demonstrated by the way they use Claude Tag in their public
Slack Channels.
```

### Auto mode mechanics, as described by Thariq and Cat (verbatim excerpts)

```
Source: simonwillison.net/2026/Jul/21/cat-and-thariq/

"Whenever Claude is doing a turn, or a bash call, there's a Sonnet
classifier that is judging the tool call and also the context of the
conversation — your instruction... So it's good at the dynamic permissions
that you yourself give inside the prompt... It also works well with our
sandboxing infrastructure... We have a sandbox, and when something needs to
escape the sandbox — like a network request — auto mode can look at that
request and ask: does this make sense? — and allow it." (Thariq)

"We've been using it within Anthropic since January, so we've been
hardening it for quite a while." (Cat)
(First made available to the public on March 24th, per Willison's own aside.)

"This is also the reason Claude Tag is so good — Claude Tag uses auto mode.
... we have a general Swiss cheese defense for security; we also RL against
this stuff — I think this is really what makes Claude Tag work." (Thariq)
```

### Remote control's unexpected adoption pattern (verbatim, from Cat)

```
Source: simonwillison.net/2026/Jul/21/cat-and-thariq/

"Once we rolled out remote control, so many people I talk to told me that
what they do every night is plug their laptop into a power charger, open a
bunch of remote control sessions, lock the screen, and then use their mobile
phone from their couch to control Claude Code. So this has become a flow
we're now leaning into that I didn't originally get — but now I do." (Cat)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-agent-identity-access-model.md` Claim 8 ("the credential
    is stored independently and mapped to that channel's identity, then
    injected at the network boundary at request time") — Claim 7 here
    confirms the identical credential-injection architecture ("usable by the
    agent but not accessible by the agent") applies to Claude Code itself
    (named example: Datadog), not only to Claude Tag channels, and gives a
    second independent first-party confirmation of the pattern.
  - `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 12 (Claude Code
    v2.1.181, released June 17, 2026, first production user of the Bun Rust
    port) — Claim 9 here independently corroborates the same shipping date
    from a second first-party source: Willison's own aside in this piece
    states Anthropic "started shipping Claude Code on Bun-in-Rust to everyone
    on June 17th," and Thariq confirms internal use on the record a month
    after that date.
  - `blog-addyosmani-earning-taste-judgment.md` Claim 1 ("Taste used to be a
    byproduct of the reps. Agents took the reps.") — Claim 10 here
    corroborates from the opposite side of the same thesis: Osmani argues the
    supply of taste is threatened (junior engineers lose the reps that used
    to build it); Cat's statement here argues the demand for taste is rising
    (compressed timelines make product judgment the scarcer, higher-value
    skill). Together they describe a taste squeeze from both directions.
  - `blog-anthropic-claude-code-auto-mode.md` Claim 11 ("the transcript
    classifier running on Sonnet 4.6") and Claim 10 ("not a drop-in
    replacement for careful human review on high-stakes infrastructure") —
    Claim 6 here corroborates both: Thariq independently names "a Sonnet
    classifier" as the auto mode mechanism (consistent with, though less
    precise than, the "Sonnet 4.6" naming in the engineering post), and Cat's
    walked-back claim ("far lower than the average human reviewer," not "100%
    safe") is consistent in spirit with the engineering post's explicit
    non-replacement caveat, using a different, narrower comparison baseline
    ("average human reviewer" rather than "careful human review").
  - `blog-simonwillison-gpt55-prompting-guide.md` Claim 4 ("Start with the
    smallest prompt that preserves the product contract, then tune reasoning
    effort, verbosity, tool descriptions, and output format") — Claims 2–3
    and 14 here corroborate the same leaner-prompt direction from Anthropic's
    side (80% system-prompt reduction, remove examples, fewer hard
    constraints) as that note documents from OpenAI's GPT-5.5 guidance. Claim
    14 here specifically quotes OpenAI's *GPT-5.6* prompting guidance (a
    later, different document than the GPT-5.5 guide that note covers) with
    its own quantified figures (10–15% eval score improvement, 41–66% token
    reduction, 33–67% cost reduction) — this is new, more recent corroborating
    evidence from the same vendor, not a duplicate of that note's claims.

- **Contradicts**: None filed. The closest candidate — Claim 5's description
  of a maturing, regression-tested trust process for automated code review
  versus `blog-anthropic-claudecode-quality-postmortem.md` Claim 7's account
  of a bug that passed human review, automated review, unit tests, E2E
  tests, and dogfooding simultaneously in April 2026 — is not a material
  contradiction under MINER.md §4a: the postmortem documents a real failure
  of the verification stack *as it existed at that time*, which is
  consistent with (and arguably the kind of incident that feeds) the
  incident-review-to-eval-set mechanism Cat describes in Claim 5 as the
  *process* for improving that stack over time. Both sources would support
  the same guide advice (automated review can be trusted incrementally, file
  by file, backed by continuous incident-driven eval expansion — not treated
  as a solved problem after a single confidence judgment), so this does not
  meet the "would lead to different guide advice" bar for filing a
  contradiction issue.

- **Extends**:
  - `blog-anthropic-claudecode-quality-postmortem.md` Claim 15 ("Add
    model-specific change gating via CLAUDE.md documentation") — that note
    documents this as a *planned* process change announced in an April 2026
    postmortem after a system-prompt-verbosity regression; Claim 4 here
    confirms, three months later, that per-model system prompts are now a
    shipped reality ("we actually have a different system prompt per model
    now"), with the specific detail that only frontier models receive the
    80%-reduced version.
  - `blog-anthropic-agent-view-claude-code.md` — that note documents the
    agent view UI for managing parallel Claude Code sessions from a single
    terminal interface; Claim 8 here (remote control's unexpected adoption
    pattern — leaving a laptop plugged in overnight and controlling sessions
    from a phone) documents a related but distinct multi-session management
    behavior pattern, on a different surface (mobile/web-to-CLI handoff
    rather than terminal session listing), that the guide's parallel-session
    management section should treat as a second, complementary practitioner
    pattern.

- **Novel**:
  - **The specific mechanism for building trust in automated code review**
    (Claim 5): incident-review PRs are added to a dedicated eval set so that
    future changes to the code-review system are regression-tested against
    every incident that previously slipped through. No prior corpus source
    documents this specific feedback loop.
  - **Per-file code-review confidence thresholds** ("for code changes that
    touch these files, code review is catching 100% of the issues there — so
    we actually don't need a human manually reviewing those") as a named,
    graduated (not binary) trust model for automated review, distinct from
    the binary code-owner/no-code-owner split.
  - **The "10% of cases where it's not true" prompt-auditing heuristic**
    (Claim 3): explicitly auditing each absolute ("always X") system prompt
    instruction for its false-case rate and rewriting it as conditional
    context is a specific, actionable prompt-editing technique not documented
    elsewhere in the corpus.
  - **Per-model-tier system prompts as a shipped, named architecture**
    (Claim 4) — the postmortem note flagged this as a planned change; this
    is the first corpus confirmation that it has shipped, plus the detail
    that the size reduction applies only to frontier models.
  - **Confirmation that Claude Code (not just Claude Tag) exposes the
    credential-injection pattern**, with a named example connector (Datadog)
    (Claim 7).
  - **The tool-cardinality design principle** ("every tool we add has a
    distinct function from every other tool") and the specific example of
    removing dedicated grep/glob tools in favor of native bash (Claim 12) are
    new, concrete harness-design guidance not previously documented in the
    corpus.
  - **The file-edit tool's UI-only justification** (Claim 13) — a concrete,
    named example of a tool whose existence is justified by UX/observability
    needs rather than model capability, useful as a general harness-design
    principle.

## Guide Impact

- **Chapter 02 (Harness Engineering — System Prompt Design)**: Add Claims
  2–4 and 14 as a dedicated "leaner system prompts" section: (a) remove
  examples for frontier-tier models (Claim 2); (b) audit every absolute
  instruction for its false-case rate and rewrite as conditional context
  rather than a hard "don't do X" rule (Claim 3); (c) maintain separate
  system prompts per model tier rather than one universal prompt (Claim 4);
  (d) cite OpenAI's independently-reported quantified gains (10–15% eval
  score, 41–66% token reduction) as cross-vendor corroboration (Claim 14).
  This directly extends the corpus's existing coverage of the April 2026
  Claude Code postmortem's planned model-specific gating with confirmation
  that it has shipped.

- **Chapter 02 (Harness Engineering — Tool Design)**: Add Claim 12 (keep
  tool cardinality low; every tool must have a function distinct from every
  other tool) and Claim 13 (a tool can be justified by UI/observability needs
  alone, independent of model capability) as concrete harness-design
  heuristics, alongside the team's own example of removing dedicated
  grep/glob tools in favor of native bash.

- **Chapter 03 (Safety and Verification — Code Review)**: Add Claim 5's
  specific trust-building mechanism (incident-review PRs feed a regression
  eval set for the code-review system itself) as a concrete pattern for
  teams gradually reducing human-in-the-loop code review. Cross-reference
  the April 2026 postmortem's account of a bug that slipped past every
  verification layer simultaneously as the caveat: automated review trust
  should be treated as continuously regression-tested, not a one-time
  judgment call.

- **Chapter 03 (Safety and Verification — Agent Permissions)**: Add Claim 6
  (auto mode's Sonnet classifier makes prompt-injection/exfiltration risk
  "far lower than the average human reviewer," a comparative not absolute
  claim) as a data point alongside the existing auto mode engineering post's
  quantified FNR/FPR figures, noting the different, narrower comparison
  baseline Cat uses here.

- **Chapter 03 (Safety and Verification — Credential Handling)**: Add Claim
  7's Datadog example as a concrete, named illustration of the
  credential-injection pattern applied to Claude Code specifically (not just
  Claude Tag), extending the existing agent-identity source note's coverage.

- **Chapter 04 (Team Adoption / Organizational Patterns)**: Add Claim 1
  (Claude Tag lands 65% of the Claude Code team's product-engineering PRs,
  precisely scoped to that one team, not Anthropic-wide) and Claim 8 (feature
  shipping gated on an internal active-user/retention bar, not a subjective
  go/no-go call) as concrete organizational patterns. Add Claim 11
  (Willison's own observation that decision latency becomes the bottleneck
  once code production accelerates) as framing for why organizations may
  want to push product-decision authority down to engineers.

- **Chapter 04 (Team Adoption — Rewrites and Migrations)**: Add Claim 9
  ("rewrites are now good"; "a codebase is a spec, and maybe it's the only
  copy of the spec that you have") as a named counter-argument to
  traditional never-rewrite orthodoxy, conditioned explicitly on having a
  good test suite. Pair with the existing Bun Zig-to-Rust rewrite case study
  sources for a fuller picture, and note the independent shipping-date
  corroboration documented above.

## Extraction Notes

- **WebFetch limitation**: The WebFetch tool returned AI-summarized
  paraphrases rather than verbatim text on two separate attempts, even when
  explicitly prompted for verbatim output. All quotes in this note were
  instead extracted from the raw page HTML (fetched via `curl`), stripped of
  markup, and copied character-for-character from that flat-text extraction
  — not reconstructed from either WebFetch summary. This is a more reliable
  method for quote-fidelity per MINER.md §2a and consistent with the
  practice already used in `blog-pragmaticengineer-bun-rust-rewrite.md`.
- **Full source read**: The entire transcript (598 lines of extracted flat
  text, covering all ~24 question segments from "How has what you do
  day-to-day changed" through the closing audience Q&A) was read in full.
  The linked YouTube video was not separately transcribed or watched; per
  Willison's own framing this blog post is "an edited copy of the transcript,"
  so the text is treated as the primary artifact for extraction, consistent
  with MINER.md's text-source extraction path (issue labeled `triaged:text`).
  No other sub-pages were followed — the post is self-contained aside from
  the video, which is a different media type outside this extraction's scope.
- **Speaker attribution discipline**: Two passages that read as if they could
  be claims from Cat or Thariq are explicitly Willison's own editorial
  insertions (his bolded highlights and first-person asides) rather than
  transcript quotes from the interviewees: Claim 11 (the decision-latency
  bottleneck observation) and the parenthetical dating asides (auto mode's
  March 24th public release date; the June 17th Bun-in-Rust shipping date).
  These are flagged explicitly in the relevant claims/artifacts above rather
  than presented as statements by the Claude Code team.
- **Triage comments**: The issue carries three separate Prospector triage
  comments with somewhat different chapter groupings (Ch01/02/04/05
  variously). This note's Guide Impact section synthesizes across all three
  rather than picking one; all four of the Prospector's named extraction
  targets (system prompt optimization, code review/verification, credential
  injection security, organizational decision-velocity bottlenecks) are
  represented above.
- **No contradiction filed**: See Cross-References → Contradicts for the
  reasoning on why the code-review trust claim (Claim 5) versus the April
  2026 postmortem's verification-stack failure does not meet the bar for a
  contradiction issue.
