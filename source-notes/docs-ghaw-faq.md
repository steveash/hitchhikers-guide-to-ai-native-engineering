---
source_url: https://github.github.com/gh-aw/reference/faq
source_type: docs
title: "GitHub Agentic Workflows: Reference FAQ"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#393"
---

# GitHub Agentic Workflows: Reference FAQ

> The official practitioner FAQ for GitHub Agentic Workflows — frames agentic
> workflows as "100% additive" to existing CI/CD, documents the four-layer
> action-constraint model, names specific operational constraints (macOS runners
> unsupported, `CLAUDE_CODE_OAUTH_TOKEN` not supported, `ANTHROPIC_API_KEY`
> required), and surfaces the cost-control levers (`max-turns`, `max-continuations`)
> and migration path (`plugins:` → `dependencies:` via APM) not found in the
> architectural or reference pages.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/faq` page — a
  practitioner Q&A reference covering six topic areas: Determinism, Capabilities,
  Guardrails, Configuration & Setup, Workflow Design, and Costs & Usage. FAQ format
  reveals what practitioners commonly confuse or ask about, which is signal for guide
  writing even when the underlying facts are documented elsewhere.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw`
  platform. Factual claims (supported auth methods, runner constraints, cost
  mechanics) are authoritative for this platform.
- **Scope**: Practitioner concerns across the full lifecycle — capability questions,
  security guardrails, cost model, authentication requirements, engine constraints,
  scheduling, workflow design decisions. Does NOT cover: the full technical
  architecture (see `docs-ghaw-how-they-work.md`), MCP server configuration (see
  `docs-ghaw-mcps.md`), Safe Outputs specification (see
  `docs-ghaw-safe-outputs-specification.md`), or the compilation internals (see
  `docs-ghaw-compilation-process.md`). Some FAQ answers deliberately simplify or
  summarize content covered at depth in those reference pages.

## Extracted Claims

### Claim 1: Agentic workflows are "100% additive" to existing CI/CD — they run as a parallel "Continuous AI" layer and do not replace deterministic build, test, or release pipelines

- **Evidence**: Direct answer to the "I like deterministic CI/CD. Isn't this
  non-deterministic?" question. The framing "100% additive" is the platform's own
  position statement for practitioners with existing CI/CD investments.
- **Confidence**: settled (first-party platform framing; consistent with design
  choices documented throughout the corpus)
- **Quote**: "Agentic workflows are '100% additive' to existing CI/CD and don't
  replace deterministic build, test, or release pipelines. They function as a
  'Continuous AI' layer alongside traditional continuous integration and deployment,
  handling tasks where exact reproducibility isn't critical—such as issue triage,
  documentation drafting, dependency research, or code improvement proposals intended
  for human review."
- **Our assessment**: This is the canonical answer to the non-determinism objection
  practitioners raise. "100% additive" is a useful rhetorical frame for teams
  uncertain about adopting agentic automation: they don't have to choose between
  CI/CD and "Continuous AI" — both coexist and serve different reliability
  requirements. For Ch01: use this framing when addressing the common objection about
  determinism. The listed use cases (triage, docs, dependency research, improvement
  proposals) are the FAQ's official taxonomy of "where AI non-determinism is
  acceptable." Corroborates `docs-ghaw-how-they-work.md` Claim 2 (deterministic
  infrastructure + AI-driven decisions) and Claim 8 ("Continuous AI" definition).

### Claim 2: The markdown body (AI instructions) loads at runtime and can be edited without recompilation; only frontmatter changes require `gh aw compile`

- **Evidence**: Direct answer to "Can I edit workflows directly on GitHub.com without
  recompiling?" The distinction between runtime-loaded markdown body and compile-time
  frontmatter is explicit.
- **Confidence**: settled (first-party; confirmed by `docs-ghaw-compilation-process.md`
  which lists the runtime/compile-time boundary as a key design constraint)
- **Quote**: "Yes, the markdown body containing AI instructions loads at runtime and
  can be edited directly on GitHub.com or in any editor. Changes take effect on the
  next workflow run without recompilation. However, frontmatter configuration requires
  recompilation when changed. Run `gh aw compile my-workflow` after editing frontmatter."
