---
source_url: https://claude.com/blog/the-claude-science-product-guide
source_type: blog-post
title: "The Claude Science product guide"
author: Anthropic (product guide; no individual byline)
date_published: 2026-08-18
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: anecdotal
issue: "#2776"
---

# The Claude Science product guide

> Anthropic's first-party deployment guide for Claude Science (beta) — a
> local-daemon AI research application for life sciences that pre-configures
> ~150 skills and 60+ scientific database connectors, runs analyses next to
> lab data/compute with jobs dispatched to SSH/SLURM/cloud GPU accounts, and
> layers five specific reliability design choices (persistent kernels,
> four-layer artifact provenance, a background reviewer agent, visible
> plan-then-approve permissioning, and unconditional biosecurity
> safeguards) — plus a three-phase (Foundation/Pilot/Scale) adoption
> roadmap and named enterprise case studies with efficiency claims that are
> vendor-supplied and not independently verified.

## Source Context

- **Type**: blog-post (claude.com/blog landing page, published August 18,
  2026) linking to a full 25-page eBook PDF ("Claude Science product guide:
  A practical deployment guide," created August 11, 2026, hosted at
  `cdn.prod.website-files.com`) and to Anthropic's June 30, 2026 product
  launch announcement ("Claude Science, an AI workbench for scientists, is
  now available," `anthropic.com/news/claude-science-ai-workbench`). This
  note extracts from all three: the landing page overview, the launch
  announcement (Manifold Bio, UCSF, and Allen Institute case studies and
  architecture description), and the full eBook (Novo Nordisk, Garvan
  Institute, and Sanofi case studies, adoption roadmap, skill/connector
  tables, FAQ for IT/CIO audiences).
- **Author credibility**: First-party Anthropic product marketing and
  deployment documentation — the highest-credibility source for *what the
  product does and how it is architected* (a vendor describing its own
  system), but the lowest-independence source for *whether the product
  delivers the claimed outcomes* (efficiency percentages and adoption
  metrics come from named but Anthropic-selected customer quotes, not
  independently audited case studies). No third party is cited as having
  reproduced any of the efficiency numbers.
- **Scope**: Covers when to use which Claude product surface for life
  sciences work (Claude Science vs. Chat vs. Cowork vs. Code vs. Platform
  vs. Managed Agents), the Claude Science architecture (local daemon,
  persistent kernels, skill/connector catalog, provenance model, approval
  broker, biosecurity controls), a three-phase adoption roadmap with
  phase-specific metrics, four customer case studies (Novo Nordisk, Garvan
  Institute, Sanofi, Manifold Bio, plus two named academic users), and an
  IT/CIO-oriented FAQ (data residency, HIPAA/GxP/NIH-controlled-data
  status, pricing, identity/access controls). Does NOT cover: independent
  benchmarking of Claude Science's scientific accuracy, pricing beyond "no
  separate license, draws down existing plan limits," the full list of
  ~150 skills (only representative tables by domain are given), or any
  quantitative comparison against competing life-sciences AI products.

## Extracted Claims

### Claim 1: Claude Science is positioned as one surface in a broader Claude product family, with an explicit division of labor — Claude Science for analysis/figures/results, Claude Cowork and Claude for Microsoft 365 for document/regulatory work, Claude Code for production software, and the Claude Platform/Managed Agents for embedding Claude into existing enterprise systems
- **Evidence**: A named product matrix table (surface, best-for, primary users, where it runs, example task) covering all six surfaces, plus explicit guidance ("Use Claude Code when the output is software that ships to other teams; reach for Claude Science when the output is an analysis, a figure, or a result.").
- **Confidence**: settled (first-party architectural/positioning fact about how Anthropic designed its own product line to fit together — not a performance claim)
- **Quote**: "Claude Science is an application for the digital steps of research, including literature review, experiment design, data analysis, figure generation, and writeups. It runs locally next to the lab's data and compute, ships with domain capabilities across genomics, single cell, proteomics, structural biology, cheminformatics, and more, and tracks the provenance of every artifact so results can be reproduced and defended."
- **Our assessment**: This is a genuinely new data point for the corpus: no existing source note maps out how Anthropic segments its product line for a single regulated vertical (life sciences) across six surfaces with an explicit "when to use which" decision table. The division-of-labor logic (surface chosen by output type — analysis vs. document vs. software vs. embedded system) is a reusable framework independent of whether Claude Science itself performs well.

### Claim 2: Claude Science runs as a local daemon on lab-owned infrastructure (laptop, Linux box, HPC login node, or cloud VM in the customer's own tenancy) with a browser-based UI, and dispatches heavy compute jobs to the lab's own SSH host, SLURM cluster, or serverless GPU account rather than running the compute itself
- **Evidence**: Architecture description repeated consistently across the launch announcement and the eBook's technical and FAQ chapters, including the specific claim that SLURM is auto-detected and batch directives are auto-written.
- **Confidence**: settled (first-party architectural fact, consistent and specific across three independently-worded restatements in the source material)
- **Quote**: "Claude Science is a standalone application for macOS and Linux that runs a local daemon with its UI in the browser—the same model as a Jupyter notebook, but the agent is driving. The scientist installs it wherever the data lives: a laptop, a lab Linux box, an HPC login node, or a cloud VM. Data, compute environments, and agents stay on that machine, while the scientist connects from a laptop browser over an SSH tunnel when the daemon is running remotely."
- **Our assessment**: This is the product's core differentiator and the design choice that makes the rest of the guide's regulated-data claims (Claim 8 below) coherent: by keeping data and compute on infrastructure the customer already controls, Claude Science avoids the "upload your controlled dataset to a SaaS vendor" problem that would otherwise block adoption in regulated life-sciences environments. It is architecturally the closest analog in the corpus to `blog-anthropic-claude-code-self-hosted-environments.md`'s self-hosted runner model — see Cross-References.

### Claim 3: Five specific design choices are named as what make Claude Science's scientific analysis "hold up under review": persistent kernels that keep loaded data/models in memory and feed generated figures back into the agent's own context, a separate background reviewer agent that flags any claim it cannot trace to evidence, full four-layer provenance on every artifact, visible plan-then-approve permissioning, and unconditional biosecurity safeguards
- **Evidence**: A dedicated eBook section ("Analysis that holds up under review") naming and describing all five design choices individually, each with a specific mechanism.
- **Confidence**: settled (specific, named architectural description of five distinct product features, not a vague reliability claim)
- **Quote**: "Agents see their own plots—every figure generated is fed back into the agent's context, so it runs QC on its own output, spots the outlier cluster in its own UMAP, and filters it before moving on." (persistent kernels) / "A separate reviewer agent reads each session's transcript while the primary agent works and flags any claim it cannot trace to evidence. Findings surface inline at the suspect sentence and the agent fixes them before finishing. The reviewer runs every session by default and can be triggered manually at any point." (background reviewer)
- **Our assessment**: The "background reviewer agent that reads the transcript and flags untraceable claims, running by default every session" is the single most concrete, novel mechanism in this source. It is architecturally distinct from a verification *skill* the user must invoke (contrast `blog-anthropic-claude-code-verification-loops-skills.md`, where verification loops are opt-in patterns a practitioner builds) — here verification is an always-on, separately-instantiated agent role built into the product by default. Whether it actually catches errors reliably is not independently measured in this source; the mechanism description is credible as architecture, not as an accuracy guarantee.

### Claim 4: A human-approval broker gates thirteen distinct action kinds (including code execution, network grants, host file access, deletions, MCP tool calls, remote compute dispatch, and skill persistence) with a uniform "allow once / for this project / always" approval card, sitting under an OS-level sandbox with deny-by-default network egress, SSRF/DNS-rebind defenses, and seccomp hardening, and plan mode is on by default so the agent drafts a step-by-step plan before executing
- **Evidence**: Two independently-worded FAQ/technical restatements naming the same "thirteen action kinds" figure and the same allow-once/project/always mechanism.
- **Confidence**: settled (specific, internally consistent architectural fact repeated verbatim in structure across two sections of the same document)
- **Quote**: "A human-approval broker gates thirteen action kinds, including code execution, network grants, host file access, deletions, MCP tool calls, remote compute dispatch, and skill persistence. Every request surfaces as a single approval card—allow once, for this project, or always—and every decision can be reviewed or revoked from one permission screen. An OS-level sandbox with allowlist-proxy network egress, SSRF and DNS-rebind defenses, and seccomp hardening sits underneath. Plan mode is on by default, so the agent drafts a step-by-step plan and waits for approval before executing."
- **Our assessment**: This is a materially different permission philosophy from `blog-anthropic-claude-code-auto-mode.md`'s auto mode, which is designed explicitly to *reduce* prompt frequency via a model-based classifier because manual approval is "effectively theater" at 93% approval rates (that note's Claim 1). Claude Science instead defaults to plan-then-approve-every-action-kind. This is not a contradiction — the two products target different risk profiles (general-purpose coding vs. dual-use biological research with CBRNE-adjacent risk) — but it is a useful data point that Anthropic's own permission-UX philosophy is not one-size-fits-all across its product line; it scales approval friction to domain risk.

