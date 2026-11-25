---
source_url: https://cognition.com/blog/swe-2-1
source_type: blog-post
title: "Introducing SWE-2.1"
author: "The Cognition Team"
date_published: 2026-11-24
date_extracted: 2026-11-25
last_checked: 2026-11-25
status: current
confidence_overall: anecdotal
issue: "#4949"
---

# Introducing SWE-2.1 (Cognition)

> Cognition's vendor release post for SWE-2.1 (pure RL on Kimi K3): a sandbox-escape canary eval used during training, a log-linear test-time-scaling curve on ExploitGym out to 6 hours, rollout-length control for stable multi-day RL, and a dual-use safeguard split (SWE-2.1 vs. SWE-2.1 Cyber) — all with vendor-reported numbers only.

## Source Context

- **Type**: blog-post (first-party vendor model-release announcement, cognition.com, 2026-11-24). Text recovered from the raw page HTML; charts are rendered as repeated text and a few are ambiguous (see Extraction Notes).
- **Author credibility**: Cognition (makers of Devin / the SWE model line). Direct knowledge of their own training and harness, but no independent verification; all benchmark numbers are self-reported and the post is also a product launch (free through 12/8, discounted until 1/30).
- **Scope**: Benchmarks (FrontierCode 2.0, Terminal-Bench 4.1, ProgramBench, SWE-Atlas QA, SWE Marathon v1.2), cybersecurity evals (ExploitBench, ExploitGym, CWE-Bench v2), training-infrastructure security, safeguards, test-time scaling, training recipe, and the Ultrafast (Cerebras) variant. Does not describe the RL algorithm in detail, dataset sizes, or the canary eval's design beyond one paragraph.

## Extracted Claims

### Claim 1: SWE-2.1 is trained with pure RL on Kimi K3, and gains come from targeting general intelligence and long-horizon workflows
- **Evidence**: Vendor assertion plus benchmark table (all vendor-reported).
- **Confidence**: anecdotal
- **Quote**: "Like its predecessor, it is trained with pure reinforcement learning on Kimi K3."
- **Our assessment**: Consistent with the RL-on-open-base line in the SWE-1.7 note. Note the post names the base "Kimi K3" in prose but compares against "Kimi K3.1" in tables; the relationship is not explained. No training-compute or data details given.

### Claim 2: The training data was expanded to cover short- and long-horizon tasks across science, performance engineering and cybersecurity
- **Evidence**: Assertion only; no dataset sizes or task counts.
- **Confidence**: anecdotal
- **Quote**: "we expanded our tasks and environments across both short- and long-horizon workflows, spanning areas from science and performance engineering to cybersecurity."
- **Our assessment**: Plausible; the cyber gain (ExploitBench 36.1 → 80.0 vs SWE-2) is the clearest evidence it transferred. Cannot be separated from the base-model change.

### Claim 3: Controlling rollout length in post-training removed length oscillations that previously destabilized RL, enabling stable training on tasks from minutes to many hours
- **Evidence**: Assertion; held-out eval improvement "throughout many days of training" is stated but no curve is shown.
- **Confidence**: anecdotal
- **Quote**: "Previously, length oscillations often destabilized training dynamics. Reducing those oscillations let us train reliably on tasks ranging from a few minutes to many hours."
- **Our assessment**: Useful as a failure-mode datapoint for long-horizon RL (rollout-length instability). The mechanism is not disclosed; compare the "alternating length penalty" in SWE-1.7.

### Claim 4: A canary eval in which the model tries to escape its sandbox, wired to alert researchers, caught four real new sandbox vulnerabilities during training despite red-teaming
- **Evidence**: Vendor-reported count (four) and claim that researchers responded immediately each time. No details of vulnerabilities.
- **Confidence**: anecdotal
- **Quote**: "Even after extensive red-teaming, the model discovered new vulnerabilities in our sandbox four times during training."
- **Our assessment**: The most transferable item in the post: a standing escape-attempt eval with automatic alerting as continuous monitoring, rather than one-off red-teaming. Evidence is a self-report, but the pattern is cheap and concrete.

### Claim 5: Training a cyber-capable model needs additional safeguards: red-teaming the training setup (esp. sandboxes) and continuous safety monitoring
- **Evidence**: Description of measures; no audit.
- **Confidence**: anecdotal
- **Quote**: "We created a canary eval where the model tries to escape the sandbox. Upon success, our infrastructure alerts the researchers."
- **Our assessment**: Pairs with Claim 4. Sandbox integrity is treated as a training-time risk, not just a deployment one.

