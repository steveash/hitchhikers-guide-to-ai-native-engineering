---
source_url: https://github.blog/changelog/2026-10-28-build-shared-workflows-for-your-team-with-copilot-automations
source_type: docs
title: "Build shared workflows for your team with Copilot Automations"
author: GitHub (official changelog)
date_published: 2026-10-28
date_extracted: 2026-10-30
last_checked: 2026-10-30
status: current
confidence_overall: emerging
issue: "#4432"
---

# Build Shared Workflows for Your Team with Copilot Automations

> GitHub's Oct 28, 2026 changelog introduces "shared" Copilot automations: repository-owned, team-visible, write-access-editable cloud-agent workflows that bill the repo owner and act as Copilot; the linked "About automations" docs page fills in the governance details (extra PR approval, AI-credit limits, tools-as-scope, no Git versioning) that the changelog omits.

## Source Context

- **Type**: docs (GitHub changelog, ~300 words, labels `copilot`, `universe26`) plus the linked reference page "Copilot automations" (docs.github.com, `about-automations#personal-and-shared-automations`), which was read in full because the changelog is thin on mechanics.
- **Author credibility**: GitHub product team describing a shipped (rolling-out) feature. Authoritative on the feature's design and stated controls; marketing-toned in the changelog. Provides no measurements or outcome data.
- **Scope**: Covers the personal-vs-shared distinction, visibility/edit/billing/attribution rules, the org billing policy gate, and rollout. The changelog does not describe how edits by write-access users are reviewed; the docs page partly answers (see Claims 6-8) but states automations are "not committed to Git" and so not PR-reviewed. Rollout is "rolling out," not GA: "Availability may vary as the rollout progresses."

## Extracted Claims

### Claim 1: Shared automations are visible to everyone with read access and editable by anyone with write access
- **Evidence**: Stated in changelog; the docs page tabulates it (personal: only you can see/edit).
- **Confidence**: emerging (vendor-stated design, not independently observed)
- **Quote**: "Everyone with read access to the repository can see a shared automation, and anyone with write access can edit it."
- **Our assessment**: A low bar for editing an autonomous agent's prompt, tools and triggers. Write access already allows code changes, but changing an automation is a different lever (it can change what an agent does with Copilot's identity and the owner's credits). The docs say tools "control what actions it can take," so an editor can widen the tool set for every user.

### Claim 2: AI credits for shared automations bill the repository owner, not the creator
- **Evidence**: Changelog and docs billing section. Docs add that GitHub Actions minutes are billed separately to the repository owner, and each run "starts a Copilot cloud agent session that uses GitHub AI Credits and GitHub Actions minutes."
- **Confidence**: emerging
- **Quote**: "AI credits are billed to the organization or user that owns the repository, rather than to the person who created the automation."
- **Our assessment**: Removes the "one person's budget funds team automation" problem. Moves cost control to the owner, and any write-access editor can raise spend, mitigated only by optional credit limits (Claim 8).

### Claim 3: Actions by a shared automation are attributed to Copilot, not to a person
- **Evidence**: Changelog "Act as Copilot" bullet; docs table row "Identity used for actions on GitHub: Your identity / Copilot's identity."
- **Confidence**: emerging
- **Quote**: "Actions on GitHub are attributed to Copilot, rather than to any one user."
- **Our assessment**: Per-action attribution to a human is lost on GitHub. The docs partly compensate: run sessions are visible to all readers, and change history records edits. Whether change history records the editor's identity is not stated.

### Claim 4: Shared automations persist beyond their creator, with change history
- **Evidence**: Changelog "Built to last"; docs: it "keeps working if that person leaves the team or loses access to the repository."
- **Confidence**: emerging
- **Quote**: "Shared automations belong to the repository, so they keep running if the person who created them leaves the team."
- **Our assessment**: Directly addresses bus-factor/ownership of agent workflows. Also means an orphaned automation keeps spending and acting with no named owner.

### Claim 5: Org-owned repos need an admin policy before shared automations can run
- **Evidence**: Changelog and docs.
- **Confidence**: emerging
- **Quote**: "For shared automations to run in an organization-owned repository, an administrator must enable the “Allow use of Copilot cloud agent billed to the organization” policy."
- **Our assessment**: The admin gate is a billing policy, not a review policy; it does not govern what automations may do.

### Claim 6: Shared-automation PRs need an additional approval by default
- **Evidence**: Docs "Security and safety" section (not in changelog).
- **Confidence**: emerging
- **Quote**: "If your repository requires at least one pull request approval, an additional approval is required by default for pull requests created by a shared automation."
- **Our assessment**: A concrete compensating control for Copilot attribution. Docs state admins can disable it in rulesets, but not in branch protection rules. Personal automations' PRs are attributed to the creator, who "can't approve those pull requests."

