---
source_url: https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/
source_type: blog-post
title: "Open Source AI Gap Map"
author: Simon Willison (linking to Current AI, a non-profit; primary quoted material from Ayah Bdeir / Current AI)
date_published: 2026-07-03
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: emerging
issue: "#1647"
---

# Open Source AI Gap Map

> Simon Willison's four-paragraph link post points at Current AI's newly
> launched "Gap Map" — a scored, citation-backed index of 421 open source AI
> products across a 3-layer/14-category taxonomy descended from the 2024
> Columbia Convening on Openness in AI — and at its MIT-licensed underlying
> dataset (1,184 YAML files on GitHub). Following the linked Current AI launch
> post and the GitHub repository itself surfaces a rigorous, sourced
> three-axis scoring methodology (openness / adoption / capability) and,
> unexpectedly, a second story: the dataset repo is itself built as an
> agent-collaborative open source project, with an `AGENTS.md`, four
> contributor-facing "skills," and a CI-enforced editor/maintainer permission
> boundary around bot-regenerated derived files — a real-world instance of
> exactly the pattern this guide's own source-note pipeline uses.

## Source Context

- **Type**: blog-post (Simon Willison's link-blog, ~140 words of original
  commentary across four short paragraphs; auto-discovered via trusted feed
  `simon-willison`). Per MINER.md §1, this note follows the two substantive
  linked pages the post points at: Current AI's own launch post
  (`currentai.org/blogs/introducing-the-gap-map-v0-1`) and the GitHub data
  repository (`github.com/currentai-org/os-ai-map`), including its README,
  `AGENTS.md`, `sources/taxonomy.yaml`, and `docs/methodology.md`.
