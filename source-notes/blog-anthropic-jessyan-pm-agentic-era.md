---
source_url: https://claude.com/blog/product-development-in-the-agentic-era
source_type: blog-post
title: "Product development in the agentic era"
author: Jess Yan (Claude Managed Agents product manager, Anthropic)
date_published: 2026-04-29
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: anecdotal
issue: "#466"
---

# Product development in the agentic era

> First-person practitioner account by the Claude Managed Agents PM documenting
> how she uses Claude Code + Managed Agents to shift PM work from administrative
> alignment toward creative craft — introducing the two-tool workflow split
> (Cowork for discovery, Code for building), three concrete agent examples built
> atop Managed Agents, and the "dogfooding-as-design-loop" pattern of building
> against your own pre-production APIs.

## Source Context

- **Type**: blog-post (Anthropic's own claude.com blog, April 29, 2026; part of
  the same Managed Agents practitioner storytelling series as the Vlasenko post
  and the Cowork enterprise post)
- **Author credibility**: Jess Yan is the product manager for Claude Managed
  Agents at Anthropic — the person responsible for the platform this post
  describes. Her account carries insider authority (she builds against
  pre-production APIs) and carries inherent promotional incentive (she is
  publicly making the case for her own product). The workflow specifics and
  agent descriptions are concrete enough to be credible as practitioner evidence;
  the framing around AI's humanizing effect on PM work is personal and
  aspirational rather than measurable.
- **Scope**: Covers one PM's use of Claude Code + Managed Agents to redesign
  her daily workflow, structured around four sections: the product management
  before/now contrast, how she builds agents, three specific agent examples,
  and what has changed about her working day. Does NOT cover: pricing,
  architecture details, team-wide adoption patterns, or failure modes. No linked
  sub-pages; the post is self-contained at roughly 800 words.

## Extracted Claims

### Claim 1: The defining irony of AI-era product management is that it makes the job feel more human, not less — time shifts from administrative alignment to creative craft

- **Evidence**: First-person practitioner observation, explicitly stated as the
  opening thesis. Supported by the before/now workflow contrast that follows.
- **Confidence**: anecdotal (single practitioner account; directionally
  consistent with research-anthropic-ai-transforming-work.md findings on
  AI shifting work toward higher-leverage tasks, but this is self-report)
- **Quote**: "One of the ironies of being a product manager in the age of AI
  is that my work feels more human than ever."
- **Our assessment**: The irony Yan names is the inverse of the "AI replaces
  human work" frame: AI has moved her toward the most distinctly human parts
  of her job (user conversations, ambiguous engineering problems, creative
  product decisions) by automating the administrative and operational work
  that crowded those out. This is a precise and memorable reframe for the
  Ch05 team-adoption discussion of why PMs (not just engineers) should adopt
  AI tools.

### Claim 2: PM work divides into "craft" and "alignment" halves — and AI has shifted time toward craft by absorbing alignment overhead

- **Evidence**: First-person narrative with specific enumeration of what
  "alignment" work consisted of (meetings, status reports, backlogs).
- **Confidence**: anecdotal (self-report; no pre/post measurement)
- **Quote**: "The job of product management has always been a mix of craft
  and alignment." The prior state: "my week was occupied by the latter:
  meetings with cross-functional stakeholders and teammates, status reports,
  and ticket backlogs"
