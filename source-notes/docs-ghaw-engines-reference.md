---
source_url: https://github.github.com/gh-aw/reference/engines
source_type: docs
title: "GitHub Agentic Workflows: AI Engines Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-26
last_checked: 2026-05-26
status: current
confidence_overall: emerging
issue: "#391"
---

# GitHub Agentic Workflows: AI Engines Reference

> The authoritative per-engine capability and configuration reference for
> gh-aw — documents seven supported coding agents (Copilot, Claude, Codex,
> Gemini, Crush, OpenCode, Pi), their authentication secrets, a feature-parity
> matrix identifying capabilities exclusive to each engine (max-turns: Claude
> only; max-continuations: Copilot only; custom agent files: Copilot only),
> timeout defaults that differ by engine, and Claude's four permission-mode
> settings for tool-allowlist enforcement.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/engines` page —
  in the "Reference" section alongside `reference/permissions`, `reference/tools`,
  `reference/network`. Reference pages document platform configuration
  authoritatively; this is the canonical page for engine selection, per-engine
  configuration fields, and capability comparison.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's "Agent Factory" blog series and the
  `gh aw` CLI. Engine names, feature flags, configuration fields, authentication
  requirements, and timeout defaults are settled platform facts. Guidance on
  which engine to choose ("Copilot offers the broadest feature support") is
  first-party recommendation, not independent measurement.
- **Scope**: Complete reference for the `engine:` frontmatter field — all
  supported engines with their required secrets, feature comparison matrix,
  configuration structure (id, version, model, command, args, env, api-target),
  Copilot-specific options (BYOK, harness script, agent files, max-continuations),
  Claude-specific options (max-turns, permission-mode), bare mode per-engine
  behavior, timeout defaults per engine, and custom token-weight overrides. Does
  NOT cover: the full frontmatter field catalog in depth (see
  `docs-ghaw-frontmatter-full-reference.md`), network egress configuration
  (`docs-ghaw-network-reference.md`), tools configuration (`docs-ghaw-tools-reference.md`),
  permissions model (`docs-ghaw-permissions-reference.md`), or sandbox configuration
  (`docs-ghaw-sandbox-reference.md`).

## Extracted Claims

### Claim 1: The platform supports seven AI engines — Copilot CLI (default), Claude, Codex, Gemini, Crush (experimental), OpenCode (experimental), and Pi (experimental) — each requiring distinct authentication secrets

- **Evidence**: The page enumerates all seven engines with their corresponding
  required secrets. Copilot CLI is the default and requires `COPILOT_GITHUB_TOKEN`;
  Claude requires `ANTHROPIC_API_KEY`; Codex requires `OPENAI_API_KEY`; Gemini
  requires `GEMINI_API_KEY`; Crush and OpenCode require `COPILOT_GITHUB_TOKEN`;
  Pi requires provider-specific secrets.
- **Confidence**: settled (first-party reference documentation; engine names and
  required secrets are authoritative platform configuration facts)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The authentication model separates engines by provider identity:
  Copilot-based engines (Copilot CLI, Crush, OpenCode) share the same credential
  source (`COPILOT_GITHUB_TOKEN`), while Claude, Codex, and Gemini each require a
  distinct provider API key. Crush and OpenCode being Copilot-token-based suggests
  they route through GitHub's Copilot infrastructure rather than calling provider
  APIs directly. The experimental label on Crush, OpenCode, and Pi signals production
  maturity differences — practitioners should default to the four main engines for
  production workflows. For Ch02 (Harness Engineering): the engine secret requirement
  is the first configuration step when adopting gh-aw with a non-default engine;
  the guide should document which secret each engine needs alongside the `engine:`
  frontmatter field.

### Claim 2: Engine selection guidance recommends choosing based on existing accounts and requirements, with Copilot having the broadest feature support and Claude excelling at iteration control

- **Evidence**: Selection guidance section on the reference page. The page explicitly
  names capability advantages for each engine.
- **Confidence**: emerging (first-party recommendation; not independently measured
  against other engines; specific feature advantages may change as engines evolve)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The "choose based on existing accounts" framing makes engine
  selection a procurement decision first and a capability decision second — if a
  team already has a GitHub Copilot subscription, Copilot CLI is the lowest-friction
  default. The "Claude excels at controlling iteration limits" note refers to
  `max-turns` (Claude-only per Claim 3), which makes Claude the preferred choice
  for workflows where runaway-loop prevention is a priority. Gemini and Codex
  "integrate well with existing tooling" — a non-specific framing that likely
  refers to teams already using those providers' APIs. For Ch02: present the
  selection criteria as a two-step decision: (1) which engine does the team already
  have credentials for? (2) does the workflow need engine-specific capabilities
  like `max-turns` (Claude), `max-continuations` (Copilot), or custom agent files
  (Copilot)?

### Claim 3: The capability feature matrix shows three exclusive features — max-turns (Claude only), max-continuations/autopilot (Copilot only), and custom agent files (Copilot only) — while web search is available to all and tools allowlist is unavailable only for Crush and OpenCode

- **Evidence**: Feature comparison section of the reference page, enumerating
  capabilities per engine. The page explicitly marks which features are
  engine-exclusive and which are universally available.
- **Confidence**: settled (first-party reference; the feature matrix is an
  authoritative platform specification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The three exclusive features define the differentiated
  capabilities between the main engines: `max-turns` makes Claude the right choice
  when iteration count control is needed; `max-continuations` (autopilot) makes
  Copilot CLI the choice for workflows expected to run many continuation cycles;
  custom agent files (referencing `.github/agents/` entries) are a Copilot-native
  pattern that cannot be used with other engines. The Crush and OpenCode exclusion
  from tools allowlist enforcement is architecturally significant — it means the
  `tools:` frontmatter allowlist has no effect when using those experimental engines,
  removing a key safety control. For Ch03 (Safety and Verification): explicitly
  warn that Crush and OpenCode bypass the tools allowlist — they should not be
  used in workflows where tool-scope restriction is a security requirement.

### Claim 4: The engine configuration block accepts five fields — id, version, model, command, and args — with version supporting GitHub Actions expression strings to enable reusable workflow_call scenarios

- **Evidence**: Configuration structure section of the reference page, with a
  YAML example. The version field description explicitly notes GitHub Actions
  expression string support.
- **Confidence**: settled (first-party reference; field names and types are
  authoritative configuration facts)
- **Quote**: "Version also accepts a GitHub Actions expression string, enabling
  `workflow_call` reusable workflows."
- **Our assessment**: The five-field engine block is the per-workflow engine
  specification — `id` selects the engine, `model` pins the model version,
  `version` pins the engine binary version, `command` overrides the executable
  path, and `args` injects CLI arguments before the prompt. The GitHub Actions
  expression support for `version` is the enabling mechanism for reusable workflows:
  a shared workflow template can accept the engine version as an input parameter
  rather than hardcoding it. This makes engine version management centralized when
  using the `workflow_call` pattern. For Ch02: document version pinning as a
  reproducibility practice — unpinned workflows track `latest`, which may change
  behavior on engine updates.

### Claim 5: The api-target field specifies a custom API hostname for enterprise deployments and accepts a hostname only (no protocol or path); the hostname must also be listed in network.allowed

- **Evidence**: API endpoint configuration section. The constraint on hostname
  format is explicitly stated, and the network.allowed requirement is noted.
- **Confidence**: settled (first-party reference; the format constraint is an
  explicit platform validation rule)
- **Quote**: "hostname only — no protocol or path"
- **Our assessment**: The `api-target` field is the enterprise redirection mechanism
  for teams running private model deployments or routing through a corporate proxy.
  The "hostname only" constraint prevents accidentally including protocol or path
  components (e.g., writing `https://my-proxy.example.com/v1` instead of
  `my-proxy.example.com` will fail). The requirement to also list the hostname in
  `network.allowed` means practitioners must configure both the engine endpoint
  and the network egress allowlist — a two-field change that is easy to overlook.
  For Ch02: document `api-target` + `network.allowed` as a paired configuration
  pattern for enterprise custom endpoints. Cross-reference `docs-ghaw-network-reference.md`
  for the network allowlist configuration syntax.

