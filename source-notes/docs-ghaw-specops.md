---
source_url: https://github.github.com/gh-aw/patterns/spec-ops
source_type: docs
title: "GitHub Agentic Workflows: SpecOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#353"
---

# GitHub Agentic Workflows: SpecOps Pattern

> First corpus entry for the gh-aw SpecOps pattern — documents how agentic
> workflows maintain formal W3C-style specifications with RFC 2119 keywords and
> automatically propagate changes to consuming repositories via `create-pull-request`
> safe-outputs, using a four-step lifecycle (Update → Review → Propagate → Verify)
> with the `w3c-specification-writer` agent and `strict: true` precision mode.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/spec-ops` page —
  in the same `patterns/` section as `patterns/orchestration` covered by
  `docs-ghaw-orchestration-patterns.md`, `patterns/agentic-ops` covered by
  `docs-ghaw-agentic-ops.md`, and `patterns/multi-repo-ops` covered by
  `docs-ghaw-multi-repo-ops.md`. Patterns pages are practitioner implementation
  references, distinct from the conceptual `introduction/` pages.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's agent factory blog series and the `gh aw`
  platform. Claims about the SpecOps pattern's tooling (`w3c-specification-writer`,
  `layout-spec-maintainer`), workflow structure, and safe-output usage are
  authoritative for the `gh aw` platform. The MCP Gateway Specification reference
  is a first-party live example, not a constructed demo.
- **Scope**: The SpecOps pattern — four-step specification lifecycle, the
  `w3c-specification-writer` agent role, W3C structural requirements, semantic
  versioning for specs, propagation to consuming repositories, compliance test
  updates, YAML workflow configurations, and relationship to MultiRepoOps.
  Does NOT cover: individual safe-output type schemas (see
  `docs-ghaw-safe-outputs-specification.md`), the compilation model in general
  (see `docs-ghaw-how-they-work.md`), or how consuming repositories handle
  the propagated PRs. The page is compact — implementation depth is in the
  companion workflow examples and the `gh-aw-mcpg` reference repository.

## Extracted Claims

### Claim 1: SpecOps is a gh-aw pattern for maintaining formal W3C-style specifications with RFC 2119 keywords and automatically propagating changes across consuming repositories

- **Evidence**: The page opens with: "SpecOps is a pattern for maintaining
  formal specifications using agentic workflows." A broader description states
  the pattern enables teams to "create W3C-style specifications with RFC 2119
  keywords (MUST, SHALL, SHOULD, MAY) and automatically propagates changes to
  consuming implementations across repositories." The pattern is positioned as a
  first-class gh-aw pattern alongside Orchestration, MultiRepoOps, AgenticOps,
  DailyOps, and others.
- **Confidence**: settled (first-party documentation; SpecOps is the pattern's
  named definition page)
- **Quote**: "SpecOps is a pattern for maintaining formal specifications using
  agentic workflows."
- **Our assessment**: SpecOps is a specialized application of agentic automation
  to a domain that benefits strongly from formal structure: specifications that
  must be maintained precisely (RFC 2119 MUST/SHOULD/MAY semantics are binary,
  not interpretive) and that have downstream consumers who must track changes.
  The formal structure is a good fit for agentic maintenance precisely because
  the rules are machine-readable. For Ch02 (Harness Engineering): SpecOps is
  the reference pattern for "agentic maintenance of formal documents" — analogous
  to how the Changeset Generator is the pattern for release changelog automation.
  Both leverage the rule-bound, unambiguous nature of the task.

### Claim 2: The SpecOps lifecycle has four distinct steps — Update, Review, Propagate, Verify — with human approval at step 2 gating the automated propagation

- **Evidence**: The page describes a four-step workflow process:
  1. "Trigger a workflow with the `w3c-specification-writer` agent to edit
     the spec document (RFC 2119 keywords, version bump, change log)."
  2. "Approve the specification pull request."
  3. "On merge, workflows detect updates and create PRs in consuming
     repositories (like gh-aw-mcpg) to maintain compliance."
  4. "Test generation workflows update compliance test suites against the new
     requirements."
  Step 2 (human PR approval) is the gate between the automated update phase
  and the automated propagation phase.
- **Confidence**: settled (first-party documentation; the four steps are the
  pattern's operational definition)
- **Quote**: "On merge, workflows detect updates and create PRs in consuming
  repositories (like gh-aw-mcpg) to maintain compliance."
- **Our assessment**: The human-in-the-loop design at step 2 is the same pattern
  as the Changeset Generator's 78% merge-rate workflow
  (`blog-gh-aw-operations-release-workflows.md` Claim 1, 6): automated proposal,
  human approval gate, then downstream effects. For SpecOps, this is particularly
  important because specification changes carry downstream contractual weight —
  a wrong `MUST` → `SHOULD` change in a merged spec would propagate automatically
  to all consuming repositories. The human gate at merge time is load-bearing,
  not ceremonial. For Ch03 (Safety and Verification): SpecOps is a reference case
  for why even well-scoped agentic tasks with unambiguous criteria still require
  human approval before propagation.

### Claim 3: The `w3c-specification-writer` agent is the named agentic role for editing specifications — operating with `strict: true` precision mode

- **Evidence**: Step 1 of the SpecOps lifecycle identifies the `w3c-specification-writer`
  agent as the workflow actor for specification updates. Both workflow YAML examples
  shown on the page use `engine: copilot` and `strict: true`. The `strict: true`
  flag is a gh-aw engine configuration that constrains the agent to follow
  instructions with high precision rather than using broader interpretive freedom.
- **Confidence**: emerging (the agent name and `strict: true` are documented; the
  full behavior specification of `w3c-specification-writer` is not detailed on
  this page)
- **Quote**: "Trigger a workflow with the `w3c-specification-writer` agent to edit
  the spec document (RFC 2119 keywords, version bump, change log)."
- **Our assessment**: The choice of `strict: true` for specification maintenance
  is architecturally significant. RFC 2119 keyword precision (MUST vs. SHOULD vs.
  MAY carries specific conformance implications) requires a mode where the agent
  follows instructions exactly rather than paraphrasing or simplifying. This
  parallels `docs-ghaw-deterministic-agentic-patterns.md`'s discussion of
  deterministic modes for high-precision tasks. The `w3c-specification-writer`
  agent name implies a purpose-built agent role distinct from general-purpose
  editing agents. For Ch02: when designing workflows for precision-critical
  document editing (specifications, legal language, formal contracts), `strict: true`
  is the appropriate engine mode — not the default.

### Claim 4: Specification propagation to consuming repositories is implemented as a `create-pull-request` safe-output triggered on merge of the specification PR

- **Evidence**: The propagation workflow YAML uses
  `safe-outputs: create-pull-request: title-prefix: "[spec-update] "` with
  labels. The workflow trigger is `on: push: branches: [main]: paths:
  [docs/src/content/docs/reference/mcp-gateway.md]` — detecting merges to
  the spec file's path. The consuming repository mentioned by name is `gh-aw-mcpg`.
- **Confidence**: emerging (the propagation mechanism is documented; the YAML
  examples from the page may be representative rather than verbatim — see
  Extraction Notes)
- **Quote**: "On merge, workflows detect updates and create PRs in consuming
  repositories (like gh-aw-mcpg) to maintain compliance."
- **Our assessment**: The propagation trigger (path-specific push to main) is an
  important design detail: the workflow only fires when the spec file itself changes,
  not on every merge. Combined with `[spec-update]` title prefix and labels, the
  downstream PRs are identifiable and filterable in the consuming repository.
  For Ch04 (Multi-Agent Orchestration): this is a concrete application of the
  upstream-to-downstream MultiRepoOps topology
  (`docs-ghaw-multi-repo-ops.md` Claim 5) — the spec repo is upstream, consuming
  repos are downstream, and the propagation uses `create-pull-request` with
  structured metadata for traceability.

### Claim 5: Compliance test suites in consuming repositories are updated automatically by test generation workflows as a fourth step in the SpecOps lifecycle

- **Evidence**: Step 4 of the four-step process: "Test generation workflows
  update compliance test suites against the new requirements." This step follows
  the propagation of specification PRs to consuming repositories.
- **Confidence**: emerging (the step is named; the implementation details of the
  test generation workflow are not described on this page)
- **Quote**: "Test generation workflows update compliance test suites against the
  new requirements."
- **Our assessment**: The compliance testing step is the most architecturally
  novel element of SpecOps relative to general document automation. A specification
  update that changes a conformance requirement should cause consuming repositories
  to update their test coverage — this closes the loop between the formal spec
  and the implementations. No other source in the corpus documents this automated
  spec-to-test propagation pattern. For Ch02 (Harness Engineering): this is the
  strongest form of "shift left" for specification compliance — rather than
  manually updating tests when a spec changes, the test generation workflow
  does it automatically. The four-step lifecycle (Update → Review → Propagate →
  Verify) is a complete specification change cycle.

### Claim 6: W3C-style specifications in the SpecOps pattern require eight structural elements including Abstract, Status, RFC 2119 keywords, Compliance testing, and a Change log

- **Evidence**: The page defines the structural requirements: "W3C-style
  specifications require: Abstract, Status, Introduction, Conformance, numbered
  technical sections with RFC 2119 keywords, Compliance testing, References, and
  a Change log."
- **Confidence**: settled (first-party documentation; W3C structural requirements
  are an industry standard; the page is providing the implementation in terms of
  that standard)
- **Quote**: "W3C-style specifications require: Abstract, Status, Introduction,
  Conformance, numbered technical sections with RFC 2119 keywords, Compliance
  testing, References, and a Change log."
- **Our assessment**: The W3C structural template gives consuming implementations
  a consistent place to find the normative requirements (numbered technical
  sections with RFC 2119 keywords) and the compliance guidance (Compliance testing
  section). It also gives the changelog section, which enables consuming repos to
  see what changed in version N vs. N-1 without diffing the full document. The
  `docs-ghaw-safe-outputs-specification.md` note is a live example of this
  structure — that spec document uses W3C style with Abstract, Status, numbered
  sections, and conformance classes (Claim 11 there). For Ch05 (Team Adoption):
  when recommending SpecOps to teams managing formal APIs or platform specifications,
  the W3C template is the concrete starting point. Teams don't need to invent their
  own structure — the pattern specifies it.

### Claim 7: SpecOps applies semantic versioning to specifications with the same major/minor/patch logic as software — major for breaking changes, minor for backward-compatible features, patch for bug fixes

- **Evidence**: The page documents the versioning strategy: "Major (X.0.0)
  Breaking changes | Minor (0.Y.0) New features, backward-compatible | Patch
  (0.0.Z) Bug fixes, clarifications."
- **Confidence**: settled (semantic versioning is an established convention;
  the page applies it to specification documents, which is its key contribution)
- **Quote**: (no single verbatim sentence; versioning is rendered as a structured
  table; see paraphrase in Our assessment)
- **Our assessment**: Applying SemVer to specifications signals to consuming
  repositories how disruptive an update is before they read the diff. A major
  version bump on an incoming spec PR signals "your implementation will need to
  change to maintain compliance." A patch bump signals "this is a clarification;
  you may not need to act." This is the same mechanism used by the Changeset
  Generator (`blog-gh-aw-operations-release-workflows.md` Claim 2) for release
  automation — deterministic, rule-bound versioning that agents can apply
  correctly because the rules are unambiguous. For Ch02: recommend SemVer for
  any formal document that is consumed across repositories. The version bump
  itself is communication — it tells downstream consumers what to expect without
  requiring them to read the full diff.

### Claim 8: The MCP Gateway Specification is the live reference example for SpecOps, maintained by the `layout-spec-maintainer` workflow

- **Evidence**: The page states: "The [MCP Gateway Specification](/gh-aw/reference/mcp-gateway/)
  is a live example — maintained by the `layout-spec-maintainer` workflow and
  implemented in [gh-aw-mcpg](https://github.com/github/gh-aw-mcpg)."
- **Confidence**: settled (first-party; the MCP Gateway Specification is a
  real gh-aw document maintained in production)
- **Quote**: "The [MCP Gateway Specification](/gh-aw/reference/mcp-gateway/)
  is a live example — maintained by the `layout-spec-maintainer` workflow and
  implemented in [gh-aw-mcpg](https://github.com/github/gh-aw-mcpg)."
- **Our assessment**: The `layout-spec-maintainer` workflow is a production
  instance of the SpecOps pattern — it is the `w3c-specification-writer` agent
  operating on the MCP Gateway Specification document. The `gh-aw-mcpg` repository
  is a consuming implementation that tracks spec changes via the propagation
  workflow. This gives practitioners a concrete, inspectable example of the
  full SpecOps cycle in production. The relationship to `docs-ghaw-safe-outputs-specification.md`
  (which covers the Safe Outputs MCP Gateway Specification at a different URL)
  is indirect — both concern the MCP Gateway system, but the live SpecOps example
  is the MCP Gateway Specification document at `/gh-aw/reference/mcp-gateway/`,
  not the Safe Outputs specification document. For Ch05: the gh-aw-mcpg repository
  is a reference implementation for teams adopting SpecOps — they can see how
  a real consuming repo integrates spec-tracking workflows.

### Claim 9: SpecOps is related to MultiRepoOps for cross-repository coordination and is positioned alongside TaskOps and SideRepoOps in the pattern ecosystem

- **Evidence**: The page's Related Patterns section links:
  "**[MultiRepoOps](/gh-aw/patterns/multi-repo-ops/)** — Cross-repository coordination"
  SpecOps was also described in the initial issue filing as positioned "alongside
  TaskOps and SideRepoOps in the broader pattern ecosystem."
- **Confidence**: emerging (the MultiRepoOps link is explicit; the TaskOps and
  SideRepoOps positioning is from the issue triage, not from the source page itself)
- **Quote**: "**[MultiRepoOps](/gh-aw/patterns/multi-repo-ops/)** — Cross-repository
  coordination"
- **Our assessment**: The explicit MultiRepoOps link confirms that SpecOps is
  architecturally built on the upstream-to-downstream MultiRepoOps topology.
  SpecOps is the domain-specific specialization (formal specification management)
  of the general MultiRepoOps cross-repo coordination pattern. The relationship
  is analogous to how IssueOps specializes the basic trigger-workflow-safe-output
  pattern for issue events. For Ch04: document SpecOps as an application of
  MultiRepoOps, not a replacement for it — practitioners who understand MultiRepoOps
  can understand SpecOps as "MultiRepoOps with W3C specification semantics."

## Concrete Artifacts

### Update Specification Workflow (spec update trigger)

The source page shows a YAML workflow example for triggering specification updates:

```yaml
---
name: Update MCP Gateway Spec
on:
  workflow_dispatch:
    inputs:
      change_description:
        description: 'What needs to change in the spec?'
        required: true
        type: string
