---
source_url: https://github.github.com/gh-aw/reference/engines
source_type: docs
title: "GitHub Agentic Workflows: AI Engines Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#391"
---

# GitHub Agentic Workflows: AI Engines Reference

> The authoritative reference for selecting and configuring one of six AI engines
> (Copilot, Claude, Codex, Gemini, Crush, OpenCode) in gh-aw workflows — documents
> the complete `engine:` configuration field set, a feature-support comparison across
> all engines, Claude-specific permission mode behavior, and the three-level timeout
> system; the key practitioner differentiator is that Claude is the only engine
> supporting `max-turns` for iteration-limit control, while Copilot is the only engine
> supporting `max-continuations`, custom agent files, and a custom harness wrapper.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/engines` page — in the
  "Reference" section. This is the per-engine configuration reference, not the
  compilation or permission model. Positioned alongside `reference/tools`,
  `reference/sandbox`, `reference/network`, and `reference/permissions` in the
  reference section.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind the `gh aw` CLI and all other `reference/` pages in the corpus. Engine
  identifiers, required secrets, configuration field names, and feature support flags
  are authoritative platform facts. Claims about when to choose one engine over another
  are editorial guidance from the platform team and reflect their recommended usage
  patterns.
- **Scope**: Engine selection (six engines with required secrets), engine configuration
  field reference (`engine:` frontmatter sub-fields), feature support comparison across
  all engines, Claude-specific permission mode behavior (`acceptEdits` vs
  `bypassPermissions`), and the three-level timeout system (`timeout-minutes`,
  `tools.timeout`, engine-specific iteration limits). Does NOT cover: the full
  frontmatter schema (see `docs-ghaw-frontmatter-full-reference.md`), custom Copilot
  agent files in depth (see `docs-ghaw-copilot-agent-files.md`), tools configuration
  (see `docs-ghaw-tools-reference.md`), or the MCP gateway (`docs-ghaw-mcps.md`).

## Extracted Claims

### Claim 1: Six AI engines are available for gh-aw workflows, each selected by an `engine:` identifier and requiring a specific authentication secret

- **Evidence**: The reference page documents all six engines in a table with their
  identifiers and required environment variables/secrets. Copilot and the two
  experimental engines (Crush, OpenCode) share `COPILOT_GITHUB_TOKEN`; Claude, Codex,
  and Gemini each require their respective provider API keys.
- **Confidence**: settled (first-party reference; the table is the platform specification
  for which engines exist and what credentials they require)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the table was
  returned by AI-processed WebFetch, not character-for-character)
- **Our assessment**: The six engines span the major commercial coding agent ecosystems:
  GitHub Copilot (default), Anthropic Claude, OpenAI Codex, Google Gemini CLI, and two
  experimental Copilot-token engines (Crush and OpenCode). The shared `COPILOT_GITHUB_TOKEN`
  for Crush and OpenCode positions them as alternative Copilot-token consumers, not
  independent providers. For Ch02 (Harness Engineering): document the six engine options
  and their credential requirements as the first engine selection decision — practitioners
  must provision the right secret before a workflow can run.

### Claim 2: Copilot is the default engine and has the broadest feature support, including the only support for `max-continuations` (autopilot mode), custom agent files (`engine.agent`), and custom harness wrappers (`engine.harness`)

- **Evidence**: The feature comparison table shows Copilot as the only engine with
  ✓ for `max-continuations`, `engine.agent`, and `engine.harness`. The reference
  describes Copilot as the recommended default.
- **Confidence**: settled (first-party feature comparison table; the Copilot-only
  features are an explicit platform specification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Copilot's exclusive ownership of `max-continuations`, `engine.agent`,
  and `engine.harness` creates a meaningful capability gap between Copilot and other
  engines. `max-continuations` controls autopilot mode (how many autonomous cycles
  the agent runs without returning for human confirmation); `engine.agent` enables
  native Copilot custom agent files; `engine.harness` allows replacing the built-in
  Node.js harness wrapper entirely. Teams that need autopilot iteration control or
  Copilot-native agent specialization cannot achieve this with Claude, Codex, or Gemini.
  For Ch02: when writing engine selection guidance, Copilot's broader feature surface
  makes it the default for teams without a specific reason to prefer another engine.
  Cross-reference `docs-ghaw-copilot-agent-files.md` Claim 1 (non-Copilot engines
  receive agent file markdown body as a prompt injection, not native agent processing).

### Claim 3: Claude is the only engine supporting `max-turns` for per-run iteration limits — the recommended choice when extended reasoning tasks require explicit control over how many agent turns are allowed

- **Evidence**: The feature comparison table shows `max-turns` (✓) for Claude and
  (✗) for all other engines. The reference notes Claude as the engine for workflows
  needing stronger iteration limit control.
- **Confidence**: settled (first-party feature table; `max-turns` is a Claude-only
  platform capability in the comparison)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `max-turns` / `max-continuations` split is architecturally
  important: Copilot controls autopilot cycles via `max-continuations`, while Claude
  controls chat iterations via `max-turns`. These are different granularities —
  `max-turns` limits individual LLM chat turns within a single execution, while
  `max-continuations` limits how many times the full workflow restarts autonomously.
  For Ch02: when a workflow involves extended multi-step reasoning (code generation,
  analysis, multi-file edits) where runaway iteration is a concern, Claude + `max-turns`
  is the correct engine + control combination. Cross-reference
  `docs-ghaw-frontmatter-full-reference.md` Claim 6 (`max-turns` as "prevents runaway
  loops" anti-runaway mechanism) for the full field semantics.

### Claim 4: The `engine:` frontmatter field accepts a comprehensive set of configuration sub-fields for version pinning, model override, custom executable, custom CLI arguments, environment injection, and cost multiplier control

- **Evidence**: The reference documents the following `engine:` sub-fields: `id`
  (engine identifier), `version` (defaults to latest; can pin specific releases),
  `model` (model override, e.g., `gpt-5`), `command` (custom executable path),
  `args` (custom CLI arguments array), `agent` (custom agent file reference, Copilot
  only), `api-target` (custom API endpoint hostname), `env` (environment variables
  for the engine), `bare` (disables automatic context loading), `harness` (custom
  Node.js harness wrapper, Copilot only), `token-weights` (cost multiplier overrides).
- **Confidence**: settled (first-party reference; the field list is the platform's
  configuration schema)
- **Quote**: (no direct quote; see paraphrase in Our assessment — field descriptions
  were returned by AI-processed WebFetch)
- **Our assessment**: The `engine:` sub-field set is more extensive than most
  practitioners realize. Beyond the identity fields (`id`, `version`, `model`),
  the configuration surface includes full execution customization (`command`, `args`,
  `harness`), network routing (`api-target`), context control (`bare`), and cost
  modeling (`token-weights`). This makes engine configuration a first-class workflow
  design concern rather than a one-line declaration. For Ch02: document these sub-fields
  as the engine configuration layer, noting that `command`/`args`/`harness` are for
  advanced use (CI environments with pre-installed CLI tools, custom wrappers), while
  `env` and `api-target` are common for enterprise proxy/GHES routing. Cross-reference
  `docs-ghaw-frontmatter-full-reference.md` Claim 5 (fully custom provider/runtime
  definitions via `engine.runtime` + `engine.provider` for non-standard inference APIs).

### Claim 5: The `api-target` field takes a hostname only (no protocol or path) and is used for routing Claude and other engine CLI calls to enterprise proxies, GHEC/GHES endpoints, or custom model routers

- **Evidence**: The reference describes the `api-target` field and specifies the
  format constraint. Code examples show `api-target: api.acme.ghe.com` (hostname only,
  no `https://` prefix).
