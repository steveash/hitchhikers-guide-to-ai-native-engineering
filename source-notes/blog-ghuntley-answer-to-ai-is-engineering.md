---
source_url: https://ghuntley.com/answer/
source_type: blog-post
title: "the answer to ai is engineering"
author: Geoffrey Huntley
date_published: 2026-11-12
date_extracted: 2026-11-12
last_checked: 2026-11-12
status: current
confidence_overall: anecdotal
issue: "#4677"
---

# the answer to ai is engineering

> A written-up AI DevCon NY talk that argues security response should be engineered (single-source-of-truth Nix environments, capability removal, self-expiring AGENTS.md reminders, deterministic back pressure, property-based testing) rather than solved with "more AI", plus the opinion that most open-source libraries should be generated or vendored instead of depended on.

## Source Context

- **Type**: blog-post (talk write-up; page byline 12 Nov 2026, feed entry dated 11 Nov 2026; we use the page date). Includes chapter timestamps (0:00–28:53) of the talk video.
- **Author credibility**: Geoffrey Huntley, originator of the Ralph loop, runs his own NixOS fleet. The post also says "At Antithesis, validation and verification of software is what we do", so the property-testing recommendation (Bombadil, Hegel) comes from an author who now works for the vendor (he adds "I'm not just talking my book"). All claims rest on personal experience; no measurements.
- **Scope**: Security "take-off" framing, dependency-skepticism, Nix overlay patching, AGENTS.md reminder, sandbox-with-root loops, back pressure, property-based testing. Does NOT cover: any quantified incident-response time, the contents of the `ghuntley/nix-demo` repo (not read), or counter-arguments. The eMudhra incident and Nix overlay mechanics are already in existing notes and are only briefly noted here.

## Extracted Claims

