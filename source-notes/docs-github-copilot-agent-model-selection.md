---
source_url: https://github.blog/changelog/2026-04-14-model-selection-for-claude-and-codex-agents-on-github-com
source_type: docs
title: "Model selection for Claude and Codex agents on github.com"
author: GitHub (official changelog)
date_published: 2026-04-14
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: anecdotal
issue: "#171"
---

# Model Selection for Claude and Codex Agents on GitHub.com

> GitHub's April 2026 announcement that model selection (Sonnet vs. Opus tiers for
> Claude; GPT-5.2-Codex through GPT-5.4 for Codex) is now available when kicking off
> tasks with third-party cloud coding agents — establishing feature parity with the
> built-in Copilot agent and introducing a two-layer admin governance model for
> enterprise teams.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words)
- **Author credibility**: GitHub engineering team announcing a production feature change.
  Authoritative for the fact that these model-selection controls now exist and what the
  subscription requirements are. Not a credible source for *which model to use* — the
  changelog implies "select the best model for your task" without any guidance on how to
  determine that.
- **Scope**: Model selection for two specific third-party agent integrations (Anthropic
  Claude and OpenAI Codex) on github.com. Covers available model names, access tiers, and
  admin policy controls. Does NOT cover: how model tier affects task success rates, cost
  differences between Sonnet and Opus in this context, whether the model selection
  propagates to sub-agents in multi-agent workflows, or any performance comparison between
  the listed model versions.

## Extracted Claims

### Claim 1: GitHub now exposes per-task model selection for Claude and Codex agents on github.com

- **Evidence**: Official GitHub product changelog announcing general availability of model
  selection for Claude (Anthropic) and Codex (OpenAI) agents. Feature is described as
  active: "you can now select a model when kicking off a task."
- **Confidence**: settled (product fact — the feature exists and is documented)
- **Quote**: "you can now select a model when kicking off a task—Anthropic models for
  Claude, and OpenAI models for Codex"
- **Our assessment**: This is a tooling-landscape fact. Model selection was previously
  available for GitHub's own Copilot cloud agent; extending it to third-party agents
  establishes a consistent interface. For Ch02: note that cloud coding-agent platforms
  are now surfacing model tier selection as a first-class UI concern, not an invisible
  vendor default. Practitioners who use GitHub-hosted agents need to develop an opinion
  on Sonnet vs. Opus for their workloads — this is a new decision point that did not
  exist before this feature.

### Claim 2: Four Claude model versions are offered — Sonnet 4.5, Opus 4.5, Sonnet 4.6, Opus 4.6

- **Evidence**: Model list enumerated in the changelog: "Claude Sonnet 4.6, Claude Opus 4.6,
  Claude Sonnet 4.5, Claude Opus 4.5."
- **Confidence**: settled (definitional; list stated directly in official changelog)
- **Quote**: (model names listed directly, no surrounding prose quote needed)
- **Our assessment**: The presence of both 4.5 and 4.6 generations, each with both Sonnet
  and Opus variants, creates a 2×2 decision matrix for practitioners. The changelog
  provides no guidance on when to use 4.6 vs. 4.5 or Sonnet vs. Opus. For Ch02: the
  guide should provide this decision framework. Default recommendation: Sonnet 4.6 for
  most coding-agent tasks (lower cost, faster, sufficient for well-specified work);
  Opus 4.6 for tasks requiring deeper reasoning or larger context (e.g., architecture
  analysis, large-codebase refactors). The 4.5 variants exist for backward compatibility
  or cost management but offer no quality advantage over 4.6.

### Claim 3: Three Codex model versions are offered — GPT-5.2-Codex, GPT-5.3-Codex, GPT-5.4

- **Evidence**: Model list enumerated in the changelog.
- **Confidence**: settled (definitional)
- **Quote**: (model names listed directly)
- **Our assessment**: The presence of sub-versions (5.2, 5.3, 5.4) within the Codex family
  mirrors the Claude generational choice. The guide's corpus is more heavily weighted
  toward Anthropic tooling; this is worth noting as a tooling-landscape datapoint that
  GitHub treats OpenAI and Anthropic agents symmetrically in terms of feature exposure.
  For practitioners choosing between Claude and Codex on GitHub: this changelog does not
  provide capability comparison data — defer to `blog-cursor-cursorbench.md` for the
  "evaluate on your own task distribution" methodology rather than relying on public
  benchmarks.

### Claim 4: Model selection parity — third-party Claude and Codex agents now have the same model controls as the built-in Copilot agent

- **Evidence**: The changelog frames this as a parity announcement: model selection was
  already available for the native Copilot agent; this extends the same control surface
  to Claude and Codex. Stated implicitly in the announcement structure, not as an explicit
  quote.
- **Confidence**: emerging (the parity framing is our interpretation of the changelog
  structure; the changelog itself does not use the word "parity")
