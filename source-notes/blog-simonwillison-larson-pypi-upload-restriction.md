---
source_url: https://simonwillison.net/2026/Jul/23/seth-larson/
source_type: blog-post
title: "Quoting Seth Larson"
author: Simon Willison (quoting Seth Larson, PyPI Developer-in-Residence)
date_published: 2026-07-23
date_extracted: 2026-07-28
last_checked: 2026-07-28
status: current
confidence_overall: settled
issue: "#2267"
---

# Quoting Seth Larson

> Simon Willison's "quotation" post relays Seth Larson's PyPI blog
> announcement that PyPI now rejects new file uploads to releases older
> than 14 days, a concrete supply-chain hardening measure designed to
> stop compromised publishing tokens or CI workflows from retroactively
> poisoning old, widely-installed package releases.

## Source Context

- **Type**: blog-post (Simon Willison's "quotation" post type — a single
  blockquote plus attribution and a link to the primary source, with
  minimal original commentary; auto-discovered via the `simon-willison`
  trusted feed). The primary source is Seth Larson's post on the official
  PyPI blog, `https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/`,
  published July 22, 2026 and credited to "Seth Larson and Mike Fiedler."
  This note reads both Willison's post and the linked PyPI blog post
  directly, since Willison's post is a thin pointer to the substantive
  content.
- **Author credibility**: Seth Larson is PyPI's Developer-in-Residence
  (funded security/packaging role); Mike Fiedler is credited in the same
  post as PyPI's Safety & Security Engineer. Both are first-party
  maintainers of PyPI infrastructure describing a policy they personally
  shipped, making this the most direct possible source for what the
  change is and why it was made. Simon Willison, a designated
  `trusted-feed` source in this repo, adds no independent analysis here —
  he is purely curating and amplifying the PyPI announcement.
- **Scope**: Covers the specific mechanics and rationale of PyPI's new
  14-day upload-restriction policy: the threat it defends against, the
  incident that prompted renewed discussion, the impact-analysis data
  used to justify the change, and its relationship to a future "Upload
  2.0 API." Does not cover: how the restriction is technically enforced
  (e.g., specific error codes/messages returned to `twine upload`), any
  rollout/monitoring plan, or PyPI's broader security roadmap beyond this
  one change.

## Extracted Claims

### Claim 1: PyPI now rejects new file uploads to any release that is older than 14 days
- **Evidence**: Stated directly, identically, in both Willison's quotation
  post and the source PyPI blog post as the core policy description.
- **Confidence**: settled (a shipped, first-party-confirmed infrastructure
  change, not a proposal)
- **Quote**: "The Python Package Index (PyPI) now rejects new files being uploaded to releases that are older than 14 days."
- **Our assessment**: This is an unambiguous, checkable behavioral change
  to PyPI's upload API. It converts every release, once past its 14-day
  window, from "open" (can still receive new files, e.g. added wheels for
  new platforms) to effectively frozen. Practitioners who currently add
  wheels to old releases post-hoc (e.g., backfilling a new Python version
  or platform build weeks after the initial release) will need to cut a
  new release instead.

### Claim 2: The restriction exists specifically to prevent old, long-stable releases from being poisoned if a project's publishing tokens or CI workflows are compromised
- **Evidence**: The stated rationale in both posts, presented as the
  primary justification for the change.
- **Confidence**: settled (stated design intent from the team that shipped
  the control)
- **Quote**: "This restriction was put in place to prevent old and long-stable releases from being poisoned in case publishing tokens or workflows of PyPI projects were compromised."
- **Our assessment**: This is a specific, well-scoped supply-chain threat
  model: an attacker who steals a publish token (or compromises a CI
  workflow with publish permissions) previously had a wide blast radius —
  they could push a malicious file to *any* release of the project,
  including old, trusted, widely-pinned versions that downstream
  consumers assume are stable and won't change. Restricting uploads to
  a 14-day window shrinks that blast radius to only the most recent
  release, where users are more likely to notice unexpected new
  activity. This is the same class of defense as "release immutability"
  controls seen elsewhere in package ecosystems, applied at PyPI scale.

