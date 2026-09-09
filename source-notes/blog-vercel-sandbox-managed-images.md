---
source_url: https://vercel.com/changelog/vercel-sandbox-managed-images
source_type: blog-post
title: "Vercel Sandbox now runs on Vercel Managed Images"
author: Andy Waller, Tom Lienard, Marc Codina Segura, Luke Phillips-Sheard (Vercel), with contributor Kevin Sundstrom
date_published: 2026-08-10
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: emerging
issue: "#3329"
---

# Vercel Sandbox now runs on Vercel Managed Images

> Vercel changelog announcing Vercel Managed Images (VMI) — a catalog of five
> versioned, open-source base images for Vercel Sandbox that replace the
> deprecated "Sandbox runtimes" concept, switch the default OS from Amazon
> Linux to Ubuntu, ship nightly-rebuilt security patches with opt-out digest
> pinning for reproducibility, and are extensible via a Dockerfile-and-push
> workflow through Vercel Container Registry (VCR).

## Source Context

- **Type**: blog-post (Vercel official changelog, `vercel.com/changelog`,
  published August 10, 2026, ~350 words). Per MINER.md §1, one linked
  documentation page was followed in full because the changelog compresses
  mechanics — especially custom-image building and image-reference syntax —
  documented in much greater depth on the linked images concept page
  (`vercel.com/docs/sandbox/concepts/images`, last updated August 11, 2026,
  one day after the changelog). A GitHub repository
  (`github.com/vercel/sandbox`) was also linked and fetched, but WebFetch
  could not retrieve the raw README text (see Extraction Notes) — its output
  is not used as a quote source or claim evidence anywhere in this note.
- **Author credibility**: First-party Vercel product announcement and
  first-party Vercel product documentation, describing a shipping change to
  Vercel Sandbox's default image/runtime model. Authoritative for the feature
  existing, the API surface, the image catalog contents, and the stated
  update/security cadence. Not independently verified; no customer name,
  adoption metric, or third-party security review appears in either page.
- **Scope**: Covers the Vercel Managed Images catalog (five named images),
  the API migration from `runtime` to `image`, the default-user and default-OS
  changes, the nightly-release/digest-pinning update model, and the
  custom-image build-and-push workflow via Vercel Container Registry. Does
  NOT cover: pricing for VCR storage or image pulls, benchmarked boot-time
  differences between the old runtime model and the new image model, an
  exhaustive list of preinstalled utilities beyond what's named in the two
  pages, or any customer's experience migrating from `runtime` to `image`.

## Extracted Claims

### Claim 1: Vercel Managed Images (VMI) replace the deprecated "Sandbox runtimes" concept, and new sandboxes now default to the `vercel/sandbox/universal:latest` image starting with Sandbox SDK v3

- **Evidence**: Explicit statement in the changelog's opening paragraphs.
- **Confidence**: settled (first-party statement of a shipped default-behavior
  change, with a specific SDK version gate)
- **Quote**: "Managed images replace Sandbox runtimes, which are now
  deprecated. Starting with version 3 of the Sandbox SDK, new sandboxes
  default to `vercel/sandbox/universal:latest`. It ships with Node.js,
  Python, common coding agents and standard utilities, so most users never
  build a custom image or install packages at boot."
- **Our assessment**: This is a default-behavior change with SDK-version
  gating, not an opt-in feature — any team on Sandbox SDK v3+ that calls
  `Sandbox.create()` without an explicit `image` or `runtime` now gets a
  different (Ubuntu-based, batteries-included) environment than before,
  which matters for reproducibility if a team's tooling implicitly depended
  on the prior Amazon-Linux-based default (see Claim 2, and Cross-References
  for a concrete case — `blog-vercel-herdr-agent-sandboxes.md`'s own code
  example predates this change).

### Claim 2: The new default image switches Vercel Sandbox's default operating system from Amazon Linux to Ubuntu

- **Evidence**: Explicit statement in the changelog, framed as an industry-
  alignment rationale.
