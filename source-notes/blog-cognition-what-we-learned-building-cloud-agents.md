---
source_url: https://cognition.com/blog/what-we-learned-building-cloud-agents
source_type: blog-post
title: "What We Learned Building Cloud Agents"
author: The Cognition Team
date_published: 2026-04-23
date_extracted: 2026-07-23
last_checked: 2026-07-23
status: current
confidence_overall: emerging
issue: "#2172"
---

# What We Learned Building Cloud Agents

> Cognition's retrospective on "over two years" of building Devin's cloud
> agent infrastructure, arguing the naive containerize-a-CLI-agent approach
> fails on three fronts — shared-kernel security, inability to survive the
> async gaps of the SDLC, and orchestration/governance/integration overhead
> at scale — and that the harder, longer second phase (rebuilding engineering
> processes around "agents execute, humans direct, review, decide") cannot
> even start until that infrastructure exists.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, byline "By The
  Cognition Team," dated "04.23.26" per the page's own byline format — the
  same MM.DD.YY convention and anonymous-team byline pattern used in
  `blog-cognition-devin-cli-terminal.md`, e.g. that post's "04.27.26"). No
  individual author is named. No structured `datePublished` metadata was
  present in the page's `<head>`; the date is taken from the visible byline
  text only.
- **Author credibility**: First-party Cognition practitioner/vendor content
  with no named customer quoted directly (the Itaú statistics are presented
  in the post's own words as a summary, not as a customer testimonial in
  quotation marks) and no independent benchmark or third-party audit of any
  figure. The post does disclose one negative data point about a third party
  ("a leading cloud data platform company... ultimately moved on after the
  project scope overwhelmed their infrastructure team") and attributes a
  specific integration-scale figure to a named third party (Stripe's "internal
  MCP server with over 400 tools," linking to Stripe's own engineering blog
  post on the topic) rather than claiming that figure as Cognition's own
  metric. Treat all Cognition-specific timeframes ("over a year," "three
  quarters," "over two years") as first-party, unaudited, and without stated
  measurement methodology.
- **Scope**: Covers two phases Cognition frames as sequential and both
  necessary: (1) infrastructure — VM-level isolation via microVMs,
  hypervisor-level full-machine-state snapshotting to survive SDLC async
  gaps, and a dedicated orchestration layer for running hundreds of
  concurrent agent sessions with governance and third-party integrations —
  and (2) organizational change management — rebuilding engineering
  processes (staffing, planning, review) around agents executing and humans
  directing. Does **not** cover: any technical detail on how the microVM
  hypervisor or the state-snapshotting mechanism is implemented (no named
  hypervisor technology, e.g. Firecracker, is mentioned); a breakdown of
  which specific engineering roles staff "a dedicated team... to manage each
  layer of this stack"; pricing, session-count, or adoption figures for
  Devin's own cloud infrastructure (the only adoption figures given are for
  the named customer, Itaú); or any comparison of Cognition's build choices
  against a specific named competitor's cloud-agent infrastructure.

## Extracted Claims

### Claim 1: Cognition frames building cloud agent infrastructure as requiring two separate investments — technical infrastructure and organizational change management — and states it has spent "over two years" on both for Devin
- **Evidence**: Opening framing statement immediately following an
  acknowledgment that other companies (citing Stripe's own published
  engineering post) are building homegrown cloud agents and make the path
  "look achievable."
- **Confidence**: anecdotal (a first-party, unquantified timeframe claim
  with no further breakdown of how the two years split across the two
  named investment categories)
- **Quote**: "Building cloud agent infrastructure requires two investments: the technical infrastructure to run agents securely and autonomously in the cloud, and the change management to make agents productive across your engineering org. We've spent over two years on both, for Devin."
- **Our assessment**: This is the post's organizing thesis, and the two-phase
  framing (infrastructure must exist before organizational change management
  can even begin) is the throughline connecting every other claim below. It
  positions the post explicitly as a rebuttal to the idea that
  containerizing a CLI agent is sufficient — the rest of the post is built
  as a list of specific ways that naive approach falls short.

### Claim 2: The "natural" and seemingly straightforward approach to building a cloud agent — containerize a CLI agent and give it repo/toolchain access — successfully moves execution to the cloud but immediately surfaces security, persistence, and orchestration problems that require further solving
- **Evidence**: Direct framing statement opening the "Right Approach" section,
  presented as the strawman the rest of the post argues against.
- **Confidence**: anecdotal (a stated premise/framing, not a benchmarked
  comparison between a containerized approach and Cognition's own
  VM-based approach on the same task)
- **Quote**: "The natural starting point for building cloud agents is straightforward: take a CLI agent, containerize it, and give it access to your repos and toolchain. This successfully moves execution to the cloud — but you quickly run into security, persistence, and orchestration issues that need to be solved."
- **Our assessment**: This sentence sets up the exact three-part structure
  the rest of the infrastructure section follows (Claims 3-4 are the
  security problem, Claim 5 is the persistence problem, Claims 6-7 are the
  orchestration problem) — useful as a compact map of the post's argument,
  but it is Cognition's own characterization of what "naturally" happens
  with a competing architecture, not a documented failure case with
  specifics (no named company or product is cited as having actually hit
  these three problems via the containerized route).

### Claim 3: Containerized agents share a kernel, creating a real security threat because a compromised session's kernel-level escape could reach every other container's filesystem, credentials, and network connections; Cognition states the industry consensus is VM-level isolation, and its own microVM implementation took "over a year of hypervisor engineering" to give every agent session a fully isolated dedicated kernel, storage, networking, and compute
- **Evidence**: Direct security-threat framing plus a stated engineering
  investment figure (over a year) for Cognition's own microVM
  implementation, with an explicit side-benefit claim about VM isolation
  enabling full-browser/desktop-app tool access.
- **Confidence**: emerging (a specific, first-party engineering-investment
  timeframe for a shipped isolation mechanism; the "industry consensus"
  claim is asserted without a citation to a specific competing
  implementation or standard)
- **Quote**: "Containerized agents share a kernel, which means one compromised session can access every other container's filesystems, credentials, and network connections. Agents generate their own code, run arbitrary commands, and probe the environment in unpredictable ways — making a kernel-level escape a real security threat." / "The industry consensus for running untrusted code is VM-level isolation — each workload gets its own kernel, with no shared attack surface." / "Our own implementation of microVMs took over a year of hypervisor engineering, ensuring every agent session runs on its own dedicated kernel with fully isolated storage, networking, and compute." / "A side benefit is that agents running in dedicated VMs can use a full browser, desktop applications, and arbitrary tool stacks, just like a developer on their workstation."
- **Our assessment**: This directly corroborates the isolation-strength
  argument in `blog-anthropic-how-contain-claude.md` Claim 15 (matching
  isolation strength to context/risk) and Claim 14 (battle-tested
  hypervisors, syscall filters, and container runtimes are more reliable
  than custom security components) — a second, independent vendor
  reaching the same VM-over-container conclusion for untrusted agent
  workloads, though Cognition's post gives no equivalent quantified
  before/after metric (contrast that source's Claim 7, which cites an 84%
  permission-prompt reduction and 83% overeager-behavior catch rate for a
  different, OS-sandbox-level containment approach). It also corroborates
  `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 6 (Cloudflare
  sandboxes providing "microVM isolation" as a named feature) — two
  independent infrastructure providers both name microVM-level isolation
  specifically (not just "containers" generically) as their untrusted-code
  isolation boundary of choice. Neither source names the specific
  hypervisor technology used.

### Claim 4: Containerized agents cannot survive the asynchronous gaps inherent to real engineering work — the minutes-to-days delays between opening a PR, waiting on CI, receiving review comments, and pushing follow-up commits — which makes containerization sufficient only for bounded, single-pass work like dependency upgrades, not work that spans the SDLC's async gaps
- **Evidence**: Direct problem statement distinguishing "bounded work" from
  work that "spans the async gaps of the SDLC," framed as the second of
  three problems with the naive containerized approach.
- **Confidence**: anecdotal (a stated architectural distinction with an
  illustrative example category — dependency upgrades — but no named
  case, task-completion-rate figure, or measured boundary for what counts
  as "bounded")
- **Quote**: "Another problem with containerized agents is they cannot survive the async gaps that define most real engineering work. An agent opens a PR, waits on CI, responds to code review, reruns tests, and pushes a follow-up commit. Between each step, there are gaps — minutes, hours, sometimes days — where the agent must preserve its full working state. For bounded work like dependency upgrades, a single-pass agent that completes and exits is enough. But work that spans the async gaps of the SDLC remains out of reach."
- **Our assessment**: This is a specific, citable articulation of *why*
  session persistence matters for agentic coding specifically (not
  generic "long-running jobs" framing) — it ties persistence directly to
  the shape of the software development lifecycle rather than to session
  length alone. It sets up Claim 5's solution and is a useful conceptual
  distinction for the guide: single-pass/bounded tasks vs.
  SDLC-async-gap-spanning tasks as two different infrastructure
  requirements.

### Claim 5: The technical root cause of the async-gap problem is that containers lack a reliable way to snapshot a container's full state, shut down compute, and restore it later — so a containerized agent can only survive gaps by burning compute to stay alive, and loses its session entirely if rescheduled, timed out, or crashed; Cognition's fix was hypervisor-level full-machine-state snapshotting (memory, process trees, filesystem), which it reports "took us longer than any other piece of infrastructure we have built to date"
- **Evidence**: Direct root-cause statement plus a described solution
  (hypervisor-level snapshotting) and an explicit engineering-effort
  superlative claim about the difficulty of making it reliable "across
  thousands of concurrent sessions, each with different repos,
  dependencies, and runtime environments."
- **Confidence**: emerging (a specific, first-party technical mechanism
  description with a comparative effort claim — "longer than any other
  piece of infrastructure" — that is qualitative, not quantified in
  engineer-months or a specific duration the way Claim 3's isolation work
  and Claim 7's orchestration-layer work are)
- **Quote**: "The root issue is that containers do not provide a reliable way to snapshot an individual container's full state, shut down compute, and restore it later. A containerized agent can only survive async breaks by burning compute to stay alive — and if the container is rescheduled, times out, or crashes, the session is lost." / "We solved this by snapshotting full machine state at the hypervisor level — memory, process trees, and filesystem. Compute shuts down while the agent is idle, and the session resumes exactly where it left off when a CI result or review comment arrives. Making this work reliably across thousands of concurrent sessions, each with different repos, dependencies, and runtime environments, took us longer than any other piece of infrastructure we have built to date."
- **Our assessment**: This is the single most mechanically specific
  infrastructure claim in the post — it names the exact technique
  (hypervisor-level, not container-runtime-level, snapshotting of memory +
  process trees + filesystem) and the exact trigger for resuming (a CI
  result or review comment arriving). No prior source in this corpus's
  Cognition or infrastructure-provider coverage names hypervisor-level
  full-machine snapshotting as the specific mechanism for surviving
  agent-session idle gaps; this is new, concrete detail rather than a
  restatement of "the agent works in its own sandbox" framing already
  documented in `blog-cognition-devin-cli-terminal.md` Claim 3 (which
  covers isolation for destructive-command containment, not session
  state persistence across multi-day async gaps).

### Claim 6: Running hundreds of concurrent cloud agents across an engineering org requires solving orchestration, governance, and integrations as three separate multi-quarter infrastructure projects; Cognition states a named-by-description ("a leading cloud data platform company") third party attempted this and abandoned the effort after the project scope overwhelmed its infrastructure team
- **Evidence**: Direct problem-framing statement plus a described,
  anonymized third-party failure case, introducing three sub-problems
  enumerated in the following bullets (Claim 7).
- **Confidence**: anecdotal (an undisclosed-identity third-party anecdote
  with no verifiable company name, timeline, or independently-checkable
  detail — Cognition's own paraphrase of "conversations with teams
  attempting this")
- **Quote**: "Running hundreds of cloud agents across an engineering org requires orchestration, governance, and integrations — each a multi-quarter infrastructure project on its own. A leading cloud data platform company we spoke with attempted this and ultimately moved on after the project scope overwhelmed their infrastructure team."
- **Our assessment**: This is the post's one explicit negative case study
  about a third party (as distinct from Cognition's own admitted
  engineering effort), but it is anonymized and unverifiable — no company
  name, no stated timeframe for the abandoned attempt, and no detail on
  which of the three named sub-problems (orchestration, governance,
  integrations) proved decisive. Cite as an illustrative anecdote
  motivating the scale of the problem, not as a documented case study with
  independently checkable facts.

### Claim 7: The three named sub-problems of running cloud agents at scale are: orchestration (provisioning unique per-session environments, routing, demand-predicting warm VM pools, and keeping environments current as codebases change daily), governance (each session must inherit the dispatching engineer's permissions with every action recorded in a tamper-evident audit trail, requiring identity chaining and access scoping at enterprise scale), and integrations (each external system — CI, monitoring, package registries, docs, source control — has its own auth model and maintenance burden, illustrated by Stripe's own internal MCP server exposing "over 400 tools")
- **Evidence**: Three explicitly labeled bullet points, each with a
  specific description of the sub-problem; the integrations bullet cites a
  named third party's own disclosed figure (Stripe's 400+-tool internal
  MCP server) rather than an anonymized anecdote.
- **Confidence**: settled for the Stripe figure specifically (attributed to
  a named, linkable third-party source — Stripe's own engineering blog);
  anecdotal for the general orchestration/governance problem descriptions
  themselves (Cognition's own first-party framing, not independently
  measured)
- **Quote**: "Orchestration: Each agent session is unique — tied to a specific task and engineer's permissions. Running hundreds concurrently requires provisioning the right environment for each one, routing sessions correctly, predicting demand to keep warm VM pools ready, and keeping every provisioned environment current as codebases change daily." / "Governance: Each session must inherit the dispatching engineer's permissions across every system it touches, with every action recorded in a tamper-evident audit trail. Building and maintaining identity chaining, access scoping, and audit logging at enterprise scale is its own engineering project that requires ongoing maintenance." / "Integrations: An agent is only as useful as the systems it can reach — CI, monitoring, package registries, documentation, source control. Each has its own authentication model, permission scoping, and maintenance burden. Stripe has an internal MCP server with over 400 tools to keep their agents connected. That is the scale of investment this layer demands."
- **Our assessment**: The governance description — every session inheriting
  the dispatching engineer's permissions, with a tamper-evident audit
  trail and identity chaining — is a specific, actionable architectural
  requirement that corroborates and adds enterprise-cloud-agent framing to
  `blog-anthropic-zero-trust-ai-agents.md` Claim 19 (identity-based
  isolation as the primary control for resource boundaries, with network
  segmentation as only a backstop): both sources independently converge on
  per-session, per-identity access scoping — rather than coarse
  network-level trust — as the governance primitive for agent
  infrastructure at scale. The Stripe 400+-tool figure is a concrete,
  attributed data point (not Cognition's own metric) that quantifies just
  how large a single enterprise's internal-tool integration surface can
  become — useful as a citable order-of-magnitude reference distinct from
  any vendor's own claimed figures.

### Claim 8: Cognition states the combined surface area of orchestration, governance, and integrations — not any single one of the three — is what becomes untenable for teams attempting to build this themselves, and reports it currently staffs a dedicated team per infrastructure layer; its own orchestration layer took "over three quarters of dedicated engineering" to build and can now manage "thousands of concurrent VMs," handling provisioning, demand prediction, crash recovery, and teardown
- **Evidence**: Direct closing synthesis of the "Right Approach to Building
  Cloud Agents" section, combining a stated organizational structure
  (dedicated team per layer) with a specific first-party engineering-effort
  figure (three quarters) and a specific first-party capacity figure
  (thousands of concurrent VMs).
- **Confidence**: emerging (specific, first-party quantified effort and
  capacity figures for a shipped, currently-operating system; no stated
  methodology for how "thousands of concurrent VMs" was measured, and no
  team-size figure accompanies "a dedicated team" per layer)
- **Quote**: "The pattern we've seen, across conversations with teams attempting this, is that the combined surface area is what becomes untenable — not any single piece, but the fact that all three have to be built, integrated, and maintained indefinitely. We currently staff a dedicated team to manage each layer of this stack. Our solution for the orchestration layer took over three quarters of dedicated engineering to build and can manage thousands of concurrent VMs — handling provisioning, demand prediction, crash recovery, and teardown."
- **Our assessment**: This is the post's clearest quantified capacity claim
  (thousands of concurrent VMs, three-plus quarters of build time) and its
  clearest organizational-cost claim (a dedicated team per layer,
  indefinitely, not a one-time build). Combined with Claim 3's "over a
  year" microVM figure and Claim 5's "longer than any other piece of
  infrastructure" snapshotting claim, the post's own disclosed timeline
  suggests the full infrastructure stack (isolation + persistence +
  orchestration) took multiple years and several dedicated teams to reach
  its current state — a useful concrete counterpoint for any reader
  evaluating a "just containerize a CLI agent" build estimate against
  Cognition's own multi-year, multi-team account.

### Claim 9: Cognition argues engineering processes designed for a world where humans do the work — how projects get scoped, how teams get staffed, how code gets reviewed and shipped — must be rebuilt around a different operating model once agents perform a significant share of execution: "agents execute and humans direct, review, and decide"
- **Evidence**: Direct architectural/organizational thesis statement opening
  the "Right Approach to Deploying Cloud Agents" section, explicitly framed
  as the second, sequential phase that "cannot start until the agents are
  deployed."
- **Confidence**: anecdotal (a stated organizational design principle, not
  a measured before/after comparison of process outcomes)
- **Quote**: "Every engineering process inside an enterprise was designed for a world where humans do the work: how projects get scoped, how teams get staffed, how code gets reviewed and shipped. When agents are doing a significant share of the execution, those processes need to be rebuilt around a different operating model. One where agents execute and humans direct, review, and decide."
- **Our assessment**: This restates, at the organizational-process level,
  the same human-directs/agent-executes division of labor already argued
  at the architectural level in
  `blog-thoughtworks-gall-supervisory-engineering.md` and the
  scope-and-authority framing in
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` (not
  independently re-verified by claim number in this note, flagged here as
  a topic overlap worth checking during synthesis rather than a confirmed
  cross-reference). Distinctively, Cognition's framing is explicitly
  sequential and gated: the post's structure states organizational change
  management is phase two and "cannot start until the agents are deployed"
  — an explicit ordering claim (infrastructure precedes process change)
  that is not present in Claim 1's framing of the two investments alone.

### Claim 10: Three specific, unresolved organizational questions are named as central to the process-rebuilding phase: engineer fluency (learning what to delegate and how to define tasks precisely, a skill Cognition says "takes months of practice on real projects to develop"), planning and resource allocation (team sizing and sprint capacity assumptions must be continuously revisited, not decided once), and review and quality standards (review processes designed for human-authored code "doesn't transfer cleanly" to a much higher volume of agent-produced code)
- **Evidence**: Three explicitly labeled bullet points under "Getting there
  is both a technical and operational challenge," each naming a specific
  open question with a described symptom.
- **Confidence**: anecdotal (three named organizational challenges
  described qualitatively, with no metric for how long "fluency" actually
  takes beyond the qualitative "months of practice," no specific sizing
  formula for the planning question, and no named review-process standard
  offered as the "high volume" replacement)
- **Quote**: "Engineer fluency: Engineers need to learn which work to delegate and which to keep, and how to define tasks precisely enough that agents execute without constant correction. Managing concurrent agent sessions is a fundamentally different skill from writing code, and it takes months of practice on real projects to develop." / "Planning and resource allocation: Every assumption about team sizing, sprint capacity, and project staffing changes when agent capacity enters the equation. These aren't one-time decisions. They have to be revisited as agents get more capable and engineers get more fluent." / "Review and quality standards: The volume of code that needs review increases dramatically, but the review process designed for human-authored code doesn't transfer cleanly. Teams need to establish what rigorous review looks like for agent-produced work at a much higher volume."
- **Our assessment**: The review-and-quality-standards question directly
  corroborates `blog-cognition-devin-review.md` Claim 1 (Cognition reports
  customers say code review, not code generation, is now the bottleneck to
  shipping, as coding-agent-produced PR volume grows past maintainers'
  ability to understand) — this post names the same review-volume problem
  as one of three named organizational open questions, while the
  Devin Review post treats it as the specific problem statement motivating
  a shipped product. Together the two posts show Cognition using the same
  review-bottleneck observation both as a product justification and as a
  named unsolved organizational-change problem, which is at minimum
  consistent, though this post's framing ("doesn't transfer cleanly," "need
  to establish what rigorous review looks like") reads as more open-ended
  than a solved problem, in some tension with Devin Review's product
  framing of the same issue as the thing that product addresses.

### Claim 11: Cognition cites Itaú, described as the largest private bank in Latin America, as a concrete outcome case for the organizational-change phase: eleven months into adoption with nearly 17,000 engineers, the bank has completed migrations 5 to 6x faster, auto-remediated 70% of static-analysis security vulnerabilities, and increased test coverage by 2x
- **Evidence**: A single blockquoted paragraph naming the customer, its
  scale (17,000 engineers), and three specific outcome metrics, placed
  immediately after the three named open organizational questions and
  before the post's closing paragraph.
- **Confidence**: anecdotal (a single named customer's self-reported or
  Cognition-reported outcome figures, with no stated measurement window
  start/end beyond "eleven months," no methodology for how "5 to 6x
  faster," "70% auto-remediated," or "2x" test coverage were calculated,
  and no comparison cohort or baseline given)
- **Quote**: "Itaú, the largest private bank in Latin America, is eleven months in with nearly 17,000 engineers — and has completed migrations 5 to 6x faster, auto-remediated 70% of static-analysis security vulnerabilities, and increased test coverage by 2x."
- **Our assessment**: This is the only named-customer, quantified outcome
  data point in the entire post — every other figure in the post
  (microVM engineering time, orchestration-layer build time, VM capacity)
  describes Cognition's own infrastructure investment, not a customer
  result. As such it functions as the post's single piece of evidence that
  the two-phase investment (infrastructure, then organizational change) pays
  off, but it is a single named case with no independent verification, no
  stated methodology, and three different metric types (speed, remediation
  rate, coverage) bundled into one sentence with no individual sourcing —
  treat as a headline vendor case-study figure, not a benchmarked result.

## Concrete Artifacts

### Article section structure (headings, in order)
```
Source: cognition.com/blog/what-we-learned-building-cloud-agents,
"By The Cognition Team," 04.23.26

1. (intro, unheaded — two investments framing, referencing Stripe's
   "Minions" cloud-agent post as an example of the homegrown path)
2. The Right Approach to Building Cloud Agents
   - A shared kernel is a security threat
   - Containerized agents can't complete real engineering work
   - Scaling from one session to hundreds requires its own infrastructure
3. The Right Approach to Deploying Cloud Agents
   - Engineering processes need to be rebuilt for agents
   (Itaú outcome blockquote)
   (closing paragraph + CTA: "reach out here" → cognition.ai/contact)
```

### Named figures and timeframes, verbatim
```
Source: cognition.com/blog/what-we-learned-building-cloud-agents

- "over two years" spent on both infrastructure and change management, for Devin
- microVM implementation: "over a year of hypervisor engineering"
- orchestration layer: "over three quarters of dedicated engineering,"
  now manages "thousands of concurrent VMs"
- Stripe's internal MCP server: "over 400 tools" (attributed to Stripe,
  linking to stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)
- Itaú (largest private bank in Latin America): 11 months into adoption,
  ~17,000 engineers, migrations 5-6x faster, 70% of static-analysis
  security vulnerabilities auto-remediated, 2x test coverage increase
```

### Three named orchestration/governance/integration sub-problems, verbatim
```
Source: cognition.com/blog/what-we-learned-building-cloud-agents,
"Scaling from one session to hundreds requires its own infrastructure"

- Orchestration: provisioning per-session environments, routing sessions,
  demand-predicting warm VM pools, keeping environments current as
  codebases change daily
- Governance: sessions inherit the dispatching engineer's permissions,
  every action recorded in a tamper-evident audit trail, identity
  chaining and access scoping at enterprise scale
- Integrations: each external system (CI, monitoring, package registries,
  documentation, source control) has its own auth model, permission
  scoping, and maintenance burden
```

### Three named organizational open questions, verbatim
```
Source: cognition.com/blog/what-we-learned-building-cloud-agents,
"Engineering processes need to be rebuilt for agents"

- Engineer fluency
- Planning and resource allocation
- Review and quality standards
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-how-contain-claude.md` Claim 14 (battle-tested
    hypervisors, syscall filters, and container runtimes are more reliable
    than custom security components) and Claim 15 (matching isolation
    strength to context/risk) — this source's Claim 3 (VM-level isolation
    as the "industry consensus" for untrusted agent workloads, with
    Cognition's own year-plus microVM investment as evidence) is a second,
    independent vendor reaching the same VM-over-container conclusion,
    though neither source names the underlying hypervisor technology and
    this source gives no equivalent quantified before/after metric to that
    source's Claim 7 (84% permission-prompt reduction, 83%
    overeager-behavior catch rate).
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 6 (Cloudflare
    sandboxes providing "microVM isolation" as a named feature) — this
    source's Claim 3 corroborates microVM-level isolation specifically
    (not generic containers) as the isolation boundary of choice from a
    second infrastructure provider.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 19 (identity-based
    isolation as the primary resource-boundary control, with network
    segmentation as only a backstop) — this source's Claim 7 (each agent
    session inheriting the dispatching engineer's permissions, with
    per-action tamper-evident audit trails and identity chaining) is an
    independently-arrived-at, enterprise-cloud-agent-specific instance of
    the same per-identity-scoping-over-network-trust governance principle.
  - `blog-cognition-devin-review.md` Claim 1 (customers report code review,
    not code generation, is now the bottleneck to shipping, as
    coding-agent PR volume grows past reviewer capacity) — this source's
    Claim 10 names "review and quality standards" as one of three
    unresolved organizational questions in near-identical terms ("the
    review process designed for human-authored code doesn't transfer
    cleanly... at a much higher volume"), giving the same observation both
    a product-justification framing (in the Devin Review post) and an
    open-organizational-problem framing (here).

- **Contradicts**: None identified. No claim in this source conflicts with
  an existing source note's claim under matching conditions. This source's
  claims are largely about Cognition's own infrastructure-build timeline
  and organizational-change framing, a topic this corpus's existing
  Cognition cluster (multi-agent coordination, product announcements,
  productivity measurement) does not otherwise cover in comparable detail,
  so no direct tension was found.

- **Extends**:
  - `blog-cognition-devin-cli-terminal.md` — that source's Claim 7
    describes Devin CLI's Autonomous mode containing shell/network access
    via OS-level sandbox scopes for a *local* terminal agent; this source's
    Claim 3 describes the analogous but architecturally distinct choice
    for *cloud* Devin sessions — full VM-level (microVM) isolation with a
    dedicated kernel per session, rather than OS-level sandboxing within a
    shared kernel. The two sources together give this corpus's most
    complete picture yet of Cognition's isolation strategy across both
    surfaces: OS-level sandbox scopes locally, full microVM isolation in
    the cloud.
  - `blog-cognition-devin-review.md` — see Corroborates above; this
    source's Claim 10 extends that post's product-level problem statement
    into a named, still-open organizational-change question rather than a
    solved-by-this-product framing.
  - `blog-anthropic-claude-managed-agents-selfhosted.md` — that source
    documents self-hosted sandbox *options* customers can plug into
    Anthropic's Managed Agents platform (Daytona, Cloudflare, Modal,
    Vercel); this source documents one vendor's (Cognition's) account of
    building the equivalent isolation and orchestration layer itself,
    end-to-end, rather than delegating to a third-party sandbox provider —
    a build-vs-integrate contrast worth noting if the guide discusses
    infrastructure sourcing options for cloud agent isolation.

