---
source_url: https://vercel.com/changelog/discover-and-install-eve-integrations-from-the-cli
source_type: blog-post
title: "Discover and install eve integrations from the CLI"
author: Colton Padden, Ben Pankow, Owen Kephart, with contributor Ben Sabic (Vercel)
date_published: 2026-07-29
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: emerging
issue: "#3002"
---

# Discover and install eve integrations from the CLI

> Vercel changelog announcing `eve add`/`eve registry` CLI commands for
> discovering and installing eve integrations from the official catalog,
> skills.sh, or any shadcn-format third-party registry — plus, via the
> linked first-party `eve.dev/docs/install-integrations` page (the exact
> page an earlier corpus note flagged as unread), the full mechanics of
> per-integration-type file placement, multi-component item selection,
> interactive vs. `--non-interactive` (NDJSON, exit-code) setup flows, and
> how to host a compatible third-party registry.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`; a
  short feature announcement — one intro paragraph, four bulleted/coded
  sections covering installation, discovery, third-party registries, and
  security). Per MINER.md §1, the changelog's own single linked documentation
  page, `eve.dev/docs/install-integrations`, was followed and read in full —
  it is a substantially longer, mechanism-level reference (11 sections,
  including a full `registry.json` schema example and a setup-automation
  exit-code table) that supplies most of this note's claims. The changelog's
  other two links, `eve.dev/integrations` (the catalog directory) and
  `eve.dev` itself, were not re-fetched: the former was already fetched in
  full for `blog-vercel-eve-extensions.md` (2026-08-20, five weeks before
  this extraction) and its catalog-listing content is not specific to the
  CLI mechanics this issue was triaged for; the latter is a general
  marketing/template landing page unrelated to this feature.
- **Author credibility**: First-party Vercel product-team announcement,
  credited to three named authors (Colton Padden, Ben Pankow, Owen Kephart)
  and one named contributor (Ben Sabic) in the changelog's byline. The linked
  `eve.dev/docs/install-integrations` page carries no separate byline
  (standard product documentation) but is consistent with the changelog
  everywhere the two overlap. No customer quotes, adoption metrics, or
  independent benchmarks appear anywhere in the source or the linked page —
  this is first-party documentation of a shipping feature, not third-party
  reporting or validation.
- **Scope**: Covers the `eve add`/`eve registry` CLI commands themselves —
  installation syntax, discovery (`list`/`search`/`view`), per-integration-type
  file placement, multi-component items, interactive and `--non-interactive`
  setup-flow automation, skills.sh integration via the built-in `@skills`
  source, third-party registry configuration and self-hosting, and the
  update/`--overwrite` mechanism. Does **not** cover: pricing, a GA/beta
  status label for the feature (none found in either page read), the
  contents of the official catalog itself beyond the two named examples
  (`agent-browser`, `linear`) used to illustrate CLI mechanics, or
  independent production usage evidence — every example given is a
  vendor-authored illustration, not a documented customer deployment.

## Extracted Claims

### Claim 1: `eve add` installs a named integration from the official eve catalog or a third-party source directly into the current eve project, using a `<type>/<name>` identifier (e.g. `extension/agent-browser`, `channel/slack`, `connection/vercel`, `instrumentation/braintrust`), and writes the integration's files directly into the project
- **Evidence**: The changelog's opening two sentences and installation code block; corroborated by the linked docs page's own "Install an integration" section using the same identifier pattern.
- **Confidence**: settled (first-party, unambiguous, matching command syntax and prose across both pages)
- **Quote**: "You can now discover and install integrations for [eve](https://eve.dev/) agents directly from the eve CLI. Integrations come from the official eve catalog and third-party sources."
- **Quote (write behavior)**: "Integrations write their files directly into your project and can add anything an eve agent uses, from a single tool to a channel to a full extension. Review the generated files and add any required configuration before running your agent."
- **Our assessment**: The `<type>/<name>` identifier namespace (`extension/`, `channel/`, `connection/`, `instrumentation/`) is itself informative: it tells a practitioner up front which of eve's four documented integration surfaces a given catalog item will land in, before installing anything. This is a scaffolding/codegen pattern — not a runtime dependency-resolution one — consistent with the changelog's explicit instruction to "review the generated files," i.e. the CLI writes editable source into the project rather than pulling in an opaque package that only exposes a config object.

### Claim 2: Three `eve registry` subcommands support catalog discovery before installing anything — `list` (browse all available items), `search <term>` (find by capability), and `view <name>` (inspect an item's details pre-install)
- **Evidence**: The changelog's discovery bullet list, matching the docs page's "Find an integration" section commands.
- **Confidence**: settled (first-party, identical command names and stated purposes across both pages)
- **Quote**: "`eve registry list`: List available integrations. `eve registry search <term>`: Search the catalog for a capability, like `browser`. `eve registry view <name>`: Inspect an integration before you install it."
- **Our assessment**: Pairing an install command (`eve add`) with a dedicated pre-install inspection command (`eve registry view`) is the same "preview before you pull it into your project" discipline the changelog's own Security Considerations section (Claim 5) later states as an explicit recommendation — the discovery commands are not just a UX convenience, they are the mechanism the security guidance assumes a cautious practitioner will use.

### Claim 3: When `eve add` is given an item name that does not exist in any configured catalog, it searches the available catalogs and prints close matches — without installing anything
- **Evidence**: A standalone sentence in the docs page's "Install an integration" section, not present anywhere in the changelog itself.
- **Confidence**: settled (first-party, specific failure-mode description)
- **Quote**: "If an item is not found, `eve add` searches the available catalogs and prints close matches without installing anything."
- **Our assessment**: This is a concrete, checkable safety property of the command's failure mode: a typo'd or misremembered item name does not silently no-op or fail with a bare "not found" error — it degrades gracefully into a fuzzy-match suggestion, and critically, performs no filesystem writes in that path. The changelog's own headline framing ("discover integrations from the CLI") omits this fallback-search behavior entirely; a practitioner relying on the changelog alone would not know `eve add` doubles as an unnamed-arg search when a name is missing.

### Claim 4: Some catalog items bundle multiple independently installable components — `eve add linear` prompts a choice between the Linear Channel, Linear MCP, or both (both selected by default) — while the narrower, single-component identifiers for the same components remain directly usable
- **Evidence**: The docs page's "Install an integration" section, giving `linear` as the named worked example.
- **Confidence**: settled (first-party, specific worked example with named default behavior)
- **Quote**: "Some integrations package several independently installable components. For example, `eve add linear` lets you choose the Linear Channel, Linear MCP, or both; both are selected by default. The specific `eve add channel/linear-agent` and `eve add connection/linear` commands remain available."
- **Our assessment**: The default-to-both behavior is a deliberate "give people the complete integration unless they ask for less" bias, but the source is explicit that the narrower identifiers stay available as an escape hatch — a team that wants only the MCP connection without the Slack-style channel is not forced into installing (and then having to manually strip out) the bundled default. This is the multi-component analogue of Claim 1's `<type>/<name>` namespace: the composite name (`linear`) groups components that also each have their own addressable, narrower identity.

### Claim 5: Integration files land in type-specific, fixed project locations — extensions may mount under `agent/extensions/`, connections write under `agent/connections/` (installing `@vercel/connect` when required), and instrumentation providers write the single file `agent/instrumentation.ts`, requiring hand-composition when more than one instrumentation provider is installed
- **Evidence**: The docs page's "Install an integration" section, stating each type's target path and the instrumentation single-file constraint explicitly.
- **Confidence**: settled (first-party mechanism description, specific and checkable per integration type)
- **Quote**: "Extensions may create a mount under `agent/extensions/`. Connections write their initial definition under `agent/connections/` and install `@vercel/connect` when required. Instrumentation providers write `agent/instrumentation.ts`; because an agent has one instrumentation file, compose multiple exporters there by hand."
- **Our assessment**: The instrumentation constraint is the sharpest edge here: unlike extensions or connections (which can be installed repeatedly into their own distinct files/mounts), a second `eve add instrumentation/<other-provider>` after a first does not compose automatically — the source states in plain terms that the developer must manually edit `agent/instrumentation.ts` to merge exporters, since eve's own auto-discovery mechanism (documented in `blog-vercel-agent-runs-mcp-cli.md` Claim 10 as "eve auto-discovers `agent/instrumentation.ts` and runs it at server startup") only looks for that one file. A team installing two observability-provider integrations back to back would get the second one's generated file silently overwriting or conflicting with the first's unless they read this constraint first.

### Claim 6: When an official catalog item declares one or more interactive setup flows, `eve add` asks whether to run them after installation, runs multiple flows in declaration order, and a printed `eve add <item> --skip-install` command lets the developer resume a skipped or cancelled setup later — rerunning the selected components' flows from the beginning
- **Evidence**: The docs page's "Install an integration" section, describing the setup-flow prompt and resume mechanism.
- **Confidence**: settled (first-party mechanism description)
- **Quote**: "When an official item declares an interactive setup flow or flows, eve asks whether to run them after installation and runs multiple flows in declaration order. Run the printed `eve add <item> --skip-install` command to resume a skipped or cancelled setup later; it reruns the selected components' declared flows from the beginning."
- **Our assessment**: "Reruns... from the beginning" (not from the point of cancellation) is a specific, non-obvious behavior worth flagging: a developer who cancels partway through a multi-question setup flow and later resumes with `--skip-install` does not get to pick up where they left off — every declared flow question is asked again. This matters most for setup flows with several sequential questions, where an accidental early cancellation costs the full re-answer, not just the remaining steps.

### Claim 7: `eve add <item> --non-interactive` is explicitly designed for scripts or coding agents that cannot answer terminal prompts — it prints NDJSON events and exits 0 (completed), 1 (failed), or 2 (needs an answer or unmet prerequisite); on exit 2 the caller reads the final event and runs its `next.command`, substituting a collected answer for non-secret questions, while secrets must go through an environment variable or secret store rather than the `--answer` flag, and `--yes` accepts recommended values (explicit answers still take precedence)
- **Evidence**: The docs page's dedicated "Automate setup" section, including the full three-row exit-code table.
- **Confidence**: settled (first-party, specific and checkable automation-interface contract)
- **Quote**: "Use `eve add <item> --non-interactive` when a script or coding agent cannot answer terminal prompts. It prints NDJSON events and exits with a status you can branch on"
- **Quote (exit codes)**: "`0` | Installation and setup completed. `1` | Installation or setup failed. `2` | Setup needs an answer or an unmet prerequisite."
- **Quote (secrets rule)**: "On exit code `2`, read the final event and run its `next.command`. For a non-secret question, replace its `<JSON value>` placeholder with the answer you collected. Never pass a secret in `--answer`; use the environment variable or secret store the integration documents. Add `--yes` to accept recommended values; explicit answers take precedence."
- **Our assessment**: This is a purpose-built agent-automation contract, not a generic `--json`-flag afterthought — the branchable three-way exit code (done / failed / needs-input) combined with a machine-readable `next.command` to run on exit 2 gives a calling script or agent a deterministic loop it can drive without parsing free-form terminal output. The explicit "never pass a secret in `--answer`" rule is a self-imposed safety constraint on the automation surface itself: the design anticipates that an agent scripting this flow might otherwise be tempted to pass a collected API key straight through the same `--answer` mechanism used for ordinary answers, and closes that path by name.

### Claim 8: A setup flow may report `eve link` (linking the local project to a Vercel project) as an unmet prerequisite, which the developer must run before retrying the setup continuation
- **Evidence**: A single sentence in the docs page's "Automate setup" section, immediately following the exit-code table and secrets guidance.
- **Confidence**: settled (first-party, narrow but specific mechanism description)
- **Quote**: "A setup may report `eve link` as a prerequisite. Run it, then retry the continuation."
- **Our assessment**: This connects the exit-code-2 "unmet prerequisite" case (Claim 7) to a concrete, named example of what such a prerequisite looks like in practice — a project that has not yet been linked to a Vercel project cannot complete certain integration setups (implicitly, ones that need to read or write Vercel project configuration, such as connections using Vercel Connect). The source does not enumerate which integration types specifically require linking, only that this is the pattern when they do.

### Claim 9: `eve registry search` additionally searches skills.sh (via a built-in `@skills` source), and a known skills.sh item can be installed directly with `eve add @skills/<org>/<repo>/<skill-name>` — skills.sh items are described as "community-authored project files" that should be reviewed before running the agent
- **Evidence**: The docs page's "Find an integration" and dedicated "Add a skill" sections, with a full worked identifier example.
- **Confidence**: settled (first-party, specific worked example and explicit trust caveat)
- **Quote**: "`list` includes the official eve catalog and every source you add to the project. `search` also includes [skills.sh](https://skills.sh), available as the built-in `@skills` source."
- **Quote (worked example)**: "`eve add @skills/vercel-labs/agent-skills/vercel-react-best-practices`"
- **Quote (trust caveat)**: "Skills from skills.sh are community-authored project files. Review their source and the resulting diff before you run your agent."
- **Our assessment**: This is the direct mechanism-level confirmation of skills.sh's role that `blog-latentspace-vercel-andrew-qu-eve.md` Claim 1 named only biographically (Andrew Qu "created skills.sh") without describing how it plugs into `eve` at all — here, skills.sh is not a separate product a developer visits manually, it is wired directly into `eve`'s own registry search and install path as a pre-configured `@skills` namespace, on equal footing with the official catalog and any third-party registry the developer adds. The explicit "community-authored... review before you run" caveat is notably stronger/more specific trust language than the general Security Considerations wording applied to the official catalog and named third-party sources (Claim 5's parallel "official catalog" framing has no equivalent caveat).

### Claim 10: A third-party registry is added with a namespace and URL template (`eve registry add @acme=https://registry.acme.com/r/{name}.json`, stored in `package.json#registries`), after which `eve add @acme/<name>` resolves `{name}` and installs; alternatively, a single known integration URL can be installed directly with no namespace configured at all
- **Evidence**: The changelog's "Third-party registry configuration" section and the docs page's matching "Add a third-party source" section, both giving the identical command forms.
- **Confidence**: settled (first-party, matching command syntax and stated storage location across both pages)
- **Quote (changelog)**: "Add third-party sources with a namespace and URL template... Then install from that source with `eve add @acme/analytics`. Registries use the [shadcn registry format](https://ui.shadcn.com/docs/registry), so any compatible registry works."
- **Quote (storage location, docs page)**: "eve stores the mapping in `package.json#registries`. The `{name}` placeholder becomes the integration name, so `@acme/analytics` resolves to `https://registry.acme.com/r/analytics.json`."
- **Quote (direct-URL path)**: "You can also pass an integration URL directly without configuring a source: `eve add https://registry.acme.com/r/analytics.json`"
- **Our assessment**: The two install paths (namespaced source vs. bare URL) trade off persistence against one-off convenience: registering a namespace via `eve registry add` is a one-time, project-committed (`package.json`) step that then makes every future item from that source addressable as a short `@acme/<name>`, while the direct-URL form is stateless and leaves no persistent record in the project of where that one integration came from — a team standardizing on a shared internal registry would want the namespaced form specifically so the mapping is visible and reviewable in version control, not scattered across ad hoc URLs in shell history.

