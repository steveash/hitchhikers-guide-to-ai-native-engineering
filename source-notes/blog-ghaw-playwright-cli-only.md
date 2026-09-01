---
source_url: https://github.github.com/gh-aw/blog/2026-09-01-why-playwright-cli-replaces-playwright-mcp/
source_type: blog-post
title: "Why the Built-In Playwright Tool Is Now CLI-Only"
author: Copilot, Peli de Halleux (GitHub Agentic Workflows / Microsoft Research)
date_published: 2026-09-01
date_extracted: 2026-09-01
last_checked: 2026-09-01
status: current
confidence_overall: settled
issue: "#3142"
---

# Why the Built-In Playwright Tool Is Now CLI-Only

> gh-aw's built-in `tools.playwright` integration dropped its Docker-based
> Playwright MCP mode in favor of CLI-only (`@playwright/cli`), trading MCP's
> persistent tool schema and container lifecycle for a single npm package and
> a lighter per-turn token footprint — with MCP still available, but only via
> explicit `mcp-servers:` configuration.

## Source Context

- **Type**: blog-post (official GitHub Agentic Workflows blog, `blog/` section
  — a short first-party platform-change announcement, distinct from the
  `reference/` and `troubleshooting/` documentation sections cited elsewhere
  in this corpus). One linked page was followed per MINER.md §1: the
  `reference/playwright/` page, which the blog post itself points to as "the
  Playwright reference for the full migration table from MCP tool names to
  `playwright-cli` subcommands." That reference page supplied the
  Configuration, Network Access, AWF Sandbox Policy, Migration, "What if you
  really want MCP?", and Common Use Cases sections extracted below.
- **Author credibility**: First-party from the GitHub Agentic Workflows team.
  Byline credits "Copilot" and Peli de Halleux (Microsoft Research) — the
  same author credited on the `docs-ghaw-*` reference pages already in this
  corpus (e.g. `docs-ghaw-tools-reference.md`, `docs-ghaw-mcps.md`). Claims
  about `gh-aw` compiler behavior, tool defaults, and configuration schema
  are authoritative for the platform; they do not generalize to other
  agentic frameworks' MCP-vs-CLI tradeoffs without independent evidence.
- **Scope**: Covers the built-in `tools.playwright` integration specifically —
  why its default mode changed from MCP (Docker) to CLI, the two stated
  rationales (token cost, attack surface), how to keep using MCP explicitly,
  and the migration path (command mapping, network configuration, sandbox
  policy). Does NOT cover: `@playwright/cli`'s full command reference beyond
  the commands shown in examples, non-Playwright built-in tools (see
  `docs-ghaw-tools-reference.md`), or MCP servers generally (see
  `docs-ghaw-mcps.md`).

## Extracted Claims

### Claim 1: The built-in Playwright tool now supports CLI mode only; the compiler rejects `mode: mcp` as a compile-time error with migration guidance, rather than silently starting a Docker container as before
- **Evidence**: Opening paragraph states the tool "used to support two modes: a
  Docker-based MCP server (`mode: mcp`) and a CLI-based integration
  (`mode: cli`)," and that as of this change "the built-in tool only supports
  CLI mode, and the compiler rejects `mode: mcp` with migration guidance
  instead of quietly starting a container." The reference page confirms: "The
  compiler now reports `mode: mcp` as an error."
- **Confidence**: settled (first-party platform-change announcement with a
  corroborating reference-page statement)
- **Quote**: "The built-in `tools.playwright` integration in `gh-aw` used to
  support two modes: a Docker-based MCP server (`mode: mcp`) and a CLI-based
  integration (`mode: cli`). As of this change, the built-in tool only
  supports CLI mode, and the compiler rejects `mode: mcp` with migration
  guidance instead of quietly starting a container."
- **Our assessment**: The shift from "silently starting a container" to a
  compile-time error is itself notable independent of the CLI-vs-MCP debate —
  it converts a previously implicit default (whichever mode a workflow's
  `mode:` value or absence resolved to) into an explicit, validated choice.
  This directly updates `docs-ghaw-tools-reference.md` Claim 10, which
  documented `playwright:` version pinning without noting any `mode:`
  distinction — that note was extracted 2026-05-11, before this change
  shipped. For Ch02: any existing guide content describing `tools.playwright`
  configuration needs an update to reflect `mode: cli` as the only built-in
  option, with `mode: mcp` now a compile error rather than a valid setting.

