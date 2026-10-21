---
source_url: https://ghuntley.com/patch/
source_type: blog-post
title: "patch the planet"
author: Geoffrey Huntley
date_published: 2026-10-20
date_extracted: 2026-10-21
last_checked: 2026-10-21
status: current
confidence_overall: anecdotal
issue: "#4252"
---

# patch the planet

> A short first-person incident write-up in which an agent identifies, patches, and schedules its own back-out of a fleet-wide NixOS workaround for a CA compromise, using a self-expiring "Temporary reminder" section in AGENTS.md as the scheduling mechanism.

## Source Context

- **Type**: blog-post (ghuntley.com; the page byline shows 21 Oct 2026, the feed entry and the author's tweet are dated 20 Oct 2026; we use the feed date).
- **Author credibility**: Geoffrey Huntley, known for agentic-coding techniques (Ralph loops); operates his own NixOS fleet. Claims rest on one personal incident, not measurements.
- **Scope**: One incident (eMudhra intermediate CA compromise, "revealed two hours ago" at writing), one prompt, one AGENTS.md reminder block. Does NOT cover: the agent's actual output (the post's "results" are an embedded image not readable as text), whether the scheduled revert ever ran, how an agent is triggered on the future date, or any quantified cost. The incident details are context only; the durable item is the reminder pattern.

## Extracted Claims

### Claim 1: An agent can be prompted to write a dated "reminder" into AGENTS.md that causes it to back out a temporary workaround later
- **Evidence**: A full reminder block is shown verbatim in the post (see Concrete Artifacts). No evidence the revert has executed; the date (2026-10-22) is after publication.
- **Confidence**: anecdotal
- **Quote**: "You can prompt an agent to update the AGENTS.MD to automatically back out these patches, let's say in five days from now, just by using the AGENTS.MD as a reminder"
- **Our assessment**: Novel and concrete as a pattern: the workaround and its own exit criteria are created together, so the debt has a recorded owner and condition. But AGENTS.md is passive context: it only fires if some session happens to start on/after the date and reads it. The post does not describe any scheduler, so "automatically" is overstated until shown to work. Treat as an untested idea.

### Claim 2: The reminder should encode an objective re-check condition, a retry cadence, an exact cleanup list, and a verification step, not just a date
- **Evidence**: The shown block names the upstream condition (channel contains nixpkgs commit `7816d39`), a command to test it, "check again two days later", files to delete/edit, what to keep, a post-revert verification, and a final instruction to delete the section itself.
- **Confidence**: anecdotal
- **Quote**: "Then verify that the built host and guest bundles still lack the four roots, and delete this section."
- **Our assessment**: This is the most reusable part. The structure (trigger condition, poll interval, removal scope, explicit keep-list, verify-after-removal, self-delete) is a good template for any temporary agent-managed change, independent of Nix. Whether the agent follows it faithfully is unreported.

### Claim 3: Nix's single source of truth lets one patch fix transitive dependencies across a whole fleet, which is why the author can respond quickly
- **Evidence**: Assertion plus an embedded screenshot of agent results (not extractable). No timings.
- **Confidence**: anecdotal
- **Quote**: "One patch fixes the entire fleet and its transitive dependencies. Patch, commit, and autodeploy your fleet 🍻"
- **Our assessment**: Restates Claim 7 of the earlier Nix note with a real-world incident rather than an illustrative OpenSSL snippet. Note the reminder itself shows the fix was not only a Nix overlay: it mentions a `public-trust.nix` module and a separate `rustls-webpki` update, i.e. several hand-wired changes. "Easiest security patch" is the author's feeling, not a measurement.

### Claim 4: A single prompt moved from "am I affected?" to a plan to a fix
- **Evidence**: The prompt is quoted; the agent's results are shown only as an image.
- **Confidence**: anecdotal
- **Quote**: "okay is my nixos for my fleet affected by https://emudhra.we-have-a-problem.com/?"
- **Our assessment**: Plausible given a declarative fleet definition the agent can read, but unverifiable here. The relevant condition is that the fleet state is code the agent can inspect, not Nix specifically.

