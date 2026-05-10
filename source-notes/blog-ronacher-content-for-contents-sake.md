---
source_url: https://lucumr.pocoo.org/2026/5/4/content-for-contents-sake/
source_type: blog-post
title: "Content for Content's Sake"
author: Armin Ronacher
date_published: 2026-05-04
date_extracted: 2026-05-05
last_checked: 2026-05-05
status: current
confidence_overall: anecdotal
issue: "#537"
---

# Content for Content's Sake

> Armin Ronacher presents linguistic evidence of LLM vocabulary inflation in coding
> sessions, argues that AI-generated content flooding is eroding social trust and
> degrading platform quality, and recommends transparency and friction as the primary
> countermeasures for practitioners and platform builders.

## Source Context

- **Type**: blog-post
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2, Click, and
  other widely-used Python/Rust open-source tools; he is also a founder of Sentry.
  His personal blog (lucumr.pocoo.org) is designated a `trusted-feed` source in this
  repo. This post is opinionated practitioner analysis backed by first-party data from
  his own coding sessions — not a research paper. Claims carry anecdotal-to-emerging
  confidence based on the evidence presented. He discloses AI assistance at the end of
  this post (Pi for visualization, code for Google Trends scraping), practicing the
  transparency he advocates.
- **Scope**: Covers linguistic evidence of LLM vocabulary influence in coding sessions,
  AI-generated content dynamics on social platforms and open-source infrastructure, trust
  erosion from LLM-phrasing detection, and practical recommendations for individuals and
  platform builders. Does NOT cover productivity measurement, code quality metrics, or
  LLM capability benchmarks.

## Extracted Claims

### Claim 1: Analysis of 90 days of coding sessions found medium-frequency words appearing more frequently than wordfreq historical norms predict, and every anomalous word also showed a Google Trends spike

- **Evidence**: Personal methodology — took 90 days of local coding session agent output,
  identified medium-frequency words with high divergence vs. the wordfreq library baseline,
  excluded highest-frequency words ("add", "commit", "patch"), an LLM-generated list of
  engineering-specific terms, common words generally, and internal project code names
  (habitat, absurd, others). All remaining high-divergence words also showed spikes on
  Google Trends US.
- **Confidence**: anecdotal (single practitioner's dataset; author describes it as "not
  entirely scientific"; sample is agent output in coding sessions, not general text;
  Google Trends corroboration is suggestive but confounded)
- **Quote**: "But of the resulting list of words with a high divergence compared to
  wordfreq, they *all* also showed spikes on Google Trends."
- **Our assessment**: Ronacher himself acknowledges "not entirely scientific" and "this
  data set might be a complete fabrication." The Google Trends corroboration is suggestive
  but confounded — LLM-generated text may drive search queries rather than both reflecting
  the same underlying frequency shift. The value here is less the specific numbers and
  more that a trusted practitioner found the signal worth measuring with basic tooling,
  and the convergence across all tested words — not just some — makes selective reporting
  an unlikely explanation.

### Claim 2: Specific words from the author's coding agent output — including "substrate" and "capability" — are inflated vs. historical norms and trending upward on Google Trends

- **Evidence**: Interactive chart on the blog post (JavaScript-rendered) showing word
  frequency over time for flagged agent output words. Author names "substrate" and
  "capability" specifically; notes his coding agent "loves substrate more than it should."
- **Confidence**: anecdotal (visualization not independently reproducible; specific words
  named but underlying data is not downloadable)
- **Quote**: "my coding agent loves substrate more than it should, and that Google Trends
  shows an increase"
- **Our assessment**: "Substrate" and "capability" are widely recognized LLM vocabulary
  markers — practitioners in many communities have noted them independently. Ronacher's
  data provides first-person observational confirmation that these words appear in
  engineering coding agent output at inflated frequencies. The significance for
  AI-native engineering: engineers reviewing AI-generated code, comments, and
  documentation encounter this vocabulary continuously, which creates both the passive
  contamination risk (Claim 3) and a low-cost signal for detecting AI-generated text in
  engineering artifacts.

### Claim 3: Constant exposure to LLM-generated text influences how humans write and speak even without directly using LLMs

- **Evidence**: Personal anecdote — author used the word "substrate" in a talk before
  noticing it was an LLM-favored word. Also observes tweet replies and HN comments from
  contacts he knows are real humans that "read like they are LLM-generated."
- **Confidence**: anecdotal
- **Quote**: "I'm increasingly worried that I'm starting to write like an LLM because I
  just read so much more LLM text."
