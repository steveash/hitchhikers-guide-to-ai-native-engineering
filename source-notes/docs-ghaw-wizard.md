---
source_url: https://github.github.com/gh-aw/wizard
source_type: docs
title: "GitHub Agentic Workflows: Workflow Generator Wizard"
author: GitHub Agentic Workflows team / GitHub Next (repo githubnext/gh-aw-wizard)
date_published: null
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: emerging
issue: "#2786"
---

# GitHub Agentic Workflows: Workflow Generator Wizard

> An interactive, free-text-driven workflow generator that pattern-matches a
> user's description against 19 empirically-profiled workflow archetypes
> (each carrying a real-world success rate, corpus count, and named
> anti-patterns) mined from 518 repositories / 819 gh-aw workflows, and
> surfaces research findings (DO NOT constraints, bimodal success, trigger
> risk) that go well beyond what the reference docs currently state.

## Source Context

- **Type**: docs (interactive tool + its open-source client code)
- **Author credibility**: Published under `github.github.com/gh-aw/` (the
  official gh-aw docs domain) and redirects to
  `githubnext.github.io/gh-aw-wizard/`, whose source lives in
  `githubnext/gh-aw-wizard` — a public repo owned by the `githubnext`
  GitHub organization (GitHub Next), MIT-licensed, created 2026-08-18. This
  is first-party tooling from the same team that ships gh-aw itself.
- **Scope**: A 5-step client-side wizard (What → When → Where → Extras →
  Agent) that generates either a downloadable gh-aw workflow `.md` file or a
  copy-pasteable natural-language prompt. It does **not** cover workflow
  *editing*, frontmatter syntax, or engine internals — those are covered by
  other `docs-ghaw-*` notes already in the corpus. Its unique contribution
  is the archetype pattern library (`patterns/archetypes/*.json` and
  `patterns/manifest.json`) bundled into the wizard's source, which encodes
  empirical usage-outcome data not published elsewhere in the docs site.

## Extracted Claims

### Claim 1: The wizard's "What" step is a free-text description field, not a fixed set of named template buttons — the archetype selection happens by pattern-matching that text server/client-side against a 19-entry archetype library
- **Evidence**: Two independent live-page extractions of `githubnext.github.io/gh-aw-wizard/` (2026-08-19) both describe Step 1 as a text input ("Describe what you want the workflow to do") rather than a bank of template buttons. This is corroborated by the wizard's own source: `patterns.js` loads `patterns/manifest.json` (which lists 19 archetype ids) and each `patterns/archetypes/<id>.json` file, then `getRecommendedConfiguration()` looks up an archetype by id to pre-fill the trigger/output/tool choices for the rest of the flow.
- **Confidence**: settled (verified directly against the shipped JavaScript source, not just the rendered page)
- **Quote**: "The pattern library is split into one file per archetype so it can be versioned and reviewed independently: `patterns/manifest.json` lists the archetype ids plus every other field, and `patterns/archetypes/<id>.json` holds each archetype's data." (`src/js/patterns.js`, file-header comment)
- **Our assessment**: This directly corrects the Prospector triage comments on this issue (three separate comments, each asserting the wizard exposes "13", "14", or "15" clickable named archetype templates as the first-step UI). None of the three counts match what the live page or the source code shows — the UI-visible first step is unstructured text entry, and the archetype library underneath has 19 entries (18 named archetypes + "Custom"), not 13–15. The triage comments appear to have guessed at archetype counts/names without reading the actual page or source; see Extraction Notes.

