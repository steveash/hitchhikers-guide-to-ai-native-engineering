---
source_url: https://news.ycombinator.com/item?id=46966879
source_type: failure-report
platform: hn
title: "Cursor switches pay-per-token when your plan limit end. Calls 'On-Demand usage'"
author: hardwellvibe
date_published: 2026-02-10
date_extracted: 2026-04-15
last_checked: 2026-04-15
status: current
confidence_overall: anecdotal
issue: "#58"
---

# Failure Report: Cursor Pro Silently Switches to Per-Token Billing After Plan Limit — $42.12 in Unexpected Charges

> A Cursor Pro subscriber hit their monthly usage limit on January 14 with no
> warning, was silently enrolled in "On-Demand" post-paid per-token billing
> without explicit consent, ran up $42.12 in unexpected charges using
> claude-4.5-opus-high-thinking at $0.50–$4.00+ per request, and was then
> given a misleading support explanation — surfacing four distinct UI and
> support transparency failures in Cursor's billing design.

## Source Context

- **Platform**: Hacker News self-post, 11 points, 6 comments, 2026-02-10
- **Author credibility**: hardwellvibe is an HN account with a first-person
  account of a specific billing incident with concrete dollar figures, dates,
  model names, and a reconstructed support exchange. The level of specificity
  ($42.12 on-demand charge, $20 subscription, Jan 14 trigger date, Feb 7
  support call) is consistent with someone reviewing their actual billing
  dashboard. The author frames this as a UX/transparency failure rather than
  accusing Cursor of fraud, which suggests familiarity with how billing
  systems work and adds credibility. No HN commenters disputed the billing
  facts; responses focused on alternatives rather than challenging the account.
- **Community response**: 11 points, 6 comments. theflyestpilot corroborates
  the cost magnitude problem from a different angle ($1,500 in one month during
  a crunch; Opus 4.5-4.6 at ~$250/day), though via known usage rather than a
  surprise. theorchid provides a workaround (Claude Max subscription proxied
  through Cursor). No one disputed the silent billing-mode switch described
  in the original post. Thread is small but all-corroborating on the core
  cost transparency problem.

## What Was Attempted

- **Goal**: Continue using Cursor Pro as usual — a paid monthly subscription
  the author had been relying on without incident.
- **Tool/approach**: Cursor Pro subscription. The author was using
  claude-4.5-opus-high-thinking within Cursor, a model tier that costs
  $0.50–$4.00+ per request at post-paid per-token rates.
- **Setup**: Individual developer on a standard Cursor Pro subscription
  (the mid-tier paid plan, below Ultra). No indication of unusual or
  agent-heavy workflows — the author characterizes this as normal use that
  happened to exhaust the monthly quota.

## What Went Wrong

- **Symptoms**:
  1. On January 14, the author hit their Cursor Pro monthly usage limit
     with no advance warning and no prompt at the time of limit hit.
  2. Cursor silently switched the account to "On-Demand" billing mode.
     No explicit opt-in. No notification. Billing mode changed without
     user awareness.
  3. The author continued using Cursor in what they believed was their
     subscription plan, accumulating $42.12 in per-token on-demand charges
     over 2.5 weeks (January 14 to approximately February 7).
  4. Within the first 4 days of the silent switch, the author had already
     spent $20 in on-demand charges — also without realizing it.
  5. When a $20 "Add API credit" prompt appeared, the author interpreted it
     as adding prepaid credit (standard for pay-as-you-go services) and
     paid it twice — only to discover it was raising the spending cap on
     retroactive charges already accumulated, not adding a balance.
  6. The February 7 support call yielded an explanation that mischaracterized
     the $42.12 bill as "17 calls to gpt-5.1-codex-max totalling $0.29 with
     a $20 minimum charge applied" — a description that does not add up to
     the actual invoice total and appears to describe a subset of the charges.

- **Severity**: Significant unexpected financial harm. $42.12 in on-demand
  charges above the $20 subscription fee, with the "Add API credit" UI
  leading the author to pay $20 twice before understanding the charge
  structure. Not catastrophic (cf. the Ultra billing explosion in
  `failure-cursor-ultra-billing-cache-explosion.md` at $1,600 projected/month),
  but the mechanism — silent enrollment in post-paid billing — represents
  a larger risk for users who use expensive models heavily.