### Claim 2: MCP servers load a schema for every available tool into the model's context window on every turn, regardless of use; Playwright MCP's wide tool surface makes this cost concrete
- **Evidence**: The "Fewer tokens spent on tool schemas" section states the
  general MCP mechanism, then names Playwright MCP's specific surface.
- **Confidence**: settled (first-party mechanism description, consistent with
  the documented MCP protocol behavior)
- **Quote**: "MCP servers advertise their tools to the agent by loading a
  schema for every available function into the model's context window.
  Playwright MCP exposes a wide surface of browser-automation tools —
  navigation, snapshots, clicks, evaluation, tracing, and more — and all of
  that schema has to be paid for in tokens on every turn, whether or not the
  agent uses most of it."
- **Our assessment**: This is a first-party platform team independently
  arriving at the same mechanism `blog-bswen-mcp-token-cost.md` Claim 1
  documents from a practitioner's `/context` measurement ("Every MCP server
  you connect loads all its tool definitions into Claude's system prompt...
  before you even start working"). Bswen measured the effect (~5-7k
  tokens/server); this source names the mechanism as the explicit design
  rationale for removing a specific built-in MCP integration. That two
  independent sources — a practitioner audit and a platform team's own
  architecture decision — converge on "MCP schema loading is a real,
  per-turn cost regardless of tool use" strengthens the claim's standing in
  the corpus.

### Claim 3: `@playwright/cli` replaces the MCP tool schema with a single `playwright-cli` command the agent invokes from bash, needing only to have seen `playwright-cli --help` once (or installed skills via `playwright-cli install --skills`)
- **Evidence**: Direct continuation of the token-cost rationale, naming the
  CLI's onboarding mechanism.
- **Confidence**: settled (first-party description of the CLI's design)
- **Quote**: "`@playwright/cli` instead exposes a single command,
  `playwright-cli`, that the agent invokes directly from bash with a
  subcommand such as `goto`, `snapshot`, or `click`. The agent only needs to
  have seen `playwright-cli --help` once (or installed skills via
  `playwright-cli install --skills`) to know how to drive the browser."
- **Our assessment**: "Installed skills via `playwright-cli install --skills`"
  is a concrete, previously undocumented detail in this corpus: the CLI
  ships its own skill-installation subcommand, implying `@playwright/cli`
  packages Claude Skills (or an equivalent skill-file format) alongside the
  binary rather than requiring gh-aw or the practitioner to author them
  separately. This is a fourth context-management lever for tool
  onboarding — alongside `--help` output, MCP tool schemas, and manually
  written CLAUDE.md instructions — that no other Ch04-relevant source in
  the corpus documents for a CLI tool specifically.

### Claim 4: The built-in Playwright tool's attack surface shrank specifically because Docker container lifecycle management (image version, extra MCP arguments, mounted volumes) was replaced by a single versioned npm package installed directly on the runner
- **Evidence**: The "A smaller, more auditable attack surface" section
  contrasts what the compiler had to track under MCP mode against the CLI
  mode's single package.
- **Confidence**: settled (first-party architectural rationale)
- **Quote**: "The built-in MCP mode ran Playwright inside a Docker container
  with its own image, arguments, and lifecycle that the compiler had to
  track, pin, and update independently. Every one of those knobs — container
  image version, extra MCP arguments, mounted volumes — was one more thing
  that could silently drift out of date or be misconfigured across
  workflows... CLI mode collapses that surface. `@playwright/cli` is a
  single npm package installed directly on the runner, with one version to
  track and one command surface to allow through the shell permission
  system."
- **Our assessment**: This names the previously-removed built-in MCP mode as
  Docker-based, which corroborates and dates `docs-ghaw-mcps.md` Claim 2's
  four-type MCP server taxonomy (stdio/Docker/HTTP/registry) — the built-in
  Playwright MCP was specifically the Docker type, the highest-isolation but
  highest-operational-complexity option in that taxonomy. The tradeoff named
  here (fewer configuration knobs = less to misconfigure or let drift) is a
  concrete instance of the general "less machinery, less to audit" security
  argument, though it is worth noting this argument trades container-level
  network/filesystem isolation (Docker) for shell-permission-system
  isolation (CLI on the runner) — a different isolation boundary, not simply
  "more secure" in every dimension. The guide should present this as a
  tradeoff, not an unqualified security upgrade.

### Claim 5: Running Playwright CLI directly on the runner (instead of in a separate Docker container) enables direct `localhost` access to local development servers without additional network configuration between container and host
- **Evidence**: Final sentence of the attack-surface section.
- **Confidence**: settled (first-party, direct architectural consequence)
- **Quote**: "Because it runs on the runner instead of in a separate
  container, it also reaches local development servers through `localhost`
  directly, without needing extra network plumbing between a container and
  the host."
- **Our assessment**: This is a genuine developer-experience win independent
  of the token/attack-surface arguments: Docker-based Playwright MCP would
  have needed explicit network bridging (e.g., `host.docker.internal` or
  equivalent) to reach a dev server running on the runner's own localhost —
  a common source of "why can't my browser automation reach my app"
  confusion. The reference page's example workflows (Concrete Artifacts,
  below) rely on this directly: the Visual Regression and End-to-End Testing
  examples start a dev server with `steps:` and then have Playwright CLI hit
  `http://localhost:4321` / `http://localhost:3000` with no network bridge
  configuration beyond the standard `network.allowed` domain list.

