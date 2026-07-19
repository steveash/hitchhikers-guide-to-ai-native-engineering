---
source_url: https://simonwillison.net/2026/Jul/14/pedalican/
source_type: blog-post
title: "simonw/pedalican"
author: Simon Willison
date_published: 2026-07-14
date_extracted: 2026-07-19
last_checked: 2026-07-19
status: current
confidence_overall: anecdotal
issue: "#2026"
---

# simonw/pedalican: A GPT-5.6 Sol multi-round sprite-generation pipeline for a Codex desktop pet

> Simon Willison's link-blog post documents (and links to) a fully-transparent
> GitHub repo in which GPT-5.6 Sol xhigh built a 9-state, 57-frame animated
> sprite sheet for a custom Codex Desktop "pet" — a pelican on a bicycle —
> through 11 chained `gpt-image-2` calls wrapped in a deterministic
> extract/validate/repair pipeline, orchestrated via two composed Codex
> skills (`hatch-pet` delegating to `imagegen`) using isolated,
> context-bounded subagent workers.

## Source Context

- **Type**: blog-post (Willison "link-blog" format — a short first-person post,
  ~250 words, pointing to an external GitHub repo that contains the
  substantive technical content). The post itself is Willison's own words;
  the deep technical artifact it links to (`github.com/simonw/pedalican`,
  originally created under the name `pedalican-pet` — GitHub now redirects
  both `github.com/simonw/pedalican-pet` and `github.com/simonw/pedalican`
  to the same renamed repo) is a 1701-line notebook file,
  `notes-on-creating-a-pet.md`, that Willison states was written by the
  model itself, not by him.
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and one of the most widely-cited practitioner commentators on
  LLM tooling. He is also the originator of the "pelican riding a bicycle"
  SVG cross-model benchmark he has run against nearly every frontier model
  release (see `blog-simonwillison-gpt55-codex-plugin.md`, Claim 1) — this
  post's pelican-on-a-bicycle subject is very likely not a coincidence given
  that recurring personal test. Important caveat specific to this source:
  the load-bearing technical claims (API call counts, QA pass/fail verdicts,
  threshold tuning results) come from a notebook that GPT-5.6 Sol wrote about
  its own work, and Willison's own commentary neither audits nor
  independently verifies those specific claims — he reports that he "spent
  some time digging into this mechanism to see how it works" but the post
  contains no first-person confirmation that he re-ran or re-checked the
  API-call ledger, threshold percentages, or QA verdicts himself.
