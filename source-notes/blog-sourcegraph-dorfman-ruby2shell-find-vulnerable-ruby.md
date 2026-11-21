---
source_url: https://sourcegraph.com/blog/ruby2shell-cve-2026-132825-find-vulnerable-ruby
source_type: blog-post
title: "Ruby2Shell (CVE-2026-132825): find vulnerable Ruby across your repos before the proof of concept lands"
author: Justin Dorfman (Sourcegraph)
date_published: 2026-11-20
date_extracted: 2026-11-21
last_checked: 2026-11-21
status: current
confidence_overall: emerging
issue: "#4875"
---

# Ruby2Shell (CVE-2026-132825): find vulnerable Ruby across your repos

> Third post in Sourcegraph's runtime-CVE series; adds the point that a stdlib bug can be reachable through default framework middleware (so "we do nothing unusual" is no defense), that a runtime version is pinned in many disagreeing places, and an explicit warning not to triage by a single CVSS score.

## Source Context

- **Type**: blog-post (Sourcegraph company blog, 2026-11-20; auto-discovered via the `sourcegraph` trusted feed). Sibling of the Java4Shell post (2026-11-18).
- **Author credibility**: Justin Dorfman, Sourcegraph, a vendor selling Code Search / Deep Search / Agentic Batch Changes. CVE facts are relayed from Ruby's advisory and Veria Labs, not original research.
- **Scope**: bug mechanism, reachability claim, affected versions, Code Search regexes, a Deep Search prompt, a seven-step response list, and an Agentic Batch Changes prompt. Product CTAs ignored.
- **Verification status**: The post itself says code execution through the Rack path was not independently reproduced. The Prospector confirmed the Ruby 3.3.14 / 3.4.13 / 4.0.10 release announcements on ruby-lang.org but could not locate the CVE/GHSA IDs there. The Miner did not re-check the advisory, Veria Labs, or Rack source. Cite exploit-path claims as "reported by Veria Labs / Sourcegraph".

## Extracted Claims

### Claim 1: The bug is a one-byte heap overflow in case conversion for 14 single-byte encodings
- **Evidence**: Mechanism described plus the one-line upstream fix diff; spare-buffer size is attributed to Veria Labs.
- **Confidence**: emerging
- **Quote**: "The case mapping loop in 14 ISO-8859 and Windows-125x encodings, including ISO-8859-1 and Windows-1252, checked for room for only one."
- **Our assessment**: Specific and internally coherent (ß upcases to SS, loop reserves one byte). Not checked against the commit by us. Illustrates that memory-safety bugs live in "safe" scripting runtimes' C internals, as the Java4Shell note argued for JIT intrinsics.

### Claim 2: Attacker controls overflow size via input length (21 ß into 20 spare bytes), and several methods reach the loop
- **Evidence**: Attributed to Veria Labs.
- **Confidence**: anecdotal
- **Quote**: "Veria Labs says the output buffer gets 20 spare bytes, so a string with 21 ß characters overflows it by one."
- **Our assessment**: Plausible; single-sourced. Methods listed: upcase, swapcase, downcase(:fold), casecmp?; present since Ruby 2.4.0; UTF-8 uses a different path.

### Claim 3: Default Rails and classic Sinatra reach the bug unauthenticated via Rack multipart charset tagging plus Rack::MethodOverride
- **Evidence**: Author read the source paths; Veria Labs reports the unauthenticated request. Author explicitly did not reproduce code execution.
- **Confidence**: anecdotal
- **Quote**: "These source paths support Veria Labs' report that an unauthenticated request can reach the bug. We did not independently reproduce code execution through this path."
- **Our assessment**: The key transferable point. Even if exploitation details change, the pattern holds: a low-level library flaw becomes reachable through default middleware that transforms attacker-controlled fields, so "application code doesn't do anything unusual" is not a reason to deprioritize. The caveat must travel with the claim.

### Claim 4: "Needs to handle Latin-1" is a wrong mental filter, because client-declared charset reaches the parser
- **Evidence**: Same chain as Claim 3.
- **Confidence**: anecdotal
- **Quote**: "That sounds like it needs an app that handles Latin-1 text. It doesn't."
- **Our assessment**: Good illustration of a failed applicability filter (compare the Java4Shell CPU-condition argument). Depends on Claim 3 holding.

