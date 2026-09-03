---
source_url: https://claude.com/blog/the-anatomy-of-effective-commerce-agents
source_type: blog-post
title: "A guide to the anatomy of effective commerce agents"
author: Ali Shazal and Matthew Koen (Anthropic)
date_published: 2026-09-02
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: settled
issue: "#3187"
---

# A guide to the anatomy of effective commerce agents

> First-party Anthropic production playbook, drawn from a year of deployments
> across retail, marketplaces, travel, entertainment, and telecom, arguing for
> a single agent-loop architecture with skills (not subagents), a frequency-based
> rule for system-prompt-vs-skill placement, concrete latency/caching economics,
> and harness-enforced (not prompt-enforced) safety guardrails for money-moving
> actions — with a public reference implementation at anthropics/commerce-agents.

## Source Context

- **Type**: blog-post (official claude.com/blog, category "Agents," product
  "Claude Platform," published September 2, 2026, ~5 min read time)
- **Author credibility**: Ali Shazal and Matthew Koen, credited as the
  article's authors; acknowledgements name six additional contributors
  (Michael Segner, Rodrigo Olivares, Amandeep Khurana, Aiza Usman, John Lopus,
  and others). This is first-party Anthropic engineering guidance describing
  patterns validated across "several enterprise deployments" over "the past
  year," not a single case study — the article states these agents "are in
  production, and enterprise customers have seen larger carts and more
  efficient seller operations when using them." No independent, non-Anthropic
  verification of the specific metrics (13% fact-recall lift, 90–99% cache
  hit rates) is available; these are vendor-reported internal eval numbers,
  consistent with how this corpus already treats other first-party Anthropic
  engineering posts (e.g. `blog-anthropic-prompt-caching-everything.md`,
  `blog-anthropic-harnessing-claude-intelligence.md`).
- **Scope**: Three explicit parts — Part 1 (architecture: single agent loop,
  skills vs. subagents, system-prompt-vs-skill placement, tool design, UI
  components as tools), Part 2 (latency and cost: turn-reduction, perceived
  latency, prompt caching, model/effort selection), Part 3 (production:
  memory, safety enforcement, evals, multi-team organizational scaling). Does
  NOT cover: model training, pricing tables, non-commerce agent domains in
  depth, or the reference implementation's actual code (only its existence
  and structure are described). Links to two other Anthropic posts it treats
  as prerequisites — "writing effective tools for agents" and an "earlier
  blog post on evals for agents" — neither of which has a source note in this
  corpus yet (checked via `grep -l "writing effective tools\|effective tools
  for agents"` and by filename pattern; none found), and to a GitHub reference
  repo, `anthropics/commerce-agents`, whose actual code was not fetched for
  this extraction (out of scope: MINER.md directs following linked *pages*,
  and a code repository is a different artifact class than a blog sub-page).

## Extracted Claims

### Claim 1: A single agent in a standard agent loop, using skills for per-domain modularity, consistently outperformed both a one-prompt-for-everything design and a subagent-per-domain design across several enterprise commerce deployments
- **Evidence**: First-party comparative claim from cross-deployment
  observation ("In our comparisons across several enterprise deployments").
  No raw numbers or specific benchmark are given — this is a qualitative
  ranking, not a quantified A/B result.
- **Confidence**: settled (stated as consistent, repeated observation across
  multiple production deployments by the vendor building the systems) —
  though note the lack of a specific quantified metric keeps this short of
  "measured" in the way the caching or memory-recall numbers are.
- **Quote**: "In our comparisons across several enterprise deployments, a single agent with skills consistently has outperformed both the one-prompt-for-everything design and the subagent design on quality, and often at a lower cost and latency per task."
- **Our assessment**: This is the article's central architectural thesis and
  the most quotable line for any guide section arguing against
  reflexive multi-agent decomposition for tightly-coupled conversational
  domains. It is scoped explicitly to "a commerce conversation is one
  tightly coupled session across multiple intents and turns" — the guide
  should preserve that scoping rather than generalizing to "subagents are
  worse than skills" universally (see Claim 3, which carves out real
  subagent use cases in the same article).

### Claim 2: Every handoff to a subagent is a state-lossy operation that degrades response quality and costs several times the tokens plus seconds of latency, because the orchestrator (not the subagent) holds the cart, preferences, and conversation history
- **Evidence**: Architectural reasoning about what a subagent handoff must
  reconstruct or lose, stated as a direct mechanism explanation rather than
  a benchmarked figure.
- **Confidence**: settled (mechanism-level architectural claim, consistent
  with independent practitioner incident evidence — see Cross-References)
- **Quote**: "Every handoff to a subagent is a state-lossy operation, which often impacts the quality of the subagent's response and, consequently, the overall response. On top of that, each handoff can cost several times the tokens and adds seconds of latency."
- **Our assessment**: "Several times the tokens" and "seconds of latency" are
  not quantified with specific multipliers or figures, unlike the caching
  section's precise numbers (Claim 9) — treat this as a directional,
  qualitative cost claim rather than a benchmarked one. It is independently
  corroborated by a practitioner incident report (see Cross-References,
  `blog-fowler-garg-orchestrator-tax.md`), which strengthens confidence in
  the mechanism even without shared quantification.