### Claim 1: Security "take-off" is the new normal, mirroring the "agent take-off" in GitHub PR volume
- **Evidence**: Anecdotal list of recent incidents (OpenCode breach, PHP update call from Japan's PM, an HTTP-stack remote shutdown bug, a 12-year-old GitLab RCE, a CA with a trivially guessable key). No data on incident rates; the "quadratic PR graph" is referenced, not shown.
- **Confidence**: anecdotal
- **Quote**: "I'm putting it to you that this is the start of the new normal."
- **Our assessment**: A threat-model assertion built on a cluster of incidents and an inference (agents trained on vulnerable code write vulnerable code). The incident cluster is checkable individually but the trend claim is not evidenced. Treat as a hypothesis, not a finding.

### Claim 2: Defenders will need more inference capacity than attackers, so tight per-employee token budgets are a security risk
- **Evidence**: Opinion/prediction; no data on attacker scanning. Repeats the point in [patch-the-planet Claim 6](blog-ghuntley-patch-the-planet.md) with a new corollary about token budgets.
- **Confidence**: anecdotal
- **Quote**: "I suspect you're going to need more inferencing capacity than your attackers to stay secure."
- **Our assessment**: Hedged by the author himself ("I suspect"). Plausible direction, but asymmetry arguments cut both ways (attackers need only one hit; defenders can also patch deterministically, which is the post's own thesis). Not citable as fact.

### Claim 3: Anything published to GitHub will be autonomously scanned and exploited by actors with large inference hardware
- **Evidence**: Assertion; no telemetry.
- **Confidence**: anecdotal
- **Quote**: "As soon as you publish any code on GitHub, someone with racks of inferencing hardware will autonomously scan it and then autonomously make tool calls to exploit what they find."
- **Our assessment**: Directionally consistent with public reports of automated scanning, but "as soon as" and "autonomously" are unsupported here. Needs a corroborating primary source before the guide states it.

### Claim 4: Open-source libraries existed because code was scarce; with agents, most higher-level libraries should be generated first-party or vendored
- **Evidence**: Author's year of personal practice ("I don't use much open source anymore"), keeping only a "trusted base" (Linux kernel, BIND, crypto). Example: a command-line argument parser built by Claude "in a loop". No measurements, no maintenance-cost comparison, no failure cases.
- **Confidence**: anecdotal
- **Quote**: "So the best you can do is either generate it first-party, or vendor the open-source software and check it into your repo so the agent can modify and extend it."
- **Our assessment**: The most novel and most contestable claim. The stated tradeoff is Dependabot/compromised-upstream time versus generation cost; the post never counts the cost side (review, security of generated code, ongoing ownership). He concedes "I'm not saying you should go and vibe-code your own cryptography." Scope-limited to "small and well-specified" code. Opinion, not evidence; note he also admits getting "grilled to hell on Hacker News" for it.

### Claim 5: The real price of a dependency includes Dependabot churn and incident response for compromised upstreams
- **Evidence**: Rhetorical questions to the audience; no figures.
- **Confidence**: anecdotal
- **Quote**: "How much time do you spend on Dependabot updates? How much time do you spend on incident response because a Dependabot update was compromised, because the upstream author was compromised?"
- **Our assessment**: A useful framing for the guide's supply-chain discussion (ask teams to measure this) even though the post gives no numbers. Cheap to turn into a checklist question.

### Claim 6: Generating a dependency removes the "tool call a human" bottleneck of getting upstream PRs merged
- **Evidence**: Assertion.
- **Confidence**: anecdotal
- **Quote**: "It turns out that if you have to tool call a human, that's not AGI."
- **Our assessment**: A quip rather than a claim, but it points to a real operational argument: vendored/first-party code can be changed at agent speed. Combine with Claim 7 (patch files) for the "route around upstream" theme.

### Claim 7: Patching is hard only because each language/library has its own build toolchain, CI, and artifact hosting; Nix overlays remove that per-language overhead
- **Evidence**: Argument by description of the usual pain (learn toolchain, new CI job per language, artifact repo and tokens). Overlay mechanism shown via the `nix-demo` repo (not read here).
- **Confidence**: anecdotal
- **Quote**: "You do that per language, and every open-source library has a different build toolchain."
- **Our assessment**: Extends [nix-overlay-agent-environments Claim 7](blog-ghuntley-nix-overlay-agent-environments.md). New here is the explicit diagnosis of *why* patching is perceived as hard and the "patch files, route around upstream" framing: "The idea that everything must be merged upstream on GitHub was never part of open source." Pro-Nix advocacy; Bazel/Buck2 or lockfile/SBOM tooling can address parts of this and are not compared.

### Claim 8: Complex tools (Nix, Bazel, Buck2) are now usable because agents drive them; you only need to know they exist
- **Evidence**: Anecdote about eng leaders "nearly getting fired" over such adoptions; no adoption data.
- **Confidence**: anecdotal
- **Quote**: "You can now use highly complex, high-powered tools simply. You just have to know they exist, and you have to falsify your priors."
- **Our assessment**: Corroborates [nix-overlay-agent-environments Claim 12](blog-ghuntley-nix-overlay-agent-environments.md). Caveat (ours): an agent-authored Nix config still needs someone who can review it; the post is silent on that and on debugging when the agent fails.

### Claim 9: Remove a capability at the system layer rather than instructing the model not to use it
- **Evidence**: Demo of a patched git (2.55 inside the project directory, 2.54 globally) without force push, created by asking Claude for a Nix overlay. Transitive consumers of git inherit the patch.
- **Confidence**: anecdotal
- **Quote**: "The best way to stop a model from doing something is to remove its ability to do it."
- **Our assessment**: Restates [nix-overlay-agent-environments Claim 8](blog-ghuntley-nix-overlay-agent-environments.md), now as a general principle ("I use this trick all over the place"). Concrete and sound as defense-in-depth. Limits (ours): only blocks that specific path; an agent with other remotes/APIs can reach equivalent effects, and a patched binary can be bypassed if the agent can install or call another git.

### Claim 10: A single source of truth for dependencies lets one patch rebuild all transitive consumers (e.g., OpenSSL under Nginx and Postgres), with CI caching making it cheap
- **Evidence**: Description plus personal account of an incident response; no build times given.
- **Confidence**: anecdotal
- **Quote**: "With a single source of truth for OpenSSL, you apply a monkey patch just like I did with git, and Nix recompiles the world."
- **Our assessment**: Corroborates [patch-the-planet Claim 3](blog-ghuntley-patch-the-planet.md). The new detail is the cache story ("CI compiles the software once, validates it, and publishes it to the cache"), which is what makes the approach practical, though no cache-hit or latency numbers are provided.

### Claim 11: A single "am I affected?" prompt to an agent was enough to patch and redeploy during the incident wave
- **Evidence**: First-person account, no transcript.
- **Confidence**: anecdotal
- **Quote**: "I opened Claude and asked whether my fleet was affected."
- **Our assessment**: Repeats [patch-the-planet Claim 4](blog-ghuntley-patch-the-planet.md). Precondition is that fleet state is declarative code the agent can read. "I didn't lose any sleep" is not a metric.

### Claim 12: A self-expiring AGENTS.md reminder replaces a Jira ticket for backing out temporary patches
- **Evidence**: Author states the next developer or agent picked up the machine and "automatically did the housekeeping". Here the interval is "seven days" (the sibling incident write-up used a specific date and verification block). No log of the back-out.
- **Confidence**: anecdotal
- **Quote**: "Instead of creating a Jira ticket, I added a reminder to my AGENTS.md."
- **Our assessment**: Corroborates [patch-the-planet Claims 1–2](blog-ghuntley-patch-the-planet.md) and now reports it as having worked ("The next developer or agent to pick up that machine automatically did the housekeeping"). It is still self-reported, and the mechanism depends on some session starting after the date. Worth distinguishing from Claim 9: one is a *scheduling/debt* pattern, the other a *prevention* pattern.

### Claim 13: Running loops as root is acceptable only inside a throwaway Nix environment, never on production hosts or against production databases
- **Evidence**: Design assertion; relies on NixOS properties and the `runNixOSTest` framework to test the whole OS and fleet before deploy.
- **Confidence**: anecdotal
- **Quote**: "do not run agents with Nix as root on production hosts, and do not connect agents to production databases. Ever."
- **Our assessment**: Extends [nix-overlay-agent-environments Claim 4](blog-ghuntley-nix-overlay-agent-environments.md) with the explicit boundary that earlier note lacked: sudo is safe only where the environment is disposable, and prod DB access is replaced by a duplicated database with "restrict the heck out of outbound network access". This tempers the earlier note's blunter "sudo is safe" framing and is the form the guide should cite.

### Claim 14: Back pressure should be deterministic checks (hooks, static analysis forbidding cross-domain coupling), not skills, and can replace much code review
- **Evidence**: Examples only: a pre-commit hook (prek) that blocks pushes if code doesn't compile; a static rule that a SQL domain must not reference an API domain. No measured review-load reduction.
- **Confidence**: emerging
- **Quote**: "The best way to stop it closing on bad output is deterministic checks. These aren't skills. This is engineering again."
- **Our assessment**: Agrees with [own-the-outer-loop Claim 10](blog-addyosmani-own-the-outer-loop.md) on "back pressure" and gives concrete mechanisms. The claim "Engineer away much of the need for code review" is stronger than the evidence; architecture-conformance checks catch structural violations only.

### Claim 15: Property-based testing catches edge cases that example-based unit tests miss and should be applied to cross-service business properties
- **Evidence**: Illustrative example (string reversal with Unicode/emoji, "reverse twice returns original"); proposed property "a customer who asks for a refund is only refunded once". No case study.
- **Confidence**: emerging
- **Quote**: "The problem with unit tests is that they only test what you specify, so edge cases slip through."
- **Our assessment**: Property-based testing is established technique (Hypothesis, QuickCheck); the novelty is recommending it as agent-loop verification. Conflict of interest noted: the author's employer sells the recommended tools.

### Claim 16: Bombadil (property-driven browser testing) should replace Playwright, and Hegel brings Hypothesis-style testing to every language
- **Evidence**: Product description; a "log out always possible" property example; counterexample reproduction. A "PewDiePie using it" anecdote. No comparison data.
- **Confidence**: anecdotal
- **Quote**: "You should ditch Playwright, folks, and I'm not just talking my book."
- **Our assessment**: Vendor-adjacent promotion; flag as such. The valuable generalizable idea is that failing properties yield reproducible counterexamples an agent loop can consume. Do not state "replace Playwright" in the guide.

## Concrete Artifacts

Source: ghuntley.com/answer/ — prompts and mechanisms as described (no code blocks in the post).

```
Prompt (git overlay):  "Can you please use Nix and create a custom overlay that removes force push?"
Prompt (reminder):     "update the AGENTS.md, and in seven days' time, get rid of my patches"
Environment:           devenv + Nix; one definition -> laptops, CI/CD, agent sandboxes, production Docker images
Version switch demo:   global git 2.54; after cd into project, patched git 2.55 (no force push)
Hooks:                 pre-commit (prek) blocks push if code doesn't compile
Static rule example:   SQL domain must never reference API domain
Property examples:     reverse(reverse(s)) == s ; "a customer who asks for a refund is only refunded once" ;
                       "the user always has the ability to log out" (Bombadil)
Linked repo (not read): github.com/ghuntley/nix-demo
```

## Cross-References

- **Corroborates**: [blog-ghuntley-patch-the-planet](blog-ghuntley-patch-the-planet.md) Claims 1–4, 6 (AGENTS.md reminder, transitive patching, "am I affected?" prompt, inference-parity); [blog-ghuntley-nix-overlay-agent-environments](blog-ghuntley-nix-overlay-agent-environments.md) Claims 1, 7, 8, 12 (single source of truth, overlay patch, force-push removal, learning cliff); [blog-addyosmani-own-the-outer-loop](blog-addyosmani-own-the-outer-loop.md) Claim 10 (back pressure).
- **Contradicts**: None filed. Soft tension: Claim 13's explicit "never on production hosts" boundary tightens the earlier note's Claim 4 ("sudo is safe because it is nearly impossible to break"); treated as refinement, not a contradiction, since the earlier note already caveated rollback limits.
- **Extends**: Nix-overlay note Claim 4 (root-in-throwaway-environment with prod-DB duplication rule); patch-the-planet Claim 1 (reports that the reminder ran).
- **Novel**: (a) "generate or vendor instead of depending on open source" as a supply-chain stance, with Dependabot/compromised-upstream cost framing (Claims 4–6); (b) security take-off + inference-parity corollary about token budgets (Claims 1–3); (c) "remove the capability" stated as a general principle; (d) property-based testing / Bombadil / Hegel as agent-loop verification (Claims 15–16). No existing source note covers property-based testing (checked filenames for property/antithesis/bombadil/hegel).

## Guide Impact

- **Chapter 06 (security)**: Add the "remove the capability at the system layer" principle (Claim 9) next to existing patched-git coverage, labelled anecdotal and with the bypass caveat; add the take-off/inference-parity framing (Claims 1–3) only as an unverified opinion.
- **Chapter 06 / Ch00 (dependencies)**: Candidate "dependency cost" checklist (Claim 5) and a flagged-as-opinion note on generate/vendor-vs-depend (Claim 4), explicitly limited to small, well-specified, non-cryptographic code.
- **Chapter 02 (harness)**: Distinguish prevention (capability removal) from scheduled debt cleanup (self-expiring AGENTS.md reminders, Claim 12); cite Claim 13's sandbox boundary instead of the unqualified "sudo is safe".
- **Chapter 03 (verification)**: Add property-based testing as a back-pressure layer producing reproducible counterexamples (Claims 15–16), with vendor-affiliation disclosure; deterministic hooks and architecture-conformance rules (Claim 14) alongside Osmani's back-pressure framing.

## Extraction Notes

- Read the full page text (fetched raw HTML and stripped markup); did not follow `nix-demo` or embedded links. Slide images are not extractable.
- Quotes copied from the page text; the post's embedded link-card text (e.g., "patch the planet", "don't waste your back pressure") is link previews, not used as claims.
- Per the Prospector, incident and Nix-overlay details already covered by existing notes were kept brief; the library-generation claim is marked anecdotal (no measurements supplied).
- No contradiction issue filed: no claim materially opposes an existing note.