### Claim 3: As of the announcement, PyPI is not aware of this specific attack (uploading new files to an old release) having actually been exploited — the restriction is preemptive
- **Evidence**: A direct, self-reported statement from the PyPI team
  about their own knowledge of abuse to date.
- **Confidence**: settled as a statement of PyPI's current knowledge, but
  inherently unverifiable from outside PyPI's own incident visibility —
  "not yet been abused" is a claim about what PyPI has detected, not a
  guarantee that no undetected instance exists.
- **Quote**: "As far as we are aware this has not yet been abused, but there is no technical reason beyond that attackers weren't aware it was possible."
- **Our assessment**: This is the most important nuance in the whole
  announcement: PyPI is explicitly framing this as closing a *theoretical*
  but technically real gap before it gets exploited, not responding to a
  confirmed incident of this exact form. The team is candid that the only
  thing preventing exploitation to date may have been attacker
  unawareness, not any inherent difficulty. That's a notable inversion of
  the usual "we're patching what already happened to us" security-fix
  narrative — this is anticipatory hardening.

### Claim 4: The internal discussion to restrict old-release uploads was restarted in March 2026 after the compromise of the popular LiteLLM and Telnyx packages
- **Evidence**: Stated as historical context for why the restriction was
  finally implemented, in the source PyPI blog post.
- **Confidence**: settled (named, dated, specific incident cited as the
  proximate trigger for renewed action)
- **Quote**: "The discussion was restarted in March 2026 after the popular packages LiteLLM and Telnyx were compromised."
- **Our assessment**: This grounds the policy in a concrete, named
  incident rather than abstract risk modeling — two specific,
  widely-depended-on packages (LiteLLM, an LLM-provider-abstraction
  library heavily used in AI-agent tooling, and Telnyx) were actually
  compromised, and that event is what moved a previously-discussed idea
  from proposal to shipped policy. This is useful evidence for the
  "incidents drive supply-chain controls" pattern this guide's Ch06
  threat model should reflect: proposals for hardening measures often
  sit dormant until a concrete compromise forces action.

### Claim 5: Impact analysis found that only 56 of roughly 15,000 scanned projects had published a Python-3.14-compatible wheel more than 14 days after their release date, informing the decision that the restriction has low disruption cost
- **Evidence**: A specific dataset cited in the PyPI blog post as
  justification that the 14-day window would not meaningfully break
  legitimate, existing publishing patterns.
- **Confidence**: emerging (a single retrospective query result, presented
  by the team making the change, not independently reproduced by this
  Miner — the underlying query/methodology was not directly verified)
- **Quote**: "only 56 projects of 15,000 had published a 3.14-compatible wheel more than 14 days after a release was available."
- **Our assessment**: This is the kind of quantified pre-rollout impact
  analysis that makes a security restriction credible rather than
  disruptive-by-fiat: PyPI checked how many real projects would be
  affected before shipping, found the number small (56/15,000 ≈ 0.37%),
  and used that to justify accepting the disruption. The post frames the
  policy consensus as: for the small remaining set of affected projects,
  "it's acceptable to require users to bump to the next version" rather
  than carve out an exception.

### Claim 6: The topic was formally discussed at the Packaging Summit at PyCon US 2026 before Seth Larson's patch implementing the restriction was merged on July 8, 2026
- **Evidence**: Stated directly in the PyPI blog post as part of the
  change's process/timeline.
- **Confidence**: settled (specific named venue and merge date)
- **Quote**: "This topic was brought to the Packaging Summit at PyCon US 2026...Seth moved forward with a patch which was merged July 8th, 2026."
- **Our assessment**: This shows the change went through a public
  community-governance venue (the Packaging Summit) rather than being a
  unilateral PyPI-admin decision, which matters for how durable and
  broadly-endorsed the policy is likely to be. It also establishes a
  clear timeline: PyCon US 2026 discussion → July 8, 2026 merge → July
  22, 2026 public announcement → July 23, 2026 Willison amplification —
  useful for dating this control relative to other 2026 supply-chain
  events in the corpus (e.g., the LiteLLM/Telnyx compromise in Claim 4,
  and the OpenAI/Hugging Face incident documented in
  `blog-simonwillison-openai-hf-cyberattack.md`, which also occurred in
  July 2026).