- **Novel**:
  - **Hypervisor-level full-machine-state snapshotting (memory, process
    trees, filesystem) as the specific mechanism for surviving multi-day
    async SDLC gaps** (Claim 5): No prior corpus source names this exact
    technique or ties it explicitly to the shape of the SDLC (PR → CI →
    review → rerun) rather than to session length or idle-timeout policy
    generically.
  - **A disclosed, anonymized third-party failure case of an enterprise
    abandoning its own cloud-agent orchestration build** (Claim 6): This
    corpus has vendor-reported success cases and Cognition's own disclosed
    negative results about its own products
    (e.g. `blog-cognition-multi-agents-working.md` Claim 10's SWE-1.5
    admission), but this is the first instance of a vendor citing another
    company's abandoned infrastructure attempt as evidence for the
    difficulty of the underlying problem.
  - **A specific, attributed third-party integration-scale figure** (Stripe's
    400+-tool internal MCP server, Claim 7): a concrete, externally
    sourced order-of-magnitude reference for how large a single
    enterprise's agent-tool integration surface can grow.
  - **An explicit two-phase, sequentially-gated framing of cloud-agent
    adoption** — infrastructure must be built before organizational change
    management can even begin (Claim 1, Claim 9) — as the entire post's
    organizing structure. Prior corpus sources address either the
    infrastructure question or the organizational-change question; this
    source's explicit claim that phase two "cannot start until the agents
    are deployed" is a stated ordering dependency not previously
    documented.
  - **A single named enterprise customer's bundled outcome figures for the
    organizational-change phase specifically** (Itaú: 5-6x faster
    migrations, 70% auto-remediated vulnerabilities, 2x test coverage,
    Claim 11) — distinct from this corpus's other Cognition productivity
    evidence (`blog-cognition-devin-productivity-estimation.md`'s
    258-session internal estimator study), this is a single-customer,
    multi-metric result with no stated methodology, offered as an
    outcome case rather than a measurement methodology.