### Claim 2: The archetype library defines 19 workflow types (18 named archetypes plus "Custom"), each carrying an empirically-measured success rate and corpus count where data exists
- **Evidence**: `patterns/manifest.json` → `archetypes` array lists exactly: custom, accessibility-expert, performance-nut, user-simulator, daily-test-improver, repo-maintainer, linter-workflows, linter-miner, linter-refiner, linter-applier, skill-pr-reviewer, issue-triage, code-improvement, pr-review, status-report, dependency-monitor, documentation-updater, content-moderation, security-scanner. Each has its own `patterns/archetypes/<id>.json` with `success_rate`, `count`, `top_repos`, `tips`, and `anti_patterns` fields.
- **Confidence**: settled (verbatim JSON, primary source)
- **Quote**: `"archetypes": ["custom", "accessibility-expert", "performance-nut", "user-simulator", "daily-test-improver", "repo-maintainer", "linter-workflows", "linter-miner", "linter-refiner", "linter-applier", "skill-pr-reviewer", "issue-triage", "code-improvement", "pr-review", "status-report", "dependency-monitor", "documentation-updater", "content-moderation", "security-scanner"]` (`patterns/manifest.json`)
- **Our assessment**: This is a materially richer taxonomy than any of the three Prospector triage comments captured — none mentioned `accessibility-expert`, `performance-nut`, `security-scanner`, `user-simulator`, or the `linter-workflows` grouping archetype, and none mentioned that per-archetype success-rate/anti-pattern data exists at all. This is the highest-value content in the source and was effectively invisible to the triage pass.

### Claim 3: Measured archetype success rates vary by roughly 2x across archetypes with sufficient corpus data — from 0.37 (Code Improvement, n=76) up to 0.73 (Content Moderation, n=6) — and several archetypes have no measured rate at all (small or zero corpus)
- **Evidence**: `code-improvement.json`: `"success_rate": 0.37, "count": 76`. `content-moderation.json`: `"success_rate": 0.73, "count": 6`. `pr-review.json`: `"success_rate": 0.45, "count": 74`. `issue-triage.json`: `"success_rate": 0.65, "count": 98`. `dependency-monitor.json`: `"success_rate": 0.5, "count": 55`. `documentation-updater.json`: `"success_rate": 0.6, "count": 25`. `status-report.json`: `"success_rate": 0.52, "count": 69`. `custom.json`: `"success_rate": 0.49, "count": 416`. Nine archetypes (`accessibility-expert`, `daily-test-improver`, `linter-applier`, `linter-miner`, `linter-refiner`, `linter-workflows`, `performance-nut`, `repo-maintainer`, `security-scanner`, `skill-pr-reviewer`, `user-simulator`) report `"success_rate": null, "count": 0`.
- **Confidence**: emerging (real measured data, but the methodology behind "success" and how the corpus of 518 repos was selected is not documented on the page)
- **Quote**: `"success_rate": 0.37,\n  "count": 76` (`patterns/archetypes/code-improvement.json`)
- **Our assessment**: The 0.73 vs 0.37 spread is a genuinely actionable signal — "Code Improvement" workflows (generic fix/CI-doctor style) are measurably less reliable than "Content Moderation" workflows, and the archetype's own tips explain *why* for Code Improvement specifically (see Claim 4). The archetypes with `count: 0` (roughly half the library) are essentially untested in the wild — the wizard still recommends them, but with no empirical backing, which is a caveat worth carrying into the guide.

### Claim 4: Each measured archetype ships explicit named anti-patterns — real-world workflow-file naming conventions the manifest associates with low success — and instructs users to avoid cloning them
- **Evidence**: `code-improvement.json` → `"tips": [..., "Avoid pr-fix and ci-doctor templates — both have <20% success in practice"], "anti_patterns": ["ci-doctor", "ci-doctor", "autofix-ci", "code-simplifier", "pr-fix"]`. `content-moderation.json` → `"tips": ["Never auto-close or lock — label and comment only", ...], "anti_patterns": ["ai-moderator"]`. The top-level `manifest.json` → `anti_patterns` array cross-references 20 specific named workflows (e.g. `documentation-audit`, `data-plane-api-review`, `mgmt-review`) each annotated with `"success_rate": 0.0`, `"repos_seen": 1`, and a `reason` string naming the exact repo where it failed (e.g. `"Very low success rate in Alvin-Wu-Garden/COBOL2SPEC"`).
- **Confidence**: emerging (n=1 repo for each named anti-pattern in the top-level list — individually weak evidence, but the pattern recurs across many independently-observed repos)
- **Quote**: "Avoid pr-fix and ci-doctor templates — both have <20% success in practice" (`patterns/archetypes/code-improvement.json`, `tips`)
- **Our assessment**: This is unusually concrete for a docs source — most gh-aw reference material documents *how* to configure a trigger or tool, not *which specific community workflow names tend to fail and why*. Worth flagging that several anti-pattern names are drive-by (n=1, `success_rate: 0.0` from a single repo) and shouldn't be read as a rigorous indictment of that exact filename — the aggregate signal (that generic "fix CI" / "doc sync" style workflows underperform) is more defensible than any single named entry.