### Claim 3: Subagents earn their place only for narrow, self-contained tasks with their own dedicated context window (e.g., deep-research subagents), or as a full conversational hand-off to a pre-existing domain agent with its own compliance surface — not for mid-task delegation within a commerce conversation
- **Evidence**: Explicit exception-carving in the same section that argues
  against subagent-per-domain design; distinguishes "hand-off" (domain agent
  becomes the user's counterpart) from "delegation" (orchestrator bounces the
  domain agent in and out within a turn).
- **Confidence**: settled
- **Quote**: "Where subagents do earn their place is when the orchestrator can call them as a tool for a narrow or self-contained task that would benefit from its own dedicated context window." … "The distinction is ownership of the conversation. A hand-off makes the domain agent the user's counterpart, while delegation keeps the orchestrator, bouncing the domain agent in and out within a single turn and degrading on every exchange."
- **Our assessment**: This is the load-bearing nuance that keeps Claim 1 from
  overgeneralizing — the article is not "subagents are bad," it's
  "subagents are the wrong tool for tightly-coupled, multi-intent
  conversational domains, and the right tool for narrow self-contained work
  or genuine ownership transfer." The guide should present Claims 1–3
  together, not Claim 1 in isolation.

### Claim 4: The decision rule for system-prompt vs. skill placement is frequency-based: a good starting point is that content relevant to roughly a third or more of traffic goes in the system prompt, and the rest goes in skills, because loading a skill costs a model turn
- **Evidence**: Stated as "a good starting point," explicitly caveated as
  depending on traffic distribution and eval-observed behavior, not a fixed
  law. Illustrated with the reference implementation's actual skill/prompt
  split (shopping agent's prompt: grounding, cart/checkout semantics,
  presentation rules, product search; skills: search-discovery,
  purchase-research, planning-goals, customer-care, memory-personalization;
  merchant skills: performance-insights, catalog-listings,
  inventory-operations, pricing-promotions, marketing-campaigns).
- **Confidence**: settled (as a "starting point" heuristic, explicitly not
  presented as a universal constant)
- **Quote**: "Loading a skill costs a model turn, so anything the agent needs on most turns generally goes in the system prompt." … "A good starting point is that anything relevant to a third or more of your traffic, whether anticipated before launch or observed in production, goes in the system prompt, and the rest goes in skills."
- **Our assessment**: This is the single most concrete, actionable, and
  previously-unquantified rule in the corpus for the system-prompt-vs-skill
  decision — existing corpus notes on skills (`blog-anthropic-context-engineering-claude-5.md`,
  `blog-anthropic-claude-code-skills-lessons.md`) describe qualitative
  criteria (progressive disclosure, don't restate what the model already
  knows) but none give a numeric traffic-share threshold. Also notable: the
  article adds that critical safety/legal/brand rules and key user facts
  (e.g. allergies) *always* go in the system prompt regardless of frequency
  — a hard override on the frequency rule worth preserving in guide text.

### Claim 5: Agent tools should call an organization's existing core systems (search/ranking, cart, inventory, promotions, analytics) rather than reimplementing that logic in the tool layer — the tool boundary is where existing system logic ends and model judgment begins
- **Evidence**: Stated as one of "two points that have mattered most in
  commerce" for tool design, with a worked example (`search_products` should
  return already-ranked results; the model's job is choosing which to show
  and how, not reimplementing ranking).
- **Confidence**: settled
- **Quote**: "The agent's tools should call those systems, not reimplement them, and the tool boundary is where their logic ends and the model's judgment takes over."
- **Our assessment**: A specific, checkable anti-pattern warning — the article
  separately warns (in the "faster tools" latency section) that this
  boundary tends to erode in practice: "we often see the tool boundary
  become the place where missing backend logic gets stitched together"
  (an availability-check tool absorbing catalog + inventory + fulfillment +
  substitution-rule logic that should live in a backend endpoint instead).
  Worth pairing both halves of this claim in the guide: state the principle,
  then name the concrete failure mode of violating it.

### Claim 6: Tool results should return only the fields the model reasons with, dropping unnecessary data (e.g., image URLs on every search row), reshaping raw backend responses inside the tool, and replacing generic error codes with actionable instructions
- **Evidence**: Stated as the second of the "two points that have mattered
  most" for tool design, with a concrete before/after example (a generic
  403 replaced with the instruction "Include a product ID when querying
  availability").
- **Confidence**: settled
- **Quote**: "Tool results are context. Return the fields the model reasons with and drop the rest. Image URLs on every search row are the usual offender."
- **Our assessment**: This generalizes past commerce — "tool results are
  context" is a compact, quotable framing for any tool-design guidance in
  the guide's harness-engineering material, and the error-code-to-instruction
  substitution is a specific, immediately actionable pattern distinct from
  generic "handle your errors" advice.

