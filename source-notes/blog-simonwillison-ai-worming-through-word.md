---
source_url: https://simonwillison.net/2026/Jul/29/ai-worming-through-word/
source_type: blog-post
title: "AI Worming through Word"
author: Simon Willison (linking Håkon Måløy)
date_published: 2026-07-29
date_extracted: 2026-09-28
last_checked: 2026-09-28
status: current
confidence_overall: emerging
issue: "#2413"
---

# AI Worming through Word

> A self-replicating, document-borne prompt injection in Copilot for Word shows that LLM-generated output becomes an attack carrier, and that a 144-day vendor coordination window produced no mitigation for the whole vulnerability class.

## Source Context

- **Type**: blog-post (link blog) pointing to a primary vulnerability write-up: Håkon Måløy, "Context Collapse, Part 3 - AI Worming through Word" (https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/, published 2026-07-28, updated 2026-07-30).
- **Author credibility**: Willison is a widely read commentator on prompt injection. Måløy is the researcher who ran the disclosure with Microsoft MSRC. The claims are the researcher's own; Willison contributes framing ("first one I've seen").
- **Scope**: One attack class (cross-domain prompt injection, XPIA) against Copilot for Word, its propagation, and the disclosure timeline. No payloads are published (class-level disclosure). Not independently reproduced by us.

## Extracted Claims

### Claim 1: Hidden instructions in a source document can make Copilot both manipulate the draft and copy the instructions into its output, turning the output into a new carrier
- **Evidence**: Måløy's PoC and disclosure to MSRC, as quoted by Willison.
- **Confidence**: emerging
- **Quote**: "Copilot may then also copy the hidden instructions into the resulting document, turning that document into a new carrier."
- **Our assessment**: Credible and consistent with known prompt injection. What is new is the copy step, which converts a one-shot injection into persistent, propagating state.

### Claim 2: The worm keeps propagating without the attacker's original document
- **Evidence**: Måløy's staged PoC (attacker doc, then infected report, then downstream reuse).
- **Confidence**: emerging
- **Quote**: "the instructions can trigger again and propagate into further documents, even without the attacker's original document being present."
- **Our assessment**: This defeats "remove the malicious file" incident response. Every generated artifact from a tainted session must be treated as suspect.

### Claim 3: Willison says this is the first hidden-text injection he has seen that deliberately self-replicates
- **Evidence**: Willison's own survey of prior cases (white-on-white text already used in job applications).
- **Confidence**: anecdotal
- **Quote**: "this is the first one I've seen that deliberately copies instructions to self-replicate itself."
- **Our assessment**: A "first" claim from one observer, phrased personally. Do not present as established fact. The mechanism is what matters.

### Claim 4: Microsoft had 144 days and there is still no mitigation covering the full class
- **Evidence**: Disclosure timeline in the primary post: reported 2026-03-06, confirmed 03-31, first mitigation 04-03, new variant 04-09, disclosure postponed twice, public 07-28. The primary post says payload-specific fixes and model upgrades (to GPT-5.5) did not close the class, and that the attack reproduced with GPT-5.6.
- **Confidence**: emerging
- **Quote**: "It was responsibly disclosed to Microsoft who then had 144 days to work on a fix, but so far (unsurprisingly) there's no mitigation that covers the full class of attack."
- **Our assessment**: Strong signal that patching individual payloads is whack-a-mole. Timeline details come from the primary post via a fetch summary, not read by us directly (see Extraction Notes).

### Claim 5: Formatting is not a defence, because the concealment only fools humans
- **Evidence**: Måløy states Copilot strips formatting before the model sees text, so white-on-white hiding affects only human reviewers.
- **Confidence**: emerging
- **Quote**: "Copilot strips all text formatting like color and font size before passing text into the underlying Large Language Model."
- **Our assessment**: Human review of rendered documents cannot catch this. Any review step must operate on extracted text, which is what the model sees.

### Claim 6: The weakness is architectural; any LLM in a trusted workflow must assume compromise at some rate
- **Evidence**: Måløy's argument that the inspected content participates in the inspection, and that layering LLM detectors becomes "LLMs all the way down".
- **Confidence**: emerging
- **Quote**: "Any system that integrates an LLM into a trusted workflow today must assume that attacker-controlled content entering the model's context will result in compromise at some rate."
- **Our assessment**: Matches the provenance/role-confusion analysis in our corpus. We agree with the design implication (assume breach, limit blast radius) but the "at some rate" wording is qualitative; no measured rate is given.