- **Confidence**: settled (first-party reference; the format constraint is explicitly
  stated alongside code examples)
- **Quote**: "the value must be a hostname only — no protocol or path"
- **Our assessment**: The hostname-only constraint is easy to misconfigure (adding
  `https://` is a natural mistake). For Ch02: document this as a footgun warning
  when using `api-target` — the value must not include a protocol prefix or trailing
  path. The correct pattern is `api-target: api.acme.ghe.com`, not
  `api-target: https://api.acme.ghe.com/v1`. A companion network allowlist entry
  is typically required for the same hostname (shown in the code examples).

### Claim 6: When Claude is the engine, two permission modes govern how tool allowlists are enforced — `acceptEdits` (default, honors the compiled allowlist) and `bypassPermissions` (triggered by unrestricted bash, silently ignores `--allowed-tools`)

- **Evidence**: The reference describes both modes explicitly. `acceptEdits` is the
  default, compiling the workflow's `tools:` and `mcp-servers: allowed:` declarations
  into a `--allowed-tools` flag. `bypassPermissions` is triggered when the workflow
  grants unrestricted bash access (`bash: "*"`, `bash: [":*"]`, or `bash: null`),
  and in this mode the Claude CLI ignores the allowlist entirely.
- **Confidence**: settled (first-party reference; the two modes and their triggers are
  explicitly documented as a security architecture detail for Claude)
