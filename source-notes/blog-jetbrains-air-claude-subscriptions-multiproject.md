---
source_url: https://blog.jetbrains.com/air/2026/08/new-in-air-claude-subscriptions-multiproject-view-and-improved-markdown/
source_type: blog-post
title: "New in Air: Claude Subscriptions, Multiproject View, and Improved Markdown"
author: Vladimir Gromozdin
date_published: 2026-08-19
date_extracted: 2026-08-20
last_checked: 2026-08-20
status: current
confidence_overall: settled
issue: "#2814"
---

# New in Air: Claude Subscriptions, Multiproject View, and Improved Markdown

> JetBrains Air's August 19, 2026 release note announces native Claude Pro/Max/Team
> subscription support — authenticated entirely through Anthropic's own login flow, with
> Air never holding a copy of the credential — as a first-party "Claude Agent" integration,
> alongside a multiproject view that puts multiple repositories and their tasks in one
> window, and Markdown files that render with formatted headings/lists/code blocks while
> remaining ordinary editable `.md` files.

## Source Context

- **Type**: blog-post (official JetBrains Air blog, published 2026-08-19 18:35 UTC;
  author Vladimir Gromozdin — the same author as the July 21, 2026 Air release note already
  in this corpus; product-release-note post, ~700 words across an intro, three named feature
  sections, and a five-question FAQ; discovered via the trusted `jetbrains-ai` feed).
