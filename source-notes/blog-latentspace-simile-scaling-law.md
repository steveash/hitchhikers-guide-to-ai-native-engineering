---
source_url: https://www.latent.space/p/simile
source_type: blog-post
title: "Simulation: the new Scaling Law — Joon Sung Park, Simile AI"
author: Latent Space (hosts Swyx and Vibhu Sapra, interviewing Joon Sung Park, co-founder/CEO of Simile AI)
date_published: 2026-08-21
date_extracted: 2026-09-08
last_checked: 2026-09-08
status: current
confidence_overall: emerging
issue: "#3307"
---

# Simulation: the new Scaling Law — Joon Sung Park, Simile AI

> Latent Space podcast interview with Joon Sung Park (author of the 2023
> "Smallville" Generative Agents paper, now co-founder/CEO of Simile AI) on
> building "digital twins" — behavioral foundation models of human
> populations validated at 85% accuracy against 1,000 real people — and the
> thesis that human-behavior simulation, not just LLM capability, is
> becoming a distinct, deliberately-trained-for scaling target.

## Source Context

- **Type**: blog-post (podcast interview transcript, Latent Space, published
  2026-08-21; sourced from the Latent Space trusted RSS feed). The page
  includes an editorial introduction written by the hosts, an episode
  outline/timestamp list, and a full transcript with speaker labels
  (Swyx, Vibhu, Joon).
- **Author credibility**: Joon Sung Park is the lead author of "Generative
  Agents: Interactive Simulacra of Human Behavior" (the "Smallville" paper,
  2023 — per the transcript, ~7,200 Google Scholar citations at time of
  recording), a PhD from Stanford under/alongside Percy Liang (who coined
  the term "foundation model") and Michael Bernstein (an author of ImageNet).
  Park is now CEO of Simile AI, which the article's introduction describes
  as having closed a "$2B Series B" backed by GreenOaks and Index Ventures,
  with Fei-Fei Li and Andrej Karpathy as named backers. This is a first-party
  founder interview: Park has direct authority over what Simile's
  methodology is, but the commercial framing (accuracy numbers, client
  names, market-size claims) is self-reported and not independently audited
  by Latent Space or this Miner. The hosts (Swyx, Vibhu) push back at
  several points (on cost, on the "billion personas" combinatorial
  alternative, on TAM), which is a mild counterweight to pure promotional
  framing but does not constitute independent verification.
- **Scope**: Covers Simile's origin story (from Generative Agents to
  digital twins), its three-bucket data-collection methodology, a validated
  85%-accuracy digital-twin study, a follow-up RCT post-training study,
  population- vs. individual-level model architecture, early scaling-law
  evidence, current commercial use cases and economics, and long-term
  ambitions (8-billion-person societal simulation, climate change, UBI).
  Does NOT cover: Simile's model architecture or training infrastructure in
  technical detail, independent replication of the 85% figure, per-client
  case-study specifics beyond names mentioned in passing (CVS, Wealthfront,
  Gallup, Deloitte), or any peer review of the cited papers ("Generative
  Agent Simulations of 1000 People" and the unnamed RCT post-training
  follow-up) beyond what Park describes verbally.

## Extracted Claims

### Claim 1: Simile AI raised a "$2B Series B" and reports running "tens of millions of simulations" for Fortune 100 clients (e.g., CVS) with "85–99% accuracy vs human focus groups"

- **Evidence**: Stated in the article's editorial introduction (written by
  the Latent Space hosts, not spoken by Park in the transcript), as framing
  context for the interview.
- **Confidence**: anecdotal (funding and headline accuracy figures are
  asserted by the publication's own framing, not sourced to a press release
  or filing in the article text; the "99%" end of the range is not
  explained or substantiated anywhere else in the transcript — only the 85%
  figure is methodologically backed, via Claim 2 below)
- **Quote**: "it has recently come back with a vengeance with SimGym in
  April and now Simile AI's $2B Series B, backed by GreenOaks and Index
  Ventures with prominent backers like Fei-Fei Li and Andrej Karpathy,
  running tens of millions of simulations for Fortune 100 clients like CVS
  and 85–99% accuracy vs human focus groups."