- **Our assessment**: This is the most practically useful operational fact for
  gh-aw practitioners editing existing workflows. Prompt engineering (editing AI
  instructions in the markdown body) is a rapid iteration loop — no compilation
  needed. Infrastructure changes (permissions, triggers, tools, MCP servers) require
  compilation. For Ch02: distinguish "fast path" (edit markdown body → deploy
  immediately) from "slow path" (edit frontmatter → compile → commit `.lock.yml`).
  This distinction affects team workflows: who can edit what without a compile step.

### Claim 3: Repository secrets are NOT accessible to the agentic step by default — the AI agent cannot directly access secrets unless explicitly configured

- **Evidence**: Direct answer to "Can agentic workflows run in GitHub Actions. Can
  they access my repository secrets?" The qualifier "unless explicitly configured"
  is from the documentation.
- **Confidence**: settled (first-party; consistent with the "read-only permissions"
  and "no write access by default" principle in `docs-ghaw-how-they-work.md` Claim 4)
- **Quote**: "Repository secrets aren't available to the agentic step by default.
  The AI agent runs with read-only permissions and cannot directly access repository
  secrets unless explicitly configured."
- **Our assessment**: This directly answers a common practitioner security concern.
  The agentic step can't exfiltrate secrets from the repository secrets store without
  explicit configuration granting access. For Ch03: cite this as the default secret
  isolation guarantee. The boundary is: the workflow YAML can reference secrets (they
  appear in environment variables for traditional steps), but the AI agent step
  doesn't have access unless a secret is explicitly passed into the agent's context.

### Claim 4: The FAQ frames agent action constraints as four defense-in-depth layers, with a separate "guardrails" answer adding compilation-time validation and runtime isolation

- **Evidence**: Two separate answers describe the security architecture: "Four
  defense-in-depth layers constrain actions: (1) read-only agent by default; (2)
  safe outputs for all writes via separate jobs with scoped tokens; (3) threat
  detection before writes scanning for prompt injection, secret leaks, and malicious
  patches; (4) network allowlist blocking all outbound access unless explicitly
  permitted." The "Tell me more about guardrails" answer adds compilation-time
  validation and runtime isolation, aligning with the five-layer architecture in
  `docs-ghaw-how-they-work.md` Claim 3.
- **Confidence**: settled (first-party; the layers are named; the FAQ's four-layer
  framing omits compilation-time validation and runtime isolation, which appear in
  the separate guardrails answer)
- **Quote**: "Four defense-in-depth layers constrain actions: (1) read-only agent
  by default; (2) safe outputs for all writes via separate jobs with scoped tokens;
  (3) threat detection before writes scanning for prompt injection, secret leaks, and
  malicious patches; (4) network allowlist blocking all outbound access unless
  explicitly permitted."
