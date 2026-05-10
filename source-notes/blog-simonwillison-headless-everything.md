---
source_url: https://simonwillison.net/2026/Apr/19/headless-everything/
source_type: blog-post
title: "Headless everything for personal AI"
author: Simon Willison (aggregating Matt Webb, Marc Benioff/Salesforce, Brandur Leach)
date_published: 2026-04-19
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#422"
---

# Headless everything for personal AI

> Simon Willison's link-blog post aggregates three converging signals — Matt Webb's
> architectural argument for headless services, Marc Benioff's Salesforce Headless 360
> announcement, and Brandur Leach's second-wave API thesis — into a single pattern:
> SaaS services must expose CLI/API interfaces for AI agents or risk being bypassed,
> with API availability becoming a decisive competitive differentiator as the industry
> emerges from an "API winter."

## Source Context

- **Type**: blog-post (Simon Willison link-blog format — a short aggregating post
  that surfaces and frames three external sources: Matt Webb's post at
  `https://interconnected.org/home/2026/04/18/headless`, Marc Benioff's tweet at
  `https://twitter.com/benioff/status/2044981547267395620`, and Brandur Leach's post
  at `https://brandur.org/second-wave-api-first`. The primary claims come from these
  three sources, framed by Willison. All three linked sources were fetched and read
  for this extraction.)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI;
  one of the highest-signal commentators on LLM tooling. Matt Webb is an independent
  technologist/inventor with a track record of early architectural pattern recognition.
  Brandur Leach is a senior engineer (formerly Stripe) with API infrastructure
  expertise. Marc Benioff is Salesforce CEO — his quote carries vendor-commitment
  weight rather than analytical authority. The combination of analyst (Webb, Leach)
  + vendor (Benioff) + curator (Willison) gives this cluster unusual signal density.
- **Scope**: Covers the broad architectural question of how SaaS services should
  expose interfaces for AI agent access, plus a historical thesis on why the first API
  wave failed and why the second wave (driven by AI agent demand) is structurally
  different. Does NOT cover implementation specifics (how to build headless services),
  pricing model mechanics in depth, or browser/GUI automation as a viable long-term
  alternative. The Matt Webb source follows up to 5 linked sub-pages not followed here
  except as referenced in the main post.

## Extracted Claims

### Claim 1: Using personal AIs gives users a better experience than using services directly, and headless APIs are faster and more dependable for agents than GUI automation

- **Evidence**: Matt Webb's direct argument in his April 18, 2026 post. First-person
  analytical claim from a practitioner who works on ambient/connected computing.
- **Confidence**: emerging (one practitioner's analytical claim; well-reasoned but
  not backed by controlled benchmarks)
- **Quote**: "using personal AIs is a better experience for users than using services
  directly (honestly); and headless services are quicker and more dependable for the
  personal AIs than having them click round a GUI with a bot-controlled mouse."
