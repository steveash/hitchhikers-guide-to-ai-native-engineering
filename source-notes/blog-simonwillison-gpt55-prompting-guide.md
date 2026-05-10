---
source_url: https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/
source_type: blog-post
title: "GPT-5.5 prompting guide"
author: Simon Willison
date_published: 2026-04-25
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: emerging
issue: "#529"
---

# GPT-5.5 prompting guide

> Simon Willison surfaces and annotates OpenAI's official GPT-5.5 prompting guidance — three actionable principles: emit a user-visible acknowledgment before tool calls, treat GPT-5.5 as a new model family requiring fresh tuning, and start from the smallest working prompt then tune five specific axes; also linked is the official OpenAI upgrade skill (GitHub) encoding a formal three-tier migration classification and a seven-dimension validation protocol.

## Source Context

- **Type**: blog-post (Willison link-post with brief annotation; ~400 words; links to official OpenAI documentation and a GitHub-hosted upgrade guide). Two sub-pages were followed per MINER.md §1: the OpenAI GPT-5.5 prompting guide (`developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5`) and the `openai/skills` upgrade guide on GitHub. Claims 1–5 come from the Willison post / OpenAI prompting guide; Claims 6–10 come from the GitHub upgrade guide.
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI; one of the most widely-cited practitioner commentators on LLM tooling. This post is his standard link-post format: he surfaces and briefly annotates official documentation he considers worth highlighting. The primary content is from OpenAI's own published guides (prompting guide + upgrade skill), not Willison's personal observations — his role here is curation and annotation. Both linked sources are official OpenAI materials.
- **Scope**: Covers GPT-5.5 prompt strategy for new and migrating users. Does NOT cover: model capability benchmarks, pricing, reasoning token costs, or broader ecosystem trends. Scope is squarely practical prompting and migration guidance from the vendor.

## Extracted Claims

### Claim 1: For multi-step tasks, send a short user-visible acknowledgment before any tool calls to prevent users perceiving the system as unresponsive

