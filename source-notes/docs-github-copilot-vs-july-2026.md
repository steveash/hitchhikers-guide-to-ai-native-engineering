---
source_url: https://github.blog/changelog/2026-07-30-github-copilot-in-visual-studio-july-update
source_type: docs
title: "GitHub Copilot in Visual Studio — July 2026 Update"
author: GitHub (official changelog)
date_published: 2026-07-30
date_extracted: 2026-08-01
last_checked: 2026-08-01
status: current
confidence_overall: settled
issue: "#2381"
---

# GitHub Copilot in Visual Studio — July 2026 Update

> GitHub's July 30, 2026 changelog for Copilot in Visual Studio 2026 (v18.8) headlines
> a new public-preview Agent built on the same Copilot SDK that powers the Copilot CLI,
> built-in .NET/Azure skills shipped off-by-default with the IDE, a selection-scoped
> ad hoc code-review surface distinct from PR review, and organization-level custom
> instructions for Copilot Chat responses — plus, per the companion Visual Studio blog
> only, branch-as-chat-context and cross-installation MSVC toolset pinning.

## Source Context

- **Type**: docs (GitHub official product changelog, "2 minute read," published July 30,
  2026, covering the Visual Studio 2026 v18.8 release). One companion page was followed
  as a substantive linked sub-page per MINER.md §1: the devblogs.microsoft.com Visual
  Studio blog post ("Visual Studio July update: Meet the new agent, powered by Copilot
  SDK"), linked from the changelog as "To learn more about what's new." The Microsoft
  Learn release-notes link (`learn.microsoft.com/visualstudio/releases/2026/release-notes`)
  is a general, non-Copilot-specific release-notes aggregator and was not followed, matching
  the precedent in `docs-github-copilot-vs-june-2026.md` Extraction Note 1 for a
  general-purpose release-notes link vs. a Copilot-specific companion post.
- **Author credibility**: GitHub and Microsoft engineering teams (changelog + devblogs
  companion post) announcing production and preview features. Authoritative for feature
  existence, exact UI paths/labels, and plan-availability gating. Not a credible source
  for the new Agent's actual first-try success-rate improvement (asserted, not measured
  with a disclosed methodology), for adoption of built-in skills, or for whether
  organization-level custom instructions are effective at achieving response consistency
  in practice.
- **Scope**: Four headline Highlights features (new SDK-based Agent, built-in .NET/Azure
  skills, selection-scoped code review, organization-level custom instructions) plus,
  from the devblogs companion post only, two additional features (branch-as-chat-context,
  cross-installation MSVC toolset auto-discovery) that the changelog's own "Highlights"
  list omits. Does NOT cover: adoption or usage data for any feature; the new Agent's
  internal architecture beyond "built on the same GitHub Copilot SDK that powers the
  GitHub Copilot CLI"; whether org-level custom instructions can be made mandatory
  (the source explicitly states they cannot — see Claim 4); or parity with the same
  month's VS Code release (see Cross-References — this was checked directly, not
  assumed).

## Extracted Claims

### Claim 1: Visual Studio's Copilot Chat has a new Agent (Preview), built on the same GitHub Copilot SDK that powers the GitHub Copilot CLI, selected from the agent picker, and designed to get more tasks right on the first try with fewer back-and-forth turns and shorter, more scannable responses

- **Evidence**: Stated in both the changelog Highlights list and the devblogs companion
  post's dedicated "Try the new Agent (Preview)" section, which adds that the design
  intent responds to user feedback for "a more consistent experience across Copilot
  surfaces" so work can move between CLI, GitHub app, VS Code, and Visual Studio.
- **Confidence**: emerging (feature is explicitly labeled Preview in both sources; the
  "gets more tasks right the first time" and "less back-and-forth" claims are asserted
  without a disclosed benchmark or methodology)
- **Quote**: "Try the new agent, now in public preview: Copilot Chat has a new Agent
  (Preview) option in the agent picker, built on the same GitHub Copilot SDK that powers
  the GitHub Copilot CLI. It gets more tasks right the first time with less
  back-and-forth. Responses are shorter and easier to scan. Select it from the agent
  picker at the bottom of the Copilot Chat window."
  (github.blog changelog, raw HTML, retrieved 2026-08-01)
