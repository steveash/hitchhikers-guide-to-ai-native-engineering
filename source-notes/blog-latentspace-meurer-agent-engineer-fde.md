---
source_url: https://www.latent.space/p/forward-deployed-engineers-aiewf
source_type: blog-post
title: "Forward Deployed Engineers and the future of software engineering"
author: Richard MacManus (interviewer, Latent Space) / Natalie Meurer (interviewee, Head of Agent Engineering, Sierra)
date_published: 2026-07-01
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: anecdotal
issue: "#1746"
---

# Forward Deployed Engineers and the future of software engineering

> A written Q&A interview (Latent Space, 2026-07-01) with Natalie Meurer, Head of
> Agent Engineering at Sierra, timed to her AI Engineer World's Fair session on
> forward deployed engineering (FDE). Meurer argues the FDE title has never had a
> consistent definition — it names customer accountability, not a fixed skill set —
> and that Sierra deliberately renamed the role "agent engineer" to foreground the
> technical work (orchestration-layer integration, "taste") over the customer-facing
> framing alone. She predicts product engineering and FDE work are converging and
> that engineering as a whole is heading toward a more generalist, holistic role
> definition rather than narrower specialization.

## Source Context

- **Type**: blog-post (written Q&A interview, not a podcast transcript)
- **Author credibility**: Richard MacManus is the interviewer/writer for this Latent
  Space piece. The substantive claims come from Natalie Meurer, Head of Agent
  Engineering at Sierra — a company building AI customer-service agents — who was
  interviewed ahead of her AI Engineer World's Fair (AIEWF) session on forward
  deployed engineering. This is first-person practitioner testimony from someone
  who runs an agent-engineering org at a named, prominent agent-building company,
  not a third-party analyst. It is a single interviewee's perspective, not a
  cross-company survey.
- **Scope**: Covers Meurer's definition of FDE, why Sierra uses "agent engineer"
  instead, what the work actually involves (orchestration layer vs. models,
  "taste," a financial-services example), and her predictions for how the FDE /
  product-engineering / AI-engineering role boundaries will evolve. Does not cover
  team structure/reporting lines, hiring criteria, or day-to-day tooling/workflows
  in operational detail — the interview stays at the level of role definition and
  industry prediction, not tactical practice.

## Extracted Claims

### Claim 1: The "forward deployed engineer" title has never had a consistent definition industry-wide; historically it is defined by accountability to customers rather than by a fixed shape of work
- **Evidence**: Direct answer to the interviewer's question "What is your definition
  of a forward deployed engineer?" — framed by Meurer as literally the topic of her
  AIEWF session.
- **Confidence**: anecdotal (single practitioner's characterization, though she
  frames it as the explicit subject of a conference talk, i.e. a considered
  position rather than an offhand remark)
- **Quote**: "That is really the point of my session: the role lacks a consistent
  definition."
- **Our assessment**: This is consistent with the corpus's existing FDE coverage —
  `blog-thebatch-fde-agents-aiact-issue355.md` (Claim 1) offers Andrew Ng's own
  first-person definition ("embedded within a client organization to help
  customize solutions, such as building and tuning agentic workflows") without
  flagging any definitional inconsistency. Meurer's claim that the term is
  contested industry-wide is itself a useful corrective: readers should not treat
  any single source's FDE definition (including Ng's) as the settled industry
  standard.

### Claim 2: Sierra deliberately named its customer-facing engineering role "agent engineer" rather than "forward deployed engineer," to make the title capture the shape of the technical work rather than only the customer-facing element
- **Evidence**: Direct answer explaining Sierra's naming choice.
- **Confidence**: anecdotal (single company's naming decision, but a first-person,
  deliberate one, not an inferred pattern)
- **Quote**: "The title should capture the shape of the technical work, rather than
  only the customer-obsession element."
- **Our assessment**: This is a concrete, checkable organizational fact (Sierra's
  actual job title) rather than a speculative claim, and it directly extends
  `blog-thebatch-fde-agents-aiact-issue355.md`'s FDE definition by showing a named
  company consciously rejecting the FDE label in favor of a title that foregrounds
  agent-building technical work. Useful for the guide's role-naming/career-track
  content as a concrete counter-example to assuming "FDE" is the default label for
  this kind of work going forward.

