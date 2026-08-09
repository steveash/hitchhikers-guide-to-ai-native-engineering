---
source_url: https://simonwillison.net/2026/Aug/2/open-letters/
source_type: blog-post
title: "Open letters about AI development"
author: Simon Willison
date_published: 2026-08-02
date_extracted: 2026-08-09
last_checked: 2026-08-09
status: current
confidence_overall: emerging
issue: "#2582"
---

# Open letters about AI development

> Simon Willison's short (~330-word) summary of three competing July 2026
> open letters on AI policy — Microsoft's pro-open-weights letter (235
> signers, including a later-signing OpenAI), Anthropic's counter-position
> (declining to sign, warning on authoritarian AI and distillation), and the
> employee-signed "Pacing the Frontier" letter (1,324 signers) calling for
> government-backed international pacing of automated AI research — with
> direct quotes from all three primary documents and three concrete examples
> of AI-research automation (Anthropic/Claude Code, OpenAI/Sol, Kimi K3) cited
> as the reason the pacing concern is being taken seriously.

## Source Context

- **Type**: blog-post (Simon Willison's "note" post type, originally written
  as a section of his sponsors-only newsletter and then also published as a
  standalone public post). Auto-discovered via the `simon-willison` trusted
  feed. Full text obtained via direct `curl` against `simonwillison.net`
  (not an AI-summarizing fetch tool) to guarantee verbatim quotes per
  MINER.md §2a.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this repo. For this post he acts mostly as a curator/synthesizer
  — he did not sign or write any of the three letters — but he adds his own
  editorial framing (e.g., noting Anthropic's conspicuous absence from the
  first letter's signatory list, and noting the "one surprising note" in the
  first letter's stance on distillation) and reads all three primary
  documents directly rather than relying on secondhand reporting.
- **Scope**: Covers exactly three primary documents, summarized and
  block-quoted, plus a short paragraph of Willison's own framing at the top
  and bottom. It does **not** independently verify the letters' full
  signatory lists, does not cover the Pacing the Frontier letter's full
  text (quotes only its core request), and does not analyze the letters'
  likely policy impact — it is a pointer/summary post, not investigative
  reporting. This Miner also followed 8 of the post's inline links (see
  Extraction Notes) to confirm quote accuracy and pull additional context
  (e.g., the specific Anthropic institute page backing the "80% of code"
  figure), staying within MINER.md §1's up-to-5-substantive-pages guidance
  by treating the three letter URLs as primary-source confirmation rather
  than separate "linked pages" requiring their own full extraction.

## Extracted Claims

### Claim 1: "Open Weights and American AI Leadership," shepherded by Microsoft and dated July 24, 2026, was signed by 235 AI-adjacent companies including NVIDIA, Amazon, Y Combinator, The Linux Foundation, and (as a later signer) OpenAI — with Anthropic conspicuously absent
- **Evidence**: Willison's direct report, cross-checked against the letter's host page.
- **Confidence**: settled (specific, named signer list and date, independently confirmable at the linked source)
- **Quote**: "was shepherded by Microsoft, dated July 24th, and signed by 235 AI-adjacent companies including NVIDIA (see Jensen's first ever tweet), Amazon, Y Combinator, The Linux Foundation, and (a later signer) OpenAI."
- **Our assessment**: A verifiable, dated industry-alignment fact. The detail that NVIDIA CEO Jensen Huang's *first-ever tweet* was used to announce signing is a striking, checkable indicator of how much weight labs are putting on public positioning here — worth citing as color for how seriously major vendors are treating this policy fight, not just Willison's opinion.

### Claim 2: The Microsoft-shepherded letter argues that concentrating advanced AI in a small number of closed models is itself a safety risk, not just an openness-vs-restriction tradeoff
- **Evidence**: Direct quote from the letter's own text, block-quoted by Willison.
- **Confidence**: settled (verbatim quote from a signed public letter)
- **Quote**: "Relying solely on closed models is not inherently safe: they can be breached, misused, or fail in ways that outsiders cannot detect. And concentrating advanced AI capabilities behind a small number of closed models compounds that risk. It results in a small number of single points of failure, weakens competition, and leaves critical technology in the hands of a few providers."
- **Our assessment**: This is the letter's core rhetorical move — reframing "open weights are risky" into "closed concentration is *also* risky, and arguably more so" (single points of failure, weakened competition). It's a policy argument, not an empirical one; the letter cites no incident or data point for "fail in ways that outsiders cannot detect" here. Useful primarily as the named industry counter-frame to restriction-focused safety arguments elsewhere in this corpus.

