---
source_url: https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/
source_type: blog-post
title: "Learning on the Shop floor"
author: Tobias Lütke (CEO, Shopify), quoted by Simon Willison
date_published: 2026-05-11
date_extracted: 2026-05-18
last_checked: 2026-05-18
status: current
confidence_overall: anecdotal
issue: "#796"
---

# Learning on the Shop floor

> Tobias Lütke (CEO, Shopify) describes River, Shopify's internal coding agent, as
> embodying "Lehrwerkstatt" (teaching workshop): a design philosophy where the agent
> operates exclusively in public Slack channels — refusing DMs — so that all work is
> visible, searchable, and observable, enabling "osmosis learning" with no curriculum,
> training plan, or manager required.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, May 11, 2026; link-blog format — a brief
  post presenting and commenting on Tobias Lütke's tweet at
  https://x.com/tobi/status/2053121182044451016. The underlying tweet is behind Twitter/X
  authentication and could not be directly fetched. All content attributed to Lütke comes
  from Willison's quotation of the tweet in his post. The Willison page is the canonical
  source URL per the issue submission.)
- **Author credibility**: Tobias Lütke is the CEO of Shopify, one of the world's largest
  e-commerce platforms, describing his own company's internal tool and organizational
  design philosophy — a direct first-person account from the decision-maker at scale.
  Simon Willison is the creator of Django, one of the highest-signal independent AI
  tooling commentators, and a designated trusted-feed author; his selection of this quote
  is itself a relevance signal. No vendor conflict of interest: Willison has no Shopify
  affiliation.
- **Scope**: Covers Shopify's River agent — specifically the design decision that River
  operates exclusively in public Slack channels — and the organizational philosophy behind
  that decision (Lehrwerkstatt / osmosis learning). Also covers Willison's Midjourney/Discord
  analogy as cross-domain corroboration of the visibility-as-learning mechanism. Does NOT
  cover: River's technical architecture, the prompts or harness behind River, how River was
  built, what coding tasks River performs, metrics on River's productivity impact, or any
  other Shopify AI tool. The source is brief (~300–400 words) and should be read as
  practitioner framing rather than a detailed case study.

## Extracted Claims

### Claim 1: Shopify's internal coding agent "River" operates exclusively in public Slack channels, refusing direct messages and suggesting users create public channels instead

- **Evidence**: Direct description by Tobias Lütke (CEO, Shopify) in his tweet, as quoted
  by Simon Willison. The design is specific and deliberate: River refuses DMs — this is an
  architectural constraint, not a default preference.
- **Confidence**: anecdotal (CEO's self-reported account of his own company's tool; no
  independent corroboration of the technical implementation)
- **Quote**: (no direct verbatim quote for this specific mechanic; the claim is consistently
  described across multiple fetches of the Willison post as River declining DMs and suggesting
  public channels)
- **Our assessment**: The "refuse DMs" design choice is not a usability decision — it is
  an organizational architecture decision. River is not optimized for individual convenience;
  it is designed to force work into the visible layer of the organization. This is a
  constraint that shapes behavior structurally, not just a default that users ignore. For
  practitioners: some agent capabilities that matter most for organizational adoption may
  require reducing individual convenience in favor of collective visibility. The constraint
  is the feature.

### Claim 2: Forcing all agent interactions into public channels makes every conversation searchable and allows anyone in the organization to observe and participate

- **Evidence**: Described by Lütke and Willison as direct consequences of the public-only
  design. The claim about searchability and open participation follows directly from Slack's
  public channel architecture — all public channel content is indexed and findable by all
  workspace members.
- **Confidence**: anecdotal (CEO's description; the mechanism is verifiable from Slack's
  architecture, but organizational impact is unquantified)