- **Our assessment**: This is a distinct and underappreciated mechanism from "I used an
  LLM to write this." The concern is passive vocabulary contamination: as engineers spend
  most of their day reading LLM output (code comments, commit messages, PR descriptions,
  documentation, review notes), their own writing may converge toward LLM patterns. The
  Baader–Meinhof effect is a legitimate alternative explanation for individual words, but
  the writing-style convergence is harder to explain away. For AI-native teams where
  agents generate a large fraction of written output, this mechanism may be accelerating:
  the fraction of human-originated text in the team's communication channels is declining
  as AI output scales up.

### Claim 4: Low-effort AI-generated content outperforms quality human content algorithmically, creating an unfair arms race

- **Evidence**: Observation of OSS "remixes" and "reimplementations" appearing within
  hours on GitHub with marketing sites and paid domains; companies (e.g., Polsia) selling
  automated LLM-generated engagement as a service.
- **Confidence**: anecdotal
- **Quote**: "Someone has a formed opinion (hopefully) at lunch, and then has a
  clanker-made post 3 minutes later. It just does not take that much time to build it."
- **Our assessment**: The asymmetry described — 3 minutes to produce vs. 15+ minutes for
  a quality human response — maps to the speed-quality tradeoff that Miller et al.
  document at the code level (`paper-miller-speed-cost-quality.md` Claim 4). Ronacher
  extends the same dynamic to content and communication. The mechanism is real: engagement
  algorithms reward speed and volume, not depth. The conclusion — "these low-effort posts,
  tweets, and Open Source projects should not make it anywhere. But they do!" — is an
  empirical observation. Polsia's commercial viability confirms market demand for
  automated LLM content generation.

### Claim 5: Existing text-based infrastructure systems are failing under AI-generated content flooding

- **Evidence**: Two named examples — (1) EU complaint system "buckling under the pressure
  of AI" (cites Politico article); (2) Pi open-source project routinely receiving
  AI-generated GitHub issues, some filed without the submitting user's knowledge (three
  specific public GitHub issue URLs linked).
- **Confidence**: anecdotal (cites external sources; Pi GitHub examples are the most
  directly verifiable as they are public issues)
- **Quote**: "Take, for instance, the EU complaints system, which is now buckling under
  the pressure of AI."
- **Our assessment**: The Pi GitHub examples are concrete and publicly verifiable: three
  linked issues document AI-generated requests filed against an open-source project,
  some without the submitting user's knowledge. This is qualitatively different from
  intentional spam — it is accidental automation. AI-native engineering teams that build
  or maintain text-intake systems (issue trackers, review queues, feedback forms) are in
  the same category and should treat AI-generated content flooding as a design requirement,
  not an edge case.

### Claim 6: The inability to distinguish human from LLM-generated text erodes trust in people you know, not just strangers

- **Evidence**: Personal accounts — Ronacher reports distrusting communication from
  people he knows when they use LLM phrasing; friend Ben forced someone to call him
  when "he was no longer convinced he was talking to a human"; Ronacher himself had "a
  handful of interactions in which I questioned reality due to the behavior of the person
  on the other side."
- **Confidence**: anecdotal
- **Quote**: "The moment I start distrusting people I otherwise trust, because they have
  started picking up LLM phrasing, it erodes trust all over society."
- **Our assessment**: This is the most significant claim in the post for AI-native
  engineering teams. When a team runs most of its written communication — PR descriptions,
  code review comments, design docs, incident postmortems — through AI assistance,
  colleagues face exactly this problem. Code review, architecture decisions, and incident
  analysis require trusting the judgment and intent of the author. If reviewers cannot
  determine which parts are the author's judgment vs. LLM synthesis, the review process
  degrades. Ronacher does not frame it as an engineering team problem, but the implication
  is direct.

### Claim 7: Some AI-generated content reaches recipients accidentally, without the sender's knowledge or intent