### Claim 6: MCP remains available for Playwright, but only via explicit `mcp-servers:` configuration naming the dependency, pinned package version, and exact allowed tool list — no longer an implicit built-in default
- **Evidence**: The "MCP is still available, just not built-in" section
  names the use case (persistent state, iterative reasoning) and the
  explicit-configuration requirement; the reference page's "What if you
  really want to use MCP?" section supplies the concrete YAML.
- **Confidence**: settled (first-party, with a worked configuration example)
- **Quote**: "Some workflows genuinely benefit from MCP's persistent state
  and richer introspection — for example, exploratory automation or
  self-healing tests that need to reason iteratively over page structure
  across many turns. That use case has not gone away; it is just no longer a
  hidden default."
- **Quote (reference page, config requirement)**: "Custom MCP servers are not
  covered by the built-in Playwright compatibility or version tracking. Pin
  and update the package deliberately, restrict `allowed` to the required
  tools, and follow the custom MCP server guidance."
- **Our assessment**: "Exploratory automation or self-healing tests that need
  to reason iteratively over page structure across many turns" is the
  specific use-case boundary the platform team draws between CLI and MCP for
  browser automation: CLI for scripted/deterministic browser interactions
  (navigate, click, screenshot in a known sequence), MCP for cases where the
  agent needs the richer, stateful tool-calling loop to explore an unknown
  page structure. This corroborates `docs-ghaw-mcps.md` Claim 3's `allowed:`
  minimal-privilege discipline — the custom Playwright MCP config example
  restricts `allowed:` to exactly `[browser_navigate, browser_snapshot]` (blog
  example) or additionally `browser_take_screenshot` (reference page
  example), not `["*"]"`, consistent with that note's recommendation to name
  specific tools rather than defaulting to unrestricted access.

### Claim 7: Default network access for the built-in Playwright CLI tool is restricted to `localhost` and `127.0.0.1` only; reaching browser binary downloads or external test targets requires adding the `playwright` ecosystem identifier and/or explicit domains to `network.allowed`
- **Evidence**: The reference page's "Network Access" subsection.
- **Confidence**: settled (first-party network configuration reference)
- **Quote**: "Domain access is controlled by the top-level `network:` field.
  By default, Playwright can only reach `localhost` and `127.0.0.1`."
- **Our assessment**: This is a new ecosystem identifier — `playwright` —
  not present in `docs-ghaw-network-reference.md` Claim 4's enumerated list
  of ecosystem identifiers (`defaults`, `github`, `local`, `dev-tools`,
  `containers`, `linux-distros`, `python`, `node`, `rust`, `go`, `java`,
  `deno`), which was extracted 2026-05-11. This is not a contradiction — that
  note never claimed its list was permanently exhaustive — but it is a
  concrete platform addition the network reference note should be updated to
  include. The reference page's own example comments the identifier as
  `- playwright   # enables browser downloads`, confirming its specific
  purpose (reaching the Playwright browser-binary CDN) rather than being a
  general "allow all Playwright-related traffic" grant.