### Claim 6: SWE-2.1 reaches 80% on ExploitBench and 27.3% on ExploitGym, with large gains over SWE-2
- **Evidence**: Vendor table. ExploitBench: SWE-2.1 80.0, SWE-2 36.1, Kimi K3.1 74.7, Claude Opus 5.5 91, GPT-6.2 Sol 100. ExploitGym success: SWE-2.1 27.3, SWE-2 12.1, Kimi K3.1 20.7, Opus 5.5 34.5, Gemini 4 Neon 47.9; flag capture: SWE-2.1 44.8, SWE-2 18.1, Kimi K3.1 29.3. CWE-Bench v2 Public: SWE-2.1 65.8 vs SWE-2 54.0.
- **Confidence**: anecdotal
- **Quote**: "SWE-2.1 achieves 80% on ExploitBench and 27.3% flags captured via intended exploits on ExploitGym."
- **Our assessment**: Vendor-reported. Internal inconsistency: the prose calls 27.3% "flags captured via intended exploits", but the table lists 27.3 under "Success" and 44.8 under "Flag capture". SWE-2.1 trails Opus 5.5, GPT-6.2 Sol and Gemini 4 Neon on most cyber rows, so "frontier-leading" would be wrong; the gain is relative to SWE-2 and open models.

### Claim 7: ExploitGym solve rate rises log-linearly with rollout time out to 6 hours, with a steeper slope than the base model
- **Evidence**: Chart of flags captured (%) vs normalized rollout time (3m to 6h) for SWE-2.1, SWE-2, Kimi K3.1, DeepSeek V4.1 Flash 1017; no numeric values given in text.
- **Confidence**: anecdotal
- **Quote**: "performance improves log-linearly as the time horizon extends, meaning that the model continues to find exploits as it works for more hours."
- **Our assessment**: A rare published measurement of solve rate vs. wall-clock for unattended runs, but it is one domain (exploit development), one vendor harness, with a simulated clock. Do not generalize to ordinary coding. Log-linear implies diminishing returns per hour — budget accordingly.

### Claim 8: Speed-independent benchmarking uses a simulated clock charging 1s TTFT per call plus a fixed seconds-per-token plus tool time
- **Evidence**: Stated method; formula in the methodology notes.
- **Confidence**: emerging
- **Quote**: "we enforce time limits on a simulated clock that charges each model call 1 s of time-to-first-token plus a constant c seconds per output token (a fixed TPS), matching our production serving speeds"
- **Our assessment**: Sensible way to compare models on time budgets without conflating hardware/serving speed; the value of c is not published, so it is not reproducible.

### Claim 9: Inference speed determines how much a test-time-scaling model can finish under a deadline; SWE-2.1 Ultrafast (Cerebras) offers 10× speed
- **Evidence**: Speed demo chart: Ultrafast 600 tok/s, SWE-2 Flash 200 tok/s, SWE-2.1 60 tok/s.
- **Confidence**: anecdotal
- **Quote**: "Because SWE-2.1 continues to improve with more test-time compute, inference speed determines how much work it can finish under a tight deadline."
- **Our assessment**: Logical link to Claim 7, but no benchmark is shown for Ultrafast; "same model" quality is asserted. Marketing-adjacent.

### Claim 10: Cyber safeguards are narrow, and a more permissive variant (SWE-2.1 Cyber) is given to defenders via Devin Security
- **Evidence**: Description of deployment policy; no safeguard design or false-positive rates.
- **Confidence**: anecdotal
- **Quote**: "we are rolling out SWE-2.1 Cyber, a version of SWE-2.1 with more permissive safeguards, to Devin Security."
- **Our assessment**: A concrete dual-use pattern (tiered access by vetted use case). The efficacy of the safeguards is unevidenced.

### Claim 11: Cross-model comparisons use different harnesses and context budgets, so scores are not like-for-like
- **Evidence**: Methodology notes: closed models in the developer's preferred harness; open and SWE models in Devin CLI; ProgramBench for SWE models at 250k context with up to 3 compactions (1M total) vs mini-swe-agent with native context up to ~1M for others.
- **Confidence**: settled (as a disclosure; it is stated plainly)
- **Quote**: "SWE-2.1 and SWE-2 are run in our harness with a 250k-token context with up to 3 compactions (1M tokens total)."
- **Our assessment**: Good disclosure; it also means ProgramBench comparisons favor neither side clearly. Treat the headline table as vendor evidence, not independent. Where upstream scores exist they were reused ("We report upstream or self-reported scores if they're available.").

### Claim 12: ExploitBench and ExploitGym are scored with generous protocols (union of five runs; mitigations disabled; flags captured includes unintended exploits)
- **Evidence**: Methodology notes.
- **Confidence**: settled (disclosure)
- **Quote**: "“Flags captured” includes successful, real exploits unrelated to the intended vulnerability specified in the initial prompt."
- **Our assessment**: ExploitBench takes the union of flags over five runs with a 3-hour clock, so it is closer to pass@5 than pass@1; ExploitGym is pass@1 over 869 tasks, 6-hour timeout. These are not comparable to each other. This is why the 44.8 flag-capture figure exceeds the 27.3 success figure.

