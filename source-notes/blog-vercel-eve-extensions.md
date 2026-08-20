---
source_url: https://vercel.com/changelog/eve-extensions
source_type: blog-post
title: "Extend eve agents with installable extensions"
author: Casey Gowrie, with contributors Ben Sabic and Kevin Corbett (Vercel)
date_published: 2026-07-22
date_extracted: 2026-08-20
last_checked: 2026-08-20
status: current
confidence_overall: emerging
issue: "#2818"
---

# Extend eve agents with installable extensions

> Vercel changelog announcing that `eve` agents can now import "extensions" —
> installable packages that bundle tools, connections, skills, instructions,
> hooks, channels, schedules, and subagents into a single namespaced,
> versioned dependency — plus, via the linked first-party `eve.dev/docs/extensions`
> documentation it points to, the full authoring/build/mount/override
> mechanics behind that headline feature.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`; a
  short feature announcement — four paragraphs, one scaffolding command, one
  file-tree diagram, one mount code sample, and a three-item capability
  list). Per MINER.md §1, four linked pages were followed because the
  changelog's own prose is thin relative to the feature's surface area:
  `eve.dev/docs/extensions` (the full first-party authoring/consumption
  reference for this exact feature, fetched and read in full), `eve.dev/docs/tools`
  (referenced for the `disableTool()` and approval mechanics an extension's
  tools inherit, read in full), `eve.dev/docs/guides/hooks` (referenced for
  the `toolResultFrom` narrowing mechanic the extensions page cites, read in
  full), and `eve.dev/integrations` (the ready-made extension/integration
  catalogue the docs page points to, read in full to confirm which shipped
  integrations are packaged as extensions today). `eve.dev/docs/subagents`
  and `eve.dev/docs/channels/overview`, both cross-linked from the extensions
  page, were not followed — they document subagent/channel mechanics
  generally rather than anything extension-specific beyond what the
  extensions page itself already states.
- **Author credibility**: First-party Vercel product-team announcement,
  credited to one named author (Casey Gowrie) with two named contributors
  (Ben Sabic, Kevin Corbett) in the changelog's byline. `eve.dev/docs/extensions`
  carries no separate byline (standard product documentation) but is
  consistent with the changelog everywhere the two overlap. No customer
  quotes, adoption metrics, or independent benchmarks appear anywhere in the
  source or the four linked pages — this is first-party documentation of a
  shipping feature, not third-party reporting or validation.
- **Scope**: Covers the extension packaging primitive itself — what an
  extension can contain, how it is scaffolded, configured, built, published,
  mounted, namespaced, overridden, and how a consumer hook can narrow an
  extension tool's result type. Does **not** cover: pricing, a GA/beta
  status label for the extensions feature itself (none found anywhere in the
  five pages read), a full per-integration breakdown of which of the
  catalogued integrations in `eve.dev/integrations` are implemented as
  extensions versus another mechanism, or independent production usage
  evidence — every example given (the `crm` extension, the workspace
  `shared-capabilities` example) is a vendor-authored illustration, not a
  documented customer deployment.

## Extracted Claims

### Claim 1: An extension bundles up to eight distinct capability types — tools, channels, connections, skills, schedules, subagents, instruction fragments, and hooks — into one package that any eve agent can import, published to a registry and installed/versioned/upgraded like a normal dependency
- **Evidence**: The changelog's opening sentence, expanded by the docs page's own opening sentence naming three additional contribution types (channels, schedules, subagents) the changelog's prose omits.
- **Confidence**: settled (first-party, unambiguous, and the two independently-fetched pages' claim counts reconcile once the docs page's fuller list is checked)
- **Quote**: "You can now package tools, connections, skills, instructions, and hooks into extensions that any eve agent can import. Extensions can be published to package registries, then installed, versioned, and upgraded like any other project dependency."
- **Quote (fuller list, docs page)**: "Extensions package eve tools, channels, connections, skills, schedules, subagents, instruction fragments, and hooks."
- **Our assessment**: The changelog's five-item list (tools, connections, skills, instructions, hooks) is a marketing-copy subset of the docs page's eight-item list — the changelog omits channels, schedules, and subagents entirely, even though the docs page's own file-tree diagram for the scaffolded package (Concrete Artifacts) includes `channels/webhook.ts` and `schedules/sync.ts` alongside the five changelog-named slots. A practitioner reading only the changelog would not learn that an extension can ship an entire subagent or a scheduled cron job, which are the two highest-surface-area contribution types (a subagent brings its own tools, hooks, and sandbox; see Claim 6).

### Claim 2: Extensions are updated by updating the package, not by copying code into the consumer's project — "nothing is copied into the consumer's agent"
- **Evidence**: The docs page's "Consumer: install and mount an extension" section header sentence.
- **Confidence**: settled (first-party, explicit architectural statement)
- **Quote**: "A mount gives the extension's contributions a namespace. Updating the package updates the mounted extension; nothing is copied into the consumer's agent."
- **Our assessment**: This is the load-bearing distinction between an "extension" and a scaffolded starter template or copy-pasted code snippet: the consumer's `agent/extensions/crm.ts` file is a thin mount point (an import plus a config call), and the actual tool/hook/skill implementations live in, and are versioned by, the published `@acme/crm` package. Bumping the extension's version in `package.json` is the entire update mechanism — no diffing or re-copying is implied anywhere in the source.

### Claim 3: A new extension is scaffolded with `npx eve@latest extension init <name>`, which creates the package, installs dependencies, initializes Git, and follows the same file conventions as an agent (`tools/`, `connections/`, `skills/`, `instructions.md`, `hooks/`, plus extension-only `channels/`, `schedules/`, and `subagents/`)
- **Evidence**: The changelog's scaffolding command and file-tree diagram, cross-checked against the docs page's fuller file-tree diagram and its "Create the package" section.
- **Confidence**: settled (first-party, matching command and largely-matching (changelog is a subset of docs) file-tree diagrams across two pages)
- **Quote**: "Start with the extension scaffold: `npx eve@latest extension init my-crm`. The command creates the package, installs dependencies, and initializes Git. It includes `extension/extension.ts`, TypeScript configuration, and the package metadata required to build and publish."
- **Quote (naming rule)**: "Names come from paths, so call the tool `search`, not `crm_search`; the consumer's mount adds the `crm__` prefix."
- **Our assessment**: Reusing the agent's own file-convention vocabulary (`tools/`, `hooks/`, etc.) for extension authoring is a deliberate design choice that means a developer who already knows how to write an eve agent's tools and hooks needs to learn only the mount/namespace/build steps to author an extension — the individual contribution files themselves (a `defineTool` call, a `defineHook` call) are unchanged in form. The one authoring constraint stated is negative: "The extension root cannot declare agent configuration, a sandbox, or nested extensions" — an extension cannot itself depend on another extension.

### Claim 4: An extension declares a typed config schema with any Standard Schema library (Zod shown); consumer settings are validated synchronously on import, and contribution files import the extension's own handle to read already-defaulted, validated config
- **Evidence**: The docs page's "Add configuration and contributions" section, with a two-file `defineExtension`/`defineTool` code example.
- **Confidence**: settled (first-party, code-sample-backed)
- **Quote**: "Give it a [Standard Schema](https://standardschema.dev) when consumers need to provide settings... Contributions, including schedule handlers, can import that handle to read the validated configuration. Defaults have already been applied."
- **Quote (constraint)**: "Config schemas must validate synchronously."
- **Our assessment**: This is a fail-fast design: because the schema validates on import rather than at first tool call, a consumer who forgets a required config key (e.g., `apiKey`) discovers the misconfiguration at agent build/start time, not on the first user turn that happens to trigger the extension's tool — a meaningfully earlier and more diagnosable failure point. `defineState`'s automatic per-extension scoping (stated in the same section) extends the same isolation principle to runtime state, not just config: "the same state name does not collide with the consumer or another extension."

### Claim 5: The consumer's mount filename sets a namespace prefix (`<name>__`) applied uniformly to the extension's tools, channels, schedules, connections, and parent-visible subagent IDs, while channel route paths and schedule cron expressions are left unchanged
- **Evidence**: The docs page's "Mount it" section, enumerating each contribution type's namespaced form.
- **Confidence**: settled (first-party, enumerated per contribution type)
- **Quote**: "The mount adds `crm__` to named contributions: `tools/search.ts` becomes `crm__search`, `channels/webhook.ts` becomes `crm__webhook`, `schedules/sync.ts` becomes `crm__sync`, `connections/api.ts` becomes `crm__api`, and `subagents/reviewer/` becomes `crm__reviewer`. Channels keep their declared route paths, and schedules keep their cron expressions."
- **Quote (per-mount independence)**: "The mount is intentionally per agent. Each consumer chooses its own mount namespace and, for a configured extension, passes its own configuration. For example, `shared.ts` contributes `shared__search`, while mounting the same package as `company.ts` in another agent contributes `company__search`."
- **Our assessment**: The split between "identifier gets namespaced" (tool/channel/schedule/connection/subagent names, which are internal handles the model or runtime resolves) and "external contract stays stable" (route paths, cron expressions, which are addresses an outside system — a webhook sender, a scheduler — depends on) is a sensible boundary: renaming an internal tool identifier from `search` to `crm__search` has no external dependents to break, but changing a webhook's route path on remount would break whatever external service is configured to POST to it. The per-agent mount independence means the same published extension package can be namespaced differently (or configured differently) by two unrelated consuming agents in the same workspace, with no shared state between the two mounts beyond the package version.

### Claim 6: A subagent authored under `extension/subagents/<id>/` is exposed to the consuming agent as `<mount>__<id>`, but its own tools, connections, skills, hooks, instructions, sandbox, and nested subagents stay isolated inside its own node and keep their un-namespaced, path-derived names
- **Evidence**: The docs page's "Add a subagent" section.
- **Confidence**: settled (first-party mechanism description)
- **Quote**: "Author a subagent under `extension/subagents/<id>/` using the same files as a subagent declared by an agent. Mounting the extension as `crm` exposes `extension/subagents/reviewer/` to the consuming agent node as `crm__reviewer`. The subagent's own tools, connections, skills, hooks, instructions, sandbox, and nested subagents remain isolated inside its node and keep their path-derived names."
- **Our assessment**: This is the one place the eight-item Claim 1 list understates the packaging surface: an extension is not limited to shipping flat tools/hooks/skills — it can ship an entire self-contained agent (with its own sandbox) as a delegatable unit, and only that unit's top-level identity is namespaced, not its internals. Combined with the stated restriction that "the extension root cannot declare agent configuration, a sandbox, or nested extensions" (Claim 3), the practical effect is that sandbox-requiring or independently-configured capability sets must be pushed down into a contributed subagent rather than declared at the extension root.

### Claim 7: A consumer can only override, replace, or remove an extension's contribution via a directory mount (`agent/extensions/<name>/` instead of a single file); hooks and instruction fragments are additive and cannot be replaced this way, and `disableTool()` removes a tool of either static or dynamic origin
- **Evidence**: The docs page's "Override a contribution" section, with three code samples (mount-with-override directory layout, a tool redefinition importing the original, and a `disableTool()` call).
- **Confidence**: settled (first-party mechanism description with worked examples)
- **Quote**: "Use a directory mount to replace or remove an extension contribution... A same-named consumer channel, tool, connection, skill, schedule, or subagent wins... Hooks and instruction fragments are additive, so they cannot be replaced. To replace a dynamic tool, use a dynamic definition in the same slot; dynamic tools win over same-named static tools at runtime. `disableTool()` removes either kind."
- **Quote (mount boundary)**: "The `crm__` prefix is reserved for this directory mount. A consumer cannot override the extension from `agent/tools/`, `agent/connections/`, `agent/subagents/`, or another agent-root slot."
- **Our assessment**: The asymmetry here is worth flagging for practitioners: most contribution types (tools, connections, skills, channels, schedules, subagents) can be overridden or removed outright by a same-named file in the override directory, but hooks and static instruction fragments cannot — they only ever add to what the extension already contributes. A consumer who wants to *suppress* an extension's hook-driven side effect (e.g., an audit-log hook that fires on every tool call) has no override mechanism described here; the only lever the source documents for hooks is addition, not removal or replacement.

### Claim 8: `toolResultFrom` narrows an `action.result` stream event to a specific tool's typed output by matching the tool *definition object* imported from the extension's own `./tools` export, not by matching the runtime-namespaced string name
- **Evidence**: The extensions doc's "Use an extension tool result in a hook" section and the fuller `toolResultFrom` explanation on the linked hooks doc page, both showing the same `import { search } from "@acme/crm/tools"` pattern.
- **Confidence**: settled (first-party, cross-confirmed on two independently-fetched pages)
- **Quote (extensions page)**: "`toolResultFrom` recognizes the mounted `crm__search` result from the original definition, not the namespaced string. Publishers should keep tool descriptions distinct so eve can assign each definition an unambiguous identity."
- **Quote (hooks page)**: "This works for a mounted extension's tools too — import the tool from the extension's `./tools` export and pass it. `toolResultFrom` matches the namespaced result (`crm__search`) because it keys off the tool definition, not the name."
- **Our assessment**: Keying identity off the definition object rather than the string name is what makes this pattern remount-safe: a consumer hook written against `toolResultFrom(event.data.result, search)` keeps working even if the consumer later remounts the extension under a different namespace (e.g., `company.ts` instead of `crm.ts`), because the hook never hard-codes the namespaced string `crm__search` anywhere. The stated precondition — "publishers should keep tool descriptions distinct" — is a soft requirement on the extension *author*, not enforced by a type system, so a poorly-authored extension with duplicate tool descriptions could in principle break this disambiguation; the source does not elaborate on what happens if two tools' descriptions collide.

### Claim 9: `eve extension build` compiles author source into a separate, publishable `dist/extension` tree; the extension declares `eve` as a wildcard peer dependency (not a regular dependency) because compatibility is checked via generated metadata at consumption time, not via the npm peer range itself
- **Evidence**: The docs page's "Build and optionally publish" section, including a full annotated `package.json` scaffold and explanatory prose.
- **Confidence**: settled (first-party, code-sample- and prose-backed)
- **Quote**: "`eve extension build` writes an agent-shaped `dist/extension` tree, copies skill assets, emits declarations, and records compatibility metadata... Publish `dist/`; consumers do not need the author's TypeScript source."
- **Quote (peer dependency rationale)**: "The exact `eve` development pin controls the extension authoring API and build tooling. The wildcard peer lets the consumer provide the runtime copy of eve. At consumption time, eve checks generated metadata, not the npm peer range. Do not add eve to regular `dependencies`."
- **Our assessment**: This is a specific, checkable packaging rule with a stated failure mode if violated implicitly: bundling `eve` as a regular dependency (rather than the documented `peerDependencies: { eve: "*" }` plus `devDependencies: { eve: "x.y.z" }` split) would risk shipping a second, potentially conflicting copy of the runtime inside the published package. The "compatibility metadata, not npm peer range" mechanism (elaborated in Claim 10) is the actual enforcement point, which is why the peer entry can safely be a wildcard rather than a version range — the real compatibility gate lives elsewhere.

### Claim 10: A package dependency that must keep its normal Node.js package layout at runtime (e.g., a native addon, or an SDK that loads package-relative assets) must be listed in `eve.extension.externalDependencies`, and `eve extension build` requires that same package to also appear in `dependencies`/`optionalDependencies`/`peerDependencies` or the build step itself enforces the requirement
- **Evidence**: The docs page's `externalDependencies` paragraph, immediately following the `package.json` scaffold that shows the field's literal placement.
- **Confidence**: settled (first-party mechanism description with a stated build-time validation rule)
- **Quote**: "When a package must keep normal Node.js package layout at runtime, add it to `eve.extension.externalDependencies`. Common cases include native addons and SDKs that load package-relative assets. `eve extension build` requires each listed package to also appear in `dependencies`, `optionalDependencies`, or `peerDependencies`, and records the requirement in the generated compatibility manifest. The consuming eve keeps the package external and preserves its complete package tree; consumers do not need to edit `agent.ts` or install the transitive package directly."
- **Our assessment**: Most extension dependencies (the docs page names `zod` or "an SDK" as the common case) are described as being "bundled into the consuming agent automatically" — the default build behavior inlines them. `externalDependencies` is the documented escape hatch for the minority case where bundling would break a package that depends on its own on-disk file layout (a native `.node` binary, package-relative asset loading). The claim that "consumers do not need to edit `agent.ts` or install the transitive package directly" is the practical payoff: the mechanism is designed so this dependency detail is invisible to whoever mounts the extension, not something they must diagnose and work around themselves.

### Claim 11: A workspace extension (an unpublished package co-located in the same monorepo as its consumers) uses the identical package contract as a published extension, and `eve dev` automatically builds and rebuilds source-backed workspace extensions before compiling a consuming agent, watching only the extension's own source and config
- **Evidence**: The docs page's "Use an extension in a workspace" and "Develop from source" subsections, with a full pnpm-workspace file-tree example and two `package.json` snippets.
- **Confidence**: settled (first-party mechanism description with a worked multi-package example)
- **Quote**: "A workspace extension is a regular extension package kept in the same monorepo as its consumers... Give the generated package the name consumers will import. Add `\"private\": true\" if it should never be published."
- **Quote (dev-mode build behavior)**: "When `eve dev` starts a consuming agent, it builds mounted, source-backed extensions found inside the same workspace before compiling the agent. It watches the extension source and relevant package and TypeScript configuration, then rebuilds only the affected extension. If an extension edit fails to build, the previous successful development generation keeps running."
- **Quote (production requirement)**: "Production `eve build` expects the extension distribution to exist already. Keep `eve extension build` in the extension package's `build` and `prepare` scripts, as the scaffold does, and run workspace builds in dependency order so extensions build before their consuming agents."
- **Our assessment**: The stated fallback behavior — "if an extension edit fails to build, the previous successful development generation keeps running" — is a concrete resilience property worth flagging: a broken in-progress edit to a shared workspace extension does not immediately break every agent that mounts it during local development, it keeps serving the last-known-good build until the edit compiles. The production/dev asymmetry (dev builds on the fly; production requires the `dist/` to already exist and depends on correct workspace build ordering) is a real operational detail a team wiring up CI for a workspace with extensions needs to get right, and the source is explicit that `eve build` itself will not build the extension for you in production.