### Claim 11: Building a compatible third-party registry means implementing two endpoint kinds of the standard shadcn registry format — a catalog JSON document and one JSON document per integration — where each item uses `registry:item`/`registry:file` types with explicit file targets specifically so installation does not depend on a UI framework or shadcn project aliases; the registry is validated and built into static JSON with the shadcn CLI itself
- **Evidence**: The docs page's "Host your own registry" section, including a full `registry.json` schema example and the validate/build commands.
- **Confidence**: settled (first-party mechanism description with a complete worked schema example)
- **Quote (endpoint kinds)**: "It needs two kinds of endpoint: A catalog such as `https://registry.acme.com/r/registry.json` for `eve registry list` and `eve registry search`. One JSON document per integration, such as `https://registry.acme.com/r/analytics.json`, for `eve registry view` and `eve add`"
- **Quote (target-path rule)**: "`files[].path` is relative to `registry.json`. `files[].target` is relative to the root of the eve project that installs the item. Use `registry:item` with explicit `registry:file` targets for eve integrations so installation does not depend on a UI framework or shadcn project aliases."
- **Quote (build commands)**: "`pnpm dlx shadcn@latest registry validate`" / "`pnpm dlx shadcn@latest build`" — "By default, the build writes the catalog to `public/r/registry.json` and each item to `public/r/<name>.json`. Deploy the `public` directory to a static host, or use the shadcn registry APIs to serve the same payloads from dynamic routes."
- **Our assessment**: This is the reuse half of a build-vs-reuse decision already visible in Claim 1/10: rather than eve defining and maintaining its own registry protocol, it adopted an existing, already-tooled specification (shadcn's registry format, plus the shadcn CLI's own `validate`/`build` commands) wholesale, and the one eve-specific deviation called out — explicit `registry:file` targets instead of shadcn's own UI-component/alias conventions — is scoped narrowly to the one place the two use cases genuinely diverge (installing files into an arbitrary project structure vs. installing UI components into a conventional one). A team that already knows the shadcn registry format from the frontend-component world can host an eve integration registry with no new protocol to learn, only this one targeting convention to apply.

