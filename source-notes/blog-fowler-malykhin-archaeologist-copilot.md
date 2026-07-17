---
source_url: https://martinfowler.com/articles/archaeologist-copilot.html
source_type: blog-post
title: "The Archaeologist's Copilot"
author: Nik Malykhin (Thoughtworks)
date_published: 2026-07-16
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: emerging
issue: "#1957"
---

# The Archaeologist's Copilot

> A first-person, artifact-rich case study of restoring a 20-year-old Java 1.5
> "Big Ball of Mud" with AI: a naive "Tourist Prompt" produced confident but
> false modernization output, while a persona-based "Archaeologist Prompt"
> forcing forensic, evidence-cited analysis surfaced the real risks (hidden
> concurrency bugs, exception-swallowing "Lying Tests", stringly-typed data)
> that then drove a disciplined four-phase containment-before-refactor
> methodology using Docker as a historical "Time Capsule" and a compiler-
> warning-driven AI feedback loop.

## Source Context

- **Type**: blog-post (long-form technical case study/memo, published on
  martinfowler.com, 16 July 2026, ~2,800 words with 8 code/config artifacts
  and a before/after comparison table)
- **Author credibility**: Nik Malykhin, described in the article's byline as
  "an Israeli software developer and Thoughtworker," is credited with the
  bio: "In addition to his interest in applying AI to software development,
  he believes that the combination of discipline and human collaboration is
  becoming even more important in the AI era." Published on martinfowler.com,
  a `trusted-feed` source in this corpus with editorial vetting distinct from
  a personal blog — the article's Acknowledgments section explicitly credits
  "Martin Fowler for his feedback and guidance throughout the writing
  process." The article discloses its own AI usage directly: "I started by
  using Gemini to highlight the key moments from my experiment and turn my
  notes into an outline. Then I used it to help draft sections from that
  outline... Finally I used AI for a pass on flow and grammar." This is a
  single-practitioner, single-project account (not a named enterprise case
  study with multiple attributed voices, unlike `blog-cursor-nab-legacy-migration.md`),
  so treat as first-person practitioner evidence: emerging confidence, not
  independently reproduced or peer-reviewed.
- **Scope**: Covers one restoration project end-to-end — a Java 1.5, Ant-built
  "brownfield" repository (`github.com/nikmalykhin/java-blobstore`) that no
  longer compiled on modern Apple Silicon hardware — across four phases
  (Analysis, Wrap, Lift, Refactor) with concrete prompts, Docker configs,
  Gradle configs, and before/after code. Does NOT cover: a team or enterprise
  rollout (this is a solo project), quantified before/after velocity metrics
  (no "Nx faster" claim is made — the article is explicitly about method, not
  speed), non-Java legacy stacks, or independent verification of the
  described outcomes by anyone other than the author.

## Extracted Claims

### Claim 1: A naive, optimistic LLM prompt ("Tourist Prompt") applied to an unfamiliar legacy codebase produced a confident, plausible, but structurally false modernization artifact — hallucinated dependency versions, an assumed standard directory layout that didn't match the real one, and a "Hello World" example that hid known concurrency and error-handling defects
- **Evidence**: Concrete before/after: the author's exact prompt ("Hi, I need
  to start working with this library. Can you please act as a Senior
  Developer and help me get started?... give me a high-level summary... and a
  simple 'Hello World' code example.") is followed by the AI's generated
  `build.gradle` (given verbatim in Concrete Artifacts below), then three
  named specific failures in that output.
- **Confidence**: anecdotal (single first-person trial, one prompt, one
  project — but the specific artifacts, not just a summary, are shown)
- **Quote**: "First, it hallucinated dependencies by suggesting commons-pool2
  (v2.x) when the legacy code actually relied on org.apache.commons.pool
  (v1.x)."
- **Our assessment**: This is a specific, checkable failure mode (not a vague
  "AI hallucinates" claim) — the exact wrong package name is given, and the
  reason it matters is stated precisely: "these libraries have completely
  different APIs, blindly running the AI's code would have crashed the build
  with 'Class Not Found' errors." The author also names two further concrete
  failure dimensions in the same output: assuming a Maven `src/main/java`
  layout against the codebase's actual non-standard Ant layout ("structural
  gaslighting"), and generating a clean example on top of
  `PooledBlobStoreImpl` while omitting that the sibling
  `SimpleBlobStoreImpl` "wasn't even thread-safe" and the "so-called 'Unit
  Tests' were actually integration tests that required a live MySQL
  database to run." This is a useful, named failure mode for the guide:
  legacy-code comprehension prompts that ask "how do I run this" invite the
  model to assume a happy path exists, rather than surface the evidence for
  whether it does.

