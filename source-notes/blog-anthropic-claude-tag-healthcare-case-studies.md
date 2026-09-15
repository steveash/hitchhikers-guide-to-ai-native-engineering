---
source_url: https://claude.com/blog/how-healthcare-organizations-use-claude-tag
source_type: blog-post
title: "How healthcare organizations use Claude Tag"
author: Camy Pearson, Maria Howe, Araba Koomson
date_published: 2026-09-14
date_extracted: 2026-09-15
last_checked: 2026-09-15
status: current
confidence_overall: emerging
issue: "#3450"
---

# How healthcare organizations use Claude Tag

> First-party Anthropic case-study post giving three named healthcare organizations
> (Insight Health, Tennr, Medallion) using Claude Tag in Slack, each with concrete
> PHI-avoidance access patterns and quantified or named outcomes — a dual-agent
> incident-response pairing with per-agent PHI/non-PHI access split, a non-technical
> team maintaining production code through a persistent Claude Tag channel, and a
> knowledge-silo-breaking payer-rules Q&A pattern with human expert oversight.

## Source Context

- **Type**: blog-post (official claude.com blog, published September 14, 2026;
  bylined to three authors: Camy Pearson, Maria Howe, Araba Koomson)
- **Author credibility**: First-party Anthropic blog post, structured as three
  named-company case studies with named executive quotes: Saran Siva (Insight
  Health co-founder and CTO), Abe Griffiths (Tennr VP of Business Operations and
  Strategy), and Armaan Sarkar (Medallion CTO). This is vendor-published customer
  testimonial content — strong signal that these are real production deployments
  with named, quotable executives willing to attach their names to specific
  metrics, but not independently audited, and the post has an obvious incentive to
  present Claude Tag favorably. The post explicitly discloses a real limitation
  up front (Claude Tag is not yet BAA-covered), which is a stronger credibility
  signal than a purely promotional post would be expected to include.
