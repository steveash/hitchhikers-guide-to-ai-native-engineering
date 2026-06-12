---
source_url: https://github.blog/changelog/2026-06-11-copilot-cli-configure-everything-from-one-place-with-settings
source_type: docs
title: "Copilot CLI: Configure everything from one place with /settings"
author: GitHub (official changelog)
date_published: 2026-06-11
date_extracted: 2026-06-12
last_checked: 2026-06-12
status: current
confidence_overall: settled
issue: "#1157"
---

# Copilot CLI: Configure Everything from One Place with /settings

> GitHub's June 11, 2026 changelog announces a unified `/settings` slash command that
> consolidates previously scattered Copilot CLI configuration (including `/theme`,
> `/streamer-mode`, and `/experimental`) into a single schema-driven, tab-completing
> interface — revealing an architectural pattern for self-documenting CLI configuration
> as AI developer tools accumulate settings surface.

## Source Context

- **Type**: docs (GitHub official product changelog, June 11, 2026; approximately 300
  words)
- **Author credibility**: GitHub engineering team announcing a production feature in the
  Copilot CLI. Authoritative for: the feature's existence, its three invocation modes,
  the supported editor types, the keyboard shortcuts, and the list of previously
  scattered commands that are consolidated. Not a credible source for: which specific
  settings keys are available in the schema, performance characteristics, whether old
  scattered commands (e.g., `/theme`, `/experimental on`) remain supported for backward
  compatibility, or how `/settings` interacts with enterprise admin policies.
- **Scope**: The new `/settings` slash command: invocation modes, dialog interface,
  tab-completion mechanics, type-specific editors, schema validation, keyboard shortcuts,
  and the commands it supersedes. Does NOT cover: full enumeration of all available
  setting keys, whether admin-level policies can restrict individual settings, plan-tier
  availability, backward compatibility with the old scattered commands, or how settings
  roam across machines or Copilot environments.

## Extracted Claims

### Claim 1: The `/settings` command consolidates previously scattered Copilot CLI configuration commands — including `/theme`, `/streamer-mode`, and `/experimental` — into a single unified interface

- **Evidence**: Official GitHub product changelog describing the consolidation with
  named examples of commands now subsumed.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: (no direct verbatim quote listing all three; described as consolidating
  previously scattered commands including `/theme`, `/streamer-mode`, and `/experimental`
  into a single interface, consistent across both source fetches)
- **Our assessment**: The consolidation addresses a real pain point in maturing CLI
  tools: as features accumulate, configuration spreads across ad-hoc commands that users
  must discover individually. The explicit naming of `/theme`, `/streamer-mode`, and
  `/experimental` signals that all three were previously handled by standalone slash
  commands — now they are entries in a unified settings schema. For practitioners who
  have automated CLI configuration in scripts (e.g., `/experimental on` to enable
  experimental features), this signals a potential interface migration. For guide
  advice: direct users to `/settings` as the canonical starting point for configuration
  rather than remembering individual command names.

### Claim 2: The command has three invocation modes — interactive full-screen dialog, inline key-value assignment, and reset to defaults — covering exploratory and scripted configuration workflows

- **Evidence**: Official changelog documents all three modes with specific syntax
  examples.
- **Confidence**: settled (product fact in official changelog, consistent across both
  source fetches)
- **Quote**: (no single verbatim quote enumerating all three modes; individual mode
  examples including `/settings autoUpdate true` and `/settings reset` confirmed across
  both fetches)
- **Our assessment**: The three-mode design covers distinct user contexts. Interactive
  mode (`/settings` alone) serves first-time discovery and browsing. Inline mode
  (`/settings key value`, e.g., `/settings autoUpdate true`) serves quick targeted
  changes and is scriptable. Reset mode (`/settings reset`) provides a safe fallback
  when configuration drifts into an unexpected state. Together, the three modes make
  the command useful for both interactive explorers and practitioners building
  CLI configuration scripts or onboarding guides. The reset mode is particularly
  valuable in team environments where practitioners inherit misconfigured setups.

### Claim 3: Tab completion surfaces every available setting key along with its description and allowed values directly at the prompt, making the entire configuration surface self-documenting

- **Evidence**: Official changelog describes the tab-completion mechanism with this
  specific scope.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: "Tab completion surfaces every available key — along with the description
  and the allowed values for booleans, enums, and enum-or-string unions — right next
  to your prompt."
- **Our assessment**: This is the most architecturally significant claim in the source.
  Tab completion as a documentation mechanism means practitioners never need to consult
  external docs to know what settings exist, what each does, or what values are valid.
  The enumeration scope — "every available key" — implies the system uses a complete
  schema as the source of truth for completion candidates, not a partial list. The
  inline description + allowed-values disclosure turns the CLI prompt itself into the
  documentation surface. For Ch02 (Harness Engineering): this is a concrete example
  of "self-documenting tooling" as a design pattern — the configuration surface is
  explorable without documentation dependencies. For practitioners onboarding to Copilot
  CLI: tab-complete through settings instead of reading a separate config reference.

