---
source_url: https://martinfowler.com/bliki/GeneratedGlossary.html
source_type: blog-post
title: "Generated Glossary"
author: Martin Fowler
date_published: 2026-11-12
date_extracted: 2026-11-13
last_checked: 2026-11-13
status: current
confidence_overall: anecdotal
issue: "#4696"
---

# Generated Glossary

> Fowler proposes having an LLM draft a domain glossary from an organization's own text, having human experts review it, keeping it in version control, and scoping it per Bounded Context so other agents can consult it. This is a proposed practice with no metrics or code.

## Source Context

- **Type**: blog-post (martinfowler.com bliki, short)
- **Author credibility**: Martin Fowler (Thoughtworks) is a long-standing authority on Domain Driven Design and software design. Here the evidence is his conversations with practitioners; the acknowledgements credit Eric Nagler and Unmesh Joshi for relating their experiences doing this.
- **Scope**: Technique for generating, reviewing, storing and using a domain glossary for LLM consumption. Contains no code, config, metrics, tooling names or experience report. Links out to Bounded Context, Agentic Engineering and "Sensors in a harness" pages, which were not followed (the source's own body carries the claims).

## Extracted Claims

### Claim 1: Specialized organizational vocabulary is foreign to LLMs because it is absent from training data, which hurts task effectiveness; a generated glossary available to other LLMs mitigates this
- **Evidence**: Assertion by author; no measurements.
- **Confidence**: anecdotal
- **Quote**: "Such words and specialized meanings will be foreign to an LLM because they aren't in its training set, making it harder for the LLM to be effective when doing tasks in that domain."
- **Our assessment**: Plausible and consistent with the context-gap theme in other notes, but unquantified. No before/after comparison is given.

### Claim 2: Source material can be any organizational text (documents, emails, chat logs), optionally transcripts
- **Evidence**: Author assertion.
- **Confidence**: anecdotal
- **Quote**: "The sources for the LLM can be any material within the organization concerned such as documents, emails, and chat logs."
- **Our assessment**: Practical, but raises privacy/access-control questions the post does not address (emails and chat logs may contain sensitive material and be published into a shared glossary).

### Claim 3: The extractor should look for single words and multi-word phrases, and specifically for known terms used in unfamiliar ways, which cause the most confusion
- **Evidence**: Author assertion.
- **Confidence**: anecdotal
- **Quote**: "The generator should be asked to identify terms that are new to it, but also known terms that are being used in unfamiliar ways. The latter can often cause the most confusion."
- **Our assessment**: Useful, non-obvious prompting guidance: the dangerous terms are homonyms rather than novel jargon, since the model silently applies its generic meaning.

### Claim 4: Definitions should be dictionary-style, precise and concise, with alternative definitions annotated by the context where they apply
- **Evidence**: Author assertion.
- **Confidence**: anecdotal
- **Quote**: "Some terms may be used in different ways, in which case the LLM should provide alternative definitions, with a note as to what context the differences appear in."
- **Our assessment**: Good entry schema: term, definition(s), context per definition.

### Claim 5: Human domain experts must review the LLM draft to correct misinterpretations
- **Evidence**: Author assertion.
- **Confidence**: anecdotal
- **Quote**: "Once we have a draft glossary, then  human experts in that domain should review it, and amend it for cases where the LLM has got the wrong ends of sticks."
- **Our assessment**: Agree. It matches the human-validation points in the Xiong and Patole notes. The post does not say how much review effort is needed.

### Claim 6: Store the glossary in a token-cheap, consultable form, in version control, with scheduled refresh by agents and humans
- **Evidence**: Author assertion.
- **Confidence**: anecdotal
- **Quote**: "We should set up a schedule to review and refresh the glossary at regular intervals, by agents and humans. We should keep it in version control, so we can see how it changes over time."
- **Our assessment**: Treats the glossary as a living artifact, consistent with context-as-lifecycle claims elsewhere. No cadence or staleness detection is given.

### Claim 7: Prefer separate glossaries per Bounded Context over a single standard glossary; a glossary's value is often showing differing usage, not fixing one definition
- **Evidence**: Author's experience ("I've yet to see that work") and DDD theory.
- **Confidence**: emerging (backed by DDD canon, but not by data here)
- **Quote**: "I'd urge everyone to resist any temptation to create a single, standard, glossary - I've yet to see that work."
- **Our assessment**: Strong, experience-based position. Aligns with Gall's domain-boundary argument against a monolithic knowledge graph. Source code is called out as a bounded context of its own.

### Claim 8: Comparing glossaries across contexts (especially code-derived vs. human-text-derived) is instructive, and LLMs can be asked to describe the differences
- **Evidence**: Author assertion.
- **Confidence**: anecdotal
- **Quote**: "Comparing a source-code derived glossary to a human text can be particularly instructive."
- **Our assessment**: Interesting and cheap, but untested here. Related to the cross-source reconciliation step in the Xiong note.

### Claim 9: For large glossaries, load only terms plus links initially and fetch full definitions on demand
- **Evidence**: Author assertion.
- **Confidence**: anecdotal
- **Quote**: "If the glossary is large, it can be worthwhile to only include the terms and links to definitions as part of the initial context."
- **Our assessment**: The same progressive-disclosure pattern as index-first loading in the Nandyala/Pani note, applied to vocabulary.

### Claim 10: Glossaries can inform code generation, and harness sensors can check naming in internals and UI
- **Evidence**: Author assertion; no sensor implementation described.
- **Confidence**: anecdotal
- **Quote**: "Sensors in a harness can check for this usage, both in the internals of the software and in the user-interface."
- **Our assessment**: A concrete, cheap computational-sensor idea (lint for forbidden or internal terms), but only stated, not demonstrated.

### Claim 11: Generated code or documents can introduce new bounded contexts; internal names should not leak into customer-facing UI
- **Evidence**: Author reasoning.
- **Confidence**: anecdotal
- **Quote**: "internal names that may be used within an organization should not be exposed in a customer-facing UI, because such internal terms are likely to be only confuse a customer."
- **Our assessment**: Good concrete use case: the customer is a distinct bounded context. (The quote reproduces the source's typo "to be only confuse".)

### Claim 12: Glossaries should include do-not-use terms with replacements, and deprecated terms with the period they are in effect
- **Evidence**: Author assertion.
- **Confidence**: anecdotal
- **Quote**: "It's often useful for glossaries to include terms that should not be used, in which case it includes advice on what other term to use instead."
- **Our assessment**: Turns the glossary into a normative artifact, which makes it enforceable by sensors (Claim 10).

### Claim 13: Specialized language is a common difficulty in large-organization agent work; a generated glossary is a simple, useful part of the larger domain-modeling/ontology/context-layer effort
- **Evidence**: "In my conversations with people working with agents in large organizations"; no named cases besides the acknowledgements.
- **Confidence**: anecdotal
- **Quote**: "Getting LLMs to generate a glossary is a simple, but useful, part of this work."
- **Our assessment**: Positions the glossary as the low-cost entry point to heavier ontology work.

## Concrete Artifacts

Workflow described in the post (paraphrased by us from the body; no code or config appears in the source):

```
1. Gather org text (docs, emails, chat logs, optional transcripts)
2. LLM pass 1: extract terms (single words + multi-word phrases);
   flag (a) new terms, (b) known terms used unfamiliarly
3. LLM pass 2: dictionary-style definitions, precise and concise;
   alternative definitions annotated with context
4. Human domain-expert review and amendment
5. Publish in LLM-consultable, token-minimal form, in version control
6. Scheduled review/refresh by agents and humans
7. One glossary per Bounded Context (code is one); include do-not-use /
   deprecated terms with replacements and effective period
8. Large glossary: terms + links in initial context, definitions on demand
```

## Cross-References

- **Corroborates:**
  - `blog-thoughtworks-nandyala-pani-bounded-context-bounded-attention.md` Claim 4 (index-first loading: short index, load only the needed path); Fowler's terms-plus-links is the same pattern for vocabulary.
  - `blog-thoughtworks-gall-layered-context-enterprise-data.md` Claim 5 (carve agentic context along domain boundaries, not one monolith) and Claim 4 (don't push large reference data into context upfront).
  - `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 8 (a shared type name across systems does not imply shared meaning) matches the multiple-definitions-per-context idea; Claim 10 (domain experts validate AI-identified gaps) and Claim 11 (context as a version-controlled, continuously updated asset) match Claims 5-6 here.
  - `blog-thoughtworks-patole-context-real-bottleneck-ai-agents.md` Claim 7 (context as a continuous lifecycle) and Claim 8 (departmental accountability for business definitions).
- **Contradicts:** None found. No contradiction issue filed.
- **Extends:** The above notes by supplying a concrete, low-cost technique (LLM-drafted, expert-reviewed glossary) for the semantic/context layer they describe at a higher level. Also `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` (same author, AI-ready data) at the vocabulary level.
- **Novel:** Prompting the extractor for known terms used in unfamiliar ways; do-not-use/deprecated terms with replacements and effective periods; glossary-as-harness-sensor input for naming in code and UI; source code as its own bounded context glossary; comparing code-derived vs. human-text-derived glossaries.

## Guide Impact

- **Chapter 04 (context engineering)**: Add a short "generated domain glossary" subsection under domain/organizational context: the LLM-draft → expert-review → version-controlled → scheduled-refresh workflow, one glossary per bounded context, and terms-plus-links loading. Cite alongside Nandyala/Pani (index-first loading) and Gall (domain-boundary carving). Label it a proposed practice without measured results.
- **Chapter 02 (harness engineering)**: Mention a naming/vocabulary sensor driven by the glossary's do-not-use list (code identifiers, UI strings) as a computational sensor candidate. Flag it as an idea stated in the source, not a demonstrated implementation.
- **Chapter 05 (team adoption)**: Domain-expert review and ownership of glossary entries fits existing ownership advice (Patole Claim 8).

## Extraction Notes

- Read the full post (short; about 700 words) via the page HTML. All quotes are verbatim, including the source's typo noted in Claim 11 and the double space in Claim 5.
- The post has no code, metrics or named case studies, so confidence is `anecdotal` overall. The Bounded Context relies on established DDD, which is why Claim 7 is graded `emerging`.
- Linked pages (Bounded Context, Agentic Engineering, harness sensors, context layers) were not followed; they are background definitions and not needed for the claims.
- Cross-referenced claim numbers were checked against the headings in the cited notes.