- **Scope**: Covers one single, non-repeated build of one custom desktop-pet
  sprite sheet using OpenAI's Codex Desktop app, the `hatch-pet` and
  `imagegen` Codex skills (both open source, Apache 2.0), and the
  `gpt-image-2` model. Does not cover: any other image-generation model,
  any comparison against manually-drawn sprite pipelines, cost/latency
  numbers (no dollar or wall-clock totals given beyond "approximately seven
  minutes" for the base image), or any claim about how well this pattern
  generalizes beyond this one pet/game-adjacent asset type.

## Extracted Claims

### Claim 1: A single conditioned "canonical base" image was reused as grounding input across 9 independent follow-up generation calls instead of regenerating character identity from text each time
- **Evidence**: The API call ledger in the notebook lists one `generate` call (`base`) followed by ten `edit` calls, nine of which pass the canonical base PNG as a repeated input image alongside a per-state layout guide.
- **Confidence**: anecdotal (single build, self-reported by the generating model)
- **Quote**: "The run made **11 GPT Image API calls**: one generation call and ten edit calls. All used `gpt-image-2` at high quality. API transport succeeded for all 11 calls; one repair result (`failed-v2`) was rejected on visual grounds." (`notes-on-creating-a-pet.md`, "Complete API-call ledger")
- **Our assessment**: This is a concrete, checkable instance of "generate once, edit repeatedly with the same reference image" as a way to fight identity drift across independently-sampled image-generation calls, rather than relying on a single mega-prompt or in-context memory the model doesn't actually have between separate API calls.

### Claim 2: Input image order to the edit endpoint was treated as a semantic contract, not an incidental detail
- **Evidence**: The notebook states explicitly that the two input images per row call have fixed, meaningful positions (layout guide first, identity reference second), and every row command in the ledger follows that order.
- **Confidence**: anecdotal
- **Quote**: "The two row calls use the Images API edit operation. Input order matters: the state layout guide is Image 1 and the canonical base is Image 2." (`notes-on-creating-a-pet.md`, "Row API command shapes now running")
- **Our assessment**: Worth surfacing as a specific, non-obvious gotcha for anyone building multi-image-input generation pipelines: which image occupies which input slot changed what the model treated as "identity to preserve" versus "layout to follow, not draw." The `hatch-pet` skill copy embedded in the same notebook reinforces this by explicitly telling the row worker not to reproduce guide pixels: "do not accept outputs that copy guide pixels" (`notes-on-creating-a-pet.md`, hatch-pet SKILL.md, Rules).

### Claim 3: A generation call was deliberately skipped and replaced with a deterministic image-processing script, conditioned on a manual visual-safety check
- **Evidence**: `running-left` was not generated via the API at all. It was produced by mirroring the already-approved `running-right` strip with a Pillow script, and only after inspecting the approved strip for directional asymmetry (text, logos, off-center props, lighting cues).
- **Confidence**: anecdotal
- **Quote**: "This produced a 1536 × 512 RGBA PNG and marked `running-left` complete in the manifest. It saved one paid Image API call without changing the character identity or cadence." (`notes-on-creating-a-pet.md`, "Deterministic leftward derivation")
- **Our assessment**: A concrete example of a broader pattern worth generalizing: before paying for another generative call, check whether the desired output is a deterministic transform (mirror, crop, recolor) of an already-accepted output. The skill copy embedded in the notebook formalizes this as a policy, not an ad hoc choice: "When `running-left` is mirrored, preserve frame order and timing semantics; derive it through the deterministic script instead of mirroring an entire strip wholesale" (hatch-pet SKILL.md, Rules).

### Claim 4: A failed row was repaired with two increasingly-constrained follow-up edit calls rather than by regenerating the whole 9-row atlas
- **Evidence**: The `failed` row's first accepted output ("api-generation/failed.png") had "serious identity/scale popping" in frames 4-7. Instead of redoing the full run, two scoped repair calls (`failed-v2`, `failed-v3`) were issued against just that row, each attaching additional grounding images (a contact sheet, the previously-rejected strip) and progressively stricter prompt language.
- **Confidence**: anecdotal
- **Quote**: "BACKGROUND IS A HARD TECHNICAL REQUIREMENT: every background pixel must be the same perfectly flat pure magenta RGB(255, 0, 255), hex #FF00FF. [...] ABSOLUTELY NO TEARS OR TEAR DROPS IN ANY FRAME." (`notes-on-creating-a-pet.md`, `prompts/repairs/failed-v3.md`, exact repair prompt)
- **Our assessment**: The escalation pattern — first repair attempt fixed the scale drift but introduced a background tear and off-key color, so the second repair attempt added an explicit "HARD TECHNICAL REQUIREMENT" callout and an all-caps prohibition — reads as the model iterating against its own QA feedback within one failure mode at a time, targeting only the specific defect rather than re-rolling the whole asset. This is a scoped-retry pattern applicable well beyond image generation.

### Claim 5: The chroma-key color was chosen adversarially against a specific prop color in the character design, not defaulted
- **Evidence**: The pet's identity includes "a tiny sky-blue bicycle" as a permanent prop. Green or cyan (more conventional chroma-key colors) were rejected in favor of magenta specifically because of that blue prop.
- **Confidence**: anecdotal
- **Quote**: "Chroma key selected by the hatching workflow: pure magenta `#FF00FF`, because green/cyan keying would be riskier around the blue bicycle." (`notes-on-creating-a-pet.md`, "Creative brief and decisions")
- **Our assessment**: A specific, transferable rule: pick the extraction key color based on what colors are absent from the subject, not from a fixed convention (green-screen is standard, but it was clearly the wrong choice for a subject with blue in it).

### Claim 6: The extraction threshold for removing the chroma-key background was numerically tuned against sampled pixel counts rather than picked by eye
- **Evidence**: The notebook reports a 3-point sweep of chroma-distance thresholds on two rows, with the count and share of "magenta-like" leftover pixels measured at each threshold before selecting the final value.
- **Confidence**: anecdotal
- **Quote**: "Three controlled extraction tests were run for `idle` and `review` at chroma-distance thresholds 128, 160, and 192." / "The final deterministic extraction will therefore use `--key-threshold 192`." (`notes-on-creating-a-pet.md`, "First final visual-QA result and repair plan")
- **Concrete measurement** (same section):

  | Threshold | Opaque sample pixels | Magenta-like pixels | Share |
  | ---: | ---: | ---: | ---: |
  | 128 | 194,411 | 1,793 | 0.9223% |
  | 160 | 193,710 | 836 | 0.4316% |
  | 192 | 193,211 | 348 | 0.1801% |

- **Our assessment**: This is a deterministic-code-in-the-loop pattern worth calling out explicitly: the generative step produced pixels, but the acceptance threshold for post-processing them was chosen using ordinary numeric measurement, not another generative/subjective pass. It's a useful concrete example of "don't ask the model to do what a five-line Python script can measure exactly."

### Claim 7: A hard chroma-key threshold was not sufficient for clean edges; a separate "soft-matte despill" pass was needed to preserve antialiasing, and that in turn broke GIF preview rendering because GIF alpha is 1-bit
- **Evidence**: After threshold-192 extraction, edges still showed a "purple halo" from partially-transparent antialiased pixels. A soft-matte/despill helper was run instead of a harder cutoff, which fixed the RGBA atlas but then made preview GIFs show "opaque colored speckles" because the GIF renderer couldn't represent partial alpha — requiring a dedicated, GIF-only frame derivative with hard-quantized alpha.
- **Confidence**: anecdotal
- **Quote**: "The next visual recheck passed the RGBA atlas/contact sheet and every animation/identity criterion, but found a preview-only GIF issue: GIF transparency is one-bit, and the renderer treated residual alpha-1 pixels as opaque colored speckles. The soft RGBA atlas used by Codex was not affected." (`notes-on-creating-a-pet.md`, "Soft-matte despill repair")
- **Our assessment**: A specific, non-obvious lesson for anyone building an image pipeline that has to serve both a high-fidelity production format (RGBA WebP here) and a lossier preview/QA format (1-bit-alpha GIF): the two outputs may need genuinely different post-processing, not just different encodings of the same pixels, or the lossier format will produce false-negative QA signals against a production asset that is actually fine.

### Claim 8: The higher-level "hatch-pet" skill never calls the image API directly — it strictly delegates all generation to a separate, lower-level "imagegen" skill
- **Evidence**: The `hatch-pet` SKILL.md, reproduced verbatim in the notebook, explicitly forbids the composing skill from touching the image API and requires it to go through the composed skill's own routing/fallback logic.
- **Confidence**: anecdotal (design statement in an open-source skill file; not a measured outcome)
- **Quote**: "Do not call the Image API, image CLI, or any other image-generation path directly. Let `$imagegen` choose its own built-in-first path and fallback rules. If `$imagegen` says a fallback requires confirmation, ask the user before continuing." (`notes-on-creating-a-pet.md`, hatch-pet SKILL.md, "Generation Delegation")
- **Our assessment**: This is a concrete, shipped example of skill composability — a domain-specific skill (build a pet sprite sheet) sitting strictly on top of a generic capability skill (generate/edit an image), rather than reimplementing image-generation logic itself. It directly instantiates the folder-of-capabilities model described in `blog-anthropic-claude-code-skills-lessons.md` (Claim 4: "They're actually folders that can include scripts, assets, data, etc.") and its progressive-disclosure framing (Claim 5), just in the Codex skills ecosystem rather than Claude Code's.

### Claim 9: Visual-generation work was fanned out to isolated, single-purpose subagent workers with a fixed two-line return contract, specifically to keep large image payloads out of the parent/orchestrator's context
- **Evidence**: The `hatch-pet` skill defines "base worker," "row worker," and "final visual QA worker" roles, each scoped to exactly one job, forbidden from editing manifests or other files, and required to return only `selected_source=...` and `qa_note=...` — no inline image previews.
- **Confidence**: anecdotal
- **Quote**: "Workers must return only `selected_source=...` and `qa_note=...`; they must not include Markdown image previews, base64, or extra visual attachments in their final response." (`notes-on-creating-a-pet.md`, hatch-pet SKILL.md, "Storage Controls")
- **Our assessment**: This is a specific, concrete pattern for a general problem: binary/generative payloads blow up orchestrator context if not isolated. It extends the general subagent-fan-out pattern documented in `blog-anthropic-vlasenko-pm-agent-orchestration.md` with a narrower, image-specific rule: not just "delegate to a subagent" but "restrict the subagent's return channel to a fixed, tiny text contract" so the parent never has to see (or pay context for) the images its workers generated.

### Claim 10: Worker model selection was tiered explicitly by task type — a smaller/cheaper model for repetitive visual generation and brand research, the full orchestrator model reserved for coordination — with an explicit concurrency cap
- **Evidence**: The skill's "Model choice for workers" section names a specific smaller model for visual and discovery workers and caps simultaneous generation workers at two by default.
- **Confidence**: anecdotal
- **Quote**: "Prefer a smaller capable model for visual workers, such as `gpt-5.4-mini` with medium reasoning, when model override is available." (`notes-on-creating-a-pet.md`, hatch-pet SKILL.md, "Subagent Delegation") — the same section also states: "Keep at most two generation workers active at once unless the user explicitly asks for higher parallelism."
- **Our assessment**: A concrete cost/latency-tiering rule for multi-agent fleets: reserve the frontier/expensive model for orchestration decisions and route repetitive, well-specified subtasks (here, "generate this exact prompt and sanity-check the image") to a cheaper model. The explicit default concurrency cap (2, not "as many as possible") is also a specific, adoptable number rather than a vague "use parallelism" recommendation.

### Claim 11: Per-state semantic constraints were baked directly into each generation prompt to prevent the model from defaulting to the literal (and wrong) interpretation of a state name
- **Evidence**: The `running` state does not mean the pet visually runs — it represents Codex actively processing a task — and the row prompt explicitly rules out the literal interpretation.
- **Confidence**: anecdotal
- **Quote**: "State action: Working loop: focused active-task processing, thinking, typing, scanning, or effortful concentration; not literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, or directional travel." (`notes-on-creating-a-pet.md`, `rows/running.md`)
- **Our assessment**: A reusable prompting lesson beyond this specific pet: when a state/label name has an obvious literal visual reading that isn't the one you want ("running" as UI-status vs. "running" as locomotion), the prompt needs to name and explicitly exclude the literal interpretation, not just describe the desired one — otherwise the model's most probable completion for the word will win.

### Claim 12: The notebook's own claimed "post-acceptance cleanup" step does not match the actual contents of the published GitHub repo
- **Evidence**: The notebook states that after acceptance, "generated prompt files... unused retry prompts... layout guides and canonical/intermediate references... original API PNG outputs... decoded and soft-matte row strips... extracted production and GIF-quantized frames... chroma-threshold test images... uncompressed `final/spritesheet.png`... `imagegen-jobs.json`" were all removed, leaving only final deliverables. We fetched the actual repo tree (`github.com/simonw/pedalican`, `git/trees/main?recursive=1`) as part of this extraction and it still contains `run/api-generation/*.png`, `run/decoded/*.png`, `run/decoded-clean/*.png`, and `run/frames-gif/*` in full — exactly the categories the notebook says were deleted.
- **Confidence**: anecdotal
- **Quote**: "The durable run now contains exactly the request metadata, final WebP, validation JSON, contact sheet, nine GIF previews, frame-review JSON, and run-summary JSON." (`notes-on-creating-a-pet.md`, "Post-acceptance cleanup")
- **Our assessment**: This is a direct, checkable gap between what the model's self-authored notebook claims happened and what is actually in the published artifact — either the cleanup step ran locally and Willison re-added the intermediate files before publishing (plausible, given the post's stated goal of transparency: "I had it make extensive notes and record all of the intermediary steps"), or the cleanup step's own completion claim was inaccurate. Either way, it's a concrete illustration of why self-reported "I did X and verified Y" narration from an agent should not be taken as confirmation that X actually happened without checking the artifact directly — the same caution that applies to the QA pass/fail verdicts elsewhere in this notebook, which are also self-graded by the system that produced the images.