### Claim 6: Per-engine environment variables configure custom API endpoints without using api-target — OPENAI_BASE_URL for Codex/Crush, ANTHROPIC_BASE_URL for Claude, GITHUB_COPILOT_BASE_URL for Copilot

- **Evidence**: API endpoint configuration section listing per-engine environment
  variable alternatives.
- **Confidence**: settled (first-party reference; environment variable names are
  authoritative platform facts)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The per-engine env vars provide an alternative to `api-target`
  for custom endpoint routing — useful when the team is already using these env
  var conventions from local development and wants the same configuration to apply
  in the workflow. The env var approach is more granular than `api-target` (which
  applies to all engines) and follows the naming convention of the underlying provider
  SDKs (Claude SDK uses `ANTHROPIC_BASE_URL`, OpenAI SDK uses `OPENAI_BASE_URL`).
  For Ch02: document both mechanisms side by side — `api-target` for workflow-level
  enterprise endpoint routing, env vars for provider-SDK-compatible endpoint
  overrides.

### Claim 7: Copilot BYOK (bring-your-own-key) mode is activated via COPILOT_PROVIDER_BASE_URL and keeps credentials out of the agent container via the AWF API proxy

- **Evidence**: Copilot BYOK configuration section. The AWF API proxy mechanism
  is explicitly named as the credential isolation mechanism.