### Claim 7: Since most commerce agent responses are UI components rather than prose, the pattern that holds up at scale is making each UI component a tool call (e.g. `present_products`, `present_itinerary`, `present_plan_comparison`) rather than prompting the model to emit custom tags parsed client-side
- **Evidence**: Explicit comparison against the custom-tag approach, with
  three named failure modes of that approach (reliability drops as nested
  components are added since the model is better trained on tool calls than
  custom markup; every new component bloats the system prompt and risks
  regressions; conversation history becomes unparseable outside a
  custom client parser). The tool-call approach's benefit: components are
  already in the messages array in native format, so history reload needs
  no re-parsing, and the last presentation call's arguments give the agent
  a record of "what's on screen" so references like "the first hotel"
  resolve correctly — provided the arguments are structured the way the UI
  is structured (ordered rows/carousels).
- **Confidence**: settled, with one explicitly named tradeoff: "the
  tradeoff is streaming granularity" — each top-level tool-call argument
  buffers server-side for schema validation before streaming, which can be
  bypassed with `eager_input_streaming: true` at the cost of losing the
  server-side schema guarantee (the article reports schema violations as
  "very rare on Claude Sonnet-class models and up" but recommends wrapping
  the call in a retry for when one slips through).
- **Quote**: "The pattern that has held up is to make each UI component a tool. The model calls present_products, present_itinerary, or present_plan_comparison with typed arguments; your server validates and enriches the call and emits an event; and your client renders it."
- **Our assessment**: This is a concrete, named, previously undocumented (in
  this corpus) architectural pattern for agent-driven UI, complete with a
  specific escape-hatch flag (`eager_input_streaming`) and its explicit
  cost. Worth extracting as a standalone pattern for any guide section on
  agent-to-UI integration, distinct from general tool-design advice.

### Claim 8: Task completion latency is the sum, over model turns, of time-to-last-token plus tool processing, giving three levers — fewer turns, faster tools, faster tokens — that sometimes compete, so the sum should be minimized rather than any single lever
- **Evidence**: Stated as the organizing framework for the entire latency
  section, with concrete named techniques under each lever: fewer turns
  (pre-loading likely context from the page the user arrived from,
  increasing model intelligence, parallel tool calls); faster tools
  (fixing backend logic that's leaked into the tool layer, and eager tool
  dispatch — executing each tool as its arguments finish streaming rather
  than waiting for the full turn); faster tokens (choosing model/config by
  eval sweep, covered in Claim 10).
- **Confidence**: settled, with one quantified figure for eager dispatch:
  "We've seen this take multi-second gaps down to a few hundred
  milliseconds, and the Claude Agent SDK does it by default."
- **Quote**: "Task completion latency is the sum, over model turns, of time to last token plus tool processing. That gives you three levers to work towards: fewer turns, faster tools, and faster tokens."
- **Our assessment**: The article explicitly argues, before presenting these
  techniques, that outcome quality (not marginal latency) is what moves
  retention/engagement/cart-size metrics — "what we have consistently seen
  move metrics like retention, engagement, and cart size is the quality of
  the outcome" — so this latency framework should be read as "don't spend
  intelligence to get speed," not "speed trumps quality." Worth preserving
  that framing alongside the levers themselves.

### Claim 9: Prompt caching economics for high-volume commerce traffic: cached input reads cost a tenth of fresh reads, cache-writes carry a ~1.25x premium (paid back on second use), and the best commerce deployments run at 90–99% cache hit rates by ordering requests into three segments (global/system-prompt, session/per-user, volatile/current-turn) from least to most frequently changing
- **Evidence**: Specific first-party cost/speed figures plus an explicit
  three-segment caching architecture with placement rules for each segment
  (global segment gets a cache breakpoint at its end and must stay
  byte-identical across turns/sessions; volatile content like timestamps
  goes at the very end of the request, never at the top of the system
  prompt, which the article names as "the most common mistake we see").
- **Confidence**: settled
- **Quote**: "Cached input token reads cost a tenth of fresh ones, and while cache-writes carry a premium of roughly 1.25x, a cached prefix pays for itself on its second use." … "The best commerce deployments we've seen run at 90–99% cache hit rates, and that is the range to design for from the start."
- **Our assessment**: The 90–99% hit-rate figure and the "cached reads
  1.5–2x faster at ~100k tokens" figure are the same order of magnitude as
  other first-party Anthropic caching guidance already in the corpus (see
  Cross-References), which increases confidence this is a stable,
  cross-product characteristic of Claude's caching rather than a
  commerce-specific artifact. Two implementation details worth preserving
  precisely: skills should load as tool results (not system-prompt
  appends) so their bodies land in the cached conversation prefix, and
  cache breakpoints should roll forward each turn to the end of the newest
  user turn (a request allows only a limited number of breakpoints).

