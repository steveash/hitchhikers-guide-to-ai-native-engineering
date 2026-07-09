---
source_url: https://blog.jetbrains.com/blog/2026/07/07/jetbrains-ai-for-teams-and-organizations-from-fragmented-ai-usage-to-coordinated-software-development/
source_type: blog-post
title: "JetBrains AI for Teams and Organizations: From Fragmented AI Usage to Coordinated Software Development"
author: Oleg Koverznev (JetBrains)
date_published: 2026-07-07
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: emerging
issue: "#1674"
---

# JetBrains AI for Teams and Organizations: From Fragmented AI Usage to Coordinated Software Development

> JetBrains announces "JetBrains AI for Teams and Organizations" — a vendor-agnostic,
> org-level coordination layer (managed cloud agents/automations, shared repository
> context, centralized governance via JetBrains Central, and MCP/ACP-based open
> integrations) rolling out gradually to business customers through July–August 2026,
> paired with a commercial-model shift from per-seat AI licenses to on-demand AI
> credits valid for twelve months.

## Source Context

- **Type**: blog-post (official JetBrains AI blog, published 2026-07-07; product
  announcement, ~900 words across an intro, a "what becomes available this summer"
  section with five named capabilities, a pricing-model section, a rollout-timeline
  section, and a closing "Looking ahead" section; author Oleg Koverznev, discovered
  via the trusted `jetbrains-ai` feed)
- **Author credibility**: First-party JetBrains vendor announcement, not bylined to
  an individual beyond the named author. Authoritative for what JetBrains is
  building, why, and the stated rollout timeline. Not independently verified: no
  benchmark, customer case study, screenshot, or named early-adopter is included in
  this post (contrast with `blog-jetbrains-codex-recommended-agent.md`, which
  discloses a specific benchmark methodology, or `blog-anthropic-admin-analytics-cost-controls.md`,
  which includes named customer testimonials). This post is announcement-level, not
  evidence-level, for every capability it describes.
- **Scope**: Covers five new organizational capabilities (team automations/cloud
  agents, JetBrains Context, JetBrains Central, JetBrains Central CLI, open
  integrations via MCP/ACP), the shift from AI licenses to AI credits, and a
  rollout timeline. Does NOT cover: specific pricing numbers for AI credits,
  technical implementation detail for any of the five capabilities (no
  architecture diagrams, API docs, or config examples), a list of which specific
  IDEs or CLI tools are governed by JetBrains Central CLI beyond three named
  examples, or any quantified outcome (no adoption, cost-savings, or productivity
  figures). No sub-pages were followed; a "prev post" footer link points to
  `blog-jetbrains-caveman-token-savings-test.md`, already in the corpus, and an
  "Explore the new offering" link to a separate marketing microsite was not
  followed as it falls outside the "read the entire source" scope of a single
  announcement post.

## Extracted Claims

### Claim 1: JetBrains frames its new offering as solving an explicit fragmentation problem — individual developer productivity gains are offset by organizational costs when there is no shared system across the different AI tools developers use
- **Evidence**: Stated as the article's problem framing, immediately preceding the product announcement.
- **Confidence**: emerging (vendor framing of a problem it is selling a solution to; plausible but not independently measured — no data on fragmentation costs is given)
- **Quote**: "But without a shared system, that freedom comes at a cost. Individual developers become more productive, while organizations are left with fragmented workflows, isolated context, and growing costs."
- **Our assessment**: This is the standard "individual tool adoption outpaces organizational coordination" narrative also present in `blog-jetbrains-agentic-ai-governance.md` (governance framed as a response to ungoverned agent capability) but stated here specifically about *tool proliferation* rather than *agent risk*. The claim that developer flexibility and organizational control are in tension is asserted, not measured — no metric for "growing costs" or "isolated context" is given anywhere in the post.