- **Author credibility**: JetBrains staff writing on the official JetBrains Air blog about
  a feature release for JetBrains' own product. Authoritative for: what shipped, the stated
  authentication mechanism and its explicit limitations, and the FAQ's plan-eligibility and
  permission answers. Not independently verified: no screenshot walkthrough, third-party
  account of actually connecting a Claude subscription, or technical detail beyond what the
  vendor chose to disclose (e.g., no token format, no protocol name for "Claude's native
  login interface" beyond the assertion that it is "the same one that opens when you run
  Claude in a terminal"). This is a vendor release-note/FAQ post, not a hands-on review or
  independent security audit of the authentication claim.
- **Scope**: Covers three shipped features in the August 19, 2026 Air release — Claude
  Pro/Max/Team subscription support via a first-party "Claude Agent" integration, a
  multiproject view, and improved Markdown rendering — plus a five-question FAQ addressing
  platform support, ACP migration, Team-seat eligibility, Anthropic permission, and
  pricing/plan requirements. Does NOT cover: the June 22, 2026 GitHub Copilot JetBrains
  plugin's separate "Claude as agent provider" integration (which uses an installed Claude
  Code CLI rather than Air's subscription login — see Cross-References), any Air-specific
  UI screenshots or step-by-step walkthrough beyond prose description, pricing/rate-limit
  detail for Claude subscriptions themselves (see Cross-References for existing corpus
  coverage of Claude subscription tiers), or a technical specification of "Anthropic's
  documented flow" the post repeatedly references but does not link with an accessible
  URL in the extracted article body.

## Extracted Claims

### Claim 1: Air now supports using an existing Claude Pro, Max, or Team subscription, with usage counted against the subscription quota rather than requiring API credits or per-token Console billing
- **Evidence**: Direct statement in the article's opening paragraph.
- **Confidence**: settled (direct statement of a shipped billing/authentication capability)
- **Quote**: "Usage counts against your subscription quota – there's no need to purchase API credits and no per-token Console billing."
- **Our assessment**: This is a concrete billing-mechanism claim: subscription usage inside Air draws down the same quota as using Claude anywhere else under that plan, with no separate API-credit purchase or Anthropic Console per-token billing involved. It mirrors the general subscription-vs-API-key distinction already documented for Claude Code itself (see Cross-References), now extended to a third-party IDE-adjacent tool.

### Claim 2: Air never sees or stores Claude credentials — login goes through Anthropic's own authentication flow rather than an Air-built one
- **Evidence**: Direct statement immediately following Claim 1, repeated and elaborated later in a dedicated "Air never touches your credentials" section.
- **Confidence**: settled
- **Quote**: "Login goes through Anthropic's own authentication flow. Air never sees or stores your credentials."
- **Our assessment**: This is the article's central architectural claim and is elaborated with mechanism detail in Claim 4 below. It is a security-relevant design choice: the host application (Air) explicitly disclaims custody of the user's Anthropic credential, shifting trust entirely to Anthropic's own login system.

### Claim 3: JetBrains states this was its most-requested feature, and that it delayed shipping specifically because it refused to build a custom OAuth workaround that could put a user's Anthropic account at risk, waiting instead for Anthropic's own documented authentication method
- **Evidence**: Direct first-party statement of internal rationale for the shipping delay, in the article's third paragraph.
- **Confidence**: settled (first-party account of the vendor's own stated design decision, not a third-party claim)
- **Quote**: "This was our most-requested feature and it took longer to implement than anyone wanted, including us. But our delay wasn't without good reason: We weren't prepared to ship an OAuth workaround that could put your Anthropic account at risk, so we waited until we could build on Anthropic's documented authentication method."
- **Our assessment**: JetBrains is explicitly framing a shipping delay as a deliberate security tradeoff rather than a technical limitation — it names the alternative it rejected ("an OAuth workaround") and the reason (risk to the user's Anthropic account). This is a specific, citable example of a vendor prioritizing a sanctioned integration path over a faster but riskier one for third-party account access, worth preserving as a general pattern independent of Air specifically.

### Claim 4: Mechanically, clicking "Connect Claude.ai Account" invokes Claude's own native login interface — the same one that opens when running Claude in a terminal — rather than Air running its own OAuth flow; the token stays with Anthropic, and Air only learns that the user is logged in
- **Evidence**: Detailed mechanism description in the "Air never touches your credentials" section.
- **Confidence**: settled
- **Quote**: "When you click Connect Claude.ai Account, Air doesn't run its own OAuth flow. It invokes Claude's native login interface – the same one that opens when you run Claude in a terminal. Your browser opens, you authorize the connection, and your token stays where Anthropic designed it to stay: with Claude. Claude owns the credential, Claude refreshes it, and Air only ever learns one thing – that you're logged in."
- **Our assessment**: This is the concrete implementation detail behind Claim 2's higher-level "Air never sees or stores your credentials" statement: Air reuses the identical login surface a practitioner would see running Claude directly in a terminal, rather than presenting its own branded OAuth consent screen. The three-part division of labor ("Claude owns the credential, Claude refreshes it, Air only learns... logged in") is a reusable pattern for evaluating any third-party tool's claim to integrate with a subscription service without handling its credentials directly.

### Claim 5: Air's implementation follows "Anthropic's documented flow for exactly this use case," with credentials handled by Claude itself end-to-end — a claim JetBrains repeats verbatim in the FAQ as evidence the integration is sanctioned rather than an unauthorized workaround
- **Evidence**: Stated once in the "Air never touches your credentials" section and restated in the FAQ under "Is this permitted by Anthropic?"
- **Confidence**: settled (direct, repeated vendor assertion; no independent Anthropic confirmation is quoted or linked in the extracted article body)
- **Quote**: "Air's implementation follows Anthropic's documented flow for exactly this use case. Your credentials are handled by Claude itself, end to end."
- **Our assessment**: The repetition of this claim — once in the feature description, once verbatim in the FAQ answering "Is this permitted by Anthropic?" — signals JetBrains anticipated practitioner skepticism about whether a third-party IDE tool integrating with a personal Claude subscription is sanctioned use, and chose to answer it explicitly rather than leave it implicit. This is consistent with Claim 3's framing of the delay as driven by a refusal to ship an unsanctioned OAuth workaround.

### Claim 6: The bundled integration, named "Claude Agent," is presented as a first-party integration distinct from previously available ACP-based Claude connections, and includes current model selection with reasoning-effort control, slash commands, MCP servers, skills, permissions/session state, and usage/status reporting
- **Evidence**: Direct feature enumeration in the "Claude in Air is the full first-party experience" section.
- **Confidence**: settled
- **Quote**: "Some of you have already connected Claude to Air yourselves through ACP. However, this bundled Claude Agent in Air is a first-party integration with: Current models, selectable in Air, with reasoning effort control [newline] Slash commands [newline] MCP servers [newline] Skills [newline] Permissions and session state [newline] Usage and status reporting"
- **Our assessment**: This explicitly names ACP (Agent Client Protocol) as the pre-existing, non-first-party way Claude could already be connected to Air — consistent with the July 21, 2026 Air release note already in this corpus, which documents ACP as the general mechanism for connecting third-party agents to Air (see Cross-References). This new "Claude Agent" integration is positioned as superseding that ACP path specifically for Claude, not as a wholly new capability category for Air.

### Claim 7: JetBrains recommends practitioners who previously connected Claude via ACP switch to the bundled Claude Agent, citing correct model reporting, slash-command support, and other first-party features as the improvement
- **Evidence**: Direct recommendation at the end of the "Claude in Air is the full first-party experience" section, restated in the FAQ.
- **Confidence**: settled
- **Quote**: "If you have Claude set up to work in Air via ACP, we suggest switching to the bundled Claude Agent for better functionality and an enhanced experience." FAQ: "Remove the ACP entry and log in through the bundled Claude Agent – you'll get correct model reporting, slash commands, and all the other first-party features."
- **Our assessment**: The phrase "correct model reporting" implies the prior ACP-based connection had some model-reporting inaccuracy relative to the new first-party path, though the article does not elaborate on what was incorrect. This is a specific, actionable migration recommendation for any practitioner already using Claude-via-ACP in Air, not a generic "new feature available" note.

### Claim 8: Claude Agent cannot currently run in Docker environments using subscription tokens, because the token lives with Claude on the practitioner's machine and Air never holds a copy — there is no credential Air could hand into an isolated container — so containerized runs require API billing or JetBrains AI credits instead
- **Evidence**: Direct statement and stated mechanism in the "Docker environments still require API billing or JetBrains AI credits" section.
- **Confidence**: settled
- **Quote**: "You can't currently run Claude Agent in Docker environments without API billing. Because your subscription token lives with Claude on your machine and Air never holds a copy, there's no credential Air could hand into an isolated container. Containerized runs have to go through API billing or JetBrains AI credits."
- **Our assessment**: This is the first concrete limitation that follows directly from the credential-custody design in Claims 2 and 4: the same design choice that keeps Air from ever touching the credential (a security benefit) is also what makes containerized/isolated execution structurally impossible without a different billing path. "JetBrains AI credits" is named here as one of the two alternatives — this is the same credit mechanism documented at greater length in existing corpus notes on JetBrains' AI-licenses-to-AI-credits shift (see Cross-References).

### Claim 9: The new multiproject view puts multiple repositories and their tasks in a single Air window — previously each repository required its own separate window — with the sidebar grouping tasks by project, search covering the full task list, and each task keeping its project and branch visible while navigating between them
- **Evidence**: Direct feature description in the "Your projects now share one window" section.
- **Confidence**: settled
- **Quote**: "Until now, opening another repository in Air meant opening another Air window. The new multiproject view puts multiple projects and their tasks in one place. The sidebar groups tasks by project, search covers the full task list, and each task keeps its project and branch visible as you move between them."
- **Our assessment**: This names the specific prior limitation being fixed (one window per repository) with enough precision to be checkable — a practitioner working across, say, three repositories previously needed three separate Air windows, and now needs one.

### Claim 10: Multiproject view is framed as changing Air's fundamental unit of navigation from windows to tasks, letting a practitioner start an agent in one repository, switch to another while it runs, and check a completed task in a third — with running and completed tasks staying visible together to coordinate multirepo work as a single workflow
- **Evidence**: Direct framing statement immediately following Claim 9's feature description.
- **Confidence**: settled
- **Quote**: "This changes the unit of navigation in Air from windows to tasks. Start an agent in your backend repo, switch to the frontend while it runs, and then jump to a completed task in a third project – all without losing track of which agent is working where. Running and completed tasks stay visible together, so you can coordinate multirepo work as one workflow instead of several disconnected Air sessions."
- **Our assessment**: This is a conceptual reframing claim, not just a feature description — JetBrains explicitly states the unit practitioners orient around inside Air has changed (window → task). The concrete example given (backend repo agent running, switch to frontend, check a third project's completed task) illustrates cross-repository agent orchestration inside one window, which is a distinct capability from the ACP-based multi-agent connectivity documented in the July 2026 Air release note (that note covers which agents can run; this one covers how many concurrent repository contexts a single window can hold).

### Claim 11: Air now renders `.md` files with heading hierarchy, formatted lists, distinct code blocks, and syntax highlighting for commands/paths/inline code, while the underlying file remains an ordinary, directly editable Markdown file whose syntax recedes while reading and reappears while editing
- **Evidence**: Direct feature description in the "Markdown files now read like documents" section.
- **Confidence**: settled
- **Quote**: "Air now renders any .md file with clear heading hierarchy, formatted lists, distinct code blocks, and syntax highlighting for commands, paths, and inline code." And: "It is still an ordinary Markdown file. The syntax recedes while you read and appears when you edit, making READMEs, plans, notes, and documentation easier to scan without parsing the formatting first."
- **Our assessment**: The explicit "still an ordinary Markdown file" framing distinguishes this from a proprietary rich-text format — the rendering is presentation-layer only, and the underlying file stays plain-text-editable. The stated use case (READMEs, plans, notes, documentation) positions this as relevant to any workflow where an agent or practitioner reads/writes Markdown planning artifacts inside Air, not just end-user-facing docs.

### Claim 12: A Claude Team subscription seat, with no separate API budget, is explicitly sufficient to use Claude Agent in Air
- **Evidence**: Direct FAQ answer to a named organizational use case.
- **Confidence**: settled
- **Quote**: "My company has Claude Team seats and no API budget. Will this implementation work for me? Yes, it will. You can use your Claude Team seat with a subscription."
- **Our assessment**: This directly answers an organizational adoption question the article anticipates: teams that provisioned Claude Team seats (rather than API budget) for their developers are explicitly told this integration works for them without any additional billing setup — a concrete, checkable eligibility statement for the Team tier specifically, distinct from the individual Pro/Max framing in Claim 1.

### Claim 13: The stated limitations of subscription-based access are structural, following directly from the credential-custody design: because the token stays on the practitioner's machine and Air never holds a copy, anything running outside that machine — Docker environments, cloud agents, and automations — requires API billing or JetBrains AI credits, and subscription-powered tasks cannot yet be shared across surfaces such as IDE or mobile
- **Evidence**: Direct FAQ answer to "What are the advantages and limitations of using a Claude subscription?"
- **Confidence**: settled
- **Quote**: "The limitations follow from the design: your token stays with Claude on your machine, and Air never holds a copy. So anything that runs outside your machine can't use it. Docker environments, cloud agents, and automations require API billing or JetBrains AI credits, and subscription-powered tasks can't yet be shared across surfaces like the IDE or mobile."
- **Our assessment**: This FAQ answer generalizes Claim 8's Docker-specific limitation into a broader rule ("anything that runs outside your machine can't use it") and adds two previously unstated cases — cloud agents and automations — plus a stated but unexplained cross-surface limitation ("can't yet be shared across surfaces like the IDE or mobile"), which implies Air (or a related JetBrains surface) has, or is building, a mobile presence not otherwise described in this article. The "not yet" phrasing suggests JetBrains considers cross-surface task sharing a planned future capability rather than a permanent design constraint, unlike the Docker/cloud/automation limitation, which is framed as following inherently from the credential-custody design.

### Claim 14: Air's desktop version remains free across macOS, Windows, and Linux, and practitioners may bring subscriptions from external AI providers at no additional charge from JetBrains
- **Evidence**: Direct FAQ answer to "Do I need JetBrains AI or a paid Air plan?"
- **Confidence**: settled
- **Quote**: "No and no. The desktop version of Air is free, and you are welcome to bring your own subscription from external AI providers. We won't charge you anything extra for using it."
- **Our assessment**: "External AI providers" (plural) implies this subscription-based, credential-free integration pattern is not exclusive to Claude, though the article names only Claude Pro/Max/Team as concrete examples throughout — no other provider's subscription-integration mechanics are described in this source. This should not be read as confirmation that other providers get an identical native-login mechanism to Claude's; only that JetBrains does not charge extra for bringing one.

## Concrete Artifacts

### Claude Agent feature list (Air, August 19, 2026 release)
```
Source: "New in Air: Claude Subscriptions, Multiproject View, and Improved
Markdown," JetBrains Air blog, August 19, 2026 (Vladimir Gromozdin).

- Current models, selectable in Air, with reasoning effort control
- Slash commands
- MCP servers
- Skills
- Permissions and session state
- Usage and status reporting

Prior connection path (being superseded): Claude connected to Air via ACP
(Agent Client Protocol), as documented in blog-jetbrains-air-acp-local-models.md.
```

### Credential-custody chain, as described
```
Practitioner clicks "Connect Claude.ai Account" in Air
        |
        v
Air invokes Claude's native login interface (same UI as `claude` CLI login)
        |
        v
Browser opens; practitioner authorizes the connection with Anthropic directly
        |
        v
Token issued and held by Claude/Anthropic; Claude refreshes it
        |
        v
Air learns only one fact: the practitioner is logged in
        (Air never receives, stores, or holds a copy of the credential itself)

Source: same article, "Air never touches your credentials" section.
```

### Subscription-access limitations (FAQ, verbatim structure)
```
Source: same article, "What are the advantages and limitations of using a
Claude subscription?" FAQ answer.

Advantage: full Claude plan (models, quota, limits) applies inside Air
  exactly as elsewhere, combined with first-party Claude Agent features.
  No API credits, no Console billing, nothing extra to set up or pay for.

Limitations (all stated as following from the token staying on-machine,
  never copied by Air):
  - Docker environments: require API billing or JetBrains AI credits
  - Cloud agents: require API billing or JetBrains AI credits
  - Automations: require API billing or JetBrains AI credits
  - Cross-surface task sharing (e.g. IDE <-> mobile): "not yet" supported
    for subscription-powered tasks
```

## Cross-References

### Cross-reference verification notes
Claims cited from `blog-jetbrains-air-acp-local-models.md`,
`blog-anthropic-maximizing-session-value.md`,
`blog-jetbrains-ai-for-teams-organizations.md`,
`blog-jetbrains-central-cli-cost-origin-story.md`,
`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`,
`blog-simonwillison-fable-5-permanent.md`, and
`failure-cursor-pro-silent-billing-switch.md` were re-read directly in those
notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates**:
  - `blog-anthropic-maximizing-session-value.md` Claim 4: "The prompt cache
    expires after one hour on a Claude subscription, or five minutes on an
    API key." That note documents subscription-vs-API-key access as a
    materially different mechanism inside Claude Code itself (different
    cache TTL). This source's Claims 1, 8, and 13 corroborate that the
    subscription-vs-API distinction is not specific to Claude Code — it
    carries into a third, separate tool (Air) with its own set of
    subscription-specific tradeoffs (no per-token billing, but no
    container/cloud/automation access), reinforcing that "subscription
    access" and "API access" to Claude are two structurally different
    integration paths across the wider Anthropic-adjacent tool ecosystem,
    not just two billing options with identical capabilities.
  - `blog-jetbrains-ai-for-teams-organizations.md` Claim 8: "For business
    customers, we will transition from AI licenses to flexible on-demand AI
    credits." This source's Claim 8 and Claim 13 name "JetBrains AI credits"
    as the fallback billing path for Docker/cloud/automation use when a
    Claude subscription token cannot reach the workload — the first
    concrete, named use case in the corpus for when a practitioner would
    actually need JetBrains AI credits rather than a personal Claude
    subscription, corroborating that the credit system is intended to cover
    exactly the machine-independent execution modes a subscription cannot.

- **Contradicts**: None identified. No existing corpus note makes a claim
  about Air, Claude subscription authentication, or JetBrains AI credits
  that this source materially opposes. No contradiction issue filed.

- **Extends**:
  - `blog-jetbrains-air-acp-local-models.md`: that note (July 21, 2026, same
    author) documents ACP as the general mechanism for connecting
    third-party agents — including Claude — to Air, alongside local-model
    support, Java/Kotlin language intelligence, Windows Docker parity, and
    per-task Claude context-window visibility. This source extends that
    picture one month later with a Claude-specific, first-party replacement
    for the ACP connection path (Claim 6), explicitly recommending
    practitioners migrate off ACP-connected Claude (Claim 7) — the two notes
    together show Air's Claude integration evolving from "one of several
    ACP-connectable agents" to "a first-party, subscription-authenticated,
    named integration" within roughly four weeks.
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim
    1: that note documents a materially different mechanism for reaching
    Claude inside a JetBrains IDE — the GitHub Copilot JetBrains plugin's
    "Claude as agent provider" (public preview, June 22, 2026) requires
    installing the Claude Code CLI locally and configuring its path in IDE
    settings ("Claude as agent provider is now available in public preview,
    giving you more flexibility to pick the agent that best fits your task,
    all without leaving your JetBrains IDE."). This source's Claim 4
    (native browser-based login, no local CLI install, no credential
    handling by the host app) is a contrasting integration pattern for the
    same underlying goal (using Claude inside a JetBrains-adjacent tool):
    Copilot's JetBrains plugin routes through an installed CLI binary the
    plugin must locate and invoke, while Air's Claude Agent routes through
    Anthropic's own hosted login flow with no local CLI dependency
    described. The guide should not treat "Claude in a JetBrains IDE" as a
    single integration pattern — these are two different products (GitHub
    Copilot's plugin vs. JetBrains' own Air) with two different
    authentication and execution mechanisms.
  - `blog-jetbrains-central-cli-cost-origin-story.md` Claim 13: that note
    states JetBrains Central CLI explicitly treats "personal AI
    subscriptions" as permanently out of scope for its governance/cost
    layer ("Niche setups and personal AI subscriptions will remain out of
    scope, as our goal is to cover the AI traffic running through the tools
    developers rely on most."). This source's Claim 1 (individual Claude
    Pro/Max/Team subscriptions as a first-class, directly supported access
    path in Air) sits on the opposite side of that same personal-subscription
    boundary: Central CLI is explicitly not built to govern the kind of
    subscription usage Air's Claude Agent is explicitly built to support.
    This is not a contradiction — the two products serve different purposes
    (governance/cost-attribution vs. individual developer tooling) — but the
    guide should note that JetBrains' own organizational cost-governance
    tooling does not currently extend visibility into the exact access
    pattern (personal Claude subscriptions) this source describes JetBrains
    encouraging developers to use directly inside Air.
  - `failure-cursor-pro-silent-billing-switch.md` Lesson 1 ("AI coding tool
    subscriptions may silently enroll users in post-paid per-token billing when
    plan limits are hit"): that note (claims are structured as numbered
    `### Lesson N` headings rather than `### Claim N`, so it is cited by lesson
    number here) documents a Cursor Pro subscriber silently moved onto
    per-token "On-Demand" billing on hitting the monthly plan limit, and
    derives the general evaluation question "For any AI tool subscription with
    a monthly usage quota, identify in advance what happens when the quota is
    hit." This source is the mirror-image case for that question and answers
    only half of it. Claim 1 establishes the steady-state billing mode ("there's
    no need to purchase API credits and no per-token Console billing"), and
    Claims 8 and 13 name API billing and JetBrains AI credits as the fallback
    path for Docker, cloud agents, and automations — but the article is silent
    on limit-hit behavior. Its only statement on quota is the FAQ's "its models,
    quota, and limits apply in Air exactly as they do everywhere else," which
    says Anthropic's own plan limits govern but does not say whether Air hard-
    stops at the subscription limit or falls through to one of the two paid
    paths it already knows how to use. Verified against the full article text:
    no sentence anywhere in the post addresses quota exhaustion. This is a real
    gap rather than a contradiction — nothing in this source opposes the Cursor
    note — but it is exactly the gap the Cursor failure report argues
    practitioners must close with the vendor before hitting the limit, not
    after, and the guide should carry it as an open question about Air rather
    than assume the credential-custody design implies a hard stop.
  - `blog-simonwillison-fable-5-permanent.md`: that note documents Anthropic's
    own subscription-tier access rules for a specific model (Claude Fable 5)
    — full inclusion at reduced limits on Max/Team Premium, credit-metered
    access on Pro/Team Standard, no access on the $20/month plan. This
    source does not name any model-specific access tier within Air's Claude
    subscription support (it treats "Claude Pro, Max, or Team" uniformly as
    eligible), so a practitioner relying on Air with a lower-tier Claude
    subscription should still expect any model-specific tier restrictions
    documented in that note to apply — Air's integration does not appear to
    change or bypass Anthropic's own per-model subscription-tier rules.

- **Novel**:
  - **A named, browser-based "native login" mechanism as a specific
    alternative to both a custom OAuth flow and an installed-CLI dependency**
    (Claim 4): no prior corpus source documents a third-party IDE-adjacent
    tool integrating with a subscription service by directly invoking that
    service's own native login UI rather than building a bespoke OAuth
    consent screen or requiring a locally installed CLI binary.
  - **A vendor naming a security-motivated shipping delay explicitly, and
    naming the rejected faster alternative** (Claim 3): prior corpus
    JetBrains sources document features shipping with security-relevant
    design choices, but this is the first source where the vendor states it
    delayed a top-requested feature specifically to avoid a credential-risk
    shortcut, rather than simply shipping and later hardening it.
  - **A concrete, FAQ-stated cross-surface task-sharing gap for a
    subscription-authenticated workflow** (Claim 13, "IDE or mobile"): no
    prior corpus source references an Air-adjacent mobile surface at all;
    this is the first mention of one, even if only as a named limitation.

## Guide Impact

- **Chapter 02 (Cost & Subscription Models)**: Add this source's
  subscription-vs-API-billing split for Air (Claims 1, 8, 13) as a second
  concrete example — alongside `blog-anthropic-maximizing-session-value.md`
  Claim 4's Claude Code cache-TTL split — of subscription access and API-key
  access being structurally different integration paths, not just different
  prices for identical capability, in Anthropic-adjacent tooling generally.
  Recommend the guide state explicitly: subscription access typically means
  no per-token billing but is tied to the credential staying on the
  practitioner's own machine, which blocks container/cloud/automation use
  cases that API billing or vendor-specific credits (e.g., JetBrains AI
  credits) are needed to cover instead.

- **Chapter 04 (Model Selection) / Chapter 05 (IDE-Native Development)**: Add
  the credential-custody chain (Concrete Artifacts) as a reusable pattern for
  evaluating any tool's claim to support "your existing subscription" —
  specifically, whether the host tool ever receives a copy of the credential
  (Air's stated design: it does not) versus requiring a locally installed
  CLI the tool locates and shells out to (the contrasting GitHub Copilot
  JetBrains-plugin mechanism, Claim 4's Cross-Reference). These are
  materially different trust and setup models even when both are described
  loosely as "using Claude in your IDE."

- **Chapter 05 (Team Adoption)**: Add Claim 12 (Claude Team seat, no API
  budget, works directly with Air's Claude Agent) as a specific,
  checkable eligibility answer for teams evaluating Air adoption without a
  separate API-billing setup. Pair with Claim 13's explicit limitations list
  (Docker, cloud agents, automations, cross-surface sharing) so teams
  evaluating Air do not assume subscription access alone covers every
  execution mode they might need — flag Central CLI's explicit exclusion of
  personal subscriptions (Cross-References) as a related governance gap: a
  team standardizing on subscription-based Air/Claude access should not
  expect JetBrains Central CLI to give them visibility into that usage.

- **Chapter 06 (Agent Orchestration)**: Add the multiproject view's
  window-to-task navigation reframing (Claims 9-10) as a concrete UI pattern
  for coordinating agents across multiple repositories from a single
  workspace, distinct from (and complementary to) the ACP-based multi-agent
  connectivity already documented in `blog-jetbrains-air-acp-local-models.md`
  — that note covers which agents Air can run; this source covers how many
  concurrent repository/task contexts a single Air window can hold at once.

## Extraction Notes

1. **WebFetch returned a condensed paraphrase on the first pass; raw HTML was
   fetched directly via `curl` for verbatim quotes**: as with several prior
   JetBrains and Willison source notes in this corpus, the initial WebFetch
   call against this URL returned a short, reworded four-section summary
   (e.g., collapsing the full credential-custody paragraph into "The
   implementation prioritizes security"), unusable for direct quotes per
   MINER.md §2a. The raw article HTML was fetched via `curl`, the `<article>`
   region was isolated, `<script>`/`<style>` blocks were stripped, HTML
   entities were decoded (`html.unescape`, recovering curly apostrophes and
   en dashes that a first, non-decoding pass left as literal `&#8217;`/`&#8211;`
   escapes), and the result was converted to plain text. All `Quote` fields in
   this note were copied character-for-character from that decoded raw-text
   extraction, not from the WebFetch summary pass.
2. **Author and publish date confirmed from page metadata**: the byline
   "Vladimir Gromozdin" and a `<time class="publish-date" datetime="2026-08-19">`
   element (data attributes: year 2026, month 08, day 19, 18:35) were both
   present in the raw HTML and used to set `date_published`.
3. **One sub-page identified but not followed as a new extraction target**:
   the article's "prev post" footer link
   (`blog.jetbrains.com/ai/2026/08/our-first-moves-to-get-ai-spend-under-control/`)
   resolves to a post already present in this corpus as
   `blog-jetbrains-central-cli-cost-origin-story.md`; it was re-read for
   cross-referencing (Claim 13) rather than re-extracted as a duplicate note.
   No other outbound link in the article body (beyond navigation, footer
   legal links, and the unlinked "Anthropic's documented flow"/"Anthropic's
   documented authentication method" phrases, which are not rendered as
   clickable hyperlinks with a resolvable URL in the fetched HTML) pointed to
   a substantive, not-yet-covered page.
4. **"Anthropic's documented flow" is referenced but not linked to a
   specific, checkable URL** in the extracted article HTML — the phrase
   appears three times (twice in the feature description, once in the FAQ)
   as emphasized text, but no `<a href>` target was found wrapping it in the
   fetched markup. This is flagged as a genuine content gap: the claim that
   Air's authentication follows an Anthropic-documented method (Claims 3, 5)
   could not be independently verified against Anthropic's own documentation
   from this source alone.
5. **Source is a short, single-page release note (~700 words, three feature
   sections plus a five-question FAQ)**: fourteen claims were extracted,
   covering every substantive statement in the post, including all five FAQ
   answers. No claim count padding was needed or attempted.
6. **No contradictions found**: this source is consistent with every existing
   JetBrains-scoped note in the corpus; where it touches a related but
   distinct product boundary (Central CLI's exclusion of personal
   subscriptions, the GitHub Copilot JetBrains plugin's separate Claude
   integration), those are flagged under Cross-References → Extends as
   scope contrasts, not contradictions, per MINER.md §4a's guidance that
   differing product scope is a conditioning variable, not a disagreement.
   No contradiction issue filed.
7. **Confidence graded "settled" overall**: all fourteen claims describe
   either a feature stated definitively as shipped (not labeled preview or
   beta anywhere in the source) or a direct FAQ answer to a specific,
   checkable eligibility/permission question. No claim in this source carries
   a stated preview/beta qualifier, unlike the July 21, 2026 Air note's Beta-
   labeled Java/Kotlin feature.