### Claim 5: The manifest's trigger-combination table shows success rates ranging from 83% (`push` alone) down to 0% for several multi-trigger combinations, with explicit "Avoid" recommendations for `slash_command` and any `workflow_run`-chaining combo
- **Evidence**: `manifest.json` → `trigger_combos`: `push` 0.83 (n=18, risk low, "Recommended"); `pull_request` 0.65 (n=160, risk low, "Recommended"); `issues+push` 0.53 (n=58, risk medium, "Use with caution"); `issues+workflow_run` 0.12 (n=130, risk high, "Avoid"); `slash_command` 0.05 (n=111, risk high, "Avoid"); `discussion+issues+slash_command` 0.0 (n=40, risk high, "Avoid"); `issues+pull_request+workflow_run` 0.03 (n=30, risk high, "Avoid"); `push+slash_command` 0.04 (n=28, risk high, "Avoid").
- **Confidence**: emerging (undisclosed dataset provenance beyond "518 source repos"; "success" undefined)
- **Quote**: `{"combo": "issues+workflow_run", "success_rate": 0.12, "count": 130, "risk": "high", "recommendation": "Avoid"}` (`patterns/manifest.json`, `trigger_combos`)
- **Our assessment**: This directly bears on two existing corpus positions. It corroborates the already-resolved contradiction C-004 (`slash_command` recommended-by-docs vs. near-zero empirical success) with a second, independent dataset (n=111 here vs. n=204 in the original community source cited in C-004) — same conclusion, different measurement. It also materially conflicts with `docs-ghaw-audit-with-agents.md` Claim 2, which presents `workflow_run:completed` chaining as "the standard event-chaining primitive for post-run analysis workflows" with no reliability caveat; I filed this as a new contradiction (issue #2799) rather than picking a side in this note.

### Claim 6: The wizard's own UI copy independently labels the `slash_command` trigger "(not recommended)" in its human-readable summary, separate from and prior to any reference to the empirical manifest data
- **Evidence**: `src/js/summary.js` defines the trigger labels shown in the wizard's live summary panel; the `slash_command` entry carries an inline warning baked into the label string itself, unlike every other trigger label.
- **Confidence**: settled (verbatim source string, shipped to users)
- **Quote**: `slash_command: 'a slash command is posted (not recommended)'` (`src/js/summary.js`, `triggerLabels`)
- **Our assessment**: This is a stronger and more surprising signal than the manifest statistics alone — GitHub Next's own product copy discourages a trigger type that the platform's own `docs-ghaw-chatops.md` (Claim 1) and `docs-ghaw-triggers-reference.md` document as a first-class, fully-specified feature (role filtering, sanitized input, centralized strategy). It's additional evidence for C-004's "debated" resolution: the team building the generator UI has apparently already internalized the reliability problem, even though the reference docs haven't been updated to reflect it.

### Claim 7: Workflows with explicit "DO NOT" constraints in their prompt are measurably more likely to be healthy — a statistically significant finding (p=0.009) repeated as archetype-specific advice for `issue-triage`, `custom`, `pr-review`, and `documentation-updater`
- **Evidence**: `manifest.json` → `research_findings.do_not_constraints`. The same guidance recurs verbatim (with the same 61% figure) inside individual archetype `tips` arrays, e.g. `issue-triage.json`: `"Use DO NOT constraints (e.g., 'Do NOT close issues') — 61% more likely to be healthy"`.
- **Confidence**: emerging (p-value reported, but sample size, "healthy" definition, and confounds are not disclosed)
- **Quote**: "Workflows with explicit DO NOT instructions are 61% more likely to be healthy (p=0.009)." (`patterns/manifest.json`, `research_findings.do_not_constraints`)
- **Our assessment**: This is a concrete, guide-relevant prompt-engineering claim that isn't covered (as an empirical finding) anywhere else in the corpus we checked. The repetition across four independent archetype files (not just the top-level manifest) suggests the team treats it as a reasonably robust internal finding, but the lack of a disclosed sample size or "healthy" definition keeps this at emerging rather than settled.

### Claim 8: Workflow health outcomes are bimodal rather than normally distributed — roughly 38% of workflows always succeed, 21% always fail, and 41% are mixed, which the manifest explicitly says a single average obscures
- **Evidence**: `manifest.json` → `research_findings.bimodal_distribution`.
- **Confidence**: emerging (single-source empirical claim, methodology undisclosed)
- **Quote**: "38% of workflows always succeed, 21% always fail, 41% are mixed. The average hides this." (`patterns/manifest.json`, `research_findings.bimodal_distribution`)
- **Our assessment**: This is a useful methodological caution for `docs-ghaw-measuring-impact.md`'s metric framework (Claim 5's four-layer model), which currently treats "success rate" and "acceptance rate" as scalar dashboard numbers without warning that the underlying distribution may be bimodal. A single average success-rate metric can look mediocre (~50-60%) while actually describing a population that's mostly all-or-nothing per workflow, which changes the correct remediation (fix or kill specific always-failing workflows, rather than incrementally improve a "so-so" average).