- **Quote (devblogs companion post, cross-surface framing)**: "It also addresses
  feedback we've heard from Copilot users asking for a more consistent experience across
  Copilot surfaces, so work can move more naturally between them. You can start in the
  CLI, GitHub app, VS Code, or Visual Studio, then transition that work into Visual
  Studio when you're ready to review, refine, or continue the change."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-01)
- **Our assessment**: This is the first corpus source documenting the Copilot SDK — which
  `docs-github-copilot-cli-sdk-session-credit-limits.md` and
  `docs-ghaw-copilot-sdk-driver-specification.md` already establish as the execution
  substrate for Copilot CLI 1.0.5+ — being surfaced as a *second, IDE-hosted* agent
  product built on that same substrate, not merely used internally by the CLI. The
  "consistent experience across surfaces" framing is a concrete architectural signal:
  GitHub is positioning the SDK as a shared agent core across CLI, GitHub app, VS Code,
  and Visual Studio, rather than maintaining IDE-specific agent implementations
  independently. This is distinct from the existing Plan agent and the June 2026 C++
  modernization agent (`docs-github-copilot-vs-may-2026.md` Claims 1–4;
  `docs-github-copilot-vs-june-2026.md` Claim 7), both of which are described in prior
  notes without any SDK-driver attribution. For Ch04 (Agentic Workflows — Agent
  Architecture): document the Agent (Preview) as evidence that GitHub is
  consolidating multiple product-surface agents onto one SDK-level implementation,
  which the driver specification note already shows enforces standalone-mode
  environment-variable contracts, token isolation, and a 7-step session lifecycle —
  properties a practitioner evaluating "is this Copilot agent surface as governable as
  the CLI one" can now expect apply here too, pending confirmation the IDE agent uses
  the same driver conformance rules.

### Claim 2: Visual Studio now ships built-in Copilot skills authored by the .NET and Azure teams, surfaced in a "Built-in" category of the tool picker only when the matching .NET or Azure workload is installed, and disabled by default so practitioners opt in per skill

- **Evidence**: Stated in the changelog Highlights list; elaborated with UI detail
  (hover-to-preview, three-dot menu to open the skill file or folder) in the devblogs
  companion post, which also links to the public `dotnet/skills` and `microsoft/azure-skills`
  GitHub repositories as the skill source.
- **Confidence**: settled (product fact, worded consistently across the changelog and
  companion post, with an off-by-default default state stated explicitly in both)
- **Quote**: "Built-in .NET and Azure skills: Visual Studio now includes built-in skills
  authored by experts from the .NET and Azure teams to help you customize your agentic
  workflow. Find them in the "Built-in" category of the tool picker when the
  corresponding workloads are installed. They're off by default, so you can review and
  enable only the ones that fit your tasks."
  (github.blog changelog, raw HTML, retrieved 2026-08-01)
- **Quote (devblogs companion post, discovery UI)**: "Hover any skill to see its
  description and path, or use the three-dot menu to open the full skill or its folder
  location. They're off by default, so you review and enable only the ones that fit the
  task in front of you."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-01)
- **Our assessment**: This is a third distinct skill-distribution channel in the corpus,
  alongside the two `docs-github-copilot-vs-april-2026.md` already documents: (a)
  directory-path discovery (`.github/skills/`, `.claude/skills/`, `.agents/skills/` —
  Claims 1–2 there, where a team places skill files in a repo-local path and any
  compatible tool picks them up) and (b) `gh skill install` from a registry
  (`docs-github-copilot-agent-skills-cli.md`, package-manager model with
  content-addressed SHAs and `--pin` version locking). Built-in skills are neither
  repo-authored nor separately installed — they ship *inside the IDE binary itself*,
  gated by which product workload (.NET, Azure) is installed, and are off by default
  rather than requiring an explicit install step. This is closer to a bundled-feature
  model than either prior pattern, and it sidesteps the "unverified skills may contain
  prompt injections" warning that `docs-github-copilot-agent-skills-cli.md` Claim 6
  documents for the `gh skill` registry model — these skills carry first-party GitHub/
  Microsoft authorship, not third-party registry provenance. For Ch02 (Harness
  Engineering — Skill Distribution): document built-in, workload-gated, off-by-default
  skills as a third skill-distribution pattern distinct from directory discovery and
  registry installation, and note the two public source repositories
  (`github.com/dotnet/skills`, `github.com/microsoft/azure-skills`) as inspectable —
  practitioners can read the skill content on GitHub even before enabling it in the IDE.