### Claim 5: Do not triage by the CVE record's score; scores disagree
- **Evidence**: MITRE 7.4 / local vector vs Ruby "critical" vs Veria Labs "network, no authentication".
- **Confidence**: emerging
- **Quote**: "Don't let the score on the CVE record slow you down."
- **Our assessment**: Useful for agent-driven triage: an automated pipeline keyed on the first-published CVSS vector would deprioritize this. The post's own framing favors the vendor with working PoCs; we cannot tell which score is right.

### Claim 6: Affected versions and fixes
- **Evidence**: Ruby's advisory as relayed by author.
- **Confidence**: emerging
- **Quote**: "Ruby 3.3.13 and earlier, 3.4.0 through 3.4.12, and 4.0.0 through 4.0.9 are affected."
- **Our assessment**: Fixed in 3.3.14, 3.4.13, 4.0.10; Ruby 3.2 and earlier get no fix, so the "fix" is a series migration. Release announcements confirmed by the Prospector. Distro backports can keep the old version number (the post says to check the full package version against the distro advisory).

### Claim 7: Runtime version is declared in many places per repo and they disagree; the production image matters
- **Evidence**: Enumerated list (`.ruby-version`, Dockerfile `ARG RUBY_VERSION`, CI, `Gemfile.lock` RUBY VERSION).
- **Confidence**: emerging
- **Quote**: "The one that matters is the Ruby in the production image, and it's often the least obvious."
- **Our assessment**: Accurate and generalizes across languages. Implication for agent work: an agent asked "what Ruby do we run?" must treat file pins as candidates, not proof of the deployed interpreter.

### Claim 8: Bundled runtimes in self-hosted products are untouched by host upgrades; vendors differ in readiness
- **Evidence**: Per Veria Labs' Nov 19 update: Mastodon 4.7.6, OpenProject 17.9.8, Discourse base on 4.0.10; GitLab 19.6.0 (3.3.13), GHES 3.22.5 (4.0.9), Chatwoot 4.20.0 (3.4.4) listed as affected. Author checked several pins in public source; GHES not verifiable.
- **Confidence**: emerging
- **Quote**: "Upgrading the host Ruby won't change a bundled runtime."
- **Our assessment**: Corroborates Java4Shell Claim 10. Product versions are a point-in-time snapshot and will be stale.

### Claim 9: Search results over-match and under-match; regexes narrow but do not prove exposure
- **Evidence**: Author's caveats: floating tags (`ruby:3.4-slim`) don't match; multi-stage Dockerfiles can have old builder and fixed final stage; build args without defaults need hand review.
- **Confidence**: settled
- **Quote**: "These queries narrow the search. They don't prove exposure."
- **Our assessment**: Honest limitation statement, and the best argument for hybrid approaches (regex for recall, an LLM/agent to reconcile stages and build args).

### Claim 10: Prioritize internet-facing apps, then workers processing imported text; treat as possibly compromised
- **Evidence**: Author's judgment from Claim 3.
- **Confidence**: anecdotal
- **Quote**: "If an internet-facing Rails or Sinatra app ran on an affected Ruby, treat it as possibly compromised until you can show it isn't."
- **Our assessment**: Conservative and conditional on the unreproduced reachability claim; reasonable given the stated deadline.

### Claim 11: Rebuild, don't just redeploy; restart every process and check the version each running process reports
- **Evidence**: Operational advice (floating tags only help if the build actually pulls them).
- **Confidence**: settled
- **Quote**: "Rebuild, don't just redeploy."
- **Our assessment**: Extends Java4Shell Claim 11 (restart) with a cached-base-image failure mode and "version reported by the running process, not on PATH".

### Claim 12: Rotate everything the app account can read; hunt for specific indicators
- **Evidence**: Author's guidance, no incident data.
- **Confidence**: anecdotal
- **Quote**: "Code runs as the app user, so anything that account can read should be treated as exposed."
- **Our assessment**: Generic, but the indicator is somewhat specific: multipart POSTs whose `_method` field declares a single-byte charset with a run of ß. Same posture as Java4Shell Claim 12.

