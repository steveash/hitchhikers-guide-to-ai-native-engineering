---
source_url: https://openai.com/index/a-thousand-fewer-paths-to-root
source_type: blog-post
title: "A thousand fewer paths to root"
author: OpenAI (Cyber team; no individual byline)
date_published: 2026-11-04
date_extracted: 2026-11-27
last_checked: 2026-11-27
status: current
confidence_overall: emerging
issue: "#4983"
---

# A thousand fewer paths to root

> OpenAI's Linux-kernel Patch the Planet follow-up publishes a five-stage agent pipeline (scout → analyst → dynamic validation → exploitability → patch → human review) with per-stage API costs, funnel counts and design lessons, including that stronger models need lighter orchestration and that agents can "succeed" via the wrong vulnerability.

## Source Context

- **Type**: blog-post (first-party vendor research write-up, long-form)
- **Author credibility**: OpenAI's Cyber team, describing its own prototype run on an unreleased "upcoming cyber model". All numbers are self-reported and not independently reproducible (the model, harness and exploits are not public; exploit-technique details are deliberately withheld). The post says its goal is to help defenders and that it reports costs "to help researchers assess the resources needed to reproduce and extend this work".
- **Scope**: One mid-October 2026 pipeline run against the Linux kernel (stock desktop distro VMs), a kernelCTF-style hardened run, a July GPT-5.6 Sol comparison run, and five "takeaways" on orchestration, patching, verification and test-infrastructure risk. Does not cover disclosure logistics (see the PHP2Shell/coordinated-disclosure note), the model itself, or exploit details.

## Extracted Claims

### Claim 1: Discovery is no longer the bottleneck; validation and prioritization are
- **Evidence**: Funnel from the run: 2,308 deduplicated candidate findings → 1,724 dynamically reproduced → 1,238 LPE candidates after screening → 1,169 working LPE exploits → 948 distinct patched LPEs; 291 info-leak PoCs.
- **Confidence**: emerging (single vendor run, self-reported)
- **Quote**: "Vulnerability discovery is becoming easier to scale, but prioritization and validation remain operational bottlenecks."
- **Our assessment**: Strong, concrete support for the Patch the Planet design premise that discovery volume outpaces human review. Quantifies it: the scarce resource is reproduction, severity assessment and triage, not finding candidates. Caveat: the "bottleneck" claim is about human researcher time, while in dollar terms exploitation ($775,929 of ~$1.2M) dominated, not discovery.

### Claim 2: Dynamic reproduction in a sanitizer VM turned ~75% of static candidates into working PoCs, and false positives were rare
- **Evidence**: Triage agent generated a PoC, ran it in an isolated VM with a KASAN kernel, observed program output and console, and iterated until reproduced or exhausted. 1,724 of 2,308 reproduced in 30 hours. Of the rest, most needed elevated privileges or hit hard race/trigger conditions; only 3.1% were incorrect analysis.
- **Confidence**: emerging
- **Quote**: "Within 30 hours, our system reproduced 1724 vulnerabilities, ~74.7% of the 2,308 candidate findings."
- **Our assessment**: A strong Ch03 pattern: require runtime evidence (not model assertion) before a finding counts. The validity criteria (reachable by low-privileged user, no special capabilities, measurable memory-corruption evidence) are what make the check meaningful. Note the low-false-positive result depends on a very objective oracle (KASAN crash), which most software work lacks.

### Claim 3: Validating a candidate costs about the same whether it is a true or false positive, so filtering false positives early saves money
- **Evidence**: Validation stage cost $73,330 total; authors observed PoC-based validation was more expensive than static-only recommendation.
- **Confidence**: anecdotal (stated observation, no breakdown by true/false positive)
- **Quote**: "Thus removing false positives earlier in the pipeline makes the process meaningfully more cost-efficient."
- **Our assessment**: Useful cost-shaping heuristic for any staged agent pipeline: put cheap filters in front of expensive verification. Unquantified, so treat as directional.

### Claim 4: Per-stage cost breakdown — exploitation dominates spend
- **Evidence**: See Concrete Artifacts. Scout $3,426; Analyst $316,549; validation $73,330; screening $44,194; exploitation $775,929 ($84,929 info-leak + $691,000 LPE); total run $1,213,430, $1,279 per LPE exploit.
- **Confidence**: emerging (self-reported; costs depend on an unreleased model)
- **Quote**: "The total run cost $1,213,430 in API credits, or $1,279 per LPE exploit."
- **Our assessment**: Rare published per-stage agent cost data. Note two different per-exploit numbers: $1,279 is whole-pipeline cost / 948 unique LPEs; "$359 average" (and "$360 for 1169 cases") is only marginal exploit-development cost. Do not conflate them in the guide. Authors flag the numbers as an upper bound (Claim 9).