### Claim 4: The interactive dialog opens an alternate-screen searchable UI with type-specific editors for each setting

- **Evidence**: Official changelog describes the dialog interface.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: "a searchable, alt-screen dialog with editors built for each setting type"
- **Our assessment**: The alternate-screen approach (like vim/less/htop) means the
  dialog does not pollute the terminal scrollback. The type-specific editors are the
  key UX investment: rather than a generic text field for every setting, boolean
  settings get toggles, enum settings get pickers, string/number settings get
  appropriate inputs. This reduces invalid input before it reaches schema validation.
  From a design perspective, the dialog pattern is consistent with how terminal-based
  configuration UIs (e.g., `kubectl edit`, `git rebase -i`, shell configuration wizards)
  work — it treats configuration as a structured editing task rather than a text input
  task. The search capability (via `/` key, consistent with pager conventions) makes
  the full settings surface navigable even as the number of settings grows.

### Claim 5: The interactive dialog supports six editor types — boolean toggles, enum pickers, string/number inputs, multi-line prose, array editors, and record editors — plus a JSON fallback with schema validation

- **Evidence**: Official changelog enumerates the supported editor types.
- **Confidence**: settled (product fact listed in official changelog)
- **Quote**: (no single verbatim quote lists all types; types confirmed across both
  source fetches as: boolean toggles, enum pickers, string/number inputs with
  multi-line prose support, array editors, record editors, and JSON fallback with
  schema validation)
- **Our assessment**: The breadth of editor types — especially array editors and record
  editors — implies the settings schema includes structured data types, not just scalar
  values. The JSON fallback with schema validation is the escape hatch for complex or
  nested values that do not fit the specialized editor types. For practitioners who need
  to configure structured settings (e.g., custom model parameters or tool configurations
  that are array or record types): the array/record editors are the right tool; the JSON
  fallback handles edge cases where the structured editor is insufficient. The schema
  validation in the JSON fallback means even raw JSON input is checked before being
  written — preventing malformed state that would otherwise require manual file editing
  to resolve.

### Claim 6: Schema validation runs before any setting is written, preventing invalid configuration states from being persisted

- **Evidence**: Official changelog states that validation happens before write.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: (no direct verbatim quote; validation-before-write described consistently
  across both source fetches)
- **Our assessment**: Validation-before-write is an important safety property for a
  settings system that affects the behavior of an AI coding assistant. A malformed
  Copilot CLI setting could cause unexpected behavior during a session — and tracking
  the cause back to a bad config entry would be non-trivial. Pre-write validation means
  the user gets an error message at edit time (when context is clear) rather than
  runtime failures (when the cause is obscure). For Ch02 (Harness Engineering): this
  is the CLI-level equivalent of type-safe configuration management — the schema acts
  as a type system for the settings, and the CLI enforces it. Teams building on top of
  Copilot CLI can rely on the settings file being schema-valid at all times.

### Claim 7: Settings changes with live side effects — such as `colorMode` and `streamerMode` — apply immediately upon saving, providing real-time visual feedback

- **Evidence**: Official changelog names `colorMode` and `streamerMode` as examples
  of settings with immediate live application.
- **Confidence**: settled (specific examples stated in official changelog)
- **Quote**: (no direct verbatim quote; `colorMode` and `streamerMode` cited as
  examples of settings that apply immediately upon saving)
- **Our assessment**: Live application is the interaction model equivalent of CSS
  hot-reload — the user sees the effect of a change without restarting the CLI or
  running a separate apply command. The specific examples (`colorMode`, `streamerMode`)
  are UI/display settings that benefit most from live preview — tweaking a color mode
  without seeing the effect immediately would require a guess-and-restart loop. This
  design choice signals that the settings system is built for interactive refinement,
  not just initial configuration. For practitioners who present or screen-share Copilot
  CLI sessions: `streamerMode` (which likely obscures sensitive information) can now
  be toggled interactively without session restart.

### Claim 8: Three keyboard shortcuts in the dialog support common configuration workflows — Ctrl+E opens the settings file in the user's preferred editor, Ctrl+R resets the focused setting to its default, and `/` enables search

- **Evidence**: Official changelog documents all three keyboard shortcuts.
- **Confidence**: settled (product facts in official changelog)
- **Quote**: (no direct verbatim quote; all three shortcuts confirmed consistently
  across both source fetches)
