---
source_url: https://github.github.com/gh-aw/experimental/enclaves
source_type: docs
title: "GitHub Agentic Workflows: Private Repository Enclaves (Experimental)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: emerging
issue: "#3106"
---

# GitHub Agentic Workflows: Private Repository Enclaves (Experimental)

> Reference documentation for `enclaves`, an experimental gh-aw feature that grants
> finite-disclosure, gateway-mediated read access to approved private repositories via
> isolated "script" or "agent" enclave executors — with masked per-run capabilities,
> a closed `issues-read-v1` REST-only GitHub Issues profile, integrity-floor
> inheritance, and a numeric timeout-bucket contract tied to a specific upstream
> firewall implementation (`github/gh-aw-firewall#6992`).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `experimental/enclaves` page —
  in the `experimental/` tier alongside `experimental/drive-memory` (previous page,
  already mined as `docs-ghaw-drive-memory.md`) and `experimental/trace-graders`
  (next page, not mined). Experimental pages document preview/in-progress features
  distinct from the generally-available `reference/` tier that covers
  `reference/mcp-gateway`, `reference/github-tools`, `reference/integrity`, etc.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind the `gh aw` CLI and the rest of the `gh-aw` documentation mined
  throughout this corpus. Configuration syntax, timeout values, version requirements,
  and security-invariant statements ("workflows cannot override these security
  invariants") are authoritative platform specifications. The page carries no
  explicit "preview enrollment required" gate (unlike `docs-ghaw-drive-memory.md`
  Claim 1's private-preview enrollment requirement) but does gate the feature behind
  an unreleased upstream dependency (Claim 6 below), which functions as a similar
  practical gate.
- **Scope**: The entire page — one short intro, a configuration example, key
  constraints, gateway security details, version requirements, a second section on
  the `issues-read-v1` GitHub Issues profile for agent enclaves (permitted
  operations, integrity/data-access rules, implementation details, token
  configuration, minimum supported versions), and a "Related Documentation" footer
  linking to `experimental/drive-memory` and `experimental/trace-graders`. Does NOT
  cover: how to request access to the `awf-enclave` MCP route generally, the
  `enclave_run_script`/`enclave_run_agent` execution semantics beyond their names,
  a worked end-to-end example combining both enclave types with real repository
  data, or the `experimental/trace-graders` page (not followed — see Extraction
  Notes).

## Extracted Claims

### Claim 1: The top-level `enclaves` array enables finite-disclosure access to approved private repositories; the compiler registers `enclave_run_script` or `enclave_run_agent` from the keyed entries on the `awf-enclave` MCP route, and omitting the array disables the feature entirely

- **Evidence**: Opening two sentences of the page describe the array's purpose and
  the compiler's registration behavior.
- **Confidence**: settled (first-party documentation stating the feature's exact
  activation mechanism)
- **Quote**: "The top-level enclaves array enables finite-disclosure access to
  approved private repositories. The compiler registers enclave_run_script or
  enclave_run_agent from the keyed entries present on the awf-enclave MCP route.
  Omit the array to disable enclaves."
- **Our assessment**: "Finite-disclosure" is the load-bearing term for this entire
  feature — it names a data-access model distinct from both the primary-agent
  GitHub Tools default scope (`docs-ghaw-github-tools.md` Claim 4: current repo +
  all public repos) and the integrity-filtering trust model
  (`docs-ghaw-integrity-reference.md` Claim 1: filters by author trust, not
  repository membership). Enclaves instead scope access by *which specific private
  repository* an executor is allowed to touch, with a bounded and enumerable set of
  operations against it. For Ch02 (Harness Engineering): document `enclaves` as the
  mechanism for "this agent may read exactly these named private repositories and
  nothing else," distinct from broadening the primary agent's GitHub token scope.

### Claim 2: Enclaves require AWF network isolation, which every supported `sandbox.agent.runtime` profile provides; the compiler launches mcpg in bridge mode and AWF attaches it to the isolated topology

- **Evidence**: Second paragraph of the page states the dependency on AWF network
  isolation and names the specific mechanism (mcpg bridge mode).
- **Confidence**: settled (first-party documentation of an architectural
  prerequisite)
- **Quote**: "Enclaves require AWF network isolation, which every supported
  sandbox.agent.runtime profile provides, so the compiler launches mcpg in bridge
  mode and AWF can attach it to the isolated topology."
- **Our assessment**: The phrase "every supported sandbox.agent.runtime profile
  provides" ties enclaves to the runtime taxonomy documented in
  `docs-ghaw-agent-runtimes-reference.md` Claim 1 (`sandbox.agent.runtime`:
  Docker/gVisor/Docker sbx) — enclaves are runtime-agnostic in the sense that they
  work identically across all three isolation tiers, because the property they
  depend on (AWF network isolation) is present in all of them, not just the
  strongest ones. This is useful for harness engineers choosing a runtime for other
  reasons (compatibility, cost) without needing to separately verify enclave
  compatibility.

### Claim 3: Each enclave type (`script` or `agent`) may appear at most once; when the same repository appears in both a script and an agent entry, its sensitivity must match because the information budget is shared across executor types, and AWF fixes both enclave networks internally so workflows cannot override these security invariants

- **Evidence**: The "Key Constraints" section states the one-per-type limit, the
  cross-type sensitivity-matching rule and its rationale, and the network-fixing
  statement.
- **Confidence**: settled (first-party documentation of hard configuration
  constraints, not recommendations)
- **Quote**: "Each type can appear at most once. When the same repository appears
  in both entries, its sensitivity must match because its information budget is
  shared across executor types. AWF fixes the script enclave network and
  interpreter and the agent enclave network internally; workflows cannot override
  those security invariants."
- **Our assessment**: "Workflows cannot override these security invariants" is the
  most consequential sentence in the constraints section for a harness engineer
  evaluating whether enclaves fit a use case that needs custom network rules per
  enclave — the answer is no, by design. The shared-information-budget rule for a
  repository appearing in both script and agent entries means sensitivity
  classification is a property of the *repository*, not of the executor accessing
  it, which prevents a workflow from declaring the same repo `confidential` for the
  script enclave and (accidentally or intentionally) a laxer level for the agent
  enclave to bypass restrictions.

### Claim 4: The gateway generates a fresh masked capability for each workflow run, excluded from the primary agent's environment and passed only to mcpg and AWF; it allows 120 seconds for the AWF-owned HTTP upstream to become available

- **Evidence**: First two sentences of the "Gateway Security Details" material (per
  the raw page text, this is presented as continuous prose rather than a bulleted
  list).
- **Confidence**: settled (first-party documentation of the capability-issuance and
  upstream-availability mechanism)
- **Quote**: "The generated gateway upstream uses a fresh masked capability for each
  workflow run. That capability is passed only to mcpg and AWF and is excluded from
  the primary agent environment. The gateway allows 120 seconds for the AWF-owned
  HTTP upstream to become available."
- **Our assessment**: "Excluded from the primary agent environment" is the
  enclave-specific instance of the general isolation guarantee documented in
  `docs-ghaw-mcp-gateway-reference.md` Claim 10 (credential isolation: "The gateway
  MUST NOT allow servers to access each other's configuration") — here the specific
  credential being isolated is the masked capability itself, and the isolation
  boundary is between the primary agent process and the enclave/gateway machinery,
  not between two co-hosted MCP servers. The per-run freshness (a new capability
  every workflow run, not a reused long-lived one) limits the blast radius of a
  leaked capability to a single run.

### Claim 5: The gateway enforces a 4,860-second tool timeout (AWF's maximum 4,800-second finite-disclosure timing bucket plus a 60-second transport allowance); executor timeouts are capped at 4,740 seconds because AWF reserves 60 seconds in the final bucket for processing and cleanup; the gateway timeout is an enforcement bound, not an absolute AWF wall-clock guarantee under pathological host cleanup or scheduler stalls

- **Evidence**: Remainder of the "Gateway Security Details" paragraph, giving the
  exact second counts and their derivation.
- **Confidence**: settled (first-party documentation with precise numeric values
  and an explicit accounting of how they combine)
- **Quote**: "It enforces a 4,860-second tool timeout, covering AWF's maximum
  4,800-second finite-disclosure timing bucket plus a 60-second transport
  allowance. Executor timeouts are capped at 4,740 seconds because AWF reserves
  60 seconds in the final bucket for processing and cleanup. The gateway timeout is
  an enforcement bound, not an absolute AWF wall-clock guarantee under pathological
  host cleanup or scheduler stalls."
- **Our assessment**: This is a distinct, enclave-specific timeout system from the
  general MCP Gateway's default startup/tool-invocation timeouts documented in
  `docs-ghaw-mcp-gateway-reference.md` Claim 8 (30-second startup default,
  60-second tool-invocation default) — a harness engineer should not conflate the
  two. The enclave numbers (4,800s / 60s / 4,860s / 4,740s) describe a much
  longer-running budget appropriate for an agent enclave session (up to ~80
  minutes), not a single tool call. The explicit caveat that the bound is "not an
  absolute AWF wall-clock guarantee under pathological host cleanup or scheduler
  stalls" is an honest disclosure that the numeric contract can be exceeded under
  failure conditions — worth flagging for anyone building monitoring/alerting
  around enclave session duration.

### Claim 6: The enclave compiler contract depends on the unified enclave implementation from `github/gh-aw-firewall#6992`; pinning an older AWF version will not provide the enclave server

- **Evidence**: Final sentence of the first page section.
- **Confidence**: settled (first-party statement of an upstream dependency, though
  the dependency issue itself is external and unverified by this extraction)
- **Quote**: "This compiler contract depends on the unified enclave implementation
  from github/gh-aw-firewall#6992. Until that change is available in an AWF
  release, pinning an older AWF version will not provide the enclave server."
- **Our assessment**: `github/gh-aw-firewall` is the same upstream repository named
  in `blog-ghaw-weekly-2026-06-29.md` Claim 4 as the source of the `gh-aw-firewall`
  runtime component (there tracked at v0.27.12 → v0.27.13 via PR #42146) — i.e.,
  "AWF" as used throughout this page is the `gh-aw-firewall` component, and the
  enclave feature's availability is gated on a specific unmerged/unreleased issue
  in that repository, not merely on a documentation flag. This is a stronger and
  more externally-verifiable gate than a "beta" label: a harness engineer can check
  the linked issue's status before attempting to adopt the feature.

### Claim 7: Agent enclaves can opt into the closed `issues-read-v1` profile, which is the only accepted `agent.github.cli` value; script enclaves cannot configure `github` at all; the first profile version accepts at most one repository whose sensitivity is not `public`, and any additional assigned repositories must declare `sensitivity: public`

- **Evidence**: Opening paragraph and constraints of the "GitHub Issues access from
  agent enclaves" section, with a YAML configuration example showing
  `github: cli: issues-read-v1` under an `agent` enclave entry.
- **Confidence**: settled (first-party documentation of a closed, versioned profile
  with explicit per-repository sensitivity limits)
- **Quote**: "issues-read-v1 is the only accepted agent.github.cli value. Script
  enclaves cannot configure github. The first profile version accepts at most one
  repository whose sensitivity is not public; additional assigned repositories must
  declare sensitivity: public."
- **Our assessment**: The "first profile version" phrasing signals this is
  explicitly designed to be extended (implying a future `issues-read-v2` or similar
  with a relaxed single-non-public-repo limit), which is useful context for a
  practitioner deciding whether to design around today's one-confidential-repo
  ceiling or wait for a later version. The script/agent asymmetry (only agent
  enclaves get `github.cli`) means script enclaves are limited to whatever their
  `repos` configuration grants at the repo-checkout level (not documented on this
  page) without a GitHub API surface at all.

### Claim 8: The `issues-read-v1` profile permits only three paginated REST GET routes; practitioners must use carefully formed `gh api --method GET ...` requests because stock `gh issue` commands are not guaranteed (they commonly use GraphQL); GraphQL, search, writes, and every other REST path are denied

- **Evidence**: The "permitted operations" list of three routes, followed by
  explicit guidance on required tooling and a denial statement.
- **Confidence**: settled (first-party enumeration of an allowlist, which is by
  construction exhaustive — anything not listed is denied)
- **Quote**: "GraphQL, search, writes, and every other REST path are denied."
- **Quote** (routes): "GET /repos/{owner}/{repo}/issues", "GET
  /repos/{owner}/{repo}/issues/{number}", "GET
  /repos/{owner}/{repo}/issues/{number}/comments"
- **Our assessment**: This is the narrowest documented GitHub API surface anywhere
  in the corpus — three read-only, paginated REST routes, versus the 18-toolset
  catalogue available to the primary agent's `tools.github` configuration
  (`docs-ghaw-github-tools.md` Claim 2). The explicit warning that "stock gh issue
  commands are not guaranteed" because they "commonly use GraphQL" is a practical
  gotcha: an agent enclave author who reaches for the ergonomic `gh issue list` or
  `gh issue view` CLI commands (the natural first instinct) may find them silently
  failing or blocked, and must instead hand-construct `gh api --method GET`
  requests against the three named paths.

### Claim 9: Public issue data uses the primary GitHub source's effective `min-integrity` (an explicit `tools.github.min-integrity` is inherited, otherwise the compiler default is `approved`, and the enclave entry cannot weaken this floor); other repositories are available only when an exact visibility check reports them public, with all other failures receiving the same denial; private repository responses carry a `private:<owner>/<repo>` DIFC secrecy label

- **Evidence**: The "Data Integrity and Access" material (unlabeled as a section
  heading in the raw text, but a distinct paragraph) describing the integrity-floor
  inheritance rule, the visibility-check behavior, and the secrecy-label mechanism.
- **Confidence**: settled (first-party documentation of an access-control floor and
  a labeling mechanism, stated as unconditional platform behavior)
- **Quote**: "An explicit tools.github.min-integrity is inherited; otherwise the
  compiler uses the primary-agent default, approved. The enclave entry cannot
  weaken this floor."
- **Quote** (secrecy label): "Private repository responses carry the
  private:<owner>/<repo> DIFC secrecy label."
- **Our assessment**: This directly corroborates and reuses the DIFC (a term
  established in `docs-ghaw-integrity-reference.md`, where filtered items are
  logged as `DIFC_FILTERED` events) machinery from the general integrity-filtering
  system, and corroborates `docs-ghaw-integrity-reference.md` Claim 4's statement
  that public repositories automatically receive `min-integrity: approved`
  protection by default — the enclave's default-to-`approved` behavior for public
  issue data is the same default, applied in a narrower context. The
  "enclave entry cannot weaken this floor" statement means an agent enclave author
  cannot use enclave configuration to loosen integrity filtering below what the
  primary agent's own `tools.github.min-integrity` setting establishes — the
  enclave is strictly more restrictive, never less. "All other failures receive
  the same denial" (i.e., a repo that fails the visibility check is denied
  identically regardless of the specific reason) is a deliberate anti-enumeration
  design: an attacker probing enclave behavior cannot distinguish "repo doesn't
  exist," "repo is private and not the assigned one," or "visibility check
  errored" from the response shape alone.

### Claim 10: The compiler starts a dedicated mcpg proxy in Docker bridge mode holding the PAT; AWF attaches it to a private control network, mints a short-lived `awf-egh1` capability into a mode-`0600` file, and exposes only an AWF-owned PAT-free local CLI proxy to the enclave — neither the primary agent nor the enclave ever receives the PAT, the mcpg address, the root key, container identity, the CA path, or the repository catalog

- **Evidence**: The "Implementation Details" paragraph, listing the specific
  artifacts withheld from both the primary agent and the enclave.
- **Confidence**: settled (first-party documentation of a specific, named isolation
  architecture with concrete artifact names)
- **Quote**: "The compiler starts a dedicated mcpg proxy in Docker bridge mode. The
  PAT remains in that proxy. AWF attaches it to a private control network, mints a
  short-lived awf-egh1 capability into a mode-0600 file, and exposes only an
  AWF-owned PAT-free local CLI proxy to the enclave. Neither the primary agent nor
  the enclave receives the PAT, mcpg address, root key, container identity, CA
  path, or repository catalog."
- **Our assessment**: This is the single most detailed concrete security artifact
  in the source: the named capability (`awf-egh1`), the exact file permission mode
  (`0600`), and an enumerated six-item list of what is deliberately withheld from
  *both* the agent and its own enclave (not just from the agent). The design
  pattern — a proxy holds the real credential, only a scoped and unnamed local CLI
  surface is exposed to the consumer — matches the "PAT-free" pattern already
  documented for the general GitHub Tools `gh-proxy` transport mode
  (`docs-ghaw-github-tools.md` Claim 3), but goes further: even the enclave itself,
  which is the intended consumer of the private repository data, never sees the
  proxy's network address or the credential backing it. This is a concrete,
  citable example of "least agency" (`blog-anthropic-zero-trust-ai-agents.md`
  Claim 5) applied at the infrastructure level — the enclave gets exactly the
  narrow REST surface it needs (Claim 8) and none of the underlying plumbing.

### Claim 11: Agent enclaves must be provided `GH_AW_GITHUB_MCP_SERVER_TOKEN` or `GH_AW_GITHUB_TOKEN` with read access to the assigned repository's Issues; the fallback `GITHUB_TOKEN` can only access repositories that token can already read, typically just the current repository in Actions

- **Evidence**: "Token Configuration" paragraph naming the two acceptable secrets
  and describing the fallback's limitation.
- **Confidence**: settled (first-party documentation of token requirements)
- **Quote**: "Provide GH_AW_GITHUB_MCP_SERVER_TOKEN or GH_AW_GITHUB_TOKEN with read
  access to the assigned repository's Issues. The fallback GITHUB_TOKEN can only
  access repositories that token can already read (typically just the current
  repository in Actions)."
- **Our assessment**: `GH_AW_GITHUB_MCP_SERVER_TOKEN` is the same magic-secret name
  documented in `docs-ghaw-github-tools.md` Claim 5 (auto-used by the primary
  agent's GitHub Tools without explicit workflow reference) and
  `docs-ghaw-multi-repo-ops.md` Claim 9, but here it serves a narrower purpose:
  granting the *enclave's* scoped `issues-read-v1` profile read access to one
  assigned private repository, not broadening the primary agent's general GitHub
  Tools scope. A practitioner already using this secret for primary-agent cross-repo
  reads should not assume it automatically also authorizes an agent enclave — the
  enclave still requires the token to have read access to the specific assigned
  repository's Issues, and the enclave's own visibility/integrity checks (Claim 9)
  apply independently of how broadly the underlying token itself is scoped.

### Claim 12: The minimum supported versions for the `issues-read-v1` profile are AWF `v0.28.9` and mcpg `v0.4.13`; the compiler does not fall back to older versions

- **Evidence**: Final "Minimum Supported Versions" statement of the page.
- **Confidence**: settled (first-party documentation of explicit version floors)
- **Quote**: "The minimum supported versions are AWF v0.28.9 and mcpg v0.4.13. The
  compiler does not fall back to older versions."
- **Our assessment**: These are specific, checkable version numbers a harness
  engineer can compare against their pinned `gh-aw-firewall` (AWF) and `gh-aw-mcpg`
  (mcpg) versions — both named as tracked runtime components in
  `blog-ghaw-weekly-2026-06-29.md` Claim 4 (which recorded `gh-aw-mcpg` at
  v0.3.31 → v0.3.32 and `gh-aw-firewall` at v0.27.12 → v0.27.13 as of that post's
  PR #42146). Both of those weekly-post version numbers are well below the
  v0.28.9/v0.4.13 floor stated here, indicating the enclave feature (and
  specifically the `issues-read-v1` profile) requires materially newer releases
  than what was current as of that mid-2026 weekly update — consistent with this
  being a recently-shipped, still-experimental capability rather than a
  long-available one.

## Concrete Artifacts

### Configuration Example — Script and Agent Enclaves (verbatim from source)

```yaml
sandbox:
  agent:
    id: awf
enclaves:
  - script:
      repos:
        - repo: octo-org/private-service
          sensitivity: confidential
      timeout: 45
  - agent:
      model: gpt-5
      repos:
        - repo: octo-org/private-service
          sensitivity: confidential
      timeout: 180
```

*Source: `https://github.github.com/gh-aw/experimental/enclaves` — top configuration example*

### Configuration Example — `issues-read-v1` Agent Enclave (verbatim from source)

```yaml
sandbox:
  agent:
    id: awf
  mcp:
    version: v0.4.13
enclaves:
  - agent:
      model: gpt-5
      github:
        cli: issues-read-v1
      repos:
        - repo: octo-org/private-service
          sensitivity: confidential
      timeout: 180
```

*Source: `https://github.github.com/gh-aw/experimental/enclaves` — "GitHub Issues access from agent enclaves" section*

### Permitted `issues-read-v1` REST Routes (verbatim from source)

```
GET /repos/{owner}/{repo}/issues
GET /repos/{owner}/{repo}/issues/{number}
GET /repos/{owner}/{repo}/issues/{number}/comments
```

*Source: `https://github.github.com/gh-aw/experimental/enclaves` — "GitHub Issues access from agent enclaves" section, permitted operations list*

### Timeout Bucket Arithmetic (as stated in source, not independently verified)

```
AWF finite-disclosure timing bucket (max):     4,800 s
+ transport allowance:                         +  60 s
= Gateway-enforced tool timeout:                4,860 s

AWF final-bucket reservation (cleanup/processing): 60 s
= Executor timeout cap:            4,800 s - 60 s = 4,740 s
```

*Derived directly from the source's prose: "a 4,860-second tool timeout, covering
AWF's maximum 4,800-second finite-disclosure timing bucket plus a 60-second
transport allowance," and "Executor timeouts are capped at 4,740 seconds because
AWF reserves 60 seconds in the final bucket for processing and cleanup."*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-integrity-reference.md` Claim 4 (public repositories automatically
    receive `min-integrity: approved` protection without any configuration; private
    and internal repositories have no default guard policy): Claim 9 here states
    the same default explicitly for enclave public-issue-data access — "otherwise
    the compiler uses the primary-agent default, approved." The enclave applies
    this identical default in a narrower, private-repo-scoped context, and adds
    that the enclave configuration can never weaken it.
  - `docs-ghaw-mcp-gateway-reference.md` Claim 10 (four-property container
    isolation guarantee: process, environment variable, credential, and volume
    mount isolation between co-hosted MCP servers, with the gateway "MUST NOT
    allow servers to access each other's configuration"): Claim 10 here is a
    concrete enclave-specific instance of the credential-isolation property —
    the PAT never leaves the dedicated mcpg proxy, and neither the primary agent
    nor the enclave itself receives the PAT, mcpg address, root key, container
    identity, CA path, or repository catalog.
  - `docs-ghaw-github-tools.md` Claim 3 (`gh-proxy` transport mode uses a
    pre-authenticated `gh` CLI directly, avoiding exposing raw credentials to the
    workflow): the enclave's "AWF-owned PAT-free local CLI proxy" (Claim 10) is
    architecturally the same PAT-shielding pattern — a proxy fronts the real
    credential and only a scoped CLI surface reaches the consumer — applied at the
    enclave layer rather than the primary-agent transport-mode layer.

- **Extends**:
  - `docs-ghaw-github-tools.md` Claim 5 and `docs-ghaw-multi-repo-ops.md` Claim 9
    (the `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret is auto-used by the primary
    agent's GitHub Tools for cross-repo reads without explicit workflow reference):
    Claim 11 here shows the *same* secret name serving a second, narrower purpose —
    authorizing an agent enclave's `issues-read-v1` profile to read one assigned
    repository's Issues via three fixed REST routes, not broadening the primary
    agent's general toolset scope. Neither prior note anticipated this second use;
    a practitioner should not assume setting the secret for one purpose
    automatically grants the other.
  - `docs-ghaw-agent-runtimes-reference.md` Claim 1 (the `sandbox.agent.runtime`
    taxonomy: Docker default, gVisor, Docker sbx): Claim 2 here adds that enclaves
    depend only on AWF network isolation, which "every supported
    sandbox.agent.runtime profile provides" — enclaves work uniformly across all
    three runtime tiers documented in that note, without a runtime-specific
    compatibility caveat (contrast with that note's Claims 3–4, where gVisor and
    Docker sbx are each incompatible with the separate `runner.topology: arc-dind`
    field).
  - `blog-ghaw-weekly-2026-06-29.md` Claim 4 (runtime components `gh-aw-mcpg` and
    `gh-aw-firewall`, tracked with SHA-pinned digests, at v0.3.31→v0.3.32 and
    v0.27.12→v0.27.13 respectively as of PR #42146): Claims 6 and 12 here name the
    same two components — "AWF" as `gh-aw-firewall` (dependency on
    `github/gh-aw-firewall#6992`, minimum v0.28.9) and "mcpg" as `gh-aw-mcpg`
    (minimum v0.4.13) — and show that the enclave feature's version floor is well
    above what that mid-2026 weekly post recorded as current, indicating enclaves
    require materially newer releases of both components than were shipping a few
    months prior.
  - `docs-ghaw-drive-memory.md`: navigationally adjacent (the enclaves page's
    "Related Documentation" footer links back to
    `/gh-aw/experimental/drive-memory/`, and that note's own page is listed as the
    immediately preceding page in the `experimental/` section). Both are
    feature-gated preview capabilities in the same documentation tier, each with
    explicit minimum-version or enrollment requirements, but they cover unrelated
    functionality (memory storage backend vs. private-repo access scoping) — no
    content overlap beyond the shared experimental-tier pattern.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 5 ("least agency" — restricting
    what each agent tool can do, how often, and where, extending least privilege to
    agentic systems): the `issues-read-v1` profile (Claims 7–8: one closed profile
    name, three fixed REST GET routes, denial of GraphQL/search/writes) is a
    concrete, platform-enforced example of least agency applied to GitHub API
    access from an agent enclave — narrower than the primary agent's 18-toolset
    catalogue (`docs-ghaw-github-tools.md` Claim 2) by design.

- **Contradicts**: None identified. The enclave's repository-scoped, capability-based
  access model (Claims 1–4, 10) is a different control axis from
  `docs-ghaw-integrity-reference.md` Claim 1's trust-based content filtering (which
  operates on *which authors'* content reaches the agent within a repository the
  agent can already access) — the two mechanisms are complementary layers (repo
  access scoping vs. within-repo content trust filtering), not competing or
  conflicting descriptions of the same control. No contradiction issue required.

- **Novel**:
  - **The entire private-repository-enclave finite-disclosure access model**
    (Claims 1–4): no existing source note in the corpus documents a mechanism for
    scoping agent access to a specific, named set of private repositories with
    per-repository sensitivity levels and separate script/agent executor types.
    This is new to the corpus.
  - **The numeric enclave timeout-bucket contract** (Claim 5: 4,800s AWF bucket +
    60s transport = 4,860s gateway timeout; 4,740s executor cap): distinct from
    and much longer than the general MCP Gateway's 30s/60s startup/tool-invocation
    defaults in `docs-ghaw-mcp-gateway-reference.md` Claim 8 — no existing note
    documents this enclave-specific timeout arithmetic.
  - **The `issues-read-v1` closed profile and its three-route allowlist**
    (Claims 7–8): the narrowest GitHub API surface documented anywhere in the
    corpus, and the first documented case of a `gh api --method GET` requirement
    because stock `gh issue` CLI commands are not guaranteed to avoid GraphQL.
  - **The `awf-egh1` capability name, mode-`0600` file exposure mechanism, and the
    explicit six-item withheld-artifact list (PAT, mcpg address, root key,
    container identity, CA path, repository catalog)** (Claim 10): a level of
    named implementation detail not present in the more architecture-level
    `docs-ghaw-mcp-gateway-reference.md` isolation claims.
  - **The `private:<owner>/<repo>` DIFC secrecy label for private repository
    responses** (Claim 9): extends the DIFC/`DIFC_FILTERED` terminology from
    `docs-ghaw-integrity-reference.md` with a new, repository-scoped label variant
    not documented in that note.
  - **The `github/gh-aw-firewall#6992` unified-enclave-implementation dependency**
    (Claim 6): a specific, externally-checkable upstream gate for feature
    availability, not previously named in the corpus.

## Guide Impact

### Chapter 06: Security and Threat Model

- **Add private repository enclaves as a named repo-access-scoping control**
  (Claims 1, 3, 9, 10): distinct from both the primary-agent GitHub Tools default
  scope and integrity filtering, enclaves let a harness engineer grant an agent (or
  a non-agentic script executor) read access to exactly one or a small enumerated
  set of private repositories, with a closed API surface for the agent case. Cite
  this as a concrete "least agency" (`blog-anthropic-zero-trust-ai-agents.md`
  Claim 5) implementation for cross-repository read access, alongside the existing
  `GH_AW_GITHUB_MCP_SERVER_TOKEN` and GitHub App token options documented in
  `docs-ghaw-github-tools.md`.
- **Add the credential-isolation architecture as a citable pattern** (Claim 10):
  when documenting how to shield PATs/tokens from agent code, cite the enclave's
  proxy-holds-the-credential, agent-never-sees-the-address pattern as a concrete
  worked example, alongside the general MCP Gateway isolation guarantees in
  `docs-ghaw-mcp-gateway-reference.md` Claim 10.
- **Flag the feature's experimental/gated status** (Claim 6): note explicitly that
  this depends on an unreleased upstream firewall change
  (`github/gh-aw-firewall#6992`) and specific minimum versions (AWF v0.28.9+, mcpg
  v0.4.13+, Claim 12) — practitioners should verify their pinned component
  versions before attempting adoption, not assume availability from the
  documentation alone.

### Chapter 02: Harness Engineering

- **Document the `issues-read-v1` allowlist as a worked minimal-API-surface
  example** (Claims 7–8): when explaining how to constrain an agent's GitHub API
  access to the smallest necessary surface, use this profile's three fixed REST GET
  routes and the "no stock `gh issue` CLI, use `gh api --method GET`" gotcha as a
  concrete illustration — more restrictive and more specific than the general
  `toolsets` catalogue guidance already sourced from `docs-ghaw-github-tools.md`.
- **Note the timeout-bucket arithmetic as a distinct system from the general MCP
  Gateway defaults** (Claim 5): if the guide documents MCP Gateway timeout
  configuration (30s/60s defaults per `docs-ghaw-mcp-gateway-reference.md`
  Claim 8), add an explicit callout that enclave sessions use a separate,
  much-longer timeout budget (4,860s/4,740s) so practitioners don't conflate the
  two when debugging a long-running enclave session that appears to hang.

## Extraction Notes

1. **WebFetch summary cross-checked against raw HTML.** An initial WebFetch pass
   returned a plausible but AI-summarized rendering of the page. To satisfy the
   verbatim-quote requirement, the page was re-fetched directly with `curl`
   (`https://github.github.com/gh-aw/experimental/enclaves`, HTTP 200) and the
   `<main>` region was converted to text with a small Python `html.parser`-based
   extractor (not `html2text`/`lynx`/`w3m`/`bs4`, none of which were available in
   this environment). Every `Quote` field above was copied character-for-character
   from that raw-HTML text extraction, not from the WebFetch summary. The two
   renderings agreed on substance; the raw extraction additionally surfaced two
   details the WebFetch summary had dropped or altered: the "Related Documentation"
   footer links (previous/next page navigation) and the exact prose wording used
   for several quotes (the WebFetch summary had rephrased some sentences into
   bullet points).
2. **Page structure is unusually prose-heavy for a gh-aw reference page.** Unlike
   `docs-ghaw-agent-runtimes-reference.md` or `docs-ghaw-mcp-gateway-reference.md`,
   this page has almost no tables — the configuration constraints, security
   details, and access rules are stated as continuous paragraphs. Where the
   WebFetch summary rendered these as bullet lists (reproduced faithfully in the
   original tool-call output above this note's drafting), the Quote fields in this
   note instead use the actual verbatim prose sentences from the raw-HTML
   extraction.
3. **No linked sub-pages were followed as separate deep-reads**, per MINER.md's
   "up to 5 linked pages" allowance — the page links only to
   `github/gh-aw-firewall#6992` (an external GitHub issue, not fetched; its
   existence and issue number are reported as stated in the source, not
   independently verified) and the two "Related Documentation" footer links
   (`/gh-aw/experimental/drive-memory/`, already mined as `docs-ghaw-drive-memory.md`,
   and `/gh-aw/experimental/trace-graders/`, not mined and outside this issue's
   scope). A future source-submission for `experimental/trace-graders` would be a
   reasonable follow-up if graders become relevant to the guide.
4. **No publication date on the page.** Consistent with other Astro/Starlight
   `gh-aw` reference and experimental pages in this corpus (e.g.
   `docs-ghaw-agent-runtimes-reference.md`, `docs-ghaw-drive-memory.md`),
   `date_published` is left null.
5. **Confidence rated `emerging`, not `settled`.** Although every individual claim
   is first-party, precise, and internally consistent (meriting `settled` at the
   claim level, as marked above), the feature as a whole is explicitly gated on an
   unreleased upstream change (`github/gh-aw-firewall#6992`, Claim 6) and versions
   newer than what a recent weekly-changelog source recorded as current
   (`blog-ghaw-weekly-2026-06-29.md` Claim 4). The overall note confidence reflects
   that the feature's real-world availability and stability cannot yet be verified
   independently of the documentation itself.
6. **No contradictions filed.** Reviewed `docs-ghaw-integrity-reference.md`,
   `docs-ghaw-mcp-gateway-reference.md`, `docs-ghaw-github-tools.md`,
   `docs-ghaw-agent-runtimes-reference.md`, `docs-ghaw-multi-repo-ops.md`,
   `docs-ghaw-drive-memory.md`, `blog-ghaw-weekly-2026-06-29.md`, and
   `blog-anthropic-zero-trust-ai-agents.md` (all cross-referenced above) plus open
   `contradiction`-labeled issues and `CONTRADICTIONS.md`. No claim in this source
   materially opposes an existing note at the MINER.md §4a filing threshold — the
   enclave feature extends and reuses existing integrity/isolation machinery
   (DIFC labels, `min-integrity` default, PAT-shielding proxy pattern) rather than
   describing it differently. No contradiction issue required.
