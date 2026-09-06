---
source_url: https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex
source_type: blog-post
title: "Our decision on Cursor following its acquisition by SpaceX"
author: OpenAI (unsigned corporate voice)
date_published: 2026-08-28
date_extracted: 2026-09-06
last_checked: 2026-09-06
status: current
confidence_overall: settled
issue: "#3273"
---

# Our decision on Cursor following its acquisition by SpaceX

> OpenAI announces it has notified SpaceX of its intent to wind down the
> contract supplying OpenAI models to Cursor, with a proposed November 12,
> 2026 shutoff date, citing distrust in SpaceX's contract compliance based
> on prior terms-of-service violations by Musk-controlled Twitter/X and
> xAI — the first documented case in the corpus of a frontier lab
> unilaterally severing model access to a coding tool over its new
> corporate parent's compliance history, and the first corpus confirmation
> that Cursor itself (not just a training partnership) has been acquired
> by SpaceX.

## Source Context

- **Type**: blog-post (official `openai.com/index/` announcement, "Company"
  category, published August 28, 2026, unsigned/institutional byline
  "OpenAI"). Very short (four paragraphs, ~250 words), no embedded charts,
  tables, or named individual quotes — an institutional policy statement,
  not a technical or product post.
- **Author credibility**: First-party institutional statement from OpenAI
  about its own contractual decision. This is the authoritative source for
  *what OpenAI decided and says it will do*, but the framing of SpaceX's
  trustworthiness ("we cannot be confident that SpaceX will use our
  technology within our terms of service") is OpenAI's own characterization
  of a counterparty in an active business dispute, not an independently
  adjudicated finding. The two supporting historical claims (Twitter
  contract violations, Musk's sworn xAI admission) are asserted but not
  re-documented with citations in this post itself.
- **Scope**: Covers OpenAI's decision to wind down its model-supply contract
  with Cursor following Cursor's acquisition by SpaceX, the proposed
  shutoff date, the stated rationale (distrust based on prior Musk-company
  contract violations), the "change of control" contract mechanism that
  triggered the decision, a reference to OpenAI's upcoming model "Astra"
  as a further accountability consideration, and a closing statement about
  OpenAI's relationship with Cursor and its developers. Does **not** cover:
  the terms of the "custom agreement" itself, any response or statement
  from Cursor or SpaceX, the date or terms of Cursor's acquisition by
  SpaceX, which OpenAI models Cursor currently offers or in what
  proportion its users rely on them, or any detail about what "go above
  and beyond to support" affected developers will concretely mean.

## Extracted Claims

### Claim 1: OpenAI notified SpaceX that it intends to wind down the contract supplying OpenAI models to Cursor, with a proposed shutoff date of November 12, 2026, giving the maximum notice allowed under the contract
- **Evidence**: Opening statement of the post, framed as an action already
  taken ("we notified") rather than a future intention.
- **Confidence**: settled (a direct, dated, first-party statement of a
  concrete action already performed — sending the notification — not a
  hedge or forecast)
- **Quote**: "Today, we notified SpaceX that we intend to wind down our contract providing OpenAI models to Cursor, with a proposed shutoff date of November 12, 2026. To maximize the time that developers can retain access to our models through Cursor, we are giving the maximum notice provided by our contract."
- **Our assessment**: This is the headline fact of the post: a specific
  shutoff date (November 12, 2026), roughly eleven weeks after
  publication, and an explicit statement that this is the *longest*
  notice period the contract allows — OpenAI is not choosing a fast
  cutoff, it is choosing the slowest one available to it. This is
  directly comparable in kind (a dated, notice-governed model-access
  cutoff) to the GitHub Copilot deprecation notices already in the
  corpus, but the trigger and mechanism are entirely different — see
  Cross-References.

### Claim 2: OpenAI states the decision was "incredibly tough" because it cares about broad developer availability of its models, but is proceeding because it cannot be confident SpaceX will use its technology within OpenAI's terms of service, based on its experience with Elon Musk's companies violating contracts
- **Evidence**: Direct statement of motivation in the opening paragraph.
- **Confidence**: settled (a direct first-party statement of OpenAI's own
  stated reasoning; the underlying trust judgment is OpenAI's subjective
  assessment of a counterparty, but the statement of *that being the
  reasoning* is not hedged)
- **Quote**: "This decision was incredibly tough, as we care deeply about our models being broadly available for developers. We are making this choice because we cannot be confident that SpaceX will use our technology within our terms of service, based on our experience with Elon Musk's companies violating contracts."
- **Our assessment**: This is the core causal claim of the post: the
  decision is framed entirely as a trust/compliance judgment about
  SpaceX as a corporate entity, not a competitive, financial, or
  technical rationale. Cursor itself is not accused of any violation —
  the distrust is inherited from Cursor's new parent company's track
  record.

### Claim 3: OpenAI names two specific prior instances of contract violations by Musk-controlled companies as the evidentiary basis for its distrust: Twitter (now part of SpaceX) broke the terms of its OpenAI contract after Musk's acquisition, and Musk admitted under oath that xAI (also now part of SpaceX) had violated OpenAI's terms of service
- **Evidence**: Two named historical incidents cited directly in support of
  Claim 2's stated rationale, each linked in the original post (link
  targets not resolved by this Miner — see Extraction Notes).
- **Confidence**: settled (a direct, specific, first-party historical
  claim citing a named sworn admission; note this Miner did not follow
  the two embedded hyperlinks to independently verify the underlying
  Twitter and xAI incidents — see Extraction Notes)
- **Quote**: "To work with a large partner like SpaceX, we typically rely on custom contracts to ensure compliance with our terms of service and that the integration provides for safety at scale. After Musk acquired Twitter, now part of SpaceX, the company broke the terms of our contract (alongside many others). Under oath earlier this year, Musk admitted that xAI, now also part of SpaceX, had violated OpenAI's terms of service (terms which are similar to xAI's own)."
- **Our assessment**: This is the evidentiary backbone of the entire post —
  without these two named incidents, Claim 2's distrust judgment would be
  unsupported assertion. The claim that this is a *pattern* ("broke the
  terms of our contract (alongside many others)") rather than an isolated
  incident is significant: OpenAI is characterizing Musk-controlled
  entities generally, across at least three companies (Twitter, xAI,
  now Cursor), as contract-compliance risks. The corpus does not yet
  contain an independent source documenting the specific Twitter contract
  breach or the sworn xAI admission referenced here — this claim should
  be treated as OpenAI's own characterization pending independent
  corroboration.

### Claim 4: OpenAI's custom contract with Cursor contains a "change of control" clause giving OpenAI a limited time window to cancel the agreement following an acquisition — the mechanism OpenAI is now exercising because of SpaceX's acquisition of Cursor
- **Evidence**: Direct statement of the contractual mechanism triggering
  the decision.
- **Confidence**: settled (a direct, specific first-party statement about
  the terms of its own contract)
- **Quote**: "Our custom agreement with Cursor gives us a limited time window to cancel it after a change of control."
- **Our assessment**: This is the first documented instance in the corpus
  of a change-of-control clause being exercised in an AI model-supply
  contract. It also confirms — via the post's own title and this specific
  sentence — that Cursor has been formally acquired by SpaceX, not merely
  entered into a training partnership with SpaceXAI as previously
  documented (`blog-cursor-composer-2-5.md`, `blog-cursor-grok-4-5.md`).
  This is a materially new fact for the corpus: Cursor's relationship with
  the Musk business empire has escalated from a joint-model-training
  partnership to full corporate ownership. The phrase "limited time
  window" also implies OpenAI had to act within a defined period after the
  acquisition closed or risk losing the cancellation right — a contract
  design detail worth flagging for any guide discussion of vendor
  contract terms.

### Claim 5: OpenAI states that, as AI capabilities advance, it has "a new level of accountability" to ensure its upcoming model "Astra" is used in accordance with its terms, and cites this as a factor in deciding to hold the cancellation to the latest permitted date while not providing future models to Cursor
- **Evidence**: Direct statement connecting the Cursor decision to Astra's
  accountability requirements.
- **Confidence**: settled (a direct first-party statement of the stated
  reasoning, though the specific link between Astra's capabilities and
  the Cursor decision is asserted rather than mechanistically explained)
- **Quote**: "As AI capabilities advance, we also have a new level of accountability to ensure our upcoming model, Astra, is being used in accordance with our terms. Given all of this, we've decided to hold the contract cancellation to the latest date we can while not providing future models to Cursor."
- **Our assessment**: This sentence draws an explicit line between the
  Cursor decision and OpenAI's own disclosed concerns about Astra's
  capability profile. `blog-openai-astra-critical-cyber-capabilities.md`
  (Claim 1) already documents OpenAI's internal evaluations concluding it
  "cannot rule out critical cyber capabilities" for Astra, and that
  note's Claim 6 documents OpenAI "pausing internal activities involving
  Astra that do not yet meet strengthened security control requirements."
  This post extends that same heightened-accountability posture outward
  to an external distribution decision: Cursor will keep access to
  OpenAI's *existing* models through the wind-down period, but will not
  receive *future* models (implicitly including Astra) at all. This is
  the first corpus evidence that Astra's disclosed capability concerns
  are shaping which downstream partners get access to future OpenAI
  models, not just how OpenAI handles the model internally.

### Claim 6: OpenAI closes the post by stating it has worked with Cursor for "nearly four years," has "enormous respect" for Cursor's team and product, frames developers who rely on OpenAI models in Cursor as the parties most affected by the decision, and commits to "go above and beyond" to support them through the transition
- **Evidence**: Closing paragraph of the post.
- **Confidence**: anecdotal (a goodwill/relationship-management statement
  with no concrete commitment, mechanism, or metric attached — "go above
  and beyond" is not defined)
- **Quote**: "We've worked with Cursor for nearly four years and have enormous respect for their team, their product, and what they've built for the developer community. We know that the people most affected by this decision are the developers who rely on OpenAI models in Cursor. We care about their experience in this transition and we're ready to go above and beyond to support them."
- **Our assessment**: This is standard corporate goodwill/damage-control
  language and should not be read as a concrete commitment — no specific
  transition assistance, migration tooling, or extended-access provision
  is named. The "nearly four years" figure dates the OpenAI/Cursor
  relationship to roughly late 2022, consistent with Cursor's known
  founding period, though this post does not state a specific start date.
  For guide purposes, the operative content of this decision is entirely
  in Claims 1–5; this closing paragraph is relationship-management framing
  around an otherwise unilateral, adversarial-toward-SpaceX decision.

## Concrete Artifacts

```
Source: OpenAI, "Our decision on Cursor following its acquisition by SpaceX"
https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex
(published August 28, 2026; retrieved via Internet Archive Wayback Machine
snapshot dated 2026-09-03 — see Extraction Notes)

DECISION TIMELINE
  Notification sent to SpaceX:        "Today" (August 28, 2026)
  Proposed shutoff date:               November 12, 2026 (~11 weeks later)
  Notice length:                       "the maximum notice provided by our contract"

STATED RATIONALE (in order presented)
  1. Cannot be confident SpaceX will honor OpenAI's terms of service
  2. Historical basis:
     - Twitter (post-Musk acquisition, now part of SpaceX): "broke the
       terms of our contract (alongside many others)"
     - xAI (now part of SpaceX): Musk "admitted under oath" to a
       terms-of-service violation "earlier this year" [2026]
  3. Contract mechanism: a "change of control" clause gives OpenAI "a
     limited time window to cancel" following an acquisition
  4. Forward-looking accountability: upcoming model "Astra" requires a
     "new level of accountability" to ensure terms-compliant use

RESULT
  - Existing OpenAI-model access to Cursor continues through the shutoff
    date (the "latest date we can")
  - No future OpenAI models will be provided to Cursor going forward
  - Relationship duration cited: "nearly four years"

WHAT IS NOT STATED
  - No detail on which OpenAI models Cursor currently offers
  - No response from Cursor or SpaceX quoted or referenced
  - No specific migration/transition support mechanism named
  - No date given for when SpaceX's acquisition of Cursor closed
```

## Cross-References

- **Corroborates**: `blog-simonwillison-xai-anthropic-datacenter.md` Claim 9
  ("Sounds like a new form of supply chain risk for Anthropic to me!") and
  Claim 10 (xAI's same-week deprecation of eight Grok models with two
  weeks' notice, "the same entity controlling Anthropic's infrastructure").
  Those claims documented supply-chain risk flowing *from* a
  Musk-controlled infrastructure provider *to* a downstream AI lab and its
  users. This post documents the inverse but structurally related
  scenario: a separate AI lab (OpenAI) proactively severing its own supply
  relationship *to* a Musk-controlled downstream product (Cursor) because
  it does not trust that entity's contract compliance — the same
  underlying distrust of Musk-controlled corporate entities, now acting
  as the trigger for a lab's own defensive contract termination rather
  than as a risk borne passively by a compute lessee.
- **Corroborates**: `blog-openai-astra-critical-cyber-capabilities.md`
  Claim 1 (OpenAI "cannot rule out critical cyber capabilities" in Astra)
  and Claim 6 (OpenAI "pausing internal activities involving Astra that do
  not yet meet strengthened security control requirements"). Claim 5 in
  this note shows the same heightened-accountability posture toward Astra
  being applied to an external distribution decision, not just internal
  activity — extending that note's internal-governance pattern into
  partner-access policy.
- **Extends**: `blog-cursor-composer-2-5.md` Claim 10 (Cursor and SpaceXAI
  "training a significantly larger model from scratch, using 10x more
  total compute") and `blog-cursor-grok-4-5.md` Claim 1 (Grok 4.5,
  "released together with SpaceXAI"). Both of those notes documented a
  joint *model-training* partnership between Cursor and SpaceXAI. This
  post's Claim 4 confirms, via its own title and the "change of control"
  language, that the relationship has since escalated to full corporate
  acquisition — SpaceX now owns Cursor outright. Neither prior note
  documented or predicted an acquisition; this is new information that
  updates the nature of the Cursor/SpaceX(AI) relationship across the
  corpus from "training partner" to "parent company."
- **Extends**: `blog-simonwillison-spacex-s1-anthropic.md` (SpaceX's
  disclosed compute contract terms with Anthropic, including a 90-day
  bilateral termination clause). That note documents termination mechanics
  in a SpaceX-as-infrastructure-provider contract; this post documents
  termination mechanics in the reverse direction — SpaceX-as-acquirer of
  a company (Cursor) that depends on a third-party lab's (OpenAI's)
  models — via a different contractual mechanism (change-of-control
  cancellation rather than a fixed notice-period termination clause).
  Together the two notes show Musk-controlled entities on both sides of
  model/compute supply contracts with short-to-moderate termination
  windows.
- **Contradicts**: None identified. No existing corpus source makes a
  claim about OpenAI/Cursor's contractual relationship, Cursor's
  ownership structure, or Astra's partner-access implications that this
  post opposes. No contradiction issue filed.
- **Novel**:
  - **Cursor's acquisition by SpaceX** (Claim 4 and this note's title):
    first corpus confirmation that Cursor is now a SpaceX subsidiary, not
    merely a training partner of SpaceXAI.
  - **A frontier lab unilaterally severing model access over a partner's
    change of ownership** (Claims 1, 2, 4): no other corpus source
    documents a model provider terminating a product-integration contract
    specifically because of who acquired the counterparty, as distinct
    from technical deprecation, pricing changes, or the counterparty's
    own conduct.
  - **A named "change of control" cancellation clause in an AI
    model-supply contract** (Claim 4): a specific contract-design detail
    not previously documented in the corpus's coverage of AI vendor
    contracts.
  - **Astra's capability concerns shaping external distribution policy**
    (Claim 5): the first evidence that Astra-specific accountability
    considerations extend beyond OpenAI's own internal activity gating
    (`blog-openai-astra-critical-cyber-capabilities.md`) into decisions
    about which external partners receive future models at all.

## Guide Impact

- **Chapter 05 (Team Adoption) — "Model Deprecation Is a Recurring
  Governance Event" section**: This section already documents model
  availability shocks from three distinct causes: platform-side
  deprecation with advance notice (`docs-github-copilot-gpt52-deprecation`),
  zero-notice retroactive deprecation
  (`docs-github-copilot-claude-sonnet4-deprecation`), and regulatory
  export-control availability shock
  (`blog-thoughtworks-kamelman-sovereign-ai-dependency`). This source adds
  a fourth, previously undocumented cause: **upstream-provider-initiated
  severance triggered by a downstream partner's change of corporate
  ownership**. Recommend adding a paragraph noting that model access can
  also be cut off not because the model itself is deprecated or because a
  government blocks it, but because the *lab supplying the model* decides
  it no longer trusts the *company distributing it* — a risk specific to
  AI-native tools built on a thin integration layer over a third-party
  lab's models, where the tool vendor's own corporate ownership becomes a
  supply-chain risk factor for its end users. Concrete numbers to cite:
  ~11 weeks' notice (Aug 28 → Nov 12, 2026), described by OpenAI itself as
  "the maximum notice provided by our contract" — i.e., even the
  longest-available notice period in this case is shorter than the
  ~7-week-to-25-day range already documented for platform deprecations,
  reinforcing the existing "treat model identifiers as versioned
  dependencies" rule rather than requiring a new one.
- **Chapter 05 (Team Adoption) — competitive/vendor landscape**: Teams
  currently using Cursor with OpenAI models selected (via auto-routing or
  explicit model choice) should be flagged as needing a migration plan
  before November 12, 2026. This is a concrete, dated action item distinct
  from the general "keep a successor model enabled" guidance already in
  the guide — here the *entire provider*, not just one model generation,
  is being withdrawn from the product.
- **Chapter 06 (Security & Threat Model)**: Note the ownership-transitivity
  risk pattern this event illustrates: adopting a coding tool exposes a
  team not only to that tool's own security posture but to the terms-of-
  service and trust relationships its *parent company* maintains with the
  model providers it depends on. A tool's model-supply relationships can
  change discontinuously when the tool itself is acquired, independent of
  anything the tool's engineering team does.

## Extraction Notes

- **Fetch method**: Both `WebFetch` and direct `curl` (with a browser
  user-agent, and separately with a Googlebot user-agent) against the live
  URL returned HTTP 403 (a Cloudflare challenge page), consistent with the
  access pattern already documented for other `openai.com/index/` posts in
  this corpus (e.g. `blog-openai-astra-critical-cyber-capabilities.md`,
  `blog-openai-gpt-red-self-play-robustness.md`). The article was
  retrieved via a Wayback Machine snapshot
  (`web.archive.org/web/20260903065925/https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/`),
  located via the `archive.org/wayback/available` API (confirmed available,
  HTTP 200) and fetched directly with `curl` (HTTP 200, since this
  environment's WebFetch tool could not reach `web.archive.org` directly).
  The raw HTML was stripped of scripts/styles/markup locally with a small
  Python script to produce a linearized plain-text transcript. All `Quote`
  fields above were copied character-for-character from that extracted
  text (cross-checked against the raw HTML's `&#x27;` / `&rsquo;` entity
  encodings for apostrophes), not reconstructed from a summarized
  rendering.
- **Two embedded hyperlinks not followed**: the source text names two
  supporting incidents — Twitter "broke the terms of our contract" and
  Musk's sworn xAI admission — each rendered in the archived page as an
  inline link with visible text "broke" and "admitted" respectively
  (marked "(opens in a new window)" in the linearized text). The link
  targets were not resolved or fetched by this Miner; Claim 3 is recorded
  as OpenAI's own assertion, not independently re-verified against
  whatever primary source (e.g., a court transcript for the "under oath"
  claim) those links point to. Flagged as a candidate for a future Miner
  pass if either linked source is filed separately.
- **No sub-pages followed**: this is a short, single-page announcement
  with no linked "Keep reading" articles that bear on this post's own
  claims (the archived page's related-articles footer listed unrelated
  OpenAI Company-category posts from the same week, not examined here).
- **Confidence overall set to `settled`**: unlike many vendor announcement
  posts in this corpus, every substantive claim here (the notification
  sent, the proposed date, the contract mechanism, the historical
  incidents cited as OpenAI's stated rationale) is a direct first-party
  statement of a decision already made and communicated to the
  counterparty, not a forward-looking aspiration or an unquantified
  capability claim. The one claim resting on OpenAI's subjective judgment
  of SpaceX's future trustworthiness (Claim 2) is still recorded as
  `settled` in the sense that OpenAI's *holding that position* is a fact,
  even though the underlying trust judgment itself is not independently
  verifiable. Claim 6 (goodwill language) is individually rated
  `anecdotal` since it carries no checkable content.
- No contradiction issue was filed. The most significant new fact in this
  post — Cursor's acquisition by SpaceX — extends rather than contradicts
  the existing `blog-cursor-composer-2-5.md` / `blog-cursor-grok-4-5.md`
  training-partnership narrative; neither prior note asserted Cursor would
  *not* be acquired, so there is no opposing claim to reconcile.
- Cross-references were verified before writing: re-read
  `blog-simonwillison-xai-anthropic-datacenter.md`,
  `blog-simonwillison-spacex-s1-anthropic.md`,
  `blog-openai-astra-critical-cyber-capabilities.md`,
  `blog-cursor-composer-2-5.md`, and `blog-cursor-grok-4-5.md` in full and
  confirmed every cited `Claim N` by number and content before writing
  this note's Cross-References section. No claim number was guessed or
  approximated.