### Claim 5: Claude Science ships pre-configured, optional connections to more than sixty scientific databases and roughly 150 curated skills, organized by domain (genes/variants, expression/single-cell, oncology, pharmacology/safety, metabolomics, neuroscience, plus multi-database toolkits), and any working pipeline can be saved as a reusable skill that future sessions inherit automatically
- **Evidence**: Explicit quantitative claim plus a detailed skill/database table listing named skills (e.g., `cellxgene-census`, `clinpgx-database`, `hmdb-database`, `foldseek`) with source and "use when" guidance for each.
- **Confidence**: settled (specific, itemized self-reported catalog — the tables name concrete skills and sources, which is a falsifiable, checkable claim rather than a vague "many integrations" statement)
- **Quote**: "Claude Science ships with configurable capabilities for common scientific workflows, backed by optional connections to more than sixty scientific databases and roughly 150 curated skills. When a project spans domains, it plans and routes across them automatically." / "Each skill is open source, so computational teams can inspect the query logic, pin versions, or extend a skill with their organization's own filters and output formats."
- **Our assessment**: The catalog table (Concrete Artifacts below) is the most reusable artifact in this source: a checkable list of named scientific-database skills a life-sciences engineering team could audit their own needs against. "Each skill is open source" is notable — it means the query logic itself is inspectable, distinguishing this from a black-box RAG-style integration.