## Guide Impact

- **Chapter 02 (Harness Engineering) / Agent Infrastructure**: Add Claim 3
  (VM-level microVM isolation as the "industry consensus" for untrusted
  agent workloads, with a concrete year-plus engineering cost figure) and
  Claim 5 (hypervisor-level full-machine snapshotting as the specific
  mechanism for surviving SDLC async gaps) as concrete infrastructure
  requirements for any team considering building cloud agent execution
  in-house, cross-referenced with `blog-anthropic-how-contain-claude.md`'s
  isolation-strength framing and
  `blog-anthropic-claude-managed-agents-selfhosted.md`'s third-party
  sandbox-provider options as a build-vs-integrate alternative.

- **Chapter 02 (Harness Engineering) / Chapter 04 (Orchestration and
  Governance)**: Add Claim 7's three-part orchestration/governance/
  integrations breakdown, specifically the governance sub-claim (per-session
  identity inheritance with tamper-evident audit trails) as a named
  requirement, cross-referenced with
  `blog-anthropic-zero-trust-ai-agents.md` Claim 19's identity-based
  isolation principle — two independent vendors converging on
  per-identity scoping over network-level trust as the governance
  primitive for agent infrastructure at scale.

- **Chapter 01 (Daily Workflows) or Chapter 00 (Principles)**: Add Claim 9's
  explicit two-phase, sequentially-gated framing (infrastructure precedes
  organizational change management) as a caveat for readers evaluating
  "we're rolling out AI agents" initiatives — Cognition's own account
  suggests the harder, longer-duration work (engineer fluency, planning
  revisions, review-standard rebuilding) only starts once the
  infrastructure phase is substantially complete, which may explain slow
  perceived ROI in early-stage rollouts.