engine: copilot
strict: true
safe-outputs:
  create-pull-request:
    title-prefix: "[spec] "
    labels: [documentation, specification]
tools:
  edit:
  bash:
---
```

*Source: `patterns/spec-ops` — spec update workflow example*
*Note: This YAML may be a representative example rather than verbatim from the
page — see Extraction Notes. The `engine: copilot`, `strict: true`,
`create-pull-request` safe-output, and `[spec]` title-prefix were confirmed as
present in the page's YAML blocks.*

### Propagation Workflow (on merge, push to consuming repos)

The source page shows a YAML workflow example for propagating spec changes:

```yaml
---
name: Propagate Spec Changes
on:
  push:
    branches:
      - main
    paths:
      - 'docs/src/content/docs/reference/mcp-gateway.md'
engine: copilot
strict: true
safe-outputs:
  create-pull-request:
    title-prefix: "[spec-update] "
    labels: [dependencies, specification]
tools:
  github:
    toolsets: [repos, pull_requests]
  edit:
  bash:
---
```

*Source: `patterns/spec-ops` — propagation workflow example*
*Note: Same caveat as above — representative; `[spec-update]` title-prefix and
path-based trigger confirmed.*

### SpecOps Four-Step Lifecycle

From the source page, "How it works" section:

```
Step 1: Update specification
  → Trigger a workflow with the `w3c-specification-writer` agent to edit
    the spec document (RFC 2119 keywords, version bump, change log).

