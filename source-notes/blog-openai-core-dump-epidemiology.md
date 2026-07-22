---
source_url: https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug
source_type: blog-post
title: "Core dump epidemiology: fixing an 18-year-old bug"
author: Nathan Bronson, Member of Technical Staff (OpenAI)
date_published: 2026-06-30
date_extracted: 2026-07-22
last_checked: 2026-07-22
status: current
confidence_overall: settled
issue: "#2131"
---

# Core dump epidemiology: fixing an 18-year-old bug

> First-party OpenAI engineering account of diagnosing seemingly-impossible C++
> crashes in Rockset (ChatGPT's data infrastructure) by abandoning single-case
> debugging in favor of an automated, population-scale analysis of a year of
> production core dumps — built with an AI-authored analysis script — which
> revealed two unrelated bugs: a bad-hardware host and an 18-year-old GNU
> libunwind race condition.

## Source Context

- **Type**: blog-post (openai.com/index, June 30, 2026)
- **Author credibility**: Nathan Bronson, "Member of Technical Staff" at OpenAI,
  writing a first-party technical account of an internal production incident in
  Rockset (a data-infrastructure service OpenAI acquired in 2024 and uses for
  ChatGPT sync connectors and search over conversations). The post includes
  compiler/ABI-level detail (exact assembly behavior of `_Ux86_64_setcontext`,
  register names, ABI red-zone semantics), a link to an upstreamed fix commit in
  the GNU libunwind repository, and named internal tooling (`coarse_thread_cputime_clock`).
  This level of specificity is consistent with a genuine engineering postmortem
  rather than marketing copy.
- **Scope**: Covers one specific debugging investigation end to end — initial
  single-core forensic analysis, the pivot to population-level analysis, the
  discovery that "one bug" was actually two, the root-cause analysis of both,
  and the fixes/mitigations applied. It does NOT cover: broader OpenAI
  infrastructure architecture beyond Rockset, other services' reliability
  practices, or any AI-agent-specific harness/tooling design (the "ChatGPT wrote
  a script" detail is a single sentence, not a described workflow).

## Extracted Claims

### Claim 1: What looked like one inexplicable bug was actually two unrelated, coincidentally concurrent bugs — silent CPU hardware corruption on one host, and an 18-year-old open-source library race condition
- **Evidence**: The post's own framing of the investigation's outcome, stated in the introduction before the technical narrative begins.
- **Confidence**: settled (first-party statement of the resolved root cause, later substantiated by the rest of the post's technical narrative)
- **Quote**: "What we assumed was one problem eventually turned out to be two unrelated bugs, coincidentally discovered at the same time. First, silent hardware corruption on one Azure host, where the CPU just didn't do math correctly. Second, an 18-year-old race condition in GNU libunwind, an unnoticed bug in a widely used open source library."
- **Our assessment**: The "coincidentally concurrent" framing is the key methodological trap the post is about: two independent, unrelated bugs surfaced in overlapping symptoms and were mentally merged into a single, harder-to-explain phantom bug. This is a specific, verifiable failure mode (conflating independent root causes because their symptoms overlap) that generalizes well beyond C++ or infrastructure debugging.

### Claim 2: The team explicitly frames debugging as a choice between "doctor" mode (deep single-case analysis) and "epidemiologist" mode (population-level pattern search), and names the shift to the latter as the turning point
- **Evidence**: A dedicated section titled "Doctor or epidemiologist?" that names the two approaches directly and states which one the team had been stuck in.
- **Confidence**: settled (first-party account of the team's own diagnostic reasoning, not a general claim about debugging practice)
- **Quote**: "One is to act like a doctor of sorts: focus on one patient, run lots of tests, and try to diagnose a single case from detailed evidence. The other is to act more like an epidemiologist: look at the entire population and ask whether there are patterns that a single case cannot reveal. Did the bug start at a specific release? Does it correlate with one hardware SKU (the specific CPU and server model), one region, or one kernel version? Are there multiple distinct clusters hiding inside what looks like one syndrome?"
- **Our assessment**: This is the article's central, reusable framing device — a named, two-mode model of debugging strategy that is directly actionable: when single-case deep-dives stall out (as they did here "for a few days" on one misaligned-`%rsp` crash), the explicit next move is to build population data rather than go deeper on the same case.

### Claim 3: The initial "doctor" approach — closely inspecting individual core dumps and ruling out hypotheses one at a time — stalled because the number of candidate causes was too large and every hypothesis had contradicting evidence
- **Evidence**: Narrative description of the first debugging attempt, including the specific candidate causes considered (compiler/linkage issue, runtime library bug, kernel bug in signal delivery, ASAN gap) and why log-based detection also failed.
- **Confidence**: settled (first-party account of a specific investigation)
- **Quote**: "Our initial approach was to treat these cores like a conventional debugging problem: inspect a few core dumps very closely, form hypotheses, and rule them out one by one."
- **Our assessment**: Notable that this is presented as the reasonable, default first move — not a mistake in itself. The failure was not trying single-case analysis; it was staying in that mode for "a few days" on one crash without stepping back once it stopped producing progress.

### Claim 4: The x86-64 System V ABI's 128-byte "red zone" below `%rsp`, which the kernel is contractually forbidden from clobbering on signal delivery, was the specific technical mechanism that let the team partially reconstruct already-returned stack frames from a core dump
- **Evidence**: Technical explanation of the ABI guarantee and how it was used to recover partial information ("X's just-popped stack frame looked valid, except for a NULL return address") from crashes that occurred after a function had already returned.
- **Confidence**: settled (this is a documented ABI property, not a hypothesis)
- **Quote**: "On Linux `x86_64`, the AMD64 System V ABI also reserves 128 bytes below `%rsp` as the red zone. That region is available to userspace code and, importantly, the kernel promises not to clobber it when it delivers a signal, as part of the ABI contract."
- **Our assessment**: A concrete, verifiable low-level fact used correctly. This is the piece of forensic infrastructure that made "clues from the stack" possible at all — without the red zone guarantee, a post-return crash would leave no trace of the already-popped frame to examine.

### Claim 5: Text-based log searches could not reliably identify all occurrences of the bug because stack-corruption crashes corrupt or erase the very stack traces that would otherwise identify them, producing both false positives and false negatives
- **Evidence**: Direct statement of the specific limitation encountered when trying to build a query over existing logs.
- **Confidence**: settled (first-party account of a specific, failed detection approach)
- **Quote**: "We tried to use our application-level logs to identify all occurrences of the problem, but stack-corruption bugs are hard to classify from logs alone because the logged stack traces are themselves corrupted or missing. We weren't able to construct a log query that didn't have both false positives and false negatives."
- **Our assessment**: This is the specific reason population-level analysis had to be built directly from core dumps rather than logs: for this class of bug, the log signal is degraded by the same mechanism causing the bug, so the detection method had to bypass logs entirely and go to raw crash artifacts.

### Claim 6: The turning point in the investigation was having ChatGPT write a script that automatically parsed, classified, and filtered every production core dump from the previous year, replacing labor-intensive manual inspection
- **Evidence**: Direct account of building an automated pipeline — script downloads a prefix of each core file, extracts registers, filters known false positives using logs, and labels each crash by type — then running it in parallel across a year of Rockset's production core dumps.
- **Confidence**: settled (first-party account of the specific tool built and its stated effect)
- **Quote**: "We had ChatGPT write a script that downloaded a prefix of each core file, extracted the registers, filtered known false positives using the logs, and automatically labeled the crash as return-to-null, misaligned-stack, or other. Then we ran that script in parallel over every production Rockset core dump from the previous year. This was the turning point."
- **Our assessment**: This is the one place the post directly names AI involvement in the investigation, and it is scoped narrowly: a well-specified, verifiable, boring data-processing task (download, extract fields, classify, filter) delegated wholesale, rather than asking an AI to diagnose the bug itself. The "turning point" characterization is about the population-scale dataset the script produced, not about AI reasoning over the crashes — the actual pattern-finding and root-causing was done by the human team once the dataset existed.

### Claim 7: Once a clean, automatically-labeled dataset existed, correlations appeared immediately, revealing that "one bug" was actually two distinct crash populations distinguishable by region, start date, and hardware pattern
- **Evidence**: Direct before/after account of what the population dataset revealed: return-to-null crashes were spread across many clusters/regions with no crisp start date, while misaligned-stack crashes were confined to one region, had a clear start date, and correlated with node uptime.
- **Confidence**: settled (first-party account of the analysis result)
- **Quote**: "Once we had a clean data set, correlations appeared immediately. What we had been treating as one weird bug was actually _two_ separate crash populations."
- **Our assessment**: This is the load-bearing claim of the whole post: the shift from anecdote to dataset is what exposed the conflation described in Claim 1. Before the dataset existed, the team was (per Claim 3) mixing counterexamples from both bug populations into a single mental model, which made every hypothesis seem to have contradicting evidence — because it did, just from two different bugs.

### Claim 8: Bug #1 (hardware corruption) was traced to a single physical Azure host via the population dataset, could not be reproduced in a controlled environment after weeks of stress testing, but crashes disappeared entirely once that host was removed from service
- **Evidence**: Direct account of the diagnosis and resolution path for the first bug, plus concrete follow-on mitigations: enhanced fatal signal handler logging (register state, so recurrence is detectable from logs without needing a fresh core dump), a control-plane change to reuse VMs rather than recycle them (making a recurring bad node easier to identify), and updated runbooks.
- **Confidence**: settled (first-party account, though the underlying hardware fault mechanism itself was never confirmed via reproduction)
- **Quote**: "We were not able to reproduce the register corruption on that host in a controlled environment, even after several weeks of stress testing. Once the problematic host was taken out of service, however, the misaligned-stack crashes disappeared."
- **Our assessment**: Notable epistemic honesty: the team never confirmed the exact hardware fault mechanism — they only confirmed correlation (this host, these crashes) and the intervention's effect (remove host, crashes stop). The post explicitly frames the accompanying process changes (better signal-handler telemetry, VM-reuse policy) as durable value independent of understanding the exact hardware failure, since "removing the bad host isn't a permanent solution... it doesn't prevent a new occurrence."

### Claim 9: Bug #2 was an 18-year-old race condition in GNU libunwind's `_Ux86_64_setcontext`, where a signal landing in a window exactly one machine instruction wide — after `%rsp` is updated but before the destination instruction pointer is read from the now-unprotected memory — corrupts the instruction pointer that will be jumped to
- **Evidence**: Direct assembly-level walkthrough: the routine synthesizes a `ucontext_t` struct on the stack, and one specific instruction updates `%rsp` to point past that struct (ending the ABI red-zone protection over it) before a later instruction reads the target instruction pointer out of it. A signal landing in between causes the kernel to build its signal frame at `%rsp-128`, which can overwrite the now-unprotected `ucontext_t` before the read happens.
- **Confidence**: settled (root cause confirmed via source reading and, per Claim 12, an upstreamed fix accepted by the GNU libunwind maintainers)
- **Quote**: "In this case the vulnerable window is literally one instruction wide! A signal must be delivered after `%rsp` has been changed, but before the next instruction loads `%rip`. Several simple instructions like this can be run per cycle on a modern super-scalar out-of-order CPU, so the race window is roughly a hundred picoseconds."
- **Our assessment**: This is the most technically striking claim in the post — a race window measured in fractions of a nanosecond, in code that had shipped for 18 years. It is also the claim best-corroborated outside the post itself: the accompanying GitHub commit (see Concrete Artifacts) shows the maintainers accepted the fix, which is independent confirmation the race is real and not just OpenAI's internal hypothesis.

### Claim 10: A Fermi estimate reconciled the vanishingly small per-instance probability of a single-instruction race with the observed fleet-wide crash rate of "more than a dozen return-to-null crashes per day," by combining the race window's duration with Rockset's signal delivery rate and its unusually high exception-throwing rate under backpressure
- **Evidence**: An order-of-magnitude calculation: given the race window's duration and the periodic signal's frequency, each individual exception-cleanup/catch event has a roughly one-in-a-hundred-million chance of losing the race; Rockset's backpressure mechanism throws on the order of ten thousand exceptions per second on an overloaded host, which multiplies out to roughly one crash every few hours per host — enough, at fleet scale, to produce the observed daily crash count.
- **Confidence**: settled as an order-of-magnitude argument, though the exact numeric values in the source's published notation did not extract cleanly as plain text (see Extraction Notes) and are paraphrased here rather than quoted
- **Quote**: (no direct quote; see paraphrase in Our assessment — the source renders the specific probabilities as mathematical notation that did not survive plain-text extraction intact, e.g. "$1 0^{- 10}$" for what is almost certainly "10⁻¹⁰")
- **Our assessment**: The Fermi-estimation step is arguably as important methodologically as the assembly-level root cause: it's the check that stopped the team from dismissing an apparently-absurd one-instruction race as "too rare to matter," by showing the math actually supports it once Rockset's specific, unusually high exception and signal rates are plugged in. This models a specific, reusable debugging habit — sanity-check an implausible-seeming mechanism with a back-of-envelope rate calculation before discarding it.

### Claim 11: The 18-year-old libunwind bug only became operationally visible now because three of Rockset's specific characteristics converged — high exception-throwing rate for backpressure, unusually frequent signal delivery for CPU-time accounting, and a recent code change that increased the signal handler's stack usage
- **Evidence**: Direct explanation naming all three factors and noting that the crash rate stayed at zero until the stack-usage-increasing change (adding a call to `timer_getoverrun`), after which the rate remained low until load was later increased.
- **Confidence**: settled (first-party account, with the specific ordering — no crashes before the stack-usage change, crashes only after — offered as evidence for the causal claim)
- **Quote**: "Rockset is unusual on all three axes. We throw exceptions at high rates as part of normal overload control; we deliver `SIGUSR2` unusually often because of `coarse_thread_cputime_clock`; and earlier this year we made the `SIGUSR2` handler use more stack by adding a call to `timer_getoverrun`, so we could account for merged signals."
- **Our assessment**: This is the answer to "why now, after 18 years" and it's a genuinely instructive systems point: a latent bug's visibility is a function of a *product* of independent operational parameters (exception rate × signal rate × handler stack depth) crossing some threshold, not any single parameter change alone. A team investigating "why did this suddenly start happening" should look for the combination of several recent changes, not just the most recent one.

### Claim 12: The immediate mitigation was switching Rockset from GNU libunwind to libgcc's unwinder — itself a performance improvement due to reduced lock contention at scale — and the team also upstreamed a self-contained reproducer and a fix to the GNU libunwind project
- **Evidence**: Direct statement of the mitigation and its side benefit, plus a linked GitHub commit as the upstreamed fix.
- **Confidence**: settled (first-party statement; the linked commit is independently checkable)
- **Quote**: "Our immediate mitigation was to switch from GNU libunwind to libgcc's unwinder. That was a good trade on its own: libgcc's implementation has benefited from a lot of work to reduce lock contention, which matters when scaling to large VMs."
- **Our assessment**: The switch is framed as a strict improvement independent of the bug (better lock contention behavior at scale), which is a useful detail: the "fix" wasn't purely defensive, it was a net-positive infrastructure change the bug investigation surfaced as worth making anyway.

### Claim 13: A separate, surprising technical detail surfaced mid-investigation — GNU libunwind's exception-unwinding symbols, not libgcc's, were the ones actually chosen by the dynamic linker in the running binary, contrary to the team's expectation from symbol versioning rules
- **Evidence**: Direct statement that inspecting running binaries contradicted the team's expectation of which library's implementation would "win" at link time.
- **Confidence**: settled (first-party account of empirically checking running-binary behavior)
- **Quote**: "GNU libunwind's definitions were the ones chosen by the dynamic linker. That surprised us; we had expected the libgcc implementation to win because of symbol versioning rules; however, inspecting running binaries showed that wasn't the case."
- **Our assessment**: A small but concrete example of a mismatch between the team's mental model of their own binary's dynamic linking behavior and its actual runtime behavior — a reminder that dynamic-linker symbol resolution is worth verifying empirically ("inspecting running binaries") rather than reasoning about from ABI/versioning rules alone, since the two disagreed here.

### Claim 14: The post's stated top-level lesson is that building a high-quality population dataset mattered more than deep technical expertise in any individual subsystem (dynamic linking, DWARF unwind metadata, signal delivery, the ABI, or C++ exception internals)
- **Evidence**: The post's closing section explicitly ranks the investigation's techniques, stating the dataset-building step outranked the assembly-level analysis in importance.
- **Confidence**: settled (first-party retrospective judgment about which step mattered most, not an externally validated finding)
- **Quote**: "The most important step was not the clever assembly reading or deep knowledge of the details. It was building a high-quality data set. In the absence of this data set, we were mixing two distinct phenomena into one story and trying to reason our way out of the confusion."
- **Our assessment**: This is a retrospective, self-assessed ranking rather than an independently measured finding — it is the team's own judgment about their investigation, not something a third party validated. That said, it is consistent with the rest of the narrative: every subsequent correct diagnosis (Claims 7, 8, 9) followed directly from having the population dataset, whereas weeks of single-case deep-dives (Claim 3) had not produced a resolution.

## Concrete Artifacts

### The automated core-dump analysis pipeline (paraphrased description from the source; no code shown)
```
Source: "Core dump epidemiology" (OpenAI, Nathan Bronson)

Step 1 (failed approach): text search over application logs
  - Failed: stack-corruption crashes produce corrupted/missing logged stack traces
  - Could not construct a log query without both false positives and false negatives

Step 2 (turning point): ChatGPT-authored script, run in parallel over
  every production Rockset core dump from the previous year
  - Downloads a prefix of each core file
  - Extracts CPU registers
  - Filters known false positives using the logs
  - Automatically labels each crash as: return-to-null / misaligned-stack / other
```

### Upstreamed fix
```
Source: "Core dump epidemiology" (OpenAI, Nathan Bronson)
"We also upstreamed a self-contained reproducer and a fix to GNU libunwind, and
verified that the other unwinders don't have a similar issue."
Linked commit: https://github.com/libunwind/libunwind/commit/a9b9293b286c14b9ed19db501aa347b46edd8a28
```

### Post-Bug-#1 (bad host) process changes (paraphrased from the source)
```
Source: "Core dump epidemiology" (OpenAI, Nathan Bronson)
- Fatal signal handler enhanced to log register state (detect recurrence from
  logs alone, no core dump needed)
- Control plane changed so VMs are usually reused instead of recycled (makes
  bad-node detection easier)
- Runbooks (and team mental models) updated to include silent hardware
  corruption as a known failure mode
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claudecode-quality-postmortem.md` Claim 9 ("The bug was
    described as 'at the intersection of Claude Code's context management, the
    Anthropic API, and extended thinking' — cross-system intersection bugs
    defeat component-level testing"): this source's Bug #2 (Claim 9 above) is
    an independent, non-AI-harness example of the same general failure
    category — a bug at the intersection of the compiler's exception metadata,
    the dynamic linker's symbol resolution, the kernel's signal delivery, and
    an application's specific signal-handling code, which no single-subsystem
    test would have caught. The two sources corroborate that "intersection
    bugs" are a real, recurring category across both AI-harness engineering
    and traditional systems engineering, not an artifact unique to LLM-based
    products.
  - `blog-anthropic-claudecode-quality-postmortem.md` Claim 12 ("Three
    independent changes on different schedules created 'broad, inconsistent
    degradation' that was hard to distinguish from normal variation"): this
    source's Claim 1 (two unrelated, coincidentally-concurrent bugs conflated
    into one apparent mystery) is a strong structural parallel — in both
    sources, multiple independent causes overlapping in time produced a single
    confusing symptom that resisted diagnosis until the causes were separated.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about core-dump analysis, ABI-level debugging, or population-based fault
  diagnosis that this source disagrees with.

- **Extends**:
  - `blog-ghaw-fault-investigation.md` Claim 1 (CI Doctor: an agentic workflow
    achieving a 69% merge rate autonomously diagnosing and fixing CI failures):
    that source documents an AI agent doing the diagnosis end-to-end for a
    narrower, more constrained failure class (CI breakage). This source is the
    inverse case for AI's role: the AI-authored component (Claim 6) is scoped
    to data extraction and classification only, and the actual root-cause
    diagnosis (recognizing two crash populations, tracing the libunwind race)
    was done by the human engineering team using the dataset the script
    produced. Read together, the two sources suggest a boundary: AI can either
    autonomously diagnose narrow, well-characterized failure classes (CI
    Doctor), or it can be delegated the bounded, verifiable data-processing
    step that unblocks a human-led diagnosis of a genuinely novel, systems-level
    bug (this source) — the harder, more novel the failure mode, the more the
    delegated AI task narrows to "produce the dataset" rather than "find the
    bug."

- **Novel**:
  - The "doctor vs. epidemiologist" framing (Claim 2) for choosing between
    single-case deep debugging and population-level pattern analysis is new to
    the corpus — no existing source names this specific decision point or
    gives it this vocabulary.
  - The specific technical mechanism of Bug #2 (Claim 9) — an ABI red-zone /
    signal-delivery race in `_Ux86_64_setcontext` — and the Fermi-estimation
    validation step (Claim 10) are both novel, low-level systems-debugging
    content not present elsewhere in the corpus, which is otherwise weighted
    toward AI-harness- and product-level engineering practices rather than
    kernel/ABI-level debugging.
  - The narrowly-scoped description of delegating a bounded data-extraction-
    and-classification script to an AI system (Claim 6), as distinct from
    delegating the diagnosis itself, is a specific and novel data point on
    where practitioners draw the line between "AI writes the tool" and "AI
    does the reasoning" during a live production investigation.

## Guide Impact

- **Chapter 01 (Daily Workflows — "When NOT to Delegate" / task-size
  threshold)**: Claim 6 is a concrete, real-world illustration of correctly
  scoping AI delegation during an open-ended, high-stakes investigation: rather
  than asking the model to diagnose the crash (an ambiguous, unverifiable ask),
  the team delegated a bounded, mechanically verifiable data-processing task
  (parse core files, extract registers, classify, filter) and kept the
  actual root-cause reasoning in human hands once the dataset existed. Add
  this as a worked example of the "delegate with checkpoints" pattern applied
  to an investigation/debugging context, distinct from the coding-task examples
  the chapter currently uses — citing this source.

- **Chapter 03 (Verification — "Cross-system intersection bugs" section)**:
  This section currently draws its "intersection bug" example solely from the
  Claude Code quality postmortem (`blog-anthropic-claudecode-quality-postmortem.md`).
  Claim 9 of this source is a second, independent example of the same failure
  category from outside the AI-harness domain — a bug at the intersection of
  the compiler, the dynamic linker, and the kernel's signal-delivery ABI.
  Recommend citing this source alongside the existing one to establish that
  intersection bugs are a general systems-engineering hazard the guide's
  advice (test cross-subsystem interactions, not just components) applies
  to broadly, not only to LLM-harness code.

## Extraction Notes

- WebFetch and a direct `curl` fetch of the source URL both returned an HTTP
  403 / Cloudflare bot-challenge page rather than article content. The article
  was successfully retrieved as clean, verbatim plain text via the `r.jina.ai`
  reader proxy (`https://r.jina.ai/<source-url>`), which returned a 200 with
  the full markdown-converted article body. All quotes above were copied from
  that raw-text extraction.
- The source contains what appear to be two instances of scientific/exponent
  notation (in the Fermi-estimation paragraph, Claim 10) that did not survive
  the plain-text extraction cleanly — rendered as e.g. "$1 0^{- 10}$" — almost
  certainly originally "10⁻¹⁰" with different markup/rendering on the live
  page. Rather than quote this garbled text as if it were the source's exact
  wording, Claim 10's numeric detail is paraphrased and the Quote field is left
  as "no direct quote" per MINER.md §2a Step 5.
- The article is a single page with no linked sub-pages containing additional
  substantive content; the only outbound link followed was the upstreamed
  GNU libunwind fix commit (captured under Concrete Artifacts), which is a
  code diff, not further prose to extract.
- No paywall encountered once the reader-proxy route was used; the full
  article text was accessible.
- No contradiction with existing source notes was found, so no contradiction
  issue was filed per MINER.md §4a.
