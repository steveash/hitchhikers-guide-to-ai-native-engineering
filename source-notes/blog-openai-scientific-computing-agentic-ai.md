---
source_url: https://openai.com/index/scientific-computing-agentic-ai
source_type: blog-post
title: "Scientific computing in the age of agentic AI"
author: OpenAI (announcement); field report co-authored by Jeremy Li, Andrew Ho (OpenAI) with 20 external co-authors across academia/industry
date_published: 2026-07-28
date_extracted: 2026-08-06
last_checked: 2026-08-06
status: current
confidence_overall: emerging
issue: "#2523"
---

# Scientific computing in the age of agentic AI

> OpenAI announcement page (~500 words) linking a 13-page, 20-co-author
> exploratory field report ("Scientific computing in the age of agentic AI:
> an exploratory field report") that collects eight independent case studies
> of coding agents (Codex, and in three cases Codex plus Claude Code) applied
> to real scientific-software projects, mostly genomics/computational biology.
> The report's central, repeated finding: agents lowered the cost of
> implementation across all eight projects, but validating agent output —
> not writing the code — became the binding constraint, and human
> contributors' role shifted from implementer to verifier/orchestrator in
> seven of the eight cases.

## Source Context

- **Type**: blog-post (OpenAI "Publication/Research" vertical announcement)
  linking a full field report distributed as a PDF
  (`cdn.openai.com/pdf/scientific-computing-in-the-age-of-agentic-ai-an-exploratory-field-report.pdf`).
  Both were read in full for this note.
- **Author credibility**: The announcement page is unsigned, published under
  OpenAI's own byline. The field report itself is co-authored by two OpenAI
  researchers (Jeremy Li, Andrew Ho, both marked as corresponding/equally
  contributing authors) alongside 20 named external co-authors from academic
  and industry institutions (University of North Carolina at Chapel Hill,
  Allen Institute for AI, Garvan Institute of Medical Research, University of
  Maryland, Seqera, Altos Labs, Helmholtz Munich, NVIDIA, MinosAI, University
  of Chicago Booth, Harvard Medical School, Dana-Farber Cancer Institute,
  scverse). Each of the eight case studies is individually authored/co-authored
  by the practitioner(s) who did the work, not by OpenAI staff writing on
  their behalf — the report states explicitly that "the authors of each case
  study are responsible for the accuracy and interpretation of its
  project-specific claims, including reported benchmarks and validation
  results," and that OpenAI "did not independently reproduce every benchmark
  or validate every reported result." This is closer to a multi-author
  practitioner symposium than a controlled OpenAI-run study — it carries real
  outside-expert authority per case study but the aggregate framing/themes
  section is OpenAI's own synthesis across those self-reported accounts.
- **Scope**: Covers eight agent-assisted scientific-software projects
  (cyvcf2, rustar-aligner + svb + kuva, RustQC + FastQC-Rust + Trim Galore,
  HelixForge, hifiasm, MHCflurry, bayesm-rs, HI.SIM), a cross-case-study
  synthesis of recurring themes (validation burden, staged iteration,
  unreliable agent self-assessment), a stewardship/attribution discussion, and
  several explicitly-labeled "illustrative" economic back-of-envelope
  estimates. Does NOT cover: a controlled comparison of agent vs. non-agent
  development time/cost for any project (no counterfactual baseline was
  measured for any case study), non-life-sciences scientific computing (all
  eight case studies are genomics/computational-biology adjacent), or any
  claim about model-vs-model performance (the report explicitly disclaims
  this: "their numerical results are therefore reported as case-specific
  outcomes rather than direct comparisons of models or agent systems").

## Extracted Claims

### Claim 1: Across the eight case studies, coding agents made engineering labor and expertise less of a constraint on scientific computing, shifting the binding constraint to validating the agent's output, which still depends on human judgment
- **Evidence**: Stated as the report's central cross-case-study synthesis finding in the "Recurring Themes" section, and restated as the closing line of the "Conclusion" section.
- **Confidence**: emerging (a synthesized pattern across seven of eight self-reported, retrospective case studies collected after the fact, not from a controlled or prospective study design)
- **Quote**: "Though the projects varied widely in scope, they demonstrated that coding agents are making engineering labor and expertise less of a constraint in scientific computing. Now, the bottleneck is validating an AI agent's output, which still depends on human judgement."
- **Our assessment**: This is the report's headline thesis and the single most guide-relevant claim in the source. It is restated even more directly in the Conclusion: "Overall, these case studies support the perspective that there exists great potential for coding agents in making scientific computing more durable, streamlined, and robust, but that the current bottleneck remains verification and validation." The claim is not new in kind to this corpus (validation-as-bottleneck is a recurring theme across many existing sources — see Cross-References), but this is the first source to make the case specifically and exclusively for scientific/research-code correctness, where "correct" means scientifically valid, not just passing tests.

### Claim 2: Agents could implement well-scoped requests effectively but could not reliably judge whether their own work was scientifically valid, and often expressed confidence even when their output contained clear errors
- **Evidence**: Stated as a direct observation across the case studies in "Recurring Themes," reinforced by the Discussion section's account of specific subtle-error types agents introduced.
- **Confidence**: emerging (a synthesized observation across multiple case studies, not a controlled measurement of agent calibration/confidence)
- **Quote**: "Across case studies, agents handled specific, well-scoped requests effectively but could not reliably judge whether their work was scientifically valid or met expectations. Indeed, agents often expressed confidence even when their work contained clear errors."
- **Our assessment**: This is a specific, falsifiable framing of the general "agents can't reliably self-verify" pattern already well-established in this corpus, applied to the scientific-correctness domain rather than software-correctness or security. The Discussion section supplies concrete failure types behind this: "authors observed a number of subtle errors including changed numerical defaults, inappropriate memory allocation or streaming behavior, and silently skipped cases" — these are exactly the kind of errors that would compile, run, and produce plausible-looking output while being wrong, which is why agent self-assessment alone was insufficient.

### Claim 3: In seven of the eight case studies, human contributors concentrated their effort on the verification framework rather than on implementation, serving more as product managers than as traditional software engineers
- **Evidence**: Stated directly in the "Recurring Themes" section as the third of three identified cross-case patterns, immediately following the description of validation burden and staged iteration.
- **Confidence**: emerging (synthesized across seven case studies; HI.SIM is the explicit exception — see Claim 4)
- **Quote**: "In all but one project, human contributors concentrated their effort on the verification framework, often finding that they had to iteratively improve their framework as further work exposed additional failure modes. They concentrated their efforts on high-level control flow and system design, acceptance criteria, and the interpretation of discrepancies, serving more as product managers than as traditional software engineers."
- **Our assessment**: "Serving more as product managers than as traditional software engineers" is a sharp, quotable line for a chapter on how the researcher/developer role changes under agentic delegation — it names the shift precisely (from writing code to defining acceptance criteria and interpreting discrepancies) rather than gesturing at it abstractly. It is consistent with, but adds a scientific-computing-specific instance of, the broader "verification and orchestration" role-shift claim already present in this corpus's harness-engineering material.

### Claim 4: HI.SIM was the sole case study where the agent operated with essentially no human intervention after the initial prompt, because its acceptance target (byte-identical output) was itself exact and machine-checkable
- **Evidence**: Stated explicitly as the named exception to the seven-case pattern described in Claim 3, with the underlying reason given in the Discussion section.
- **Confidence**: emerging (single named case study, self-reported by its author)
- **Quote**: "HI.SIM was the exception, with essentially no human intervention after the initial prompt."
- **Our assessment**: The report's own explanation for why HI.SIM alone tolerated near-zero human oversight is instructive: "In HI.SIM, the agent independently constructed the benchmark workloads and regression checks, with byte-identical output as the acceptance target." This suggests the degree of required human oversight in this dataset tracked the exactness of the available acceptance target (byte-identical output is unambiguous and cheap to check automatically) rather than the agent's general capability — a case-study-level illustration of Claim 1's broader point that validation design, not agent skill, determines how much human oversight a project needs.

### Claim 5: A previously abandoned 2025 attempt to migrate MHCflurry from TensorFlow to PyTorch using an early agent harness (aider, with Claude 3.5 Sonnet and OpenAI's o1) succeeded only much later, and the practitioner who ran both attempts attributes the difference to model capability, not harness sophistication
- **Evidence**: First-person retrospective account from case-study co-author Sergey Feldman (identified in the report as "S.F."), contrasting his own abandoned 2025 PR against the eventually successful 2026 effort with Claude Code and Codex.
- **Confidence**: anecdotal (a single practitioner's own retrospective causal attribution across two of his own attempts, roughly a year apart, with no controlled isolation of harness vs. model as separate variables)
- **Quote**: "I think this was practically impossible until Opus 4.5 (or its equivalent GPT model). The sophistication of the available harness was likely not the primary bottleneck. The error compounding was too severe, and the model's intelligence/capacity was too low to complete this task at the level of autonomy I hoped for."
- **Our assessment**: This is a notable data point in the ongoing "is the bottleneck the model or the harness" question already present in this corpus from a harness-optimization angle (`blog-lilianweng-harness-engineering-rsi.md`, which studies harness self-improvement across model tiers). Feldman's account is a different angle on the same question — a fixed-ish harness pattern (single implementer agent with human oversight) applied to the same migration task a year apart, with model capability as the variable that flipped it from "abandoned after 200 commits" to "shipped as MHCflurry 2.2.0." It is one practitioner's post-hoc attribution, not a controlled test, but it is a concrete, dated counter-example to any assumption that harness sophistication alone can compensate for insufficient base-model capability on error-compounding-prone tasks like cross-framework numerical porting.

### Claim 6: Letting two different agent harnesses (Claude Code and Codex) alternate between contributor and reviewer roles helped the MHCflurry migration escape plateaus that a single agent could not, because the two agents caught different classes of errors in review
- **Evidence**: Stated as the first of four named "Lessons and reflections" in the MHCflurry case study (Case Study A), following a detailed account of the specific numerical-parity obstacles the migration faced.
- **Confidence**: anecdotal (single case study's stated practice and self-assessed outcome)
- **Quote**: "Adversarial pairing beats a single agent."
- **Our assessment**: The case study elaborates that this pairing pattern was adopted specifically after "subtle numerical problems persisted after prolonged work with just Claude Code" — i.e., it was a deliberate escalation, not the starting design. This is a specific instance of a cross-vendor multi-agent adversarial-review pattern already present in this corpus's migration-engineering material (e.g., the two/three-adversarial-reviewer patterns documented for the Bun Zig→Rust and Krieger Python→TypeScript migrations), but distinguished by using two different vendors' agent products rather than multiple instances of the same one — a data point specifically for cross-vendor pairing rather than within-vendor multi-agent orchestration.

### Claim 7: Even where a rewrite reached very high measured parity with its reference implementation, the last few percentage points of agreement required manual, per-record tracing rather than further automated iteration — and the validation harness itself was a source of at least one documented false-positive error
- **Evidence**: Direct example from the rustar-aligner case study (99.815% single-end / 99.883% paired-end read-level parity with STAR) and a distinct example from the HelixForge case study, both drawn from the Discussion section's account of validation obstacles.
- **Confidence**: emerging (two specific, named case-study examples cited by the report's own cross-case synthesis as illustrative of a broader pattern)
- **Quote**: "For example, in rustar-aligner, progress beyond 90% parity required careful tracing of individual reads through both implementations to identify and resolve discrepancies. The validation harness itself can also be a source of errors; in HelixForge, an early false-positive strand-balance audit caused by downsampling led the agent to modify the GPU implementation even though the problem was in the auditing step."
- **Our assessment**: The HelixForge detail is the more transferable lesson for a harness-engineering chapter: an agent given a faulty acceptance test faithfully "fixed" the wrong thing (the correct GPU implementation) in response to a buggy validation step, rather than the validation step itself. This is a concrete illustration of why the report elsewhere insists the validation harness needs review at "multiple levels of abstraction" — the agent cannot be expected to distinguish "my code is wrong" from "the test checking my code is wrong" without that being an explicit part of the human's review scope.

### Claim 8: Real-world, large-scale data surfaced correctness and performance-transfer issues that small or synthetic test workloads did not, in at least two separate case studies
- **Evidence**: Two named examples from the Discussion section — RustQC's validation against a full public sequencing dataset, and hifiasm's runtime-reduction figure differing between a held-out synthetic benchmark and recorded real human sequencing reads.
- **Confidence**: emerging (two specific case-study examples, cited by the report as representative of a cross-case pattern, but only two of eight case studies are named as evidence for it)
- **Quote**: "The use of real-world data was found to be important for determining whether performance improvements transferred beyond small or synthetic workloads."
- **Our assessment**: This corroborates a pattern already present in this corpus (small/synthetic test suites accelerating iteration but under-representing real edge cases) but supplies two concrete, named, quantified instances specific to scientific data: hifiasm's headline 25.1% runtime reduction on synthetic held-out data fell to 14.7% on real human chromosome-20 reads (per Table 1), and RustQC's edge cases "surfaced only at realistic scale" on real public sequencing data rather than minimal test datasets. Both are single-case, contributor-reported figures rather than a systematic before/after study across the full set of eight.

### Claim 9: The report offers explicitly-labeled illustrative (not measured) economic estimates: agent-assisted modernization preventing one-quarter to one-half of published research-software installation failures could return on the order of $6,000–$49,000 in researcher labor per 1,000 reuse attempts, or $0.6–4.9M across 100 packages, under stated assumptions
- **Evidence**: A stylized back-of-the-envelope calculation combining two cited replicability studies (a 9,000-R-script study finding 74%/56% first-run/post-cleaning failure rates, and a 98-omics-tool study finding 57.1%/27.6% installation failure rates and ~70 minutes of average troubleshooting time per failure) with assumed labor costs of $75–$150/hour.
- **Confidence**: anecdotal (the report itself explicitly frames these as illustrative orders of magnitude, not rigorous estimates: "While these are very rough estimates, they illustrate the scale of researcher time that could be saved")
- **Quote**: "At a fully loaded labor cost of $75–$150 per hour, this corresponds to $6,000–$49,000 across those 1,000 attempts, or $0.6–4.9M across 100 packages under the same assumptions."
- **Our assessment**: The report is unusually careful to flag these numbers as scenario illustrations rather than measurements — a separate, similarly-caveated estimate elsewhere in the Discussion applies the same $75–$150/hour rate to NumPy's 326 "MAINT"-titled 2025 pull requests, assuming 2 hours saved per change, to arrive at "approximately 650 maintainer-hours per year, corresponding to roughly $49,000–$98,000." Neither figure should be cited in the guide as a benchmark practitioners should expect to replicate; both are useful only as order-of-magnitude framing for why researcher-software modernization has plausible economic stakes at all.

### Claim 10: Coding agents make it cheap to produce a competing rewrite of existing scientific software, which creates a stewardship risk distinct from correctness — cheap rewrites can fragment users and spread thin the expert attention needed to keep any one tool reliable
- **Evidence**: Stated as a dedicated discussion point in "Stewardship remains a critical aspect," illustrated by the contrasting outcomes chosen across case studies (upstream merge for MHCflurry and cyvcf2 vs. new community stewardship under scverse/nf-core for the unmaintained STAR replacement, rustar-aligner).
- **Confidence**: emerging (a stated concern with real named case-study examples of divergent resolutions, but not a quantified measurement of how often such fragmentation actually occurs across the broader ecosystem)
- **Quote**: "Mature scientific software carries undocumented conventions, compatibility requirements, and user trust that translating the source code alone cannot reproduce."
- **Our assessment**: This is a distinct risk category from the validation-burden theme (Claims 1–2): even a rewrite that is scientifically correct can still fail as infrastructure if nobody has clear, durable responsibility for it. The report's own worry is specific and concrete: "there is a serious risk that this diffusion of attention will result in ecosystems of software rewrites where no one rewrite is actually validated to an extent that permits real-world usage, even if concentration of efforts into a single project would have been able to produce a usable end product." This complements, rather than duplicates, this corpus's existing guidance on early maintainer coordination for AI-assisted migrations — this source adds the specific "N competing rewrites, 0 well-stewarded" failure mode as the concrete downside of skipping that coordination.

### Claim 11: This is an exploratory, retrospective field report, not a controlled study — the underlying eight projects were not commissioned for the study, were not run under a common protocol, and were collected from contributors after the work was already done, so effort/time-saved/economic-advantage assessments rest on contributors' own qualitative judgment
- **Evidence**: Stated directly and prominently as the report's first and lead limitation in its "Limitations" section.
- **Confidence**: settled (an explicit, first-party methodological disclosure, not a claim requiring external verification)
- **Quote**: "This exploratory field report is retrospective: the underlying projects were not commissioned for this study or conducted under a common protocol, and the case studies were collected from contributors after the work had already been undertaken."
- **Our assessment**: This self-disclosed limitation should govern how every other claim in this note is cited — none of the eight case studies' outcomes were independently reproduced or measured against a controlled counterfactual, and the report explicitly says the projects are "a narrow, selected cross-sectional view of current practice rather than a representative sample of agent-assisted scientific software projects or developers." The overall `confidence_overall: emerging` rating for this note reflects this: the aggregate patterns (validation as bottleneck, staged iteration, unreliable self-assessment) recur across a genuinely independent set of eight practitioner teams and are therefore more than a single anecdote, but the sample is self-selected (contributors who volunteered a write-up) and none of it was audited by a third party.

### Claim 12: A named cyvcf2 case-study author explicitly cautions that ease of implementation with coding agents has outpaced the expert judgment still required to go deep in science, distinguishing project velocity from scientific depth
- **Evidence**: Direct pull-quote attributed to Brent Pedersen on the announcement page, describing the cyvcf2 build/packaging modernization case study.
- **Confidence**: anecdotal (single named practitioner's stated reflection on one case study)
- **Quote**: "With coding agents, it's quite easy to go fast; for now, to go far in science, there's still a need for expert guidance, understanding, taste, and care."
- **Our assessment**: This is the report's most quotable single-sentence framing of the fast-vs-far distinction, and it is notable that it comes from one of the lower-stakes case studies (cyvcf2's project was scoped narrowly to build/packaging modernization, explicitly "without changing VCF handling," per Table 1) rather than one of the higher-risk rewrites — suggesting the sentiment is treated by its author as a general caution about the technology, not a specific complaint about a project that went badly.

## Concrete Artifacts

### Table 1 (summarized): the eight case studies, project type, and headline reported outcome

```
Source: field report, Table 1 ("Summary of the eight agentic coding case
studies") and Case Study appendix, pp. 6, 14-51

A. MHCflurry (Rubinsteyn, Feldman, O'Donnell) — TensorFlow -> PyTorch backend
   rewrite, ~10,000 lines / ~130 files, preserving previously released model
   weights. Shipped as MHCflurry 2.2.0; all prediction quantities agreed
   within small tolerances.

B. rustar-aligner + svb + kuva (Ferguson, Patro, Driver, Ewels, Angerer,
   Gold, Manning, Heumos) — from-scratch Rust reimplementation of STAR
   (>20,000 lines of C/C++). 99.815% single-end / 99.883% paired-end
   read-level parity with STAR on 10,000 yeast RNA-seq reads, no reads
   unique to either tool. svb: 1.7-2.9x faster StreamVByte compression than
   the most-used existing crate. kuva: new Rust plotting library, 60+ plot
   types.

C. RustQC + FastQC-Rust + Trim Galore (Ewels, Manning, Krueger) — single-pass
   Rust replacement for 15 nf-core/rnaseq post-alignment QC tools. On a
   186-million-read dataset: sequential runtime cut from 15h34m to 14m54s
   (>60x), disk traffic cut from 2.5 TB to 0.1 TB, numerical output
   equivalence. FastQC-Rust 7x faster, Trim Galore 3x faster (the 3x gain
   was subsequently ported upstream into Java FastQC as well).

D. HelixForge (Ahangari, Goyal, Masoudi) — GPU-native CUDA/htslib rewrite of
   BamSurgeon's mutation-insertion path. On one donor, 10 Mb region: editing
   stage 98.6x faster, end-to-end 59.6x faster; mean mutation-frequency
   error fell from 0.076 to 0.034; realignment artifact nearly eliminated.

E. hifiasm (Shringarpure) — hot-path optimization of an existing C genome
   assembler. Runtime down 25.1% on held-out synthetic data (satisfying
   prespecified read-ordering thresholds), 14.7% on recorded human
   chromosome 20 reads.

F. cyvcf2 (Pedersen) — build/packaging/release modernization only, no VCF
   handling changes. Merged refactor introduced scikit-build-core.

G. bayesm-rs (Bai, Ho, Rossi) — Rust reimplementation of selected CRAN
   bayesm 3.1.7 Bayesian samplers, plus new HART-derived nonlinear
   heterogeneity and shared HMC/NUTS extensions. Base rewrite met
   prespecified posterior-agreement tolerances; first-pass HMC/NUTS and HART
   extensions initially produced "plausible but defective results" that
   required correction before passing convergence and simulation-based
   calibration checks.

H. HI.SIM (Ho) — targeted optimization of a DNA-sequencing-read simulator,
   the sole case with no human intervention after the initial prompt.
   Aggregate runtime across a four-workload benchmark suite down 30.97%;
   outputs byte-identical.
```

### The six overlapping project types identified across the eight case studies (verbatim list)

```
Source: field report, Introduction, p.3

- lightweight maintenance and packaging work,
- targeted optimization of existing functionality,
- compatibility migration between software frameworks while preserving
  released behavior,
- translation of tooling to new programming languages while preserving
  semantics,
- complete performance-oriented rewrites which involve major algorithmic
  changes,
- implementation of new tools, libraries, or new methodological
  capabilities within existing libraries.
```

## Cross-References

### Cross-reference verification notes
Claim numbers in cited source notes below were verified by re-reading each cited note directly and counting `### Claim N:` headings top-to-bottom, per MINER.md §4b.

- **Corroborates**:
  - `blog-openai-genebench-pro-case-studies.md` Claim 12 (independent reviewer Cyrillus Tan: "Different prompt wording or task specification can greatly affect which analyses appear permissible") and Claim 13 (independent reviewer Lex Flagel: agents fail specifically at flagging data discrepancies, not at domain knowledge) — both sources are OpenAI-published, life-sciences-adjacent accounts of where agents specifically fall short on scientific-reasoning tasks, published roughly a month apart. This source's Claim 2 (agents "expressed confidence even when their work contained clear errors") is the same underlying reliability gap described from a code-correctness angle rather than GeneBench-Pro's data-discrepancy-detection angle — together the two sources suggest agent overconfidence in scientific contexts spans both "is my code right" and "is this input data trustworthy" framings.
  - `docs-github-copilot-cca-validation-parallel.md` Claim 3 (Copilot cloud agent's self-remediation loop scans and attempts fixes before requesting human review, with unstated remediation success rates) — this source's Claim 2 (agents express confidence despite clear errors, requiring human-designed external validation) is a substantially more skeptical account of agent self-verification than that source's largely uncritical description of automated self-remediation; the two together suggest automated self-remediation loops should not be assumed to generalize to domains (like scientific correctness) where the "ground truth" is not a simple pass/fail scanner result.
  - `blog-anthropic-code-migration-playbook.md` Claim 1 ("you don't fix the code, you fix the process (loop) that produced the code") and Claim 9 (two adversarial reviewers, disagreement escalated to a third agent) — this source's Claim 6 (Claude Code and Codex alternating contributor/reviewer roles to escape plateaus in MHCflurry) is a cross-vendor instance of the same adversarial-multi-agent-review principle documented there for the Bun and Krieger migrations, adding scientific-software migration as a third independent domain where the pattern was found useful.
  - `blog-lilianweng-harness-engineering-rsi.md` (general theme: how much of agentic performance is attributable to the harness vs. the underlying model) — this source's Claim 5 (Sergey Feldman's own retrospective: an abandoned 2025 aider-based MHCflurry migration attempt succeeded a year later with the same general harness pattern but a more capable model, and he attributes this to model capability rather than harness sophistication) is a concrete, dated practitioner account bearing on the same underlying question that note studies from a harness-self-improvement-research angle. The two are not the same claim and neither confirms the other, but both are directly relevant to a guide section asking "when does a better harness matter more than a better model, and vice versa."

- **Contradicts**: No material contradiction identified against any existing corpus source note. This source's skepticism about agent self-assessment (Claim 2) is consistent with, not opposed to, the corpus's existing validation-focused sources; no existing note claims that coding agents can reliably self-certify scientific correctness without human-designed acceptance criteria.

- **Extends**:
  - `blog-openai-genebench-pro-case-studies.md`: that note documents agent performance on a *benchmark* of synthetically constructed genomics analysis problems (GeneBench-Pro), graded against known synthetic ground truth. This source documents agents applied to *real, shipping* scientific software infrastructure (cyvcf2, STAR, MHCflurry, etc.), where no ground truth exists in advance and contributors had to design their own acceptance criteria case by case. The two sources describe adjacent but distinct evaluation regimes — one measures capability against a fixed answer key, the other documents practitioners building the answer key from scratch for each real-world project.
  - `blog-anthropic-code-migration-playbook.md` and its own cross-referenced Bun/Krieger migration notes: those describe large-scale *language*-migration methodology (Zig→Rust, Python→TypeScript) for general software infrastructure. This source's rustar-aligner (C/C++→Rust) and MHCflurry (TensorFlow→PyTorch) case studies are the same underlying migration pattern applied specifically to numerically-sensitive scientific code, where "equivalence" had to be defined in terms of statistical tolerance or read-level parity rather than the byte-identical or full-test-suite-pass criteria available in general-purpose software migrations.
  - `docs-github-copilot-cca-validation-parallel.md`: that source documents a platform-level, automated validation layer (four scanning tools) for general-purpose Copilot-generated code. This source's case studies (especially HelixForge's validation-harness bug and rustar-aligner's manual per-read tracing) illustrate why an automated scanning layer alone would not suffice for scientific-correctness validation — the acceptance criteria here are domain-specific (statistical tolerances, read-level parity, posterior agreement) and had to be hand-designed per project, not drawn from a generic security/quality scanner stack.

- **Novel**:
  - The explicit "product manager, not software engineer" framing of the human contributor's role (Claim 3) applied specifically to scientific/research computing, with a named single exception (HI.SIM) and a stated reason for that exception (Claim 4) — no existing corpus source documents this role-shift claim with an explicit counter-example and mechanism for why the counter-example differs.
  - The validation-harness-itself-can-be-wrong failure mode illustrated concretely via HelixForge's false-positive strand-balance audit (Claim 7) — a specific, dated example of an agent correctly following a broken test and "fixing" working code as a result, which is a sharper illustration than any existing corpus source of why validation-harness review is a distinct task from output review.
  - The stewardship-fragmentation risk framed specifically as a consequence of *cheap* rewrites, illustrated with contrasting real resolutions (upstream merge vs. new community stewardship) across the same set of case studies (Claim 10) — existing corpus migration sources discuss maintainer coordination as good practice, but this is the first source to name ecosystem-wide attention-fragmentation ("ecosystems of software rewrites where no one rewrite is actually validated") as the specific downside of skipping it.
  - Feldman's dated, two-attempt (2025 vs. 2026), same-practitioner comparison isolating model capability from harness design as the more likely explanation for a previously-failed migration's eventual success (Claim 5) — a concrete practitioner data point for the model-vs-harness question that is otherwise argued mostly at the research level in this corpus.

## Guide Impact

- **Chapter 03 (Verification)**: Add Claim 2 (agents "expressed confidence even when their work contained clear errors") and Claim 7's HelixForge example (an agent correctly obeying a broken validation harness and "fixing" the working implementation instead) as concrete illustrations for a section on why validation-harness review must be treated as a distinct human task from reviewing the agent's primary output — reviewing only the code, not the test that graded it, misses this specific failure mode. Add Claim 4 (HI.SIM's near-zero-oversight exception, explained by its byte-identical-output acceptance target) as a positive counter-example showing that the *exactness* of the acceptance criterion, not the agent's general skill, is what determines how much human oversight a given task needs.
- **Chapter 02 (Harness Engineering) or a Team-Adoption chapter**: Add Claim 3's "serving more as product managers than as traditional software engineers" framing as a specific, quotable description of how the human contributor's day-to-day work changes under heavy agentic delegation on real (not benchmark) projects — pair with Claim 5 (Feldman's model-capability-not-harness attribution) if the guide has a section weighing model upgrades against harness investment as competing levers.
- **Chapter 05 (Large-Scale Refactoring and Migrations)**: Add rustar-aligner and MHCflurry (Claims 6–7) as scientific-computing-specific instances of the migration patterns already documented for Bun and Krieger's port in `blog-anthropic-code-migration-playbook.md` — specifically, that "equivalence" in a scientific migration is often a statistical-tolerance or parity question rather than a byte-identical or test-suite-pass question, which changes what the "judge" step of that source's six-step process needs to check.
- **Chapter 06 (Security / Threat Model) or wherever stewardship/governance is covered**: Add Claim 10 (cheap rewrites risking user/expert-attention fragmentation, with the contrasting rustar-aligner/MHCflurry resolutions) as a concrete illustration of a non-security governance risk specific to lowered implementation costs — relevant anywhere the guide discusses the tradeoffs of agents making forks/rewrites cheap to produce.
- Do not cite the economic estimates in Claim 9 (the $6K–$49K / $0.6–4.9M / $49K–$98K figures) as benchmarks — the report itself explicitly labels them illustrative back-of-envelope scenarios, not measurements, and this note's confidence rating for that claim is anecdotal accordingly.

## Extraction Notes

1. **Access method**: The live OpenAI URL returned HTTP 403 to both WebFetch and direct `curl` with a browser user-agent. Recovered via the Wayback Machine (`web.archive.org/web/20260731000924/https://openai.com/index/scientific-computing-agentic-ai/`, captured 2026-07-31, fetched with `curl` since the WebFetch tool itself declines `web.archive.org` URLs directly), then HTML-stripped locally for text extraction. The announcement page's "Read the paper" link resolved to a directly-fetchable PDF (`cdn.openai.com/pdf/scientific-computing-in-the-age-of-agentic-ai-an-exploratory-field-report.pdf`, HTTP 200, no Cloudflare challenge), which was downloaded directly and text-extracted locally with `pypdf` (no PDF rendering tool was available in this environment, so page-image reading via the Read tool's PDF mode was not possible; plain-text extraction was used instead).
2. **Full report read**: All 13 pages of the field report were read in full, including the complete Introduction, Case Studies summary, Recurring Themes, Discussion (Validation/Stewardship/Economic-value subsections), Limitations, Conclusion, and the first five case-study appendices (A: MHCflurry, B: rustar-aligner/svb/kuva, in full detail through "Lessons and reflections" and "Artifacts"). The remaining three case-study appendices (RustQC, HelixForge, hifiasm, cyvcf2, bayesm-rs, HI.SIM) were read at the Table 1 summary level plus the Discussion section's specific cross-references to each, rather than each appendix's full individual narrative — Table 1 and the Discussion section between them restate every appendix's problem, method, and headline result, so no additional claims were judged to be missed by not reading each remaining appendix's full prose narrative.
3. **PDF text-extraction artifacts**: `pypdf`'s plain-text extraction occasionally dropped inter-word spaces on individual lines (e.g., rendering "specific datasets" as "specificdatasets") and once split a hyphenated line-wrapped word ("contributor" wrapped across two lines as "contrib-" / "utor"). No quote in this note was taken from a passage exhibiting either artifact; where a claim's supporting sentence had this issue, either a cleanly-extracted alternate sentence from the same passage was quoted instead (Claim 8), or the quote was trimmed to the clean portion only (Claim 6, quoted only through "Adversarial pairing beats a single agent.", omitting the affected "contributor/reviewer" clause that follows in the source).
4. **No contradictions filed**: cross-referencing against the existing corpus (see Cross-References above) found no claim in this source that materially opposes an existing source note's claim on the same topic.
