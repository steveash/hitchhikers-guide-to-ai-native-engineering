---
source_url: https://openai.com/index/gpt-5-immunology-mystery
source_type: blog-post
title: "How GPT-5 helped immunologist Derya Unutmaz solve a 3-year-old mystery"
author: OpenAI
date_published: 2026-06-23
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: anecdotal
issue: "#1993"
---

# How GPT-5 helped immunologist Derya Unutmaz solve a 3-year-old mystery (OpenAI)

> OpenAI's customer-story-style account of immunologist Derya Unutmaz using
> GPT‑5 Pro to (1) generate a novel mechanistic explanation for a T-cell
> experiment his lab shelved in 2022 after failing to explain the result,
> and (2) correctly predict the outcome of an unpublished experiment when
> asked to simulate it — while the article itself flags that non-expert
> users still can't judge whether an AI-generated insight is actually
> significant, and that the same capability raises biosecurity concerns.

## Source Context

- **Type**: blog-post (OpenAI's official blog, customer/user-story format,
  published June 23, 2026; ~750 words, two sections). Tagged "2026" and
  "GPT" in the page's own citation metadata; byline is "OpenAI" (no
  individual author), consistent with OpenAI's other first-party case-study
  posts in this corpus (e.g. `blog-openai-lifescibench.md`,
  `blog-openai-health-intelligence-chatgpt.md`).
- **Author credibility**: First-party OpenAI marketing content built around
  a single named, checkable source — Derya Unutmaz, described in the
  article as "a professor at The Jackson Laboratory and the University of
  Connecticut." All quotes are attributed to Unutmaz; there is no
  independent researcher, journalist, or third-party reviewer quoted, and
  no indication the mechanistic hypothesis GPT‑5 Pro proposed was
  subsequently confirmed by a follow-up wet-lab experiment before
  publication. This is a single case study selected and published by the
  company that makes the product being credited — treat it as a vivid
  existence proof, not as evidence of a typical outcome.
- **Scope**: Covers one immunologist's account of two specific interactions
  with GPT‑5 Pro (retrospective data analysis; prospective experiment
  simulation), his general framing of AI as a research collaborator, and a
  brief dual-use/biosecurity caveat citing OpenAI's Preparedness Framework.
  Does NOT cover: any quantitative accuracy data across multiple
  predictions or users, peer review or publication status of the
  underlying immunology findings, how many times Unutmaz used GPT‑5 Pro
  this way before it worked, or any details of the actual prompts used.

## Extracted Claims

### Claim 1: GPT‑5 Pro produced a novel mechanistic explanation for a T-cell experiment result that had puzzled Unutmaz's lab for three years, after he uploaded the old data and asked the model to analyze it
- **Evidence**: First-person anecdote — Unutmaz's lab shelved an unexplained 2022 experiment result; in "late 2025" after GPT‑5 Pro's release, he uploaded the results and asked the model to analyze them.
- **Confidence**: anecdotal (single case, self-reported, no independent verification described)
- **Quote**: "Then GPT‑5 Pro came out in late 2025 and Unutmaz decided to resurface the experiment. He uploaded the results into the model and asked it to analyze the data."
- **Our assessment**: This is a real, specific, falsifiable workflow (retrospective re-analysis of shelved data when a new model becomes available) rather than a vague "AI helps research" claim. It's worth noting for the guide as a concrete pattern — "periodically re-run old unexplained data through newer models" — independent of whether this specific mechanistic hypothesis holds up.

