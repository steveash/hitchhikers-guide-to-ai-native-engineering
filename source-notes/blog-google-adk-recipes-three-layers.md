---
source_url: https://developers.googleblog.com/three-layers-one-repo-a-tour-of-googleadk-recipes/
source_type: blog-post
title: "Three layers, one repo: a tour of google/adk-recipes"
author: Pier Paolo Ippolito (Product Manager), Shahin Saadati (Software Engineer), Google Developers Blog
date_published: 2026-10-15
date_extracted: 2026-10-16
last_checked: 2026-10-16
status: current
confidence_overall: emerging
issue: "#4159"
---

# Three layers, one repo: a tour of google/adk-recipes

> Google describes a repository structured for coding-assistant consumption
> (core/ reference patterns, plugins/ installable skills with EVAL.yaml
> quality gates, contrib/ deployable services), but the post is a vendor
> tour with no measured outcomes: the concrete value is the layout and the
> gate mechanics, not evidence they work.

## Source Context

- **Type**: blog-post (vendor, Google Developers Blog, Oct 15, 2026)
- **Author credibility**: A product manager and an engineer on the ADK / Agent Platform team; first-party description of their own repo. The post closes with "Not an officially supported Google product. Recipes are for demonstration and as starting points, not production use."
- **Scope**: Repo layout, the Horizon long-horizon reference harness, the retail Plugin Recipe (Agent Plugins v1.0.0 packaging, `npx skills` install, EVAL.yaml gate), and the contrib/ deployable counterpart. It does not report eval results, pass rates, or adoption data. The Agents CLI / Agent Garden / Gemini Enterprise sections are product positioning and are only summarized. The linked repo and spec were not fetched; claims are from the post alone.

## Extracted Claims

### Claim 1: A repo can be organized into three top-level roots, each anchored on one reader action (reference pattern / installable skill / deployable service)
- **Evidence**: Description of google/adk-recipes: `core/` (reference patterns), `plugins/` (installable vertical skills), `contrib/` (end-to-end deployable services across five languages; twelve Python agents). Worked example per layer.
- **Confidence**: anecdotal
- **Quote**: "google/adk-recipes splits its content into three top-level folders: core/ for reference patterns curated by the Agents CLI and DevRel teams, plugins/ for installable vertical skills packaged as Plugin Recipes conforming to the Agent Plugins v1.0.0 spec, and contrib/ for end-to-end deployable services across five languages."
- **Our assessment**: A useful taxonomy for "agent-consumable example repos": pattern vs. one-shot installer vs. running service. No evidence given that assistants navigate it better than a flat repo.

### Claim 2: Repo artifacts are written primarily for the coding assistant, with READMEs left for humans
- **Evidence**: Stated design principle; every recipe ships `manifest.yaml`, `AGENTS.md`, and (for contrib/ and plugins/) a Dockerfile plus runnability test.
- **Confidence**: anecdotal
- **Quote**: "Every AGENTS.md, every manifest.yaml, every SKILL.md is written primarily for the AI coding assistant that will open the repo on your behalf; README.md files are what humans still read."
- **Our assessment**: A clear statement of an audience split (AGENTS.md/SKILL.md for agents, README for humans). Contrasts in emphasis with evidence that context files change efficiency rather than correctness (see Cross-References). Unmeasured here.

### Claim 3: CI enforces the agent-readability standards on every PR, and repo-resident skills prepare contributions
- **Evidence**: Description only; named skills include prepare-python-recipe, generate-manifest, github-pr-review.
- **Confidence**: anecdotal
- **Quote**: "CI enforces the standards on every PR, and a suite of coding-assistant skills in the repo (prepare-python-recipe, generate-manifest, github-pr-review, and others) does most of the preparation, so your agent can scaffold, validate, and submit a recipe end-to-end."
- **Our assessment**: The pattern (validate manifest in CI + ship skills that produce compliant contributions) is the replicable part. The post doesn't show the validator or rejection rates.

### Claim 4: Horizon packages the recurring hard parts of long-horizon agents into one reference harness
- **Evidence**: Lives at `core/python/long-horizon-harness`; uses Agent Platform Sandboxes, Memory Bank, and Sessions; `make dev-local` default uses local backend with in-memory sessions; `make deploy` to Cloud Run via Terraform.
- **Confidence**: anecdotal
- **Quote**: "The hard parts of such a long-horizon system are the same regardless of what the agent is being built to do: cross-session memory, per-user sandboxing of tool execution, secrets management, guardrails against runaway behaviour, and the orchestration primitives that make multi-step tasks resumable."
- **Our assessment**: A concise checklist of long-horizon harness primitives, useful as a Ch02 taxonomy. Largely GCP-coupled; implementation not shown.

