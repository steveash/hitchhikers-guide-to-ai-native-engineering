---
source_url: https://github.blog/changelog/2026-08-28-upcoming-changes-to-github-copilot-policies-and-billing
source_type: docs
title: "Upcoming changes to GitHub Copilot policies and billing"
author: GitHub (official changelog)
date_published: 2026-08-28
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#3051"
---

# Upcoming Changes to GitHub Copilot Policies and Billing

> GitHub's August 28, 2026 changelog announcing three separate, dated policy
> and billing changes: Business/Enterprise signups reopen September 1, 2026
> with a new upfront-per-seat payment requirement (extending to existing
> credit-card/PayPal customers October 1, 2026); Copilot Chat on github.com,
> GitHub Mobile, and Copilot cloud agent converge into a single unified
> experience no earlier than September 28, 2026, moving web/mobile chat data
> retention from 28 days to the life of the account; and the Copilot code
> review default effort level flips from Lite to Balanced on September 28,
> 2026 unless an org or repo explicitly locks in Lite beforehand.

## Source Context

- **Type**: docs (GitHub official product changelog, August 28, 2026; a
  "3 minute read" article, roughly 550 words across three named sections,
  each with its own "What's changing" / "What's not changing" or equivalent
  subsections)
- **Author credibility**: GitHub engineering/product team announcing three
  concrete, dated policy and billing changes on its own official changelog.
  Authoritative for the fact that these changes are planned, their effective
  or target dates, which account types/plans are affected, and the specific
  configuration steps to opt out or lock in prior behavior. Not a credible
  source for why GitHub chose these specific dates or thresholds, for
  competitive/market context, or for quantifying the actual cost or workflow
  impact these changes will have on any specific team.
- **Scope**: Covers three independent changes bundled into one changelog
  entry: (1) Business/Enterprise signup reopening and upfront-billing
  changes, (2) convergence of Copilot Chat on github.com, GitHub Mobile, and
  Copilot cloud agent into one experience/policy with a chat-data-retention
  change, and (3) the Copilot code review default effort level moving from
  Lite to Balanced. Does NOT cover: specific per-seat dollar pricing, exact
  AI-credit or Actions-minute cost deltas from the Balanced default flip,
  whether Free/Pro/Pro+/Student individual plans are affected (the entry is
  scoped to Business/Enterprise for billing and to Business/Enterprise "team"
  policy language for the unified-experience section), or a firm launch date
  for the unified experience beyond "no earlier than September 28th, 2026."

## Extracted Claims

### Claim 1: Starting September 1, 2026, GitHub will resume accepting new Copilot Business and Enterprise signups paid by credit card or PayPal, alongside strengthened account vetting
- **Evidence**: Dedicated changelog section, "Reopening Copilot Business and Enterprise signups with billing updates."
- **Confidence**: settled (dated product/policy change stated directly in official changelog)
- **Quote**: "Starting September 1, 2026, GitHub will start reenabling sign-ups for new Copilot Business and Copilot Enterprise customers paying by credit card or PayPal. To improve availability and reliability of Copilot services, we're strengthening account vetting and updating billing experiences for customers who pay by credit card or PayPal."
- **Our assessment**: The framing implies these signups were previously paused or restricted for credit-card/PayPal payers specifically — the changelog does not state when or why that prior pause began, only that it is ending September 1 with new conditions attached. For Ch05 (Team Adoption): teams that were previously blocked from self-service Business/Enterprise signup via credit card or PayPal (e.g., because they lacked an invoiced/contracted billing relationship) now have a re-opened path, but it comes with new upfront-payment terms (Claim 2) rather than a return to prior terms.