### Claim 13: Exploit window is shrinking, and the bottleneck is discovery rather than the fix
- **Evidence**: Veria Labs said to publish a PoC as early as Nov 25 (5 days after the post); fix is a public one-line diff.
- **Confidence**: anecdotal
- **Quote**: "The time between "patch available" and "exploit available" keeps shrinking, and the part that eats it is still the same: finding every place the runtime is pinned."
- **Our assessment**: Directionally consistent with the PHP2Shell/"patch the planet" notes. Vendor-motivated framing ("You can't patch what you can't find.").

### Claim 14: Batch-change agent prompt design: explicit scope, ordered rules, negative constraints, and routing ambiguity to named lists
- **Evidence**: Published prompt (see Artifacts). In a local demo, 13 of 1,213 workspaces had been run; the image update was unpublished, so no outcome data on real fleets.
- **Confidence**: emerging
- **Quote**: "If the version is set through a build arg you can't resolve, don't guess. List it under "needs review"."
- **Our assessment**: Extends the Java4Shell prompt with new constraints worth noting: separate final-runtime vs builder vs CI pins; never bump across series; do not publish a partial fix while the final runtime is still affected; verify proposed image tags against the registry, not search results. A prompt, not a result.

## Concrete Artifacts

Upstream fix, as quoted in the post:

```diff
- while (*pp < end && to < to_end) {
+ while (*pp < end && to_end - to > 1) {
```

Selected rules from the post's Agentic Batch Changes prompt (verbatim):

```
3. Don't change floating pins (ruby:3.4-slim, ruby-version: "3.3", latest, or no
   tag). List them under "rebuild only". If the version is set through a build
   arg you can't resolve, don't guess. List it under "needs review".
4. Don't bump Ruby 3.2 or earlier across series. List those repos under "needs
   migration" with the version you found.
7. Only propose Ruby versions confirmed fixed by Ruby's advisory. Verify
   proposed image tags against their registry, not search results; list any
   unverified tags under "needs review" instead of guessing. Do not publish
   a partial fix while the final runtime still uses affected Ruby.
```

Deep Search prompt requirement worth noting (verbatim): "List every repository checked, including those with no affected runtime; give non-overlapping category counts that add up to the total checked."

The post also supplies vendor-specific Code Search regexes (Dockerfile pins, version files, Gemfile.lock, distro packages, bundled-product images, legacy-encoding calls, GitHub Actions); not reproduced here.

## Cross-References

- **Corroborates**: `blog-sourcegraph-dorfman-java4shell-find-vulnerable-jdk` Claim 10 (bundled vendor runtimes invisible to host patching), Claim 11 (restart required), Claim 12 (rotate on exposure), Claim 6 (inventory must span many pin locations).
- **Contradicts**: none found.
- **Extends**: `blog-sourcegraph-dorfman-java4shell-find-vulnerable-jdk` Claim 14 (batch-change prompt design) with final-stage-vs-builder separation, no-cross-series-bump, and registry-verified tags; `blog-sourcegraph-dorfman-repo-security-posture` (multi-repo detection framing).
- **Related**: `blog-latentspace-ainews-php2shell-patch-the-planet` and `blog-openai-patch-the-planet` (same run of runtime disclosures).
- **Novel**: reachability through default framework middleware as an argument against "we do nothing unusual"; a three-way CVSS disagreement as a reason not to triage by score; the legacy-encoding case-conversion caveat for application code.

## Guide Impact

- **Chapter 06**: Add the default-middleware reachability pattern (Claim 3, with the not-reproduced caveat) and the CVSS-disagreement warning (Claim 5) to the threat model for dependency/runtime CVEs. Cite as vendor-reported, emerging.
- **Chapter 03**: In verification guidance for agent-driven inventory, note that version files and lockfiles are candidates, not proof of the deployed interpreter (Claims 7, 9, 11); require the agent to report checked-repo counts that sum to the total.
- **Chapter 05**: Optionally cite Claim 14 alongside the Java4Shell note as a second instance of a constrained fleet-wide agent prompt. Incremental, not a new pattern.

## Extraction Notes

- Read the full post (fetched raw HTML, text-extracted so quotes are verbatim). The Sources links (GHSA, Veria Labs, Cloudflare) were not followed; the Prospector noted the GHSA could not be located via the GitHub API.
- Per triage guidance, Code Search regexes were not mined as guide content and the generic playbook already in the Java4Shell note was not duplicated.
- No contradiction issue filed.