### Claim 3: The same letter explicitly endorses distillation ("using one model's outputs to help train or improve another") as a legitimate, widely-used technique that policymakers should not conflate with misappropriation
- **Evidence**: Direct quote from the letter's text; flagged by Willison himself as the letter's most surprising position.
- **Confidence**: settled (verbatim quote)
- **Quote**: "In shaping this ecosystem, policymakers should be careful not to conflate legitimate model-development techniques with misappropriation. Distillation, or the practice of using one model's outputs to help train or improve another, is a widely used technique for model improvement, evaluation, and validation. It reflects a long tradition of learning from, building upon, and improving existing technologies, a tradition that has helped drive innovation since the rise of the open-source software movement."
- **Our assessment**: This is the single sharpest point of documented industry disagreement in the source: 235 companies (including eventual signer OpenAI) publicly endorsing distillation as legitimate, three days before Anthropic publicly called for a "crack down on industrial-scale distillation operations" (Claim 5). Willison himself flags this as "the one surprising note in the letter" — the source presents both positions side by side without resolving them, so this note does the same. See Cross-References for how this intersects with the magnitude-of-distillation-benefit question already tracked in this corpus under contradiction #2536 (a related but distinct question — that one is about how *much* distillation helps Chinese labs' capabilities, this one is about whether distillation should be *policy-restricted* at all).