- **Our assessment**: The strategic signal here is that GitHub is treating third-party AI
  agents as first-class citizens with equivalent operator controls to its own product.
  This matters for enterprise teams comparing GitHub's native Copilot agent against the
  Claude and Codex integrations — they can now make that choice on capability/cost grounds
  rather than on governance-feature grounds (both offer model selection, both require the
  same admin policy enablement). For Ch05: when advising teams on agent platform selection,
  note that GitHub is actively leveling the feature floor across all its hosted agents.

### Claim 5: Access is gated on a two-layer governance model — Copilot subscription plus admin policy enablement

- **Evidence**: Changelog states: Copilot Business or Enterprise subscribers require
  administrator enablement of the relevant policies (Anthropic Claude or OpenAI Codex
  policy). Individual/free subscribers are not addressed.
- **Confidence**: settled (access requirements stated directly in official changelog)
- **Quote**: "Copilot Business or Enterprise subscribers require admin enablement of
  relevant policies (Anthropic Claude or OpenAI Codex)"
- **Our assessment**: This is the most operationally important claim for enterprise teams.
  Two conditions must be met: (1) the organization has Copilot Business or Enterprise,
  and (2) an admin has explicitly enabled the Claude or Codex policy. Engineers cannot
  self-enable — the choice of which third-party AI agents are available is an admin-layer
  governance decision. For Ch05: document this as an enterprise AI governance pattern.
  Organizations that want to limit which AI providers their developers can use can do so
  through these policy controls rather than relying on informal norms. Contrast with
  individual-tool choices (e.g., local Claude Code installations) where individual
  developers control their own model selection without organizational oversight.

### Claim 6: Repository-level enablement is required in addition to org-level policy

- **Evidence**: Changelog states: "repository owners/organizations must enable agents via
  Settings > Copilot > Cloud agent."
- **Confidence**: settled (stated directly in changelog)
- **Quote**: (path: Settings > Copilot > Cloud agent)
- **Our assessment**: The two-step model (org admin enables the policy; repo owner
  enables the agent) gives organizations fine-grained control: even if the org admin
  enables Claude as a policy, individual repositories are not automatically enrolled.
  This is a sensible security design for teams with repos containing sensitive code where
  sending context to a third-party AI provider may require additional review. For Ch02:
  document the repository-level opt-in as a surface where harness configuration decisions
  are made — a team's AI tooling inventory is partially determined at the repository
  settings layer, not just at the developer workstation layer.

### Claim 7: The changelog implies model tier choice matters for task quality, but provides no guidance

- **Evidence**: Prospector triage note; the feature announcement's implicit rationale is
  that different models perform differently, otherwise model selection would be pointless.
  No guidance text, benchmark, or heuristic is provided in the changelog.
- **Confidence**: anecdotal (vendor design decision implies the claim; no evidence cited)
- **Quote**: (implicit in the feature's existence — if models were equivalent, selection
  would add no value)
- **Our assessment**: The existence of the feature is evidence that GitHub and its AI
  partners believe model tier selection affects outcomes. However, the changelog provides
  no practitioner guidance. This is a gap the guide should fill. The question "should I
  use Sonnet 4.6 or Opus 4.6 for this GitHub agent task?" is now a real decision that
  practitioners face, and nothing in this source answers it. Combine with
  `blog-cursor-cursorbench.md` (which argues for task-specific evaluation over benchmark
  scores) to build a recommendation: for routine coding-agent tasks on GitHub, start with
  Sonnet 4.6 and escalate to Opus only for tasks that require broader context or more
  complex reasoning. Track cost alongside outcome metrics.

## Concrete Artifacts

### Model Roster (as of April 14, 2026)

```
GitHub.com Cloud Coding Agents — Available Models

CLAUDE (Anthropic):
  claude-sonnet-4-6    (Claude Sonnet 4.6)  ← current generation, standard tier
  claude-opus-4-6      (Claude Opus 4.6)    ← current generation, high-capability tier
  claude-sonnet-4-5    (Claude Sonnet 4.5)  ← prior generation, standard tier
  claude-opus-4-5      (Claude Opus 4.5)    ← prior generation, high-capability tier

CODEX (OpenAI):
  gpt-5.2-codex        (GPT-5.2-Codex)      ← older Codex generation
  gpt-5.3-codex        (GPT-5.3-Codex)
  gpt-5.4              (GPT-5.4)             ← latest listed in announcement
```

### Access and Governance Checklist

```
Prerequisites for model selection in Claude/Codex agents on GitHub:

Layer 1 — Subscription
  [ ] Copilot Business OR Copilot Enterprise subscription (org or enterprise level)

Layer 2 — Admin Policy (org/enterprise admin required)
  [ ] Enable "Anthropic Claude" policy   (for Claude agent access)
  [ ] Enable "OpenAI Codex" policy       (for Codex agent access)
  Navigate: org Settings > Copilot > Policies > [Third-party agents section]

Layer 3 — Repository Enablement (repo owner required)
  [ ] Enable agents for the specific repository
  Navigate: repo Settings > Copilot > Cloud agent > Enable

At task initiation:
  [ ] Select desired model from dropdown when starting an agent task
```