### Claim 6: Claude Science defines an explicit decision rule for when to use a "skill" (public data, queried precisely and reproducibly) versus a "connector" (organization's own systems, where entitlements matter), and states that most real questions combine both
- **Evidence**: A named decision-rule paragraph in the eBook's product-overview chapter.
- **Confidence**: settled (explicit, stated design principle, not inferred)
- **Quote**: "Use a connector when the answer lives in the organization's own systems, such as an ELN, a CTMS, or a regulatory document repository, and entitlements matter. Use a scientific data skill when the answer lives in the public record and the value is in querying it precisely, reproducibly, and in combination with other sources. Most real questions use both: Claude pulls the internal context through a connector, grounds it against public reference data through a skill, and returns an analysis the scientist can verify line by line."
- **Our assessment**: This skill-vs-connector distinction generalizes beyond life sciences: any harness that mixes "query the internal system of record" with "ground against public reference data" faces the same design choice. It is a crisper articulation of a distinction the corpus has previously treated informally when discussing MCP servers vs. skills as extension points.

### Claim 7: Claude Science ships biosecurity-specific safeguards on top of the general sandbox — biosecurity rules written unconditionally into every agent's system prompt (not user- or admin-disableable), a per-turn bio trajectory classifier running in the binary that cannot be disabled, OAuth-only authentication with no anonymous or API-key access, and completed external red-teaming plus Anthropic Safeguards review against CBRNE risk before public release
- **Evidence**: Two matching restatements (technical chapter and CIO FAQ) of the same four-part safeguard list.
- **Confidence**: settled (specific, named safeguard mechanisms, consistent across two independently-worded sections)
- **Quote**: "Biosecurity rules ship unconditionally in every agent's system prompt, a per-turn bio trajectory classifier runs in the binary and cannot be disabled by the user or admin, and authentication is OAuth-only with no anonymous or API-key access against the product. Claude Science completed external red-teaming and Anthropic Safeguards review against CBRNE risk before public release."
- **Our assessment**: "Cannot be disabled by the user or admin" is a meaningfully stronger claim than a configurable safety setting — it states the classifier is compiled into the binary rather than policy-configured. This is consistent with Anthropic's general dual-use-domain posture elsewhere in the corpus but is the first source with this level of implementation specificity (binary-level, not prompt-level or account-policy-level) for a bio-specific safeguard.

### Claim 8: Claude Science explicitly disclaims validated-system status — it is not HIPAA-ready at launch, not assessed against NIST SP 800-171 (required for NIH controlled-access data like dbGaP), and not usable in GxP-regulated workflows without a qualified human reviewer approving every output before it enters a validated record
- **Evidence**: Three separate, direct FAQ answers to CIO-posed questions about regulated-data readiness, each stating a specific limitation and, where applicable, a roadmap status.
- **Confidence**: settled (self-disclosed scope limitation — this is the kind of claim that strengthens credibility precisely because it is a limitation the vendor did not need to volunteer)
- **Quote**: "Not at launch. HIPAA readiness is on the post-launch roadmap. Until then, Claude Science should not be used to process protected health information." / "Claude Science is not a validated system. Organizations typically deploy it in research, analysis, and draft-support roles, with a qualified scientist or reviewer approving every output before it enters a validated record, a regulatory submission, or a publication."
- **Our assessment**: This is the most important claim in the source for guide purposes because it directly bounds every other claim: whatever the background reviewer and provenance system provide, Anthropic itself states this is not sufficient for compliance-grade validation without an additional qualified-human-review step. Any guide recommendation for regulated-industry adoption of Claude Science must carry this caveat forward, not just the reliability-design claims (Claim 3).