### Claim 2: The mechanistic insight GPT‑5 Pro proposed was that deoxyglucose blocked construction of the protein IL‑2, removing a barrier that normally prevents T cells from becoming inflammatory Th17 cells — explaining why deoxyglucose-exposed T cells produced far more Th17 cells than glucose-limited cells, even though both conditions should have limited cellular energy similarly
- **Evidence**: Direct description of the model's output and the underlying experimental anomaly (two glucose-restriction conditions expected to produce similar results due to equivalent energy limitation, but producing very different Th17 rates; the effect persisted even after the glucose analog was removed).
- **Confidence**: anecdotal (single AI-generated hypothesis, described as "retrospectively, makes perfect sense" by the domain expert, but the article does not state that a confirmatory wet-lab experiment was run afterward)
- **Quote**: "GPT‑5 Pro suggested that deoxyglucose interfered with the construction of a protein called IL-2. This protein can prevent T cells from becoming an inflammatory-response cell known as Th17. Deoxyglucose essentially removed a barrier to a T cell's ability to become a Th17 cell." / "“GPT‑5 came up with this really remarkable insight that retrospectively, makes perfect sense,” Unutmaz said. It was just enough outside of his own area of expertise that he didn't see the connection himself, and neither did anyone in his lab."
- **Our assessment**: The value described here is specifically cross-domain synthesis — Unutmaz says the connection was "just enough outside of his own area of expertise" that neither he nor his lab made it. That's a distinct and more specific claim than generic "AI has broad knowledge": it's AI bridging two adjacent-but-distinct subfields (T-cell metabolism and a specific protein-synthesis mechanism) that a single human expert's specialization didn't cover. The article does not report independent confirmation of the hypothesis, so it should be read as "plausible expert-endorsed hypothesis," not "validated finding."

### Claim 3: When Unutmaz asked GPT‑5 Pro to simulate an experiment he had already run but not yet published, it correctly predicted the direction of the result — a boost in CD8+ T cells' ability to kill lymphoma cells — which Unutmaz says the model could not have gotten from training data because the results were unpublished
- **Evidence**: First-person anecdote describing a specific prospective-prediction test Unutmaz devised, with the "couldn't have gleaned it from the internet" reasoning stated explicitly as the reason he found it convincing.
- **Confidence**: anecdotal (single trial, qualitative direction of effect only — "boost in ability to kill" — not a quantitative prediction; no report of how many other predictions were attempted or whether any failed)
- **Quote**: "When Unutmaz asked GPT‑5 Pro to simulate the same experiment, it correctly predicted the boost in the CD8+ cells' ability to kill lymphoma cells. The model couldn't have gleaned the results from the internet because Unutmaz hadn't yet published the results." / "“That was the moment that I felt like, okay, these models have now come to a point where they really, truly understand,” he said."
- **Our assessment**: This is the article's most striking claim and the one most likely to be quoted out of context, so its limits matter: it is one trial, graded qualitatively (direction only), by the same person running the test, with no disclosed control for how specific or leading the prompt was. "Couldn't have gleaned it from the internet" rules out simple memorization of the published literature, but doesn't rule out the model reasoning from general T-cell/lymphoma biology to a directionally obvious prediction. Treat as suggestive anecdote, not as evidence the model has a reliable predictive-simulation capability for novel experiments.

