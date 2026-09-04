---
source_url: https://github.blog/changelog/2026-09-03-gemini-3-8-flash-is-now-available-in-github-copilot
source_type: docs
title: "Gemini 3.8 Flash is now available in GitHub Copilot"
author: GitHub (official changelog)
date_published: 2026-09-03
date_extracted: 2026-09-04
last_checked: 2026-09-04
status: current
confidence_overall: settled
issue: "#3223"
---

# Gemini 3.8 Flash Is Now Available in GitHub Copilot

> GitHub's September 3, 2026 changelog adds Gemini 3.8 Flash to eight Copilot
> surfaces under introductory usage-based pricing through December 31, 2026 —
> the first standalone "now available" Copilot changelog for a Gemini Flash
> point release since Gemini 3.5 Flash's June 2 debut (Gemini 3.6 Flash and
> Gemini 3.7 Flash never received their own dedicated Copilot availability
> notice; both surfaced in the corpus only as shifting "suggested alternative"
> names in the Gemini 3.1 Pro deprecation tables) — and the first concrete,
> named-model instance of the "enabled automatically unless disabled" default
> that `docs-github-copilot-global-model-policy-ga.md` documented going into
> enforcement on the Business/Enterprise tier just days earlier.

## Source Context

- **Type**: docs (GitHub official product changelog, September 3, 2026; ~110
  words of primary announcement text across four short sections —
  "Availability in GitHub Copilot," "Enabling access," "Learn more," "Share
  your feedback" — "1 minute read"; confirmed via direct raw-HTML fetch with
  `curl`, not just a WebFetch AI summary)
- **Author credibility**: GitHub engineering/product team announcing a
  production feature addition. Authoritative for: the model's Copilot debut
  date, the eight surfaces where it is selectable, the five eligible plan
  tiers, the pricing window, and the admin-policy default behavior. Not a
  source for: Gemini 3.8 Flash's original release date or model card from
  Google (this changelog documents only its arrival inside Copilot, not
  whether or when Google shipped it independently), capability benchmarks
  beyond the single early-testing sentence quoted below, or cost multipliers
  relative to other Copilot models.