- **Quote**: (no direct verbatim quote; see Claim 3 for the framing principle)
- **Our assessment**: Searchability is the organizational memory dimension of this design.
  When an engineer or manager at Shopify wants to understand how a problem was approached,
  they can search across all River conversations — not just their own. This is distinct from
  traditional knowledge management (wikis, documentation) because the record is the actual
  work as it happened, not a curated post-hoc summary. For harness designers: logging agent
  interactions to a shared, searchable space — beyond internal audit logs — is an
  organizational capability worth engineering explicitly. It converts individual AI sessions
  into organizational institutional memory.

### Claim 3: Lütke calls this model "Lehrwerkstatt" (teaching workshop) — "the whole shop floor is the classroom," where learning happens through proximity to work rather than through a curriculum

- **Evidence**: Direct quote from Lütke's tweet as reproduced in Willison's post.
  "Lehrwerkstatt" is the German term for a teaching workshop — a traditional craft-education
  model where apprentices learn by working alongside experienced practitioners, not through
  formal instruction. The framing is Lütke's own, not an analyst's label applied afterward.
- **Confidence**: anecdotal (CEO's own framing of his company's philosophy; well-evidenced
  by the design decision described in Claim 1)
- **Quote**: "The whole shop floor is the classroom."
- **Our assessment**: The Lehrwerkstatt metaphor is the richest conceptual contribution in
  this source. It names a learning model that is: (a) **spatial** — learning requires
  proximity to where work happens; (b) **observational** — learning comes from watching,
  not being taught; (c) **non-hierarchical** — anyone near the work can learn, not just
  formal apprentices. Translating to AI agent deployment: the "shop floor" is the Slack
  channel; the "work" is the agent's interactions with real engineering problems; the
  "classroom" framing implies that the conversations themselves are the curriculum. For
  practitioners: this is a named pattern — if you want your organization to develop AI
  fluency through observation rather than training programs, visibility is the prerequisite,
  and a tool that refuses private operation is one way to enforce it.

### Claim 4: The visibility design enables "osmosis learning" — which requires no curriculum, training plan, or manager, only visible work that allows everyone to learn from each other

- **Evidence**: Direct quote from Lütke's tweet as reproduced in Willison's post.
  "Osmosis learning" is Lütke's term for knowledge transfer that happens through proximity
  and observation rather than instruction.
- **Confidence**: anecdotal (CEO's description of intended organizational outcome; no
  measurement of actual learning rates or knowledge transfer provided)
- **Quote**: "osmosis learning, because it does not require a curriculum, a training plan, or a manager."
- **Our assessment**: The "no manager required" framing is particularly significant for
  team adoption at scale. Most organizational AI adoption programs require managers to
  champion adoption, trainers to run sessions, and coordinators to monitor utilization.
  The Lehrwerkstatt model inverts this: if the tool is always public, learning is a
  byproduct of normal work rather than a parallel program. The prerequisite is not
  organizational buy-in for a training program — it is an agent that refuses private
  operation. For practitioners: the lever is tool design, not training design. Mandatory
  visibility substitutes for mandatory training. This has resource implications: the
  up-front cost is an architectural constraint in the agent; the ongoing cost is near
  zero.

### Claim 5: In Lütke's own Slack channel, over 100 people engage in River sessions — reacting, adding context, picking up threads, and helping with reviews

- **Evidence**: Lütke's own report of engagement in his channel, as cited by Willison.
  This is the only quantitative signal in the source.
- **Confidence**: anecdotal (self-reported engagement metric from the CEO's own channel;
  no methodology for what "engage" means; no company-wide engagement data provided)
- **Quote**: "over 100 people who, react to threads, add color and add context, pick up the torch, help with the reviews"
- **Our assessment**: The CEO's channel is a special case — Lütke's own River sessions
  attract more observers than a typical engineer's channel would, simply because of his
  organizational role. However, the scale (100+ active participants) suggests the engagement
  is not purely passive: "pick up the torch, help with the reviews" implies active
  co-participation, not just observation. The engagement pattern in the CEO's channel may
  be the best-case demonstration of the model rather than the average. For practitioners:
  expect variability in channel engagement depending on the organizational role and
  visibility of the person using the agent — peer learning works best when the observed
  work is done by someone whose judgment others want to understand.

