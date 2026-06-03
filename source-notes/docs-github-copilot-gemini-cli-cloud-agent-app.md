---
source_url: https://github.blog/changelog/2026-06-02-gemini-models-in-copilot-cli-cloud-agent-and-the-copilot-app
source_type: docs
title: "Gemini models in Copilot CLI, cloud agent, and the Copilot app"
author: GitHub (official changelog)
date_published: 2026-06-02
date_extracted: 2026-06-03
last_checked: 2026-06-03
status: current
confidence_overall: settled
issue: "#1035"
---

# Gemini Models in Copilot CLI, Cloud Agent, and the Copilot App

> GitHub's June 2, 2026 changelog announcing Gemini 3.1 Pro (Preview) and Gemini 3.5 Flash
> across four Copilot developer surfaces — CLI, cloud agent, the Copilot app, and the SDK —
> reversing the corpus characterization (from the May 20 web model consolidation note) that
> Gemini was "never in CLI or agent surfaces," and revealing a deliberate surface-segmented
> Gemini strategy: removed from web, added to developer-facing surfaces.

## Source Context

- **Type**: docs (GitHub official product changelog, ~150 words of primary announcement text;
  June 2, 2026)
- **Author credibility**: GitHub engineering team announcing a production feature change.
  Authoritative for: model names, plan-tier availability, admin opt-in requirement, and which
  surfaces are affected. Not authoritative for: comparative capability of Gemini vs. Claude or
  OpenAI alternatives on the same surfaces, whether this is a permanent or trial expansion, or
  the cost multipliers for these Gemini models.
- **Scope**: The addition of Gemini 3.1 Pro (Preview) and Gemini 3.5 Flash to Copilot CLI,
  cloud agent, the Copilot app (technical preview), and the Copilot SDK. Does NOT cover: how
  these Gemini models compare in performance to Claude Sonnet/Haiku or GPT-5.4 in the same
  surfaces, whether Gemini models are available in VS Code Copilot, the full model selection
  UI in each surface, or any pricing/multiplier guidance.

## Extracted Claims

### Claim 1: Gemini 3.1 Pro (Preview) and Gemini 3.5 Flash are now available in Copilot CLI, cloud agent, the Copilot app, and the Copilot SDK

- **Evidence**: Official GitHub product changelog announcing availability as a completed
  action — the phrasing "can now be used in" indicates this is an already-implemented change.
- **Confidence**: settled (product fact stated in official changelog as current)
- **Quote**: "Gemini 3.1 Pro (Preview) and Gemini 3.5 Flash can now be used in" Copilot CLI,
  cloud agent, the Copilot app, and the Copilot SDK
- **Our assessment**: This is the core claim. All four surfaces (CLI, cloud agent, app, SDK)
  are developer-facing rather than browser-facing web chat — distinguishing this expansion
  from the web surface that removed Gemini on May 20. For Ch02: practitioners who use the
  CLI or cloud agent as their primary Copilot surface now have access to Google's Gemini
  model family alongside the existing Claude and OpenAI options. The inclusion of the Copilot
  SDK is notable: it extends Gemini access to programmatic workflows, not just interactive
  ones. VS Code Copilot is conspicuously absent from the listed surfaces — its Gemini status
  is undocumented by this announcement.

### Claim 2: Plan-tier availability differs between the two Gemini models, with Gemini 3.5 Flash excluded from Copilot Student

- **Evidence**: The changelog explicitly lists subscription tiers for each model. Gemini 3.1
  Pro (Preview) is available to Student, Pro, Pro+, Business, and Enterprise; Gemini 3.5
  Flash is available to Pro, Pro+, Business, and Enterprise — omitting Student.
- **Confidence**: settled (tier availability stated in official changelog)
- **Quote**: (no direct quote for the tier table; see Concrete Artifacts for full tier mapping)
- **Our assessment**: The asymmetry is counterintuitive: the more capable model (Gemini 3.1
  Pro Preview) is available to Student, while the faster/cheaper Flash variant is not. If cost
  were the driver for the Student exclusion, Flash (cheaper) should be the included one, not
  the excluded. This may reflect a feature showcase strategy (GitHub highlights 3.1 Pro as the
  strategic Gemini model), a licensing constraint, or a rollout order that will be corrected.
  For Ch04 (model selection): practitioners on Student plans have one Gemini option (3.1 Pro
  Preview), not two.

### Claim 3: Copilot Business and Enterprise organizations require administrator opt-in before Gemini models become available

- **Evidence**: The changelog states an explicit admin policy requirement for organizational
  deployments, framing this as a policy the admin must enable, not a default-on expansion.