### Claim 2: All new Copilot Business or Enterprise seat assignments will require upfront payment per seat before the user gains access, and existing credit-card/PayPal customers face the same upfront-per-seat charge starting October 1, 2026
- **Evidence**: "What's changing" subsection of the signup-reopening section.
- **Confidence**: settled (specific dated billing mechanism stated directly in official changelog)
- **Quote**: "All new Copilot Business or Copilot Enterprise seat assignments will require payment for each seat before users gain Copilot access."
- **Quote**: "At the start of the next billing cycle, all Copilot Business and Copilot Enterprise seats assigned will incur an upfront charge. This will apply to existing Copilot Business and Copilot Enterprise customers with a credit card or paypal payment method starting October 1, 2026."
- **Our assessment**: This is the highest-impact claim in the source for teams already running Copilot Business/Enterprise on credit card or PayPal billing. The shift is from (implicitly) pay-after-use or standard monthly billing to pay-before-access per seat — a cash-flow and provisioning-workflow change, not a price change (see Claim 3). For Ch03/Ch05: any automated or bulk seat-provisioning workflow (e.g., auto-assigning Copilot seats to new hires via SCIM or a script) must now account for an upfront per-seat charge succeeding before the user can actually use Copilot, which may introduce a provisioning delay or a billing-approval gate that didn't previously exist.

### Claim 3: Copilot Business and Enterprise per-seat pricing is not changing, but seat removal will not generate a prorated refund
- **Evidence**: "What's not changing" subsection of the signup-reopening section.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Copilot Business and Copilot Enterprise prices are not changing." "Revoking a seat does not result in a prorated refund. The removal will be reflected in your next monthly billing cycle."
- **Our assessment**: Combined with Claim 2, this means the billing *model* is changing (upfront, per-seat, non-refundable-on-removal) while the *price* stays flat. Teams doing headcount-driven seat churn (e.g., contractors rotating on and off a repo) should budget for the fact that removing a seat mid-cycle does not recover any of that cycle's cost — the seat is paid for in full regardless of how much of the billing cycle remains. For Ch05 (Team Adoption / TCO): this changes the cost-optimization advice around frequent seat reassignment; churning seats to save money no longer works the way it might have when seats were billed differently.

### Claim 4: Seats added mid-cycle continue to be prorated from assignment date to end of the billing cycle, and additional usage beyond included allowances remains purchasable with spend controls, usage tracking, and additional AI-credit purchases still available
- **Evidence**: Remainder of the "What's not changing" subsection.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "All seats added in the middle of a billing cycle will continue to be prorated from date of assignment to end of bill cycle." "Spend controls, usage tracking, and the option to purchase additional AI credits will remain available."
- **Our assessment**: This confirms the existing usage-governance tooling (spend controls, usage tracking, AI-credit top-ups) is unaffected by the billing-model change — the change is specifically about *when* the base seat charge is collected (upfront vs. not), not about removing any of the cost-control mechanisms teams may already depend on. For Ch05: admins who have built governance workflows around spend controls and usage tracking do not need to rebuild them; only the seat-assignment billing trigger changes.

### Claim 5: Fully canceling Copilot and later returning may trigger updated account vetting and billing behaviors
- **Evidence**: Closing sentence of the signup-reopening section, before the link to Copilot Quick Start documentation.
- **Confidence**: settled (stated directly, though the specific vetting/billing behaviors triggered are not enumerated)
- **Quote**: "Fully canceling Copilot and returning later may trigger updated account vetting and billing behaviors."
- **Our assessment**: This is a vague but consequential warning — it implies that "cancel now, resubscribe later to reset something" is not a safe assumption under the new regime, without specifying what the "updated" vetting or billing looks like. For Ch05: teams considering a temporary Copilot cancellation (e.g., over a hiring freeze or budget pause) should not assume resubscription will restore prior terms unchanged; this is a caveat worth flagging even though the source doesn't quantify it.

### Claim 6: No earlier than September 28, 2026, GitHub will relaunch Copilot Chat on github.com, Copilot Chat in GitHub Mobile, and Copilot cloud agent as a single, unified Copilot experience governed by one policy, enabled by default
- **Evidence**: Dedicated changelog section, "Copilot cloud agent, Copilot Chat on github.com, and Copilot Chat in GitHub Mobile are converging to a single experience and policy."
- **Confidence**: settled for the fact of convergence; the "no earlier than" phrasing means the specific launch date is explicitly not committed
- **Quote**: "No earlier than September 28th, 2026, GitHub will relaunch Copilot Chat on github.com, Copilot Chat in GitHub Mobile, and GitHub Copilot cloud agent as a single, unified Copilot experience." "The separate policies for these experiences will be replaced by a single policy." "This unified Copilot experience will be enabled by default after launch."
- **Our assessment**: GitHub deliberately hedges the date ("no earlier than") rather than committing to September 28 as a firm launch date — unlike the code review default change (Claim 11) and the October 1 billing change (Claim 2), which use firm dates. Guide text citing this should preserve that distinction: the code review and billing dates are commitments, the unified-experience date is a floor, not a target. For Ch02 (Harness Engineering): this collapses three previously independently-policied surfaces (web chat, mobile chat, cloud agent) into one, which simplifies the policy surface admins must manage but also means a single opt-out decision now governs three previously separable surfaces.

