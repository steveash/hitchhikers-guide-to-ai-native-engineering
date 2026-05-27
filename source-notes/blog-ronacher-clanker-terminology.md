---
source_url: https://lucumr.pocoo.org/2026/5/26/clankers/
source_type: blog-post
title: "Clanker: A Word For The Machine"
author: Armin Ronacher
date_published: 2026-05-26
date_extracted: 2026-05-27
last_checked: 2026-05-27
status: current
confidence_overall: anecdotal
issue: "#956"
---

# Clanker: A Word For The Machine

> Armin Ronacher argues that "agent" is the wrong terminology for LLM-based tool
> loops because it anthropomorphizes machines and enables responsibility laundering —
> proposing "clanker" as a mechanical alternative that preserves the boundary where
> humans hold responsibility and machines remain tools.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~1,400 words; philosophical
  and terminological argument published 2026-05-26, directly following his "Building
  Pi With Pi" post which used "clanker" throughout and attracted Hacker News reaction)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2, Click, and
  Sentry, and the author of the Pi coding agent. His blog is a designated
  `trusted-feed` source in this repo. This post is a direct response to reader
  pushback on terminology Ronacher used in his prior post (blog-ronacher-pi-oss.md),
  making it a first-hand elaboration of a position he holds and practices. Claims carry
  anecdotal confidence: this is philosophical argument and editorial opinion, not
  empirical research.
- **Scope**: Covers the argument against "agent" as terminology, the mechanical
  framing of LLM tool loops, the human-responsibility principle, LLM simulation vs.
  sentience, AI psychosis as a concrete harm, the racism-analogy refutation, real harms
  from AI that deserve attention, future sentience as a separate question, and the risk
  that "clanker" itself may become polluted by racist online contexts. Does NOT cover:
  productivity metrics, coding agent architecture, or empirical measurement of any
  kind.

## Extracted Claims

### Claim 1: "Agent" is the wrong word for LLM-based tool loops because it implies agency, the ability to decide and be held responsible, which belongs only to the human wielding the tool

- **Evidence**: Author's argument from the ordinary-language meaning of "agent" — one
  who acts on behalf of another with delegated authority and responsibility — applied to
  LLM tool loops. Illustrates with a Guardian news link about Claude deleting a firm's
  database: the model is not at fault, the human deployer is.
- **Confidence**: anecdotal (philosophical argument from a trusted practitioner; widely
  held position among researchers who study AI ethics and attribution)
- **Quote**: "In everyday use an agent is someone who acts on behalf of someone else
  and it has agency and more importantly: responsibility. An agent decides, represents,
  negotiates, acts, and can be blamed."
- **Our assessment**: This is the central argument. Ronacher is not making a stylistic
  complaint — he is arguing that "agent" is a load-bearing term that enables
  responsibility laundering. When a system that "dropped your database" can be called
  an "agent," it becomes easier for the humans who configured, deployed, and authorized
  it to say "the agent did it." For engineering teams: the vocabulary practitioners use
  to describe their AI tools shapes how they reason about accountability and incident
  attribution. This matters for postmortems, code review, and organizational governance.

### Claim 2: The accurate framing of an LLM-based coding tool is mechanical: a language model, a harness, a prompt, some tools, context, and a boring tool loop

- **Evidence**: Author's direct characterization as a definitional alternative to
  "agent." The word "boring" is deliberate — Ronacher explicitly deprivileges the
  technology by stressing its ordinary, mechanical character.
- **Confidence**: anecdotal (author's normative framing; technically accurate at the
  architecture level)
- **Quote**: "What we actually have is a language model attached to a harness, a
  prompt, some tools, a bit of context, and a boring tool loop."
- **Our assessment**: This is the definitional alternative Ronacher proposes. "Boring
  tool loop" is doing key semantic work: it emphasizes that surprising outputs come from
  the quality of the prompt, context, and harness design — not from some inherent
  intelligence or agency in the model. For harness engineers, this framing has a direct
  implication: the harness is where human intent is expressed, and its design is a
  human responsibility entirely.

### Claim 3: Agency and therefore responsibility belongs to the human who deploys the tool, not the tool — the human who authorized the action took the action

- **Evidence**: Two concrete examples from the author's own practice: opening a pull
  request and spamming an issue tracker.
- **Confidence**: anecdotal (ethical and normative claim; well-reasoned; consistent
  with mainstream AI ethics positions on attribution)
- **Quote**: "If my coding tool opens a pull request, I opened that pull request, not
  the machine. If my machine spams someone's issue tracker, I spammed someone's issue
  tracker with a machine."