- **Our assessment**: The FAQ's four-layer framing is agent-action-centric (what
  constrains what the agent *does*), while `docs-ghaw-how-they-work.md` Claim 3's
  five-layer model is security-pipeline-centric (what validates the system at each
  stage). Both describe the same architecture; they are complementary framings, not
  contradictions. Layer 3 ("threat detection before writes scanning for prompt
  injection, secret leaks, and malicious patches") is the most specific description
  of the content-inspection step in the output sanitization layer — more detailed
  than any existing source note. For Ch03: the "threat detection before writes"
  description (scanning for prompt injection, secret leaks, malicious patches) is
  the concrete content of the output sanitization layer that should be named
  explicitly in the guide.

### Claim 5: Safe output sanitization applies seven named transforms: secret redaction, URL domain filtering, XML escaping, size limits, control character stripping, GitHub reference escaping, and HTTPS enforcement

- **Evidence**: Direct answer to "What sanitization is done on AI outputs before
  applying changes?" The seven transforms are enumerated explicitly.
- **Confidence**: settled (first-party; the list is complete per the FAQ; consistent
  with `docs-ghaw-safe-outputs-specification.md` which documents the validation
  pipeline in detail)
- **Quote**: "All safe outputs are sanitized before application, including secret
  redaction, URL domain filtering, XML escaping, size limits, control character
  stripping, GitHub reference escaping, and HTTPS enforcement."
- **Our assessment**: This is the only source in the FAQ that names all seven
  sanitization transforms in plain language. The Safe Outputs specification
  (`docs-ghaw-safe-outputs-specification.md`) documents the full validation pipeline
  technically, but the FAQ gives practitioners a quick checklist. The "GitHub reference
  escaping" transform (preventing `#123` auto-links) is separately addressable via
  `allowed-github-references: []` (see Claim 10). For Ch03: use the seven-item list
  as a practitioner checklist of what Safe Outputs sanitize — useful for explaining
  why certain content modifications occur in safe output results.

### Claim 6: Human approval for safe outputs is implemented via GitHub Environment protection rules, with the option to invoke external policy engines completely independent of GitHub

- **Evidence**: Direct answer to "Can I require external human approval before safe
  outputs are applied?" The mechanism (Environment protection rules) and the external
  option (call external policy engines from gate jobs) are both described.
- **Confidence**: settled (first-party; mechanism matches GitHub Actions environment
  protection rules, which are a platform feature)
- **Quote**: "Use GitHub Environment protection rules on a custom safe output job to
  require designated reviewers to approve before execution. Additionally, you can call
  external policy engines from gate jobs to place admission decisions in systems
  completely independent of GitHub."
- **Our assessment**: The external policy engine option is notably stronger than
  just GitHub Environment protection rules — it means approval decisions can live in
  OPA, Cerbos, or a corporate compliance system, fully outside GitHub's control
  plane. This is the pattern for regulated industries (financial services, healthcare)
  where workflow approval may need to be governed by external compliance systems.
  For Ch03: add the external policy engine option alongside Environment protection
  rules as the enterprise-grade variant of human-in-the-loop approval. Corroborates
  `docs-ghaw-how-they-work.md` Claim 10 (human approval as a configurable escalation
  point).

### Claim 7: The AI engine runs in a containerized sandbox with network egress control via the Agent Workflow Firewall — container isolation is a hard architectural requirement, making macOS runners unsupported

- **Evidence**: Two related answers: "The AI engine runs in a containerized sandbox
  with network egress control via the Agent Workflow Firewall, container isolation,
  GitHub Actions resource constraints, and limited filesystem access to workspace
  and temporary directories." And: "Agentic workflows rely on containers to build a
  secure execution sandbox. GitHub-hosted macOS runners don't support container jobs,
  which is a hard requirement for the security architecture. Use `ubuntu-latest` or
  another Linux-based runner instead."
- **Confidence**: settled (first-party; GitHub-hosted macOS runners not supporting
  container jobs is a documented GitHub Actions constraint; the connection to the
  security architecture is first-party)
- **Quote**: "Agentic workflows rely on containers to build a secure execution
  sandbox. GitHub-hosted macOS runners don't support container jobs, which is a hard
  requirement for the security architecture."
- **Our assessment**: The macOS exclusion is a hard constraint with a clear reason.
  Teams that run existing CI/CD on macOS runners (common for iOS/macOS development)
  cannot run agentic workflows on the same runners — they would need a separate Linux
  runner pool. This is the first source in the corpus to state this constraint
  explicitly with the security architecture rationale. For Ch02: document that
  `ubuntu-latest` (or equivalent Linux runner) is required, and explain why (container
  jobs are the security sandbox). For Ch03: the container requirement is not just
  operational — it is the runtime isolation layer of the five-layer security
  architecture (`docs-ghaw-how-they-work.md` Claim 3 Layer 2).

### Claim 8: The only supported authentication for the Claude engine is `ANTHROPIC_API_KEY` as a GitHub Actions secret — `CLAUDE_CODE_OAUTH_TOKEN` is explicitly unsupported

- **Evidence**: Direct answer to "Can I use CLAUDE_CODE_OAUTH_TOKEN with the Claude
  engine?" The answer is unambiguous.
- **Confidence**: settled (first-party; authentication methods are a platform
  specification, not a practitioner observation)
- **Quote**: "No. The only supported authentication method for the Claude engine is
  `ANTHROPIC_API_KEY`, which must be configured as a GitHub Actions secret.
  Provider-based OAuth authentication is not supported."
- **Our assessment**: This is the most specific authentication gotcha in the corpus.
  Practitioners coming from Claude Code or the Claude.ai ecosystem might try
  `CLAUDE_CODE_OAUTH_TOKEN` — it won't work. The `ANTHROPIC_API_KEY` requirement
  means costs are billed directly to the Anthropic account, not to a GitHub Copilot
  subscription. For Ch02: add a note when describing Claude engine configuration
  that `ANTHROPIC_API_KEY` is the only supported auth method; do not attempt
  `CLAUDE_CODE_OAUTH_TOKEN`. For Ch01: Anthropic billing is separate from GitHub
  billing (see Claim 11).

### Claim 9: The `plugins:` frontmatter field has been replaced by `dependencies:` backed by Microsoft APM (Agent Package Manager); `gh aw fix --write` auto-migrates existing workflows

- **Evidence**: Direct answer to "The `plugins:` field I was using is gone — how do
  I install agent plugins now?" The APM backing and the `claude` engine handling are
  explicitly described.
- **Confidence**: settled (first-party; the migration command is authoritative)
- **Quote**: "The `plugins:` field has been replaced by `dependencies:` backed by
  Microsoft APM (Agent Package Manager). Run `gh aw fix --write` to automatically
  migrate existing `plugins:` fields. Use the `dependencies:` field to install
  plugins across multiple agent types, providing broader cross-engine support than
  the previous Copilot-only approach."
- **Our assessment**: The APM migration is new to the corpus. The shift from
  `plugins:` to `dependencies:` is significant for practitioners with existing
  workflows: any workflow using `plugins:` will silently fail or produce unexpected
  behavior until migrated. The `gh aw fix --write` command is the recovery path.
  The cross-engine support improvement (APM supports Claude and Codex, vs the
  previous Copilot-only `plugins:`) also changes the architecture of plugin
  management. For Ch02: document the `gh aw fix --write` migration command as a
  required step when upgrading older workflows. For Claude engine users: APM
  automatically infers the target engine from `engine: claude` and unpacks only
  Claude-compatible primitives; `#tag` or `#branch` suffixes pin specific versions.

### Claim 10: `slash_command` workflows show "many started then skipped runs" because they compile into multiple GitHub event listeners — non-matching comments cause quick skipped runs

- **Evidence**: Direct answer to "Why do slash-command workflows show many 'started
  then skipped' runs on comments?" The mechanism (multiple event listeners from a
  single `slash_command`) and the mitigation strategies are both described.