### Claim 7: As part of the unified experience, Copilot on github.com will fully migrate to the "agent sessions" architecture previously used only by Copilot cloud agent, and as a direct result chat data retention changes from 28 days to the life of the account
- **Evidence**: "What's changing" subsection of the unified-experience section.
- **Confidence**: settled (stated directly as a consequence of the architectural migration)
- **Quote**: "Copilot on github.com will fully migrate to the agent sessions experience, previously used only by Copilot cloud agent. As a result, chat data will be retained for the life of the account instead of 28 days, aligning with our existing Copilot cloud agent experience."
- **Our assessment**: This is the single most consequential claim in the source for privacy- and compliance-conscious teams. A 28-day retention window becoming indefinite (life-of-account) retention is a material data-handling change, not a cosmetic UX update — any team that has represented Copilot web chat as having bounded data retention (e.g., in an internal data-handling policy or a customer-facing compliance statement) needs to update that representation once this migration ships. The changelog frames this as an automatic *consequence* of the architectural migration (chat moving onto the agent-sessions storage model) rather than as an independently chosen retention policy — worth noting because it means the retention change cannot be selectively opted out of without opting out of the entire unified experience (Claim 8).

### Claim 8: Cloud agent will leverage Sandbox to provide a faster cloud experience as part of the unification
- **Evidence**: "What's changing" subsection of the unified-experience section.
- **Confidence**: settled (stated directly, though no performance figures are given)
- **Quote**: "Cloud agent will leverage Sandbox to provide a faster cloud experience."
- **Our assessment**: No metrics accompany this claim (no latency numbers, no before/after comparison) — it should be treated as a vendor performance assertion, not a verified benchmark, consistent with how this corpus treats other unqualified vendor performance claims. For Ch04 (Agents): if Copilot cloud agent's execution substrate changes to "Sandbox," this may be worth tracking against other corpus notes about GitHub's sandboxed execution environments for agent runs, though this source does not name or describe "Sandbox" beyond the one-line mention.

### Claim 9: Opting out of the unified experience means losing Copilot access on github.com and GitHub Mobile entirely after the new experience launches — there is no "opt out but keep access under old policy" path
- **Evidence**: "Stay opted in" subsection of the unified-experience section.
- **Confidence**: settled (stated directly and unambiguously)
- **Quote**: "No changes are required to keep Copilot available on github.com and GitHub Mobile. However, if you opt out of the unified experience, you or your teams will lose access to Copilot on github.com and GitHub Mobile after the new experience launches."
- **Our assessment**: This is a binary framing with no middle ground: admins can accept the unified policy (and its retention change, Claim 7) and keep web/mobile Copilot access, or reject it and lose that access entirely. There is no disclosed option to keep the old 28-day-retention chat experience while declining the unification. For Ch05: Business/Enterprise administrators evaluating this should treat it as an accept-or-lose-access decision for web and mobile Copilot specifically — Copilot cloud agent access itself is not described as contingent on this opt-in/opt-out choice in the same binary way (the source frames cloud agent as already converging into the same experience, so it is unclear from this source alone whether declining also removes cloud agent access, or only web/mobile chat access — the quoted text names only "Copilot on github.com and GitHub Mobile" as what is lost).

