---
source_url: https://www.thoughtworks.com/insights/articles/path-to-ai-first-organization
source_type: blog-post
title: "Path to AI-first organization"
author: May Xu (Head of Technology, APAC, Thoughtworks)
date_published: 2026-09-23
date_extracted: 2026-09-26
last_checked: 2026-09-26
status: current
confidence_overall: anecdotal
issue: "#3728"
---

# Path to AI-First Organization

> Thoughtworks essay arguing that "AI-native" (designed around AI from the
> outset) is unrealistic for most established organizations, and proposing
> "AI-first" (deliberately redesigning strategy, workflows and operating
> model around AI while other systems continue at their own pace) as the
> practical target — structured around a three-stage adoption model
> (AI-assisted → AI-enabled → AI-first), six organizational shifts, and five
> enterprise-capability building blocks.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Articles" category, tagged
  "Technology strategy" and "AI and ML"; published September 23, 2026; from
  the trusted `thoughtworks` RSS feed). A single-author, ~1,350-word
  framework/thought-leadership piece with no inline citations to external
  sources; two named illustrative examples (one internal legacy-modernization
  project, one client engagement referenced only by outcome) and one named
  external company (Spotify) cited for its platform tooling.
- **Author credibility**: May Xu (full name "May Ping Xu" per the article's
  page metadata) is titled, per her Thoughtworks profile page
  (thoughtworks.com/profiles/m/may-ping-xu), "Head of Technology, APAC." Her
  profile bio states: "As Head of Technology for Thoughtworks in Asia
  Pacific, May advises on client projects, driving regional technology
  strategies, and champions Thoughtworks as a leading and trusted tech brand
  for our clients, consultants and the industry at large." This is a senior
  regional technology-leadership title — comparable in seniority to Thomas
  Squeo's "CTO, Thoughtworks Americas" byline in
  `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`, and
  more senior than several other Thoughtworks bylines in this corpus that
  carry no stated title (e.g. Ankur Buttan in
  `blog-thoughtworks-buttan-alpha-playbook.md`). No prior corpus source is
  authored by Xu.
- **Scope**: Covers a definitional distinction between AI-native and
  AI-first organizations; an argument for why AI-native is impractical for
  most established enterprises; a three-stage organizational adoption model
  (AI-assisted, AI-enabled, AI-first); six named shifts required to build an
  "AI-first team"; and five named organizational capabilities required to
  scale those shifts across an enterprise. Does NOT cover: a named client
  case study with a quantified metric (the one client anecdote given — a
  project stretching from ~3 to ~10 months — has no company name, industry,
  or measurement methodology attached), a technical harness or tooling
  implementation, or any comparison of organizations that pursued AI-native
  versus AI-first and their relative outcomes.

## Extracted Claims

### Claim 1: Becoming truly AI-native is unrealistic for most established organizations because AI is only one part of a much more complex technology landscape that cannot move at a single pace, so AI-first (deliberately redesigning strategy, workflows, and operating model around AI) is a more realistic ambition than AI-native (designed around AI from the outset)
- **Evidence**: The article's opening thesis, restated as a direct
  definitional contrast in the following paragraph, using the historical
  analogy of digital-native vs. digital transformation.
- **Confidence**: anecdotal (framing/definitional argument by analogy; no
  data on the proportion of enterprises that have achieved either status, or
  on outcome differences between the two paths)
- **Quote**: "During the shift to digital, many organizations aspired to
  become digital-native, but relatively few achieved it. We are seeing a
  similar pattern in the AI era: while a small number of companies are
  AI-native, becoming AI-first is a more realistic ambition for most
  established organizations."
- **Quote** (definitions): "An AI-native organization is one whose products,
  operating model and technology foundations have been designed around AI
  from the outset. An AI-first organization does not need to have been built
  around AI. Instead, it deliberately redesigns its strategy, workflows and
  operating model to take advantage of AI."
- **Quote** (root cause): "For most established organizations, becoming
  truly AI-native is difficult because AI is only one part of a much more
  complex technology landscape. A typical enterprise runs a mix of legacy
  systems, SaaS products, traditional machine learning applications and
  newer LLM-enabled products, all built for different purposes and operating
  assumptions. They cannot all become AI-native at the same pace."
- **Our assessment**: This is the article's central, guide-relevant
  contribution — a named vocabulary distinction (AI-native vs. AI-first)
  that this Miner's corpus search did not find named elsewhere prior to this
  source. It is directly relevant to the guide's own title and framing
  ("AI-native engineering"): the guide should be explicit about which of the
  two statuses it is actually recommending teams pursue, since this source
  argues the two are meaningfully different targets with different levels of
  achievability. See Cross-References → Extends for how this reframes
  `blog-anthropic-ai-native-engineering-org.md`.

### Claim 2: An AI-first organization should be understood as a "smart traffic-management system" — not every part of the organization needs to move at the same speed, and not every problem needs AI; becoming AI-first means deliberately deciding where AI adds value, what it should be responsible for, and where people or existing technology remain the better choice
- **Evidence**: Author's direct metaphor, presented immediately after the
  AI-native/AI-first definitional split, as the operating principle that
  follows from accepting that not all systems can modernize at once.
