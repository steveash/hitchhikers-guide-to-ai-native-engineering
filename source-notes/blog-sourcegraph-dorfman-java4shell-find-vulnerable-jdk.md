---
source_url: https://sourcegraph.com/blog/java4shell-cve-2026-114938-find-vulnerable-jdk
source_type: blog-post
title: "Java4Shell (CVE-2026-114938): how to find every vulnerable JDK across your repos and servers"
author: Justin Dorfman (Sourcegraph)
date_published: 2026-11-18
date_extracted: 2026-11-19
last_checked: 2026-11-19
status: current
confidence_overall: emerging
issue: "#4827"
---

# Java4Shell (CVE-2026-114938): how to find every vulnerable JDK

> Sourcegraph vendor post on a hardware-conditional JVM memory-corruption CVE; its transferable contribution is the argument that runtime exploitability can depend on the host CPU (so CPU must not be used as a patching filter), plus a concrete inventory, stopgap, triage, and batch-change playbook.

## Source Context

- **Type**: blog-post (Sourcegraph company blog, 2026-11-18; auto-discovered via the `sourcegraph` trusted feed). Follow-up to the same vendor's PHP2Shell post.
- **Author credibility**: Justin Dorfman, Sourcegraph (also author of `blog-sourcegraph-dorfman-repo-security-posture`). Vendor author selling Code Search / Deep Search / Agentic Batch Changes; the CVE facts are secondary, relayed from Calif Research and distro/security-vendor advisories (Datadog, Qualys, watchTowr, Orca), not original research.
- **Scope**: CVE summary, "am I affected" rules, Code Search regexes, a Deep Search prompt, an eight-step response checklist, and an Agentic Batch Changes prompt. Does not independently verify exploit details. Product CTAs ignored.
- **Verification status**: The Prospector confirmed NVD lists CVE-2026-114938 (published 2026-11-17, Oracle Java SE, Compiler component, "Undergoing Analysis"). CVSS 9.2, the 64-byte overrun mechanics, and Oracle's 2026-11-17 patch date are the article's own claims (via Calif) and are NOT independently verified here. The Miner did not re-check NVD or Calif's disclosure.

## Extracted Claims

### Claim 1: Java4Shell is a memory-corruption bug in OpenJDK's AVX-512 Base64 decode intrinsic, reachable by any code that decodes untrusted Base64
- **Evidence**: Vendor-reported via Calif Research disclosure (linked, not read by us). Mechanism described: padding at end of input miscalculates the store mask, so the decoder writes 64 bytes regardless of room left; Calif's example overruns a 50-byte array by 62 bytes; trigger is a string of As followed by `=`.
- **Confidence**: emerging
- **Quote**: "When Base64 input ends with padding, the store mask is miscalculated and the decoder writes 64 bytes no matter how much room is left."
- **Our assessment**: Plausible and well-specified, but single-sourced through a vendor. Cite as "reported by Calif / Sourcegraph" until cross-checked against primary advisories.

### Claim 2: "Memory-safe" managed runtimes are not memory-safe for JIT/intrinsic code the runtime generates itself
- **Evidence**: Explanation of HotSpot intrinsics as hand-written, CPU-tuned machine code running without bounds checks.
- **Confidence**: emerging
- **Quote**: "That's true for the code you write. It isn't true for the code the JVM writes for you."
- **Our assessment**: A useful threat-model correction for teams that deprioritise "memory-safe language" runtimes. Technically sound as a general principle (intrinsics bypass Java-level checks).

### Claim 3: Exploitability depends on the CPU under the JVM, so the same container image can be vulnerable on one node and safe on another
- **Evidence**: Bug fires only on x86-64 with AVX-512 VBMI; scheduling placement (autoscaling groups, Karpenter, instance availability) is decided outside the app repo.
- **Confidence**: emerging
- **Quote**: "So the same container image can be vulnerable on one node and safe on the next."
- **Our assessment**: The key novel point. Follows logically from the bug's mechanism; shifts the exposure unit from "image/repo" to "image x hardware x time".