- **Our assessment**: This is the core thesis driving the headless-first pattern.
  "Quicker and more dependable" than GUI automation aligns precisely with Anthropic's
  own stated hierarchy in `blog-anthropic-dispatch-computer-use.md` (Claim 1 there:
  "Claude will reach for the most precise tool first, starting with connectors...when
  there isn't a connector, Claude can directly control your browser, mouse, keyboard").
  Webb provides the market-level explanation for WHY this hierarchy exists — it is not
  just a technical preference but a user-experience and reliability reality. GUI
  automation's unreliability is the failure mode headless APIs are designed to prevent.

### Claim 2: CLIs have a smaller attack surface and are easier to secure than full GUI applications, making them appropriate for AI agent access

- **Evidence**: Matt Webb's argument in the same post. Security claim based on
  architectural simplicity reasoning.
- **Confidence**: emerging (a reasonable security argument but not benchmarked;
  stated as Webb's inference from the security posture of CLI vs. GUI systems)
- **Quote**: "CLIs are smaller than regular apps and so they are easier to secure."
- **Our assessment**: The claim is architecturally sound — fewer code paths, no
  rendering engine, no JavaScript engine = smaller attack surface. Webb cites as
  supporting evidence a claim that Anthropic's "Mythos model" is "so good at
  discovering security flaws that it has been held back from the public and governments
  are convening emergency meetings," implying AI agents will actively probe the surfaces
  they're given. The Mythos claim is anecdotal and unverifiable; the core security
  argument (smaller = easier to harden) is conventional wisdom in security engineering.

### Claim 3: CLIs are composable in ways that GUI apps are not, enabling AI agents to chain across multiple services in a single workflow

- **Evidence**: Matt Webb's argument. Compositional property of CLIs traced to their
  Unix heritage.
- **Confidence**: emerging (analytical claim; composability is a design property, not
  a measurement)
- **Quote**: "you can: query your notes then jump to a spreadsheet then research the
  web then jump back to the spreadsheet then text the user a clarifying question then
  double-check your notes, all by bouncing between CLIs"
- **Our assessment**: This quote captures the "multi-service agent workflow" pattern
  that is central to agentic harness design. CLIs compose naturally because they take
  stdin/stdout; apps enforce "user journeys" that are linear and non-composable. The
  practical implication for harness engineers: design external service access as CLI
  invocations or API calls with clean I/O, not as GUI automation sequences. Webb's
  framing inverts the traditional design priority: composability for agents is what
  ease-of-use was for human users.

### Claim 4: Traditional app design around "user journeys" is incompatible with how AI agents actually work — agents multitask across services, not along linear paths

- **Evidence**: Matt Webb's conceptual argument about design paradigms.
- **Confidence**: anecdotal (one analyst's observation; emerging practitioner pattern)
- **Quote**: "apps and their user journeys are not composable"
- **Our assessment**: "User journey" as a design concept assumes a human following
  a linear flow through a single service. AI agents don't follow journeys — they
  jump between services dynamically based on task requirements. This framing has
  direct implications for how practitioners should evaluate third-party service
  integration options: prefer services with CLI/API access to services that assume
  a GUI-navigated workflow.

### Claim 5: Frontend design will shift from optimizing for ease-of-use to optimizing for brand, as AI agents displace direct human interaction with service UIs

- **Evidence**: Matt Webb's prediction. Includes the supporting claim that services
  are not fungible — users will still choose which services to trust their AI to use,
  so brand matters.
- **Confidence**: anecdotal (speculative forecast; no empirical evidence cited)
- **Quote**: "front-end design for apps and services optimising for brand rather than
  ease of use"
- **Our assessment**: This is a longer-horizon prediction rather than an immediately
  actionable pattern. The underlying logic is sound: if AI agents mediate service
  interactions, human-facing UX quality becomes less important than API quality and
  brand trust. The "services are not fungible" observation is the key check: commodity
  services (where any provider works) face the strongest pressure to compete on API
  quality; differentiated services (where brand matters) may maintain GUI-first design
  longer.

### Claim 6: Concrete existing examples of the headless-for-agents pattern include MCP integrations (Granola), Google Workspace CLI, Obsidian CLI, Salesforce CLI, and the CLI-Anything auto-generation tool

- **Evidence**: Matt Webb's enumeration of real deployed examples in his April 18,
  2026 post.
- **Confidence**: settled (named products; independently verifiable)
- **Quote**: (no single quote captures the full list; see Our assessment)
- **Our assessment**: The example set establishes that this is not a theoretical
  pattern — it's already in production. Granola (AI meeting transcription via MCP),
  Google Workspace CLI, Obsidian CLI, and Salesforce CLI represent different SaaS
  categories (productivity, notes, CRM) all moving toward agent-accessible interfaces.
  CLI-Anything (which "auto-generates command-line interfaces for any codebase") is
  particularly notable: it's a meta-tool that adds headless access to services that
  don't natively provide it, suggesting the ecosystem is building bridge tools for
  services slow to adopt APIs.

### Claim 7: Salesforce has exposed its entire platform as APIs, MCP, and CLI — calling API the new UI under the "Salesforce Headless 360" banner

- **Evidence**: Marc Benioff's direct announcement quoted verbatim by Willison.
  Vendor commitment from the CEO of a major enterprise SaaS company.
- **Confidence**: settled (CEO public statement about a released product direction)
- **Quote**: "Welcome Salesforce Headless 360: No Browser Required! Our API is the UI.
  Entire Salesforce & Agentforce & Slack platforms are now exposed as APIs, MCP, & CLI.
  All AI agents can access data, workflows, and tasks directly in Slack, Voice, or
  anywhere else with Salesforce Headless."
- **Our assessment**: "Our API is the UI" is a declarative inversion of the
  traditional SaaS design hierarchy. This is not a roadmap item — Benioff frames it
  as a completed exposure of the platform. The explicit mention of MCP (Model Context
  Protocol) alongside traditional API and CLI signals that enterprise SaaS is adapting
  specifically to LLM agent access patterns, not just general API access. This is the
  strongest vendor signal in this source cluster that the headless-for-agents pattern
  has moved from emerging to early mainstream adoption.

### Claim 8: There was an "API winter" from roughly the mid-2010s through mid-2025, driven by monetization pressure, abuse, competitive risk, and privacy concerns — APIs contracted across the industry

- **Evidence**: Brandur Leach's historical analysis in "The Second Wave of the
  API-first Economy." He names specific platforms (Twitter, Facebook/Instagram, GitHub)
  and their specific rationales.
- **Confidence**: emerging (analytical retrospective; the historical pattern is
  well-documented but characterizing it as an "API winter" is Leach's framing)
- **Quote**: "APIs didn't disappear, but it was a cold winter for them"
- **Our assessment**: Leach names specific drivers per platform: Twitter "leveled off
  and began to dip as the company struggled to find ways to generate revenue";
  Facebook was "hugely constricted post-Cambridge Analytica"; Instagram "saw no reason
  to share ad revenue"; GitHub "had to crack down" on abuse. The general pattern is
  "abuse, monetization pressure, competitive risk, privacy, etc." This is important
  context for the second-wave thesis: the first wave failed not because APIs were
  technically wrong but because the business incentives turned against them. The second
  wave depends on business incentives flipping again — which Leach argues AI agent
  demand is doing.

### Claim 9: The second API wave is structurally different from the first: the first wave was about third-party platforms extending services; the second wave is about agents acting on behalf of individual users within their own accounts

- **Evidence**: Brandur Leach's analytical distinction in his post. This is the
  central thesis of his piece.
- **Confidence**: emerging (analytical claim; well-reasoned; the structural distinction
  is clear but whether it actually changes business incentives is yet to be proven
  at scale)
- **Quote**: "instead of APIs being to offer infinitely flexible access...their primary
  use will be to fulfill requests on behalf of a primary user"
- **Our assessment**: This structural distinction matters for how practitioners think
  about API integration design. First-wave APIs were B2B (app-to-platform); second-wave
  APIs are agent-to-service-on-behalf-of-user. The key implication: second-wave API
  access doesn't require a developer to build an integration product. It requires a
  user to authorize an agent to act. This shifts the primary integration audience from
  developer-platform partnerships to user-agent authorization — a fundamentally
  different design target.

### Claim 10: API availability is becoming a decisive competitive differentiator in markets with commodity services — the presence or absence of an API may determine which service wins

- **Evidence**: Brandur Leach's prediction in his post, citing the shift in API value
  from liability to competitive advantage.
- **Confidence**: emerging (forward-looking claim with strong analytical support;
  not yet verified by market outcomes at scale)
- **Quote**: "Suddenly, an API is no longer liability, but a major saleable vector to
  give users what they want: a way into the services they use and pay for so that an
  agent can carry out work on their behalf. Especially given a field of relatively
  undifferentiated products, in the near future the availability of an API might just
  be the crucial deciding factor that leads to one choice winning the field."
- **Our assessment**: This is the business-model consequence of the headless pattern.
  If AI agents are the primary user interface for a category of service, and agents
  require APIs to work effectively, then services without APIs are inaccessible to
  agent-mediated users. In commoditized markets (where multiple providers are
  functionally equivalent), agent accessibility could break tie-decisions in favor of
  the provider with the better API. Practitioners advising on tool/service selection
  for agent harnesses should include API availability as a first-class evaluation
  criterion.

### Claim 11: Monopoly or ad-driven platforms (utilities, social media) have little incentive to provide agent-accessible APIs and will likely resist the shift

- **Evidence**: Brandur Leach's specific callouts of Xfinity ("you won't be reliably
  paying your Xfinity bill via agent anytime soon") and ad-driven platforms ("Don't
  expect much out of Instagram, TikTok, or other platforms that power themselves with
  ads").
- **Confidence**: emerging (analytical prediction; the incentive logic is sound but
  not verified by outcomes)
- **Quote**: (no single verbatim quote; two separate claims — see Our assessment)
- **Our assessment**: Leach identifies two categories of API holdouts: (1) monopoly
  utilities with no competitive pressure (Xfinity: no competitor to lose customers
  to), and (2) ad-driven platforms (Instagram, TikTok) where API access would bypass
  ad inventory. This matters for harness engineers choosing which services to integrate:
  APIs from competitive SaaS providers are a reasonable long-term assumption; APIs
  from utilities or ad-supported social platforms are not. Plan for computer-use
  (GUI automation) fallbacks for these categories, not API-first integration.

### Claim 12: Basecamp has actively revamped for LLM accessibility, adding new APIs and CLIs — joining Salesforce as an early enterprise adapter

- **Evidence**: Brandur Leach's observation in his post about specific companies
  responding to the second-wave opportunity.
- **Confidence**: emerging (asserted by Leach; independently verifiable)
- **Quote**: "revamped themselves for LLM accessibility, including new API, new CLI"
- **Our assessment**: Basecamp is notable because it's a smaller, opinionated SaaS
  company (known for anti-complexity philosophy) that has nonetheless chosen to
  invest in LLM accessibility. This signals the pattern is not just an enterprise-scale
  initiative — even smaller SaaS companies are evaluating headless-first as a
  strategic move.

## Concrete Artifacts

### Salesforce Headless 360 Announcement (verbatim)

```
Source: Marc Benioff tweet (https://twitter.com/benioff/status/2044981547267395620)
Via: Simon Willison, simonwillison.net, April 19, 2026

"Welcome Salesforce Headless 360: No Browser Required! Our API is the UI.
Entire Salesforce & Agentforce & Slack platforms are now exposed as APIs, MCP, & CLI.
All AI agents can access data, workflows, and tasks directly in Slack, Voice, or
anywhere else with Salesforce Headless."
```

### Webb's Multi-Service Agent Workflow Example (verbatim)

```
Source: Matt Webb, interconnected.org/home/2026/04/18/headless, April 18, 2026

"you can: query your notes then jump to a spreadsheet then research the web then jump
back to the spreadsheet then text the user a clarifying question then double-check
your notes, all by bouncing between CLIs"

Context: Webb uses this to illustrate CLI composability vs. app user-journey linearity.
```

### Leach's API Value Inversion Thesis (verbatim)

```
Source: Brandur Leach, brandur.org/second-wave-api-first

"Suddenly, an API is no longer liability, but a major saleable vector to give users
what they want: a way into the services they use and pay for so that an agent can
carry out work on their behalf. Especially given a field of relatively undifferentiated
products, in the near future the availability of an API might just be the crucial
deciding factor that leads to one choice winning the field."
```

### API Winter Drivers (Leach's enumeration)

```
Source: Brandur Leach, brandur.org/second-wave-api-first

Twitter: "leveled off and began to dip as the company struggled to find ways to
          generate revenue"
Facebook: "hugely constricted post-Cambridge Analytica where a single rogue app was
           able to suck up data"
Instagram: "Realizing they had a real money maker on their hands, they saw no reason
            to share ad revenue"
GitHub: "had to crack down...Endpoints became authenticated by necessity"
General: "abuse, monetization pressure, competitive risk, privacy, etc."
```

### First vs. Second API Wave Structural Distinction

```
Source: Brandur Leach, brandur.org/second-wave-api-first

First wave purpose: "APIs were largely aimed at third parties who'd use them to
                    extend and augment the underlying platform"

Second wave purpose: "APIs map cleanly to normal product capabilities. They provide
                     programmatic access for agents that act on behalf of people."

Key distinction: "instead of APIs being to offer infinitely flexible access...their
                 primary use will be to fulfill requests on behalf of a primary user"
```

### Services Named as Early Headless Adopters (Webb's enumeration)

```
Source: Matt Webb, interconnected.org/home/2026/04/18/headless

Already providing agent-accessible interfaces:
- Granola: MCP integration for AI-accessible meeting transcription
- Google Workspace CLI
- Obsidian CLI
- Salesforce CLI
- CLI-Anything: auto-generates CLIs for any codebase

Named as AI agent targets (no CLI/API noted):
- Companies House, Yelp, Google Maps, Resy, The Infatuation, Monzo, Booking.com
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-dispatch-computer-use.md` Claim 1 ("Claude will reach for the
    most precise tool first, starting with connectors...when there isn't a connector,
    Claude can directly control your browser, mouse, keyboard") — Webb's Claim 1
    here provides the market-level explanation for WHY this hierarchy exists: headless
    APIs are "quicker and more dependable" than GUI automation. The Anthropic dispatch
    post establishes the design hierarchy; the Webb/Willison post establishes the
    *reason* that hierarchy is correct as a general pattern, not just an Anthropic
    product choice.
  - `blog-anthropic-dispatch-computer-use.md` Claim 6 ("computer use is still early,
    slower, and less reliable than direct integrations") — Directly corroborates
    Webb's claim that GUI-based agent automation is less reliable than headless access.
    Computer use as a fallback (Anthropic's framing) is exactly the position Webb
    advocates for at the market level.

- **Extends**:
  - `blog-anthropic-dispatch-computer-use.md` — The Dispatch note establishes a
    connector-first → computer-use fallback hierarchy as an Anthropic product
    decision. The Webb/Willison source extends this to a market-level architectural
    thesis: the reason to prefer connectors (headless APIs) over computer use (GUI
    automation) is not just Anthropic's design preference — it is a general principle
    emerging across the SaaS industry. Practitioners should read the two sources
    together: one explains what the hierarchy is; the other explains why the market
    is converging on it.
  - `blog-bswen-mcp-token-cost.md` — The MCP token cost note documents a practitioner
    cost of MCP server proliferation (excessive context token consumption). The Webb
    post lists Granola's MCP integration as a positive example of headless agent
    access. Together these frame MCP as a double-edged pattern: the right interface
    layer for headless access, but with a cost-management burden that requires active
    curation (prune to essential servers, per Bswen's recommendation).

- **Contradicts**: None identified. No existing corpus note makes claims that contradict
  the headless-first architectural thesis. The closest potential tension is between
  "API winter was driven by business incentives against APIs" (Leach, this source)
  and the generally optimistic framing of API/MCP integration throughout the corpus —
  but these are complementary (the winter is over; the second wave is starting) rather
  than contradictory.

- **Novel**:
  - **First in-corpus documentation of the "headless services for agents" pattern as a
    named market-level trend**: No prior source note frames the headless-vs-GUI
    question at the SaaS industry level with named vendor adoption signals (Salesforce,
    Basecamp) and a historical thesis (API winter → second wave).
  - **"API winter" thesis and the second-wave structural distinction**: Leach's argument
    that the second wave is structurally different (user-behalf vs. third-party
    extension) is entirely new to the corpus.
  - **API availability as competitive differentiator**: The claim that API presence
    could "be the crucial deciding factor" in commodity markets is new — no prior source
    frames API access as a first-class evaluation criterion for service selection in
    agent harnesses.
  - **CLI composability vs. app user-journey linearity**: Webb's specific framing of why
    CLIs are a better agent interface than apps (composability from Unix heritage;
    apps enforce linear "user journeys" incompatible with agent multitasking) is new
    to the corpus.
  - **Vendor-intent signal at CEO level**: Marc Benioff's "Our API is the UI" quote is
    the first CEO-level vendor commitment to headless-for-agents in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — Tool Selection and Integration)**: The guide
  currently documents the connector-first → computer-use fallback hierarchy as an
  Anthropic product decision (`blog-anthropic-dispatch-computer-use.md`). This source
  provides a second, independent justification for the same hierarchy — not as an
  Anthropic design choice but as a market convergence pattern. Recommend adding a
  "why headless first" framing: APIs are faster, more reliable, and more composable
  than GUI automation for agents; computer use is the last resort precisely because
  headless access is becoming the industry standard. The guide should also add API
  availability as an explicit evaluation criterion when selecting external services
  for agent integration — following Leach's competitive differentiator claim.

- **Chapter 02 (Harness Engineering — External Service Selection)**: Add guidance on
  which service categories are likely to provide agent-accessible APIs (competitive
  SaaS, productivity tools) vs. which are unlikely (monopoly utilities, ad-driven
  social platforms). Per Leach's analysis: plan for GUI automation fallbacks when
  integrating Xfinity-class utilities or Instagram/TikTok-class ad platforms; assume
  API availability for competitive SaaS in the near term.

- **Chapter 03 (Safety and Verification — Integration Scope)**: Webb's security claim
  (CLIs are smaller and easier to harden than full GUI apps) provides a security
  argument for preferring API/CLI integration over computer use beyond just reliability.
  A smaller attack surface for agent-accessible interfaces is a security design
  principle. The guide should note that headless access is not just faster — it
  also constrains the attack surface available to prompt injection attempts targeting
  agent-controlled interfaces.

- **Chapter 00 (Principles — Macro Context)**: The second-wave API thesis and the
  "API is no longer liability but saleable vector" framing should inform the guide's
  macro-context section. AI agents are changing the business incentive structure for
  APIs — practitioners building agent harnesses today are operating in a market
  that is actively improving API availability. This is a tailwind, not a barrier.

## Extraction Notes

- The Willison post itself is short (a link aggregator with brief framing). The
  substantive claims come from the three linked sources, all of which were fetched
  and read. The Matt Webb post and Brandur Leach post were the primary content sources.
- The Marc Benioff tweet URL is included as a reference, but tweets are authentication-
  gated. The verbatim quote is available in the Willison post itself.
- Brandur Leach's post (`brandur.org/second-wave-api-first`) initially declined to
  return verbatim text in bulk; targeted follow-up fetches were used to extract
  specific quotes on specific claims. The verbatim quotes in this note were confirmed
  against the source.
- The "Mythos model" claim (Webb: Anthropic's Mythos model so good at finding security
  flaws that governments are convening emergency meetings) is noted as anecdotal — no
  Anthropic source in the corpus confirms a model by this name or this characterization.
  It is included in the security argument (Claim 2) but not extracted as a standalone
  claim given the absence of corroboration.
- The Prospector's triage note identified "per-head pricing models may break" as a
  key theme. This claim surfaces as background context in Brandur Leach's article
  (the API winter was partly driven by per-API-call monetization pressures; the second
  wave incentivizes per-API-seat vs. per-GUI-seat models) but neither Webb nor Leach
  makes an explicit claim about per-head pricing in the quotes retrieved. Accordingly,
  it is captured in Claim 10's assessment rather than as a standalone claim.
