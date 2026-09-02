---
source_url: https://github.github.com/gh-aw/blog/2026-09-01-sandbox-runtime-profiles/
source_type: blog-post
title: "Sandbox Security Options Are Now Runtime Profiles"
author: Copilot and Peli de Halleux (GitHub Agentic Workflows team / GitHub Next / Microsoft Research)
date_published: 2026-09-01
date_extracted: 2026-09-02
last_checked: 2026-09-02
status: current
confidence_overall: settled
issue: "#3159"
---

# Sandbox Security Options Are Now Runtime Profiles

> Breaking-change announcement: gh-aw removes `sandbox.agent.legacy-security`
> and `sandbox.agent.sudo` and replaces them with explicit named
> `sandbox.agent.runtime` profiles (`docker`, `docker-sudo-iptables`,
> `gvisor`, `docker-sbx`, `cloud-hypervisor`), each an explicit
> security-and-topology choice, with an automated `gh aw fix --write`
> migration codemod.

## Source Context

- **Type**: blog-post (official GitHub Agentic Workflows blog, part of the
  `blog/YYYY-MM-DD-<slug>` series alongside prior migration posts like
  `blog-ghaw-ai-credits-migration.md`. Short-form breaking-change
  announcement — one intro paragraph, one code example, and a "Migrate
  existing workflows" section — not a long conceptual piece.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team.
  The page's structured author metadata lists two authors: "Copilot"
  (linked to `github.com/features/copilot`) and Peli de Halleux (linked to
  his Microsoft Research page), matching the co-authorship pattern already
  seen in other gh-aw blog posts in the corpus (e.g. the Agent Factory
  series). This is the authoritative source for gh-aw platform configuration
  changes — the same team owns `reference/sandbox` and
  `reference/agent-runtimes`, which this post explicitly links to as further
  reading.
- **Scope**: Covers the removal of two frontmatter fields
  (`sandbox.agent.legacy-security`, `sandbox.agent.sudo`), the new
  `sandbox.agent.runtime` profile values and their headline behavior
  differences, and the `sandbox-runtime-profiles` codemod invoked via
  `gh aw fix --write`. Does NOT cover: per-profile runner prerequisites
  (KVM, sudo, systemd, credentials — see `docs-ghaw-agent-runtimes-reference.md`
  for the pre-migration `gvisor`/`docker-sbx` requirements, which this post
  does not restate), the `cloud-hypervisor` profile's own requirements or
  isolation mechanism beyond "virtual-machine boundaries," the exact schema
  of `sandbox.agent.allow-host-ports`, or a deprecation timeline for the
  removed fields (the post says they "have been removed," not "will be
  removed," implying immediate effect rather than a grace period, but no
  version number or date is attached to the removal itself).

## Extracted Claims

### Claim 1: `sandbox.agent.legacy-security` and `sandbox.agent.sudo` have been removed from gh-aw; sandbox security behavior is now selected entirely through `sandbox.agent.runtime`, making each runtime an explicit security-and-topology profile

- **Evidence**: Opening sentence of the post, stated as a direct fact about
  current platform state (not a future plan).
- **Confidence**: settled (first-party breaking-change announcement, stated
  in the definite past tense — "have been removed" — not as a proposal)
- **Quote**: "Sandbox security behavior is now selected through
  `sandbox.agent.runtime`. The separate `sandbox.agent.legacy-security` and
  `sandbox.agent.sudo` settings have been removed, making each runtime an
  explicit security and topology profile."
- **Our assessment**: This directly supersedes the `sandbox.agent.sudo`
  field documented as valid (if discouraged/strict-mode-rejected) syntax in
  `docs-ghaw-agent-runtimes-reference.md` Claim 5, and used in a working
  example in that note's Concrete Artifacts (Docker sbx frontmatter with
  `sudo: true`). See contradiction issue **#3173**, filed before this PR per
  MINER.md §4a — the two notes, three weeks apart from the same team, give
  opposite answers to "is `sandbox.agent.sudo` valid syntax?" This claim is
  the single most guide-impacting item in the post: any Ch02/Ch03 material
  that shows `sandbox.agent.sudo` as current syntax needs updating.