- **Confidence**: settled (first-party reference; the env var name and proxy
  mechanism are authoritative configuration facts)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: BYOK mode allows teams to route Copilot requests through an
  external LLM provider they control — the `COPILOT_PROVIDER_BASE_URL` environment
  variable (plus model name and optional provider type, wire format, and token limit
  fields) configures the routing. The "credentials kept out of the agent container
  via the AWF API proxy" design means the AI agent never has direct access to the
  provider credentials — the proxy mediates the call. This is architecturally
  consistent with the broader gh-aw security model (agents are never given secrets
  directly). For Ch02: BYOK mode is the enterprise mechanism for teams who want to
  use GitHub Agentic Workflows with their own model deployments rather than GitHub's
  Copilot service.

### Claim 8: Bare mode disables automatic context loading and its behavior varies per engine — Copilot suppresses AGENTS.md, Claude suppresses memory files, other engines override system prompts

- **Evidence**: Bare mode section of the reference page, with per-engine behavior
  enumerated.
- **Confidence**: settled (first-party reference; per-engine behavior differences
  are authoritative platform facts)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The per-engine variation in bare mode behavior is an important
  detail that the frontmatter reference (`docs-ghaw-frontmatter-full-reference.md`
  Claim 7) does not capture — it describes bare mode as "disable auto-loading of
  context/custom instructions" without specifying what "context" means for each
  engine. Knowing that Claude's bare mode suppresses memory files (while Copilot
  suppresses AGENTS.md) matters when a workflow needs to exclude specific context
  types. For Ch04 (Context Engineering): the engine-specific meaning of bare mode
  is critical for practitioners designing workflows that need precise context
  control — what gets suppressed depends on which engine is running. Add a
  per-engine breakdown alongside the bare mode documentation.

### Claim 9: Job-level timeout defaults to 20 minutes via timeout-minutes, while per-tool-call timeout via tools.timeout has engine-specific defaults — Claude defaults to 60 seconds, Codex defaults to 120 seconds

- **Evidence**: Timeout configuration section with explicit per-engine default
  values for per-tool-call timeout.
- **Confidence**: settled (first-party reference; numeric defaults are authoritative
  platform facts)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The timeout architecture has two distinct layers: the job-level
  wall-clock limit (`timeout-minutes`, default 20 min) bounds the entire agent job,
  while the per-tool-call limit (`tools.timeout`, in seconds) bounds individual
  tool invocations within the job. The different defaults for Claude (60s) and Codex
  (120s) suggest different expected tool-execution patterns — Claude is optimized
  for faster tool calls; Codex has a more generous per-call budget. For Ch02:
  document both timeout layers together as the complete timeout configuration model.
  Recommend setting both explicitly rather than relying on defaults, since the
  interaction between them (a slow tool can exhaust the per-call budget before the
  job times out) can produce confusing failures.

### Claim 10: Engine-specific runaway-prevention mechanisms differ — Claude uses max-turns to cap AI iterations; Copilot uses max-continuations to limit autopilot runs; other engines rely only on job-level timeout

- **Evidence**: Engine-specific timeout controls section, enumerating the
  runaway-prevention mechanism for each engine category.