- **Our assessment**: The three shortcuts cover three distinct escape hatches from the
  dialog: external editor (Ctrl+E) for power users who prefer raw file editing or need
  to batch-edit settings; per-setting reset (Ctrl+R) for recovering individual
  misconfigured values without resetting everything; and search (`/`) for navigating a
  growing settings surface. The Ctrl+E shortcut is architecturally important: it means
  the settings system has a canonical file representation that can be edited, version-
  controlled, and shared across a team. This implies the settings are stored as a
  human-readable file (likely JSON or YAML) rather than being opaque or binary.
  For enterprise deployments: teams could potentially version-control a baseline
  settings file and distribute it as part of onboarding, using Ctrl+E as the path to
  produce it initially.

## Concrete Artifacts

### `/settings` Invocation Modes

```
# Mode 1: Full-screen interactive dialog (browsable, searchable)
/settings

# Mode 2: Inline key-value assignment (scripted or quick changes)
/settings autoUpdate true
/settings <dotted.key.path> <value>

# Mode 3: Reset to defaults
/settings reset

# Update CLI to get the feature first:
copilot update
```

*Source: Copilot CLI changelog, June 11, 2026*

### Dialog Keyboard Shortcuts

```
# Within the /settings dialog:
/          — search within settings
Ctrl+R     — reset focused setting to its default value
Ctrl+E     — open settings file in preferred editor (exit dialog → editor)

# Editor types available per setting:
#   - Boolean toggles
#   - Enum pickers (for finite allowed values)
#   - String / number inputs (with multi-line prose support)
#   - Array editors
#   - Record editors
#   - JSON fallback (with schema validation before write)
```

*Source: Copilot CLI changelog, June 11, 2026*

### Commands Consolidated Into `/settings`

```
Previously scattered commands now managed through /settings:
  /theme           → managed via settings key (e.g., colorMode)
  /streamer-mode   → managed via settings key
  /experimental    → managed via settings key (e.g., experimental true/false)

Design property: schema validation before write; live application of
changes with side effects (colorMode, streamerMode apply immediately).

Tab completion: /settings <Tab> surfaces every key + description +
allowed values directly at the prompt.
```

*Source: Copilot CLI changelog, June 11, 2026*

## Cross-References