### Claim 2: The default `docker` profile runs AWF without sudo and isolates network access

- **Evidence**: Stated as the first specific profile description, immediately
  following the general announcement.
- **Confidence**: settled (first-party specification of default behavior)
- **Quote**: "The default `docker` profile runs AWF without sudo and
  isolates network access."
- **Our assessment**: This confirms the new taxonomy's `docker` profile is a
  drop-in continuation of the prior default (no-sudo, network-isolated AWF)
  documented in `docs-ghaw-sandbox-reference.md` Claim 1 (`sandbox.agent:
  awf` default) and `docs-ghaw-agent-runtimes-reference.md`'s Docker row
  (Linux namespaces/cgroups, "AWF still provides network isolation"). Teams
  that never touched sandbox security settings are unaffected by this
  change — the behavior they already had is now just named `docker`
  explicitly rather than being the implicit absence of `legacy-security`/
  `sudo` settings.

### Claim 3: Workflows that need the previous privileged iptables behavior select the `docker-sudo-iptables` runtime profile

- **Evidence**: Direct instruction paired with a YAML code example showing
  `sandbox.agent.runtime: docker-sudo-iptables`.
- **Confidence**: settled (first-party specification with a working
  configuration example)
- **Quote**: "Workflows that need the previous privileged iptables behavior
  can select `docker-sudo-iptables`:"
- **Our assessment**: The phrase "the previous privileged iptables behavior"
  is the post's own framing of what `docker-sudo-iptables` replaces — it is
  presented as the direct successor to whatever combination of
  `sandbox.agent.legacy-security: enable` and/or `sandbox.agent.sudo: true`
  a workflow previously used to get sudo + iptables networking. This is the
  profile the migration codemod (Claim 7) targets specifically.

### Claim 4: `docker-sudo-iptables` runs AWF with sudo, uses iptables-based networking, and permits host and GitHub Actions service access; it is required for `sandbox.agent.allow-host-ports` and for connecting to published `services:` ports

- **Evidence**: Direct behavioral specification immediately following the
  code example in Claim 3.
- **Confidence**: settled (first-party specification naming two concrete
  dependent features)
- **Quote**: "This profile runs AWF with sudo, uses iptables-based
  networking, and permits host and GitHub Actions service access. It is
  required for `sandbox.agent.allow-host-ports` and for connecting to
  published `services:` ports."
- **Our assessment**: This is the most concrete, checkable claim in the
  post — it names two specific features (`sandbox.agent.allow-host-ports`
  and GitHub Actions `services:` port publishing) that hard-require this
  one profile. Neither `allow-host-ports` nor agent-workflow `services:`
  port access is documented anywhere else in the corpus (confirmed by
  grepping existing source notes) — this is the first appearance of both.
  For a harness engineer whose workflow needs to reach a `services:`
  container (e.g., a test database or mock API running as a GitHub Actions
  service), this claim is the actionable takeaway: the default `docker`
  profile will not permit that access; `docker-sudo-iptables` is required.

### Claim 5: Other profiles retain their own isolation guarantees — `gvisor` adds kernel-level isolation, while `docker-sbx` and `cloud-hypervisor` use virtual-machine boundaries

- **Evidence**: Closing sentence of the intro section, summarizing the
  remaining profile options after `docker` and `docker-sudo-iptables` are
  described in detail.
- **Confidence**: settled for `gvisor`/`docker-sbx` (corroborated in depth by
  `docs-ghaw-agent-runtimes-reference.md`); emerging for `cloud-hypervisor`
  specifically (this post is the corpus's only mention of it, with no
  detail beyond "virtual-machine boundaries")
- **Quote**: "Other profiles retain their own isolation guarantees: `gvisor`
  adds kernel-level isolation, while `docker-sbx` and `cloud-hypervisor` use
  virtual-machine boundaries."