Step 2: Review changes
  → Approve the specification pull request.
  [HUMAN GATE: propagation does not begin until this PR is merged]

Step 3: Propagate automatically
  → On merge, workflows detect updates and create PRs in consuming
    repositories (like gh-aw-mcpg) to maintain compliance.

Step 4: Verify compliance
  → Test generation workflows update compliance test suites against
    the new requirements.
```

*Source: `patterns/spec-ops` — four-step workflow description*

### W3C Specification Structure Requirements

```
Required sections (verbatim from source):
  Abstract
  Status
  Introduction
  Conformance
  Numbered technical sections with RFC 2119 keywords (MUST, SHALL, SHOULD, MAY)
  Compliance testing
  References
  Change log

Semantic versioning:
  Major (X.0.0): Breaking changes
  Minor (0.Y.0): New features, backward-compatible
  Patch (0.0.Z): Bug fixes, clarifications
```

*Source: `patterns/spec-ops` — "Specification structure" section*

### Live Reference Implementation

```
Live example: MCP Gateway Specification
  URL:             https://github.github.com/gh-aw/reference/mcp-gateway/
  Maintained by:   `layout-spec-maintainer` workflow (SpecOps instance)
  Implementation:  github/gh-aw-mcpg (consuming repository)

Pattern:
  layout-spec-maintainer workflow → edits mcp-gateway.md
  → PR opened and reviewed by humans
  → On merge → propagation workflow fires → creates PR in gh-aw-mcpg
  → Test generation workflow updates compliance tests
