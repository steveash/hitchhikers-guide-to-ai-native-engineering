---
source_url: https://cognition.com/blog/introducing-devin-desktop
source_type: blog-post
title: "Introducing Devin Desktop"
author: Scott Wu and Jeff Wang (Cognition)
date_published: 2026-06-02
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: emerging
issue: "#2003"
---

# Introducing Devin Desktop

> Cognition's announcement of Devin Desktop, "the next generation of
> Windsurf," which makes the Agent Command Center (a unified Kanban view
> for local and cloud agents) the IDE's default surface, introduces
> Spaces for cross-agent context sharing, adds Agent Client Protocol
> (ACP) support so third-party agents (Codex, Claude Agent, OpenCode)
> run alongside Devin with identical UI treatment, and replaces Cascade
> with a Rust-rewritten local agent — validated by first-party
> testimonials from five named customers (Ramp, Harvey, NVIDIA, Modal,
> Intact Financial).

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  06.02.26 per the page's byline, i.e. 2026-06-02; byline "By Scott Wu
  and Jeff Wang" — Scott Wu is Cognition's CEO and Jeff Wang is named
  only by that byline in this source, with no further title given). The
  post explicitly hands off to a second, companion post for
  implementation detail: "You can read the full product details on the
  Devin blog," linking to `devin.ai/blog/windsurf-is-now-devin-desktop`
  (byline "Cognition," June 2, 2026, "4 min read"). Both posts were
  fetched in full for this note; quotes below are attributed to
  whichever of the two pages they actually appear on.
- **Author credibility**: First-party product announcement from the
  company that builds Devin and now owns Windsurf, published on both
  Cognition's and Devin's own blogs simultaneously. This is vendor
  marketing content for a shipped, downloadable product (the post ends
  with "Download Devin Desktop today" / "Download Devin Desktop"), not
  independent or practitioner-authored. Five named customers are quoted
  by name, title, and company — more third-party validation than the
  single-customer pattern seen in `blog-cognition-auto-triage.md`
  (one named quote, Hari Subbaraj @ Modal) — but all five testimonials
  are hosted on Cognition's own page, not independently published, and
  none includes a quantified metric (no accuracy rate, time saved, or
  incident/task count from any of the five).
- **Scope**: Covers the product-philosophy framing (engineers shifting
  from pair-programming to agent management), the Agent Command Center
  becoming the default IDE surface with a unified Kanban view, Spaces
  as a context-sharing mechanism, ACP support and the three named
  launch-supported third-party agents, IDE backwards-compatibility with
  Windsurf/VSCode, Devin Local as a from-scratch Rust rewrite of Cascade
  with a stated token-efficiency figure, the "one Devin, every surface"
  four-surface unification (Desktop/Cloud/CLI/Review), five customer
  testimonials, and the migration path for existing Windsurf users. Does
  **not** cover: any accuracy, adoption, session-duration, or
  cost/pricing metric for Devin Desktop itself; the technical
  implementation of ACP support (how third-party agent state/auth is
  isolated, whether Spaces context is shared with third-party ACP
  agents identically to Devin); a worked example or screenshot
  walkthrough of the Kanban view or a Space; the methodology or
  baseline behind the "30% more token efficient" Devin Local figure; or
  any detail on how Devin's "use the best model for each task" model
  routing actually interacts with a user-added ACP agent that has its
  own model choice.

## Extracted Claims

### Claim 1: Cognition frames the core shift in software engineering work as moving from pair-programming with one agent to managing multiple agents — scoping/planning work, delegating to cloud agents, reviewing progress, and deciding what reaches production
- **Evidence**: Direct framing statement following a reference to the
  earlier Windsurf 2.0 launch, presented as an observed trend across
  "the best engineers we work with."
- **Confidence**: emerging (first-party framing citing unnamed
  "best engineers," no survey data, adoption number, or named
  practitioner behind the generalization)