### Claim 2: JetBrains explicitly rejects vendor lock-in as the solution to fragmentation — teams should not have to standardize on a single AI vendor to be productive
- **Evidence**: Stated directly as a value statement preceding the fragmentation-cost framing (Claim 1).
- **Confidence**: settled (direct, unambiguous statement of company position)
- **Quote**: "That freedom is a good thing. Teams shouldn't have to standardize on a single vendor to benefit from AI."
- **Our assessment**: This positions JetBrains' offering explicitly against a competing strategy (vendor consolidation) rather than as a mere feature list. It is consistent with `blog-jetbrains-codex-recommended-agent.md` Claim 9, where JetBrains itself publishes explicit use-case carve-outs to its own recommended-agent default rather than pushing a single winner — both sources show JetBrains positioning multi-vendor flexibility as a deliberate product stance, not an unaddressed gap.

### Claim 3: Team automations let developers run agents in managed cloud environments so long-running engineering tasks execute independently while remaining visible and shared across the team, triggered by repository events, schedules, or other workflows
- **Evidence**: Direct feature description in the "What becomes available this summer" section, under "Team automations and cloud agents."
- **Confidence**: settled (first-party description of an announced, not-yet-fully-shipped capability — status is "rolling out" per the rollout-timeline section, Claim 9)
- **Quote**: "Developers will be able to run agents in managed cloud environments, allowing long-running engineering tasks to execute independently while remaining visible and shared between team members. Teams will be able to create automations that trigger cloud agents in response to repository events, schedules, or other engineering workflows."
- **Our assessment**: This three-trigger taxonomy (repository events, schedules, other workflows) is functionally the same shape as the three-axis taxonomy (scheduled / API-triggered / webhook-triggered) `blog-anthropic-claude-code-routines.md` Claim 2 documents for Claude Code Routines, and both explicitly position the managed-cloud-execution model as the replacement for self-managed cron/scheduling infrastructure — Routines' Claim 1 names "cron jobs, infrastructure, and additional tooling like MCP servers" as what it eliminates; this post does not name the infrastructure being replaced as explicitly, but the "visible and shared between team members" framing adds a team-coordination angle Routines' single-developer framing does not emphasize.

### Claim 4: JetBrains Context is a shared repository-intelligence layer intended to reduce how much agents need to explore a codebase before acting, thereby lowering execution cost and improving code quality
- **Evidence**: Direct feature description under "JetBrains Context."
- **Confidence**: emerging (stated causal mechanism — faster context access reduces agent turns, cost, and improves quality — is plausible but no before/after measurement is given in this post)
- **Quote**: "JetBrains Context will provide agents with the repository intelligence they need to understand complex codebases more efficiently, helping them spend less time exploring and more time executing. Fast access to cross-repository knowledge, code examples, and references will reduce agent turns, lower execution costs, and improve code quality."
- **Our assessment**: This is a specific, testable mechanism claim ("reduce agent turns, lower execution costs, improve code quality") stated with no supporting benchmark in this post. It is the kind of claim the JetBrains team itself has elsewhere been willing to empirically test and publish (see `blog-jetbrains-caveman-token-savings-test.md`, where the same blog ran a controlled benchmark on a token-savings claim and found the marketed figure overstated by ~7.6x). No equivalent test accompanies this claim — it should be tracked as an unverified vendor claim pending a follow-up benchmark, not treated as measured.