- **Reproducibility**: Structural. Any Cursor Pro user who hits their monthly
  plan limit is exposed to this exact failure mode if Cursor's billing design
  has not changed. theflyestpilot's comment ($1,500 in one month) suggests
  the per-token cost for high-reasoning models is large enough to produce
  catastrophic bills for heavier users who experience the same silent switch.

## Root Cause (if identified)

- **Author's diagnosis (failure 1 — silent mode switch)**: When the Pro plan
  limit is hit, Cursor's system automatically enrolls the account in "On-Demand"
  per-token billing with no explicit consent, no notification at limit-hit time,
  and no hard stop. Quote (reconstructed from post): "No warning. No 'Hey,
  you've used up your included quota — want to keep going at per-token rates?'
  Cursor just... kept going."

- **Author's diagnosis (failure 2 — terminology)**: "On-Demand usage" is
  standard English for "available whenever I need it" — i.e., included service
  on demand. In Cursor's system it means post-paid per-token charges. The
  author explicitly notes: "'On-Demand usage' in literally every other context
  means included service, not post-paid charges." The term carries the opposite
  semantic payload of what users will assume.

- **Author's diagnosis (failure 3 — UI deception)**: The "Add API credit"
  button, which appears after on-demand charges accumulate, looks and behaves
  like a prepaid top-up in the UI. It is not — it raises the billing cap on
  retroactive charges. The author paid $20 twice before understanding this
  distinction. "Who interprets that as post-paid charges?"

- **Author's diagnosis (failure 4 — support failure)**: The support explanation
  (17 calls at $0.29 = $20 minimum) does not reconcile with the $42.12
  invoice the author received. Either the support agent described a subset of
  charges, did not understand the billing structure, or provided a deliberately
  simplified explanation. The author characterizes this as support that
  "misrepresented the bill structure."