### Claim 12: Ready-made extensions are separately distributed through an "eve integration registry," discoverable and installable with `eve add`, distinct from the author-your-own workflow the rest of the page documents — and the live integrations catalogue lists at least one entry, GitHub Tools, explicitly as adding "scoped GitHub tools with Vercel Connect authentication and approval rules"
- **Evidence**: The extensions doc's opening section pointing to a separate "Add Integrations" page and `eve add` command; corroborated by the linked `eve.dev/integrations` catalogue page, which lists `github-tools` among ~70 named integrations spanning channels, connections, and (per this claim) extensions.
- **Confidence**: emerging (the extensions page states the registry and `eve add` command exist and links out to a separate page for using them, but this note did not fetch that separate "Add Integrations" page itself — see Extraction Notes)
- **Quote**: "Ready-made extensions can also be distributed through an eve integration registry. See [Add Integrations](./install-integrations) to discover and add one with `eve add`; this page explains how extension packages are authored, mounted, configured, and overridden."
- **Quote (catalogue entry)**: "[GitHub Tools](/integrations/github-tools): Add scoped GitHub tools with Vercel Connect authentication and approval rules."
- **Our assessment**: This is the direct link to `blog-vercel-github-tools-eve.md` Claim 8, which documented a `@github-tools/eve-extension` package that, as of that source's 2026-07-07 publication date, was "not yet published to npm." This changelog (published 2026-07-22, fifteen days later) generalizes the packaging primitive that a published `@github-tools/eve-extension` would use, and the `eve.dev/integrations` catalogue (fetched during this extraction, 2026-08-20) now lists a `github-tools` integration entry with extension-style framing ("scoped GitHub tools... approval rules"). This note cannot confirm from the catalogue listing alone whether that entry is specifically the `@github-tools/eve-extension` npm package now publicly published, or a distinct registry entry Vercel maintains independently of that package's npm status — see Extraction Notes.