- **Confidence**: settled (first-party reference; the per-engine mechanism
  enumeration is authoritative)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The asymmetry in runaway-prevention mechanisms is the
  sharpest capability difference between Claude and Copilot. `max-turns` (Claude)
  limits the number of AI reasoning steps, regardless of how long each step takes;
  `max-continuations` (Copilot) limits autopilot continuation cycles, which is
  a different granularity. Other engines (Gemini, Codex) have no semantic-level
  runaway protection beyond the wall-clock job timeout — meaning a Codex workflow
  that makes many fast tool calls can exceed the intended iteration budget without
  triggering any limit until `timeout-minutes` fires. For Ch02: when documenting
  anti-runaway practices, be engine-specific. The guide should recommend
  `max-turns` for Claude workflows, `max-continuations` for Copilot autopilot
  workflows, and a conservative `timeout-minutes` as the safety net for Codex
  and Gemini workflows where semantic iteration limits are not available.

### Claim 11: Claude's permission-mode setting controls whether Claude Code honors the tools allowlist — four modes exist: acceptEdits (default, respects allowlist), auto (ignores allowlist when tools.edit: false), plan, and bypassPermissions (silently ignores allowlist)

- **Evidence**: Claude Tool Enforcement Security section, with explicit description
  of each permission-mode value and its behavior.
- **Confidence**: settled (first-party reference; mode names and behaviors are
  authoritative platform facts)
- **Quote**: "Claude Code silently ignores `--allowed-tools`" (describing
  bypassPermissions mode)
- **Our assessment**: The four permission modes create a spectrum from strict
  enforcement to complete bypass of the tools allowlist. The default (`acceptEdits`)
  correctly honors the `tools:` frontmatter allowlist. The `auto` mode is a designed
  escape hatch for when `tools.edit: false` is set — in that case, the allowlist
  enforcement would conflict with the "no edit" requirement, so `auto` mode is the
  correct default. The `bypassPermissions` mode is the most concerning: Claude Code
  silently ignores `--allowed-tools`, meaning the `tools:` frontmatter allowlist
  has no effect. This should only be used by maintainers who understand the security
  implications. The `plan` mode adds an additional review step. For Ch03 (Safety
  and Verification): document `bypassPermissions` as a security-relevant setting
  that removes the tools allowlist enforcement layer — it should be treated as a
  privileged configuration requiring explicit justification in code review.

### Claim 12: The MCP gateway's allowed list provides server-side tool enforcement regardless of Claude's permission-mode setting — it is the safety backstop when permission-mode bypasses client-side enforcement

- **Evidence**: Claude Tool Enforcement Security section, which notes the MCP
  gateway enforcement as independent of and unaffected by permission-mode.
- **Confidence**: settled (first-party reference; the independence of MCP gateway
  enforcement is explicitly stated)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The MCP gateway's `allowed:` list represents a server-side
  enforcement layer that cannot be overridden by client-side configuration like
  `permission-mode`. Even if a workflow sets `permission-mode: bypassPermissions`,
  the MCP gateway still enforces its own allowlist on tool invocations. This is
  the architectural defense-in-depth principle: multiple independent enforcement
  layers so that no single configuration error removes all safety controls. For
  Ch03: document the MCP gateway as the server-side complement to the client-side
  `tools:` allowlist — practitioners should understand that `bypassPermissions`
  bypasses client-side checks but not the MCP gateway. Cross-reference
  `docs-ghaw-mcps.md` for the MCP gateway configuration.

### Claim 13: Custom token-weight multipliers via token-weights.multipliers allow overriding built-in cost multipliers for non-standard or experimental models

- **Evidence**: Custom Token Weights section of the reference page.
- **Confidence**: emerging (first-party reference; field existence is certain but
  practical usage context for experimental models is not provided)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `token-weights.multipliers` field allows teams to
  override the platform's built-in cost calculation for models not in the default
  weight table — for example, when using a BYOK (Claim 7) deployment with a custom
  model that the platform doesn't have cost data for. Without a custom weight, the
  cost reporting for that model would be zero or incorrect, making `gh aw logs` cost
  data unreliable for capacity planning. For Ch02: document `token-weights.multipliers`
  as a required configuration companion to BYOK mode and custom model deployments —
  without it, cost monitoring will be inaccurate. Cross-reference
  `docs-ghaw-cost-management.md` for the cost monitoring context.

## Concrete Artifacts

### Engine Capability Feature Matrix