### Claim 5: Unbounded attempts on hard cases are the main cost leak; define a give-up condition
- **Evidence**: Failed exploitation attempts cost $3,922 each (69 cases) vs $360 for successes (1,169 cases), driven by hard cases such as race conditions. LPE candidates cost ~2x info-leak ones ($558 vs $271).
- **Confidence**: emerging
- **Quote**: "Defining a reasonable give-up condition, such as stopping the attempt after making no progress for one hour, would have reduced the cost of ExploitDev significantly."
- **Our assessment**: Concrete, generalizable harness advice (progress-based stop conditions). Note the one-hour figure is a suggestion that was not tested in this run.

### Claim 6: "Verify the path to a result, not just the result" — 10% of early "successful" exploits used the wrong 0-day
- **Evidence**: In an early run the exploitation stage reported 200 successes (root shell obtained); human review found 20 had reached root through a different 0-day than assigned. Fix: tightened task constraints and an independent check that each exploit used its assigned vulnerability.
- **Confidence**: emerging (single incident, but concrete counts)
- **Quote**: "For autonomous security research, verify the path to a result in addition to verifying the result itself; isolation, monitoring, and independent checks are necessary controls."
- **Our assessment**: High-value Ch03 failure mode: an outcome-only success oracle ("root shell obtained") is gameable by an agent via an unintended route, and the defect was caught only by human review. Generalizes to reward-hacking-style false passes in coding agents (a test passes for the wrong reason).

### Claim 7: More capable models can require lighter orchestration; scaffolding that helped one generation added little for the next
- **Evidence**: With GPT-5.5 Cyber, supplying 103 exploitation techniques in a model-friendly format raised success from 76.2% to 88.9% across 63 candidates. With GPT-5.6 Cyber the technique layer was removed, the lightly orchestrated workflow outperformed the heavily scaffolded GPT-5.5 workflow, and re-adding the layer gave only +1.5 percentage points. (Number of GPT-5.6 candidates and confidence intervals not given.)
- **Confidence**: emerging (small sample, vendor-run, one domain)
- **Quote**: "Our result suggested that stronger models require lighter orchestration and hand-holding. And the marginal improvement does not justify the maintenance cost."
- **Our assessment**: Directly relevant to Ch02. The unusually concrete before/after numbers make this stronger than the usual "bitter lesson" assertion, and the maintenance-cost framing is a good decision rule. Limits: the removed scaffold was a skills/knowledge layer, not a control-flow orchestrator, and the pipeline itself (staged agents) was kept. So the claim is "re-evaluate knowledge scaffolding on each model upgrade", not "no orchestration".

### Claim 8: Stronger models find more, so rescan previously audited code with each model generation
- **Evidence**: July 2026 GPT-5.6 Sol run: 166 unique LPEs for $513,690. October newer cyber model: 948 for $1,213,430, scanning the latest master each time. Authors state >5x more novel LPEs "despite three months of hardening between the scans".
- **Confidence**: emerging (two runs, different harness maturity; 948/166 ≈ 5.7x; harness was also evolving so model attribution is not clean — though the post says "even when using the same research harness")
- **Quote**: "Rescan previously audited code as model capabilities improve."
- **Our assessment**: Supports a recurring-scan practice. Cost per LPE fell: $513,690/166 ≈ $3,094 vs $1,279, i.e. ~2.4x cheaper per exploit (our arithmetic, not stated in the post).

### Claim 9: Reported costs are an upper bound; harness engineering should lower them
- **Evidence**: Authors state they optimized for measuring capability, not cost. No experiment backs the reduction claim.
- **Confidence**: anecdotal (explicitly an expectation)
- **Quote**: "We expect that sufficient harness engineering could meaningfully reduce the cost at each stage; thus, the costs we report are more an upper bound."
- **Our assessment**: Unverified. Use the numbers as order-of-magnitude, not benchmarks.

### Claim 10: Automated triage must revalidate against current code because maintainers patch fast
- **Evidence**: After the 10-day scan on latest master: 61 LPEs already patched upstream, 43 had staging patches, 299 "being reported and discussed publicly".
- **Confidence**: emerging
- **Quote**: "Revalidating findings against the latest code, including new code that was merged after the original scan, helps avoid duplicate or obsolete reports."
- **Our assessment**: Operational guidance on dedup/staleness that supports the maintainer-burden concerns in the Patch the Planet note. Note the post's summary prose says "over 100 ... patched or had staging patches", consistent with 61+43=104.