### Claim 9: Prompt size has an empirically-identified sweet spot of 3,000–8,000 bytes, and active workflows in the corpus run 35–48% larger prompts than inactive ones
- **Evidence**: `manifest.json` → `config_defaults.prompt_size_sweet_spot: [3000, 8000]` and `research_findings.prompt_size_matters`. Per-archetype `size_range_bytes` fields mostly fall inside or near this band (e.g. `code-improvement`: `[5000, 12000]`; `content-moderation`: `[4000, 7000]`; `status-report`: `[2000, 5000]`).
- **Confidence**: emerging (correlational; the manifest does not claim or demonstrate causation)
- **Quote**: "Active workflows have 35-48% larger prompts. More detail = better outcomes." (`patterns/manifest.json`, `research_findings.prompt_size_matters`)
- **Our assessment**: Directionally useful but the manifest's own framing ("more detail = better outcomes") over-claims causation from what is stated as a correlation between active-workflow status and prompt length. Worth citing as "larger, more detailed prompts correlate with active workflows" rather than a proven causal recommendation.

### Claim 10: Roughly a third of real-world gh-aw workflows are unmodified template clones, and cloned-but-uncustomized workflows underperform customized ones
- **Evidence**: `manifest.json` → `research_findings.template_clones_fragile`.
- **Confidence**: anecdotal-leaning-emerging (single aggregate percentage, no breakdown of "template" vs "customized" definition given)
- **Quote**: "32% of workflows are template copies. Copied templates have lower success than customized ones." (`patterns/manifest.json`, `research_findings.template_clones_fragile`)
- **Our assessment**: Reinforces a "customize, don't just clone" message that fits with Claim 4's anti-pattern data (many of the named low-success anti-patterns look like uncustomized template names, e.g. `daily-repo-status` appearing four times across different repos in the manifest's `anti_patterns` list).