```
Engine            Required Secret              max-turns  max-cont  agent-files  tools-allowlist
─────────────────────────────────────────────────────────────────────────────────────────────
Copilot CLI       COPILOT_GITHUB_TOKEN           —           ✓          ✓             ✓
Claude            ANTHROPIC_API_KEY              ✓           —          —             ✓
Codex             OPENAI_API_KEY                 —           —          —             ✓
Gemini CLI        GEMINI_API_KEY                 —           —          —             ✓
Crush (exp)       COPILOT_GITHUB_TOKEN           —           —          —             —
OpenCode (exp)    COPILOT_GITHUB_TOKEN           —           —          —             —
Pi (exp)          provider-specific secrets      —           —          —             (unknown)

Web search: all engines (Codex requires opt-in)
max-turns: limits AI chat iterations per run (Claude only)
max-continuations: limits autopilot continuation cycles (Copilot only)
agent-files: references .github/agents/*.agent.md (Copilot only)
tools-allowlist: tools: frontmatter section enforced (not Crush/OpenCode)
```

*Source: https://github.github.com/gh-aw/reference/engines — feature comparison section*

### Engine Configuration Block Structure

```yaml
# Minimal: engine id shorthand
engine: copilot

# Full configuration block
engine:
  id: copilot          # copilot | claude | codex | gemini | crush | opencode | pi
  version: latest      # accepts GitHub Actions expression string for workflow_call
  model: gpt-5         # model version override
  command: /usr/local/bin/copilot  # executable path override
  args: ["--add-dir", "/workspace"]  # injected before prompt

# Custom API endpoint (enterprise)
engine:
  id: claude
  api-target: my-ghes.example.com   # hostname only — no protocol or path
                                     # must also appear in network.allowed
# Per-engine env vars (alternative to api-target):
#   Codex/Crush:  OPENAI_BASE_URL
#   Claude:       ANTHROPIC_BASE_URL
#   Copilot:      GITHUB_COPILOT_BASE_URL
```

*Source: https://github.github.com/gh-aw/reference/engines — configuration options sections*

### Timeout Configuration by Layer and Engine

```
Layer               Field                  Default
─────────────────────────────────────────────────────
Job-level           timeout-minutes        20 minutes (all engines)
Per-tool-call       tools.timeout          Claude:  60 seconds
                                           Codex:   120 seconds
                                           Others:  (not specified)

Runaway prevention (semantic):
  Claude:   max-turns          (cap AI iterations per run)
  Copilot:  max-continuations  (cap autopilot cycles)
  Others:   timeout-minutes only (no semantic iteration limit)
```

*Source: https://github.github.com/gh-aw/reference/engines — timeout configuration section*

### Claude permission-mode Values

```yaml
# acceptEdits (default): Claude respects --allowed-tools flags from tools: frontmatter
engine:
  id: claude
  permission-mode: acceptEdits

# auto: Claude ignores allowlist — correct default when tools.edit: false is set
engine:
  id: claude
  permission-mode: auto   # (also the automatic default when tools.edit: false is explicit)

# plan: Plan mode enforcement
engine:
  id: claude
  permission-mode: plan

# bypassPermissions: Claude Code silently ignores --allowed-tools
# WARNING: removes client-side tool enforcement; MCP gateway still enforces its own allowed: list
engine:
  id: claude
  permission-mode: bypassPermissions
```

*Source: https://github.github.com/gh-aw/reference/engines — Claude Tool Enforcement Security section*

### Copilot BYOK Configuration

```yaml
# Activate BYOK mode via COPILOT_PROVIDER_BASE_URL env var
# Credentials kept out of agent container via AWF API proxy
engine:
  id: copilot
  env:
    COPILOT_PROVIDER_BASE_URL: ${{ secrets.MY_LLM_BASE_URL }}
    # Optional fields: model name, provider type, wire format, token limits
    # AWF API proxy mediates calls — agent never holds credentials directly
```

*Source: https://github.github.com/gh-aw/reference/engines — Copilot BYOK Mode section*

### Bare Mode Per-Engine Behavior

```
Engine           What bare: true suppresses
──────────────────────────────────────────────────────────
Copilot          AGENTS.md auto-injection
Claude           Memory files auto-injection
Others           System prompt override
```

