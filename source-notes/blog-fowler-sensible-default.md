---
source_url: https://martinfowler.com/bliki/SensibleDefault.html
source_type: blog-post
title: "Bliki: Sensible Default"
author: Martin Fowler
date_published: 2026-09-29
date_extracted: 2026-09-30
last_checked: 2026-09-30
status: current
confidence_overall: emerging
issue: "#3804"
---

# Bliki: Sensible Default

> Fowler's short bliki entry defines "sensible default" as a practice expected absent overriding context, deliberately contrasted with "best practice", and gives the vocabulary (and Thoughtworks lineage) for treating team practices as reassessable starting points.

## Source Context

- **Type**: blog-post (martinfowler.com bliki entry; no AI content)
- **Author credibility**: Martin Fowler, Chief Scientist at Thoughtworks, long-standing authority on software design and agile practice. He is relaying a term popularized inside Thoughtworks by Evan Bottcher, not originating it.
- **Scope**: A definition plus provenance and rationale. It does not list the defaults themselves (it links to a Thoughtworks playbook), contains no AI-specific discussion, no data, and no examples beyond three one-line illustrations. It is a vocabulary source, not an evidence source.

## Extracted Claims

### Claim 1: A sensible default is a practice that should be used absent overriding context
- **Evidence**: Definition by an authority; illustrated with three examples (version control, separating UI from domain logic, automated deployment pipelines). No empirical data.
- **Confidence**: settled (as a definition; it is a convention, not an empirical claim)
- **Quote**: "A Sensible Default is a practice that, absent some overriding context, should be used when carrying out a certain kind of task."
- **Our assessment**: Clean and usable. It gives the guide a label for practices that are strong baselines but not universal. The article's examples are all pre-AI, so which AI-native practices qualify is left to us.

### Claim 2: "Sensible default" is deliberately contrasted with "best practice" because the latter implies it should always be done
- **Evidence**: Fowler's reasoning about terminology.
- **Confidence**: settled
- **Quote**: "Folks dislike calling things “best practice” because that term implies a general presumption that the best practice is something we should always expect to do."
- **Our assessment**: Directly relevant to how the guide words recommendations. Most AI-engineering advice is young and context-dependent, so "default, reassess on context change" is the more defensible register than "best practice".

### Claim 3: A default should be reassessed in new contexts and can, and should, be overridden when circumstances change
- **Evidence**: Definitional; reinforced by the Agile-principle and Tech Radar references in Claim 6.
- **Confidence**: settled
- **Quote**: "A “sensible default”, however, is something that should be reassessed in a new context, something that can (and should) be overridden when circumstances change."
- **Our assessment**: Note "can (and should)": overriding is expected behaviour, not an exception. The source does not say how to detect that the context has changed, which is the hard part.

### Claim 4: Overriding a default carries an obligation to justify it
- **Evidence**: Evan Bottcher's formulation, quoted by Fowler.
- **Confidence**: emerging (single practitioner's norm, no outcome data)
- **Quote**: "Do these practices, or do better, and be prepared to explain why you've chosen some other way."
- **Our assessment**: This is the operational rule: the default sets the burden of proof, not the answer. It pairs naturally with lightweight decision records (see the Bennett post under Extraction Notes). The source doesn't prescribe a mechanism.

### Claim 5: The concept originated as a known-good starting point, popularized within Thoughtworks by Evan Bottcher
- **Evidence**: Fowler's attribution; he says Bottcher got the name from James Ross and was seeking "a known-good starting point".
- **Confidence**: anecdotal (provenance narrative; Fowler himself says he doesn't know whether a parallel Steve Bennett post was the origin)
- **Quote**: "I first heard the term when it was popularized within Thoughtworks by Evan Bottcher."
- **Our assessment**: Useful for citation hygiene only. Attribute the term to Thoughtworks/Bottcher, not to Fowler.

### Claim 6: Defaults earn their status through repeated use, teams must know their limits, and they must be reassessed regularly
- **Evidence**: Thoughtworks practice: a published playbook of defaults and the Technology Radar as the reassessment mechanism; the twelfth agile principle cited as grounding.
- **Confidence**: emerging (organizational practice, asserted by a participant)
- **Quote**: "They are our defaults because we've used them in many situations and found them to be effective."
- **Our assessment**: Defaults are legitimized by track record across contexts, which is a high bar for AI practices less than two years old. Applied to this guide: most AI-native defaults should be labelled provisional and carry a re-check date. The Fowler text also says "We also reassess these defaults regularly - this is the heart of the Thoughtworks Technology Radar."

## Concrete Artifacts

```
Definition (Fowler, martinfowler.com/bliki/SensibleDefault.html):
"A Sensible Default is a practice that, absent some overriding context,
  should be used when carrying out a certain kind of task."

Evan Bottcher, quoted in the article:
"A sensible default is what we'd expect you to do, the practices to apply,
    if there are no hard constraints in the environment. Do these practices, or
    do better, and be prepared to explain why you've chosen some other way."

Examples given: use version control; separate UI logic from domain logic;
automate deployment pipelines.
```

## Cross-References

- **Corroborates**: None directly. Existing notes use "sensible default" only descriptively, e.g. `docs-github-copilot-security-validation-third-party-agents.md` (Our assessment on inheriting Copilot config) and `blog-vercel-workflow-sdk-payload-compression.md` (compression-threshold assessment). This note supplies the primary definition those uses implicitly rely on.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-thoughtworks-gall-supervisory-engineering.md` Claim 3 (and Claim 8), which says engineering standards should be codified explicitly so agents don't invent design patterns. A sensible-defaults playbook is one concrete form that codified baseline could take, with the override-and-explain rule governing deviations.
- **Novel**: The defaults-vs-best-practice vocabulary and the "explain deviations" burden-of-proof norm; nothing equivalent exists in the corpus.

## Guide Impact

- **Chapter 00 (Principles)**: Consider adopting "sensible default" wording for recommendations that are strong but context-dependent, distinguishing them from invariants. Cite this note for the definition. The article is silent on AI, so any mapping of specific AI practices to "default" status needs other sources.
- **Chapter 05 (Team Adoption)**: Candidate framing for team playbooks: publish defaults, require a stated reason to deviate (Claim 4), and schedule reassessment (Claim 6). Evidence is organizational opinion, so present as a pattern, not a proven result.
- **Chapter 02 (Harness Engineering)**: Weak impact. Harness config (CLAUDE.md conventions, hooks) could be described as a team's agent-facing defaults, but this source doesn't make that link.

## Extraction Notes

- The article is about 5 short paragraphs; fully read via the raw HTML. Confidence is `emerging`, not `settled`, because the source is a definitional opinion piece without outcome data, and its AI relevance is our inference.
- Followed two linked pages. Steve Bennett, "The Power of Sensible Defaults" (https://stevebennett.co/posts/the-power-of-sensible-defaults): defines a sensible default as "a practice, language, framework or tool adopted as the default choice for an engineering team", says deviation is fine "providing it's a considered decision", and recommends ADRs. Thoughtworks sensible-defaults page (https://www.thoughtworks.com/insights/topic/sensible-defaults): gives four reasons for defaults (less repeated decision-making, faster workflows, consistency, quicker onboarding) and points to a playbook. These were read via a summarizing fetch tool, so their wording is not treated as verbatim-verified and is not used in Claims above.
- The triage comments on the issue disagreed on novelty (high/medium/medium-high) and proposed chapters; the assessment here is that the piece is conceptually useful but thin.