### Claim 4: The CPU condition should prioritise patching, never exclude from it
- **Evidence**: Argument from placement drift (resizes, hardware refreshes move a service from a safe node to an affected one). No empirical data.
- **Confidence**: emerging
- **Quote**: "Treat the CPU as a reason to move fast, not a reason to skip anything."
- **Our assessment**: Sound operational advice; the conservative policy is cheap relative to proving per-node CPU for every workload over time. Note the vendor also benefits from "inventory everything".

### Claim 5: Affected-version rule: OpenJDK 17.0.6+ that decodes attacker-influenced Base64; stock 8 and 11 lack the intrinsic, except Oracle's 8u511 Performance Pack
- **Evidence**: Article's own statement; defers to Oracle's advisory for exact builds.
- **Confidence**: emerging
- **Quote**: "Standard OpenJDK 8 and 11 don't have the vulnerable intrinsic, though Oracle's 8u511 Performance Pack build does."
- **Our assessment**: Version bounds are vendor-reported; verify against Oracle/NVD before encoding in any guide advice.

### Claim 6: Java hides in more places than a typical language runtime, and each pins its JDK differently, so inventory must span base images, CI, build tools, Helm charts, and vendor-bundled runtimes
- **Evidence**: Enumerated list of distributions and pinning locations; accompanied by Code Search regexes (see Artifacts).
- **Confidence**: emerging
- **Quote**: "Every one of those pins its JDK differently."
- **Our assessment**: Accurate and practically useful. Supports the corpus theme that fleet-scale remediation is bottlenecked on discovery, not the fix.

### Claim 7: Triage order: patch the pre-auth identity/build tier first (Keycloak, Jira, Confluence, Artifactory, Jenkins, PingFederate)
- **Evidence**: Argument by blast radius; no data.
- **Confidence**: anecdotal
- **Quote**: "These are your identity and build systems, which makes them the worst possible place to get popped."
- **Our assessment**: Reasonable heuristic (credential/signing-key custody). Generalises to any fleet-wide CVE.

### Claim 8: Stopgap is `-XX:-UseBASE64Intrinsics` (all architectures); `-XX:UseAVX=2` works on x86-64 but prevents OpenJDK startup on ARM, so pushing it through a shared `JAVA_TOOL_OPTIONS` can take down a Graviton fleet
- **Evidence**: Stated by the author; Calif's guidance is cited as the basis for the nginx point.
- **Confidence**: emerging
- **Quote**: "-XX:UseAVX=2 also works on x86-64, but OpenJDK on ARM won't start with it."
- **Our assessment**: High-value, concrete failure mode of a mitigation applied uniformly across a heterogeneous fleet. A blast-radius lesson independent of Java: a mitigation that is safe on one architecture can be an outage on another. Not independently tested by us.

### Claim 9: Front-proxy request buffering (nginx) is not a mitigation
- **Evidence**: Attributed to Calif's demonstration of the Elasticsearch chain and WebSocket-upgrade paths (not read by us).
- **Confidence**: anecdotal
- **Quote**: "Don't rely on nginx request buffering either."
- **Our assessment**: Consistent with the PHP2Shell corpus point that edge/WAF controls can create false confidence (see `blog-latentspace-ainews-php2shell-patch-the-planet`, Claim 10).

### Claim 10: Bundled vendor JDKs are invisible to host-level patching; set the flag in the vendor's JVM options, or move/isolate the host if the vendor has no answer
- **Evidence**: Author's operational guidance.
- **Confidence**: anecdotal
- **Quote**: "Vendor appliances and self-hosted tools often ship their own runtime under the install directory, so a host-level JDK update won't touch them."
- **Our assessment**: Correct and commonly missed. Fallbacks (move to ARM / older CPU, or take offline) are CVE-specific hardware workarounds.

### Claim 11: A flag or patched image has no effect until the process restarts
- **Evidence**: Operational fact.
- **Confidence**: settled
- **Quote**: "A flag or a patched image does nothing until the process restarts."
- **Our assessment**: Trivially true but a frequent gap in remediation tracking: "merged" or "deployed config" is not "running patched".