- **Quote**: "In this mode, Claude Code silently ignores `--allowed-tools`."
  (describing `bypassPermissions` mode)
- **Our assessment**: The `bypassPermissions` behavior is a significant security
  consideration for Claude workflows: granting unrestricted bash is not just a tool
  expansion — it disables the entire `--allowed-tools` enforcement layer for Claude.
  Every MCP tool becomes reachable regardless of the workflow's declared tool
  configuration. The MCP gateway's `allowed:` filter provides the only server-side
  enforcement in this mode. For Ch02: when documenting bash tool grants for Claude
  workflows, flag that `bash: "*"` or `bash: null` shifts enforcement entirely to
  the MCP gateway — the workflow's tool allowlist no longer constrains what Claude
  can do. For Ch03 (Safety and Verification): this is a security-relevant design
  decision: the two enforcement layers (client-side `--allowed-tools` and server-side
  MCP `allowed:` filter) are not always both active, and the condition under which
  one is silently removed deserves explicit documentation.

### Claim 7: The MCP gateway's `allowed:` filter provides server-side enforcement regardless of whether the client is in `acceptEdits` or `bypassPermissions` mode — it is the last enforcement layer when `--allowed-tools` is inactive

- **Evidence**: The reference documents the MCP gateway's `allowed:` filter as
  operating independently of the Claude permission mode. In `bypassPermissions` mode,
  where `--allowed-tools` is ignored, the MCP gateway's `allowed:` filter still
  restricts which tools the engine can reach.
- **Confidence**: settled (first-party security architecture documentation)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The two-layer enforcement model (client-side `--allowed-tools`
  + server-side MCP gateway `allowed:` filter) maps to different failure modes: if
  the client-side layer is bypassed (by unrestricted bash), the server-side layer
  remains the backstop. Teams using Claude with unrestricted bash should audit their
  MCP gateway `allowed:` declarations as the effective security boundary. For Ch03:
  add the MCP gateway `allowed:` filter as the server-side enforcement primitive
  for Claude tool access control, positioned as the deepest layer in the five-layer
  security model documented in `docs-ghaw-how-they-work.md` Claim 3.

### Claim 8: Three timeout controls operate at different levels and can be combined: job-level (`timeout-minutes`, default 20), per-tool-call (`tools.timeout` in seconds), and engine-specific iteration limits (`max-turns` for Claude, `max-continuations` for Copilot)

- **Evidence**: The reference presents code examples for each level independently
  and in combination. The default `timeout-minutes` value of 20 minutes is documented.
  `tools.timeout` is set in seconds. The combination for Claude workflows shows
  `max-turns: 20` + `tools.timeout: 600` + `timeout-minutes: 60` as a complete
  timeout configuration.
