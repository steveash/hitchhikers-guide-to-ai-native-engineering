---
source_url: https://github.github.com/gh-aw/guides/third-party-agent
source_type: docs
title: "GitHub Agentic Workflows: How to Configure a Third-Party Agent"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: settled
issue: "#1893"
---

# GitHub Agentic Workflows: How to Configure a Third-Party Agent

> The practitioner guide for integrating a coding agent CLI that is not one of
> gh-aw's seven built-in engines — using OpenCode as the worked example — via
> a publisher-distributed "engine definition file" that gh-aw registers at
> compile time through the `imports:` mechanism, with no changes to the gh-aw
> binary required.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/third-party-agent`
  page — in the "Guides" section of site navigation, alongside "Agentic
  Authoring," "Network Configuration," and "Azure OpenAI BYOK." This is a
  how-to guide, not a reference/spec page: it walks through one worked example
  end to end rather than enumerating the full configuration surface.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team that operates the gh-aw platform and authored the "AI Engines
  Reference" (`docs-ghaw-engines-reference.md`). Claims about the mechanism
  (`engine.behaviors` format, compile-time registration, frontmatter fields)
  are authoritative platform facts. The choice of OpenCode as the example is
  illustrative, not a platform endorsement claim.
- **Scope**: The third-party engine integration mechanism — how a publisher
  distributes an engine definition file, how a workflow imports it, how
  credentials and network access are configured, and how version pinning and
  recompilation work. Uses OpenCode as the sole worked example. Does NOT
  cover: the seven built-in engines' configuration surface (see
  `docs-ghaw-engines-reference.md`), the general `imports:` field mechanics
  and frontmatter-merging behavior beyond this one use case, or network
  ecosystem identifiers in depth (see `docs-ghaw-guides-network-configuration.md`
  and `docs-ghaw-network-reference.md`, both linked from this page's "Related
  documentation" section).

## Extracted Claims

### Claim 1: Third-party coding agent CLIs not built into gh-aw integrate through a declarative engine definition file that the agent publisher — not GitHub — distributes and maintains
- **Evidence**: Opening framing sentence of the guide, stated before any
  worked example is introduced.
- **Confidence**: settled (first-party platform documentation stating the
  general integration model)
- **Quote**: "Third-party coding agent CLIs that are not built into gh-aw can integrate through a declarative engine definition file that the agent publisher distributes."
- **Our assessment**: This inverts the usual "GitHub adds engine support"
  model documented in `docs-ghaw-engines-reference.md` (Claim 1's seven
  built-in engines, each shipped and maintained by the gh-aw team). Here the
  integration burden shifts to the third-party publisher, who owns and
  updates the engine definition file in their own repository. gh-aw's role
  is limited to interpreting a declarative spec format
  (`engine.behaviors`) at compile time. This is the mechanism that lets the
  engine roster grow past the seven built-ins without gh-aw core releases.

### Claim 2: A third-party engine definition file is a Markdown file whose frontmatter uses the `engine.behaviors` format to declare installation, configuration, and execution steps; importing it registers the engine at compile time with no gh-aw binary changes required
- **Evidence**: "How third-party engine integration works" section, the
  guide's core mechanism statement.
- **Confidence**: settled (first-party; describes the compile-time
  registration mechanism explicitly)
- **Quote**: "A third-party agent publishes a Markdown engine definition file to their GitHub repository. The file's frontmatter declares the agent's installation, configuration, and execution steps using the engine.behaviors format. When a workflow imports that file, gh-aw registers the engine at compile time — no changes to the gh-aw binary are required."
- **Our assessment**: This is the load-bearing architectural claim of the
  whole guide: `engine.behaviors` is a plugin-like extension point built on
  top of the existing `imports:` mechanism (rather than a separate plugin
  system). Compile-time registration means the engine only becomes "known"
  to gh-aw when a workflow explicitly imports the definition file — there is
  no global engine registry to update. This is consistent with gh-aw's
  general compile-then-run model (`gh aw compile` materializes frontmatter
  into `lock.yml`, per `docs-ghaw-compilation-process.md`).

### Claim 3: OpenCode is presented as the concrete worked example — an open-source, provider-agnostic, BYOK coding agent supporting 75+ models from Anthropic, OpenAI, Google, Groq, and others via a unified CLI
- **Evidence**: "Example: OpenCode" section, opening description.
- **Confidence**: settled (first-party guide; the multi-provider claim is
  presented as fact about OpenCode, not independently verified against the
  OpenCode project itself)
- **Quote**: "OpenCode is an open-source, provider-agnostic AI coding agent (BYOK — Bring Your Own Key) that supports 75+ models from Anthropic, OpenAI, Google, Groq, and others via a unified CLI interface."
- **Our assessment**: OpenCode's "provider-agnostic" design is precisely why
  it needs the `network.allowed` + credential guidance later in the guide
  (Claims 5 and 6) — unlike a single-provider built-in engine, an OpenCode
  workflow's network and secret requirements depend on which provider the
  operator points it at. Note this guide's own definition of OpenCode's
  "BYOK" differs from GitHub Copilot's BYOK feature covered in
  `docs-github-copilot-byok-app.md` and `docs-github-copilot-byok-vscode.md`
  — those describe routing GitHub Copilot itself through a customer-supplied
  model endpoint; here "BYOK" describes OpenCode's own multi-provider
  credential model, unrelated to Copilot. Different product surfaces, same
  term — worth flagging so the guide doesn't conflate the two BYOK patterns.

### Claim 4: The OpenCode engine definition file's `engine.behaviors` block fully specifies installation (npm package, pinned version, verify command), a config-file to write, and the execution command/args — all without any gh-aw-side code
- **Evidence**: Full YAML frontmatter of `opencode-engine.md`, reproduced
  in the guide as the worked example (see Concrete Artifacts).
- **Confidence**: settled (first-party; this is the literal file content
  shown in the guide, described as published by the OpenCode project)
- **Quote**: "An agent publisher provides an engine definition file like the following in their repository. The file's engine.behaviors block tells gh-aw exactly how to install, configure, and invoke the CLI:"
- **Our assessment**: The four `behaviors` sub-blocks (`installation`,
  `config-file`, `execution`, `mcp`) form a complete lifecycle spec: how to
  get the binary on the runner (npm install, pinned to `1.2.14`, verified
  with `opencode --version`), what config file to materialize
  (`opencode.jsonc`, merged via `json-merge` so publisher defaults and
  workflow overrides combine rather than clobber), and how to invoke it
  (`opencode run --print-logs --log-level DEBUG`, with model and MCP config
  injected via named env vars). `secret-strategy: universal-llm-consumer`
  and `provider-env-mode: universal-llm-consumer` are the fields that let
  one engine definition support many providers rather than being hardcoded
  to one — this is the "provider-agnostic" claim (Claim 3) made concrete in
  configuration.

### Claim 5: A workflow adopts a third-party engine by setting `engine: <id>` and adding a version-pinned import reference to the engine definition file; the imported reference should be pinned to a tag or SHA, not tracked unpinned
- **Evidence**: "Configure a workflow to use OpenCode" section, with a
  worked frontmatter example (`imports: - sst/opencode/.github/workflows/opencode-engine.md@v1.2.14`)
  and an explicit pinning recommendation.
- **Confidence**: settled (first-party; the pinning guidance is stated as
  an imperative instruction, not a suggestion framed as optional)
- **Quote**: "Pin the import to a specific tag or SHA to control when you pick up new versions of the engine definition."
- **Our assessment**: This mirrors the version-pinning discipline documented
  for built-in engines in `docs-ghaw-engines-reference.md` (Claim 4:
  `engine.version` pinning) but applies it to the import reference itself —
  a third-party engine definition can change its own installation/config/
  execution behavior between commits, so pinning the import is a distinct
  supply-chain control from pinning the CLI version (Claim 6 below).
  Unpinned imports (tracking a branch) mean the publisher can silently
  change what gets installed and executed in your workflow's CI runner —
  this is a real supply-chain surface that the guide flags but does not
  elaborate on beyond the one-sentence recommendation.

### Claim 6: The `network.allowed` entry in the workflow must match whichever provider OpenCode is configured to call — `api.anthropic.com` for the default Anthropic provider, or e.g. `api.openai.com` in addition to or instead of it when using an OpenAI model
- **Evidence**: "Configure a workflow to use OpenCode" section, closing
  guidance after the worked frontmatter example.
- **Confidence**: settled (first-party; states the coupling between engine
  provider choice and network allowlist explicitly)
- **Quote**: "The network.allowed entry should match the provider you are using. OpenCode supports multiple providers — for example, add api.openai.com instead of (or in addition to) api.anthropic.com when using an OpenAI model."
- **Our assessment**: This is a third-party-engine-specific instance of the
  general pattern documented in `docs-ghaw-engines-reference.md` Claim 5
  (custom `api-target` must also appear in `network.allowed`) — both cases
  require a paired change across two frontmatter sections that's easy to
  forget. For a single-provider built-in engine (e.g. Claude), the default
  network allowlist can bake in the one required domain; for a
  provider-agnostic third-party engine like OpenCode, the operator must
  actively choose and declare the domain matching whatever provider they
  configured — there is no single correct default.

### Claim 7: OpenCode reads provider credentials from environment variables rather than an engine-specific auth flow; the default Anthropic provider requires `ANTHROPIC_API_KEY` set as a repository or organization secret, and other providers require their own key referenced via the workflow's `engine.env` block
- **Evidence**: "Add the API key secret" section, with a two-step
  repository-settings walkthrough for the default case and a general
  statement for other providers.
- **Confidence**: settled (first-party; states the exact secret name and
  the UI path for configuring it)
- **Quote**: "OpenCode reads provider credentials from environment variables. For the default Anthropic provider, add ANTHROPIC_API_KEY to your repository or organization:"
- **Our assessment**: `ANTHROPIC_API_KEY` as OpenCode's default-provider
  secret name is identical to the secret name gh-aw's own built-in Claude
  engine requires (`docs-ghaw-engines-reference.md` Claim 1). This is not
  coincidental — OpenCode's `secret-strategy: universal-llm-consumer`
  (Claim 4) means it follows the same provider-SDK environment variable
  convention that built-in engines use, so a repository already configured
  for the built-in Claude engine does not need a new secret to also run
  OpenCode against Anthropic. Switching providers (e.g. to OpenAI) requires
  provisioning a *different* secret (`OPENAI_API_KEY`) and explicitly wiring
  it into `engine.env` — it is not automatically picked up the way the
  default-provider secret is.

### Claim 8: The engine definition file's declared default CLI version (under `behaviors.installation.version`) can be overridden per-workflow via `engine.version` in the workflow's own frontmatter, decoupling the CLI version from the engine definition file's version
- **Evidence**: "Pin the engine version" section, with a worked frontmatter
  example showing `engine: { id: opencode, version: "1.3.0" }` alongside the
  same `@v1.2.14`-pinned import.
- **Confidence**: settled (first-party; the override mechanism and its
  independence from the import pin are stated explicitly)
- **Quote**: "The engine definition above declares a default CLI version under behaviors.installation.version. Override it with engine.version in your workflow to pin or upgrade independently of the engine definition file:"
- **Our assessment**: This creates two independent version-pinning axes for
  a third-party engine: the import reference (Claim 5, which version of the
  *engine definition file / integration logic* to use) and `engine.version`
  (which version of the *CLI binary* to install). The worked example shows
  these can legitimately diverge — `imports:` pinned to `@v1.2.14` while
  `engine.version` is set to `"1.3.0"` — meaning a workflow can adopt a
  newer CLI release without waiting for the publisher to cut a new engine
  definition tag, as long as the installation mechanism (npm package name,
  config format) hasn't changed between CLI versions.

### Claim 9: Any edit to workflow frontmatter that touches the import reference, engine version, or other frontmatter fields requires recompilation via `gh aw compile`, because engine settings live in and are resolved from frontmatter
- **Evidence**: "Recompile after workflow edits" section, with a terminal
  command example.
- **Confidence**: settled (first-party; states the recompilation requirement
  as a direct consequence of where engine settings are stored)
- **Quote**: "Engine settings live in workflow frontmatter. Recompile whenever you change the import reference, the engine version, or any other frontmatter field:"
- **Our assessment**: This is a specific instance of the general gh-aw
  compile-then-run architecture (`docs-ghaw-compilation-process.md`) applied
  to the third-party-engine adoption workflow: after any of the changes
  described in Claims 5, 6, or 8 (import pin, network allowlist, engine
  version), the operator must re-run `gh aw compile` before the change takes
  effect in `lock.yml`. The `--watch` flag shown in the command example
  suggests this is intended to be run continuously during iterative
  configuration rather than as a one-off step per edit.

## Concrete Artifacts

### Full OpenCode engine definition file frontmatter (`.github/workflows/opencode-engine.md`, published by the OpenCode project per the guide)

```yaml
---
engine:
  id: opencode
  display-name: OpenCode
  description: OpenCode CLI with headless mode and multi-provider LLM support
  runtime-id: opencode
  experimental: true
  behaviors:
    secret-strategy: universal-llm-consumer
    capabilities:
      max-turns: true
    manifest:
      files:
        - opencode.jsonc
        - AGENTS.md
      path-prefixes:
        - .opencode/
    installation:
      package-manager: npm
      package-name: opencode-ai
      version: "1.2.14"
      step-name: Install OpenCode
      binary-name: opencode
      include-node-setup: true
      cooldown: true
      verify-command: opencode --version
      verify-step-name: Verify OpenCode CLI installation
      docs-url: https://opencode.ai/docs
    config-file:
      path: opencode.jsonc
      step-name: Write OpenCode Config
      content: |-
        {
          "agent": {
            "build": {
              "permission": {
                "bash": "allow",
                "edit": "allow",
                "read": "allow",
                "glob": "allow",
                "grep": "allow",
                "webfetch": "allow",
                "websearch": "allow",
                "external_directory": "allow"
              }
            }
          },
          "autoupdate": false
        }
      merge-strategy: json-merge
    execution:
      command-name: opencode
      args:
        - run
        - --print-logs
        - --log-level
        - DEBUG
      step-name: Execute OpenCode CLI
      model-env-var: OPENCODE_MODEL
      mcp-config-env-var: GH_AW_MCP_CONFIG
      write-timestamp: true
      provider-env-mode: universal-llm-consumer
    mcp:
      config-path: opencode.jsonc