## Concrete Artifacts

### Extension package scaffold and mount (verbatim, from `eve.dev/docs/extensions`)

```
Source: https://eve.dev/docs/extensions

$ npx eve@latest extension init my-crm

@acme/crm/
  package.json
  extension/
    extension.ts
    tools/search.ts
    channels/webhook.ts
    connections/api.ts
    skills/triage/SKILL.md
    schedules/sync.ts
    subagents/reviewer/agent.ts
    instructions.md
    hooks/audit.ts
    lib/http.ts

// extension/extension.ts
import { defineExtension } from "eve/extension";
import { z } from "zod";

export default defineExtension({
  config: z.object({
    apiKey: z.string(),
    baseUrl: z.string().url().default("https://api.acme.example"),
  }),
});

// extension/tools/search.ts
import { defineTool } from "eve/tools";
import { z } from "zod";
import extension from "../extension";

export default defineTool({
  description: "Search the CRM.",
  inputSchema: z.object({ query: z.string() }),
  async execute({ query }) {
    const { apiKey, baseUrl } = extension.config;
    return { query, baseUrl, authenticated: apiKey.length > 0 };
  },
});

// agent/extensions/crm.ts (consumer mount)
import crm from "@acme/crm";

export default crm({ apiKey: process.env.CRM_API_KEY! });
```