*Source: https://github.github.com/gh-aw/reference/engines — Bare Mode section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-frontmatter-full-reference.md` Claim 6 (`engine.max-turns` limits AI
    chat iterations per run, prevents runaway loops): The engines reference confirms
    this is Claude-only behavior (Claim 3 and 10 here), extending the frontmatter
    reference which does not specify engine exclusivity.
  - `docs-ghaw-frontmatter-full-reference.md` Claim 7 (`engine.bare` disables
    auto-loading of context/custom instructions): Corroborated and extended by
    Claim 8 here, which adds per-engine specifics the frontmatter reference omits.
  - `docs-ghaw-network-reference.md` Claim 1 (network: controls domain access for
    AI engines during workflow execution): The engines reference's Claim 5 (api-target
    + network.allowed pairing) corroborates the network reference's model — custom
    API endpoints require explicit network egress configuration.
  - `docs-ghaw-agentic-ops.md` Claim 8 (audit workflow uses `gh aw logs --engine
    copilot`): The engine-selection flag in that command is consistent with this
    reference's enumeration of named engines — `--engine copilot` corresponds to
    the Copilot CLI engine documented here.
  - `docs-ghaw-tools-reference.md` Claim 1 (tools: frontmatter section is the
    declarative capability sandbox): The engines reference's Claim 11 (permission-mode
    controls tools allowlist enforcement for Claude) describes how the agent runtime
    interacts with the tools capability sandbox documented there.

- **Extends**:
  - `docs-ghaw-frontmatter-full-reference.md` Claim 5 (engine configuration supports
    fully custom provider/runtime definitions): The engines reference provides the
    user-facing view of engine selection and configuration without the full custom
    provider/OAuth complexity — it is the practitioner's first contact with `engine:`
    configuration. Frontmatter-full covers the extensibility ceiling (Tier 3 custom);
    this reference covers the common cases (Tiers 1–2 plus engine-specific options).
  - `docs-ghaw-frontmatter-full-reference.md` Claim 7 (`engine.bare`): The engines
    reference's Claim 8 adds per-engine behavioral specifics that complete the
    frontmatter reference's generic description.
  - `docs-ghaw-cost-management.md`: The cost management reference covers cost
    monitoring and optimization strategies; the engines reference extends it with
    `token-weights.multipliers` (Claim 13) as the mechanism for accurate cost
    reporting when using custom or BYOK model deployments.

- **Contradicts**: None identified. All claims in this source are consistent with
  existing source notes. The per-engine capability differentiation and timeout
  defaults extend rather than oppose existing notes. No contradiction issue
  required.

- **Novel**:
  - **Full seven-engine roster with authentication secrets** (Claim 1): No existing
    source note documents all seven engines together with their required secrets.
    The corpus mentions `--engine copilot` in workflow examples and `engine: claude`
    in configuration examples, but the complete enumeration with secret requirements
    is new.
  - **Feature parity matrix** (Claim 3): The explicit capability comparison
    (max-turns: Claude only; max-continuations: Copilot only; agent files: Copilot
    only; tools allowlist: not for Crush/OpenCode) is not summarized in any existing
    source note. The frontmatter reference documents individual fields but not the
    engine-exclusivity constraints.
  - **Engine-specific timeout defaults** (Claim 9): Claude's 60-second and Codex's
    120-second per-tool-call defaults are not documented in any existing source note.
    The sandbox reference covers job-level timeouts; the tools reference covers timeout
    configuration fields — but neither specifies per-engine numeric defaults.
  - **Claude permission-mode four-value taxonomy** (Claim 11): The
    `acceptEdits`/`auto`/`plan`/`bypassPermissions` permission-mode values for
    Claude are not documented in any existing source note. This is the first corpus
    entry describing how Claude's tool-allowlist enforcement can be configured or
    bypassed.
  - **MCP gateway as independent enforcement backstop** (Claim 12): The explicit
    statement that MCP gateway enforcement is independent of (and unaffected by)
    Claude's permission-mode is a defense-in-depth design detail not articulated
    in any existing source note.
  - **Copilot BYOK via AWF API proxy** (Claim 7): The BYOK activation mechanism
    (`COPILOT_PROVIDER_BASE_URL`) and the AWF proxy as the credential isolation
    mechanism are not documented elsewhere in the corpus.
  - **Bare mode per-engine behavioral differences** (Claim 8): The frontmatter
    reference documents bare mode generically; the per-engine breakdown (Copilot →
    AGENTS.md, Claude → memory files, others → system prompt) is new to the corpus.
  - **Per-engine env vars for custom API endpoints** (Claim 6): The three
    provider-specific env vars (`ANTHROPIC_BASE_URL`, `OPENAI_BASE_URL`,
    `GITHUB_COPILOT_BASE_URL`) as alternatives to `api-target` are not documented
    in any existing source note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add the seven-engine roster with required secrets as the engine selection
    reference table. Practitioners adopting a non-default engine need to know which
    secret to provision before they can test the workflow.
  - Add the feature parity matrix (Claim 3) as a decision aid for engine selection.
    The current corpus documents individual engine capabilities but not the
    comparative view needed to make an informed choice. "Use Claude when you need
    `max-turns`; use Copilot CLI when you need agent files or autopilot
    continuations" is the practical guide takeaway.
  - Document the `api-target` + `network.allowed` pairing (Claim 5) as the
    enterprise endpoint configuration pattern, with the "hostname only" format
    constraint prominently noted to prevent misconfiguration.
  - Document `token-weights.multipliers` (Claim 13) as a required companion to
    BYOK mode (Claim 7) and custom model deployments — without it, `gh aw logs`
    cost data will be inaccurate.
  - Add bare mode per-engine behavior (Claim 8) to the context engineering section —
    what gets suppressed depends on which engine is running.

