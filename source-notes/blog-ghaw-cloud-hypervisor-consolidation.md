---
source_url: https://github.github.com/gh-aw/blog/2026-09-05-cloud-hypervisor-consolidation/
source_type: blog-post
title: "MicroVM Support Is Consolidating on Cloud Hypervisor"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-09-05
date_extracted: 2026-09-06
last_checked: 2026-09-06
status: current
confidence_overall: emerging
issue: "#3271"
---

# MicroVM Support Is Consolidating on Cloud Hypervisor

> gh-aw is deprecating both the `gvisor` and `docker-sbx` sandbox runtimes in
> favor of consolidating all microVM-level agent isolation on
> `cloud-hypervisor`, currently in preview and gated to GitHub-hosted Ubuntu
> x86_64 runners with `/dev/kvm`.

## Source Context

- **Type**: blog-post (official gh-aw platform blog; a short, single-page
  announcement with two named sections, "What changes" and "Migrating
  existing workflows")
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The page's `schema.org/BlogPosting`
  JSON-LD names the author as "Copilot" (`https://github.com/features/copilot`)
  — the same non-human byline pattern documented in prior weekly/blog notes
  (e.g. `blog-ghaw-weekly-2026-08-17.md`). `datePublished` in the JSON-LD is
  `2026-09-05T00:00:00.000Z`, matching the on-page "Sep 5, 2026" byline.
- **Scope**: A deprecation/consolidation announcement for two named sandbox
  runtimes (`gvisor`, `docker-sbx`), the resulting two-option runtime surface
  (default `docker`, preview `cloud-hypervisor`), `cloud-hypervisor`'s stated
  runner eligibility requirement, and a short migration procedure. Does NOT
  cover: a removal timeline or version number for `gvisor`/`docker-sbx`
  ("a future release" is the only timing given); any isolation-strength
  benchmark or cost/latency comparison between `cloud-hypervisor` and the
  runtimes it replaces; the full eligibility/configuration schema for
  `cloud-hypervisor` (the post explicitly defers this to the linked "Agent
  Runtime Selection" reference page); or what "digest-pinned runtime assets"
  specifically pins or how a practitioner would inspect those pins.

## Extracted Claims

### Claim 1: gh-aw is deprecating the `gvisor` and `docker-sbx` sandbox runtime options, consolidating specialized microVM isolation on `cloud-hypervisor`; the deprecated values will be removed in a future release
- **Evidence**: Opening paragraph, stated as a direct platform decision, not a proposal.
- **Confidence**: settled (first-party, unambiguous present-tense statement of an already-made decision, though no version/date is attached to the eventual removal)
- **Quote**: "GitHub Agentic Workflows is consolidating its specialized sandbox runtime support on cloud-hypervisor. The gvisor and docker-sbx runtime options are deprecated and will be removed in a future release."
- **Our assessment**: This is the load-bearing claim of the post and the reason it required a dedicated deep-dive mining pass: `blog-ghaw-weekly-2026-08-17.md` Claim 4 introduced `cloud-hypervisor` nine days earlier as a new, additive runtime tier ("enabled on eligible agentic workflows for improved isolation") without any indication that it would displace existing runtimes. This post reframes that addition as the first step of a consolidation that actively deprecates two runtimes `docs-ghaw-agent-runtimes-reference.md` (extracted 2026-08-09, one week before `cloud-hypervisor`'s announcement) documents as first-class, currently-recommended isolation tiers — including recommending `docker-sbx` as the *strongest* isolation option in that note's priority-ordered selection procedure. See Cross-References → Contradicts.

### Claim 2: The stated rationale for consolidation is that maintaining `gvisor` and `docker-sbx` alongside Cloud Hypervisor created separate installation, compatibility, and troubleshooting surfaces, and that one microVM implementation is more consistent and easier to evolve
- **Evidence**: Second paragraph, immediately following the deprecation announcement.
- **Confidence**: settled (first-party stated rationale, though not independently verified against any incident or cost data)
- **Quote**: "docker-sbx introduced a KVM-backed microVM boundary, while gvisor provided a user-space kernel between the agent container and host kernel. Maintaining both paths alongside Cloud Hypervisor created separate installation, compatibility, and troubleshooting surfaces. Consolidating on one microVM implementation makes the stronger isolation path more consistent and easier to evolve."
- **Our assessment**: This restates `docker-sbx` and `gvisor`'s isolation mechanisms in language that matches `docs-ghaw-agent-runtimes-reference.md`'s Choose-a-Runtime Comparison Table almost exactly (that table describes `docker-sbx` as "a KVM-backed microVM for the agent" and `gvisor` as "a runsc user-space kernel between the agent and host kernel") — confirming both sources describe the same two mechanisms, one framing them as current options, the other framing them as legacy paths being retired. The stated engineering rationale ("separate installation, compatibility, and troubleshooting surfaces") is a maintenance-burden argument, not a security regression claim — the post does not say `gvisor` or `docker-sbx` were found unsafe, only redundant to maintain once Cloud Hypervisor covers the same threat model.

### Claim 3: The default `docker` runtime is unaffected by the consolidation and continues to run AWF with network isolation and proxy enforcement
- **Evidence**: "What changes" section, opening sentence.
- **Confidence**: settled (first-party, direct statement)
- **Quote**: "The default docker runtime remains available and continues to run AWF with network isolation and proxy enforcement."
- **Our assessment**: This corroborates `docs-ghaw-agent-runtimes-reference.md`'s Claim on the Docker section ("AWF still provides network isolation and proxy enforcement; 'Docker' does not mean that the agent runs without a sandbox") and confirms that consolidation is scoped narrowly to the specialized/hardware-virtualized tier — teams not currently using `gvisor` or `docker-sbx` have no required action.

### Claim 4: For workflows requiring a hardware-virtualized boundary, `cloud-hypervisor` is configured via `sandbox.agent.runtime: cloud-hypervisor` and is now "the supported direction"
- **Evidence**: "What changes" section, second sentence plus a YAML frontmatter example.
- **Confidence**: settled (first-party, with a concrete working config example)
- **Quote**: "For workflows that require a hardware-virtualized boundary, cloud-hypervisor is now the supported direction:"
- **Our assessment**: The example frontmatter omits `sandbox.agent.id: awf`, showing only `sandbox: agent: runtime: cloud-hypervisor` — consistent with `docs-ghaw-agent-runtimes-reference.md`'s Frontmatter Examples (which also show `runtime:` as a sibling of `id: awf` but note `id` is otherwise unstated as required); this note cannot confirm from this example alone whether `id: awf` is now optional or was just omitted for brevity in a short announcement post. This is the first corpus confirmation that `cloud-hypervisor` is a valid literal value for the `sandbox.agent.runtime` field, the same field path documented for `gvisor`/`docker-sbx` in `docs-ghaw-agent-runtimes-reference.md`'s Field Purpose Table — i.e., `cloud-hypervisor` slots into the existing field taxonomy rather than introducing a new configuration surface.

### Claim 5: `cloud-hypervisor` support is currently in preview and requires a GitHub-hosted Ubuntu x86_64 runner with `/dev/kvm`; the compiler adds host checks and provisions digest-pinned runtime assets
- **Evidence**: "What changes" section, closing sentence.
- **Confidence**: emerging (specific runner/OS/architecture/device requirement stated plainly, but "preview" status, "the required host checks," and "digest-pinned runtime assets" are none of them elaborated — no list of what checks are added or what is pinned)
- **Quote**: "Cloud Hypervisor support is currently in preview and requires a GitHub-hosted Ubuntu x86_64 runner with /dev/kvm. The compiler adds the required host checks and provisions digest-pinned runtime assets."
- **Our assessment**: This is the first corpus statement of `cloud-hypervisor`'s concrete eligibility gate — the exact detail `blog-ghaw-weekly-2026-08-17.md` Claim 4's assessment flagged as missing ("no detail on what 'eligible' means"). It is narrower than `docker-sbx`'s stated requirements in `docs-ghaw-agent-runtimes-reference.md` (KVM, nested virtualization, sudo, apt, Docker Hub credentials, local Docker) in that it names a specific runner OS/architecture (GitHub-hosted Ubuntu x86_64) rather than a generic KVM-capable host — this could mean `cloud-hypervisor` is GitHub-hosted-runner-only (no self-hosted-runner path stated here, unlike `docker-sbx`/`gvisor`), but the post does not explicitly rule out self-hosted eligibility, so this reading is our inference, not a stated claim. "Preview" status and the unelaborated "required host checks"/"digest-pinned runtime assets" language mean a harness engineer cannot yet reproduce or audit the compiler's provisioning behavior from this post alone — this is exactly the gap the linked "Agent Runtime Selection" reference page (Claim 8) is supposed to fill but, as of this extraction, does not.

### Claim 6: Migration guidance for workflows explicitly setting `runtime: gvisor` or `runtime: docker-sbx`: select `cloud-hypervisor` if the runner is eligible and a microVM boundary is needed, otherwise remove the `runtime` setting entirely to fall back to the default Docker profile
- **Evidence**: "Migrating existing workflows" section, first two sentences.
- **Confidence**: settled (first-party, direct prescriptive instruction)
- **Quote**: "Review workflows that explicitly set runtime: gvisor or runtime: docker-sbx. Select cloud-hypervisor when the workflow runs on an eligible GitHub-hosted runner and needs a microVM boundary. Otherwise, remove the runtime setting to use the default Docker profile."
- **Our assessment**: This is a binary decision, not a three-way choice — a workflow currently on `gvisor` or `docker-sbx` either qualifies for `cloud-hypervisor` (GitHub-hosted Ubuntu x86_64 + `/dev/kvm`, per Claim 5) or must fall back all the way to default Docker; there is no stated "keep using gvisor/docker-sbx a while longer without action" option beyond Claim 7's transition window, and no gVisor-equivalent middle tier remains once the deprecated runtimes are removed. This directly narrows the four-way (or per `docs-ghaw-agent-runtimes-reference.md` Claim 12's reframing, "three isolation tiers × two topologies") decision space that note documented down to two runtime choices post-consolidation.

### Claim 7: Practitioners should compile each updated workflow with `gh aw compile` and review the generated lock file as part of migration; the deprecated runtime values remain documented during a transition period, but new workflows should use default Docker or `cloud-hypervisor`
- **Evidence**: "Migrating existing workflows" section, remaining sentences.
- **Confidence**: settled (first-party, direct instruction plus a stated transition policy)
- **Quote**: "Compile each updated workflow and review the generated lock file: `gh aw compile` The deprecated values remain documented during the transition, but new workflows should use either the default Docker runtime or cloud-hypervisor."
- **Our assessment**: "Remain documented during the transition" is the only signal in this post about how long `gvisor`/`docker-sbx` stay usable — it implies a deliberate, if unscheduled, deprecation window rather than an immediate break, consistent with the "removed in a future release" language in Claim 1 rather than "removed now." The recommend-compile-and-inspect-the-lock-file instruction matches the general gh-aw operational pattern already documented in `docs-ghaw-agent-runtimes-reference.md`'s "Debug in dependency order" procedure (confirm frontmatter → `gh aw compile` → inspect generated lock file), applied here specifically to a runtime migration rather than a failure investigation.

### Claim 8: The post defers "requirements and tradeoffs" detail to the "Agent Runtime Selection" reference page, which is the same URL already mined as `docs-ghaw-agent-runtimes-reference.md` — but that note's content, extracted 2026-08-09, predates `cloud-hypervisor` entirely and documents no `cloud-hypervisor` requirements or tradeoffs
- **Evidence**: Closing sentence's hyperlink, confirmed by inspecting the raw page HTML: the anchor text "Agent Runtime Selection" resolves to `href="/gh-aw/reference/agent-runtimes/"`, which is the same path as `docs-ghaw-agent-runtimes-reference.md`'s `source_url` (`https://github.github.com/gh-aw/reference/agent-runtimes`).
- **Confidence**: settled for the link target (directly confirmed in the page's HTML `<a>` tag, not inferred); settled for the gap (directly confirmed by re-reading `docs-ghaw-agent-runtimes-reference.md`, which contains no mention of `cloud-hypervisor` anywhere in its Extracted Claims or Concrete Artifacts)
- **Quote**: "See Agent Runtime Selection for requirements and tradeoffs."
- **Our assessment**: This is a documentation gap, not a contradiction: the post points readers to a reference page for exactly the detail (eligibility criteria, tradeoffs) this note's Claim 5 found thin, but that reference page has not been updated (or at least not re-mined) to cover `cloud-hypervisor` at all — its four-way comparison table (Docker / gVisor / Docker sbx / ARC DinD) and priority-ordered selection procedure make no mention of the runtime this blog post now calls "the supported direction." A harness engineer following this post's own citation would currently find no `cloud-hypervisor` row in the comparison table it points to. This is the second time in the corpus this exact gap has been flagged (`blog-ghaw-weekly-2026-08-17.md` Claim 4 flagged it as "worth a dedicated reference-doc mining pass once GHAW documents eligibility criteria and mechanism in more depth") — this post is that follow-up in spirit, but it is itself a short blog announcement, not the reference-doc update; the underlying reference page still needs a fresh mining pass once GitHub updates it.

## Concrete Artifacts

### Working `cloud-hypervisor` frontmatter example (verbatim from source)

```yaml
---
on: issues
sandbox:
  agent:
    runtime: cloud-hypervisor
---
Investigate this issue.
```

*Source: "What changes" section.*

### Migration compile step (verbatim from source)

```
gh aw compile
```

*Source: "Migrating existing workflows" section, under "Compile each updated workflow and review the generated lock file."*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agent-runtimes-reference.md` Choose-a-Runtime Comparison Table
    (Concrete Artifacts): this post's one-line mechanism descriptions
    ("docker-sbx introduced a KVM-backed microVM boundary, while gvisor
    provided a user-space kernel between the agent container and host
    kernel") match that table's descriptions of `docker-sbx` ("a KVM-backed
    microVM for the agent") and `gvisor` ("a runsc user-space kernel between
    the agent and host kernel") almost verbatim, confirming both sources
    describe the same two mechanisms.
  - `docs-ghaw-agent-runtimes-reference.md` Claim on the Docker runtime
    ("AWF still provides network isolation and proxy enforcement"): Claim 3
    here confirms the default Docker runtime's behavior is unchanged by this
    consolidation.
  - `docs-ghaw-agent-runtimes-reference.md`'s "Debug in dependency order"
    procedure (confirm frontmatter → `gh aw compile` → inspect lock file):
    Claim 7 here applies the same compile-and-inspect pattern to a runtime
    migration.

- **Contradicts**: `docs-ghaw-agent-runtimes-reference.md` Claim 2 (the
  priority-ordered runtime-selection procedure that recommends `docker-sbx`
  as the strongest isolation tier when KVM is available, ahead of `gvisor`
  and default Docker) and Claims 3–4 (the `docker-sbx`/`gvisor` × ARC DinD
  mutual-exclusion rules, which presuppose both runtimes remain
  first-class, selectable options). This post (Claim 1) states both
  `gvisor` and `docker-sbx` are deprecated and will be removed, replaced as
  "the supported direction" for hardware-virtualized isolation by
  `cloud-hypervisor` — a runtime the August reference page does not
  mention at all. A guide section built from the reference page alone would
  currently recommend selecting a runtime this first-party blog post has
  since deprecated. Filed as **[contradiction issue #3285](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3285)** per MINER.md §4a; no verdict is asserted
  here pending human/Smith resolution and a CONTRADICTIONS.md entry.

- **Extends**:
  - `blog-ghaw-weekly-2026-08-17.md` Claim 4 (`cloud-hypervisor` runtime
    "enabled on eligible agentic workflows for improved isolation," PR
    #52932, with "no detail on what 'eligible' means, what hypervisor is
    used, or what isolation improvement is measured/claimed" per that
    note's own assessment): this post is the explicitly-anticipated
    deep-dive follow-up, supplying the eligibility criteria (GitHub-hosted
    Ubuntu x86_64, `/dev/kvm`, Claim 5 here) that note flagged as missing —
    though it still does not supply a measured isolation-improvement claim
    beyond "stronger isolation path" (Claim 2) and "hardware-virtualized
    boundary" (Claim 4).

- **Novel**:
  - **The consolidation/deprecation decision itself** (Claim 1): first
    corpus record that `gvisor` and `docker-sbx` are being retired, not
    merely that a new runtime was added alongside them.
  - **`cloud-hypervisor`'s stated eligibility gate** (Claim 5): first
    corpus statement of concrete runner requirements (GitHub-hosted Ubuntu
    x86_64, `/dev/kvm`) for this runtime.
  - **The migration procedure** (Claims 6–7): first corpus guidance for
    moving an existing `gvisor`/`docker-sbx` workflow to the post-
    consolidation runtime surface.
  - **The unresolved documentation gap** (Claim 8): first corpus
    confirmation that the reference page this post cites for "requirements
    and tradeoffs" does not yet cover the runtime the post is announcing.

## Guide Impact

- **Chapter 04 (Safety and Constraints)**: Update any guide text describing
  gh-aw's specialized sandbox runtime tiers to reflect that `gvisor` and
  `docker-sbx` are deprecated and scheduled for removal (Claim 1), with
  `cloud-hypervisor` (preview, GitHub-hosted Ubuntu x86_64 + `/dev/kvm` only,
  Claim 5) as the sole forward path for a hardware-virtualized boundary, and
  default Docker (unchanged network isolation/proxy enforcement, Claim 3)
  as the fallback for workflows that don't need one. Flag `cloud-hypervisor`
  as preview-status — not yet a like-for-like settled replacement — and note
  the still-open documentation gap (Claim 8) around its exact isolation
  guarantees.
- **Chapter 02 (Harness Engineering)**: The "choosing an agent runtime"
  subsection recommended by `docs-ghaw-agent-runtimes-reference.md`'s own
  Guide Impact section (built on that page's four-way comparison table and
  priority-ordered selection procedure) needs revision once this
  contradiction (issue #3285) is resolved: that procedure currently
  recommends `docker-sbx` as the strongest isolation tier, which this post
  deprecates. Add the migration steps (Claims 6–7: review `runtime:
  gvisor`/`runtime: docker-sbx` settings, select `cloud-hypervisor` if
  eligible else remove the field, `gh aw compile`, inspect the lock file)
  as concrete guidance for teams with existing workflows on the deprecated
  runtimes.
- **Follow-up mining**: The "Agent Runtime Selection" reference page
  (`docs-ghaw-agent-runtimes-reference.md`'s source URL) is the page this
  post itself cites for `cloud-hypervisor` requirements and tradeoffs, but
  as of this extraction that page has not been re-mined since 2026-08-09
  and contains no `cloud-hypervisor` content. A dedicated re-mining pass of
  that page is warranted once GitHub updates it to include
  `cloud-hypervisor`'s full eligibility/configuration schema and the
  deprecation timeline for `gvisor`/`docker-sbx`.

## Extraction Notes

1. **Raw HTML fetched via `curl` and parsed with BeautifulSoup**, following
   the practice established in prior notes on this domain (e.g.
   `blog-ghaw-weekly-2026-08-03.md` Extraction Note 1,
   `docs-ghaw-agent-runtimes-reference.md` Extraction Note 1). Content was
   extracted from `div.sl-markdown-content` and cross-checked against an
   initial WebFetch summarization pass; the two were consistent, and all
   `Quote` fields above were copied character-for-character from the raw
   BeautifulSoup text extraction, not the WebFetch summary.
2. **One linked page was inspected but not independently re-fetched in
   full**: the "Agent Runtime Selection" hyperlink's `href` attribute was
   read directly from the raw HTML (`/gh-aw/reference/agent-runtimes/`) to
   confirm it resolves to the same URL already mined as
   `docs-ghaw-agent-runtimes-reference.md`. That existing note was re-read
   in full (not re-fetched from the web) to confirm it contains no
   `cloud-hypervisor` content, supporting Claim 8. A second link on the
   page ("Agent of the Day – September 3, 2026") is a blog
   next-post/navigation link, not part of the article body, and resolves to
   a post already in the corpus (`blog-ghaw-agent-of-the-day-2026-09-03.md`)
   — not followed further.
3. **`schema.org/BlogPosting` JSON-LD confirmed** `datePublished:
   2026-09-05T00:00:00.000Z` and author "Copilot," matching the on-page
   byline and the non-human byline pattern documented in prior gh-aw blog
   notes.
4. **Confidence rated `emerging` overall**, not `settled`: the deprecation
   decision itself (Claim 1) and the migration procedure (Claims 6–7) are
   stated plainly and rate `settled` individually, but the note's most
   actionable new content — `cloud-hypervisor`'s eligibility gate and
   provisioning behavior (Claim 5) — is explicitly preview-status and
   thinly documented, and the reference page this post cites for fuller
   detail does not yet cover it (Claim 8). The overall grade reflects that
   mix rather than treating the whole post as uniformly settled.
5. **Cross-reference check performed** against `docs-ghaw-agent-runtimes-reference.md`,
   `blog-ghaw-weekly-2026-08-17.md`, `blog-ghaw-agent-of-the-day-2026-08-26.md`
   (which shows a working `runtime: cloud-hypervisor` example in its
   Concrete Artifacts, consistent with Claim 4 here), `docs-ghaw-sandbox-reference.md`,
   and `CONTRADICTIONS.md` for existing open entries. No prior contradiction
   entry covers `gvisor`/`docker-sbx`/`cloud-hypervisor`; the only related
   contradiction issue found (#3173, a different field —
   `sandbox.agent.sudo` — closed as unresolved because its Side B source
   note was never mined) is not a duplicate of the contradiction filed here.
   A new contradiction was filed as issue #3285 per MINER.md §4a against
   `docs-ghaw-agent-runtimes-reference.md` Claims 2–4, recommending
   "superseded" given this is a newer (Sep 2026 vs. Aug 2026), first-party,
   explicitly-framed deprecation announcement — the same pattern the
   Assayer's assessment of issue #3173 identified as the strongest form of
   evidence for that verdict, provided (unlike #3173) both sides are
   quote-verified source notes at filing time.