### Claim 6: Willison believes Midjourney's early success with public Discord channels was driven by the same visibility mechanism — helping users learn text-to-image prompting by observing each other's attempts

- **Evidence**: Willison's own editorial commentary in the post. He marks this as a
  persistent interpretive position ("I continue to believe"), not a new claim. The
  Midjourney/Discord parallel is Willison's addition, not Lütke's.
- **Confidence**: anecdotal (one commentator's interpretation of Midjourney's growth
  trajectory; no empirical evidence cited on what drove Midjourney's early user-base
  expansion)
- **Quote**: "I continue to believe that the early success of Midjourney was tied to this mechanism, helping to compensate for how weird and finicky text-to-image prompting is."
- **Our assessment**: "I continue to believe" marks this as Willison's standing position
  across multiple posts, not a one-off observation. The Midjourney/Discord analogy is
  valuable as cross-domain corroboration: if forced public visibility independently drove
  rapid user learning in a different AI product (text-to-image generation), the mechanism
  may generalize beyond enterprise coding agents. The mechanism is consistent: when the
  domain is complex and outcomes unpredictable (text-to-image prompting; coding agent
  collaboration), watching others' work reveals latent effective patterns better than
  documentation or training. River in Slack applies this to enterprise coding agents;
  Midjourney in Discord applied it to consumer creative AI. Same learning pattern, two
  domains, independent evidence.

## Concrete Artifacts

### River Design Principles (from Lütke's tweet, as quoted by Willison)

```
Shopify's River Agent — Key Design Decisions
Source: Tobias Lütke (CEO, Shopify), via Simon Willison
        https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/
Original source: https://x.com/tobi/status/2053121182044451016

ARCHITECTURAL CONSTRAINT:
  - River operates exclusively in public Slack channels
  - River refuses direct messages (DMs)
  - When users attempt DMs, River suggests creating a public channel instead

ORGANIZATIONAL PHILOSOPHY:
  Name:    Lehrwerkstatt (German: teaching workshop)
  Concept: "The whole shop floor is the classroom."
  Mode:    "osmosis learning"

OSMOSIS LEARNING REQUIREMENTS:
  Required:     Visible work (public agent interactions)
  Not required: Curriculum
  Not required: Training plan
  Not required: Manager

OBSERVED OUTCOME (CEO's own channel):
  100+ people: react to threads, add color and context,
               pick up the torch, help with reviews
```

### The Visibility-as-Learning Pattern (Willison's cross-domain commentary)

```
Cross-domain comparison of forced-visibility learning:
Source: Simon Willison, simonwillison.net/2026/May/11/learning-on-the-shop-floor/

DOMAIN 1 — Consumer AI (Midjourney + Discord):
  Tool:        Midjourney text-to-image
  Channel:     Public Discord server
  Mechanism:   All image generations visible to all community members
  Outcome:     Users learned prompting by observing others' attempts
  Complexity:  "how weird and finicky text-to-image prompting is"
  Willison:    "I continue to believe that the early success of Midjourney was
               tied to this mechanism, helping to compensate for how weird and
               finicky text-to-image prompting is."

DOMAIN 2 — Enterprise AI (River + Slack):
  Tool:        River coding agent
  Channel:     Public Slack channels (enforced; DMs refused)
  Mechanism:   All agent interactions visible to all Shopify employees
  Outcome:     Engineers learn AI collaboration patterns by observing peers
  Complexity:  Learning how to direct an AI coding agent effectively

Common mechanism: forced visibility → observational learning → skill acquisition
                  without formal curriculum or dedicated training resources
```

## Cross-References