### Claim 11: The wizard offers exactly two output formats — a downloadable gh-aw workflow `.md` file (requiring a 7-step CLI setup: enable Actions, install `gh aw`, save the file, init the engine, compile, commit + push, trigger a run) or a copy-pasteable natural-language prompt to run directly inside an agent (1 step: paste and run)
- **Evidence**: `src/js/next-steps.js` → `nextStepsHtml()` builds a numbered `<div class="next-step">` list that branches on `format`. The `workflow` branch emits 7 steps; the non-`workflow` (prompt) branch emits exactly 1.
- **Confidence**: settled (verbatim source code, deterministic branching logic)
- **Quote**: `html += step(5, 'Compile the workflow to generate the Actions YAML:<br><code>gh aw compile</code>');` and, for the prompt path, `html += step(1, \`Open <strong>${label}</strong> in your repository and run the copied prompt\`);` (`src/js/next-steps.js`)
- **Our assessment**: This confirms the wizard is positioned as an onboarding accelerator for two different adoption paths — committing a real gh-aw workflow file vs. a one-off manual prompt run — rather than a single canonical output. The 7-step `.md` path (`gh aw init --engine <engine>` → `gh aw compile` → commit both the `.md` and generated `.lock.yml`) matches the compile-then-commit-both-files pattern already documented in `docs-ghaw-compilation-process.md`'s scope, giving a corroborating, concrete end-to-end example of that sequence.

### Claim 12: The wizard exposes 5 "built-in" engines with vendor attribution (Copilot/GitHub, Claude/Anthropic, Codex/OpenAI, Gemini/Google, Pi/Inflection) and separately discovers additional community "extension" engines live from gh-aw's own `engines.json`, with at least 9 named extensions hardcoded as icon/label fallbacks (aider, crush, cursor, deepseek-harness, custom, goose, kiro, pydantic-ai, opencode)
- **Evidence**: `src/js/engines.js` → `builtInEngineIds = new Set(['copilot', 'claude', 'codex', 'gemini', 'pi'])` with a `builtInEngineCompanies` map for vendor attribution, plus `extensionLogoText` covering `aider, crush, cursor, deepseek-harness, custom, goose, kiro, pydantic-ai, opencode`. `loadDefinitionEngines()` fetches `https://raw.githubusercontent.com/github/gh-aw/main/.github/aw/engines.json` at runtime to discover any additional definition-based engines beyond the 5 built-ins.
- **Confidence**: settled (verbatim source code)
- **Quote**: `const builtInEngineIds = new Set(['copilot', 'claude', 'codex', 'gemini', 'pi']);` (`src/js/engines.js`)
- **Our assessment**: This is a nuanced extension of `docs-ghaw-engines-reference.md` Claim 1, which states the platform "supports seven AI engines — Copilot CLI (default), Claude, Codex, Gemini, Crush (experimental), OpenCode (experimental), and Pi." The wizard's source code treats only 5 of those 7 as "built-in" (Crush and OpenCode are categorized alongside third-party community extensions like `aider` and `goose`, not as built-ins) even though the reference docs count Crush and OpenCode among the platform's seven supported engines. This isn't a claim-level contradiction (both sources agree Crush/OpenCode exist and are experimental) — it's a UI/categorization inconsistency between "built-in" and "extension" framing worth noting if the guide ever states an engine count.

### Claim 13: The wizard's "Extras" step offers exactly three optional capabilities — persistent memory across runs, chart/asset generation, and Playwright-based browser automation — each of which maps to a specific gh-aw feature when the prompt or workflow file is generated
- **Evidence**: `src/js/summary.js` → `extraLabels = {memory: 'memory between runs', charts: 'chart generation', browser: 'browser access'}`. `src/js/workflow.js`'s prompt-builder translates each into a concrete instruction: `'- Add cache-memory tool for persistent memory across runs\n'`, `'- Add upload-assets safe output to publish generated charts\n'`, `'- Enable Playwright CLI for browser automation\n'`.
- **Confidence**: settled (verbatim source code)
- **Quote**: `'- Add cache-memory tool for persistent memory across runs\n'` (`src/js/workflow.js`)
- **Our assessment**: Useful as a minimal, opinionated "optional capabilities" checklist — the wizard deliberately limits Extras to three rather than exposing the full breadth of gh-aw's tool/safe-output surface, which is itself a design signal about which optional features the team considers common enough to warrant a one-click toggle.