### Claim 4: Anthropic was notably absent from the Microsoft-led letter's signatories and instead published its own separate position statement three days later
- **Evidence**: Willison's direct observation plus a link to Anthropic's own statement.
- **Confidence**: settled (directly verifiable — Anthropic's absence from a public signatory list and publication of a separate, dated statement)
- **Quote**: "Notably absent from the signatures: Anthropic, who published their own response Our position on open-weights models three days later."
- **Our assessment**: Corroborates `blog-simonwillison-oxide-open-weight-revolution.md` Claim 8, which documents this same holdout live (via a podcast recorded July 31, before Anthropic's statement had fully registered in that conversation) and attributes it to Bryan Cantrill's real-time observation ("leaving only Anthropic and then Anthropic had a blog post"). This source is the more citable version: a written, dated, directly-linked confirmation from Willison's own subsequent post, rather than an in-the-moment podcast remark.

### Claim 5: Anthropic CEO Dario Amodei's response letter warns of authoritarian governments building more powerful AI than the US, of models being misused for cyberattacks or biological attacks, calls for a crackdown on industrial-scale distillation operations, but explicitly denies ever advocating a ban on open-weight models
- **Evidence**: Direct quotes from Amodei's statement, block-quoted/paraphrased by Willison with the quoted phrases preserved.
- **Confidence**: settled (verbatim quoted phrases from a named CEO's public statement)
- **Quote**: "CEO Dario Amodei doubled down on the risk of authoritarian governments building \"AI models that are more powerful than those built by the US\", and models being \"misused to carry out cyberattacks or biological attacks\", and called for \"a crack down on industrial-scale distillation operations\", while also stating that \"Anthropic has never advocated for a ban on open-weights models\"."
- **Our assessment**: This is a carefully hedged position — Anthropic is not arguing against open weights per se, only against a specific practice (large-scale distillation) and specific downstream risks (authoritarian capability parity, cyber/bio misuse). This nuance matters for the guide: it would be inaccurate to characterize Anthropic's position as simply "anti-open-weights" (as the Microsoft letter's framing might imply by omission), and this source's verbatim quote is the cleanest documentation in the corpus of Anthropic's actual, narrower stated position. Compare against `blog-ronacher-gaslighting-openness.md`, which argues (about Anthropic specifically, among others) that "safety"-framed restriction language is often narrative cover for access control — this source doesn't resolve that skepticism, but it does supply the specific, checkable claims (crackdown on distillation *operations*, not weights; no ban advocacy) that such skepticism would need to engage with directly rather than argue against a straw-man "Anthropic wants to ban open weights" position.

### Claim 6: "Pacing the Frontier," published July 28, 2026, gathered 1,324 signatures from employees of frontier AI companies, including OpenAI's Chief Scientist Jakub Pachocki, Ilya Sutskever, and Anthropic's Dario Amodei and Jack Clark
- **Evidence**: Direct quote/paraphrase from Willison, describing the letter's signatory composition.
- **Confidence**: settled (specific signer count and named signatories, independently checkable at the linked letter)
- **Quote**: "featuring signatures from \"1,324 employees of frontier AI companies\" - with names like Jakub Pachocki (Chief Scientist, OpenAI), Ilya Sutskever (Safe Superintelligence Inc, previously OpenAI), Dario Amodei (Anthropic), Jack Clark (Anthropic) and more."
- **Our assessment**: Notably, this is an *employee*-signed letter (not a company-signed one like Claim 1), and it draws signatories from across labs that otherwise publicly disagree (OpenAI signed the pro-open-weights letter; Anthropic did not, yet Anthropic's own leadership signs this third letter alongside OpenAI's). This is new to the corpus and a useful data point: on the narrower question of "should development pace itself," there is cross-lab employee alignment even where company-level positions on open weights diverge sharply.

### Claim 7: The Pacing the Frontier letter's core request is for the US government to support an international effort to build the technical and governance tools needed to deliberately slow the frontier of automated AI development
- **Evidence**: Direct quote from the letter's own text.
- **Confidence**: settled (verbatim quote from a signed public letter)
- **Quote**: "We request that the U.S. government support an international effort to develop the technical and governance tools needed to deliberately pace the frontier of automated AI development."
- **Our assessment**: This is the most novel claim in the source for this corpus — no existing source note documents the Pacing the Frontier letter. It's a specific, actionable policy ask (government-backed *international* coordination on pacing tools) rather than a general "AI is moving too fast" sentiment, which is what makes it citable rather than just atmospheric.

### Claim 8: Willison frames the letter's urgency as grounded in three concrete, named examples of automated-AI-research acceleration already underway: Anthropic producing 80% of its own code with Claude Code, OpenAI's Sol model reducing end-to-end serving costs by 20%, and Kimi K3 being used to design a chip to serve a nano model built on its own architecture
- **Evidence**: Willison's own connecting argument, each example linked to its own primary source (Anthropic's institute page, OpenAI's GPT-5.6/Sol efficiency post, Kimi's K3 blog chip-design section).
- **Confidence**: emerging (each individual figure comes from the respective vendor's own first-party announcement, not independently audited by Willison or this note; Willison's contribution is the framing connecting the three as evidence for the letter's stated concern)
- **Quote**: "Their concern is intense competitive pressure combined with accelerated AI progress caused by automated AI research - and given that Anthropic produce 80% of their code with Claude Code, OpenAI had Sol reduce their end-to-end serving costs by 20%, and Kimi K3 designed a chip to serve a nano model built on its own architecture, you can see why people are taking that risk more seriously right now."
- **Our assessment**: These three figures function as the letter's implicit evidentiary backing in Willison's framing, but none are independently verified in this source — they are vendor self-reports linked, not audited. Treat as "why observers say they're worried," not as independently confirmed capability milestones. The Kimi K3 chip-design claim specifically echoes (and is likely the same underlying claim as) `blog-simonwillison-oxide-open-weight-revolution.md` Claim 10, which already flags that source's own account of this claim as unverified and hedged by one of the podcast speakers ("I don't think they actually like fabricated or anything") — this note's citation of the same claim, sourced independently via Kimi's own blog post, does not resolve that uncertainty but does show the claim persists in Willison's own framing weeks later without added verification.

## Concrete Artifacts

### Full post text (verbatim, via direct `curl` against simonwillison.net)

```
Open letters about AI development
2nd August 2026

I wrote this summary of the past few weeks of open letters as a section of
my sponsors-only newsletter but I've decided to share it here as well.

Open Weights and American AI Leadership was shepherded by Microsoft, dated
July 24th, and signed by 235 AI-adjacent companies including NVIDIA (see
Jensen's first ever tweet), Amazon, Y Combinator, The Linux Foundation, and
(a later signer) OpenAI.

It's clearly an argument designed to counter any instincts by the current
US government to ban or limit open weight models over "safety" concerns -
a reasonable consideration given what happened to Claude Fable 5!

Relying solely on closed models is not inherently safe: they can be
breached, misused, or fail in ways that outsiders cannot detect. And
concentrating advanced AI capabilities behind a small number of closed
models compounds that risk. It results in a small number of single points
of failure, weakens competition, and leaves critical technology in the
hands of a few providers. Open weight models, on the other hand, allow a
broad community of researchers and developers to examine their behavior,
identify vulnerabilities, develop safeguards, and improve them over time.

The one surprising note in the letter is that it comes out in support of
distillation, where models train on output from other models:

In shaping this ecosystem, policymakers should be careful not to conflate
legitimate model-development techniques with misappropriation. Distillation,
or the practice of using one model's outputs to help train or improve
another, is a widely used technique for model improvement, evaluation, and
validation. It reflects a long tradition of learning from, building upon,
and improving existing technologies, a tradition that has helped drive
innovation since the rise of the open-source software movement.

Notably absent from the signatures: Anthropic, who published their own
response Our position on open-weights models three days later. CEO Dario
Amodei doubled down on the risk of authoritarian governments building "AI
models that are more powerful than those built by the US", and models
being "misused to carry out cyberattacks or biological attacks", and
called for "a crack down on industrial-scale distillation operations",
while also stating that "Anthropic has never advocated for a ban on
open-weights models".

Then on July 28th Pacing the Frontier was published, featuring signatures
from "1,324 employees of frontier AI companies" - with names like Jakub
Pachocki (Chief Scientist, OpenAI), Ilya Sutskever (Safe Superintelligence
Inc, previously OpenAI), Dario Amodei (Anthropic), Jack Clark (Anthropic)
and more. Their core message:

We request that the U.S. government support an international effort to
develop the technical and governance tools needed to deliberately pace the
frontier of automated AI development.

Their concern is intense competitive pressure combined with accelerated AI
progress caused by automated AI research - and given that Anthropic produce
80% of their code with Claude Code, OpenAI had Sol reduce their end-to-end
serving costs by 20%, and Kimi K3 designed a chip to serve a nano model
built on its own architecture, you can see why people are taking that risk
more seriously right now.

Posted 2nd August 2026 at 4:16 am
Tags: ai, openai, generative-ai, llms, anthropic, ai-ethics
```

### Primary-source links cited in the post (confirmed via raw HTML link extraction)

```
"Open Weights and American AI Leadership" letter (Microsoft-hosted):
  https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/
Anthropic's response ("Our position on open-weights models"):
  https://www.anthropic.com/news/position-open-weights-models
Anthropic's distillation-detection post (linked from "distillation operations"):
  https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
"Pacing the Frontier" letter:
  https://www.pacingthefrontier.com
Anthropic institute page backing the "80% of code" claim:
  https://www.anthropic.com/institute/recursive-self-improvement
OpenAI post backing the "Sol / 20% serving cost reduction" claim:
  https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/
Kimi K3 blog post backing the chip-design claim:
  https://www.kimi.com/blog/kimi-k3#chip-design
Background link ("what happened to Claude Fable 5"):
  https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/
  (already covered in this corpus as blog-simonwillison-fable-mythos-access-directive.md)
```

## Cross-References

- **Corroborates**: `blog-simonwillison-oxide-open-weight-revolution.md` Claim
  8 (Anthropic as the sole major-lab holdout from the Microsoft-led letter)
  and Claim 9 (Anthropic's bio/chem/nuclear-risk rationale for declining) —
  this source provides the written, directly-quoted, dated confirmation of
  both, superseding the podcast's real-time, partially-hedged framing with
  Anthropic's own published statement language (Claim 5 above). Also
  corroborates that same note's Claim 10 (Kimi K3 chip-design claim,
  unverified/hedged there) by showing the claim persists, cited from Kimi's
  own blog, in Willison's later framing (Claim 8 above) without new
  verification.
- **Contradicts**: No new contradiction issue filed. The letter itself
  documents an unresolved industry disagreement (Microsoft-letter signers'
  pro-distillation stance, Claim 3, vs. Anthropic's call for a distillation
  "crack down," Claim 5) but this is the *subject* of the source, already
  presented by Willison as two sides without a resolution to pick — not a
  case of this source's claim opposing an existing settled claim in this
  corpus per MINER.md §4a. It is a related but distinct question from the
  already-tracked contradiction #2536 (magnitude of distillation's benefit
  to Chinese labs' capabilities specifically, from
  `blog-simonwillison-oxide-open-weight-revolution.md` Claim 4 vs.
  `blog-simonwillison-afraid-of-chinese-models.md` Claim 10) — that
  contradiction is about how much distillation helps, this source's tension
  is about whether distillation should be policy-restricted at all. Checked
  open `contradiction`-labeled issues before writing this section; found
  none covering the policy-legitimacy question specifically, but judged it
  does not meet the filing bar since the source itself surfaces both sides
  without asserting a corpus-level claim that would need adjudication.
- **Extends**: `blog-simonwillison-fable-mythos-access-directive.md` (the
  "what happened to Claude Fable 5" background link, government-mandated
  suspension of Fable 5/Mythos 5 access, used here as Willison's own
  justification for why "safety"-framed restriction arguments deserve
  scrutiny). `blog-simonwillison-open-source-ai-gap-map.md` and
  `blog-simonwillison-inkling-open-weights.md` (both document the
  open-weights ecosystem's technical/openness state; this source adds the
  policy layer sitting on top of that ecosystem). `blog-ronacher-
  gaslighting-openness.md` (argues "safety" framing from companies including
  Anthropic can be narrative cover for access restriction; this source
  supplies the specific, narrower, checkable version of Anthropic's actual
  stated position — Claim 5 — that such a critique would need to engage
  with directly).
- **Novel**: The "Pacing the Frontier" letter (Claims 6-7) is entirely new
  to this corpus — no existing source note documents it. The specific
  verbatim text of both the Microsoft-led letter's pro-distillation passage
  (Claim 3) and Anthropic's own quoted response language (Claim 5) are also
  new — prior notes reference the general open-weights/distillation debate
  but this is the first to quote the actual letter and Anthropic-statement
  text directly.

## Guide Impact

- **Ch01 (AI landscape) / Ch08 (policy and organizational context)**: Add
  the three-letter timeline (Claims 1, 4, 6) as a concrete, dated example of
  how fractured industry positioning is on AI openness policy as of August
  2026 — useful for any guide section explaining why practitioners should
  not expect a single "industry consensus" on model access/openness to
  emerge soon, and should track vendor-specific positions rather than
  assuming alignment.
- **Ch07 (dependencies and model sourcing)**: Cite Claim 5's precise
  wording of Anthropic's position (opposed to unrestricted large-scale
  distillation and certain misuse vectors, explicitly *not* opposed to open
  weights generally) as the accurate baseline when the guide characterizes
  Anthropic's stance — avoid the imprecise shorthand "Anthropic is against
  open-weight models."