- **Corroborates**: `blog-bvp-shopify-ai-playbook.md` — The BVP/Shopify note establishes
  the organizational context: Shopify is one of the most aggressive AI adopters in tech,
  with deliberate design choices across infrastructure (LLM proxy), policy (no autonomous
  merges), and performance management (AI-reflexive behavior evaluations). Claim 7 in
  the BVP note ("Performance reviews evaluate 'AI-reflexive' behavior") shows Shopify
  using performance mandates to drive adoption; this source shows a complementary
  mechanism (visibility-by-design) that drives adoption through learning rather than
  mandate. Both corroborate Shopify's systematic, multi-lever approach to organizational
  AI integration. Neither note is a duplicate — BVP covers infrastructure and policy;
  this source covers learning culture design.

- **Corroborates**: `blog-cursor-paypal-enterprise-adoption.md` Claim 1 — PayPal's
  adoption rollout "spread organically as engineers witnessed peer accomplishments."
  PayPal's version was undesigned (organic spread from early adopters who demonstrated
  value to watching peers). Shopify's River version is the same mechanism deliberately
  engineered into the tool (forced public channels). Both demonstrate that observation of
  peers' AI-assisted work is a powerful adoption accelerator — Shopify's approach makes
  this systematic rather than incidental, and River's DM refusal is the structural
  guarantee that the observation opportunity always exists.

- **Extends**: `blog-bvp-shopify-ai-playbook.md` — The BVP note covers three pillars of
  Shopify's AI adoption approach: centralized control (LLM proxy), behavioral expectation
  (AI-reflexive performance reviews), and technical guardrails (no autonomous merges).
  This source adds a fourth pillar: learning culture through visibility (River's
  public-only design, Lehrwerkstatt philosophy). Together, the two notes provide the
  most complete picture in the corpus of how a single large organization has systematically
  designed AI adoption across multiple organizational levers simultaneously.

- **Novel**:
  - **"Lehrwerkstatt" as a named AI agent deployment pattern**: No prior corpus source
    names or describes visibility-as-learning as an explicit design philosophy for AI
    agent tools. The Lehrwerkstatt frame is conceptually distinct from "make AI work
    visible for auditing" (a safety/governance concern) or "share prompts in a wiki"
    (a knowledge management approach). It is an organizational learning model embedded
    into the agent's behavioral design.
  - **Agent refusal as an organizational learning mechanism**: River's refusal of DMs is
    the first example in the corpus of an agent deliberately constrained to produce
    organizational benefits (distributed learning) at the cost of individual convenience.
    No prior source documents an agent designed to refuse interaction modes for
    organizational rather than safety or security reasons.
  - **Midjourney/Discord as cross-domain validation**: Willison's comparison is the
    first corpus instance of using a consumer AI product's adoption pattern to validate
    an enterprise organizational design decision. The mechanism (visibility → learning)
    is domain-agnostic — it applied to text-to-image prompting complexity and applies
    to coding agent collaboration complexity.
  - **Osmosis learning as a named alternative to formal training programs**: The corpus
    has coverage of developer onboarding for AI tools (e.g.,
    `blog-anthropic-maccoss-developer-onboarding.md` on the trainee-developer analogy
    for individual skill-building). This source introduces a different question: not
    "how does an individual learn to use AI" but "how does an organization develop
    AI fluency at scale without formal training infrastructure." The Lehrwerkstatt
    answer — visibility is the curriculum — is new to the corpus.

## Guide Impact

- **Chapter 05 (Team Adoption) — Learning Culture Design**: Add the Lehrwerkstatt
  pattern as a named organizational strategy for developing team-wide AI fluency
  without a formal training program. Current corpus coverage of team adoption focuses
  on harness standardization, shared configuration files, and policy guardrails
  (from `blog-bvp-shopify-ai-playbook.md`). This source contributes the complementary
  learning-culture dimension: design AI tools for visibility, and skill transfer becomes
  a byproduct of normal work. The guide should present the Lehrwerkstatt model alongside
  structured training approaches as an architectural alternative — one that requires
  deliberate design commitment (agent refuses private operation) but pays no ongoing
  training overhead.