### Claim 8: When a workflow runs inside the AWF sandbox, the compiler injects an additional policy prompt reinforcing a specific secure browser topology, which takes precedence over generic Playwright CLI skill suggestions like `npm install`/`npx` fallback installation
- **Evidence**: The reference page's "AWF Sandbox Policy" subsection, verbatim.
- **Confidence**: settled (first-party sandbox behavior description)
- **Quote**: "When the workflow runs inside the AWF sandbox (`sandbox.agent`
  enabled, or the firewall enabled by default for the configured engine), the
  compiler injects an additional policy prompt reinforcing the secure browser
  topology: bind local servers to `127.0.0.1` only, wait for a loopback
  readiness check before navigating, keep `localhost`/`127.0.0.1` on the
  proxy bypass list, and never install packages or browsers at runtime. This
  guidance takes precedence over generic Playwright CLI skill suggestions
  such as `npm install`/`npx` fallback installation or navigating to
  arbitrary example domains."
- **Our assessment**: This is a concrete, previously undocumented example of
  a compiler-injected prompt overriding a tool's own default skill
  guidance — a governance mechanism not described in `docs-ghaw-how-they-work.md`'s
  five-layer security model as extracted so far. "Never install packages or
  browsers at runtime" directly closes a supply-chain risk: without this
  override, a generic Playwright CLI skill might suggest `npx
  playwright@latest install` as a fallback if the browser binary is missing,
  which would pull an unpinned package at runtime inside the sandbox. For
  Ch03 (Safety and Verification): document compiler-injected policy prompts
  that override tool-level default guidance as a distinct security
  mechanism from network allowlisting or the `allowed:` tool filter — it
  operates at the prompt-instruction layer, not the protocol/network layer.

### Claim 9: The official migration path replaces five specific Playwright MCP tool calls with five `playwright-cli` bash commands, and instructs removing MCP-specific tool names (e.g. `mcp__playwright__browser_navigate`) from prompts and engine allowlists
- **Evidence**: The reference page's "Migrate from Playwright MCP" table and
  accompanying instructions, fetched verbatim from the page's raw HTML.
- **Confidence**: settled (first-party migration reference) — see Claim 10
  and Extraction Notes for an important caveat about internal consistency.
- **Quote**: "Replace MCP tool calls in prompts with equivalent
  `playwright-cli` commands run through bash." Migration table: `browser_navigate`
  → `playwright-cli goto <url>`; `browser_snapshot` → `playwright-cli
  snapshot`; `browser_take_screenshot` → `playwright-cli screenshot
  --filename <path>`; `browser_click` → `playwright-cli click <ref>`;
  `browser_evaluate` → `playwright-cli eval "() => document.title"`.
- **Quote (cleanup instruction)**: "Remove Playwright MCP container arguments
  and MCP-specific tool names such as `mcp__playwright__browser_navigate`
  from prompts and engine allowlists."
- **Our assessment**: This table is the authoritative statement of what the
  post-migration command surface should look like: short verbs (`goto`,
  `snapshot`, `screenshot`, `click`, `eval`) with no `browser_` prefix. This
  matters directly for Ch02 if the guide reproduces any Playwright CLI
  example — see Claim 10, which documents that the same reference page's own
  worked examples do not consistently follow this table.

### Claim 10: The reference page's own "Common Use Cases" worked examples (Accessibility Testing, Visual Regression Testing, End-to-End Testing) contradict the migration table by using MCP-style `browser_`-prefixed names as `playwright-cli` subcommands
- **Evidence**: Verbatim code blocks from the same reference page, extracted
  from raw HTML line-by-line to rule out a rendering artifact.
- **Confidence**: settled (both sides verified verbatim from the same raw
  HTML capture) — filed as **contradiction issue #3147** per MINER.md §4a,
  since this affects which command syntax the guide would show practitioners.
- **Quote (Accessibility Testing example)**: `playwright-cli browser_navigate
  --url "https://docs.example.com"` / `playwright-cli browser_snapshot`
- **Quote (Visual Regression Testing example)**: `playwright-cli
  browser_resize --width 375 --height 812` / `playwright-cli browser_navigate
  --url "http://localhost:4321/"` / `playwright-cli browser_take_screenshot
  --filename /tmp/mobile-screenshot.png --full-page true`
- **Quote (End-to-End Testing example)**: "drive a full user journey with
  `playwright-cli browser_navigate --url "http://localhost:3000"`"
- **Our assessment**: See **Contradicts** below and issue #3147 for the full
  writeup. Do not resolve this in the guide by silently picking one syntax —
  either flag both forms as seen in the wild (with a note that the migration
  table is the more authoritative/recent-looking source), or wait for the
  contradiction to resolve before publishing a specific Playwright CLI
  command example in the guide.