- **Evidence**: Official OpenAI recommendation in the GPT-5.5 prompting guide, highlighted by Willison as the lead recommendation in his post. Willison specifically flags this as the first practical pattern worth noting.
- **Confidence**: emerging (official vendor guidance; concrete UX pattern; testable)
- **Quote**: "Before any tool calls for a multi-step task, send a short user-visible update that acknowledges the request and states the first step. Keep it to one or two sentences."
- **Our assessment**: This is the "preamble before tool calls" pattern — emit a brief acknowledgment the moment a multi-step request arrives, before the model begins any tool execution. The mechanism is simple: the user sees at least one visible response immediately, eliminating the "dead silence while planning" perception problem. The 1–2 sentence constraint matters: too long defeats the purpose (delays tool execution without adding information); too short fails to acknowledge the specific request. This connects to the dual-channel output architecture documented in `blog-simonwillison-codex-base-instructions.md` Claim 5 (the `commentary` / `final` channel split baked into GPT-5.5's system prompt), but applies here as a prompt engineering recommendation rather than a protocol enforcement — practitioners can adopt this pattern independent of whether they're using Codex's native channel architecture.

### Claim 2: GPT-5.5 should be treated as a new model family requiring deliberate prompt retuning, not a drop-in replacement for GPT-5.2 or GPT-5.4

- **Evidence**: Official OpenAI guidance surfaced by Willison in the GPT-5.5 prompting guide; Willison highlights this as the key migration posture change.
- **Confidence**: emerging (official vendor recommendation; reinforced by the detailed upgrade guide that anticipates non-trivial migration effort)
- **Quote**: "To get the most out of GPT-5.5, treat it as a new model family to tune for, not a drop-in replacement for `gpt-5.2` or `gpt-5.4`."
- **Our assessment**: This directly modifies the scope of the "model-swap-ability" principle documented in `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4, which recommends designing software stacks to "swap models as easily as bumping a dependency." These operate at different levels: the architectural swap (model string change + API compatibility) may be easy, but optimal performance requires deliberate prompt work afterward. Practitioners should not read "swap like a dependency bump" as "performance-preserving swap." The two claims are consistent if read as architectural flexibility (make it mechanically possible) + operational reality (plan for prompt tuning after the swap). For practitioners who have deferred prompt investment because "it still works," this is the vendor signal to schedule prompt work.

### Claim 3: Model migration should start from a fresh minimal baseline prompt rather than carrying forward accumulated legacy prompt instructions

- **Evidence**: Official OpenAI guidance from the GPT-5.5 prompting guide, noted by Willison.
- **Confidence**: emerging (official vendor guidance with practical rationale)
- **Quote**: "Begin migration with a fresh baseline instead of carrying over every instruction from an older prompt stack."
- **Our assessment**: Accumulated prompts for older models often include compensatory instructions patched in for known limitations (verbosity constraints, reasoning-effort hints, output format enforcers) that are no longer needed or that actively interfere with a more capable model. Carrying them forward creates prompt debt: instructions that do nothing useful but consume tokens and add noise. Starting from the minimal prompt that preserves the product contract reveals which instructions are genuinely load-bearing and which were compensatory workarounds. This is consistent with the principle from Claims 2 and 4: GPT-5.5 is a different model that requires its own tuning, not the same tuning with old prompts removed one-by-one.

### Claim 4: The GPT-5.5 prompt optimization sequence is: start with the smallest prompt that preserves the product contract, then tune five specific axes against representative examples

- **Evidence**: Official OpenAI guidance from the GPT-5.5 prompting guide; quoted verbatim in Willison's post as the actionable tuning sequence.
- **Confidence**: emerging (official vendor guidance)
- **Quote**: "Start with the smallest prompt that preserves the product contract, then tune reasoning effort, verbosity, tool descriptions, and output format against representative examples."
- **Our assessment**: This gives practitioners a concrete five-axis tuning checklist: (1) reasoning effort, (2) verbosity, (3) tool descriptions, (4) output format — calibrated against (5) representative examples rather than synthetic tests or qualitative gut-feel. The sequencing is important: establish the baseline that meets the contract first, then optimize along individual dimensions. This prevents the common failure mode of optimizing one dimension (e.g., adding verbose reasoning instructions) while unknowingly degrading another (e.g., output format compliance). "Representative examples" as the calibration set is more rigorous than "does it look right?" but more practical than a full eval suite.

### Claim 5: OpenAI's Codex app includes an `openai-docs` upgrade skill that automates GPT-5.5 migration from a natural language command

- **Evidence**: Willison's post notes this tooling exists; the GitHub-hosted `openai/skills` repository contains the full upgrade guide specification that the skill implements.
- **Confidence**: emerging (tooling exists and is publicly documented; requires Codex subscription access)
- **Quote**: "$openai-docs migrate this project to gpt-5.5" (Codex skill invocation command, from Willison's post)
- **Our assessment**: The Codex upgrade skill is not just a convenience wrapper — it implements the full migration workflow documented in Claims 6–10. For practitioners using Codex, this automates the inventory, classification, and migration steps. For those without Codex access, the GitHub-published upgrade guide (fully public at the URL listed in the source) provides the same methodology as a manual checklist. The skill includes a freshness check (`node scripts/resolve-latest-model-info.js`) that determines whether to use the bundled guide or fetch the current remote version — a useful pattern for any migration tooling designed to stay current.

### Claim 6: OpenAI's upgrade workflow classifies every model usage site into one of three upgrade tiers: "model string only", "model string + light prompt rewrite", or "blocked without code changes"

- **Evidence**: OpenAI's official upgrade guide, hosted in the public `openai/skills` GitHub repository and linked from Willison's post. The classification system is the backbone of the entire upgrade workflow.
- **Confidence**: settled (public official document; directly inspectable at the source URL; the three classes have dedicated specification sections)
- **Quote**: (from upgrade guide section headings and decision criteria) `model string only` / `model string + light prompt rewrite` / `blocked without code changes`
- **Our assessment**: This triage framework is independently useful as a migration planning tool, separate from the Codex automation. For each integration point in a codebase, explicitly classifying the upgrade scope before starting prevents scope creep and sets realistic expectations. The "blocked" category is critical: it names the failure mode where practitioners attempt a prompt-only migration when the integration actually requires implementation changes (API surface, tool wiring, SDK migration). Naming this class makes it appropriate to stop and raise the issue rather than improvise a workaround.

### Claim 7: The upgrade guide explicitly instructs against automatically upgrading intentionally-pinned model usages such as test examples, eval baselines, and low-cost fallback routing paths

- **Evidence**: OpenAI upgrade guide, "Upgrade posture" section. This is an explicit constraint in the official workflow specification.
- **Confidence**: settled (directly inspectable; official guidance)
- **Quote**: "do not automatically upgrade older or ambiguous model usages that may be intentionally pinned, such as historical docs, examples, tests, eval baselines, comparison code, or low-cost fallback/routing paths. Unless the user explicitly asks to upgrade all model usage, leave those sites unchanged and list them as confirmation-needed"
- **Our assessment**: Intentional model pinning is a real and common engineering pattern in multi-model architectures — regression test suites use a known model for repeatable baselines; cost-optimized routing paths use older cheaper models for low-stakes tasks; eval suites use a reference model for cross-run comparability. The explicit enumeration here (historical docs, examples, tests, eval baselines, comparison code, routing paths) covers the full range. For practitioners migrating large codebases, this list is a useful checklist for identifying sites that should be excluded from automated migration and flagged for manual review.

### Claim 8: Post-migration validation requires comparing GPT-5.5 against the GPT-5.4 baseline across seven dimensions: task success, retry count, tool-call count, total tokens, latency, output shape, and user-visible quality

- **Evidence**: OpenAI upgrade guide validation section. The seven-dimension checklist is explicit official guidance.
- **Confidence**: settled (official guidance; directly inspectable)
- **Quote**: "Compare against the current GPT-5.4 baseline when available. Check task success, retry count, tool-call count, total tokens, latency, output shape, and user-visible quality."
- **Our assessment**: The multi-dimension comparison list prevents silent regressions that raw output quality checks miss. A migration that preserves task success but doubles tool-call count and triples latency is a regression, not a success — it will cause cost overruns and user-experience degradation in production. The explicit inclusion of "retry count" is notable: an increased retry rate signals that the model is more frequently failing on tasks that previously succeeded on the first attempt, even if the eventual outputs look fine. For practitioners building model migration CI/CD: these seven dimensions should each have a baseline measurement captured before the migration begins.

### Claim 9: During GPT-5.5 migration, preserve the current reasoning effort setting as the starting point rather than changing it unless there is a measured reason to do so

- **Evidence**: OpenAI upgrade guide, step 6 ("Apply the upgrade").
- **Confidence**: settled (official guidance)
- **Quote**: "Start from the current reasoning effort when it is visible unless there is a measured reason to change it."
- **Our assessment**: This is conservative migration discipline: when two variables change simultaneously (model version + reasoning effort), behavioral differences cannot be attributed to either cause alone. The recommendation keeps the migration narrowly scoped to the model string change first, allowing practitioners to independently evaluate whether reasoning effort tuning adds additional value after the baseline migration is validated. This connects to Claim 4's tuning sequence — reasoning effort is one of the five axes to tune, but it should be tuned as a separate step after the baseline migration, not as part of the migration itself.

### Claim 10: When a GPT-5.5 upgrade would require API-surface changes, parameter rewrites, tool definition changes, or SDK migration, the upgrade should be classified as "blocked" rather than worked around through prompts

- **Evidence**: OpenAI upgrade guide, "blocked" classification section with explicit criteria.
- **Confidence**: settled (official guidance)
- **Quote**: "if the upgrade would require API-surface changes, parameter rewrites, tool rewiring, provider migration, or broader code edits, mark it as blocked instead of stretching the scope"
- **Our assessment**: This is healthy scope discipline for migration engagements. When a model upgrade reveals that an integration has hidden implementation dependencies (tool definitions, API parameter shapes, provider-specific behavior), the correct response is to scope that implementation work separately — not to work around it by adding compensatory prompt complexity. The explicit instruction "do not improvise a broader upgrade" is important: it prevents the anti-pattern of using prompts as a substitute for fixing the real problem. For practitioners who discover a "blocked" upgrade: the correct path is to open an implementation task for the API/tool work, then revisit the model upgrade once the interface is clean.

## Concrete Artifacts

### Codex upgrade skill invocation (from Willison's post)

```
$openai-docs migrate this project to gpt-5.5
```

*Source: Simon Willison, simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/. The `$openai-docs` prefix invokes the OpenAI Docs skill in the Codex app; the remainder is the natural language task.*

### OpenAI upgrade classification system (from `openai/skills` upgrade guide)

```
Upgrade classes for each model usage site:

1. model string only
   → Use when: source is GPT-5.4, existing prompts are already short and 
     explicit, no strict output format / tool-call / batch / long-horizon 
     execution requirements
   → Action: replace model string, preserve reasoning effort, keep prompts 
     unchanged, validate with existing tests or spot checks

2. model string + light prompt rewrite
   → Use when: task needs stronger completeness, citation discipline, 
     verification, or dependency handling; OR output is too verbose/dense/
     hard to scan; OR workflow is coding/terminal/tool-heavy (but API surface 
     and tool definitions can remain unchanged)
   → Action: replace model string, make only the smallest prompt edits needed 
     for the observed workflow risk, read GPT-5.5 prompting guide for guidance

3. blocked without code changes
   → Use when: upgrade requires API-surface changes, parameter rewrites, tool 
     rewiring, provider migration, or broader code edits
   → Action: do NOT improvise; report the blocker; scope the implementation 
     work separately
```

*Source: openai/skills, `skills/.curated/openai-docs/references/upgrade-guide.md`, commit `724cd511c96593f642bddf13187217aa155d2554`*

### Seven-dimension post-migration validation checklist (from upgrade guide)

```
After migrating to GPT-5.5, compare against GPT-5.4 baseline:

□ Task success rate
□ Retry count
□ Tool-call count
□ Total tokens used
□ Latency
□ Output shape (format compliance)
□ User-visible quality

For specialized workflows: validate the contract that matters most 
rather than judging only general output quality.
If prompt edits were added: confirm each block is doing real work 
instead of adding noise.
```

*Source: openai/skills, upgrade-guide.md, "Validation plan" section*

### GPT-5.5 upgrade freshness check pattern (from upgrade guide)

```bash
# Before applying bundled upgrade guide, check if it is still current:
node scripts/resolve-latest-model-info.js

# If returns { modelSlug: "gpt-5p5" } → use bundled guide
# If returns a different modelSlug → fetch migrationGuideUrl and 
#   promptingGuideUrl from the result and use those instead
# If the command fails → continue with bundled fallback and say the 
#   freshness check was unavailable
```

*Source: openai/skills, upgrade-guide.md, "Freshness check" section*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-codex-base-instructions.md` Claim 5: That note documents GPT-5.5's dual-channel output protocol baked into the system prompt (`commentary` for in-progress updates, `final` for completed answers). Claim 1 here (preamble before tool calls) is the prompt-engineering application of the same architectural principle — the system-prompt channel design enables the pattern, and this official guidance recommends practitioners explicitly use it.
  - `blog-simonwillison-codex-base-instructions.md` Claim 9: That note documents the "autonomy and persistence" directive across Codex model tiers ("Persist until the task is fully handled end-to-end within the current turn whenever feasible"). The preamble-before-tool-calls pattern (Claim 1 here) is the user-experience complement to that persistence directive: the model is going to keep running until done, so the first action should be signaling that to the user.
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 1: That note documents the 240× reasoning token cost difference between default and `xhigh` settings on GPT-5.5. Claim 9 here (preserve current reasoning effort during migration) is the conservative migration discipline that makes the cost difference visible as an independent variable after the model string swap, rather than obscuring it.

- **Contradicts**: None filed. The apparent tension between this source (Claim 2: "treat GPT-5.5 as a new model family, not a drop-in replacement") and `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4 ("swap models as easily as bumping a dependency") is not a contradiction — it is a conditioning variable. The Batch editorial describes an architectural property (the swap should be mechanically easy); this source describes an operational consequence (plan for prompt tuning after the swap). Both can be true simultaneously: build harnesses where the model string can be changed in one line, AND expect to spend time retuning prompts for GPT-5.5 after you do.

- **Extends**:
  - `blog-simonwillison-gpt55-codex-plugin.md`: That note (April 23) documents the GPT-5.5 access mechanism and reasoning token cost. This note (April 25) adds the official prompting strategy for GPT-5.5 — moving from "how to access the model" to "how to prompt it effectively." Together they complete the GPT-5.5 practitioner picture: access path → cost/effort calibration → prompting strategy.
  - `blog-simonwillison-codex-base-instructions.md`: That note documents the behavioral contracts baked into GPT-5.5's system prompt. This note documents the complementary layer: official prompt engineering recommendations for practitioners building on top of that system prompt. The two together give practitioners both the embedded behavioral constraints and the vendor-recommended prompting strategy.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4: The model-swap-ability editorial principle is extended by the upgrade classification system here (Claims 6–10). The Batch says "design for easy swaps"; this source says here is the formal workflow for executing those swaps, including when a swap is genuinely easy (model string only) vs. when it requires real engineering work (blocked).

- **Novel**:
  - **Formal three-tier upgrade classification for model migrations**: No existing corpus source documents a structured approach to classifying migration effort. The `model string only` / `model string + light prompt rewrite` / `blocked` taxonomy is the first in-corpus framework for scoping model migration work.
  - **Seven-dimension post-migration validation checklist**: No existing source specifies what dimensions to measure when validating a model upgrade. The explicit list (task success, retry count, tool-call count, total tokens, latency, output shape, user-visible quality) is the first in-corpus migration validation protocol.
  - **Do-not-upgrade-pinned-usages guidance**: The explicit protection of intentionally-pinned model usages (eval baselines, fallback paths, test suites) from automatic migration is not documented elsewhere in the corpus. This is the first in-corpus statement that multi-model architectures require deliberate handling during model upgrades.
  - **Fresh baseline migration principle**: The "start from the smallest prompt that preserves the product contract" principle (as distinct from iterative cleanup of an existing prompt) is new to the corpus. Existing notes discuss prompt construction but not this specific migration sequencing.
  - **Upgrade freshness check pattern**: The pattern of programmatically verifying whether a bundled migration guide is still current before applying it (rather than assuming it is) is a novel operational pattern with broader applicability beyond this specific migration.

## Guide Impact

- **Chapter 02 (Harness Engineering — Model Migration)**: No chapter currently documents model migration methodology. Claims 6–10 together constitute a complete migration framework that should be synthesized into a "how to upgrade your model version" section. Specifically: the three-tier classification (Claim 6) gives practitioners a scoping tool; the pinned-usage protection (Claim 7) prevents accidental regression in multi-model architectures; the seven-dimension validation (Claim 8) provides a concrete post-migration checklist; the conservative reasoning-effort preservation (Claim 9) prevents two-variable confounds; and the "blocked" category discipline (Claim 10) prevents prompt-as-workaround antipatterns.

- **Chapter 03 (Prompting Patterns — UX for Multi-Step Agents)**: Claim 1 (preamble before tool calls) should be added as a concrete UX pattern recommendation in any section covering long-running or multi-step agent interactions. The recommendation is: emit one brief acknowledgment immediately upon receiving the request, before any tool calls begin. This is low-effort to implement and has direct user-experience impact.

- **Chapter 03 (Prompting Patterns — Model-Specific Tuning)**: Claims 2–4 together define the GPT-5.5 migration posture: (a) treat as a new model, not drop-in; (b) start from fresh minimal baseline, not legacy prompt stack; (c) tune five axes (reasoning effort, verbosity, tool descriptions, output format) against representative examples. This should be documented as the vendor-recommended approach for GPT-5.5 and, by extension, as a general model migration practice.

- **Chapter 04 (Context Engineering — Reasoning Effort)**: Claim 9 (preserve current reasoning effort during migration as a starting point) adds a specific migration discipline to any section on reasoning effort configuration. The current corpus (`blog-simonwillison-gpt55-codex-plugin.md` Claim 1) documents the cost implications of reasoning effort; this claim adds the migration best practice: isolate reasoning effort changes from model version changes so each can be evaluated independently.

## Extraction Notes

- **Two sub-pages followed**: (1) The OpenAI GPT-5.5 prompting guide at `developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5` — provides the official prompting strategy (Claims 1–4); WebFetch returned a summary with key guidance preserved but could not return the full document verbatim. Quotes attributed to this page came from a consistent extraction across two separate WebFetch calls; the Assayer should verify exact wording against the live source. (2) The OpenAI upgrade guide at `github.com/openai/skills/blob/724cd511c96593f642bddf13187217aa155d2554/skills/.curated/openai-docs/references/upgrade-guide.md` — WebFetch returned what appears to be the complete file content (Claims 6–10 and Concrete Artifacts); quotes from this source have higher confidence.
- **Simon Willison's post is brief annotation, not analysis**: The blog post highlights three or four key items from the official OpenAI docs; the substantive content is in the linked sources. This note treats the linked pages as the primary extraction sources per MINER.md §1 ("follow up to 5 linked pages that seem substantive").
- **No direct access to rendered OpenAI docs**: `developers.openai.com` routes require interactive rendering (likely JavaScript-heavy). Quotes from that page (Claims 1–4) were extracted via WebFetch summary; they are consistent across multiple fetches and consistent with the Prospector's triage comment, but the Assayer should spot-check against the live page.
- **Third linked page not followed**: `developers.openai.com/api/docs/guides/latest-model` (titled "Using GPT-5.5 guide") was not followed because Claims 1–10 sufficiently cover the prompting and migration guidance from the primary and first linked sub-page; the third link appears to cover broader model usage rather than the prompting/migration focus of this issue.