- **Our assessment**: "Craft vs. alignment" is a clean vocabulary for a
  real PM tension: the craft (user insight, product strategy, design judgment)
  is what PMs are hired for; the alignment (stakeholder syncs, status
  communications, backlog grooming) is what consumes the week. Yan's claim
  is that AI absorbs alignment overhead, freeing time for craft. This is the
  PM-specific version of the shift that research-anthropic-ai-transforming-work.md
  documents in engineering contexts ("AI shifts work toward higher-leverage
  tasks").

### Claim 3: Building against pre-production API specs with Claude Code surfaces design problems that document review misses — API shape and UX abstractions were reshaped multiple times based on what prototyping revealed

- **Evidence**: Named outcome from Yan's own team's process: API abstractions
  and Claude Console UX were reshaped "several times" based on prototype
  feedback, not on document review.
- **Confidence**: anecdotal (first-person account; specific and concrete;
  plausible as a practitioner process claim)
- **Quote**: "A spec that reads elegantly in a doc can fall apart the first
  time you try to build against it." And: "We reshaped API abstractions and
  Claude Console UX several times based on what we learned building with our
  own primitives–changes that even a multi-week doc review would never have
  surfaced, and otherwise would've come up too late via user feedback."
- **Our assessment**: "On the AI exponential, we build with what we ship"
  is Yan's formulation of this. The claim is that the prototype loop now
  runs fast enough to substitute for (and outperform) the document review
  loop for API design decisions. This is a concrete, named benefit of
  AI-accelerated prototyping that the guide's Ch01 (daily workflows) section
  can cite as a reason PMs — not just engineers — should reach for Claude Code
  in the design phase.

### Claim 4: A PM can go from zero to a functional end-to-end agent prototype in a single afternoon

- **Evidence**: Direct first-person claim with specific time unit ("an
  afternoon") and mechanism (building against pre-production API specs).
- **Confidence**: anecdotal (self-reported timeline; practitioner claim)
- **Quote**: "With Claude Code, I can sketch out an agent against
  pre-production versions of our API specs, and within an afternoon be
  running a real prototype end-to-end."
- **Our assessment**: The "single afternoon" figure is important because it
  changes the economics of prototyping: if a functional prototype takes a
  week of engineering time, PMs do not build prototypes. If it takes an
  afternoon of PM time, prototyping becomes a design tool, not a development
  commitment. Compare with blog-anthropic-vlasenko-pm-agent-orchestration.md
  Claim 4 (a complete stack rewrite executed in hours during a hackathon
  sprint): both point to AI dramatically reducing the cost of exploratory
  technical decisions. The guide should frame this as a change in who can
  prototype, not just how fast prototyping is.

### Claim 5: Claude Code compresses the "hello world to functional agent" arc to a single sitting

- **Evidence**: Direct practitioner claim about iteration speed within a
  session.
- **Confidence**: anecdotal (self-report; specific and precise)
- **Quote**: "Claude Code gets me from the basic 'hello world' test to a
  functional agent in the same sitting."
- **Our assessment**: This is the most actionable benchmark in the post for
  PMs evaluating whether to try agent building. A single-sitting time horizon
  removes the "I need to block off a week" barrier to entry. Paired with
  Claim 4 (prototype in one afternoon), it gives PMs a concrete time budget:
  hello world to functional prototype in one afternoon.

### Claim 6: The PM workflow now splits cleanly between two tools: Claude/Cowork for open-ended discovery; Claude Code for building custom agents atop Managed Agents

- **Evidence**: Direct practitioner workflow description. Both tools named
  with explicit role assignments.
- **Confidence**: anecdotal (practitioner self-report; specific enough to
  serve as a workflow template)
- **Quote**: "My workflow as a PM now splits cleanly across our products. I
  use Claude and Claude Cowork for open-ended research and discovery–the
  murky, early-stage exploration where I want an ongoing conversation. Once
  I have greater clarity on the job to be done, I use Claude Code to write
  and ship a custom agent for it, built atop of Managed Agents."
- **Our assessment**: This is the most structurally novel claim in the post.
  It names a clear phase boundary: discovery/exploration uses a conversational
  tool (Cowork); implementation uses a code-generating tool (Code). The
  "murky, early-stage" language is key — Cowork is for when the problem is
  not yet well-defined enough to specify to a coding agent. This two-phase
  split is a concrete PM workflow pattern that Ch01 can present alongside
  engineering-centric workflow patterns. It also corroborates blog-anthropic-
  cowork-enterprise.md Claim 6 ("surrounding work first") from a different
  angle: Cowork is used for the pre-specification discovery phase that
  *precedes* the building phase.

### Claim 7: Dogfooding via Claude Code raises the PM's ceiling on what she can imagine shipping — building against your own API reveals what the platform can flex for the next model/task evolution

- **Evidence**: Direct practitioner claim about the design feedback effect
  of dogfooding.
- **Confidence**: anecdotal (self-reported design insight; plausible and
  specific)
- **Quote**: "being able to build against my own product easily raises the
  ceiling on what I can imagine shipping next." And: "As I build these agents,
  I'm able to more concretely anticipate ways our harness and API can flex
  for the next wave of model and task evolution."
- **Our assessment**: The "ceiling on imagination" framing is notable: this
  is not a productivity claim (I work faster) but a scope claim (I can
  imagine more). Dogfooding typically produces feedback on current capabilities;
  Yan's claim extends it: building with Claude Code also generates foresight
  about what capabilities the platform should add next. This is a PM-specific
  argument for dogfooding that goes beyond the standard "find bugs before
  users do" justification.

### Claim 8: Building one Managed Agents instance is simple: load the Managed Agents skill in Claude Code, sketch the job to be done, and Claude builds the agent while explaining integration steps

- **Evidence**: Step-by-step description of Yan's agent-building workflow,
  including a specific CTA to other developers.
- **Confidence**: anecdotal (practitioner account + CTA language that implies
  general applicability)
- **Quote**: "Building one is simple: I load the Managed Agents skill in
  Claude Code and outline a quick sketch of what I'm looking for. After
  invoking this skill, Claude builds the agent, explaining its integration
  steps along the way, so I can easily shift direction as needed."
  And: "Developers can also use the latest version of Claude Code and
  built-in claude-api skill to build with Managed Agents–just prompt Claude
  with 'start onboarding for managed agents in Claude API' to get started."
- **Our assessment**: This is the most concrete onboarding description for
  Managed Agents in the corpus — more actionable than the April 8 product
  announcement (blog-anthropic-claude-managed-agents.md), which described
  capabilities without describing the entry point. The Managed Agents skill
  in Claude Code as a bootstrapping interface is the specific pattern to
  document in Ch02.

### Claim 9: An adoption analytics agent with persistent database access uses memory of prior runs to build on prior findings and continuously advance its analytical perspective

- **Evidence**: First-person description of a production agent Yan built
  and runs for her own PM work.
- **Confidence**: anecdotal (practitioner account; specific enough to be
  credible)
- **Quote**: "An agent with persistent access to our internal databases and
  skills for understanding our data schemas runs queries to surface interesting
  outliers and patterns. With memory of prior runs, it can build on prior
  findings and continuously advance its perspective."
- **Our assessment**: The "memory of prior runs" mechanism is the key
  detail here. This implements exactly the session-layer memory described
  in blog-anthropic-managed-agents-dreaming-outcomes.md Claim 3 ("memory
  lets each agent capture what it learns as it works"). The accumulation
  of analytical perspective across runs — rather than restarting from
  scratch each session — is the practical value of persistent memory for
  operational analytics. No other corpus source documents this pattern with
  a named, in-production use case from a practitioner who built it herself.

### Claim 10: A developer sentiment monitoring agent uses web search + parallel multi-agent fanout to synthesize developer feedback at scale, waiting for all parallel results before synthesizing themes

- **Evidence**: First-person description of a production agent Yan built.
  Explicitly describes the orchestration pattern (fan out to multiple agents,
  wait for results, synthesize).
- **Confidence**: anecdotal (practitioner account; the orchestration pattern
  is specific and architecturally sound)
- **Quote**: "An agent with the pre-built web search tool and guidance on
  focus areas scans a specific list of domains for the latest developer
  feedback, reporting back on common themes. Since there is so much content
  to analyze, it fans out research to multiple agents in parallel, waits for
  results, and synthesizes findings."
- **Our assessment**: This is the scatter-gather orchestration pattern
  applied to research workloads. The explicit "waits for results" language
  confirms sequential synchronization after parallel fanout — classic
  fork-join. As a PM-built production example of multi-agent orchestration,
  it directly corroborates blog-anthropic-multi-agent-coordination-patterns.md
  (the orchestrator-subagent pattern) from a non-engineering practitioner.
  The specific use case (domain scanning for developer feedback) is a
  concrete template for the guide.

### Claim 11: A demo building agent with GitHub repo access, branding assets, and event deck converts prebuilt templates into audience-tailored demos without manual effort

- **Evidence**: First-person description of a production agent Yan built
  for her own operational use.
- **Confidence**: anecdotal (practitioner account; concrete enough to be
  credible)
- **Quote**: "An agent with access to demo GitHub repos, branding assets,
  and an event deck turns prebuilt templates into a polished demo tailored
  to the relevant audience, such as a conference or customer meeting."
- **Our assessment**: This illustrates the "automating the long tail of
  operational work" claim from Claim 12. Demo customization is exactly
  the kind of work that is repeatable, slightly variable per instance, and
  never gets optimized because it is never a high enough priority to
  engineer — until agent building becomes a PM-accessible skill. The
  multi-source input pattern (repos + assets + deck) is a practical example
  of multi-tool agent design.

### Claim 12: Managed Agents cloud sessions enable fire-and-forget workflows — launch, walk away, return to completed work

- **Evidence**: Direct practitioner claim about the workflow change enabled
  by cloud-hosted sessions.
- **Confidence**: anecdotal (self-report; corroborated by the technical
  feature description in blog-anthropic-claude-managed-agents.md Claim 3)
- **Quote**: "Managed Agents sessions run in the cloud, so I can walk away
  and come back to find the work done."
- **Our assessment**: "Walk away and come back" is the user-facing expression
  of the session persistence architecture documented in blog-anthropic-
  scaling-managed-agents.md (Claim 6: session as durable context object
  outside Claude's context window). The practitioner's experience of
  fire-and-forget is the product of the underlying decoupled session design.
  For Ch01 (daily workflows), this is the most accessible statement of
  what long-running agent sessions mean in practice.

## Concrete Artifacts

### PM Two-Tool Workflow Split

```
Jess Yan — PM workflow split (Anthropic, April 2026)
Source: https://claude.com/blog/product-development-in-the-agentic-era

PHASE 1 — Discovery (Claude / Claude Cowork):
  When: "murky, early-stage exploration where I want an ongoing conversation"
  Use: "open-ended research and discovery"
  Trigger to exit: "greater clarity on the job to be done"

PHASE 2 — Building (Claude Code → Managed Agents):
  When: job to be done is clear enough to specify
  Use: "write and ship a custom agent for it, built atop of Managed Agents"
  Entry pattern: "I load the Managed Agents skill in Claude Code and
                  outline a quick sketch of what I'm looking for"
  CTA prompt: "start onboarding for managed agents in Claude API"
```

### Three Production Agent Examples (PM-built)

```
Jess Yan — three operational PM agents (Anthropic, April 2026)
Source: https://claude.com/blog/product-development-in-the-agentic-era

1. ADOPTION ANALYTICS AGENT
   Input:       Persistent access to internal databases + data schema skills
   Operation:   Queries for outliers and patterns
   Memory:      Persistent memory of prior runs; builds on prior findings
   Outcome:     "Continuously advance its perspective" across sessions
   Pattern:     Stateful analytics agent with memory accumulation

2. DEVELOPER SENTIMENT MONITORING AGENT
   Input:       Pre-built web search tool + focus area guidance
   Domains:     Specific list of domains scanned for developer feedback
   Orchestration: Fans out to multiple agents in parallel (scatter-gather)
   Output:      "Common themes" across synthesized parallel results
   Pattern:     Fork-join research aggregation

3. DEMO BUILDING AGENT
   Input:       Demo GitHub repos + branding assets + event deck
   Operation:   Converts prebuilt templates into audience-tailored demos
   Use case:    Conference or customer meetings
   Pattern:     Multi-source template customization
```

### API Design Shift Observation

```
"API design used to live in documents and comment threads;
 on the AI exponential, we build with what we ship."
— Jess Yan, April 29, 2026

Mechanism:
  Before: Spec written in doc → multi-week comment thread review →
          design flaws surface at user feedback stage
  After:  Spec prototyped in Claude Code same day →
          "We reshaped API abstractions and Claude Console UX several times
           based on what we learned building with our own primitives–changes
           that even a multi-week doc review would never have surfaced"

Implication: Prototype loop now faster and more diagnostic than doc review loop
             for API design decisions.
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-vlasenko-pm-agent-orchestration.md** (Claim 1: "I have
    a lot of experience managing real people. I realized this was the same
    thing, only managing agents inside my IDE."): Yan extends this from
    *orchestrating* agents to *building* agents. Vlasenko ran 15+ named
    specialist agents as a PM-orchestrator; Yan builds the agents themselves
    using Claude Code. Together the two sources establish a spectrum: PMs can
    both build and orchestrate agent systems without engineering background.
  - **blog-anthropic-claude-managed-agents.md** (Claim 3: "Long-running
    sessions that operate autonomously for hours, with progress and outputs
    that persist even through disconnections."): Yan's Claim 12 is the
    practitioner expression of this platform feature — the fire-and-forget
    workflow the session persistence architecture enables.
  - **blog-thebatch-ng-pm-bottleneck.md** (Claim 1: "Deciding what to build,
    more than the actual building, is becoming a bottleneck."): Yan is a
    named practitioner enacting Ng's observation. She delegates the building
    (operational analytics, sentiment monitoring, demo customization) to
    agents and redirects her time toward "developing the most impactful
    products." Her account is the strongest practitioner instantiation of
    the PM-bottleneck claim in the corpus.
  - **blog-anthropic-cowork-enterprise.md** (Claim 6: "The vast majority of
    Claude Cowork usage comes from outside engineering teams...surrounding
    work"): Yan's Cowork usage (open-ended research and discovery) is a
    first-person instance of non-engineering Cowork usage. Her workflow is
    the discovery phase that precedes agent building — exactly the surrounding
    work the enterprise data describes.

- **Extends**:
  - **blog-anthropic-claude-managed-agents.md** (Claim 1, the infrastructure
    build problem, and Claim 8, the weeks-vs-months deployment evidence): Yan
    adds the PM perspective — she experiences the "no infrastructure to build"
    benefit without engineering background. The product announcement provided
    enterprise customer testimonials; this note adds the PM-within-Anthropic
    perspective on the same productivity benefit.
  - **blog-anthropic-cowork-enterprise.md** (Claim 6, surrounding-work-first
    adoption): Yan's workflow clarifies the phase boundary: Cowork is not
    "surrounding work" as lower-stakes peripheral tasks — it is the discovery
    and research phase that produces the specification for the agent being
    built in phase 2. This is more structured than the "surrounding work"
    framing suggests.
  - **blog-anthropic-vlasenko-pm-agent-orchestration.md** (Claim 3:
    screenshot-driven UI navigation; Claim 6: non-technical background as
    advantage): Yan's account extends the PM-builds-agents pattern to an
    insider PM with product context, providing a different angle on PM agency
    in agent building: domain expertise over technical background.

- **Contradicts**: None filed. Yan's workflow split (Cowork for discovery,
  Code for building) is novel but opposes nothing in the corpus. Her
  "surrounding work" usage of Cowork (discovery/research) vs. the enterprise
  Cowork note's framing (surrounding work as lower-stakes peripheral tasks)
  is a conditioning variable (solo insider PM vs. cross-functional enterprise
  teams), not a contradiction.

- **Novel**:
  - **Two-tool workflow split as a named PM pattern**: No prior corpus source
    documents a clean Cowork (discovery) → Claude Code (building) phase split
    as a named, reusable PM workflow. The earlier Cowork note describes enterprise
    usage without a phase model; the Vlasenko note describes all-in on Claude Code.
    Yan's split is the first named two-phase workflow in the corpus.
  - **"Dogfooding as ceiling-raiser"**: The claim that building against your own
    product "raises the ceiling on what I can imagine shipping next" is not a
    standard dogfooding justification (catch bugs early, empathize with users).
    It is a scope-expansion claim: implementation experience expands the
    imagination of what to build. No prior corpus source makes this specific claim.
  - **Adoption analytics with memory accumulation**: The pattern of an analytics
    agent with persistent memory that builds on prior findings across sessions —
    "continuously advance its perspective" — is not documented as a named pattern
    in any prior corpus source. blog-anthropic-managed-agents-dreaming-outcomes.md
    discusses memory at the architectural level; this source names the operational
    value in a specific production use case.
  - **PM-built scatter-gather research agent as production example**: The developer
    sentiment agent (web search + parallel fanout + synthesis) is the first named,
    in-production PM-built multi-agent orchestration example in the corpus. Vlasenko
    used 15+ specialist agents built by Claude Code; Yan built a fan-out orchestration
    pattern herself. The practitioner-built scatter-gather is novel.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add Yan's two-tool workflow split as a named
  PM workflow pattern: Cowork for open-ended discovery → Claude Code for building
  custom agents atop Managed Agents. Frame the phase boundary explicitly: "move
  to Claude Code when the job to be done is clear enough to specify." Cite this
  source. The pattern is actionable for any non-engineering role that uses Claude
  for research before needing to automate the output.

- **Chapter 01 (Daily Workflows)**: Add the "build instead of doc review" pattern
  for API design (Claim 3). The guide should note that for PMs and engineers
  working on APIs or platform surfaces: building a prototype against pre-production
  specs with Claude Code surfaces design problems faster than document review.
  Quote: "We reshaped API abstractions and Claude Console UX several times based
  on what we learned building with our own primitives." Pair with the "single
  afternoon prototype" framing from Claim 4.

- **Chapter 02 (Harness Engineering)**: Add the Managed Agents onboarding entry
  point: "load the Managed Agents skill in Claude Code, outline a sketch of what
  you're looking for, prompt 'start onboarding for managed agents in Claude API'."
  This is the lowest-friction entry to Managed Agents building and belongs in any
  "getting started" guidance. Cite this source alongside blog-anthropic-claude-
  managed-agents.md, which describes the platform capabilities but not the entry
  point.

- **Chapter 02 (Harness Engineering)**: The three agent examples (Concrete
  Artifacts) are reusable as illustrative templates: analytics agent (persistent
  DB + memory accumulation), research agent (scatter-gather with synthesis), and
  customization agent (multi-source inputs → tailored outputs). Add these as
  example patterns in any "types of agents PMs or non-engineers can build" section.

- **Chapter 05 (Team Adoption)**: Yan's account is the strongest first-person
  evidence for the "craft vs. alignment" reframe of AI's effect on PM work.
  Specifically: "I'm finally spending real time with our users and my team on
  the part of the job that always mattered most: the craft." Add this as the
  opening motivator for the PM adoption section. The irony framing ("my work
  feels more human than ever") is memorable and accurate as a thesis.

- **Chapter 05 (Team Adoption)**: Add Yan's specific outcome as the PM-role
  case study: from "cross-functional staffing requests, chaotic spreadsheets,
  or half-baked concepts I just never got to try out" to "generating innovative
  ideas with customers, digging into murky and ambiguous problems with my
  engineering counterparts, and investing real creative energy in frontier
  product work." This is the concrete before/after for PM adoption that the
  chapter needs alongside the engineering before/after cases.

## Extraction Notes

- **Source is promotional**: This is Anthropic's own blog featuring its own
  PM describing its own product. The "raises the ceiling on what I can imagine
  shipping next" and "every agent run feels energizing instead of tedious"
  framings are advocacy, not measurement. Extract workflow patterns and agent
  descriptions as practitioner evidence; treat attitudinal claims (energizing,
  feels more human) as framing context rather than measurable outcomes.
- **No sub-pages followed**: The post is self-contained (~800 words) with no
  linked technical resources or sub-pages. Extraction reflects the full depth
  of the source.
- **Author is the subject**: Yan is both the author and the primary evidence
  source. No corroborating testimony from colleagues, no product metrics, no
  code samples. All claims are single-source.
- **Confidence overall: anecdotal**: Claims are specific and concrete (named
  agent patterns, named tools, named outcomes), which raises credibility above
  generic anecdote. But the source is single-subject, self-reported, from an
  Anthropic insider with strong promotional incentive. No claim rises above
  anecdotal confidence. The guide should use this source for direction and
  illustration, not as empirical evidence.
- **Relationship to Vlasenko post**: Both are Anthropic marketing blog posts
  featuring PMs who built with Claude Code. Vlasenko is an outsider winning
  a hackathon; Yan is an Anthropic insider managing the product. Together they
  form a practitioner pair for PM-as-agent-builder patterns. Neither corroborates
  the other's specific claims, but both point in the same direction.