- **Confidence**: anecdotal (a framing metaphor, not a measured claim)
- **Quote**: "A better way to think about an AI-first organization is as a
  smart traffic-management system. Not every part of the organization needs
  to move at the same speed, and not every problem needs AI. Becoming
  AI-first means deliberately deciding where AI adds value, what it should
  be responsible for and where people or existing technology remain the
  better choice."
- **Our assessment**: This is a useful corrective against a common failure
  mode implicit in more totalizing "AI-native" framings elsewhere in the
  corpus — the idea that every system, team, or workflow must modernize
  uniformly. It gives the guide a explicit permission structure for uneven,
  selective AI adoption rather than blanket transformation, which is a
  distinct and complementary idea to the guide's existing risk/value
  prioritization content.

### Claim 3: Individual-productivity gains from AI (helping people do existing tasks faster) rarely amount to organizational transformation on their own; scaling AI requires moving beyond individual productivity toward greater autonomy and organizational change, structured as three adoption stages — AI-assisted (individual productivity), AI-enabled (team productivity), and AI-first (organizational productivity, redesigning products/processes/operating models around what humans and AI can accomplish together)
- **Evidence**: Direct three-stage taxonomy presented under "One useful way
  to think about organizational AI adoption is across three stages," each
  stage given a one-sentence definition.
- **Confidence**: anecdotal (a named, three-tier maturity model; no data on
  what fraction of organizations sit at each stage or how stage transitions
  are measured)
- **Quote**: "Much enterprise AI adoption still begins with individual
  productivity: helping people perform existing tasks faster. While useful,
  these gains alone rarely amount to organizational transformation. Scaling
  AI requires moving beyond individual productivity toward greater autonomy
  and organizational change."
- **Quote** (three stages): "AI-assisted: AI supports existing workflows,
  focusing on individual productivity." / "AI-enabled: AI is embedded into
  processes and operations, elevating team productivity." / "AI-first:
  Redesign products, processes and operating models around what humans and
  AI can accomplish together, focusing on organizational productivity."
- **Our assessment**: This three-stage model (AI-assisted → AI-enabled →
  AI-first) directly corroborates the general shape of maturity models
  elsewhere in the corpus that separate individual-tool-use adoption from
  organizational transformation (see Cross-References → Corroborates), while
  contributing its own specific stage names and definitions. The claim that
  individual-productivity gains "rarely amount to organizational
  transformation" is a pointed caution against treating tool-adoption
  metrics (e.g. Claude-assisted commit rate) as sufficient evidence of
  organizational-level change.

### Claim 4: Reaching the AI-first stage requires organizations to rethink where the boundary lies between people and AI and to adopt a risk-based tiered autonomy model
- **Evidence**: Direct statement bridging the three-stage model to the six
  shifts that follow.
- **Confidence**: anecdotal (asserted transition requirement; the article
  does not itself define the tiers of the "risk-based tiered autonomy
  model" it names — no tier boundaries, criteria, or worked example are
  given anywhere in this article)
- **Quote**: "Reaching this AI-first stage requires organizations to rethink
  how people and AI work together, where is the boundary between people and
  AI and adopt a risk-based tiered autonomy model."
- **Our assessment**: This is the thinnest claim in the article — the
  phrase "risk-based tiered autonomy model" is asserted as a requirement but
  never elaborated (no tiers, criteria, or governance mechanism are named,
  in contrast to how the same underlying idea is worked out in more detail
  elsewhere in the corpus — see Cross-References → Corroborates for the
  Gordon/Kamelman three-tier oversight structure, which is the more
  substantive version of this same idea already in the corpus).