- **Scope**: Covers Gemini 3.8 Flash's addition to the Copilot model picker
  across eight named surfaces, its plan-tier eligibility, its introductory
  pricing window, and the standard Business/Enterprise admin-policy control.
  Does NOT cover: any relationship to Gemini 3.1 Pro's ongoing deprecation
  and shifting successor designation (Gemini 3.6 Flash → Gemini 3.7 Flash,
  per `docs-github-copilot-selected-models-deprecated-sept2026.md` and
  contradiction #3170) — this notice makes no reference to that deprecation
  event, to Gemini 3.1 Pro, or to any other Gemini model by name — nor does
  it cover rate limits, premium-request multipliers, or a technical-preview
  qualifier for any surface (unlike the June 2 Gemini rollout, which flagged
  the Copilot app as technical preview).

## Extracted Claims

### Claim 1: Gemini 3.8 Flash is now selectable in the Copilot model picker across eight named surfaces: Visual Studio Code, Visual Studio, Copilot CLI, GitHub Copilot cloud agent, GitHub Copilot app, JetBrains IDEs, Xcode, and Eclipse

- **Evidence**: Official GitHub Copilot changelog, "Availability in GitHub
  Copilot" section, extracted from raw page HTML.
- **Confidence**: settled (product fact stated directly and enumerated as a
  list in the official changelog)
- **Quote**: "Gemini 3.8 Flash, Google's latest Flash model, is now available
  in GitHub Copilot." / "You'll be able to select the model in the model
  picker in: Visual Studio Code, Visual Studio, Copilot CLI, GitHub Copilot
  cloud agent, GitHub Copilot app, JetBrains IDEs, Xcode, Eclipse"
- **Our assessment**: This is the broadest single-notice surface list for a
  Gemini model documented anywhere in the corpus so far. The June 2, 2026
  rollout (`docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 1) named
  four surfaces for Gemini 3.1 Pro/3.5 Flash — CLI, cloud agent, app, SDK —
  and explicitly excluded VS Code and JetBrains as "not mentioned." This
  notice adds VS Code, Visual Studio, JetBrains IDEs, Xcode, and Eclipse,
  while dropping the Copilot SDK from the named list entirely (the SDK is
  neither confirmed nor denied here — simply absent). For Ch02: the guide's
  cross-surface Gemini availability table should be updated to show Gemini
  3.8 Flash as the first Gemini variant with IDE-level (not just
  developer-surface) presence across this many editors simultaneously.

### Claim 2: In GitHub's early testing, Gemini 3.8 Flash performed strongly on complex terminal-based coding tasks and showed rigorous validation and persistent recovery from actionable failures

- **Evidence**: Official changelog body text, single evaluative sentence,
  extracted from raw page HTML.
- **Confidence**: anecdotal (a first-party vendor characterization with no
  benchmark, dataset, or methodology named — "early testing" is not further
  specified)
- **Quote**: "In our early testing, Gemini 3.8 Flash performed strongly on
  complex terminal-based coding tasks and demonstrated rigorous validation
  and persistent recovery from actionable failures."
- **Our assessment**: This is GitHub's own marketing characterization, not an
  independent benchmark — no score, dataset, or comparison model is named,
  unlike the corpus's independent third-party benchmark coverage of Gemini
  3.7 Flash (`blog-latentspace-ainews-gemini37-flash-gdm.md` Claims 2-4,
  DeepSWE V1.1 chart data). "Terminal-based coding tasks" and "recovery from
  actionable failures" are notable as specific capability claims (agentic,
  not just single-turn code generation), consistent with Copilot CLI and
  cloud agent being two of the eight listed surfaces. Practitioners should
  treat this as an unverified vendor claim until an independent benchmark
  source (in the style of the AINews/DeepSWE coverage of 3.7 Flash) becomes
  available for 3.8 Flash specifically.

### Claim 3: Gemini 3.8 Flash is billed at introductory provider pricing under usage-based billing through December 31, 2026

- **Evidence**: Official changelog body text, extracted from raw page HTML.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "This model is billed at introductory provider pricing under
  usage-based billing through December 31, 2026. See pricing for GitHub
  Copilot models and requests for details."
- **Our assessment**: The notice does not state the actual price or a
  specific premium-request multiplier (unlike `docs-github-copilot-cca-cost-efficient-models.md`,
  which assigns Claude Haiku and GPT-5.4-mini explicit 0.33x multipliers) —
  it only names an end date for whatever "introductory" rate applies. This
  is a four-month window (September 3 to December 31, 2026) after which
  pricing presumably changes to a non-introductory rate not disclosed here.
  For Ch04: flag Gemini 3.8 Flash's cost as unknown/introductory-rate rather
  than assuming parity with Gemini 3.5/3.6/3.7 Flash's costs documented
  elsewhere in the corpus (e.g., `blog-simonwillison-muse-code-spark-12.md`'s
  $1.50/$7.50 per-million-token figure for Gemini 3.6 Flash), since none of
  those figures are confirmed to apply to 3.8 Flash inside Copilot.

### Claim 4: Gemini 3.8 Flash is available to Copilot Pro, Pro+, Max, Business, and Enterprise subscribers — with no Free or Student tier named

- **Evidence**: Official changelog, "Availability in GitHub Copilot" section
  opening sentence, extracted from raw page HTML.
- **Confidence**: settled (plan tiers stated directly and exhaustively as a
  list)
- **Quote**: "Gemini 3.8 Flash will be available to Copilot Pro, Pro+, Max,
  Business, and Enterprise users."
- **Our assessment**: This continues the pattern first observed in
  `docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 2, where Gemini
  3.5 Flash was excluded from the Student tier while Gemini 3.1 Pro
  (Preview) was included — Flash-tier Gemini models have now twice launched
  in Copilot without Student or Free access, while at least one non-Flash
  Gemini model (3.1 Pro) once shipped with Student inclusion. No Free tier
  is named for any Gemini variant in either announcement. "Max" is an
  already-documented Copilot plan tier in the corpus (see
  `docs-github-copilot-cca-fix-failing-actions-pro-max.md`), not a new tier
  introduced by this source.

### Claim 5: The rollout across the eight listed surfaces is gradual, and users who do not yet see the model should check back later

- **Evidence**: Official changelog, closing sentence of the "Availability in
  GitHub Copilot" section, extracted from raw page HTML.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Rollout will be gradual. Check back soon if you don't see it
  yet."
- **Our assessment**: This is a standard staggered-rollout disclaimer,
  functionally similar to the enterprise-by-enterprise staggered enforcement
  window documented for the global model policy
  (`docs-github-copilot-global-model-policy-ga.md` Claim 1: "it will take
  effect at different times for different enterprises"). Practitioners on an
  eligible plan who do not see Gemini 3.8 Flash in their picker on September
  3 should not assume ineligibility or a configuration error before this
  gradual rollout has had time to reach their account.

### Claim 6: Business and Enterprise administrators manage Gemini 3.8 Flash access through the Copilot model policy, and new models are enabled automatically unless an administrator has turned off the global default or explicitly disabled this specific model

- **Evidence**: Official changelog, "Enabling access" section, extracted
  from raw page HTML.
- **Confidence**: settled (stated directly in official changelog; the
  broader default-enablement mechanism it describes is independently
  corroborated by `docs-github-copilot-global-model-policy-ga.md`, fetched
  and verified in a separate prior source note)
- **Quote**: "Copilot Enterprise and Copilot Business plan administrators can
  manage access to Gemini 3.8 Flash through the model policy in Copilot
  settings. Under default model enablement, new models are enabled
  automatically unless an administrator has turned off the global default or
  explicitly disables this model."
- **Our assessment**: This is the first corpus source to name a specific new
  model as a live instance of the global default-enablement policy that
  `docs-github-copilot-global-model-policy-ga.md` documented reaching full
  enforcement (through September 1, 2026) just two days before this
  changelog. That prior note's Claim 2 ("Models you haven't previously
  configured will change their state to 'Delegate to default policy'... If
  your policy is enabled — which is the default — those models will become
  available to your users") and Claim 10 ("New models are announced on
  GitHub's changelog") predicted exactly this behavior for future model
  announcements; this is the first changelog entry in the corpus published
  after that enforcement date, and it matches the predicted default-on
  behavior precisely. This is materially different admin-default language
  from the June 2, 2026 Gemini rollout's opt-in framing
  (`docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 3: "Copilot
  Business and Enterprise administrators must opt in by enabling the
  relevant Gemini model policy in Copilot settings") — but that difference
  reflects the global policy's intervening rollout (announced July 2026, GA
  and enforced August 26-September 1, 2026), not a factual conflict between
  two sources describing the same point in time. No contradiction issue is
  filed; per MINER.md §4a this is superseding product evolution, the same
  treatment `docs-github-copilot-global-model-policy-ga.md` itself gave the
  two-state-to-four-state taxonomy shift. For Ch05: enterprise admins who
  have not reviewed their global default-enablement policy setting (or who
  assume Gemini models still require the June 2-era manual opt-in) should be
  told that, as of September 2026, a new Gemini model is likely to appear
  automatically for their users unless they have disabled the global
  default or this specific model.

### Claim 7: This is the first standalone "now available" Copilot changelog entry for a Gemini Flash point release since Gemini 3.5 Flash on June 2, 2026 — Gemini 3.6 Flash and Gemini 3.7 Flash never received a dedicated Copilot availability notice of their own

- **Evidence**: Cross-referencing this source against the full set of
  Gemini-related `docs-github-copilot-*` notes in the corpus:
  `docs-github-copilot-gemini-cli-cloud-agent-app.md` (June 2, 2026 — 3.1 Pro
  and 3.5 Flash), `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`
  (July 2, 2026 — deprecates 2.5 Pro/3 Flash, names 3.1 Pro/3.5 Flash as
  successors), `docs-github-copilot-aug2026-model-deprecations.md` (July 31,
  2026 — deprecates 3.1 Pro, names Gemini 3.6 Flash as its successor), and
  `docs-github-copilot-selected-models-deprecated-sept2026.md` (August 31,
  2026 — same deprecation event confirmed, successor revised to Gemini 3.7
  Flash, filed as contradiction #3170). None of these four prior notices is
  a dedicated "Gemini 3.6/3.7 Flash is now available" changelog; 3.6 Flash
  and 3.7 Flash appear in the corpus's Copilot-specific notes only as
  successor-column entries in deprecation tables.
- **Confidence**: emerging (the "first standalone availability notice since
  3.5 Flash" framing is a corpus-completeness observation across five
  sources, not a claim this changelog itself makes)
- **Quote**: (no direct quote; corpus cross-reference finding)
- **Our assessment**: Gemini 3.6 Flash and Gemini 3.7 Flash both reached
  real-world availability outside Copilot in the corpus — 3.6 Flash as a
  production fallback model in `blog-google-agents-challenge-engineering-patterns.md`
  and priced in `blog-simonwillison-muse-code-spark-12.md`; 3.7 Flash with
  its own GA launch and pelican-benchmark writeup in
  `blog-simonwillison-llm-gemini-033.md` (August 13, 2026) — but neither one
  was ever separately confirmed as *added to Copilot's model picker* the way
  this notice confirms for 3.8 Flash and the June 2 notice confirmed for 3.5
  Flash. This leaves an open question the source does not resolve: whether
  Gemini 3.6 Flash and 3.7 Flash were ever actually selectable inside
  Copilot at all (as opposed to only being named as deprecation-table
  successors for a model, Gemini 3.1 Pro, that was itself a different model
  from either Flash variant), or whether Copilot's Flash-tier Gemini
  offering jumped directly from 3.5 Flash to 3.8 Flash. Practitioners
  relying on the corpus for a complete Gemini-in-Copilot timeline should
  treat 3.6 Flash and 3.7 Flash's Copilot-specific availability as
  unconfirmed, distinct from their confirmed availability via other tools
  (llm-gemini, third-party API access).

### Claim 8: This notice makes no reference to Gemini 3.1 Pro, its September 1, 2026 deprecation, or any successor-naming history for that deprecation event

- **Evidence**: Full-text review of the changelog body (Concrete Artifacts
  below); no mention of "3.1 Pro," "deprecat," "retired," or any successor
  terminology appears anywhere on the page.
- **Confidence**: settled (a directly observable absence in the source text
  itself)
- **Quote**: (no quote; this claim documents an absence)
- **Our assessment**: Given that Gemini 3.1 Pro's deprecation notice named
  Gemini 3.6 Flash, then Gemini 3.7 Flash, as its "suggested alternative"
  across two successive changelog entries (contradiction #3170), a reader
  might expect Gemini 3.8 Flash's arrival to explicitly supersede one of
  those successor designations. It does not — this changelog presents 3.8
  Flash as a new, independent addition to the model roster, not as a
  revision to the Gemini 3.1 Pro migration guidance. The guide should not
  infer that Gemini 3.8 Flash is now "the" replacement for Gemini 3.1 Pro;
  that would be a synthesis beyond what either source states. If a future
  GitHub source updates the Gemini 3.1 Pro successor designation a third
  time (from 3.7 Flash to 3.8 Flash or otherwise), that would extend
  contradiction #3170's pattern, but this notice does not itself do so.

## Concrete Artifacts

### Full Article Text (verbatim, extracted from raw page HTML via direct curl fetch)

```
Gemini 3.8 Flash is now available in GitHub Copilot

Release: September 3, 2026 (1 minute read)

Gemini 3.8 Flash, Google's latest Flash model, is now available in GitHub
Copilot.

In our early testing, Gemini 3.8 Flash performed strongly on complex
terminal-based coding tasks and demonstrated rigorous validation and
persistent recovery from actionable failures.

This model is billed at introductory provider pricing under usage-based
billing through December 31, 2026. See pricing for GitHub Copilot models and
requests for details.

Availability in GitHub Copilot
Gemini 3.8 Flash will be available to Copilot Pro, Pro+, Max, Business, and
Enterprise users.

You'll be able to select the model in the model picker in:
- Visual Studio Code
- Visual Studio
- Copilot CLI
- GitHub Copilot cloud agent
- GitHub Copilot app
- JetBrains IDEs
- Xcode
- Eclipse

Rollout will be gradual. Check back soon if you don't see it yet.

Enabling access
Copilot Enterprise and Copilot Business plan administrators can manage
access to Gemini 3.8 Flash through the model policy in Copilot settings.
Under default model enablement, new models are enabled automatically unless
an administrator has turned off the global default or explicitly disables
this model.

Learn more
To explore all models available in GitHub Copilot, see our documentation on
models and get started with Copilot.

Share your feedback
Join the GitHub Community to share your feedback.
```

*Source: raw HTML of
https://github.blog/changelog/2026-09-03-gemini-3-8-flash-is-now-available-in-github-copilot,
fetched directly via `curl` (not WebFetch summarization alone) on
2026-09-04. Page category tag: "Release." Published: September 3, 2026.
Read time: "1 minute read." Two independent WebFetch AI-summary passes were
also run before the raw-HTML fetch and returned two different wordings for
the early-testing quote in Claim 2 (one truncated, one with an extra
clause), confirming the AI-summarization risk already flagged in prior
notes in this family — the raw-HTML text above is the character-verified
version used for all quotes in this note.*

### Gemini-in-Copilot Timeline (derived from five corpus sources)

```
Date          Event                                          Source
------------  ---------------------------------------------  --------------------------------------------------------
2026-06-02    Gemini 3.1 Pro (Preview) + 3.5 Flash added to   docs-github-copilot-gemini-cli-cloud-agent-app.md
              CLI, cloud agent, app, SDK
2026-07-02    Gemini 2.5 Pro + Gemini 3 Flash deprecated;     docs-github-copilot-gemini25pro-gemini3flash-deprecation.md
              successors: 3.1 Pro, 3.5 Flash
2026-07-31    Gemini 3.1 Pro deprecated (effective 9-1-26);   docs-github-copilot-aug2026-model-deprecations.md
              successor named: Gemini 3.6 Flash
2026-08-31    Same deprecation confirmed effective 9-1-26;    docs-github-copilot-selected-models-deprecated-sept2026.md
              successor revised: Gemini 3.7 Flash
              (contradiction #3170 vs. the 7-31 successor name)
2026-09-03    Gemini 3.8 Flash added to VS Code, Visual       THIS NOTE
              Studio, CLI, cloud agent, app, JetBrains,
              Xcode, Eclipse — no reference to 3.1 Pro's
              deprecation or either prior successor name

Open question (Claim 7): whether Gemini 3.6 Flash or Gemini 3.7 Flash was
ever independently confirmed as selectable in Copilot's own model picker,
as opposed to only appearing as a deprecation-table successor name.
```

## Cross-References

- **Corroborates** `docs-github-copilot-global-model-policy-ga.md` Claims 2
  and 10: that source predicted new GA models would default to enabled
  ("Delegate to default policy," on unless disabled) once the global policy
  reached full enforcement (through September 1, 2026), and separately
  stated GitHub's recommendation to track new-model announcements via the
  changelog. This is the first corpus changelog published after that
  enforcement window to describe a specific model's admin-default behavior,
  and it matches the predicted "enabled unless disabled" framing exactly.

- **Extends** `docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 1
  (Gemini's June 2, 2026 four-surface Copilot debut: CLI, cloud agent, app,
  SDK): this source expands the surface count to eight, adding VS Code,
  Visual Studio, JetBrains IDEs, Xcode, and Eclipse, while the Copilot SDK
  is absent from this notice's list.

- **Extends** `docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 2
  (Gemini 3.5 Flash excluded from the Student tier at its June 2, 2026
  debut): this source shows the same Free/Student exclusion pattern
  repeating for Gemini 3.8 Flash, now also excluding Free explicitly by
  omission from a five-tier list that includes the previously-undocumented-for-Gemini
  "Max" tier.

- **Extends** `docs-github-copilot-selected-models-deprecated-sept2026.md`
  Claim 4 and `docs-github-copilot-aug2026-model-deprecations.md` Claim 1
  (Gemini 3.1 Pro's successor renamed from Gemini 3.6 Flash to Gemini 3.7
  Flash between pre-announcement and confirmation, contradiction #3170):
  this source adds a third Gemini Flash point-release name (3.8) to the
  same rapid-succession pattern, though — per Claim 8 — without explicitly
  connecting it to that deprecation event or either prior successor name.

- **Extends** `blog-simonwillison-llm-gemini-033.md` (Gemini 3.7 Flash's
  independent GA launch and llm-gemini plugin support, August 13, 2026) and
  `blog-latentspace-ainews-gemini37-flash-gdm.md` (third-party benchmark
  coverage of the same 3.7 Flash launch): both establish Gemini 3.7 Flash
  reached general availability and independent benchmarking three weeks
  before this notice's Gemini 3.8 Flash debut in Copilot — consistent with
  Google's Flash-tier release cadence outpacing GitHub's Copilot integration
  announcements, though this source does not itself state Gemini 3.8
  Flash's original (non-Copilot) release date.

- **Contradicts**: None identified. The admin-default language difference
  from `docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 3 (see
  Claim 6's Our assessment) is resolved as product evolution via the
  intervening global model policy GA
  (`docs-github-copilot-global-model-policy-ga.md`), not a factual conflict
  between two sources describing the same point in time — no contradiction
  issue filed, per MINER.md §4a's "when NOT to file" guidance.

- **Novel**:
  - First corpus mention of "Gemini 3.8 Flash" in any source, Copilot-related
    or otherwise — no prior source note documents this specific model
    version.
  - First Gemini Copilot rollout notice to list eight surfaces in a single
    announcement, and the first to include VS Code, Visual Studio,
    JetBrains IDEs, Xcode, and Eclipse for any Gemini model.
  - First concrete, named-model confirmation in the corpus of the global
    default-enablement policy (`docs-github-copilot-global-model-policy-ga.md`)
    actually applying to a newly announced model after that policy's
    enforcement date.
  - First Copilot changelog to use the category tag "Release" for a Gemini
    model addition, as distinct from the "Retired" tag used across every
    deprecation notice in the Gemini/Claude/GPT deprecation family
    (`docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 7).

## Guide Impact

- **Chapter 02 (Harness Engineering / Tooling Landscape)**: Add Gemini 3.8
  Flash to the guide's Copilot model roster as newly available (September 3,
  2026) across VS Code, Visual Studio, Copilot CLI, cloud agent, Copilot
  app, JetBrains IDEs, Xcode, and Eclipse — the broadest single-notice
  surface list documented for any Gemini variant so far. Note the open
  question (Claim 7) about whether Gemini 3.6 Flash and 3.7 Flash were ever
  independently confirmed inside Copilot's picker, so the guide does not
  overstate a complete point-release history for Gemini Flash inside
  Copilot specifically.

- **Chapter 04 (Model Selection and Cost Management)**: Record Gemini 3.8
  Flash's plan-tier eligibility (Pro, Pro+, Max, Business, Enterprise — no
  Free/Student) and flag its cost as unknown/introductory-rate through
  December 31, 2026, per Claim 3. Do not carry over Gemini 3.5/3.6/3.7
  Flash's documented per-token prices from other corpus sources as an
  assumed price for 3.8 Flash inside Copilot — this source states only a
  pricing *window*, not a rate.

- **Chapter 05 (Team Adoption / Enterprise Governance)**: Use this notice as
  a concrete example for governance documentation of the global
  default-enablement policy in practice: an admin who has left the global
  policy enabled, and has not explicitly disabled Gemini 3.8 Flash, will see
  it become available to Business/Enterprise users automatically, without
  the opt-in action that earlier Gemini rollouts required. Governance
  checklists built around the pre-August-2026 "Gemini requires opt-in"
  assumption (from `docs-github-copilot-gemini-cli-cloud-agent-app.md`
  Claim 3) should be updated to reflect the new default-on posture unless
  the enterprise has disabled the global policy.

## Extraction Notes

1. **WebFetch AI-summarization risk confirmed again**: Two independent
   WebFetch calls to this changelog returned two different paraphrases of
   the same early-testing sentence (one omitting "and demonstrated rigorous
   validation and persistent recovery from actionable failures," the other
   including it with slightly different wording). The page's raw HTML was
   then fetched directly via `curl` and the article body extracted
   programmatically; all quotes in this note are taken from that raw-HTML
   extraction, verified character-for-character against the live page on
   2026-09-04, not from either WebFetch summary.
2. **No sub-pages followed beyond the source page itself**: The changelog
   links to a general "documentation on models" page and a "get started
   with Copilot" page, both general-purpose references already covered by
   prior corpus notes (e.g., `docs-github-copilot-aug2026-model-deprecations.md`
   Extraction Notes item 2, which fetched the equivalent supported-models
   page and found nothing specific to extract beyond the general current
   roster). Per MINER.md §1's "up to 5 substantive linked pages" guidance,
   these were judged non-substantive for this specific model-availability
   announcement and were not separately mined.
3. **No contradiction issue filed**: The admin-default policy language
   difference between this source and the June 2, 2026 Gemini rollout notice
   (Claim 6) is resolved as product evolution via the intervening global
   model policy GA (`docs-github-copilot-global-model-policy-ga.md`,
   enforced August 26-September 1, 2026), not a same-point-in-time factual
   conflict. See Cross-References → Contradicts.
4. **Cross-reference verification performed**: All `Claim N` citations to
   `docs-github-copilot-gemini-cli-cloud-agent-app.md`,
   `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`,
   `docs-github-copilot-aug2026-model-deprecations.md`,
   `docs-github-copilot-selected-models-deprecated-sept2026.md`, and
   `docs-github-copilot-global-model-policy-ga.md` were checked against
   those notes' actual claim numbering (each note re-read in full before
   citing); none were guessed.
5. **Source is thin by design**: The changelog is approximately 110 words
   of primary text across four short sections. All extractable facts are
   captured in the eight claims above; Claims 7 and 8 are corpus
   cross-reference findings rather than facts stated by the source itself,
   and are labeled `emerging`/absence-based accordingly.
