---
source_url: https://blog.jetbrains.com/ai/2026/10/how-netflix-made-ai-coding-agents-more-efficient/
source_type: blog-post
title: "How Netflix Made AI Coding Agents More Efficient with JetBrains IDE Intelligence"
author: Anastasia Kazakova (JetBrains), with quotes from Paul Bakker (Netflix) and Aleksey Stukalov (JetBrains)
date_published: 2026-10-15
date_extracted: 2026-10-16
last_checked: 2026-10-16
status: current
confidence_overall: emerging
issue: "#4157"
---

# How Netflix Made AI Coding Agents More Efficient with JetBrains IDE Intelligence

> Netflix wrapped JetBrains' headless code-intelligence engine (LSP) in a self-built warm daemon + CLI for Claude Code and Codex, and reports roughly 20–30% token/time efficiency gains over grep/unzip navigation on Java/Kotlin code, with correctness unchanged.

## Source Context

- **Type**: blog-post (vendor-hosted customer case study)
- **Author credibility**: Written by a JetBrains author about a JetBrains product; the Netflix side is a quoted Staff Software Engineer (Paul Bakker) from Netflix's Application Development Platform, GenAI Platform and Agentic SDLC teams. Vendor-published, so results are favorable-by-construction, though the method (paired A/B, outlier rule, correctness judge) is partly disclosed. Raw per-run data is not published.
- **Scope**: Java/Kotlin only; two codebases (an internal Spring Boot 4/Gradle service and the open-source DGS Framework); Claude Code (Opus 5, Sonnet 5) and Codex (GPT-5.6 Sol) at medium/high effort; July–August 2026. Does not cover Python/TS/Go (planned), cost in dollars, or any non-JetBrains code-intelligence baseline.

## Extracted Claims

### Claim 1: Agents navigate JVM code poorly across library (JAR) boundaries because libraries ship as JARs without source
- **Evidence**: Netflix engineer's stated observation; no measurements of the baseline failure rate are given.
- **Confidence**: anecdotal
- **Quote**: "JVM projects typically ship libraries as JAR files only, never as source. Agents have to unzip the JARs (guessing which ones matter), potentially decompile class files, then grep through that incomplete view."
- **Our assessment**: Plausible and a concrete, nameable failure mode. It is specific to compiled-dependency ecosystems; the article itself says mechanics differ for other languages.

### Claim 2: An LSP alone is not enough for an agent; it needs a daemon and CLI so stateless tool calls can reuse a warm index
- **Evidence**: Architecture description; Netflix built the daemon because JetBrains had not shipped one.
- **Confidence**: emerging
- **Quote**: "The LSP alone isn’t enough for a coding agent to use directly: It’s just a server speaking a protocol, with no easy way for an agent to call it and no built-in process management to reuse a running instance between calls."
- **Our assessment**: A reusable harness pattern: short-lived stateless tool call → CLI → long-lived daemon → per-project server. Mirrors the cold-start vs. warm-index issue seen in other indexing tools. No cold-start timing numbers beyond "multi-second".

### Claim 3: Cold-starting an LSP per call would cost multi-second overhead each time, so a session manager routes calls by project root to a warm server
- **Evidence**: Described design (session manager, stdio to warm server, GraalVM native executable for daemon/CLI).
- **Confidence**: emerging
- **Quote**: "Its session manager routes each call by project root to the matching server process, which holds that project’s index in memory."
- **Our assessment**: Sound engineering rationale; no measured latency is provided to size the benefit.

### Claim 4: With the tool available, agents were typically 20–30% more efficient (tokens + time), up to ~65% in the best case
- **Evidence**: Paired A/B benchmark; per-configuration table (strongest model/high effort: ~65% navigation, ~24% end-to-end; mid model/high: ~29%/~30%; mid/medium: ~24%/~22%; lighter/high: ~17%*/~21%). Efficiency is "the average of token and time savings".
- **Confidence**: emerging
- **Quote**: "typically 20–30% more efficient, and up to about 65% in the best case, depending on the specific model, agent, and task."
- **Our assessment**: Useful order of magnitude, but vendor-published, two codebases, no confidence intervals or run counts, and the efficiency metric blends tokens and time. Report as a range with attribution only. Contrast with the same vendor's skeptical token-saver tests (see Cross-References).

