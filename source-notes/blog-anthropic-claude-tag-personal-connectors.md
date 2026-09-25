---
source_url: https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels
source_type: blog-post
title: "Claude Tag now supports personal connectors in channels"
author: Anthropic (no individual byline)
date_published: 2026-09-24
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: emerging
issue: "#3692"
---

# Claude Tag now supports personal connectors in channels

> First-party Anthropic product-update post announcing that Claude Tag can now use an
> individual channel member's own personal connectors (calendar, drive, CRM, staging
> deploys) for requests that member makes in a shared channel, alongside the existing
> admin-provisioned channel connectors — with a distinct consent model, a separate
> per-user audit log, and an explicit scope boundary restricting personal connectors to
> attended, user-initiated requests only.

## Source Context

- **Type**: blog-post (official claude.com/blog product update, September 24, 2026; no
  individual byline — published as Anthropic, consistent with the June 24, 2026
  agent-identity announcement and the August 13, 2026 context-awareness update already in
  this corpus)
- **Author credibility**: First-party Anthropic product-update post describing a shipped
  (Team plans) / upcoming (Enterprise) change to Claude Tag's connector access model.
  Architectural and behavioral claims about how personal connectors work, how they are
  logged, and how they differ from admin-attached channel connectors are vendor-authoritative
  for describing shipped/rolling-out product behavior. The post contains no quantitative
  metrics (no percentages, no timing figures) — it is a capability and governance
  description, not a results report.