- **Our assessment**: `gvisor` (runsc user-space kernel) and `docker-sbx`
  (KVM-backed microVM) match the isolation descriptions already in
  `docs-ghaw-agent-runtimes-reference.md`'s Choose-a-Runtime table almost
  exactly ("A runsc user-space kernel between the agent and host kernel" /
  "A KVM-backed microVM for the agent"). `cloud-hypervisor` is new: it is
  grouped with `docker-sbx` as a "virtual-machine boundary" runtime, which
  suggests a second VM-based isolation backend (Cloud Hypervisor is a
  real open-source VMM project used for lightweight VMs) — but this post
  gives no runner prerequisites, no mutual-exclusion rules with ARC DinD,
  and no troubleshooting guidance for it, unlike the thorough per-runtime
  treatment `docs-ghaw-agent-runtimes-reference.md` gives `gvisor` and
  `docker-sbx`. Flagged as a documentation gap: the `reference/agent-runtimes`
  page this post links to may now document `cloud-hypervisor` in full, but
  that page was last mined 2026-08-09, before `cloud-hypervisor` existed in
  the corpus — it should be re-mined.

### Claim 6: `gh aw fix --write` runs the fixer to update existing workflow frontmatter for the new runtime-profile model

- **Evidence**: Section heading "Migrate existing workflows" followed
  directly by the instruction and a terminal code block.
- **Confidence**: settled (first-party migration command, consistent with
  the `gh aw fix --write` pattern already documented for the unrelated
  Effective-Tokens-to-AI-Credits migration in `blog-ghaw-ai-credits-migration.md`
  Claim 8)
- **Quote**: "Run the fixer to update workflow frontmatter:" (command shown
  in the following terminal code block is `gh aw fix --write`)
- **Our assessment**: This is now the second distinct breaking change in the
  corpus that uses the identical `gh aw fix --write` command as its
  migration path (the other being the AI Credits migration). This
  corroborates that `gh aw fix --write` is a general-purpose, reusable
  codemod runner in the gh-aw CLI, not a one-off tool built for a single
  migration — worth stating explicitly as a platform pattern in Ch02/Ch05
  guidance: when gh-aw makes a breaking frontmatter change, check for a
  `gh aw fix --write`-compatible codemod before hand-editing workflows.

### Claim 7: The `sandbox-runtime-profiles` codemod rewrites `sandbox.agent.legacy-security: enable` to `sandbox.agent.runtime: docker-sudo-iptables`

- **Evidence**: Named codemod with an explicit before/after YAML pair shown
  in the post.
- **Confidence**: settled (first-party specification of the codemod's exact
  transformation, with a concrete example)
- **Quote**: "The `sandbox-runtime-profiles` codemod rewrites this
  configuration:" (before/after YAML shown in Concrete Artifacts below)
- **Our assessment**: Naming the specific codemod (`sandbox-runtime-profiles`)
  implies `gh aw fix --write` runs a registry of named, targeted codemods
  rather than one monolithic fixer — consistent with a CLI design that can
  apply multiple independent migrations in one pass. The specific mapping
  shown (`legacy-security: enable` → `runtime: docker-sudo-iptables`)
  confirms `docker-sudo-iptables` is specifically the successor to
  `legacy-security: enable`, disambiguating it from a `sudo: true`-only
  configuration (Claim 8 covers that half separately).

### Claim 8: The codemod also removes obsolete `sudo` settings and preserves compatible runtime choices; when a configuration combination cannot be migrated without changing its security intent, the fixer reports an actionable error instead of silently choosing a profile

- **Evidence**: Direct statement following the codemod's before/after
  example, describing the codemod's handling of the `sudo` field and its
  failure-mode behavior.
- **Confidence**: settled (first-party specification of migration-tool
  safety behavior)
- **Quote**: "The codemod also removes obsolete `sudo` settings and
  preserves compatible runtime choices. When a combination cannot be
  migrated without changing its security intent, the fixer reports an
  actionable error instead of selecting a profile silently."