### Claim 3: Sierra's agent-engineer model was somewhat influenced by Palantir's forward-deployed-engineer model, but the title was intentionally changed
- **Evidence**: Direct answer to the interviewer's question about Palantir's
  influence on Sierra's role design.
- **Confidence**: anecdotal (single first-person confirmation)
- **Quote**: "Somewhat, although we intentionally called the role agent engineer,
  rather than forward deployed engineer."
- **Our assessment**: This grounds Claim 2 — Sierra isn't inventing a role from
  scratch, it is consciously repositioning a Palantir-style FDE model under a
  different title. This matters for the guide because it shows the "agent
  engineer" title is being used as a deliberate rebrand of FDE-style work at at
  least one major agent-building company, not a wholly distinct role category.

### Claim 4: Most customer-specific work in agent engineering happens at the orchestration layer, not inside the underlying models
- **Evidence**: Direct answer describing where customer-specific engineering effort
  actually goes.
- **Confidence**: anecdotal (single practitioner's first-person account of Sierra's
  own engineering split)
- **Quote**: "In practice, most customer-specific work takes place at the
  orchestration layer rather than in the models themselves."
- **Our assessment**: This is a specific, guide-relevant technical claim: it says
  where the customization effort actually concentrates (integration/orchestration,
  not model fine-tuning or prompt-only tricks). It corroborates the guide's general
  harness-engineering thesis that the orchestration/integration layer, not the
  model, is where most differentiated engineering value is created in production
  agent deployments — though this is one company's account, not a cross-company
  measurement.

### Claim 5: Agent engineering requires technical integration skill plus "taste" — judgment about what feels human and high-quality, illustrated via voice-agent design
- **Evidence**: Direct answer describing the skill mix the role requires, with a
  concrete illustrative example (voice agent tone/pacing).
- **Confidence**: anecdotal (single practitioner's framing of required skills, not
  a validated competency model)
- **Quote**: "You need to understand what sounds good and what will feel human when
  you are designing a voice agent."
- **Our assessment**: "Taste" as an irreducible human-judgment skill echoes
  `blog-anthropic-ai-native-engineering-org.md` (Claim 6), where an Anthropic
  engineering director describes product managers and designers needing to be
  involved for "product sense and taste" that Claude's code review cannot supply.
  The framing differs — Fung's claim is about PMs/designers reviewing agent
  output, Meurer's is about the agent engineer's own judgment while building the
  agent — but both independently name "taste" as the specific human-judgment
  quality that AI tooling does not replace, which strengthens this as a pattern
  worth citing in the guide rather than a one-off word choice.

### Claim 6: A financial-services dispute-processing example illustrates why agent engineering requires emotional-intelligence design, not just correctness
- **Evidence**: Concrete anecdotal example given by Meurer to illustrate the kind
  of customer interaction agent engineers must design for.
- **Confidence**: anecdotal (single illustrative example, not a case study with
  outcome data)
- **Quote**: "In financial services, for example, that might begin with dispute
  processing. It is complex and needs to be done correctly, but it is also a
  high-emotional-intelligence interaction. If somebody sees a fraudulent charge on
  their credit card statement, they may be frightened, and the agent needs to calm
  them down."
- **Our assessment**: This is the most concrete artifact in the interview — a
  specific customer-interaction scenario rather than an abstract skill claim. It
  grounds Claim 5's "taste" claim in a real design constraint (an agent that is
  technically correct but tonally wrong in a fraud-dispute conversation would
  fail the customer), which is useful as a worked example for any guide section
  discussing agent UX/tone design beyond task correctness.

### Claim 7: Product engineering and forward deployed engineering are converging, at least among the best practitioners in each role
- **Evidence**: Direct answer to a question about how the FDE role will evolve as
  companies build more internal expertise.
- **Confidence**: anecdotal (single practitioner's industry-trend prediction, not
  measured data)
- **Quote**: "Product engineering and forward deployed engineering are therefore
  converging in some respects — at least among the best people in each role."