## Concrete Artifacts

### Custom Playwright MCP configuration (verbatim, from the blog post)

```yaml
mcp-servers:
  playwright:
    command: npx
    args:
      - --yes
      - "@playwright/mcp@0.0.79"
      - --no-sandbox
    allowed:
      - browser_navigate
      - browser_snapshot
```
*Source: blog post, "MCP is still available, just not built-in" section*

### Custom Playwright MCP configuration (verbatim, from the reference page — adds a third allowed tool and explicit network block)

```yaml
mcp-servers:
  playwright:
    command: npx
    args:
      - --yes
      - "@playwright/mcp@0.0.79"
      - --no-sandbox
    allowed:
      - browser_navigate
      - browser_snapshot
      - browser_take_screenshot
network:
  allowed:
    - defaults
    - node
    - playwright
```
*Source: reference/playwright/, "What if you really want to use MCP?" section*

### Built-in CLI configuration and version pinning (verbatim)

```yaml
tools:
  playwright:
    mode: cli

tools:
  playwright:
    mode: cli
    version: "0.1.18"
```
*Source: reference/playwright/, "Configuration" and "Version" subsections*

### CLI command surface per the Configuration example (verbatim)

```
playwright-cli goto "https://example.com"
playwright-cli screenshot --filename /tmp/screenshot.png
playwright-cli snapshot
playwright-cli eval "() => document.title"
playwright-cli run-code "async (page) => { await page.goto('https://example.com'); return await page.title(); }"
```
*Source: reference/playwright/, "Configuration" subsection*

### Migration table (verbatim)

```
Playwright MCP tool         | Playwright CLI command
browser_navigate            | playwright-cli goto <url>
browser_snapshot            | playwright-cli snapshot
browser_take_screenshot     | playwright-cli screenshot --filename <path>
browser_click                | playwright-cli click <ref>
browser_evaluate             | playwright-cli eval "() => document.title"
```
*Source: reference/playwright/, "Migrate from Playwright MCP" section*

### Network access default and ecosystem identifier (verbatim)

```yaml
network:
  allowed:
    - defaults
    - playwright                 # enables browser downloads
    - "example.com"               # matches example.com and subdomains
    - "*.staging.example.com"     # wildcard pattern
```
*Source: reference/playwright/, "Network Access" subsection*

### Visual Regression Testing example workflow (verbatim, full frontmatter + prompt)

```yaml
---
on:
  pull_request:
    types: [opened, synchronize]
    paths:
      - 'docs/src/**/*.css'
      - 'docs/src/**/*.tsx'
      - 'docs/src/**/*.astro'
      - 'docs/astro.config.mjs'

steps:
  - uses: actions/checkout@v6
    with:
      persist-credentials: false
  - working-directory: ./docs
    run: npm ci && npm run build && npm run dev &
  - run: |
      # wait for dev server (max 30s)
      for i in $(seq 1 30); do
        curl -sf http://localhost:4321/ >/dev/null && exit 0
        sleep 1
      done
      exit 1

tools:
  playwright:
    mode: cli
    version: "0.1.18"  # pins `@playwright/cli` npm package; see Configuration > Version
  bash:
    - "npm *"
    - "curl http://localhost:*"

network:
  allowed:
    - defaults
    - playwright
    - local
    - node

permissions:
  contents: read

safe-outputs:
  add-comment:
    max: 1
  noop:
---
# Visual Regression Check
The dev server is running at http://localhost:4321/. Check for visual regressions
on the home, getting-started, and reference pages across three viewports:
- Mobile: 375×812
- Tablet: 768×1024
- Desktop: 1440×900

For each viewport, resize and screenshot:
```bash
playwright-cli browser_resize --width 375 --height 812
playwright-cli browser_navigate --url "http://localhost:4321/"
playwright-cli browser_take_screenshot --filename /tmp/mobile-screenshot.png --full-page true
```
Compare against baseline and report differences as a PR comment with screenshots.
If there are no regressions, call noop.
```
*Source: reference/playwright/, "Visual Regression Testing" subsection — note
the `browser_`-prefixed command names inside the prompt, per Claim 10 /
issue #3147*

## Cross-References

