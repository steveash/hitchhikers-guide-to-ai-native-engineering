---
source_url: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
source_type: blog-post
title: "Be alert: targeted attacks on prominent Rustaceans"
author: Simon Willison (link-blog, quoting Adam Harvey and the crates.io security response working group)
date_published: 2026-09-17
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: emerging
issue: "#3653"
---

# Be alert: targeted attacks on prominent Rustaceans

> Simon Willison amplifies an official Rust security advisory describing an
> ongoing, DPRK-linked "contagious interview" social-engineering campaign
> against rust-lang members and popular crate maintainers — video calls used
> as a pretext to get victims to install malware or run a clipboard-pasted
> command — and, following the trail through the linked `arrayref` crate
> incident and a referenced "dependency cooldowns" post, this note surfaces a
> concrete, low-cost mitigation (7–14 day upload cooldowns) with an 8/10
> historical hit rate against real supply-chain attack timelines.

## Source Context

- **Type**: blog-post (Simon Willison's "link post" format — a short
  blockquote of the primary source plus his own editorial framing and a
  recommended mitigation, auto-discovered via the `simon-willison` trusted
  feed). The primary source is the official Rust Blog advisory at
  `https://blog.rust-lang.org/2026/09/17/targeted-attacks/`, authored by Adam
  Harvey "on behalf of the crates.io team and security response working
  group." This note fetches and extracts from three pages: Willison's post,
  the Rust Blog advisory it quotes, and two pages the advisory/Willison link
  to — the prior `arrayref` compromise advisory
  (`blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/`) and
  Yossarian's "We should all be using dependency cooldowns"
  (`blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns`,
  published Nov 21, 2025, which Willison cites as "our best defense right
  now").
- **Author credibility**: Adam Harvey and the crates.io security response
  working group are the first-party operators of the Rust package registry
  and are reporting on an active, in-progress incident they are directly
  responding to — the highest-credibility source type for this claim class.
  Simon Willison is a designated `trusted-feed` source in this repo; here he
  adds an original editorial synthesis (the "network of human beings who are
  potential attack vectors" framing and the cooldowns recommendation), not
  just pure amplification. Yossarian (the pseudonymous author of the
  dependency-cooldowns post, also known for the widely-cited zizmor GitHub
  Actions security scanner and prior Ultralytics/tj-actions supply-chain
  write-ups) is an established supply-chain-security practitioner whose post
  is data-driven (a 10-attack comparison table with cited sources per row).
- **Scope**: Covers the specific social-engineering attack pattern
  (video-call pretext → malware install or clipboard command execution)
  targeting Rust ecosystem maintainers, its DPRK/"contagious interview"
  attribution, Rust's advisory-level recommended defenses, and — via the
  linked cooldowns post — a quantified, cross-ecosystem argument for
  dependency cooldowns as a mitigation. Does **not** cover: technical
  indicators of compromise (malware hashes, C2 infrastructure), the
  `arrayref` attack's initial compromise vector (the advisory for that
  incident explicitly states this is unknown — "their computer or
  credentials are likely compromised" with no further detail), or whether
  the September 2026 campaign and the June 2026 and August 2026 incidents
  are confirmed to be the same actor (the advisory explicitly states this is
  unconfirmed).

## Extracted Claims

### Claim 1: Rust's security team believes there is an active, ongoing campaign targeting rust-lang members and popular crate owners intended to compromise devices/accounts and publish malware through them
- **Evidence**: Direct first-party statement from the crates.io security
  response working group, published as an official advisory on the Rust
  Blog.
- **Confidence**: emerging (an active, first-party-confirmed campaign, but
  explicitly framed by the source itself as a belief/assessment in progress
  — "We believe" — not a closed post-incident report)
- **Quote**: "We believe that there is an ongoing campaign targeting rust-lang members and owners of popular crates that is attempting to compromise devices and accounts in order to use them to publish malware."
- **Our assessment**: This is a credible, first-party threat assessment from
  the team that operates the registry under attack, not third-party
  speculation. For AI-native teams, the significance is structural: the
  target isn't a system vulnerability but the humans who hold publish
  rights — a class of attack surface that code-level scanning cannot
  detect or patch.

### Claim 2: The attack vector is a video call set up under a plausible positive pretext (job, project, or contract offer), used to get the target to either install malware (e.g., a "missing audio codec") or execute a command via the clipboard
- **Evidence**: Direct description from the Rust security advisory's "What
  we've seen" section.
- **Confidence**: emerging (specific, first-party-observed attack pattern
  described across multiple incidents by the responding team)
- **Quote**: "A video call is set up for something positive — maybe for a job, maybe for a project, maybe for a contract opportunity — and then that's used as a vector to either get the target to install something on their computer (such as a purportedly missing audio codec) or execute another command (for example, via putting a command on the clipboard)."
- **Our assessment**: This is a well-documented technique (see Claim 3, the
  DPRK "contagious interview" attribution) applied specifically to open
  source maintainers rather than corporate job candidates. The "missing
  audio codec" and clipboard-paste-command variants are notable because they
  require zero exploit development — pure social engineering converts a
  trusted human into the delivery mechanism. This is not defensible by
  endpoint security tooling alone; it requires operational awareness
  training for anyone with publish rights.
- **Corroborates**: `failure-meta-ai-instagram-account-takeover.md` on the
  broader theme that account/identity compromise, not technical exploitation,
  is often the actual attack surface — though that incident involved an AI
  support bot accepting a false ownership claim, while this campaign targets
  the human maintainer directly via social engineering. Both establish that
  the weakest link in a security chain is frequently identity/access
  verification rather than code.

### Claim 3: Attackers are creating new but legitimate-seeming company profiles, including plausible LinkedIn presences, to pass cursory inspection by targets
- **Evidence**: Direct statement in the Rust advisory's "What we've seen"
  section.
- **Confidence**: emerging (first-party observation, consistent with
  publicly documented "contagious interview" tradecraft cited in the same
  advisory)
- **Quote**: "These attackers are setting up new but legitimate seeming company profiles, including plausible LinkedIn presences, in order to pass cursory inspection."
- **Our assessment**: This raises the bar for "do basic diligence on who's
  contacting you" defenses — a plausible LinkedIn profile is not a
  meaningful signal of legitimacy on its own. Teams should treat unsolicited
  video-call outreach (job offers, contract opportunities, project
  collaboration asks) to anyone with publish/commit/deploy credentials as a
  standing threat category requiring verification independent of the
  contacting profile's apparent polish.

### Claim 4: This attack style is attributed to being known to be used by the DPRK ("contagious interview") and has been observed outside the Rust community as well
- **Evidence**: The advisory links to two external sources: a Kudelski
  Security research writeup on DPRK's "contagious interview" campaign and an
  independent security researcher's (ashishb.net) documentation of the
  pattern occurring outside the Rust community. The advisory also links to a
  prior "dissecting a failed nation-state attack" writeup describing a June
  2026 attack of the same form against "many prominent Rust developers."
- **Confidence**: emerging (the DPRK attribution and cross-community
  pattern are supported by cited third-party sources, but the advisory
  itself explicitly does not confirm whether the June, August, and
  September 2026 incidents are the same campaign or actor: "At this moment
  we do not know if these are all a part of the same campaign")
- **Quote**: "This attack style is known to be used by the DPRK, and has been seen outside of the Rust community as well."
- **Our assessment**: The "contagious interview" pattern is a recognized,
  named nation-state tradecraft category (not a novel technique specific to
  this incident), which means defenses developed here (verify who's
  actually on the call, don't run codec/dependency-install instructions
  from a recruiter, don't paste unfamiliar clipboard commands into a
  terminal) generalize well beyond the Rust ecosystem to any org where
  engineers might receive unsolicited "job opportunity" video-call outreach.

### Claim 5: Last month's (August 2026) `arrayref` crate compromise used the same social-engineering trick, and was one of several crates affected in that incident
- **Evidence**: Willison's post links directly to the Rust Blog's own
  August 20, 2026 advisory on the `arrayref` compromise. That advisory
  states the incident was first reported and verified on 2026-08-20 at
  7:15 UTC, when the `proc-macro1` crate was found to have "a build script
  that was downloading a malicious payload." The Rust team does not believe
  the `arrayref` maintainer acted maliciously — their account/device is
  assessed as compromised, though the advisory does not describe how.
- **Confidence**: emerging (first-party Rust Blog advisory for the
  incident itself; the claim that this specific incident used "the same
  trick" as the September campaign is Willison's/the advisory's assertion,
  not independently re-derived by this Miner)
- **Quote**: "Last month this trick was used in a successful supply chain attack against the array ref crate, among others."
- **Our assessment**: This converts the September advisory from a
  theoretical warning into one backed by a very recent, real, successful
  compromise on the same registry — raising the credibility and urgency of
  the warning substantially above a generic "be careful" advisory.

### Claim 6: The August 2026 `arrayref` incident affected multiple crates — six malicious crates were removed outright, and three legitimate, widely-used crates briefly carried malicious versions before being pulled
- **Evidence**: The Rust Blog's `arrayref` advisory, fetched directly.
- **Confidence**: settled (specific, first-party-confirmed incident
  facts — named packages, versions, and exact online-duration figures)
- **Quote**: "We do not believe the author of `arrayref` to be acting maliciously, but their computer or credentials are likely compromised."
- **Our assessment**: The concrete numbers here are the most citable part of
  this incident for a guide on supply-chain risk: `arrayref@0.3.10` was live
  for 86 minutes, `internment@0.8.7` for 90 minutes, and
  `append-only-vec@0.1.9` for 107 minutes before removal — all under two
  hours. Six other, apparently attacker-created, crates
  (`proc-macro1`, `proc-macro-en`, `aovine`, `arone`, `aronenao`,
  `tinymember`) were deleted outright. This is a textbook illustration of
  Yossarian's "window of opportunity" framing in Claim 8 below: detection
  and removal happened in under two hours, which is exactly the kind of
  short window a dependency cooldown of even a few days would sidestep
  entirely for any consumer who hadn't yet upgraded.

### Claim 7: Willison's core risk framing is that nearly every piece of software depends on open source, and therefore has a network of human beings — everyone with publish rights across its full dependency tree — who are all potential attack vectors
- **Evidence**: Willison's own editorial synthesis, added on top of the
  quoted Rust advisory.
- **Confidence**: emerging (an analytical framing/argument, not an
  empirical measurement — the underlying premise, that most software
  depends on open source, is uncontroversial, but the framing itself is
  Willison's own contribution)
- **Quote**: "Any piece of software that depends on open source (which is almost every piece of software) has a network of human beings who are potential attack vectors - everyone with publishing rights to any of the packages in the dependency network for that software."
- **Our assessment**: This reframes supply-chain risk away from "is this
  package's code safe" (a static, one-time question) toward "is everyone
  with publish rights across my entire transitive dependency tree currently
  safe from social engineering" (a continuously-changing, human-scale
  question that scales with dependency tree size). For AI-native teams that
  are pulling in dependencies faster than before via AI-assisted scaffolding
  and package search, this argues for treating dependency-tree size itself
  as a security cost, not just a convenience.

### Claim 8: Willison's recommended mitigation is dependency cooldowns — waiting a few days after a new release before upgrading to it, on the theory that supply-chain attacks will be spotted by someone else in that window
- **Evidence**: Willison's own recommendation, explicitly hedged ("I guess"),
  linking to Yossarian's "We should all be using dependency cooldowns" post
  as the source of the idea.
- **Confidence**: emerging (Willison's own hedged recommendation; but the
  linked source it points to — Yossarian's post — supplies a data-backed
  argument, elevating this from a bare opinion to a quantified claim; see
  Claim 9)
- **Quote**: "I guess our best defense right now is dependency cooldowns - giving new package releases a few days before upgrading to them, in the hope that supply chain attacks like this will be spotted by someone else."
- **Our assessment**: Notable because it directly extends
  `blog-simonwillison-larson-pypi-upload-restriction.md`'s claim (PyPI's
  first-party 14-day upload restriction) with a second, independent, and
  older (Nov 2025) data point recommending the same class of control —
  consumer-side cooldowns rather than registry-side upload restrictions.
  Both approaches target the same underlying structural fact (Claim 6):
  compromise-to-removal windows are usually short, so simply not being an
  early adopter of a new release is a cheap, high-leverage defense.

### Claim 9: Per Yossarian's analysis of 10 recent prominent open-source supply-chain attacks, 8 of 10 had a "window of opportunity" (publish-to-detection-and-removal) of less than one week; a 7-day cooldown would have prevented the large majority, and 14 days would have prevented all but one (xz-utils)
- **Evidence**: A comparison table in the linked cooldowns post, citing a
  named source per attack (e.g., research.swtch.com for xz-utils,
  stepsecurity.io for Nx, wiz.io for web3.js). Measured windows range from
  1 hour (rspack, Ultralytics phase 2) to approximately 5 weeks (xz-utils,
  described as "a significant outlier").
- **Confidence**: emerging (a single author's compilation and analysis
  across 10 named, individually-sourced incidents — each incident's window
  figure traces to a distinct third-party report, but the aggregate 8/10
  and "14-day would stop all but 1" conclusions are the post author's own
  synthesis, not independently re-verified by this Miner)
- **Quote**: "In the very small sample set above, 8/10 attacks had windows of opportunity of less than a week. Setting a cooldown of 7 days would have prevented the vast majority of these attacks from reaching end users (and causing knock-on attacks, which several of these were). Increasing the cooldown to 14 days would have prevented all but 1 of these attacks."
- **Our assessment**: This is the strongest quantitative backing in this
  source for a mitigation the guide could recommend concretely, and it maps
  directly onto Claim 6's `arrayref` data point (86–107 minute windows,
  comfortably inside even a 1-day cooldown). It's a small, self-selected
  sample (10 attacks, one author's compilation) rather than a systematic
  study, so we treat the 8/10 and "80–90% reduction" figures as suggestive
  rather than statistically rigorous — but the underlying mechanism (attack
  windows are typically short because supply-chain-security vendors and
  registries move fast once alerted) is independently plausible and
  consistent with the `arrayref` and PyPI evidence already in this corpus.

### Claim 10: Cooldowns are cheap to implement — free, first-class support already exists in Dependabot, Renovate, pnpm (`minimumReleaseAge`), and uv (`exclude-newer`)
- **Evidence**: The cooldowns post lists specific tools and links to their
  documentation, plus a working Dependabot YAML config example.
- **Confidence**: settled (specific, named, currently-shipping tool
  features, directly checkable against each tool's own documentation)
- **Quote**: "They're incredibly easy to implement. Moreover, they're literally free to implement in most cases: most people can use Dependabot's functionality, Renovate's functionality, or the functionality build directly into their package manager."
- **Our assessment**: This removes the most common objection to a new
  security practice (cost/effort) — cooldowns are largely a configuration
  change, not new tooling to build or buy. This is directly actionable
  guidance for a guide chapter on dependency management.

## Concrete Artifacts

### Willison's post, full text (verbatim, per direct WebFetch verbatim-mode extraction)

```
Source: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
Posted: 17th September 2026 at 11:59 pm

"Be alert: targeted attacks on prominent Rustaceans. Important warning from
Adam Harvey and the crates security team:

  We believe that there is an ongoing campaign targeting rust-lang members
  and owners of popular crates that is attempting to compromise devices
  and accounts in order to use them to publish malware.

  A video call is set up for something positive — maybe for a job, maybe
  for a project, maybe for a contract opportunity — and then that's used
  as a vector to either get the target to install something on their
  computer (such as a purportedly missing audio codec) or execute another
  command (for example, via putting a command on the clipboard).

Last month this trick was used in a successful supply chain attack against
the array ref crate, among others.

Any piece of software that depends on open source (which is almost every
piece of software) has a network of human beings who are potential attack
vectors - everyone with publishing rights to any of the packages in the
dependency network for that software.

I guess our best defense right now is dependency cooldowns - giving new
package releases a few days before upgrading to them, in the hope that
supply chain attacks like this will be spotted by someone else."

Tags: open-source, security, rust, supply-chain, dependency-cooldowns
```

### Rust Blog advisory, "What you can do" section (verbatim)

```
Source: https://blog.rust-lang.org/2026/09/17/targeted-attacks/
Sept. 17, 2026 · Adam Harvey on behalf of the crates.io team and security
response working group

"Please take extra care in the near term. Be appropriately suspicious of
cold outreaches, and ensure that any calls you have with new people are on
platforms you trust — ideally, try to be the one who sets up the call on a
platform you already use.

Please also re-check that your accounts look normal: MFA enabled, no
unexpected logins on platforms that can track that, and so on.

If you have any concerns about your accounts, please reach out to
help@crates.io (for crates.io account concerns) and/or
security@rust-lang.org (for any other concerns). We're very happy to help."
```

### `arrayref` incident facts (from blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/)

```
Source: https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/
Initial report: "On 2026-08-20 at 7:15 UTC we got a report that the
proc-macro1 crate was malicious. The Rust Security Response Team verified
this to be the case: the crate had a build script that was downloading a
malicious payload."

Malicious crates deleted outright:
  proc-macro1, proc-macro-en, aovine, arone, aronenao, tinymember

Legitimate crates with malicious versions published (all removed same day):
  arrayref@0.3.10        — 86 minutes online
  internment@0.8.7        — 90 minutes online
  append-only-vec@0.1.9   — 107 minutes online

Attack vector on the arrayref maintainer's account: not disclosed. Advisory
states only: "We do not believe the author of arrayref to be acting
maliciously, but their computer or credentials are likely compromised."

User remediation (verbatim shape, per advisory): a `find` command against
~/.cargo/registry/cache to check local caches for the specific malicious
`.crate` files by name and version.
```

### Dependency cooldown attack-window data (from blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns)

```
Source: https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns
Published: Nov 21, 2025

Attack                     | Window of Opportunity
----------------------------|----------------------
xz-utils                    | ≈ 5 weeks (significant outlier)
Ultralytics (phase 1)       | 12 hours
Ultralytics (phase 2)       | 1 hour
tj-actions                  | 3 days
chalk                       | < 12 hours
Nx                          | 4 hours
rspack                      | 1 hour
num2words                   | < 12 hours
Kong Ingress Controller     | ≈ 10 days
web3.js                     | 5 hours

"8/10 attacks had windows of opportunity of less than a week."
7-day cooldown: prevents "the vast majority."
14-day cooldown: prevents "all but 1" (xz-utils).

Example Dependabot cooldown config (verbatim from post):
  version: 2
  # update once a week, with a 7-day cooldown
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
    cooldown:
      default-days: 7

Other tools with native cooldown support cited: Renovate
(minimum-release-age), pnpm (minimumReleaseAge), uv (exclude-newer, an
absolute cutoff rather than rolling cooldown).
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-larson-pypi-upload-restriction.md` Claim 2: PyPI's
    first-party rationale for its 14-day upload restriction ("to prevent
    old and long-stable releases from being poisoned in case publishing
    tokens or workflows of PyPI projects were compromised") is the
    registry-side mirror of this source's consumer-side cooldown
    recommendation (Claim 8). Both independently converge on "time delay as
    a cheap, structural supply-chain defense," from two different
    ecosystems (PyPI vs. crates.io/Cargo) and two different actors
    (registry operator vs. individual practitioner).
  - `failure-meta-ai-instagram-account-takeover.md`: Both sources document
    that identity/access compromise — not code-level exploitation — is the
    actual attack surface. The Meta case is architectural (an AI support
    bot accepted an unverified ownership claim); this case is
    human-targeted social engineering (a video call pretext to get a
    maintainer to install malware or run a command). Both argue that hard
    controls (out-of-band verification for Meta; cooldowns and outreach
    skepticism here) beat trusting a single point of judgment (bot or
    human) in the moment.
  - `blog-anthropic-zero-trust-ai-agents.md`: That source's general
    "assume compromise is possible" zero-trust framing for AI agent
    deployments extends naturally to human maintainers with publish
    rights — this campaign demonstrates the same assume-breach posture is
    warranted for the humans upstream of the dependency tree, not just the
    AI systems downstream of it.

- **Contradicts**: None identified. No existing corpus source makes claims
  about dependency-cooldown effectiveness, crates.io/Cargo supply-chain
  incidents, or DPRK-attributed social engineering against OSS maintainers
  that this note's claims conflict with.

- **Extends**:
  - `blog-simonwillison-larson-pypi-upload-restriction.md`: That note
    documented one registry's (PyPI's) shipped, registry-side hardening
    control. This note adds a second, independent data point for the same
    underlying "time delay defeats fast-moving supply chain attacks"
    principle, this time from the consumer side and backed by Yossarian's
    cross-ecosystem 10-attack comparison (Claim 9) rather than a single
    registry's internal impact analysis. Together the two notes give the
    guide both a registry-side and a consumer-side worked example of the
    same mitigation class.
  - `docs-ghaw-dependabot.md`: That note documents GitHub Agentic
    Workflows' automated dependency-update tooling built on Dependabot.
    This note's Concrete Artifacts section supplies the specific
    `cooldown: default-days: 7` YAML stanza that could be layered directly
    onto that tooling as a concrete hardening recommendation.

- **Novel**:
  - First corpus source documenting a nation-state-attributed ("contagious
    interview" / DPRK), video-call-pretext social-engineering campaign
    targeting open-source package maintainers specifically (as opposed to
    corporate job candidates, the more commonly reported target of this
    tradecraft).
  - First corpus source with a quantified, cross-ecosystem, multi-incident
    comparison of supply-chain-attack "windows of opportunity" (Claim 9's
    10-attack table), giving the guide a data point for recommending a
    specific cooldown duration (7 or 14 days) rather than a vague
    "use cooldowns" suggestion.
  - First corpus source with concrete, sub-two-hour compromise-to-removal
    timing data for a real crates.io incident (the `arrayref` case, Claim
    6), which functions as a live illustration of why short cooldowns are
    effective.

## Guide Impact

- **Chapter 06 (Security Threat Model / Governance & Operations)**: Add a
  named example of maintainer-targeted social engineering (video-call
  pretext → malware install or clipboard-command execution) as a distinct
  supply-chain threat category, separate from credential-leak or CI
  pipeline compromise. Recommend the advisory's specific operational
  guidance verbatim: be suspicious of cold video-call outreach, prefer
  platforms you already trust and control the setup of, and periodically
  audit account security (MFA, login history) for anyone with publish
  rights. Cite this source alongside the DPRK "contagious interview"
  attribution to justify treating this as a standing, not one-off, threat
  category.
- **Chapter 04 (Managing Dependencies)**: Add dependency cooldowns as a
  concrete, low-cost recommended practice, citing both this source's 7/14
  day analysis (Claim 9, with the 8/10-under-a-week data) and
  `blog-simonwillison-larson-pypi-upload-restriction.md`'s PyPI registry-
  side control as complementary registry-side/consumer-side defenses.
  Include the working Dependabot YAML snippet from Concrete Artifacts as a
  copy-pasteable example, and name the equivalent flags for Renovate,
  pnpm, and uv so the recommendation is actionable regardless of a team's
  package manager.
- **Chapter 04 (Managing Dependencies)**: Use the `arrayref` incident's
  86–107 minute compromise-to-removal window (Claim 6) as the guide's
  concrete illustrative number for "why even a 1-day cooldown meaningfully
  reduces exposure" — it is a real, recent, first-party-confirmed data
  point rather than a hypothetical.

## Extraction Notes

- **Multi-hop extraction across 4 pages**: This note follows Willison's
  post → the Rust Blog September advisory it quotes → the Rust Blog's
  August `arrayref` advisory it links to → Yossarian's dependency-cooldowns
  post it links to as "our best defense." All four were fetched directly.
  This is within the "up to 5 linked pages" guidance in `agents/MINER.md`.
- **Quote extraction approach**: The main Willison/Rust-advisory quotes
  were obtained via a single verbatim full-page-reproduction WebFetch call
  each, and cross-checked against each other (Willison's post quotes the
  advisory verbatim, and both copies matched). The `arrayref` advisory
  page declined a full verbatim reproduction on one attempt (citing
  copyright-reproduction caution) but yielded the specific quotes and
  figures used here (all under 40 words each) on a second, narrower,
  explicitly-scoped request — consistent with the approach used in
  `blog-simonwillison-larson-pypi-upload-restriction.md`'s extraction
  notes for the same kind of WebFetch refusal.
- **Unresolved/unconfirmed by the source itself**: The Rust advisory
  explicitly does not confirm whether the June 2026 ("failed nation-state
  attack" against "many prominent Rust developers"), August 2026
  (`arrayref`), and September 2026 (this advisory) incidents are the same
  campaign or actor — "At this moment we do not know if these are all a
  part of the same campaign." This note preserves that uncertainty rather
  than treating the incidents as confirmed-linked.
  - The `arrayref` maintainer's specific compromise vector (how their
    device/credentials were actually obtained) is not disclosed in the
    August advisory and was not found elsewhere during extraction.
- **No contradiction filed**: This source does not conflict with any
  existing corpus claim; the "corroborates"/"extends" relationships above
  are additive, not disputed.