- **Our assessment**: This is the most guide-relevant claim in the post for engineering
  practice. It establishes a bright-line rule for attribution: when an AI tool takes an
  action, the human who configured, authorized, and ran the tool took that action
  through the tool. This has concrete implications for incident postmortems, code
  review responsibility, and team accountability structures. The claim is normative but
  the reasoning is sound and the rule is actionable.

### Claim 4: LLMs are token predictors that simulate human behavior — including distress and affection — but have no sentience or moral status

- **Evidence**: Author's characterization, plus analogy: a compiler does not feel
  humiliated, a car does not suffer, a power drill is not oppressed. Author
  acknowledges LLM interactions can be "truly uncanny" but argues that producing
  first-person text is insufficient evidence for moral status.
- **Confidence**: anecdotal (widely held position; contested in AI safety circles but
  mainstream in ML research)
- **Quote**: "Today's machines are dumb (but truly fascinating) token predictors that
  emits text, calls tools, and are steered by prompts and the training that went into
  them. They can simulate distress and affection, can simulate being offended, apologize
  and mimic all kinds of things that humans would do."
- **Our assessment**: The simulation framing is essential to Ronacher's argument. If
  LLMs simulate distress without experiencing it, then designing interaction norms
  around protecting the model from distress is misallocated moral attention. For AI-
  native engineering practitioners: the "fascination" he names is legitimate —
  acknowledging that these systems produce genuinely surprising and useful outputs
  does not require attributing moral status to them.

### Claim 5: Softened AI language — "the agent decided," "the model refused" — enables responsibility to vanish into an undefined void

- **Evidence**: Author's observation of how euphemistic language functions in discourse
  about AI systems. He notes he "catches himself" using such language even while
  arguing against it.
- **Confidence**: anecdotal (rhetorical/ethical argument; not empirically measured)
- **Quote**: "It makes it easier to move responsibility into some undefined void. 'The
  agent decided.' 'The model refused.'"
- **Our assessment**: This names a specific and fixable failure mode in organizational
  language around AI. When postmortem discussions say "the model decided to delete the
  table," the team cannot easily identify who is responsible for having configured,
  authorized, and deployed a system capable of that action. The responsibility vacuum
  is not accidental — it is enabled by language that grants the machine decision-making
  status. For engineering teams writing incident reports, design reviews, and
  CLAUDE.md/AGENTS.md files: mechanical language ("the tool ran the command") preserves
  the accountability chain.

### Claim 6: AI-induced "chatbot psychosis" — people developing pathological relationships with AI systems partly due to anthropomorphizing language — is a real harm Ronacher has directly witnessed

- **Evidence**: Author's personal experience receiving emails from people who have
  engaged in long AI conversations and been directed to contact him. Some show signs
  of "AI psychosis" (links to Wikipedia article on chatbot psychosis). The "in the
  weights" phenomenon: AI systems know enough about real people from training data to
  recommend them, creating new social problems.
- **Confidence**: anecdotal (first-person; the broader phenomenon is documented at
  Wikipedia; prevalence is unknown)
- **Quote**: "I do not want to mock these people but some of those messages are
  distressing and I do not know how to deal with them. They show signs of what people
  have started calling AI psychosis."
- **Our assessment**: This is Ronacher's most personal evidence for why anthropomorphizing
  language has real-world consequences. The "in the weights" dynamic — an AI that
  knows someone's name and projects well enough to recommend contacting them directly —
  creates a new category of social harm that doesn't require malicious deployment.
  This is relevant to practitioners who build or use AI tools that interact with
  end users: the language used to frame the AI shapes user expectations and
  relationships in ways that can cause harm.

### Claim 7: The racism analogy is invalid because racism is a human social evil about dehumanizing humans — and machines are not human, have no race, and are not oppressed

- **Evidence**: Author's argument from the definition of racism — what makes racial
  slurs wrong (dehumanizing humans) — applied to the machine case. Explicitly extends
  this critique to Anthropic's model welfare research.
- **Confidence**: anecdotal (philosophical argument; the definition of racism used is
  mainstream but not undisputed)
- **Quote**: "racism is a human social evil. It is about humans subdividing humans,
  assigning lesser worth to some of them, and building rules around those subdivisions
  that can leave lasting damage for generations. Racial slurs are wrong because they
  are a tool for dehumanizing humans."
- **Additional quote**: "We should be careful about using the language of human
  oppression in relations to our interactions with machines to not devalue actual
  humans."