- **Our assessment**: This is a forward-looking structural prediction, not a
  description of current state. It should be flagged as such in the guide rather
  than presented as an already-settled organizational fact. See Cross-References
  below — this claim is in direct tension with a specialization prediction
  elsewhere in the corpus, filed as a contradiction (issue #1764).

### Claim 8: Meurer leans toward generalists becoming more valuable, not specialists, as code becomes cheaper to produce
- **Evidence**: Direct answer to a question about whether developers will
  increasingly need product/customer-facing skills, presenting two possible views
  and stating her own lean.
- **Confidence**: anecdotal (single practitioner's stated preference between two
  named alternative futures, not a resolved prediction)
- **Quote**: "The other view, which I lean towards, is that generalists will become
  more valuable."
- **Our assessment**: Meurer explicitly frames this as her lean between two
  possible futures, not a certainty — this hedge should be preserved when citing
  the claim in the guide. It corroborates `blog-thebatch-ng-aiteam-structure.md`
  (Claim 6: generalists excel in 2-10 person AI-native teams; Claim 7: the
  generalist model means deep-plus-broad, not shallow-everywhere), though that
  claim is explicitly scoped to small teams while Meurer's is an industry-wide
  claim about how the FDE/product-engineering boundary evolves. It directly
  contradicts `blog-thebatch-fde-agents-aiact-issue355.md` (Claim 5: the AI
  Engineer role will specialize into named sub-roles like LLMOps and Evals
  Engineering) — filed as contradiction issue #1764, verdict pending.

### Claim 9: Meurer expects engineering as a whole to move toward a more holistic role definition that absorbs what is currently split across forward deployed engineering, go-to-market engineering, agent engineering, and AI engineering
- **Evidence**: Direct answer to a question about whether "agent engineer" could
  become the default term for this kind of work.
- **Confidence**: anecdotal (single practitioner's long-range industry prediction)
- **Quote**: "I expect engineering as a whole to move towards a more holistic
  definition, one that may incorporate more of what we currently call forward
  deployed engineering."
- **Our assessment**: This is the clearest statement of Meurer's overall thesis —
  today's proliferation of adjacent titles (FDE, GTM engineer, agent engineer, AI
  engineer) is, in her view, a transitional state rather than a stable end state.
  This is a genuinely novel framing for the corpus: prior sources (Ng's Batch
  pieces) treat FDE, AI Engineer, and specialized sub-roles as roles that will
  persist and multiply; Meurer treats the current title proliferation itself as
  the anomaly that will resolve toward fewer, broader roles.

### Claim 10: When code becomes cheap to author, it becomes easier to translate customer insights directly into a product
- **Evidence**: Direct statement connecting the economics of AI-assisted coding to
  the generalist/convergence argument.
- **Confidence**: anecdotal (single practitioner's causal claim, stated as a
  general mechanism rather than illustrated with a specific example)
- **Quote**: "When code becomes cheap to author, it also becomes easier to
  translate customer insights directly into a product."
- **Our assessment**: This is the mechanism Meurer offers for Claims 7-9: cheap
  code authorship shortens the distance between "engineer who talks to customers"
  and "engineer who ships the fix," which is why she expects the FDE/product
  boundary to dissolve rather than harden into separate specialisms. It parallels
  (without directly citing) the "distance collapsing" framing in
  `blog-anthropic-code-w-claude-london-2026.md` (per its citation in
  `blog-anthropic-ai-native-engineering-org.md`'s Cross-References: "you describe
  a problem, and the program shows up") — both describe cheap code production
  collapsing an organizational distance, though Cherny's framing is about the
  engineer-to-running-program distance and Meurer's is specifically about the
  customer-insight-to-product distance.

## Concrete Artifacts

No code, config, transcripts, or metrics are present in this source — it is a
prose Q&A interview about role definition and industry prediction, with one
illustrative customer-interaction example (Claim 6). There is no artifact to
extract into a fenced code block.

## Cross-References

- **Corroborates**:
  - `blog-thebatch-ng-aiteam-structure.md` (Claims 6-7): generalists excelling in
    small AI-native teams, and "generalist" meaning deep-in-one-role plus
    functional fluency in adjacent roles rather than shallow everywhere. Meurer's
    Claim 8 (generalists becoming more valuable) reaches a similar conclusion from
    an industry-labor-market angle rather than a small-team-structure angle.
  - `blog-anthropic-ai-native-engineering-org.md` (Claim 6): "taste" named as the
    specific human-judgment quality AI tooling does not replace — there for
    PM/designer review of agent output, here (Claim 5) for the agent engineer's
    own design judgment.
  - `blog-thebatch-fde-agents-aiact-issue355.md` (Claim 1): Ng's FDE definition
    ("embedded within a client organization... building and tuning agentic
    workflows") is structurally consistent with Meurer's account of orchestration-
    layer, customer-integration work (Claim 4), even though the two sources use
    different titles for the role.

- **Contradicts**: `blog-thebatch-fde-agents-aiact-issue355.md` (Claim 5: the AI
  Engineer role will specialize into named sub-roles — LLMOps Engineer, Evals
  Engineer, AI Data Engineer — following the historical frontend/backend/mobile
  specialization pattern). Meurer's Claims 7-9 predict the opposite structural
  direction: role boundaries converging into a broader, more generalist/holistic
  engineering definition. Filed as **contradiction issue #1764** (Miner-filed,
  verdict pending) — do not treat either direction as the guide's settled
  position on how AI-native engineering roles will structurally evolve until that
  issue is resolved.

- **Extends**: `blog-pragmaticengineer-ai-hiring-market-2026.md` (Claim 9: the
  AI/ML/FDE job market described by multiple respondents as historically hot,
  with unsolicited inbound offers). That note documents FDE as a *hiring-market*
  phenomenon (compensation, demand) without describing what the work actually
  involves. This source fills that gap directly: it describes what an
  agent-engineer/FDE-equivalent role at a leading agent-building company actually
  does day to day (orchestration-layer integration, voice/chat agent design,
  "taste"), per Claims 4-6.

- **Novel**: The claim that "forward deployed engineer" itself lacks a consistent
  industry definition (Claim 1) is new to the corpus — prior FDE sources (Ng's
  Batch editorial) state a definition without flagging definitional
  inconsistency as an issue. The specific example of a company (Sierra)
  deliberately rejecting the FDE title in favor of "agent engineer" for
  technical-work-framing reasons (Claims 2-3) is also new — the corpus previously
  had FDE and AI Engineer as the two named role categories (per
  `blog-thebatch-fde-agents-aiact-issue355.md`) without "agent engineer" as a
  third, deliberately-differentiated title.

## Guide Impact

- **Ch01 (Daily Workflows)**: Where the guide discusses the FDE/agent-engineer
  role, add Sierra's "agent engineer" title (Claims 2-3) as a concrete example of
  companies moving away from the "forward deployed engineer" label toward titles
  that foreground the technical (orchestration-layer, agent-building) work — and
  flag, per Claim 1, that "FDE" itself is a contested, inconsistently-defined
  term industry-wide, so the guide should not present any single definition
  (including Ng's in `blog-thebatch-fde-agents-aiact-issue355.md`) as canonical.

- **Ch05 (Team Adoption)**: The generalist-vs-specialist prediction (Claims 7-9)
  should be added to any team-structure/career-track guidance as a `**Debated:**`
  point once contradiction issue #1764 is resolved — currently the corpus has
  Meurer (Sierra) predicting convergence/generalism and Ng (Batch 355) predicting
  specialization into named sub-roles, with no empirical data yet on either side.
  Until resolved, the guide should present both directions rather than picking
  one, per the Editorial Constitution's contradiction-handling tenet.

## Extraction Notes

This source was accessed via automated fetch-and-summarize tooling rather than a
direct HTML/text dump, since the underlying tool declines full verbatim
reproduction of copyrighted third-party text. To compensate, every quote above
was independently re-verified with a targeted follow-up fetch asking for the
exact character-for-character sentence (not a summary) around each claim, and
several quotes (the orchestration-layer sentence, the Palantir question/answer,
the "taste" sentence) were cross-checked twice across separate fetches and came
back identical both times — this gives reasonable confidence the quotes are
accurate, though it is not the same guarantee as reading raw HTML directly. The
Assayer should spot-check at least the longer quotes (Claim 6's dispute-
processing example) against the live source URL. No linked sub-pages were
followed — the source is a single-page Q&A interview with no substantive
internal links to related content. The interview is fairly short (a focused
Q&A, not a long-form essay); 10 claims is close to full coverage of its
substantive content rather than a sign of under-reading, but there is little
room left for additional claims — team structure, hiring criteria, and
day-to-day tooling are simply not covered by this source (noted explicitly in
Source Context → Scope).