```

*Source: `patterns/spec-ops` — MCP Gateway Specification reference*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 5 (upstream-to-downstream topology —
    "Main repo propagates changes using `create-pull-request` with `target-repo`
    per downstream"): SpecOps's propagation step (step 3) is a concrete application
    of this topology. The spec repo is the upstream; consuming repos like
    `gh-aw-mcpg` are downstream; `create-pull-request` is the safe-output type
    used for propagation. SpecOps adds the domain-specific layer (W3C structure,
    semantic versioning, compliance testing) on top of the general MultiRepoOps
    mechanism.
  - `docs-ghaw-how-they-work.md` Claim 7 (`.md` → `.lock.yml` compilation model):
    SpecOps workflows use the standard gh-aw compilation model. The `strict: true`
    engine mode is a frontmatter parameter compiled into the lock file. This
    confirms that SpecOps operates within the standard platform compilation model,
    not as a special-case mechanism.
  - `blog-gh-aw-operations-release-workflows.md` Claim 2 (well-defined tasks with
    unambiguous success criteria are suited for agentic automation): SpecOps
    corroborates this from the specification domain. RFC 2119 keyword edits are
    as rule-bound as SemVer bumps — the agent applies formal rules, not
    interpretive judgment. The 78% merge rate for the Changeset Generator suggests
    SpecOps (with similar task structure) would achieve comparable precision.

- **Extends**:
  - `docs-ghaw-multi-repo-ops.md`: That note covers the general upstream-to-
    downstream topology and the `create-pull-request` with `target-repo` mechanism.
    SpecOps adds a domain-specific layer: formal specification documents with
    W3C structure, RFC 2119 keywords, semantic versioning, and compliance testing.
    Together, the two notes give the general pattern (MultiRepoOps) and a
    specific application (SpecOps for formal specification management).
  - `docs-ghaw-safe-outputs-specification.md` Claim 1 (the Safe Outputs MCP
    Gateway Specification is a formal W3C-style document with RFC 2119 requirement
    terminology): The SpecOps page identifies the MCP Gateway Specification
    (at `/gh-aw/reference/mcp-gateway/`) as its live example. These may be
    related but distinct documents; the Safe Outputs spec covers a related system
    (Safe Outputs mechanism) at a different URL. What they share: both are
    formal specification documents using W3C/RFC 2119 conventions — confirming
    that the gh-aw team practices SpecOps on their own specifications.
  - `blog-ghaw-pelis-agent-factory-intro.md` Claim 2 (heterogeneous specialization
    over monolith — "Create many specialized workflows as opportunities emerge"):
    SpecOps is the factory pattern for the specification maintenance opportunity.
    The `w3c-specification-writer` and `layout-spec-maintainer` are specialized
    workflows for this specific task class, not adaptations of a general-purpose
    agent.

- **Contradicts**: None. SpecOps is the first corpus source on formal specification
  maintenance. No existing note makes claims about W3C-style specification workflows
  or RFC 2119 keyword automation. The MultiRepoOps claim that propagation uses
  `create-pull-request` is consistent with the SpecOps propagation mechanism. No
  contradiction issue required.

- **Novel**:
  - **SpecOps as a named gh-aw pattern for formal specification maintenance**
    (Claim 1): No existing corpus note covers the SpecOps pattern. This is the
    first source documenting agentic workflows for maintaining formal specifications
    with RFC 2119 semantics. Entirely new to the corpus.
  - **`w3c-specification-writer` as a named agentic role** (Claim 3): The
    `w3c-specification-writer` agent is not mentioned in any existing source note.
    This is a new named agent role for precision-critical, formal document editing.
  - **Four-step specification change lifecycle** (Claim 2): Update → Review →
    Propagate → Verify. The Verify step (compliance test suite update) is
    particularly novel — no existing corpus note documents automated compliance
    test updates triggered by specification changes.
  - **Automated compliance test generation following spec changes** (Claim 5):
    The pattern of test generation workflows updating compliance test suites after
    a specification merge is not described in any existing source. This closes the
    loop between specification changes and implementation testing in an automated
    cycle.
  - **SemVer for formal specification documents** (Claim 7): Applying SemVer to
    specifications (rather than software) as a communication primitive for consuming
    repositories is not described in any existing note.
  - **`strict: true` engine mode for precision-critical document editing** (Claim 3):
    No existing source note documents the `strict: true` engine configuration or
    distinguishes it from default engine behavior in the context of formal document
    maintenance.
  - **`layout-spec-maintainer` workflow as a production SpecOps instance** (Claim 8):
    The reference to a specific production workflow maintaining the MCP Gateway
    Specification gives practitioners an inspectable live example not documented
    elsewhere in the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add SpecOps as the canonical pattern for formal specification maintenance**
  (Claims 1, 2): When a team maintains a formal specification used by multiple
  consuming repositories, SpecOps is the reference harness design. The four-step
  lifecycle (Update via `w3c-specification-writer` → PR review → propagate via
  `create-pull-request` → update compliance tests) is a concrete harness template.
  Cite the live example (`layout-spec-maintainer` maintaining the MCP Gateway
  Specification in production).

- **Document `strict: true` as the engine mode for precision-critical editing**
  (Claim 3): When a workflow edits formal documents where precision is contractual
  (RFC 2119 keywords, legal language, API contracts), `strict: true` is the
  appropriate mode. Do not use default engine mode for specification maintenance.
  SpecOps is the reference case.

- **Add W3C structural template as a starting point for formal specifications**
  (Claim 6): Eight required sections (Abstract, Status, Introduction, Conformance,
  numbered sections with RFC 2119 keywords, Compliance testing, References,
  Change log). Teams adopting SpecOps should use this template rather than
  inventing their own specification structure.

- **Recommend SemVer for consumed formal documents** (Claim 7): Apply major/minor/
  patch versioning to any formal document consumed across repositories. The version
  bump on the propagated PR signals the change magnitude to consuming teams before
  they read the diff.

### Chapter 04: Multi-Agent Orchestration

- **Position SpecOps as a domain-specific MultiRepoOps application** (Claims 4, 9):
  SpecOps is not a standalone pattern but an application of the upstream-to-downstream
  MultiRepoOps topology to formal specification documents. Practitioners who understand
  MultiRepoOps Claim 5 (`create-pull-request` with `target-repo` per downstream)
  can understand SpecOps as the same mechanism with W3C semantics. Cross-reference
  `docs-ghaw-multi-repo-ops.md`.

- **Add the automated compliance test propagation cycle** (Claims 4, 5): The
  propagation trigger (path-based push to main) + test generation workflow forms
  a two-step event chain: spec merge → propagate PRs → update compliance tests.
  This is a multi-workflow event chain not documented elsewhere for this use case.

### Chapter 05: Team Adoption

- **Identify specification-managing teams as a SpecOps adoption target** (Claims
  1, 8): Teams that maintain formal API specifications, platform contracts, or
  protocol documents used by multiple consuming repositories are the primary SpecOps
  audience. The adoption signal: if a specification change requires manually updating
  multiple downstream repositories, SpecOps is the pattern to adopt. Reference the
  `gh-aw-mcpg` consuming repository as an inspectable example of downstream
  integration.

- **Use the MCP Gateway Specification as a template reference** (Claim 8):
  Practitioners can inspect the MCP Gateway Specification at
  `https://github.github.com/gh-aw/reference/mcp-gateway/` as a live example of
  the W3C template structure in use. The `layout-spec-maintainer` workflow is the
  production SpecOps instance they can adapt.