- **Ch03/05 (AI safety / pacing)**: Add the Pacing the Frontier letter
  (Claims 6-7) as a citable primary source if the guide ever discusses
  industry self-governance proposals around development pace — note that
  its ask is specifically for *international, government-backed* pacing
  tooling, not a unilateral slowdown pledge.

## Extraction Notes

1. **Verbatim text obtained via direct `curl`, not an AI-summarizing fetch
   tool**: an initial WebFetch attempt against the page returned a
   paraphrased, restructured summary with headers and bullet points not
   present in the source, and a second WebFetch attempt (asking explicitly
   for verbatim quotes) still fabricated an incorrect parenthetical
   ("126 chars - exceeds limit") not present anywhere in the source. Per
   MINER.md §2a, all quotes in this note were instead obtained by fetching
   the raw HTML directly with `curl` (browser user-agent) against
   `simonwillison.net` and copying text character-for-character after
   stripping HTML tags with a script, then cross-checked against a second,
   independent link-extraction pass over the same raw HTML for the inline
   hyperlink targets.
2. **Source is short but dense**: the post itself is ~330 words, but every
   sentence carries a specific, checkable claim (a date, a signer count, a
   named individual, or a direct quote), so this note extracts 8 claims
   despite the source's brevity — consistent with MINER.md's "if you only
   found 1-2, you probably didn't read deeply enough" guidance applied to a
   short-but-dense source rather than a long one.