### Claim 12: Rotate secrets the JVM could read on exposure, not on proof, because heap overflow can leak memory without RCE
- **Evidence**: Analogy to Heartbleed; no incident data.
- **Confidence**: anecdotal
- **Quote**: "so rotate on exposure, not on proof."
- **Our assessment**: Defensible conservative posture; the Heartbleed-style leak claim is an assertion rather than demonstrated for this bug. The Prospector noted the secret-rotation and hunting sections are generic advice.

### Claim 13: Hunting indicators are JVM crash logs (`hs_err_pid*.log`), unexpected child processes from the Java user, and new files in plugin/webapp directories since disclosure
- **Evidence**: Author's list; no source cited for these specific IOCs.
- **Confidence**: anecdotal
- **Quote**: "Look for JVM crashes with hs_err_pid*.log files, unexpected child processes from the Java user, and new files in plugin or webapp directories since disclosure."
- **Our assessment**: Generic but sensible starting points.

### Claim 14: Remediation across hundreds of repos should be "one spec, one PR per repo, and a dashboard", and the batch-change agent prompt must explicitly route ambiguity to a "needs review" list rather than guessing
- **Evidence**: The published prompt (see Artifacts) encodes: ignore build stages, don't guess on unpinned tags or unresolvable build args, don't invent a JVM-flags mechanism, append rather than overwrite existing flags, never add `UseAVX=2`, report existing `UseAVX=2` without changing it.
- **Confidence**: emerging
- **Quote**: "If the tag is unpinned (latest or no tag) or set through a build arg you can't resolve, don't guess."
- **Our assessment**: The most transferable artifact for the guide: a well-constrained agent prompt with explicit scope, ordered decision rules, negative constraints, and structured outputs (changed / needs-review / skipped). No outcome data on how well the agent performed on a real fleet; this is a prompt, not a result.

### Claim 15: The lesson generalises: each new runtime CVE adds another axis (hardware, libc, kernel feature, GPU driver) that can't be pinned from a repo, which argues for finding every runtime rather than fewer
- **Evidence**: Author's extrapolation from PHP2Shell then Java4Shell.
- **Confidence**: anecdotal
- **Quote**: "That's an argument for finding every runtime, not fewer."
- **Our assessment**: Interesting framing but speculative (the predicted next axes are guesses). Also self-serving for a code-search vendor.

## Concrete Artifacts

Code Search queries (Sourcegraph syntax), verbatim from the post:

```
file:(Dockerfile|Containerfile) /^FROM\s+\S*(eclipse-temurin|amazoncorretto|openjdk|azul\/zulu|bellsoft\/liberica|sapmachine|microsoft\/openjdk|ubi\d*\/openjdk|graalvm)/ patterntype:regexp
/(apt-get|apk|yum|dnf|microdnf)\s+(install|add).*(openjdk|temurin|corretto|zulu|java-\d+)/ patterntype:regexp
file:\.github/workflows/ uses: actions/setup-java
file:(\.java-version|\.sdkmanrc|\.tool-versions|build\.gradle(\.kts)?|pom\.xml)$ /(java|languageVersion|maven\.compiler\.release)\D{0,20}(17|21|25|27)/ patterntype:regexp
file:(Chart\.yaml|values\.ya?ml|kustomization\.ya?ml)$ /(keycloak|jenkins|confluence|jira|artifactory|pingfederate|kafka|solr|elasticsearch|gerrit|spinnaker)/ patterntype:regexp
```

Deep Search prompt (verbatim):

```
Which services run on a JDK 17 or later image, and where is the Java version pinned for each one?
```

Agentic Batch Changes prompt (verbatim, Sourcegraph blog):

