---
source_url: https://github.blog/changelog/2026-04-27-copilot-student-gpt-5-3-codex-removal-from-model-picker
source_type: docs
title: "Copilot Student GPT-5.3-Codex removal from model picker"
author: GitHub (official changelog)
date_published: 2026-04-27
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: settled
issue: "#447"
---

# Copilot Student GPT-5.3-Codex Removal from Model Picker

> GitHub's April 27, 2026 changelog documenting the removal of GPT-5.3-Codex from the manual model picker on the Copilot Student (free educational) tier — while retaining it via auto model selection — establishing product-tier-specific model picker constraints not previously documented in the corpus.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200 words, April 27, 2026)
- **Author credibility**: GitHub engineering team. Authoritative for the fact that this removal occurred, which plan tier it affects, and what the stated rationale is. Not a source for capability comparisons between GPT-5.3-Codex and other models, or for predicting when auto selection will be constrained similarly.
- **Scope**: Removal of GPT-5.3-Codex from the model picker in the Copilot Student plan (free educational tier) while preserving access through auto model selection. Covers: affected model, affected plan, retention mechanism (auto), stated rationale (reliability measures tied to usage-based billing transition), and pointers to documentation and the GitHub Education Community. Does NOT cover: which other models remain in the Student picker, whether auto selection on Student is plan-constrained to a lower pool, numeric usage limits for Student, or whether this removal is permanent or genuinely temporary.

## Extracted Claims

### Claim 1: GPT-5.3-Codex is removed from the model picker in the Copilot Student plan as of April 27, 2026

- **Evidence**: Official GitHub Copilot changelog dated April 27, 2026; stated as a same-day change ("Starting today").
- **Confidence**: settled (product fact; stated in official changelog with an effective date of the announcement itself)
- **Quote**: "Starting today, in our Copilot Student plan, we are removing GPT-5.3-Codex from the model picker."
- **Our assessment**: This is the first source in the corpus documenting a model being removed from the manual picker on a specific plan tier. The removal is targeted: only the Student plan, only GPT-5.3-Codex, only from the explicit picker (not from auto). Prior deprecation changelogs (`docs-github-copilot-gpt41-deprecation.md`, `docs-github-copilot-gpt52-deprecation.md`) removed models entirely from Copilot — this source establishes a different mechanism: picker-removal with auto-retention. For Ch02: the model selection landscape now has a third state beyond "available" and "deprecated": "available via auto only."

### Claim 2: GPT-5.3-Codex remains accessible on the Copilot Student plan through auto model selection after its removal from the picker

- **Evidence**: Changelog explicitly states the model "remains available through auto model selection."
- **Confidence**: settled (retention mechanism stated directly in official changelog)
- **Quote**: "remains available through auto model selection"
- **Our assessment**: This is the key operational nuance. Students do not lose GPT-5.3-Codex capability outright; they lose the ability to explicitly request it. Auto selection may or may not route to GPT-5.3-Codex depending on the same heuristics documented in `docs-github-copilot-cli-auto-model-selection.md` Claim 2 (plan + policies + rate-limit pressure). For practitioners: a Student who was explicitly pinning GPT-5.3-Codex can no longer do so, but their requests may still land on GPT-5.3-Codex if auto selects it. This is a weaker access guarantee than explicit selection.

### Claim 3: The removal is framed as part of temporary reliability and performance measures applied across all Copilot Individual plans