### Claim 12: Generated integration files are explicitly "project code" a developer is expected to edit and commit, not a managed dependency — re-running `eve add <item>` applies a publisher's updated scaffold, but only overwrites an already-generated file when `--overwrite` is explicitly passed
- **Evidence**: The docs page's "Update an installed integration" section.
- **Confidence**: settled (first-party mechanism description, explicit default-safe behavior)
- **Quote**: "Treat generated files as project code. Commit or review local changes before you install the integration again... Run the same command when the registry publisher provides an updated scaffold: `eve add extension/agent-browser`... Pass `--overwrite` only when you intend to replace an existing generated file: `eve add extension/agent-browser --overwrite`. Update the installed package with your package manager. Check the publisher's release notes before changing the generated mount or package version."
- **Our assessment**: This is the direct opposite update model from the extension-packaging mechanism `blog-vercel-eve-extensions.md` Claim 2 documents for authored extensions ("nothing is copied into the consumer's agent... updating the package updates the mounted extension") — see Cross-References → Contradicts-adjacent note below. For a catalog-installed integration specifically, the generated files are a one-time scaffold the developer is expected to have since edited, so eve defaults to *not* clobbering local changes on a repeat `eve add`, requiring the explicit `--overwrite` flag to accept that risk. A developer who has customized a generated `agent/extensions/<name>.ts` file and later runs `eve add <same-item>` expecting an update, without `--overwrite`, would see no file change at all — the source does not state what feedback (if any) the command prints in that no-op case.