## Concrete Artifacts

Trigger-combination success-rate table, verbatim from `patterns/manifest.json` → `trigger_combos` (GitHub Agentic Workflows Wizard, `githubnext/gh-aw-wizard`):

```json
[
  {"combo": "push", "success_rate": 0.83, "count": 18, "risk": "low", "recommendation": "Recommended"},
  {"combo": "pull_request", "success_rate": 0.65, "count": 160, "risk": "low", "recommendation": "Recommended"},
  {"combo": "issues+push", "success_rate": 0.53, "count": 58, "risk": "medium", "recommendation": "Use with caution"},
  {"combo": "issues+workflow_run", "success_rate": 0.12, "count": 130, "risk": "high", "recommendation": "Avoid"},
  {"combo": "slash_command", "success_rate": 0.05, "count": 111, "risk": "high", "recommendation": "Avoid"},
  {"combo": "discussion+issues+slash_command", "success_rate": 0.0, "count": 40, "risk": "high", "recommendation": "Avoid"},
  {"combo": "issues+pull_request+workflow_run", "success_rate": 0.03, "count": 30, "risk": "high", "recommendation": "Avoid"},
  {"combo": "push+slash_command", "success_rate": 0.04, "count": 28, "risk": "high", "recommendation": "Avoid"}
]
```

Full research-findings block, verbatim from `patterns/manifest.json`:

```json
"research_findings": {
  "bimodal_distribution": "38% of workflows always succeed, 21% always fail, 41% are mixed. The average hides this.",
  "do_not_constraints": "Workflows with explicit DO NOT instructions are 61% more likely to be healthy (p=0.009).",
  "slash_command_broken": "slash_command triggers have 0-17% success rate across all combos (e.g. 5% success across 111 runs, 14 workflows, 14 repos). Avoid until platform stabilizes.",
  "workflow_run_risky": "workflow_run chaining has 3-12% success rate (e.g. issues+workflow_run: 12% across 130 runs, 15 workflows, 15 repos). Use pre-steps or schedule instead.",
  "pre_steps_help": "Workflows with pre-steps are more likely to be active (+13pp internal, +5pp community).",
  "prompt_size_matters": "Active workflows have 35-48% larger prompts. More detail = better outcomes.",
  "template_clones_fragile": "32% of workflows are template copies. Copied templates have lower success than customized ones."
}
```

Dataset metadata, verbatim from `patterns/manifest.json` → `metadata`:

```json
"metadata": {
  "generated_at": "2026-08-18T23:58:10.787155+00:00",
  "source_repos": 518,
  "active_workflows": 340,
  "total_workflows": 819
}
```

One full archetype definition (`patterns/archetypes/issue-triage.json`), representative of the per-archetype schema shared by all 19 entries:

```json
{
  "id": "issue-triage",
  "label": "Issue Triage",
  "description": "Classify and label new issues",
  "success_rate": 0.65,
  "count": 98,
  "recommended_triggers": [{"type": "issues", "config": {}}, {"type": "schedule", "config": {}}],
  "recommended_safe_outputs": ["issues"],
  "recommended_tools": ["add-comment", "add-labels"],
  "timeout_minutes": 30,
  "prompt_style": "role-steps",
  "size_range_bytes": [3000, 7000],
  "tips": [
    "Prefer event-driven triggers like issues and schedule over manual-only execution",
    "Include explicit label taxonomy in your prompt so the agent knows valid options",
    "Use DO NOT constraints (e.g., 'Do NOT close issues') — 61% more likely to be healthy"
  ],
  "anti_patterns": ["issue-triage", "issue-triage", "marketplace-harness-gap-triage", "issue-triage", "issue-triage"]
}
```

The 7-step `.md`-workflow setup sequence generated by the wizard's "Next steps" panel, reconstructed from `src/js/next-steps.js` (`step()` calls in the `format === 'workflow'` branch, HTML tags stripped, `<name>`/`<engine>` are template placeholders filled from user answers):