- **Evidence**: Changelog states the change is part of temporary measures affecting Individual plans including Free, Pro, Pro+, and Student.
- **Confidence**: settled (rationale stated directly; "temporary" modifier is the vendor's framing)
- **Quote**: (no direct quote available for the full sentence; see paraphrase in Our assessment)
- **Our assessment**: The changelog describes these as "temporary reliability and performance measures" across Copilot Individual plans (Free, Pro, Pro+, and Student). The word "temporary" is notable — this implies GitHub may restore explicit GPT-5.3-Codex selection to the Student picker once the reliability pressures ease. However, prior changes framed as reliability measures (see `docs-github-copilot-individual-plan-changes.md` Claim 8: "to ensure service reliability and a sustainable Copilot experience for all users") have not documented a reversal mechanism. Practitioners should treat "temporary" as vendor aspiration rather than a committed timeline.

### Claim 4: The model picker changes are connected to GitHub's transition toward usage-based billing for Individual plans

- **Evidence**: Changelog links the reliability measures to a transition toward usage-based billing, positioning the picker restrictions as a bridging mechanism during the billing model change.
- **Confidence**: emerging (the link to usage-based billing is stated in the changelog, but how billing model changes affect picker availability is not mechanically explained)
- **Quote**: (no direct quote capturing the billing transition context; see paraphrase in Our assessment)
- **Our assessment**: The framing of picker removal as a precursor to usage-based billing signals that GitHub may be restructuring which models are picker-accessible by plan tier before introducing per-use pricing. Once usage-based billing is in place, the access rationale shifts from "pool fairness" to "you pay for what you use." The picker removal from Student may be permanent in that post-transition state — Student being a free tier with no billing mechanism could mean GPT-5.3-Codex simply never returns to the Student picker. For Ch05: teams advising educational or student developers should factor in that the Student plan model picker may stabilize at a lower capability ceiling than paid tiers.

### Claim 5: Auto model selection is presented as a direct substitute for manual model picking, framed as routing each request to the strongest available model

- **Evidence**: Changelog provides a promotional description of auto selection immediately after announcing the removal, positioning it as a positive replacement.
- **Confidence**: settled (the claim that auto exists and is offered as a substitute is a product fact; the claim that auto always selects the "strongest model" is vendor framing without supporting evidence)
- **Quote**: "Auto model selection is built to match each request with the strongest model for the job, which means less time toggling settings and more time coding."
- **Our assessment**: The framing is marketing language. Auto model selection in the CLI (documented in `docs-github-copilot-cli-auto-model-selection.md` Claim 2) routes based on plan + policies + rate-limit pressure, not task complexity. "Strongest model for the job" implies task-aware routing, but no evidence is provided that auto reasons about what the user is actually working on. For practitioners: auto is a reliability and cost optimization, not a capability optimizer. Students who relied on GPT-5.3-Codex for its specific capabilities (Codex-family instruction-following for code tasks) may receive a different model via auto depending on conditions.

### Claim 6: The Copilot Student plan is an educational free tier with model access restrictions that now differ from the paid Individual plans (Pro, Pro+)

- **Evidence**: The changelog isolates the Student plan as the subject of this specific removal, distinct from changes to Pro and Pro+. The Prospector's triage note identifies this as the first corpus documentation of product-tier-specific constraints on model availability between Student and other Individual plans.
- **Confidence**: emerging (the claim that Student is differentiated from Pro/Pro+ on this specific picker is settled from the changelog; the broader inference about Student being a distinct governance tier is derived, not stated)
- **Quote**: (no direct quote beyond "in our Copilot Student plan")
- **Our assessment**: The corpus previously documented model access differences between individual tiers (Opus removed from Pro but available on Pro+, per `docs-github-copilot-individual-plan-changes.md` Claim 5). This source adds a new layer: even within the non-Opus model family, the Student plan has a more restricted picker than Pro or Pro+. This is the first evidence of GitHub applying picker-level differentiation to the educational free tier independently of the paid individual plans. For Ch05: enterprise teams with student developer programs should document that the Student plan model picker is a subset of the Pro/Pro+ picker and may narrow further.

## Concrete Artifacts

### Student Plan Model Picker Change (April 27, 2026)

```
GitHub Copilot Student Plan — GPT-5.3-Codex Model Access

Before April 27, 2026:
  GPT-5.3-Codex:  Available in model picker (explicit selection)

After April 27, 2026:
  GPT-5.3-Codex:  REMOVED from model picker
                  Still available via auto model selection

Rationale given:   Temporary reliability and performance measures
                   across all Individual plans (Free, Pro, Pro+, Student)
                   during transition to usage-based billing

Affected plans:    Student only (picker change; broader reliability measures
                   affect all Individual plans)

Auto model pool:   GPT-5.3-Codex remains in the auto pool
                   (consistent with docs-github-copilot-cli-auto-model-selection.md
                    Claim 3 which listed GPT-5.3-Codex in the CLI auto pool
                    as of April 17, 2026)
```

*Source: GitHub Copilot official changelog, April 27, 2026*

### Copilot Student Plan — Model Access Pattern Summary

```
For Student plan practitioners post-April 27, 2026:

  GPT-5.3-Codex:
    Explicit picker selection:    NOT available
    Auto model selection:         Available (GitHub will route to it
                                  based on plan + policies + rate-limit pressure)
    Reliability guarantee:        Lower than explicit selection — auto may
                                  route to a different model depending on conditions

  Developer guidance:
    [ ] Cannot pin GPT-5.3-Codex explicitly — must use auto or a different model
    [ ] Auto may still select GPT-5.3-Codex, but this is not guaranteed
    [ ] Check the GitHub Education Community for feedback from other students
    [ ] Monitor GitHub changelog for restoration or further narrowing of picker

  Related resources (per changelog):
    - GitHub docs: supported models for Copilot
    - GitHub Education Community discussion forum
```

*Source: Derived from GitHub Copilot official changelog, April 27, 2026*

## Cross-References

- **Corroborates** `docs-github-copilot-individual-plan-changes.md` Claim 8 ("to ensure service reliability and a sustainable Copilot experience for all users"): The rationale in that source (April 20, 2026 plan changes) and this source (April 27, 2026 Student picker change) are parallel — both frame model access restrictions as reliability measures. This source extends the pattern one week later to the Student tier specifically. Together they show GitHub applying a consistent reliability-driven restriction rationale across its entire Individual plan family (Free, Pro, Pro+, Student) during the usage-based billing transition.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` Claim 3 (auto pool includes GPT-5.3-Codex as of April 17, 2026): The Student plan changelog says GPT-5.3-Codex "remains available through auto model selection." This is consistent with GPT-5.3-Codex being in the CLI auto pool. The consistency across two separate auto selection contexts (CLI and the web Copilot picker) suggests GitHub's auto model pool is a shared resource list, not surface-specific.

- **Extends** `docs-github-copilot-gpt52-deprecation.md` Claim 2: That source (May 1, 2026) designated GPT-5.3-Codex as the suggested replacement for GPT-5.2-Codex in general Copilot. This source (April 27, 2026) reveals that GPT-5.3-Codex is removed from the Student picker three days before that deprecation announcement. The replacement chain (GPT-5.2-Codex → GPT-5.3-Codex) now has a product-tier asterisk: on the Student plan, GPT-5.3-Codex as a replacement is accessible only via auto, not via explicit selection. Practitioners migrating Student users from GPT-5.2-Codex to GPT-5.3-Codex cannot do so via explicit picker selection on the Student tier.

- **Extends** `docs-github-copilot-individual-plan-changes.md` Claims 5 and 6 (Opus removed from Pro; Opus 4.7 available only on Pro+): Prior to this source, the corpus documented model access tiering between Pro and Pro+ (Opus availability). This source introduces a third tier in the comparison: Student has a more restricted picker than Pro, which has a more restricted picker than Pro+ (which retains Opus). The access ladder is: Student (most restricted picker) → Free → Pro → Pro+ (most model access). This is the first source to place Student explicitly below Free and Pro in terms of model picker capabilities.

- **Contradicts**: None. This source narrows what the Student picker offers; it does not contradict any prior claim about what models exist or what auto selection does. The GPT-5.3-Codex deprecation note's claim that GPT-5.3-Codex is a "suggested alternative" for general Copilot is not contradicted — the Student-specific restriction is a product-tier overlay, not a general reversal.

- **Novel**:
  - First source in corpus to document a "picker-removal with auto-retention" mechanism — a third access state beyond "available for explicit selection" and "fully deprecated." Prior deprecations removed models from both explicit selection and auto; this source shows a model can be removed from explicit selection while remaining in the auto pool. This is a new model lifecycle state the guide has not documented.
  - First documentation of product-tier model access differentiation specifically for the Student (educational free) tier versus other Individual plans. Prior sources documented Pro vs. Pro+ differences; this is the first Student-specific access restriction in the corpus.
  - First explicit connection in corpus between model picker restrictions and a billing model transition (usage-based billing) as the stated driving mechanism.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Third model access state — picker-removed but auto-retained**: Add a note that Copilot model access has at least three states: (1) fully available for explicit selection, (2) picker-removed but auto-accessible, and (3) deprecated/removed entirely. The Student plan GPT-5.3-Codex case is the first example of state (2). Practitioners building harnesses that rely on explicit model pinning should test their configurations against the actual model picker, not against the model's "availability" in auto or documentation.
- **Auto selection is not an equivalent substitute for explicit pinning**: The changelog frames auto as a direct substitute ("match each request with the strongest model for the job"), but `docs-github-copilot-cli-auto-model-selection.md` Claim 2 documents that auto routes on plan + policies + rate-limit pressure, not task type. Harnesses that depended on explicit GPT-5.3-Codex selection on Student cannot reproduce that dependency via auto. This is a configuration drift risk: a harness written against the Student picker before April 27 will silently change behavior if it relied on GPT-5.3-Codex selection.

### Chapter 05: Team Adoption / Enterprise Governance

- **Student plan model access is narrower than individual paid plans**: Teams with student developer programs (GitHub Education, academic teams, boot camps) should document that the Student plan picker is a subset of the Pro/Pro+ picker. Model access planning for student developers must account for this tier ceiling. If a workflow requires explicit Codex-family model selection, the Student plan no longer supports it for GPT-5.3-Codex.
- **Model picker restrictions as a billing transition mechanism**: The connection to usage-based billing is a signal for governance planning. As GitHub transitions Individual plans to usage-based billing, model picker access may continue to shift — models may move between the "available for explicit selection," "auto-only," and "deprecated" states as the billing mechanism stabilizes. Teams advising individual developers should treat the current Copilot Individual plan model picker as unstable and monitor GitHub's changelog for picker-level changes, not just full deprecations.
- **Educational tier governance**: This is the first source documenting GitHub treating the Student plan as a separate governance category for model access, not just a "Free with educational verification" variant. Teams building onboarding guidance for student developers should reference the Student plan's specific model access constraints, separate from guidance for Free, Pro, or Pro+ users.

## Extraction Notes

1. **Source is very short**: The changelog is approximately 200 words. All substantive claims are captured in the six claims above.
2. **WebFetch returned summaries, not raw HTML**: Both fetches returned structured markdown summaries rather than verbatim page text. Verbatim quotes (Claims 1, 2, and 5) were consistent across both fetches and are presented with high confidence. For Claims 3 and 4 (rationale and billing transition context), exact wording could not be reconstructed with confidence — these are marked as paraphrased in Our assessment and tagged `(no direct quote; see paraphrase in Our assessment)`.
3. **"Temporary" modifier not verifiable**: The changelog describes the measures as "temporary" but gives no timeline or reversal condition. This note does not speculate about when or whether GPT-5.3-Codex returns to the Student picker.
4. **Auto model selection mechanics**: The changelog does not specify whether "auto model selection" on the Student plan uses the same 0x–1x multiplier-bounded pool documented in `docs-github-copilot-cli-auto-model-selection.md` Claim 3, or whether the Student auto pool is separately constrained. GPT-5.3-Codex is in the CLI auto pool (per that note), so Student auto availability is plausible, but the exact Student auto pool composition is not confirmed in this source.
5. **No contradictions to file**: The picker removal is a product-tier-specific overlay on the existing model landscape. No existing source note claims that Student plan access is equivalent to Pro or Pro+ picker access; no claim is directly contradicted. No contradiction issue required.