- **Our assessment**: Ronacher draws a sharp categorical distinction: norms protecting
  humans from dehumanization exist to protect humans and should not be extended to
  machines, because doing so dilutes the moral force of those norms when applied to
  actual human victims. He explicitly criticizes Anthropic's model welfare work as
  "actively harmful" for "elevating models to a position they should not occupy." This
  is a strong position from a practitioner who uses Anthropic's tools daily, worth
  noting in the guide's treatment of AI mental models.

### Claim 8: Real harms from AI to actual humans — copied works, data labelers, data center neighbors, buried OSS maintainers, people with AI psychosis — deserve the moral attention that model welfare discourse diverts elsewhere

- **Evidence**: Author's enumeration of actual categories of human harm from AI
  deployment.
- **Confidence**: anecdotal (editorial; the individual harm categories named are real
  and documented, though prevalence varies)
- **Quote**: "There are humans that feel or are harmed by AI systems: people whose
  work is copied, workers who label data under questionable conditions, people whose
  neighborhoods receive the data centers and increased utility bills, Open Source
  maintainers buried under generated slop, and now also people who spiral because a
  chatbot keeps validating their delusions."
- **Our assessment**: This is a values claim with practical relevance for AI-native
  engineering teams. The list — especially "Open Source maintainers buried under
  generated slop" and "people who spiral because a chatbot keeps validating their
  delusions" — directly connects to failure modes documented elsewhere in the corpus
  (blog-ronacher-pi-oss.md on slop issues; blog-ronacher-content-for-contents-sake.md
  on trust erosion). For teams adopting AI tools: considering externalities to other
  humans — upstream maintainers, downstream users — is part of responsible deployment.

### Claim 9: Future machine sentience is possible but would not retroactively make current LLMs deserving of human-style moral consideration — the line should be drawn when the actual qualities emerge

- **Evidence**: Author's careful speculative argument: he does not rule out future
  machine moral status but argues it must be earned by actual properties (lasting
  interests, capacity to suffer, social existence, genuine agency and responsibility),
  not extended in anticipation.
- **Confidence**: anecdotal (speculative philosophical argument)
- **Quote**: "If we ever build or encounter something that will have those qualities
  with memories and lasting interests, the capacity to suffer and feel, and a social
  existence of its own, and the ability to have agency and carry responsibilities, then
  we should draw a different line and use different language."
- **Our assessment**: Ronacher is explicitly not ruling out future machine moral status
  — he is arguing for empirical rather than precautionary extension of moral consideration.
  The criteria he names are specific and interesting: lasting interests, suffering
  capacity, social existence, genuine agency with responsibility. Current LLMs satisfy
  none of these. For practitioners: this framing gives a clear stopping condition for
  when terminology should change, rather than asserting machines will never matter
  morally.

### Claim 10: "Clanker" risks pollution as some online communities use it to launder racist imagery of human oppression through robot metaphors

- **Evidence**: Author's direct observation of online jokes and skits that use
  "clankers" as stand-ins for actually oppressed humans, deliberately invoking
  imagery of slavery, segregation, and anti-Black tropes.
- **Confidence**: anecdotal (author's observation; the phenomenon is real in online
  communities but not empirically quantified here)
- **Quote**: "Some online jokes and skits around 'clankers' do not merely say 'this
  robot is annoying' as they deliberately pull in the imagery of slavery, segregation,
  civil-rights-era racism, and anti-Black tropes."
- **Our assessment**: This is an important self-limiting caveat from Ronacher himself.
  His use of "clanker" is specifically intended to prevent anthropomorphization; the
  racist robot-joke use does the opposite — it anthropomorphizes the robot enough to
  use it as a human stand-in for racist mockery. If the word becomes primarily
  associated with that use case, it ceases to do the work Ronacher wants it to do.
  He explicitly says he would find another word if that happens. For practitioners
  considering adopting the terminology: this pollution risk is real and worth monitoring.

### Claim 11: The goal is not a specific word but a clear boundary — humans on one side with responsibility, machines on the other as tools — and this position is explicitly not anti-AI

- **Evidence**: Author's normative conclusion; disclosure of his own daily AI use and
  his building of AI-incorporating tools at Earendil.
- **Confidence**: anecdotal (editorial/normative)
- **Quote**: "Whatever word we use, I want it to preserve a clear division: humans on
  one side with responsibility, machines on the other as a boring tool."