### Claim 3: Practitioners can select a block of code in the editor, right-click, and choose Copilot Actions > Review Selection to get inline review comments scoped to that selection, powered by GitHub Copilot code review, with a sparkle icon on each comment to apply or generate a fix

- **Evidence**: Stated in the changelog Highlights list, framed as a response to wanting
  "a second opinion on a specific block of code" rather than a full-file or full-PR
  review.
- **Confidence**: settled (product fact stated directly in the official changelog)
- **Quote**: "Review selected code with Copilot: Sometimes you just want a second
  opinion on a specific block of code. Select code in the editor, right-click, and
  select Copilot Actions > Review Selection to get inline comments you can act on. Use
  the sparkle icon on any comment to apply a suggestion or have Copilot generate one,
  powered by GitHub Copilot code review."
  (github.blog changelog, raw HTML, retrieved 2026-08-01)
- **Our assessment**: This is a third distinct Copilot code-review surface in the corpus,
  scoped more narrowly than either of the two already documented: PR-level review
  (`docs-github-copilot-code-review-comment-ux.md`,
  `docs-github-copilot-code-review-config-controls.md`, both governance/UX layers on top
  of a PR-triggered review) and general chat-based review (ask Copilot Chat about code,
  unscoped). Review Selection is scoped to an explicit editor selection, invoked ad hoc
  mid-edit, before a PR exists — the same underlying "GitHub Copilot code review" engine
  documented across the PR-review notes now runs on an arbitrary selection rather than a
  diff. For Ch01 (Daily Workflows): document Review Selection as the new fastest-path ad
  hoc review workflow — get review comments on a block of code being actively edited,
  without committing, opening a PR, or switching to chat and re-pasting the code as
  context.

### Claim 4: GitHub organization owners can now add organization-level custom instructions that automatically apply to Copilot's responses across every repository in the organization, are visible in the reference list during Copilot interactions, can be disabled per-developer via a settings toggle, are gated to Business/Enterprise plans, and are explicitly scoped as preference-setting rather than policy enforcement

- **Evidence**: Stated in the changelog Highlights list and elaborated at length in the
  devblogs companion post's dedicated section, which adds the explicit "not enforcing
  policy" scoping and the per-developer opt-out toggle location.
- **Confidence**: settled (product fact, worded consistently across the changelog and
  companion post, with the "preferences not policy" framing explicit in the companion
  post)
- **Quote**: "Organization-level custom instructions: GitHub organization owners can now
  add custom instructions that tailor Copilot's responses across the entire
  organization, so shared preferences don't have to be configured per developer. They
  automatically apply in repositories that belong to your organization and appear in
  the reference list, and you can disable them under Tools > Options > GitHub > Copilot
  > Copilot Chat."
  (github.blog changelog, raw HTML, retrieved 2026-08-01)
- **Quote (devblogs companion post, preference-not-policy scoping)**: "This works when
  the repository belongs to a GitHub organization, and it's meant for setting
  preferences, not enforcing policy."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-01)
- **Quote (devblogs companion post, opt-out mechanism)**: "If you'd rather not use them,
  or want to avoid conflicts with your own user-level instructions, you can turn them
  off under Tools > Options > GitHub > Copilot > Copilot Chat by unchecking Enable
  organization-level custom instructions."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-01)
- **Our assessment**: This adds a third rung to the corpus's instruction/preference
  hierarchy for Copilot Chat, above the two already documented: individual, inferred
  user-level Memory preferences (`docs-github-copilot-memory-user-preferences.md`
  Claim 1 — Pro/Pro+, cross-repository, stated-or-inferred) and repository-level
  `.github/copilot-instructions.md` / `*.instructions.md` files (whose 4,000-character
  limit was removed per `docs-github-copilot-code-review-config-controls.md` Claim 5,
  in the code-review-specific context). Organization-level custom instructions sit above
  both: org-owner-authored, org-wide by default, but explicitly and by design
  overridable by a developer's own settings toggle — the source's own "not enforcing
  policy" language is a direct, first-party statement that this mechanism does not
  compete with the lockable, admin-enforced runner configuration
  `docs-github-copilot-code-review-config-controls.md` Claims 1–2 document for code
  review specifically (where organization defaults *can* be locked to override
  repo-level settings). The two governance models — lockable enforcement for code-review
  runner config vs. overridable-by-default preferences for chat custom instructions —
  are not in tension; they are different mechanisms for different surfaces, so this is
  not filed as a contradiction per MINER.md §4a's "differ only in context" exclusion.
  For Ch07 (Security & Governance): document the emerging three-tier instruction
  hierarchy (user Memory → repo instructions file → org-level instructions) and flag
  that, unlike code-review runner configuration, org-level custom instructions cannot
  currently be locked to prevent per-developer opt-out — a limitation teams relying on
  it for actual compliance (rather than convenience) should know before treating it as
  a governance control.

