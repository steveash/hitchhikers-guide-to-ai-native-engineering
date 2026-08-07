---
source_url: https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/
source_type: blog-post
title: "Agent Plugins package your skills, tools, and more"
author: Kevin Hou (Senior Staff Engineer, Google DeepMind), Haoyu Wang (Staff Software Engineer, Google Cloud Data), Alan Blount (Technical Product Manager, Google Cloud AI)
date_published: 2026-08-06
date_extracted: 2026-08-07
last_checked: 2026-08-07
status: current
confidence_overall: emerging
issue: "#2549"
---

# Agent Plugins Package Your Skills, Tools, and More

> Google's first-party announcement that it is joining Agent Plugins 1.0.0 —
> a vendor-neutral, RFC-2119-normative directory-and-manifest specification
> for packaging Agent Skills and MCP servers into portable plugins, already
> backed by Amazon, Cursor, Microsoft, OpenAI, and Vercel — as a Core
> Maintainer, with two Google products (Agents CLI, Data Agent Kit) already
> shipping conformant plugins.

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party
  standards-adoption announcement, August 6, 2026), cross-checked against
  the specification's own normative text at agent-plugins.org/specification
  (a linked primary source, not independent of Google since Google is now a
  Core Maintainer, but authoritative for the spec's actual requirements).
- **Author credibility**: Three named Google engineers/PMs (Kevin Hou,
  Senior Staff Engineer, Google DeepMind — named in the post as the
  individual representing Google on the Technical Steering Committee;
  Haoyu Wang, Staff Software Engineer, Google Cloud Data; Alan Blount,
  Technical Product Manager, Google Cloud AI) writing on Google's own
  official developer blog about a standard Google is joining as a governing
  member, not merely observing. This is first-party vendor content
  announcing a governance and product-adoption decision — not independent
  practitioner evaluation. The underlying specification is a public,
  versioned document with RFC 2119 conformance language, which makes the
  technical claims about the format independently checkable against the
  spec text itself (done for this note; see Extraction Notes).
- **Scope**: Covers what an Agent Plugin is (directory + manifest), the
  problem it solves (client-specific wrapper drift), what the v1 spec
  deliberately excludes (install, distribution, permissions, sandboxing,
  trust, UX), how it composes with three adjacent, independently-adoptable
  layers (Agentic Resource Discovery for finding plugins, AI Catalog for
  describing them, MCP/Agent Skills for running their contents), and two
  shipping Google implementations (Agents CLI, Data Agent Kit). Does
  **not** cover: performance data, adoption numbers, a security/trust
  model (explicitly deferred), or a rendered list of all compatible
  clients (the linked `agent-plugins.org/compatible-clients` page renders
  its client list via a client-side JavaScript component not present in
  static HTML — see Extraction Notes). To fill in the mechanics the blog
  post only sketches, this note also extracts the specification's own
  normative text (`agent-plugins.org/specification`, Spec Version 1.0.0,
  Status: Working Draft), which documents the closed manifest schema, the
  MCP transport variants, the `${PLUGIN_ROOT}`/`${PLUGIN_DATA}` placeholder
  system, and the spec's own "Design Decisions" rationale section in far
  more concrete, falsifiable detail than the announcement post.

## Extracted Claims

### Claim 1: Agent Plugins 1.0.0 is an open, vendor-neutral specification for packaging Agent Skills and MCP servers into portable plugins, published by a Technical Steering Committee of Core Maintainers from Amazon, Cursor, Microsoft, OpenAI, and Vercel, with Google now joining as a Core Maintainer represented by Kevin Hou
- **Evidence**: First-party statement in the post's opening section, naming the governing body and its member organizations.
- **Confidence**: settled (a direct, falsifiable statement about the spec's governance structure — corroborated by the spec's own "Governance model" section, which points to a separate Technical Charter document, and the spec text confirms a versioned, publicly hosted normative document exists)
- **Quote**: "is an open, vendor-neutral specification for packaging Agent Skills and MCP servers into portable plugins. It was published by a TSC of Core Maintainers from Amazon, Cursor, Microsoft, OpenAI, and Vercel. Google is joining that group as a Core Maintainer, represented by Kevin Hou, and we're starting to build support into our own products."
- **Our assessment**: This is the corpus's first documentation of a plugin-packaging standard with six major agent/IDE vendors as governing co-maintainers (five prior plus Google). That breadth of buy-in is itself the most significant fact in the post — it is a stronger signal than any single vendor's format because switching cost for a plugin author drops only if enough clients actually implement it. We cannot independently verify from this post alone how many of the five prior maintainers have shipped conformant clients (the blog's "Shipping Today" section only names Google's own two products); this claim should be read as a governance/backing fact, not an adoption-breadth fact.

### Claim 2: The problem Agent Plugins solves is not the portability of individual components (skills, MCP servers), which were already portable, but the non-portability of the "wrapper" around them — directory layout, manifest metadata shape, and MCP configuration shape differ per client, forcing authors to fork and maintain drifting duplicate packages
- **Evidence**: First-party problem statement, using a concrete illustrative scenario (a reporting-database skill plus its MCP server) to motivate the spec.
- **Confidence**: settled (a direct statement of the design rationale, corroborated by the specification's own "Design Decisions" section, "Why an explicit MCP configuration format?", which states the same problem independently: "Existing clients use incompatible MCP configuration shapes and infer transports differently.")
- **Quote**: "The skill is fine. The MCP server is fine. But the wrapper around them is not: the directory layout is different, the manifest wants different top-level metadata, the MCP configuration uses a different shape and infers transports differently. So you fork the package, maintain two copies of components that were never different in the first place, and watch them drift."
- **Our assessment**: This is a precise diagnosis worth preserving verbatim for the guide: the portability gap is specifically at the packaging layer, not the execution layer (MCP, Agent Skills already had portable execution contracts). The post summarizes this in one line elsewhere in the same section: "The core problem isn't the components. It's the manifest." That framing is the kind of specific, falsifiable claim that's more useful to a practitioner than a generic standardization-is-good statement.

### Claim 3: A plugin is defined as nothing more than a directory with a manifest whose only required substance is two fields — `$schema` and `name`; the specification's own text confirms the manifest's top-level schema is closed to exactly ten permitted fields
- **Evidence**: Blog post minimal-manifest example plus the specification's own normative "Manifest object" section (§5.2), which enumerates the closed field list.
- **Confidence**: settled (the blog's minimal example and the specification's normative field list agree, and the spec text is independently checkable — this is not a vendor characterization but a quotable requirement)
- **Quote**: "A plugin is a directory. That's the whole idea, and the restraint is the point." (blog post) / "The manifest MUST be JSON and MUST contain a top-level object. Its schema is closed: the only permitted top-level fields are `$schema`, `name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, and `extensions`." (specification, §5.2)
- **Our assessment**: The closed-schema design (as opposed to an open/extensible top-level object) is a deliberate anti-sprawl choice, and the spec's own "Design Decisions" section states why: "Restricting root `plugin.json` to known fields enables strict validation, typo detection, and schema-driven key completion. Client experiments cannot claim arbitrary top-level fields; they are contained under reverse-domain keys in extensions." This is a reusable design principle beyond this specific spec: keep the portable core's schema closed and route all client-specific extensibility through a namespaced escape hatch rather than an open top-level object.

### Claim 4: Fixed component locations (`skills/`, `mcp.json`) mean a client never has to guess where a component lives or in what order to check multiple possible locations, and missing or failing components fail independently rather than taking down the whole plugin
- **Evidence**: Blog post description plus specification normative text: "If a fixed component location is absent, the client MUST NOT treat that as an error" (§6) and a per-component-type failure isolation rule enumerated in the spec's containment-failure table.
- **Confidence**: settled (both the blog's plain-language description and the spec's RFC-2119 normative requirements state the same behavior)
- **Quote**: "Notice what `plugin.json` cannot do. It cannot relocate components, and it cannot declare them inline. There is no discovery path to configure and no precedence order to learn. If `skills/` isn't there, the client loads what is there and moves on. A `mcp.json` server that fails to start doesn't take the plugin's skills down with it — the client skips that entry, keeps loading, and reports the failure. Independent components fail independently."
- **Our assessment**: This "independent components fail independently" property is a concrete, checkable resilience property distinct from a merely aspirational goal — the specification's own Design Decisions section explains the rationale: "A plugin that provides skills and an MCP server should not become entirely unusable because one server is unavailable. The spec pairs non-fatal component failures with diagnostic requirements so that failures are visible rather than silent." This directly parallels the graceful, visible-degradation-over-silent-failure pattern already documented elsewhere in the corpus (see Cross-References) but applied specifically to plugin component loading rather than to agent-pipeline execution.

### Claim 5: MCP servers declared in a plugin's `mcp.json` must carry an explicit `type` field selecting one of three closed transport variants (`stdio`, `streamable-http`, `sse`), eliminating the need for a client to infer transport from the shape of a config object
- **Evidence**: Blog post description plus specification normative text defining the three closed server-configuration variants and their required/optional fields (e.g., `stdio` requires `type` and `command`, with optional `args`, `env`, `cwd`).
- **Confidence**: settled (directly reproducible from the public specification text: "Each server configuration MUST contain a `type` field and match exactly one of the closed variants below. An unknown field, an unknown `type` value, or a field belonging to another variant makes that server entry invalid.")
- **Quote**: "MCP servers are declared in `mcp.json`, with an explicit type on every entry. A client never has to guess a transport from the shape of a config object, it will work on stdio, Streamable HTTP, or legacy HTTP+SSE."
- **Our assessment**: This is a specific, low-level design fix for a stated real problem (per the spec's own Design Decisions: "Existing clients use incompatible MCP configuration shapes and infer transports differently"). It is a concrete, actionable detail for anyone currently maintaining per-client MCP configs by hand, and it names "legacy HTTP+SSE" explicitly as a still-supported (not yet dropped) transport alongside the newer Streamable HTTP.

### Claim 6: Client-specific customization is confined to reverse-domain-namespaced directories and manifest keys (e.g., `com.example.client/`) that are an "escape hatch" — owned entirely by one client, ignored by clients that don't recognize them — keeping the portable core small
- **Evidence**: Blog post description plus specification normative text requiring clients to "MUST ignore manifest entries for namespaces it does not implement without validating the contents of their values," and the Design Decisions rationale for reverse-domain naming.
- **Confidence**: settled (a direct mechanism description matching the spec's normative requirement)
- **Quote**: "That last reverse-domain directory is the escape hatch. `com.example.client/` is an extension namespace owned entirely by one client, for hooks, agents, commands, or anything else that client wants to add. Clients that don't recognize it ignore it. The portable core stays small because the non-portable parts have somewhere legitimate to go."
- **Our assessment**: The reverse-domain convention (borrowed from Java package naming / Android manifest conventions) is notable because it solves namespace-collision avoidance without a central registry — the spec's Design Decisions section states this explicitly: "Reverse-domain identifiers provide a decentralized convention for avoiding collisions without requiring a central client-name registry." This is the mechanism by which the spec can stay genuinely vendor-neutral at the core while still letting Claude Code, Cursor, or any other client bundle hooks, commands, or agent definitions that only that client understands — directly relevant to any guide discussion of multi-client plugin/skill authoring.

### Claim 7: The spec explicitly advises against using a plugin for a single MCP server targeting a single client, or for a single skill — a bare `mcp.json` or a standalone skill directory is the simpler answer in those cases, and "Agent Plugins earns its keep when you have components that belong together and need to travel together"
- **Evidence**: Blog post section titled "Not Every skill should be a Plugin."
- **Confidence**: settled (a direct statement of scope/applicability guidance from the spec's own authors and adopters)
- **Quote**: "Before you reach for a plugin, ask whether you need one. If you're shipping a single MCP server to a single client, `mcp.json` on its own is still the simpler answer. If you have a single skill, you don't need a plugin. Agent Plugins earns its keep when you have components that belong together and need to travel together."
- **Our assessment**: This is a useful, self-limiting scoping statement from a vendor announcing a new standard — most standards-announcement posts do not proactively tell readers when *not* to adopt the standard. This is directly actionable guidance for a practitioner deciding packaging granularity: don't wrap a single MCP server or single skill in plugin scaffolding just because the format exists; reach for it only when multiple components need to move together as a unit.

### Claim 8: Agent Plugins v1 deliberately defines no install mechanism, no distribution protocol, no permission model, no sandboxing requirements, and no trust or provenance verification, and no user experience — these are named openly in the project's "future considerations" document rather than silently omitted, because installation, policy, and approval UX are legitimately different across an IDE, a CLI, and a managed enterprise platform
- **Evidence**: Blog post section "What It Deliberately Leaves Out," with an explicit link to a `FUTURE_CONSIDERATIONS.md` document in the spec's GitHub repository.
- **Confidence**: settled (a direct, falsifiable statement of scope; the spec's own Design Decisions section corroborates the "why only Agent Skills and MCP in v1" reasoning: "Other proposed component types — such as commands, hooks, agents, rules, and LSP servers — remain too client-specific for a stable portable contract and are outside the v1 format until their formats converge")
- **Quote**: "Agent Plugins v1 is a package format and nothing more. It defines no install mechanism, no distribution protocol, no permission model, no sandboxing requirements, no trust or provenance verification, and no user experience. Those are named openly in the project's future considerations, not quietly omitted." / "This is the right call. Installation, policy, enterprise controls, and approval UX are quite different across clients like an IDE, a CLI, and a managed enterprise platform. Each agentic application has genuinely different obligations to their users."
- **Our assessment**: This is the single most important scoping caveat for any guide section citing this spec as a governance or security mechanism: Agent Plugins standardizes *packaging*, not *trust*. A plugin conforming to this spec carries no built-in guarantee about what its skills or MCP servers actually do, no signature/provenance verification, and no sandboxing — those remain entirely the responsibility of whichever client installs it (e.g., a `.github-private/`-style enterprise governance layer, or a client's own approval UX). This directly bears on `docs-github-copilot-enterprise-managed-plugins-vscode.md`'s enterprise plugin-governance claims — see Cross-References.

### Claim 9: The Agent Plugins ecosystem is explicitly layered into four independently-adoptable pieces — discovery (Agentic Resource Discovery, an open protocol treating a Plugin as a first-class discoverable resource type), description (AI Catalog, an entry format with a proposed `application/agent-plugins+json` media type), packaging (Agent Plugins itself), and execution (the pre-existing MCP and Agent Skills contracts) — and adopting one layer never obligates adopting another
- **Evidence**: Blog post section "Plugins are part of an ecosystem," which names each layer with a one-line verb-first label ("Find it," "Describe it," "Package it," "Run it").
- **Confidence**: emerging (the layering model and independence claim are stated as design intent by the same vendor group defining all four layers; no independent third party is cited confirming that ARD or the AI Catalog media-type proposal are actually implemented anywhere yet, so the "independently adoptable" claim is architecturally plausible but not yet demonstrated in practice by this post)
- **Quote**: "Find it — Agentic Resource Discovery. An open discovery protocol that lets a client ask "what is available for this task?" and get back matching resources. ARD already treats a Plugin as a first-class agentic resource type, alongside agents, MCP servers, and Skills. It sits entirely before invocation." / "Each layer is independently useful and independently adoptable. You can publish a plugin with no catalog entry, catalog a resource that isn't a plugin, and run skills with no plugin at all. Adopting one never obligates you to the next."
- **Our assessment**: This four-layer separation (discover / describe / package / run) is a useful mental model for the guide's tool-composition chapters, distinct from treating the plugin ecosystem as one monolithic thing. However, we should flag that this is the vendor's own architectural narrative for how its own newly-announced pieces fit together, not a third-party assessment of whether the layers are actually decoupled in practice — worth citing as a framework, not as a proven interoperability result.

### Claim 10: Two Google products already conform to the Agent Plugins format as of the post's publication — Agents CLI (packaging Google's own agent-building/eval/deployment/observability skills for use across Antigravity, Gemini CLI, Claude Code, and Cursor) and Data Agent Kit (plugins connecting agents to BigQuery, Spanner, Cloud SQL, and other Google Cloud data services)
- **Evidence**: Blog post section "Shipping Today," naming both products and linking to their respective repositories/guides (`google.github.io/agents-cli/guide/getting-started/` and `github.com/GoogleCloudPlatform/data-agent-kit`).
- **Confidence**: settled (a direct, falsifiable statement of what has shipped, with linked, publicly inspectable artifacts — this note did not clone or execute either repository, so the claim is verified only to the level of "the linked resources exist and are named as conformant," not to the level of independently validating conformance against the spec's schema)
- **Quote**: "Agents CLI packages Google's expert skills for agent building, evaluation, deployment, observability, and publishing, turning any AI coding agent — Antigravity, Gemini CLI, Claude Code, or Cursor — into an expert at agent building and agent ops. Those skills were already distributable. Now they're distributable in a format that isn't ours alone." / "By adopting the Agent Plugins standard, the Data Agent Kit ensures that its rich set of agentic skills and MCP servers—connecting to BigQuery, Spanner, Cloud SQL, and more—are portably available across any compatible client."
- **Our assessment**: This is the concrete adoption evidence that elevates the announcement above a pure standards proposal — two real, named, linked products are cited as already conformant. Notably, Agents CLI's stated target-client list (Antigravity, Gemini CLI, Claude Code, Cursor) spans four separate vendors' tools, which is a direct practical illustration of the one-package-multiple-clients value proposition the whole post argues for.

### Claim 11: A minimal, valid Agent Plugin can be created in about a minute — a directory, a `plugin.json` with just a name, and a one-line "hello world" instruction file at `skills/greet/SKILL.md`
- **Evidence**: Blog post "Get Started with Agent Plugins" section.
- **Confidence**: settled (a directly reproducible, falsifiable claim about minimum effort to produce a spec-conformant artifact — a reader can attempt this and check the result against the spec's manifest requirements in Claim 3)
- **Quote**: "Build one. Create a directory, add a `plugin.json` with a name, write a quick "hello world" instruction to `skills/greet/SKILL.md.` That's a valid plugin, and it takes about a minute."
- **Our assessment**: This is a good concrete onboarding data point for the guide — a time-to-first-working-artifact claim that a practitioner can verify directly rather than an abstract ease-of-use assertion.

### Claim 12: The Agent Plugins specification's own published normative text (agent-plugins.org/specification, Spec Version 1.0.0) is currently labeled "Status: Working Draft," even though both the blog post and the spec's own version number describe it as "1.0.0"
- **Evidence**: Direct observation from fetching the specification page itself, which displays "Spec Version: 1.0.0" immediately followed by "Status: Working Draft" in its header metadata.
- **Confidence**: settled (a directly observed fact about the spec document's current self-declared status, independent of the blog post's framing)
- **Quote**: "Spec Version: 1.0.0" / "Status: Working Draft"
- **Our assessment**: This is a maturity caveat the blog post itself does not mention — the announcement's framing ("Agent Plugins 1.0.0 is an open, vendor-neutral specification") reads as describing a finished, stable v1.0 release, while the specification site's own status field says the document is still a working draft. This is not a factual contradiction (a document can be versioned 1.0.0 and still be a working draft of that version — the two fields describe different axes, version identity vs. review/ratification status), but it is a nuance worth flagging for the guide: cite this as an actively-evolving specification, not a finalized, frozen standard, and re-check the status field before treating any specific normative requirement as durable.

## Concrete Artifacts

### Minimal plugin manifest (verbatim, blog post)
```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "reports-plugin"
}
```
Source: developers.googleblog.com, "What an Agent Plugin Actually Is" section.

### Standard plugin directory layout (verbatim, blog post)
```
reports-plugin/
├── plugin.json
├── skills/
│   └── summarize/
│       ├── SKILL.md
│       ├── scripts/
│       └── references/
├── mcp.json
└── com.example.client/
```
Source: developers.googleblog.com, "What an Agent Plugin Actually Is" section.

### Expanded standard layout with a client extension directory (verbatim, specification §4.2)
```
my-plugin/
├── plugin.json
├── skills/
│   └── summarize/
│       ├── SKILL.md
│       ├── scripts/
│       │   └── analyze.sh
│       └── references/
│           └── checklist.md
├── mcp.json
├── com.example.client/
│   └── hooks/
├── LICENSE
└── CHANGELOG.md
```
Source: agent-plugins.org/specification, §4.2 "Standard layout."

### Closed manifest field list (verbatim requirement, specification §5.2)
```
The only permitted top-level fields are $schema, name, version,
description, author, homepage, repository, license, keywords, and
extensions.

Any schema violation other than an unknown top-level field or a
non-object `extensions` field is fatal: the client MUST reject the
plugin and MUST NOT discover or execute any of its components.
```
Source: agent-plugins.org/specification, §5.2 "Manifest object."

### MCP server transport variants and required/optional fields (specification §7.2, stdio variant shown)
```
type    "stdio"           Yes   Selects the MCP stdio transport.
command string            Yes   Executable token to launch.
args    string[]          No    Arguments passed to the executable.
env     object of strings No    Environment variables supplied to the process.
cwd     string            No    Working directory for the process.

"Each server configuration MUST contain a type field and match exactly
one of the closed variants below. An unknown field, an unknown type
value, or a field belonging to another variant makes that server entry
invalid."
```
Source: agent-plugins.org/specification, §7.2.2 (stdio field table and closed-variant requirement).

### Placeholder expansion variables for MCP server configs (specification, "Why plugin variables over relative paths in configs?")
```
${PLUGIN_ROOT}   — client-resolved absolute path to the plugin root,
                   for bundled files.
${PLUGIN_DATA}   — client-managed, writable state directory that
                   persists across package updates.

Supported only in `args`, `env` values, and `cwd` — not in `command`
or fixed component locations. Expansion is a single, non-recursive
textual replacement of every exact occurrence of either placeholder.
```
Source: agent-plugins.org/specification, §9 (Environment variables and
placeholder expansion) and Design Decisions, "Why plugin variables over
relative paths in configs?"

### Design Decisions rationale excerpts (verbatim, specification, non-normative "Design Decisions" section)
```
Why directory-based discovery?
"Plugins use filesystem directories as the package unit rather than
archive formats (.zip, .tar.gz) or registry-fetched bundles. This
keeps plugins inspectable with standard tools (ls, cat, git), editable
in-place during development, and compatible with version control
without special tooling."

Why component failures are non-fatal
"A plugin that provides skills and an MCP server should not become
entirely unusable because one server is unavailable. The spec pairs
non-fatal component failures with diagnostic requirements so that
failures are visible rather than silent."

Why only Agent Skills and MCP in v1?
"Other proposed component types — such as commands, hooks, agents,
rules, and LSP servers — remain too client-specific for a stable
portable contract and are outside the v1 format until their formats
converge."
```
Source: agent-plugins.org/specification, "Design Decisions" section
(explicitly marked non-normative — "context only," per the spec's own
§2 conformance-language note).

## Cross-References

- **Corroborates**:
  - `blog-google-conductor-plugin-antigravity.md` (Claim 1: Conductor
    "evolving from a Gemini CLI extension into the Conductor Plugin.
    Plugins can include skills, rules, MCP servers, and hooks in a
    single package"): this note's Claim 8 explains *why* Conductor's
    plugin bundle can include "rules" and "hooks" even though this
    spec's v1 format only standardizes `skills/` and `mcp.json` —
    per this note's Design Decisions excerpt, "commands, hooks, agents,
    rules... remain too client-specific for a stable portable contract
    and are outside the v1 format," meaning Conductor's rules/hooks
    almost certainly live in a client-specific reverse-domain extension
    directory (this note's Claim 6) rather than the portable core, not
    in a first-class portable component type. This is a useful
    clarification the Conductor note itself does not make, since it
    predates this spec's public documentation being mined.
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` (Claim 5:
    enterprises can define "hooks and MCP configurations that are always
    enabled across your enterprise" via `.github-private/.github/copilot/settings.json`):
    this note's Claim 8 (Agent Plugins v1 explicitly excludes any
    permission model, sandboxing, or trust verification, deferring
    those entirely to individual clients) explains the gap that
    GitHub's enterprise-managed settings mechanism is filling at the
    client level — the portable plugin format intentionally has no
    opinion on enforcement, so a client-specific governance layer like
    `.github-private/` is exactly the kind of client-owned concern this
    spec anticipates and defers, not a competing or overlapping
    standard.

- **Contradicts**: None filed. The "1.0.0" version label vs. "Working
  Draft" status juxtaposition (this note's Claim 12) was considered but
  is a maturity/status nuance about a single source's own internal
  labeling, not a disagreement between two sources or a claim that would
  change guide advice in opposing directions — see MINER.md §4a's
  "conditioning variable" / non-contradiction guidance. Flagged
  prominently in Claim 12 and Extraction Notes instead.

- **Extends**:
  - `blog-google-conductor-plugin-antigravity.md`: that note documents
    one concrete, shipped plugin (Conductor) built before this spec's
    governance and normative text were mined into the corpus. This note
    supplies the actual portability contract (closed manifest schema,
    fixed component locations, reverse-domain extension namespaces) that
    a plugin like Conductor must conform to at its portable core, giving
    the corpus, for the first time, the underlying standard rather than
    only a single vendor's example implementation of "a plugin."
  - `blog-google-adk-a2a-contract-compliance.md` and
    `blog-anthropic-multi-agent-coordination-patterns.md`: both existing
    notes document protocols/contracts for portability and coordination
    at the *agent-to-agent* or *agent-to-service* level (A2A, MCP
    execution). This note adds the *packaging* layer immediately below
    those execution contracts — Agent Skills and MCP servers were
    already portable at runtime (per this note's Claim 2, "Both are
    portable on their own"); what was missing, and what this spec adds,
    is a portable way to bundle and ship them together.

- **Novel**:
  - **A six-vendor-governed (Amazon, Cursor, Microsoft, OpenAI, Vercel,
    now Google), RFC-2119-normative plugin packaging specification** with
    a publicly readable conformance document (Claims 1, 3-6, 8): no
    prior corpus source documents a cross-vendor governance body for
    agent tooling packaging with this level of named institutional
    backing and a formal normative-language spec text.
  - **A closed top-level manifest schema paired with a reverse-domain
    extension escape hatch** (Claims 3, 6): this specific design
    pattern — closed core schema + namespaced extension directories for
    client-specific data — is new to the corpus as a named, documented
    convention with an explicit stated rationale (avoiding a central
    client-name registry while still preventing top-level schema
    sprawl).
  - **An explicit vendor statement of what a plugin standard should
    *not* try to solve** (Claim 8: no install mechanism, no
    distribution, no permissions, no sandboxing, no trust verification,
    no UX) is a notably restrained scoping statement; most standards
    announcements in the corpus emphasize what a new spec adds, not what
    it deliberately excludes and why.
  - **A four-layer "find / describe / package / run" ecosystem model**
    (Claim 9) for agent tooling discovery-through-execution is new
    framing language not previously present in the corpus.

## Guide Impact

- **Chapter 04 (MCP and Tool Orchestration)**: add a new subsection on
  Agent Plugins as the emerging packaging layer above MCP — cite Claim 2
  (the portability gap is at the wrapper/manifest layer, not the
  execution layer, since MCP and Agent Skills were "already portable on
  their own") and Claim 5 (the closed three-variant `mcp.json` transport
  format eliminates client-specific transport inference). Frame this as:
  "if you are currently maintaining separate MCP configs or skill
  wrappers per client (Claude Code, Cursor, an IDE), Agent Plugins is the
  standard six major vendors are now converging on to eliminate that
  duplication — but note it is still a Working Draft (Claim 12) and
  explicitly does not cover installation, trust, or permissions (Claim
  8)." This is new content, not an update to an existing recommendation,
  since no current guide section documents a cross-client plugin
  packaging standard.

- **Chapter 06 (Agent Skills)**: add Claim 7 (the spec's own guidance
  that a single skill or single-client MCP server does not need plugin
  packaging — only bundles of components that must travel together do)
  as a concrete decision rule for when to wrap a skill in a plugin versus
  distributing it standalone. This directly informs any "how do I
  package and ship this skill" guidance the chapter gives.

- **Chapter 02 (AI-Native Development Fundamentals)**: if this chapter
  discusses standardization/interoperability trends across agent
  vendors, cite Claim 1 (the six-vendor TSC governance structure) and
  Claim 10 (two concrete shipping Google implementations, one of which —
  Agents CLI — explicitly targets four separate vendors' clients:
  Antigravity, Gemini CLI, Claude Code, Cursor) as the most concrete
  evidence yet in the corpus of competing agent vendors converging on a
  shared packaging format rather than each maintaining incompatible
  proprietary plugin systems.

- **Security/Threat-model discussion (wherever the guide covers
  plugin/extension trust)**: prominently cite Claim 8 — Agent Plugins v1
  provides zero built-in trust, provenance, sandboxing, or permission
  guarantees. Any guide text that might imply "a conformant Agent Plugin
  is vetted" needs the explicit caveat that conformance is purely a
  packaging-format claim, and that a plugin author, marketplace, or
  client-side approval mechanism (e.g., the enterprise governance layer
  in `docs-github-copilot-enterprise-managed-plugins-vscode.md`) is doing
  all of the actual trust work.

## Extraction Notes

- Read the blog post via two independent extraction methods: (1) the
  WebFetch tool's small-model summarizer for an initial overview pass,
  and (2) a direct `curl` fetch of the raw HTML (stripped to plain text
  with a Python regex script), used to verify every `Quote` field above
  character-for-character against the source's own wording before use.
  All quotes above are taken from the raw-fetched plain text, not the
  summarizer output. One character-level detail confirmed directly in
  the raw HTML bytes: the sentence "If you have a single skill, you
  don't need a plugin" uses a Unicode curly apostrophe (U+2019) in the
  source's own markup, inconsistent with the straight-apostrophe HTML
  entities (`&#x27;`) used everywhere else on the page — reproduced
  here exactly as it appears in the source, not normalized.
- Followed two linked resources beyond the blog post itself, both judged
  substantive per MINER.md's "follow up to 5 linked pages" guidance,
  since the blog post gives almost no normative detail and nearly all of
  the format's actual technical requirements live in the specification
  document itself:
  1. `agent-plugins.org/specification` (Spec Version 1.0.0) — fetched
     both via WebFetch's summarizer and via a direct `curl` + Python
     HTML-to-text conversion, with every `Quote` field above drawn from
     and verified against the raw-converted plain text (`/tmp/spec.txt`
     during extraction), not the summarizer's paraphrase. This is the
     primary source for Claims 3-9 and 12, and for the Concrete
     Artifacts beyond the two blog-post examples.
  2. `agent-plugins.org/compatible-clients` — attempted but the page
     renders its actual client list via a client-side JavaScript
     component (`<CompatibleClients />`) not present in the static
     HTML/WebFetch-accessible content. No compatible-clients list could
     be extracted from this page; this note does not claim a specific
     client count or list beyond the two Google products the blog post
     names directly (Claim 10). A future mining pass with a
     JavaScript-rendering fetch method could recover this list if judged
     valuable.
  Did not follow `github.com/agentplugins/agent-plugins-spec/blob/main/FUTURE_CONSIDERATIONS.md`
  (linked from the blog's "What It Deliberately Leaves Out" section) —
  the blog post and specification's own Design Decisions section already
  cover the same v1-exclusion rationale (Claim 8) in sufficient depth;
  judged as likely duplicative rather than substantively new.
- The specification page's own header metadata reads "Spec Version:
  1.0.0" immediately followed by "Status: Working Draft" — extracted
  directly and prominently as Claim 12, since it is a maturity signal
  the announcement post itself does not surface and that the Assayer/
  Smith should consider before treating any specific normative
  requirement extracted here as a stable, unlikely-to-change contract.
- No contradiction issue filed per MINER.md §4a: the "1.0.0" vs.
  "Working Draft" juxtaposition (Claim 12) is a single source's own
  internal status labeling, not a disagreement between two sources or
  within the source about a factual claim — it does not meet the bar for
  a filed contradiction, but is flagged prominently per the "conditioning
  variable"/nuance-not-contradiction handling used elsewhere in the
  corpus (e.g., `blog-google-conductor-plugin-antigravity.md`'s
  Extraction Notes).