- **Chapter 03 (Patterns and Anti-Patterns)**: Add Claim 10's three named
  organizational open questions (engineer fluency, planning/resource
  allocation, review/quality standards) as a checklist of unresolved
  problems teams should expect to face during agent adoption, rather than
  one-time decisions — particularly flagging that Cognition itself
  describes these as ongoing, revisited-over-time problems rather than
  problems with a fixed solution.

## Extraction Notes

- WebFetch was not used for primary-quote extraction on this source. The
  article was instead fetched directly via `curl` with a browser
  user-agent, the `<article>` element isolated by regex, and HTML tags
  stripped with the `html2text` tool — the same verbatim-verification
  approach documented in this corpus's other Cognition source notes
  (e.g. `blog-cognition-multi-agents-working.md`,
  `blog-cognition-devin-cli-terminal.md` Extraction Notes). One HTML→text
  conversion artifact was caught and corrected: the "Containerized agents
  can't complete real engineering work" heading rendered with a stray
  space ("can 't") in the `html2text` output due to how it handled the
  `&#x27;` HTML entity; the raw HTML was checked directly to confirm the
  source's actual apostrophe placement before using the heading text
  anywhere in this note.
- The full article is short (~1,050 words across two major sections, no
  numbered footnotes) — this is a shorter source than several other
  Cognition posts in this corpus (contrast the ~2,400-word
  `blog-cognition-multi-agents-working.md`). All eleven claims above were
  extracted from the complete article body; no section was skipped or
  condensed.