### Claim 7: PyPI frames the 14-day restriction as a stopgap ahead of a future "Upload 2.0 API" that will provide explicit semantics for releases being "closed" rather than "open"
- **Evidence**: Stated in the PyPI blog post as forward-looking context
  for where this fits in PyPI's broader upload-API design direction.
- **Confidence**: emerging (a stated future intent/roadmap item, not a
  shipped feature — no timeline given for Upload 2.0 API delivery)
- **Quote**: "Upload 2.0 API provides semantics for releases that are 'closed' instead of 'open'."
- **Our assessment**: This reframes the 14-day rule as an interim,
  time-based proxy for a concept (explicit release closure) that PyPI
  intends to make a first-class, deliberate action in a future API
  version. Practitioners should read the 14-day window as a heuristic
  stopgap, not the final design — a project publisher will eventually be
  able to (or be required to) explicitly close a release rather than
  relying on a rolling time cutoff. This claim has no confirmed shipping
  date and should not be treated as settled practice.

### Claim 8: Simon Willison's post adds no independent security analysis of his own — it is a pure amplification of the PyPI announcement via his "quotation" post format
- **Evidence**: Direct comparison of Willison's post content against the
  PyPI blog post shows Willison's contribution is the blockquote,
  attribution, and tags only; no additional framing or opinion is added.
- **Confidence**: settled (structural observation about the post itself,
  independently confirmed by fetching both pages)
- **Quote**: (no direct quote for this claim's core assertion — this is
  a structural observation, not a quoted statement; see Willison's
  verbatim blockquote reproduced under Claim 1 and Concrete Artifacts)
- **Our assessment**: Consistent with the pattern seen in
  `blog-simonwillison-ptacek-open-weights-pentest.md` (also a "quotation"
  post), Willison's curatorial signal (choosing to amplify this
  particular PyPI announcement to his trusted-feed audience) is itself
  the primary editorial value here, not any original analysis. The
  underlying evidentiary weight of this note rests entirely on the PyPI
  blog post as first-party source, not on Willison's framing.

## Concrete Artifacts

### Full quoted blockquote, Willison's post (verbatim, per WebFetch verbatim-mode extraction)

```
Source: https://simonwillison.net/2026/Jul/23/seth-larson/

"The Python Package Index (PyPI) now rejects new files being uploaded
to releases that are older than 14 days. This restriction was put in
place to prevent old and long-stable releases from being poisoned in
case publishing tokens or workflows of PyPI projects were compromised.
As far as we are aware this has not yet been abused, but there is no
technical reason beyond that attackers weren't aware it was possible."

— Seth Larson, PyPI blog
Posted: 23rd July 2026 at 4:50 am
Tags: packaging, pypi, python, supply-chain, seth-michael-larson
```

### Primary source link and key facts (PyPI blog post)

```
Source: https://blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/
Published: July 22, 2026
Credited to: Seth Larson and Mike Fiedler (PyPI Safety & Security Engineer)

Key facts extracted:
- Policy: uploads of new files to releases >14 days old are now rejected
- Threat mitigated: publishing-token or CI-workflow compromise used to
  retroactively poison old, stable releases
- Trigger for renewed discussion: LiteLLM and Telnyx package compromises,
  March 2026
- Impact analysis: 56 of ~15,000 scanned projects had published a
  Python-3.14-compatible wheel >14 days post-release
- Process: discussed at the Packaging Summit, PyCon US 2026; patch
  merged July 8, 2026
- Future direction: "Upload 2.0 API" to add explicit "closed" vs "open"
  release semantics
```

## Cross-References

- **Corroborates**: `blog-simonwillison-openai-hf-cyberattack.md` — that
  note's Claim 10 records Hugging Face stating it "found no evidence of
  tampering with public models, datasets, Spaces, or the software supply
  chain" after its July 2026 breach; this note documents a different
  organization (PyPI) making an anticipatory infrastructure change to
  prevent a specific supply-chain compromise scenario before it happens.
  Both notes reflect the same broader 2026 pattern of infrastructure
  operators treating credential/token compromise as a live, high-priority
  threat vector, though they address different attack surfaces (model/
  dataset hosting vs. package registry uploads) and neither directly
  supports or tests the other's specific claims.