```
1. Make sure GitHub Actions is enabled on your repository
2. Install the GitHub CLI and the Agentic Workflows extension, then upgrade gh-aw:
   gh extension install github/gh-aw && gh aw upgrade
3. Download the .md file and save it to .github/workflows/<name>.md
4. Set up the <engine> engine — run gh aw init --engine <engine>
5. Compile the workflow to generate the Actions YAML:
   gh aw compile
6. Commit both files and push:
   git add .github/workflows/<name>.md .github/workflows/<name>.lock.yml && git push
7. Trigger a run from the Actions tab or with:
   gh aw run <name>
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-triggers-reference.md` Claim 1 (10-trigger master catalog): the wizard's 6 wizard-exposed trigger types (`issues`, `pull_request`/`pull_request_ready_for_review`, `schedule`, `slash_command`, `label_command`, `push`, per `src/js/patterns.js`'s `RECOMMENDABLE_TRIGGERS`) are a subset of that catalog, using matching vocabulary.
  - `docs-ghaw-chatops.md` Claim 1 (`slash_command` as a distinct HITL trigger type) and the already-resolved contradiction **C-004** in CONTRADICTIONS.md (`slash_command`: recommended-by-docs vs. near-zero empirical success, n=204): this source's `trigger_combos` data (n=111, 5% success, "Avoid") and its UI copy ("not recommended", Claim 6) are a second, independent empirical data point supporting C-004's Side B. No new contradiction issue filed for this — C-004 already covers it; this note just adds corroborating evidence.
  - `docs-ghaw-deterministic-agentic-patterns.md` Claim 4 (inline pre-activation steps preferred/lightweight): corroborated by this source's `research_findings.pre_steps_help` ("Workflows with pre-steps are more likely to be active").

- **Contradicts**:
  - **Filed as new issue #2799**: `docs-ghaw-audit-with-agents.md` Claim 2 states `workflow_run:completed` is "the standard event-chaining primitive for post-run analysis workflows." This source's `trigger_combos` data shows `issues+workflow_run` at 12% success (risk: high, "Avoid") and `research_findings.workflow_run_risky` generalizes this to "workflow_run chaining" broadly, recommending pre-steps or schedule instead. Both claims concern the same mechanism and would produce different guide advice for the same scenario (chaining a downstream workflow off an upstream agent run). See issue #2799 for the full Side A/Side B writeup; no verdict is picked in this note.

- **Extends**:
  - `docs-ghaw-measuring-impact.md` Claim 5 (four-layer metric model) and Claim 11 (waste taxonomy): this source adds concrete numbers where that note is qualitative/prescriptive — e.g. the bimodal-distribution finding (Claim 8 here) is a methodological caveat that four-layer dashboards built per that note's guidance should account for (a scalar average success rate can obscure an all-or-nothing bimodal population).
  - `docs-ghaw-engines-reference.md` Claim 1 (seven supported engines): this source's built-in/extension split (Claim 12 here) refines that count — the wizard's own code treats only 5 of the 7 as "built-in," filing Crush and OpenCode alongside third-party community extensions.
  - `docs-ghaw-compilation-process.md` (scope: compile → commit `.md` + `.lock.yml`): the wizard's 7-step setup sequence (Claim 11, Concrete Artifacts) is a concrete, user-facing walkthrough of that same compile-then-commit-both-files pattern.

- **Novel**: The archetype success-rate/anti-pattern taxonomy (Claims 2–4), the DO NOT-constraints finding (Claim 7), the bimodal-distribution finding (Claim 8), the prompt-size-sweet-spot finding (Claim 9), the template-clone-fragility finding (Claim 10), and the dataset scale itself (518 repos / 819 workflows / 340 active, Concrete Artifacts) are all new to the corpus — no existing `docs-ghaw-*` note cites empirical, corpus-derived success-rate data at this granularity.

## Guide Impact