### Claim 9: The recommended adoption sequence is a three-phase roadmap — Foundation (IT/governance review, daemon host decision, 2-3 champion groups identified), Pilot (champions run real analyses, measured against cycle time / trust-without-rerun rate / cold-reproduce rate, adjacent document surfaces onboard in parallel), and Scale (managed daemon host pattern, curated org skill catalog, governance settled before scale, not after) — with a specific warning that a scientist's first session determines whether they return
- **Evidence**: A dedicated adoption-roadmap chapter with a phase/actions/what-you'll-see table and two explicit "pro-tip" call-outs.
- **Confidence**: emerging (this is prescriptive rollout guidance from the vendor, not a measured outcome of any specific rollout — no source-cited organization is shown having followed exactly this three-phase sequence with reported results)
- **Quote**: "A scientist who opens Claude Science, points it at a folder of FASTQ files, approves the plan, and gets a clustered UMAP with the code and environment captured underneath will come back. A scientist who opens it without data in reach will close it. Make sure the install lands next to real data." / "Governance should be settled before scale, not after."
- **Our assessment**: The three named pilot-phase metrics — cycle time (before/after on the same dataset class), trust-without-rerun rate, and cold-reproduce rate (can a different scientist re-run week-one's artifact in week four) — are a specific, reusable measurement framework for any AI-tool pilot in a scientific or technical domain, independent of whether Claude Science specifically delivers on them. This is the most guide-actionable content in the roadmap chapter.

### Claim 10: Novo Nordisk built "NovoScribe" on Claude and reports cutting CSR (clinical study report) writing time by 90%, with clinical documentation that previously took more than ten weeks now reaching a reviewable first draft in roughly ten minutes
- **Evidence**: A named customer case study with an attributed quote from a named executive (Waheed Jowiya, Digitalization Strategy Director, Novo Nordisk).
- **Confidence**: anecdotal (single-customer, vendor-selected, self-reported efficiency figure; no independent verification or methodology for the "ten weeks to ten minutes" comparison is given — e.g., unclear whether the ten-minute draft required the same downstream review effort the ten-week process included)
- **Quote**: "Clinical documentation that previously took more than ten weeks now reaches a reviewable first draft in roughly ten minutes." / "Claude has helped us cut writing times on CSRs by 90% so we can get documentation directly into human hands for review and approval." — Waheed Jowiya, Digitalization Strategy Director, Novo Nordisk
- **Our assessment**: This describes Claude Cowork/Platform-based document automation (NovoScribe), not Claude Science itself — the guide should not conflate this case study's efficiency number with Claude Science's own capabilities. As with all vendor-selected testimonials, the 90%/ten-minutes figures describe time-to-first-draft, not time-to-approved-output, and the quote itself acknowledges a human review-and-approval step still follows.

### Claim 11: Independent academic users report Claude Science accelerating specific research workflows — a UCSF epidemiologist's germline-variant analysis pipeline "in roughly one-tenth the time it previously took" (independently validated by the researcher's own team), and an Allen Institute neuroscientist's 20-skill multi-agent literature-review pipeline cutting review-writing time from up to two years to producing about ten reviews, several over 100 pages
- **Evidence**: Two named academic case studies (Stephen Francis, UCSF Brain Tumor Center; Jérôme Lecoq, Allen Institute) with attributed quotes and a stated independent-validation step for the UCSF case.
- **Confidence**: anecdotal (named, individually-attributed accounts — stronger than a generic testimonial because a specific validation step is claimed — but still self-selected by Anthropic for the case-study chapter, single-lab, and not peer-reviewed or independently reproduced outside the source)
- **Quote**: "Although this work predated Claude Science, Francis said the app has dramatically accelerated the analysis, enabling comprehensive germline workups across multiple approaches in roughly one-tenth the time it previously took." / "A key component of the workflow, enabled by Claude Science, is the use of actor-critic pairs: one agent creates content while a separate reviewer agent evaluates it for accuracy and citation fidelity."
- **Our assessment**: The Lecoq "actor-critic pairs" description is the most concrete multi-agent pattern in the case-study chapter and is architecturally consistent with, and an independent-practitioner-level instance of, the product's own background-reviewer design (Claim 3). The UCSF case is notable for including a stated independent validation step ("His group independently validated Claude Science's results") — this is a meaningfully stronger evidentiary bar than the Novo Nordisk/Sanofi testimonials, which report vendor-facing metrics with no validation step described.

### Claim 12: Claude Science pricing draws down from the user's existing Claude plan (Pro/Max/Team/Enterprise) with no separate license and no free tier; usage is token-intensive enough that heavy users are expected to need Max-tier limits, at a rate "comparable to heavy Claude Code use"
- **Evidence**: Direct FAQ answer on pricing and usage intensity.
- **Confidence**: settled (specific, first-party pricing-model fact, though the comparative "rate comparable to heavy Claude Code use" is a qualitative rather than quantified comparison)
- **Quote**: "Claude Science draws down from the usage limits of the user's existing Claude plan—Pro, Max, Team, or Enterprise—with no separate license and no free tier. It is token-intensive: scientists routinely run several long agentic analyses in parallel, and heavy users consume at a rate comparable to heavy Claude Code use, so organizations should plan usage limits accordingly and expect heavy individual users to need Max-tier limits."
- **Our assessment**: This is a practically important operational data point for any team budgeting adoption: Claude Science is not a separately-metered product, so its usage competes with the same plan-level token budget as every other Claude surface a scientist uses. A pilot-phase budgeting recommendation should flag this explicitly rather than assuming Claude Science usage is additive to existing plan costs.

## Concrete Artifacts

### Product matrix: when to use which Claude surface

```
Source: eBook, Chapter 1 ("Claude product matrix: when to use what")

Surface              Best for                                  Where it runs
Claude Science       End-to-end research analysis with full    Local app (macOS, Linux);
                      provenance — literature, pipelines,        dispatches to SSH, SLURM,
                      figures, writeup                           or cloud compute
Claude Chat          Conversational drafting, day-to-day Q&A    Browser, desktop, mobile
Claude Cowork        Cross-app study/document work spanning      Claude desktop app
                      files and multiple systems
Claude Code          Agentic software engineering inside a       Terminal, IDE
                      repository
Claude for           In-place drafting, redlining, review       Word/Outlook/Excel/
Microsoft 365         across the Microsoft suite                 PowerPoint add-ins; Teams/
                                                                  SharePoint/OneDrive connector
Claude Platform (API) Embedding Claude into ELN, LIMS, CTMS,     Anthropic API, Bedrock,
                      safety, or RWE systems                     Vertex AI, Microsoft Foundry
Claude Managed Agents Running custom agents as hosted cloud      Claude Platform (hosted by
                      services                                    Anthropic)
```

### Scientific database skill catalog (representative, by domain)

```
Source: eBook, Chapter 2 ("Domain expertise, ready on day one")

Genes/variants/annotation:
  gene-database          NCBI Gene/Datasets     gene lookup by symbol/ID, RefSeqs, GO terms
  biothings-database      BioThings.io           cross-database ID resolution (MyGene/MyVariant/
                                                  MyChem/MyDisease)
  ena-database            European Nucleotide     raw sequence data (FASTQ, assemblies) by
                          Archive                 accession
  harmonizome-database     Harmonizome            gene associations across 170+ functional
                                                  genomics resources at once

Expression/single-cell:
  cellxgene-census        CZ CELLxGENE Census    filter 125M+ cells by type/tissue/disease,
                                                  pull expression matrices into scanpy/PyTorch
  immgen-database          ImmGen                 gene expression across mouse immune cell
                                                  populations
  allen-brain-database     Allen Brain Atlas       gene expression/connectivity/spatial
                                                  transcriptomics, mouse and human brain

Oncology:
  cosmic-database          COSMIC                 somatic mutations, Cancer Gene Census,
                                                  mutational signatures (requires institutional auth)
  tcia-database            The Cancer Imaging      DICOM imaging series for radiomics/model
                          Archive                 training

Pharmacology/safety:
  clinpgx-database         ClinPGx (PharmGKB)      gene-drug interactions, CPIC dosing guidelines
  fda-database             openFDA                 adverse events, recalls, drug labels, 510(k)/PMA

Metabolomics:
  hmdb-database            Human Metabolome DB     220K+ human metabolites, biomarker associations
  metabolomics-workbench-  Metabolomics Workbench  4,200+ public metabolomics studies

Neuroscience:
  neuromorpho-database      NeuroMorpho.Org         neuron morphology reconstructions
  openneuro-database        OpenNeuro               BIDS-formatted MRI/fMRI/EEG/MEG/PET datasets

Multi-database toolkits (broader Python packages loadable as skills):
  bioservices  (40+ services: UniProt, ChEMBL, PubChem, Reactome, QuickGO, KEGG, Ensembl, BioMart)
  gget         (20+ databases: Ensembl, UniProt, NCBI, ARCHS4, Enrichr, OpenTargets, PDB, AlphaFold, BLAST)
  biopython (Bio.Entrez)  (all NCBI Entrez databases: PubMed, Gene, Nucleotide, Protein, SRA, Taxonomy,
                            Assembly, BioProject)
  hmmer        (Pfam, UniProtKB, Reference Proteomes — profile/sequence search)
  foldseek     (AlphaFold DB, PDB100, ESMAtlas, CATH — structure-based homolog search)

Total catalog: "more than sixty scientific databases and roughly 150 curated skills"
```

### Three-phase adoption roadmap table

```
Source: eBook, Chapter 4 ("Claude Science adoption roadmap")

Phase        Actions                                        What you'll see
Foundation   IT and data-governance review of local          Champions reporting back use
             install, sandbox, and network allowlist.        cases. First "this would have
             Decide daemon host pattern. Identify 2-3         taken me three weeks" moments.
             champion groups in computational biology
             or bioinformatics. Confirm SSO/SCIM and
             Team/Enterprise plan.

Pilot        Champions run real analyses on real lab          Measurable time savings.
             data. Weekly check-ins. Measure cycle             Champions saving custom skills
             time, keep-rate, and cold-reproduce rate.         and specialists. Wet-lab
             Stand up Cowork and M365 for adjacent             scientists and PIs joining
             document functions in parallel.                   behind the computational leads.

Scale        Managed daemon host pattern. Curated org         Skills shared across
             skill catalog. Vetted network allowlist and       therapeutic areas. New hires
             compute-dispatch targets. Agreed provenance-      ramping on encoded pipelines.
             retention policy for regulated and                Declining "can someone help me
             publication-bound analyses. Onboard the           run this" requests to the
             next wave of groups.                               bioinformatics core.

Pilot-phase metrics named explicitly:
  1. Cycle time — how long the pilot analysis took before Claude Science vs. after, same dataset class
  2. Trust-without-rerun rate — how often a scientist/PI trusts the result without manually re-running it
  3. Cold-reproduce rate — hand week-one's provenance bundle to a different scientist in week four; can they re-run it cold
```

### Human-approval broker: gated action kinds

```
Source: eBook, Chapter 6 (CIO/IT FAQ, "How is code execution and file access controlled?")

Gated action kinds (13 total; list as enumerated in source, non-exhaustive per "including"):
  - code execution
  - network grants
  - host file access
  - deletions
  - MCP tool calls
  - remote compute dispatch
  - skill persistence

Approval granularity: allow once | allow for this project | allow always
Underlying layer: OS-level sandbox, allowlist-proxy network egress, SSRF/DNS-rebind
  defenses, seccomp hardening
Default mode: plan mode on by default (step-by-step plan drafted, approval required
  before execution)
```

### Anthropic internal research statistics (cited in Foreword)

```
Source: eBook, Foreword

"Deloitte's 2026 Life Sciences Outlook, a survey of 280 biopharma and medtech
leaders, found that 78% expect AI to play a central role in driving major change
this year—yet only 14% report full implementation of AI tools into daily
workflows, with another 40% still working toward it."

"Anthropic's own internal research, drawn from interviews with researchers
across chemistry, physics, biology, and computational fields, found that 91%
of scientists want more AI in their research, while 79% named trust and
reliability as their number-one barrier to adoption."
```

## Cross-References

- **Corroborates**: `blog-anthropic-claude-code-self-hosted-environments.md`
  (Claim 6, Claim 8, Claim 10). That note documents Claude Code's
  self-hosted-runner model, where "repository checkouts, build artifacts,
  secrets, and session-created files stay on customer infrastructure, but
  conversation content...is sent to Anthropic for inference" and the
  runner-side hardening checklist includes "default-deny network egress"
  and "blocking the cloud metadata endpoint." Claude Science's local-daemon
  model (Claim 2 here) and its explicit FAQ answer — "Files remain on the
  host and are read in place; content the agent reads as part of an
  analysis is sent to Anthropic's API as context...An OS-level sandbox
  with deny-by-default network egress controls all other traffic leaving
  the host" — describes the same data-residency split (compute/files local,
  inference content sent to Anthropic) and the same deny-by-default egress
  posture, independently implemented for a different product line. This is
  strong evidence that "local compute/data, cloud inference, default-deny
  egress" is Anthropic's standard architecture for regulated or
  sensitive-data deployments across at least two separate products (Claude
  Code, Claude Science), not a one-off design for either.

