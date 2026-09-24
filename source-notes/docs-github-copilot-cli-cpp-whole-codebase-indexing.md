---
source_url: https://github.blog/changelog/2026-09-22-faster-c-code-intelligence-with-whole-codebase-indexing
source_type: docs
title: "Faster C++ code intelligence with whole codebase indexing"
author: GitHub (official changelog); Microsoft (cpp-language-server documentation)
date_published: 2026-09-22
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: emerging
issue: "#3654"
---

# Faster C++ Code Intelligence with Whole Codebase Indexing

> GitHub's September 22, 2026 changelog announces whole codebase indexing (WCI), a
> persistent symbol index for the (preview-status) Microsoft C++ Language Server, which
> brings Visual Studio/VS Code-grade C++ code intelligence to **GitHub Copilot CLI** —
> not an IDE — as an installable plugin that requires a `compile_commands.json`
> compilation database and ships its own Copilot CLI skill to generate one.

## Source Context

- **Type**: docs (GitHub official product changelog, `github.blog/changelog`, published
  September 22, 2026; a very short "1 minute read" release note, tagged `copilot`). Five
  linked pages from the `microsoft/cpp-language-server` GitHub repository were followed
  as substantive sub-pages per MINER.md §1, since the changelog itself is only six short
  paragraphs and defers essentially all mechanism, configuration, and prerequisite detail
  to that repository's documentation: the repository `README.md` (quick start, product
  framing, prerequisites), `docs/indexing.md` (the page the changelog explicitly links
  for disabling WCI), `docs/configuration.md` (the three-file configuration model),
  `docs/compile-commands.md` (the `compile_commands.json` prerequisite and the
  auto-generation skill), and `docs/lsp-features.md` (the supported-capability matrix).
  All six pages (changelog + five) were fetched via `curl` with a browser user-agent and
  read as plain text/raw Markdown, not through a summarizing fetch tool, so every `Quote`
  field below is copied character-for-character from the source.