### Claim 13: SWE-2.1 on general coding benchmarks: big gains over SWE-2 but behind top closed models
- **Evidence**: Table: Terminal-Bench 4.1 50.0 (SWE-2 24.2; Opus 5.5 65.8); FrontierCode 2.0 41.3 (24.1; Opus 5.5 47.3); ProgramBench 44.0 (17.0; GPT-6.2 Sol 66.0); SWE-Atlas QA 71.0 (63.7; Opus 5.5 77.4); SWE Marathon v1.2 54.9 (32.5; Opus 5.5 73.1).
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Vendor-reported. Kimi K3.1 beats SWE-2.1 on Terminal-Bench 4.1 (59.7 vs 50.0), so the RL recipe did not dominate its open-weight peer on every benchmark. The FrontierCode cost chart is image-only in the scrape and not extracted.

## Concrete Artifacts

Simulated-clock formula (Cognition, Benchmark Methodology Notes, rendered as text in the page):

```
time in seconds = turns + c × tokens + tools
```
(1 s TTFT per model call, constant c seconds per output token, plus real tool time.)

Harness setup for ProgramBench (SWE-2.1 / SWE-2): 250k-token context, up to 3 compactions, 1M tokens total. ExploitBench: 5 runs per task, 3-hour simulated clock, union of flags. ExploitGym: pass@1, 869 tasks, 6-hour timeout, mitigations disabled, agent-as-a-judge for "success".

Training safeguards (paraphrased list from the post): red-team training setup especially sandboxes; continuous safety monitoring; sandbox-escape canary eval with researcher alerting.

## Cross-References

- **Corroborates**: `blog-cognition-swe17.md` Claim 8 (self-compaction enabling six-hour rollouts) — SWE-2.1's 250k-context-with-3-compactions harness and 6-hour ExploitGym window are consistent with that long-horizon approach; Claim 9 (alternating length penalty) — both address rollout-length control in RL.
- **Contradicts**: None found.
- **Extends**: `blog-cognition-swe17.md` Claim 14 (per-vendor harness choice, Devin CLI for non-vendor models) — same convention continued, now with a simulated clock. `blog-cognition-frontiercode-2-0.md` Claim 3 (headline FrontierCode 2.0 scores, Opus 5.5 at 45.5%) — this post gives Opus 5.5 at 47.3 and SWE-2.1 at 41.3 on the same benchmark; the difference in the Opus 5.5 figure (45.5 vs 47.3) is unexplained and may reflect harness/run differences. `blog-cognition-devin-security-swarm-launch.md` — SWE-2.1 Cyber is positioned as the model for Devin Security normal scans, with deep scans on other frontier cyber models.
- **Novel**: Sandbox-escape canary eval as continuous training-time monitoring (four real escapes); published log-linear solve-rate-vs-time curve out to 6 hours; the simulated-clock method for speed-independent benchmarking; a tiered dual-use model release.

## Guide Impact

- **Chapter 06**: Add the sandbox-escape canary eval with alerting as an example of continuous monitoring of agent sandboxes (vendor-reported, four detections). Add SWE-2.1 / SWE-2.1 Cyber as an example of tiered safeguards for dual-use capability.
- **Chapter 03**: Cite the methodology notes as an example of harness disclosure (and its limits: different harnesses, union-of-5 scoring, unpublished c). Caution against using the headline table as independent evidence.
- **Chapter 02**: Cite Claim 7 as one vendor measurement that, in exploit tasks, success keeps rising log-linearly for up to 6 hours, informing unattended-run budgets; note the domain limitation.
- **Chapter 01**: Optional footnote: SWE-2.1 trails Kimi K3.1 on Terminal-Bench 4.1 and closed frontier models on most rows, but is a cost/speed option (Ultrafast at 600 tok/s per the post's chart).

## Extraction Notes

- Fetched raw HTML and stripped tags; read the full article and methodology notes. No linked sub-pages followed (links are product/legal pages).
- Chart data was recovered from rendered text. The ExploitGym headline chart lists Muse Wonder at 2.3, matching the table's "Success" row (marked * for Muse Wonder Full). The ExploitBench Gemini 4 Neon cell is "—".
- Table layouts repeat in the scrape; figures above come from the HTML tables, and the prose/table discrepancy on 27.3% is noted in Claim 6.
- The speed-demo section contains lorem-ipsum placeholder text on the page; ignored.
- All numbers are vendor-reported.