### Claim 5: Visual Studio can now attach a Git branch to Copilot Chat as context, alongside the previously existing ability to attach commits, changes, and pull requests, via right-click "Add to Chat" in the Git Repository window

- **Evidence**: Stated only in the devblogs companion post's dedicated "Attach branches
  to Copilot Chat" section; absent from the changelog's own Highlights list.
- **Confidence**: settled (product fact, from the official companion blog post)
- **Quote**: "Ever wanted to ask Copilot about a branch before you check it out?
  Branches now join commits, changes, and pull requests as context you can attach to
  Copilot Chat. Right-click any branch in the Git Repository window and select Add to
  Chat to bring it into your conversation."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-01)
- **Our assessment**: This is a fourth Git-object type addable as Copilot Chat context
  in Visual Studio, extending the same right-click "Add to Chat" gesture the corpus
  already documents for commits (`docs-github-copilot-vs-may-2026.md` Claim 10) and pull
  requests (`docs-github-copilot-vs-june-2026.md` Claim 11) — the devblogs post's own
  phrasing ("Branches now join commits, changes, and pull requests") confirms this is
  additive to, not a replacement for, those existing context types. The stated use case
  — "ask Copilot about a branch before you check it out" — is a pre-checkout
  exploration workflow distinct from the post-checkout, in-progress-work context the
  commit/PR attachment mechanisms serve. For Ch01 (Daily Workflows): add branch
  attachment to the existing "right-click Git object → Add to Chat" habit already
  documented for commits and PRs, framed as a way to get a Copilot-generated branch
  summary before deciding whether to check it out.

### Claim 6: Visual Studio C++ projects can now opt in to discovering a pinned MSVC toolset version across all Visual Studio and Visual Studio Build Tools installations on a machine, not just the current installation, by setting `EnableVCToolsVersionDiscovery` to `true`

- **Evidence**: Stated only in the devblogs companion post's "MSVC Build Tools
  auto-discovery across installations" section; absent from the changelog. The post
  contrasts the new behavior with the prior behavior in detail.
- **Confidence**: settled (product fact with a stated mechanism and an explicit
  before/after behavioral contrast, from the official companion blog post)
- **Quote**: "You can now opt in to automatic discovery of the Microsoft C++ (MSVC)
  Build Tools across all your Visual Studio IDE and Visual Studio Build Tools
  installations, so a pinned VCToolsVersion resolves correctly even when it lives in a
  different install."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-01)
- **Quote (prior-behavior contrast)**: "Previously, Visual Studio only searched other
  installations when your current install had no toolset at all for your target
  platform toolset. If your project targeted v143 and the current install already had
  any v143 toolset, the search stopped there, even when you'd pinned a specific
  VCToolsVersion that only existed elsewhere. Now the search keeps going to find the
  exact version you asked for."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-01)
- **Our assessment**: This is not a Copilot AI feature — it is a C++ build-toolchain
  fix bundled into the same monthly Copilot-branded changelog cycle (via the devblogs
  companion post, not the github.blog Copilot changelog itself), which is itself a
  minor but concrete data point: GitHub/Microsoft use the Visual Studio blog as a
  general product-update channel, not an exclusively-Copilot one, and the github.blog
  Copilot changelog is edited down to AI-relevant items only (this feature was excluded
  from it). For build-reproducibility content (if the guide covers CI/toolchain pinning
  adjacent to AI-assisted workflows, e.g. in Ch02's environment-reproducibility
  discussion): document `EnableVCToolsVersionDiscovery` as a concrete fix for a
  version-pin resolution bug that silently used the wrong toolset when *any* matching
  major-version toolset existed locally, even if it wasn't the pinned one — relevant to
  teams whose C++ builds are being modernized or reviewed by the GA'd modernization
  agent (`docs-github-copilot-vs-june-2026.md` Claim 7), since toolset resolution
  correctness directly affects that agent's build verification step.