---
```
*Source: https://github.github.com/gh-aw/guides/third-party-agent — "Example: OpenCode" section*

### Workflow frontmatter to adopt the third-party engine

```yaml
on: issues
engine: opencode
imports:
  - sst/opencode/.github/workflows/opencode-engine.md@v1.2.14
network:
  allowed:
    - defaults
    - api.anthropic.com
---
Triage this issue and apply an appropriate label.
```
*Source: https://github.github.com/gh-aw/guides/third-party-agent — "Configure a workflow to use OpenCode" section*

### Version-pinning override example

```yaml
engine:
  id: opencode
  version: "1.3.0"
imports:
  - sst/opencode/.github/workflows/opencode-engine.md@v1.2.14
```
*Source: https://github.github.com/gh-aw/guides/third-party-agent — "Pin the engine version" section*

### Recompile command

```
gh aw compile .github/workflows/my-workflow.md --watch
```
*Source: https://github.github.com/gh-aw/guides/third-party-agent — "Recompile after workflow edits" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-engines-reference.md` Claim 1 (Claude requires
    `ANTHROPIC_API_KEY` as its required secret): this guide's Claim 7 shows
    OpenCode's default-provider secret uses the identical name, corroborating
    that gh-aw's engines share the underlying provider-SDK environment
    variable convention rather than each engine inventing its own secret
    naming scheme.
  - `docs-ghaw-engines-reference.md` Claim 5 (custom `api-target` must also
    appear in `network.allowed` — a paired configuration step that's easy to
    overlook): this guide's Claim 6 is a third-party-engine instance of the
    same paired-configuration pattern (provider choice must be mirrored into
    `network.allowed`).
  - `docs-ghaw-engines-reference.md` Claim 4 (`engine.version` supports
    pinning independent of other configuration): this guide's Claim 8 shows
    the same field applied to a third-party engine, decoupled from the
    import-reference pin.