### Claim 5: Wasteful, worldwide cost is being incurred by teams manually patching transitive dependencies
- **Evidence**: None; estimate asserted.
- **Confidence**: anecdotal
- **Quote**: "Tens of millions of dollars (if not more) in productivity are being lost worldwide right now as everyone tries to patch their transitive dependencies."
- **Our assessment**: Unsupported hyperbole; also "almost impossible without Nix" is overstated (other lockfile/SBOM approaches exist). Not citable.

### Claim 6: Ownership and speed of response matter more as offensive models attack continuously
- **Evidence**: Opinion.
- **Confidence**: anecdotal
- **Quote**: "To defend, you need more inferencing capability than the attacker, and you also need to respond rapidly."
- **Our assessment**: A threat-model assertion with no data. Compatible with, but not evidence for, an agent-assisted patch loop. Also: "If you build something, you own it, including all the dependencies you rely on." is a sound maxim but a framing, not a finding.

### Claim 7: Scheduling the back-out means the workaround adds little lasting tech debt
- **Evidence**: Prediction made before the revert date.
- **Confidence**: anecdotal
- **Quote**: "the best part is I won't carry this tech debt for long because an agent will automatically back it out in a couple of days."
- **Our assessment**: Untested prediction. Risk (ours): unattended automatic removal of a security mitigation is a failure mode if the condition check is wrong; the block mitigates with a verify step, but a human review gate is absent.

## Concrete Artifacts

Source: ghuntley.com/patch/ — the AGENTS.md reminder section as published.

```markdown
## Temporary reminder: eMudhra root blacklist (from 2026-10-22)

On or after 2026-10-22, check whether the `nixos-26.05` channel contains nixpkgs
commit `7816d39` (the backported `security/ca.nix` distrust of the eMudhra roots), e.g.
`nix eval --raw --refresh --impure --expr '(builtins.getFlake "github:NixOS/nixpkgs/nixos-26.05").rev'`
then `git merge-base --is-ancestor`. If it does not, check again two days later.
Once it does, back out the fleet-wide workaround: update the `nixpkgs` pin to include
it, delete `nix/domains/system/public-trust.nix` (contract `fleet-distrust-emudhra-roots`)
and its imports in `nix/domains/system/catalog.nix`,
`nix/domains/artifacts/guest/configuration.nix` and the `host-kexec` modules in
`flake.nix`, and remove the eMudhra paragraph from
`marshall/priv/hldd/12-configuration.md`. Then verify that the built host and guest
bundles still lack the four roots, and delete this section. Keep Marshall's
system-store TLS defaults (`runtime-postgres-system-trust`, `mail-smtp-system-trust`)
and the `rustls-webpki` update; they are not part of the workaround.
```

The triggering prompt (same source): `okay is my nixos for my fleet affected by https://emudhra.we-have-a-problem.com/?`

## Cross-References

- **Corroborates**: [blog-ghuntley-nix-overlay-agent-environments](blog-ghuntley-nix-overlay-agent-environments.md) Claim 7 (one overlay patches a transitive dependency fleet-wide) — this post supplies a real incident, though still with no metrics. Its Claim 9 ("you can patch anything by asking an agent to customize it.") is likewise given a first-person example, still unverified.
- **Contradicts**: None.
- **Extends**: [blog-ghuntley-nix-overlay-agent-environments](blog-ghuntley-nix-overlay-agent-environments.md) — adds the lifecycle half (scheduled removal of the patch) that the earlier note does not cover.
- **Novel**: AGENTS.md used as a self-expiring, condition-gated reminder that carries its own revert, verification, and self-deletion instructions.

## Guide Impact

- **Chapter 02**: Candidate small example/sidebar under context files: a "Temporary reminder" section pattern (re-check condition, retry cadence, removal list, keep-list, verification, delete-self). Present as a single anecdotal practitioner pattern, and note the caveat that AGENTS.md is passive and needs a session to fire.
- **Chapter 06**: Optional one-line mention that incident response can pair an emergency mitigation with an explicit, verified exit plan; recommend a human review gate before automated removal of a security control. Do not cite the "tens of millions" or "almost impossible without Nix" claims.

## Extraction Notes

- Fetched page HTML with curl and read the full text; the post is short. The agent's output after the prompt is an embedded image and was not readable; claims about results are therefore limited to the author's prose.
- Per triage, incident details are context only; no outcome of the 2026-10-22 revert existed at extraction time (2026-10-21).
- Cross-reference to Claim 7 and Claim 9 of the Nix note verified by re-reading that note.