### Claim 7: Automations are not versioned in Git or reviewed via PRs
- **Evidence**: Docs "Configuration inherited from the repository" section.
- **Confidence**: emerging
- **Quote**: "Automations are stored separately from your repository's contents. They are not committed to Git, so they are not versioned alongside your code or managed through pull requests."
- **Our assessment**: Answers the triage question: edits by write-access users are not PR-reviewed; only the product's "change history" tracks them. The docs point to GitHub Agentic Workflows for automation-as-code reviewed via PRs. This is a real gap against the guide's usual "agent config as reviewed code" advice.

### Claim 8: Tool selection is the main scope control, and AI-credit limits cap spend
- **Evidence**: Docs: tools are GitHub tools (single-repo) or MCP-server tools (not repo-limited); limits per run (minimum 30 credits), daily, weekly, monthly; daily/weekly/monthly don't stop in-progress runs.
- **Confidence**: emerging
- **Quote**: "Selecting tools is the main way you control the scope of an automation."
- **Our assessment**: A tool allowlist plus budget caps is the right shape. Caveat from the docs: MCP tools "aren't limited to that repository," so a write-access editor adding an MCP tool can widen reach beyond the repo.

### Claim 9: Untrusted-input and workflow-run defaults mitigate prompt injection
- **Evidence**: Docs: events from users without write access are ignored by default (opt-in override); Actions workflows don't run on automation PRs until a write-access user approves; sessions are visible to all readers.
- **Confidence**: emerging
- **Quote**: "By default, automations ignore events triggered by users without write access to the repository, to reduce the risk of prompt injection from untrusted users."
- **Our assessment**: Sensible defaults. Note the docs' availability rule that automations are limited to private or internal repos.

### Claim 10: Automations can propose improvements to themselves and other automations
- **Evidence**: Docs "Proposed improvements": notifications, user applies or dismisses.
- **Confidence**: anecdotal (described, no outcome data)
- **Quote**: "Automations can propose improvements to their own tools, triggers, and prompts, and to those of other automations."
- **Our assessment**: Novel self-modifying-config pattern, gated by human approval. Worth tracking; no evidence of effectiveness.

## Concrete Artifacts

```
Personal vs shared (docs.github.com, "Personal and shared automations" table, condensed)
Who can see the automation:        Only you | Everyone with read access
Who can see the automation's runs: Everyone with read access (both)
Who can edit:                      Only you | Everyone with write access
Who is billed for AI credits:      You | The organization or user that owns the repository
Identity used for actions:         Your identity | Copilot's identity
Type is fixed at creation ("You can’t change an automation’s type after you create it.")
```

```
AI credit limits (docs, Billing): per run (min 30), daily (reset 00:00 UTC),
weekly (Monday 00:00 UTC), monthly (1st, 00:00 UTC). Daily/weekly/monthly
do not stop an in-progress run.
```

Changelog example use cases: reproduce bugs when an issue opens; capture screenshots when a PR is marked ready; investigate production incidents detected by monitoring. Availability: Pro, Pro+, Max, Business, Enterprise; VS Code cloud automations need 1.144+ and `chat.automations.cloud.enabled`.

## Cross-References

- **Corroborates**: `docs-github-copilot-automations-comment-trigger.md` Claim 7 (write-access event filter default); the docs page here confirms the filter as a prompt-injection mitigation for all automations.
- **Contradicts**: None filed. Not a contradiction but a supersession: `docs-github-copilot-automations-comment-trigger.md` Claim 6 says automations "are private to their creator"; that now holds only for personal automations.
- **Extends**: `docs-github-copilot-automations-comment-trigger.md` (Claims 5-6: availability and billing) with the shared type; `docs-github-copilot-enterprise-agent-operations-permissions.md` Claim 13, which says managed `permissions.*` rules are not supported in the Copilot cloud agent, so the per-automation tool allowlist is the main available control here; `docs-github-copilot-policies-billing-sept2026.md` for billing policy context (not claim-cited).
- **Novel**: Repo-owned agent workflows with Copilot identity, an extra-approval default on their PRs, non-Git-versioned configuration edited by any writer, and self-proposed improvements.

## Guide Impact

- **Chapter 05**: Add shared automations as an example of agent workflows that survive their author, with the caveat that ownership, billing, and edit rights are decoupled (Claims 1, 2, 4).
- **Chapter 06**: Add the governance gap: automation edits by write-access users are not PR-reviewed (Claim 7), actions are attributed to Copilot (Claim 3), and MCP tools can exceed repo scope (Claim 8). Cite the extra-approval default (Claim 6) as a compensating control.
- **Chapter 02**: Automations as cloud-agent config: prompt + triggers + tool allowlist + credit limits (Claim 8), inheriting repo instructions, skills, firewall, and secrets.

## Extraction Notes

- Fetched the changelog HTML and the linked docs page directly; quotes were copied from the extracted page text. The community discussion link (discussions/211004) was not read.
- Rollout is staged, not GA ("Availability may vary"), hence `emerging`.
- Open questions the sources don't answer: whether change history records the editor's identity; whether tool/trigger edits notify other team members.