### Claim 10: Model and effort-level selection should be driven by sweeping the full eval suite across every candidate model/effort combination and measuring cost per completed task (not cost per model call), rather than assuming a larger model is always better
- **Evidence**: Stated as a three-step process (pick metric and floor; sweep
  the eval suite across every model/effort level, weighted by real query
  mix if available; read results carefully for two named surprises — prompts
  tuned to one model can underperform on another, and a more intelligent
  configuration sometimes wins even on p90/p99 latency despite slower
  per-token speed, because it needs fewer rounds). Gives directional
  starting points (Opus for analysis-heavy merchant agents, Sonnet for
  latency-sensitive consumer agents) but frames these as starting points to
  verify by sweep, not conclusions.
- **Confidence**: settled
- **Quote**: "Sweep. Run your entire eval suite across every model and effort level you'd consider." … "Sometimes Opus 5's lift on cart-driving tasks justifies the cost difference over Sonnet, and sometimes it doesn't." … "Measure cost per completed task rather than per model call, since a cheaper model that needs more turns, or fails more often, is not cheaper."
- **Our assessment**: This corroborates and sharpens existing corpus guidance
  on model selection (see Cross-References) with a commerce-specific
  starting heuristic (Opus for merchant/analysis, Sonnet for
  consumer/latency) that neither prior source states, while preserving the
  same underlying "measure, don't assume" methodology.

### Claim 11: Long-term memory belongs in an organization's own systems (a database of small typed fact records), not in the model's context or a flat markdown profile — the latter works only while profiles are small and the agent is the sole reader
- **Evidence**: Direct architectural prescription, with a specific record
  shape (key, short value, category, source session) and a four-part
  data-handling framework specific to memory holding regulated personal
  data: decide retainable memory types and enforce at the write path; give
  users visibility/correction/deletion tied into account-deletion flows; set
  a retention period; make memory a per-deployment on/off switch for regions
  that can't take on the handling obligations. Also specifies that
  merchant-facing agents should key memory by individual operator, not
  shared account login, respecting each operator's permission scope.
- **Confidence**: settled
- **Quote**: "Memory belongs in your systems, not in the model." … "A fact is a small typed record: a key (such as shoe_size, default_store, preferred_report_cadence), a short value, a category, and the session it came from."
- **Our assessment**: This is a specific, opinionated architectural claim
  (database over markdown/context) distinct from the consumer-product
  memory design covered elsewhere in the corpus (see Cross-References,
  `blog-anthropic-memory-works-everywhere.md`) — that source describes a
  settings-UI topic-file store for chat/Cowork; this source describes a
  developer-owned database for a production commerce agent. Both converge
  on "memory as discrete, inspectable records" as a design philosophy, but
  for different product surfaces and audiences (end-user-editable UI vs.
  developer-owned schema with a validator on the write path).