### Claim 7: The harm is silent integrity corruption laundered through trusted internal channels
- **Evidence**: Måløy's scenario: a downloaded market analysis leads to a financial report with altered figures, which colleagues then reuse as source material.
- **Confidence**: anecdotal
- **Quote**: "Once malicious instructions are embedded in generated content, they may persist across documents, be redistributed by legitimate users, and be reintroduced into new contexts."
- **Our assessment**: A hypothetical scenario, not observed in the wild. It is a useful threat model for any workflow where AI outputs feed later AI inputs.

### Claim 8: Withholding disclosure was rejected; the author disclosed at class level, not payload level
- **Evidence**: Måløy's stated rationale (defenders cannot reduce unknown risk; 144 days yielded no robust fix).
- **Confidence**: anecdotal
- **Quote**: "Defenders cannot reduce exposure to a risk they are unaware of"
- **Our assessment**: An ethics and process datapoint, not a technical claim. Relevant to how the guide advises teams to treat vendor "fixed" claims.

## Concrete Artifacts

```
Propagation chain (Måløy, via Willison's quoted excerpt and the primary post):
1. Attacker doc with hidden (white-on-white) instructions -> attached as source in Copilot for Word
2. Copilot drafts new doc: (a) manipulates content per hidden instructions,
   (b) re-embeds the hidden instructions in the output
3. Output doc shared/reused as source in another Copilot session -> repeat from 2,
   attacker's original doc no longer needed

Disclosure timeline (primary post): 2026-03-06 report to MSRC; 03-31 confirmed;
04-03 first mitigation; 04-09 variant found; 07-14 model upgrade to GPT-5.5;
07-15 reproduced on GPT-5.6; 07-28 public disclosure (144 days total).

Interim guidance (primary post, paraphrased): treat external documents as untrusted,
review attachments, inspect Copilot output before sharing.
```

## Cross-References

- **Corroborates**: `blog-simonwillison-prompt-injection-role-confusion.md`, Claim 8 (without provenance-based role perception, injection defence is structurally non-durable) and Claim 5 (frontier models still fail automated role-confusion attacks). The Word worm is a production-scale example of the persistence those claims predict.
- **Contradicts**: none found; no contradiction issue filed.
- **Extends**: `blog-anthropic-ciso-guide-agentic-ai.md` and `blog-anthropic-claude-code-auto-mode.md` (prompt injection in threat models). Those treat injection as a single-shot input threat; this adds output-as-carrier propagation across sessions and users.
- **Related**: `blog-simonwillison-calif-weworm.md` (a worm using AI-assisted exploit development, not a prompt-injection worm; no mechanism overlap).
- **Novel**: Self-replicating prompt injection through generated documents; a documented case where vendor mitigations plus a model upgrade failed to close the class; the point that formatting-based concealment is invisible to the model-side pipeline.

## Guide Impact

- **Chapter 08 (Security)**: Add a "generated output as attack carrier" threat: outputs derived from untrusted inputs inherit their taint, and later sessions using them as context are exposed. Recommend provenance labels on AI-generated artifacts and treating them as untrusted where derived from external inputs.
- **Chapter 04 (Guardrails)**: Add that review of rendered documents does not catch hidden-text injection; checks should run on the text the model receives. Also note that vendor payload-level fixes and model upgrades do not close the class, so guardrails should limit blast radius instead.
- **Chapter 02**: When designing AI-in-the-loop document pipelines, avoid feeding AI outputs back as trusted inputs without a trust boundary.

## Extraction Notes

- The Willison post is a short link-blog entry; it was read in full. I followed its main link to Måløy's primary post. That page was retrieved through a summarizing fetch tool rather than raw text, so the Måløy quotes (Claims 5-8) and the disclosure timeline should be spot-checked against the primary URL. Claims 1-4 quotes are copied from Willison's page.
- Quotes in Claims 1-2 are Willison's block-quote of Måløy's text.
- The triage comments mention "style-based role boundaries" as the closing argument; this is from our role-confusion note, not from this source, and is not attributed to it here.