- **Chapter 05 (Team Adoption) — Adoption Mechanism Taxonomy**: Add the observation-based
  adoption pattern as a distinct named mechanism alongside structured-training adoption
  (`blog-cursor-nab-legacy-migration.md` sprint days model). The guide should distinguish:
  (a) organic peer observation — the observation pattern emerges without intervention,
  as PayPal experienced; (b) designed visibility — the tool architecture forces work
  public, making the observation pattern systematic and guaranteed, as Shopify designed
  with River. The Shopify/River example is the first in the corpus of approach (b) at
  enterprise scale with a named philosophy behind it.

- **Chapter 02 (Harness Engineering) — Observable Agent Behavior as Organizational
  Design**: Add the River pattern as a concrete example of designing for organizational
  observability as a first-class harness concern, distinct from audit logging and safety.
  Current corpus harness engineering content focuses on CLAUDE.md, hooks, tool permissions,
  and logging for debugging. This source introduces a different harness question: what
  interaction modes should the agent refuse, and why? River's DM refusal is a harness
  design decision with organizational learning consequences. Teams building internal AI
  agents should evaluate: should this agent be able to operate privately, and what does
  private operation cost in terms of organizational skill transfer?

## Extraction Notes

1. **Link-blog format and source depth**: This is a Simon Willison link-blog post —
   short (~300–400 words) with a featured quote from Lütke's tweet plus brief Willison
   commentary. The source is intentionally light on implementation detail. The Prospector's
   triage comment asks about barriers to adoption (privacy concerns, channel overload) and
   conditions under which the model works — these are not addressed in the source. They
   represent guide-authoring questions the Smith should address by synthesizing across
   sources, not gaps in this extraction.

2. **Underlying tweet not directly accessible**: The original Lütke tweet
   (https://x.com/tobi/status/2053121182044451016) returned HTTP 402 (payment required)
   and could not be fetched. All content attributed to Lütke is taken from Willison's
   quotation and paraphrase in his blog post. Quotes labeled as Lütke's should be read as
   "Lütke as quoted by Willison." Verbatim accuracy should be verified against the
   original tweet before use as a pull quote in the guide.

3. **Quote confidence levels**:
   - "The whole shop floor is the classroom." — appeared consistently across multiple
     WebFetch responses; treated as reliable verbatim from the Willison post.
   - "osmosis learning, because it does not require a curriculum, a training plan, or a
     manager." — consistent across fetches; treated as reliable verbatim.
   - "I continue to believe that the early success of Midjourney was tied to this
     mechanism, helping to compensate for how weird and finicky text-to-image prompting
     is." — consistent; Willison's own words; treated as reliable verbatim.
   - "over 100 people who, react to threads, add color and add context, pick up the
     torch, help with the reviews" — appeared in one fetch only; the unusual comma
     placement after "who," may indicate a WebFetch reconstruction rather than verbatim
     transcription. Verify against original before using as a pull quote.

4. **Cross-reference claim verification**:
   - `blog-bvp-shopify-ai-playbook.md` Claim 7 ("Performance reviews evaluate 'AI-reflexive'
     behavior") — verified by reading lines 70–74 of that note directly.
   - `blog-cursor-paypal-enterprise-adoption.md` Claim 1 ("spread organically as engineers
     witnessed peer accomplishments") — verified by reading lines 27–31 of that note directly.

5. **Confidence calibration**: Rated "anecdotal" overall. The CEO's account of his own
   company's tool is first-person and high credibility, but: (a) the source is brief and
   provides no operational depth; (b) the 100+ engagement metric is from the CEO's own
   channel — a high-visibility special case; (c) no independent validation of osmosis
   learning outcomes is provided; (d) the Midjourney claim is Willison's own interpretation
   marked as a persistent belief, not a measured finding.