- **Our assessment**: All four diagnoses are credible and the mechanism is
  straightforward: Cursor's billing design optimizes for continued service
  delivery (which requires no interruption) over user cost transparency
  (which requires a hard stop or explicit consent gate). The "On-Demand"
  terminology is a genuine semantic mismatch — the term is industry-standard
  for included on-demand access (see AWS, Azure, SaaS in general). The
  "Add API credit" UI mismatch between affordance (looks like top-up) and
  function (raises retroactive cap) is a classic dark pattern, whether
  intentional or not. The support failure is the most damaging element:
  a user investigating unexpected charges who gets an inaccurate
  reconciliation from support has no path to understanding their bill.
  This is NOT the same failure mode as the Cursor Ultra cache explosion
  (Issue #75, `failure-cursor-ultra-billing-cache-explosion.md`): that
  failure is about billing magnitude within a plan via prompt-cache replay;
  this failure is about unauthorized enrollment in a different billing mode
  entirely. Mechanism, trigger, and prevention are all distinct.

- **Category**: product-transparency-failure / UX-dark-pattern. Not a bug
  in the technical sense — the system presumably worked as Cursor designed it.
  The failure is in the consent model, terminology, and UI affordance design.

## Recovery Path

- **What they switched to**: Not explicitly stated. The author's focus is on
  documenting and seeking remedy, not on a specific replacement. Community
  commenters suggest: Claude Max subscription ($100/month) proxied through
  Cursor (theorchid), Antigravity as a Cursor alternative (gorgmah), or
  direct Claude Code access (drakenot/theflyestpilot).

- **Workaround**: None identified for the billing charges already incurred.
  Forward mitigation: monitor billing dashboard explicitly (not product UI),
  set billing alerts, and assume any AI tool subscription may silently switch
  billing modes at limit.

- **Author's recommended fixes**:
  1. Hard-stop at the plan limit with an explicit consent prompt: "You've
     used your included quota. Do you want to continue at per-token rates?"
  2. Rename "On-Demand usage" to "Overage charges" or "Pay-per-use billing"
     to accurately describe the charge type.
  3. Make "Add API credit" actually add a prepaid balance rather than raise
     a retroactive spending cap.
  4. Train support to accurately explain the billing line items.

- **Unresolved**: Cursor's billing design has not been publicly changed as of
  the extraction date. The structural risk (any Pro user who hits their limit
  faces silent enrollment in on-demand billing) remains unaddressed.

## Extracted Lessons

### Lesson 1: AI coding tool subscriptions may silently enroll users in post-paid per-token billing when plan limits are hit

- **Evidence**: hardwellvibe's first-person account of hitting the Pro limit
  on January 14 and accumulating $42.12 in on-demand charges over 2.5 weeks
  without awareness. The trigger is hitting the plan limit; the mechanism is
  automatic billing-mode enrollment without explicit consent.
- **Confidence**: anecdotal (single documented case; the mechanism is
  plausible and no commenter disputed it)
- **Actionable as**: For any AI tool subscription with a monthly usage quota,
  identify in advance what happens when the quota is hit. Options to look for:
  (a) hard stop with opt-in to continue at overage rates, (b) automatic
  enrollment in overage billing, or (c) service suspension. Option (b) is the
  dangerous one. Ask the vendor before hitting the limit, not after.

### Lesson 2: Subscription billing terminology ("On-Demand," "Add API credit") can carry the opposite semantic payload of user expectation

- **Evidence**: hardwellvibe's explicit analysis: "'On-Demand usage' in
  literally every other context means included service, not post-paid charges."
  The "Add API credit" prompt looks like a top-up but raises a retroactive cap.
- **Confidence**: anecdotal (but the semantic mismatch is verifiable
  independent of this specific case — "on-demand" is standard industry
  terminology for included service)
- **Actionable as**: When evaluating AI tool subscriptions, read the billing
  FAQ for every terminology term. Do not assume industry-standard terms
  carry their industry-standard meanings. "On-Demand," "credit," "balance,"
  and "usage" are all terms AI vendors sometimes redefine in ways that shift
  cost risk to the user.

### Lesson 3: High-reasoning model costs ($0.50–$4.00+ per request) compound dangerously when the user doesn't know they're in per-token billing mode

- **Evidence**: hardwellvibe spent $42.12 in 2.5 weeks using
  claude-4.5-opus-high-thinking at $0.50–$4.00+ per request. theflyestpilot
  corroborates the magnitude: $1,500 in one month, Opus 4.5-4.6 at ~$250/day,
  individual requests up to $45.74 per call.
- **Confidence**: anecdotal (two independent disclosures confirm the cost
  magnitude for high-reasoning model tiers)
- **Actionable as**: When using high-reasoning model tiers (Opus-class,
  "high-thinking" variants), treat each request as potentially $1–$50, not
  fractions of a cent. If you're in a per-token billing mode — even
  accidentally — a single coding session can incur tens of dollars. Avoid
  using high-reasoning models in any subscription context where you're
  uncertain about your billing mode.

### Lesson 4: Billing UIs that look like top-up prompts may instead be raising retroactive spending caps

- **Evidence**: hardwellvibe paid $20 via "Add API credit" twice before
  discovering it was raising the cap on accumulated charges, not adding a
  prepaid balance. The affordance (credit = prepay) did not match the
  function (cap raise = authorize retroactive spend).
- **Confidence**: anecdotal
- **Actionable as**: Before interacting with any billing UI element in an
  AI tool (especially a "top-up," "add credit," or "add balance" prompt),
  verify from the vendor's documentation what the action actually does.
  Retroactive spending cap raises are fundamentally different from prepaid
  top-ups, but they may look identical in the UI.

### Lesson 5: Support explanations of billing may not accurately reconcile with the actual invoice

- **Evidence**: Cursor support explained the $42.12 charge as "17 calls to
  gpt-5.1-codex-max totalling $0.29 with a $20 minimum charge applied" —
  a description that does not arithmetically produce $42.12. hardwellvibe
  explicitly flags this as misrepresentation.
- **Confidence**: anecdotal (only hardwellvibe's account of the support
  exchange; no corroborating source)
- **Actionable as**: For any unexpected billing charge on an AI tool,
  export the billing CSV and line-item detail yourself rather than relying
  on support's verbal explanation. Support explanations of complex billing
  structures may be simplified, incorrect, or incomplete. Cross-check
  every line item independently.

### Lesson 6: Cost monitoring practices must account for billing mode, not just billing amount

- **Evidence**: hardwellvibe's experience shows that monitoring "how much
  I'm spending" is insufficient if you don't know the billing mode you're
  in. The charges accumulated without any in-product signal that the billing
  mode had changed. The same usage behavior generates radically different
  costs under subscription vs. per-token billing.
- **Confidence**: anecdotal
- **Actionable as**: Establish a practice of periodically checking not just
  billing totals but the billing mode the account is in. For AI tool
  subscriptions with plan limits, add a calendar reminder to check billing
  mode around the limit reset date. Do not assume your subscription mode
  is stable.

## Concrete Artifacts

### The core billing event timeline (from hardwellvibe's post)

```
Jan 14:  Hit Cursor Pro monthly usage limit — no warning, no prompt
Jan 14:  Cursor silently enrolls in "On-Demand" per-token billing
Jan 14+: Using claude-4.5-opus-high-thinking at $0.50–$4.00+ per request
Jan 18:  (approx) First 4 days accumulated ~$20 in on-demand charges
Jan 18:  "Add API credit" prompt appears — user interprets as prepaid top-up
Jan 18:  Pays $20 — actually raises spending cap on retroactive charges
Jan 18+: Continues using Cursor, continues accumulating per-token charges
Feb 7:   Support call — support explanation: "17 calls to gpt-5.1-codex-max
          totalling $0.29 with $20 minimum charge applied"
Feb 7:   Actual invoice: $42.12 in On-Demand charges + $20 subscription
Feb 7:   User discovers "Add API credit" was not a prepaid top-up
         Pays $20 again before understanding the structure
```

### The terminology failure (hardwellvibe's verbatim framing)

> "On-Demand usage" — who interprets that as post-paid charges?

> "No warning. No 'Hey, you've used up your included quota — want to keep
> going at per-token rates?' Cursor just... kept going."

### theflyestpilot's corroborating cost data (comment, 2026-02-11)

```
Monthly spend:        $1,500 (crunch-time month)
Model:                Opus 4.5-4.6
Cost per day:         ~$250
Per-request range:    $0.05 to $45.74 per call
```

Note: theflyestpilot's usage was known and intentional — this is not a
surprise billing case. But the per-request figures corroborate the cost
magnitude hardwellvibe encountered without knowing they were in per-token mode.

### theorchid's subscription arbitrage workaround (comment, 2026-02-11)

```
Cursor Ultra:         $200/month → ~$500 API value
Claude Max:           $100/month → ~$2,000 API value (via subscription)
Workaround:           Proxy Cursor requests through Claude Max subscription
                      using a script — Cursor gets local model; billing
                      hits Claude Max subscription, not Cursor On-Demand
```

This is a practitioner workaround, not an endorsement.

## Cross-References

- **Corroborates** `failure-cursor-ultra-billing-cache-explosion.md`: Both
  are Cursor billing opacity failures with concrete dollar figures and similar
  UX transparency failures. The mechanisms are entirely different — that note
  covers billing magnitude explosion from prompt-cache replay depth within an
  Ultra plan; this note covers silent billing-mode switch after a Pro plan
  limit. Both have the same root: Cursor's billing model is not transparently
  communicated in the product UI. Together these two reports form a
  complementary pair of Cursor billing failure modes. The Ultra note
  explicitly pre-identifies Issue #58 (this source) as the complementary
  case; this note confirms that pairing.

- **Corroborates** `blog-bswen-mcp-token-cost.md` on token cost opacity:
  Bswen documents 100k tokens consumed before the user types anything, with
  the mechanism being vendor-controlled MCP tool overhead. hardwellvibe
  documents $42.12 in charges accumulated without user awareness, with the
  mechanism being vendor-controlled billing-mode switching. The shared pattern:
  AI tool vendors make decisions (about token accumulation, about billing mode)
  that have material cost consequences but are not surfaced in the product UI.
  Users build mental models from what the UI shows them; the bill is determined
  by what the UI does not show.

- **Corroborates** `failure-hooks-enforcement-2k.md` on practitioner cost
  disclosures: That note documents a $2K/year solo developer on Claude Code.
  theflyestpilot in this thread documents $1,500 in a single month on Cursor.
  Together with hardwellvibe's $42.12 surprise charge, these establish that
  AI coding tool costs range from the anecdotally manageable to the
  catastrophic, and that the difference is often a billing transparency gap
  rather than a usage difference.

- **Novel**: The specific failure mode of silent billing-mode switch upon
  hitting a subscription plan limit is new to our corpus. The Ultra billing
  explosion (existing note) is about magnitude within a plan; this is about
  unauthorized enrollment in a different plan tier. The four distinct failure
  vectors documented here (silent enrollment, terminology mismatch, UI
  affordance deception, support misrepresentation) as a compound failure chain
  is the most complete account of this failure pattern in our corpus.

## Guide Impact

- **Chapter 01 (Daily workflows — tool setup and cost monitoring)**: Add a
  specific workflow item: check your AI tool subscription's billing mode
  explicitly, not just the billing total. Recommend identifying in advance
  what happens when the plan limit is hit (hard stop vs. silent overage
  enrollment). Set a calendar reminder to verify billing mode around the
  monthly limit reset date. Do not assume subscription mode is stable.

- **Chapter 01 (Daily workflows — billing practices)**: Add the billing CSV
  export recommendation as a hard requirement, not optional. The product UI
  for AI tools is demonstrably insufficient as a billing signal: hardwellvibe's
  Cursor UI did not signal the billing-mode switch; throwawayround's Cursor UI
  did not surface the prompt-cache depth. Both failures required CSV export
  to diagnose. For any AI tool subscription, treat the billing dashboard CSV
  as the source of truth.

- **Chapter 05 (Team adoption — tool evaluation)**: When evaluating an AI
  coding tool for team adoption, explicitly test the overage/limit behavior:
  What happens when the plan limit is hit? Is the behavior documented? Is it
  tested? Add billing terminology to the evaluation rubric: do "On-Demand,"
  "credit," and "balance" mean what you think they mean in this vendor's
  billing system? Run a billing pilot (per the Ultra billing note's Ch05
  recommendation) under real workloads and intentionally approach the plan
  limit to observe the limit-hit behavior before committing to wider rollout.

- **Chapter 05 (Team adoption — AI tool cost governance)**: Add guidance on
  per-request cost awareness for high-reasoning model tiers. At $0.50–$4.00+
  per request for Opus-class / high-thinking models, team-scale usage without
  billing mode awareness can generate thousands of dollars in unexpected charges.
  Teams should know which model tier their tooling defaults to and what the
  per-request cost is at that tier.

## Extraction Notes

- The HN thread is small (11 points, 6 comments) but substantive. The original
  post contains concrete dates, dollar amounts, model names, and a reconstructed
  support exchange — the kind of specificity that indicates actual billing
  investigation rather than venting. No commenter disputed the facts; responses
  focused on workarounds and alternatives.
- WebFetch returned synthesized summaries rather than verbatim text for both
  the HN page and the Algolia API. The core claims (Jan 14 trigger, $42.12
  on-demand, $0.50–$4.00+ per request for claude-4.5-opus-high-thinking, $20
  paid twice, support misrepresentation) are consistent across both fetch paths
  and are treated as reliable for extraction purposes. Direct quotes are
  marked as reconstructed where they are not character-for-character confirmed.
- The model name "gpt-5.1-codex-max" appears in the support explanation of the
  Feb 7 bill (attributed to support, not hardwellvibe). This is a curious
  detail — either Cursor's support system uses model names differently than
  the product UI, or the support agent was describing a different model from
  the one hardwellvibe was using. This detail is not fully explained by the
  thread and is noted here for the Assayer's awareness. It does not
  materially change the billing failure narrative but is flagged as an
  unresolved inconsistency.
- The failure is Cursor-specific but the pattern (silent enrollment in
  post-paid billing upon hitting a plan limit) could apply to any AI coding
  tool with subscription plans that have usage limits. Teams evaluating
  other tools should ask explicitly about limit-hit behavior regardless of
  vendor.
- This note completes the pairing with `failure-cursor-ultra-billing-cache-explosion.md`.
  The Ultra note pre-identified Issue #58 as the complementary case; this note
  fills that gap. No contradiction issue is warranted — the two notes describe
  distinct failure modes, not conflicting claims about the same phenomenon.