### Claim 2: A persona-based prompt that explicitly forbids README summarization and instead demands a structured, evidence-citing "Forensic Code Audit" across four named pillars (Carbon Dating, Architectural Integrity, Data Flow & Typing, Safety Check) reliably shifts the model from an optimistic to a critical stance
- **Evidence**: The full prompt template is given verbatim (see Concrete
  Artifacts), followed by the model's response, described as dropping "the
  polite facade immediately" and returning "a Risk Assessment Report with a
  brutal verdict: 'critical rewrite recommended'."
- **Confidence**: anecdotal (one prompt template, one trial, one project; no
  comparison of this technique against other persona-prompting variants)
- **Quote**: "I assigned the AI a specific persona: Senior Legacy Systems
  Architect. I explicitly forbade it from summarizing the README (which is
  often a lie in legacy projects) and ordered a 'Forensic Code Audit'."
- **Our assessment**: The specific, reusable mechanism here is not just
  "use a persona" (already a well-worn prompting tactic) but the combination
  of (a) an explicit negative instruction ("do not summarize the README")
  and (b) a structured deliverable spec (four named pillars, each requiring
  cited forensic evidence, output as a "Risk Assessment Report for a
  stakeholder deciding whether to refactor or rewrite"). This is a concrete,
  transferable prompt template for legacy-code comprehension work, distinct
  from the higher-level "Ask Mode / Plan Mode" tool description in
  `blog-cursor-nab-legacy-migration.md` Claim 5, which describes the
  *outcome* (better user stories and API specs) without showing the actual
  prompt text used to get there.

### Claim 3: A legacy test suite that appears to pass can mask complete absence of coverage on the riskiest code paths, because the tests exercise only a local mock implementation rather than the real networked, thread-unsafe code
- **Evidence**: The AI-driven forensic audit's "Finding 3," describing how
  `TestBlobStore`'s suite relied on `LocalFileBlobStoreImpl`, a from-scratch
  reimplementation of the storage layer that writes to local disk instead of
  exercising the network path.
- **Confidence**: anecdotal (one codebase, one audit)
- **Quote**: "While these tests successfully proved that this local mock
  worked flawlessly in isolation, that superficial success masked an
  alarming reality: the actual networking code, the thread-unsafe pooling,
  and the fragile protocol parser—the absolute most volatile parts of the
  system—were being completely bypassed."
- **Our assessment**: This is a specific instance of a general legacy-code
  risk (green tests that exercise a substitute implementation rather than
  the real one), and the article credits the AI-driven forensic audit — not
  manual code reading — with surfacing it before any refactoring began. The
  practical payoff is stated directly: acting on the earlier "Tourist"
  advice to refactor `SimpleBlobStoreImpl` immediately "would have blindly
  introduced generics and broken the fragile parsing logic. The tests would
  have still passed—thanks to that deceptive local mock—but the actual
  production code would have been completely non-functional."

### Claim 4: When a legacy artifact cannot be stabilized in a modern build environment because encapsulation/visibility rules have tightened over the intervening decades, the fix is not to loosen the legacy code's visibility but to recreate the original ("Time Capsule") environment in Docker and treat the code as strictly immutable during stabilization
- **Evidence**: A specific build failure (Gradle 8 rejecting
  package-private cross-package access that Ant/Eclipse in 2008 permitted)
  is shown verbatim, followed by the author's explicit refusal to change the
  code and the resulting Docker-based strategy pivot.
- **Confidence**: anecdotal (one project, one specific encapsulation failure)
- **Quote**: "Realizing that I couldn't stabilize the artifact in a modern
  environment, I pivoted to a 'Time Capsule' strategy. If I wanted to
  capture this system, I had to build a containment zone that strictly
  mirrored the standards of 2008."
- **Our assessment**: This names a specific decision rule worth generalizing:
  when a legacy build fails against a modern toolchain for reasons rooted in
  the toolchain's evolution (not a code defect), containerizing an
  environment that matches the code's original era is a lower-risk fix than
  patching the code to satisfy the modern tool. The author is explicit that
  this decision was itself guarded by a "prime directive" of zero code
  changes, established in the prior phase specifically to prevent
  "modernizer's hubris" from creeping in ("Okay, I can't change the Java
  code, but surely I can swap out this ancient Ant build for Gradle 8,
  right?").

### Claim 5: Emulation layers (e.g., Rosetta/QEMU for running x86 legacy Docker images on ARM64 hardware) introduce an unacceptable confound when validating an already-fragile legacy build, because a failure could originate from either the code or the emulation layer, and the two cannot be distinguished — the resolution was switching to native x86 hardware entirely
- **Evidence**: Direct description of hitting the constraint (only x86
  Java 6 images were available; the author's laptop was Apple Silicon) and
  the explicit reasoning for rejecting emulation as a workaround.
- **Confidence**: anecdotal (one hardware constraint, one project)
- **Quote**: "If the build fails, how do you know whether it's an inherent
  code defect or just the emulation layer choking on twenty-year-old
  binaries?"
- **Our assessment**: This is a specific, well-reasoned methodological point
  about establishing a *verifiable* baseline: a baseline is only useful as a
  ground truth if failures against it can be unambiguously attributed. Adding
  an emulation layer to a legacy-verification environment reintroduces
  exactly the kind of unattributable-failure ambiguity the whole "Time
  Capsule" strategy (Claim 4) was designed to eliminate. The practical
  resolution — abandoning the ARM64 laptop for a native Intel i9 machine —
  is a concrete, if unglamorous, illustration that hardware architecture
  choice is sometimes a first-order variable in AI-assisted legacy work, not
  an implementation detail.

### Claim 6: Java 8 was selected as the modernization target version specifically because it is the newest JDK still able to compile Java 1.5 source and, simultaneously, one of the oldest JDKs able to run natively on Apple Silicon (ARM64) — a narrow hardware/toolchain intersection, not a stylistic preference — which in turn forced a further pivot from Gradle 8 to Gradle 7.6 because Gradle 8's daemon requires Java 17, which cannot compile Java 1.5 source
- **Evidence**: Two chained, explicit technical constraints (Java version
  vs. ARM64 support; Gradle daemon's Java version requirement vs. Java 1.5
  compilation support), each with the specific version numbers and the
  resulting toolchain.
- **Confidence**: settled (the compatibility facts — Java 17+ dropping
  `-source 1.5` support, Gradle 8's Java 17 daemon requirement, Java 6's lack
  of native ARM64 support — are stated as concrete, checkable technical
  facts about the toolchains involved, not estimates)
- **Quote**: "Because it stands as the absolute last version to support the
  compilation of Java 1.5 targets and one of the earliest versions that can
  be installed natively on modern Mac hardware, it became our perfect
  architectural entry point."
- **Our assessment**: The resulting dependency chain — "Apple Silicon ->
  Java 8 JVM -> Gradle 7.6 -> Java 1.5 Source" — is a concrete, reusable
  worked example of how hardware architecture (not just OS or code age) can
  constrain the feasible toolchain range for legacy modernization work, and
  is a specific instance of the more general "hardware matters" theme
  flagged by the Prospector triage.

### Claim 7: Feeding a model the exact compiler warning output and a targeted instruction to fix only the flagged lines (an "AI-Compiler Feedback Loop"), rather than vaguely asking it to "fix the codebase," produced disciplined, localized refactors from raw types to generics with zero remaining compiler warnings
- **Evidence**: A specific before/after code pair (raw `List`/`Map` fields
  with blind casting → generic `List<InetSocketAddress>`/`Map<InetSocketAddress, Long>`
  with no casting) plus the exact `-Xlint:unchecked`/`-Xlint:deprecation`
  compiler notes that drove the fix.
- **Confidence**: anecdotal (one codebase, one iterative loop, not compared
  against an alternative refactoring approach)
- **Quote**: "I didn't just ask the AI to vaguely 'fix the codebase';
  instead, I used the compiler itself as the ultimate driver."
- **Our assessment**: This is a concrete instantiation of a general
  principle already present in the corpus in more abstract form (tight,
  narrow, evidence-driven prompts outperform broad delegation) — the novel
  contribution here is the specific mechanism (compiler diagnostics as the
  literal input to each prompt iteration, one warning category at a time)
  applied specifically to raw-type-to-generics migration, with a concrete
  before/after code sample the guide could reproduce directly.

### Claim 8: A legacy test suite silently swallowing exceptions ("Lying Tests") gave a misleadingly green build; deliberately stripping the try/catch block to force the process to crash on failure was the first structural code change made, undertaken specifically to convert the test baseline from falsely-green to honestly-red-then-green before any further modernization proceeded
- **Evidence**: Two code snippets given verbatim (the exception-swallowing
  original, and the hardened version with the try/catch removed and
  `throws Exception` added), plus the stated purpose and outcome ("the build
  turned bright red... I spent the next hour tracing down and repairing the
  broken connection configurations until the build pipeline finally flipped
  back to green").
- **Confidence**: anecdotal (one test file, one project)
- **Quote**: "This marked my very first structural change to the legacy
  codebase, and it was done with a singular purpose: to force my verifiable
  baseline to become completely honest."
- **Our assessment**: This directly names and demonstrates a specific
  technique — treat "hardening the baseline" (removing error-swallowing) as
  a deliberate, scoped, first modification, distinct from and prior to any
  feature-level refactoring — that corroborates but is more concrete than
  the general TDD/CI-discipline-as-guardrail claim in
  `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 10. The
  order of operations matters: the author explicitly treats a newly-red
  build as "a massive narrative victory," reframing test failures surfaced
  by hardening as progress, not regression.

### Claim 9: Reproducing hardcoded legacy assumptions (a magic hostname, a magic absolute file path) via Docker network aliases and volume mounts — rather than editing the test code that contained them — let a "wet," environment-dependent integration test pass unmodified inside the containment strategy
- **Evidence**: The `docker-compose.yml` snippet is given verbatim (network
  alias `qbert.legacycorp.com`, volume mount to the exact historical path),
  along with the explicit rationale for not editing the test file.
- **Confidence**: anecdotal (one test file, one project)
- **Quote**: "In a standard modern refactor, I would have simply deleted
  these lines. But because I was strictly in containment mode, touching the
  test file was off the table. Instead of changing the code to fit modern
  reality, I had to change reality to fit the code."
- **Our assessment**: This is a specific, generalizable containment
  technique for any legacy system whose tests encode environment
  assumptions that are themselves undocumented specification (a hardcoded
  hostname/path IS the contract, even though it looks like an accident) —
  the Docker network-alias-plus-volume-mount pattern lets the environment
  satisfy the contract without touching the code that expresses it, which
  is a stronger form of containment discipline than typically described in
  "just containerize it" advice.

### Claim 10: An attempt to replace the manual `docker-compose` setup with TestContainers was deliberately abandoned mid-migration after it turned into a multi-front "Big Bang" refactor compounded by Docker-in-Docker networking complexity on ARM, in favor of reverting to the simpler, already-working manual "External Sidecar" pattern
- **Evidence**: Direct first-person account of the failed migration attempt,
  its specific failure mode (simultaneous overhaul of test runner, network
  topology, and startup logic), and the deliberate decision to abort.
- **Confidence**: anecdotal (one migration attempt, one project — and
  explicitly a *negative* result the author chose not to pursue further)
- **Quote**: "This friction taught me a vital engineering lesson: momentum
  is oxygen. The moment I realized I was spending all my energy fighting
  the tooling rather than recovering the actual code, I made the conscious
  decision to abort the experiment."
- **Our assessment**: This is a first-class failure report embedded inside a
  larger success narrative (per MINER.md's guidance to treat these with the
  same rigor as positive patterns). The specific, transferable lesson is the
  named anti-pattern — attempting to modernize test runner, network
  topology, and startup logic simultaneously ("Big Bang" scope) — paired
  with a named recovery heuristic ("momentum is oxygen": stop when more
  effort is going into fighting tooling than into the actual recovery goal)
  and an explicit acceptance of a less "clean" but functional pattern
  (manual `docker-compose up`, termed the "External Sidecar" pattern) over a
  theoretically more elegant one.

### Claim 11: A final concurrency verification step — modernizing a load-testing tool to use `ExecutorService` and running 100 iterations across 10 concurrent threads against the containerized backend — was treated as a required, distinct proof step before declaring the AI-assisted modernization complete, not an optional nice-to-have
- **Evidence**: Specific test parameters (100 iterations, 10 concurrent
  threads) and the stated purpose (proving `PooledBlobStoreImpl`'s
  Apache-Commons-Pool-based isolation actually holds under load after the
  generics/JUnit/collection-type changes).
- **Confidence**: anecdotal (one test run, one project; no comparison against
  skipping this step)
- **Quote**: "By verifying this behavior under intense, simulated
  real-world conditions, I confirmed that our deep modernizations—the
  generics, the JUnit migration, and the structural collection swaps—had
  not destabilized the core historical logic."
- **Our assessment**: This closes the loop on Claim 3 (the original test
  suite bypassed exactly this thread-safety-critical code path) — the
  author explicitly returns to verify, under load, the specific risk
  category the forensic audit flagged as unverified at the start. This is a
  concrete example of designing verification around the *specific* risks a
  system was known to carry, rather than a generic "run the tests" checkbox.

### Claim 12: The author frames the overall outcome not as AI autonomously restoring the system, but as AI acting as a "force multiplier" for mechanical translation work (Ant→Gradle conversion, Dockerfile drafting, squashing ~50 compiler warnings) while the human provided strategy, sequencing, and persona-switching (Architect → DevOps Engineer → Performance Engineer → repository maintainer) across the four phases
- **Evidence**: The article's explicit closing thesis, following a
  structured account of the persona changes made at each phase transition.
- **Confidence**: emerging (this is the author's own interpretive framing of
  their own project, stated directly and consistently applied throughout
  the article's phase-by-phase structure — not an independent measurement,
  but not merely an incidental aside either)
- **Quote**: "The AI didn't magically restore this historical system on its
  own; rather, I restored it by wielding the technology as a powerful force
  multiplier."
- **Our assessment**: The specific, reusable pattern buried inside this
  general "AI as force multiplier" framing (a common refrain across the
  corpus) is persona-switching tied to phase transitions: "I switched AI
  persona from Architect to Senior DevOps Engineer" (Phase I → II), then to
  "senior performance engineer" (final concurrency phase), then "I switched
  my AI persona one last time to act as a lead repository maintainer"
  (handover). Each switch is paired with a distinct deliverable type (risk
  assessment → working Docker environment → verified concurrency → clean
  handover). This is a more granular, phase-tied version of persona
  prompting than the single-persona "Archaeologist Prompt" in Claim 2.

## Concrete Artifacts

### The "Tourist Prompt" and its AI-generated `build.gradle`

```
Source: "The Archaeologist's Copilot," martinfowler.com, 16 July 2026
        Section: "The 'Tourist' Trap"

Prompt used:
"Hi, I need to start working with this library. Can you please act as a
Senior Developer and help me get started? Read the repo and give me a
high-level summary... and a simple 'Hello World' code example."

AI-generated build.gradle (verbatim):

plugins {
   id 'java'
}

group = 'com.legacycorp.blobstore'
version = '1.1'

sourceCompatibility = '1.8'
targetCompatibility = '1.8'

repositories {
   mavenCentral()
}

dependencies {
   implementation 'org.apache.commons:commons-pool2:2.11.1'
   implementation 'log4j:log4j:1.2.17'
   testImplementation 'junit:junit:4.13.2'
}

test {
   useJUnit()
}
```

### The Archaeologist Prompt (full template, verbatim)

```
Source: "The Archaeologist's Copilot," martinfowler.com, 16 July 2026
        Section: "Phase I: The Analysis" / "The Archaeologist Prompt"

I am conducting a technical due diligence assessment on this legacy Java
repository: https://github.com/nikmalykhin/java-blobstore.

Act as a Senior Legacy Systems Architect. Your goal is not to tell me what the
code "does," but to evaluate its structural health and "age."

Do not summarize the README. Instead, perform a "Forensic Code Audit" focusing
on these four pillars:

1.  Carbon Dating (The Era):
    * Based on syntax (e.g., raw types vs. generics, annotations), imports, and
    build tools (Ant vs. Maven), estimate the specific Java version (e.g., 1.4,
    1.5, 6) and the year this code was likely written.
    * Cite specific lines of code as "forensic evidence."

2.  Architectural Integrity (The Structure):
    * Does it follow standard separation of concerns (Transport vs. Protocol vs.
    Logic), or is it a "Big Ball of Mud"?
    * Identify any "God Classes" that are doing too much.

3.  Data Flow & Typing (The "Stringly" Trap):
    * Analyze how data is passed. Is it using proper Domain Objects, or is it
    relying on "Stringly-typed" Maps and raw arrays?
    * Look for "Leaky Abstractions" where protocol details leak into business logic.

4.  The "Safety" Check (Error Handling & Threading):
    * Look for anti-patterns in error handling (swallowed exceptions, returning null).
    * Analyze the threading model. Is SimpleBlobStoreImpl thread-safe?

Output your findings as a structured "Risk Assessment Report" for a stakeholder
deciding whether to refactor or rewrite.
```

### Build failure from tightened encapsulation rules (2008 Ant/Eclipse vs. 2026 Gradle 8/modern JDK)

```
Source: "The Archaeologist's Copilot," martinfowler.com, 16 July 2026
        Section: "Phase II: The Wrap" / "The Mission: Brownfield Restoration"

/src/test/java/com/legacycorp/blobstore/test/TestBackend.java:12:
error: Backend is not public in com.legacycorp.blobstore; cannot be accessed from outside package
        Backend backend = new Backend(trackers, true);
        ^
```

### The "Time Capsule" docker-compose.yml (network alias + volume-mount trickery)

```
Source: "The Archaeologist's Copilot," martinfowler.com, 16 July 2026
        Section: "The 'Wet' Test: Bending Reality"

services:
  blobstore:
    image: hrchu/blobstore-all-in-one:latest
    networks:
      default:
        aliases:
          - qbert.legacycorp.com

  builder:
    image: blobstore-legacy-builder
    volumes:
      - .:~/Projects/blobstore/java/com/legacycorp/blobstore/
    command: ant test
```

### AI-Compiler Feedback Loop: raw types → generics (before/after)

```
Source: "The Archaeologist's Copilot," martinfowler.com, 16 July 2026
        Section: "Phase III: The Lift" / "The AI-Compiler Feedback Loop"

Compiler warning that drove the fix:
  Note: Some input files use or override a deprecated API.
  Note: Recompile with -Xlint:deprecation for details.
  Note: Some input files use unchecked or unsafe operations.
  Note: Recompile with -Xlint:unchecked for details.

BEFORE (Java 1.4-style raw types, blind casting required):
  public class Backend {
      private List hosts;
      private Map deadHosts;

      public void reload(List trackers, boolean connectNow) {
          this.hosts = trackers;
          this.deadHosts = new HashMap();
      }

      InetSocketAddress host = (InetSocketAddress) hosts.get(index);
  }

AFTER (Java 8-style generics, compiler-enforced, no casting):
  public class Backend {
      private List<InetSocketAddress> hosts;
      private Map<InetSocketAddress, Long> deadHosts;

      public void reload(List<InetSocketAddress> trackers, boolean connectNow) {
          this.hosts = trackers;
          this.deadHosts = new HashMap<>();
      }

      InetSocketAddress host = hosts.get(index);
  }
```

### "Lying Tests" — before/after hardening (exception-swallowing removed)

```
Source: "The Archaeologist's Copilot," martinfowler.com, 16 July 2026
        Section: "The 'Lying Tests' Discovery" / "Hardening the Baseline"

BEFORE (silently swallows failures; always exits 0):
  public static void main(String[] args) {
      try {
          BlobStore bs = new PooledBlobStoreImpl(...);
          bs.storeFile("test_file", ...);
          System.out.println("Success!");
      } catch (Exception e) {
          System.out.println("Failed: " + e.getMessage());
          e.printStackTrace();
      }
  }

AFTER (hardened; crashes naturally on any failure):
  public static void main(String[] args) throws Exception {
      BlobStore bs = new PooledBlobStoreImpl(...);
      bs.storeFile("test_file", ...);
  }
```

### Hardware/toolchain dependency chain (Phase III)

```
Source: "The Archaeologist's Copilot," martinfowler.com, 16 July 2026
        Section: "The 'Java 17 Trap'"

Apple Silicon -> Java 8 JVM -> Gradle 7.6 -> Java 1.5 Source

(Java 17+ cannot compile -source 1.5; Gradle 8's daemon requires Java 17;
 Java 6 has no native ARM64 build; Java 8 is the single JDK version that
 satisfies both the compile-target floor and the native-ARM64 ceiling.)
```

### Four-Phase Methodology and Before/After Transformation Table

```
Source: "The Archaeologist's Copilot," martinfowler.com, 16 July 2026

Phase I:   The Analysis  — forensic audit via the Archaeologist Prompt;
                            "Critical Legacy" verdict; containment over repair
Phase II:  The Wrap      — Docker "Time Capsule" (Java 6/Ant, native x86);
                            zero code changes; network/volume Docker trickery
Phase III: The Lift      — Java 8 + Gradle 7.6; AI-Compiler Feedback Loop;
                            "Lying Tests" hardened; zero compiler warnings
Phase IV:  The Refactor  — standard src/main/java layout; JUnit 5 migration;
                            TestContainers attempt abandoned; concurrency
                            verified via ExecutorService stress test

                    Day 0 (The Archive)        Day N (The Product)
Build System        Ant                        Gradle 8
Compiler            Java 1.5                   Java 8
Environment         "Works on my machine"      Docker
Testing             Manual Scripts             JUnit 5
Safety              Runtime Risk               Compile-time Safety
Confidence          Swallowed Exceptions       Hardened Tests
Onboarding          "Good luck figuring it out" README.md
```

## Cross-References

### Cross-reference verification notes
`blog-cursor-nab-legacy-migration.md`, `blog-thoughtworks-harrison-insurance-legacy-modernization.md`,
and `blog-thoughtworks-lewis-gov-structural-modernization.md` were re-read
directly (MINER.md §4b) and the claim numbers cited below were confirmed
against those notes' numbered `### Claim N:` headings in document order
before writing this section. `blog-fowler-boeckeler-local-models-viability.md`
was also checked (per the Prospector's overlap list) but is scoped to local
model hardware viability, not legacy modernization method, and shares no
specific claim-level overlap with this source — it is not cited below.

- **Corroborates**:
  - `blog-thoughtworks-harrison-insurance-legacy-modernization.md` Claim 7
    (AI has changed legacy-modernization economics by reducing uncertainty
    and manual comprehension effort, "not by turning modernization into a
    push-button exercise"): This source is a concrete, artifact-level
    illustration of exactly that hedge. The "Tourist Trap" (Claim 1 above)
    is what happens when the push-button temptation is followed literally
    ("How do I run this?"); the Archaeologist Prompt and four-phase
    methodology (Claims 2, 4-11) are the "not push-button" disciplined
    alternative Harrison's article describes only in the abstract. Two
    independent Thoughtworks-published sources now converge on the same
    "AI reduces comprehension cost but does not eliminate the underlying
    disciplined work" claim — one at the strategic/economic level
    (Harrison), one at the engineering-execution level (this source).
  - `blog-cursor-nab-legacy-migration.md` Claim 5 (Ask Mode/Plan Mode
    generating user stories and API specs from legacy code, compressing
    BizCalc pre-development work from 2 months to 1 week): Both sources
    describe AI's core legacy-modernization value as substituting for
    manual legacy-system comprehension effort. This source's contribution
    is the actual prompt template and technique (Claim 2's Archaeologist
    Prompt) behind that value, where the NAB source describes only the
    tool mode used (Ask/Plan) and the resulting artifact type (user
    stories, API specs) without showing prompt text.
  - `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 10
    (test-driven development, continuous integration, and refactoring
    discipline are guardrails for AI-assisted development): This source's
    "Hardening the Baseline" pattern (Claim 8 — deliberately stripping
    exception-swallowing to force an honest red build before trusting a
    legacy test suite as a safety net) is a specific, concrete technique
    instantiating that general claim, adding a level of mechanism Lewis's
    article does not provide.

- **Contradicts**: None filed as a formal contradiction. There is a framing
  difference worth naming: `blog-cursor-nab-legacy-migration.md` Claims 6-7
  report headline velocity multipliers (3x, 5-8x) achieved via relatively
  direct AI delegation (Ask/Plan modes, Composer), while this source reports
  no velocity figure at all and instead emphasizes the discipline required to
  avoid AI-driven false confidence. This is not a material contradiction per
  MINER.md §4a — the two sources describe different projects, different
  scopes (enterprise team vs. solo practitioner), and neither source claims
  the other's approach is wrong; NAB's Ask/Plan mode usage is not shown in
  enough prompt-level detail to know whether it resembles the "Tourist" or
  "Archaeologist" approach described here.

- **Extends**:
  - `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 7
    (eight named bottlenecks between AI prototype and trusted production,
    including "Brittle legacy systems" and "Fragmented architectures"): This
    source is a granular, single-project case study of exactly that named
    bottleneck category in action — the four-phase methodology (Analysis →
    Wrap → Lift → Refactor) is one concrete way to work through a "brittle
    legacy system" bottleneck rather than merely naming it as an obstacle.
  - `blog-cursor-nab-legacy-migration.md` Claim 5: extends the NAB source's
    high-level description of AI-assisted legacy comprehension with the
    actual reusable prompt template (Claim 2's Archaeologist Prompt) and a
    concrete illustration of the naive-prompt failure mode (Claim 1's
    Tourist Trap) that the NAB source does not document.

- **Novel**:
  - **The Archaeologist Prompt** (Claim 2): No existing corpus source
    provides a full, reusable, persona-plus-structured-deliverable prompt
    template specifically for forensic legacy-code risk assessment with
    named pillars (Carbon Dating, Architectural Integrity, Data Flow &
    Typing, Safety Check).
  - **The "Tourist Trap" naive-prompt failure mode** (Claim 1): No existing
    corpus source documents, with specific artifacts (an actual hallucinated
    `build.gradle`), what a naive "how do I run this" legacy-code prompt
    produces and why each specific failure (wrong dependency version, wrong
    directory layout, masked concurrency/error-handling defects) occurred.
  - **Docker "Time Capsule" containment strategy** (Claim 4) and the
    network-alias-plus-volume-mount technique for satisfying hardcoded
    legacy test assumptions without editing test code (Claim 9): No existing
    corpus source documents recreating a historical build/runtime
    environment in Docker, under a strict zero-code-change policy, as a
    deliberate pre-modernization containment step.
  - **"Lying Tests" pattern and hardening technique** (Claim 8): No existing
    corpus source names and demonstrates, with before/after code, the
    specific technique of stripping exception-swallowing from a legacy test
    harness as the first, deliberately-scoped structural change made before
    any feature-level refactoring.
  - **AI-Compiler Feedback Loop** (Claim 7): No existing corpus source
    documents feeding literal compiler warning output back to the model as
    the iteration driver for a raw-types-to-generics migration, as opposed
    to broader "refactor this file" delegation.
  - **TestContainers migration abandonment / "External Sidecar" pattern**
    (Claim 10): No existing corpus source documents a mid-migration
    abandonment of a "cleaner" tooling migration in favor of a working
    manual pattern, with the named heuristic "momentum is oxygen."
  - **Phase-tied persona switching** (Claim 12): No existing corpus source
    documents switching the AI's assigned persona at each project-phase
    transition (Architect → DevOps Engineer → Performance Engineer →
    repository maintainer) as a deliberate technique tied to the
    deliverable type expected at each phase.

## Guide Impact

- **Chapter 02 (Harness Engineering) — legacy-code comprehension prompting**:
  Add the Archaeologist Prompt (Claim 2, full template in Concrete Artifacts)
  as a named, reusable technique for legacy-code forensic analysis: assign a
  skeptical persona, explicitly forbid summary-mode reading, and require a
  structured, evidence-citing deliverable. Pair it directly with the "Tourist
  Prompt" failure mode (Claim 1) as the concrete negative example the
  Archaeologist Prompt is designed to avoid — a naive "how do I run this"
  prompt on unfamiliar legacy code produces confident, checkable-but-wrong
  output (hallucinated dependency version, assumed directory layout, masked
  defects), not a generic "AI hallucinates" warning.

- **Chapter 03 (Verification) — test-suite trust and hardening**: Add the
  "Lying Tests" pattern and hardening technique (Claim 8: deliberately strip
  exception-swallowing to force an honest red build before treating a legacy
  test suite as a refactoring safety net) as a concrete verification pattern.
  This gives `blog-thoughtworks-lewis-gov-structural-modernization.md`
  Claim 10's more abstract "TDD/CI as AI guardrail" claim a specific,
  reproducible mechanism: before trusting any pre-existing test suite as a
  baseline for AI-assisted refactoring, verify it can actually fail.

- **Chapter 05 (Team Adoption) — legacy modernization section** (which
  already cites `blog-cursor-nab-legacy-migration.md` Claims 6-7 around
  `guide/05-team-adoption.md:963-975`): Add this source as a second,
  execution-level case study alongside NAB's outcome-level metrics. Where
  the NAB source documents *that* AI-assisted legacy comprehension worked (a
  2-months-to-1-week compression), this source documents *how* — the actual
  prompt engineering (Claim 2), containment methodology (Claim 4, Claim 9),
  and verification discipline (Claim 3, Claim 8, Claim 11) behind that kind
  of outcome. Also add the Docker "Time Capsule" containment strategy
  (Claim 4) as a named infrastructure pattern for establishing a verifiable
  baseline before any AI-assisted modernization work begins.

## Extraction Notes

1. **WebFetch's AI-mediated summarization produced inconsistent quotes
   across passes; raw HTML was fetched directly instead**: An initial
   WebFetch pass returned a lossy summary. Follow-up WebFetch passes
   explicitly requesting short verbatim quotes returned text that, on
   cross-checking, was internally inconsistent — e.g., one pass returned
   the closing "force multiplier" sentence as "The AI didn't magically
   restore this historical system on its own; rather, I restored it by
   wielding the technology as a powerful force multiplier," while a later
   pass returned a *different* sentence ("Success only arrived when I
   wielded the technology as a powerful force multiplier") for the same
   citation request. To resolve this and satisfy MINER.md §2a's
   verbatim-quote requirement, the raw HTML was fetched directly via `curl`
   with a browser user-agent, tags were stripped with a Python script
   (preserving `<pre>` code blocks separately), and the full ~2,800-word
   article body was read from that raw-text extraction. Every quote in this
   note was copied character-for-character from that raw-text file, not
   from any WebFetch-summarized pass; the correct "force multiplier" quote
   (confirmed against the raw HTML) is the one used in Claim 12.
2. **No sub-pages followed**: The article is self-contained; no inline links
   to substantive external pages were found in the raw HTML extraction
   (the linked GitHub repository URL in the Archaeologist Prompt is quoted
   as prompt content, not followed as a separate source).
3. **A named lead for a future source**: The Acknowledgments credit "Matteo
   Vaccari for the series of articles on AI-assisted modernization" as "a
   key inspiration." A grep across `source-notes/` for "Vaccari" found no
   existing corpus source — this is a candidate lead for a future source
   submission, not something extracted here since the referenced series
   itself was not fetched or read.
4. **No contradictions filed**: Cross-referenced against the three
   overlapping legacy-modernization notes named by the Prospector
   (`blog-cursor-nab-legacy-migration.md`,
   `blog-thoughtworks-harrison-insurance-legacy-modernization.md`,
   `blog-thoughtworks-lewis-gov-structural-modernization.md`) — found strong
   corroboration and extension but no material contradiction; see
   Cross-References → Contradicts above for the one framing tension
   (velocity-multiplier claims vs. no-velocity-figure/discipline-emphasis
   framing) that was considered and judged not to rise to a formal
   contradiction per MINER.md §4a, since the sources describe different
   projects at different scales rather than opposing claims about the same
   situation.
5. **Overall confidence rationale**: Rated `emerging` rather than
   `anecdotal` because, while this is a single-practitioner, unreplicated
   case study (most individual claims are anecdotal in isolation), the
   article provides an unusually high density of concrete, independently
   checkable artifacts (verbatim prompts, before/after code, config files,
   specific version-compatibility facts) rather than summary-level
   assertions — several individual claims (Claim 6's toolchain
   compatibility facts, Claim 12's stated authorial framing) are rated
   `settled` on their own terms. Not rated `settled` overall because the
   central methodological claims (that the Archaeologist Prompt technique,
   the Time Capsule strategy, and the various hardening/verification steps
   generalize beyond this one project) are asserted by a single author on a
   single project with no independent replication.