## Cross-References

- **Corroborates** `docs-github-copilot-pr-review-metrics.md`: both are official GitHub
  Copilot changelog entries documenting progressive enterprise feature additions. That
  source adds measurement primitives for Copilot's effect on PR review; this source adds
  operator control over which AI model runs the agent. Together they show GitHub building
  out an enterprise-grade control surface: measure what Copilot does (metrics), govern
  what AI models it uses (model selection). Both require GitHub Enterprise Cloud and
  admin-layer enablement.
- **Extends** `blog-ghaw-agent-observability.md`: that source covers observability
  architecture for the `gh aw` platform (performance tracking, cost optimization,
  meta-audit). This source adds a new upstream variable to the cost-optimization tier:
  model selection affects cost per agent run. The three-tier observability framework from
  that note should now include model tier as a tracked variable — Opus runs cost
  materially more than Sonnet per token.
- **Extends** `blog-gh-aw-operations-release-workflows.md`: that source documents
  agent-generated PRs using the `gh aw` platform (78% merge rate for Changeset Generator).
  This source adds model selection as a now-explicit parameter for such workflows. The
  Changeset Generator analysis does not report which model was used — practitioners
  replicating those results now have a new variable to control for.
- **Complements** `blog-cursor-cursorbench.md` Claims 1-2: Cursor demonstrates that
  public benchmarks no longer differentiate frontier models — practitioners need
  task-specific evaluation. GitHub exposing model selection implicitly accepts that
  Sonnet and Opus produce different outcomes (otherwise the control would be meaningless).
  The guide should use `blog-cursor-cursorbench.md` to fill the guidance gap that this
  changelog leaves open: how to choose between Sonnet and Opus for a given agent task.
- **Novel**: First source in this corpus specifically documenting model tier selection
  (Sonnet vs. Opus) as an operator-controlled, admin-governed parameter in a cloud
  coding-agent platform. Prior sources discuss model choice in local tools (Claude Code,
  Cursor) but none document it as an organizational governance decision point in a
  hosted-agent context.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model selection as a new configuration surface**: Add a note that GitHub-hosted
  coding agents now require practitioners to have an explicit model selection policy.
  The guide should recommend: default to Claude Sonnet 4.6 for most coding-agent tasks
  (lower cost, lower latency, sufficient for well-specified work); escalate to Opus 4.6
  for tasks requiring deep context analysis, complex multi-file reasoning, or where
  initial Sonnet runs produce insufficient output quality. Document the org admin +
  repo-owner permission model as the GitHub-specific governance path.
- **Third-party agent parity**: Note that GitHub now treats Claude and Codex agents as
  first-class agent integrations with equivalent controls to its own Copilot agent. Teams
  evaluating "should we use GitHub's native Copilot agent or integrate Claude?" should
  weight this feature parity — governance-feature differences no longer favor the native
  agent.

### Chapter 05: Team Adoption / Enterprise Governance

- **Two-layer admin governance as a pattern**: The Copilot Business/Enterprise +
  admin-policy + repo-owner-enablement model is a concrete example of layered AI
  governance in a cloud coding platform. Teams building AI governance policies can
  reference this structure: org-level policy controls which AI providers are permitted;
  repo-level settings control which projects use them; individual users select the
  model at task time within those constraints. This maps to a "central guardrails,
  local agency" governance model that enterprise teams should consider.
- **Model selection as a new training/onboarding need**: Once model selection is exposed,
  engineers need guidance on when to use Sonnet vs. Opus. Without guidance, practitioners
  may default to the highest-capability (most expensive) model for all tasks, or ignore
  the control entirely and always use the default. Recommend teams document their model
  selection heuristics alongside their CLAUDE.md / agent harness configurations.

## Extraction Notes

1. **Source is thin by design**: This is a feature-availability changelog (~300 words).
   All substantive claims are exhausted above. The source does not discuss performance
   characteristics, cost differences, or practitioner experiences with different model
   tiers.
2. **Model names normalized**: The changelog lists model names in plain English. The
   artifact section maps these to API-style identifiers for practical use.
3. **No contradictions to file**: No existing source note claims that GitHub does not
   allow third-party agent model selection, or that Sonnet and Opus produce equivalent
   results for coding-agent tasks. No contradiction issue required.
4. **Individual-tier access not addressed**: The changelog only explicitly addresses
   Business/Enterprise admin policy requirements. Individual/Pro Copilot subscribers
   may have different access — the changelog does not clarify, and this note does not
   speculate.
5. **Feature may evolve rapidly**: Model lists for cloud AI services change frequently
   (new versions added, older versions deprecated). The specific model versions in the
   artifact section (Sonnet/Opus 4.5, 4.6; GPT-5.2 through 5.4) are accurate as of
   the April 14, 2026 announcement. Check the changelog for updates before citing
   specific version names.