## Concrete Artifacts

Full 9-state animation contract driving the sprite atlas (`notes-on-creating-a-pet.md`, "Required animation contract"):

```text
The final atlas is 1536 x 1872, divided into 192 x 208 cells. It uses an 8-column x 9-row layout:

1. idle — 6 frames
2. running-right — 8 frames
3. running-left — 8 frames
4. waving — 4 frames
5. jumping — 5 frames
6. failed — 8 frames
7. waiting — 6 frames
8. running — 6 frames
9. review — 6 frames

Unused cells must be fully transparent.
```

Base identity prompt sent to `gpt-image-2` (`notes-on-creating-a-pet.md` / `run/prompts/base-pet.md`, fetched directly):

```text
Create one clean full-body reference sprite for Codex pet Pedalican.

Pet identity: A compact adorable baby pelican with a round cream-white body, soft coral-orange bill and feet, riding a tiny sky-blue bicycle. The bicycle is a permanent identity prop and stays attached to the pelican in every pose. Large warm expressive eyes, cheerful personality, readable silhouette, no helmet, no clothing, no text or logos..
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `sticker`: Polished sticker mascot with bold clean shapes, crisp outline, flat colors, and minimal highlight detail. User style notes: Polished cute sticker illustration with softly rounded shapes, clean dark-navy outlines, simple cel shading, and a consistent pastel palette. The pet and bicycle form one compact whole-body sprite silhouette..

Place a single centered pose on a perfectly flat pure magenta #FF00FF chroma-key background. Keep the full pet visible, compact, readable at 192x208, and easy to animate. Preserve approved reference identity cues. No scenery, text, borders, checkerboard transparency, shadows, glows, detached effects, or extra props. Keep #FF00FF and close colors out of the pet, props, highlights, and effects.
```