- **Evidence**: Three public GitHub issues on the Pi project where AI-generated requests
  were filed "without the knowledge of the author" (URLs to pi-mono issues #4111, #3862,
  #3783 linked in the post).
- **Confidence**: anecdotal (public examples linked; the "without knowledge" claim is
  Ronacher's characterization of the linked issues, not independently verified mechanism)
- **Quote**: "Pi is routinely getting AI-generated issue requests, sometimes even without
  the knowledge of the author."
- **Our assessment**: This is an important edge case that "intentional vs. unintentional
  AI use" framing misses. Standard transparency recommendations assume the user knows they
  used AI. These examples suggest some automation is happening below the user's awareness
  — possibly AI-assisted browser extensions, form-completion tooling, or agents submitting
  on the user's behalf. For engineering teams: a policy response to AI-generated content
  cannot assume intent; rate limiting, confirmation steps, and friction in text-submission
  flows address accidental generation more reliably than transparency norms alone.

### Claim 8: Declaring AI assistance when there is ambiguity is necessary to preserve social trust in professional interactions

- **Evidence**: Author's argument from the trust-erosion claim (Claim 6) plus his own
  practice (maintains an AI transparency disclaimer page on his blog; explicitly discloses
  AI use at the end of this post — Pi for visualization, code for Google Trends scraping).
- **Confidence**: anecdotal
- **Quote**: "Transparency in either direction, when there is ambiguity, can help great
  lengths."
- **Our assessment**: Ronacher practices what he recommends — the post itself discloses
  specific AI tools used. The recommendation is framed as a social norm ("change has to
  start with awareness"), not a technical enforcement mechanism. For AI-native engineering
  teams: establishing explicit norms for declaring AI assistance in code reviews, design
  documents, incident reports, and external communications is a trust-preservation
  mechanism for team relationships — not a restriction on tool use.

### Claim 9: Engagement metrics are the wrong KPI for healthy long-term platforms in a world of AI-generated content

- **Evidence**: Author's argument from the platform-flooding observations (Claims 4–5)
  applied to GitHub and other developer platforms.
- **Confidence**: anecdotal
- **Quote**: "More engagement is increasingly the wrong thing to look at if you want a
  long term healthy platform."
- **Our assessment**: This is the clearest guide-relevant claim for teams building or
  measuring developer tooling. Teams that measure AI-adoption productivity by PR count,
  commit frequency, or issue-opened volume will see those metrics inflate under AI adoption
  without any improvement in actual outcomes. The Faros productivity-paradox report
  documents this at the organization level (PR volume up, review time up, cycle time flat);
  Ronacher names the underlying mechanism at the platform design level. KPI misalignment
  is a specific, fixable problem — and fixing it requires actively choosing not to
  optimize for engagement.

### Claim 10: Platforms accepting text submissions need friction and "backpressure" mechanisms against AI-generated content flooding

- **Evidence**: Author's argument from the infrastructure-failure evidence (Claim 5) and
  the speed-asymmetry analysis (Claim 4); explicit recommendation for GitHub and
  similar platforms.
- **Confidence**: anecdotal
- **Quote**: "The fact that it was cheap for you to produce does not make it cheap for
  someone else to receive, and we need to find more creative ways to increase the
  backpressure."
- **Our assessment**: The asymmetric-cost argument applies directly to AI-native
  engineering environments: AI-generated PR descriptions, review comments, issues, and
  documentation are cheap to produce but require human judgment to evaluate. A team that
  adopts AI tools without adding friction to text-intake paths will find its reviewers
  and maintainers overwhelmed. The practical response is not to ban AI use but to add
  confirmation steps, rate limits, or review queues — the same mechanisms that Pi
  maintainers and EU complaint systems now need retroactively.

### Claim 11: Using AI agents in communications with others risks becoming an "energy vampire" — draining recipients' attention without proportional human investment

- **Evidence**: Author's synthesis of the vocabulary contamination (Claims 1–3) and
  trust-erosion (Claim 6) dynamics.
- **Confidence**: anecdotal
- **Quote**: "we need to become more aware of how easily we can turn into energy vampires
  when we use agents to back us up in interactions with others"
- **Our assessment**: "Energy vampire" names a dynamic that is otherwise hard to articulate:
  a practitioner who uses AI to generate all their code review comments, PR descriptions,
  and design proposals may inadvertently drain their team's attention budget without
  realizing it — not necessarily because the content is low quality, but because AI-phrased
  content requires extra verification overhead from every recipient. The asymmetry is
  structural: generating costs seconds, evaluating costs minutes. At scale across a team,
  this asymmetry accumulates into the review-time inflation documented by Faros.

## Concrete Artifacts

### Ronacher's vocabulary-inflation detection methodology

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/4/content-for-contents-sake/

Methodology for detecting LLM vocabulary inflation in personal coding sessions:

  Input data:     90 days of local coding session agent output
  Baseline:       wordfreq (github.com/tecnickcom/wordfreq) historical frequency
  Target:         Medium-frequency words with high divergence vs. wordfreq
  Exclusions:
    - Highest-frequency coding words ("add", "commit", "patch", etc.)
    - LLM-generated list of engineering-specific terms (excluded entirely)
    - Most common words generally
    - Internal project code names (habitat, absurd, others)
  Validation:     Google Trends US — every remaining high-divergence word
                  showed a corresponding Google Trends spike
  Output:         Interactive JavaScript chart on the blog post (not static)

Self-described caveat: "not entirely scientific"
                       "this data set might be a complete fabrication"

Named inflated words: "substrate", "capability"
```

### Pi project: AI-generated GitHub issues filed without author knowledge

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/4/content-for-contents-sake/

Three public examples linked in post (pi.dev / badlogic/pi-mono):
  https://github.com/badlogic/pi-mono/issues/4111
  https://github.com/badlogic/pi-mono/issues/3862
  https://github.com/badlogic/pi-mono/issues/3783

Pattern: AI-generated GitHub issues filed against an AI-adjacent open-source project,
         some without the submitting user's knowledge
Implication: AI content automation can operate below the user's explicit awareness
```

### Author's recommendations (verbatim from "Suggestions for Change" section)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/4/content-for-contents-sake/

For individuals:
  "Transparency in either direction, when there is ambiguity, can help great lengths."
  "If we care about them, we should tell them [when they send undeclared slop].
   If we don't care about them, we should not give them visibility and not engage."
  "I would rather have someone ghost me or reject me than send me back some
   AI-generated slop."

For platform/interface builders:
  "we need to throw more wrenches in"
  "The fact that it was cheap for you to produce does not make it cheap for someone
   else to receive, and we need to find more creative ways to increase the backpressure."
  "More engagement is increasingly the wrong thing to look at if you want a long term
   healthy platform."
  "Whatever we can do to rate-limit social interactions is something we should try:
   more in-person meetings, more platforms where trust has to be earned, and maybe more
   acceptance that sometimes the right response is no response at all."

What technology cannot fix:
  "while it can hide some spam and label some generated text, it won't fix us humans.
   What is being damaged here are social interactions across the board"
```

## Cross-References

- **Corroborates**: `paper-miller-speed-cost-quality.md` Claim 4 (AI velocity gains last
  only ~2 months, then disappear as quality debt accumulates). Miller et al. document the
  speed-quality tradeoff at the code-production level — fast AI generation creates
  persistent quality debt that erodes velocity gains. Ronacher documents the structurally
  identical tradeoff at the content/communication layer — fast AI generation floods
  platforms and erodes the social trust that enables collaboration. Both identify the same
  asymmetry: generation speed benefits the producer, quality cost is borne by others.

- **Corroborates**: `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 1 (the
  "arms race" where the party willing to outspend the other in tokens wins). In the
  cybersecurity domain, defenders must outspend attackers in token budget to harden their
  systems. In Ronacher's content domain, generators who automate engagement at scale
  outcompete humans who do not. Both sources identify the same structural problem: AI
  lowers the cost of generation faster than it lowers the cost of evaluation, creating an
  arms race that friction (proof-of-work / rate-limiting) can partially rebalance.

- **Extends**: `survey-pragmaticengineer-ai-tooling-2026.md` Claim 4 (95% of surveyed
  engineers use AI weekly; 56% do ≥70% of engineering work with AI). The Pragmatic
  Engineer survey documents the scale of AI adoption. Ronacher documents the negative
  externalities — trust erosion, vocabulary contamination, content flooding — that emerge
  at this adoption scale. The survey explains why the problem Ronacher describes has become
  acute in 2026: with the majority of senior engineers using AI for the majority of their
  work, the volume of AI-influenced text in engineering communication channels is large
  enough to manifest the effects he observes.

- **Novel**:
  - **Linguistic forensics for personal LLM vocabulary inflation detection**: No other
    corpus source describes a practitioner using word-frequency analysis against a
    historical baseline to detect LLM vocabulary inflation in their own coding session
    output. This is a novel individual-scale observability technique, applicable as a
    low-cost team practice.
  - **Passive vocabulary contamination from LLM exposure without direct LLM use**: The
    mechanism by which reading large volumes of LLM output shifts human writing style —
    without directly using an LLM — is not discussed in any other corpus source. The corpus
    extensively addresses direct AI use; this is the first source to flag the indirect
    influence path.
  - **Trust erosion at the team/interpersonal level from LLM-phrasing detection**: Other
    corpus sources discuss trust in AI *output* (verification, hallucination). This is the
    first corpus source to discuss the inverse: loss of trust in *human* communication
    because it has become indistinguishable from AI output. The "distrusting people I
    otherwise trust" framing is new to the corpus.
  - **Accidental AI content generation without user awareness**: The Pi GitHub examples
    document a failure mode where AI generates content on the user's behalf without
    explicit user action. This is distinct from "intentional but undisclosed AI use" and
    requires different countermeasures (friction, confirmation steps) rather than
    transparency norms alone.
  - **KPI misalignment as the systemic cause of platform degradation**: Ronacher
    explicitly names engagement-metric optimization as the mechanism that rewards LLM slop
    and punishes quality human content. The framing — "our measurement systems incentivize
    the bad behavior" rather than "AI is bad" — is novel in the corpus and directly
    actionable for teams choosing productivity metrics for AI-native workflows.
  - **"Energy vampire" framing for asymmetric attention costs**: No other corpus source
    names the dynamic where AI-assisted practitioners drain others' attention budget
    through high-volume AI-generated communications. The term captures a structural
    asymmetry (seconds to generate, minutes to evaluate) that accumulates into the PR
    review-time inflation documented by Faros.

## Guide Impact

- **Chapter 00 (Principles — Verification Over Generation)**: Extend the verification
  framing to communication, not just code. When AI tools generate a significant fraction
  of a team's written communication (PR descriptions, review comments, design docs),
  recipients bear a verification burden on *human intent*, not just technical correctness.
  Current chapter frames verification as a code-quality concern; Ronacher's observation
  extends it to a trust concern. Consider adding: transparency norms for AI-assisted
  communication are a verification discipline, not a restriction.

- **Chapter 01 (Daily Workflows — Communication norms)**: Add Ronacher's transparency
  recommendation as a team practice: declare AI assistance in professional communications
  when there is ambiguity. Frame as trust-preservation (Claim 8), not surveillance. The
  practical scope: PR descriptions, design documents, incident postmortems, and external
  communications are higher-stakes than commit messages; the norm is most important there.

- **Chapter 02 (Harness Engineering — Measuring AI impact)**: The KPI misalignment claim
  (Claim 9) is a direct warning for any team measuring harness productivity by activity
  metrics. PR count, comment volume, and issue-filed counts will inflate under AI adoption
  without reflecting quality or throughput. Use this alongside the Faros ROI framework to
  argue for signal-quality metrics (defect escape rate, cycle time, review-acceptance
  rate) over engagement counts.

- **Chapter 03 (Safety and Verification — Text intake systems)**: If this chapter
  addresses systems AI-native engineering teams build or maintain, Claim 10 applies
  directly: any text-intake system (issue trackers, review queues, feedback forms) should
  be treated as a potential flooding target. AI-generated content flooding is a design
  requirement, not an edge case, post-2026.

- **Chapter 05 (Team Adoption — Communication and trust norms)**: Claim 6 (trust erosion
  at the interpersonal level) is a team-adoption concern that belongs alongside technical
  adoption recommendations. Teams where most written communication passes through AI
  will encounter colleague-trust erosion without explicit transparency norms. Recommend
  adding to any "team communication standards" section: shared norms for declaring AI
  assistance in code reviews, incident reports, and design proposals — especially where
  author judgment is the primary value delivered.

## Extraction Notes

- Full markdown source fetched directly from
  `https://lucumr.pocoo.org/2026/5/4/content-for-contents-sake.md` (the blog provides
  a markdown export endpoint). All quotes verified character-for-character against the
  markdown source.
- The interactive word-trends visualization is JavaScript-rendered on the blog post; the
  underlying frequency data is not extractable from the HTML source. The specific word
  list (substrate, capability, habitat, absurd, plus unnamed internal code names) is
  described in the text; the chart is referenced but the data is not reproducible here.
- Author discloses at the end of the post: used Pi as an agent for the dynamic
  visualization and wrote code to analyze and scrape Google Trends data. This is
  consistent with his stated recommendation to declare AI use when there is ambiguity.
- The EU complaint system link (Politico article) and the Pi GitHub issue links are
  corroborating external references cited in the post. They were not fetched as part of
  this extraction; the Pi GitHub URLs are publicly verifiable independently.
- Confidence rated anecdotal overall: core claims are first-person observations from a
  single trusted practitioner, backed by self-described non-scientific methodology. The
  observations are internally consistent and plausible, but not peer-reviewed and not
  independently reproducible from this extraction alone.
- The Prospector's triage identifies this as high-novelty with no overlapping existing
  source notes. Cross-reference verification confirmed: no existing corpus note addresses
  passive vocabulary contamination, interpersonal trust erosion from LLM phrasing, or
  accidental AI content automation as distinct claims.