```
Scope: repositories matching github.com/<your-org>/*. Skip forks, mirrors, and archived repos.
Task: add -XX:-UseBASE64Intrinsics to the JVM options of every service that runs on a Java 17+ image.
1. Find services. A service is anything with a Dockerfile, Jib/buildpack config,
   or Helm chart that produces a deployed Java workload.
2. Decide the Java version. Check, in order: the final runtime stage of the
   Dockerfile (ignore build stages), the Helm image tag, then build config
   (Jib baseImage, sourceCompatibility, .java-version). Include a service only
   if the runtime image is Java 17 or newer. If the tag is unpinned (latest or
   no tag) or set through a build arg you can't resolve, don't guess. List it
   under "needs review".
3. Add the flag where the service already sets JVM flags: JAVA_TOOL_OPTIONS,
   JAVA_OPTS, JDK_JAVA_OPTIONS, a Helm values file, or a jvm.options file.
   Append to the existing value and keep the existing flags. If a service
   sets no JVM flags anywhere, don't invent a new mechanism. List it under
   "needs review".
4. Above each change, add this comment, using the file's comment syntax:
   Disable BASE64 intrinsics: https://nvd.nist.gov/vuln/detail/CVE-2026-114938
   Remove -XX:-UseBASE64Intrinsics once the JDK is patched.
5. Never add -XX:UseAVX=2. It prevents the JVM from starting on ARM. Search
   the repos for it and report any existing occurrences without changing them.
Output:
- A table of changed files: repo, file, image and version, variable edited.
- A "needs review" list with the reason for each entry.
- A "skipped" list of Java services below 17.
- One PR per repo, titled "Disable BASE64 intrinsics (CVE-2026-114938)".
```

Response checklist (summarised from the post's "Assume you're exposed" section): patch pre-auth tier first; use `-XX:-UseBASE64Intrinsics`; chase bundled JDKs; restart every JVM; rotate secrets; hunt; rebuild rather than hotfix once a vendor build is published.

## Cross-References

- **Corroborates**: `blog-sourcegraph-dorfman-repo-security-posture` (Claim 4: most teams can't tell within a week which repos are exposed to a new disclosure; this post is a worked example of the discovery step). `blog-latentspace-ainews-php2shell-patch-the-planet` (Claim 10: edge controls create false confidence, parallel to the nginx-buffering point; Claim 9: ownership/distribution problem as much as discovery). `blog-sourcegraph-preston-agentic-batch-changes` (Claim 3: describe-scope-plan-trial-rollout workflow; Claim 8: Mercari cross-repo security patch) which this post applies to a live CVE.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-sourcegraph-tanner-vulnerability-remediation-scale` (Claim 8: ticket-per-team, PR-per-repo does not scale; this post supplies a concrete one-spec/one-PR-per-repo prompt). `blog-cognition-devin-security-vulnerability-remediation-program` (fleet-scale agent remediation, but Cognition's is a services engagement; this is a self-serve prompt pattern).
- **Novel**: (1) Hardware-conditional exploitability as a reason to inventory all runtimes rather than filter by CPU. (2) A mitigation flag that is safe on x86-64 but prevents JVM startup on ARM, with the fleet-wide `JAVA_TOOL_OPTIONS` blast-radius warning. (3) A fully published agent prompt with "needs review"/"skipped" escape hatches and negative constraints. (4) Bundled vendor runtimes as a patching blind spot.

## Guide Impact

- **Chapter 06 (security threat model)**: Add a subsection or bullet on "environmental conditions are not a patching filter": exposure can depend on host hardware/placement that changes over time, so prioritise (not exclude) by condition. Cite Claims 3-4 as vendor-reported. Also add "mitigations can have architecture-specific side effects; test on every fleet architecture before pushing via a shared env var" (Claim 8). Keep CVE specifics (CVSS 9.2, 64-byte overrun, patch date) attributed to the vendor until verified against NVD / Oracle.
- **Chapter 05 (team adoption)**: Use the Agentic Batch Changes prompt as an example of a well-scoped delegated fleet change (explicit scope, ordered decision rules, "don't guess -> needs review", structured outputs, one PR per repo). Note the absence of outcome data.
- **Chapter 04 (context engineering / agentic remediation)**: Optionally reference the prompt as a pattern for encoding negative constraints ("never add X") and escape hatches for unresolvable inputs.

## Extraction Notes

- Fetched the full page via curl and read it end to end (about 10k characters of text); all quotes copied from that text. The page links to Calif, NVD, CVE Record, watchTowr, Datadog, Qualys, and Orca; these were NOT followed, so all exploit/CVSS/patch-date details are second-hand. The Prospector's NVD check confirmed only that the CVE record exists.
- Quotes avoid the page's curly-apostrophe sentences where possible to keep them character-exact.
- Product CTAs (demo, Deep Search marketing) ignored per triage guidance.
- Cross-reference claim numbers were verified against the headings of the cited notes.