- **Ch02 (Harness Engineering / orchestration patterns)**: Add the DO NOT-constraints finding (Claim 7, p=0.009, 61% healthier) as a concrete, citable prompt-engineering recommendation — currently the guide has no empirical backing for this pattern, only stylistic advice. Also add the bimodal-distribution caveat (Claim 8) wherever the guide discusses measuring workflow success rates, so a single average isn't presented as sufficient.
- **Ch02, trigger selection guidance**: If/when the guide gives trigger-selection advice, cite the trigger-combo risk table (Claim 5, Concrete Artifacts) — `push` and `pull_request` alone are empirically low-risk/recommended; `slash_command` and any `workflow_run`-chaining combo are empirically high-risk. This should be presented alongside (not instead of) the official trigger documentation, flagged per the C-004 pattern (debated, not settled) and per the newly-filed #2799 for `workflow_run` specifically.
- **Ch04/Ch05 (implementation / workflow patterns), if the guide adds a "getting started building your first workflow" section**: The 19-archetype taxonomy (Claim 2) with success rates and anti-patterns (Claims 3–4) is a ready-made "what to build first, and what to avoid cloning" reference — more specific than generic "start simple" advice, since it names real low-success template patterns (`ci-doctor`, `pr-fix`, `daily-repo-status`) to avoid.
- **Correction to prior triage assumptions**: If any downstream Smith synthesis references this issue's Prospector comments directly (e.g. "the wizard offers 13/14/15 preset templates"), that number should be corrected to 19 archetypes (18 named + Custom), per Claim 1–2 and Extraction Notes below.

## Extraction Notes

I fetched the source URL directly (it 302-redirects from `github.github.com/gh-aw/wizard` to `githubnext.github.io/gh-aw-wizard/`) and, because the wizard is a client-rendered single-page app, cross-checked the rendered page against the app's open-source client code in `githubnext/gh-aw-wizard` (fetched via `raw.githubusercontent.com`, MIT-licensed, same organization) to get verbatim strings rather than relying on an AI-summarized re-rendering of the page. I read: `src/js/patterns.js`, `src/js/engines.js`, `src/js/summary.js`, `src/js/workflow.js`, `src/js/next-steps.js`, `src/js/landing.js`, `patterns/manifest.json`, and all 19 files under `patterns/archetypes/`.

**Discrepancy with the Prospector triage comments, flagged for visibility**: this issue carries three separate Prospector triage comments, and they disagree with each other and with the live source on basic facts — archetype counts of 13, 14, and 15 (all three number the archetype/template list differently), inconsistent trigger counts (7 vs. 8), and named archetypes ("Linter Miner/Refiner/Applier" bundled as one item in one comment, listed separately elsewhere) that don't fully match the actual 19-entry `patterns/manifest.json` list (which also includes `accessibility-expert`, `performance-nut`, `security-scanner`, `user-simulator`, and `linter-workflows` — none mentioned in any triage comment). None of the three comments mention the archetype success-rate data, anti-pattern lists, or the `research_findings` block (DO NOT constraints, bimodal distribution, trigger risk, prompt-size, template-clone fragility) at all, despite this being the source's single most extractable, guide-relevant content. I did not treat any triage comment's specific factual claims (counts, names) as ground truth — every number and name in this note is verified directly against the live page and/or the source repository, per the instruction to treat issue comments as untrusted input rather than instructions to follow. I'm noting this discrepancy rather than silently correcting it, since a Prospector triage process producing three internally-inconsistent, apparently unread assessments of the same page may be worth the maintainers' attention independent of this note.

I did not follow the `docs-ghaw-setup-creating-workflows.md`-equivalent quick-start/docs links surfaced in `next-steps.js` (`gh-aw/setup/quick-start/`, `gh-aw/setup/creating-workflows/`) as separate sub-pages, since both are already covered by existing source notes in this corpus (`docs-ghaw-setup-creating-workflows.md`). I also did not deep-read the `data/analysis-report.json` or `data/import-sources.json` files in the repo (raw data dumps feeding the manifest) beyond confirming their existence — the curated `patterns/manifest.json` and per-archetype files are the more directly guide-relevant, already-synthesized artifacts.