- **Confidence**: settled (first-party; describes the compilation behavior of the
  `slash_command` trigger type)
- **Quote**: "This is expected. A `slash_command` compiles into multiple GitHub event
  listeners. GitHub dispatches the event, then activation logic checks whether the
  comment matches a command. Non-matching comments result in quick skipped runs.
  Narrow scope with `events:` or use LabelOps for fewer incidental runs."
- **Our assessment**: The "started then skipped" behavior is a common source of
  confusion for practitioners who see many workflow runs in their Actions tab and
  worry about cost. The FAQ clarifies it is expected, nearly zero cost (quick skips),
  and mitigation options exist. The `events:` field (see `docs-ghaw-chatops.md`
  Claim 2 — six filter values that scope slash commands to specific comment contexts)
  is the inline mitigation. LabelOps is the alternative trigger pattern for workflows
  that should only run on deliberate human action. For Ch02: add a note in the
  `slash_command` section that skipped runs are expected and explain how to reduce
  them via `events:` scoping.

### Claim 11: Cost model — Copilot CLI uses 1–2 premium requests per execution; Claude billed to Anthropic account; Actions minutes billed separately; `max-turns` and `max-continuations` are the primary per-run cost levers

- **Evidence**: Multiple cost-related Q&A answers: "GitHub Copilot CLI typically uses
  1–2 premium requests per execution. Track usage with `gh aw logs` for runs and
  metrics, or `gh aw audit <run-id>` for detailed token usage and costs." And: "gh-aw
  has no automatic retry mechanism, but you can control reasoning depth with `max-turns`
  (Claude) and autopilot continuation with `max-continuations` (Copilot). Keep these
  values low for cost-sensitive workflows. Run frequency is the primary cost lever for
  scheduled workflows."
- **Confidence**: settled (first-party; cost mechanics per engine are authoritative
  platform documentation)
- **Quote**: "GitHub Copilot CLI typically uses 1–2 premium requests per execution.
  Track usage with `gh aw logs` for runs and metrics, or `gh aw audit <run-id>` for
  detailed token usage and costs."
- **Our assessment**: The 1–2 premium requests figure is the first quantified cost
  benchmark for Copilot CLI in the corpus. The separation of cost levers is
  actionable: `max-turns` (Claude) caps reasoning depth; `max-continuations` (Copilot)
  caps autopilot continuation; run frequency is the major lever for scheduled
  workflows. "gh-aw has no automatic retry mechanism" is also important — unexpected
  retries are not a cost risk. For Ch01/cost guidance: the 1–2 premium request
  baseline and the `max-turns`/`max-continuations` controls should be named as the
  primary cost management tools alongside `gh aw audit`. Spending limits live at
  the provider level — GitHub Billing for Actions minutes, Anthropic Console for
  Claude costs.