### Claim 12: Writing memory asynchronously (a separate thread/process reads the conversation after each turn or every few turns) adds no conversation latency and achieved 13% higher fact recall than the alternative of a synchronous tool the agent calls mid-turn to save a fact
- **Evidence**: Internal eval-suite comparison ("our internal commerce memory
  eval suite"), plus a mechanism explanation for why the synchronous
  tool-call alternative underperforms: every save becomes a latency-costing
  turn, an update/dedupe often needs a read first, and the extra decision
  competes for the model's attention on every turn — which the article
  states "showed up as missed memories" in their evals.
- **Confidence**: settled, single-source (internal eval suite, not
  independently reproduced)
- **Quote**: "Write memory asynchronously." … "It adds nothing to the conversation's latency, and achieved 13% higher fact recall on our internal commerce memory eval suite."
- **Our assessment**: The 13% figure is the article's only precisely
  quantified quality metric tied to a specific architectural choice (versus
  the more qualitative "consistently outperformed" language elsewhere), and
  is worth flagging in the guide as vendor-internal-eval-sourced rather than
  independently benchmarked. The mechanism argument (separating the
  extractor lets it be prompted narrowly — reading only user/assistant text,
  never tool results, "so a product description or a review can't become a
  fact about the user") is a specific, reusable prompt-injection-adjacent
  design detail: it prevents third-party or catalog content read via tools
  from contaminating the user-fact store.

### Claim 13: Financial and business-state-changing actions must be staged by the model and applied by a person or policy through code the harness controls — no model tool call directly moves money or changes the business
- **Evidence**: Explicit architectural rule with two concrete implementations:
  on the consumer side the checkout tool renders a cart with a placement
  button and "the backend interface the agent calls has no charge method at
  all"; on the merchant side every write tool produces a staged change with
  a server-generated ID, and `apply_change` succeeds only for IDs approved
  through a real approval surface (operator portal button, CLI
  confirmation, or a Managed-Agents tool-approval prompt) — re-checked
  against current limits at apply time, not the limits in force when staged.
- **Confidence**: settled
- **Quote**: "No model tool call moves money or changes the business. Order placement, payments, refunds, price changes, and campaign launches all end in an action the harness controls instead of the model."
- **Our assessment**: This is the article's clearest single safety
  principle and the most guide-quotable line for any "safety belongs in
  code, not prompts" section — the explicit reasoning given is that "a
  prompt rule is one injection or one bad sample away from being skipped,"
  which is a sharper articulation of the general prompt-injection risk than
  a generic warning. The re-check-limits-at-apply-time detail (not
  limits-at-staging-time) is a specific, easy-to-miss implementation detail
  worth preserving — a naive implementation that checks limits only once,
  at staging, would be vulnerable to limits changing between staging and
  approval.

### Claim 14: Writes and renders must accept only server-issued IDs — any ID that arrived by another path (model hallucination, user-pasted text, or content planted in a review) is refused before it reaches the backend — and per-session write caps must be enforced against the resulting state and serialized, so repeated or parallel requests cannot stack past a limit
- **Evidence**: Two paired mechanism descriptions: (1) the harness keeps a
  per-session record of every ID the server has handed the model, and that
  record is the sole accepted key for any write or render, including
  presentation-tool renders (the server fills in product/order/change
  records itself) and subagent delegates (a merchant analysis subagent can
  read data but never adds to the writable ID set); (2) transaction/price/
  discount/restock/campaign-budget caps are enforced "on the line as it
  would be after the write" rather than against the request in isolation,
  and writes for one session are serialized so parallel tool calls in a
  single turn cannot combine to exceed a cap.
- **Confidence**: settled
- **Quote**: "The harness keeps a per-session record of every ID the server has handed the model, and that record is the only key any write or render will accept." … "The rule generalizes: enforce every limit on the resulting state rather than the request, and serialize writes per session."
- **Our assessment**: This is a specific, implementable defense against two
  distinct attack/failure classes at once: ID injection (via hallucination
  or adversarial content) and cap evasion via retry/parallelism (an agent
  "will retry, rephrase, and parallelize in ways a human clicking a button
  never did" — a sharp framing of why agent-driven UIs need stricter
  server-side enforcement than human-driven ones, even when the underlying
  business rule is identical).

### Claim 15: Every tool result authored by a third party (listings, reviews, policies, seller messages, stored memory) is sanitized and wrapped in a fence with a fixed label before the model sees it, with the sanitizer stripping control/bidirectional characters, defusing text that imitates fence markers or conversation/tool-call turns, and capping content size
- **Evidence**: Explicit sanitizer specification, paired with a
  complementary prompt-side rule: fenced text is framed to the model as
  "material to report on, never to act on."
- **Confidence**: settled
- **Quote**: "Every tool result authored by a third party, such as listings, reviews, policies, seller messages, and stored memory, is sanitized and wrapped in a fence with a fixed label before the model sees it." … "The prompt carries the other half of the contract: fenced text is material to report on, never to act on."
- **Our assessment**: This is a concrete, two-part (code + prompt) mitigation
  for data-plane prompt injection via commerce content — sellers, reviewers,
  and competitors are explicitly named as untrusted-input sources ("most of
  the context is written by people who aren't you"). The article later
  reinforces this is tested, not just designed: its evals section requires
  splitting injection test cases into "user-authored injection" and
  "data-plane injection... planted in product names, reviews, or web
  snippets that arrive via tool results" (see Claim 16), so the defense and
  its test coverage are described as a matched pair.

### Claim 16: Evals for commerce agents should be snapshot-based (construct test state directly, append a test message, grade the final state and rendered response) rather than simulated-user conversations, cover five specific categories including a mandatory negative case for every positive case, and draw 50–100 cases per user flow starting from real production failures
- **Evidence**: Explicit methodology comparison (simulated user + judge model
  called "a poor tool for measurement" because "two non-deterministic
  systems interacting need larger samples, cost more per trial, are harder
  to judge" — relegated to coverage-gap discovery and "a general vibe
  check," not measurement) plus a named five-category coverage list: core
  requests, context-dependent requests (including memory), safety and brand
  cases (split into user-authored vs. data-plane injection), interface
  evaluations, and requests spanning multiple capabilities at once (a named
  gap: "evals written per capability won't catch this, because each grades
  only its own half").
- **Confidence**: settled
- **Quote**: "Evaluate snapshots, not conversations" … "Simulated-user evals, in which a second model plays the user and a judge grades the whole conversation, are a poor tool for measurement." … "For every positive case, write its negative counterpart: a 'should serve' for every 'should refuse,' a 'should just do it' for every 'should ask.' Missing negatives are the most common gap we find in a suite." … "Real failures make the best evals, and 50-100 eval cases per user flow is a good starting point."
- **Our assessment**: The explicit case against simulated-user evals as a
  *measurement* tool (vs. a discovery tool) is a specific, actionable
  methodology stance — not just "write more evals," but a ranked preference
  between two named eval architectures with named reasons (sample size,
  per-trial cost, judgeability, attribution difficulty). The
  multi-capability-boundary category (a request needing two skills' answers
  combined, e.g. "if I mark this down 15%, do I have enough stock to cover
  the demand?") names a specific coverage gap — per-skill eval suites
  structurally cannot catch it because each suite only grades its own
  half of a combined answer.

### Claim 17: In large organizations, each skill and tool should have a single owner team, CI should run a curated subset (core high-traffic + all safety cases, plus cases touching the specific change) rather than the full suite on every pull request, and prompt/skill changes should roll out via canary cohort with a per-skill kill switch and pre-peak freezes
- **Evidence**: Explicit organizational process description, framed as an
  alternative to the "tempting fix" of splitting the system into
  one-subagent-per-business-unit (explicitly rejected, cross-referencing
  Part 1's architecture argument: "As discussed in Part 1, we recommend
  against it for quality reasons"). Full-suite runs are relegated to nightly
  and pre-release, not per-PR. Gating criteria named: pass rate over
  multiple trials, cache hit rate, and cost per turn.
- **Confidence**: settled
- **Quote**: "Every skill and tool has a single owner team." … "Running the full suite on every pull request is too slow and too expensive to survive, so build a CI set from it instead." … "Roll prompt and skill changes to a canary cohort first, keep a switch that turns off one skill without a deploy, and freeze the agent ahead of peak periods the same way you freeze other systems."
- **Our assessment**: This is the article's answer to a structural problem it
  states plainly: "Unlike a service, an agent has no strict module boundary
  protecting the others: a change made by the pricing team shares a context
  window with checkout." That framing — a single shared context window as
  the reason agents can't be organizationally decomposed the way
  microservices can — is a distinct, transferable argument connecting this
  section back to Claim 1's single-agent architecture choice; multi-team
  ownership of one shared agent, not one agent per team, is presented as the
  direct organizational consequence of the architecture decision made in
  Part 1.

## Concrete Artifacts

### Reference implementation's system-prompt vs. skills split (verbatim, "In the prompt" / skills callout boxes)
```
Source: claude.com/blog/the-anatomy-of-effective-commerce-agents, "System prompt or skill: decide by frequency"

In the prompt — Shopping agent:
  Grounding, cart and checkout semantics, presentation rules, and product search.

Shopping skills — The long tail:
  search-discovery · purchase-research · planning-goals · customer-care · memory-personalization

Merchant skills — One per operational domain:
  performance-insights · catalog-listings · inventory-operations · pricing-promotions · marketing-campaigns
```

### Three-segment prompt-caching request structure (verbatim mechanism description)
```
Source: claude.com/blog/the-anatomy-of-effective-commerce-agents, "Prompt caching"

Global: most of the system prompt and tool definitions, identical across every
  session. Warmest cache; at scale will likely not expire. Keep byte-identical
  across turns and sessions; put a cache breakpoint at its end.

Session: per-user context and conversation history — differs across sessions,
  stable within one. Comes after the global segment.

Volatile: anything that changes within a session (current time, current page).
  Goes at the very end of the request — as a tagged block in the newest user
  turn, or (on models supporting mid-conversation system messages) as a
  system-role message appended to the messages array.

"The most common mistake we see is a timestamp or the current page at the top
of the system prompt, which silently breaks the cache on every request."

Implementation notes:
- Skills should load as tool results, not appended to the system prompt, so
  the skill body lands in the (cached) conversation prefix.
- Roll cache breakpoints forward each turn — move the newest breakpoint to
  the end of each user turn, since a request allows a limited number of
  breakpoints.
```

### Four memory data-handling obligations (verbatim, numbered in source as an unordered list)
```
Source: claude.com/blog/the-anatomy-of-effective-commerce-agents, "Storing memories"

- Decide which types of memories you are willing to hold. Enforce that at
  the write path, with a validator that every save goes through, rather than
  in the prompt alone.
- Give users a way to see, correct, and delete what is stored. Wire deletion
  into your account-deletion and data-request flows.
- Set a retention period. A preference from a few years ago is likely to be
  outdated, so a retention period helps keep memory facts fresh.
- Memory should be a per-deployment switch. This allows regions that can't
  take on these obligations to run without it.
```

### Five eval coverage categories (verbatim category names, source's own bullet list)
```
Source: claude.com/blog/the-anatomy-of-effective-commerce-agents, "Cover the different types of commerce agent evals"

- Core requests that make up the bulk of your traffic
- Context-dependent requests (references to what's on screen, carried-over
  constraints, writes against an existing cart; includes memory evaluation)
- Safety and brand cases (injection — split into user-authored vs.
  data-plane injection — unauthorized data access, regulated language
  checked byte for byte)
- Interface evaluations (right component rendered, item caps respected, no
  internal identifiers in user-facing text, timeouts/empty results)
- Requests that belong to multiple capabilities at once (graded on both
  halves of the combined answer; per-capability eval suites structurally
  cannot catch these)
```

### Article structure / table of contents (verbatim heading list, "In this guide")
```
Source: claude.com/blog/the-anatomy-of-effective-commerce-agents

Part 1: The architecture
  - What is a commerce agent?
  - Skills, not subagents
  - System prompt or skill: decide by frequency
  - Engineering agent tooling
  - The UI components are tools
Part 2: Making it fast and affordable
  - Minimizing task completion latency
  - Perceived latency
  - Prompt caching
  - Choosing the model and its configuration
Part 3: Running it in production
  - Memory that survives the session
  - Safety: enforcement lives in the harness
  - Evals: shipping a non-deterministic system
  - Shipping with a large organization
Looking ahead
```

## Cross-References

- **Corroborates**:
  - `blog-fowler-garg-orchestrator-tax.md` Claim 8 ("the orchestrator is the
    only part of the system that accumulates understanding across a long
    session... subagents... are supposed to be disposable. Exploration,
    repeated file reads, failed approaches, and noisy intermediate reasoning
    are meant to stay in worker contexts and never make the trip back to the
    main thread") — an independent practitioner incident (a .NET refactor
    session) arrives at the same containment-not-specialization view of
    subagent value that this source's Claim 2/3 state from a vendor,
    cross-deployment perspective. Together: one vendor source (broad,
    unquantified) and one single-incident practitioner source (narrow,
    self-flagged as anecdotal) converge on subagents being justified by
    context isolation for narrow work, not by role-based task splitting.
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 6 ("Sub-agents
    work as a 'context firewall' for isolating discrete tasks in separate
    context windows, but role-based specialization (frontend/backend/
    data-analyst sub-agents) does not work") — directly corroborates this
    source's Claim 1/Claim 3 distinction between subagents-for-narrow-
    isolated-work (endorsed) and subagents-as-domain-specialists
    (rejected), from an independent practitioner source in a different
    domain (general coding agents, not commerce).
  - `blog-anthropic-choosing-claude-model.md` Claim 2 ("Cost-per-task is
    often lower for more intelligent models even when their price-per-token
    is higher, because capable models need fewer turns and less thinking
    time") and Claim 9 ("Anthropic recommends custom evaluations over
    standard benchmarks specifically when comparing powerful models...
    because those models can solve nearly all questions on a standard
    benchmark") — both corroborate this source's Claim 10 (sweep your own
    eval suite across models/effort levels; measure cost per completed
    task, not per call). This source adds a commerce-specific starting
    heuristic (Opus for merchant/analysis-heavy agents, Sonnet for
    latency-sensitive consumer agents) not present in either prior source.
  - `blog-anthropic-prompt-caching-everything.md` Claim 3 ("'Static content
    first, dynamic content last' is the foundational rule for prompt
    structure under prefix caching") — corroborates this source's Claim 9
    three-segment ordering (global → session → volatile), which is a more
    granular, commerce-specific elaboration of the same static-first rule,
    including the same named anti-pattern (a timestamp at the top of the
    system prompt breaking the cache).

- **Contradicts**: None identified. Checked specifically against
  `blog-anthropic-multi-agent-coordination-patterns.md`,
  `blog-latentspace-ainews-zawinskis-law-multiagents.md` (a different domain
  — agent-to-agent messaging infrastructure trends across separate agents,
  not intra-conversation subagent orchestration for one assistant — not a
  real disagreement, just a different context), and
  `blog-anthropic-choosing-claude-model.md` (that source's "default to the
  most intelligent model" framing and this source's "sweep and measure,
  starting point varies by agent type" framing are complementary starting
  heuristics under the same underlying eval-driven methodology, not opposed
  positions — no contradiction issue filed per MINER.md §4a).

- **Extends**:
  - `blog-anthropic-context-engineering-claude-5.md` and
    `blog-anthropic-claude-code-skills-lessons.md` (existing corpus guidance
    on skills design — progressive disclosure, avoid restating what the
    model already knows, keep skills lightweight) — this source adds a
    numeric decision rule (≈1/3 traffic threshold) for *when* content
    belongs in the system prompt vs. a skill in the first place, which
    neither prior source quantifies.
  - `blog-anthropic-memory-works-everywhere.md` (Claims 1, 3, 4 — the
    consumer chat/Cowork topic-file memory product) — both sources converge
    on "memory as discrete, inspectable, editable records" as a design
    philosophy, but for different product surfaces: that source describes
    an end-user-facing Settings UI for consumer chat; this source describes
    a developer-owned database with a write-path validator for a production
    commerce agent. The guide should treat these as structurally similar
    but organizationally distinct memory systems, consistent with how
    `blog-anthropic-memory-works-everywhere.md`'s own Cross-References
    section already treats its relationship to
    `blog-anthropic-claude-managed-agents-memory.md`.

- **Novel**: The server-issued-ID-only write/render acceptance pattern
  (Claim 14); enforcing caps against resulting state rather than the
  request, combined with per-session write serialization, as a defense
  against agent-specific retry/parallelism cap evasion (Claim 14); the
  third-party content fencing/sanitization contract paired with matching
  data-plane-injection eval coverage (Claims 15–16); the
  snapshot-vs-simulated-user eval methodology with simulated-user evals
  explicitly demoted to a discovery-only role (Claim 16); the
  multi-capability-boundary eval category naming a specific structural gap
  in per-skill eval suites (Claim 16); the UI-components-as-tools pattern
  with the `eager_input_streaming` streaming/schema-guarantee tradeoff
  (Claim 7); and the CI test-subsetting strategy (core + safety + changed
  cases per PR, full suite nightly/pre-release) for multi-team ownership of
  a single shared agent (Claim 17) are all new to this corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claims 1–3 (skills over
  subagents for tightly-coupled conversational domains, with the narrow-task/
  hand-off exception) as a named counterpoint to any existing "when to use
  subagents" guidance, explicitly scoped to tightly-coupled multi-intent
  conversational agents rather than generalized to all agent domains. Add
  the ~1/3-traffic-share heuristic (Claim 4) as a concrete, numeric addition
  to the existing progressive-disclosure/skills-design guidance sourced from
  `blog-anthropic-context-engineering-claude-5.md` and
  `blog-anthropic-claude-code-skills-lessons.md`, which currently lack any
  quantified placement rule. Add the tool-design principles (Claims 5–6:
  call core systems rather than reimplementing logic; return context, not
  clutter; replace error codes with instructions) as concrete guidance
  distinct from the existing `blog-anthropic-harnessing-claude-intelligence.md`
  material on familiar tools.

- **Chapter 04 (Context Engineering / Agents & Multi-turn)**: Add the
  three-segment prompt-caching model (Claim 9, Concrete Artifacts) as a
  commerce-domain elaboration of the existing static-first/dynamic-last
  caching guidance, with the specific economics (1/10 cost, 1.25x write
  premium, 90–99% hit-rate target) as a benchmark practitioners can compare
  their own deployments against. Add the memory architecture (Claims 11–12:
  database-backed typed facts, async extraction, three-layer read model) as
  a production-scale counterpart to the consumer topic-file memory already
  documented via `blog-anthropic-memory-works-everywhere.md` — explicitly
  as two different systems for two different product types, not a single
  evolving memory feature.

- **Chapter 03 (Verification)**: Add the snapshot-vs-simulated-user eval
  methodology stance (Claim 16) as a specific, argued position — simulated-
  user evals are a discovery tool, not a measurement tool — with named
  reasons (sample size, cost, judgeability, attribution). Add the five eval
  categories and the mandatory-negative-case rule (Claim 16, Concrete
  Artifacts) as a concrete checklist, and the 50–100-cases-per-flow starting
  point sourced from real production failures.

- **Chapter 05 (Building AI-Native Applications / Team Adoption)**: Add
  Claim 17 (single owner per skill/tool, CI test-subsetting instead of full-
  suite-per-PR, canary rollout with a per-skill kill switch) as a concrete
  organizational pattern for teams scaling one shared agent across multiple
  owning teams, paired with the article's stated reason a shared agent can't
  be decomposed like microservices: "an agent has no strict module boundary
  protecting the others: a change made by the pricing team shares a context
  window with checkout." Add Claims 13–15 (harness-enforced safety: staged
  changes with human/policy approval, server-issued-ID-only writes, capped-
  transaction serialization, third-party content sanitization) as a
  concrete guardrail checklist for any guide section on deploying
  money-moving or business-state-changing agents to production.

## Extraction Notes

- WebFetch's default summarizing pass on this URL returned only a
  condensed, paraphrased summary and then explicitly refused longer verbatim
  reproduction on subsequent targeted prompts, citing copyright caution (a
  pattern already documented in this corpus, e.g.
  `blog-fowler-garg-orchestrator-tax.md` and
  `blog-cognition-multi-agents-working.md` Extraction Notes). Per that
  precedent, the full article was instead fetched via `curl` with a browser
  user-agent, stripped of HTML markup with a small script, and read in full
  (all three parts, all named sections, the acknowledgements, and the "In
  this guide" table of contents). Every `Quote` field above was copied
  character-for-character from that raw-text extraction, including its
  Unicode curly-apostrophe/en-dash usage where the source uses them (e.g.
  "subagent's response" uses a curly apostrophe in the source).
- The article links to two other Anthropic blog posts it treats as
  prerequisite reading ("writing effective tools for agents" and an "earlier
  blog post on evals for agents") and to a GitHub reference implementation
  (`anthropics/commerce-agents`). Neither prerequisite post has a source
  note in this corpus yet (grepped by filename pattern and by quoted phrase
  — no match); both are flagged here as candidates for future separate
  source submissions, since they are described as covering "tool design in
  general" and "the general practice" of agent evals respectively — likely
  substantive, general-purpose sources beyond this commerce-specific
  extension of them. The GitHub repository's actual code was not fetched;
  MINER.md's "follow up to 5 linked pages" guidance is scoped to substantive
  linked *pages*, and a full code repository is a different artifact class
  better suited to a separate, dedicated extraction if the Prospector queues
  it.
- No contradiction meeting the MINER.md §4a bar was identified against the
  existing corpus (see Cross-References → Contradicts); none filed.
- The source's specific quantified metrics (13% fact-recall lift, 90–99%
  cache hit rates, "several times the tokens" for subagent handoffs) are
  vendor-reported internal figures from Anthropic's own deployments and
  eval suites, not independently reproduced benchmarks — flagged per-claim
  above rather than discounting the whole source, consistent with how this
  corpus treats other first-party Anthropic engineering posts with internal
  metrics.