## Concrete Artifacts

### MSVC Toolset Version Pinning — Opt-In Cross-Installation Discovery (Visual Studio, July 2026)

```
Source: devblogs.microsoft.com companion post, retrieved 2026-08-01

Setting: EnableVCToolsVersionDiscovery (MSBuild property, default: not set / off)

Project or Directory.Build.props:

<PropertyGroup>
  <EnableVCToolsVersionDiscovery>true</EnableVCToolsVersionDiscovery>
  <VCToolsVersion>14.43.34604</VCToolsVersion>
</PropertyGroup>

BEHAVIOR CHANGE:
  Before: search across other VS/Build Tools installations stopped as soon as
          ANY toolset matching the target platform toolset (e.g. v143) was found
          locally, even if it did not match the pinned VCToolsVersion.
  After:  with the flag enabled, search continues across all installations
          until the exact pinned VCToolsVersion is found, regardless of
          installation location.

Stated payoff (devblogs post, verbatim): "version pins are honored regardless
of which installation contains them, builds stay reproducible across your
team without individual IDE updates changing compiler behavior, and
cross-install toolset references resolve automatically instead of requiring
manual VCToolsInstallDir overrides."
```

### July 2026 Visual Studio Copilot Release — Feature/Source Map

```
Source: github.blog changelog (2026-07-30) + devblogs.microsoft.com companion
        post, both retrieved 2026-08-01

FROM CHANGELOG "HIGHLIGHTS" (all four; availability noted):
  - New Agent (Preview), SDK-based           [Claim 1] — all plans
  - Built-in .NET/Azure skills, off-by-default [Claim 2] — all plans
  - Review Selection (selection-scoped code review) [Claim 3] — all plans
  - Organization-level custom instructions   [Claim 4] — Business/Enterprise only

FROM DEVBLOGS COMPANION POST ONLY (not in changelog Highlights list):
  - Attach branches to Copilot Chat          [Claim 5]
  - MSVC Build Tools cross-installation auto-discovery [Claim 6] (not an AI
    feature; C++ toolchain fix)

"WHAT'S NEXT" SECTION (changelog): no concrete roadmap items disclosed — only
points to the Visual Studio blog for future roadmap updates and feedback
channels. No claim extracted; content-free beyond a pointer.
```

## Cross-References

### Cross-reference verification notes

Claims cited from `docs-github-copilot-vs-april-2026.md`,
`docs-github-copilot-vs-may-2026.md`, `docs-github-copilot-vs-june-2026.md`,
`docs-github-copilot-agent-skills-cli.md`,
`docs-github-copilot-code-review-config-controls.md`,
`docs-github-copilot-memory-user-preferences.md`,
`docs-github-copilot-cli-sdk-session-credit-limits.md`, and
`docs-ghaw-copilot-sdk-driver-specification.md` were re-read directly in
those notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Extends**:
  - `docs-github-copilot-cli-sdk-session-credit-limits.md` (Claim 1, Copilot
    SDK 1.0.5+ backing Copilot CLI) and `docs-ghaw-copilot-sdk-driver-specification.md`
    (whole note, SDK driver conformance requirements): Claim 1 (new Agent
    Preview) is the first corpus evidence of the Copilot SDK being surfaced as
    a shared agent core for a *second* first-party product surface (Visual
    Studio), not only the CLI — extending "Copilot SDK" from a CLI
    implementation detail to a cross-surface architecture choice.
  - `docs-github-copilot-vs-april-2026.md` (Claims 1–2, directory-path skill
    discovery) and `docs-github-copilot-agent-skills-cli.md` (whole note,
    `gh skill` registry distribution): Claim 2 (built-in .NET/Azure skills)
    adds a third skill-distribution channel — shipped inside the IDE,
    workload-gated, off-by-default — distinct from both directory discovery
    and registry installation.
  - `docs-github-copilot-code-review-comment-ux.md` and
    `docs-github-copilot-code-review-config-controls.md` (PR-scoped Copilot
    code review): Claim 3 (Review Selection) is a third review surface using
    the same underlying review engine, scoped to an arbitrary editor
    selection rather than a PR diff.
  - `docs-github-copilot-memory-user-preferences.md` (Claim 1, user-level
    Memory) and `docs-github-copilot-code-review-config-controls.md` (Claim
    5, repo-level `.github/copilot-instructions.md` character-limit removal):
    Claim 4 (organization-level custom instructions) completes a three-tier
    instruction hierarchy — user Memory (individual, inferred) → repository
    instructions file (team, explicit) → organization-level instructions
    (org-wide, explicit, overridable per developer).
  - `docs-github-copilot-vs-may-2026.md` (Claim 10, commit-attachment) and
    `docs-github-copilot-vs-june-2026.md` (Claim 11, PR-attachment): Claim 5
    (branch attachment) is the fourth Git-object type addable to Copilot Chat
    via the same right-click "Add to Chat" gesture in the Git Repository
    window.
  - `docs-github-copilot-vs-june-2026.md` (Claim 7, C++ modernization agent
    GA): Claim 6 (MSVC toolset cross-installation discovery) is relevant
    build-correctness context for teams using that agent, since its
    build-verification step depends on the correct toolset being resolved.