3. **Linked primary documents not independently fetched in full**: this
   note did not separately `curl` and fully re-extract Microsoft's letter
   page, Anthropic's position statement, or the Pacing the Frontier site as
   standalone sources — it treats Willison's direct quotes from each as
   sufficiently verbatim (his post's quoting style, cross-checked against
   his established pattern in other already-mined posts in this corpus,
   e.g. `blog-simonwillison-inkling-open-weights.md`, has consistently
   proven to reproduce source text exactly). If the guide later needs
   *additional* claims from any of the three letters beyond what Willison
   quoted, those would need separate, dedicated source-note extraction
   under new issues, per the same reasoning already applied to companion
   articles in `blog-simonwillison-ptacek-open-weights-pentest.md`
   Extraction Note 4.
4. **No contradiction issue filed**: see Cross-References — Contradicts
   above for the reasoning. The distillation-legitimacy tension in this
   source is the subject of the source itself, not a new corpus-level
   contradiction requiring adjudication.
5. **Overall confidence set to `emerging`**: Claims 1-7 are `settled`
   (verbatim quotes from named, dated, publicly signed letters and
   statements, independently link-checkable). Claim 8 is `emerging`
   (vendor self-reported figures, linked but not independently audited by
   this note or, as far as this source shows, by Willison himself). The
   note-level confidence reflects this mix: strong on the documentary facts
   of who said what and when, weaker on the underlying capability figures
   used to justify the letters' urgency.