### Claim 5: Horizon ships eighteen named behavioural eval rubrics, run with pytest
- **Evidence**: Evalsets in `tests/eval/evalsets/`; run via `uv run pytest tests/eval`. Categories listed; no scores.
- **Confidence**: anecdotal
- **Quote**: "Horizon's evaluation suite lives in tests/eval/evalsets/ as eighteen named behavioural rubrics covering memory recall, injection-based exfiltration attempts, guardrail halting under adversarial input, tool-selection discipline, and a journey-level plot-artifact evaluation."
- **Our assessment**: Good concrete list of what a harness-level behavioural suite should cover (memory, security, guardrails, tool selection, journey-level). Rubric contents and pass rates are not in the post; a Miner follow-up on the repo could extract them.

### Claim 6: Horizon is positioned as the thing coding assistants should "study before building something harder"
- **Evidence**: Assertion; Agents CLI is said to treat Horizon as a production template.
- **Confidence**: anecdotal
- **Quote**: "Horizon is the harness we give coding assistants to study before building something harder."
- **Our assessment**: Reference-implementation-as-scaffold is an interesting distribution strategy. Note the contradictory disclaimer that recipes are "not production use".

### Claim 7: A plugin is a bundle of skills with a plugin.json manifest; each skill is a self-contained folder including a conversational installer and quality gates
- **Evidence**: Layout diagram of `plugins/retail/` with `plugin.json`, `skills/<name>/{SKILL.md, README.md, EVAL.yaml, scripts/, references/, assets/}`.
- **Confidence**: emerging
- **Quote**: "Each skill is a self-contained folder with a SKILL.md conversational installer, a README.md, an EVAL.yaml of quality gates, and the scripts and assets the skill needs to do its work."
- **Our assessment**: Adds `EVAL.yaml` per skill as a convention on top of the base spec as described in the Copilot note (which describes only `plugin.json` + `SKILL.md`). Unclear from this post whether EVAL.yaml is part of the v1.0.0 spec or a Google convention; the post words it as the spec defining it. Verify against agent-plugins.org.

### Claim 8: A skill's EVAL.yaml mixes LLM-as-judge rubrics with deterministic assertions, with an 80% pass target that halts setup on failure
- **Evidence**: Layout comment and prose describing the retail-product-search setup flow; the demo shows setup logs but not the EVAL output.
- **Confidence**: anecdotal
- **Quote**: "If the rubric and assertion checks fall below the 80 percent passing target, the skill halts and surfaces the specific failures."
- **Our assessment**: The most reusable mechanism: an install-time acceptance test that gates the skill's own output and surfaces specific failures. The 80% threshold is unjustified, and the demo (5-product catalog) shows no gate firing. Layout comment: "# LLM-as-judge rubrics + deterministic assertions".

### Claim 9: SKILL.md can act as a conversational installer: a short interview (Q-MODE) writes a design spec, then a script executes the pipeline
- **Evidence**: Quick Start = two questions (GCP project ID, product data path); Full Setup adds two (product-fields level, region); writes `./design-spec.md`, runs `scripts/setup.py --config ./design-spec.md`, then EVAL.yaml. Transcript of setup run included.
- **Confidence**: anecdotal
- **Quote**: "Once installed, the coding assistant reads SKILL.md and initiates a Q-MODE interview."
- **Our assessment**: A concrete "interview → spec file → deterministic script → eval" skill shape that keeps the LLM out of the pipeline execution. Worth a Ch04 example of skills as installers rather than prompts.

### Claim 10: A single-agent design (one root agent, one tool) is deliberate because orchestration would obscure the pattern
- **Evidence**: Design rationale for retail-product-search; the ADK Web UI graph shows `product_search_agent → retrieve_docs`.
- **Confidence**: anecdotal
- **Quote**: "adding orchestration layers would obscure the pattern rather than clarify it."
- **Our assessment**: Reasonable, but it's justified as pedagogy for a reference recipe, not as a production recommendation. Complexity is placed "in the retrieval pipeline and the evaluator rubric". Don't over-generalize.

### Claim 11: Skills install across many assistants via the open `npx skills` CLI, symlinked from one canonical directory
- **Evidence**: Install transcript: lands in `~/.agents/skills/<skill-name>/`, symlinked into detected assistants; `--full-depth` needed to find nested `plugins/retail/skills/`; skills may instruct the host to pull companion skills from google/skills.
- **Confidence**: emerging
- **Quote**: "Done!  Review skills before use; they run with full agent permissions."
- **Our assessment**: The CLI's own warning is the most important line for supply-chain risk: installed skills have full agent permissions. Cross-assistant distribution is real (vercel-labs CLI), but the post is silent on vetting.