- **Contradicts**: None identified. No existing corpus source makes
  claims about PyPI upload policy, release immutability, or publishing-
  token compromise that this note's claims conflict with.
- **Extends**: `docs-ghaw-dependabot.md` — that note documents how GitHub
  Agentic Workflows generates and monitors dependency manifests (including
  `requirements.txt` for pip-installed tools) for security updates, which
  is a *consumer-side* supply-chain control (detecting vulnerable pinned
  versions after the fact). This note documents a complementary
  *registry-side* control (preventing a compromised release from being
  silently modified in the first place) at the infrastructure layer
  Dependabot's pip ecosystem ultimately depends on.
- **Novel**: The PyPI 14-day upload-restriction policy itself; the named
  LiteLLM/Telnyx March 2026 compromise as the proximate trigger; the
  56/15,000 impact-analysis figure; and the "Upload 2.0 API" open/closed
  release semantics roadmap item are all new to this corpus. No existing
  source note documents package-registry-level (as opposed to CI/Actions-
  level) supply-chain hardening controls.

## Guide Impact

- **Chapter 06 (Security Threat Model)**: Chapter 06 already has a
  section on "The MCP supply chain: rug-pull tool redefinition" (around
  the registry-allowlist discussion) but has no content on package-
  registry-level defenses against publishing-credential compromise. This
  source supports adding a concrete, named example to the supply-chain
  section: package registries (PyPI as the documented case here) are
  moving toward time-windowed or explicit release-closure controls to
  limit the blast radius of a compromised publish token — i.e., even if
  an attacker steals credentials with publish rights, they can no longer
  silently modify old, already-trusted, widely-pinned releases; the
  attack surface narrows to newly-published versions where anomalous
  activity is more likely to be noticed. Recommend citing this as a
  specific instance of a general pattern practitioners should recognize:
  "trust in a specific version" and "trust in the publisher's ongoing
  credential hygiene" are different things, and registry-level immutability
  windows are one architectural mitigation for the gap between them.
- **Chapter 06 (Security Threat Model) — incident-driven hardening
  pattern**: The LiteLLM/Telnyx compromise (Claim 4) prompting this
  change is a specific, citable example of the general pattern that
  security controls in package ecosystems tend to ship after a named
  incident reopens a previously-dormant proposal, rather than purely from
  proactive risk modeling. Worth a brief mention alongside other
  incident-driven hardening examples already in or being added to Ch06.

## Extraction Notes

- **Two-hop extraction**: Willison's post (`simonwillison.net/2026/Jul/23/seth-larson/`)
  is a thin "quotation" post; nearly all substantive content in this note
  comes from following its linked primary source, the PyPI blog post at
  `blog.pypi.org/posts/2026-07-22-releases-now-reject-new-files-after-14-days/`.
  Both were fetched directly via WebFetch with verbatim-extraction
  prompts; Claims 1–3 and 8 are confirmed from Willison's post itself,
  Claims 2–7 draw additional detail from the PyPI blog post.
- **Quote extraction caveat**: WebFetch content is processed by a small
  model before being returned to this Miner, so quotes were extracted
  via multiple independently-phrased, verbatim-only prompts against the
  same URL and cross-checked for consistency across calls before being
  recorded here. One WebFetch call against the PyPI blog post declined to
  reproduce the full article text due to a copyright-reproduction
  guideline, which is why this note relies on multiple short, targeted
  verbatim-quote requests rather than one full-text fetch.
- **Not independently verified**: The specific byline/date of the PyPI
  blog post's individual author attribution (vs. the "Seth Larson and
  Mike Fiedler" credit line) and any FAQ/exception carve-outs were
  checked and found absent from the post — the Miner confirmed this
  negative (no stated exceptions for hotfixes/security patches) rather
  than assuming it. The BigQuery-style impact-analysis methodology behind
  the 56/15,000 figure (Claim 5) was not independently reproduced.
- **Confidence set to `settled`**: The core policy (Claim 1) and its
  stated threat-model rationale (Claim 2) are a shipped, first-party-
  confirmed infrastructure change on critical Python ecosystem
  infrastructure, not a proposal or rumor. Individual claims with more
  uncertainty (the impact-analysis methodology, the unshipped Upload 2.0
  API) are marked `emerging` at the claim level.