### Claim 5: Gains were largest for the strongest model at high effort, and differ noticeably between models
- **Evidence**: Table above; authors' explanation is that stronger models are more expensive and use indexes more effectively.
- **Confidence**: anecdotal
- **Quote**: "The stronger models, with higher effort, saw the largest gains."
- **Our assessment**: Interesting but the causal explanation is asserted, not tested; the headline ~65% rests on one configuration.

### Claim 6: Code-navigation tasks used fewer tokens in every configuration (roughly 15–60%), and correctness never dropped
- **Evidence**: Navigation tasks scored deterministically; correctness "held steady in most runs and improved in two".
- **Confidence**: emerging
- **Quote**: "Every model and effort level tested used fewer tokens with JetBrains IDE intelligence – no exceptions there – with savings ranging from roughly 15% to 60%."
- **Our assessment**: Plausible; token savings on symbol-lookup questions ("where is this interface used") are the intuitive best case.

### Claim 7: One tool/model combination showed no time benefit on navigation because it batches multiple searches into a single command; the authors say this is unrepresentative
- **Evidence**: The authors' own explanation; the table marks that configuration "Tokens only".
- **Confidence**: anecdotal
- **Quote**: "which is what produced the clear lack of time benefit for that combination, not a fair reflection of real-world use."
- **Our assessment**: Honest disclosure, but also a hint that agent-native batched grep can erase the time advantage; the "unrepresentative" framing is the authors' judgment. The ~17% figure for that row is tokens only.

### Claim 8: On end-to-end tasks (feature, refactor, removal), every combination was roughly 10–30% more efficient, largely from fewer tool calls
- **Evidence**: Expanded end-to-end suite; LLM-as-judge against a reference change set; time faster everywhere.
- **Confidence**: emerging
- **Quote**: "A lot of this is explained by requiring fewer tool calls to come to the same conclusions."
- **Our assessment**: Mechanism (fewer calls) is plausible but not broken down. LLM-as-judge correctness is a weak guard against subtle regressions.

### Claim 9: Methodology: same model/task/codebase with one variable, repeated runs, outliers excluded from both arms
- **Evidence**: Methodology section.
- **Confidence**: emerging
- **Quote**: "A task that crashed, hit a budget cap, or thrashed in either arm was excluded from both, so one blow-up couldn’t skew the comparison."
- **Our assessment**: Paired exclusion is reasonable, but excluding "thrashing" runs can hide a failure mode that unaided agents (or the tool) hit; exclusion counts are not reported.

### Claim 10: Netflix rejected an IDE-attached CLI (requires a running IDE) and the Eclipse LSP (did not work with its Gradle build)
- **Evidence**: Alternatives section; no details on the Eclipse failure.
- **Confidence**: anecdotal
- **Quote**: "But for Netflix’s build system (Gradle-based), it just didn’t work."
- **Our assessment**: Useful design constraint: headless environments (CI, distributed refactoring tooling, background agents) rule out IDE-bound approaches.

### Claim 11: LSP's cursor-position primitive is the wrong agent-facing abstraction; agents need symbol/diagnostic/test-relation level operations ("a code engine, not a virtual editor")
- **Evidence**: JetBrains opinion (Aleksey Stukalov); no experiment. Note JetBrains says it "continues experiments with the LSP+CLI approach".
- **Confidence**: anecdotal
- **Quote**: "Agents need a code engine, not a virtual editor."
- **Our assessment**: A design argument from a vendor with a product to sell; worth tracking as a hypothesis, not a finding.

## Concrete Artifacts

```
Architecture (paraphrased in our words from the article's "Architecture in detail" section; not a quote):
agent tool call (short-lived, stateless)
   -> CLI (shells out; Java, GraalVM native executable)
      -> daemon (long-lived; session manager routes by project root)
         -> per-project headless JetBrains LSP server (index in memory, stdio)
```