### Claim 12: Plugin and deployable agent are split: the plugin owns one-shot setup, the contrib agent owns the service shape
- **Evidence**: contrib/python/retail-product-search reads the collection created by the plugin's setup; README directs users to run `make -C plugins/retail/skills/product-search setup PROJECT_ID=your-project` first; deployable in five "personas" via boolean flags in `.env`.
- **Confidence**: anecdotal
- **Quote**: "The plugin owns the one-shot setup; the contrib agent owns the service shape."
- **Our assessment**: Notable: two artifacts "maintained by the same team to stay synchronised" is a drift risk the post acknowledges only implicitly.

## Concrete Artifacts

Plugin layout (source: post, "The retail Plugin Recipe"):

```
plugins/retail/
├── plugin.json
└── skills/
    ├── product-search/
    │   ├── SKILL.md       # Q-MODE conversational installer
    │   ├── README.md
    │   ├── EVAL.yaml      # LLM-as-judge rubrics + deterministic assertions
    │   ├── scripts/
    │   ├── references/
    │   └── assets/
    └── virtual-tryon/
        └── ...
```

Install commands (source: post):

```
npx skills add google/adk-recipes --skill retail-product-search --full-depth
npx skills add google/adk-recipes --skill retail-virtual-tryon --full-depth
```

Horizon quick start (source: post, abridged):

```
git clone --depth 1 --filter=blob:none --sparse https://github.com/google/adk-recipes.git
cd adk-recipes
git sparse-checkout set core/python/long-horizon-harness
cd core/python/long-horizon-harness
make dev-local
```

Eval run: `uv run pytest tests/eval`

## Cross-References

- **Corroborates**: `docs-github-copilot-agent-plugins-1-0.md` Claim 1 (Google joins Agent Plugins 1.0 as core maintainer) and Claim 8 (minimal plugin = `plugin.json` + `skills/<skill>/SKILL.md`): this post is Google's concrete use of the same format. `blog-latentspace-macmanus-wayfinder-skill.md` (skills as structured, multi-step workflows) is conceptually adjacent.
- **Contradicts**: None filed. Mild tension, not a contradiction: this post's premise that AGENTS.md/manifest files written for assistants make repos easier to use sits alongside `blog-addyosmani-audit-agent-files.md` Claim 6 (context files did not measurably change task correctness across 288 runs) and Claim 7 (context files help with operational facts only). The post offers no measurements, so it cannot be weighed against that evidence; the claims differ in what is measured.
- **Extends**: `docs-github-copilot-agent-plugins-1-0.md` by adding per-skill `EVAL.yaml` gates and the `npx skills` install path. `blog-google-adk-*` notes (e.g. `blog-google-adk-2-0-deterministic-workflows.md`) cover the framework, not this repo.
- **Novel**: Install-time EVAL.yaml gate with an 80% threshold; 18-rubric behavioural suite categories for a long-horizon harness; core/plugins/contrib layering; conversational-installer skill pattern; the explicit statement that AGENTS.md/SKILL.md/manifest.yaml are for assistants while README is for humans.

## Guide Impact

- **Chapter 04 (context engineering / skills)**: Add the interview → design-spec.md → script → EVAL gate pattern as a skill-as-installer example (Claims 8, 9), flagged as vendor-described and unmeasured.
- **Chapter 02 (harness)**: Use Claim 4's primitive list (cross-session memory, per-user sandboxing, secrets, guardrails, resumable orchestration) as an illustrative checklist for long-horizon harnesses.
- **Chapter 03 (verification)**: Cite Claim 5's rubric categories (memory recall, injection exfiltration, guardrail halting, tool-selection discipline) as an example of what a harness-level behavioural suite covers; cite Claim 8 for install-time gates that halt on failure.
- **Supply chain / security discussion**: Quote the `npx skills` warning (Claim 11) as evidence that cross-assistant skill installers run with full permissions.

## Extraction Notes

- Read the full post (fetched raw HTML, stripped to text). Images, the layer table, and some code-block outputs (first chat turn, retrieval screenshots) are not in the text. The "Published" date was unknown in the issue; the post shows Oct. 15, 2026.
- The repo, handbook, and spec were not fetched, so EVAL.yaml schema, rubric contents, and CI validators remain unverified; a follow-up could mine them.
- Skipped as marketing: Agents CLI, Agent Garden, and Gemini Enterprise positioning, and the virtual-tryon demo.
- No contradiction issue filed: the tension noted above is not a direct conflict on the same measured claim.