- **Our assessment**: Treat the "99%" figure with caution — it appears only
  in this framing paragraph and is never referenced, derived, or explained
  in the interview itself, unlike the 85% figure (Claim 2), which has a
  full methodology behind it. This is a case where the guide should cite
  85% (the substantiated number) and not repeat "85–99%" as if both ends of
  the range were equally supported.

### Claim 2: Simile validated "digital twins" of 1,000 real people that replicated the same individuals' own behaviors and attitudes 85% as accurately as the individuals replicated their own prior responses

- **Evidence**: Described methodology: 1,000 people representatively
  sampled from the US were brought to a "virtual lab," gave ~2 hours of
  interview and behavioral data (interview script sourced from the American
  Voices Project), were sent away for ~2 weeks, and then had their digital
  twins predict how they themselves would answer a battery of behavioral
  economics games, a Big Five personality test, the General Social Survey,
  and PNAS-published randomized controlled trials — compared against the
  real participants' own answers when they returned.
- **Confidence**: emerging (a described, specific, falsifiable study design
  — self-reported by the company that ran it, published as "Generative
  Agent Simulations of 1000 People," but not independently replicated in
  this source)
- **Quote**: "And we would have their digital twins predict how the source
  individuals would have acted in these studies and surveys. And this is
  where we could replicate people's behaviors and attitudes 85 percent as
  accurately as people would replicate their own."
- **Our assessment**: The self-consistency framing here matters: the 85%
  figure is not "twin accuracy vs. ground truth" in the abstract — it is
  twin accuracy relative to the individual's own test-retest reliability
  after a two-week gap, which is a more rigorous (and more defensible)
  baseline than comparing against a single ground-truth answer, since human
  responses to surveys and behavioral games are not perfectly stable over
  two weeks either. This is the single most load-bearing claim in the
  source and the number the guide should cite if any is cited.

### Claim 3: On the same benchmark, frontier LLMs (not specifically trained for behavior prediction) scored far below Simile's digital twins — as low as 20–30% on niche populations and 50–60% on general population

- **Evidence**: Direct comparison stated by Park immediately after
  describing the 85% figure, contrasting Simile's models against unnamed
  "frontier models" (context makes clear this includes models like
  ChatGPT/Claude, referenced earlier in the same answer).
- **Confidence**: emerging (a specific, quantified comparative figure,
  self-reported by the vendor whose competing product benefits from the
  comparison, with no baseline model or evaluation methodology named)
- **Quote**: "This is also where we see quite a bit of discrepancy in the
  performance in human behavior prediction between the frontier models,
  Simile's model, and the models being created in this space, where in some
  cases, the model performance of frontier models go all the way down to
  20, 30 percent, especially if you go into that more niche population on
  topics that our customers would care about. On more gen pop, it might be
  around 50 to 60 percent."
- **Our assessment**: This is a self-serving comparison (Simile grading its
  own product against unnamed competitors on an unnamed test), so treat the
  specific numbers as directional rather than a verified benchmark result.
  The underlying mechanism claim (Claim 4) is more defensible than the raw
  percentages.

### Claim 4: Frontier models are trained to be "super rational, objective machines" (optimized on data from professional programmers/scientists), which is the wrong optimization target for modeling how ordinary humans actually behave — Simile instead deliberately trains models to reproduce human biases and mistakes

- **Evidence**: Park's stated mechanism for why frontier models underperform
  at behavior prediction (Claim 3): their training data and objective
  (reasoning correctness, via vendors like Mercor and Scale) rewards
  rationality, not realistic human irrationality.
- **Confidence**: anecdotal (a mechanistic explanation offered by the
  company's founder, plausible and internally consistent with Claims 2–3,
  but not independently tested against an ablation or control)
- **Quote**: "So what these models are really good at today is they're
  trying to become the super rational, objective machines, right? So you go
  get their data from places like Mercor, Scale. You talk to professional
  programmers, scientists to create model that's amazing at reasoning.
  That's what they do. Simile doesn't care about any of this. The models
  that we're talking about here, what we're trying to create are models
  that are as dumb as I am, right? So if I make some mistakes, the model
  has to make the same mistake."
- **Our assessment**: This is the clearest one-line statement of Simile's
  core differentiation thesis: optimizing for correctness and optimizing
  for realism are different, sometimes opposing, training objectives. It's
  a useful counterpoint anywhere the guide discusses "smarter/more capable
  model is always better" — for behavior-simulation use cases specifically,
  a model that is *less* rational may be more accurate.