### Claim 12: PRs created by agentic workflows do not trigger CI checks by default — `GH_AW_CI_TRIGGER_TOKEN` (PAT) is required to trigger CI on agent-created PRs

- **Evidence**: Direct answer to "Why don't pull requests created by agentic workflows
  trigger my CI checks?" The cause (GitHub's default `GITHUB_TOKEN` restriction) and
  the fix (`GH_AW_CI_TRIGGER_TOKEN` with a PAT) are both explicit.
- **Confidence**: settled (first-party; the default `GITHUB_TOKEN` not triggering
  workflow runs on its own PRs is a documented GitHub Actions security constraint)
- **Quote**: "This is expected GitHub Actions security behavior—PRs created using the
  default `GITHUB_TOKEN` don't trigger workflow runs. Set a `GH_AW_CI_TRIGGER_TOKEN`
  secret with a Personal Access Token to trigger CI checks."
- **Our assessment**: This is one of the most common operational gaps practitioners
  hit when building agent-created PR workflows. An agent creates a PR but CI never
  runs — the fix requires a PAT stored as a repository secret named
  `GH_AW_CI_TRIGGER_TOKEN`. This is new to the corpus. For Ch02: document this as a
  required setup step when configuring any workflow that uses `create-pull-request`
  safe output AND expects CI to run on the resulting PR. The underlying reason
  (GitHub Actions security: self-triggering prevention) is worth explaining so
  practitioners understand it's not a gh-aw bug.

### Claim 13: Integrity filtering restricts which GitHub content the agent can see — for public repositories, `min-integrity: approved` is automatically applied at runtime

- **Evidence**: Direct answer to "How does integrity filtering protect my workflow?"
  The automatic behavior for public repositories is explicitly stated.
- **Confidence**: settled (first-party; the automatic application for public repos
  is a platform behavior)
- **Quote**: "For public repositories, `min-integrity: approved` is automatically
  applied at runtime, restricting content to owners, members, and collaborators."
- **Our assessment**: The automatic `min-integrity: approved` for public repos is
  important because it means public-facing agent workflows are not fully open to
  arbitrary content injection by anonymous contributors — the platform applies a
  baseline trust filter without requiring any configuration. Practitioners building
  public-repo workflows don't need to explicitly set this; practitioners building
  private-repo workflows should know the automatic protection doesn't apply the same
  way. For Ch03: note the automatic integrity floor for public repositories as a
  built-in prompt injection mitigation that requires no configuration.

### Claim 14: `inlined-imports: true` resolves two runtime file-access failures — repository rulesets and cross-organization `workflow_call` — by embedding all imported content at compile time

- **Evidence**: Two separate Q&A answers: "My workflow fails with 'Runtime import
  file not found' when used in a repository ruleset: Enable `inlined-imports: true`"
  and "My cross-organization workflow_call fails with a repository checkout error:
  Enable `inlined-imports: true` on the platform workflow."
- **Confidence**: settled (first-party; the configuration flag and its effect are
  explicitly documented)
- **Quote**: "Enable `inlined-imports: true` in your workflow frontmatter so the
  compiler bundles all imported content into the compiled `.lock.yml` at compile
  time, avoiding file system access issues."
- **Our assessment**: `inlined-imports: true` for cross-org workflow_call is already
  in the corpus via `docs-ghaw-central-repo-ops.md` Claim 7. The FAQ adds a new
  failure context: repository rulesets. A workflow deployed via a repository ruleset
  runs without direct access to the repo's file system, which breaks runtime import
  loading. `inlined-imports: true` is the fix in both cases. For Ch02: document
  `inlined-imports: true` as required for any workflow distributed via repository
  rulesets, in addition to the cross-org use case already documented.

## Concrete Artifacts

### Four Defense Layers (from FAQ "How are agent actions constrained?" answer)

```
Layer 1: Read-only agent by default
  → AI cannot write to repository or GitHub state directly

Layer 2: Safe outputs for all writes — via separate jobs with scoped tokens
  → All state mutations go through permission-separated safe output jobs

Layer 3: Threat detection before writes
  → Scans for: prompt injection, secret leaks, malicious patches

Layer 4: Network allowlist
  → All outbound access blocked unless explicitly permitted via network: config
```

*Source: FAQ "How are agent actions constrained — commenting, opening PRs,
modifying files, and calling external tools?" answer*