- **Author credibility**: First-party GitHub product changelog plus first-party Microsoft
  documentation for the language server it announces. Authoritative for feature existence,
  default-on/off status, exact configuration file names and JSON keys, and the documented
  LSP capability matrix. Not a source for adoption data, independent benchmarking of the
  indexing performance claims ("less time waiting for definitions, references,
  implementations"), or any comparison against competing C++ code-intelligence tooling —
  no metrics, customer quotes, or before/after timing numbers appear anywhere in the six
  pages read.
- **Scope**: Covers WCI specifically (what it is, default status, how to disable it, its
  performance-tradeoff framing) plus enough of the surrounding `cpp-language-server`
  project documentation to explain the feature's prerequisites (a `compile_commands.json`
  file), configuration surface (three config files, automatic-discovery mode, exclude
  patterns), and functional scope (which LSP operations are and are not supported). Does
  **not** cover: MSBuild/vcxproj support (explicitly stated as "planned for a future
  release," with a third-party sample tool offered as a stopgap), adoption or performance
  metrics, the language server's relationship to the separate GitHub Copilot
  "modernization agent" for MSVC toolset upgrades (a different, Visual-Studio-side C++
  feature — see Cross-References), or any detail about the two other documentation pages
  linked from the README that were not fetched (`installation.md`,
  `command-line-options.md`, `authentication.md`, `troubleshooting.md` — judged
  non-substantive for this note's WCI-focused scope beyond the five pages already read).

## Extracted Claims

### Claim 1: Whole codebase indexing (WCI) creates a persistent symbol index across an entire C++ project — including files not currently open — so that code-intelligence requests reuse resolved symbol information instead of rediscovering it on every request

- **Evidence**: The changelog's core problem/solution framing, stated in two consecutive
  paragraphs (the problem WCI solves, then WCI's mechanism).
- **Confidence**: settled (first-party feature description, internally consistent between
  the changelog and the `indexing.md` companion doc's "WCI is the language server's
  semantic symbol index" framing)
- **Quote**: "C++ repositories can contain millions of lines of code across deeply
  connected source files and headers. Without a reusable index, code-intelligence
  requests may need to rediscover project information as you navigate, making it slower
  to find a definition, locate references, or understand unfamiliar code. Whole codebase
  indexing (WCI) creates a persistent index of symbols across your C++ project, including
  files that aren't currently open. The Microsoft C++ Language Server uses your project's
  compilation information to resolve types, symbols, includes, and relationships between
  files. WCI makes that symbol information available for reuse instead of rediscovering
  it for each request."
- **Our assessment**: The "including files that aren't currently open" detail is the
  substantive claim — a per-request, on-demand resolution model (parse only what's
  touched by the current request) would not need to track symbols in unopened files at
  all. A persistent, whole-project index is architecturally the same idea as an IDE's
  background symbol database (ctags/clangd-style), now applied to a CLI-based coding
  agent's tool calls rather than an editor's live UI. No independent timing numbers are
  given for how much faster indexed vs. non-indexed requests are — the claim is
  qualitative ("less time waiting").

### Claim 2: WCI is enabled by default; the language server builds the index on first opening a C++ project, indexing progress can be checked at any time with `/lsp logs`, and the disable path requires restarting the Copilot session

- **Evidence**: The changelog's "Configure indexing" section, stated as a single
  connected passage.
- **Confidence**: settled (first-party product-behavior statement)
- **Quote**: "Whole codebase indexing is enabled by default because its persistent symbol
  index helps the Microsoft C++ Language Server efficiently understand relationships
  across your entire project. The language server loads the index when you first open a
  C++ project. You can check indexing progress at any time with /lsp logs." / "Restart
  your Copilot session after changing the setting."
- **Our assessment**: `/lsp logs` as a named, in-session diagnostic command implies
  Copilot CLI has a general `/lsp` command surface for managing language servers (also
  referenced in the README's "Within GitHub Copilot CLI, run `/lsp show`" quick-start
  step, Claim 4) — a CLI-native equivalent of an IDE's "language server output panel."
  The changelog does not itself explain what "loads the index" fully entails (in-memory
  load of a pre-built index vs. triggering a fresh build) — that detail comes from the
  `docs/indexing.md` companion doc (Claim 3).

### Claim 3: Building the WCI index for the first time can take additional time and temporarily increase memory usage, particularly for large repositories, but this overhead is a one-time setup cost — the index is then reused and dynamically updated on subsequent use

- **Evidence**: The changelog's explicit performance-tradeoff framing, one paragraph.
- **Confidence**: settled (first-party statement of a known performance tradeoff,
  self-disclosed rather than omitted); the actual magnitude ("additional time," "large or
  complex repositories") is qualitative, not quantified
- **Quote**: "Building the index for the first time can take additional time and
  temporarily increase memory usage, particularly for large or complex repositories.
  After the initial index is complete, it is reused and dynamically updated, so this
  overhead is primarily associated with initial setup."
- **Our assessment**: This is a standard cold-start-index tradeoff (also documented for
  Serena's LSP-backed indexes in `docs-ghaw-guides-serena.md` Claim 10 — "Slow initial
  analysis... expected behavior as language servers build indexes, subsequent runs use
  cached data") — but with a structural difference: Serena's cache persistence is an
  opt-in workflow step (`mkdir -p /tmp/gh-aw/cache-memory/serena` plus a pinned cache
  key) that the *user* must configure, whereas WCI's index reuse is stated here as
  automatic and on-by-default within a single Copilot CLI project, with no equivalent
  user-managed cache-directory step described in any of the five pages read. Neither
  source gives a number for "how long" or "how much memory" the first-time build costs.

### Claim 4: WCI belongs to the Microsoft C++ Language Server, a separate, currently-preview npm package/Copilot CLI plugin that brings "the same C++ code intelligence used in Visual Studio and VS Code" specifically to **GitHub Copilot CLI** (not an IDE), requiring an active Copilot subscription, the Copilot CLI, npm, and a one-time EULA-accept-and-login step

- **Evidence**: The repository README's opening framing paragraph and "Prerequisites"/
  "Quick start" sections; the preview-status disclosure is a standalone italicized line
  directly under the README's title.
- **Confidence**: settled (first-party project README, unambiguous about product name,
  target surface, and preview status)
- **Quote**: "_The Microsoft C++ Language Server is currently in preview and may be
  subject to change in future releases._" / "**Microsoft C++ Language Server** brings the
  same C++ code intelligence used in Visual Studio and VS Code to GitHub Copilot CLI on
  Windows, macOS, and Linux. It provides fast, accurate understanding of C++ codebases
  with features like symbol search and semantic navigation." / "Run `npx
  @microsoft/cpp-language-server --accept-eula --login` to accept the license terms and
  login to GitHub. An active GitHub Copilot subscription is required."
- **Our assessment**: This is the single most important scoping correction this
  extraction surfaces relative to the source issue's own triage comments (see Extraction
  Notes): all three Prospector triage comments on issue #3654 framed this as an "IDE
  Configuration" or general "code intelligence" feature without noting that the
  changelog's very first sentence names **Copilot CLI**, not Visual Studio or VS Code, as
  the surface. The README makes this explicit and adds that the underlying capability
  ("the same C++ code intelligence used in Visual Studio and VS Code") is being ported
  *from* the IDEs *to* the CLI-based agent, not the reverse. For Ch02/Ch04 (per triage):
  guide text should describe this as "IDE-grade LSP tooling now available to a
  CLI/terminal-based coding agent," not as an IDE feature. The explicit preview-status
  disclosure ("currently in preview and may be subject to change") is also the reason
  this note's overall confidence is graded `emerging` rather than `settled` — the product
  itself, not just this one feature, could change materially before GA.

### Claim 5: The language server requires a `compile_commands.json` compilation database to function; GitHub/Microsoft ship a bundled "generate-compile-commands" Copilot CLI skill that can auto-generate this file for CMake or MSBuild (vcxproj) projects from a natural-language prompt such as "regenerate compile commands" or "load project"

- **Evidence**: Stated in both the README's Quick Start (step 3) and `docs/compile-commands.md`'s "Generate with Copilot CLI" section, worded consistently.
- **Confidence**: settled (first-party documentation of a concrete, named mechanism)
- **Quote**: "Create a compile_commands.json file for your project. For CMake or MSBuild
  (vcxproj) projects, run the generate-compile-commands skill in GitHub Copilot CLI with
  a prompt like \"regenerate compile commands\" or \"load project\" to generate the file
  and configure the language server." (README, Quick Start step 3) / "For CMake or
  MSBuild (vcxproj) projects, run the generate-compile-commands skill in GitHub Copilot
  CLI with a prompt like \"regenerate compile commands\" or \"load project\" to generate
  the file and configure the language server. The skill is included with the
  cpp-language-server plugin." (`docs/compile-commands.md`)
- **Our assessment**: This is a concrete instance of a pattern already documented in this
  corpus (`docs-github-copilot-agent-skills-cli.md` Claim 1 and Concrete Artifacts): a
  Copilot CLI plugin bundling a skill (`skills/generate-compile-commands/SKILL.md`) as
  part of its own installation, rather than requiring the user to author or separately
  install one. The novel wrinkle here is that the skill's job is *self-configuration of
  the tool it ships with* — the plugin cannot do semantic C++ navigation until
  `compile_commands.json` exists, and the plugin solves its own bootstrapping problem by
  including a skill that generates that exact prerequisite file. For Ch02 (Harness
  Engineering — Extension Points): document this as a design pattern worth citing
  alongside the general skills-as-package-manager coverage — a plugin can ship a
  companion skill whose sole purpose is satisfying the plugin's own configuration
  prerequisite, reducing "read the docs, run three manual commands" onboarding to a
  single natural-language prompt.

### Claim 6: For build systems other than CMake/MSBuild, the documentation explicitly recommends capturing the ad hoc `compile_commands.json`-generation steps as a project-specific, reusable Copilot CLI skill rather than a one-off manual procedure, and points to a starter template and a separate authoring guide for doing so

- **Evidence**: `docs/compile-commands.md`'s "Other build systems" section, a direct
  recommendation with two named supporting resources (a starter-template skill and an
  "authoring an extractor skill" guide).
- **Confidence**: emerging (a documented recommendation/best-practice framing rather than
  a required mechanism — the linked `AUTHORING_EXTRACTOR_SKILL.md` guide and
  `setup-cpp-language-server` starter-template skill were not independently fetched by
  this Miner, so their content beyond this quoted pointer is not verified)
- **Quote**: "Refer to your build system vendor's documentation. For custom or
  non-standard builds, we recommend capturing the steps to generate
  compile_commands.json in a project-specific skill so the process is reproducible for
  you and your team. Once you've worked out the commands needed to produce the file,
  save them as a skill (for example, in your project's skills/ directory) following the
  GitHub Copilot CLI skills documentation. The setup-cpp-language-server skill is a good
  starting template to adapt."
- **Our assessment**: This is a second, more general instance of the same
  skill-as-self-configuration pattern from Claim 5, but explicitly generalized by the
  documentation itself into team-level practitioner guidance: any non-standard,
  hard-to-reproduce local setup procedure is a candidate for encoding as a project-owned
  skill, not just documentation prose a human has to re-follow. For Ch01/Ch02: this is a
  citable, first-party-recommended instance of "turn a one-off manual setup procedure
  into a reproducible skill" as a general onboarding/reproducibility practice, independent
  of the specific C++ language-server use case.

### Claim 7: The LSP feature-support matrix explicitly documents that the server does not support live text-document synchronization — the AI agent is expected to write files to disk before invoking any LSP operation, rather than the language server tracking in-memory unsaved edits the way an IDE's LSP client does

- **Evidence**: `docs/lsp-features.md`'s support table, first row, with an explicit
  "Notes" annotation — the only row in the entire 19-row table carrying an explanatory
  note.
- **Confidence**: settled (first-party, explicit statement of an architectural
  precondition, singled out for annotation among 19 listed capabilities)
- **Quote**: "Text document sync | No | AI agent is expected to update files on disk
  before invoking LSP operations."
- **Our assessment**: This is the single most consequential architectural fact in the
  source for anyone building or evaluating agent-facing LSP integrations generally, and
  it is easy to miss because it appears only as one cell in a feature table, not called
  out in the changelog's prose. A conventional IDE-facing language server tracks
  in-buffer, unsaved edits via `textDocument/didChange` notifications and can answer
  "go to definition" against code the user hasn't saved yet. This server explicitly does
  not: an agent must persist its edit to disk first, then invoke the LSP operation, or
  risk querying against stale on-disk state. For Ch02 (Harness Engineering — Extension
  Points, LSP integrations): this is a concrete gotcha to document for any agent
  orchestration loop that interleaves edit-tool calls with LSP navigation calls — the
  ordering (write-then-query, not query-during-editing) is a hard requirement here, not
  an optimization. It also distinguishes this LSP integration from Serena's, which does
  not document an equivalent disk-sync constraint in `docs-ghaw-guides-serena.md` (though
  that note does not explicitly confirm the opposite either — this is a documented gap
  worth flagging, not a contradiction).

### Claim 8: Disabling WCI requires editing a per-user, cross-repository `state.json` file (not a per-project config file) to set `use_symbol_index` to `false`, restarting Copilot CLI, and the same file can also contain authentication data — so it must never be committed to a repository or attached to a public issue

- **Evidence**: `docs/indexing.md`'s "Disabling WCI" procedure and its "IMPORTANT" callout, stated as a numbered four-step process plus a boxed warning.
- **Confidence**: settled (first-party, procedural documentation with an explicit
  security/secrets-hygiene warning)
- **Quote**: "To reduce background indexing work, set use_symbol_index to the JSON
  boolean false in the language server's per-user state.json file. This setting applies
  to all repositories for that user; it does not belong in your project's cpp-lsp.json
  or Copilot CLI's lsp.json." / "The state file can also contain authentication data and
  other user settings. Do not replace an existing file with only the example above,
  commit it to your repository, or attach it to a public issue."
- **Our assessment**: Two distinct facts worth separating: (1) the disable toggle is
  scoped to the *user*, globally across every repository they work in — a practitioner
  cannot disable WCI for one noisy monorepo while keeping it on for a smaller project
  without disabling it everywhere for that user; and (2) the file holding that toggle is
  the same file that may hold credentials, which is the kind of "innocuous-looking config
  file actually contains secrets" trap this guide's security-review discipline should
  flag by name. The explicit warning against attaching the file to a public GitHub issue
  ("do not... attach it to a public issue") is a first-party acknowledgment that this
  specific failure mode (a user pasting their state.json into a bug report to demonstrate
  a config problem) is anticipated and considered likely enough to warn about explicitly.
  For Ch07 (Security, per corpus convention) or Ch03 (Safety and Verification): add
  per-user language-server state files as a named category of "config files that may
  silently contain credentials," alongside any existing guidance on `.mcp.json` or
  similar files.

### Claim 9: Configuration for the language server is split across three cooperating files with distinct scopes — `.github/lsp.json` (registers the server with Copilot CLI and sets its launch arguments), `.mscppls/cpp-lsp.json` (optional; sets the project root and `compile_commands.json` path), and `compile_commands.json` itself — with an automatic-discovery mode available that eliminates the need for the middle file

- **Evidence**: `docs/configuration.md`'s "Configuration files" list and its "Minimal
  configuration (automatic discovery)" section.
- **Confidence**: settled (first-party configuration-file reference documentation)
- **Quote**: ".github/lsp.json configures GitHub Copilot CLI to use the Microsoft C++
  Language Server for C++ files, and sets the command line arguments passed to mscppls.
  The plugin supplies a server definition; use this project-level file to customize it."
  / ".mscppls/cpp-lsp.json is optional and sets the path to the project root and the path
  to the compile_commands.json file... version must always be 1." / "If you omit the
  --lsp-config argument (or pass --allow-missing-lsp-config), the language server
  automatically searches each workspace folder for a single compile_commands.json and
  infers the repository root from the workspace folder. In this mode you don't need a
  cpp-lsp.json file or a repositoryPath... Discovery fails if no compile_commands.json is
  found or if more than one is found; in that case, use an explicit cpp-lsp.json."
- **Our assessment**: The automatic-discovery fallback is a meaningful ergonomics detail:
  a project with exactly one `compile_commands.json` needs zero project-specific LSP
  configuration files beyond what the plugin itself supplies — the explicit
  `cpp-lsp.json` file exists specifically to disambiguate multi-target or
  non-standard-layout repositories (multiple `compile_commands.json` files, or a
  repository root that differs from the workspace folder). For Ch02: document the
  "works with zero config for the common case, explicit config file only for the
  disambiguation case" pattern as the intended configuration ergonomics, and note the
  `.github/lsp.json` reference points to the general GitHub Copilot CLI
  "Configuring LSP servers" mechanism — meaning any LSP server (not just this C++ one)
  can plug into Copilot CLI via the same `.github/lsp.json` convention, which is a
  broader, reusable extension point worth documenting independently of this specific
  C++ plugin.

### Claim 10: Directory-scan exclude/include settings (`filesExclude`, `searchExclude`, `browse.path` in `cpp-lsp.json`) only affect which *additional* files are scanned for browsing/symbol search — they never remove or add to the translation units actually built from `compile_commands.json`, which remain the authoritative source of what gets compiled and indexed for build-accurate results

- **Evidence**: `docs/indexing.md`'s "Excluding files and customizing indexed
  directories" section, stated as an explicit boundary condition with a worked JSON
  example.
- **Confidence**: settled (first-party documentation of a specific, bounded configuration
  mechanism, with an explicit statement of what it does *not* affect)
- **Quote**: "The translation units listed in compile_commands.json are not affected by
  the exclude settings below. The directories containing those translation units are
  also scanned to discover additional files (such as headers) to index for browsing and
  symbol search, and this scan applies a small set of default excludes. The settings in
  cpp-lsp.json customize only this additional directory scan; they are separate from the
  WCI setting above." / "Include additional directories in the scan via browse.path. The
  scanned directories are always derived from the compile_commands.json entries;
  browse.path specifies further directories to index/parse on top of those."
- **Our assessment**: This is a precise, load-bearing distinction that a practitioner
  could easily get wrong: adding a directory to `filesExclude` does not narrow what the
  compiler-accurate part of the index covers (that's fixed by `compile_commands.json`),
  it only narrows the *supplementary* browse/search scan used for things like header
  files not directly listed as translation units. A practitioner trying to speed up
  indexing by excluding a large generated-code directory via `filesExclude` will not
  affect indexing time for anything that's actually a build target — only for headers or
  browse-only files under that path. For Ch02: document this exclude/build-index
  distinction explicitly if the guide covers indexing-performance tuning for this or
  similar compiler-database-driven tools, since the two exclude mechanisms
  (build-database-derived vs. directory-scan-derived) are easy to conflate.

### Claim 11: The documented LSP capability matrix supports navigation and read-oriented operations (hover, completion, signature help, go to definition, find references, document/workspace symbols, folding ranges, go to declaration/type definition, call hierarchy, pull diagnostics, workspace folders — 12 of 19 listed capabilities) but explicitly does not support write/refactor-oriented operations (rename, code actions, code lens, any formatting variant, document highlight)

- **Evidence**: `docs/lsp-features.md`'s complete 19-row Yes/No support table.
- **Confidence**: settled (first-party, explicit Yes/No enumeration of every listed LSP
  capability — no ambiguity about what is and is not supported as of this documentation
  snapshot)
- **Quote**: (see Concrete Artifacts for the full verbatim table; representative rows)
  "Rename | No |" / "Code Action | No |" / "Go to Definition | Yes |" / "Find References
  | Yes |" / "Call Hierarchy | Yes |"
- **Our assessment**: The Yes/No split cleanly separates "understand the code" operations
  (all supported) from "change the code via the language server itself" operations (all
  unsupported) — consistent with Claim 7's disk-sync constraint: a language server that
  isn't tracking live edits is a poor fit for LSP-native rename/refactor operations
  anyway, since those require coordinated, atomic multi-file edits the server would need
  to apply itself. In practice this means an agent using this integration gets
  IDE-grade *navigation* (this is genuinely equivalent to what a human C++ developer's
  IDE gives them) but must still perform all actual code *modification* through its
  normal file-editing tools, not through the language server. For Ch02: document this
  navigate-yes/refactor-no scope explicitly so practitioners don't expect
  LSP-driven rename or auto-fix behavior from this integration — it is a symbol-finding
  and reference-tracing tool, not a refactoring engine, corroborating the "prefer
  symbol-level operations... over file-level edits" framing in `docs-ghaw-guides-serena.md`
  Claim 5 only for the subset of operations (`replace_symbol_body`-equivalent) this
  server does not itself expose — this server would need to be paired with a separate
  edit tool to modify what it helps you find, whereas Serena bundles both navigation and
  symbol-level editing tools directly.

## Concrete Artifacts

### WCI disable procedure (verbatim JSON + steps, from `docs/indexing.md`)

```
Source: https://github.com/microsoft/cpp-language-server/blob/main/docs/indexing.md
(linked from the github.blog changelog's "Configure indexing" section)

1. Close running Copilot CLI sessions that use the C++ language server.
2. Open the state file for your platform:
     Windows:         %LOCALAPPDATA%\mscppls\state.json
     macOS and Linux: $HOME/.mscppls/state.json
3. Add or update the use_symbol_index property in the existing top-level JSON
   object, preserving all other properties. If the file does not exist, create
   its parent directory and a file containing:

   {
     "use_symbol_index": false
   }

4. Restart Copilot CLI so the language server reads the updated setting.

IMPORTANT (verbatim): "The state file can also contain authentication data and
other user settings. Do not replace an existing file with only the example
above, commit it to your repository, or attach it to a public issue."

To re-enable: set use_symbol_index to true and restart the language server again.
```

### Minimal automatic-discovery `.github/lsp.json` (verbatim, from `docs/configuration.md`)

```json
{
  "lspServers": {
    "cpp": {
      "command": "mscppls",
      "args": [],
      "fileExtensions": {
        ".cpp": "cpp",
        ".c": "cpp",
        ".h": "cpp",
        ".hpp": "cpp"
      },
      "requestTimeoutMs": 1000000
    }
  }
}
```

### `cpp-lsp.json` with exclude/browse customization (verbatim, from `docs/indexing.md`)

```json
{
  "version": 1,
  "repositoryPath": "../",
  "compileCommands": "../build/compile_commands.json",
  "filesExclude": { "**/out": true, "**/third_party": true },
  "searchExclude": { "**/*.generated.h": true },
  "browse": { "path": ["${workspaceFolder}/src"] }
}
```

### Full LSP capability matrix (verbatim, from `docs/lsp-features.md`)

```
Source: https://github.com/microsoft/cpp-language-server/blob/main/docs/lsp-features.md

| Feature                | Supported | Notes                                                          |
| ----------------------- | --------- | --------------------------------------------------------------- |
| Text document sync     | No        | AI agent is expected to update files on disk before invoking LSP operations. |
| Hover                  | Yes       |                                                                   |
| Completion             | Yes       |                                                                   |
| Signature help         | Yes       |                                                                   |
| Go to Definition       | Yes       |                                                                   |
| Find References        | Yes       |                                                                   |
| Document Highlight     | No        |                                                                   |
| Document Symbols       | Yes       |                                                                   |
| Workspace Symbols      | Yes       |                                                                   |
| Code Action            | No        |                                                                   |
| Code Lens              | No        |                                                                   |
| Document Formatting    | No        |                                                                   |
| Range Formatting       | No        |                                                                   |
| On type Formatting     | No        |                                                                   |
| Folding Ranges         | Yes       |                                                                   |
| Rename                 | No        |                                                                   |
| Go to Declaration      | Yes       |                                                                   |
| Go to Type Definition  | Yes       |                                                                   |
| Call Hierarchy         | Yes       |                                                                   |
| Pull Diagnostics       | Yes       |                                                                   |
| Workspace Folders      | Yes       |                                                                   |
```

### Quick Start (verbatim excerpt, from `README.md`)

```
Source: https://github.com/microsoft/cpp-language-server (main branch README)

1. Install the cpp-language-server plugin from the copilot-plugins marketplace.
   From within GitHub Copilot CLI, run:
     /plugin install cpp-language-server@copilot-plugins
   This bundles the language server and auto-updates with the latest version,
   so you don't need to install the npm package manually.
2. Run `npx @microsoft/cpp-language-server --accept-eula --login` to accept
   the license terms and login to GitHub. An active GitHub Copilot subscription
   is required.
3. Create a compile_commands.json file for your project. For CMake or MSBuild
   (vcxproj) projects, run the generate-compile-commands skill in GitHub
   Copilot CLI with a prompt like "regenerate compile commands" or "load
   project" to generate the file and configure the language server.
4. Launch GitHub Copilot CLI from your project root directory.
5. Within GitHub Copilot CLI, run /lsp show. You should see a "cpp" server running.
6. Use GitHub Copilot CLI like normal, now with enhanced C++ capabilities. To
   nudge the agent to use the tools, try adding phrases like "use LSP tools"
   to your prompt.
```

## Cross-References

- **Extends**:
  - `docs-github-copilot-agent-skills-cli.md` (Claim 1, `gh skill` package-manager
    paradigm and Concrete Artifacts, `--agent` host targeting): this note's Claim 5/6
    (the bundled `generate-compile-commands` skill, and the documentation's explicit
    "capture ad hoc setup steps as a project skill" recommendation) is a first-party,
    shipped example of a plugin using a skill for *self-configuration* — narrower and
    more specific than that note's general package-manager coverage of skill
    distribution, install, and versioning.
  - `docs-github-copilot-agent-plugins-1-0.md` (Claim 8, minimal plugin structure with a
    `skills/` subdirectory; Claim 13, GitHub's native plugin format supporting an
    `lsp.json` file "in the plugin root, or in `.github/`"): this note's `cpp-language-server`
    plugin is a concrete, shipped instance of exactly the `lsp.json`-bundling plugin
    capability that note documents only as an abstract format field. The Quick Start's
    `/plugin install cpp-language-server@copilot-plugins` also confirms that note's Claim
    14 detail that `copilot-plugins` is one of VS Code/Copilot CLI's default marketplaces.
  - `blog-anthropic-large-codebase-best-practices.md` (Claim 5, the "seven extension
    points" taxonomy naming LSP integrations as one of two additional capabilities beyond
    the five primary ones; Claim 10, "LSP integrations give Claude IDE-level symbol
    navigation... follow a function call to its definition, trace references across
    files"): this note is a concrete, vendor-specific (GitHub/Microsoft, not Anthropic)
    instance of exactly that LSP-integration extension point, for a different agent host
    (Copilot CLI, not Claude Code) and a different language (C++ specifically, not
    general-purpose). The capability description lines up closely; this note adds
    operational detail (the disk-sync constraint of Claim 7, the compile-database
    prerequisite of Claim 5, the exclude/build-index boundary of Claim 10) that the
    Anthropic post does not cover for its own LSP integrations.
  - `docs-ghaw-guides-serena.md` (Claim 10, "Slow initial analysis... expected behavior as
    language servers build indexes, subsequent runs use cached data"): corroborates this
    note's Claim 3 cold-start-index tradeoff as a general property of LSP-backed agentic
    tooling, not specific to either product. See Claim 3's "Our assessment" for the
    structural difference (opt-in user-managed cache directory for Serena vs. automatic,
    on-by-default reuse described here).

- **Contradicts**: None identified. No existing corpus source makes a claim about C++
  code intelligence, whole-codebase indexing, or the `cpp-language-server` project that
  this source opposes. The existing C++-related note in the corpus,
  `docs-github-copilot-vs-june-2026.md` (Claim 7, the GitHub Copilot "modernization
  agent" reaching GA for MSVC/C++ toolset-upgrade scenarios in **Visual Studio**), covers
  a different product, a different surface (Visual Studio, not Copilot CLI), and a
  different task (automated compiler/toolset migration, not symbol navigation) — the two
  sources are complementary C++ tooling announcements from the same vendor family, not
  competing or conflicting claims about the same feature. No contradiction issue filed.

- **Novel**:
  - **A CLI-native (not IDE-native) LSP integration explicitly designed around an
    agent-writes-then-queries model, with the "no text document sync" constraint
    documented as a first-class limitation** (Claim 7): no existing corpus source
    documents this specific disk-sync precondition for an agent-facing language server
    integration.
  - **A plugin that bundles a skill specifically to generate its own missing
    configuration prerequisite** (Claim 5): the self-bootstrapping skill pattern (plugin
    ships a skill whose job is to produce the exact file the plugin needs to function) is
    new to the corpus; prior skill-related notes document skills as general-purpose
    capabilities, not prerequisite-generation for their own host plugin.
  - **A per-user, cross-repository (not per-project) toggle for a code-intelligence
    feature, stored in a file that may also hold credentials** (Claim 8): the
    global-scope-toggle-in-a-secrets-adjacent-file combination is a specific, novel
    configuration-hygiene detail not previously documented in this corpus's LSP or
    code-navigation coverage.
  - **An explicit, first-party documented boundary between compile-database-derived
    indexing scope and directory-scan exclude/include settings** (Claim 10): no existing
    corpus source documents this specific two-tier exclude-mechanism distinction for a
    compiler-database-driven code-intelligence tool.
  - **A complete, enumerated LSP capability matrix (19 rows) for a shipped,
    agent-facing language server integration** (Claim 11 and Concrete Artifacts): no
    existing corpus source gives this level of granular, row-by-row LSP feature support
    detail for any Copilot, Claude, or gh-aw code-navigation integration.

## Guide Impact

- **Chapter 02 (Harness Engineering — IDE Configuration and Code Understanding / LSP
  Extension Points)**:
  - Correct the framing implied by the source issue's own triage: this is a **Copilot
    CLI** (terminal/agent-native) feature, not a Visual Studio or VS Code IDE feature —
    it ports IDE-grade C++ code intelligence *to* a CLI coding agent (Claim 4). If the
    guide's LSP-integration coverage (following
    `blog-anthropic-large-codebase-best-practices.md` Claim 10) currently discusses LSP
    integrations only in the abstract or only for Claude Code, add this as a
    vendor-independent, concrete second example with operational specifics.
  - Document the "agent writes to disk, then queries the language server" precondition
    (Claim 7) as a general design constraint worth checking for any LSP-backed agent tool
    — this determines whether an orchestration loop can safely interleave edit and
    navigation calls or must sequence them strictly.
  - Document the "plugin bundles a skill to generate its own prerequisite config"
    pattern (Claim 5) and the more general "capture ad hoc setup steps as a
    project-owned skill" recommendation (Claim 6) as reusable onboarding-automation
    patterns, independent of C++ or this specific plugin.
  - Document the compile-database-vs-directory-scan exclude boundary (Claim 10) if the
    guide covers indexing-performance tuning for any similar compiler-database-driven
    tool, to prevent practitioners from assuming `filesExclude` narrows build-accurate
    index scope when it does not.

- **Chapter 03 (Safety and Verification) or wherever the guide covers secrets-adjacent
  config files**:
  - Add per-user language-server state files (`state.json`, Claim 8) as a named example
    of a config/debugging file that may also carry authentication data — with the
    specific, first-party-documented failure mode of accidentally attaching such a file
    to a public bug report.

- **Chapter 04 (Agentic Workflows — Code Navigation and Context)**:
  - Document the navigate-yes/refactor-no capability split (Claim 11) so practitioners
    correctly scope what this class of tool does for them: it accelerates
    finding/understanding code, not applying multi-file refactors — those still go
    through the agent's normal file-editing tools.

## Extraction Notes

1. **Six pages fetched, within MINER.md's "up to 5 linked pages" guidance**: the primary
   github.blog changelog (very short — six paragraphs) plus five substantive linked pages
   from the `microsoft/cpp-language-server` repository: `README.md`, `docs/indexing.md`
   (directly linked from the changelog's "disable WCI" sentence), `docs/configuration.md`,
   `docs/compile-commands.md`, and `docs/lsp-features.md`. All were fetched via `curl`
   with a browser user-agent (the changelog required following an HTTP 301 redirect to
   its trailing-slash URL first) and read as raw HTML-stripped text or raw Markdown, not
   through a summarizing fetch tool — every `Quote` field above was copied
   character-for-character from that raw text, including exact curly-apostrophe
   characters (’) as they appear in the source HTML. Four further linked pages
   (`docs/installation.md`, `docs/command-line-options.md`, `docs/authentication.md`,
   `docs/troubleshooting.md`) were not fetched — judged non-substantive for this note's
   WCI-focused scope beyond what the five pages already read cover (installation
   platforms, CLI flags, auth methods, and troubleshooting entries not central to how WCI
   itself works or is configured).

2. **Scope correction relative to the Prospector's triage comments**: All three triage
   comments on issue #3654 characterized this source as being about "IDE Configuration,"
   general "code intelligence," or a general "development workflow" question, and one
   explicitly framed the "key question" around whether this "change[s] how agents
   understand or navigate unfamiliar codebases" in a general sense. Direct reading of the
   source (both the changelog's first sentence and the README's product description)
   shows the feature is specific to **GitHub Copilot CLI**, not an IDE, and the "agents"
   in question are Copilot CLI sessions specifically, not agentic coding tools generally.
   This note's Claim 4 documents this correction explicitly; Guide Impact recommendations
   are written against the corrected (CLI-specific) framing rather than the triage
   comments' more general framing.

3. **`cpp-lsp.json` vs. `.github/lsp.json` vs. `compile_commands.json` naming is easy to
   confuse**: three distinct, similarly-named JSON files exist in this system
   (`.github/lsp.json`, `.mscppls/cpp-lsp.json`, `compile_commands.json`), each with a
   different owner (Copilot CLI's general LSP-server registration mechanism, this
   specific language server's project-root/compile-commands pointer, and the
   compiler-database format respectively). This note's Claim 9 and the Concrete Artifacts
   examples preserve the exact file paths and JSON shapes as documented, to avoid
   introducing a naming error in guide text that cites this configuration surface.

4. **MSBuild/vcxproj support is explicitly incomplete**: `docs/compile-commands.md`
   states "Improved support for MSBuild projects is planned for a future release of the
   Microsoft C++ Language Server" and points to a third-party sample application
   (`microsoft/msbuild-extractor-sample`) as a current workaround, noting it "may require
   adaptation for complex projects." This was not extracted as its own numbered claim
   (it is a documented gap/roadmap item rather than a shipped capability) but is flagged
   here since it directly qualifies the README's Quick Start's blanket "For CMake or
   MSBuild (vcxproj) projects, run the generate-compile-commands skill" instruction —
   MSBuild support via that skill is not yet at the same maturity as CMake support per
   this caveat.

5. **No contradictions identified; one related-but-distinct existing note found**:
   Cross-referenced against all existing GitHub Copilot CLI, VS/VS Code, agent-skills,
   agent-plugins, and LSP/code-navigation notes in the corpus (see Cross-References). The
   only C++-specific existing note, `docs-github-copilot-vs-june-2026.md`, covers a
   different product (Visual Studio's MSVC modernization agent) and does not overlap in
   claim content with this source. No contradiction issue filed.

6. **Overall confidence graded `emerging`, not `settled`**: individual claims about
   documented behavior are graded `settled` (unambiguous first-party statements of
   shipped mechanism), but the overall confidence reflects that the underlying product —
   the Microsoft C++ Language Server itself — is explicitly self-described as "currently
   in preview and may be subject to change in future releases," and no claim in this
   source is independently verified, benchmarked, or corroborated by any non-Microsoft/
   non-GitHub source.
