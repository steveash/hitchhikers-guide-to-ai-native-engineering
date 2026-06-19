---
source_url: https://github.blog/changelog/2026-06-18-generated-release-notes-credit-you-for-copilot-pull-requests
source_type: docs
title: "Generated release notes credit you for Copilot pull requests"
author: GitHub (official changelog)
date_published: 2026-06-18
date_extracted: 2026-06-19
last_checked: 2026-06-19
status: current
confidence_overall: settled
issue: "#1220"
---

# Generated Release Notes Credit You for Copilot Pull Requests

> GitHub now attributes both the human requester and @copilot when a Copilot cloud
> agent–opened PR appears in generated release notes, introducing a "by @[user] with
> @copilot" dual-authorship pattern that makes human agency visible even when the
> agent performs the mechanical PR-open action.

## Source Context

- **Type**: docs (GitHub official changelog, June 18, 2026; ~150 words)
- **Author credibility**: GitHub engineering team announcing a production feature change.
  Authoritative for the feature's existence, its exact attribution format, and its
  availability scope. Not a credible source for: how the feature interacts with
  third-party release-note generators, whether the attribution appears in the GitHub
  Releases API output as well as UI-generated notes, or how it handles PRs created
  via non-CCA Copilot paths.
- **Scope**: The change to how GitHub's built-in generated release notes display Copilot
  cloud agent–created PRs: the format switch from "by @copilot" to "by @[requester]
  with @copilot," universal availability across all plans and repositories, and the
  framing that the human requester retains authorship credit. Does NOT cover: the
  Releases API response schema, behavior with non-CCA Copilot PRs (e.g., Copilot CLI
  auto-review), how release notes generated before this change behave retroactively,
  or any enterprise-level attribution override settings.

## Extracted Claims

### Claim 1: GitHub's generated release notes now credit both the human requester and @copilot when a CCA-opened PR is merged

- **Evidence**: Official GitHub product changelog announcing the feature change, June 18,
  2026. The changelog is the authoritative source for feature behavior in GitHub's
  own release-note generation.
- **Confidence**: settled (product fact; announced in official changelog, available now)
- **Quote**: "the developer who asked Copilot to open the pull request gets credit
  alongside `@copilot`."
- **Our assessment**: This is the core feature. Before this change, a Copilot cloud
  agent–created PR appeared in generated release notes as authored solely by @copilot.
  After the change, the human who invoked the agent appears as co-author. This is a
  meaningful attribution correction: the human made the decision, specified the intent,
  and is responsible for the PR being in the release — the agent only performed the
  mechanical act of opening it.

### Claim 2: The attribution format is "by @[requester] with @copilot" — not "by @copilot" alone

- **Evidence**: Concrete before/after example from the changelog:
  - Before: "Add `create_feature_flag` MCP tool by `@copilot`"
  - After: "Add `create_feature_flag` MCP tool by `@monalisa` with `@copilot`"
- **Confidence**: settled (concrete example in official changelog)
- **Quote**: The before example is "Add `create_feature_flag` MCP tool by `@copilot`";
  the after example is "Add `create_feature_flag` MCP tool by `@monalisa` with `@copilot`"
- **Our assessment**: The "with" conjunction is a deliberate design choice. It frames
  the relationship as collaboration — @monalisa did the work *with* @copilot's assistance
  — rather than delegation ("by @copilot on behalf of @monalisa"). This framing matters
  for team culture and recognition: the release history reflects a human-led contribution
  aided by AI, not an AI contribution approved by a human. The pattern is also
  machine-readable — tooling that parses release notes for contribution attribution
  can distinguish "by @copilot" (unattributed to a human) from "by @user with @copilot"
  (human-attributed with AI assistance).

### Claim 3: The dual-attribution feature is available for all repositories and all GitHub plan tiers

- **Evidence**: Explicit availability statement in the changelog.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "This is available now for all repositories on GitHub and all plans."
- **Our assessment**: Unlike most GitHub Copilot cloud agent features (which require
  Copilot Business or Enterprise subscriptions), this attribution change is universal.
  It applies to any repository whose release notes include CCA-opened PRs. The universal
  availability makes sense: this is a rendering change to an existing GitHub feature
  (generated release notes), not a new paid capability. Teams on any plan that use
  a Copilot Business/Enterprise member's CCA work will see the updated attribution in
  their release notes.

### Claim 4: Generated release notes are built from the list of merged PRs since the last release, making CCA PR attribution automatically visible in the standard release workflow

