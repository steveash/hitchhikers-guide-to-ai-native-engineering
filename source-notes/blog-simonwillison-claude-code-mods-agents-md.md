---
source_url: https://simonwillison.net/2026/Sep/18/thariq-shihipar/
source_type: blog-post
title: "A quote from Thariq Shihipar"
author: Simon Willison (quoting Thariq Shihipar, Anthropic)
date_published: 2026-09-18
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: emerging
issue: "#3687"
---

# A quote from Thariq Shihipar

> Simon Willison's one-quote post announcing Claude Code v2.1.277's AGENTS.md support is
> thin on its own, but it links directly to the source of the underlying "mods" plugin —
> Claude Code's new built-in harness-customization mechanism — and that primary source
> (`mods/README.md` and `mods/agents-md/README.md` in the `anthropics/claude-code` repo)
> is a detailed, verbatim specification of four built-in mods, the `register(on, options)`
> hook contract, a dedicated mod-testing framework, and the exact semantics of AGENTS.md's
> four configurable loading modes.

## Source Context

- **Type**: blog-post (a one-quote "quotation" post on Simon Willison's Weblog, a
  `trusted-feed` source) linking to primary-source documentation on GitHub
- **Author credibility**: The quote itself is from Thariq Shihipar, an Anthropic engineer
  working on Claude Code (posted to Twitter/X as @trq212), reproduced verbatim by Simon
  Willison. Willison adds no independent commentary beyond the quotation and tags — this is
  a pure "worth reading" pointer post, not analysis. The real evidentiary weight in this
  note comes from the two linked GitHub pages the quote points to
  (`github.com/anthropics/claude-code/tree/main/mods/agents-md` and
  `github.com/anthropics/claude-code/tree/main/mods`), which are the shipped source and
  documentation for the feature, fetched directly and reproduced verbatim below.
- **Scope**: Covers (1) the Twitter announcement that Claude Code 2.1.277 adds AGENTS.md as
  a CLAUDE.md fallback, (2) the "mods" plugin architecture that AGENTS.md support is built
  on, including all four built-in mods (`sec-default`, `diff`, `telemetry`, `agents-md`),
  (3) the `agents-md` mod's four configuration modes and their exact loading semantics, (4)
  the mod testing/typing framework. Does NOT cover: the `diff`, `sec-default`, or
  `telemetry` mods' own source code in detail (only their one-line descriptions from
  `mods/README.md` were extracted — their individual `hooks/` implementations were not
  fetched), any Anthropic first-party blog post or documentation page formally announcing
  mods (none was linked from this source), or user reaction/adoption data (the post is 7
  days old at extraction time).

## Extracted Claims

### Claim 1: Claude Code 2.1.277 added automatic AGENTS.md support as a fallback used only when a folder has no CLAUDE.md

- **Evidence**: Direct quote from Thariq Shihipar (Anthropic), reproduced verbatim in
  Willison's post from the linked tweet.
- **Confidence**: settled (primary-source engineer statement, corroborated by the linked
  `mods/agents-md/README.md` documentation, which describes the identical default
  behavior — see Claim 5)
- **Quote**: "We're adding support for AGENTS.md to Claude Code. Starting today in version
  2.1.277, if there is no CLAUDE.md in a folder, Claude will check for and use AGENTS.md."