### Claim 5: The first of six shifts to build an AI-first team is "from execution to judgment" — as AI takes on more execution work, the human role increasingly shifts toward judgment (deciding what to delegate, evaluating outputs, determining when intervention is required), becoming more architectural in nature, which also creates opportunities to embed validation and guardrails earlier in the delivery lifecycle
- **Evidence**: Direct statement under "1. From execution to judgment,"
  illustrated with one named internal example (an unnamed "legacy
  modernization project").
- **Confidence**: anecdotal (single unnamed internal project as illustration;
  no name, client, or metric given)
- **Quote**: "As AI takes on more execution work, human contribution
  increasingly shifts toward judgment: deciding what to delegate, evaluating
  outputs and determining when intervention is required. In one legacy
  modernization project, agents perform much of the execution and
  evaluation, while developers decide what agents can do independently and
  where human approval is required. Their role shifts from authoring every
  part of the solution to designing its flows, decision points and
  controls, becoming more architectural in nature. This also creates
  opportunities to shift controls earlier in the delivery lifecycle,
  embedding validation and guardrails into AI-first workflows."
- **Our assessment**: "Becoming more architectural in nature" is a specific,
  citable reframing of the engineer's role under heavy AI delegation — it
  corroborates the corpus's existing "supervisory engineering" vocabulary
  (see Cross-References → Corroborates) with an independent, differently-
  worded description of the same shift (deciding what to delegate,
  evaluating outputs, determining when to intervene — functionally the same
  three activities as "directing, evaluating, correcting").

### Claim 6: The second shift is "from T-shaped to E-shaped" — a concept the article attributes to Marc Andreessen (co-founder of a16z) — describing people who maintain a deep, specialized vertical core while developing real, functional capabilities across multiple adjacent horizontal disciplines (product, design, engineering) simultaneously, using AI as the "vertical connector" or "backbone" that makes those multiple horizontal arms possible without eliminating the need for deep expertise
- **Evidence**: Direct definitional statement plus a named illustrative
  example (an unnamed "product manager" who built much of a prototype
  directly).
- **Confidence**: anecdotal (concept attribution to Andreessen given without
  a citation link; one unnamed internal example)
- **Quote**: "AI can help people work effectively across a broader range of
  activities without eliminating the need for deep expertise. E-shaped is
  the concept introduced by Marc Andreessen (Co-founder of a16z), describing
  people who have: Deep vertical core: Maintaining deep, specialized
  expertise in a primary craft. Multiple horizontal bars: Developing real,
  functional capabilities in server adjacent disciples simultaneously like
  product, design and engineering. The AI 'backbone': Using AI as the
  vertical connector that makes these multiple horizontal 'arms' possible.
  AI acts as a force multiplier, allowing a single person to execute
  high-level tasks in areas where they aren't naturally experts."
- **Quote** (example and outcome): "In one project, a product manager built
  much of a prototype directly, shortening a feedback cycle that would
  traditionally have required coordination across product, design and
  development. The result is not that everyone becomes an expert in
  everything, but that the boundaries between roles become more permeable."
- **Our assessment**: The article's own text contains a verbatim typo
  ("server adjacent disciples" — almost certainly intended as "several
  adjacent disciplines"), preserved here per MINER.md §2a rather than
  silently corrected; flagged so the Assayer and Smith do not mistake it for
  a transcription error introduced during extraction. Setting the typo
  aside, "E-shaped" (as opposed to the more familiar "T-shaped") is a novel
  named vocabulary term for this corpus, and directly corroborates
  `blog-anthropic-ai-native-engineering-org.md` Claim 8 ("Our PMs code a lot
  now... engineers who take on things like content and design") with an
  independent named framework for the same phenomenon (role permeability
  enabled by AI as a cross-discipline force multiplier) — see
  Cross-References → Corroborates.

### Claim 7: The third shift is "from document to managed context" — documentation remains important, but AI creates a new requirement that organizational knowledge must also be structured and made accessible as usable context, with requirements/specifications/architectural decision records moving closer to the codebase so both people and AI can use them; teams must treat context as an engineered asset rather than knowledge scattered across documents, systems, and people's heads
- **Evidence**: Direct statement under "3. From document to managed
  context," with an illustrative reference to "some AI-enabled projects."
- **Confidence**: anecdotal (general claim illustrated by an unnamed class
  of projects, not a specific named example)
- **Quote**: "Documentation remains important, but AI creates a new
  requirement: organizational knowledge must also be structured and
  accessible as usable context. On some AI-enabled projects, requirements,
  specifications and architectural decision records are moving closer to
  the codebase so both people and AI can use them. Teams therefore need to
  treat context as an engineered asset, not knowledge scattered across
  documents, systems and people's heads."
- **Our assessment**: "Context as an engineered asset" is a compact,
  quotable restatement of a principle this corpus already documents from
  multiple other angles (context engineering as a discipline, guides/sensors
  vocabulary, AI-ready data). This article's specific contribution is
  naming the migration path — documentation and ADRs moving physically
  closer to the codebase — as the mechanism by which that engineering
  happens, rather than treating "context engineering" as an abstract
  principle alone.

### Claim 8: The fourth shift is "from tool to partner" — earlier AI developer tools largely assisted with bounded tasks (code completion/generation); agentic systems can now take on multi-step activities, use tools, and interact with other systems (with protocols such as MCP as one connecting mechanism), which changes the organizational challenge from providing AI capabilities to defining what work can be delegated and under what controls — but becoming AI-first does not mean every activity is performed by an agent; the realistic model is hybrid, with people remaining accountable for outcomes while AI takes on different levels of execution depending on the task
- **Evidence**: Direct statement under "4. From tool to partner," naming MCP
  explicitly as an example protocol.
- **Confidence**: anecdotal (general architectural/organizational claim; no
  named implementation or metric)
- **Quote**: "Earlier AI developer tools largely assisted with bounded tasks
  such as code completion or generation. Agentic systems can now take on
  multi-step activities, use tools and interact with other systems. That
  changes the challenge from simply providing AI capabilities to defining
  what work can be delegated and under what controls. Protocols such as MCP
  are one mechanism for connecting agents to a wider ecosystem of tools and
  information."
- **Quote** (hybrid model): "But becoming AI-first does not mean imagining an
  organization in which every activity is performed by an agent. The more
  realistic model is hybrid: people remain accountable for outcomes while AI
  takes on different levels of execution depending on the task. The goal is
  to use AI where it performs well, rather than assuming it can solve every
  problem."
- **Our assessment**: The explicit rejection of "every activity performed by
  an agent" as the AI-first end-state is a useful guardrail against an
  over-totalizing reading of "AI-first" — it corroborates the "bounded
  autonomy" framing already in the corpus's harness-engineering sourcing
  (people remain accountable for outcomes; AI's execution level varies by
  task) — see Cross-References → Corroborates.

### Claim 9: The fifth shift, "engineering practice as safety net," argues that faster AI-assisted delivery only creates value if teams can detect and recover from mistakes quickly; practices such as automated testing, continuous integration, observability, security controls, and small reversible changes become more important as AI increases delivery pace, and because AI generates more change than people can realistically review manually, traditional code review alone cannot provide sufficient control — so TDD and BDD gain renewed importance as automated ways to verify that changes behave as expected
- **Evidence**: Direct statement under "5. Engineering practice as safety
  net."
- **Confidence**: anecdotal (a prescriptive argument; no measured comparison
  of review-only versus TDD/BDD-augmented team outcomes is given)
- **Quote**: "Faster AI-assisted delivery only creates value if teams can
  detect and recover from mistakes quickly. Practices such as automated
  testing, continuous integration, observability, security controls and
  small reversible changes become more important as AI increases the pace of
  delivery. As AI generates more change than people can realistically review
  manually, traditional code review alone cannot provide the necessary
  control. Practices such as TDD and BDD therefore gain renewed importance
  by providing automated ways to determine whether changes behave as
  expected."
- **Our assessment**: "Traditional code review alone cannot provide the
  necessary control" is a direct, specific claim that code review capacity
  does not scale linearly with AI-generated change volume — this
  corroborates the corpus's existing "verification is the new bottleneck"
  convergence (Osmani, Shopify, Fung — see Cross-References → Corroborates)
  by naming a specific mitigation (TDD/BDD as automated verification that
  does not require human review capacity to scale with change volume) rather
  than simply restating the bottleneck diagnosis.

### Claim 10: The sixth shift is "from individual learning to feedback" — every interaction with AI can reveal useful information about where prompts work, where context is missing, and where controls fail; teams need mechanisms to capture those lessons and improve shared instructions, context, tools, and workflows, rather than leaving the learning isolated with individual users
- **Evidence**: Direct statement under "6. From individual learning to
  feedback."
- **Confidence**: anecdotal (a prescriptive organizational claim; no named
  feedback-capture mechanism, tool, or example is given)
- **Quote**: "Every interaction with AI can reveal useful information: where
  prompts work, where context is missing and where controls fail. Teams
  need mechanisms to capture those lessons and improve shared instructions,
  context, tools and workflows rather than leaving the learning with
  individual users."
- **Our assessment**: This names the organizational-learning gap without
  prescribing a specific mechanism (no shared prompt library, retro process,
  or tooling is named) — it is the least concretely actionable of the six
  shifts, though it is a real and underserved concern: individual engineers
  discovering "this phrasing works better" or "this context is
  consistently missing" is common but the article does not describe how
  Thoughtworks itself captures and propagates that learning.

### Claim 11: Scaling the six team-level shifts across an enterprise requires a "clear AI stance" — an explicit, redefined organizational boundary (since most existing operating models were designed around people as the primary actors) stating how AI is expected to be used, where its use is restricted, what decisions can be delegated, where AI executes autonomously, where people remain in the loop, and how responsibility passes between them
- **Evidence**: Direct statement under "A clear AI stance," the first of
  five named organizational capabilities under "Building AI-first
  organizational capabilities."
- **Confidence**: anecdotal (a prescriptive organizational requirement; no
  named example of an organization's actual "AI stance" document is given)
- **Quote**: "People need to understand how AI is expected to be used, where
  its use is restricted, what decisions can be delegated and where human
  accountability remains essential. Most existing operating models were
  designed around people as the primary actors. An AI-first operating model
  needs to redefine that boundary explicitly, determining where AI executes
  autonomously, where people remain in the loop and how responsibility
  passes between them."
- **Our assessment**: This is a framing-level restatement of the
  accountability/governance principle already present in more elaborated
  form elsewhere in this corpus's Thoughtworks governance cluster (see
  Cross-References → Corroborates) — this article contributes the specific
  observation that most *existing* operating models assumed people as the
  sole actors, which is a useful diagnostic for why organizations find this
  redefinition hard: it is not adding a new rule to an existing model, it is
  changing the model's foundational assumption about who acts.

### Claim 12: AI systems need secure access to reliable internal data, documentation, code, and business context — but availability alone is not enough; that information also needs sufficient quality, meaning, and governance for AI systems to use it correctly, and legacy systems/APIs designed for human interaction (not agents) can turn a straightforward human process into one requiring an agent to coordinate many API calls, stretching delivery timelines significantly; organizations must therefore consider agent experience alongside customer experience
- **Evidence**: Direct statement under "AI-ready data and context," with one
  named client example given by outcome only (no company name, industry, or
  named product).
- **Confidence**: anecdotal (a single unnamed client example with a
  before/after timeline figure but no company name, methodology, or
  independent verification)
- **Quote**: "AI systems need secure access to reliable internal data,
  documentation, code and business context. Improving availability alone
  isn't enough; that information also needs sufficient quality, meaning and
  governance for AI systems to use it correctly."
- **Quote** (client example): "The consequences can be significant. In one
  client example, a product expected to take about three months stretched
  to around ten months, partly because legacy systems and APIs had been
  designed for human interactions rather than agents. A process that was
  straightforward for a person could require an agent to coordinate 10 or 20
  API calls. Organizations therefore need to consider agent experience
  alongside customer experience."
- **Our assessment**: The ~3-to-~10-month project-timeline stretch is the
  article's single most concrete (if unnamed and unverifiable) data point.
  "Consider agent experience alongside customer experience" is a specific,
  reusable design principle — it names a category (agent experience, AX) as
  a first-class design concern distinct from the already-familiar customer
  experience (CX) and developer experience (DX) categories, which is novel
  framing for this corpus (see Cross-References → Novel). This client
  example could not be independently verified — no company name, industry,
  or corroborating source is given.

### Claim 13: Strong engineering practices (automated testing, observability, continuous delivery, reversible changes) provide the technical safety net that lets teams experiment with AI without sacrificing reliability; AI amplifies whichever foundation is already in place, so teams with strong engineering practices can move faster because they have mechanisms for validating and controlling change, while weak foundations simply let problems scale faster too
- **Evidence**: Direct statement under "Strong engineering practices," the
  third named organizational capability.
- **Confidence**: anecdotal (a general architectural/organizational claim;
  no named team comparison or measured outcome distinguishing "strong
  foundation" teams from "weak foundation" teams is given)
- **Quote**: "Automated testing, observability, continuous delivery and
  reversible changes provide the technical safety net teams need to
  experiment with AI without sacrificing reliability. AI amplifies the
  foundations already in place. Teams with strong engineering practices can
  move faster because they have mechanisms for validating and controlling
  change; weak foundations simply allow problems to scale faster too."
- **Our assessment**: "AI amplifies the foundations already in place" —
  applying equally to strong and weak foundations — is a sharp, memorable
  restatement of the corpus's existing "AI is an amplifier, not an
  equalizer" theme, phrased here specifically in terms of engineering-practice
  maturity rather than general capability.

### Claim 14: Internal platforms that make approved AI capabilities easy to access while encoding organizational guardrails around models, data, tools, and permissions make the safe path the easiest path; as systems become more agentic, platforms must also govern what agents can access and do and where human intervention is required — organizations with strong existing engineering-platform capabilities (the article names Spotify's Backstage and Fleet Management specifically) move faster with AI adoption than those without
- **Evidence**: Direct statement under "AI-enabled internal platforms," with
  one named external company example (Spotify) cited by its named platform
  tooling, not by a measured outcome specific to Spotify's own AI adoption.
- **Confidence**: anecdotal (Spotify is named for its general
  platform-engineering capability, not for a measured AI-adoption speed
  comparison against organizations lacking such platforms — the claim that
  such organizations "move much faster with AI adoption" is asserted, not
  demonstrated with a comparative measurement)
- **Quote**: "Internal platforms can make approved AI capabilities easy to
  access while encoding organizational guardrails around models, data,
  tools and permissions. Done well, they make the safe path the easiest
  path. As systems become more agentic, platforms also need to govern what
  agents can access and do, and where human intervention is required.
  Organizations like Spotify with strong engineering platform capabilities
  (Backstage, Fleet Management) move much faster with AI adoption than
  those without."
- **Our assessment**: "Make the safe path the easiest path" is the same
  underlying principle as this corpus's existing "paved roads" framing (see
  Cross-References → Corroborates), applied specifically to AI-capability
  platforms rather than general software-delivery platforms. The Spotify
  citation is a named example but not a sourced comparative claim — no
  data, timeframe, or methodology accompanies the assertion that
  Backstage/Fleet-Management-equipped organizations adopt AI faster; treat
  as an illustrative analogy rather than evidence.

### Claim 15: Becoming AI-first is less about adopting more AI tools and more about redesigning how work happens around them; the goal is not to make every system AI-powered or every activity agent-driven, but to determine where AI creates value and build the operating model, data, controls, and engineering foundations to support it — organizations may never become AI-native, but they can still become deliberately and effectively AI-first
- **Evidence**: The article's closing synthesis paragraph.
- **Confidence**: anecdotal (closing restatement of the article's thesis)
- **Quote**: "Becoming AI-first is therefore less about adopting more AI
  tools and more about redesigning how work happens around them. Established
  organizations will continue to operate a mix of legacy, traditional and
  AI-enabled systems, with people and AI taking on different roles across
  that landscape."
- **Quote**: "The goal is not to make every system AI-powered or every
  activity agent-driven, but to determine where AI creates value and build
  the operating model, data, controls and engineering foundations to
  support it. Organizations may never become AI-native, but they can still
  become deliberately and effectively AI-first, achieve meaningful business
  impacts."
- **Our assessment**: This closing statement is the article's clearest,
  most directly guide-quotable sentence for framing organizational ambition:
  it explicitly tells readers not to treat "AI-native" as the required
  end-state, and gives "AI-first" as a legitimate, distinct, achievable
  target. This has direct bearing on how the guide should frame its own
  title's ambition level for readers at established, non-greenfield
  organizations.

## Concrete Artifacts

### Three-stage adoption model (verbatim)

```
Source: May Xu, "Path to AI-first organization," Thoughtworks Insights,
September 23, 2026

AI-assisted: AI supports existing workflows, focusing on individual
  productivity.
AI-enabled:  AI is embedded into processes and operations, elevating team
  productivity.
AI-first:    Redesign products, processes and operating models around what
  humans and AI can accomplish together, focusing on organizational
  productivity.
```

### Six shifts to build an AI-first team (verbatim headings + one-line summary)

```
Source: as above

1. From execution to judgment: humans shift from authoring every part of a
   solution to designing flows, decision points and controls (more
   architectural). Example: a legacy modernization project where agents
   execute/evaluate and developers decide delegation boundaries and
   approval gates.
2. From T-shaped to E-shaped: deep vertical expertise + multiple horizontal
   capabilities (product/design/engineering) + AI as the "backbone"
   connecting them. Concept attributed to Marc Andreessen (co-founder,
   a16z). Example: a product manager building much of a prototype directly.
3. From document to managed context: requirements/specs/ADRs move closer to
   the codebase; context becomes an engineered asset, not scattered
   knowledge.
4. From tool to partner: agentic systems (connected via protocols such as
   MCP) take on multi-step, cross-system work; the realistic model is
   hybrid — people remain accountable for outcomes, AI's execution level
   varies by task.
5. Engineering practice as safety net: automated testing, CI, observability,
   security controls, small reversible changes, TDD/BDD — because
   "traditional code review alone cannot provide the necessary control"
   against AI-generated change volume.
6. From individual learning to feedback: capture per-interaction lessons
   (what prompts work, where context is missing, where controls fail) into
   shared instructions/context/tools/workflows rather than leaving learning
   with individual users.
```

### Five organizational capabilities for AI-first at scale (verbatim headings)

```
Source: as above

1. A clear AI stance — explicit redefinition of the people/AI operating
   boundary (most existing operating models assumed people as sole actors).
2. AI-ready data and context — availability + quality + meaning + governance;
   "consider agent experience alongside customer experience." Named client
   example: a project stretched from ~3 months to ~10 months because
   legacy systems/APIs (built for humans) required an agent to coordinate
   10-20 API calls for what was a single straightforward step for a person.
3. Strong engineering practices — automated testing, observability,
   continuous delivery, reversible changes; "AI amplifies the foundations
   already in place" (for better or worse).
4. Customer-centricity — clear customer outcomes as the "North Star" for
   deciding where AI should and shouldn't be applied.
5. AI-enabled internal platforms — guardrails around models/data/tools/
   permissions, "make the safe path the easiest path"; govern what agents
   can access/do and where human intervention is required. Named example:
   Spotify (Backstage, Fleet Management).
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`,
`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`,
`blog-anthropic-ai-native-engineering-org.md`,
`blog-thoughtworks-malykhin-quantifying-ai-adoption.md`,
`blog-thoughtworks-gall-supervisory-engineering.md`, and
`blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` were re-read directly
(MINER.md §4b) and claim numbers cited below were confirmed against those
notes' numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-anthropic-ai-native-engineering-org.md` Claim 8 (roles blurred at
    Anthropic's Claude Code team — "Our PMs code a lot now... engineers who
    take on things like content and design"): this article's "E-shaped"
    framework (Claim 6 here — deep vertical core plus multiple horizontal
    capabilities, AI as the connecting "backbone") supplies an independent,
    named conceptual model for the exact same phenomenon Fung reports as
    lived practice at Anthropic. Notably, Fung's article ("Running an
    AI-native engineering org") describes an organization that is arguably
    closer to genuinely AI-native (Claude Code's own team, building the
    product it uses) than AI-first as this article defines the terms — a
    useful paired citation: this article supplies the general framework and
    names why most organizations can't replicate Anthropic's path; Fung's
    article is closer to a worked example of what the rarer AI-native case
    actually looks like in practice.
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 7 (the
    three-pillar "directing, evaluating, correcting" framing of supervisory
    engineering) and `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
    Claim 11 ("supervisory engineering becomes a primary human function in
    AI-augmented development teams"): this article's "from execution to
    judgment" shift (Claim 5 here — deciding what to delegate, evaluating
    outputs, determining when intervention is required, becoming "more
    architectural in nature") is a third, independently-worded description
    of the same underlying role shift, without using the term "supervisory
    engineering" itself.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5
    (the three-tier manual/semi-automated/automated oversight structure):
    this article's Claim 4 ("adopt a risk-based tiered autonomy model") names
    the same requirement but does not itself define any tiers, criteria, or
    mechanism — Gordon/Kamelman's article is the more substantive, worked-out
    version of the same underlying idea this article only gestures at.
  - `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
    Claim 5 ("delegation failures" — the model, platform, and practitioner
    controls all worked, yet the organization was still harmed because no
    one had defined who approved the autonomy or owned the policy) and
    Claim 6 (the organizational harness's "capability disclosure" and
    "identity and accountability" requirements): this article's "clear AI
    stance" capability (Claim 11 here — explicit redefinition of where AI
    executes autonomously, where people remain in the loop, and how
    responsibility passes between them) is a shorter, less-elaborated
    restatement of the same organizational-governance-layer requirement.
  - `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` (the "paved roads"
    framework — pre-audited self-service platforms that out-compete shadow-IT
    workarounds on friction): this article's "AI-enabled internal platforms"
    capability (Claim 14 here — "make the safe path the easiest path") is
    the same principle applied specifically to AI-capability platforms
    rather than general software-delivery platforms.
  - `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
    Claim 1 (most enterprise AI failures trace to a missing organizational
    operating system, not model weakness) and this corpus's broader
    "harness/system, not model alone" theme: this article's "strong
    engineering practices" capability (Claim 13 here — "AI amplifies the
    foundations already in place") and its "engineering practice as safety
    net" shift (Claim 9 here — traditional code review alone cannot scale
    with AI-generated change volume) both independently restate that the
    surrounding system, not the model, determines whether AI adoption is
    safe and effective.

- **Contradicts**: None identified and none filed. This article's Claim 1
  (AI-native is unrealistic for most established organizations) is in
  productive tension with, but does not factually contradict, this corpus's
  own guide title and framing, or `blog-anthropic-ai-native-engineering-org.md`
  — Fung's article describes Anthropic's own team, which this article's own
  logic would classify as one of the "small number of companies" that are
  genuinely AI-native (Claude Code's team builds the product it uses,
  arguably closer to "designed around AI from the outset" than a redesigned
  legacy operating model). The two sources describe different populations
  (a company literally building the AI product vs. established enterprises
  redesigning around a third-party AI capability) rather than disagreeing
  about a shared fact, so this is not filed as a contradiction per MINER.md
  §4a's "differ only in context" guidance — but it is a framing tension
  worth the Smith's attention when deciding how the guide itself uses the
  term "AI-native" given that most of its readers are likely to be in the
  "AI-first, not AI-native" population this article describes.

- **Extends**:
  - `blog-thoughtworks-malykhin-quantifying-ai-adoption.md` (a single team's
    8-month adoption journey through individual-productivity experimentation
    toward a durable team workflow): that source is a worked, ground-level
    case study of exactly the "AI-assisted → AI-enabled" transition this
    article names abstractly (Claim 3 here) — Malykhin's team's early
    individual-productivity experimentation phase, followed by settling on a
    team-level workflow, is a concrete instance of the stage-1-to-stage-2
    transition this article's three-stage model describes without a worked
    example of its own.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`: that
    article works out a detailed legal/governance framework (actual vs.
    apparent authority, named oversight tiers, contractual guardrails) for
    exactly the "risk-based tiered autonomy model" this article names in
    Claim 4 but does not itself define.

- **Novel**:
  - **The "AI-native" vs. "AI-first" definitional distinction itself**
    (Claim 1): no prior corpus source explicitly names and contrasts these
    two organizational-maturity targets as distinct, differently-achievable
    goals; prior corpus sources tend to use "AI-native" (including this
    guide's own title) without distinguishing it from a more incremental
    "redesign around AI" target.
  - **"E-shaped" as a named skill-shape vocabulary term** (Claim 6),
    attributed to Marc Andreessen: distinct from, and a specific evolution
    of, the more familiar "T-shaped" skills vocabulary; not previously named
    in this corpus.
  - **"Agent experience" (implicitly, alongside customer experience) as a
    named first-class design consideration** (Claim 12 — "organizations
    therefore need to consider agent experience alongside customer
    experience"): frames legacy-system/API design quality specifically from
    the perspective of what an agent needs to accomplish a task efficiently
    (contrasted with what a human needs), a framing this Miner did not find
    named elsewhere in the corpus's data/API-readiness sourcing.
  - **The three-stage AI-assisted/AI-enabled/AI-first adoption model as a
    named, organization-level maturity framework** (Claim 3): a specific,
    three-tier vocabulary distinct from (though thematically related to)
    other maturity-model framings already in the corpus.

## Guide Impact

- **Chapter 00 (Principles)**: The AI-native/AI-first distinction (Claim 1)
  bears directly on how the guide frames its own ambition level. If the
  guide's title uses "AI-native" as an aspirational end-state, add an
  explicit callout — sourced to this article — that "AI-native" (designed
  around AI from the outset) and "AI-first" (deliberately redesigned around
  AI) are different, differently-achievable targets, and that most readers
  at established organizations should treat AI-first as the realistic goal,
  not a lesser consolation prize. Pair with the closing line (Claim 15):
  "Organizations may never become AI-native, but they can still become
  deliberately and effectively AI-first."

- **Chapter 05 (Team Adoption)**: Add the three-stage adoption model
  (AI-assisted → AI-enabled → AI-first, Claim 3) as a named maturity
  framework for assessing where a team or organization currently sits, and
  the explicit caution that individual-productivity gains "rarely amount to
  organizational transformation" on their own — useful context for any
  section that cites individual-level productivity metrics (e.g. commit
  rates, per-story time savings) as evidence of adoption success. Add the
  "E-shaped" vocabulary (Claim 6) alongside the existing role-blurring
  evidence from `blog-anthropic-ai-native-engineering-org.md` as a named
  conceptual frame for why and how roles are blurring, not just that they
  are.

- **Chapter 02 (Harness Engineering) / Chapter 03 (Verification)**: Add the
  "engineering practice as safety net" argument (Claim 9 — traditional code
  review alone cannot scale with AI-generated change volume, so TDD/BDD
  regain importance as automated verification) as a specific mechanism
  supporting the guide's existing verification-bottleneck content, and the
  "AI amplifies the foundations already in place" framing (Claim 13) as a
  memorable summary line for why engineering-practice maturity is a
  precondition for, not a nice-to-have alongside, AI adoption speed.

- **Chapter 04 (Context Engineering) or wherever AI-ready data is discussed**:
  Add "agent experience alongside customer experience" (Claim 12) as a named
  design consideration, with the ~3-to-~10-month project stretch as an
  illustrative (though unverified, unnamed-client) cautionary anecdote for
  why legacy APIs designed for human interaction can silently multiply an
  agent's required tool-call count.

- **Chapter 05 (Team Adoption) — Governance/Autonomy sections**: Note that
  this article's "risk-based tiered autonomy model" (Claim 4) is asserted
  but undefined here; if citing this article for that phrase, pair it with
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`'s actual
  three-tier oversight structure, which supplies the substance this article
  only gestures toward.

## Extraction Notes

1. **Full verbatim article text obtained via direct HTML fetch, not
   WebFetch summarization.** The article's raw HTML was fetched directly via
   `curl` with a standard browser user agent (HTTP 200) and parsed locally
   with a Python regex-based tag-stripping pass, extracting the complete
   visible body text (byline, publish date, all section headings, all body
   paragraphs). All quotes in this note were copied character-for-character
   from that extraction. The author's profile page
   (thoughtworks.com/profiles/m/may-ping-xu) was fetched the same way to
   confirm her title ("Head of Technology, APAC"), since the article page
   itself carries only the bare byline "By May Xu" with no title or bio.

2. **One verbatim typo preserved from the source, flagged explicitly**: the
   "E-shaped" section (Claim 6) contains the phrase "server adjacent
   disciples," almost certainly intended as "several adjacent disciplines."
   Per MINER.md §2a, quoted text is copied character-for-character rather
   than silently corrected; noted here so the Assayer and Smith do not
   mistake it for a transcription error introduced during extraction, and so
   the guide does not propagate the typo as if it were an intentional term
   of art.

3. **No linked sub-pages were followed.** The article's "More insights"
   footer links (three unrelated Thoughtworks pieces: "Data modernization: A
   practical guide for getting it right," "Bridging the data modernization
   gap," "Top five data modernization strategies for business success") and
   the "Explore a snapshot of today's tech landscape" (Tech Radar) link are
   the page's standard cross-promotion widget, not in-text citations the
   article's argument depends on, per MINER.md §1's "substantive linked
   page" criterion — none was followed.

4. **Two named examples in the article (the legacy modernization project
   and the client whose project stretched from ~3 to ~10 months) are both
   unnamed** — no company, industry, or independently verifiable detail is
   given for either. Spotify is the only named external company in the
   article, and it is cited for its general platform-engineering tooling
   (Backstage, Fleet Management), not for a measured AI-adoption outcome
   specific to Spotify. All three examples are treated as illustrative
   anecdotes, not verified case studies, consistent with how this Miner's
   prior notes have treated comparable single-vendor illustrative examples
   elsewhere in the Thoughtworks cluster.

5. **No contradiction issue filed.** See Cross-References → Contradicts: one
   framing tension with `blog-anthropic-ai-native-engineering-org.md` is
   flagged (this article's own logic would likely classify Anthropic's
   Claude Code team as one of the rare genuinely-AI-native organizations,
   which is a different population from the established enterprises this
   article addresses) but not escalated to a filed issue, since the two
   sources describe different populations rather than disputing a shared
   fact.

6. **Overall confidence rated "anecdotal."** Every claim in this article is
   a framework, named definitional distinction, or prescriptive
   recommendation illustrated with unnamed internal examples or a single
   named company cited for general tooling capability rather than a
   measured AI-adoption outcome. No named client case study, quantified
   before/after metric with methodology, or external statistic is given
   anywhere in the text. The author's senior title (Head of Technology,
   APAC) supports treating the framework itself as a credible practitioner
   synthesis, but does not substitute for missing outcome data — consistent
   with this Miner's "anecdotal" rating for other single-author Thoughtworks
   framework pieces in this corpus that lack a quantified case study (e.g.
   `blog-thoughtworks-buttan-alpha-playbook.md`).