### Claim 5: JetBrains Central provides organization-wide management tools for AI adoption — centralized visibility into which AI tools teams use, plus governance, access management, model and agent controls, policies, analytics, and cost attribution across teams
- **Evidence**: Direct feature description under "JetBrains Central."
- **Confidence**: settled (first-party description of the product's stated capability scope)
- **Quote**: "JetBrains Central will provide organization-wide management tools for AI adoption, giving engineering leaders centralized visibility into the AI tools their teams use, as well as governance, access management, model and agent controls, policies, analytics, and cost attribution across teams."
- **Our assessment**: This is the concrete product implementation of the abstract governance principles `blog-jetbrains-agentic-ai-governance.md` lays out — that source's Claim 13 explicitly names JetBrains Central as the referenced example ("JetBrains Central was built to address this: bringing governance into the development infrastructure itself, rather than treating it as something bolted on after AI workflows are already in production"). This post is the first corpus source to enumerate JetBrains Central's actual feature list (visibility, governance, access management, model/agent controls, policies, analytics, cost attribution) rather than referencing it only as a named example.

### Claim 6: JetBrains Central CLI extends the same organizational governance, visibility, and analytics to third-party terminal-based agent tools — specifically naming Claude Code, Codex, and Gemini CLI — without requiring developers to change which tool they use
- **Evidence**: Direct feature description under "JetBrains Central CLI."
- **Confidence**: settled (first-party description; the three named tools are a specific, checkable claim about integration scope)
- **Quote**: "Developers increasingly use different AI tools such as Claude Code, Codex, and Gemini CLI. JetBrains Central CLI will bring these workflows into the same organizational environment, providing governance, visibility, and analytics, while allowing developers to continue working in the tools they already prefer."
- **Our assessment**: This is the most concrete evidence in the post that JetBrains Central's governance layer is designed to reach *outside* JetBrains' own product surface — into the terminal-based agent category the guide already covers extensively (Claude Code, Codex, Gemini CLI). This corroborates `blog-jetbrains-codex-recommended-agent.md`, which documents JetBrains AI Chat already offering Claude Agent and other ACP-compatible agents as switchable options — that post covered agent *selection* inside a JetBrains surface; this post covers organizational *governance* extending outward to tools running entirely outside any JetBrains surface (a plain terminal), which is a materially different integration depth.

### Claim 7: The offering is vendor-agnostic by design, connecting external tools via MCP and external agents via ACP, so organizations can evolve their AI stack without sacrificing governance or developer choice
- **Evidence**: Direct statement under "Open integrations."
- **Confidence**: settled (direct statement of architectural design choice)
- **Quote**: "Organizations rarely rely on a single AI tool. JetBrains AI for Teams and Organizations is vendor-agnostic by design, connecting external tools via MCP and external agents via ACP, so organizations can evolve their AI stack without sacrificing governance or developer choice."
- **Our assessment**: This confirms MCP (Model Context Protocol) and ACP (Agent Client Protocol — JetBrains' own product post for the June 30, 2026 GitHub Copilot integration, `blog-jetbrains-copilot-integrated-agent.md` Claim 2, names "ACP Registry" as the specific product surface for this mechanism) as the two named integration protocols underpinning JetBrains' entire multi-vendor governance strategy, not just the individual agent-picker feature documented in the Copilot and Codex notes. This is the first corpus source to state that the *organizational governance* layer itself (not just IDE-level agent selection) is built on the same two protocols.

### Claim 8: JetBrains is replacing per-seat AI licenses with flexible, on-demand AI credits for business customers, explicitly to support transparent and sustainable pricing without hidden fees, subsidized packages, or unexpected cost increases
- **Evidence**: Direct statement in the "From AI licenses to AI credits" section, stating both the mechanism and the stated rationale.
- **Confidence**: settled (direct statement of a commercial-model change and its stated rationale)
- **Quote**: "We believe companies need transparent and sustainable pricing as they adopt AI and agentic development at scale. This means no hidden fees, no deeply subsidized packages, and no proxy pricing that can lead to unexpected cost increases later."
- **Quote**: "For business customers, we will transition from AI licenses to flexible on-demand AI credits."
- **Our assessment**: This is a vendor-level pricing-model shift analogous in shape (though not in mechanism) to GitHub's own Effective-Tokens-to-AI-Credits migration documented in `blog-ghaw-ai-credits-migration.md` — both vendors are moving toward a credit-denominated spend unit, though GitHub's AIC is explicitly a fixed dollar conversion (1 AIC = $0.01 USD, that note's Claim 7) while this JetBrains announcement gives no equivalent conversion rate or dollar-per-credit figure. The rhetorical similarity ("AI credits" as the new unit name) across two unrelated vendors making unrelated changes is notable as a naming-convention trend, but the underlying mechanisms are not documented as equivalent — this note does not have enough detail from JetBrains to compare the two credit systems directly.

### Claim 9: AI credits are valid for twelve months, versus one month for the prior AI license model, making it easier for organizations to reallocate AI investment between developers over time
- **Evidence**: Direct statement in the "From AI licenses to AI credits" section, giving the specific validity-period comparison.
- **Confidence**: settled (specific, checkable numeric claim about the new commercial terms)
- **Quote**: "AI credits make it easier for organizations to reallocate AI investments between developers and manage them over time, as credits are valid for longer (twelve months as opposed to one month)."
- **Our assessment**: The twelve-months-vs-one-month validity comparison is the single most concrete, falsifiable commercial detail in the post. It directly supports the reallocation use case: a manager can now shift unused AI spend from a light user to a heavy user within a 12-month window rather than losing unused capacity every 30 days. No prior corpus source documents a credit-validity-period change of this specific magnitude for enterprise AI tooling.

### Claim 10: AI credits are designed to eventually extend beyond LLM token consumption, covering payment for additional JetBrains services not yet introduced
- **Evidence**: Direct forward-looking statement in the "From AI licenses to AI credits" section.
- **Confidence**: anecdotal (forward-looking statement of intent with no named services, timeline, or specifics)
- **Quote**: "Furthermore, AI credits will eventually go beyond LLM tokens and will be able to be used to pay for new services we plan to introduce in the near future."
- **Our assessment**: This is the vaguest claim in the post — no services are named, and "near future" has no date attached. It signals JetBrains intends AI credits to become a general-purpose internal currency for its platform, not just an LLM-usage unit, but this should be treated as a stated intention, not a shipped or scoped capability.

### Claim 11: The new capabilities will roll out gradually to business customers throughout July and August 2026, while individual and non-commercial users will see minimal changes in the near term
- **Evidence**: Direct statement in the "A gradual rollout" section.
- **Confidence**: settled (explicit, dated rollout statement from the vendor)
- **Quote**: "The improved capabilities will become available gradually to business customers throughout July and August. Individual and non-commercial users will mostly not be exposed to these changes and new capabilities yet."
- **Our assessment**: This dates every capability claim in this note (Claims 3–8) as "announced, rolling out July–August 2026" rather than "already generally available" as of the July 7, 2026 publish date. For the guide, any citation of JetBrains Central, JetBrains Context, Team Automations, or JetBrains Central CLI should carry this rollout-status caveat, and `last_checked` on this note should be revisited after August 2026 to confirm the capabilities actually shipped as described.

### Claim 12: JetBrains frames its long-term direction as building an open system connecting developers, AI agents, and organizations without forcing a single model, interface, or workflow — with IDEs remaining the place developers do hands-on coding, surrounded by coordination services
- **Evidence**: Closing "Looking ahead" section, stated as the article's strategic thesis.
- **Confidence**: anecdotal (strategic/directional statement, not a specific product commitment)
- **Quote**: "Our direction is to build an open system that connects developers, AI agents, and organizations without forcing customers into a single model, interface, or workflow."
- **Quote**: "JetBrains IDEs remain where developers do their best hands-on coding. Around them, we're building the services that help teams coordinate AI work across repositories, terminals, agents, and cloud execution environments."
- **Our assessment**: This closing framing positions the IDE as the durable center of JetBrains' strategy, with every new capability in this post (Central, Context, Automations, Central CLI) explicitly described as built "around" the IDE rather than replacing it — even though JetBrains Central CLI (Claim 6) explicitly reaches into terminal-only tools with no IDE involvement at all. This is a minor internal tension worth flagging: the strategic narrative centers the IDE, but the most vendor-agnostic capability described (Central CLI) is the one least dependent on anyone using a JetBrains IDE at all.

## Concrete Artifacts

### Five new capabilities announced for Summer 2026 rollout (JetBrains AI blog, July 7, 2026)

```
1. Team automations and cloud agents
   - Managed cloud environments for long-running agent execution
   - Visible/shared across team members
   - Triggers: repository events, schedules, other engineering workflows

2. JetBrains Context
   - Repository intelligence layer for agents
   - Goal: fewer exploration turns, lower execution cost, better code quality
   - Cross-repository knowledge, code examples, references

3. JetBrains Central
   - Org-wide AI adoption management
   - Centralized visibility, governance, access management,
     model/agent controls, policies, analytics, cost attribution

4. JetBrains Central CLI
   - Extends governance/visibility/analytics to terminal-based agents
   - Named tools: Claude Code, Codex, Gemini CLI
   - Developers keep using their preferred tool

5. Open integrations
   - Vendor-agnostic by design
   - External tools connected via MCP
   - External agents connected via ACP

Source: "JetBrains AI for Teams and Organizations: From Fragmented AI Usage
to Coordinated Software Development," JetBrains AI blog, July 7, 2026
(Oleg Koverznev).
```

### Pricing-model shift: AI licenses → AI credits

```
Prior model:  AI licenses (per-seat), valid 1 month
New model:    On-demand AI credits, valid 12 months
Stated goal:  transparent, sustainable pricing — no hidden fees, no deeply
              subsidized packages, no proxy pricing
Future scope: credits intended to eventually cover non-LLM-token services
              (unspecified, "near future")
IDE licenses that already include AI resources (AI Free, All Product Pack,
  dotUltimate) continue to include them, "yet with more flexibility."

Source: same post, "From AI licenses to AI credits" section.
```

### Rollout timeline

```
July–August 2026:  gradual rollout to business customers
Ongoing:           individual and non-commercial users "mostly not exposed"
                    to these changes yet
Prior testing:     "early design partners" tested capabilities before this
                    public announcement (no partner named, no dates given)

Source: same post, "A gradual rollout" section.
```

## Cross-References

### Cross-reference verification notes
Claims cited from other source notes below were re-read directly in those notes
before citing (per MINER.md §4b); claim numbers are counted top-to-bottom in
document order as they appear in each cited note.

- **Corroborates**:
  - `blog-jetbrains-agentic-ai-governance.md` Claim 13: "Governance at scale
    requires a consistent approach to guardrails, access management, and
    control across agents and workflows... JetBrains Central was built to
    address this: bringing governance into the development infrastructure
    itself, rather than treating it as something bolted on after AI workflows
    are already in production." This post's Claim 5 supplies the concrete
    feature list (visibility, governance, access management, model/agent
    controls, policies, analytics, cost attribution) behind that prior
    reference-only mention of JetBrains Central — the two notes describe the
    same product at two points: abstract justification (governance note) and
    concrete feature enumeration (this note).
  - `blog-jetbrains-codex-recommended-agent.md` Claim 9: JetBrains explicitly
    retaining Junie as the better choice for specific use cases rather than
    pushing Codex universally, and naming "Claude Agent, or other
    ACP-compatible agents" as switchable alternatives. This post's Claim 2
    (teams shouldn't have to standardize on one vendor) and Claim 7
    (vendor-agnostic via MCP/ACP) corroborate the same underlying JetBrains
    product philosophy — multi-vendor flexibility as a deliberate, repeated
    company position, not a one-off feature carve-out.
  - `blog-anthropic-claude-code-routines.md` Claim 1 and Claim 2: Routines'
    stated goal is eliminating self-managed "cron jobs, infrastructure, and
    additional tooling like MCP servers" via a three-axis trigger taxonomy
    (scheduled/API/webhook) run on Anthropic's own cloud infrastructure. This
    post's Claim 3 (Team automations and cloud agents, triggered by
    repository events, schedules, or other workflows) describes a
    functionally equivalent managed-cloud-execution pattern at a second,
    independent vendor — corroborating that "move scheduled/event-triggered
    agent execution off developer laptops and onto vendor-managed cloud
    infrastructure" is becoming a convergent product pattern across
    Anthropic and JetBrains, not a single-vendor feature.
  - `blog-anthropic-admin-analytics-cost-controls.md` Claim 1 and Claim 4:
    Anthropic's admin analytics dashboard (cost/usage by SCIM group, with an
    Analytics API integrating third-party FinOps tools) is a shipped,
    detailed implementation of the same "centralized visibility, governance,
    analytics, cost attribution across teams" goal this post's Claim 5 states
    for JetBrains Central, at a materially greater level of feature detail
    (specific dashboard tabs, alert thresholds, API integrations named) than
    this JetBrains announcement provides for its own not-yet-shipped
    equivalent.

- **Contradicts**: None identified requiring a contradiction issue per
  MINER.md §4a. The closing "IDE remains the center" framing (Claim 12) sits
  in some tension with the vendor-agnostic, IDE-independent reach of
  JetBrains Central CLI (Claim 6) — both claims are internal to this single
  source and do not rise to a stated factual disagreement (one is a strategic
  narrative choice, the other a product feature scope), so this is flagged
  in Claim 12's "Our assessment" as an internal framing tension rather than
  filed as a contradiction.

- **Extends**:
  - `blog-jetbrains-agentic-ai-governance.md`: that source provides the
    organizational/architectural governance *principles* (chain of command,
    boundary conditions, audit trails, human checkpoints, blast radius,
    governance-as-architecture) with JetBrains Central referenced only as a
    single supporting example. This post extends that picture with the
    *product surface* those principles are implemented in — JetBrains
    Central's actual feature list (Claim 5) and its CLI extension into
    third-party terminal tools (Claim 6) — though still without
    implementation-level detail (no screenshots, API docs, or config
    examples for any capability).
  - `blog-ghaw-ai-credits-migration.md`: that source documents GitHub's own,
    unrelated "AI Credits" terminology shift (Effective Tokens → AI Credits,
    1 AIC = $0.01 USD) for a completely different product (`gh-aw`
    workflows). This post's Claims 8–10 add a second, independent vendor
    adopting "AI credits" as a spend-unit name, but for an entirely
    different purpose (replacing per-seat licenses, not replacing a
    cost-normalization metric) and with no disclosed conversion rate. The
    guide should not conflate the two "AI credits" systems as the same
    mechanism — they share a name and a general "credit-based spend unit"
    shape but nothing else is confirmed comparable from the two sources.

- **Novel**:
  - **Explicit rejection of vendor-lock-in as fragmentation's solution**
    (Claim 2): while other corpus sources document multi-vendor agent
    picker features, this is the first source where a vendor states this as
    an explicit organizational principle ("Teams shouldn't have to
    standardize on a single vendor to benefit from AI") rather than a
    product-feature-level carve-out.
  - **Twelve-month AI credit validity vs. one-month AI license validity**
    (Claim 9): no prior corpus source documents a specific
    credit/license-validity-period comparison of this kind for enterprise
    AI tooling.
  - **JetBrains Central CLI's terminal-tool governance reach** (Claim 6):
    the first corpus source describing an IDE vendor's governance layer
    extending explicitly into terminal-only competitor/complementary tools
    (Claude Code, Codex, Gemini CLI) rather than only into its own IDE or
    IDE-plugin surfaces.
  - **A named three-capability "coordination layer" bundle sold as a single
    offering** (Team Automations/Cloud Agents + JetBrains Context +
    JetBrains Central, plus Central CLI and open integrations): no prior
    corpus source documents this specific five-capability bundle; individual
    pieces have been documented separately (governance principles, agent
    picker mechanics) but not as a single coordinated commercial
    announcement.

## Guide Impact

- **Chapter 02 (Harness Engineering — Multi-Vendor Coordination /
  Governance as Architecture)**: Add the five-capability bundle (Concrete
  Artifacts) as a second concrete, shipping-in-progress example of
  governance-as-architecture (alongside `blog-jetbrains-agentic-ai-governance.md`
  and `blog-anthropic-admin-analytics-cost-controls.md`), with the caveat
  (Claim 11) that as of this post's publish date the capabilities are
  announced/rolling out, not fully generally available — cite with a
  "as announced July 2026, rollout through August 2026" qualifier and
  revisit after that window closes.

- **Chapter 02 (Harness Engineering — Scheduled/Event-Triggered Agent
  Execution)**: Add Claim 3 (Team automations and cloud agents, triggered by
  repo events/schedules/workflows) as a second vendor (alongside Anthropic's
  Claude Code Routines) converging on the pattern of moving background agent
  execution off developer machines and onto vendor-managed cloud
  infrastructure. Note the shared taxonomy shape (event/schedule-triggered)
  without claiming the two products are equivalent — no comparative detail
  is available from either source.

- **Chapter 05 (Team Adoption — Organizational Cost/Licensing Models)**: Add
  the AI-licenses-to-AI-credits shift (Claims 8–10) as an example of a
  second, independent vendor (alongside GitHub's ET→AIC migration,
  `blog-ghaw-ai-credits-migration.md`) moving toward credit-denominated
  spend units for AI tooling — while flagging that the two "AI credits"
  systems are not confirmed to work the same way and should not be
  presented as interchangeable in the guide. Add the twelve-month vs.
  one-month validity comparison (Claim 9) as the single concrete, checkable
  commercial-terms detail from this source.

- **Chapter 04 (Evaluation — Unverified Vendor Efficiency Claims)**: Flag
  Claim 4 (JetBrains Context reducing agent turns, execution cost, and
  improving code quality) as an unverified mechanism claim with no
  accompanying benchmark in this post — worth contrasting with the same
  JetBrains AI blog's own empirical rigor elsewhere
  (`blog-jetbrains-caveman-token-savings-test.md`, which tested and
  substantially deflated a similar efficiency claim for a different
  feature). The guide should not cite JetBrains Context's cost/quality
  claims as measured until a comparable benchmark is published.

## Extraction Notes

1. **WebFetch returned an AI-summarized pass; raw HTML was fetched directly
   for verbatim quotes**: an initial WebFetch call returned a bulleted
   summary (not quote-safe per MINER.md §2a). To get exact wording, the raw
   article HTML was fetched via `curl` and converted to plain text by
   stripping markup with a script. All `Quote` fields in this note were
   copied character-for-character from that raw-text extraction, not from
   the WebFetch summary pass.
2. **Author and publish date confirmed from page metadata**: the byline
   "Oleg Koverznev" and the `<time>` element (`datetime="2026-07-07"`,
   13:03 UTC) were both present in the raw HTML and used to set
   `date_published`.
3. **No sub-pages followed**: the article's only outbound links of
   substance are a "prev post" footer link to
   `blog-jetbrains-caveman-token-savings-test.md` (already in the corpus)
   and an "Explore the new offering" link to a separate marketing
   microsite, which was not followed — the announcement post itself is
   self-contained and does not require the microsite to understand any of
   the twelve extracted claims.
4. **No quantified outcomes anywhere in the source**: this is a pure
   capability/roadmap announcement. No adoption numbers, cost-savings
   figures, benchmark results, or named customer examples appear anywhere
   in the post — every claim about capability effectiveness (Claims 3, 4)
   is a stated design goal, not a measured result. This is reflected in the
   `confidence_overall: emerging` rating and in the individual claim
   confidence levels (settled only for "what was announced," emerging or
   anecdotal for "what effect it will have").
5. **No contradictions filed**: cross-referencing against the corpus found
   no source making a claim that materially opposes anything stated here —
   see Cross-References → Contradicts for the one internal framing tension
   noted (IDE-centric narrative vs. IDE-independent Central CLI reach),
   which does not meet the MINER.md §4a bar for a contradiction issue.