- **Confidence**: settled (first-party reference; the three timeout levels and their
  field names are explicitly documented with examples)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The three-level timeout hierarchy gives practitioners granular
  cost and reliability control: `timeout-minutes` is the emergency cutoff (wall clock),
  `tools.timeout` prevents individual slow tool calls from blocking the agent,
  and `max-turns`/`max-continuations` limits how much the agent can do within the
  time budget. For Ch02: document the three levels as a single "timeout stack" — teams
  should configure all three intentionally rather than relying on defaults. The 20-minute
  job default is appropriate for simple tasks; complex workflows (analysis, multi-file
  refactors) need explicit increases. A per-tool timeout of 300s is a reasonable
  default for most tool calls; 600s for Claude workflows with long-running bash steps.

### Claim 9: Codex requires explicit `web-search:` declaration to enable web access, while all other engines use MCP servers for web search capabilities

- **Evidence**: The feature comparison table shows `web-search:` as `✓ (opt-in)` for
  Codex and `via MCP` for all other engines. This is consistent with
  `docs-ghaw-tools-reference.md` Claim 3 (`web-search:` disabled by default for
  Codex, enabled when explicitly declared).
- **Confidence**: settled (corroborated by two first-party sources)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The Codex web-search default is the only built-in tool with a
  documented engine-specific behavior difference. It is a migration footgun:
  practitioners porting a Copilot or Claude workflow to Codex will find that web
  search silently stops working unless `web-search:` is explicitly declared.
  This claim corroborates `docs-ghaw-tools-reference.md` Claim 3 — the engines
  reference is the second corpus source confirming this behavior.

### Claim 10: The `token-weights` field allows overriding cost multipliers per model and per token class — enabling accurate cost accounting for custom or non-standard model deployments

- **Evidence**: The reference documents `token-weights.multipliers` (per-model
  multipliers, e.g., `my-custom-model: 2.5`) and `token-weights.token-class-weights`
  (per-class overrides, e.g., `output: 6.0`, `cached-input: 0.05`). A code example
  shows both in use for a non-standard model.
- **Confidence**: settled (first-party reference; field names and structure are
  explicitly documented with examples)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: `token-weights` is primarily useful for two scenarios: (1) custom
  or enterprise model deployments where the platform's default cost model doesn't
  match actual pricing, and (2) experimental workflows where practitioners want to
  model the cost impact of cached input tokens differently. For teams using
  `docs-ghaw-effective-tokens-specification.md`'s effective token metric, the
  `token-class-weights` overrides enable adjusting the effective-to-nominal token
  ratio for non-standard providers. For Ch02: document `token-weights` as an advanced
  cost-modeling field for non-standard deployments; most teams will not need it.
  Cross-reference `docs-ghaw-effective-tokens-specification.md` for the effective
  tokens model that `token-class-weights` feeds into.

## Concrete Artifacts

### Engine Selection Table

From `https://github.github.com/gh-aw/reference/engines`:

```
| Engine                    | engine: value | Required Secret         |
|---------------------------|---------------|-------------------------|
| GitHub Copilot CLI (default) | copilot    | COPILOT_GITHUB_TOKEN    |
| Claude by Anthropic       | claude        | ANTHROPIC_API_KEY       |
| OpenAI Codex              | codex         | OPENAI_API_KEY          |
| Google Gemini CLI         | gemini        | GEMINI_API_KEY          |
| Crush (experimental)      | crush         | COPILOT_GITHUB_TOKEN    |
| OpenCode (experimental)   | opencode      | COPILOT_GITHUB_TOKEN    |
```

*Note: table structure returned by AI-processed WebFetch; verify against source before citing as verbatim.*

### Feature Support Comparison (AI-processed)

From `https://github.github.com/gh-aw/reference/engines`:

```
Feature               | Copilot | Claude | Codex | Gemini | Crush | OpenCode
----------------------|---------|--------|-------|--------|-------|----------
max-turns             |    ✗    |   ✓    |   ✗   |   ✗    |   ✗   |    ✗
max-continuations     |    ✓    |   ✗    |   ✗   |   ✗    |   ✗   |    ✗
tools.web-search      | via MCP | via MCP| opt-in| via MCP|via MCP| via MCP
engine.agent          |    ✓    |   ✗    |   ✗   |   ✗    |   ✗   |    ✗
engine.api-target     |    ✓    |   ✓    |   ✓   |   ✓    |   ✓   |    ✓
engine.bare           |    ✓    |   ✓    |   ✓   |   ✓    |   ✗   |    ✗
engine.harness        |    ✓    |   ✗    |   ✗   |   ✗    |   ✗   |    ✗
Tools allowlist       |    ✓    |   ✓    |   ✓   |   ✓    |   ✗   |    ✗
```

*Note: table structure returned by AI-processed WebFetch; verify against source before citing as verbatim.*

### Engine Configuration YAML Examples

From `https://github.github.com/gh-aw/reference/engines` (returned by WebFetch):

```yaml
# Full engine configuration with all main fields (Copilot)
engine:
  id: copilot
  version: latest
  model: gpt-5
  command: /usr/local/bin/copilot
  args: ["--add-dir", "/workspace"]
  agent: agent-id
  api-target: api.acme.ghe.com
```

```yaml
# Version pinning
engine:
  id: copilot
  version: "0.0.422"
```

```yaml
# Custom agent file (Copilot only)
engine:
  id: copilot
  agent: technical-doc-writer
```

```yaml
# Environment variable injection
engine:
  id: copilot
  env:
    DEBUG_MODE: "true"
    AWS_REGION: us-west-2
    CUSTOM_API_ENDPOINT: https://api.example.com
```

```yaml
# api-target for GHES routing (hostname only — no protocol or path)
engine:
  id: copilot
  api-target: api.acme.ghe.com
network:
  allowed:
    - defaults
    - acme.ghe.com
    - api.acme.ghe.com
```

```yaml
# Codex with custom model router
engine:
  id: codex
  model: gpt-4o
  env:
    OPENAI_BASE_URL: "https://llm-router.internal.example.com/v1"
    OPENAI_API_KEY: ${{ secrets.LLM_ROUTER_KEY }}
network:
  allowed:
    - github.com
    - llm-router.internal.example.com
```

```yaml
# Custom provider via Copilot engine
engine:
  id: copilot
  env:
    COPILOT_PROVIDER_BASE_URL: ${{ secrets.PROVIDER_BASE_URL }}
    COPILOT_MODEL: claude-sonnet-4
    COPILOT_PROVIDER_API_KEY: ${{ secrets.PROVIDER_API_KEY }}
network:
  allowed:
    - defaults
    - your-provider-domain.example.com
```

```yaml
# bare mode — disables automatic context loading
engine:
  id: claude
  bare: true
```

```yaml
# token-weights — custom cost multipliers
engine:
  id: claude
  token-weights:
    multipliers:
      my-custom-model: 2.5
      experimental-llm: 0.8
    token-class-weights:
      output: 6.0
      cached-input: 0.05
```

```yaml
# Three-level timeout stack for a complex Claude workflow
engine:
  id: claude
max-turns: 20
tools:
  timeout: 600
timeout-minutes: 60
```

```yaml
# Copilot autopilot mode with timeouts
engine:
  id: copilot
max-continuations: 3
timeout-minutes: 60
```

### Claude Permission Mode Descriptions

From `https://github.github.com/gh-aw/reference/engines` (returned by WebFetch;
likely close to verbatim given specificity):