- **Evidence**: Context sentence from the changelog describing how generated release
  notes work.
- **Confidence**: settled (description of an existing GitHub feature in official changelog)
- **Quote**: "When you generate release notes for a new release, the generated notes
  include a list of pull requests merged since the last release."
- **Our assessment**: This places the attribution change in its operational context.
  Teams that use GitHub's built-in generated release notes feature — whether triggered
  manually through the UI ("Auto-generate release notes" button), via the GitHub Releases
  API, or through CI/CD pipelines that call the Releases API — will see the dual
  attribution automatically for any CCA-opened PRs. No opt-in or configuration is needed.
  The feature is passive: it changes the display of data that was already being collected.

### Claim 5: The feature is framed as recognition for human agency in AI-assisted contributions, even when the agent performs the mechanical PR-open action

- **Evidence**: Feature framing in the changelog, describing the intent of the change.
- **Confidence**: settled (stated explicitly in official changelog)
- **Quote**: "you get recognition for the work you do with Copilot cloud agent, even
  when the agent opens the pull request on your behalf."
- **Our assessment**: The phrase "the work you do with Copilot cloud agent" is
  significant. GitHub frames the human's act of *invoking* the agent — specifying the
  task, reviewing the output, and deciding to merge — as substantive work deserving of
  attribution. This aligns with how effective AI-native teams describe their work:
  the human contributes judgment and direction; the agent contributes execution. Release
  notes are now a public record of that collaborative model. The phrasing "on your
  behalf" further positions the agent as executing the human's decision, not the reverse.

## Concrete Artifacts

### Before/After Attribution Format (from changelog, June 18, 2026)

```
# Generated release notes attribution change for Copilot cloud agent PRs
# Source: github.blog/changelog/2026-06-18-generated-release-notes-credit-you-for-copilot-pull-requests

BEFORE (Copilot cloud agent creates PR):
  Add `create_feature_flag` MCP tool by `@copilot`

AFTER (same scenario, post-June 18, 2026):
  Add `create_feature_flag` MCP tool by `@monalisa` with `@copilot`

  Where:
    @monalisa = the developer who asked Copilot to open the PR
    @copilot  = the agent that opened the PR mechanically

Scope:
  - Applies to: all repositories on GitHub, all plans
  - Trigger: GitHub's built-in "Generate release notes" feature
  - Requires: PR must have been opened by Copilot cloud agent
  - Date available: June 18, 2026 (no opt-in required)
```

### Attribution Pattern Summary

```
# Human-AI PR co-authorship attribution pattern in GitHub release notes

Pattern: "[PR title] by @[human-requester] with @copilot"

Signals:
  @[human-requester] = the person who invoked CCA to create this PR
                        (made the decision, specified the task, owns the intent)
  @copilot           = the agent that performed the mechanical PR creation
                        (executed the task, opened the PR)
  "with"             = collaboration framing (human-led, AI-assisted)
                        NOT delegation framing (AI-created, human-approved)

Appears in:
  - GitHub-generated release notes (UI: "Auto-generate release notes")
  - GitHub Releases API (releases that use auto-generated notes)
  - Any CI/CD workflow that calls the Releases API with auto-generated content
```

## Cross-References

- **Corroborates** `docs-github-copilot-cca-rest-api-tasks.md` Claim 5 (REST API
  enables automated weekly release preparation including release notes): That source
  documents the technical trigger path (REST API call); this source documents what the
  resulting release notes look like when CCA-opened PRs are included. Together they
  describe an automated release pipeline where: (1) a cron-triggered REST API call
  instructs CCA to prepare a release, (2) CCA opens PRs, (3) humans review and merge,
  and (4) generated release notes attribute the merges as "by @[releaser] with @copilot."
  The human requester visible in (4) is whoever initiated the REST API call in (1).

- **Extends** `blog-gh-aw-operations-release-workflows.md` Claim 1 (Changeset Generator
  achieved 78% PR merge rate): That source documents GitHub's own use of an agent
  workflow to generate release PRs at production scale. The 22 merged PRs from that
  workflow would, after June 18, 2026, appear in generated release notes as "by
  @[workflow-triggerer] with @copilot" rather than "by @copilot" alone. The attribution
  change retrospectively strengthens the human-accountability story in that data:
  the 78% merge rate is not just an agent metric but a human decision rate — each
  merged PR reflects a human choosing to accept the agent's output.