```
Benchmark matrix (from the article's "Evaluation environment" table):
Datasets: internal Spring Boot 4 + Gradle service; open-source DGS Framework (Kotlin/Java)
Tasks: small navigation questions; end-to-end feature/refactor/removal
Models: Claude Code Opus 5, Claude Code Sonnet 5, Codex GPT-5.6 Sol (medium/high effort)
Scoring: tokens + time; LLM-as-judge (end-to-end), deterministic (navigation)
```

```
Efficiency gain per configuration (navigation / end-to-end), source table:
Strongest model, high effort  ~65% / ~24%
Mid model, high effort        ~29% / ~30%
Mid model, medium effort      ~24% / ~22%
Lighter configuration, high   ~17%* / ~21%   (*tokens only)
```

## Cross-References

- **Corroborates**: `blog-anthropic-large-codebase-best-practices.md` Claim 10 (LSP integrations give IDE-level symbol navigation) and Claim 5 (LSP listed as a harness extension point); `docs-github-copilot-cli-cpp-whole-codebase-indexing.md` Claim 1 and Claim 3 (persistent symbol index reused across agent requests, with one-time indexing cost); `blog-jetbrains-rag-semantic-code-search.md` Claim 1 (grep is limited for agentic code search) and Claim 3 (JetBrains reusing its "Code Engine" for agents); `blog-sourcegraph-dorfman-file-picker-symbol-ranking.md` Claim 2 and Claim 6 (symbol-level lookup succeeds where filename/text matching fails).
- **Contradicts**: None filed. Mild tension with `blog-anthropic-large-codebase-best-practices.md` Claim 2/Claim 4, which present index-free agentic search as an advantage because there is no index to keep fresh; this source argues a deterministic index pays off (20–30%) for typed/compiled code. This is a conditioning variable (compiled-library boundaries, stack, vendor perspective), not a direct opposition, so no contradiction issue was opened.
- **Extends**: `docs-github-copilot-cli-cpp-whole-codebase-indexing.md` (same pattern of a warm language-server index for a CLI agent) with a measured A/B and the daemon/CLI wrapping design. Related methodology: `blog-jetbrains-rtk-token-savings-test.md` Claim 11 and Claim 12 (paired measurement, don't trust self-reported savings); this article is less rigorous than that series (no run counts, no p-values), so its numbers deserve more caution.
- **Novel**: Warm-daemon-routing-by-project-root pattern for making an LSP callable by stateless agent tool calls; the JAR-boundary failure mode; vendor-reported per-configuration efficiency ranges for deterministic code intelligence vs. grep; the argument that LSP's position primitive is the wrong agent abstraction.

## Guide Impact

- **Chapter 04 (context engineering)**: Add a short note, attributed and with ranges, that deterministic symbol-level code intelligence can reduce tokens/tool calls on navigation in compiled-dependency stacks (JetBrains/Netflix: ~15–60% navigation token savings, ~10–30% end-to-end). Present it as a counterpoint/conditioning case next to the index-free agentic-search position cited from `blog-anthropic-large-codebase-best-practices.md`.
- **Chapter 02 (harness engineering)**: Add the pattern "stateless tool call → CLI → warm daemon routed by project root" as a way to expose stateful engines (LSPs, indexers) to agents without per-call cold starts. Guide currently has no LSP/code-intelligence coverage.
- **Evidence caveat for any chapter**: label the figures vendor-published, Java/Kotlin only, July–August 2026 models, snapshot.

## Extraction Notes

- Fetched the full article HTML directly (WebFetch returned 403; curl with a browser user agent succeeded) and read it in full, including the results table. No linked sub-pages were followed; the article links no further primary material (no benchmark data or repo).
- All quotes were copied from the fetched text. The architecture diagram above is our paraphrase and is labeled as such.
- Compared against the overlapping notes named in the triage comments; claim numbers cited above were checked against those notes' headings.
- Derived registry is rebuilt from front-matter; `registry/sources.json` was not edited.