`edit` API command shape used for every row strip (`notes-on-creating-a-pet.md`, "Row API command shapes now running"):

```sh
OPENAI_API_KEY="$(llm keys get openai)" \
  uv run --with openai python \
  /Users/simon/.codex/skills/.system/imagegen/scripts/image_gen.py edit \
  --model gpt-image-2 \
  --prompt-file /Users/simon/Dropbox/dev/pedalican-pet/run/prompts/rows/idle.md \
  --image /Users/simon/Dropbox/dev/pedalican-pet/run/references/layout-guides/idle.png \
  --image /Users/simon/Dropbox/dev/pedalican-pet/run/references/canonical-base.png \
  --quality high \
  --size 1536x512 \
  --out /Users/simon/Dropbox/dev/pedalican-pet/run/api-generation/idle.png
```

Row-worker subagent contract from the `hatch-pet` skill (`notes-on-creating-a-pet.md`, hatch-pet SKILL.md, "Subagent Delegation"):

```text
Generate one hatch-pet row.

Run dir: <absolute run dir>
Row id: <row-id>
Prompt file: <absolute prompt file>
Retry prompt file: <absolute retry prompt file>
Input images:
- <absolute path> — <role>
- <absolute path> — <role>

Use $imagegen only. Read the row prompt and attach every listed input image. If imagegen returns Bad Request, retry once with the retry prompt and the same input images.

Before returning, visually check: exact frame count, same pet identity as canonical base, flat chroma background, complete separated unclipped poses, and no detached effects or guide marks. [...]

Do not edit manifests, copy into decoded, mark jobs complete, mirror rows, run image-processing scripts, repair, package, or open unrelated files.
Do not include Markdown image previews, base64, or extra attachments in the final response.

Return exactly:
selected_source=/absolute/path/to/selected-output.png
qa_note=<one sentence>
```