### Safe Output Sanitization Transforms (verbatim from FAQ)

```
All safe outputs are sanitized before application, including:
  1. Secret redaction
  2. URL domain filtering
  3. XML escaping
  4. Size limits
  5. Control character stripping
  6. GitHub reference escaping
  7. HTTPS enforcement
```

*Source: FAQ "What sanitization is done on AI outputs before applying changes?" answer*

### Cost Model by Engine

```
GitHub Copilot CLI:
  - 1–2 premium requests per execution (typical)
  - Billed from individual's monthly premium request quota

Claude engine:
  - Billed to Anthropic account associated with ANTHROPIC_API_KEY
  - Auth: ANTHROPIC_API_KEY only (CLAUDE_CODE_OAUTH_TOKEN: NOT supported)
  - Cost control: max-turns to cap reasoning depth

Codex engine:
  - Billed to OpenAI account associated with OPENAI_API_KEY

All engines:
  - GitHub Actions minutes billed SEPARATELY via GitHub Billing
  - No automatic retry mechanism (no unexpected cost from retries)
  - Cost monitoring: gh aw logs / gh aw audit <run-id>
  - Spend limits: set at provider level AND GitHub organization level
```

*Source: FAQ "Costs & Usage" section*

### Cost Control Parameters

```yaml
# Claude: cap reasoning depth
engine:
  name: claude
  max-turns: 10   # keep low for cost-sensitive workflows

# Copilot: cap autopilot continuation
engine:
  name: copilot
  max-continuations: 5  # keep low for cost-sensitive workflows
```

*Source: FAQ "How do retries and agent loops affect costs?" answer*

### CI Trigger Token Setup

```
Problem:  PRs created by agentic workflows don't trigger CI checks
Cause:    Default GITHUB_TOKEN cannot trigger workflow runs (GitHub security)
Fix:      Set a Personal Access Token as repository secret GH_AW_CI_TRIGGER_TOKEN

Repository Secrets → New secret:
  Name:  GH_AW_CI_TRIGGER_TOKEN
  Value: <PAT with repo + workflow permissions>
```

*Source: FAQ "Why don't pull requests created by agentic workflows trigger my CI
checks?" answer*

### APM Migration (plugins: → dependencies:)

```bash
# Migrate all existing workflows from plugins: to dependencies: automatically
gh aw fix --write

# After migration, workflows use:
# dependencies:
#   - <package>  # supports claude, copilot, codex engines
#
# For Claude engine with version pinning:
# dependencies:
#   - <package>#tag-or-branch
```

*Source: FAQ "The `plugins:` field I was using is gone" answer*

### Dependabot Suppression for gh-aw-actions Pins

```yaml
# .github/dependabot.yml — suppress Dependabot PRs for gh-aw-actions pins
# These pins are managed exclusively by `gh aw compile`
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    ignore:
      - dependency-name: "github/gh-aw-actions"
```

*Source: FAQ "Why is Dependabot opening PRs to update github/gh-aw-actions?" answer*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 2 (deterministic infrastructure + AI-driven
    decisions): Claim 1 ("100% additive") is the practitioner-facing framing of the
    same architectural principle. The FAQ answers the "non-determinism" objection
    explicitly; the how-they-work page describes the architectural design that makes
    it safe.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer security pipeline): Claim 4
    (four-layer action constraints) corroborates the same architecture from an
    agent-action perspective. The FAQ's Layer 3 ("threat detection: prompt injection,
    secret leaks, malicious patches") is the most specific description of output
    sanitization content in the corpus.
  - `docs-ghaw-how-they-work.md` Claim 4 (no write access by default): Claim 3
    (secrets not accessible by default) and Claim 4 (four-layer constraints) both
    corroborate the base "zero capability" principle.
  - `docs-ghaw-how-they-work.md` Claim 10 (human approval configurable): Claim 6
    (GitHub Environment protection rules + external policy engines) is the concrete
    mechanism FAQ that corroborates the architectural claim. FAQ adds the external
    policy engine option.
  - `docs-ghaw-safe-outputs-specification.md` Claim 1 (Safe Outputs MCP Gateway
    definition) and the seven-stage validation pipeline: Claim 5 (seven sanitization
    transforms) is the plain-language summary of what the spec documents technically.
    Both sources are consistent; the spec is authoritative for implementation detail.
  - `docs-ghaw-chatops.md` Claim 1 (`slash_command` trigger type): Claim 10 extends
    this by explaining the "started then skipped" operational behavior that arises
    from the trigger compiling into multiple event listeners.
  - `docs-ghaw-network-reference.md` Claim 1 (`network:` field defaults): Claim 7
    (Agent Workflow Firewall as part of containerized sandbox) corroborates that
    network egress is controlled — the network reference page documents the
    configuration mechanism, the FAQ confirms it as part of the security sandbox.
  - `docs-ghaw-compilation-process.md` (runtime/compile-time boundary): Claim 2
    (markdown body loads at runtime; frontmatter requires recompilation) is the
    practitioner-facing summary of the compile-time boundary documented in depth
    in that note.