- **Confidence**: settled (stated in official changelog as a requirement)
- **Quote**: "Copilot Business and Enterprise administrators must opt in by enabling the
  relevant Gemini model policy in Copilot settings."
- **Our assessment**: This contrasts with the evaluation models announcement (June 1, #1027,
  Claim 2), which was opt-out (users receive evaluation models by default unless they disable
  them). Here, organizational Gemini access is opt-in — admins must actively enable it.
  Practitioners on Business/Enterprise plans who read this announcement and expect immediate
  Gemini availability will find it unavailable until their admin acts. For Ch05 (enterprise
  governance): admins must be aware that this requires an explicit "Gemini model policy"
  action in Copilot settings — it is not inherited from any prior multi-provider policy.

### Claim 4: The Copilot app availability of Gemini models is designated as technical preview

- **Evidence**: The WebFetch summary of the source explicitly noted "GitHub Copilot app
  (technical preview)" as the availability status for that surface, indicating a staged
  rather than fully-GA rollout.
- **Confidence**: settled (noted in source summary; see Extraction Notes for caveat)
- **Quote**: (no character-for-character quote isolated; Assayer should verify "technical
  preview" wording directly against the source URL)
- **Our assessment**: The technical preview label signals that Gemini integration in the
  Copilot app is not fully hardened. Practitioners using the Copilot app should understand
  that Gemini availability there may have rough edges, change, or carry different stability
  guarantees vs. the CLI and cloud agent surfaces. For Ch02: document the Copilot app surface
  as technical preview when citing Gemini availability in that specific surface.

### Claim 5: The Copilot SDK is now a Gemini-accessible surface, enabling programmatic Gemini-powered Copilot workflows

- **Evidence**: The SDK is explicitly listed as one of the four surfaces receiving Gemini
  access in this announcement — alongside CLI, cloud agent, and the Copilot app.
- **Confidence**: settled (SDK listed as a surface in official changelog; see Claim 1 quote)
- **Quote**: (no direct quote isolated for SDK specifically; see Claim 1 quote covering the
  combined surface list)
- **Our assessment**: SDK access is the most developer-enabling capability in this
  announcement. CLI and cloud agent access is primarily interactive or workflow-driven; SDK
  access means developers can programmatically invoke Gemini models through the Copilot
  abstraction layer — potentially enabling Gemini as a model option in custom tooling built
  on the Copilot SDK. For Ch02 (harness engineering): teams using the Copilot SDK for
  automation or custom tooling should check whether their SDK version surfaces Gemini as a
  selectable model, and whether the admin policy (Claim 3) gates SDK access the same way it
  gates interactive surface access.

### Claim 6: This expansion represents a deliberate surface-segmented Gemini strategy — removed from web (May 20), added to developer-facing surfaces (June 2)

- **Evidence**: Cross-referencing this source with `docs-github-copilot-web-model-consolidation.md`
  (May 20, 2026), which documented the removal of all Gemini models from Copilot Chat on the
  web. The 13-day gap and inverse movement (removal from web, addition to CLI/agent/app/SDK)
  suggests intentional surface differentiation rather than random sequencing.
- **Confidence**: emerging (the "deliberate strategy" framing is an inference; neither source
  explicitly states this as a strategic principle)
- **Quote**: (no direct quote; see Our assessment)
- **Our assessment**: If the emerging framing is correct, GitHub is positioning web Copilot
  chat as a two-provider (OpenAI + Anthropic) reliability-optimized surface, while routing
  Gemini availability to developer-facing programmatic surfaces (CLI, cloud agent, app, SDK).
  The web consolidation source's forward commitment to "a more limited set of new model
  rollouts" is consistent with the web becoming the narrow-but-reliable surface, while
  CLI/agent/SDK absorb the expanding model variety. For Ch02 and Ch04: practitioners choosing
  between web and non-web Copilot surfaces should now understand that the model menu differs
  deliberately — not accidentally — across surfaces. This is a continuation of the
  surface-specific policy principle established in the May 20 note, but with the model
  geography now reversed for Gemini.

## Concrete Artifacts

### Announcement Summary and Tier Table (June 2, 2026)

```
Title:   Gemini models in Copilot CLI, cloud agent, and the Copilot app
Date:    June 2, 2026
Source:  https://github.blog/changelog/2026-06-02-gemini-models-in-copilot-cli-cloud-agent-and-the-copilot-app

Key quote: "Gemini 3.1 Pro (Preview) and Gemini 3.5 Flash can now be used in"
           Copilot CLI, cloud agent, the Copilot app, and the Copilot SDK.

Admin requirement (Business/Enterprise):
  "Copilot Business and Enterprise administrators must opt in by enabling the
   relevant Gemini model policy in Copilot settings."

MODEL AVAILABILITY BY PLAN TIER:

Model                     Student   Pro   Pro+   Business   Enterprise
───────────────────────────────────────────────────────────────────────
Gemini 3.1 Pro (Preview)    YES     YES    YES    YES*        YES*
Gemini 3.5 Flash             NO     YES    YES    YES*        YES*

* = requires admin opt-in via "Gemini model policy" in Copilot settings

SURFACES AFFECTED (as of June 2, 2026):
  Copilot CLI                    — available
  Copilot cloud agent            — available
  GitHub Copilot app             — available (technical preview)
  Copilot SDK                    — available

SURFACES NOT AFFECTED:
  Copilot Chat on the web        — Gemini removed May 20, 2026 (not re-added)
  VS Code Copilot                — not mentioned in this announcement
```

### Cross-Surface Gemini Model Availability (synthesized, as of June 2, 2026)

```
Surface                 Gemini 3.1 Pro (Preview)   Gemini 3.5 Flash
─────────────────────────────────────────────────────────────────────
Web chat (github.com)   REMOVED (May 20, 2026)     REMOVED (May 20, 2026)
Copilot CLI             ✓ (June 2, 2026)            ✓ (June 2, 2026)†
Copilot cloud agent     ✓ (June 2, 2026)            ✓ (June 2, 2026)†
Copilot app             ✓ technical preview          ✓ technical preview†
Copilot SDK             ✓ (June 2, 2026)            ✓ (June 2, 2026)†
VS Code Copilot         not documented              not documented

† = Not available to Student plan tier
  Business/Enterprise: requires admin opt-in via Gemini model policy
  Student/Pro/Pro+: available by default (individual plan access)
```

## Cross-References

- **Contradicts** `docs-github-copilot-web-model-consolidation.md` Claim 7: That May 20 note
  stated "The fact that Gemini was in web chat but never in CLI or agent surfaces confirms
  surface-specific policies." The June 2 source directly supersedes the factual predicate —
  Gemini IS now in CLI, cloud agent, app, and SDK. The broader conclusion of Claim 7 (that
  surface-specific model policies exist) remains valid, but the specific "never in CLI or
  agent" statement is no longer accurate as guide advice. **Contradiction issue filed: #1042.**

- **Corroborates** `docs-github-copilot-cca-cost-efficient-models.md` Claim 5: That May 18
  note mentioned "Gemini 3.5 Flash availability" as a concurrent changelog update occurring
  around the same time. This June 2 source is the dedicated, surface-explicit announcement
  of Gemini availability that the May 18 note foreshadowed as a separate item. The two-week
  gap between the concurrent mention (May 18) and this dedicated announcement (June 2) is
  consistent with Gemini models being in active rollout across surfaces during this period.

- **Extends** `docs-github-copilot-web-model-consolidation.md` Claims 4 and 6: The May 20
  note established that GitHub is managing the web surface with "a more limited set of new
  model rollouts" and explicitly committed to fewer web model additions going forward. This
  June 2 source is consistent with that web strategy — Gemini is NOT being added to the web
  surface. Instead, the multi-provider expansion is happening on developer-facing surfaces.
  Together, the two notes establish a two-tier model availability philosophy: web =
  curated/stable/two-provider; CLI/agent/SDK = broader/evolving/three-provider.

- **Complements** `docs-github-copilot-evaluation-models-individual-plans.md` Claim 3 (#1027):
  That June 1 note established that evaluation models are individual-user-facing and explicitly
  excluded from enterprise plans. This source shows a complementary pattern: Gemini models
  require admin opt-in for Business/Enterprise but are available by default for individual
  plan tiers (Student for 3.1 Pro, Pro and above for both). Two consecutive-day announcements
  (June 1 and June 2) reveal GitHub applying plan-differentiated access in complementary
  directions: individual users get evaluation model routing by default; organizational users
  get Gemini only after admin action.

- **Contradicts**: See Contradicts section above — contradiction issue #1042 filed for the
  conflict with `docs-github-copilot-web-model-consolidation.md` Claim 7.

- **Novel**:
  - **First corpus source documenting Gemini availability in Copilot CLI**: No prior source
    note documented Google Gemini models as selectable options in Copilot CLI. The May 20
    consolidation note explicitly stated (Claim 7 assessment) that Gemini was "never in CLI
    or agent surfaces" — this source is the first to document Gemini CLI availability.
  - **First corpus source documenting Gemini in Copilot cloud agent**: Same rationale — prior
    CCA notes established a three-tier model selection structure (Haiku/Sonnet/Opus) without
    Gemini; this source adds a fourth multi-provider dimension.
  - **First corpus source documenting the Copilot SDK as a surface with model selection
    relevance**: No prior note identified the Copilot SDK as a distinct surface with
    practitioner-relevant model availability information.
  - **Student plan inclusion for Gemini 3.1 Pro (Preview)**: No prior corpus source documented
    Student plan access to a Google Gemini model. The inclusion (with exclusion of Flash from
    Student) is novel plan-tier granularity for the Gemini model family.
  - **Surface-segmented Gemini strategy**: The combination of this source with the May 20 web
    removal source is the first corpus evidence for deliberate surface-differentiated model
    availability as a platform strategy — web contracts, developer surfaces expand.

## Guide Impact

- **Chapter 02 (Harness Engineering / Tooling Landscape)**: The May 20 consolidation note
  recommended documenting "Gemini not available in CLI/agent" as a practical knowledge item.
  This source reverses that: Gemini is now available in CLI and cloud agent. Update any guide
  content that states or implies Gemini is absent from developer-facing Copilot surfaces. Add:
  practitioners using Copilot CLI or cloud agent may now select Gemini 3.1 Pro (Preview) or
  Gemini 3.5 Flash. Document the admin opt-in requirement for Business/Enterprise. Note the
  technical preview status for the Copilot app surface. The cross-surface model availability
  picture should now list Gemini as available in CLI/agent/app/SDK (not web), with the
  surface-specific policy principle still intact but the specific Gemini geography changed.

- **Chapter 04 (Model Selection and Cost Management)**: Add Gemini 3.1 Pro (Preview) and
  Gemini 3.5 Flash as options in CLI and cloud agent model selection guidance. For CCA
  specifically, the model decision matrix (from `docs-github-copilot-cca-cost-efficient-models.md`)
  now includes a third provider alongside Claude and OpenAI. Note plan-tier availability:
  Student plans have Gemini 3.1 Pro only; Pro and above have both Gemini variants. No cost
  multipliers are provided in this announcement — practitioners cannot yet compare Gemini cost
  relative to Claude Haiku (0.33x) or GPT-5.4-mini (0.33x) from `docs-github-copilot-cca-cost-efficient-models.md`.

- **Chapter 05 (Team Adoption / Enterprise Governance)**: Document the Gemini admin opt-in
  requirement as an actionable governance item. Unlike Claude or OpenAI models (which appear
  available without explicit policy action for appropriate plan tiers), Gemini in Copilot
  requires an explicit "Gemini model policy" decision by Business/Enterprise admins. Teams
  implementing a model governance policy should add this as a configurable option in their
  Copilot settings review process.

## Extraction Notes

1. **WebFetch returns AI-processed summaries, not raw HTML**: Two independent WebFetch calls
   returned consistent information about models, surfaces, and tier availability. The quote
   in Claim 1 — "Gemini 3.1 Pro (Preview) and Gemini 3.5 Flash can now be used in" [Copilot
   CLI, cloud agent, the Copilot app, and the Copilot SDK] — and the quote in Claim 3 —
   "Copilot Business and Enterprise administrators must opt in by enabling the relevant Gemini
   model policy in Copilot settings." — appeared in the second WebFetch result enclosed in
   quotation marks. These are taken as near-verbatim, but the Assayer should verify
   character-for-character against the source URL.

2. **"Technical preview" label for Copilot app**: Surfaced in the first WebFetch result's
   structured summary ("GitHub Copilot app (technical preview)") but not as an isolated
   direct quote. The Assayer should verify that the Copilot app surface is described with a
   "technical preview" qualifier in the source.

3. **VS Code Copilot absent from the announcement**: The source lists four surfaces
   (CLI, cloud agent, app, SDK). VS Code is not mentioned. No claim is made about VS Code
   Gemini availability or absence — the announcement scope simply does not include it.

4. **No cost multipliers for Gemini models**: Neither Gemini 3.1 Pro (Preview) nor Gemini
   3.5 Flash is assigned a premium request multiplier in this announcement. The cost
   comparison relative to Claude Haiku (0.33x) or GPT-5.4-mini (0.33x) in CCA remains
   unknown from this source.

5. **Contradiction issue filed**: A contradiction issue (#1042) has been filed for the
   conflict between this source (Gemini now in CLI/agent) and `docs-github-copilot-web-model-consolidation.md`
   Claim 7 ("Gemini was in web chat but never in CLI or agent surfaces"). The recommended
   verdict is `superseded` — the May 20 statement was accurate as of that date, but the June
   2 expansion supersedes the "never in CLI/agent" predicate.

6. **Tier table source**: The plan-tier availability mapping (Student/Pro/Pro+/Business/Enterprise)
   was drawn from the WebFetch summary. The Assayer should verify these tier assignments
   against the source page, particularly the Student exclusion from Gemini 3.5 Flash.