- **Contradicts**: **`docs-ghaw-engines-reference.md` Claim 1 / feature
  matrix — OpenCode credential mechanism and built-in-vs-third-party status.
  Filed as contradiction issue #1909.** The engines-reference note documents
  a **built-in** `opencode (experimental)` engine whose required secret is
  `COPILOT_GITHUB_TOKEN` (its feature-matrix row reads
  `OpenCode (exp) | COPILOT_GITHUB_TOKEN`, routed through GitHub Copilot
  infrastructure). This guide's Claim 7 (and the reproduced `opencode-engine.md`
  YAML) describes an engine *also* declared as `id: opencode` /
  `experimental: true`, but authenticating via direct provider credentials —
  `ANTHROPIC_API_KEY` for the default Anthropic provider, `OPENAI_API_KEY`
  etc. for others (BYOK). Critically, this guide makes **zero mention** of
  `COPILOT_GITHUB_TOKEN` or of any pre-existing built-in OpenCode engine; it
  presents the third-party engine-definition-file path as the way to run
  OpenCode under gh-aw. So the corpus now contains two notes describing an
  engine with the identical id (`id: opencode`, `experimental: true`) but two
  different, non-overlapping credential mechanisms, and the sources do not
  reconcile them. Two questions are left unresolved by the sources and must
  not be silently collapsed by the Smith: (a) are these two coexisting
  integration paths (built-in Copilot-routed vs. third-party BYOK) that
  happen to share an id, or does one supersede the other; and (b) if a
  workflow `imports:` the third-party `opencode-engine.md` while `engine:`
  is set to the same `opencode` id, does the imported definition
  shadow/override the built-in engine or collide with it? Neither note
  answers these. Per the Miner process, this is filed for human resolution
  rather than adjudicated here — see issue #1909; no `C-NNN` verdict is
  assigned in this note.