Deterministic post-processing chain, run only after all generation jobs complete (`notes-on-creating-a-pet.md`, hatch-pet SKILL.md, "Default Workflow"): `extract_strip_frames.py` → `inspect_frames.py` (component/clipping check) → `compose_atlas.py` (assembles the 1536×1872 sheet) → `validate_atlas.py` → `make_contact_sheet.py` → `render_animation_previews.py` (per-state GIFs) — with a final atlas-validation JSON output shape:

```json
{
  "ok": true,
  "format": "WEBP",
  "mode": "RGBA",
  "width": 1536,
  "height": 1872,
  "transparent_rgb_residue_pixels": 0,
  "errors": [],
  "warnings": []
}
```

## Cross-References

- **Corroborates**: `blog-simonwillison-gpt55-codex-plugin.md` (Claim 1) — Willison's recurring "pelican riding a bicycle" cross-model SVG benchmark. This source doesn't run that exact benchmark, but the fact that Willison's own custom-built desktop pet is also a pelican on a bicycle is consistent with that established personal-benchmark habit, and is worth noting for readers who track his output as a recurring evaluation signal rather than a one-off pattern.
- **Extends**: `blog-anthropic-claude-code-skills-lessons.md` (Claim 4: skills are folders with scripts/assets/data, not just markdown; Claim 5: skill file systems as progressive disclosure; Claim 12: helper scripts let the agent compose instead of reconstruct boilerplate). This source is a concrete, shipped, cross-vendor (OpenAI Codex, not Claude Code) instance of exactly this design pattern: the `hatch-pet` skill folder bundles Python helper scripts (`extract_strip_frames.py`, `compose_atlas.py`, `validate_atlas.py`, etc.) that the agent invokes rather than reimplementing raster logic itself, and composes a second, lower-level skill (`imagegen`) rather than duplicating its image-generation logic. Useful as independent, cross-ecosystem corroboration that the "skill as folder of capabilities, not just prompt text" pattern is not Anthropic-specific.
- **Extends**: `blog-anthropic-vlasenko-pm-agent-orchestration.md` (parallel specialized subagent orchestration pattern) — this source adds a narrower, more specific sub-pattern not present in that note: bounding each subagent's *return channel* to a fixed two-field text contract (`selected_source=`, `qa_note=`) specifically to keep large binary/generative payloads (images) out of the orchestrator's context, plus an explicit default concurrency cap (2 simultaneous generation workers) and per-role model tiering (cheaper model for repetitive visual workers, orchestrator model reserved for coordination).
- **Contradicts**: None identified against an existing source note. Claim 12 above does identify an internal contradiction — between the source's own notebook narration and the actual published repo contents — but this is an internal inconsistency within the source itself, not a disagreement with another source-note claim, so no contradiction issue was filed per MINER.md §4a (that section requires filing only when a claim opposes an existing source note or two claims within the same source materially disagree in a way that would change guide advice; here it's a notebook-vs-artifact discrepancy rather than a genuine claims dispute, but readers should note this observation directly rather than trust the notebook's cleanup claim at face value — see the "Our assessment" line under Claim 12).
- **Novel**: No existing source note in this corpus covers a multi-round, conditioned image-generation pipeline for producing structured, constrained visual assets (a sprite atlas with fixed geometry, transparency, and semantic-per-state requirements). This is the first source note to document: (1) chroma-key color selection strategy for AI-generated sprites, (2) numeric threshold-tuning of chroma-key extraction against measured pixel counts, (3) the RGBA-vs-1-bit-GIF alpha mismatch as a specific pitfall when a generative pipeline has to serve both a production and a preview/QA output format, and (4) input-image-order-as-semantic-contract for multi-image edit calls.