- **Corroborates**: None beyond the "Extends" relationships above — no
  existing corpus note makes an independent, separately-sourced claim that
  this source's claims directly restate without adding new detail.

- **Contradicts**: None identified and none filed. Organization-level custom
  instructions being explicitly non-enforcing (Claim 4) sits alongside, not
  in opposition to, the lockable organization-level runner configuration
  `docs-github-copilot-code-review-config-controls.md` Claims 1–2 document for
  code review — these are two different governance mechanisms for two
  different Copilot surfaces (general chat instructions vs. code-review
  runner selection), and the source itself frames the distinction explicitly
  ("preferences, not policy") rather than leaving it as an unexplained
  inconsistency. Per MINER.md §4a, this is a conditioning-variable difference
  (which surface, which governance need), not a material contradiction — no
  contradiction issue filed.

- **Novel**:
  - **Copilot SDK named as the shared substrate behind a second, IDE-hosted
    agent product** (Claim 1): first corpus evidence that GitHub is
    consolidating agent implementations across CLI and IDE surfaces onto one
    SDK, beyond the CLI-only usage the SDK notes previously documented.
  - **Built-in, workload-gated, off-by-default first-party skills shipped
    inside the IDE** (Claim 2): a third skill-distribution model not
    previously documented in the corpus, distinct from directory discovery
    and registry installation.
  - **Selection-scoped ad hoc code review, independent of both PR review and
    general chat** (Claim 3): first corpus documentation of a review surface
    scoped to an arbitrary in-editor selection rather than a diff or an
    unscoped chat question.
  - **Organization-level custom instructions for Copilot Chat, explicitly
    scoped as non-enforceable preferences** (Claim 4): first corpus source to
    document an org-wide instruction-setting mechanism for general Copilot
    Chat responses (as opposed to code-review-specific configuration), and
    the first to explicitly state such a mechanism is deliberately
    non-enforcing.
  - **Branch as a fourth attachable Git-object context type** (Claim 5) and
    **opt-in cross-installation MSVC toolset pinning** (Claim 6): incremental
    but concrete additions to already-documented patterns.

## Guide Impact

- **Chapter 04 (Agentic Workflows — Agent Architecture)**: Add the new Agent
  (Preview) (Claim 1) as evidence that GitHub is building multiple
  product-surface agents (CLI, VS Code, Visual Studio, GitHub app) on one
  shared Copilot SDK core, rather than maintaining separate per-surface agent
  implementations — cite alongside the SDK driver specification's
  conformance requirements (standalone mode, token isolation, 7-step
  lifecycle) as the properties this consolidation should bring to the IDE
  agent surface too, pending confirmation.

- **Chapter 02 (Harness Engineering — Skill Distribution)**: Add built-in,
  workload-gated, off-by-default skills (Claim 2) as a third
  skill-distribution pattern in the guide's skills-ecosystem coverage,
  alongside directory-path discovery and `gh skill` registry installation.
  Note the two public source repositories (`dotnet/skills`,
  `microsoft/azure-skills`) as independently inspectable before enabling.