- **Confidence**: settled (first-party statement of the specific OS change)
- **Quote**: "The universal image switches our default operating system from
  Amazon Linux to Ubuntu, a lighter and more widely used system across the
  industry."
- **Our assessment**: This is a breaking change in the sense that packages,
  paths, or `yum`/`dnf`-based provisioning scripts written against the prior
  Amazon-Linux default will not work unmodified against the new Ubuntu-based
  default — the changelog itself flags an escape hatch for exactly this case
  (Claim 8: Amazon Linux stays available via the deprecated `runtime`
  property). Teams with existing boot-time provisioning logic tied to Amazon
  Linux package names or paths should audit that logic before adopting
  Sandbox SDK v3's new default, or pin explicitly to `runtime` in the interim.

### Claim 3: Every managed image receives a nightly release; rolling tags (`latest`, major-version tags) pick up OS and dependency security patches automatically, while digest-pinned images opt out of automatic updates for full reproducibility

- **Evidence**: Explicit statement under the changelog's "Secure by default"
  heading, corroborated by the docs page's "Release cadence" section.
- **Confidence**: settled (first-party statement of a specific, named update
  mechanism and its opt-out path)
- **Quote**: "Every managed image gets a nightly release. Rolling tags such as
  `latest` and the major-version tags pick up operating system and dependency
  updates automatically, including security patches and new releases of
  Node.js, Python, and the preinstalled coding agents." / "If you need a
  fully immutable, reproducible environment, pin to an image digest (SHA).
  Digest-pinned images opt out of automatic updates."
- **Our assessment**: This is the same "rolling tag for freshness vs. pinned
  digest for reproducibility" tradeoff familiar from general OCI/Docker
  practice, made explicit and vendor-endorsed for agent sandboxes
  specifically. The practical implication for a harness engineer: a fleet of
  agent sandboxes on `universal:latest` will silently receive new coding-agent
  versions (the changelog names `opencode`, `claude-code`, `codex`, and `pi`
  as preinstalled — see Claim 5) whenever Vercel's nightly pipeline ships one,
  which is convenient for staying current but means agent-version drift is
  possible across sandboxes created on different days unless a team pins to a
  specific digest.

### Claim 4: Within a given image release, dependency versions are pinned wherever possible so that a specific image version's behavior stays consistent

- **Evidence**: Explicit statement in the changelog, immediately following the
  nightly-release claim.
- **Confidence**: settled (first-party statement of an internal consistency
  guarantee)
- **Quote**: "Within each release, dependencies are pinned to specific
  versions wherever possible, so a given image version stays consistent."
- **Our assessment**: This qualifies Claim 3's "automatic updates" framing —
  the rolling tag moves forward release-to-release, but a single materialized
  release (and by extension, a specific digest) is internally pinned rather
  than resolving dependency versions dynamically at pull or boot time. This
  is a meaningful distinction for debugging: a bug reproduced against one
  digest should reproduce identically on that digest indefinitely, even
  though `latest` itself is a moving target.

### Claim 5: The managed image catalog offers five distinct starting points — universal, three pinned Node.js majors, Python, plain Ubuntu, and Arch Linux — each with a different preinstalled toolset

- **Evidence**: Enumerated list in the changelog, corroborated by a table with
  base-image and contents columns on the docs page.
- **Confidence**: settled (first-party enumeration of the current catalog)
- **Quote**: "`vercel/sandbox/universal:latest` is the new default, a rolling
  release on Ubuntu 26.04 with Node.js 24, Python 3.14 with `uv`, the
  `opencode`, `claude-code`, `codex`, and `pi` coding agents, and utilities
  including `git`, `vim`, `nano`, `tmux`, `ripgrep`, `jq`, and `fzf`."
  / "`vercel/sandbox/arch:latest` provides Arch Linux, regularly updated, with
  no Node.js or Python preinstalled. Its large package repository makes it
  useful for agents that install tools on the fly."