- **Our assessment**: This is a deliberate safety design choice worth
  naming explicitly: the migration tool refuses to silently downgrade or
  upgrade a workflow's security posture when the old
  `legacy-security`/`sudo` combination doesn't map cleanly onto one new
  profile. This is the opposite failure mode from "best-effort migration
  that might silently weaken security" — it fails loud instead. For a
  harness engineer auditing a fleet of workflows before running
  `gh aw fix --write`, this means a clean run (no errors) is itself a
  signal that no workflow's security intent was ambiguous; any reported
  error requires a manual decision about which new profile to choose.

### Claim 9: After migration, workflows must be recompiled with `gh aw compile` and the generated lock file reviewed

- **Evidence**: Explicit closing instruction after the codemod description,
  paired with a terminal code block showing `gh aw compile`.
- **Confidence**: settled (first-party operational instruction, consistent
  with the standard gh-aw compile step already documented elsewhere in the
  corpus, e.g. `docs-ghaw-compilation-process.md`)
- **Quote**: "After migration, compile the workflow and review the
  generated lock file:" (command shown in the following terminal code
  block is `gh aw compile`)
- **Our assessment**: This reinforces that `gh aw fix --write` only edits
  the frontmatter source — it does not itself regenerate the compiled lock
  file that GitHub Actions actually executes. A practitioner who runs the
  fixer but skips `gh aw compile` would have updated source frontmatter
  with a stale, still-`legacy-security`-based lock file in effect. This is
  a two-step migration (fix, then compile), not a one-command migration,
  and should be documented as such.

## Concrete Artifacts

### `docker-sudo-iptables` profile selection (verbatim from source)

```yaml
sandbox:
  agent:
    runtime: docker-sudo-iptables
```

*Source: gh-aw blog, `blog/2026-09-01-sandbox-runtime-profiles`, intro section.*

### Migration command

```sh
gh aw fix --write
```

*Source: gh-aw blog, "Migrate existing workflows" section.*

### `sandbox-runtime-profiles` codemod before/after (verbatim from source)

```yaml
# Before
sandbox:
  agent:
    legacy-security: enable

# After
sandbox:
  agent:
    runtime: docker-sudo-iptables
```

*Source: gh-aw blog, "Migrate existing workflows" section.*

### Post-migration compile command

```sh
gh aw compile
```

*Source: gh-aw blog, "Migrate existing workflows" section, final instruction.*

### Post structure (full heading outline)

```
1. Sandbox Security Options Are Now Runtime Profiles   [intro: removal announcement, docker + docker-sudo-iptables description, other profiles summary]
2. Migrate existing workflows                          [fix --write instruction, codemod before/after, compile instruction, links to sandbox + agent-runtime references]
```

*Confirmed against raw HTML `<h1>`/`<h2>` tags — the post has exactly two
headings; no sub-sections were missed.*

## Cross-References

- **Contradicts**: `docs-ghaw-agent-runtimes-reference.md` Claim 5 (and its
  Docker sbx Concrete Artifacts YAML example using `sudo: true`) — this
  post states `sandbox.agent.sudo` "has been removed," directly opposing
  that note's documentation of `sandbox.agent.sudo` as valid (if
  discouraged/strict-mode-rejected) syntax. **Contradiction issue #3173
  filed** before this PR, per MINER.md §4a, with recommended verdict
  `superseded` (this post is ~3 weeks newer, first-party, and an explicit
  breaking-change announcement with a migration codemod). See Claim 1.