- **Chapter 01 (Daily Workflows)**:
  - Add Review Selection (Claim 3) as the fastest ad hoc review path — get
    inline comments on a specific in-editor code selection without a commit
    or PR.
  - Add branch attachment (Claim 5) to the existing commit/PR "Add to Chat"
    habit, framed as a pre-checkout branch-summary workflow.

- **Chapter 07 (Security & Governance)**: Document the emerging three-tier
  Copilot instruction hierarchy (user Memory → repo instructions file →
  organization-level instructions, Claim 4) and flag explicitly that,
  unlike code-review runner configuration, organization-level custom
  instructions cannot be locked against per-developer opt-out — teams
  wanting actual compliance rather than convenience need a different
  control.

## Extraction Notes

1. **Raw HTML fetched via `curl`, not WebFetch's AI-summarized output**:
   Following the precedent set in `docs-github-copilot-vs-june-2026.md`
   Extraction Note 2 and `docs-github-copilot-vscode-july-2026.md` Extraction
   Note 1, an initial WebFetch call to the primary changelog returned a
   condensed, restructured summary (different section framing and compressed
   sentences vs. the source). To avoid citing paraphrased text as a direct
   quote (MINER.md §2a), both the changelog and the devblogs companion post
   were re-fetched via `curl` with a browser user-agent, and body text was
   extracted from the raw HTML with a Python script (strip
   `<script>`/`<style>`, convert block-level tags to newlines, strip
   remaining tags, unescape entities). All quotes in this note are taken
   from that raw-HTML-derived plain text.

2. **One companion page followed; the Microsoft Learn release-notes link was
   not**: The changelog links to two pages — the devblogs.microsoft.com
   Visual Studio blog post (Copilot-specific, followed and extracted above)
   and `learn.microsoft.com/visualstudio/releases/2026/release-notes`
   (general Visual Studio release notes, not Copilot-specific). Consistent
   with the June 2026 note's judgment on the same category of link, the
   general release-notes aggregator was not followed — the changelog plus
   its Copilot-specific companion post is the complete AI-feature record for
   this release cycle.

3. **Two features exist only in the companion post, not the changelog's own
   Highlights list**: Branch attachment (Claim 5) and MSVC toolset
   auto-discovery (Claim 6) do not appear anywhere in the github.blog
   changelog text — confirmed by direct inspection of the raw-HTML-derived
   changelog transcript. Both are documented here from the devblogs post
   only. This mirrors the pattern `docs-github-copilot-vs-june-2026.md`
   Extraction Note 4 documents for color-emoji rendering (devblogs-only,
   changelog-omitted) — GitHub's own Copilot changelog appears to be edited
   down to a curated subset of what the fuller Visual Studio blog post
   covers.

4. **VS Code July 2026 parity check performed directly, per the Prospector's
   triage request**: The Prospector's triage comment asked whether the new
   SDK-based agent, built-in skills, selection-based review, and org-level
   custom instructions have parity with the same month's VS Code release.
   `docs-github-copilot-vscode-july-2026.md` (issue #2352, covering VS Code
   v1.127–v1.131, same July 2026 window) was read in full: it documents no
   SDK-based "Agent (Preview)," no built-in first-party .NET/Azure skills, no
   selection-scoped ad hoc code review, and no organization-level custom
   instructions. The two releases share no overlapping headline feature this
   month — VS Code's July highlights are worktree-based multi-harness
   sessions, multi-chat/forking, BYOK-in-Agents-window, and dictation (see
   that note's Claims 1–13), none of which this Visual Studio source
   mentions either. This is a genuine finding, not an omission: the two IDEs'
   July 2026 Copilot releases are feature-disjoint at the headline level,
   contrary to what a reader might assume from "same vendor, same month."
   Recorded here rather than filed as a contradiction, since divergent
   release contents across IDE products is not a claim conflict under
   MINER.md §4a.

5. **No contradictions identified**: Cross-referenced against all existing
   VS/VS Code Copilot notes, the skills-distribution notes
   (`docs-github-copilot-vs-april-2026.md`,
   `docs-github-copilot-agent-skills-cli.md`), the code-review governance
   notes, the Copilot Memory note, and the Copilot SDK notes. No claim in
   this source opposes an existing corpus position; the org-level custom
   instructions "preferences, not policy" framing (Claim 4) is a distinction
   the source draws explicitly, not an unresolved tension with the code
   review governance notes' lockable runner configuration. No contradiction
   issue filed.