- **Corroborates**:
  - `blog-bswen-mcp-token-cost.md` Claim 1 (every MCP server loads all its
    tool definitions before you type anything): Claim 2 here is a first-party
    platform team naming the identical mechanism as the reason for removing
    a specific built-in MCP integration — independent confirmation of
    Bswen's practitioner-measured finding from the vendor side.
  - `docs-ghaw-tools-reference.md` Claim 4 (`cli-proxy:` mounts MCP servers as
    standalone CLI tools on PATH to eliminate schema-loading token cost):
    Claims 2-4 here apply the same underlying philosophy (CLI surface instead
    of MCP schema loading) to a specific built-in tool. These are
    *different* mechanisms, not the same one — `cli-proxy:` wraps an
    arbitrary configured MCP server as a CLI at the platform layer, while
    `@playwright/cli` is a standalone npm package Playwright's own vendor
    (Microsoft/Playwright team, via `@playwright/cli`) ships independent of
    gh-aw's `cli-proxy:` feature. The guide should present them as two
    instances of the same design principle (CLI > MCP schema loading for
    token cost) rather than conflate the mechanisms.
  - `docs-ghaw-mcps.md` Claim 3 (`allowed:` as a minimal-privilege,
    token-cost-reducing tool filter): the custom Playwright MCP config
    examples (Concrete Artifacts) both restrict `allowed:` to 2-3 named
    tools rather than `["*"]`, consistent with that note's recommended
    discipline.

- **Contradicts**:
  - **Filed as contradiction issue #3147** ("Playwright CLI command syntax:
    verb-only (`goto`) vs. MCP-style prefixed (`browser_navigate`)"). See
    Claim 10. The same `reference/playwright/` page's migration table and
    Configuration example use short-verb command names (`goto`, `snapshot`,
    `screenshot`, `click`, `eval`), while its own "Common Use Cases" worked
    examples (Accessibility Testing, Visual Regression Testing,
    End-to-End Testing) use `browser_`-prefixed MCP-style names as CLI
    subcommands — exactly the naming convention the migration table
    instructs readers to remove. Per MINER.md §4a, no verdict is picked
    here; see the issue for full detail. The Smith/Assayer should not cite a
    specific `playwright-cli` command example in the guide without
    resolving or flagging this ambiguity.
  - **Not filed, noted for the Assayer**: `docs-ghaw-troubleshooting-common-issues.md`
    Claims 5-6 document troubleshooting for the *Docker-based Playwright MCP*
    integration this source describes as removed from the built-in tool
    (the EOF-at-initialization error tied to Docker security flags, and the
    "Cannot find module 'playwright'" / `mcp__playwright__` usage pattern).
    This is not a contradiction — that note was accurate as of its
    2026-05-11 extraction date, describing the then-current built-in
    behavior — but the guide should date-qualify or update that content: as
    of 2026-09-01, those troubleshooting entries apply only to a workflow
    that has opted into custom `mcp-servers: playwright:` configuration, not
    to the (now CLI-only) built-in `tools.playwright:` path.

- **Extends**:
  - `docs-ghaw-tools-reference.md` Claim 10 (`playwright:` supports version
    pinning via an optional `version:` parameter): that note, extracted
    2026-05-11, documented version pinning without any `mode:` distinction.
    This source adds the `mode: cli` / `mode: mcp` split (Claim 1), confirms
    `mode: cli` is now the only built-in option, and shows the `version:`
    field now pins `@playwright/cli` specifically (example: `"0.1.18"`) —
    a different package/version namespace than the removed built-in MCP
    mode would have pinned, and different again from the *custom*
    `mcp-servers: playwright:` example's `@playwright/mcp@0.0.79`. The Ch02
    guide content citing that claim needs updating to reflect this.
  - `docs-ghaw-network-reference.md` Claim 4 (ecosystem identifiers:
    `defaults`, `github`, `local`, `dev-tools`, `containers`,
    `linux-distros`, `python`, `node`, `rust`, `go`, `java`, `deno`): this
    source's Claim 7 adds a `playwright` ecosystem identifier not present in
    that list as of the 2026-05-11 extraction — a platform addition the
    network reference note should incorporate on its next refresh.
  - `docs-ghaw-mcps.md` Claim 2 (four MCP server types: stdio, Docker, HTTP,
    registry, with Docker as the highest-isolation/highest-complexity
    option): Claim 4 here confirms the removed built-in Playwright MCP was
    specifically the Docker type, and that its removal was motivated by
    exactly the operational-complexity tradeoff (image version, args,
    lifecycle tracking) that note's isolation-hierarchy discussion predicts
    for Docker-type servers.