- **Extends** `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 9):
  That source documented the two-tier availability pattern for Copilot CLI features and
  specified that experimental features are enabled via `/experimental on`. This source
  introduces the `/settings` command that consolidates `/experimental` into the unified
  settings interface. The rubber duck note's guidance (`/experimental on` to enable
  prompt scheduling and experimental terminal) is now superseded by the settings path —
  but whether the old command still works (backward compatibility) is not confirmed by
  this source. For the guide: update advice on enabling experimental features to
  reference `/settings` as the canonical path, with a note that the old command may
  still work.

- **Extends** `docs-github-copilot-cli-security-review.md` (Claim 1):
  That source documented `/security-review` as an experimental feature requiring
  `/experimental on`. With `/settings` consolidating experimental mode management,
  the path to enable `/security-review` would now flow through `/settings experimental`
  rather than the standalone `/experimental on` command. The same applies to prompt
  scheduling and experimental terminal from `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` (Claim 5):
  That source documented routing transparency (surfacing the selected model name) as
  a practitioner affordance in the CLI. The `/settings` command extends this pattern
  of making the CLI's internal state visible and controllable: transparency about model
  selection at runtime, and transparency about the full configuration surface via tab
  completion. Together, these two sources show GitHub building "legible configuration
  and runtime state" as a systematic CLI design theme.

- **Related** `docs-github-copilot-cca-rest-api-audit-config.md`:
  That source covers REST API-based auditing of Copilot Cloud Agent repository
  configuration (MCP servers, enabled tools, workflow policy, firewall config). This
  source covers developer-facing CLI settings (theme, experimental mode, auto-update).
  The two are complementary, not overlapping: the REST API addresses enterprise admins
  auditing CCA security posture at scale; `/settings` addresses individual practitioners
  configuring their local CLI experience. Together they reveal GitHub building
  configuration management primitives at two levels: enterprise audit (REST API) and
  developer self-service (CLI dialog).

- **Novel**:
  - **Schema-driven, tab-completing CLI settings as a design pattern**: No prior corpus
    source documents a CLI tool using its own schema as the source of truth for tab
    completion — surfacing keys, descriptions, and allowed values inline. Prior corpus
    sources discuss model selection menus and configuration flags, but none document
    this specific pattern of schema-as-documentation.
  - **Six-type editor system for CLI settings**: No prior corpus source documents a
    CLI tool with type-specific editors (boolean toggles, enum pickers, array editors,
    record editors, JSON fallback) built into its settings interface. CLI configuration
    in prior corpus sources is uniformly text/flag-based.
  - **Validation-before-write as a CLI safety property**: Prior corpus sources on CLI
    safety focus on agent action validation and confirmation prompts. This is the first
    corpus source to document schema validation at the configuration-write layer as a
    safety mechanism, preventing misconfiguration at the source rather than handling
    configuration errors at runtime.
  - **Configuration consolidation as feature maturity signal**: No prior corpus source
    explicitly discusses the consolidation of scattered CLI commands into a unified
    settings system as a stage in CLI tool maturity. This source provides a concrete
    example of that lifecycle pattern in a production AI developer tool.

## Guide Impact

### Chapter 01: Daily Workflows

- **Single entry point for CLI configuration**: Add `/settings` as the canonical
  starting point for all Copilot CLI configuration. When practitioners want to change
  theme, enable experimental features, or toggle auto-update, direct them to `/settings`
  rather than individual slash commands. The tab completion + inline descriptions make
  the full configuration surface self-discoverable. For teams onboarding new members:
  `copilot update && /settings` is now the equivalent of a guided setup wizard.
- **Update experimental feature enablement advice**: Prior guidance (from
  `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` and
  `docs-github-copilot-cli-security-review.md`) directed practitioners to use
  `/experimental on` to access experimental features (prompt scheduling, security
  review, experimental terminal). With `/settings` consolidating this, update to
  recommend `/settings` as the canonical path, noting `/experimental on` may still
  work for backward compatibility.

### Chapter 02: Harness Engineering / CLI Configuration

- **Self-documenting configuration as a CLI design principle**: The tab-completion
  approach — surfacing every available key + description + allowed values inline —
  is a concrete example of self-documenting tooling. Add this as a design pattern
  practitioners can apply when building their own CLI harnesses: if users must consult
  external documentation to discover available configuration, the interface is
  underdesigned. A schema-backed tab-completion system eliminates that dependency.
- **Validation-before-write as a harness safety property**: Document the
  schema-validation-before-write pattern as a configuration safety technique. Harnesses
  that write configuration files without validation risk silent misconfiguration;
  the Copilot CLI model validates at the dialog/command layer so the config file stays
  schema-valid at all times. Teams building CLI wrappers should adopt this pattern.
- **Settings file as a team baseline artifact**: The Ctrl+E shortcut reveals that
  settings are stored in a human-editable file. Teams can version-control a baseline
  settings file (e.g., experimental mode on, preferred theme, auto-update policy)
  and distribute it as part of dev environment setup, ensuring consistent CLI behavior
  across the team.

### Chapter 06 / Chapter 07: AI-Native Tooling and Enterprise Operations

- **CLI settings and enterprise policy interplay**: The `/settings` command manages
  developer-controllable settings, but does not address admin-level policy constraints
  (which model restrictions or feature availability are governed at the org level).
  The guide should clarify the boundary: `/settings` is the developer's self-service
  surface; organization-level policy restrictions (documented across multiple Copilot
  governance source notes) operate at a higher layer that `/settings` cannot override.

## Extraction Notes

1. **Source is a short changelog (~300 words)**: Two independent WebFetch calls were
   made. The tool summarized rather than reproducing content verbatim. Only two quotes
   are presented as verbatim (placed in quotation marks by the summarizing model across
   both fetches): "Tab completion surfaces every available key — along with the
   description and the allowed values for booleans, enums, and enum-or-string unions
   — right next to your prompt." and "a searchable, alt-screen dialog with editors built
   for each setting type." All other claims rely on consistent paraphrased description
   across both fetch passes; those claims are marked with "(no direct verbatim quote;
   see paraphrase in Our assessment)." The Assayer should verify all quotes against the
   source URL.
2. **Backward compatibility of old commands unknown**: The changelog does not state
   whether `/experimental on`, `/theme`, and `/streamer-mode` continue to work as
   standalone commands, or whether they have been removed. Claims about consolidation
   are accurate per the source; no backward-compatibility claims are made here.
3. **No settings key enumeration**: The changelog does not list all available settings
   keys. The tab-completion system implies a complete schema exists, but its contents
   are not published in this changelog. Practitioners must use `/settings <Tab>` to
   discover the full surface.
4. **No plan-tier information**: The changelog does not specify whether `/settings`
   is available on all Copilot plans (Individual, Business, Enterprise) or gated.
   Given that prior CLI features like auto model selection are available across all
   plans, this is likely broadly available, but not confirmed by this source.
5. **No contradiction issues filed**: This source adds a new CLI capability and supersedes
   the mechanism for enabling experimental features, but does not contradict any prior
   source note in a way that would lead to different guide advice. The rubber duck and
   security review notes' advice to use `/experimental on` may become stale as `/settings`
   consolidates it — this is a supersession, not a contradiction. No contradiction
   issue filed.