- **Chapter 02 (Harness Engineering) — anti-runaway practices**:
  - Replace the current generic `max-turns` recommendation (from
    `docs-ghaw-frontmatter-full-reference.md` Claim 6) with an engine-specific
    version: `max-turns` for Claude, `max-continuations` for Copilot, conservative
    `timeout-minutes` as the only semantic-limit option for Codex and Gemini.

- **Chapter 03 (Safety and Verification)**:
  - Add an explicit warning that Crush and OpenCode (Claim 3) do not support the
    tools allowlist — these engines should not be used in workflows where tool-scope
    restriction is a security requirement.
  - Document Claude's four permission-mode values (Claim 11) with a security
    classification: `acceptEdits` is the safe default; `bypassPermissions` removes
    client-side tool enforcement and requires explicit justification.
  - Document the MCP gateway as the server-side enforcement backstop (Claim 12)
    that remains effective even when client-side enforcement is bypassed via
    `bypassPermissions`. Frame this as the defense-in-depth principle for tool
    enforcement in gh-aw.

## Extraction Notes

1. **Source content processed via WebFetch AI model**: The WebFetch tool processes
   page content through a small AI model before returning results. Quotes marked
   as direct quotes (Claims 4 and 5, and the Concrete Artifacts configuration
   examples) appeared in quotation marks in the WebFetch output, suggesting the
   processing model identified them as verbatim passages. Claims without confirmed
   direct quotes use "(no direct quote; see paraphrase in Our assessment)" per
   extraction protocol. A second WebFetch pass confirmed the page structure and
   confirmed the key configuration field names, but the model declined to reproduce
   full verbatim content from the page.

2. **Engine feature matrix data reliability**: The feature comparison matrix
   (Claim 3 and Concrete Artifacts) was consistently extracted across two WebFetch
   passes. Engine-to-feature mappings are authoritative platform facts and are
   unlikely to differ from the source; however, practitioners should check the
   current page for updates as experimental engines (Crush, OpenCode, Pi) are
   explicitly labeled as evolving.

3. **Pi engine details not fully extracted**: The Pi engine is listed with "uses
   provider-specific secrets" but the specific secret names and its feature support
   level were not clearly specified in the WebFetch responses. It is included in
   the roster (Claim 1) with the caveat that it requires "provider-specific secrets."
   Practitioners using Pi should consult the current engines reference directly.

4. **Relationship to frontmatter-full reference**: The `docs-ghaw-frontmatter-full-reference.md`
   covers the `engine:` field as part of the complete frontmatter schema but with
   less per-engine specificity than this reference page provides. The two notes are
   complementary: frontmatter-full for the complete field catalog, engines reference
   for per-engine behavioral differences and capability comparison.

5. **No contradictions filed**: Reviewed all existing source notes against claims
   in this source. All claims are consistent with or extend existing notes. The
   per-engine capability differentiation clarifies rather than contradicts the
   general engine documentation in `docs-ghaw-frontmatter-full-reference.md`.
   No contradiction issue required.