## Concrete Artifacts

### CLI installation examples (verbatim, from the changelog)

```
Source: https://vercel.com/changelog/discover-and-install-eve-integrations-from-the-cli

eve add extension/agent-browser
eve add channel/slack
eve add connection/vercel
eve add instrumentation/braintrust
```

### `--non-interactive` exit-code table (verbatim, from `eve.dev/docs/install-integrations`)

```
Source: https://eve.dev/docs/install-integrations

Exit code | Meaning
0         | Installation and setup completed.
1         | Installation or setup failed.
2         | Setup needs an answer or an unmet prerequisite.
```

### Third-party registry schema example (verbatim, from `eve.dev/docs/install-integrations`)

```
Source: https://eve.dev/docs/install-integrations

registry.json
registry/
└── analytics.ts

// registry.json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://registry.acme.com",
  "items": [
    {
      "name": "analytics",
      "type": "registry:item",
      "title": "Acme Analytics",
      "description": "Add Acme analytics tools to an eve agent.",
      "dependencies": ["@acme/eve-analytics"],
      "envVars": {
        "ACME_API_KEY": ""
      },
      "files": [
        {
          "path": "registry/analytics.ts",
          "type": "registry:file",
          "target": "agent/extensions/analytics.ts"
        }
      ]
    }
  ]
}

$ pnpm dlx shadcn@latest registry validate
$ pnpm dlx shadcn@latest build
```