- One linked page — Stripe's own "Minions" cloud-agent engineering post
  (stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents),
  referenced both in the intro (as the example of a homegrown build) and
  in the integrations bullet (as the source of the "400 tools" figure) —
  was identified as a substantive, directly relevant linked page under
  MINER.md §1's "follow up to 5 linked pages" allowance, but was **not**
  separately fetched and mined for this note; the 400-tools figure and the
  "homegrown cloud agent" characterization are both taken from this
  source's own paraphrase/attribution, not independently verified against
  Stripe's original post. A search of `source-notes/` found no existing
  note for the Stripe post — it is a candidate for a future, separate
  source submission if a fuller account of Stripe's own build (and a
  verification of the "over 400 tools" figure against Stripe's own
  wording) is wanted.
- No contradiction meeting the MINER.md §4a filing bar was identified
  during cross-referencing. This source's claims describe Cognition's own
  infrastructure-build timeline and organizational-change framing, which
  did not conflict with any existing source note's claims on the same
  specific points; where topics overlapped (isolation strategy, governance
  design, review bottlenecks) the relationship was corroboration or
  extension, not disagreement.
- Cross-references verified before writing: re-read
  `blog-anthropic-how-contain-claude.md` in full and confirmed Claims 3, 5,
  7, 14, and 15 by number and content; re-read
  `blog-anthropic-claude-managed-agents-selfhosted.md` in full and
  confirmed Claim 6 by number and content; re-read
  `blog-anthropic-zero-trust-ai-agents.md` in full and confirmed Claim 19
  by number and content; re-read `blog-cognition-devin-review.md` in full
  and confirmed Claim 1 by number and content; re-read
  `blog-cognition-devin-cli-terminal.md` in full and confirmed Claim 3 and
  Claim 7 by number and content; re-read
  `blog-cognition-multi-agents-working.md` in full and confirmed Claim 10
  by number and content (cited only in this note's Extraction Notes as a
  comparison point, not as a numbered cross-reference in the main text).
  `blog-thoughtworks-gall-supervisory-engineering.md` and
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` are named
  in Claim 9's assessment only as topic-overlap candidates for a future
  synthesis pass — their specific claim numbers were **not** verified
  against this source's Claim 9 and are explicitly flagged as unconfirmed
  rather than cited as a resolved cross-reference. No claim number was
  guessed or approximated for any source cited as a confirmed
  cross-reference.
- Confidence is rated `emerging` overall: this source combines a
  consistent first-party account with several specific, named engineering-
  effort timeframes (over a year for microVMs, three-plus quarters for
  orchestration) and one attributed third-party figure (Stripe's 400+
  tools) that exceed pure marketing/philosophy framing, but nearly every
  figure lacks a stated measurement methodology, the one named-customer
  outcome case (Itaú) bundles three different metric types into a single
  unsourced sentence, and the one third-party failure case (the
  unnamed "leading cloud data platform company") is anonymized and
  unverifiable — so it does not reach `settled`.