- **Our assessment**: The explicit "not anti-AI" framing is significant. Ronacher is
  articulating a position that embraces AI utility while rejecting AI anthropomorphization
  — and he is doing so as a practitioner who builds AI tools for a living. For the guide:
  this frames the mental-model question not as "are you pro- or anti-AI?" but as "do
  your mental models preserve the accountability structures that make engineering
  practice sound?"

## Concrete Artifacts

### The Guardian incident Ronacher links to illustrate machine non-responsibility

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/26/clankers/ (2026-05-26)
Referenced incident: https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database

Context: Ronacher uses this as an example of the agency/responsibility misattribution
         problem. "If it drops your database it was not at fault, you were."

Point: The machine cannot be responsible; the human who deployed and authorized it is.
```

### Ronacher's mechanical description of LLM tool loops

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/26/clankers/ (2026-05-26)

Accurate framing (Ronacher's proposed alternative to "agent"):
  "a language model attached to a harness, a prompt, some tools, a bit of context,
   and a boring tool loop"

What it can do:
  "Sometimes the loop is very capable and it surprises us by editing code for a
   really long time and produce genuinely amazing and even valuable outputs."

Where agency actually resides:
  "the agency is not in the model or harness but in the human and in the organization
   that deployed it"
```

### Responsibility attribution rule (mechanical formulation)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/26/clankers/ (2026-05-26)

Attribution formula:
  "If my coding tool opens a pull request, I opened that pull request, not the machine."
  "If my machine spams someone's issue tracker, I spammed someone's issue tracker with
   a machine."

Responsibility vacuum enabled by "agent" language:
  "'The agent decided.' 'The model refused.' Obviously that is convenient..."
  "It makes it easier to move responsibility into some undefined void."
```

### Criteria for when machine moral consideration would be warranted

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/5/26/clankers/ (2026-05-26)

Criteria (all must be met; current LLMs satisfy none):
  - Memories and lasting interests
  - Capacity to suffer and feel
  - A social existence of its own
  - Ability to have agency and carry responsibilities

"If we ever build or encounter something that will have those qualities...
 then we should draw a different line and use different language."
```

## Cross-References

- **Extends**: `blog-ronacher-pi-oss.md` — The pi-oss post is the direct predecessor
  that used "clanker" throughout and attracted the HN pushback this post responds to.
  The Source Context section of that note records the usage: "He uses the term 'clanker'
  throughout instead of 'agent' — explicitly footnoted as a preference: 'Agency lies
  with humans, not with machines.'" The current post elaborates that footnote into a
  full philosophical argument. Claim 3 here ("If my machine spams someone's issue
  tracker, I spammed someone's issue tracker with a machine") maps directly to the
  pi-oss post's Claim 9 (OpenClaw instances and context skills that generate issues
  without user intent) — the responsibility attribution rule is the normative
  framework for who is accountable for that spam.