- **Corroborates**: `blog-anthropic-claude-code-verification-loops-skills.md`
  (Claim 2, Claim 8). That note describes verification loops as an
  opt-in pattern practitioners build (standalone/embedded/chained skills,
  including an internal Anthropic chain `/code-review` → `/simplify` →
  `/verify` → `/design`). Claude Science's "background reviewer" (Claim 3
  here — "a separate reviewer agent reads each session's transcript...and
  flags any claim it cannot trace to evidence...runs every session by
  default") is architecturally the same actor-critic concept but built in
  as an always-on default rather than a skill a practitioner must author
  and invoke. The Lecoq case study's "actor-critic pairs" (Claim 11 here)
  is an independent user's articulation of the exact same pattern. Together
  these sources show the actor-critic/reviewer-agent pattern recurring
  across Anthropic's own product design and independent practitioner
  usage — see also `blog-anthropic-carta-healthcare-context-engineering.md`
  Claim 8 (human-in-the-loop transparency via shown evidence/rationale per
  extracted data point), which is the same "show your work so a human can
  verify without blind acceptance" principle applied to structured clinical
  extraction rather than agentic review.

- **Extends**: `blog-anthropic-claude-code-auto-mode.md` (Claim 1, Claim 9).
  That note establishes that manual permission-approval is "effectively
  theater" at a 93% approval rate, motivating auto mode's classifier-based
  reduction in prompt frequency, and documents a three-tier permission
  structure (safe allowlist, in-project edits, classifier-evaluated).
  Claude Science's human-approval broker (Claim 4 here) takes the opposite
  design direction for a higher-risk domain: thirteen gated action kinds,
  plan-mode-on-by-default, no classifier-based auto-approval described in
  this source. This is not a contradiction (per MINER.md §4a, this is a
  conditioning variable — different products serving different risk
  profiles, general coding vs. dual-use biological research) but it is a
  useful data point for the guide: Anthropic's own permission philosophy
  scales approval friction to domain risk rather than applying one fixed
  policy across its entire product line.