### Publishable `package.json` scaffold (verbatim, from `eve.dev/docs/extensions`)

```
Source: https://eve.dev/docs/extensions

{
  "name": "my-crm",
  "version": "0.0.0",
  "type": "module",
  "eve": {
    "extension": {
      "source": "./extension",
      "dist": "./dist/extension",
      "externalDependencies": ["@acme/runtime-sdk"]
    }
  },
  "files": ["dist"],
  "exports": {
    ".": { "types": "./dist/index.d.ts", "default": "./dist/index.mjs" },
    "./tools": { "types": "./dist/tools/index.d.ts", "default": "./dist/tools/index.mjs" }
  },
  "scripts": {
    "build": "eve extension build",
    "prepare": "eve extension build",
    "typecheck": "tsc"
  },
  "dependencies": { "@acme/runtime-sdk": "^x", "zod": "^x" },
  "devDependencies": { "@types/node": "^x", "eve": "x.y.z", "typescript": "^x" },
  "peerDependencies": { "eve": "*" },
  "engines": { "node": ">=24" }
}
```

### Override and disable a contribution (verbatim, from `eve.dev/docs/extensions`)

```
Source: https://eve.dev/docs/extensions

agent/extensions/crm/
  extension.ts
  tools/search.ts

// agent/extensions/crm/extension.ts
import crm from "@acme/crm";
export default crm({ apiKey: process.env.CRM_API_KEY! });

// agent/extensions/crm/tools/search.ts  (redefine with stricter approval)
import { search } from "@acme/crm/tools";
import { defineTool } from "eve/tools";
import { always } from "eve/tools/approval";

export default defineTool({ ...search, approval: always() });

// agent/extensions/crm/tools/search.ts  (or: remove entirely)
import { disableTool } from "eve/tools";
export default disableTool();
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-github-tools-eve.md`, `blog-vercel-agent-runs-mcp-cli.md`,
`blog-latentspace-vercel-andrew-qu-eve.md`, and
`blog-anthropic-large-codebase-best-practices.md` were re-read (in full, or
via their numbered `### Claim N:` heading list) during this extraction per
MINER.md §4b, and every claim number cited below was located and confirmed
against that note's own numbered claims in document order before writing
this section.