- **Extends**:
  - `docs-ghaw-central-repo-ops.md` Claim 7 (`inlined-imports: true` for cross-org
    workflow_call): Claim 14 adds a second failure context (repository rulesets) to
    the same fix. Both are now documented; the guide should list both scenarios when
    recommending `inlined-imports: true`.
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support): Claim 8 adds the
    specific authentication constraint for the Claude engine (`ANTHROPIC_API_KEY`
    only, `CLAUDE_CODE_OAUTH_TOKEN` not supported), which the how-they-work page
    does not detail.

- **Contradicts**: None identified. The FAQ's four-layer action-constraint model and
  `docs-ghaw-how-they-work.md`'s five-layer security pipeline are complementary
  framings of the same architecture, not contradictions. The FAQ's "four layers" cover
  runtime agent constraints; the five-layer model includes compile-time and runtime
  isolation layers that the FAQ covers separately in the guardrails answer.

- **Novel**:
  - **macOS runners unsupported** (Claim 7): No existing source note states that
    GitHub-hosted macOS runners are unsupported for gh-aw because container jobs
    are a hard security requirement. This is an important operational constraint for
    teams with mixed-OS CI infrastructure.
  - **`CLAUDE_CODE_OAUTH_TOKEN` not supported** (Claim 8): No existing source
    documents this specific authentication gotcha for the Claude engine. Practitioners
    from Claude Code environments will likely attempt this token first.
  - **APM migration (`plugins:` → `dependencies:`)** (Claim 9): No existing source
    note documents the `plugins:` deprecation, the APM backing, or the `gh aw fix
    --write` migration command. Teams with existing workflows using `plugins:` are
    at risk of silent failures without this information.
  - **`slash_command` "started then skipped" explanation** (Claim 10): `docs-ghaw-chatops.md`
    documents the `slash_command` trigger mechanics but not the "many skipped runs"
    operational behavior that arises from it compiling into multiple event listeners.
  - **`GH_AW_CI_TRIGGER_TOKEN` for CI triggering** (Claim 12): No existing source
    note documents this required PAT secret for CI to run on agent-created PRs. This
    is one of the most common silent failures in agentic PR workflows.
  - **`max-turns` / `max-continuations` as cost controls** (Claim 11): No existing
    source note names these parameters as cost-control levers. The 1–2 premium
    request baseline for Copilot CLI is also new to the corpus.
  - **Automatic `min-integrity: approved` for public repos** (Claim 13): While
    integrity filtering appears in other notes, the automatic application for
    public repositories without any configuration is not previously documented in
    the corpus.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add "100% additive" framing for non-determinism objections** (Claim 1): When
  practitioners ask whether agentic workflows replace CI/CD, the answer is "100%
  additive." The listed use cases (issue triage, documentation drafting, dependency
  research, improvement proposals) are the official taxonomy of tasks where
  non-determinism is acceptable. Cite both this FAQ and `docs-ghaw-how-they-work.md`
  Claim 2 as the dual justification.

- **Add cost model and cost controls** (Claim 11): The guide currently lacks specific
  cost numbers. Add: Copilot CLI typically uses 1–2 premium requests per execution;
  Claude is billed to the Anthropic account; Actions minutes are billed separately.
  Name `max-turns` (Claude) and `max-continuations` (Copilot) as the per-run depth
  controls, and run frequency as the primary cost lever for scheduled workflows.

### Chapter 02: Harness Engineering

- **Document the markdown body vs frontmatter edit boundary** (Claim 2): Teams need
  to know that editing AI instructions (the markdown body) requires no recompilation
  — fast iteration. Editing permissions, triggers, or tools (frontmatter) requires
  `gh aw compile` and committing the new `.lock.yml`. This boundary defines the
  two-speed development loop.