### Claim 5: Simile's data collection is organized into three buckets — rich qualitative interview data ("tell me the story of your life"), observational/transactional behavioral data, and causal-mechanism data from randomized controlled trials

- **Evidence**: Park's direct description of Simile's data taxonomy, in
  response to a question about what a "behavior foundation model" actually
  requires beyond prompting.
- **Confidence**: emerging (a specific, structured methodology description
  from the company's own founder; internally consistent with the rest of
  the interview)
- **Quote**: "We think about data in three buckets. So one bucket is
  interview data. It's quite interesting. Rich qualitative data is
  interesting. It's not behavioral, but we would literally ask people,
  'Hey, tell me the story of your life.'"
- **Quote (causal bucket)**: "there is the last category of data, that I
  personally think is perhaps the most important, which is the data that
  describes the causal mechanism, the whys of people... really, where you
  get to see the most behavioral aspect of this is in randomized controlled
  trials, like RCTs."
- **Our assessment**: The explicit ranking — causal/RCT data as "perhaps the
  most important" — is notable because it's the hardest and most expensive
  bucket to collect (each RCT is a real controlled experiment run once).
  This maps directly onto Claim 6 (the RCT post-training paper) as the
  practical payoff of prioritizing this bucket.

### Claim 6: Simulation is valuable not because it predicts a fixed future outcome, but because it can reveal a step-by-step, sometimes counterintuitive *path* to a stated goal — a framing Park explicitly connects to Asimov's Foundation and "psychohistory"

- **Evidence**: Park's answer to why simulation differs from prediction,
  using an extended Foundation-series analogy (exiling the scientists who
  foresaw galactic collapse to Terminus as the "obviously wrong but actually
  correct" first move) and a hypothetical EV-marketing example.
- **Confidence**: anecdotal (a conceptual/philosophical framing argument
  illustrated by a fictional example and one hypothetical business example,
  not a measured result)
- **Quote**: "So really what simulation allows you to do in its highest form
  is you give it not a problem or question, like what would people answer
  to the survey? That's not what we do. What we tell it is, 'Here is a goal
  that we have. In the context of foundation, we want to keep the unrest to
  a 1,000 years. What is the path that we need to take now to get to that
  particular future?' And that's what simulation allows you to do."
- **Our assessment**: This reframes what a "simulation" product is actually
  for: not "what will happen" (a prediction problem) but "what should we do
  to reach an outcome" (a planning/search problem over simulated futures).
  This distinction is the conceptual core of the source and is what
  differentiates it from pure survey/forecasting tools — but it is also the
  most purely rhetorical claim in the piece, resting on a science-fiction
  analogy rather than a demonstrated case study.

### Claim 7: A follow-up study post-trained a model on tens of thousands of real, pre-registered randomized controlled trials sourced from the Open Science Framework platform, and reported this produced "significant improvement in model's capability to predict human behaviors"

- **Evidence**: Park's description of a second paper (unnamed in the
  transcript), which used OSF's pre-registered-study data (chosen because
  pre-registration reduces publication/survivorship bias relative to
  post-hoc-published findings) to post-train a model — described as a
  research/open-science exercise, not a commercially deployed model.
- **Confidence**: emerging (a described, specific data source and training
  approach with a stated directional result; no quantitative before/after
  accuracy figure is given for this specific study, unlike Claim 2)
- **Quote**: "this particular data set, helped us make a point that by
  collecting a lot of these randomized controlled trials, that are really
  well-designed, we can make significant improvement in model's capability
  to predict human behaviors. So that's what this paper was about."