- **Extends**:
  - `docs-ghaw-engines-reference.md` (which documents only the seven
    built-in engines and states their configuration surface authoritatively):
    this guide extends the corpus's engine coverage to the previously
    undocumented case of engines *not* in that seven-engine roster —
    third-party engines integrated purely through publisher-distributed
    `imports:` content, with no gh-aw-side code changes. Note, however, that
    the engines reference's Claim 1 roster (Copilot, Claude, Codex, Gemini,
    Crush, OpenCode, Pi) already lists OpenCode as one of its seven engines
    with `experimental: true` — and, unlike this guide, ties it to
    `COPILOT_GITHUB_TOKEN`. This is **not** a clean "extends" relationship on
    the OpenCode row specifically: whether "OpenCode" in the engines
    reference is the *same* engine as the third-party definition described
    here (differing only in how it is documented) or a *different* built-in
    engine that merely shares the `id: opencode` string is unresolved by the
    sources. That unresolved overlap is filed as a contradiction (issue
    #1909) and captured under the **Contradicts** heading above — do not read
    this "Extends" bullet as having settled it. The genuinely additive part
    of this guide is the *mechanism* (third-party `engine.behaviors` imports),
    which the engines reference does not document at all.
  - `docs-ghaw-custom-agent-for-aw.md` Claim 6 (the authoring agent imports
    workflows from external repositories "with optional customizations like
    engine selection"): this guide extends that by documenting the manual
    mechanics behind an "engine selection" customization when the desired
    engine is a third-party one rather than one of the seven built-ins — the
    `imports:` + `engine: <id>` pattern documented here is what the authoring
    agent would need to produce under the hood for a third-party-engine
    customization.

- **Novel**:
  - **`engine.behaviors` as a publisher-owned extension format** (Claims 1,
    2, 4): No existing source note documents that gh-aw engines can be
    defined entirely outside the gh-aw codebase via a declarative
    `engine.behaviors` YAML block distributed as a Markdown import. This is
    the first corpus entry describing gh-aw's third-party engine extension
    mechanism as opposed to its built-in engine roster.
  - **Two independent version-pinning axes for third-party engines**
    (Claims 5, 8): The distinction between pinning the *import reference*
    (which engine definition/integration logic to use) and pinning
    `engine.version` (which CLI binary to install) is new to the corpus —
    existing notes (`docs-ghaw-engines-reference.md` Claim 4) document only
    the single `engine.version` axis for built-in engines, which have no
    separate "import reference" to pin.
  - **`secret-strategy: universal-llm-consumer` / `provider-env-mode:
    universal-llm-consumer`** (Claim 4): These specific `engine.behaviors`
    field values, and the pattern they enable (one engine definition
    supporting many LLM providers via standard env var conventions), are not
    documented in any existing source note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a subsection on adopting
  third-party (non-built-in) engines, distinct from the existing built-in
  engine selection guidance sourced from `docs-ghaw-engines-reference.md`.
  Specifically: (1) name the `imports:` + `engine: <id>` pattern as the
  adoption mechanism, (2) recommend pinning the import reference to a tag or
  SHA as a supply-chain control (Claim 5) — this is currently undocumented
  in the guide's version-pinning advice, which so far only covers
  `engine.version` for built-in engines, (3) note the paired
  `network.allowed` + provider-secret configuration required for
  provider-agnostic engines like OpenCode (Claims 6, 7), and (4) flag that
  `gh aw compile` must be re-run after any frontmatter change touching the
  import, engine version, or network fields (Claim 9).
  - **Do NOT present OpenCode credential/secret guidance without
    disambiguating the integration path.** This note's Claim 7 says OpenCode
    authenticates via `ANTHROPIC_API_KEY`/`OPENAI_API_KEY` (third-party
    engine-definition import, BYOK), whereas `docs-ghaw-engines-reference.md`
    ties the built-in `opencode (experimental)` engine to
    `COPILOT_GITHUB_TOKEN`. These are documented under the identical
    `id: opencode`. When writing any OpenCode secret guidance into the guide,
    the Smith must explicitly state which path the guidance applies to
    (built-in experimental engine via Copilot token vs. third-party
    engine-definition import via provider API key) and must not merge the two
    into a single "OpenCode needs secret X" statement. This overlap is filed
    as contradiction issue #1909; treat it as unresolved until a `C-NNN`
    verdict lands in CONTRADICTIONS.md.
- **Chapter 05 (Composition & Orchestration)**: Use this guide as the
  concrete example for "how does gh-aw let you bring in agents the platform
  team hasn't built" — a composition pattern distinct from importing
  workflow-authoring agent files (`docs-ghaw-custom-agent-for-aw.md`) or
  Copilot Agent Files as workflow components. The engine-definition-file
  mechanism composes at the *engine* layer rather than the *prompt/role*
  layer.

## Extraction Notes

1. **WebFetch summarized rather than reproduced verbatim content**: an
   initial WebFetch pass returned a paraphrased summary of the page (missing
   the full YAML engine definition and losing exact wording), consistent
   with the extraction caveats noted in `docs-ghaw-engines-reference.md` and
   `docs-ghaw-custom-agent-for-aw.md`. To get verbatim text for quoting, the
   raw page HTML was downloaded directly and converted to plain text with a
   local script, preserving exact wording, YAML content, and section
   structure. All quotes and code blocks in this note are taken from that
   raw-HTML extraction, not from the WebFetch summary.
2. **Single-page source, no sub-pages followed**: the page's "Related
   documentation" section links to the AI Engines Reference, Imports
   Reference, and Network Configuration Guide — all three already have
   existing source notes in the corpus (`docs-ghaw-engines-reference.md`,
   `docs-ghaw-guides-network-configuration.md`; no dedicated "Imports
   Reference" note was found in `source-notes/` under an obvious name, which
   may be a coverage gap worth flagging to the Prospector separately). No
   new sub-pages were fetched since the linked references are already in the
   corpus.
3. **One contradiction filed (issue #1909)**: reviewed against the three
   overlapping notes named by the Prospector (`docs-ghaw-engines-reference.md`,
   `docs-ghaw-agentic-authoring.md`, `docs-ghaw-custom-agent-for-aw.md`) plus
   `docs-ghaw-guides-network-configuration.md` and the two GitHub Copilot
   BYOK notes. Most claims are consistent with or extend existing notes, but
   this guide's Claim 7 (OpenCode via third-party engine-definition import,
   authenticating with `ANTHROPIC_API_KEY`/`OPENAI_API_KEY`) materially
   overlaps `docs-ghaw-engines-reference.md`'s built-in `opencode` engine
   (authenticating with `COPILOT_GITHUB_TOKEN`) under an identical
   `id: opencode`. This overlap is filed as contradiction issue #1909 and
   documented under Cross-References → **Contradicts**; no verdict is assigned
   in this note. (An earlier draft of this note asserted "Contradicts: None
   identified" — that was corrected during Assayer rework.)