- **Complements** `docs-github-copilot-cli-auto-model-selection.md` Claim 5 (CLI
  surfaces which model was used per request as a transparency affordance): Both sources
  document GitHub building transparency primitives into AI-assisted workflows — CLI
  surfaces which model ran; release notes surface which human invoked the agent.
  Together they evidence GitHub's design philosophy that AI tooling should make its
  human-AI collaboration legible, not opaque.

- **Contradicts**: None identified. No existing corpus source claims that CCA-opened
  PRs in release notes should show only @copilot as author, and no source argues
  against dual attribution. No contradiction issue filed.

- **Novel**:
  - **First corpus source documenting a GitHub-native transparency primitive for
    human-AI co-authorship in release artifacts**: No prior source discusses how AI
    agent contributions are attributed in permanent project records (release notes,
    changelogs). This is the first evidence that GitHub treats AI-assisted PRs as
    requiring dual attribution rather than AI-only attribution.
  - **The "with @copilot" co-authorship format as a named attribution pattern**: The
    specific "by @[human] with @copilot" format is a concrete, quotable example of
    how human-AI collaboration is being encoded in structured project artifacts. No
    prior corpus source provides a specific attribution format for AI-assisted work.
  - **Universal (all-plans) availability for a Copilot feature with no enterprise
    prerequisite**: Most Copilot cloud agent features require Business/Enterprise.
    This attribution change requires no paid CCA subscription to benefit from; it
    applies to any repository whose release notes include CCA-opened PRs, regardless
    of the repository owner's plan. This makes it a broadly applicable pattern to
    document.

## Guide Impact

- **Chapter 01 (AI-Native Developer Workflows — Daily Patterns)**:
  Add a note that release notes now make human agency in AI-assisted PRs visible
  by name. Developers using Copilot cloud agent to create PRs should know that their
  name — not just @copilot — appears in the release history. This addresses the
  "invisible contribution" concern: team members who use AI tools to accelerate
  their work receive explicit attribution in the project record. The attribution
  pattern also makes AI tool adoption individually verifiable (a team lead can see
  which releases involved Copilot-assisted PRs and which team members drove them).

- **Chapter 02 (Tool Integration — Release Workflow Automation)**:
  When documenting automated release pipelines (CCA REST API → agent creates PRs →
  human merges → release notes generated), specify that generated release notes will
  attribute the human who triggered the CCA task as co-author alongside @copilot.
  Practitioners building automation should design the trigger so the correct human
  identity is associated with CCA invocations — e.g., avoid using a service account
  to call the REST API if individual developer attribution in release notes matters.

- **Chapter 05 (Human-AI Collaboration Patterns)**:
  The "by @[human] with @copilot" format is a concrete GitHub-native implementation
  of the principle that AI tools should augment and acknowledge human agency, not
  replace or obscure it. Use this as an example when discussing how AI-native teams
  can maintain accountability and recognition structures: GitHub has baked dual
  attribution directly into its release artifact infrastructure. Teams designing
  their own release workflows can use this as a reference for how to encode
  human-AI collaboration in permanent project records.

## Extraction Notes

1. **Very brief source (~150 words)**: This is a concise changelog announcement.
   All extractable claims are covered in 5 items above. The substantive design
   decision embedded in the source — that human agency in AI-assisted PRs deserves
   explicit attribution — is more significant than the brevity might suggest.

2. **Quote confidence caveat**: Two WebFetch calls were made to the source URL.
   The before/after attribution examples and availability statement appeared
   consistently across both fetches and are presented verbatim with high confidence.
   The quotes in Claims 1 and 5 were returned in subtly different wording between
   the two fetches; the versions used here were selected as the more complete and
   grammatically characteristic of GitHub's changelog writing style. The Assayer
   should spot-check these two quotes against the live URL.

3. **No contradictions to file**: The source makes no claims that conflict with
   existing corpus notes. The attribution format is new to the corpus, not a
   conflicting position on an existing claim.

4. **Interaction with non-CCA Copilot paths**: The source specifies this feature
   applies to PRs created via "Copilot cloud agent." It is unclear whether PRs
   that are *reviewed* by Copilot (not opened by it) also trigger the "with @copilot"
   attribution. This was not addressed in the changelog and is not claimed here.

5. **Retroactive coverage unclear**: The changelog does not address whether release
   notes generated before June 18, 2026 (or regenerated after) will show the updated
   attribution for historical CCA-opened PRs. This is not claimed here.