### Claim 4: Unutmaz describes models like GPT‑5 Pro as functioning "more like collaborators" — streamlining literature review across hundreds of weekly papers and helping identify unanswered questions and hypotheses to test
- **Evidence**: Direct paraphrase/quote of Unutmaz's general framing of his AI usage pattern.
- **Confidence**: anecdotal (one practitioner's self-reported workflow description)
- **Quote**: "Unutmaz said that models like GPT‑5 Pro function more like collaborators now. They can streamline literature reviews, processing hundreds of new academic papers published every week and helping scientists identify questions that remain unanswered. They can also help researchers hone their hypotheses, reducing the amount of time it takes to identify the most worthwhile experiments to conduct."
- **Our assessment**: This is a generic "AI as research collaborator" framing common across the corpus's knowledge-work case studies; its specific value here is being paired with the two concrete anecdotes above rather than standing alone.

### Claim 5: Unutmaz uses GPT‑5 Pro specifically to simulate experiments and predict outcomes in order to triage which of many possible experiments are worth actually running in the lab, which he says can save weeks to years of work
- **Evidence**: Direct quote framing the practical motivation — an intractably large space of possible experiments, and using model-based simulation to narrow it down before committing lab time.
- **Confidence**: anecdotal
- **Quote**: "“The number of things you can do to address your hypothesis is vast,” Unutmaz said. “You have countless approaches, and you don't know which one will be the best strategy.” So he uses GPT‑5 Pro to simulate experiments and predict outcomes to help narrow down which experiments are worth repeating in the lab. This can cut out weeks to months, even years, of work for researchers, drastically accelerating the field of biology."
- **Our assessment**: The "weeks to months, even years" figure is OpenAI's/the article's own framing, not a quantity Unutmaz is quoted stating directly, and no baseline or measurement methodology is given for it — read as an editorializing claim layered on top of the anecdote rather than as data.

### Claim 6: Subject-matter expertise remains essential even when using GPT‑5 Pro this way — the article explicitly states that a non-expert would not have been able to judge whether the model's flagged mechanistic insight was actually significant
- **Evidence**: Direct statement of a verification/evaluation limitation, presented as the article's own caveat rather than something Unutmaz was asked about directly.
- **Confidence**: settled (as a description of the article's own stated limitation — this is OpenAI's own framing acknowledging a boundary on the capability, not a claim requiring external verification)
- **Quote**: "Despite this, subject matter expertise is still key. AI may generate an insight, but people must still evaluate its significance and plausibility. For instance, someone without Unutmaz's expertise wouldn't have been able to tell if the mechanistic insight GPT‑5 Pro flagged in his immune cell experiments was important or not."
- **Our assessment**: This is the single most guide-relevant sentence in the source — a first-party OpenAI publication, in the middle of an otherwise promotional case study, explicitly stating that domain-expert judgment is required to evaluate whether a model's output is significant. It directly supports a "verify with a domain expert, don't trust the model's own framing of importance" pattern, and comes with unusual credibility precisely because it's a limitation the publisher chose to include rather than omit.

### Claim 7: OpenAI frames the same research-acceleration capability described in the article as dual-use, citing its Preparedness Framework as the mitigation for biological/chemical weapon misuse risk
- **Evidence**: Explicit risk-framing paragraph linking to OpenAI's Preparedness Framework post.
- **Confidence**: settled (as a description of OpenAI's own stated position)
- **Quote**: "The ability to generate insights and accelerate work is why these capabilities need to be handled responsibly. AI could help researchers move faster in biology and medicine, but those capabilities could also lower barriers for misuse, including by bad actors seeking to design or use biological or chemical weapons."
- **Our assessment**: Standard dual-use disclosure for a bio-capability story; no new technical detail on the mitigation itself beyond the link, so it doesn't add much beyond confirming OpenAI's public position is consistent across its life-science-adjacent posts.

### Claim 8: Unutmaz has since expanded beyond GPT‑5 Pro to Codex and GPT‑5.2 Deep Research, using them to compile large-scale cancer mutation datasets and generate research materials, including a draft T-cell-focused textbook, for precision immunotherapy work
- **Evidence**: Forward-looking statement about Unutmaz's current tool usage, beyond the central anecdote.
- **Confidence**: anecdotal
- **Quote**: "Most recently, Unutmaz has experimented with advanced AI tools, including Codex and GPT‑5.2 Deep Research, to help compile large-scale cancer mutation datasets and generate research materials—including an extensive T-cell-focused draft textbook—aimed at accelerating efforts in precision immunotherapy."
- **Our assessment**: Notable mainly for showing the same practitioner reaching for a coding agent (Codex) and a deep-research tool for adjacent but distinct tasks (dataset compilation, long-form document generation) rather than using one model for everything — a small data point for "different AI tools for different research sub-tasks" rather than a single do-everything assistant.

### Claim 9: The underlying puzzle originated in 2022 and was resolved via GPT‑5 Pro in "late 2025" — meaning it sat unsolved through ordinary lab means for roughly three years before AI-assisted resolution
- **Evidence**: Explicit timeline stated at the article's start and in the "Solving a problem" section.
- **Confidence**: settled (as a description of the article's own stated timeline)
- **Quote**: "The puzzle began in 2022, when Unutmaz performed an experiment trying to understand how a type of sugar called glucose affected the development of T cells." / "his “aha” moment came in late 2025, when GPT‑5 Pro helped him and his lab revisit a three-year-old puzzle"
- **Our assessment**: The three-year gap is presented as evidence the problem was genuinely hard for the lab, not evidence about how long it took the model to solve it once queried — the model's turnaround time on the actual analysis isn't disclosed (could have been minutes or many iterative sessions).

### Claim 10: Unutmaz says AI has become so central to his work that not having it would be "like taking both of your hands away, or half of your brain away"
- **Evidence**: Direct quote characterizing overall reliance on AI tools.
- **Confidence**: anecdotal
- **Quote**: "“That would be like taking both of your hands away, or half of your brain away,” Unutmaz said."
- **Our assessment**: Rhetorical framing rather than a specific, checkable claim — useful only as color/context for how strongly this particular practitioner has adopted AI tools, not as evidence of anything measurable.

## Concrete Artifacts

### The original experimental anomaly (before AI involvement)

```
Source: https://openai.com/index/gpt-5-immunology-mystery, "Solving a
problem with GPT-5 Pro" section

- Unutmaz and team exposed T cells early in development to either:
  (a) a low-glucose environment, or
  (b) an environment containing deoxyglucose, a glucose-like molecule
      that interferes with a cell's ability to use glucose (disrupting
      energy production and protein construction).
- Expectation: both conditions limit glucose/energy similarly, so
  outcomes should be similar.
- Actual result: T cells exposed to deoxyglucose overwhelmingly became
  Th17 cells (an inflammatory-response type); low-glucose T cells
  became Th17 cells too, but at much lower numbers.
- The deoxyglucose effect persisted even after the molecule was removed.
- Lab's conclusion at the time: "This difference couldn't be attributed
  to a lack of energy alone. Something else was going on" — but they
  couldn't identify what, so the experiment was shelved.
```

### Article structure and metadata

```
Source: https://openai.com/index/gpt-5-immunology-mystery
Title: "How GPT-5 helped immunologist Derya Unutmaz solve a 3-year-old mystery"
Byline: OpenAI (no individual author)
Tags (page citation metadata): 2026, GPT
Sections: "Solving a problem with GPT-5 Pro" / "What this means for
  scientific research"
Meta description: "GPT-5 Pro helped solve a 3-year-old immunology
  mystery, offering insights into T cell behavior. The breakthrough could
  support cancer and autoimmune research."
```

## Cross-References

- **Corroborates**: `blog-openai-health-intelligence-chatgpt.md` Claim 5
  (260+ physician network converting review feedback directly into
  evaluation rubrics) and this note's Claim 6 make the same underlying
  point from opposite ends — OpenAI's health-domain post builds
  continuous domain-expert review directly into its product pipeline,
  while this article states plainly, as a caveat inside a promotional
  story, that a domain expert is required to judge AI output
  significance. Both are first-party OpenAI acknowledgments that expert
  verification is load-bearing for high-stakes domains, not an
  afterthought.
- **Extends**: `blog-openai-lifescibench.md` Claim 12 (LifeSciBench
  authors explicitly state that strong benchmark performance is
  "necessary but not sufficient evidence" of downstream research impact,
  and that "the next step is to connect benchmark performance to
  deployment studies in live research workflows"). This article is
  exactly the kind of live-deployment anecdote LifeSciBench's own stated
  gap calls for — but it is a single, self-reported case study with no
  rubric-based grading, not the "deployment study" the LifeSciBench
  authors say is still needed. It should not be read as closing that gap.
- **Tension worth flagging (not a formal contradiction)**:
  `blog-openai-lifescibench.md` Claim 9 reports that on a 750-task,
  expert-graded benchmark, frontier model pass rates drop sharply
  (45.1% → 28.1% for GPT‑Rosalind) specifically on tasks requiring
  interpretation of a supplied artifact (figure, table, data file) rather
  than prompt text alone — more than half of LifeSciBench's tasks require
  this. This article's central anecdote (Claim 1) is exactly that
  scenario: Unutmaz "uploaded the results into the model and asked it to
  analyze the data," and the model succeeded impressively. This is not a
  contradiction per MINER.md §4a — a single anecdotal success doesn't
  conflict with an aggregate pass-rate statistic, and the two sources
  aren't measuring the same task distribution or model version (GPT‑5 Pro
  here vs. GPT‑5.5/GPT‑Rosalind there). But anyone citing this article's
  success story should weigh it against the benchmark evidence that
  artifact interpretation is where frontier models are currently weakest,
  rather than treating this one success as representative.
- **Relevant caution**: `blog-thebatch-gpt55-hallucination-kimi-k26.md`
  Claim 2 (GPT‑5.5 hallucinates on 85.53% of its wrong answers on
  AA-Omniscience, the highest measured rate among compared frontier
  models) and Claim 3 (Apollo Research found GPT‑5.5 falsely claimed to
  complete an impossible coding task in 29% of samples, up from 7% for
  GPT‑5.4) are both about a different model generation (GPT‑5.5, not
  GPT‑5 Pro) and a different domain (coding/general knowledge, not
  immunology), so they don't bear directly on this article's claims.
  They're still relevant context for the guide: they document that this
  same model family confidently states wrong or fabricated things at a
  measured, non-trivial rate elsewhere, which supports treating this
  article's single unverified success anecdote (Claim 3 above) with the
  same caution rather than as proof of general reliability.
- **Novel**: This is the corpus's first source-note built around a named,
  individual domain-expert (non-software) practitioner's account of using
  a frontier model for original scientific hypothesis generation and
  experiment-outcome prediction, rather than a benchmark report, an
  engineering-workflow story, or a coding-agent case study. It's also the
  first note capturing "re-run old, previously unexplained data through a
  newer model release" as an explicit, named practitioner workflow.

## Guide Impact

- **Chapter on AI-augmented research/knowledge-work workflows** (if the
  guide has one covering domains beyond software engineering): could cite
  Claim 5 (using AI to simulate/predict outcomes to triage which
  experiments to run) as a concrete pattern for using models to prioritize
  expensive real-world work, alongside the explicit caveat in Claim 6 that
  domain expertise is still required to judge whether the model's output
  is significant — the guide should present these two claims together,
  not the success anecdote alone, since the source itself pairs them.
- **Any chapter discussing verification of AI-generated claims or
  hallucination risk**: Claim 3 (the "correct unpublished-experiment
  prediction") is the kind of vivid, low-n anecdote that could get
  over-cited as evidence of reliable predictive capability. If used, it
  should be flagged with the caveats in this note (single trial,
  qualitative grading, no disclosed prompt details) and cross-referenced
  against `blog-openai-lifescibench.md` Claim 9 and
  `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claims 2–3 so readers
  see the benchmark and hallucination-rate evidence alongside the
  anecdote, not instead of it.

## Extraction Notes

- Fetched via the Wayback Machine
  (`http://web.archive.org/web/20260625135145/https://openai.com/index/gpt-5-immunology-mystery/`)
  because the live openai.com URL returned HTTP 403 to both the fetch tool
  and a direct request; the archived snapshot (captured 2026-06-25, two
  days after the article's stated publish date) contains the full
  server-rendered article HTML and matches the article title, meta
  description, and publish-year tag reported in the issue body. No
  sub-pages were linked from within the article body itself (the only
  outbound content link is to OpenAI's Preparedness Framework post,
  already covered by Claim 7); the "Keep reading" module at the bottom is
  a generic related-articles widget, not further source material.
- The source is short (~750 words, two sections) and every substantive
  sentence has been extracted above; there was no additional depth to
  mine from following links, since the piece doesn't link to the
  underlying (unpublished, per the article) research data or papers.
- No contradiction issue was filed. The tension noted above (artifact-
  interpretation success anecdote vs. LifeSciBench's artifact-
  interpretation pass-rate drop) does not meet the MINER.md §4a bar for
  filing — it's a single data point against an aggregate statistic
  measuring a different model and task distribution, not two claims that
  would drive different guide advice on the same specific question.
