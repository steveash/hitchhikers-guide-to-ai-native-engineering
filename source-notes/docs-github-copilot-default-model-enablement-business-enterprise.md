---
source_url: https://github.blog/changelog/2026-07-29-default-model-enablement-for-copilot-business-and-enterprise
source_type: docs
title: "Default model enablement for Copilot Business and Enterprise"
author: GitHub (official changelog)
date_published: 2026-07-29
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: settled
issue: "#2319"
---

# Default Model Enablement for Copilot Business and Enterprise

> GitHub's July 29, 2026 changelog introducing a global "default availability for
> released models" policy for Copilot Business and Enterprise: generally-available
> models will be on by default going forward instead of requiring manual admin
> activation, with a 28-day configuration grace period before the policy takes
> effect on August 26, 2026, and a standing exclusion for open-weight and
> non-data-retention-agreement models regardless of policy.

## Source Context

- **Type**: docs (GitHub official product changelog, July 29, 2026; ~250 words of
  primary announcement text across a summary paragraph and a "What's changing"
  section, tagged "Improvement", 1-minute read). No linked documentation pages were
  present in the article body to follow per MINER.md §1 — the page's only outbound
  links are the changelog's own social-share controls and a `copilot` topic tag.
- **Author credibility**: GitHub engineering team announcing a production policy
  change to enterprise/organization Copilot model governance. Authoritative for:
  the existence and mechanics of the new policy, the "unconfigured" → "inherits
  default" state transition, the August 26, 2026 effective date, the 28-day grace
  period, and the standing open-weight/non-DRA exclusion list. Not a credible
  source for: how this policy interacts with per-model Enabled/Optional settings
  or targeted model rules (issue #957) beyond what is stated, whether the default
  policy value is itself "enabled" versus admin-set at rollout, the full current
  DRA-excluded model list beyond the two named examples, or any usage/adoption data.
- **Scope**: A single new governance policy — "default availability for released
  models" — configurable in enterprise and organization Copilot model settings,
  scoped to Copilot Business and Copilot Enterprise. Covers: the policy's purpose
  (removing the need for admins to manually activate each newly-GA model), the
  28-day configuration-only grace period, the August 26, 2026 effective date, the
  "unconfigured" → "inherits default" relabeling, preservation of explicit
  per-model choices, and the standing exclusion for open-weight models (DeepSeek,
  Kimi K2.7) and non-DRA models (Fable 5). Does NOT cover: which specific models
  are currently "unconfigured" and thus affected, whether the enterprise-level and
  organization-level policy settings can diverge (e.g., enterprise enabled but a
  specific org disabled), the UI navigation path to the setting, or any relationship
  to the `model: auto` conversation-starting-mode default (issue #1542).

## Extracted Claims

### Claim 1: GitHub is introducing a global default-enablement policy so that generally-available Copilot models are on by default, instead of requiring admins to manually activate each new model
- **Evidence**: Official GitHub changelog, opening summary statement framing this as the entry's core change.
- **Confidence**: settled (stated as the headline policy change in an official changelog)
- **Quote**: "We're introducing a global default enablement policy for generally available Copilot models on Copilot Business and Copilot Enterprise plans. Instead of requiring admins to manually turn on each new model as it ships, models that become generally available will now be on by default."
- **Our assessment**: This inverts the prior operating assumption in the corpus — that a newly-GA model requires explicit admin action to become available (implicit in the Enabled/Optional/Unconfigured taxonomy documented in `docs-github-copilot-org-targeted-model-rules.md`, issue #957, Claims 3 and 7). For Ch05: this is a default-behavior flip with direct governance consequence — enterprises that were relying on manual model activation as an implicit approval gate will lose that gate on August 26, 2026 unless they explicitly disable the policy.

### Claim 2: GitHub is adding a single opt-out control for organizations and enterprises that need stricter governance
- **Evidence**: Official changelog, second sentence of the opening summary, directly following Claim 1's statement.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "We're adding a single opt-out control for organizations and enterprises that need stricter governance."
- **Our assessment**: "Organizations and enterprises" (plural, both levels named) implies the opt-out control is configurable at both the organization level and the enterprise level, not just enterprise-wide — consistent with the two-level governance structure (enterprise defaults + organization-level control) already documented in `docs-github-copilot-org-targeted-model-rules.md` (issue #957). The source does not state how an organization-level opt-out interacts with an enterprise-level one if they diverge; flagged as a documentation gap.

### Claim 3: A new "default availability for released models" policy is available today in enterprise and organization model settings, but is configuration-only with no effect on model availability for the first 28 days
- **Evidence**: Official changelog, "What's changing" section, first paragraph.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Today, a new default availability for released models policy is available in your enterprise and organization model settings. For the next 28 days, this policy is configurable but has no effect on model availability — nothing changes for your users yet."
- **Our assessment**: This is the specific setting name practitioners should search for in Copilot admin settings: "default availability for released models." The 28-day grace period (July 29 → August 26, 2026) is a deliberate no-surprise rollout design, giving admins a window to set their preferred policy value before it takes live effect. For Ch05: document this as a concrete, dated action item for enterprise Copilot governance calendars — review and set this policy before August 26, 2026.

### Claim 4: On August 26, 2026, models that admins have not explicitly configured will be relabeled from "unconfigured" to "inherits default" and will begin following the policy setting — available if the policy is enabled, off if disabled
- **Evidence**: Official changelog, "What's changing" section, stating the effective-date mechanics with an explicit if/then behavior description.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "On August 26, the policy takes effect: Models you haven't explicitly configured will be relabeled from "unconfigured" to "inherits default" and will begin following your policy setting. If your policy is enabled (i.e., the default), those models become available to your users. If it's disabled, they stay off."
- **Our assessment**: This confirms "enabled" is the policy's own default value if an admin takes no action — an admin who does nothing during the 28-day window ends up with newly-GA models becoming available automatically. The "unconfigured" state name matches the state name used in `docs-github-copilot-org-targeted-model-rules.md` (issue #957, Claim 7: org admins can leave an "Optional" model "Unconfigured (inheriting enterprise default)"), but this source's "inherits default" is a renamed, dynamically-tracking state governed by the new policy toggle rather than a one-time inheritance snapshot — see Cross-References for why this extends rather than contradicts that note.

### Claim 5: "Inherits default" is a live, dynamic state that always tracks the policy setting, and flipping the policy at any time causes all "inherits default" models to follow immediately
- **Evidence**: Official changelog, "What's changing" section, third bullet.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: ""Inherits default" is a live, dynamic state that always tracks your policy. You can flip the policy at any time and all "inherits default" models follow immediately."
- **Our assessment**: This is an operationally important behavior for incident response — an admin who discovers an undesired newly-enabled model can flip the org/enterprise-wide policy and immediately turn off every model still in the "inherits default" state, without needing to locate and disable each model individually. For Ch05: document this single-toggle rollback as the fast governance lever for this policy, distinct from per-model Enabled/Disabled settings which require individual action.

### Claim 6: Explicit per-model choices are always preserved — a model an admin has deliberately enabled or disabled is never touched by this policy
- **Evidence**: Official changelog, "What's changing" section, fourth bullet.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Explicit choices are always preserved. If you've deliberately enabled or disabled a specific model, that setting is never touched."
- **Our assessment**: This bounds the blast radius of the policy change to genuinely untouched models only. Enterprises that have already explicitly configured their full model roster (e.g., via targeted model rules or per-model Enabled/Optional settings per issue #957) are unaffected by this policy regardless of its value — the risk is specific to models nobody has ever made an explicit decision about, which is most consequential for newly-GA models released after an enterprise's last governance review.

### Claim 7: Open-weight models (e.g., DeepSeek, Kimi K2.7) and models not covered by GitHub's data retention agreement (e.g., Fable 5) are excluded from default enablement regardless of the policy setting
- **Evidence**: Official changelog, "What's changing" section, fifth bullet, naming two specific open-weight models and one specific non-DRA model as examples.
- **Confidence**: settled (stated directly in official changelog, with named examples)
- **Quote**: "Open-weight models (e.g., DeepSeek, Kimi K2.7) and models not covered by GitHub's data retention agreement (e.g., Fable 5) are excluded from default enablement regardless of your policy."
- **Our assessment**: This is the most novel and guide-relevant claim in the source. It establishes a standing category exclusion that sits above the enabled/disabled policy toggle — even an enterprise that sets the policy to "enabled" does not get open-weight or non-DRA models auto-enabled; those always require explicit admin action regardless of the global default. Notably, Fable 5 is named as a non-DRA example despite being a first-party model family in this corpus's broader landscape (see the extensive `blog-simonwillison-fable-*`, `blog-anthropic-*fable5*`, and `blog-latentspace-*fable*` notes) — this is the first corpus source to document that data-retention-agreement coverage, not model-family origin, is the governing factor for Copilot's default-enablement exclusion list. For Ch04/Ch05: teams relying on this policy to auto-provision new models should not assume "enabled" policy covers open-weight or non-DRA models; those remain a manual-activation category indefinitely.

### Claim 8: The recommended action for organizations preferring manual model approval is to set the policy to "disabled" before August 26
- **Evidence**: Official changelog, closing paragraph of "What's changing," stated as direct guidance to admins.
- **Confidence**: settled (stated directly in official changelog as explicit recommendation)
- **Quote**: "Use the next 28 days to review your model settings. If you're happy with models being available by default, no action is needed. If you'd rather manually approve each model, set the policy to disabled before August 26."
- **Our assessment**: This is the source's explicit call to action, confirming Claim 4's inference that no action defaults to "enabled." For Ch05: this is a concrete, dated checklist item — enterprise Copilot governance teams that prefer manual model approval (the posture implied by the existing Enabled/Optional/targeted-rules governance stack documented in issue #957) must take affirmative action before August 26, 2026, or their governance posture will change by default rather than by decision.

## Concrete Artifacts

### Full changelog body text (verified against raw HTML, not AI-summarized WebFetch output)

```
Source: https://github.blog/changelog/2026-07-29-default-model-enablement-for-copilot-business-and-enterprise
Title: Default model enablement for Copilot Business and Enterprise
Published: July 29, 2026 · 1 minute read · Type: Improvement

--- SUMMARY ---

We're introducing a global default enablement policy for generally available
Copilot models on Copilot Business and Copilot Enterprise plans. Instead of
requiring admins to manually turn on each new model as it ships, models that
become generally available will now be on by default. We're adding a single
opt-out control for organizations and enterprises that need stricter governance.

--- WHAT'S CHANGING ---

Today, a new default availability for released models policy is available in
your enterprise and organization model settings. For the next 28 days, this
policy is configurable but has no effect on model availability — nothing
changes for your users yet.

On August 26, the policy takes effect:

- Models you haven't explicitly configured will be relabeled from "unconfigured"
  to "inherits default" and will begin following your policy setting. If your
  policy is enabled (i.e., the default), those models become available to your
  users. If it's disabled, they stay off.
- "Inherits default" is a live, dynamic state that always tracks your policy.
  You can flip the policy at any time and all "inherits default" models follow
  immediately.
- Explicit choices are always preserved. If you've deliberately enabled or
  disabled a specific model, that setting is never touched.
- Open-weight models (e.g., DeepSeek, Kimi K2.7) and models not covered by
  GitHub's data retention agreement (e.g., Fable 5) are excluded from default
  enablement regardless of your policy.

Use the next 28 days to review your model settings. If you're happy with models
being available by default, no action is needed. If you'd rather manually
approve each model, set the policy to disabled before August 26.

[topic tag: copilot]
```

### Timeline

```
GitHub Copilot Default Model Enablement Policy

July 29, 2026:    Policy introduced; "default availability for released models"
                   setting appears in enterprise/org model settings. Configurable,
                   no effect yet.

Jul 29 – Aug 25:  28-day grace period. Admins should review and set the policy.
                   Default value if untouched: enabled.

August 26, 2026:  POLICY TAKES EFFECT
                   - "Unconfigured" models relabeled "inherits default"
                   - "Inherits default" models follow the policy setting live
                   - Explicit per-model Enabled/Disabled settings unaffected
                   - Open-weight (DeepSeek, Kimi K2.7) and non-DRA (Fable 5)
                     models remain excluded regardless of policy value

Source: GitHub Copilot official changelog, July 29, 2026
```

### Standing exclusion list (named examples, not necessarily exhaustive)

```
Category                          Named examples       Effect
─────────────────────────────────────────────────────────────────────────
Open-weight models                DeepSeek, Kimi K2.7   Excluded from default
                                                          enablement regardless
                                                          of policy setting
Models outside GitHub's data      Fable 5               Excluded from default
retention agreement (non-DRA)                            enablement regardless
                                                          of policy setting

Source: GitHub Copilot official changelog, July 29, 2026. Examples are
illustrative ("e.g.") — the changelog does not state these are the complete
lists for either category.
```

## Cross-References

- **Extends** `docs-github-copilot-org-targeted-model-rules.md` (issue #957,
  Claims 3 and 7): That May 26, 2026 source documented the Enabled/Optional
  model-availability taxonomy and the "Unconfigured (inheriting enterprise
  default)" state for organization-level control of "Optional" models. This
  source reuses the "unconfigured" state name but describes a distinct,
  newer mechanism: a single enterprise/organization-wide policy toggle
  ("default availability for released models") that determines what
  unconfigured, never-explicitly-set models do — specifically for models
  that have never received any admin decision at all, most relevantly newly-
  GA models released after an enterprise's last governance review. This is
  not a contradiction: issue #957 describes per-model Enabled/Optional
  settings an admin actively assigns, and per-org overrides of "Optional"
  models; this source describes what happens to models nobody has assigned
  anything to yet, via a policy that (per Claim 5) dynamically tracks a
  single toggle rather than being fixed at configuration time. The guide
  should present the two sources together as complementary layers of the
  same governance stack: (1) this source's global default-enablement policy
  governs the starting state for never-touched models, (2) issue #957's
  Enabled/Optional/targeted-rules mechanics govern models an admin has
  actively decided about. No contradiction issue filed.
- **Extends** `docs-github-copilot-enterprise-auto-model-default.md` (issue
  #1542, Claims 1–2): That July 1, 2026 source documented an enterprise
  `managed-settings.json` `model: auto` permission that sets which *mode*
  (auto vs. manual) a new conversation starts in — a soft default that does
  not remove manual model selection. This source's policy is a different
  governance axis entirely: whether a model is *available for selection at
  all*, not what mode a conversation starts in. The two are independent and
  compose: an enterprise could have `model: auto` as the conversation
  starting mode (issue #1542) while also controlling, via this source's
  policy, which underlying models are available for auto or manual selection
  to draw from. Neither source states an explicit interaction between the two
  mechanisms; flagged as a documentation gap for the guide to note rather than
  resolve.
- **Corroborates** `docs-github-copilot-gpt53codex-base-model.md` (issue
  #797, Claim 5): That May 17, 2026 source established that the base-model
  change applied only to Copilot Business and Copilot Enterprise plans, with
  Pro, Pro+, and Free unaffected. This source's default-enablement policy is
  scoped identically — Business and Enterprise only — reconfirming that
  model-governance policy changes in this corpus continue to be gated to the
  same two paid enterprise plan tiers, not individual plans.
- **Novel**:
  - First corpus source to document a global "default availability for
    released models" policy governing whether newly-GA Copilot models are
    auto-enabled or require manual admin activation. Prior governance
    sources (issue #957) document per-model targeting and availability
    controls an admin actively sets; none document a policy governing the
    default treatment of models an admin has never touched.
  - First corpus source to document a standing, policy-independent exclusion
    category for open-weight models (DeepSeek, Kimi K2.7 named) and models
    outside GitHub's data retention agreement (Fable 5 named) in the Copilot
    model-governance context.
  - First corpus source to state explicitly that GitHub's own data-retention-
    agreement coverage, rather than model-family origin, governs a Copilot
    default-enablement exclusion — notable because Fable 5 is a first-party
    model family extensively covered elsewhere in this corpus's broader
    landscape notes, yet is excluded here on DRA grounds specific to the
    Copilot product's data handling terms with that model, not a blanket
    judgment about the model itself.

## Guide Impact

- **Chapter 02 (Harness Engineering / Tooling Landscape)**: Note that as of
  August 26, 2026, newly-GA Copilot models become available to Business/
  Enterprise users automatically unless an admin has explicitly disabled the
  "default availability for released models" policy. Harness configurations
  or documentation that assume a stable, admin-curated model roster should
  flag this as a source of roster drift — the available model set can change
  without an explicit admin action from August 26 onward, for any enterprise
  that leaves the policy at its "enabled" default.
- **Chapter 04 (Model Selection and Cost Management)**: Flag the policy's
  "enabled by default" behavior as a cost-governance risk: newly-GA models
  that carry a non-zero premium-request or AI-credit multiplier can become
  available to end users without a budget review, if an enterprise takes no
  action during the 28-day window. Recommend enterprise finance/governance
  teams treat "set this policy to disabled" as the conservative default
  during any budget-review cycle, re-enabling per-model as each new model is
  evaluated. Also note the standing DRA-based exclusion (Claim 7) as a
  reminder that "enabled" policy does not equal "all models available" —
  open-weight and non-DRA models remain gated separately.
- **Chapter 05 (Enterprise Governance)**: Add a dated action item to the
  enterprise Copilot governance checklist: review and explicitly set the
  "default availability for released models" policy (enterprise and/or
  organization level) before August 26, 2026. Present this alongside the
  existing Enabled/Optional/targeted-model-rules governance stack (issue
  #957) as a fourth lever, specifically governing models nobody has yet
  made an explicit decision about. Document the single-toggle rollback
  behavior (Claim 5) as the fast-response mechanism if an undesired model
  becomes available. Note the two-level (enterprise and organization)
  scope of the opt-out control (Claim 2) without a stated resolution order
  if the two levels diverge — flag this as an open question for governance
  teams to test directly rather than assume.

## Extraction Notes

1. **Quotes verified against raw HTML, not AI-summarized WebFetch output**:
   An initial WebFetch call returned a reasonable but restructured summary
   (different heading names, paraphrased sentences). To satisfy MINER.md
   §2a's verbatim-quote requirement, the full article body was independently
   fetched via `curl` and the article `<article>` element was isolated and
   stripped of HTML tags directly, then cross-checked against `grep`
   matches on the raw HTML (confirming curly-quote and em-dash entities
   `&rsquo;`/`&rdquo;`/`&hellip;` render as the apostrophes/quotes/ellipsis
   used in the claims above). All quotes in this note are taken from that
   raw-HTML extraction, not from the WebFetch summary. This gives higher
   quote-fidelity confidence than several prior Copilot changelog notes in
   this corpus, which flagged WebFetch AI-summarization as an unverified-quote
   risk in their own Extraction Notes (e.g., issue #1542's note, Extraction
   Note 2; issue #797's note, Extraction Note 1; issue #845's note,
   Extraction Note 1).
2. **No linked sub-pages to follow**: Unlike several prior Copilot changelog
   sources in this corpus (issues #957, #1542), this article contains no
   inline links to supporting documentation pages — only the changelog's own
   navigation, social-share controls, and a `copilot` topic-browse link.
   MINER.md §1's "follow up to 5 linked pages" step therefore found nothing
   substantive to follow; all eight claims are drawn directly from the
   changelog body.
3. **Source is short by design (~250 words of primary text)**: All
   substantive claims are exhausted in Claims 1–8. The source does not name
   a complete list of currently-"unconfigured" models, does not specify the
   UI navigation path to the new setting, and does not state whether
   enterprise-level and organization-level policy values can diverge or
   which takes precedence if they do — flagged as documentation gaps in
   Guide Impact above rather than filled in.
4. **No contradictions found**: This source's "unconfigured" → "inherits
   default" mechanism overlaps in terminology with the org-targeted-model-
   rules note's "Unconfigured (inheriting enterprise default)" state (issue
   #957, Claim 7), but describes a distinct, newer, policy-driven mechanism
   rather than restating or reversing that claim. See Cross-References for
   the detailed reasoning on why this is treated as an extension, not a
   contradiction. No contradiction issue filed per MINER.md §4a.