- **Add `GH_AW_CI_TRIGGER_TOKEN` as required setup for `create-pull-request`**
  (Claim 12): Any workflow using the `create-pull-request` safe output AND expecting
  CI to run on the resulting PR requires this PAT secret. Document it as a required
  setup step, not an optional enhancement. Explain the underlying cause (GitHub
  Actions self-triggering prevention) so practitioners understand it's architectural.

- **Document APM migration** (Claim 9): Teams with existing workflows using
  `plugins:` must run `gh aw fix --write` to migrate to `dependencies:`. Add this
  to any upgrade guidance for gh-aw workflows. Note the cross-engine benefit (APM
  supports Claude, Copilot, Codex vs. Copilot-only for `plugins:`).

- **Add `slash_command` skipped-runs note** (Claim 10): In the slash command section,
  note that many "started then skipped" runs are expected behavior, not errors. The
  `events:` field narrows scope to reduce incidental runs; LabelOps is the alternative
  for deliberate-action-only workflows.

- **Add macOS runner constraint** (Claim 7): When listing infrastructure requirements
  for gh-aw workflows, explicitly state that macOS runners are unsupported. The reason
  (container jobs required for sandbox security) is worth including so teams understand
  it is architectural, not a workaround.

- **Add `inlined-imports: true` for ruleset deployments** (Claim 14): Extend the
  existing cross-org `inlined-imports` guidance to cover repository rulesets as a
  second scenario. The "Runtime import file not found" error is the diagnostic signal.

### Chapter 03: Safety and Verification

- **Name the threat detection content** (Claim 4): The existing guide likely describes
  "output sanitization" in general terms. The FAQ provides the specific content:
  scanning for prompt injection, secret leaks, and malicious patches. Update Ch03 to
  name these three threat categories explicitly.

- **Add seven-item sanitization checklist** (Claim 5): The seven transforms (secret
  redaction, URL domain filtering, XML escaping, size limits, control character
  stripping, GitHub reference escaping, HTTPS enforcement) are a practitioner-friendly
  checklist that explains why certain content modifications occur in safe output
  results.

- **Add Claude authentication constraint** (Claim 8): When recommending the Claude
  engine, note that `ANTHROPIC_API_KEY` is the only supported auth method. Do not
  use `CLAUDE_CODE_OAUTH_TOKEN`. This prevents a common misconfiguration.

- **Add automatic integrity floor for public repos** (Claim 13): Note that public
  repositories get `min-integrity: approved` automatically — this is a built-in
  prompt injection mitigation requiring no configuration. Private repo practitioners
  should know they don't get the same automatic protection.

- **Add external policy engine option for human approval** (Claim 6): Extend the
  human-in-the-loop guidance to include the option of calling external policy engines
  (OPA, Cerbos, corporate compliance systems) from gate jobs for approval decisions
  fully independent of GitHub. This is the pattern for regulated industries.

## Extraction Notes

1. **Source is a practitioner FAQ, not a reference spec**: Many answers simplify or
   summarize content covered in depth in companion reference pages
   (`docs-ghaw-how-they-work.md`, `docs-ghaw-mcps.md`, `docs-ghaw-safe-outputs-
   specification.md`, `docs-ghaw-compilation-process.md`). The unique extraction
   value is in operational specifics (auth methods, runner constraints, cost numbers,
   migration commands) and the Q&A framing that reveals common practitioner confusion.

2. **Six topic sections covered**: Determinism, Capabilities, Guardrails,
   Configuration & Setup, Workflow Design, and Costs & Usage. The Workflow Design
   and Configuration & Setup sections contained the highest density of novel claims
   (operational specifics, authentication constraints, migration paths).

3. **No publication date**: The documentation does not carry an explicit publication
   date. Content is consistent with gh-aw platform state including APM/`dependencies:`
   migration (post-`plugins:` era), indicating this is current documentation.

4. **No contradictions filed**: Reviewed all existing source notes. The FAQ's
   four-layer action-constraint model is complementary to, not contradictory with,
   the five-layer security architecture in `docs-ghaw-how-they-work.md`. All other
   FAQ claims are consistent with existing notes.

5. **`sparse-checkout` claim omitted**: The FAQ mentions `sparse-checkout` config for
   large monorepos. This is likely covered in more detail in other reference pages
   and is not extracted here to avoid duplication without sufficient unique value.
   The FAQ answer is brief and does not add concrete detail beyond what the field
   name implies.