- **Our assessment**: This is evidence for a specific, actionable technique
  — post-training on real RCT data, not just prompting — as the mechanism
  by which "social physics" (Claim 4/5's causal-mechanism data) actually
  gets baked into a model. Notably, this model is explicitly *not* what
  Simile sells commercially ("this particular model is not... something
  that we're serving commercially because this was a part of the open
  science"), so its result is a research proof-of-concept, not a
  production benchmark.

### Claim 8: Simile trains two architecturally distinct model types for every study — a "population-level model" and an "individual-level model" — both taking a population/individual description plus a stimulus as input

- **Evidence**: Direct answer to whether behavior modeling happens
  per-individual or per-population; Park states both are trained and used,
  with individual-level modeling described as the harder task.
- **Confidence**: emerging (architecture description from the founder;
  internally consistent, no further technical detail given)
- **Quote**: "We always train 2, distinct model. One is what we call the
  population-level model. The other is what we call the individual-level
  model. And both take very similar input, which is the description of a
  subpopulation or individual and a stimuli."
- **Our assessment**: This is a concrete architectural detail (two model
  types, not one) that would be useful for anyone trying to understand or
  replicate the approach, though no detail is given on how the two model
  types differ in training beyond the granularity of their target.

### Claim 9: Simile reports "early glimpses" of a scaling law specific to human-behavior simulation — more human data and more compute produce predictable gains in simulation accuracy

- **Evidence**: Park's direct answer to a question about whether scaling
  (larger models, more parameters/compute) produces emergent gains in
  simulation quality.
- **Confidence**: anecdotal (a qualitative, self-reported observation —
  "early glimpse" — with no chart, curve, or quantitative data given in the
  transcript)
- **Quote**: "The thing that we're seeing is the early glimpse of scaling
  law in simulations. The more data about humans and more compute you
  ingest, you start to get predictive and predictable gains of the model
  performance in simulating it, simulating people."
- **Our assessment**: This is the claim referenced in the episode's title
  ("Simulation: the new Scaling Law") and the Prospector's framing for this
  issue, but it is the thinnest claim in the interview — an assertion of
  "early glimpse," not a published curve or figure. The guide should not
  cite this as a demonstrated scaling law; it should be cited, if at all,
  as a company's stated internal observation.

### Claim 10: Simile operates today at a scale of tens of thousands of newly collected respondents per week, with panel partnerships reaching "tens of millions of people globally," and anticipates that societal-scale simulation will eventually require compute "as much as training a foundation model" or "an entire data center worth of simulations"

- **Evidence**: Park's answer to a cost/scale question, contrasting current
  operating scale (hundreds of thousands of modeled people per study is
  "more than enough" for most use cases) against a stated long-term
  ambition.
- **Confidence**: anecdotal (self-reported operating figures and a
  forward-looking cost projection with no supporting calculation shown)
- **Quote**: "today what we do is every week we are collecting data on the
  scale of tens of thousands people's data, and we have panel partnerships
  that gets us to tens of millions of people globally."
- **Quote (future cost)**: "my hunch here is I do think in the next some
  number of years, we will start creating simulations that will cost as
  much as training a foundation model. But perhaps it's going to be so
  valuable to the society that it would be a no-brainer."
- **Our assessment**: The reuse economics point buried in this same answer
  is more concrete and verifiable in principle than the cost projection:
  once a digital twin exists, Park says it is reused across unrelated
  studies because it's "domain-agnostic" (see Claim 13) — meaning the
  marginal cost of an additional study on an already-modeled population is
  much lower than the cost of the first study.

### Claim 11: Park's stated long-term ambition is a simulation of all 8 billion people on Earth, aimed at "wicked problems" like climate change, detecting collapsing democracy, and the origin of the monetary system — explicitly framed as inheriting from Thomas Schelling's Nobel-winning 1970s agent-based segregation model

- **Evidence**: Park's answer describing the field's long-term vision, using
  Schelling's "red dots and blue dots" segregation model (which found that
  even a very small individual preference for same-color neighbors produces
  complete societal segregation over time, and influenced US mixed-income
  housing policy) as the historical precedent for high-fidelity,
  generative-AI-powered agent-based models.
- **Confidence**: anecdotal (an aspirational, forward-looking claim; the
  Schelling precedent is real and independently well-documented history,
  but its application to "8 billion people" via generative-agent models is
  Park's own extrapolation, not a demonstrated result)
- **Quote**: "can we create a simulation of 8 billion people living on
  Earth? I think that's quite interesting... it's questions like, can we
  help solve climate change?... this is what we, like social scientists
  would often call it the wicked problems."
- **Quote (Schelling)**: "One of the striking finding of this paper or this
  agent-based model was for the longest time, people thought the
  segregation within society was caused by explicit and overt racism. But
  if you look at this model, people's preference towards living with people
  of the same color, that preference can be very minute. But the very small
  difference causes the society to segregate completely over time."
- **Our assessment**: The Schelling reference is the strongest piece of
  intellectual grounding in the source — it's a real, independently
  verifiable historical precedent (agent-based modeling won a Nobel Prize in
  Economics) for the general claim that simple agent rules can produce
  emergent, non-obvious societal outcomes. It supports the *plausibility*
  of agent-based societal simulation as a field, but does not by itself
  support Simile's specific claim that LLM-based digital twins at 8-billion
  scale would work the same way — that remains aspirational.

### Claim 12: Simile's current commercial use cases center on concept testing, focus-group replacement, A/B-style product testing, and modeling investor-facing events like public-company earnings calls, for named clients including CVS, Wealthfront, Gallup, and Deloitte

- **Evidence**: Park's direct description of what customers use Simile for
  today, plus a specific Wealthfront example (multimodal product testing —
  agents reasoning over images and traversing Figma mockups/websites).
- **Confidence**: emerging (specific, named client use cases from the
  founder; no independent client confirmation or outcome metric beyond
  Wealthfront being described as an early enthusiastic adopter)
- **Quote**: "Oftentimes, the core use cases are things like concept
  testing, to start with. But also, people sometimes want to do focus
  groups or one of the fun use cases that we also serve is even modeling
  things like earnings calls for public companies."
- **Quote (Wealthfront)**: "some of the things that our agents can also do
  is it can be given a domain, like, or, like, a website URL and go use it
  for a while. It's these things. And Wealthfront was one of the first,
  customers, that was very excited about this possibility."
- **Our assessment**: The earnings-call and Figma/website-traversal use
  cases are the most concrete, differentiated product surface described in
  the interview — they go beyond survey-replication into agents that
  interact with an artifact (a mockup, a live site) the way a real user or
  analyst would, which is a meaningfully different technical claim than
  the twin-accuracy validation study.

### Claim 13: A single digital twin is reused across many unrelated commercial studies because human-behavior models are "domain-agnostic" — some traits (e.g., risk tolerance) are stable over time while others (e.g., store-visit frequency) change and must be refreshed

- **Evidence**: Park's direct answer to whether a modeled person can be
  reused for subsequent, unrelated studies.
- **Confidence**: anecdotal (an assertion about which human traits are
  stable, offered without citation to specific psychological/behavioral
  literature, though the general claim — some traits are more temporally
  stable than others — is broadly consistent with established personality
  psychology)
- **Quote**: "The beauty of this model and these agents is the fact that
  they are domain-agnostic... there's so many traits about people that are
  also known to never change. Like, your risk tolerance doesn't really
  change over time. It's very consistent."
- **Our assessment**: This is the economic core of Simile's business model:
  amortizing the expensive, bespoke per-person data-collection cost (Claims
  2, 5) across many unrelated commercial studies. It also implicitly
  concedes that some fraction of any twin's outputs will go stale and
  require refresh (e.g., recent purchase history), which is a maintenance
  cost the interview does not quantify.

### Claim 14: Park explicitly rejects pure combinatorial/statistical persona generation (contrasted against a described "Billion Personas" paper that cross-multiplies demographic attributes) as insufficient — arguing that if that approach alone worked, "we have solved simulation," which has not happened, because detailed/niche knowledge about people is not already embedded in frontier model parameters and requires bespoke data collection

- **Evidence**: Park's direct response to a host question comparing Simile's
  approach to a described paper that generates a billion personas via a
  "cross matrix" / "dot product" of professions and demographic backgrounds
  without Simile's underlying data-collection groundwork.
- **Confidence**: anecdotal (a critique of a named alternative approach,
  offered by a commercial competitor in the space; plausible reasoning but
  not independently tested against the "Billion Personas" approach in a
  head-to-head comparison)
- **Quote**: "it is relying heavily on the known statistics that went into
  training the model. So to the extent that you believe that statistics is
  correct, this is not a bad way to go about this. But the thesis here...
  if this works, then we have solved simulation."
- **Quote (bespoke data)**: "That's not, unfortunately, what we see, where
  there is such detailed and also niche knowledge about people that if you
  just take one example, it might feel very mundane, but it's quite rich
  when you put together, that you do need to do a lot of bespoke data
  collection to better understand people."
- **Our assessment**: This is a useful methodological dividing line for the
  broader "synthetic persona" space: pure statistical/combinatorial
  persona generation (sampling from known demographic distributions
  already latent in a model's training data) versus Simile's
  bespoke-data-collection approach (interviews, RCTs, observational data
  from real consenting participants). Park's argument is essentially that
  the former only retrieves what a model's pretraining already encodes,
  while the latter adds genuinely new information the model didn't have.

### Claim 15: Simile's origin traces to a "time machine game" thought experiment during the Generative Agents/Smallville research period, where the team bet that accurate personal AI assistants require a deep model of the user *before* they can be built reliably

- **Evidence**: Park's origin story: playing a "time machine game"
  (imagining looking back from 10 years in the future at the most important
  application) with co-founders Michael Bernstein and Percy Liang, choosing
  "recreate the world" (simulation) over "automation tools" (personal
  agents) as the more ambitious bet — but explicitly reasoning that
  personal-agent quality is bottlenecked on user modeling.
- **Confidence**: anecdotal (a personal origin narrative with one
  illustrative hypothetical example, not a measured claim)
- **Quote**: "my bet was if you were to create a really amazing personal
  assistant out of this technology, what you need first is an amazing
  model of your users. So I told a model, 'Hey, can you go buy late dinner
  for me?' And it orders Hawaiian pizza, and I do not like pineapples on my
  pizza. Then it totally failed. The way for it to not make that mistake is
  only by having a deep understanding of who I am."
- **Our assessment**: This origin story is the connective tissue between
  Simile's simulation product and the corpus's existing personal-agent /
  context-engineering material: Park's claim is that personalization
  quality for any agent (not just simulation products) is bottlenecked on
  how deeply the system models the specific user, and that this is
  presently unsolved — a claim he repeats later in the interview ("I don't
  think we've seen a true personal assistant that's useful, in ways that
  meet the ambition of that particular line of work").

### Claim 16: Simile's 2023 Generative Agents work concluded that storing agent memory as a plain Markdown/text file (rather than a knowledge graph or bespoke trained model) works well because LLMs are already good at reasoning over text — but Park argues some behaviors require touching model *weights* (post-training), not just prompting

- **Evidence**: Park's direct comparison between the memory architecture
  decision made for the 2022–23 Generative Agents paper and the same
  design choice he observes in current products (referred to in the
  transcript as "OpenClaw"); followed by his stated criterion for when
  prompting is insufficient and post-training is required.
- **Confidence**: emerging (a specific architectural claim about why
  prompting has limits, tied to a concrete example — the choice of
  Markdown-file memory — and to Simile's own post-training practice
  described elsewhere in the interview, e.g. Claim 7)
- **Quote**: "these language models are quite good at modeling text and
  understanding and reasoning about text. So just put everything in a
  Markdown file or a text file. You're done... there are certain things you
  just cannot shape just by prompting the model. So to some degree, you do
  need to touch the parameters of the model itself."
- **Quote (social physics criterion)**: "My intuition behind the actual
  when do you train or even post-train a model versus just prompt a model
  is if the model has to learn the underlying physics of the world that
  it's operating in. So it has to learn new social physics."
- **Our assessment**: This gives a concrete, general-purpose heuristic for
  when prompt/context engineering is sufficient versus when post-training
  is required: if the model already "trusts" the physics of the
  environment (i.e. has the base statistics from pretraining), prompting
  suffices; if the model needs to learn genuinely new physics (Simile's
  claim about human behavioral "social physics" specifically), prompting
  alone will not get there. This is a reusable framing for the guide's
  context-engineering material, independent of whether one buys Simile's
  specific human-simulation thesis.

## Concrete Artifacts

### Three-bucket data taxonomy (Simile AI, per Park)

```
Source: Latent Space interview, "Simulation: the new Scaling Law" (2026-08-21)

1. Interview data
   - Rich qualitative data: "tell me the story of your life"
   - Not behavioral, but provides texture / long-tail information
     (childhood memory, trauma, first love, etc.)

2. Behavioral data (observational)
   - Transaction data, web-scraped data
   - Gives "base statistics of people's behavior"

3. Behavioral data (causal mechanism)
   - Randomized controlled trials (RCTs)
   - Described as "perhaps the most important" bucket
   - Explains the "whys" of decisions, not just the "whats"
   - Hardest to collect: "the world is our ground truth, but it happens once"
```

### Validation study design ("Generative Agent Simulations of 1000 People")

```
Source: Latent Space interview (Park describing the paper), 2026-08-21

- 1,000 people, representatively sampled from the US
- ~2 hours of interview data collected (script from American Voices
  Project) + behavior data, in a "virtual lab"
- Digital twins built from this data
- Participants brought back after ~2 weeks
- Participants completed: behavioral economics games, Big Five
  personality test, General Social Survey, PNAS-published RCTs
- Digital twins predicted how the same individuals would answer
- Result: twins replicated the individuals' own behaviors/attitudes
  85% as accurately as the individuals replicated their own
  (test-retest) responses
- Paper published end of 2024
```

### Frontier-model vs. Simile-model accuracy on behavior prediction (self-reported, no baseline named)

```
Source: Latent Space interview (Park), 2026-08-21

Frontier models, niche/customer-relevant populations:  ~20-30% accuracy
Frontier models, general population:                    ~50-60% accuracy
Simile digital twins (1000-person validation study):    ~85% accuracy
```

### Company structure (Simile AI, per Park)

```
Source: Latent Space interview (Park), 2026-08-21

Founders (4): Joon Sung Park (CEO), Michael Bernstein, Percy Liang,
              Lainie Yallen (business co-founder)
Headcount: ~60 people
Offices: HQ in Mission Rock, SF; smaller office in New York
Composition: ~15-20% of employees are Park's former Microsoft Research
             lab-mates (many previously went to OpenAI, Google Gemini,
             and have since joined Simile)
```

## Cross-References

- **Contradicts**: See filed contradiction issue
  [#3310](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3310)
  — `blog-cursor-real-time-rl.md` Claim 1 states, as a core architectural
  principle, that "real users cannot be faithfully simulated" (the reason
  Cursor built a real-time RL pipeline on actual production user
  interactions instead of a simulated-user training environment for its
  Composer coding agent). This source's Claim 2 (85%-accuracy digital-twin
  validation study) and Claim 4 (deliberately modeling human irrationality)
  directly bear on the same underlying question — whether human/user
  behavior can be simulated with enough fidelity to substitute for real
  signal — and reach the opposite practical conclusion for a different
  (but overlapping) use case. Per MINER.md §4a, no verdict is picked here;
  see the filed issue for Side A/Side B framing and a possible
  reconciliation via a granularity/stakes conditioning variable (live
  interactive per-session agent behavior vs. bounded-stimulus
  survey/RCT-style population response prediction).
- **Extends**: `blog-openai-deployment-simulation.md` — that note documents
  OpenAI's "Deployment Simulation," which replays real (not synthetic)
  production conversations to forecast a candidate model's undesired
  behavior rates before release; its Claim 1 and Claim 10 both rest on the
  principle that realistic context (sourced from real users) beats
  synthetic construction for eliciting representative behavior. This
  source's Claim 2 is a parallel, independently-arrived-at data point for
  the opposite direction of the same underlying question: instead of
  replaying *real* conversations to avoid needing to simulate a user
  (OpenAI's approach), Simile is trying to build models that stand in
  *for* real users directly, and claims 85% fidelity against real
  test-retest responses on structured instruments. The two sources
  represent different bets on the same core tension — realistic-context
  sourcing vs. synthetic user modeling — without directly contradicting
  each other, since OpenAI's use case (safety forecasting for a chat
  assistant) and Simile's (market research / decision simulation) are
  different domains; the closer, more direct tension is with
  `blog-cursor-real-time-rl.md` (see Contradicts above).
- **Extends**: `blog-anthropic-coderabbit-agent-orchestration.md` — that
  note documents a production multi-model orchestration pipeline (Opus/
  Sonnet/Haiku) with an eval-harness-driven, "we don't guess" philosophy
  for model routing (Claim 8). This source's Claim 8 (Simile's population-
  level vs. individual-level model split) and Claim 16 (a stated criterion
  for when post-training is required vs. when prompting suffices — "if the
  model has to learn the underlying physics of the world it's operating
  in") both describe architectural decisions in a similarly disciplined,
  criterion-driven way, though for a different kind of system (behavior
  simulation vs. code-generation orchestration).
- **Novel**: No existing corpus source note documents: (1) a company
  building foundation models deliberately optimized to reproduce human
  *irrationality* and mistakes rather than to be more capable/rational
  (Claim 4); (2) a quantified digital-twin behavioral-fidelity validation
  study with a test-retest-relative accuracy figure (Claim 2); (3) the
  "three data buckets" (interview / observational / causal-RCT) taxonomy
  for behavior modeling (Claim 5); (4) post-training on real,
  pre-registered RCT data (sourced from the Open Science Framework) as a
  technique for improving a model's human-behavior-prediction accuracy
  (Claim 7); (5) the "simulation shows a path to a goal, not a predicted
  outcome" framing, via the Foundation/psychohistory analogy (Claim 6);
  (6) Thomas Schelling's agent-based segregation model as historical
  grounding for LLM-based societal-scale agent simulation (Claim 11); (7)
  a critique of pure combinatorial/statistical persona-generation
  approaches as merely retrieving latent pretraining statistics rather
  than adding new information (Claim 14).

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add Claim 16's stated criterion for
  when prompting is sufficient versus when post-training/fine-tuning is
  required — "if the model has to learn the underlying physics of the
  world that it's operating in" (i.e., genuinely new domain knowledge the
  base model doesn't already trust) versus tasks where the model already
  has the relevant base statistics and can be steered via context alone.
  This gives a reusable heuristic distinct from generic "prompting vs.
  fine-tuning" tradeoff discussions already in the corpus, framed around
  *what kind of knowledge gap* the task has, not just cost or latency.
- **Chapter 03 (Verification)**: If the guide ever covers simulation-based
  or synthetic-user evaluation techniques, this source is directly
  relevant — but only after the contradiction filed as
  [#3310](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3310)
  is resolved, since this source's core claim (human behavior can be
  simulated with high fidelity) is in tension with the existing
  `blog-cursor-real-time-rl.md` citation recommended for Chapter 00. Do not
  cite Claim 2's 85% figure as a general endorsement of "simulated users
  are a reliable substitute for real user testing" without flagging that
  tension.
- **Chapter 00 (Principles)**: Add Claim 4 (optimizing for realism vs.
  optimizing for capability/rationality are different, sometimes opposing,
  objectives) as a specific counterexample to any "more capable model is
  strictly better" framing — for behavior-simulation and persona-fidelity
  use cases specifically, a more "rational" model can be a worse fit.

## Extraction Notes

- The full transcript was recovered by fetching the raw Substack HTML
  directly via `curl` (WebFetch's summarizing model returned only a
  high-level summary, not usable for verbatim quote extraction) and
  extracting the balanced `<div class="body markup">` container, which
  contained the complete episode introduction, "We discuss" outline,
  timestamps, and full speaker-labeled transcript (not paywalled — this
  episode's full transcript was in the free/public HTML). The transcript
  was read in full, start to end, before extraction; no sections were
  skipped or summarized without reading.
- All `Quote` fields were copied character-for-character from the parsed
  transcript text, including original curly quotation marks and em-dashes
  where present in the source's own rendering.
- One material discrepancy was found and flagged rather than smoothed
  over: the article's introduction (Claim 1) states "85–99% accuracy vs
  human focus groups," but the interview itself only substantiates the 85%
  figure (Claim 2) with a described methodology; no passage in the
  transcript explains or derives a 99% figure. Treat 85% as the
  citable number.
- A contradiction was identified between this source's core thesis (human
  behavior can be simulated with high, validated fidelity) and
  `blog-cursor-real-time-rl.md`'s architectural claim that real users
  "cannot be faithfully simulated." Filed as GitHub issue
  [#3310](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3310)
  per MINER.md §4a; no verdict was picked in this note.
- Cross-references verified: `blog-cursor-real-time-rl.md` Claim 1,
  `blog-openai-deployment-simulation.md` Claims 1 and 10, and
  `blog-anthropic-coderabbit-agent-orchestration.md` Claim 8 were each
  re-read in full before citing; no claim numbers were guessed.
- Three separate Prospector triage comments appear on the source issue
  (apparently from repeated/parallel triage passes), citing slightly
  different chapter relevance (Ch00/Ch02, Ch03/Ch04, Ch02/Ch03/Ch04). This
  note addresses the union of that guidance where the transcript
  substantively supports it (Ch00, Ch03, Ch04); no evidence was found in
  the transcript for a distinct "training/benchmark methodology" angle
  beyond what's captured in Claims 2, 3, and 7.
