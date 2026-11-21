---
source_url: https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team
source_type: docs
title: "Customize GitHub Copilot for your team"
author: GitHub (official changelog)
date_published: 2026-11-18
date_extracted: 2026-11-21
last_checked: 2026-11-21
status: current
confidence_overall: settled
issue: "#4872"
---

# Customize GitHub Copilot for your team

> GitHub's Nov 18, 2026 changelog makes team customizations GA: team maintainers and org owners pick approved Agent Plugins as team defaults, a self-serve middle layer between individual setup and org/enterprise policy, which always wins.

## Source Context

- **Type**: docs (GitHub official changelog, "Release", 1-minute read, tagged `copilot`). Short announcement (~250 words); no config, code or metrics. Linked docs ("plugins for GitHub Copilot") and a Community discussion were not followed; the Prospector asked for precedence/inheritance rules only, not the UI walkthrough.
- **Author credibility**: GitHub product team; authoritative for the stated behavior, not for edge cases (conflict surfacing, audit, adoption data).
- **Scope**: Covers team-level default plugins on the "Customize Copilot" tab of an organization team, inheritance, member opt-out, and policy precedence. Does NOT cover: what happens when a team enables a plugin that policy later blocks (beyond "don't override"), whether team marketplace additions are constrained by `strictKnownMarketplaces`, multi-team membership resolution, or audit tooling.

## Extracted Claims

### Claim 1: Team defaults are a shared starting point between individual customization and organization-wide policy
- **Evidence**: Product announcement; GA for organization teams.
- **Confidence**: settled
- **Quote**: "This gives your team a shared starting point between individual customization and organization-wide policy."
- **Our assessment**: Clean three-layer framing (individual / team / org-enterprise) for Ch05. Buy it as description of the product; effectiveness is unmeasured.

### Claim 2: Team maintainers and org owners (not ordinary members) select the approved plugins
- **Evidence**: Stated role gating; setup is on github.com's team page.
- **Confidence**: settled
- **Quote**: "Team maintainers and organization owners can select approved Agent Plugins as team defaults."
- **Our assessment**: Delegates curation to a team-level role rather than central admins, unlike the admin-managed `team-mappings.json` mechanism.

### Claim 3: Teams can browse built-in, enterprise, and team-added marketplaces, and can add a marketplace from a GitHub repository
- **Evidence**: UI description of the Customize Copilot tab.
- **Confidence**: settled
- **Quote**: "Add a marketplace from a GitHub repository that contains a plugin marketplace."
- **Our assessment**: Self-serve marketplace addition widens the trust surface; the note is silent on how this interacts with enterprise marketplace allowlists beyond the generic precedence statement (Claim 6). Open question.

### Claim 4: Team plugins are enabled by default for direct members across VS Code, the Copilot app, and Copilot CLI
- **Evidence**: Stated client list.
- **Confidence**: settled
- **Quote**: "Selected plugins are enabled by default for the team’s direct members in VS Code, the GitHub Copilot app, and Copilot CLI."
- **Our assessment**: Cloud agent is not listed here, whereas the enterprise team-specialization note lists it; coverage is narrower for this layer.

### Claim 5: Child-team members do not inherit team defaults, and defaults are optional for members
- **Evidence**: Stated rules.
- **Confidence**: settled
- **Quote**: "Members of child teams don’t inherit them. Team defaults are optional. Members can turn a team plugin off in their Copilot client where policy permits."
- **Our assessment**: Non-inheritance means nested org structures must configure each team explicitly; opt-out makes team defaults a soft default, not enforcement. "Where policy permits" implies policy can make some non-optional.

### Claim 6: Enterprise and org policy take precedence; team defaults cannot override marketplace allowlists or required/blocked plugins
- **Evidence**: Stated precedence; clients enforce policy.
- **Confidence**: settled
- **Quote**: "Team defaults don’t override those controls."
- **Our assessment**: Same ceiling pattern as non-overridable keys in the enterprise team-specialization note. Full sentence: "Enterprise and organization policies take precedence over team choices."

### Claim 7: Availability is Copilot Business and Copilot Enterprise
- **Evidence**: Stated.
- **Confidence**: settled
- **Quote**: "Team customizations are available for Copilot Business and Copilot Enterprise."
- **Our assessment**: Not available on individual plans.

## Concrete Artifacts

No code or config. Procedure (paraphrased from the source's setup section): org team on github.com → "Customize Copilot" tab → browse plugins / add marketplace → add individual plugins to the team.

## Cross-References

- **Corroborates**: `docs-github-copilot-enterprise-team-specialization-managed-settings.md` Claim 10 (non-overridable enterprise decisions form a compliance ceiling; team settings apply beneath the enterprise file) and Claim 7 (team-level plugin additions are layered over an enterprise baseline).
- **Contradicts**: None found. (Differences in mechanism, self-serve org-team UI vs admin-managed `team-mappings.json`, and client coverage are conditioning variables, not contradictions.)
- **Extends**: `docs-github-copilot-strict-plugin-only-customization.md` Claim 6 (plugin-only is not a marketplace allowlist; pair with `strictKnownMarketplaces`), as the precedence counterpart for team-added marketplaces; `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2 (enterprise baseline plugins apply uniformly), now with a team layer beneath; `docs-github-copilot-agent-plugins-1-0.md` Claim 11 (managed-settings governance applies to Agent Plugins).
- **Novel**: Self-serve team-maintainer plugin defaults with no child-team inheritance and member opt-out.

## Guide Impact

- **Chapter 05**: Describe per-team plugin governance as three layers (individual, team defaults, org/enterprise policy), noting team defaults are optional, direct-members-only, and subordinate to policy. Cite this note alongside the team-specialization note.
- **Chapter 02**: Note that plugin sharing for a team no longer requires per-member setup in Copilot.
- **Chapter 06**: Flag that team-added GitHub-repo marketplaces are a trust boundary; recommend pairing with `strictKnownMarketplaces`. Behavior of that interaction is unconfirmed by this source.

## Extraction Notes

Read full page (raw HTML text extracted via curl; quotes verbatim from it, with typographic apostrophes). Short source; linked docs and community discussion not followed. Thin by nature, per Prospector's "short extension" guidance.