- **Corroborates**:
  - `docs-ghaw-enclaves.md` Claim 2 ("every supported `sandbox.agent.runtime`
    profile provides" AWF network isolation): this post's closing line
    ("Other profiles retain their own isolation guarantees") is consistent
    with that note's framing that AWF network isolation is a baseline
    guarantee across the runtime taxonomy, not something only some profiles
    provide.
  - `docs-ghaw-agent-runtimes-reference.md`'s Choose-a-Runtime comparison
    table (Concrete Artifacts): the `gvisor` ("kernel-level isolation") and
    `docker-sbx` ("virtual-machine boundaries") descriptions in this post
    match that table's "A runsc user-space kernel between the agent and
    host kernel" and "A KVM-backed microVM for the agent" rows in substance,
    though this post uses shorter, less technical phrasing.
  - `blog-ghaw-ai-credits-migration.md` Claim 8 (`gh aw fix --write` as the
    migration command for the Effective-Tokens-to-AI-Credits breaking
    change): corroborates that `gh aw fix --write` is a reusable,
    general-purpose codemod runner used across unrelated gh-aw breaking
    changes, not a one-off tool.

- **Extends**:
  - `docs-ghaw-agent-runtimes-reference.md`: that note's Field Purpose Table
    documents `sandbox.agent.runtime` values as "gvisor, docker-sbx, or
    omitted for Docker" (as of 2026-08-09) — it does not include
    `docker-sudo-iptables` or `cloud-hypervisor` as explicit runtime values,
    and it documents `docker` only as an *omitted-field* default, not as an
    explicit settable value. This post extends the taxonomy to five named
    profiles (`docker`, `docker-sudo-iptables`, `gvisor`, `docker-sbx`,
    `cloud-hypervisor`) and confirms `docker` is now (or always was) also
    settable explicitly. The per-runtime requirements, mutual-exclusion
    rules, and troubleshooting guidance in that note are not restated or
    contradicted here — they remain the more detailed reference for
    `gvisor`/`docker-sbx`, but that note should be re-mined to check
    whether its `reference/agent-runtimes` source page has been updated for
    `docker-sudo-iptables` and `cloud-hypervisor` (see Claim 5 assessment).
  - `docs-ghaw-sandbox-reference.md`: that note documents `sandbox.agent:
    awf` (default) and `sandbox.agent: false` (disable firewall only) as
    the sandbox toggle — a simpler boolean/string model than either the
    `id: awf` + `runtime:` nested structure in
    `docs-ghaw-agent-runtimes-reference.md` or this post's pure
    `runtime:`-selection model. This post is a further step in the same
    evolution: security posture selection has moved from a top-level
    enable/disable flag, through an `id`/`runtime` split, to runtime name
    alone being the full security-and-topology profile. The `sandbox-reference`
    note's filesystem-access-tier and environment-variable claims (Claims
    4–8 there) are about the AWF sandbox mechanism itself, not the
    `legacy-security`/`sudo` fields, and are not addressed by this post.
  - `blog-ghaw-ai-credits-migration.md`: extends the corpus's pattern
    library of gh-aw breaking-change announcements with automated
    `gh aw fix --write` migration — this is now a second, independent
    example of the same announce-plus-codemod pattern.

- **Novel** (what this note adds that no prior source covers):
  - **`sandbox.agent.legacy-security` and `sandbox.agent.sudo` removal**
    (Claim 1): first corpus documentation that these fields no longer exist.
  - **`docker-sudo-iptables` as a named runtime profile** (Claims 3, 4): not
    present in any existing source note.
  - **`cloud-hypervisor` as a runtime profile** (Claim 5): entirely new to
    the corpus; no prior source mentions this runtime option at all.
  - **`sandbox.agent.allow-host-ports`** (Claim 4): first corpus mention of
    this field; confirmed via grep that no existing source note references
    it.
  - **GitHub Actions `services:` port access for agent workflows requiring
    `docker-sudo-iptables`** (Claim 4): first corpus documentation that
    connecting to published `services:` ports is gated behind a specific
    sandbox runtime profile.
  - **The `sandbox-runtime-profiles` named codemod** (Claim 7): first
    corpus documentation of a specific, named `gh aw fix --write` codemod
    and its exact before/after transformation.
  - **Migration-tool fail-loud-on-ambiguity design** (Claim 8): the
    "actionable error instead of selecting a profile silently" behavior is
    a new, generalizable harness-engineering pattern not documented
    elsewhere — the AI Credits migration note does not describe this level
    of `gh aw fix --write` safety behavior.

## Guide Impact