## Guide Impact

- **Chapter 04 (creative/multimodal AI)**: Add a documented pattern for structured, constrained asset generation (sprites, icon sets, or other assets with fixed geometry/format requirements): generate a single canonical reference image once, then condition every subsequent variant/pose on that same reference plus a purpose-built (and now this note gives worked examples: chroma-key color selection versus the subject's own palette, numeric threshold-tuning against measured pixel counts rather than eyeballing, and the need for a *separate* post-processing branch when a lossy preview format like GIF can't represent what the production format (RGBA WebP/PNG) can — citing this source as the concrete worked example (Claims 1, 2, 5, 6, 7).
- **Chapter 05 (multi-step AI orchestration / tool building)**: Add this source as a worked example of two orchestration disciplines that existing notes state as principles but don't show fully instantiated end-to-end: (a) skill composability — a higher-level skill strictly delegating to a lower-level capability skill rather than reimplementing it (Claim 8, extending `blog-anthropic-claude-code-skills-lessons.md`); (b) context-bounded subagent workers with a fixed, minimal return contract specifically to keep large generative payloads out of the orchestrator (Claim 9, extending `blog-anthropic-vlasenko-pm-agent-orchestration.md`), plus a concrete default concurrency cap and per-role model tiering (Claim 10) that could be cited as a specific, adoptable number rather than the vaguer "use subagents for parallel work" guidance currently in the guide.
- **Chapter 05 / editorial note on source hygiene**: Claim 12 (the notebook's cleanup claim vs. actual repo contents) is a good illustrative example for any guide section that discusses trusting agent self-reports — worth citing as a caution that "the agent said it verified/cleaned up/passed QA" is not equivalent to independently checking the artifact, even when the agent produces detailed, transparent-looking documentation of its own process.

## Extraction Notes

- The blog post itself is very short (~250 words); nearly all substantive content came from following linked pages, per MINER.md §1. I followed: (1) the blog post itself; (2) `notes-on-creating-a-pet.md` (1701 lines — the full build notebook, including two verbatim embedded SKILL.md copies for `hatch-pet` and `imagegen`, which meant I did not need to separately fetch the `openai/skills` and `openai/codex` repos to get their content); (3) `run/prompts/base-pet.md`; (4) `run/prompts/rows/waving.md`; (5) the repo's `README.md`. That is 5 pages beyond the blog post itself, at the top of MINER.md's "up to 5 linked pages" guidance.
- The repo was originally created as `simonw/pedalican-pet` and later renamed to `simonw/pedalican`; both URLs now redirect to the same repo (verified via `curl -L`). The blog post and the notebook's raw links use the older name; I cite the current canonical name (`simonw/pedalican`) but note the discrepancy here so the Assayer doesn't flag it as a broken/wrong link.
- I independently fetched the repo's file tree via the GitHub API (`git/trees/main?recursive=1`) specifically to check the notebook's own "post-acceptance cleanup" claim against reality — this surfaced Claim 12 above (the claimed cleanup did not happen, or was reversed before publishing).
- No paywall or access issues. All linked pages loaded without authentication.
- I did not attempt to independently reproduce any part of the pipeline (no `OPENAI_API_KEY` credential access or intent to spend money on image generation as part of this extraction) — all claims here are extracted from the published text/artifacts, not independently re-verified by re-running the pipeline.