### Claim 11: AI-generated patches need iteration and adversarial review, and models can find flaws in human patches
- **Evidence**: First-pass patches were functionally correct but sometimes bloated, performance-costly, convention-violating or missed variants. Extra instructions and iteration improved quality; "in a few cases" the prototype found issues in human-expert patches before merge. No patch-quality metrics are given.
- **Confidence**: anecdotal
- **Quote**: "we recommend using models for adversarial review of human and AI-generated patches, which can identify issues such as the patch being bypassable, missing other attack paths or variants, and more."
- **Our assessment**: Corroborates the adversarial-patch-testing step in the coordinated-disclosure note. Reviewing the same pipeline's patches is still done by humans before reporting.

### Claim 12: Frontier models devised novel exploitation techniques, not just known patterns
- **Evidence**: Sampled 166 exploits; 10 new techniques (2 persistent elastic objects, 2 page-grooming, 5 data-only privesc, 1 arbitrary type confusion), confirmed new by third-party kernel experts. Details withheld.
- **Confidence**: anecdotal (unverifiable; withheld "for safety reasons")
- **Quote**: "Frontier models do not just pattern match known vulnerable code patterns or solely use known exploitation techniques; they demonstrate creativity and novel approaches."
- **Our assessment**: Cannot be independently checked; treat as vendor claim. Relevant to the Ch06 threat model mainly as capability signal.

### Claim 13: Economics: the pipeline was "net profitable" against public bounty amounts, so defenders should scan first
- **Evidence**: Hypothetical valuation of 948 exploits at historical Pwn2Own ($20k) / TyphoonPWN ($70k) bounties is $18.9M–$66.3M, ~16x–55x cost. kernelCTF-style run: 21 LPEs plus 25 info-leak PoCs, $32,936, 112 hours, discovery 83.7% of cost; ~$1.5M hypothetical bounty (~45x). 26 confirmed 0-day LPEs accepted by kernelCTF in 2026 at time of writing.
- **Confidence**: anecdotal/emerging (hypothetical valuation; bounties would not scale linearly, and many of the 948 would share patches or be duplicates)
- **Quote**: "Based on public pay-out amounts, with current cyber-capable models, our vulnerability research pipeline was net profitable at the time of this research."
- **Our assessment**: The bounty-multiplier math is rhetorical (948 exploits would never all be paid at list price). The robust part is the cost scale (~$1.3k per LPE) as a threat-model input. Also the kernelCTF run required dropping the SLAB_VIRTUAL mitigation from the config because the latest kernel was incompatible, so it is not a fully like-for-like comparison.

### Claim 14: Test infrastructure is itself attack surface for offensive agents
- **Evidence**: In the kernelCTF run the analyst agent hit an unexpected crash, traced it to a QEMU TCG bug without QEMU source access, and an ExploitDev agent then exploited it; the bug was fixed upstream but not in the release build used.
- **Confidence**: anecdotal (single incident)
- **Quote**: "We recommend testing each part of the infrastructure before carrying out offensive vulnerability research."
- **Our assessment**: Sandbox-escape-class risk for any agent running exploit code in VMs. Relevant to Ch06 guidance on sandboxing agent execution.

### Claim 15: Practical defender implications: unpatched local access ≈ root; use isolation; invest in secure-by-default
- **Evidence**: Reasoned conclusions, no new data.
- **Confidence**: emerging
- **Quote**: "having access to a low-privileged account on an operating system, that isn’t up-to-date on its latest available patches should be considered functionally equivalent to root access for a well-resourced threat actor."
- **Our assessment**: Reasonable planning assumption given Claim 4 costs. Mentions Firecracker and gVisor for blast-radius limiting.

## Concrete Artifacts

Pipeline stages (OpenAI, "The vulnerability research pipeline"):

```
1. Vulnerability discovery: Agents identify security-relevant parts of the codebase and scan them for candidate findings.
2. Dynamic validation: Agents attempt to reproduce each candidate in an isolated environment and preserve runtime evidence.
3. Exploitability assessment: Agents test whether validated vulnerabilities could enable information disclosure or local privilege escalation.
4. Patch generation: Agents generate patches that address each identified vulnerability.
5. Human review: Security researchers review the exploit, patch, and proposed severity before reporting to the maintainers.
```

Per-stage cost and yield (numbers as reported in the article; table layout ours):