## Extraction Notes

1. **Source is compact**: The `patterns/spec-ops` page is shorter than most gh-aw
   documentation (consistent with other `patterns/` pages). The information density
   is in the four-step lifecycle, the YAML examples, and the W3C structural
   requirements. Claims were exhausted in 9 extractions; this is consistent with
   the pattern's compact presentation format.

2. **YAML examples may be representative rather than character-perfect**: The
   WebFetch model reported that the page displays two workflow YAML blocks, and
   confirmed the presence of `engine: copilot`, `strict: true`, `create-pull-request`
   safe-output, and the `[spec]`/`[spec-update]` title prefixes. However, the
   full YAML reproduced in Concrete Artifacts was reconstructed by the WebFetch
   model rather than directly extracted character-for-character. The YAML blocks
   should be treated as representative configurations, not verbatim source artifacts.
   An Assayer wanting to verify should check the source URL directly.

3. **MCP Gateway Specification vs. Safe Outputs MCP Gateway Specification**:
   The SpecOps page references `/gh-aw/reference/mcp-gateway/` as the live example.
   `docs-ghaw-safe-outputs-specification.md` covers a document at
   `/gh-aw/reference/safe-outputs-specification`. These are different documents.
   Both concern the gh-aw MCP gateway system, but the live SpecOps example (the
   one maintained by `layout-spec-maintainer`) is the `mcp-gateway` document,
   not the `safe-outputs-specification`.

4. **`w3c-specification-writer` agent not further described**: The page names the
   agent but does not describe its system prompt, training, or configuration
   constraints beyond the `strict: true` engine mode. A dedicated source note on
   the agent configuration (if one exists in the gh-aw documentation) would fill
   this gap.

5. **TaskOps and SideRepoOps positioning**: The issue triage mentioned SpecOps is
   "positioned alongside TaskOps and SideRepoOps in the broader pattern ecosystem."
   This was not confirmed on the source page (the Related Patterns section only
   links MultiRepoOps explicitly). TaskOps and SideRepoOps are gh-aw patterns
   mentioned in `docs-ghaw-ephemerals.md` and other notes; their relationship to
   SpecOps is not documented on this page.

6. **No publication date**: The documentation does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with post-January
   2026 gh-aw documentation based on the `gh-aw-mcpg` repository reference.

7. **No contradictions to file**: Reviewed all existing gh-aw source notes against
   all claims. No claims here materially oppose any existing source note. The
   MultiRepoOps upstream-to-downstream topology is consistent with (and confirmed
   by) SpecOps's propagation mechanism. No contradiction issue filed.