- **Scope**: Covers Claude Tag's healthcare-specific security posture (channel
  gating, connector scoping, workspace-visibility limits, access bundles) and
  three named-company deployments: incident-response triage at Insight Health,
  internal-tooling maintenance at Tennr, and payer-rules knowledge-sharing at
  Medallion. Ends with a "getting started" rollout recommendation. Does NOT
  cover: pricing beyond the time-limited enterprise credit promo, the technical
  implementation of "access bundles" or the agent identity model beyond a one-line
  pointer to `blog-anthropic-agent-identity-access-model.md`, the Claude Agent SDK
  architecture of Insight Health's second agent ("Zeus") beyond naming it, or any
  quantitative detail on Tennr's or Medallion's outcomes beyond what is stated
  (Tennr and Medallion give no equivalent to Insight Health's 97% figure).

## Extracted Claims

### Claim 1: Claude Tag is not yet covered by Anthropic's Business Associate Agreement, so the healthcare organizations profiled use it only in channels and with connectors that never touch PHI
- **Evidence**: Direct disclosure statement at the top of the post, immediately
  followed by the four security mechanisms (Claims 2-4) that make PHI avoidance
  operationally enforceable rather than merely a policy.
- **Confidence**: settled (direct first-party statement of current product/compliance
  status, not a claim requiring independent verification of intent)
- **Quote**: "While Claude Tag isn't yet covered by Anthropic's Business Associate Agreement, several healthcare organizations are using it today in channels and with connectors that never touch protected health information (PHI)."
- **Our assessment**: This is the load-bearing constraint for the entire post: every
  pattern described afterward (dual-agent PHI/non-PHI split at Insight Health,
  Tennr's PHI confined to a separate limited set of private channels, Medallion's
  "policy level, not individual patients or providers" framing) is a direct
  consequence of this one compliance gap. For the guide, this is a concrete,
  named example of an organization publicly working around a specific, disclosed
  compliance limitation of a beta product rather than waiting for full compliance
  coverage or avoiding the product entirely — a middle path between "wait for
  BAA coverage" and "use it everywhere."

### Claim 2: Claude Tag can be switched off by default and enabled only in approved channels, with direct messages disabled and connectors scoped per channel
- **Evidence**: First bullet point in the post's "admins decide where Claude Tag
  works" security list.
- **Confidence**: settled (specific first-party description of a shipped admin
  control)
- **Quote**: "Claude Tag can be off by default and enabled only in approved channels, with DMs disabled and connectors scoped per channel."
- **Our assessment**: This is an off-by-default, allowlist posture rather than an
  on-by-default, denylist posture — the more conservative of the two rollout
  defaults, and consistent with the "start with a baseline profile in a few
  channels" incremental-grant recommendation already documented in
  `blog-anthropic-agent-identity-access-model.md` Claim 11. Disabling DMs
  specifically is notable: it forecloses a private, unaudited one-on-one channel
  between an employee and Claude Tag, forcing all interaction into visible,
  admin-approved channels — directly relevant to any guide section on rollout
  controls for regulated environments.

### Claim 3: Claude Tag only sees what a workspace member can see — it can read and keyword-search public channels but has no access to private channels it hasn't been invited to
- **Evidence**: Second bullet point in the security list, stated as a scope
  limitation rather than a configurable option.
- **Confidence**: settled (specific first-party description of a structural
  access limitation, not an admin-toggled setting)
- **Quote**: "Claude Tag doesn't read all of Slack – instead, it only sees what a workspace member sees. While it can read the public channels of the workspace and search them by keyword, it doesn't have access to private channels it hasn't been invited to."
- **Our assessment**: This is a structural (not merely policy-level) boundary:
  Claude Tag's visibility is modeled on a workspace member's own Slack
  permissions, not a superuser view of the workspace. This corroborates and
  gives Slack-specific mechanism detail for the "workspace-level security
  boundaries" principle already documented in `blog-anthropic-human-agent-teams.md`
  Claim 4 — here the boundary is literally "private channel invitation status,"
  the same primitive Slack already uses to control human visibility.

### Claim 4: "Access bundles" let a team connect non-PHI data sources like a codebase and issue tracker in one channel while keeping the EHR, clinical systems, and patient communications inaccessible
- **Evidence**: Third bullet point in the security list, naming the specific
  mechanism used to achieve the PHI/non-PHI split described in the Insight Health
  case study (Claim 5).
- **Confidence**: settled (specific first-party description of a named product
  feature)
- **Quote**: "Access bundles let a team connect data sources like its codebase and issue tracker in one channel while the EHR, clinical systems, and patient communications are inaccessible."
- **Our assessment**: "Access bundles" is a named configuration primitive that
  bundles a set of connectors as a unit scoped to a channel — this is the concrete
  product mechanism underlying the "connectors scoped per channel" claim (Claim 2)
  and the channel-level override half of the two-level identity hierarchy already
  documented in `blog-anthropic-agent-identity-access-model.md` Claim 6. The
  specific examples given (EHR, clinical systems, patient communications, as the
  excluded category) are healthcare-specific instantiations of what "PHI-bearing
  systems" concretely means for this vertical.

### Claim 5: At Insight Health, Claude Tag and a second agent (Zeus, built on the Claude Agent SDK) are deliberately given different access — Claude Tag holds codebase and ticket-system access while Zeus alone can query production data, masking PHI before it reaches Slack
- **Evidence**: Direct architectural description of the two-agent incident-response
  pairing in the Insight Health section.
- **Confidence**: emerging (single named company's production architecture,
  described by the vendor rather than by Insight Health directly, though attributed
  to a named co-founder/CTO elsewhere in the same section)
- **Quote**: "The two agents have deliberately different access: Claude Tag sees the codebase and Linear, so it knows the code patterns and ticket history; Zeus runs on the company's BAA-covered Claude API organization, so it can query production data, masking PHI before the data reaches Slack."
- **Our assessment**: This is the most concrete multi-agent access-partitioning
  pattern in the corpus to date, and it maps directly onto the "shared state" and
  "orchestrator-subagent" mechanics taxonomy in
  `blog-anthropic-multi-agent-coordination-patterns.md`, but with an access-control
  dimension that taxonomy does not name: the two agents are partitioned not by
  what *type* of work they do, but by which *compliance tier* of data each may
  touch (Claude Tag = non-PHI/BAA-free; Zeus = BAA-covered API org with PHI
  masking as a further control). This is a direct, healthcare-specific
  instantiation of the "context-centric decomposition" principle from that
  taxonomy's Claim 13 ("divide work by what context each agent needs"), here
  applied as "divide work by what data-compliance tier each agent may access."

### Claim 6: Since Claude Tag went live at Insight Health, 97% of alerts in its critical alert channel have closed without an engineer having to step in
- **Evidence**: Single quantitative outcome metric, attributed to the post
  without a named methodology, sample period definition (beyond "since Claude Tag
  went live," itself dated elsewhere in the same section as "the past three
  months"), or independent audit.
- **Confidence**: anecdotal (single company's self-reported, vendor-published
  metric; no baseline comparison period stated, no definition of "critical alert
  channel" volume given)
- **Quote**: "Since Claude Tag went live, 97% of alerts in Insight Health's critical alert channel have closed without an engineer having to step in, freeing the team to focus on core product work."
- **Our assessment**: This is the headline metric of the post and should be
  treated with the same caution as other single-company, vendor-published
  percentage claims in this corpus (e.g., the "~30% better" proactivity figure in
  `blog-anthropic-claude-tag-context-awareness.md` Claim 1) — plausible given the
  described mechanism (dual-agent investigation plus draft-PR-then-human-merge
  workflow, Claim 7 below), but not independently reproducible from this source.
  Note the metric is specifically "closed without an engineer having to step in,"
  not "resolved correctly" or "resolved without any human review" — a draft PR
  is still opened and a human still merges it (Claim 7), so this 97% figure
  measures triage/investigation autonomy, not full end-to-end unsupervised
  remediation.

### Claim 7: The Insight Health agents run a full incident pipeline — investigate the alert, compare it against code/deploys/past tickets, open a draft PR, monitor tests — before an engineer reviews and merges
- **Evidence**: Direct step-by-step description of the incident workflow.
- **Confidence**: settled (specific first-party description of a shipped
  workflow, naming each pipeline stage and where human review occurs)
- **Quote**: "When an alert arrives, the agents investigate it–querying production data, checking it against the code and recent deploys, and comparing it to past tickets–all while reporting on their progress in the Slack thread. Once they identify the root cause, they open a draft PR and monitor the tests, and finally an engineer reviews and merges."
- **Our assessment**: The human checkpoint is placed at the very end of the
  pipeline (PR review and merge), not at intermediate investigation steps — the
  agents are trusted to investigate, diagnose, and draft a fix autonomously, with
  the human review concentrated on the single artifact (a tested draft PR) rather
  than on each investigative step. This is a concrete instance of the "trust
  proportional to demonstrated reliability, checkpoint placed at the highest-
  leverage point" pattern that complements the trust-ramp guidance in
  `blog-anthropic-human-agent-teams.md` Claim 9, here made specific to an
  incident-response pipeline: verify the diff and passing tests, not each
  intermediate investigative claim.

### Claim 8: Claude Tag's persistent channel memory lets it recognize a new complaint as a known issue with a fix already pending, recall investigations from weeks earlier, and follow standing instructions without being re-prompted
- **Evidence**: Direct description of channel-memory behavior in the incident-
  response workflow, immediately following the pipeline description (Claim 7).
- **Confidence**: emerging (first-party description of observed behavior in one
  company's deployment; no frequency or accuracy data on how often memory recall
  is correct vs. stale/wrong)
- **Quote**: "Claude Tag's channel memory is valuable here: it recognizes a new complaint as a known issue with a fix pending, recalls investigations from weeks earlier, and follows standing instructions unprompted."
- **Our assessment**: This is a concrete illustration of channel-scoped persistent
  memory doing real deduplication work in a high-volume production-alerts
  channel specifically, extending the general "channel memory means long-running
  work never needs re-explaining" framing stated earlier in the same post's
  overview paragraph into a named, valuable behavior: recognizing that an
  incoming alert is a duplicate of an already-tracked issue, which directly
  supports the "files and de-duplicates tickets" capability named earlier in the
  Insight Health section.

### Claim 9: Transparency into both agents' reasoning and division of labor, visible to the whole Slack channel, builds team trust and teaches the team how to extract value from the agents
- **Evidence**: Direct quote from Insight Health's co-founder and CTO.
- **Confidence**: anecdotal (single executive's stated rationale; no measurement
  of "trust" or of any behavior change attributed to this transparency)
- **Quote**: "Everyone in the Slack channel sees both agents' reasoning and how they divide the work," said Saran Siva, Insight Health's co-founder and CTO. "That transparency builds trust and teaches the team how to get the most value out of the agents."
- **Our assessment**: This names a specific mechanism — shared visibility into
  *both* agents' reasoning and their division of labor between each other, not
  just each agent's output — as the trust-building lever in a two-agent,
  human-observed setup. This extends the "work in public" principle from
  `blog-anthropic-human-agent-teams.md` Claim 3 to the multi-agent case
  specifically: it is not only human-agent interaction that should be public,
  but agent-to-agent coordination and division of labor as well, so the humans
  supervising the pair can audit not just what was done but who decided to do
  which part.

### Claim 10: Tennr made Claude Tag the primary maintainer of an internal recruiting tool, letting non-technical staff (recruiters, People team, hiring managers, RevOps) ship production code changes via plain-language Slack requests
- **Evidence**: Direct description of the recruiting.tennr.com deployment,
  naming the specific non-technical roles who interact with the channel.
- **Confidence**: emerging (single company's described practice, corroborated
  with specific shipped-ticket examples in Claim 11)
- **Quote**: "Now the people who actually use the tool (recruiters, People team members, hiring managers, and RevOps) @-mention Claude with requests in plain language English, and Claude ships the code change, deploys it, and reports back. They can iterate on the tool directly, without pulling engineers off product work."
- **Our assessment**: This extends the non-engineer-as-Claude-Tag-channel-owner
  pattern already documented for a single individual (Molly Villagra, legal, in
  `blog-anthropic-claude-tag-employee-workflows.md` Claim 7) to an entire
  multi-role team maintaining a shared production tool, with "Claude ships the
  code change, deploys it" stated as the default behavior — a materially higher
  autonomy grant than Molly's review-and-flag channel, since here Claude Tag is
  making and deploying code changes without an engineer in the loop by default
  (see also Claim 13, where the company's stated rationale for this posture is
  explicit).

### Claim 11: In roughly a month, Tennr shipped 15+ tickets through the Claude Tag channel, including a proactive, unprompted incident notice when a bug briefly miscalculated candidate compensation
- **Evidence**: Named list of shipped work plus one specific unprompted-response
  example.
- **Confidence**: anecdotal (single company, single month, self-reported ticket
  count with illustrative examples rather than a full ticket log)
- **Quote**: "In roughly a month, the team shipped 15+ tickets this way: a benefits deep-dive section built from an uploaded PDF one-pager, a "Sign your offer here" banner linking to Dropbox Sign, target bonus fields, and self-service admin controls. When a publicly exposed copy API was flagged, Claude locked it down the same day. When an Ashby import bug kept resetting equity on live offers, Claude fixed the bug and propagated the corrected values. When a separate bug briefly showed candidates variable comp incorrectly, Claude posted a channel-wide notice with the affected window and remediation without being asked."
- **Our assessment**: The unprompted incident notice ("without being asked") for
  a comp-display bug is the most consequential single behavior in this claim: it
  shows Claude Tag proactively self-reporting a data-accuracy incident affecting
  end users, rather than waiting to be asked whether anything was wrong — a
  concrete instance of the "north star"-guided productive proactivity described
  abstractly in `blog-anthropic-human-agent-teams.md` Claim 7, here applied to
  incident self-disclosure specifically rather than feature suggestion.

### Claim 12: The Tennr team taught Claude Tag its own in-channel operating conventions (an emoji status legend and a specific ticket format), and Claude adopted them going forward
- **Evidence**: Direct description of channel-specific convention-teaching and
  adoption.
- **Confidence**: anecdotal (single company's described practice; no detail on
  how the conventions were taught — e.g., standing instructions vs. in-context
  correction)
- **Quote**: "The team taught Claude its own ops conventions in-channel, including an emoji status legend, and a ticket format with numbered tickets, requester, commit link, screenshots, and a live test link. Claude adopted them going forward."
- **Our assessment**: This is a lighter-weight, team-authored analog to the
  standing-instruction-evolution pattern already documented in
  `blog-anthropic-claude-tag-employee-workflows.md` Claims 9-10 (Molly's
  real-time correction becoming a permanent instruction, later formalized into a
  weekly review routine) — here the convention (ticket format, emoji legend) is
  established once by the team and durably adopted, without the weekly-review
  formalization layer described in that other case study. Together the two
  sources suggest channel-specific convention-teaching is a recurring,
  low-effort Claude Tag adoption practice across different company contexts.

### Claim 13: Tennr's VP of Business Operations and Strategy explicitly ties the willingness to grant Claude Tag high autonomy to per-channel access scoping — full autonomy (skip PR review, ship directly) in the low-risk offer-tool channel, but not in Product or Eng channels
- **Evidence**: Direct quote explaining the channel-differentiated autonomy
  posture and the stated reason it was acceptable.
- **Confidence**: emerging (single executive's stated rationale for one company's
  configuration choice; not independently validated risk analysis)
- **Quote**: "In the offer tool channel, we want Claude to be proactive: fix problems, modify code, skip PR reviews, and ship," Griffiths said. "That posture would obviously be wrong for, say, a Product or Eng channel where Claude's role is closer to info gathering or keeping us organized. Being able to draw those lines channel by channel meant we could give Claude real autonomy where it's low risk without granting it everywhere."
- **Our assessment**: This is a clean, named counterexample to a "consistent
  autonomy policy across the org" model: the same company runs Claude Tag at
  a much higher autonomy level (skipping PR review entirely) in one channel than
  in others, and frames per-channel scoping specifically as what makes that
  differentiation *safe* rather than reckless. This is a concrete instantiation
  of the two-level workspace/channel identity hierarchy in
  `blog-anthropic-agent-identity-access-model.md` Claim 6, but applied to
  *autonomy level* (does Claude skip human review before shipping?) rather than
  to *data/connector access* — a dimension that source note's identity taxonomy
  does not explicitly separate out. Worth flagging for the guide as a distinct
  configurable axis: per-channel data access and per-channel review-gating
  autonomy can and should be set independently.

### Claim 14: At Medallion, Claude Tag breaks a knowledge silo around undocumented payer rules by answering engineers' questions from accumulated past expert responses, tagging in a human expert when it isn't confident, and having that expert's answer become the basis for future answers
- **Evidence**: Direct description of the workflow plus a quote from Medallion's
  CTO describing the escalation mechanism.
- **Confidence**: emerging (single company's described practice and CTO
  characterization; no data on how often Claude Tag answers directly vs. escalates,
  or on answer accuracy)
- **Quote**: "When it isn't confident, it tags in the right expert, and their response becomes the basis for future answers on related topics," said CTO Armaan Sarkar.
- **Our assessment**: The self-reported confidence-gated escalation ("when it
  isn't confident, it tags in the right expert") is the key mechanism here, and
  the compounding structure — each expert answer becomes reusable context for
  future related questions — is what actually breaks the silo, rather than a
  one-off Q&A. This is a domain-general pattern (accumulate expert corrections
  as durable, searchable context rather than losing them after a single
  exchange) that generalizes well beyond payer rules to any domain where
  expertise currently lives ephemerally in individual experts' heads; it is a
  narrower, escalation-triggered variant of the "domain expert feedback becomes
  standing instructions" pattern in `blog-anthropic-claude-tag-employee-workflows.md`
  Claims 9-10, but triggered by low agent confidence rather than by a human
  proactively correcting an already-given answer.

### Claim 15: Medallion's comfort deploying Claude Tag for payer-rules Q&A rests on three factors — operating at the policy level rather than on individual patient/provider data, ongoing expert oversight of answers, and downstream automated validation of the actions those policies drive
- **Evidence**: Direct enumeration of the CTO's stated rationale for why the
  deployment was acceptable, immediately following the escalation-mechanism
  quote (Claim 14).
- **Confidence**: emerging (single executive's stated risk rationale, not an
  independently audited risk assessment)
- **Quote**: "Sarkar points to picking the right PHI-free workstreams, expert review, and automated validation. Claude Tag operates at the policy level: the questions are about payer rules and process, not individual patients or providers. It doesn't answer alone: experts provide oversight and corrections, and every exchange happens in a Slack channel anyone at the company can audit. And the outputs get checked downstream, since Medallion's systems use these policies to take actions that are audited and validated on their own."
- **Our assessment**: This three-factor rationale (data-category selection +
  human review + downstream automated validation) is a reusable risk-mitigation
  checklist for any team considering a Claude Tag deployment in a
  regulated-adjacent domain: choose data categories that are inherently
  lower-risk (policy/process knowledge rather than individual records), keep a
  human review step even when the agent answers directly, and rely on an
  independent downstream check rather than trusting the Q&A answer as the final
  authority. This is more structured than the single-factor rationales given
  in the Insight Health and Tennr sections and is worth extracting as its own
  named checklist for the guide.

### Claim 16: The recommended rollout path is to start with one engineering, product, ops, or recruiting channel with one or two connectors, work in open threads rather than DMs, and run a two-week trial before widening the allowlist
- **Evidence**: Direct prescriptive guidance in the post's closing "Getting
  started" section, framed as the common starting point across all three
  profiled companies.
- **Confidence**: settled (direct first-party recommendation, and factually
  consistent with the channel types actually named for each of the three
  companies earlier in the post)
- **Quote**: "The teams above all started in the same place: engineering, product, ops, or recruiting channels, with one or two connectors, working in open threads rather than DMs so the whole team could review and pick up context." / "Review the Claude Tag best practices for healthcare organizations, here, then start with one channel. Turn Claude Tag on for an alert or support-engineering channel, connect GitHub, and let the team work with it for two weeks before widening the allowlist."
- **Our assessment**: The "open threads rather than DMs, so the whole team could
  review and pick up context" rationale is the same "work in public" principle
  from `blog-anthropic-human-agent-teams.md` Claim 3, here given as an explicit
  rollout instruction rather than a general team-hygiene principle, plus a
  concrete phase length (two weeks) not given in that more general post. This
  is directly actionable rollout guidance: pick one non-PHI channel, one or two
  connectors, GitHub if applicable, and a fixed two-week observation window
  before expanding — a more specific timeline than the "read the audit trail,
  extend where the work justifies it" guidance in
  `blog-anthropic-agent-identity-access-model.md` Claim 11, which does not name
  a specific trial duration.

## Concrete Artifacts

### Security mechanisms enabling PHI-free Claude Tag use (verbatim, from the post's bulleted list)

```
Source: claude.com/blog/how-healthcare-organizations-use-claude-tag, Sep 14, 2026

1. Channel gating: "Claude Tag can be off by default and enabled only in
   approved channels, with DMs disabled and connectors scoped per channel."

2. Workspace-relative visibility: "Claude Tag doesn't read all of Slack –
   instead, it only sees what a workspace member sees. While it can read the
   public channels of the workspace and search them by keyword, it doesn't
   have access to private channels it hasn't been invited to."

3. Access bundles: "Access bundles let a team connect data sources like its
   codebase and issue tracker in one channel while the EHR, clinical systems,
   and patient communications are inaccessible."

Compliance status disclosed up front: "Claude Tag isn't yet covered by
Anthropic's Business Associate Agreement" — hence the PHI-free channel/connector
scoping above.
```

### Insight Health: dual-agent incident-response pipeline

```
Source: claude.com/blog/how-healthcare-organizations-use-claude-tag, Sep 14, 2026

Company: Insight Health (builds MagicDocs, an AI referral coordinator;
  1,100+ practices, 56 specialties)
Setup: Claude Tag + "Zeus" (Insight Health's own agent, built on the
  Claude Agent SDK), running in production alert channels for ~3 months
  at time of publication

ACCESS SPLIT:
  Claude Tag -> codebase + Linear (ticket history, code patterns)
  Zeus       -> BAA-covered Claude API org -> production data,
                masking PHI before it reaches Slack

PIPELINE:
  alert arrives
    -> agents investigate (query prod data, check code/deploys, compare
       to past tickets), reporting progress in the Slack thread
    -> agents identify root cause
    -> agents open a draft PR, monitor tests
    -> engineer reviews and merges

CHANNEL MEMORY BEHAVIOR:
  - recognizes new complaint as a known issue with a fix pending
  - recalls investigations from weeks earlier
  - follows standing instructions unprompted

OUTCOME (self-reported, not independently audited):
  "97% of alerts in Insight Health's critical alert channel have closed
  without an engineer having to step in"

Other stated uses at Insight Health: hiring, vendor negotiation prep,
contract review against call transcripts, general business operations.
```

### Tennr: Claude Tag as internal-tool maintainer

```
Source: claude.com/blog/how-healthcare-organizations-use-claude-tag, Sep 14, 2026

Company: Tennr (patient orchestration / intake automation platform)
Tool: recruiting.tennr.com, an internal offer-presentation portal built
  in Claude Code; launched July 2026; Claude Tag made "primary maintainer"
  via a dedicated Slack channel
Users: recruiters, People team members, hiring managers, RevOps
  (non-technical; @-mention Claude with plain-language requests)

~1 MONTH OF SHIPPED WORK (15+ tickets), examples given:
  - benefits deep-dive section built from an uploaded PDF one-pager
  - "Sign your offer here" banner linking to Dropbox Sign
  - target bonus fields
  - self-service admin controls
  - locked down a publicly exposed copy API the same day it was flagged
  - fixed an Ashby import bug that reset equity on live offers, and
    propagated corrected values
  - posted an unprompted, channel-wide notice (affected window +
    remediation) when a separate bug briefly miscalculated candidate
    variable comp
  - wrote onboarding documentation; handles permission management

TEAM-TAUGHT CONVENTIONS (adopted by Claude going forward):
  - an emoji status legend
  - ticket format: numbered ticket, requester, commit link, screenshots,
    live test link

PER-CHANNEL AUTONOMY POSTURE (Abe Griffiths, VP Business Ops & Strategy):
  Offer-tool channel: "fix problems, modify code, skip PR reviews, and ship"
  Product/Eng channels: role "closer to info gathering or keeping us
  organized" — explicitly NOT given the same skip-review autonomy
  Rationale: "Being able to draw those lines channel by channel meant we
  could give Claude real autonomy where it's low risk without granting
  it everywhere."

Rollout note: "Tennr only allows PHI in a limited set of private channels,
so adding Claude Tag broadly didn't introduce a new data problem."
```

### Medallion: payer-rules knowledge-silo breaking

```
Source: claude.com/blog/how-healthcare-organizations-use-claude-tag, Sep 14, 2026

Company: Medallion (provider credentialing, licensing, payer enrollment)
Problem: arcane, undocumented payer/state rules historically known only
  to a small group of in-house domain experts -> human bottleneck for
  engineers codifying process into product

WORKFLOW:
  engineer asks payer-rules question in Slack
    -> Claude Tag answers from past expert responses + historical data +
       unstructured internal resources
    -> if not confident, tags in the right expert
    -> expert's response becomes basis for future answers on related topics
  (expertise accumulates in an auditable channel, not one person's head)

RISK RATIONALE (CTO Armaan Sarkar), three factors:
  1. PHI-free workstream selection: "operates at the policy level... not
     individual patients or providers"
  2. Expert oversight: "experts provide oversight and corrections"
  3. Downstream automated validation: "Medallion's systems use these
     policies to take actions that are audited and validated on their own"
  Plus: "every exchange happens in a Slack channel anyone at the company
  can audit"
```

### Getting-started rollout recommendation (verbatim)

```
Source: claude.com/blog/how-healthcare-organizations-use-claude-tag, Sep 14, 2026

"The teams above all started in the same place: engineering, product,
ops, or recruiting channels, with one or two connectors, working in
open threads rather than DMs so the whole team could review and pick
up context."

"Review the Claude Tag best practices for healthcare organizations,
here, then start with one channel. Turn Claude Tag on for an alert or
support-engineering channel, connect GitHub, and let the team work with
it for two weeks before widening the allowlist."

Also noted: enterprise organizations that activate Claude Tag and link
it to GitHub receive $25,000 in Claude Tag credit ($2,500 for Team
organizations with 10+ seats); credits expire October 1, 2026.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-agent-identity-access-model.md` Claim 6 (two-level
    workspace/channel identity hierarchy) and Claim 11 (start with a baseline
    profile, extend one deliberate grant at a time): the "access bundles" per
    channel (Claim 4 here) and the getting-started two-week trial (Claim 16
    here) are concrete, named-company instances of exactly this architecture
    and rollout discipline, applied specifically to a regulated (PHI) vertical.
  - `blog-anthropic-human-agent-teams.md` Claim 3 ("work in public" — agents can
    only use what's written down and searchable) and Claim 4 (workspace-level
    security boundaries remove decision fatigue): Claim 3 here (Claude Tag's
    visibility mirrors a workspace member's own Slack access) and Claim 16 here
    (open threads over DMs "so the whole team could review and pick up context")
    are direct practitioner confirmations of both principles in a healthcare
    deployment context.
  - `blog-anthropic-human-agent-teams.md` Claim 9 (trust granted proportional to
    demonstrated reliability, expanded deliberately): Tennr's per-channel
    autonomy differentiation (Claim 13 here — full autonomy in the low-risk
    offer-tool channel, conservative posture elsewhere) is a concrete,
    channel-granular instance of this principle, and extends it by showing the
    "proportional trust" dimension can vary *by channel within the same company*
    at the same point in time, not just ramp upward over time for one agent.
  - `blog-anthropic-claude-tag-employee-workflows.md` Claim 3 (Hema's scoped-access
    private channel; Claude reports rather than silently works around missing
    access) and Claims 9-10 (in-channel feedback becoming a standing instruction,
    later a scheduled review routine): Tennr's team-taught ops conventions
    (Claim 12 here) are a lighter-weight version of the same convention-teaching
    pattern, corroborating that this is a repeatable practice across different
    companies' Claude Tag deployments, not a one-off.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 13
    (context-centric decomposition: divide work by what context each agent
    needs, not by work type): Insight Health's Claude Tag/Zeus access split
    (Claim 5 here) instantiates this principle with a compliance-tier axis
    (BAA-covered vs. not) that the original taxonomy does not explicitly name.

- **Contradicts**: None identified. No claim in this post conflicts with the
  access-model, human-agent-teaming, or multi-agent-coordination framing already
  in the corpus; this post supplies healthcare-vertical practitioner evidence
  consistent with all of it.

- **Extends**:
  - `blog-anthropic-agent-identity-access-model.md`: that post specifies the
    identity/access architecture in the abstract (workspace/channel hierarchy,
    four configurable components, credential isolation). This post shows three
    named companies configuring that architecture specifically to exclude PHI,
    including the first corpus example of a *compliance-tier* access split
    between two cooperating agents (Insight Health's Claude Tag vs. Zeus).
  - `blog-anthropic-human-agent-teams.md`: that post's four lessons and trust-ramp
    model are prescriptive and mostly illustrated with single-employee Anthropic-
    internal anecdotes. This post supplies three external, named-company
    instances, including the first corpus example of per-channel (not
    per-agent-over-time) autonomy differentiation as a deliberate governance
    choice (Tennr, Claim 13).
  - `blog-anthropic-claude-tag-employee-workflows.md`: that post documents
    named-individual, cross-functional (non-engineering) Claude Tag use at
    Anthropic itself. This post documents named-company, cross-functional use at
    three external healthcare organizations, in a regulated data environment that
    Anthropic's own internal examples did not need to navigate (Anthropic
    employees were not shown working around a PHI/BAA constraint).
  - `blog-anthropic-carta-healthcare-context-engineering.md`: that post covers a
    different healthcare AI use case entirely (structured clinical-data
    extraction via context engineering, not a Slack-based human-agent team) and
    does not mention Claude Tag. The two sources corroborate only at the level of
    "healthcare organizations are willing to name themselves and share concrete
    metrics for production Claude deployments" — there is no overlap in
    technical pattern.

- **Novel**:
  - **Compliance-tier-based multi-agent access partitioning**: Insight Health's
    Claude Tag (non-PHI, non-BAA) vs. Zeus (BAA-covered API org, PHI-masking)
    split (Claim 5) is the first corpus example of two cooperating agents
    partitioned specifically by which data-compliance tier each may touch, as
    opposed to by task type or context need.
  - **Per-channel autonomy-gate differentiation within one company**: Tennr's
    explicit "skip PR review and ship" posture in one channel vs. a
    conservative, review-gated posture in others (Claim 13) is a distinct
    governance axis (review-gating autonomy) from per-channel data/connector
    access, not previously separated out in the corpus's identity/access
    coverage.
  - **A three-factor risk-acceptance checklist for regulated-adjacent Q&A
    deployments**: Medallion's policy-level-not-individual-data + expert
    oversight + downstream automated validation rationale (Claim 15) is a named,
    reusable checklist not present in prior corpus coverage of Claude Tag risk
    posture.
  - **Unprompted incident self-disclosure to end users**: Tennr's Claude Tag
    posting a channel-wide notice about a comp-display bug "without being asked"
    (Claim 11) is a new instance of proactive self-reporting distinct from the
    unprompted-legal-issue-resolution example in
    `blog-anthropic-claude-tag-employee-workflows.md` Claim 8 — here the
    unprompted action is disclosure of the agent's own team's user-facing
    incident, not resolution of a previously flagged item.
  - **A named, fixed two-week trial period before widening the allowlist**
    (Claim 16) is a more specific rollout timeline than the "read the audit
    trail, extend where the work justifies it" guidance in
    `blog-anthropic-agent-identity-access-model.md` Claim 11, which does not
    commit to a duration.

## Guide Impact

- **Chapter 05 (Team Adoption — Regulated Environments)**: Add a new subsection
  on adopting Claude Tag (or similar persistent-channel agents) in
  compliance-constrained environments before full compliance coverage exists,
  using this post's PHI/BAA framing as the model: (1) explicitly identify which
  systems/data categories are off-limits given the current compliance gap, (2)
  use channel gating, DM disabling, and connector/access-bundle scoping to make
  that boundary structural rather than policy-only, (3) where two agents must
  cooperate and one needs access to the sensitive data, partition by compliance
  tier (Claim 5) rather than granting both agents the same access "for
  simplicity." Cite Medallion's three-factor risk checklist (Claim 15) as a
  reusable risk-acceptance framework: policy-level not individual-record data,
  ongoing expert review, and independent downstream validation.

- **Chapter 05 (Team Adoption — Rollout)**: Add the specific getting-started
  recipe (Claim 16) as a concrete rollout template, more specific than existing
  guidance: pick one eng/product/ops/recruiting channel, one or two connectors,
  open threads (not DMs), a fixed two-week trial, then widen the allowlist.

- **Chapter 02 (Harness Engineering — Access Control)**: Add per-channel
  autonomy-gating (whether an agent may skip human review before shipping,
  Claim 13) as a configuration axis distinct from per-channel data/connector
  access (already covered via `blog-anthropic-agent-identity-access-model.md`).
  A team may reasonably want to vary these two axes independently — Tennr grants
  wide data access and skip-review autonomy in one narrow, low-risk channel while
  keeping both tighter elsewhere.

- **Chapter 02 (Harness Engineering — Multi-Agent Patterns)**: Add
  compliance-tier partitioning as a named instance of context-centric
  decomposition (extending `blog-anthropic-multi-agent-coordination-patterns.md`
  Claim 13) for any system where some agents must touch regulated data and
  others should not: give the regulated-data agent its own credential path
  (here, a BAA-covered API org) and have it pre-filter/mask before handing
  results to the non-regulated agent, rather than routing raw sensitive data
  through a shared context.

- **Chapter 03 (Safety and Verification)**: Add Insight Health's pipeline
  checkpoint placement (Claim 7 — human review concentrated at the final
  draft-PR-and-passing-tests stage, not at each investigative step) as a
  concrete example of where to place the human-in-the-loop gate in an
  autonomous investigation-to-fix pipeline, alongside the caveat (Claim 6) that
  the reported 97% "closed without engineer intervention" figure measures
  triage/investigation autonomy specifically, not unsupervised end-to-end
  remediation (a human still reviews and merges every PR).

## Extraction Notes

- **Fetch method**: WebFetch on this URL returned a compact AI-generated
  summary rather than verbatim article text (consistent with prior notes on
  this domain — see Extraction Notes in
  `blog-anthropic-claude-tag-employee-workflows.md` and
  `blog-anthropic-claude-tag-context-awareness.md`). The raw page HTML was
  downloaded directly via `curl` with a browser user agent and stripped to flat
  text with a Python script (script and stylesheet blocks removed, tags
  stripped, HTML entities unescaped). Every `Quote` field above was located and
  verified character-for-character against that flat-text extraction and, for
  several passages, against the surrounding raw HTML directly (to confirm
  paragraph boundaries and rule out `<br>`-joined sentences being misread as a
  single run-on sentence). Curly quotes/apostrophes in the source are rendered
  here as straight quotes, consistent with prior notes' convention; one
  em-dash-joined clause in the Insight Health section ("investigate it–querying
  production data...") is reproduced with the source's own dash usage.
- **Full source read**: The article's entire body was extracted from the flat
  text (lines ~186–214 of the stripped output): the overview, the
  three-bullet security list, the three named-company case studies, and the
  closing "Getting started" section. Nothing in the article body was skipped.
  No sub-pages were followed; the article links to
  `blog-anthropic-agent-identity-access-model.md` (already in the corpus, cited
  above), `blog-anthropic-human-agent-teams.md` under its "a teammate" anchor
  text (already in the corpus, cited above), and several docs/support pages
  (Claude Tag definition, BAA definition, security-and-data-handling docs,
  healthcare best-practices docs, the launch-promo credit terms) that were not
  fetched — none of the extracted claims depend on their content, only on what
  this post states directly.
- **Byline**: three authors are credited (Camy Pearson, Maria Howe, Araba
  Koomson) with no individual attribution of which sections each wrote; the
  post is treated as a single first-party Anthropic voice throughout.
- **No contradiction found or filed**: see Cross-References → Contradicts. This
  post's disclosed BAA gap for Claude Tag is a different product/scope than the
  BAA-covered Claude API mentioned for Zeus in the same post — the two are
  consistent, not conflicting, statements about two different products.
- **Confidence rated `emerging` overall**: the compliance-mechanism claims
  (Claims 1-4) and the pipeline/workflow mechanics (Claims 7, 8, 10, 12, 14) are
  settled first-party descriptions of shipped product behavior and named
  companies' described practices; the quantitative and outcome claims (Claim 6's
  97% figure, the 15+ tickets in Claim 11, the implicit success of Medallion's
  and Tennr's setups) are single-company, vendor-published, self-reported
  figures with no independent audit or disclosed methodology, and the named
  executives' risk/trust rationales (Claims 9, 13, 15) are single-informant
  characterizations rather than measured outcomes. This mirrors the `emerging`
  rating already assigned to the two prior Claude Tag practitioner-evidence
  notes in this corpus.