- **Quote**: "Since then, one thing has become increasingly clear: the work of software engineers is shifting towards agent management." "The best engineers we work with are not just pair programming with one agent at a time. They are using agents to scope and plan work, delegating tasks to cloud agents, reviewing progress, and deciding what makes it to production." (cognition.com/blog/introducing-devin-desktop)
- **Our assessment**: This is the post's thesis statement and the
  motivating premise for every feature described afterward (Agent
  Command Center, Spaces, ACP support). It generalizes the local/cloud
  agent-role division already documented in
  `blog-cognition-devin-in-windsurf.md` (Claim 5: local for
  planning/prototyping/iteration, cloud for
  implementation/testing/QA/deployment) into a broader claim that
  managing *multiple* agents — not just handing off to one cloud agent
  — is becoming the engineer's core activity. No data backs the "best
  engineers" generalization; treat as vendor thesis, not a measured
  workforce trend.

### Claim 2: Devin Desktop makes the Agent Command Center the IDE's default surface, giving a single unified Kanban view for managing every local and cloud agent
- **Evidence**: Direct feature description appearing on both posts, with
  the companion post adding the specific UI mechanism ("Kanban view")
  that the primary post does not name.
- **Confidence**: emerging (concrete, shipped feature description; no
  screenshot, walkthrough, or independent confirmation of the Kanban
  mechanic in this note beyond the vendor's own text)
- **Quote**: "Devin Desktop makes the Agent Command Center the default surface in the IDE, so you can manage local and cloud agents, PRs, and context from one place." (cognition.com/blog/introducing-devin-desktop) / "Devin Desktop puts them in one place, and makes the Agent Command Center the default surface: you manage every local and cloud agent from a single Kanban view." (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: The Agent Command Center itself is not new to
  Cognition's product line — this post's own opening line states
  "Earlier this year, we launched Windsurf 2.0 with the Agent Command
  Center and Devin inside Windsurf" — but making it the IDE's *default*
  surface, and naming the specific "Kanban view" mechanic, is new,
  quotable detail this corpus did not previously have (see Cross-References
  → Extends for why: the earlier Windsurf 2.0 launch post could not be
  verbatim-quoted when it was fetched for `blog-cognition-devin-in-windsurf.md`).

### Claim 3: Spaces is introduced as a new mechanism letting related agents share context by grouping sessions, PRs, files, and context together
- **Evidence**: Direct feature description on both posts.
- **Confidence**: emerging (concrete, named, shipped feature; no
  walkthrough of what "sharing context" looks like mechanically —
  e.g., whether agents see each other's full transcripts or a
  summarized handoff — and no example Space is shown)
- **Quote**: "We built Spaces to enable related agents to share context, so they can collaborate effectively on tasks." (cognition.com/blog/introducing-devin-desktop) / "We're also introducing Spaces, a new way to share context between agents while grouping sessions, PRs, files, and context." (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is the most novel mechanism claim in the
  post for this corpus — a named, product-level answer to "how do
  multiple agents working on related tasks avoid re-deriving context
  from scratch." Like Claim 2, "Spaces" is not entirely new
  terminology at Cognition (the unquotable Windsurf 2.0 launch post
  reportedly had a "Windsurf Spaces" section per
  `blog-cognition-devin-in-windsurf.md`'s Extraction Notes), but this
  is the first source in this corpus with actual quotable claims about
  what Spaces does. No detail is given on the underlying mechanism
  (shared context window? shared retrieval index? manual grouping
  only?), so this should be cited as a named capability, not an
  implementation pattern.

### Claim 4: Devin Desktop supports the Agent Client Protocol (ACP), letting any ACP-compatible agent run alongside Devin inside the IDE; at launch this includes Codex, Claude Agent, OpenCode, and custom in-house agents
- **Evidence**: Direct feature description with an explicit rationale
  (model-agnosticism extended to agent-agnosticism) and a named list of
  launch-supported agents, more detailed on the companion post.
- **Confidence**: emerging (concrete, named, shipped integration
  surface; no detail on how third-party agent execution is sandboxed,
  billed, or how conflicts between agents are resolved)
- **Quote**: "With support for the Agent Client Protocol (ACP), we are extending that same idea to agents running in Devin Desktop. Any ACP-compatible agent can run inside Devin Desktop alongside Devin, so teams can use the agents that work best for different parts of the development lifecycle and manage them from the same surface." (cognition.com/blog/introducing-devin-desktop) / "Devin Desktop launches today with support for the Agent Client Protocol (ACP), an open-source protocol that lets any compatible agent run inside any ACP-compatible editor. At launch, Devin Desktop supports Codex, Claude Agent, OpenCode, and any other ACP-compatible agents - including agents built by your team in-house." (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is a concrete, named instance of a vendor
  building a multi-agent IDE surface around an open protocol rather
  than a closed, single-agent product — the explicit rationale given
  ("Devin has been built to use the best model for each task instead
  of being tied to a single model... extending that same idea to
  agents") reframes model-agnosticism as agent-agnosticism. This
  corroborates and extends `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`
  Claim 1, which documents ACP as the mechanism letting GitHub Copilot
  run as a guest agent inside JetBrains' own AI Assistant product — see
  Cross-References for how the two differ (guest-in-host vs.
  multiple-guests-alongside-a-native-agent).

### Claim 5: Third-party ACP agents receive identical interface treatment to Devin itself — they appear in the same Kanban view, run inside Spaces, share context with other agents, and are organized and reviewed the same way as a native Devin session
- **Evidence**: Direct statement on the companion post only (not present
  on the primary cognition.com post), specifying the concrete UI parity
  claim.
- **Confidence**: emerging (specific parity claim for a shipped feature;
  no screenshot or example showing a third-party agent's session inside
  the Kanban view or a Space)
- **Quote**: "Third-party agents get the same interface as Devin: they show up in the Kanban view, run inside Spaces, and share context with other agents. You organize and review their work the same way you would any Devin session." (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is the most concrete, falsifiable version of
  the "agent-agnostic surface" claim in Claim 4 — it specifically
  asserts that Codex, Claude Agent, and OpenCode sessions are not
  second-class citizens inside Devin Desktop's UI, down to sharing the
  same Spaces context-sharing mechanism described in Claim 3. Whether
  "share context with other agents" means a third-party agent can read
  a Devin agent's session context (and vice versa) inside the same
  Space, or only that they appear grouped together, is not specified.

### Claim 6: Devin Desktop remains a full IDE with an agent manager built in, not the reverse — editor, extensions, keybindings, LSPs, terminal, and workflows are preserved and fully backwards-compatible with Windsurf (and VSCode)
- **Evidence**: Direct statement of product philosophy on both posts,
  with the companion post adding the explicit "IDE first" framing.
- **Confidence**: emerging (product-philosophy and compatibility claim;
  no independent verification that existing Windsurf/VSCode extensions,
  keybindings, or LSP configurations actually carry over without
  modification)
- **Quote**: "When that happens, your editor, extensions, keybindings, LSPs, terminal, and workflows matter, so we built the agent manager into the full IDE, which remains fully backwards-compatible with Windsurf." (cognition.com/blog/introducing-devin-desktop) / "Devin Desktop is a full IDE with an agent manager built in — not the other way around. The editor, extensions, keybindings, LSPs, and workflows you rely on are all there and backwards-compatible with Windsurf and VSCode." (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This directly extends
  `blog-cognition-devin-in-windsurf.md`'s framing that "the IDE still
  matters to serious developers" for local work, review, and QA — this
  post makes explicit that adding a default multi-agent management
  surface (Agent Command Center) is not meant to replace the IDE, only
  to sit alongside it as the default entry point. No specific example
  of a previously-broken extension or LSP is given as evidence of
  successful compatibility.

### Claim 7: Devin Local, a from-scratch Rust rewrite and successor to Cascade, is up to 30% more token-efficient and supports "modern features like subagents," with legacy Cascade remaining available through July 1st for incremental migration
- **Evidence**: Direct feature description under the "Introducing Devin
  Local" section, giving a specific percentage figure and a named
  migration deadline; appears only on the companion post, not the
  primary cognition.com announcement.
- **Confidence**: anecdotal (the "30% more token efficient" figure is
  given with no baseline, benchmark methodology, task set, or
  measurement window — a bare percentage claim in the same evidentiary
  class as `blog-google-conductor-plugin-antigravity.md` Claim 5's
  unquantified "higher success rate," except this claim at least
  attaches a number, so it is graded anecdotal rather than the weaker
  "no figure at all" case)
- **Quote**: "We're also introducing Devin Local, which is the successor to Cascade as our primary local agent. The Cognition team has completely rewritten the local agent from scratch in Rust, supporting the same capabilities and settings as Cascade. Devin Local is up to 30% more token efficient and supports modern features like subagents. For incremental migration, you can still continue to use the legacy Cascade agent through July 1st." (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is the single most concrete engineering claim
  in either post — a named language rewrite (Rust), a specific
  (if unverified) efficiency figure, a named new capability
  (subagents), and a hard migration deadline (July 1st). "Up to 30%"
  is a ceiling figure, not an average or typical figure, and no
  comparison methodology (which workloads, which token-counting
  method, compared against which Cascade version) is disclosed — this
  should be cited in the guide, if at all, as an unverified vendor
  efficiency claim, not a benchmarked result.

### Claim 8: Cognition frames Devin as now unifying "one agent, same context" across four distinct surfaces — Devin Desktop (agent manager with a full IDE), Devin Cloud (autonomous long-running agent on its own cloud machine), Devin CLI (in the terminal), and Devin Review (code review on every diff)
- **Evidence**: Direct enumeration under the "One Devin, every surface"
  section heading, framed as an evolution from Windsurf and Devin being
  separate products.
- **Confidence**: emerging (a named four-surface product taxonomy for a
  shipped/announced product line; no detail on how "same agent, same
  context" is technically achieved across the four surfaces, e.g.
  whether a session started in Devin CLI can be picked up mid-task in
  Devin Desktop)
- **Quote**: "We started with Windsurf and Devin as separate products. Now, Devin can run across your entire stack. Same agent, same context, regardless of where you run it: Devin Desktop: Agent manager with a full IDE. Devin Cloud: The autonomous and long-running Devin agent running on its own machine in the cloud. Devin CLI: The intelligence of Devin in your terminal. Devin Review: Code review on every diff." (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is a useful, citable taxonomy for "what does
  a single vendor's multi-surface agent product line actually consist
  of" — four named surfaces mapped to four distinct usage contexts
  (IDE-based management, autonomous cloud execution, terminal, code
  review). The "same agent, same context" claim is the more interesting
  and less-substantiated half: no example is given of context actually
  persisting across a surface switch (e.g., start in CLI, continue in
  Desktop), so this should be read as an architectural goal statement,
  not a demonstrated capability.

### Claim 9: Existing Windsurf users receive Devin Desktop as a standard over-the-air update with unchanged plan, pricing, and extensions; new users can download it directly
- **Evidence**: Direct migration-path statement in the closing "Get
  started" section.
- **Confidence**: emerging (a stated rollout mechanism and pricing
  continuity claim for existing customers; not independently verified
  by this note, and no rollout timeline or percentage of users migrated
  is given)
- **Quote**: "If you're on Windsurf, the update will arrive as a standard over-the-air update. Your plan, pricing, extensions, and other features remain the same: Devin Desktop is a new look for the product you already love." (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: A low-friction migration claim (no re-purchase, no
  extension loss) for existing customers — consistent with the
  "backwards-compatible" framing in Claim 6, but this is the pricing/
  plan-continuity half specifically. No detail on what happens to a
  user who does not want to receive the update, or whether Cascade's
  July 1st sunset (Claim 7) is enforced regardless of update timing.

### Claim 10: Ramp reports using Devin Desktop to dispatch and monitor its array of agents from a single command center, partnering with Cognition to bring the agents Ramp engineers already use into one shared workspace
- **Evidence**: Named customer testimonial, attributed to Shaiyon
  Hariri, Research Engineer at Ramp.
- **Confidence**: anecdotal (single named practitioner at a single
  customer, vendor-hosted quote, no incident/session count, time-saved
  figure, or accuracy measure given)
- **Quote**: "Devin Desktop makes it easy to dispatch and monitor our array of agents from a single command center. We're excited to partner with Cognition to bring the agents Ramp engineers already use into one shared workspace, making it easier to jump between tasks, preserve context, and get more done." — Shaiyon Hariri, Research Engineer (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is a direct customer-side echo of Claim 2's
  "unified Kanban view for local and cloud agents" claim — "dispatch
  and monitor our array of agents from a single command center" is the
  practitioner-facing restatement of the vendor's own Agent Command
  Center description. It should be read as corroborating that at least
  one named customer uses the multi-agent-dispatch workflow the post
  describes, not as evidence of how many agents, how often, or with
  what success rate.

### Claim 11: Harvey reports that Devin Desktop's support for custom background agents extends its internal background agent Spectre's organizational context (spanning legal research, engineering, product, and design teams) to every engineer's laptop
- **Evidence**: Named customer testimonial, attributed to Joey Wang,
  Engineering Lead at Harvey, naming Harvey's own internal agent
  ("Spectre") by name.
- **Confidence**: anecdotal (single named practitioner at a single
  customer; the claim that context "now extends to every engineer's
  laptop" is stated without any measurement of coverage, adoption
  percentage, or before/after comparison)
- **Quote**: "At Harvey, we built our internal background agent, Spectre, to work across long-running engineering efforts while carrying organizational context for our legal research, engineering, product, and design teams to seamlessly collaborate. With Devin Desktop's support for custom background agents, that context now extends to every engineer's laptop, so humans and agents work from the same shared understanding instead of starting from scratch." — Joey Wang, Engineering Lead (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is the most concrete named-customer instance
  of the ACP/custom-agent-support claim (Claim 4) — Harvey's own
  in-house agent (Spectre) is explicitly the kind of "agent built by
  your team in-house" the companion post's ACP section names as
  supported. This gives Claim 4's "including agents built by your team
  in-house" a single, named, cross-functional (legal, engineering,
  product, design) real-world instance, though still with zero
  measurement of how much friction it actually removes.

### Claim 12: NVIDIA is joining Cognition's research preview for multi-agent support in Devin Desktop, with an engineering lead stating their engineers run multiple agents across complex workflows every day
- **Evidence**: Named customer testimonial, attributed to Subhash
  Ranjan, Engineering Lead - AI Tools at NVIDIA, explicitly naming a
  "research preview" program.
- **Confidence**: anecdotal (single named practitioner; explicitly
  describes a "research preview" — i.e., a pre-GA, limited-availability
  program — rather than general-availability customer usage; no
  detail on research-preview scope, duration, or participant count)
- **Quote**: "NVIDIA is joining Cognition's research preview for multi-agent support in Devin Desktop. Our engineers run multiple agents across complex workflows every day, and we're excited to help define how they share context and coordinate in one place." — Subhash Ranjan, Engineering Lead - AI Tools (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is the one testimonial that explicitly flags
  itself as pre-GA ("research preview," "excited to help define how
  they share context and coordinate") rather than settled production
  usage — it should be read as NVIDIA co-designing the multi-agent
  coordination feature (Spaces, per Claim 3) rather than reporting an
  established outcome, distinct in kind from Ramp's and Harvey's
  present-tense usage claims (Claims 10-11).

### Claim 13: Modal, describing itself as a design partner on multi-agent support, reports Devin Desktop as the first tool letting its engineers manage all their agents together with shared context from one place
- **Evidence**: Named customer testimonial, attributed to Rahul
  Chalamala, Member of Technical Staff at Modal, explicitly naming a
  "design partner" relationship.
- **Confidence**: anecdotal (single named practitioner; explicit
  superlative "the first tool" is Modal's own characterization, not an
  independently verified market claim)
- **Quote**: "We've been working closely with Cognition as a design partner on multi-agent support in Devin Desktop. Our engineers run multiple agents every day and Devin Desktop is the first tool that lets them manage all of them together, with shared context, from one place." — Rahul Chalamala, Member of Technical Staff (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: Modal is the second named "design partner" (after
  NVIDIA's "research preview" framing) in these testimonials, suggesting
  multi-agent support in Devin Desktop was co-developed with at least
  two named customers before this public launch. The "first tool" claim
  is Modal's own subjective assessment relative to whatever tools
  Modal's engineers had tried previously — not a comparative benchmark
  against named competitors.

### Claim 14: Intact Financial reports that Devin Desktop gives its teams the same intelligent agent experience as before but with the full permissions and flexibility of their local machines, describing it as "snappier" and "more accessible" for hands-on development work
- **Evidence**: Named customer testimonial, attributed to Ciprian
  Nechita, Senior IT Architect at Intact Financial.
- **Confidence**: anecdotal (single named practitioner; "snappier" and
  "accessible" are qualitative impressions with no latency figure, no
  before/after benchmark, and no description of what tool or workflow
  is being compared against)
- **Quote**: "Devin Desktop gives our teams the same intelligent agent experience, but with the full permissions and flexibility of their local machines. For development work that benefits from a faster, more hands-on environment, it's a natural fit. It's snappier, it's accessible, and it fits the way a lot of our developers are working today." — Ciprian Nechita, Senior IT Architect (devin.ai/blog/windsurf-is-now-devin-desktop)
- **Our assessment**: This is the one testimonial that speaks
  specifically to the local-execution value proposition (full
  permissions and flexibility of local machines) rather than the
  multi-agent-management theme common to the other four — it reads as
  a customer-side echo of Claim 6 (IDE/local backwards-compatibility)
  rather than of the Agent Command Center or Spaces claims. No latency
  number backs "snappier."

## Concrete Artifacts

### Full "Agent Command Center" and "Spaces" framing, verbatim (primary post)
```
Source: cognition.com/blog/introducing-devin-desktop, "By Scott Wu and Jeff Wang," 06.02.26

"Devin Desktop makes the Agent Command Center the default surface in
the IDE, so you can manage local and cloud agents, PRs, and context
from one place. We built Spaces to enable related agents to share
context, so they can collaborate effectively on tasks."
```

### Full "Devin Desktop is not just for Devin" section, verbatim (companion post)
```
Source: devin.ai/blog/windsurf-is-now-devin-desktop, "Cognition," June 2, 2026

"Devin Desktop is not just for Devin
Devin Desktop launches today with support for the Agent Client Protocol
(ACP), an open-source protocol that lets any compatible agent run
inside any ACP-compatible editor. At launch, Devin Desktop supports
Codex, Claude Agent, OpenCode, and any other ACP-compatible agents -
including agents built by your team in-house.
Third-party agents get the same interface as Devin: they show up in
the Kanban view, run inside Spaces, and share context with other
agents. You organize and review their work the same way you would any
Devin session."
```

### "One Devin, every surface" list, verbatim (companion post)
```
Source: devin.ai/blog/windsurf-is-now-devin-desktop

Devin Desktop: Agent manager with a full IDE
Devin Cloud: The autonomous and long-running Devin agent running on
  its own machine in the cloud
Devin CLI: The intelligence of Devin in your terminal
Devin Review: Code review on every diff
```

### All five customer testimonials, full text and attribution (companion post)
```
Source: devin.ai/blog/windsurf-is-now-devin-desktop, testimonial carousel (5 of 5)

Ramp — Shaiyon Hariri, Research Engineer:
"Devin Desktop makes it easy to dispatch and monitor our array of
agents from a single command center. We're excited to partner with
Cognition to bring the agents Ramp engineers already use into one
shared workspace, making it easier to jump between tasks, preserve
context, and get more done."

Harvey — Joey Wang, Engineering Lead:
"At Harvey, we built our internal background agent, Spectre, to work
across long-running engineering efforts while carrying organizational
context for our legal research, engineering, product, and design teams
to seamlessly collaborate. With Devin Desktop's support for custom
background agents, that context now extends to every engineer's
laptop, so humans and agents work from the same shared understanding
instead of starting from scratch."

NVIDIA — Subhash Ranjan, Engineering Lead - AI Tools:
"NVIDIA is joining Cognition's research preview for multi-agent
support in Devin Desktop. Our engineers run multiple agents across
complex workflows every day, and we're excited to help define how they
share context and coordinate in one place."

Modal — Rahul Chalamala, Member of Technical Staff:
"We've been working closely with Cognition as a design partner on
multi-agent support in Devin Desktop. Our engineers run multiple
agents every day and Devin Desktop is the first tool that lets them
manage all of them together, with shared context, from one place."

Intact Financial — Ciprian Nechita, Senior IT Architect:
"Devin Desktop gives our teams the same intelligent agent experience,
but with the full permissions and flexibility of their local machines.
For development work that benefits from a faster, more hands-on
environment, it's a natural fit. It's snappier, it's accessible, and it
fits the way a lot of our developers are working today."
```

### Devin Local section, verbatim (companion post)
```
Source: devin.ai/blog/windsurf-is-now-devin-desktop, "Introducing Devin Local"

"We're also introducing Devin Local, which is the successor to Cascade
as our primary local agent.
The Cognition team has completely rewritten the local agent from
scratch in Rust, supporting the same capabilities and settings as
Cascade. Devin Local is up to 30% more token efficient and supports
modern features like subagents.
For incremental migration, you can still continue to use the legacy
Cascade agent through July 1st."
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`
    Claim 1 (GitHub Copilot became reachable inside JetBrains AI
    Assistant "via the Agent Client Protocol (ACP)," an open-source
    protocol connecting a guest agent to a host IDE) — this note's
    Claim 4 (Devin Desktop supporting Codex, Claude Agent, and OpenCode
    as ACP-compatible guest agents) is a second, independent vendor
    building on the same named protocol, corroborating that ACP is
    emerging as a genuine cross-vendor standard for multi-agent IDE
    composition rather than a single company's proprietary mechanism.
    The two cases differ in shape: the JetBrains case is one guest
    agent (Copilot) reachable inside a host product's own picker,
    while this source's Claim 5 describes multiple third-party guest
    agents receiving full UI parity (same Kanban view, same Spaces)
    alongside a native agent (Devin) — a broader composition model than
    a single guest-agent integration.
  - `blog-cognition-auto-triage.md` Claim 3 ("spin up sub-Devins to
    investigate in parallel") — thematically corroborates that
    Cognition has an established, shipped pattern of coordinating
    multiple agent instances on related work; this note's Spaces
    (Claim 3) generalizes that pattern from same-product sub-agent
    parallelism (multiple Devin instances on one incident) to
    cross-product, cross-vendor agent coordination (Devin plus
    third-party ACP agents sharing a grouping of sessions/PRs/files).

- **Contradicts**: None identified. No claim in this source conflicts
  with an existing source note's claim under matching conditions.

- **Extends**:
  - `blog-cognition-devin-in-windsurf.md` — this is the direct,
    named product-evolution successor to the post that note documents
    ("We're excited to announce Devin Desktop - the next generation of
    Windsurf"). That note's Claim 5 (task taxonomy: local for
    planning/prototyping/iteration, cloud for
    implementation/testing/QA/deployment) and Claims 7-8 (Windsurf 2.0's
    single-click plan-to-Devin handoff, PR review back in Windsurf) are
    extended here from a one-off delegation loop into a persistent,
    default multi-agent management surface (Agent Command Center,
    Claim 2 here) plus a named cross-agent context-sharing mechanism
    (Spaces, Claim 3 here) that did not exist in that note's described
    mechanics. That note's Extraction Notes also record that the
    original Windsurf 2.0 launch post reportedly already had "The Agent
    Command Center" and "Windsurf Spaces" as named sections, but could
    not be verbatim-quoted at the time (WebFetch returned only a
    paraphrased summary) — this source is therefore the first place in
    this corpus with actual, verbatim, citable claims about what Agent
    Command Center and Spaces do, even though the feature *names* are
    not new to Cognition's product line.
  - `blog-cognition-auto-triage.md` — see Corroborates above; this
    source's Spaces mechanism is a more general context-sharing
    primitive than that note's sub-Devin parallel-investigation
    pattern, extending "multiple Devin instances coordinate" toward
    "multiple agents, including third-party ones, share a grouped
    context."

- **Novel**: The Agent Client Protocol (ACP) support enabling named
  third-party agents (Codex, Claude Agent, OpenCode, plus in-house
  agents) to run inside Devin Desktop with full UI parity to Devin
  (Claims 4-5) is new to this corpus — no prior Cognition source
  documents multi-vendor agent composition inside a Cognition-built
  surface. Devin Local as a from-scratch Rust rewrite of Cascade with a
  stated (unverified) 30% token-efficiency figure and subagent support
  (Claim 7) is entirely new — no prior source in this corpus names
  "Cascade" or "Devin Local" at all. The explicit four-surface
  unification framing — Desktop, Cloud, CLI, Review, described as "same
  agent, same context" (Claim 8) — is also new; prior Cognition sources
  in this corpus describe Devin as a cloud agent and Windsurf as a
  local IDE integration, but none previously named a CLI or Review
  surface as part of a single unified product line. The five named,
  multi-company customer testimonial set (Claims 10-14) is the largest
  named-customer validation block for any single Cognition source in
  this corpus (prior largest was one, in `blog-cognition-auto-triage.md`).

## Guide Impact

- **Chapter 01 (Daily Workflows) / Chapter 02 (Harness Engineering)**:
  Add Claim 1 (the framing shift from "pair programming with one agent"
  to "agent management" as the described core engineer activity) and
  Claim 2 (Agent Command Center as the IDE's default surface, unified
  Kanban view for local+cloud agents) as the most current, concrete
  vendor articulation of a multi-agent-management IDE workflow,
  updating the guide's existing single-vendor local/cloud coverage
  (`blog-cognition-devin-in-windsurf.md`) with the product's next
  iteration. Flag clearly that "the best engineers we work with" is an
  unsupported generalization with no survey or adoption data behind it.

- **Chapter 02 (Harness Engineering)**: Add Claims 4-5 (ACP support,
  named launch agents Codex/Claude Agent/OpenCode, and the explicit UI-parity
  claim for third-party agents) as a concrete, named example of an IDE
  vendor building an open, multi-agent composition surface rather than
  a closed single-agent product — pair with
  `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claim
  1 to show ACP adoption from two independent vendors in the same
  guide section. Note that neither source discloses the underlying
  isolation/sandboxing model for a third-party agent's execution.

- **Chapter 04 (Context Engineering)**: Add Claim 3 (Spaces:
  cross-agent context sharing via grouped sessions, PRs, files, and
  context) as a named, shipped mechanism for the "how do multiple
  related agent sessions avoid re-deriving context independently"
  problem. Flag that the underlying sharing mechanism (full transcript
  access vs. summarized handoff vs. manual grouping only) is
  undisclosed — this is a capability-exists claim, not an
  implementation pattern the guide can currently describe mechanically.

- **Chapter 01 (Daily Workflows)**: If the guide covers local-agent
  tooling choices, add Claim 7 (Devin Local: Rust rewrite of Cascade,
  claimed up to 30% more token-efficient, adds subagent support, with
  Cascade sunsetting after July 1st) as a concrete example of a vendor
  replacing an existing local agent implementation for efficiency —
  explicitly caveat the 30% figure as an unquantified, no-methodology
  vendor claim, in the same evidentiary tier as
  `blog-google-conductor-plugin-antigravity.md` Claim 5's unquantified
  "higher success rate" claim.

## Extraction Notes

- Two pages were read in full: the primary source
  (`cognition.com/blog/introducing-devin-desktop`) and the companion
  post it explicitly links to for "full product details"
  (`devin.ai/blog/windsurf-is-now-devin-desktop`) — following that link
  per MINER.md §1's "follow up to 5 linked pages that seem substantive"
  guidance, since the primary post is short (~330 words) and defers
  most concrete detail (customer testimonials, Devin Local, the
  four-surface taxonomy, the migration path) to the companion page
  entirely. No other linked pages (site nav, prior-article links) were
  judged substantive to this topic.
- WebFetch's summarizing pass was used for an initial read of both
  pages, then every quote used above was independently verified against
  a raw HTML fetch (`curl` with a browser user-agent, HTML tags stripped
  via a Python regex script) of both pages, following the same
  verification approach documented in
  `blog-google-conductor-plugin-antigravity.md`'s Extraction Notes. This
  was necessary because WebFetch's small-model summarizer gave two
  different, both truncated, fragments of the Intact Financial
  testimonial across two separate fetch attempts (a Claim 14 candidate
  quote and a shorter alternate ending); the raw HTML fetch resolved
  this to the single, full, correct testimonial quoted in Claim 14 and
  Concrete Artifacts. All quotes in this note are taken from the raw,
  tag-stripped HTML text, not from any WebFetch summarizer output.
- Cross-references verified before writing: re-read
  `blog-cognition-devin-in-windsurf.md` in full and confirmed Claims 5,
  7, and 8 by number and content, and confirmed its Extraction Notes'
  account of the unquotable Windsurf 2.0 launch post; re-read
  `blog-cognition-auto-triage.md` in full and confirmed Claim 3 by
  number and content; re-read
  `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` in
  full and confirmed Claim 1 by number and content; re-read
  `blog-google-conductor-plugin-antigravity.md` in full and confirmed
  Claim 5 by number and content. No claim number was guessed or
  approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified.
  One candidate was considered and rejected: this source's framing that
  the Agent Command Center and Spaces are becoming the IDE's *default*,
  central surface could be read as being in tension with
  `blog-cognition-devin-in-windsurf.md`'s framing of Windsurf as
  primarily a place to "think" and plan before a one-click handoff to
  Devin. This is not a same-claim conflict: the earlier post describes
  a one-way plan → delegate → review loop between exactly two agents
  (a local Windsurf agent and cloud Devin); this post describes a
  persistent management surface for an arbitrary number of concurrent
  local, cloud, and third-party agents. The newer post is best read as
  a superset/evolution of the same underlying product, not a
  contradicting claim about how the same feature behaves — no
  contradiction issue filed.