### Registry discovery and third-party-source commands (verbatim, from `eve.dev/docs/install-integrations`)

```
Source: https://eve.dev/docs/install-integrations

eve registry list
eve registry search browser --limit 5
eve registry view extension/agent-browser
eve add @skills/vercel-labs/agent-skills/vercel-react-best-practices
eve registry add @acme=https://registry.acme.com/r/{name}.json
eve add @acme/analytics
eve add https://registry.acme.com/r/analytics.json
eve registry list --registry @acme
eve registry search analytics --registry @acme
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-eve-extensions.md`, `blog-vercel-github-tools-eve.md`,
`blog-vercel-agent-runs-mcp-cli.md`, and
`blog-latentspace-vercel-andrew-qu-eve.md` were re-read in full (including
their numbered `### Claim N:` heading lists) during this extraction per
MINER.md §4b, and every claim number cited below was located and confirmed
against that note's own numbered claims in document order before writing
this section.

- **Corroborates**:
  - `blog-vercel-agent-runs-mcp-cli.md` Claim 4 ("Every CLI subcommand
    supports `--json` for machine-readable output... so coding agents
    without MCP access can call the CLI directly to debug their own runs"):
    this source's Claim 7 (`--non-interactive`'s NDJSON output and branchable
    exit codes, explicitly "for scripts or coding agents that cannot answer
    terminal prompts") is a second, independent instance of the same
    "design the CLI's own output/interaction contract around a coding agent
    as a first-class consumer, not only a human terminal user" pattern —
    here applied to an interactive multi-step setup flow rather than a
    read-only data query, which is a harder automation problem (branching on
    a needs-input state, not just formatting a result).
  - `blog-latentspace-vercel-andrew-qu-eve.md` Claim 8 (Andrew Qu: "We value
    partners that provide specialized parts of the agent lifecycle... while
    making it easy to integrate with partners rather than owning every
    component"): this source's third-party registry mechanism (Claim 10) and
    self-hosting instructions (Claim 11) are the concrete technical
    implementation of that stated "easy to integrate with partners"
    strategy — any team or vendor can publish an eve-installable integration
    without Vercel curating or hosting it, using an existing open
    specification (shadcn's registry format) rather than a bespoke one.

- **Contradicts-adjacent (not filed as a MINER.md §4a contradiction)**:
  This source's Claim 12 (catalog-installed integration files are
  developer-owned "project code"; a repeat `eve add` does not overwrite
  local edits unless `--overwrite` is passed) describes an update model that
  is the functional opposite of `blog-vercel-eve-extensions.md` Claim 2
  (an authored extension's consumer mount is "a thin mount point... updating
  the package updates the mounted extension; nothing is copied into the
  consumer's agent"). This is **not** filed as a contradiction under
  MINER.md §4a because the two claims describe two different, non-competing
  eve mechanisms rather than disagreeing about the same one: Claim 12 here
  covers `eve add`-installed *catalog integrations* (files generated once,
  then owned and edited locally), while the extensions-note claim covers
  *authored extension packages* mounted via a versioned npm dependency (files
  never copied in at all). A single catalog item could in principle be
  distributed as either an installable scaffold or a mountable extension
  package, and this source's own Claim 1 lists "extension" as one of four
  `eve add` identifier types — meaning at least some catalog items *are*
  extensions, installed via the copy-and-own model this note documents, which
  sits alongside (not in place of) the separate authored-extension mount
  model the other note documents for extensions consumed directly as a
  package dependency rather than through `eve add`. Readers of both notes
  should not assume "installing an extension via `eve add`" and "mounting an
  extension package directly" have identical update semantics — this source
  does not state whether an `eve add`-installed extension's generated mount
  file, once edited, can later be converted to track package updates the way
  a manually-authored mount does.

- **Extends**:
  - `blog-vercel-eve-extensions.md` Claim 12 (that note's one lower-confidence
    "emerging" claim — the eve integration registry and `eve add` command
    exist and are documented on a separate "Add Integrations" page, which
    that note explicitly did not fetch): **this source is that missing
    page**, read in full. It resolves the gap that note flagged: `eve add`
    installs from the official catalog, skills.sh, or any third-party
    shadcn-format registry (Claims 1, 9, 10 here), with specific,
    previously-undocumented mechanics for multi-component items (Claim 4),
    per-type file placement (Claim 5), interactive and automated setup flows
    (Claims 6-8), and the update/`--overwrite` model (Claim 12). This note
    does not resolve that note's separate, still-open sub-question of
    whether the `github-tools` entry in `eve.dev/integrations` corresponds
    to the specific `@github-tools/eve-extension` npm package
    `blog-vercel-github-tools-eve.md` Claim 8 described as unpublished as of
    2026-07-07 — this source's worked examples (`agent-browser`, `linear`,
    `braintrust`) do not include `github-tools`, so that status remains
    unconfirmed.
  - `blog-latentspace-vercel-andrew-qu-eve.md` Claim 1 (Andrew Qu "created
    skills.sh" — stated only as a biographical fact, with no description of
    how skills.sh relates to `eve` mechanically): this source's Claim 9
    supplies that missing mechanism — skills.sh is wired directly into
    `eve`'s own `registry search`/`add` commands as a built-in `@skills`
    namespace, not a separate product a developer must visit and integrate
    by hand.

- **Novel**:
  - **A `--non-interactive` CLI setup flow with NDJSON events, a
    three-way branchable exit code, and a machine-readable `next.command`
    continuation for an interactive multi-step installer, explicitly
    targeted at coding agents that cannot answer terminal prompts** (Claim
    7): no prior corpus source documents a CLI *installer* (as opposed to a
    read-only query tool) designed with this level of automation
    granularity — most agent-facing CLI design in the corpus so far
    (`blog-vercel-agent-runs-mcp-cli.md` Claim 4) covers read/query output
    formatting, not driving a multi-step, potentially-prerequisite-blocked
    setup wizard programmatically.
  - **An explicit rule against passing secrets through a generic CLI
    `--answer` flag, directing them to an environment variable or secret
    store instead** (Claim 7): no prior corpus source documents this specific
    class of self-imposed CLI-automation safety constraint — anticipating
    that an agent or script driving an interactive setup flow via
    `--non-interactive` might otherwise pass a credential through the same
    generic answer-passing mechanism used for ordinary configuration values.
  - **A single-file instrumentation-composition constraint stated as a
    deliberate limitation of an auto-discovery mechanism** (Claim 5): no
    prior corpus source documents an integration-installation system where a
    specific integration type (instrumentation) is capped at one generated
    file by the framework's own auto-discovery design, requiring manual
    hand-composition the moment a second integration of that type is added.
  - **Adopting an existing, externally-specified package-registry format
    (shadcn's) wholesale for a coding-agent framework's own integration
    distribution, rather than defining a bespoke one** (Claim 11): no prior
    corpus source documents an agent-framework vendor explicitly reusing a
    frontend-tooling ecosystem's registry specification and CLI (`shadcn`)
    as the distribution mechanism for agent capabilities, rather than
    building new registry tooling from scratch.

## Guide Impact

- **Chapter 02 (Harness Engineering) — installable capability distribution**:
  Add this source's `eve add`/`eve registry` mechanics (Claims 1-5, 9-12) as
  a second, CLI-first layer on top of the extension-packaging primitive
  `blog-vercel-eve-extensions.md` already documents — specifically, note that
  eve now has *two* distinct ways a capability reaches a project
  (`eve add`'s copy-and-own scaffold vs. an authored extension's
  versioned-package mount, see Cross-References → Contradicts-adjacent), and
  a guide section on harness extension-point taxonomies should distinguish
  which update-semantics model applies before recommending either.

- **Chapter 02 (Harness Engineering) — designing CLIs for agent consumption**:
  Add Claim 7's `--non-interactive`/NDJSON/exit-code/`next.command` pattern
  as a concrete, more advanced example than
  `blog-vercel-agent-runs-mcp-cli.md` Claim 4's `--json` output flag — this
  source documents automating a stateful, potentially multi-step,
  prerequisite-blocked *installer* flow for a coding-agent caller, not just
  formatting a read-only query's result. Recommend citing Claim 7's
  never-pass-secrets-via-`--answer` rule specifically wherever the guide
  discusses designing tool/CLI interfaces that an agent itself will drive.

- **Chapter 06 (Security Threat Model) or wherever third-party capability
  adoption is covered**: Add Claim 9's differentiated trust language — the
  skills.sh `@skills` source is explicitly called "community-authored" with
  an instruction to "review their source and the resulting diff," language
  not applied with the same explicitness to the official catalog or a
  self-added third-party registry namespace elsewhere in this source — as a
  concrete example of a vendor signaling a *different* trust tier for one
  built-in source than for its own first-party catalog, worth surfacing
  wherever the guide discusses evaluating third-party or community-sourced
  agent capabilities before installation.

## Extraction Notes

1. **Raw markdown fetched via content negotiation, not WebFetch
   summarization.** Both pages in this source family (the changelog and
   `eve.dev/docs/install-integrations`) support an `Accept: text/markdown`
   request that returns clean, already-de-HTML'd markdown, consistent with
   the pattern noted in `blog-vercel-eve-extensions.md`'s and
   `blog-vercel-github-tools-eve.md`'s Extraction Notes for the same
   `eve.dev`/`vercel.com` site family. Every `Quote` field in this note was
   located character-for-character in the markdown captured via `curl -H
   "Accept: text/markdown"` before being used here, per MINER.md §2a.
2. **One linked page followed per MINER.md §1**: `eve.dev/docs/install-integrations`
   was read in full — it is the exact page `blog-vercel-eve-extensions.md`
   Claim 12 explicitly flagged as unfetched five weeks prior, and supplied
   nearly every claim in this note (Claims 3-12). The changelog's other two
   links (`eve.dev/integrations`, the catalog directory; and `eve.dev`
   itself) were not re-fetched — the former was already read in full for
   `blog-vercel-eve-extensions.md` and its content (a catalog listing) is not
   specific to this issue's CLI-mechanics triage question, and the latter is
   a general marketing/template landing page unrelated to this feature.
   `eve.dev/docs/extensions` (cross-linked from the install-integrations
   page's own "What to read next" list) was not re-fetched — it was already
   read in full for `blog-vercel-eve-extensions.md` and this note's Claim 1
   already cross-references its extension-mount model directly.
3. **`eve.dev/integrations` catalog was not re-checked for a `github-tools`
   entry.** `blog-vercel-eve-extensions.md`'s Extraction Notes left open
   whether a `github-tools` entry visible in that catalog on 2026-08-20
   corresponds to the specific `@github-tools/eve-extension` npm package
   `blog-vercel-github-tools-eve.md` Claim 8 described as unpublished on
   2026-07-07. This note's worked examples do not include `github-tools`, so
   that status remains unconfirmed; a future source note reading
   `eve.dev/integrations/github-tools` directly (or checking npm) would be
   the place to resolve it.
4. **No contradiction issues filed.** No claim in this source directly
   opposes an existing corpus note on the same mechanism; see Cross-References
   → Contradicts-adjacent for the one place two notes describe different,
   non-competing eve mechanisms that a reader could otherwise conflate.
5. **Confidence calibration: emerging.** Individual claims are rated
   "settled" because they are first-party, unambiguous mechanism
   descriptions cross-checked across two independently-fetched pages
   (changelog and docs) that agree everywhere they overlap, several with
   full worked command sequences or a complete schema example. The note's
   overall confidence is "emerging" rather than "settled" because: (a) this
   is a single vendor's own changelog and documentation with no independent
   verification, benchmark, or named production customer anywhere in the
   source family; (b) the feature is one month old as of this extraction
   (published 2026-07-29) with no GA/beta status label found in either page
   read; and (c) at least one open cross-corpus question (the `github-tools`
   catalog-entry/npm-package correspondence, Extraction Note 3) remains
   unresolved by this note.