### Claim 10: Business and Enterprise administrators should review and set the unified-experience policy before September 28, 2026 via Copilot settings → "Copilot cloud agent (coming soon)" → policy option
- **Evidence**: "Stay opted in" subsection, including the numbered configuration steps.
- **Confidence**: settled (concrete configuration path stated directly in official changelog)
- **Quote**: "Business and enterprise administrators should review the policy before September 28th, 2026 and confirm that it reflects how they want to manage Copilot access for their teams."
- **Our assessment**: The changelog gives an explicit three-step path: "Go to Copilot settings on github.com. Select Copilot cloud agent (coming soon). Set the policy option." The parenthetical "(coming soon)" label on the settings entry itself signals that, as of August 28, 2026 (publication date), the actual policy control surface described here is not yet live — administrators reading this changelog on publication day cannot yet act on it, only prepare to. For Ch05: add this as a dated action item for Business/Enterprise admins — review and set this policy before September 28, 2026, once the "Copilot cloud agent (coming soon)" settings entry goes live.

### Claim 11: Starting September 28, 2026, the Copilot code review "Default" effort-level setting resolves to Balanced instead of Lite for both existing and new repositories/organizations, unless Lite is explicitly selected beforehand
- **Evidence**: Dedicated changelog section, "Copilot code review default is changing to Balanced effort level," including its "Balanced is becoming the default effort level" subsection.
- **Confidence**: settled (specific dated default-value change stated directly in official changelog)
- **Quote**: "For existing and new repositories and organizations using Copilot code review, the review effort value of Default uses Balanced starting September 28th, 2026."
- **Quote**: "If you'd prefer to keep Lite as your default experience, change your review effort level away from Default and explicitly select Lite in your repository or organization settings before September 28th, 2026. We'll respect that selection and won't switch your default to Balanced."
- **Our assessment**: This is a silent cost-increasing default change for any org or repo currently relying on the implicit "Default" value rather than an explicit Lite/Balanced selection — per `docs-github-copilot-code-review-effort-levels-ga.md` Claim 8, Balanced "uses more AI credits and GitHub Actions minutes than Lite reviews," so teams that take no action will see their per-review cost profile shift upward on September 28 without any code or configuration change on their part. The changelog's own "How review effort level defaults work" subsection restates the org-default / repo-default precedence already documented in that prior note's Claims 4–5 (organization default → repository override), so the only genuinely new fact here is which value "Default" resolves to, and the date it flips. For Ch02 and Ch05: this is a concrete, dated action item — any team wanting to keep Lite's lower AI-credit/Actions-minute cost profile must explicitly select Lite in org or repo settings before September 28, 2026, rather than relying on "Default."

## Concrete Artifacts

### Changelog Full Text (verbatim, extracted via raw HTML fetch, August 28, 2026)