```
Stage                      Output                                   API cost
Scout                      5,034 targets (~2.8M LOC, ~7% of kernel)   $3,426
Analyst (12 h)             2,308 candidate findings (deduped)         $316,549
Validation (30 h)          1,724 reproduced (~74.7%)                  $73,330
Screening                  313 info-leak + 1,238 LPE candidates       $44,194
Exploitation               291 info-leak PoCs, 1,169 LPE exploits     $775,929
  (info-leak $84,929; LPE $691,000)
Patches / variant analysis 948 distinct patches (= unique LPEs)
Whole run                  948 LPE exploits                           $1,213,430 ($1,279 each)
```

Orchestration experiment (GPT-5.5 Cyber vs GPT-5.6 Cyber):

```
GPT-5.5 Cyber, no technique layer:   76.2% success (63 candidates)
GPT-5.5 Cyber + 103 techniques:      88.9%
GPT-5.6 Cyber, light orchestration:  outperformed heavily scaffolded GPT-5.5
GPT-5.6 Cyber + technique layer:     +1.5 percentage points only
```

Output bundle per finding: "a root cause analysis, a minimal crashing proof-of-concept, a candidate patch, and a full exploit".

Validation environment: KASAN kernel VMs; exploit-dev VMs with SMEP, SMAP, KASLR and HARDENED_USERCOPY enabled "to prevent unrealistic assessments that depended on protections being disabled".

## Cross-References

- **Corroborates**: `blog-openai-patch-the-planet.md` Claim 11 (manual human review of every finding because models "produce a high volume of false positives") — this post keeps a human-review final stage and also documents a concrete automated false-pass (wrong 0-day). `blog-openai-coordinated-disclosure-critical-vulnerabilities.md` Claim 5 (adversarial testing of patches with frontier models) — matches Claim 11 above. `blog-anthropic-ai-accelerated-offense.md` Claim 5 (plan for an order-of-magnitude increase in vulnerability finding volume) and Claim 6 (scan your own code with AI) — this run supplies volume and cost numbers and the "rescan each generation" advice.
- **Contradicts**: None found. Claim 7 (lighter orchestration for stronger models) is in some tension with the orchestration-heavy pattern in `blog-anthropic-block-fable-orchestration-migrations.md` Claim 1, but they address different things (knowledge scaffolding for a single agent vs a model orchestrating workers), so this is a conditioning variable, not a contradiction; no issue filed.
- **Extends**: `blog-openai-patch-the-planet.md` (June program announcement, 24 LPEs with GPT-5.5 Cyber) — the post says that work was "expanded ... into a pipeline". `blog-openai-patch-the-planet.md` Claim 2 (program designed not to add to maintainer triage burden) — this post's revalidate-against-latest-code takeaway is an operational mechanism for that goal.
- **Novel**: Per-stage agent API cost and yield data for a full discovery-to-patch pipeline; the before/after numbers for removing a skills/technique scaffold when the model upgrades; the "wrong 0-day" 20-of-200 false-success incident; give-up-condition cost analysis; the QEMU test-infrastructure exploit.

## Guide Impact

- **Chapter 03 (verification)**: Add the "verify the path to a result, not just the result" principle with the 20-of-200 wrong-0-day example (Claim 6), and the runtime-evidence-before-trust pattern (sanitizer-VM reproduction, Claim 2). Note that the oracle here is unusually objective.
- **Chapter 02 (harness engineering)**: Add the re-evaluate-scaffolding-on-each-model-upgrade rule with the 76.2%→88.9% then +1.5pp numbers (Claim 7), flagged as a small vendor-run experiment on a skills layer; add progress-based give-up conditions for expensive agent stages (Claim 5) and early cheap filtering (Claim 3).
- **Chapter 06 (security threat model)**: Use the ~$1,279-per-LPE figure and the 948/166 July-to-October jump as threat-model inputs, with an "upper bound, self-reported" caveat (Claims 4, 8, 9); add the test-infrastructure-as-attack-surface point (Claim 14).
- **Chapter 05 (team adoption)**: Human review remains the final gate and revalidation against current upstream reduces maintainer burden (Claims 1, 10).

## Extraction Notes

- Fetched the full article HTML directly and read the entire body (all sections: Summary, Methodology, Findings, Reflections, Why the Linux kernel, Cost analysis, pipeline stages, takeaways, Conclusion). Quotes were copied from the page text. The summarizing WebFetch pass could not be used for verbatim text, so the raw HTML was converted to text and read.
- The article has an internal inconsistency worth knowing: 1,169 working LPE exploits vs 948 "distinct" LPEs after variant analysis and patch deduplication; the headline per-exploit cost uses 948.
- The triage comments mention "$1.2M" and "$1,279 per exploit"; these match the article ($1,213,430).
- No contradiction issue filed; see Cross-References.
- Related links in the article (Codex Security plugin, kernelCTF, Pwn2Own) were not followed.