- **Our assessment**: The universal image bundling four named coding agents
  (`opencode`, `claude-code`, `codex`, `pi`) directly by default is notable
  for harness engineers: a sandbox created with no image argument is now
  pre-provisioned to run any of those four agents without an install step,
  narrowing the gap between "spin up a sandbox" and "an agent is ready to
  work inside it." The Arch option is explicitly positioned for the opposite
  use case — agents that self-provision tools at runtime rather than relying
  on a curated preinstalled set — which is a concrete two-ends-of-a-spectrum
  design choice (curated batteries-included vs. large-repository
  self-service) offered within the same product.

### Claim 6: The `runtime` property is deprecated but not removed — the SDK types the new `image` property to autocomplete built-in image names while still accepting any string, and existing `runtime`-based code keeps working unchanged

- **Evidence**: Explicit migration-path statement in the changelog.
- **Confidence**: settled (first-party statement of the specific backward-
  compatibility guarantee for the API change)
- **Quote**: "The SDK types the `image` property so built-in images
  autocomplete while any string is still accepted. The previous `runtime`
  property is deprecated, not removed, so existing code keeps working."
- **Our assessment**: This is a soft-migration API design worth naming as a
  pattern: introduce the new, richer surface (`image`, which accepts both
  known catalog names with autocomplete and arbitrary custom-image strings)
  alongside the old one (`runtime`) rather than a hard cutover, so existing
  production code is not broken by the change. The tradeoff is that
  `runtime`-based code silently keeps running on the old model (Amazon
  Linux, `vercel-sandbox` user) rather than being force-migrated, so
  migration is opt-in and could be deferred indefinitely by teams who never
  revisit their `Sandbox.create()` call sites.

### Claim 7: Amazon Linux is not part of the managed image catalog at all — teams that specifically need AL2023 must stay on the deprecated `runtime` property rather than switching to any managed image

- **Evidence**: Explicit statement in the changelog's migration section.
- **Confidence**: settled (first-party statement of a specific catalog gap
  and its stated workaround)
- **Quote**: "Amazon Linux runtimes are not part of the managed image catalog,
  so teams that need AL2023 can stay on `runtime`."
