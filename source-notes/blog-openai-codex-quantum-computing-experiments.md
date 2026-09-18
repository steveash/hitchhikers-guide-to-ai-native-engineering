---
source_url: https://openai.com/index/codex-quantum-computing-experiments
source_type: blog-post
title: "How GPT‑5.6 Sol helps run quantum computing experiments"
author: OpenAI (case study co-authored with MIT EQuS group researchers)
date_published: 2026-09-08
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: emerging
issue: "#3532"
---

# How GPT‑5.6 Sol helps run quantum computing experiments (OpenAI × MIT EQuS)

> OpenAI's case-study blog post, backed by a co-authored technical paper
> from MIT's Engineering Quantum Systems group, documents GPT‑5.6 Sol
> (Ultra reasoning level) running inside Codex, connected via a simple
> in-house Jupyter MCP, autonomously executing 36 of 40 target calibration
> measurements on a never-before-measured six-qubit chip (researchers
> intervened on only 4), while explicitly documenting where it failed:
> noisy/ambiguous signals, one case of the agent wrongly declaring a bad
> fit acceptable, and a stated architectural limit — physical measurement
> is serial, so "agent swarms... cannot accelerate the process through
> parallel, brute-force exploration."

## Source Context

- **Type**: blog-post (OpenAI `openai.com/index/` "Applied AI" vertical,
  published September 8, 2026) linking out to a full technical case study
  PDF hosted at `cdn.openai.com/pdf/case-study-agentic-calibration-of-superconducting-qubits.pdf`
  (10 pages, titled "Case Study: Agentic Calibration of Superconducting
  Qubits," dated September 4, 2026). This note extracts claims from both
  documents — the blog post is a ~600-word summary/marketing framing of
  the same work described in much greater technical detail in the PDF.
- **Author credibility**: The PDF is co-authored by five named individuals:
  Beatriz Yankelevich, Jeffrey A. Grover, and William D. Oliver (MIT
  Research Laboratory of Electronics / EQuS — Engineering Quantum Systems
  Group), and Eva Zhang and JonLuca DeCaro (OpenAI). The "Contributions"
  section explicitly states: "MIT authors developed the agentic
  measurement infrastructure and performed the experiments. OAI authors
  provided advice on the agentic infrastructure and comments on the text."
  This is a materially stronger credibility structure than OpenAI's
  single-practitioner-testimonial case studies (contrast
  `blog-openai-gpt5-immunology-mystery.md`, built entirely around one
  self-reported account with no named co-author and no technical paper):
  here the domain-expert authors are independently named, affiliated with
  a specific academic lab (MIT EQuS, home to William D. Oliver, a
  well-known superconducting-qubit researcher), and the paper includes
  citations to a body of prior work on LLM-assisted qubit experiments,
  including a direct competitor result (arXiv:2606.22376, "autonomous
  bring-up of a 112-Qubit superconducting quantum processor"), which the
  authors do not attempt to claim credit over. Still a vendor-published,
  non-peer-reviewed case study — OpenAI selected which chip, which
  measurements, and which failure examples to publish.
- **Scope**: Covers one specific, standard-benchmarking six-qubit chip
  (four fixed-frequency, two tunable qubits) at MIT's EQuS lab, the
  measurement workflow architecture, quantitative and qualitative results
  for both qubit types, and a discussion section on generalizing to novel
  multi-qubit experiments. Does NOT cover: performance on more complex,
  many-qubit or novel-physics experiments (explicitly flagged as future
  work); any comparison of cost or wall-clock time against a human-only
  baseline beyond a qualitative "researchers can characterize
  fixed-frequency qubits in about a day, tunable qubits in about a week";
  or any quantitative benchmark score (contrast the arXiv:2604.25884
  "QCal-Eval" benchmark the paper itself cites in its references but does
  not report scores from).

## Extracted Claims

### Claim 1: GPT‑5.6 Sol, at "Ultra" reasoning level, run as a general-purpose agent through the Codex app with no specialized harness beyond a simple in-house Jupyter MCP, autonomously discovered all six resonators and appropriate initial readout powers on a never-before-calibrated six-qubit chip
- **Evidence**: Direct technical description in the case study PDF of the agent architecture and the first measurement stage (resonator spectroscopy), plus an embedded Codex chain-of-thought excerpt identifying the six resonator frequencies.
- **Confidence**: emerging (single chip, single research group, vendor/co-author-published; the underlying physics measurements themselves are standard and independently checkable in principle, but the "no specialized harness" framing is a specific infrastructure claim not independently verified)
- **Quote**: "The agent ran through the Codex app with no specialized harness beyond a simple EQuS in-house Jupyter MCP. It had access to live measurement parameters, programs, plots, raw data, logs, and the measurement database." / Codex quote: "... [these measurements] ... isolate six regularly spaced RF-stable candidates at approximately 7.2920, 7.3770, 7.4715, 7.5585, 7.6580, and 7.7520 GHz. That spacing is consistent with a six-resonator multiplexed design. I'll provisionally assign them in ascending frequency to r1-r6 ..."
- **Our assessment**: The "no specialized harness" claim is notable — this isn't a purpose-built lab-automation agent, but a general coding agent (Codex) with a thin MCP bridge to an existing Jupyter-based orchestration system. If accurate, it suggests the barrier to agentic physical-science work is lower than a bespoke-robotics framing would imply, and the actual engineering investment (per Claim 4 below) went into context/skill design rather than tooling.

### Claim 2: Across 40 target measurements on the four fixed-frequency qubits, the agent completed the calibration fully autonomously, with researchers intervening to improve only 4 — a concrete, checkable 90% unassisted-completion rate on that measurement set
- **Evidence**: Explicit stated count in the case study's results section, distinct from the more general qualitative claims elsewhere in the source.
- **Confidence**: emerging (a specific numerator/denominator from a single chip and single measurement campaign — the clearest quantitative result in the source, but n=1 chip and no stated criteria for what counted as an "intervention" vs. routine oversight)
- **Quote**: "The figure below shows the final results for the first qubit, obtained fully autonomously by the agent. Across the 40 target measurements for the four fixed-frequency qubits, researchers intervened to improve only four."
- **Our assessment**: This is the single most citable number in the source — far more specific than the blog post's vaguer "could often complete routine measurement workflows autonomously." It should be cited as "40 target measurements, 4 interventions, one six-qubit chip, four fixed-frequency qubits" rather than generalized to "quantum experiments" broadly, since the authors themselves separate this result from the much rockier tunable-qubit results (Claim 3).

### Claim 3: The agent had substantially more difficulty with the frequency-tunable qubits — weaker signal-to-noise farther from maximum frequency required significant researcher guidance, and in one documented instance the agent incorrectly concluded a poor-fit measurement was acceptable
- **Evidence**: A detailed, image-by-image walkthrough (Figure 6, panels A–G) of one tunable-qubit spectroscopy measurement, narrated by the authors, including an explicit statement that the agent's self-assessment was wrong at one step.
- **Confidence**: emerging (a single documented example, but presented candidly by the co-authors as a limitation rather than omitted, and the qubit design/signal explanation given for *why* it was harder is physically specific rather than hand-waved)
- **Quote**: "The agent (unprompted) analyzing each individual flux linecut to observe if a peak is present, or just noise. The agent (incorrectly) concludes that this measurement is acceptable." / "The user requests a finer final scan, and points out that, in the previous scan, the qubit spectrum likely fell out of the range at the greater flux regions." / "Although the agent initially located the qubit spectrum, it required significant instruction from the researcher to converge on a satisfactory result. The qubit signal here is faint over much of the flux range, and it takes an experienced eye to visually identify it."
- **Our assessment**: This is the strongest concrete failure-mode evidence in the source — not a hedge or disclaimer, but a step-by-step narrated example of the agent's self-assessment being wrong and requiring a human to notice a specific physical detail (spectrum falling out of the scanned flux range) the agent had missed. Directly useful as a "confident-but-wrong self-assessment on ambiguous physical/visual data" example, structurally similar to hallucination-under-ambiguity patterns already in the corpus (see Cross-References) but grounded in a hardware measurement rather than text generation.

### Claim 4: EQuS researchers spent "several months of iteration" to converge on the context design that made agentic calibration work — a combination of experimental setup details, chip designs, orchestration source code access, and per-measurement "skills" containing template code, prerequisite calibrations, parameter-selection tips, common physical failure modes, and example successful/failed plots
- **Evidence**: Direct description of the iteration process and the specific contents of a measurement skill.
- **Confidence**: emerging (a specific, detailed description of the context-engineering solution from the paper's co-authors, though the "several months" figure is not broken down further — e.g., how much of that time was skill-writing vs. infrastructure vs. model-generation upgrades)
- **Quote**: "The main challenge was identifying the context agents needed to work effectively. After several months of iteration, the researchers converged on a combination of the experimental setup details, chip designs, and measurement-specific skills, as well as access to the orchestration software's source code. The skill for a particular measurement includes information about the template code for execution and analysis, the crucial calibrations that must be completed before the measurement can be performed, tips to choose good measurement and analysis parameters, common physical reasons that the measurement might fail, characteristics of a successful or failed measurement/analysis, and example plots of both successful and failed measurements."
- **Our assessment**: This is a physical-science instance of a pattern already documented in the corpus for niche programming domains — a hand-built reference corpus compensating for thin training-data coverage of a specific, non-mainstream domain (see Cross-References → Extends). The specific structural elements named here (prerequisite calibrations, failure-mode enumeration, example plots of *both* success and failure) are a concrete, reusable checklist for building a domain skill file for any physical or experimental workflow, not just qubits.

### Claim 5: EQuS researchers separately state that "elaborating the potential physical failure modes in the measurement-specific skills has proven to be an important strategy to improve agentic measurement performance," and that observed agent performance has improved across model generations, "particularly with regards to visual analysis of measurements"
- **Evidence**: Direct statement in the "Implications" discussion section, distinct from and additional to the skill-design description in Claim 4.
- **Confidence**: anecdotal (a qualitative, non-quantified claim about what improved performance and why — no ablation or before/after comparison of skills-with-failure-modes vs. skills-without is presented)
- **Quote**: "EQuS researchers have observed that agent performance has improved as models become more advanced - particularly with regards to visual analysis of measurements. Furthermore, elaborating the potential physical failure modes in the measurement-specific skills has proven to be an important strategy to improve agentic measurement performance."
- **Our assessment**: Two separate levers are being credited here — model-generation improvement (out of the practitioner's control) and skill-authoring investment (in the practitioner's control). The guide-relevant one is the second: it's a specific, actionable claim ("enumerate failure modes, not just the happy path, in your skill files") rather than a vague "better skills help."

### Claim 6: The authors explicitly state that current agents lack "experimental intuition" — they take longer than experienced researchers even when they converge on the correct answer, and can pursue an incorrect line of investigation or miss an obvious physical reason a measurement failed
- **Evidence**: Direct, candid statement of a capability limitation in the discussion section.
- **Confidence**: settled (as a description of the authors' own stated assessment; presented plainly as a limitation rather than a hedge, consistent with the rest of the source's candor about failure modes)
- **Quote**: "Anecdotally, agents take longer than experienced researchers, even when they successfully converge on the correct measurement parameters. Often, agents appear to lack experimental 'intuition' - pursuing an incorrect line of investigation or not realizing an obvious physical reason why a measurement has failed."
- **Our assessment**: This directly tempers the impressive 90%-autonomous headline number (Claim 2): success does not imply speed or efficiency parity with a human expert, only that the agent eventually got there with less supervision. Worth pairing the two claims in any guide citation.

### Claim 7: Because physical measurements take minutes and must run serially, the rate-limiting step is physical acquisition itself, not reasoning — meaning agent swarms cannot accelerate qubit calibration through parallel, brute-force exploration the way they could a purely digital/software task
- **Evidence**: Explicit architectural/economic reasoning stated in the discussion section, contrasting this domain with tasks where parallel agent exploration is viable.
- **Confidence**: settled (a directly stated structural constraint of the physical domain, not a benchmarked claim — but the underlying logic, serial hardware access, is a straightforward physical fact about the experimental setup described earlier in the same paper)
- **Quote**: "Because measurements can take several minutes and run serially, physical acquisition itself is the rate-limiting step; agent swarms therefore cannot accelerate the process through parallel, brute-force exploration. Model fine-tuning in order to confer experimental intuition may be necessary to produce agents that pursue the most efficient path of exploration."
- **Our assessment**: This is a specific, named limit on a coordination pattern (agent swarms / parallel exploration) that the corpus otherwise documents as a general lever for accelerating agentic work (see Cross-References → Contrast). It's a useful boundary condition: agent-swarm parallelism helps when the constraint is reasoning/compute throughput, not when the constraint is a shared, serial physical resource. The paper's own proposed fix — fine-tuning for "experimental intuition" rather than more parallel agents — is speculative and not demonstrated in this source.

### Claim 8: Once the agent had calibrated the fixed-flux point for the tunable qubit, researchers handed off the remaining coherence measurements to an automated overnight loop that ran 200 measurements over 12 hours unattended, after which the agent manually investigated the points that had failed
- **Evidence**: Direct description of the automated-loop handoff at the end of the tunable-qubit section.
- **Confidence**: emerging (a specific run reported once, for one qubit/chip; not repeated or aggregated across multiple overnight runs in this source)
- **Quote**: "This loop steps over a flux range and takes the coherence measurements at each point, programmatically varying the measurement parameters and skipping over failed points. This was successful; the agent monitored the loop over the twelve hours it ran overnight (taking 200 measurements), and then the agent manually investigated a few points where the measurements failed."
- **Our assessment**: This is a concrete, numbered instance of the "unattended overnight agent run with morning triage" pattern already documented elsewhere in the corpus for software/business workflows (see Cross-References → Corroborates), here applied to physical hardware — the agent isn't just monitoring a batch job, it is actively driving lab instruments overnight and then doing its own failure triage the next step, before human review.

### Claim 9: Yankelevich (the MIT researcher) describes running multiple agents concurrently on different parts of her work — measurement, theory, and chip design — checking in from her phone, and now spends most of her time on higher-level interpretation, experiment design, and planning rather than step-by-step monitoring
- **Evidence**: Two direct first-person quotes in the blog post (not present in the PDF, which has no first-person practitioner quotes).
- **Confidence**: anecdotal (single practitioner's self-reported workflow and time allocation; no quantified before/after time breakdown)
- **Quote**: "I can have agents running measurements for many hours overnight or while I'm working in the cleanroom. I can check in from my phone, see what they've done, and steer them if something needs fixing or if I want to explore a different direction." / "I've built infrastructure to guide agents through several parts of my work—measurement, theory, and chip design—and now it's really starting to pay off. I can have multiple agents working on different problems at once, and I spend most of my time on higher-level work—interpreting results, devising experiments, planning next steps for the agents, reading, and writing."
- **Our assessment**: The "multiple agents on different problems, checked in from a phone" framing matches a general work-shifts-from-execution-to-supervision pattern already common across the corpus's case studies, but this is the first instance grounded in physical-lab work (cleanroom time as an explicit reason for wanting async, checkable-from-phone agent supervision) rather than a purely digital/office workflow.

### Claim 10: The paper's discussion section states that future superconducting-qubit calibration will remain harder than this benchmark case because qubit properties drift over time and diagnosing a failure may require recalibrating and revisiting measurements completed "dozens of steps earlier" — meaning experimental reasoning must handle a drifting system and hidden physical variables, not just a one-shot calibration
- **Evidence**: Explicit forward-looking limitation stated in the "Implications" section, distinct from the completed-chip results reported earlier.
- **Confidence**: settled (a stated, physically-grounded limitation of the demonstrated approach, framed by the authors as future work rather than a solved problem)
- **Quote**: "Such instabilities may mean that a measurement that worked one day fails the next. Diagnosing such failures may require recalibrating the qubit and revisiting measurements completed dozens of steps earlier. Thus, experimental reasoning must accommodate a drifting system, hidden physical variables, and ambiguous failures."
- **Our assessment**: This is the paper's own scoping statement for why the demonstrated six-qubit, single-session result should not be extrapolated to long-running, drifting, multi-qubit experimental programs — the authors are explicit that this remains unsolved, which should temper any guide citation of the 90%-autonomous headline number (Claim 2) as representative of harder, longer-running lab work.

### Claim 11: The chip benchmarked here is explicitly described by the authors as simple relative to novel multi-qubit experiments, and an experienced human researcher can characterize a set of fixed-frequency qubits in about one day and tunable qubits in about one week — the paper does not report a comparable wall-clock or cost figure for the agent's run
- **Evidence**: Direct scoping statement plus baseline human-timing figures in the discussion section; absence of a comparable agent-timing figure verified by reading the full paper.
- **Confidence**: settled (the scoping and human baseline are directly quoted; the absence of a matching agent-time figure is a verified absence, not an inference)
- **Quote**: "The chip presented here is a simple design meant to benchmark the fabrication process or noise environment of the experimental setup. The measurements demonstrated are standard in the field, and very simple compared to those that would be developed for a novel, multi-qubit experiment. An experienced researcher can characterize a set of fixed-frequency qubits in approximately one day, whereas characterizing a set of tunable qubits takes approximately one week."
- **Our assessment**: Without a reported agent wall-clock time, it's not possible to say from this source whether the agent was faster, slower, or comparable to the one-day/one-week human baseline — only that it required fewer touch-points (Claim 2) and could run unattended overnight (Claim 8). Any guide citation should avoid implying a demonstrated speed advantage, since the source itself doesn't make that comparison.

## Concrete Artifacts

### Measurement-skill contents (verbatim description, case study PDF §4)
```
Each measurement-specific skill given to the agent included:
- Template code for execution and analysis
- The crucial calibrations that must be completed before the
  measurement can be performed
- Tips to choose good measurement and analysis parameters
- Common physical reasons that the measurement might fail
- Characteristics of a successful or failed measurement/analysis
- Example plots of both successful and failed measurements

Source: cdn.openai.com/pdf/case-study-agentic-calibration-of-superconducting-qubits.pdf,
§4 "Agentic calibration results"
```

### Measurement workflow loop (Figure 3, case study PDF §3, paraphrased structure with direct labels)
```
1. Define measurement (USER/agent): measurement type, target qubit/
   resonator, swept/individual parameters
2. Generate measurement (ORCHESTRATOR): resolve instrument ports,
   compile pulse sequence, play pulses + acquire signal
3. Plot/Analyze (ORCHESTRATOR): plot normalized data, extract features,
   fit to model if one exists
4. Assess results (USER / ORCHESTRATOR): visually inspect plots,
   possibly iterate on analysis; orchestrator assesses fit goodness
   → Ambiguous results: iterate measurement parameters (loop to step 1)
   → Clear results: continue to next measurement
5. Update calibration settings (ORCHESTRATOR): persist extracted
   parameters

"EQuS's in-house orchestration software drives the process, while an
agent can assume the user's role."

Source: case study PDF, Figure 3 and accompanying text
```

### Codex chain-of-thought excerpts (case study PDF, Figure 4 captions)
```
"... [these measurements] ... isolate six regularly spaced RF-stable
candidates at approximately 7.2920, 7.3770, 7.4715, 7.5585, 7.6580, and
7.7520 GHz. That spacing is consistent with a six-resonator multiplexed
design. I'll provisionally assign them in ascending frequency to r1-r6 ..."

"All six resonances show real punchout behavior. The punchout branches
settle at usable powers between about -31 and -34 dBm."

"I'm taking one higher-stat narrow trace per resonator there to get
defensible centers and linewidths before the flux maps; this avoids
fitting κ from the low-SNR tail of the 2D sweep."

Source: case study PDF, Figure 4 captions ("Resonator calibration,
performed by an agent")
```

### Headline metrics (both documents)
```
Chip: 6 qubits (4 fixed-frequency, 2 tunable), never previously
      calibrated, standard EQuS fabrication-benchmark design
Agent: GPT-5.6 Sol, Ultra reasoning level, via Codex app
Harness: plain Codex app + simple in-house Jupyter MCP (no bespoke
      lab-automation framework)
Fixed-frequency qubit result: 40 target measurements, researcher
      intervention on 4 (90% unassisted completion on this subset)
Overnight automated loop: 200 measurements over 12 hours, unattended,
      followed by agent-led triage of failed points
Human baseline (not directly compared to agent time): ~1 day to
      characterize fixed-frequency qubits, ~1 week for tunable qubits

Sources: openai.com/index/codex-quantum-computing-experiments (Sept 8,
2026); case-study-agentic-calibration-of-superconducting-qubits.pdf
(Sept 4, 2026)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-rakuten-fable5-overnight-agents.md` (unattended,
    multi-hour agent runs going unattended without an early wrong
    assumption silently burning the whole run) — this source's Claim 8
    (200 measurements over 12 unattended overnight hours, with the agent
    itself triaging failures afterward) is a physical-hardware instance
    of the same "unattended overnight run + morning triage" shape,
    though for a different vendor (OpenAI/Codex vs. Anthropic/Fable 5)
    and a different failure-recovery mechanism (orchestrator skips
    failed points and the agent investigates after, vs. Fable 5's
    in-run self-verification).
  - `blog-anthropic-warp-self-improving-skills.md` (skill files as the
    unit of accumulated domain knowledge, iteratively improved) —
    corroborates the general pattern of investing in structured,
    example-rich skill files as the primary lever for improving agent
    performance in a specialized domain; this source's Claim 4/5 give a
    physical-science-specific version of what a good skill file contains
    (prerequisite calibrations, enumerated physical failure modes,
    example plots of both success and failure).
  - `blog-openai-gpt5-immunology-mystery.md` Claim 6 (a non-expert
    "wouldn't have been able to tell if the mechanistic insight...was
    important or not") — corroborated structurally by this source's
    Claim 3 and Claim 6: both are first-party accounts explicitly
    stating that domain-expert judgment remains necessary to catch
    agent errors (here, catching an incorrectly-accepted noisy fit;
    there, judging significance of a generated hypothesis).

- **Contradicts**: None filed as a formal contradiction issue. See
  "Contrast" entry below for a related-but-not-conflicting tension.

- **Extends**:
  - `guide/04-context-engineering.md` §"Pre-Session Corpus Loading for
    Low-Coverage Domains" (the Godogen/GDScript pattern: hand-written
    language spec + API docs + a "quirks database for engine behaviors
    you can't learn from docs alone," lazy-loaded via an isolated skill
    context) — this source is a physical-science generalization of the
    same underlying pattern: a low-training-data-coverage domain (a
    specific lab's orchestration software and chip designs, not a
    programming language) compensated for by a hand-built reference
    corpus. The "quirks database" concept maps directly onto this
    source's "common physical reasons that the measurement might fail"
    skill component. Recommend extending that guide section's bulleted
    list of applicable domains ("Domain-specific or niche language...
    Internal or proprietary API...") to explicitly include physical/
    experimental workflows with lab-specific tooling and instrumentation,
    citing this source.
  - `blog-cursor-agent-swarm-model-economics.md` (Cursor's
    planner/worker agent-swarm architecture for accelerating software
    tasks through parallel exploration) — this source's Claim 7 states a
    specific boundary condition on when that pattern applies: agent-swarm
    parallelism helps when the bottleneck is reasoning/compute
    throughput on a digital task, but not when the bottleneck is a
    shared, serial physical resource (here, one chip in one dilution
    refrigerator). This is a **contrast worth flagging explicitly in the
    guide**, not a contradiction — Cursor's swarm claims are about
    software tasks and don't claim to apply to serial hardware access; this
    source is the first in the corpus to state the boundary of swarm
    parallelism explicitly for a physical-world task.

- **Novel**: First corpus source describing a general-purpose coding
  agent (not a bespoke lab-automation system) driving live physical
  laboratory hardware end-to-end — choosing measurement parameters,
  operating instruments, interpreting returned signal data, and deciding
  what to measure next — with a named, quantified autonomous-completion
  rate (40 measurements, 4 interventions) and a candid, example-level
  account of where and how it failed (the tunable-qubit fit
  misjudgment). `blog-latentspace-lila-sciences-lab-data-center.md`
  previously covered automated wet-lab science as data-center-style
  infrastructure at a company built for that purpose (Lila Sciences);
  this source is the first covering a *general-purpose* coding agent
  (Codex/GPT‑5.6 Sol) doing physical-science measurement work in an
  existing academic lab's environment, with a co-authored technical
  paper rather than a podcast-style account as its primary evidentiary
  basis.

## Guide Impact

- **Chapter 04 (Context Engineering) → §"Pre-Session Corpus Loading for
  Low-Coverage Domains"**: Add this source as a second, physical-science
  example alongside the existing Godogen/GDScript case. The reusable
  checklist for a domain skill file (Claim 4's five-part structure:
  template code, prerequisite calibrations, parameter-selection tips,
  common failure modes, example plots of both success *and* failure) is
  concrete enough to state as a general template, not just a qubit-
  specific one. Pair with Claim 5's specific, actionable finding that
  enumerating failure modes (not just the happy path) measurably helped.

- **Chapter 03 (Verification)**: Claim 3 (the tunable-qubit fit the
  agent wrongly judged acceptable, corrected only because a researcher
  spotted a specific physical detail — the spectrum falling outside the
  scanned flux range — that the agent's own self-assessment missed) is a
  strong, narrated example for any section on agents overestimating
  their own output quality on ambiguous/visual data, and on why a human
  checkpoint before "accept and move on" matters even when the agent
  reports success. Should be paired with Claim 6 (agents "lack
  experimental intuition") for the caveat that this is a stated,
  acknowledged limitation, not a one-off.

- **Chapter 01 (Daily Workflows) or wherever agent-swarm/parallelism
  patterns are discussed**: Claim 7 (physical measurement is serial, so
  agent swarms cannot accelerate this domain the way they can a
  parallelizable software task) is a clean, quotable boundary condition
  to cite alongside `blog-cursor-agent-swarm-model-economics.md` —
  useful for a "when does agent-swarm parallelism actually help"
  discussion, since it's a case where the authors explicitly ruled the
  pattern out and explained why (shared serial resource, not a reasoning
  bottleneck).

- **Caution for any chapter citing the headline autonomy number**: Claim
  2's "40 measurements, 4 interventions" is real but narrowly scoped —
  one chip, one lab, the *simpler* half of the chip (fixed-frequency
  qubits only; the tunable-qubit results were substantially rockier per
  Claim 3), and with no comparable human-time baseline reported (Claim
  11). The paper's own Claim 10 states that longer-running, drifting,
  multi-qubit experiments remain explicitly unsolved. Any guide citation
  should carry these scope qualifiers rather than generalizing to
  "agents can run scientific experiments autonomously."

## Extraction Notes

- **Live URL blocked**: `https://openai.com/index/codex-quantum-computing-experiments`
  returned HTTP 403 with a Cloudflare bot-challenge (`cf-mitigated:
  challenge`) to both the WebFetch tool and a direct `curl` with browser
  headers, consistent with the access pattern already documented for
  `openai.com/index/` pages elsewhere in the corpus (e.g.
  `blog-openai-gpt56-sol-ultrafast-mode.md`, `blog-openai-gpt5-immunology-mystery.md`).
  The blog post was retrieved via an Internet Archive Wayback Machine
  snapshot dated 2026-09-10 (`web.archive.org/web/20260910060010/`),
  stripped of HTML/scripts/styles, and hand-extracted.
- **One substantive linked page followed, per MINER.md §1**: the blog
  post's "Read the technical case study" link resolves to
  `cdn.openai.com/pdf/case-study-agentic-calibration-of-superconducting-qubits.pdf`.
  This PDF was not archived by the Wayback Machine (404 on the archived
  URL) but was fetched successfully from the live CDN (HTTP 200, 6.2 MB,
  10 pages) and read in full using `pypdf` text extraction — it is the
  primary technical source for most of the claims in this note, and is
  substantially more detailed and more candid about failure modes than
  the blog post summarizing it. All 10 pages, including the references
  section, were read.
- **Related-articles module not followed**: the blog post's "Keep
  reading" widget links to "The builder's guide to GPT‑5.6" (already
  covered in `blog-openai-builders-guide-gpt56.md`), "How GPT-5 helped
  immunologist Derya Unutmaz solve a 3-year-old mystery" (already
  covered in `blog-openai-gpt5-immunology-mystery.md`), and "Using AI to
  help physicians diagnose rare genetic diseases affecting children"
  (not yet in the corpus, not covered by this note's scope — the
  Prospector may want to file this as a separate source submission if
  judged novel). Consistent with prior extraction notes' treatment, this
  is a generic related-articles widget, not further material about this
  specific source's topic.
- **Figures with only plots/axis data and no prose claims** (Figure 2,
  the qubit energy-level diagram; most of Figure 5's individual T1/T2/
  Rabi measurement panels) were reviewed but not extracted as claims —
  they are standard physics-measurement plots illustrating the
  calibration workflow, not novel assertions about AI capability. The
  specific coherence-time numbers visible in Figure 5 (e.g., T1 = 32.1
  us, T2 = 59.27 us) are reported as an example of the kind of physical
  parameter the agent extracted, not as claims requiring independent
  verification in their own right.
- No contradiction issue was filed. The tension noted under
  Cross-References → Extends (agent-swarm parallelism not applying to
  serial physical measurement) is a scope boundary on an existing
  pattern, not a conflicting claim about the same question — per
  MINER.md §4a's "when not to file" guidance (differ only in context,
  not a real contradiction).