- **Our assessment**: This establishes the headline fact and the version number
  (2.1.277) as a corpus first — no existing note pins this specific version to AGENTS.md
  support. The framing "if there is no CLAUDE.md in a folder" is imprecise on its own (the
  primary source in Claim 5 clarifies this is evaluated at the whole-project level, not
  per-folder, and only for the project's "own" files) — the tweet is a marketing-length
  summary; the mod README is the precise specification.

### Claim 2: AGENTS.md support ships as a "mod" — a new, not-yet-fully-released mechanism for customizing the Claude Code harness

- **Evidence**: Direct quote from Thariq Shihipar; corroborated by `mods/README.md`, which
  documents four built-in mods and describes the mechanism as "early access."
- **Confidence**: emerging (the feature is explicitly self-described as early access and
  subject to change without notice — see Claim 9)
- **Quote**: "AGENTS.md support is built off of Claude Code mods, our upcoming way to
  customize the Claude Code harness. This is a built-in mod, but you'll be able to build
  custom versions of project instructions yourself as you'd like too."
- **Our assessment**: This is the most novel claim in the source for our corpus: "mods" is
  a previously undocumented layer in the Claude Code harness-configuration taxonomy. The
  existing seven-extension-point taxonomy in `blog-anthropic-large-codebase-best-practices.md`
  Claim 5 (CLAUDE.md, hooks, skills, plugins, MCP servers, LSP integrations, subagents) has
  no "mods" entry — this source suggests mods are architecturally a specific kind of plugin
  (see Claim 3), not an eighth independent surface, so the taxonomy should be refined rather
  than simply extended by one.

### Claim 3: A mod is technically a Claude Code plugin whose behavior lives entirely in one hooks module — a single `register(on, options)` entry that hooks engine events as `($, e, next)` functions

- **Evidence**: Verbatim architectural definition from `mods/README.md`, the primary
  source the tweet links to.
- **Confidence**: settled (primary source code documentation, directly fetched)
- **Quote**: "A mod is a Claude Code plugin whose behaviour lives in a hooks module: one
  `register(on, options)` entry that hooks the engine's events as functions `($, e, next)`.
  These four ship inside Claude Code; this folder is their source, published as it is built
  into the binary."
- **Our assessment**: This is the precise technical relationship the tweet glosses over:
  mods are not a new plugin *type* distinct from Claude Code's existing plugin system
  (`blog-anthropic-large-codebase-best-practices.md` Claim 11: plugins bundle skills,
  hooks, and MCP configs) — a mod is specifically a plugin built entirely around the hooks
  mechanism, with no skill or MCP bundling of its own. This refines rather than
  contradicts the existing plugin taxonomy: mods are a narrower, hooks-only subset of what
  a plugin can be, used here for four capabilities Anthropic ships as part of the binary
  itself rather than as marketplace-installed plugins.

### Claim 4: Four mods ship built into Claude Code — `sec-default` (keeps org-managed policy out of reach of installed plugins), `diff` (a `/diff` pane of uncommitted changes), `telemetry` (first-party analytics event logging), and `agents-md` (AGENTS.md as project instructions)

- **Evidence**: Verbatim summary table from `mods/README.md`.
- **Confidence**: settled (primary source documentation table, directly fetched)
- **Quote**: "| [`sec-default`](sec-default) | Keeps an organization's classic hooks, prompt
  content, managed settings and tool policy out of reach of the plugins a person installs;
  adds no policy of its own. | Outermost, on a machine with managed settings or for a Team
  or Enterprise organization, unless managed `prependPlugins` says otherwise | | [`diff`](diff)
  | `/diff`: the session's uncommitted changes in a pane beside the transcript... | Built in
  |"
  (table continues with `telemetry` and `agents-md` rows, reproduced in full in Concrete
  Artifacts below)
- **Our assessment**: `sec-default` is a new corpus data point for enterprise governance:
  it is a mod, not a settings flag, whose specific job is to shield org-managed hooks,
  prompt content, settings and tool policy from plugins a user installs — and it loads
  "outermost" on managed machines or Team/Enterprise orgs by default. This is a concrete
  mechanism for the "org policy should not be overridable by an individual's plugin
  choices" governance requirement that prior corpus sources discuss only in the abstract
  (e.g. `blog-anthropic-agent-identity-access-model.md`). It deserves a mention wherever
  the guide covers enterprise/Team hardening of Claude Code, independent of the AGENTS.md
  material.

### Claim 5: The `agents-md` mod's default mode (`claude-md-or-agents-md`) loads AGENTS.md files project-wide only when the project has no CLAUDE.md, `.claude/CLAUDE.md`, or `CLAUDE.local.md` of its own anywhere from the root down to the working directory — the organization's managed file and the user's personal `~/.claude/CLAUDE.md` do not count against this check

- **Evidence**: Verbatim specification from `mods/agents-md/README.md`.
- **Confidence**: settled (primary source documentation, directly fetched)
- **Quote**: "`claude-md-or-agents-md` (the default): a project with no instruction files of
  its own gets its `AGENTS.md` files instead, loaded exactly where and how `CLAUDE.md`
  would be. \"Of its own\" is read off what the engine loaded for the context: a
  `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` in any directory from the root down
  to the working directory leaves the whole project to the engine, and the plugin stays out
  (the organization's managed file, the person's `~/.claude/CLAUDE.md`, a `.claude/rules`
  file and an added directory's `CLAUDE.md` do not count, as the nested walk does not see
  them either)."
- **Our assessment**: This is the precise mechanic behind Claim 1's simplified tweet
  summary, and it matters practically: a team with only an org-managed CLAUDE.md (no
  project-level file) will still get AGENTS.md loaded under the default mode, because the
  managed file doesn't count as a project file "of its own." Teams migrating from CLAUDE.md
  to AGENTS.md, or adopting AGENTS.md as the cross-tool standard documented in
  `docs-github-copilot-code-review-agents-md-ui.md` and `blog-simonwillison-sqlite-agents-md.md`,
  need to know this fallback is all-or-nothing at the project level, not evaluated
  independently per subfolder.

### Claim 6: AGENTS.md files the mod loads are rendered by the engine identically to CLAUDE.md — same context placement, same announcement, same omission rules for agents that skip project instructions (e.g. Explore, Plan, or a custom agent with `omitClaudeMd`)

- **Evidence**: Verbatim specification from `mods/agents-md/README.md`.
- **Confidence**: settled (primary source documentation, directly fetched)
- **Quote**: "The engine then renders `claudeMd` from the answered files with its own
  preamble and framing, announces them by name, and keeps only the `managed` ones for an
  agent that omits project instructions (Explore, Plan, a custom agent with
  `omitClaudeMd`). So an `AGENTS.md` this plugin adds as a `project` file is, to everything
  downstream, a project instruction file: same place in the context, same framing, same
  omission rules, same announcement."
- **Our assessment**: This is a strong compatibility guarantee — AGENTS.md is not a
  second-class citizen once loaded; it is indistinguishable from CLAUDE.md to every
  downstream consumer, including subagents that are configured to omit project
  instructions entirely (they still keep only the managed-tier files, whether those came
  from CLAUDE.md or AGENTS.md). This directly informs guide advice on Explore/Plan-style
  read-only subagents: the `omitClaudeMd` behavior applies uniformly regardless of which
  file format a team has adopted.

### Claim 7: Nested AGENTS.md files attach automatically when Claude reads a file with the `Read` tool under a subdirectory — but this differs from nested CLAUDE.md attachment in at least eight documented ways, including that it fires only on `Read`, not on `@`-mentions, IDE file selection, or notebook/image/PDF results

- **Evidence**: Verbatim "Where it still differs from CLAUDE.md" section of
  `mods/agents-md/README.md`, an explicit, numbered list of eight gaps between the plugin's
  event-driven implementation and the engine's native CLAUDE.md nested-file handling.
- **Confidence**: settled (primary source documentation, directly fetched; the source
  itself frames these as acknowledged current limitations, not aspirational)
- **Quote**: "Nested files attach on a text `Read` only. The engine also attaches a
  directory's `CLAUDE.md` for a file `@`-mentioned in the prompt, for the IDE's opened file
  or selection, and for the `Read` tool's notebook, image and PDF results." ... "A nested
  file the plugin attaches is not registered in the loop's read-file state, so after a
  compaction the engine does not restore it among the recently read files" ... "A subagent
  that is not a fork gets a nested `AGENTS.md` at its own first `Read` under that directory
  even when its parent's loop was already given it; the engine does not hand such a
  subagent the nested `CLAUDE.md` again. A fork matches the engine on both sides."
- **Our assessment**: This is the single most actionable claim in the source for teams
  currently relying on CLAUDE.md's nested-file behavior and considering a switch to
  AGENTS.md. It is a genuine, currently-shipping functional gap (not just a documentation
  nuance): `@`-mentions, IDE selections, and notebook/image/PDF reads will silently miss
  nested AGENTS.md context that nested CLAUDE.md would have picked up; compaction will
  cause nested AGENTS.md files to be re-fetched rather than restored from state; and
  non-fork subagents will re-attach nested AGENTS.md redundantly where CLAUDE.md would not.
  Teams should treat AGENTS.md's nested-directory support as a strict subset of CLAUDE.md's
  until the plugin's event coverage is extended.

### Claim 8: Mods are composed and typed through "noun contracts" — a mod that adds a capability to the shared `$` object (e.g. `$.telemetry`) owns that capability's only TypeScript declaration, and other mods import that declaration by path rather than duplicating it

- **Evidence**: Verbatim "Composing mods: noun contracts" section of `mods/README.md`,
  including the concrete example of `telemetry/types/index.d.ts` declaring `$.telemetry`
  and `diff` importing and type-checking against it.
- **Confidence**: settled (primary source documentation, directly fetched)
- **Quote**: "The contract is the only declaration of the noun. The mod's own hooks import
  its types from the folder (`import type { Telemetry } from '../types'`), and the value
  its `engine.create` hook returns is checked against `EngineInterface['telemetry']`, so
  the implementation cannot drift from what callers read." ... "`mods/tsconfig.json`
  includes `*/types/**/*.d.ts`, so `$.telemetry.log(…)` in `diff` types against
  `telemetry`'s contract as it stands."
- **Our assessment**: This is an internal engineering-architecture detail (how Anthropic
  prevents type drift between first-party mods) rather than a practitioner-facing feature,
  but it is evidence of engineering discipline behind the harness extension mechanism: a
  single-source-of-truth contract per capability, checked at compile time via
  `tsc -p mods/tsconfig.json`, with an explicit test harness (`claude plugin test`) that
  mocks the engine's `$` object per-event. Lower priority for the guide than Claims 1, 5,
  and 7, but useful context for any future guide section on building custom hooks-based
  plugins, since the README states third-party plugins can follow the same noun-contract
  pattern by pointing their own `tsconfig` at a mod's `types/` folder.

### Claim 9: Mods are explicitly labeled early access — function hooks must be enabled for them to load, the underlying API may change release to release without notice, and mods are not listed in the plugin marketplace

- **Evidence**: Verbatim closing caveat in `mods/README.md`.
- **Confidence**: settled as a direct quote of Anthropic's own stability disclaimer;
  emerging as a signal for how much weight practitioners should put on the specifics of
  the mod API documented in this note
- **Quote**: "Early access: hooks modules load only where function hooks are enabled, and
  the API these mods are written against may change between releases without notice. They
  are not listed in this repository's marketplace; the copies that matter are the ones
  already in your Claude Code."
- **Our assessment**: This is a load-bearing caveat for the guide: the detailed mechanics
  in Claims 3, 5, 6, 7, and 8 describe a specific, dated snapshot (as of the commit fetched
  2026-09-25, five business days after the September 18 announcement) of an API Anthropic
  has explicitly reserved the right to change without notice. The guide should present the
  AGENTS.md *behavior* (fallback semantics, rendering parity, nested-file gaps) as the
  stable practitioner-facing contract, and flag the underlying mods *plugin API* itself
  (the `register(on, options)` signature, noun contracts, `claude --plugin-dir` /
  `claude plugin test` commands) as subject to change.

### Claim 10: The `agents-md` mod's option key was renamed from `projectInstructions` (with values `claude`, `agents-fallback`, `both`, `none`) to `instructionFiles` (with values `claude-md`, `claude-md-or-agents-md`, `claude-md-and-agents-md`, `managed-only`), with the old key still honored and a one-time transcript notice guiding migration

- **Evidence**: Verbatim migration-compatibility paragraph from `mods/agents-md/README.md`.
- **Confidence**: settled (primary source documentation, directly fetched)
- **Quote**: "The option was first keyed `projectInstructions`, with the values `claude`,
  `agents-fallback`, `both` and `none`. A value still stored under that key is honoured for
  now while `instructionFiles` reads as its default... the first `session.start` of a load
  says in the transcript how it was read. Once `instructionFiles` is set to anything but its
  default, the old key is not read and the transcript says to remove it."
- **Our assessment**: This confirms the feature existed under an earlier internal option
  name before the September 18 public announcement — the renaming and backward-compatible
  migration path is itself evidence that `agents-md` had already shipped (at least as an
  internal or gated option) prior to the tweet, and the tweet marks its public/default
  rollout rather than its first implementation. Practically minor for the guide, but useful
  for dating: anyone who configured `projectInstructions` before this note's extraction
  date should check their transcript for the migration notice and update to
  `instructionFiles`.

## Concrete Artifacts

### Tweet (verbatim, via Simon Willison's blockquote reproduction)

```
Source: https://simonwillison.net/2026/Sep/18/thariq-shihipar/
Attributed to: Thariq Shihipar (@trq212), 18 September 2026

We're adding support for AGENTS.md to Claude Code.

Starting today in version 2.1.277, if there is no CLAUDE.md in a folder, Claude
will check for and use AGENTS.md.

AGENTS.md support is built off of Claude Code mods, our upcoming way to
customize the Claude Code harness.

This is a built-in mod, but you'll be able to build custom versions of project
instructions yourself as you'd like too.

You can see [the source for the mod here] (linked to
github.com/anthropics/claude-code/tree/main/mods/agents-md)!

— cited context: "there are [more mods here]" (linked to
github.com/anthropics/claude-code/tree/main/mods)
```

### Full built-in mods table (verbatim)

```
Source: https://raw.githubusercontent.com/anthropics/claude-code/main/mods/README.md
(fetched 2026-09-25)

| Mod | What it does | Seated |
| --- | --- | --- |
| `sec-default` | Keeps an organization's classic hooks, prompt content, managed
  settings and tool policy out of reach of the plugins a person installs; adds
  no policy of its own. | Outermost, on a machine with managed settings or for
  a Team or Enterprise organization, unless managed `prependPlugins` says
  otherwise |
| `diff` | `/diff`: the session's uncommitted changes in a pane beside the
  transcript, file by file with their hunks, refreshed as Claude edits files
  and runs commands. | Built in |
| `telemetry` | Hooks `$.telemetry`'s two events (`log`, `mark`), adding the
  noun in the `engine.create` fold where the engine has none, so a built-in
  plugin can record an event as a first-party analytics row, sent in batches;
  refuses installed plugins; sends nothing wherever Claude Code's analytics
  are off. | Built in |
| `agents-md` | `AGENTS.md` as project instructions, by one option: loaded
  where the project has no `CLAUDE.md` of its own (`claude-md-or-agents-md`,
  the default) or beside it (`claude-md-and-agents-md`), placed and framed
  exactly as the engine places `CLAUDE.md`, nested ones on a `Read`; or the
  project's and the person's instruction files dropped and the organization's
  kept (`managed-only`); or `CLAUDE.md` alone, as the engine reads it
  (`claude-md`). | Built in |
```

### agents-md mod: hook table (verbatim, from `mods/agents-md/README.md` "What it hooks")

```
Source: https://raw.githubusercontent.com/anthropics/claude-code/main/mods/agents-md/README.md
(fetched 2026-09-25)

| event | what the hook does |
| --- | --- |
| `session.start` | in every mode: passes the start straight through and
  floats the usage row for the configured mode, never awaited; the first
  start of a load logs how a stored `projectInstructions` value is read. |
| `prompt.context` | under `claude-md-or-agents-md` and
  `claude-md-and-agents-md`: walks `$.fs.ancestors` for the `AGENTS.md` files
  above the working directory and answers them as `project` instruction
  files... under `claude-md-or-agents-md` it answers nothing when the project
  has a `CLAUDE.md` of its own... under `managed-only` (matcher: a `project`,
  `local` or `user` file present): answers the list without those kinds |
| `agent.spawn` on `fork: true` | ...a fork the Agent tool starts shares its
  parent's prompt prefix, so the parent loop's delivered nested files are
  copied to the fork's loop and not attached to it again |
| `tool.call` on `Read` | ...walks only the directories strictly between the
  root and the read file... and attaches their `AGENTS.md` files not yet
  given to that agent loop... framed `Contents of <path>:` byte for byte as
  the engine frames a nested `CLAUDE.md` |
```

### Setting the option by hand (verbatim JSON example)

```json
Source: https://raw.githubusercontent.com/anthropics/claude-code/main/mods/agents-md/README.md
(fetched 2026-09-25) — placed in ~/.claude/settings.json, --settings, or managed settings

{
  "pluginConfigs": {
    "agents-md@builtin": {
      "options": { "instructionFiles": "claude-md-and-agents-md" }
    }
  }
}
```

### Mod test-file example (verbatim, from `mods/README.md` "Testing")

```ts
Source: https://raw.githubusercontent.com/anthropics/claude-code/main/mods/README.md
(fetched 2026-09-25)

import { describe, expect, mock, test, tier } from 'claude-code/testing'

tier('builtin')

describe('register', () => {
  test('outside a git repository /diff says so, opens nothing', async ($, on) => {
    const opened: string[] = []
    mock.clock(on)
    on('session.start', ($, e) => ({ cwd: e.cwd }))
    on('command.register', ($, e) => ({ value: { command: e.name } }))
    on('process.run', () => ({
      value: { exitCode: 128, stdout: '', stderr: 'fatal: not a git repository' },
    }))
    on('ui.open', ($, e, next) => {
      opened.push(e.id)
      return next(e)
    })

    await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })
    const { text } = await $.command.run({
      command: 'diff',
      args: '',
      origin: { kind: 'composer' },
    })

    expect(text).toContain("isn't in a git repository")
    expect(opened).toEqual([])
  })
})
```

### agents-md telemetry event schema (verbatim, from `mods/agents-md/README.md` "What it logs")

```
Source: https://raw.githubusercontent.com/anthropics/claude-code/main/mods/agents-md/README.md
(fetched 2026-09-25)

| event | when | properties |
| --- | --- | --- |
| `agents_md_mode` | once per fresh load, at `session.start` | `mode`
  (`claude-md` \| `claude-md-or-agents-md` \| `claude-md-and-agents-md` \|
  `managed-only`), `is_interactive` |
| `agents_md_load` | the first context of a load, under
  `claude-md-or-agents-md` and `claude-md-and-agents-md` | `mode`,
  `file_count` (`AGENTS.md` files handed to the engine), `import_count`
  (their `@` imports), `total_content_length`, `yielded`
  (`claude-md-or-agents-md` stood down for a `CLAUDE.md` of the project's
  own), `walk_failed` |
| `agents_md_nested` | a Read that attached nested files | `mode`,
  `file_count` |

"Counts and closed choices only; no path and no file text."
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-code-review-agents-md-ui.md` Claim 1–2: that note documents
    GitHub Copilot code review reading AGENTS.md automatically as of June 18, 2026,
    establishing AGENTS.md as a cross-agent standard. This source adds the Claude Code
    side of that same cross-agent convergence, three months later, with the added detail
    that Claude Code's adoption is fallback-only by default (`claude-md-or-agents-md`),
    not "read alongside CLAUDE.md" as the default — a nuance the Copilot changelog does
    not need to address since Copilot's AGENTS.md support has no CLAUDE.md-precedence
    question of its own.
  - `blog-simonwillison-sqlite-agents-md.md` Claim 6 and Claim 10: that note documents
    AGENTS.md's dual purpose (governance + technical context) and frames 2026 as the year
    AGENTS.md became a cross-tool convention practitioners must discover. Claude Code's
    own first-party adoption of the format (this source) is the strongest evidence yet for
    that claim — the vendor that originated CLAUDE.md is now natively supporting the
    competing/complementary community standard.
  - `blog-anthropic-large-codebase-best-practices.md` Claim 11 (plugins bundle skills,
    hooks, and MCP configs into an installable package): this source's Claim 3 (a mod is a
    plugin whose behavior lives entirely in a hooks module) is consistent with, and
    narrows, that general plugin description — a mod is the hooks-only special case,
    without skill or MCP bundling, used for behavior Anthropic ships in the binary itself.
  - `docs-github-copilot-agent-plugins-1-0.md` (Agent Plugins 1.0, a cross-vendor
    plugin/skill/MCP packaging standard co-published by GitHub, AWS, Anysphere, Microsoft,
    OpenAI, Vercel, and Google): both sources document 2026 as a year of increasing
    plugin/extension-mechanism standardization and formalization across coding-agent
    vendors, though the two mechanisms are architecturally distinct (Agent Plugins 1.0
    packages skills + MCP servers; Claude Code mods are hooks-module plugins with no
    skill/MCP bundling of their own, per this source's Claim 3) and not documented as
    interoperable.

- **Contradicts**: None found. No existing corpus source makes claims about Claude Code's
  AGENTS.md support, mods architecture, or nested-file attachment behavior that this
  source's primary-source material conflicts with. No contradiction issue filed.

- **Extends**:
  - `blog-anthropic-large-codebase-best-practices.md` Claim 5 (the seven-extension-point
    harness taxonomy: CLAUDE.md, hooks, skills, plugins, MCP servers, LSP integrations,
    subagents): this source suggests "mods" should be documented as a specific
    architectural pattern *within* the existing "plugins" extension point (a
    hooks-only plugin used for built-in, binary-shipped capabilities), rather than as an
    eighth independent extension point. The guide's taxonomy figure should note this
    distinction when it is next updated.
  - `blog-anthropic-large-codebase-best-practices.md` Claim 6 (CLAUDE.md files should be
    lean and layered, loaded additively root-to-subdirectory): this source's Claim 7
    documents that AGENTS.md's nested-directory loading, while modeled on the same
    additive pattern, currently has narrower event coverage (Read-tool only) than native
    CLAUDE.md nested loading. Guide advice on lean/layered context files should note this
    gap specifically for teams using AGENTS.md instead of CLAUDE.md in Claude Code.

- **Novel**:
  - **"Mods" as a documented Claude Code harness-customization mechanism**: no prior
    corpus source names or describes mods, the `register(on, options)` hook contract, or
    the four built-in mods (`sec-default`, `diff`, `telemetry`, `agents-md`).
  - **`sec-default` as a concrete mechanism for org-policy isolation from user-installed
    plugins**: no prior corpus source documents a specific mechanism (as opposed to a
    general governance principle) for preventing a Claude Code user's own plugin
    installations from overriding organization-managed hooks, prompt content, or tool
    policy.
  - **The eight documented gaps between nested AGENTS.md and nested CLAUDE.md attachment
    behavior**: this is the first corpus source to enumerate specific, current functional
    differences between the two file formats' nested-directory loading, rather than
    treating them as equivalent.
  - **A first-party mod-testing framework** (`claude plugin test`, the `$`/`on` mock
    harness, `tier('builtin')`): no prior corpus source documents how Anthropic internally
    tests harness-extension code.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: When next revising the harness-extension-point
  taxonomy (currently sourced from `blog-anthropic-large-codebase-best-practices.md` Claim
  5), add a note that "plugins" includes a hooks-only subtype Anthropic calls "mods," used
  for capabilities shipped inside the Claude Code binary itself (AGENTS.md support, the
  `/diff` pane, first-party telemetry, and `sec-default` policy isolation) rather than
  marketplace-installed plugins. Cite this source's Claims 2–4.
- **Chapter 02 (Harness Engineering) — AGENTS.md adoption**: Add the precise default
  fallback rule (Claim 5: AGENTS.md loads project-wide only when no CLAUDE.md exists
  anywhere from root to working directory, and the org-managed/personal files don't count
  against that check) as the authoritative mechanic for any guide section discussing
  CLAUDE.md-vs-AGENTS.md choice in Claude Code specifically. Add Claim 7 (the eight
  nested-file attachment gaps) as an explicit caveat: teams relying on nested-directory
  CLAUDE.md context should not assume AGENTS.md is a drop-in replacement yet, particularly
  for `@`-mention, IDE-selection, and non-text `Read` results, and for non-fork subagents.
- **Chapter 02 (Harness Engineering) — enterprise governance**: Add `sec-default` (Claim 4)
  as a concrete named mechanism when the guide discusses preventing user-installed plugins
  from overriding organization policy on managed machines or in Team/Enterprise orgs.
- **Chapter 04 (Agents/Context Engineering)**: Add Claim 6 (AGENTS.md renders identically to
  CLAUDE.md downstream, including the `omitClaudeMd` omission rule for Explore/Plan-style
  subagents) to any discussion of subagent context configuration — the file-format choice
  (CLAUDE.md vs AGENTS.md) does not change subagent-level context-omission behavior.
- **All chapters citing AGENTS.md mechanics from this source**: Flag per Claim 9 that the
  underlying mods API is explicitly early access and may change without notice; the
  AGENTS.md *behavioral contract* (fallback semantics, rendering parity) should be treated
  as more durable than the *mods plugin API* details (hook names, noun-contract mechanics,
  CLI commands) used to implement it.

## Extraction Notes

- Willison's post itself is exactly as thin as the Prospector's second and third triage
  comments characterized it (one quote, no independent analysis) — but per MINER.md §1,
  "If it links to related pages ... that seem substantive ... follow up to 5 linked pages."
  The two GitHub links in the quote (`mods/agents-md` and `mods`) were followed via the
  GitHub API and `raw.githubusercontent.com`, and both proved highly substantive —
  `mods/README.md` (6,458 bytes) and `mods/agents-md/README.md` (12,274 bytes) together
  contain the great majority of the material in this note. The Prospector's third triage
  comment ("high novelty... first documentation of 'Claude Code mods'") anticipated this;
  the first and second triage comments, which rated the source thin/low-novelty, appear to
  have evaluated only Willison's page and not followed the linked primary source. This note
  follows the third (most thorough) triage assessment.
- All quotes from `simonwillison.net` were taken from the page's raw HTML
  (`<blockquote>` element), fetched directly via `curl`, not from a WebFetch model
  summarization pass — no verbatim-recovery caveat applies to the tweet quote.
- All quotes from `mods/README.md` and `mods/agents-md/README.md` were taken from
  `raw.githubusercontent.com` verbatim Markdown source, not rendered/summarized HTML.
- Did not fetch or extract the individual `hooks/` TypeScript source files for `diff`,
  `sec-default`, `telemetry`, or `agents-md` (only their `README.md` and the `mods/README.md`
  top-level summary table) — those would be a natural follow-up mining target if the guide
  later wants concrete hook-registration code examples beyond the one test-file example
  reproduced in Concrete Artifacts.
- Three separate Prospector triage comments are present on issue #3687, apparently from
  repeated triage runs, with escalating novelty assessments (medium-high → low → high).
  This note is written to satisfy the most demanding (third) assessment's key question
  ("What is the scope of Claude Code mods as a customization framework, and how do they
  interact with CLAUDE.md/AGENTS.md configuration?").
- No contradiction with existing source notes was found; none filed per MINER.md §4a.