- **Our assessment**: This is a named, self-disclosed limitation rather than
  a temporary gap description — the changelog does not say an Amazon-Linux
  managed image is planned. For any team whose build or deployment tooling
  is hard-dependent on AL2023 specifically (e.g., to match an AWS Lambda
  runtime's userspace), the managed-image migration path documented here
  does not apply, and `runtime` remains the only supported route for that
  requirement.

### Claim 8: Managed images run as a default `ubuntu` or `arch` user with passwordless sudo, replacing the previous `vercel-sandbox` user

- **Evidence**: Explicit statement in the changelog's migration section.
- **Confidence**: settled (first-party statement of the specific default-user
  change)
- **Quote**: "Managed images run as the default `ubuntu` or `arch` user with
  passwordless sudo, rather than the `vercel-sandbox` user."
- **Our assessment**: A default-user rename is a concrete, easy-to-miss
  breaking change for any provisioning script, Dockerfile `USER` directive,
  or file-permission assumption written against the old `vercel-sandbox`
  username — such logic will not error loudly, it will silently run as a
  different user (or fail permission checks scoped to the old username) after
  migrating to a managed image. Passwordless sudo being retained as a
  property of the new default user(s) means the privilege level is unchanged,
  only the username is.

### Claim 9: Managed image source is fully open, published in the public `vercel/sandbox` GitHub repository under `images/`, and community contributions are accepted via pull request

- **Evidence**: Explicit statement in the changelog's opening paragraph,
  corroborated by the docs page's "Release cadence" section with a direct
  link to the `images/` directory.
- **Confidence**: settled (first-party statement of a specific open-source
  publication and contribution model)
- **Quote**: "The source for every image lives in the public
  [vercel/sandbox](https://github.com/vercel/sandbox) repository." / "Images
  are open source, with their source code available on GitHub. To propose
  changes, open a pull request."
- **Our assessment**: This is a concrete supply-chain-auditability property:
  a team relying on `vercel/sandbox/universal:latest` for agent execution can
  inspect the exact Dockerfile-equivalent build definition that produces the
  image their agents run inside, rather than trusting an opaque vendor image.
  Combined with digest pinning (Claim 3), this gives a reproducibility and
  auditability story — pin to a digest, and separately verify what
  Dockerfile-equivalent source produced that digest — that a fully closed
  base-image catalog could not offer.

### Claim 10: Custom images are built locally and pushed to Vercel Container Registry (VCR) with a single CLI command; Sandbox will not use a custom image until VCR reports it "Ready" (an optimized `linux/amd64` build), and `Sandbox.create()` returns an `image_not_ready` error if called before that

- **Evidence**: The docs page's "Custom images" section, including the exact
  push command and a three-state readiness table.
- **Confidence**: settled (first-party specification of the exact build/push
  command and the readiness state machine)
- **Quote**: "First, push an OCI image to Vercel Container Registry (VCR):
  `vercel vcr build docker . my-repository:latest --push`" — followed by a
  readiness table: "`Ready` — VCR prepared the image and Sandbox can use it.
  `Preparing` — VCR is preparing a `linux/amd64` image. `Unoptimized` — The
  image is pullable from VCR, but it is not `linux/amd64` and cannot be used
  in Sandbox. If `Sandbox.create()` returns `image_not_ready`, retry after
  preparation finishes."
- **Our assessment**: This is a specific, actionable operational detail for
  anyone automating sandbox creation immediately after a CI-driven image
  push: a naive "push image, then immediately create sandbox" pipeline can
  race VCR's own `linux/amd64` optimization step and receive `image_not_ready`
  — a retry-with-backoff (or explicit readiness poll) is required between
  push and first use, not just between build and push.

### Claim 11: Vercel Sandbox does not execute a custom image's Docker `ENTRYPOINT` or `CMD`; any long-running process must be started explicitly with `sandbox.runCommand()` after the sandbox boots, and the working directory for commands defaults to the Dockerfile's `WORKDIR` if set, or `/` otherwise

- **Evidence**: An explicit callout box on the docs page's "Custom images"
  section, plus a directly adjacent statement about `WORKDIR` behavior.
- **Confidence**: settled (first-party statement of a specific, easy-to-miss
  runtime-semantics divergence from standard Docker behavior)
- **Quote**: "Vercel Sandbox does not run Docker `ENTRYPOINT` or `CMD` for
  custom images. Start processes with `sandbox.runCommand()` after the
  sandbox is created." / "If the Dockerfile defines `WORKDIR`, new commands
  start in that directory. Otherwise, commands start from `/`."
- **Our assessment**: This is exactly the kind of self-disclosed divergence
  from a practitioner's most likely mental model that MINER.md flags as
  high-value: anyone porting an existing Dockerfile (built for `docker run`,
  where `ENTRYPOINT`/`CMD` normally launches the main process) into a Vercel
  Sandbox custom image will find that the image boots but does nothing until
  `runCommand()` is explicitly called — a difference that will not surface
  as an error, only as an apparently-idle sandbox, unless the practitioner
  already knows this callout exists.

### Claim 12: Image references support six distinct forms — bare name, tag, digest, and team-scoped versions of each, plus an optional fully-qualified `vcr.vercel.com/` registry prefix that works identically with any team-scoped form — and images can be shared with a specific team or made public to any Vercel team, which is the same mechanism Vercel uses internally to publish VMI itself

- **Evidence**: The docs page's "Image references" table, plus an explicit
  statement connecting the sharing mechanism to VMI's own distribution.
- **Confidence**: settled (first-party specification of the exact reference
  grammar and an explicit statement that VMI uses the general-purpose sharing
  mechanism rather than special-cased internal plumbing)
- **Quote**: "A team can mark a VCR repository as public to give any other
  team read access to its images. Anyone on Vercel can then create sandboxes
  from the repository's images with a team-scoped reference... Vercel uses
  that approach to make Vercel Managed Images (VMI) accessible to any team."
- **Our assessment**: The fact that VMI is distributed through the same
  public-repository-sharing primitive available to any Vercel customer (not
  a private, Vercel-only distribution channel) is a useful signal for teams
  considering publishing their own shared base images internally across
  projects or teams — the mechanism is proven at the scale of "every Vercel
  customer's default sandbox image" and is not a second-class or
  internal-only capability.

## Concrete Artifacts

### Managed image catalog (verbatim table, from the docs page)

```
| Image                              | Base                    | Contents                                                  |
|-------------------------------------|--------------------------|------------------------------------------------------------|
| vercel/sandbox/universal:latest     | vercel/sandbox/ubuntu    | Node.js LTS (24), Python (3.14), coding agents, utilities  |
| vercel/sandbox/node:22|24|26        | vercel/sandbox/ubuntu    | Node.js (major pinned), pnpm                                |
| vercel/sandbox/python:3.14          | vercel/sandbox/ubuntu    | Python 3.14 (pinned), pip, venv, uv                         |
| vercel/sandbox/arch:latest          | archlinux:latest         | Arch Linux, yay (AUR), base-devel, git                      |
| vercel/sandbox/ubuntu:latest        | ubuntu:26.04             | Ubuntu + sudo                                               |
```
Source: https://vercel.com/docs/sandbox/concepts/images — "Vercel Managed Images" section.

### Image reference resolution forms (verbatim table, from the docs page)

```
| Reference                                                  | What it resolves                                     |
|-------------------------------------------------------------|-------------------------------------------------------|
| my-repository                                                | The `latest` tag in the authenticated project          |
| my-repository:v1                                             | A specific tag in the authenticated project            |
| my-repository@sha256:...                                     | A specific digest in the authenticated project         |
| team-slug/project-slug/my-repository                         | The `latest` tag in the referenced team and project    |
| team-slug/project-slug/my-repository:v1                      | A specific tag in the referenced team and project      |
| team-slug/project-slug/my-repository@sha256:...              | A specific digest in the referenced team and project   |
| vcr.vercel.com/team-slug/project-slug/my-repository:v1       | Same as the team-scoped reference, fully qualified URL |
```
Source: https://vercel.com/docs/sandbox/concepts/images — "Image references" section.

### SDK usage — selecting a managed image (verbatim, from the changelog)

```typescript
import { Sandbox } from '@vercel/sandbox';

const sandbox = await Sandbox.create({
  image: 'vercel/sandbox/universal:latest',
});
```
Source: https://vercel.com/changelog/vercel-sandbox-managed-images

### SDK usage — pinning to a digest, or selecting a non-default catalog image (verbatim, from the docs page)

```ts filename="index.ts"
import { Sandbox } from '@vercel/sandbox';

const sandbox = await Sandbox.create({
  image: 'vercel/sandbox/universal@sha256:...', // Use a specific digest of the universal image
  // image: 'vercel/sandbox/node:24',           // Use the Node.js 24 image
  // image: 'vercel/sandbox/ubuntu',            // Use the latest Ubuntu image
});
```
Source: https://vercel.com/docs/sandbox/concepts/images — "Vercel Managed Images" section.

### Custom image build, push, and use (verbatim commands, from the docs page)

```bash
# Push an OCI image to Vercel Container Registry (VCR)
vercel vcr build docker . my-repository:latest --push
```

```ts filename="index.ts"
import { Sandbox } from '@vercel/sandbox';

const sandbox = await Sandbox.create({
  image: 'my-repository:latest',
});

try {
  const result = await sandbox.runCommand('pwd');
  console.log(await result.stdout());
} finally {
  await sandbox.stop();
}
```
Source: https://vercel.com/docs/sandbox/concepts/images — "Custom images" section.

### Custom-image readiness states (verbatim table, from the docs page)

```
| Status      | Meaning                                                                              |
|-------------|----------------------------------------------------------------------------------------|
| Ready       | VCR prepared the image and Sandbox can use it.                                         |
| Preparing   | VCR is preparing a linux/amd64 image.                                                   |
| Unoptimized | The image is pullable from VCR, but it is not linux/amd64 and cannot be used in Sandbox.|
```
Source: https://vercel.com/docs/sandbox/concepts/images — "Custom images" section.

## Cross-References

### Cross-reference verification notes
`blog-vercel-herdr-agent-sandboxes.md`, `blog-anthropic-claude-managed-agents-selfhosted.md`,
`blog-cursor-cloud-agent-dev-environments.md`, and `docs-github-copilot-cca-startup-custom-images.md`
were re-read in full during this extraction (MINER.md §4b), and every claim
number cited below was located and confirmed against that note's own
numbered `### Claim N:` headings in document order before writing this
section.

- **Corroborates**:
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 3 ("You also
    control the compute: resource sizing and the runtime image are set on
    your side, so agents running compute-heavy work such as long builds or
    image generation get the CPU, memory, and capacity the task needs"):
    that note documents
    Vercel Sandbox as one of four pluggable providers for Claude Managed
    Agents, with "runtime image" control described only abstractly from the
    Anthropic integration's point of view. This source is the concrete,
    Vercel-native specification of exactly what "the runtime image" means for
    Vercel Sandbox as of August 2026: a five-image managed catalog, or a
    custom OCI image built and pushed to VCR — filling in the mechanism
    behind that note's abstract "set on your side" claim.
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 8 (Vercel
    Sandbox firewall injects credentials at the network boundary so they
    never enter the sandbox): unaffected by, but running on top of, the image
    layer this source documents — the credential-injection guarantee that
    note describes applies regardless of which managed or custom image the
    sandbox boots from, since it is enforced at the network boundary, not
    inside the image.

- **Extends**:
  - `blog-vercel-herdr-agent-sandboxes.md`: that note documents two
    per-agent isolation models native to Vercel Sandbox (one sandbox per
    agent, or one sandbox with per-agent Unix users) but does not touch the
    base-image/runtime layer — its own `Sandbox.create()` code example
    (Concrete Artifacts, "Multi-user isolation SDK example") calls
    `Sandbox.create()` with no `image` or `runtime` argument at all, and that
    note was published August 6, 2026, four days before this changelog. Per
    Claim 1 of this source, a sandbox created the same way today (Sandbox SDK
    v3+) now defaults to the Ubuntu-based `vercel/sandbox/universal:latest`
    image rather than whatever the prior implicit default was — the same
    isolation mechanics that note documents (createUser/createGroup, or a
    full sandbox per Herdr-managed agent) now run on top of a different
    default base image than when that note was written. This source and
    that one together give a fuller picture of Vercel Sandbox's two
    orthogonal configuration axes: how many agents share a sandbox
    (isolation layer, that note) and what base environment the sandbox boots
    from (image layer, this note).
  - `docs-github-copilot-cca-startup-custom-images.md` Claim 2 (GitHub
    reduces Copilot cloud agent cold-start latency by prebuilding the agent's
    runtime environment as a custom GitHub Actions image): both sources
    document a vendor using a prebuilt-image strategy to avoid runtime
    dependency installation for agent sandboxes, but the two differ in scope
    and audience — GitHub's optimization is platform-side, automatic, and
    not user-configurable ("no configuration steps, prerequisites, or opt-in
    instructions"), while Vercel's managed images are a user-selectable
    catalog (Claim 5 of this source) plus a fully custom, user-buildable
    alternative (Claim 10). This source is more relevant to a harness
    engineer who wants direct control over the base environment; the GitHub
    source documents an equivalent benefit (faster cold start via
    prebuilding) delivered with zero configuration surface.
  - `blog-cursor-cloud-agent-dev-environments.md` Claim 7 (Cursor can
    auto-generate a Dockerfile by inspecting a repository, in private beta)
    and Claim 9 (on configuration failure, Cursor falls back to "a base image
    with clear warning signs" so agents keep running): this source documents
    a structurally different philosophy for the same underlying problem
    ("what environment does my agent's sandbox start in") — Vercel offers a
    small, curated, versioned catalog of general-purpose images (Claim 5)
    plus an explicit, manually-triggered custom-image build/push workflow
    (Claim 10), with no repo-inspection or auto-generation step and no
    automatic-fallback-on-failure behavior described anywhere in either
    fetched page. Neither source claims the other's approach is wrong; they
    represent different points on a spectrum from "vendor infers your
    environment automatically" (Cursor) to "you pick from a maintained
    catalog or bring your own fully custom image" (Vercel) — a conditioning
    variable rather than a contradiction (MINER.md §4a "when NOT to file").

- **Contradicts**: No contradiction issue filed. No existing corpus note
  makes a claim about Vercel Sandbox's default OS, default user, or image
  model that this source's claims oppose — the only prior corpus code
  example using Vercel Sandbox's implicit default
  (`blog-vercel-herdr-agent-sandboxes.md`) simply predates this change and is
  noted above as an "Extends" relationship (a before/after timeline point),
  not a factual disagreement.

- **Novel** (what this note adds that no prior source covers):
  - **A named, versioned, open-source base-image catalog for an agent
    sandbox product** (Claims 1, 5, 9): no prior corpus source documents a
    sandbox vendor publishing the actual build source for its default agent
    execution environments in a public repository with an open
    pull-request-based contribution model.
  - **Digest-pinning as an explicit opt-out of automatic security updates**
    (Claims 3, 4): the specific tradeoff — rolling tags get automatic OS/
    dependency patches, but a team can trade that freshness for full
    reproducibility by pinning to a SHA digest — is new to the corpus as a
    named, vendor-endorsed mechanism for agent sandboxes specifically.
  - **A default-user and default-OS rename as a breaking-but-soft-migrated
    change** (Claims 2, 6, 7, 8): the specific combination of "the default
    changed materially (OS, username) but the old API path (`runtime`) still
    works unchanged" is a concrete API-evolution pattern not previously
    documented in the corpus for a sandbox product.
  - **`ENTRYPOINT`/`CMD` non-execution for custom images** (Claim 11): no
    prior corpus source documents a sandbox product that accepts standard
    OCI/Docker images but explicitly does not honor two of Docker's most
    basic process-launch directives, requiring an explicit post-boot command
    invocation instead.
  - **A three-state readiness gate between image push and first sandbox use**
    (Claim 10): the specific `Ready`/`Preparing`/`Unoptimized` state machine,
    and the `image_not_ready` error a caller can hit by racing it, is a new,
    concrete operational detail for anyone scripting CI-driven custom-image
    publishing into sandbox creation.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "which base image" as a named,
  separate configuration decision for teams building on Vercel Sandbox,
  distinct from the isolation-granularity decision already documented from
  `blog-vercel-herdr-agent-sandboxes.md` (Claims 1, 8 of that note). Document
  the five-image catalog (Claim 5 of this source) as a concrete starting-
  point menu, and the digest-pinning vs. rolling-tag tradeoff (Claim 3) as
  the relevant reproducibility-vs.-freshness axis. Note the preinstalled
  coding agents in the universal image (`opencode`, `claude-code`, `codex`,
  `pi`) as a specific, checkable fact for teams evaluating whether a given
  sandbox's default image already supports their preferred coding agent
  without a custom build.

- **Chapter 02 (Harness Engineering)**: Document the `runtime` → `image`
  migration (Claim 6) as a concrete example of a soft, non-breaking API
  migration pattern worth naming explicitly: the old property keeps working,
  but its underlying environment (Amazon Linux, `vercel-sandbox` user) is
  frozen while the new default (Ubuntu, `ubuntu`/`arch` user) receives
  ongoing security updates — meaning staying on the old path is a security-
  update tradeoff, not merely an API-style preference. Flag the specific
  breaking details (Claims 2, 7, 8: OS change, no Amazon Linux managed image,
  default-user rename) as concrete migration-checklist items for any team
  currently relying on `runtime`'s implicit environment characteristics.

- **Chapter 06 (Security Threat Model)**: Add the open-source, publicly
  auditable managed-image source (Claim 9) alongside digest pinning (Claim 3)
  as a concrete supply-chain-auditability pattern for agent sandbox base
  images — a team can both pin to an exact digest for reproducibility and
  independently inspect the Dockerfile-equivalent source that produced that
  digest, rather than trusting an opaque vendor image. This is a stronger
  auditability position than a closed-source base-image catalog would offer,
  worth naming as a differentiator when evaluating sandbox vendors on supply-
  chain grounds.

## Extraction Notes

1. **Verbatim-quote confidence.** The changelog was fetched twice: an initial
   fetch and a second fetch with an explicit verbatim-reproduction prompt
   (per MINER.md §2a's caution about WebFetch's summarizing pass); both
   returned structurally consistent text, and the second, more explicit fetch
   is the source of every quote in this note from the changelog page. The
   linked images concept page (`vercel.com/docs/sandbox/concepts/images`)
   was fetched once with an explicit verbatim-reproduction prompt and returned
   what appears to be the page's underlying markdown/frontmatter source
   (including a YAML frontmatter block, docsgraph link metadata, and exact
   Markdown tables), which is consistent with a non-summarized, faithful
   reproduction; that fetch is the source of every quote and table attributed
   to the docs page in this note.
2. **GitHub repository not used as a quote source.** `github.com/vercel/sandbox`
   was fetched twice: once with a general description prompt (which returned
   a page clearly labeled by the model itself as a "README Content Summary,"
   i.e., paraphrased) and once with an explicit request for the verbatim raw
   README text, to which the fetch explicitly responded that it could not
   access the raw README content and offered only a paraphrased description
   of visible topics, recommending the `raw.githubusercontent.com` URL for a
   verbatim copy instead. Per MINER.md §2a, no quote or claim evidence in this
   note is drawn from either GitHub fetch; the only facts sourced from the
   GitHub repository's existence are the two facts independently and
   explicitly stated by the changelog and docs page themselves (the repo is
   public, and images live under an `images/` directory), both already
   captured as direct quotes from those two first-party pages in Claim 9.
3. **No other sub-pages followed.** The docs page links to several related
   pages (Vercel Container Registry getting-started and public/shared-
   repository docs, a "Running Docker on Vercel" KB guide, an "install system
   packages" KB guide, and an Eve-concepts page). These were not fetched
   because the docs page's own "Custom images" and "Image references"
   sections already provide the complete command sequence, readiness states,
   and reference-resolution grammar needed to use custom and shared images —
   the linked pages appeared to cover general VCR mechanics not specific to
   Sandbox, which is outside this issue's scope per the Prospector's stated
   key question (managed-image customization for agent sandboxes
   specifically, not general container-registry usage).
4. **No customer or adoption evidence.** Neither fetched page names a
   customer, gives a usage metric, or cites independent security review or
   benchmarked boot-time data. All claims are first-party vendor
   documentation of a shipped feature. Overall confidence is rated
   "emerging" for this reason, despite individual claims being rated
   "settled" (unambiguous, internally consistent, first-party descriptions of
   specific, shipping mechanisms with concrete version numbers, command
   syntax, and named states).
5. **No contradictions filed.** Reviewed `blog-vercel-herdr-agent-sandboxes.md`,
   `blog-anthropic-claude-managed-agents-selfhosted.md`,
   `blog-cursor-cloud-agent-dev-environments.md`, and
   `docs-github-copilot-cca-startup-custom-images.md` in full. No existing
   corpus note makes a claim that materially opposes anything in this source
   at the MINER.md §4a filing threshold; the closest candidate (Cursor's
   auto-generated-Dockerfile philosophy vs. Vercel's curated-catalog-plus-
   manual-custom-image philosophy) is a conditioning/design-philosophy
   difference between two vendors, not two claims about the same mechanism
   disagreeing — no contradiction issue filed.