- **Corroborates**:
  - `blog-vercel-agent-runs-mcp-cli.md` Claim 8 ("no instrumentation file
    required... appears automatically for eve projects") and this source's
    Claim 2 (extensions update by updating the package, "nothing is copied
    into the consumer's agent") are two independent instances of the same
    "eve inherits/wires platform capability automatically, minimal explicit
    config" design philosophy already flagged as recurring in that note's
    own Extends section — here applied to dependency/packaging mechanics
    rather than observability.
  - `blog-anthropic-large-codebase-best-practices.md` Claim 5 (Claude Code's
    harness has seven named extension points, including "plugins" as one of
    five primary points, without further elaborating what a plugin bundles):
    both sources independently converge on the idea that a coding-agent
    harness benefits from a single, installable, namespaced unit that
    bundles several lower-level extension mechanisms (tools, hooks, skills)
    together rather than requiring each to be configured separately — Claude
    Code names this unit a "plugin," eve names it an "extension." That prior
    note does not describe what a Claude Code plugin technically bundles or
    how it is namespaced/overridden, so this source cannot be checked against
    it at the mechanism level (mount namespacing, `disableTool()`,
    `toolResultFrom` definition-identity matching) — only at the
    architectural-pattern level of "bundled, installable capability packages
    as a named harness concept."

- **Contradicts**: None identified as a MINER.md §4a contradiction. No claim
  in this source opposes any existing corpus note.

- **Extends**:
  - `blog-vercel-github-tools-eve.md` Claim 8 (the eve extension form of
    GitHub Tools, `@github-tools/eve-extension`, was "not yet published to
    npm" as of that source's 2026-07-07 publication, with the direct
    `@github-tools/sdk/eve` import documented as the stable path in the
    meantime): this source (published 2026-07-22) is the general-purpose
    extension packaging system that a published `@github-tools/eve-extension`
    would be built on. This note's Claim 12 found a `github-tools` entry in
    the live `eve.dev/integrations` catalogue as of this extraction
    (2026-08-20) but could not confirm from that listing alone whether it
    represents the specific npm-published extension package that earlier
    note flagged as pending — a future source note reading
    `eve.dev/integrations/github-tools` directly would be the place to
    confirm or update that status.
  - `blog-vercel-agent-runs-mcp-cli.md` Claim 6 (`get_agent_run_trace`'s
    `maxFieldLength` parameter truncates a tool's own return payload before
    it re-enters a calling agent's context) and this source's Claim 8
    (`toolResultFrom` narrows a tool result to a typed, definition-matched
    object for a hook to consume): both sources document mechanisms for
    handling a tool's `action.result` payload precisely, but for different
    purposes — that note's mechanism budgets payload *size* against the
    model's context window; this source's mechanism narrows payload *type*
    and *identity* for a hook's own (non-model) consumption. Together they
    describe two independent axes eve provides for working with tool-result
    data downstream of the tool call itself.

- **Novel**:
  - **A single distributable package that can bundle a full sub-agent,
    including its own sandbox, as one of several contribution types**
    (Claim 6): no prior corpus source documents a coding-agent extension/plugin
    mechanism where the distributable unit can itself contain a nested,
    independently-sandboxed agent, distinguishable from every other
    contribution type in the same package by being namespaced only at its
    top level while its own internals stay unnamespaced.
  - **Result-narrowing keyed to a tool's definition object rather than its
    runtime (namespaced) string name, explicitly justified as remount-safety**
    (Claim 8): no prior corpus source documents a hook/observability
    mechanism designed specifically so that renaming an extension's mount
    namespace does not require rewriting code that inspects that
    extension's tool results.
  - **A documented, asymmetric override model where most contribution types
    can be replaced or disabled by the consumer but hooks and static
    instructions cannot** (Claim 7): no prior corpus source documents a
    plugin/extension system that explicitly withholds an override mechanism
    for a subset of its own contribution types (here, hooks and instruction
    fragments are additive-only) while allowing it for the rest (tools,
    connections, skills, channels, schedules, subagents).
  - **A build-time compatibility gate based on generated metadata rather
    than the npm peer-dependency range itself** (Claim 9): no prior corpus
    source documents a packaging system that intentionally uses a wildcard
    peer-dependency declaration (`"eve": "*"`) precisely because the real
    version-compatibility enforcement happens through a separate,
    build-generated manifest instead.

## Guide Impact

- **Chapter 05 (Agent Architecture & Design) or wherever harness
  extension-point taxonomies are covered**: Add eve's extension packaging
  primitive (Claim 1's eight contribution types; Claims 3-6's authoring,
  namespacing, and subagent-bundling mechanics) as a second, structurally
  different named example of "bundle several lower-level extension
  mechanisms into one installable unit," alongside
  `blog-anthropic-large-codebase-best-practices.md` Claim 5's Claude Code
  "plugin" concept — flag explicitly that the corpus does not yet have a
  claim-level description of what a Claude Code plugin technically bundles,
  so the two cannot be compared mechanism-for-mechanism yet, only at the
  level of "both frameworks converged on a bundled/installable capability
  unit as a named harness concept."

- **Chapter 06 (Patterns & Integration)**: Add Claim 7's override model
  (directory-mount replacement for tools/connections/skills/channels/schedules/subagents,
  but hooks and static instructions are additive-only) as a concrete,
  checkable example of a composition pattern's limits — a team adopting a
  third-party extension whose hook has an unwanted side effect has no
  documented way to suppress that specific hook short of not mounting the
  extension at all, which is a design trade-off worth surfacing wherever the
  guide discusses adopting third-party agent capability packages.

- **Chapter 04 (Context Engineering) or wherever tool-result handling
  patterns are covered**: Add Claim 8's `toolResultFrom` definition-identity
  matching as a second, remount-safety-motivated instance of typed
  tool-result narrowing, distinguishable from
  `blog-vercel-agent-runs-mcp-cli.md` Claim 6's `maxFieldLength` payload-size
  truncation — the two are complementary tool-result-handling mechanisms
  (type/identity narrowing vs. size truncation) documented in the same
  vendor ecosystem, worth presenting together if the guide builds out a
  "handling tool results downstream of the call" section.

## Extraction Notes

1. **Raw markdown fetched via content negotiation, not WebFetch
   summarization.** All five pages in this source family (the changelog and
   the four `eve.dev` docs/integrations pages) support an `Accept:
   text/markdown` request that returns clean, already-de-HTML'd markdown.
   An initial WebFetch pass on the changelog alone returned a shortened,
   reworded paraphrase (its "Core Content Summary" section did not preserve
   the changelog's own sentence boundaries or bold lead-ins). Per MINER.md
   §2a, every `Quote` field in this note was instead located
   character-for-character in the markdown captures fetched directly via
   `curl -H "Accept: text/markdown"` before being used here.
2. **Four linked pages followed per MINER.md §1**: `eve.dev/docs/extensions`
   (read in full — supplied nearly every claim in this note), `eve.dev/docs/tools`
   (read in full — corroborating detail for Claim 7's `disableTool()`/`approval`
   mechanics and confirming `toModelOutput`/approval vocabulary used
   consistently with the extensions page), `eve.dev/docs/guides/hooks` (read
   in full — supplied the fuller `toolResultFrom` explanation used in Claim
   8, plus general hook-execution-order and failure-handling context not
   otherwise cited in this note), and `eve.dev/integrations` (read in full —
   supplied Claim 12's catalogue-entry evidence). A fifth candidate,
   `eve.dev/install-integrations` (linked from the extensions page as "Add
   Integrations," the page that documents `eve add` and the integration
   registry itself), was **not** fetched — this note's Claim 12 is rated
   "emerging" specifically because that page was not read, and its content
   (how `eve add` selects/installs a registry extension, whether registry
   entries are always npm-published extension packages or can be a distinct
   mechanism) is unverified here. `eve.dev/docs/subagents` and
   `eve.dev/docs/channels/overview`, both cross-linked from the extensions
   page's own "What to read next" list, were judged out of scope: the
   extensions page's own subagent- and channel-specific prose (Claim 6;
   Claim 5's route-path/cron stability) already states everything
   extension-specific about those two contribution types, and the general
   subagent/channel mechanics pages would only restate non-extension-specific
   behavior already out of this note's scope.
3. **Claim 12's registry status left unresolved by design.** This note
   deliberately does not assert whether the `github-tools` entry now visible
   in `eve.dev/integrations` corresponds to the specific
   `@github-tools/eve-extension` npm package `blog-vercel-github-tools-eve.md`
   Claim 8 described as unpublished on 2026-07-07. Confirming that would
   require fetching `eve.dev/integrations/github-tools` directly and,
   ideally, checking npm for the package's publication status — both out of
   scope for a note anchored to this general-extensions changelog rather
   than to the GitHub Tools integration specifically.
4. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts.
5. **Confidence calibration: emerging.** Individual claims are rated
   "settled" (except Claim 12) because they are first-party, unambiguous
   mechanism descriptions cross-checked across up to three independently-fetched
   pages that agree everywhere they overlap, several with full worked code
   examples. The note's overall confidence is "emerging" rather than
   "settled" because: (a) this is a single vendor's own changelog and
   documentation with no independent verification, benchmark, or named
   production customer anywhere in the source family; (b) the feature is
   four weeks old as of this extraction (published 2026-07-22) with no
   GA/beta status label found anywhere in the five pages read; and (c) at
   least one claim (12) rests on an unfetched page and is explicitly flagged
   as such rather than asserted with full confidence.