- **Novel**:
  - **A platform team publicly documenting the removal of a built-in MCP
    integration in favor of CLI**, with both rationales (token cost, attack
    surface) stated explicitly as the reason (Claims 1-5): no existing
    corpus source documents a *reversal* of an MCP integration decision —
    prior sources document MCP token-cost mitigations (`allowed:`,
    `cli-proxy:`) that keep MCP but reduce its cost, not a wholesale
    default-mode change away from MCP for a specific tool.
  - **`playwright-cli install --skills`** (Claim 3): a CLI tool shipping its
    own skill-installation subcommand is new to the corpus — no other source
    documents a non-MCP tool with a built-in skill-packaging mechanism.
  - **Compiler-injected policy prompts overriding tool-level default
    guidance** (Claim 8): the AWF sandbox's override of "generic Playwright
    CLI skill suggestions such as `npm install`/`npx` fallback installation"
    is a governance mechanism (prompt-injection at the compiler level to
    override a tool's own skill defaults) not documented elsewhere in the
    corpus's security-architecture notes.
  - **A `playwright` network ecosystem identifier** (Claim 7): new to the
    corpus's documented ecosystem-identifier list.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Update any existing Playwright /
  `tools.playwright:` guidance to reflect `mode: cli` as the only built-in
  option (Claim 1) and `mode: mcp` as a compile-time error. If the guide
  reproduces a `playwright-cli` command example, resolve or flag contradiction
  #3147 first (Claim 10) rather than picking a syntax silently.
- **Chapter 02 (Harness Engineering)**: Add the MCP-vs-CLI decision boundary
  named in Claim 6 as a concrete example of when to choose MCP over a
  simpler CLI/bash tool integration: MCP for open-ended, multi-turn
  exploration of unknown state (e.g. self-healing tests reasoning over page
  structure); CLI/bash for scripted, deterministic tool sequences. This is a
  generalizable pattern beyond Playwright specifically.
- **Chapter 03 (Safety and Verification)**: Add compiler-injected sandbox
  policy prompts (Claim 8) as a security mechanism distinct from network
  allowlisting and `allowed:` tool filtering — it operates by overriding a
  tool's own default instructions (e.g., blocking "install browsers at
  runtime" suggestions) rather than by blocking an action at the
  network/protocol layer.
- **Chapter 04 (Context Engineering / Tool Choice)**: Cite Claims 2-3
  alongside `blog-bswen-mcp-token-cost.md` and `docs-ghaw-tools-reference.md`
  Claim 4 as a third, independently-arrived-at data point for "CLI/bash tool
  access is cheaper per-turn than MCP schema loading" — now with a concrete
  platform team decision (not just a practitioner measurement or a general
  platform feature) as evidence.

## Extraction Notes

1. **WebFetch output not trusted for quotes; raw HTML fetched and parsed
   instead.** An initial WebFetch pass on the blog post returned a clean but
   restructured summary (different section framing than the source). Per
   MINER.md §2a, both the blog post and the linked `reference/playwright/`
   page were fetched directly via `curl` with a browser user-agent, and the
   markdown content region (`div.sl-markdown-content`) was parsed from the
   raw HTML. Code examples specifically were extracted from the
   Starlight/expressive-code `<div class="ec-line">` line structure (not a
   naive tag-strip) after an initial crude regex pass concatenated adjacent
   lines without newlines and risked misrepresenting multi-line code
   examples — this was caught and corrected before extracting Claim 10 and
   the Concrete Artifacts code blocks, which is also how the Claim
   10/issue #3147 contradiction was verified as real rather than a parsing
   artifact.
2. **One linked page followed per MINER.md §1.** The blog post explicitly
   points to `reference/playwright/` ("the Playwright reference for the full
   migration table") as its companion page; it was fetched in full. No other
   substantive links were present in the blog post's body beyond navigation
   chrome.
3. **Contradiction filed before this PR, per MINER.md §4a.** Issue #3147 was
   opened for the Claim 10 self-contradiction (migration table vs. Common Use
   Cases examples) prior to writing this note. No verdict is asserted here;
   see Cross-References → Contradicts.
4. **No date on the reference page.** Unlike the blog post (dated
   2026-09-01), the `reference/playwright/` page carries no publication date
   in its rendered content. Given the blog post's explicit same-day link to
   it as "the" migration reference, it is treated as reflecting the same
   2026-09-01 platform state.