- **Author credibility**: Simon Willison is a designated `trusted-feed` source
  in this repo (creator of Django, Datasette, `sqlite-utils`, `llm`). For this
  post he is a curator/pointer, not a primary source — the substantive claims
  originate from Current AI (a non-profit "global partnership building a
  public option for AI," founded at the AI Action Summit in Paris, February
  2025, backed by "$400m already committed" per Willison's post) and from the
  GitHub repository's own documentation. Current AI's launch post is
  bylined to Ayah Bdeir, a named contributor, under the organization's own
  blog.
- **Scope**: Covers the Gap Map's headline product-count statistics, its
  discovery/scoring methodology, its openness/adoption/capability axes, its
  category-maturity-stage and gap taxonomy, two named "early findings," and
  the structure of the underlying data repository (including its
  agent/skills-oriented contribution model). Does NOT cover the map's visual
  UI/UX (`map.currentai.org` itself was not rendered or interacted with — only
  its data and documentation were read), does not independently verify any
  individual product's score, and does not cover the companion notebooks
  (`pypi-geo-trends.py`, `oss-ai-trends.py`, `long-tail-explorer.py`) beyond
  the one-line descriptions in the README.

## Extracted Claims

### Claim 1: The Gap Map v0.1 scores 421 products in depth (266 software tools/libraries, 85 models, 50 datasets, 20 hardware projects) from 228 organizations, leaving a much larger uncategorized long tail unscored
- **Evidence**: Identical statistic appears in three independent places read for this note: Simon Willison's blockquote (sourced from Current AI), Current AI's own launch post, and the GitHub repo's `docs/methodology.md` template prose (as `{total}`/`{scored}` placeholders resolving to the same figures at build time).
- **Confidence**: settled (a specific, repeatedly-stated, citation-backed count from the primary organization, corroborated verbatim across the announcement, the launch post, and the repo's own methodology doc)
- **Quote**: "The Gap Map v0.1 details 421 products in depth: 266 software tools and libraries, 85 models, 50 datasets, and 20 hardware projects, produced by 228 organizations. These products are organized into 14 categories across 3 layers of the stack (model components, product / UX, and infrastructure). The remaining 24,400 artifacts constitute the uncategorized long tail of the open source AI ecosystem, and will carry no score until they are researched and cited."
- **Our assessment**: The scored set (421) is a curated 1.7% slice of everything discovered (421 of ~24,626 candidates, per Claim 3) — the methodology doc is explicit that this is "a curated sample of the most prominent products, not a census." Practitioners should read Gap Map coverage as "the ecosystem's prominent, well-documented tip," not as an exhaustive catalog; the 24,400-item long tail is real but deliberately left unscored.

### Claim 2: The underlying dataset is released under an MIT license as 1,184 curated YAML files on GitHub, and the project separately tracks 16,185 GitHub repositories explorable via Datasette Lite
- **Evidence**: Direct statement in Willison's own commentary (not a blockquote), naming the specific file count, license, and a working Datasette Lite URL loading a CSV of tracked repos.
- **Confidence**: settled (specific, independently-checkable counts; the repository was fetched directly for this note and confirmed to exist with an MIT `LICENSE` file)
- **Quote**: "The map itself is interesting to explore, but I'm more excited about the underlying data - released under an MIT license in the currentai-org/os-ai-map GitHub account: 1,184 YAML files plus the notebooks, schemas and other scripts used to help gather them."
- **Our assessment**: This is the practically useful takeaway for practitioners over the map's UI itself: a machine-readable, MIT-licensed, per-record YAML dataset (one file per organization/category/product/score, per Claim 9) that can be queried, diffed, or re-purposed directly, rather than only viewed through Current AI's own visualization.

### Claim 3: Current AI's discovery step surveyed roughly 24,626 candidate projects, seeded from Chip Huyen's "Good AI List" and broadened via the Hugging Face Hub, the Open LLM Leaderboard, the AI Incident Database, and package-registry/SBOM data
- **Evidence**: Stated directly in both Current AI's launch post and the GitHub repo's `docs/methodology.md`, which names the specific seed source and expansion sources.
- **Confidence**: emerging (the pipeline and seed sources are specific and named, but the discovery methodology itself — how candidates are ranked and cut off before scoring — is Current AI's own editorial process, not independently audited)
- **Quote**: "The discovery step draws on large-scale open data from the software supply chain compiled by Open Source Observer. We seeded it from Chip Huyen's Good AI List, a catalog of AI-focused repositories, then broadened it through analysis of the Hugging Face Hub, the Open LLM Leaderboard, the AI Incident Database, package registries and SBOMs, and academic and industry publications."
- **Our assessment**: Naming a specific, checkable seed corpus (Good AI List) and expansion sources gives the discovery step more provenance than a typical "we crawled the internet" landscape survey. It's still a curated, ranked-by-adoption-signal process ("we ranked the candidates by adoption signal ... and enriched the most prominent first"), so the map systematically under-represents low-adoption/low-visibility projects even within its already-narrow scored set.

### Claim 4: Each product is graded on three independent axes — openness (0–5 against the Model Openness Framework / OSI license classes), adoption (real usage, not GitHub stars), and capability (benchmarks or feature coverage) — and every non-null score value requires a primary-source citation
- **Evidence**: Stated in both the GitHub README's "How scoring works" section and `docs/methodology.md`'s "The three axes" section, with axis definitions matching across both documents.
- **Confidence**: settled (a specific, documented, and cross-corroborated rubric, not a vague description)
- **Quote**: "Openness — a 0–5 grade against openness frameworks (the Model Openness Framework for models, OSI license classes for software), not a yes/no. The open-source vs. open-weights distinction is the one the map exists to draw. Adoption — real usage (downloads, active users, deployments), not GitHub stars. Capability — community benchmarks where they exist, feature coverage where they don't."
- **Our assessment**: This three-axis split (openness / adoption / capability) is directly reusable by a practitioner evaluating *any* open source AI tool, not just ones already on the map — it's a decision rubric independent of the map's specific dataset. The explicit "GitHub stars are treated as a weak last-resort signal and never raise a product above level 3" rule (from `docs/methodology.md`) is a concrete, actionable anti-pattern warning: don't let stars stand in for usage evidence when evaluating a dependency.

### Claim 5: Category "maturity stage" (0 Void to 5 Mature) is computed only from fully-open products — open-weights models never advance a category's stage no matter how capable or adopted they are
- **Evidence**: Directly stated and justified in `docs/methodology.md`'s "Maturity stages" section, including a stated sensitivity analysis of what would change if open-weights products were credited instead.
- **Confidence**: settled (an explicit, documented scoring rule with a stated rationale and a stated counterfactual)
- **Quote**: "Only fully open products advance a category's stage. Open-ish products (open weights, source-available, and the like) are used solely to detect the openness gap below; crediting them would blur the line between open source and open weights that the map exists to draw. The choice is consequential but bounded: counting open-weights models as open would move only three categories, all in the model layer — base/pretrained models (Stage 3→5), fine-tuned/chat models (2→3), and edge hardware (3→4) — and would leave every infrastructure and tooling verdict unchanged."
- **Our assessment**: This is a deliberate, disclosed methodological choice, not an oversight — and Current AI quantifies its own blast radius (3 of the map's categories, all model-layer). This level of self-auditing (stating exactly which verdicts would flip under a different rule) is more rigorous than most landscape surveys we've extracted, and it directly operationalizes the "open-weights is not open-source" distinction practitioners often gloss over when picking a "open" model for licensing or dependency-risk reasons.

### Claim 6: A category can carry a "disclosure" gap even at Stage 5 maturity — flagging that the closed frontier's own equivalent (proprietary training data, exact recipe) is undisclosed, which is a fundamentally different signal from the open ecosystem being immature or under-adopted
- **Evidence**: Defined in `docs/methodology.md`'s "Gaps" section as one of six gap types (void, capability, adoption, maturity, openness, disclosure), stated to be curator-asserted per category rather than inferred from scores, so it doesn't silently change on a routine curation update.
- **Confidence**: emerging (a well-specified concept, but it is hand-flagged by Current AI's own curators rather than computed from a metric, so it is closer to editorial judgment than the other five gap types)
- **Quote**: "Disclosure: the open products are real and widely used, but the closed frontier's own equivalent is undisclosed — labs publish neither their proprietary and licensed data nor their exact recipe. Training data is the clear case: the open corpora are shared (frontier models draw on the same web substrate, and some open corpora were built by the labs themselves), but the proprietary additions and the mixing recipe stay invisible, and that asymmetry is the finding worth surfacing rather than a maturity or adoption shortfall."
- **Our assessment**: This is a genuinely novel framing for this corpus: a landscape-mapping methodology that explicitly separates "the open thing is weak" from "the closed thing is opaque, and that opacity is itself the finding." It gives practitioners language for a specific kind of ecosystem risk (frontier labs' own inputs are unauditable) that is distinct from the usual "open vs. closed capability gap" framing.

### Claim 7: Current AI's own early reading of the data is that entire capability categories — orchestration agents among them — were pioneered by the open source ecosystem first, not by frontier labs
- **Evidence**: Stated as one of three named "early insights" in Current AI's launch post, without a supporting citation list in the post itself (the underlying per-category score files presumably back this, but the launch post does not cite specific products or dates for the claim).
- **Confidence**: anecdotal (an unsupported editorial claim in a launch/marketing post from the organization that built the map — directionally plausible given well-known early open source agent-orchestration projects, but not accompanied by named examples or dates in the source read for this note)
- **Quote**: "Open source isn't chasing the frontier. Entire capability categories (orchestration agents among them) were first developed in the open source ecosystem, not by frontier labs. The open source AI economy is actually out-innovating the closed one."
- **Our assessment**: This is a strong, quotable claim that would materially support this guide's framing of "agentic orchestration as an open, practitioner-driven space rather than a vendor-controlled one" — but as extracted it is asserted, not evidenced, in the launch post. Treat as a hypothesis worth checking against the actual scored `orchestration_agents` category data (in `sources/categories/` and `sources/scores/` in the repo) before citing at higher than `anecdotal` confidence in the guide.

### Claim 8: Current AI frames "health" and "resilience" as distinct axes using the inference-code category as an example — vLLM, llama.cpp, and SGLang are mature, well-adopted, and genuinely open, but there are only a handful of them, which the post explicitly names as a "bus factor" risk for the whole inference layer
- **Evidence**: Stated as a named early insight in Current AI's launch post, using three specific, named, well-known open source inference projects as the illustrating example.
- **Confidence**: emerging (the named projects and the underlying logic are independently verifiable and plausible, but the framing itself — that this constitutes a structural vulnerability "public investment is positioned to close" — is Current AI's own editorial interpretation, consistent with its role as a funder)
- **Quote**: "Health and resilience aren't the same thing. Take inference code, for example. vLLM, llama.cpp, and SGLang are mature, well-adopted, and genuinely open. But there are only a handful of them. Capable, yes. Redundant, not yet. Engineers call this the bus factor: the whole inference layer depends on a handful of projects staying good. This is a common structural vulnerability we see across the stack that public investment is positioned to close."
- **Our assessment**: This maps directly onto the map's own "maturity gap" definition (Claim 6's sibling gap type: "open options exist, and at least one may be mature, but the ecosystem lacks the depth and redundancy of a mature one"). It's a concrete, named illustration — useful for this guide's dependency-risk framing — that "does a mature open source option exist" and "is that layer redundant/bus-factor-safe" are two different questions a team should ask when choosing an inference stack, not one.

### Claim 9: The Gap Map's taxonomy organizes categories into three "arcs" that are the three layers of the 2024 Columbia Convening's openness ontology (model components, product/UX, infrastructure), with each arc's category list and display order defined in a single machine-readable manifest file
- **Evidence**: Directly read from `sources/taxonomy.yaml` in the GitHub repository (fetched 2026-07-08), which enumerates, under `arcs:`, "Model components" (7 categories: `base_pretrained`, `finetuned_chat`, `inference_code`, `finetuning_code`, `evaluation_code`, `benchmark_eval_data`, `training_synthetic_datasets`), "Product / UX" (5 categories: `orchestration_agents`, `ui_api`, `telemetry_observability`, `safeguards`, `agent_tools_protocols`), and "Infrastructure" (3 categories: `ml_frameworks`, `deployment`, `edge_hardware`).
- **Confidence**: settled (read directly from the machine-readable source file, not a secondary description)
- **Quote**: "Arcs are the three layers of the Columbia openness ontology (GPAIS tech stack): Product / UX (above), Model components (middle), Infrastructure (below). Each arc declares its Columbia `layer` slug; serialize derives both the display arc name and the machine layer slug from here, so a category's layer is never a separate hand-maintained field -- it is whichever arc the category sits in." (comment header, `sources/taxonomy.yaml`)
- **Our assessment**: This taxonomy — three stack layers, each broken into a handful of named categories (agent orchestration and tooling/protocols sit in "Product/UX"; base models, fine-tuning, evaluation, and training data sit in "Model components"; frameworks, deployment, and edge hardware sit in "Infrastructure") — is a reusable organizing frame for any "what's out there" discussion of the open source AI stack, independent of the specific scores. Note a live-data discrepancy: the taxonomy file (fetched 2026-07-08) enumerates 15 category slugs total (7+5+3), while every narrative source (Willison's blockquote, Current AI's launch post, and the methodology doc's own templated prose) states "14 categories" — see Extraction Notes.

### Claim 10: The dataset repository is itself built for AI-agent-assisted contribution — it ships an `AGENTS.md`, four named contributor "skills" that scaffold and validate common edits, and a CI-enforced boundary that keeps editors from touching build-generated files or the write-privileged data warehouse
- **Evidence**: Directly read from the repository's `AGENTS.md` and README (fetched 2026-07-08). `AGENTS.md` names four skills (`curate-category`, `add-product`, `add-data-source`, `pyoso-analyst`) and states an explicit editor/maintainer permission split; the README states that two specific generated files are bot-regenerated on merge and that CI blocks PRs which hand-edit them.
- **Confidence**: settled (read directly from the repository's own governance documentation, not inferred)
- **Quote**: "Editors (curators, analysts) work only in `sources/`, `docs/`, and `notebooks/`. They open PRs. They do not: Run MCP tools. Upload or revise UDMs or static models. Push to main directly." (`AGENTS.md`)
- **Quote (generated-file boundary)**: "Don't hand-edit generated files. `build/notebook_data.json` and `notebooks/ai-stack-map.py` are regenerated by a bot on merge; PRs that touch them are blocked." (README)
- **Quote (citation requirement)**: "Every score cites a primary source. The map excludes anything it can't verify against one." (README)
- **Our assessment**: This is the most directly relevant finding for this guide's own operating model, and it is not something the Prospector's triage comments anticipated. `os-ai-map` independently arrived at the same three structural choices this repository's Miner/Assayer/Smith pipeline uses: (1) a derived artifact (`build/notebook_data.json`, analogous to this repo's `registry/sources.json`) that contributors must never hand-edit and that a bot regenerates after merge specifically to avoid the parallel-PR merge-conflict problem this guide's own Miner instructions call out explicitly; (2) named "skills" that scaffold a specific contribution type (`add-product` mirrors this repo's per-source-type note templates); (3) a hard read/write boundary between content contributors and infrastructure maintainers, enforced by CI rather than by policy alone. This is independent, real-world corroboration — from an unrelated domain (AI ecosystem cataloging) — that this exact pattern (bot-owned derived index + blocked hand-edits + skill-scaffolded contribution + CI-enforced boundary) is a generalizable answer to "how do you let many parallel AI-assisted contributors edit a shared curated dataset without merge conflicts or privilege creep," not an idiosyncratic choice specific to this guide's own tooling.

## Concrete Artifacts

### Taxonomy manifest (verbatim, `sources/taxonomy.yaml`, fetched 2026-07-08)

```yaml
# Arcs are the three layers of the Columbia openness ontology (GPAIS tech stack):
# Product / UX (above), Model components (middle), Infrastructure (below).
# Each arc declares its Columbia `layer` slug; serialize derives both the display
# arc name and the machine layer slug from here, so a category's layer is never a
# separate hand-maintained field -- it is whichever arc the category sits in.
arcs:
- name: Model components
  layer: model_components
  categories:
  - base_pretrained
  - finetuned_chat
  - inference_code
  - finetuning_code
  - evaluation_code
  - benchmark_eval_data
  - training_synthetic_datasets
- name: Product / UX
  layer: product_ux
  categories:
  - orchestration_agents
  - ui_api
  - telemetry_observability
  - safeguards
  - agent_tools_protocols
- name: Infrastructure
  layer: infrastructure
  categories:
  - ml_frameworks
  - deployment
  - edge_hardware
```

### Repository editor-skills table (verbatim, `AGENTS.md`, fetched 2026-07-08)

```
| Skill | When to use |
|-------|------------|
| `curate-category` | Edit category definition, weights, litmus, or product roster |
| `add-product` | Add a new product (scaffolds product + score YAML, updates roster) |
| `add-data-source` | Register a new external data source and add a fetcher |
| `pyoso-analyst` | Query `currentai.*` tables via `pyoso` (read-only analysis) |
```

### Maturity stage ladder (verbatim, `docs/methodology.md`)

```
Stage 5: Mature Open Ecosystem. Four or more mature fully open products:
  redundant and resilient.
Stage 4: Competitive Open Ecosystem. At least one mature fully open product,
  but fewer than four.
Stage 3: Viable Alternatives. No mature fully open product, but the best
  fully open option is strong.
Stage 2: Emerging Alternatives. No mature fully open product; the best fully
  open option is promising but limited.
Stage 1: Open Experiments. Fully open options exist but are weak on both
  axes.
Stage 0: Void. No usable open option exists.
```

### Source data scale (from Simon Willison's post and the repository)

```
421 products scored in depth: 266 software tools/libraries, 85 models,
  50 datasets, 20 hardware projects
228 organizations
24,400 uncategorized long-tail artifacts (unscored)
~24,626 total candidate projects surveyed at discovery
1,184 YAML files (MIT licensed), one per organization/category/product/score record
16,185 GitHub repos tracked, explorable via Datasette Lite
```

## Cross-References

- **Corroborates**: No existing source note in this corpus directly overlaps
  with a comprehensive open source AI landscape/taxonomy map; this is treated
  as a new category of source per the Prospector's triage ("Existing notes
  that overlap: None"). At a pattern level, the bot-regenerated-derived-file +
  blocked-hand-edit convention (Claim 10) is the same convention this guide's
  own `registry/sources.json` rebuild (`scripts/build_registry.py`, run via
  `registry-rebuild.yml` after merge, per this Miner's own task
  instructions) already uses — that is process corroboration from outside
  this corpus's source notes, not a citation of another note.
- **Contradicts**: None identified against existing source notes. (One
  internal, source-vs-itself inconsistency was found — see Claim 9's "14 vs.
  15 categories" discrepancy — but this is a live-data/announcement-copy drift
  within the same source, not a disagreement between two sources on a claim
  that would change guide advice, so no contradiction issue was filed per
  MINER.md §4a's "when NOT to file" guidance.)
- **Extends**: `paper-gloaguen-agentsmd-effectiveness.md` (evaluates whether
  `AGENTS.md` files help coding agents complete tasks) touches the same file
  convention as Claim 10 here, but from a completely different angle — that
  note is about whether an individual agent performs better with an
  `AGENTS.md` present; this note is about `AGENTS.md` as one piece of a
  larger *multi-contributor governance* structure (skills + CI boundary +
  bot-owned derived files) for a dataset that many humans and agents edit in
  parallel. Worth linking the two in the guide as "AGENTS.md for a single
  agent's task performance" vs. "AGENTS.md as part of a repo's contribution
  architecture."
- **Novel**: The three-axis (openness/adoption/capability) scoring rubric
  with per-axis anti-gaming rules (Claim 4); the maturity-stage ladder that
  only credits fully-open products (Claim 5); the "disclosure" gap type
  naming frontier-lab opacity as a distinct, quotable finding (Claim 6); and
  the repository's own agent-collaborative governance structure (Claim 10)
  are all new to this corpus.

## Guide Impact

- **`guide/02-harness-engineering.md` ("Agent Boundaries" / "The Enforcement
  Hierarchy" / "The Three-Tier Boundary System" sections)**: Add the
  `os-ai-map` repository (Claim 10) as a named, independent real-world example
  of the same editor/maintainer permission split and bot-owned-derived-file
  pattern this guide documents in the abstract — concrete evidence that the
  pattern generalizes beyond this guide's own tooling to an unrelated
  AI-ecosystem-cataloging project with its own `AGENTS.md` and named
  contributor skills.
- **`guide/02-harness-engineering.md` or `guide/00-principles.md` (tool /
  dependency selection)**: There is no dedicated "landscape" or "tool
  selection" chapter yet (the Prospector's triage comments referenced
  "Ch03 tool selection" / "Ch05 landscape," which do not correspond to
  current chapter files — the closest existing homes are
  `02-harness-engineering.md`'s "Stack" sections or `00-principles.md`'s
  decision-framework material). If/when such guidance is added, cite the
  three-axis openness/adoption/capability rubric (Claim 4) as a reusable
  evaluation checklist for choosing any open source AI dependency, and the
  "bus factor" framing (Claim 8, naming vLLM/llama.cpp/SGLang as capable but
  under-redundant) as a concrete illustration that "does a mature open option
  exist" and "is this layer redundant" are separate questions.
- **`guide/00-principles.md`**: The open-source-vs-open-weights distinction
  and its stated, quantified scoring consequences (Claim 5) is a sharper,
  more citable version of a distinction practitioners often blur when
  describing a model as "open" for licensing or governance purposes.

## Extraction Notes

- **Verbatim text obtained directly via `curl`, not AI summarization**: A
  first attempt to fetch the Simon Willison post via an AI-summarizing fetch
  tool returned only a paraphrased summary, not source text suitable for
  quote extraction (flagged per MINER.md §2a). All quotes in this note were
  instead obtained by fetching the raw HTML directly (`curl`) for
  `simonwillison.net`, `currentai.org`, and `github.com/currentai-org/os-ai-map`,
  and reading `docs/methodology.md`, `AGENTS.md`, and `sources/taxonomy.yaml`
  as raw files via `raw.githubusercontent.com`. All quotes were copied
  character-for-character from that fetched raw text.
- **Linked pages followed (3, within MINER.md §1's up-to-5 budget)**: Current
  AI's launch blog post, the `os-ai-map` GitHub repository README, and three
  files within that repository (`AGENTS.md`, `sources/taxonomy.yaml`,
  `docs/methodology.md`). The map's own interactive UI at
  `map.currentai.org` and the companion marimo notebooks were not rendered or
  interacted with — only referenced via the documentation that describes
  them.
- **14 vs. 15 categories discrepancy (see Claim 9)**: Every narrative
  description of the map (Willison's blockquote, Current AI's launch post,
  and `docs/methodology.md`'s own templated summary prose) states "14
  categories." The machine-readable `sources/taxonomy.yaml`, fetched directly
  on 2026-07-08 — five days after the map's July 1 publish date — enumerates
  15 category slugs (7 + 5 + 3 across the three arcs). Since the repository
  explicitly describes itself as "a public, iterative effort" with community
  PRs adding categories and products, the most likely explanation is that a
  category was added to the live taxonomy between publication and this note's
  extraction date, rather than a citation error in this note or in the
  original sources. This is flagged rather than silently reconciled; it is
  not treated as a contradiction requiring an issue per MINER.md §4a, since
  it is drift in the same live source over time, not a disagreement between
  two sources.
- **Claim 7 (open source pioneering orchestration agents) could not be
  independently verified** against the repository's actual per-category score
  files within this note's scope — the claim is sourced only to Current AI's
  own launch-post prose, not to a specific cited product or date. Flagged at
  `anecdotal` confidence accordingly; a follow-up source note or direct query
  of `sources/categories/orchestration_agents.yaml` and its constituent
  product scores would be needed to raise this above `anecdotal`.
- **No contradiction issue filed**: see Cross-References → Contradicts above.
- **Overall confidence set to `emerging`**: Claims 1, 2, 4, 5, 9, and 10 are
  `settled` (directly read from primary machine-readable sources or
  cross-corroborated verbatim across multiple documents from the same
  organization). Claims 3, 6, and 8 are `emerging` (specific and plausible,
  but resting on Current AI's own editorial framing without independent
  audit). Claim 7 is `anecdotal`. The note-level confidence reflects this
  mixed bag: strong on the map's own documented mechanics, weaker on its
  narrative "early findings."