- **Chapter 02 (Harness Engineering — sandbox/runtime configuration)**:
  Update any material describing `sandbox.agent.sudo` or
  `sandbox.agent.legacy-security` as current syntax (sourced from
  `docs-ghaw-agent-runtimes-reference.md`) to reflect the removal. Add the
  five-profile `sandbox.agent.runtime` taxonomy (`docker`,
  `docker-sudo-iptables`, `gvisor`, `docker-sbx`, `cloud-hypervisor`) as the
  current model, explicitly noting `cloud-hypervisor` as underdocumented
  pending re-mining of `reference/agent-runtimes`. Add
  `sandbox.agent.allow-host-ports` and `services:` port access as a
  documented reason to choose `docker-sudo-iptables` over the default.
  Document the two-step migration (`gh aw fix --write` then `gh aw compile`)
  as the standard procedure when gh-aw ships this class of breaking change,
  generalizing from both this post and the AI Credits migration.

- **Chapter 03 (Safety and Verification — sandbox security configuration)**:
  Flag this as a breaking change requiring audit: any workflow authored
  before 2026-09-01 that used `sandbox.agent.legacy-security: enable` or
  `sandbox.agent.sudo: true` needs migration. Note the migration tool's
  fail-loud design (Claim 8) as a positive pattern worth naming explicitly —
  automated security-config migrations should refuse silent security-intent
  changes and require human decision on ambiguous cases. Do not cite
  `sandbox.agent.sudo` as current, valid syntax pending resolution of
  contradiction issue #3173.

## Extraction Notes

1. **Verbatim text sourced from raw HTML via `curl` + `html2text`, not
   WebFetch's AI-summarization pass.** An initial WebFetch pass (used for
   orientation only) returned plausible but paraphrased prose that did not
   match the source's exact wording in places (e.g., it rendered "Peli de
   Halleux" as a co-author correctly but restructured sentences). Per the
   precedent in `docs-ghaw-agent-runtimes-reference.md` Extraction Note 1,
   the page was re-fetched directly with `curl` and converted to Markdown
   with `html2text` (`body_width=0`), and every `Quote` field above was
   copied character-for-character from that raw conversion. The extracted
   `<article>`/`<main data-pagefind-body>` HTML was isolated first to avoid
   picking up nav/footer boilerplate.
2. **The post is short and fully self-contained** — two headings, one
   intro paragraph split into three sentences plus one code example, and
   one "Migrate existing workflows" section with a codemod example and two
   commands. All of it was extracted; nothing was judged skippable. The
   post links to `reference/sandbox` and `reference/agent-runtimes` as
   further reading — both are already mined
   (`docs-ghaw-sandbox-reference.md`, extracted 2026-05-12;
   `docs-ghaw-agent-runtimes-reference.md`, extracted 2026-08-09) but
   **both predate this post** and do not reflect the runtime-profile
   consolidation described here. Re-mining `reference/agent-runtimes` in
   particular is recommended to capture full `docker-sudo-iptables` and
   `cloud-hypervisor` details (runner prerequisites, troubleshooting) that
   this short announcement post does not include.
3. **No removal timeline stated.** The post uses present-perfect phrasing
   ("have been removed") with no version number, no deprecation grace
   period, and no stated GA/preview status for the new profiles. Treated as
   immediate/current effective behavior for `confidence_overall: settled`
   purposes, consistent with how `blog-ghaw-ai-credits-migration.md`
   treated its own removal-of-primacy announcement.
4. **Contradiction issue #3173 filed before this PR**, per MINER.md §4a,
   against `docs-ghaw-agent-runtimes-reference.md` Claim 5. See
   Cross-References → Contradicts above. No other contradictions were
   identified against the corpus — `docs-ghaw-sandbox-reference.md` and
   `docs-ghaw-enclaves.md` are treated as extended/corroborated rather than
   contradicted, since neither makes a claim about `sandbox.agent.sudo`
   or `legacy-security` specifically that this post opposes (see
   Cross-References → Extends for the reasoning).