```
Title: Upcoming changes to GitHub Copilot policies and billing
Published: August 28, 2026 (Improvement, 3 minute read)
Source: https://github.blog/changelog/2026-08-28-upcoming-changes-to-github-copilot-policies-and-billing

To provide a strong, consistent Copilot experience, we're making three
separate, upcoming changes to Copilot policies and billing. Please review
the upcoming updates to understand what may impact you.

--- SECTION: Reopening Copilot Business and Enterprise signups with billing
    updates ---

Starting September 1, 2026, GitHub will start reenabling sign-ups for new
Copilot Business and Copilot Enterprise customers paying by credit card or
PayPal. To improve availability and reliability of Copilot services, we're
strengthening account vetting and updating billing experiences for
customers who pay by credit card or PayPal.

What's changing

- All new Copilot Business or Copilot Enterprise seat assignments will
  require payment for each seat before users gain Copilot access.
- At the start of the next billing cycle, all Copilot Business and Copilot
  Enterprise seats assigned will incur an upfront charge. This will apply
  to existing Copilot Business and Copilot Enterprise customers with a
  credit card or paypal payment method starting October 1, 2026.
- If you exceed your included usage, additional payment may be required
  for you and your users to continue using Copilot.
- Included usage may be prorated across the month to align with the seat
  cost proration.

What's not changing

- Copilot Business and Copilot Enterprise prices are not changing.
- Revoking a seat does not result in a prorated refund. The removal will
  be reflected in your next monthly billing cycle.
- All seats added in the middle of a billing cycle will continue to be
  prorated from date of assignment to end of bill cycle.
- Additional usage exceeding included allowances will remain available
  for purchase.
- Spend controls, usage tracking, and the option to purchase additional
  AI credits will remain available.

Existing Copilot Business and Copilot Enterprise customers can expect
these billing updates to take effect starting October 1, 2026.

Fully canceling Copilot and returning later may trigger updated account
vetting and billing behaviors.

For more information, read our Copilot Quick Start documentation.

--- SECTION: Copilot cloud agent, Copilot Chat on github.com, and Copilot
    Chat in GitHub Mobile are converging to a single experience and
    policy ---

No earlier than September 28th, 2026, GitHub will relaunch Copilot Chat on
github.com, Copilot Chat in GitHub Mobile, and GitHub Copilot cloud agent
as a single, unified Copilot experience.

What's changing

- The separate policies for these experiences will be replaced by a
  single policy.
- This unified Copilot experience will be enabled by default after
  launch.
- Cloud agent will leverage Sandbox to provide a faster cloud experience.
- Copilot on github.com will fully migrate to the agent sessions
  experience, previously used only by Copilot cloud agent. As a result,
  chat data will be retained for the life of the account instead of 28
  days, aligning with our existing Copilot cloud agent experience.

Stay opted in

No changes are required to keep Copilot available on github.com and
GitHub Mobile. However, if you opt out of the unified experience, you or
your teams will lose access to Copilot on github.com and GitHub Mobile
after the new experience launches.

Business and enterprise administrators should review the policy before
September 28th, 2026 and confirm that it reflects how they want to manage
Copilot access for their teams.

To update the policy:
  1. Go to Copilot settings on github.com.
  2. Select Copilot cloud agent (coming soon).
  3. Set the policy option.

--- SECTION: Copilot code review default is changing to Balanced effort
    level ---

Following the release of Copilot code review effort levels, the default
review effort level for GitHub Copilot code review is changing from Lite
to Balanced.

How review effort level defaults work

You can set a default review effort level at the organization and
repository levels:

- The organization default applies to all repositories owned by the
  organization that haven't selected their own review effort level.
- The repository default applies to all automatically requested reviews
  within the repository. For manually requested reviews, you can select
  which effort level is used from the "Reviewers" bar in the pull
  request.

Balanced is becoming the default effort level

For existing and new repositories and organizations using Copilot code
review, the review effort value of Default uses Balanced starting
September 28th, 2026.

If you'd prefer to keep Lite as your default experience, change your
review effort level away from Default and explicitly select Lite in your
repository or organization settings before September 28th, 2026. We'll
respect that selection and won't switch your default to Balanced.

Review the Copilot code review documentation to understand how this may
affect your usage.
```

### Three-Change Summary Table (compiled from the changelog)

```
Change                          Effective Date          Scope
──────────────────────────────────────────────────────────────────────────
Business/Enterprise signup       Sept 1, 2026            New customers,
reopening (credit card/PayPal)                           credit card/PayPal
Upfront per-seat billing         Oct 1, 2026 (existing)   Existing Business/
(new customers: immediate)                               Enterprise customers,
                                                          credit card/PayPal
Unified Chat/Mobile/Cloud Agent  No earlier than          Copilot Chat on
experience + policy                Sept 28, 2026          github.com, GitHub
                                  (floor, not committed)  Mobile, cloud agent
Chat data retention:             Tied to unified-         Copilot on github.com
28 days -> life of account       experience launch        (post-migration)
Code review default:             Sept 28, 2026 (firm)     Repos/orgs using
Lite -> Balanced                                          "Default" setting
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-effort-levels-ga.md` (issue #2585):
  - This source's Claim 11 (Default resolves to Balanced starting Sept 28, 2026)
    is the direct sequel to that note's Claims 1–2 (Low/Medium renamed to
    Lite/Balanced, GA August 7, 2026) and Claim 8 (Balanced consumes more AI
    credits and GitHub Actions minutes than Lite). That note documented the
    two-tier system and its costs; this source documents which tier is now
    the silent default and the exact date the default flips.
  - This source's changelog restates, without adding new mechanics, the
    org-default/repo-default precedence already fully documented in that
    note's Claims 4–5 and its "Effort-Level Configuration Hierarchy" Concrete
    Artifact. No new precedence facts are introduced here — only the default
    *value* changes, not the *hierarchy*.