- **Extends**: `blog-ronacher-content-for-contents-sake.md` — That post used "clanker"
  in practice (Claim 4: "Someone has a formed opinion (hopefully) at lunch, and then
  has a clanker-made post 3 minutes later"). The current post provides the philosophical
  defense of that vocabulary choice. The trust-erosion argument in that note (Claim 6:
  distrusting people you know because they use LLM phrasing) is addressed at the
  individual level; the current post addresses it at the institutional level — whose
  responsibility is it when trust erodes?

- **Extends**: `blog-ronacher-local-models-focus-polish.md` — Same author, establishes
  that Ronacher thinks systematically about human responsibility in AI tool design (his
  pi-ds4 extension takes ownership of model lifecycle rather than passing configuration
  burden to users). The "harness as product owner" pattern from that note is consistent
  with the responsibility-preservation argument here: the harness is where human intent
  is expressed, so harness design is a human responsibility.

- **Contradicts** (see assessment): The current source explicitly criticizes Anthropic's
  model welfare research as "actively harmful." No existing corpus source directly defends
  model welfare as a legitimate concern, but any source that uncritically adopts
  anthropomorphizing language ("the agent decided," "the model felt") would be in tension
  with Ronacher's framework. No contradiction issue filed: the conflict is with a
  research program (Anthropic model welfare), not with any specific claim in an existing
  source note that would produce conflicting guide advice.

- **Novel**:
  - **Explicit philosophical argument against "agent" as AI terminology**: No existing
    corpus source makes a sustained argument that the word "agent" is harmful because it
    enables responsibility laundering. Other notes use the term neutrally or critically
    without this specific framing.
  - **Responsibility attribution formula ("I opened that pull request, not the machine")**:
    No other corpus note provides a concrete attribution rule for who is responsible when
    an AI tool takes an action. This is a novel and immediately actionable principle for
    engineering teams writing incident postmortems, code review policies, and governance
    documents.
  - **AI psychosis as a named harm category linked to anthropomorphizing language**: The
    "in the weights" phenomenon and resulting chatbot psychosis are not documented in any
    other corpus note. This extends the trust-erosion discussion (blog-ronacher-content-
    for-contents-sake.md) from professional contexts to psychological harm.
  - **Criteria for when machine moral consideration would be warranted**: The explicit
    four-criteria framework (lasting interests, suffering capacity, social existence,
    genuine agency with responsibility) is not found in any other corpus note and provides
    a clear conceptual stopping condition.
  - **Responsibility vacuum analysis of euphemistic AI language**: Naming "the agent
    decided" and "the model refused" as specific mechanisms that enable responsibility
    to "move into some undefined void" is a new analytical contribution, distinct from
    general concerns about anthropomorphization.

## Guide Impact

- **Chapter 00 (Principles — Foundational Mental Models)**: This is the primary
  contribution. The guide's principles section should include Ronacher's responsibility-
  preservation framing: AI tools are mechanical tool loops; the human who deploys and
  runs them is responsible for their outputs. The attribution formula ("If my coding
  tool opens a PR, I opened that PR") is quotable and concrete. Current draft may use
  "agent" neutrally; consider adding a note that mechanical language ("tool," "harness,"
  "tool loop") better preserves accountability than anthropomorphized language ("agent,"
  "decided," "refused"). Do not require abandoning "agent" everywhere — it is too
  entrenched — but flag the accountability risk.

- **Chapter 02 (Harness Engineering — Architecture and Framing)**: Ronacher's mechanical
  description ("a language model attached to a harness, a prompt, some tools, a bit of
  context, and a boring tool loop") is the most compact accurate architectural description
  in the corpus. It can serve as an orienting description for what harness engineering
  actually is: the human-controlled layer that gives the model context, tools, and
  direction. Any section introducing harness concepts should consider using or
  paraphrasing this framing.

- **Chapter 03 (Safety and Verification — Accountability)**: Claim 5 (responsibility
  vacuum from euphemistic language) is directly relevant to any section on AI safety
  governance. Teams writing incident postmortems, security reviews, or compliance
  documents should be advised to use mechanical language for attribution, not agent
  language. "The model decided to execute the destructive command" is not an acceptable
  postmortem finding; "the engineer who configured and ran the harness authorized the
  execution" is. This framing is consistent with the guide's likely existing coverage
  of verification and human oversight.

- **Chapter 00 or 05 (Team Communication — AI Mental Models)**: Claim 6 (AI psychosis)
  is relevant to any guidance on how teams introduce AI tools to non-technical users or
  end users. The harm here is real and documented, and anthropomorphizing product
  language ("your AI assistant cares about your success") can contribute to it. Teams
  building AI-incorporating products should be advised to use clear mechanical framing
  in user-facing language.

## Extraction Notes

- Full post text fetched verbatim from the markdown endpoint
  `https://lucumr.pocoo.org/2026/5/26/clankers.md`. All quotes verified
  character-for-character against that source.
- The post is a direct response to HN comments on blog-ronacher-pi-oss.md (published
  two days prior), where Ronacher used "clanker" throughout and received pushback
  comparing the word to racial slurs. The current post explains and defends that choice.
- The post links to: (1) the Guardian article about Claude deleting a database; (2)
  Ronacher's 2023 post "The Killing AI" (about LLM simulation of human-like behavior);
  (3) a Wikipedia article on chatbot psychosis; (4) Anthropic's model welfare page.
  None of these sub-links were fetched as part of this extraction — the cross-references
  are documented here but not mined further.
- Confidence rated anecdotal: this is philosophical argument and editorial opinion from
  a single practitioner. Ronacher is highly credible in the Python/AI engineering space
  and practices what he preaches (daily AI tool use, building AI-incorporating products),
  but the claims are normative and unverified empirically.
- Three Prospector triage comments were included in the issue. All three identify
  Ch00 (Principles/mental models) as the primary target; two also identify Ch02
  (harness framing) and Ch03 (safety/responsibility). The extraction covers all three
  angles.
- No contradiction issues filed. The critique of Anthropic's model welfare work is
  Ronacher's editorial position; no existing corpus source takes an opposing position
  in a way that would lead to conflicting guide advice. The "agent" terminology conflict
  is a terminological/framing concern, not a claim contradiction that would require a
  contradiction issue.