- **Corroborates (different domain)**: `blog-openai-lifescibench.md`
  (Claim 9 — GPT-Rosalind's pass rate on life-science tasks falls from
  45.1% on text-only tasks to 28.1% on tasks requiring interpretation of a
  supplied artifact/figure/file). This is independent third-party
  quantitative evidence, from a competing lab's own benchmark, for exactly
  the failure mode Claude Science's design choices (persistent kernels
  feeding generated figures back into agent context; the background
  reviewer flagging untraceable claims) are built to catch. Neither source
  measures whether Claude Science's specific mitigations close this gap —
  LifeSciBench does not evaluate Claude Science, and this source does not
  report benchmark numbers — but the two together frame a concrete,
  checkable question for future extraction: does Claude Science's
  reviewer-agent + persistent-kernel design measurably reduce the
  artifact-interpretation failure rate LifeSciBench documents industry-wide?

- **Extends**: `blog-anthropic-claude-managed-agents.md` (Claim 6 — "Multi-
  agent coordination...is available as a first-class platform feature").
  Claude Science's "generalist coordinating agent with access to over 60
  curated skills and connectors...these agents can spin up others and
  engage with specialist agents created by users" (launch announcement) is
  a domain-specific (life sciences) instance of the same multi-agent
  coordination capability that note documents at the platform level.

- **Novel**: The "skill vs. connector" decision rule (Claim 6) — no prior
  corpus source states this distinction as an explicit design principle
  ("Use a connector when the answer lives in the organization's own
  systems...and entitlements matter. Use a scientific data skill when
  the answer lives in the public record..."). The named background-reviewer
  architecture running by default every session (Claim 3) is more specific
  than any prior corpus description of AI-generated-content review — prior
  sources describe reviewer patterns as something practitioners build
  (see Extends above), not something the vendor ships turned-on-by-default.
  The three-metric pilot-phase measurement framework (cycle time /
  trust-without-rerun rate / cold-reproduce rate, Claim 9) is a novel,
  reusable pilot-evaluation framework not documented elsewhere in the
  corpus for any AI tool rollout.

- **Contradicts**: None found. The permission-philosophy difference
  against `blog-anthropic-claude-code-auto-mode.md` (noted under Extends
  above) is a conditioning variable, not a factual contradiction — both
  claims can be true simultaneously for their respective product contexts.
  No contradiction issue filed.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Domain-specific harness patterns**:
  Add Claude Science as a case study of a domain-scoped harness: ~150
  pre-configured skills organized by taxonomy (gene/variant, expression,
  oncology, pharmacology, etc.), an explicit skill-vs-connector decision
  rule (Claim 6), and skills that are individually open-source and
  inspectable (Claim 5). This is a concrete example of the "curated skill
  catalog" pattern the guide already discusses abstractly for Claude Code
  (`blog-anthropic-claude-code-skills-lessons.md`), applied at product
  scale for a single vertical. Recommend citing the skill-vs-connector
  decision rule verbatim as a reusable framework for any harness that mixes
  internal-system and public-reference-data sources.

- **Chapter 02 (Harness Engineering) — Reviewer-agent-as-default pattern**:
  The background reviewer (Claim 3, Claim 4) is architecturally novel
  relative to the guide's existing coverage of verification loops as
  opt-in practitioner-built skills (`blog-anthropic-claude-code-
  verification-loops-skills.md`). Recommend adding a note that some
  Anthropic products now ship a reviewer/critic agent turned on by default
  at the product level rather than leaving it to practitioner-built skills
  — a design choice teams building their own harnesses could consider
  adopting for high-stakes domains, alongside the existing "build a
  verification skill" guidance.

- **Chapter 04 (Context Engineering) — Provenance as first-class context**:
  The four-layer provenance model (description, code, conversation
  history, environment/package snapshot on every artifact) is a specific,
  reusable pattern for any harness producing artifacts a human must later
  audit or reproduce. Recommend citing alongside
  `blog-anthropic-carta-healthcare-context-engineering.md` Claim 8
  (human-in-the-loop transparency via shown evidence/rationale) as two
  independently-arrived-at instances of "make the reasoning and inputs
  inspectable, not just the output" for regulated or high-stakes domains.

- **Chapter 05 (Team Adoption) — Pilot measurement framework**: The
  three-phase roadmap's pilot metrics (cycle time, trust-without-rerun
  rate, cold-reproduce rate — Claim 9) are a reusable, domain-agnostic
  framework for measuring whether any AI-tool pilot is actually working,
  distinct from adoption-count vanity metrics. Recommend adding as a
  named framework in the team-adoption chapter, with the explicit caveat
  that this is vendor-prescribed guidance, not a measured outcome of any
  specific rollout in this source.

- **Chapter 05 (Team Adoption) — Caveat all vendor efficiency claims**: Any
  guide use of the Novo Nordisk (90% CSR time reduction), UCSF (10x
  speedup), or Allen Institute (2-years-to-10-reviews) figures (Claims 10,
  11) must carry the anecdotal/vendor-selected caveat forward explicitly —
  these are individually-attributed but Anthropic-curated testimonials,
  not independently reproduced results. The UCSF case's stated independent
  validation step is the one data point in this source with a meaningfully
  stronger evidentiary bar and could be called out as the exception.

- **Not recommended for the guide**: The regulated-data limitations (Claim
  8 — not HIPAA-ready, not NIST SP 800-171 assessed, not GxP-validated) are
  important as a caveat on adoption claims but do not by themselves
  motivate a new guide section; they should travel with any citation of
  Claude Science's reliability design (Claim 3) rather than standing alone.

## Extraction Notes

- Three sources were read in full: the claude.com/blog landing page (thin,
  ~600 words, mostly a table of contents for the eBook), the June 30, 2026
  launch announcement at anthropic.com/news (full text recovered via
  WebFetch, ~1,400 words, contains the customer case studies), and the
  25-page eBook PDF linked from the landing page. The eBook is the primary
  source for most claims in this note.
- The eBook PDF's text layer initially failed to extract via WebFetch
  (returned a refusal citing FlateDecode compression it could not
  decompress). `poppler-utils` (`pdftotext`) was installed via `apt-get`
  in the sandbox to extract the text layer directly. The eBook is a
  landscape two-column layout, and plain `pdftotext` (with or without
  `-layout`, which produce identical output here) interleaves the two
  columns line-by-line — so no quote reads as contiguous text in a naive
  extraction, and quotes must not be verified against one. Reading order
  was instead reconstructed from `pdftotext -bbox-layout` word
  coordinates, assigning each line to the left or right column by its
  x-extent and emitting columns in order. Every quote in this note was
  verified as a contiguous, unsplit passage in that reconstruction
  (eBook quotes) or in the launch-announcement text (case-study quotes).
- The Prospector's three triage comments on this issue disagree with each
  other on novelty (high / high / low) and on which chapters are most
  relevant; this note follows the majority framing (Ch01/Ch02/Ch04/Ch05
  relevance, domain-specific harness and adoption patterns as the primary
  contribution) and does not attempt to adjudicate between the three
  triage comments.
- Not followed as sub-pages (outside the 5-link budget and lower expected
  yield for this note's guide-relevant claims): the "Learn more in our
  getting started guide" and "Claude for life sciences solutions page"
  links referenced in the eBook's Resources chapter, and the "Read the
  paper" link (if any) associated with the product — none were located as
  distinct fetchable URLs separate from the two pages already extracted.
- No contradictions with existing corpus notes were identified; none
  filed.