- **Extends** `docs-github-copilot-code-review-actions-billing.md` (issue #445):
  - That source established that Copilot code review draws on both AI Credits
    and GitHub Actions minutes for private-repo reviews (dual billing since
    June 1, 2026). This source's Claim 11 identifies a concrete, dated event
    (September 28, 2026) that will raise the *typical* per-review cost for any
    org/repo that has not explicitly configured Lite — a first-class trigger
    for re-checking Actions-minute and AI-credit consumption trend lines
    around that date.

- **Extends** `docs-github-copilot-chat-agent-sessions.md` (issue #1145):
  - That source documented the "agent sessions" architecture as, at the time,
    specific to Copilot cloud agent (CCA), with Copilot Chat gaining the
    ability to query and search CCA sessions. This source's Claim 7 shows the
    architecture itself expanding: Copilot Chat on github.com will "fully
    migrate to the agent sessions experience, previously used only by Copilot
    cloud agent" — the retention-model consequence (28 days → life of
    account) is a direct, disclosed side effect of that migration, not an
    independent retention-policy decision.

- **Extends** `docs-github-copilot-web-model-consolidation.md` (issue #845):
  - That source documented GitHub narrowing the Copilot web chat model roster
    in May 2026 with the stated rationale of ensuring "reliable responses"
    and a "simplified experience." This source's opening line — "To provide a
    strong, consistent Copilot experience, we're making three separate,
    upcoming changes" — continues the same consistency-over-flexibility
    narrative GitHub has used repeatedly across 2026 for web/Copilot Chat
    changes, now applied to policy unification and billing rather than model
    availability.

- **Extends** `docs-github-copilot-individual-plan-changes.md` (issue #289):
  - That source documented new-signup *pauses* for individual Copilot Pro,
    Pro+, and Student plans (April 2026), explicitly scoped away from
    Business/Enterprise. This source documents the opposite trajectory for a
    different tier: Business/Enterprise signups *reopening* (Claim 1) — but
    with new upfront-payment terms attached, not a return to whatever billing
    terms preceded the pause this source implies existed for credit-card/
    PayPal payers. Guide text should keep these two signup events clearly
    separated by plan tier: individual-plan signup pauses (Pro/Pro+/Student,
    still open as of that note's last check) versus Business/Enterprise
    signup reopening with upfront billing (this source).

- **Contradicts**: None identified. No existing corpus source documents
  Copilot web chat's prior data-retention window, Business/Enterprise seat
  billing timing, or a "Default" code-review effort-level value in a way
  this source's claims conflict with — the retention change (Claim 7) and
  default-value change (Claim 11) are the first corpus sources to state
  the *prior* state (28 days; Lite-as-default) at all, so there is nothing
  in the existing corpus to contradict. No contradiction issue filed.

- **Novel**:
  - **Upfront, per-seat pre-payment as the Business/Enterprise billing model**
    for credit-card/PayPal customers: no prior corpus source documents
    GitHub requiring payment before seat access is granted, for any plan tier.
  - **28-day chat data retention as the prior state for Copilot on github.com**:
    this is the first corpus source to state a specific retention window for
    Copilot web chat data, revealed via its announced replacement (life of
    account).
  - **Convergence of three previously separate Copilot surfaces (web chat,
    mobile chat, cloud agent) under one policy**: no prior corpus source
    documents GitHub unifying policy across these three specific surfaces;
    prior sources (e.g., `docs-github-copilot-chat-agent-sessions.md`)
    documented them gaining *interoperability* (chat querying CCA sessions)
    while remaining under separate policies.
  - **A named "Default" effort-level value for code review distinct from
    "Lite" and "Balanced"**: prior corpus sources documented Lite and
    Balanced as the two selectable effort levels; this source is the first
    to reveal that org/repo settings can also be left at an unresolved
    "Default" state that itself maps to one of the two levels, and that this
    mapping is a value GitHub can and will change.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Update any code-review effort-level
  configuration guidance built from `docs-github-copilot-code-review-effort-levels-ga.md`
  to flag September 28, 2026 as the date "Default" silently becomes Balanced
  rather than Lite. Teams standardizing review-effort configuration across
  many repositories should treat "explicitly set Lite or Balanced, never rely
  on Default" as the recommended practice going forward, since Default's
  resolved value is not stable over time. Also update the Copilot surface
  inventory to note that Copilot Chat on github.com, GitHub Mobile, and
  cloud agent are converging under one policy no earlier than September 28,
  2026 — this reduces the number of independently configurable policy
  surfaces admins must track from three to one, once it ships.

- **Chapter 03 (Cost Management)**: Add two dated, concrete cost-impact
  events to any GitHub Copilot TCO discussion: (1) October 1, 2026 — existing
  Business/Enterprise credit-card/PayPal customers begin upfront per-seat
  billing, changing cash-flow timing though not per-seat price; (2)
  September 28, 2026 — code review's Default effort level moves to Balanced,
  which per `docs-github-copilot-code-review-effort-levels-ga.md` Claim 8
  consumes more AI credits and Actions minutes than Lite, raising the
  effective per-review cost for any org/repo that has not explicitly pinned
  Lite. Recommend an explicit action item: audit code review effort-level
  settings before September 28, 2026, and decide deliberately rather than
  inheriting the new default.

- **Chapter 05 (Team Adoption / Governance)**: Add three dated action items
  for Business/Enterprise administrators: (1) before September 1, 2026 —
  understand that new seat assignments will require upfront per-seat payment;
  (2) before September 28, 2026 — review and set the unified Copilot
  experience policy via Copilot settings → "Copilot cloud agent (coming
  soon)," understanding that declining the unified experience means losing
  Copilot access on github.com and GitHub Mobile entirely, with no partial
  opt-out; (3) before September 28, 2026 — decide on and explicitly configure
  a code review effort-level default rather than leaving it at "Default."
  Also flag the chat-data-retention change (28 days → life of account) as a
  compliance/data-handling fact that any team with an internal or
  customer-facing data-retention statement referencing Copilot chat needs to
  update once the unified experience ships.

- **Chapter 01 (Daily Workflows)**: Note that practitioners requesting Copilot
  code review on a repository or organization that has not explicitly
  configured an effort level will, starting September 28, 2026, receive
  Balanced-depth reviews by default instead of Lite — reviews may take longer
  and consume more AI credits/Actions minutes than practitioners are used to,
  with no code or workflow change on the practitioner's part.

## Extraction Notes

1. **WebFetch summarization avoided for quotes**: An initial WebFetch call
   against the changelog URL returned an AI-paraphrased summary with
   reconstructed quotation marks around content (e.g., it paraphrased the
   28-day retention sentence and the upfront-payment sentence in shortened
   form). All quotes used in this note were instead sourced from a direct
   `curl` fetch of the raw changelog HTML (after following a 301 redirect to
   the canonical URL), with HTML tags stripped and entities unescaped
   programmatically, then verified character-for-character against the raw
   text before inclusion.

2. **No sub-pages followed**: The changelog's only outbound content links are
   to "Copilot Quick Start documentation" and "Copilot code review
   documentation," both referenced only as pointers for further reading
   rather than as sources of additional claims needed to support this
   changelog's own statements (unlike, for example,
   `docs-github-copilot-code-review-effort-levels-ga.md`, which needed a
   linked docs page to support several of its claims). Given that this
   changelog is self-contained and states all three changes' mechanics
   directly, no linked pages were fetched for this extraction.

3. **"No earlier than" date treated as a floor, not a commitment**: The
   unified-experience section's date ("No earlier than September 28th,
   2026") is qualitatively different from the code review section's date
   ("starting September 28th, 2026") and the billing section's date
   ("starting October 1, 2026"), both of which are stated as firm. This
   note preserves that distinction throughout (see Claim 6's Our assessment)
   rather than treating all three dates as equally committed.

4. **Ambiguity in Claim 9 flagged, not resolved**: The "Stay opted in"
   subsection names only "Copilot on github.com and GitHub Mobile" as what
   is lost by opting out of the unified experience; it does not explicitly
   state whether opting out also removes Copilot cloud agent access, even
   though cloud agent is one of the three converging surfaces. This note
   flags the ambiguity in Claim 9's Our assessment rather than guessing at
   an answer the source does not provide.

5. **No contradictions filed**: This changelog's most consequential claims
   (prior 28-day chat retention, prior signup-pause state implied for
   Business/Enterprise credit-card/PayPal customers, "Default" as a
   third effort-level state) are all revealed for the first time by this
   source rather than conflicting with any existing corpus claim about the
   prior state. See Cross-References → Contradicts above.