```
acceptEdits mode (default):
  "In this mode, Claude honors the --allowed-tools flag. The workflow's declared
  tools: and mcp-servers: allowed: configuration is compiled into an explicit
  allowlist and passed to the Claude CLI. Only the tools listed there are
  accessible to the agent."

bypassPermissions mode:
  "When the workflow grants unrestricted bash access — bash: "*", bash: [":*"],
  or bash: null — gh-aw switches to --permission-mode bypassPermissions. In this
  mode, Claude Code silently ignores --allowed-tools. Every tool exposed by the
  MCP gateway is reachable regardless of the workflow's declared tool configuration."
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-tools-reference.md` Claim 3 ("`web-search:` is disabled by default
    for the Codex engine... only enabled when explicitly declared"): The engines
    reference feature table shows the same information — Codex web-search is
    `opt-in` while other engines access web search via MCP. Two first-party sources
    now confirm this Codex-specific default.
  - `docs-ghaw-copilot-agent-files.md` Claim 1 ("Copilot supports agent files
    natively, while other engines (Claude, Codex) inject the markdown body as a
    prompt"): The engines reference feature table confirms `engine.agent` (✓ Copilot
    only). The two sources agree on which engines support native agent file processing.
  - `docs-ghaw-agentic-ops.md` Claim 8 (the reference implementation uses
    `gh aw logs --engine copilot`): Consistent with Claim 1 here — Copilot is the
    default engine requiring `COPILOT_GITHUB_TOKEN`. The agentic-ops implementation
    specifically targets the Copilot engine by name in its CLI invocation.
  - `docs-ghaw-frontmatter-full-reference.md` Claim 6 (`engine.max-turns` described
    as "Maximum chat iterations per run (prevents runaway loops)"): Corroborates
    Claim 3 here. The frontmatter reference confirms the anti-runaway framing; the
    engines reference adds the engine-specificity constraint (Claude only).
  - `docs-ghaw-frontmatter-full-reference.md` Claim 7 (`engine.bare` described as
    "Disable auto-loading of context/custom instructions"): Corroborates the `bare`
    field in Claim 4 here.

- **Extends**:
  - `docs-ghaw-how-they-work.md`: That conceptual reference explicitly notes it
    "Does NOT cover... how to choose between engine providers." This engines reference
    is the filling for that gap — it is the engine selection and configuration guide.
  - `docs-ghaw-frontmatter-full-reference.md` Claim 5 (custom provider/runtime via
    `engine.runtime` + `engine.provider`): The frontmatter reference documents the
    full custom provider schema; this engines reference adds the practical YAML
    examples showing provider routing via `engine.env` for common routing patterns
    (custom model routers, GHES endpoints).
  - `docs-ghaw-agentic-authoring.md`: That guide covers the authoring lifecycle
    (init, create, migrate, debug) but does not discuss engine selection or
    configuration options. This reference adds the engine layer as a workflow
    design consideration absent from the authoring guide.

- **Contradicts**: None identified. All claims about engine capabilities are either
  novel to this source (engine selection table, Claude permission modes) or corroborate
  existing notes (Codex web-search, Copilot agent files). No existing source note
  makes claims that oppose the feature table or permission mode descriptions here.

- **Novel**:
  - **Six-engine enumeration with required secrets** (Claim 1): No prior corpus source
    enumerates all six engines and their credential requirements in one place. Prior
    notes reference Copilot as the default and note Claude as an alternative, but
    the complete set (including Gemini, Crush, OpenCode) is new to the corpus.
  - **`max-turns` as Claude-exclusive and `max-continuations` as Copilot-exclusive**
    (Claims 2 and 3): The engine-specificity of these iteration controls is not
    documented in any existing source note at the feature-comparison level.
    `docs-ghaw-frontmatter-full-reference.md` Claim 6 documents `max-turns` as a
    field but does not specify it is Claude-only.
  - **Claude `acceptEdits` / `bypassPermissions` permission mode detail** (Claims 6
    and 7): The two-mode enforcement behavior — including the specific trigger
    (`bash: "*"`, `bash: [":*"]`, or `bash: null`) and the consequence ("Claude Code
    silently ignores `--allowed-tools`") — is not documented in any existing source
    note. This is the most security-relevant novel finding in this source.
  - **`token-weights` configuration** (Claim 10): No existing source note documents
    the `token-weights.multipliers` and `token-weights.token-class-weights` sub-fields.
    Prior sources cover the effective tokens specification (`docs-ghaw-effective-tokens-specification.md`)
    but not the per-workflow cost model override mechanism.
  - **Crush and OpenCode as experimental engines** (Claim 1): Neither engine is
    mentioned in any existing corpus source note. Their existence (using
    `COPILOT_GITHUB_TOKEN`, status: experimental) is new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add an engine selection section: document the six engines with their required
    secrets, then provide selection guidance: default to Copilot for the broadest
    feature support; switch to Claude when iteration limit control via `max-turns`
    is required; switch to Codex or Gemini for specific provider ecosystem reasons.
    Note that Crush and OpenCode are experimental and may not be production-ready.
  - Add the complete `engine:` sub-field reference (Claim 4): `id`, `version`,
    `model`, `command`, `args`, `agent` (Copilot only), `api-target`, `env`, `bare`,
    `harness` (Copilot only), `token-weights`. Currently, the guide does not document
    this configuration surface.
  - Add the three-level timeout stack (Claim 8): `timeout-minutes` (job-level wall
    clock, default 20m), `tools.timeout` (per-tool-call), and `max-turns`/
    `max-continuations` (engine-specific iteration limit). Provide the recommended
    configuration for simple vs. complex workflows.
  - Add the `api-target` hostname-only format constraint (Claim 5) as a footgun
    warning. This is the kind of error that produces a silent misroute rather than
    a clear error message.

- **Chapter 03 (Safety and Verification)**:
  - Add Claude's `bypassPermissions` trigger and consequence as a security design
    note (Claims 6 and 7): granting unrestricted bash to a Claude workflow disables
    the client-side `--allowed-tools` enforcement layer. The MCP gateway `allowed:`
    filter becomes the only enforcement boundary. Practitioners must audit MCP
    `allowed:` declarations before granting unrestricted bash to Claude workflows.
    This is a non-obvious security property that requires explicit documentation.

## Extraction Notes

1. **WebFetch processes content through an AI model**: This page's content was not
   available as raw HTML — the WebFetch tool summarizes page content via an AI model
   before returning. Three separate fetches were performed to maximize fidelity.
   Passages cited as quotes were returned consistently across multiple fetches in
   the same specific form; they are marked with notes where the verbatim character
   cannot be fully guaranteed. The Assayer should spot-check the Claude permission
   mode text (Claim 6 / Concrete Artifacts section) and the `api-target` format
   constraint (Claim 5) against the live source URL.

2. **Feature comparison table is AI-reconstructed**: The feature table in Concrete
   Artifacts was returned by AI-processed WebFetch. Individual cells (particularly
   `max-runs` and `tools.allowlist` rows) should be verified against the live page.
   The Copilot-only status of `engine.agent`, `engine.harness`, and `max-continuations`
   was consistent across all three fetches and corroborated by existing corpus sources;
   the Claude-only status of `max-turns` was consistent across all three fetches and
   corroborated by `docs-ghaw-frontmatter-full-reference.md` Claim 6.

3. **YAML code examples are likely verbatim**: The YAML code blocks were returned
   as structured code, not prose summaries. Code blocks are less susceptible to
   AI-model paraphrasing than prose. The YAML field names, values, and structure
   are specific enough (e.g., `COPILOT_PROVIDER_BASE_URL`, `token-class-weights:`,
   `cached-input: 0.05`) to be treated as close to verbatim from the source.

4. **No contradictions filed**: Reviewed all existing GHAW source notes. No claims
   here materially oppose existing source notes. The Claude permission mode detail
   (Claims 6 and 7) is novel to the corpus; no prior note makes claims about
   `acceptEdits` vs. `bypassPermissions` mode semantics.

5. **Prospector triage accuracy**: The Prospector assessed novelty as low-to-medium
   and noted `docs-ghaw-agentic-ops.md` as briefly mentioning `--engine copilot`.
   After deep reading, the novel content is higher than low — specifically the Claude
   permission mode behavior (Claims 6 and 7) and the six-engine feature comparison
   (Claims 2 and 3) are materially new. The Prospector's priority:low assessment
   may reflect uncertainty before deep reading; recommend upgrading to priority:medium
   based on the security-relevant Claim 6 finding.