- **Scope**: Covers one specific capability addition to Claude Tag: individual users
  invoking their own personal connectors for requests they make in a channel, the two
  consent modes (review vs. auto), the admin governance options this creates, one worked
  example (Priya, #checkout-migration), the audit-logging split between personal-connector
  use and channel service-account work, the explicit scope boundary that personal
  connectors cannot be used for unattended/scheduled work, and rollout status. Does NOT
  cover: the underlying agent-identity/service-account architecture for channel-level
  connectors (see `blog-anthropic-agent-identity-access-model.md`), the proactivity/
  response-decision mechanism (see `blog-anthropic-claude-tag-context-awareness.md`),
  pricing or usage-limit impact of this feature, or any third-party/practitioner account of
  using personal connectors (this is a same-day announcement; no user reports exist yet).

## Extracted Claims

### Claim 1: Before this update, Claude Tag in a channel could only use connectors an admin had attached to that channel, and most organizations deliberately kept that list short so that access would follow the person, not the channel
- **Evidence**: Direct framing statement opening the post, stating both the prior
  limitation and the stated organizational rationale for it.
- **Confidence**: settled (specific first-party statement of prior product behavior and
  observed admin practice)
- **Quote**: "Claude Tag (beta) lets you add Claude to a Slack channel, where it works alongside your team. Until now, Claude could only use the connectors an admin attached to the channel, and most organizations keep that list short on purpose: they want access to follow the person, not the channel."
- **Our assessment**: This framing establishes the specific gap the feature fills: admins
  restricting channel connector lists is presented not as an oversight but as a deliberate
  access-control choice ("access to follow the person, not the channel") that the prior
  admin-only-connectors model could not satisfy — since a channel-wide connector grant
  necessarily gives every channel member and Claude itself access regardless of who is
  making the individual request.

### Claim 2: Claude can now use an individual channel member's own personal connectors (calendar, drive, CRM accounts, staging deploys) for a request that member makes in the channel, provided the member has connected that tool to their own Claude account
- **Evidence**: Direct statement of the new capability with a named list of example
  connector types.
- **Confidence**: settled (specific first-party description of shipped/rolling-out
  capability)
- **Quote**: "Now Claude can use your own connectors for a request you make in a channel. For example, your calendar, your drive, your assigned accounts on the CRM, or your staging deploys. If you have connected it to your Claude account, you can access it in the channel."
- **Our assessment**: This is the core capability of the post. The four named example
  connector types (calendar, drive, CRM, staging deploys) share a property worth noting:
  each is inherently individual-scoped data (whose calendar, whose CRM book, whose deploy
  target) rather than shared team resources — which is exactly the category of access the
  prior admin-only-connector model structurally could not serve well, per Claim 1.

### Claim 3: Users choose between two response-surfacing modes for personal-connector requests — review mode (see the response before it posts) and auto mode (Claude posts automatically unless it judges the content sensitive); Enterprise admins will be able to mandate review mode for everyone
- **Evidence**: Direct description of the consent/posting mechanism, including the
  Enterprise-only admin override.
- **Confidence**: settled (specific first-party description of a shipped/planned UI and
  policy control)
- **Quote**: "You decide how information is surfaced from when you ask Claude to access your connectors. You can review each response before it posts. Alternatively, you can use auto mode to post automatically unless Claude determines there is sensitive content that needs your review. On  Enterprise plans, admins will be able to require review for everyone."
- **Our assessment**: Auto mode's safety property rests entirely on "Claude determines
  there is sensitive content that needs your review" — a model-judgment call, not a
  deterministic rule, applied to content that by definition already touched channel-visible
  connectors. The post does not define what triggers the sensitivity determination or
  disclose an error rate for it. The Enterprise admin override (mandatory review mode for
  everyone) is the deterministic fallback for organizations that don't want to rely on that
  judgment call — worth noting as the safer default for regulated or high-sensitivity teams.

### Claim 4: Personal connectors give admins three distinct channel-governance configurations to choose from: shared tools under an agent identity, channel members relying solely on personal connectors under existing role-based access, or a tool-by-tool mixed decision
- **Evidence**: Direct enumeration of admin governance options immediately following the
  consent-mode description.
- **Confidence**: settled (specific first-party enumeration of the configuration surface)
- **Quote**: "Personal connectors provide admins more governance options. They can provide access to a shared set of tools under an agent identity, have channel members only use personal connectors to rely on existing role-based access, or decide tool by tool."
- **Our assessment**: The first option ("a shared set of tools under an agent identity")
  is a direct reference to the service-account model documented in
  `blog-anthropic-agent-identity-access-model.md`; the second option (personal-connectors-only,
  relying on each user's existing RBAC in the underlying tool) is new to the corpus — it
  means a channel can be configured so Claude has *no* standing channel-level access at
  all, and every action is gated by whichever individual user is making the request having
  their own tool-level permissions. The third ("tool by tool") implies these two models are
  not mutually exclusive within a single channel — some connectors can be agent-identity/
  shared while others are personal-only, decided per tool.

### Claim 5: Personal connectors in Claude Tag are rolling out now on Team plans, with Enterprise availability to follow
- **Evidence**: Direct rollout-status statement, restated identically at both the top and
  bottom of the post.
- **Confidence**: settled (specific first-party availability statement)
- **Quote**: "Personal connectors in Claude Tag are rolling out now on Team plans, with Enterprise to follow."
- **Our assessment**: As of the September 24, 2026 publish date this is Team-plan-only;
  the Enterprise-admin governance controls described in Claims 3 and 4 (mandatory review
  mode, agent-identity vs. RBAC-only channel configuration) are therefore not yet available
  to Enterprise customers even though they are documented in the same post — worth flagging
  for any guide section that scopes this feature by plan tier.

### Claim 6: In the worked example, Priya in a GitHub-connected channel asks Claude to compare her personal Google Drive planning doc against merged pull requests — a single request that spans a channel-level connector (GitHub) and a personal connector (her Drive) in one turn
- **Evidence**: The post's single concrete worked example, including Priya's literal
  prompt and the described execution.
- **Confidence**: settled (specific first-party worked example with literal quoted prompt)
- **Quote**: "For example, here's Priya in #checkout-migration, a channel connected to GitHub. She asks: "@Claude check my Google Drive doc 'Checkout migration, Q3' against what we've shipped. What's still open?" ... Claude reads the merged pull requests through the channel's GitHub connector. The doc is one only Priya can open. Before, Claude would have stopped there."
- **Our assessment**: "Before, Claude would have stopped there" is the sharpest evidence
  in the post for what problem this feature actually solves: prior to this update, a
  request requiring both a channel-shared resource (GitHub) and a requester-private
  resource (a personal Drive doc only Priya can open) was structurally impossible to
  fulfil in one pass — Claude had no path to the private doc at all. This is a concrete,
  reusable pattern description: mixed-scope requests (shared context + individual private
  data) as the specific use case personal connectors unlock, not personal connectors as a
  general connector-access expansion.

### Claim 7: Once personal connectors are used, the same review/auto choice from Claim 3 applies per-document sensitivity, illustrated by Priya using auto mode for a non-sensitive doc but noting she could switch to review mode for a document she'd rather check first
- **Evidence**: Direct continuation of the worked example, describing Priya's mode choice
  and the alternative.
- **Confidence**: settled (specific first-party description within the worked example)
- **Quote**: "Priya's plan isn't sensitive, so she uses auto mode and Claude screens the comparison before it posts. For a document she'd rather check first, she can switch to review mode and see the response before the channel does."
- **Our assessment**: This confirms the consent mode (Claim 3) is a per-request, user-level
  choice rather than a fixed channel-wide or connector-wide setting — the same user, same
  channel, same connector can be used in either mode depending on the individual document's
  sensitivity as judged by the user, not by a static policy attached to the connector
  itself.

### Claim 8: Activity through a personal connector is logged in that tool's own log under the requesting user's individual account — the same way direct-message use of that connector is logged today — while the channel's own work continues to log under its shared service account
- **Evidence**: Direct architectural statement about the audit-logging split, given
  immediately after the worked example.
- **Confidence**: settled (specific first-party statement of shipped logging behavior)
- **Quote**: "Everything Claude does through your connector appears in that tool's own log under your account, the way your direct-message work does today. The channel's own work stays under its service account, the one your security team already follows."
- **Our assessment**: This is a direct, load-bearing refinement of
  `blog-anthropic-agent-identity-access-model.md` Claim 5 and Claim 10 (Claude "isn't
  acting on behalf of a single user... it has its own account in each system it touches,"
  feeding a dual audit trail of Claude's own log plus each connected system's native log).
  Personal connectors introduce a third logging identity for a subset of actions:
  connector activity attributable to a specific human user's own account in that external
  tool, distinct from both the channel's agent-identity service account and Claude's
  internal audit trail. The post frames this as continuity with existing DM behavior
  ("the way your direct-message work does today"), not as a new logging mechanism — see
  Cross-References for why this is an extension of, not a contradiction to, the agent
  identity model.

### Claim 9: Users control what Claude can reach and what the channel sees via their personal connectors, the same as when using those connectors in a direct message, and can disconnect a connector at any time
- **Evidence**: Direct statement of user control, immediately following the audit-logging
  statement (Claim 8).
- **Confidence**: settled (specific first-party statement of a user-facing control)
- **Quote**: "You decide what Claude reaches and what the channel sees, the same as when you use your connectors in a direct message, and you can disconnect a connector at any time."
- **Our assessment**: "What the channel sees" is the operative phrase distinguishing this
  from ordinary DM connector use: because the output posts into a shared channel visible
  to other members, the user is not just controlling Claude's *access* (as in a DM) but
  also implicitly controlling what private-connector-derived information becomes visible
  to teammates who have no access to that connector themselves. The post does not describe
  any technical enforcement preventing a user from posting connector-derived content that
  reveals more than they intended — the review-mode option (Claim 3) is the only stated
  safeguard, and it is opt-in, not default.

### Claim 10: Personal connectors do not run unattended — any scheduled routine or any action Claude initiates on its own in a channel must use connectors an admin attached to the channel, not a member's personal connector
- **Evidence**: Direct scope-boundary statement in the "Where the channel's own connectors
  still matter" section.
- **Confidence**: settled (specific first-party architectural boundary statement)
- **Quote**: "Personal connectors don't run unattended. Scheduled routines, and anything Claude starts on its own, use the connectors an admin attached to the channel. Tools that are needed for unattended actions, or actions the entire channel relies on, should use shared connectors."
- **Our assessment**: This is the scope boundary that reconciles personal connectors with
  the existing agent-identity model rather than replacing it: personal connectors are
  additive and apply only to attended, user-initiated requests within a live thread; any
  proactive or scheduled behavior — including the four-mode proactive response decisioning
  documented in `blog-anthropic-claude-tag-context-awareness.md` — continues to run
  exclusively under the channel's admin-provisioned, agent-identity connectors. This
  statement is the reason we treat Claim 8's per-user logging as an extension of the
  agent-identity architecture rather than a conflicting claim — see Cross-References.

### Claim 11: A channel configured to rely solely on personal connectors (no admin-provisioned shared connectors) suits closely supervised collaborative work, illustrated by drafting an RFP response that pulls from sensitive pricing sources not provisioned to the whole channel; anything Claude posts remains visible to every channel member
- **Evidence**: Direct use-case description and caveat in the "Where the channel's own
  connectors still matter" section.
- **Confidence**: settled (specific first-party use-case guidance with a stated caveat)
- **Quote**: "A channel that solely relies on personal connectors suits closely supervised work. For example, collaboratively drafting an RFP response may require pulling data from pricing or other sensitive sources that are not provisioned to the entire channel. Anything Claude posts is visible to everyone in the channel."
- **Our assessment**: The explicit caveat — "anything Claude posts is visible to everyone
  in the channel" — is a plainly stated residual risk that the post does not otherwise
  resolve: even though the *source* connector access is individually scoped (only the
  requesting user can reach the pricing data), the *output* Claude posts using that data
  is channel-wide visible by default, so a user could inadvertently expose sensitive
  personal-connector-derived content to channel members who have no access to the
  underlying source. Review mode (Claim 3) is the only mitigation offered, and it requires
  the user to actively choose it.

### Claim 12: A dedicated shared-connector use case — a #on-call channel with runbook, monitoring, and deployment-history connectors attached by an admin — lets Claude identify and help remediate issues, including after work hours, because that work is unattended
- **Evidence**: Direct example given in the "Where the channel's own connectors still
  matter" section, contrasting with the personal-connector use case in Claim 11.
- **Confidence**: settled (specific first-party example use case)
- **Quote**: "For example, you may want to add Claude to your #on-call channel to help with CI triage and response. Claude can identify and help remediate issues (even after work hours) if you set up shared connectors to your runbook, monitoring tools, and deployment history."
- **Our assessment**: This example is deliberately paired with Claim 11's RFP example to
  contrast the two channel-governance models the post recommends: shared/agent-identity
  connectors for autonomous, after-hours, unattended work (on-call triage) versus
  personal-connector-only for closely supervised, attended collaborative work (RFP
  drafting) — reinforcing Claim 10's unattended/attended scope boundary with a concrete
  pair of opposite-end use cases rather than an abstract rule alone.

### Claim 13: No installation is required for personal connectors — Claude asks the user for permission the first time a request needs one of their connectors, then continues using it within that thread
- **Evidence**: Direct statement in the closing "What's next" section.
- **Confidence**: settled (specific first-party description of the first-use consent
  mechanic)
- **Quote**: "There's nothing to install. When a request of yours needs one of your connectors, Claude asks you the first time, then uses it in the thread."
- **Our assessment**: This describes a thread-scoped, not channel-scoped or account-scoped,
  permission grant: the post says the ask-once behavior applies "in the thread," implying a
  new thread on the same connector may re-trigger the permission prompt, though the post
  does not state this explicitly either way — this is our inference, not a direct claim,
  and should be verified against Claude Tag documentation before being stated as fact in
  the guide.

## Concrete Artifacts

### Priya worked example (verbatim, "Using personal connectors" section)

```
Source: claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels, Sep 24, 2026

SETUP: Priya in #checkout-migration, a channel connected to GitHub (channel-level
connector, admin-provisioned).

REQUEST (Priya's literal prompt):
"@Claude check my Google Drive doc 'Checkout migration, Q3' against what
we've shipped. What's still open?"

EXECUTION:
1. Claude reads merged pull requests through the channel's GitHub connector
   (shared/admin-provisioned scope).
2. Claude reads the doc through Priya's personal Google Drive connector
   (personal scope) — "The doc is one only Priya can open. Before, Claude
   would have stopped there."
3. Claude posts the comparison of what shipped vs. what's still open.

MODE CHOICE: Priya's plan isn't sensitive, so she uses auto mode; Claude
screens the comparison before posting. For a document she'd rather check
first, she could instead use review mode and see the response before the
channel does.
```

### Governance and scope-boundary rules (verbatim, "Governance & Consent" and "Where the channel's own connectors still matter")

```
Source: claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels, Sep 24, 2026

CONSENT MODES:
- Review mode: user sees each response before it posts to the channel.
- Auto mode: "post automatically unless Claude determines there is
  sensitive content that needs your review."
- Enterprise (not yet shipped as of this post): "admins will be able to
  require review for everyone."

ADMIN GOVERNANCE OPTIONS (three, not mutually exclusive across tools in
one channel):
1. Shared set of tools under an agent identity (admin-provisioned,
   channel-wide — the pre-existing model from
   blog-anthropic-agent-identity-access-model.md).
2. Channel members rely only on personal connectors, governed by each
   member's existing role-based access in the underlying tool.
3. Decide tool by tool (mix of 1 and 2 within a single channel).

AUDIT LOGGING SPLIT:
- Personal connector use -> logs under the user's own account in that
  tool, "the way your direct-message work does today."
- Channel's own (admin-provisioned/agent-identity) work -> logs under
  the channel's service account, "the one your security team already
  follows."

UNATTENDED-WORK BOUNDARY:
"Personal connectors don't run unattended. Scheduled routines, and
anything Claude starts on its own, use the connectors an admin attached
to the channel."

PAIRED USE-CASE CONTRAST:
- Shared/unattended: #on-call channel with runbook, monitoring, and
  deployment-history connectors -> CI triage/remediation, including
  after hours.
- Personal-only/attended: collaboratively drafting an RFP response
  pulling from pricing/sensitive sources not provisioned to the whole
  channel -> "closely supervised work," with the caveat that "anything
  Claude posts is visible to everyone in the channel."

ROLLOUT: "rolling out now on Team plans, with Enterprise to follow."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-agent-identity-access-model.md` Claim 7 (admins configure four identity
    components per channel, including "Connectors: the tools and API keys that Claude uses
    to do its job") — this post's first admin governance option (Claim 4 here: "a shared
    set of tools under an agent identity") is a direct restatement of that existing
    connector-configuration surface, confirming it is unchanged by this feature.
  - `blog-anthropic-claude-tag-employee-workflows.md` Claim 3 (Hema's scoped Claude Tag
    channel: "Claude's access is deliberately scoped: it only works from the channels and
    documents it has been granted access to, and will let her know when it does not have
    the access") — that note documents Claude reporting a missing grant rather than
    silently failing; this post's Priya example (Claim 6 here) shows the specific product
    change that closes exactly the kind of access gap Hema's note describes as a reported
    limitation, for the private-document case specifically.

- **Contradicts**: None filed. This post's Claim 8 ("Everything Claude does through your
  connector appears in that tool's own log under your account") is, read in isolation,
  in tension with `blog-anthropic-agent-identity-access-model.md` Claim 5 ("Claude isn't
  acting on behalf of a single user. It has its own account in each system it touches.")
  and Claim 4 ("Agent identity replaces the question 'what can this user do?' with 'what
  can this agent do in this compartment?'"). We did not file a contradiction issue because
  this post itself supplies the reconciling scope boundary (Claim 10: "Personal connectors
  don't run unattended... anything Claude starts on its own use[s] the connectors an admin
  attached to the channel") — the agent-identity/service-account model continues to govern
  all unattended and channel-shared work unchanged; personal connectors are an additive,
  narrowly-scoped exception that applies only to attended, in-thread, user-initiated
  requests, where Claude temporarily acts through the requesting user's own tool-level
  account for that one connector and that one request. This is a conditioning-variable
  case per MINER.md §4a ("claims differ only in context... that's not a contradiction"),
  not a case where the same claim is asserted under the same conditions by both sources.

- **Extends**:
  - `blog-anthropic-agent-identity-access-model.md`: that post's dual audit trail (Claim
    10 there — Claude's own log plus each connected system's native log, both keyed to
    the channel's service-account identity) is extended by this post's Claim 8 into a
    three-way logging picture for channels using personal connectors: Claude's internal
    log, the channel's service-account entries in each connected system, and now a third
    stream of user-account-attributed entries in each connector for personal-connector
    use specifically. Also extends that post's Claim 6 (two-level workspace/channel
    identity hierarchy) and Claim 7 (four admin-configurable identity components) by
    adding a third governance dimension inside the "Connectors" component: not just which
    connectors a channel has, but whether they are agent-identity/shared, personal/RBAC-only,
    or decided per tool (Claim 4 here).
  - `blog-anthropic-claude-tag-context-awareness.md`: that post's four-mode proactive
    response taxonomy (reply inline / start thread work / route to existing workstream /
    say nothing) and its scope-boundary statement ("It acts within the boundaries of the
    permissions, tools, and scope you have configured") describe *when and how* Claude
    decides to act using whatever connectors are already configured for the channel; this
    post's unattended-work boundary (Claim 10 here) clarifies that none of those four
    proactive modes can draw on a member's personal connector — proactive/self-initiated
    action is confined to admin-provisioned channel connectors regardless of which of the
    four response modes Claude selects.

- **Novel**:
  - **User-initiated, per-request personal connector access inside a shared channel** is a
    new capability not previously documented in the corpus's three prior Claude Tag notes,
    all of which describe only admin-provisioned, channel-scoped connector access.
  - **The review/auto consent-mode toggle for connector-derived output** is a new,
    named user-facing control not previously documented for Claude Tag.
  - **A worked example combining a channel-scoped and a personal-scoped connector in a
    single request** (Claim 6 — Priya's GitHub + Drive comparison) is the first corpus
    example of Claude drawing on two different connector-identity scopes within one
    request/response cycle.
  - **The three-tier admin governance choice for connector scoping** (agent-identity-shared
    / personal-RBAC-only / decided tool-by-tool) is new to the corpus as an explicit,
    named configuration surface.
  - **The explicit unattended-work scope boundary** (Claim 10) restricting personal
    connectors to attended use is a new architectural rule that had no prior corpus
    statement to either confirm or conflict with, since no prior source described any
    user-scoped (as opposed to channel/service-account-scoped) connector access existing
    at all.

## Guide Impact

- **Chapter 02 (Harness Engineering — connector/access scoping)**: Add personal connectors
  as a second, narrower access-scope tier alongside the existing agent-identity/service-account
  model documented via `blog-anthropic-agent-identity-access-model.md`: (1) admin-provisioned,
  channel-wide connectors for any unattended, proactive, or channel-shared work (Claim 10),
  and (2) individually-authorized, per-request personal connectors for attended work
  requiring a specific user's own private data (Claim 2, illustrated by Claim 6). Recommend
  harness designers building any multi-user shared-channel agent explicitly separate these
  two connector classes in their access model rather than assuming a single flat connector
  list per channel — this post's three-tier admin governance choice (Claim 4) is a concrete
  reference taxonomy for that separation.

- **Chapter 05 (Team Adoption — Claude Tag governance)**: Update existing Claude Tag
  coverage to note the new per-user audit-logging stream personal connectors introduce
  (Claim 8): teams relying on the channel service-account log as their complete audit
  picture (per `blog-anthropic-agent-identity-access-model.md` Claim 10) now need to also
  account for personal-connector activity, which logs separately under each individual
  user's own account in that tool. Add the review-mode vs. auto-mode choice (Claim 3) and
  the residual channel-visibility risk flagged in Claim 11 ("anything Claude posts is
  visible to everyone in the channel," even when the source data was individually scoped)
  as a specific point of adoption guidance: teams piloting personal connectors for
  sensitive-data workflows (e.g., the RFP example) should default new channels to review
  mode until the sensitivity-detection behavior in auto mode has been observed in practice,
  since the post discloses no error rate or methodology for that detection.

- **Chapter 06 (Security / Threat Model)**: Note the reconciliation between this feature and
  the agent-identity service-account model as a specific case study in scoping mixed-identity
  access within one system: rather than replacing service-account identity with per-user
  credentials, Claude Tag now supports both simultaneously, gated by a hard attended/
  unattended boundary (Claim 10) rather than a per-connector policy choice. This is a
  concrete pattern for any harness design question of "should this agent act as itself or
  as the requesting user" — the answer here is context-dependent (unattended: agent
  identity; attended, user-specific data: personal identity), not a single fixed choice.

## Extraction Notes

- **Fetch method**: An initial WebFetch call returned an AI-summarized version of the
  article (not verbatim). Per MINER.md §2a, the raw page HTML was separately retrieved via
  `curl` and stripped to plain text; every `Quote` field above was checked
  character-for-character against that independently extracted flat text (the flat-text
  extraction contained the full article body — opening section, "Using personal
  connectors," "Where the channel's own connectors still matter," and "What's next" — plus
  site navigation chrome, which was excluded from quoting) before being included in this
  note. The WebFetch summary's paraphrased renderings of these same passages were discarded
  in favor of the verbatim HTML-sourced text.
- **Full source read**: The post is a short, single-page product update (stated 5-minute
  read) with no linked sub-pages containing additional substantive content beyond a single
  "Learn more about Claude Tag" link at the close, which was not followed since it points
  to general Claude Tag documentation rather than content specific to this feature. All
  four content sections of the post (opening/lead, "Using personal connectors," "Where the
  channel's own connectors still matter," "What's next") were extracted; no claims from any
  section were skipped.
- **Contradiction assessment**: See Cross-References → Contradicts. A tension with
  `blog-anthropic-agent-identity-access-model.md`'s "Claude isn't acting on behalf of a
  single user" framing was identified and analyzed in detail, but was resolved by this
  post's own explicit scope boundary (unattended vs. attended work) rather than filed as a
  contradiction issue, per MINER.md §4a's guidance that claims differing only by context/
  conditioning variable are not contradictions.
- **Confidence rationale**: Rated `emerging` overall. Every individual claim about shipped
  or rolling-out behavior is a specific, first-party, unambiguous product description
  (several individually would merit `settled` in isolation), but the overall feature is
  one day old at time of extraction (published September 24, 2026; extracted September 25,
  2026), Team-plan-only with Enterprise "to follow" (Claim 5), and contains zero independent
  or practitioner validation — no third-party account of using personal connectors exists
  yet in the corpus or elsewhere. `emerging` reflects a brand-new, precisely-described,
  vendor-authoritative capability without any usage evidence yet, consistent with how this
  corpus rated the June 2026 agent-identity announcement and the August 2026
  context-awareness update at comparable maturity stages.
