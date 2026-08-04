---
source_url: https://simonwillison.net/2026/Jul/30/bruce-schneier/
source_type: blog-post
title: "Quoting Bruce Schneier: The Work vs. Gym Framework for Deciding When to Use AI"
author: Bruce Schneier (excerpted by Simon Willison); framework attributed to Daniel Miessler
date_published: 2026-07-30
date_extracted: 2026-08-04
last_checked: 2026-08-04
status: current
confidence_overall: emerging
issue: "#2468"
---

# Quoting Bruce Schneier: The Work vs. Gym Framework for Deciding When to Use AI

> Schneier (via a Willison link-blog excerpt) names a decision heuristic — borrowed from
> AI researcher Daniel Miessler — for when to delegate a task to AI: if the task is
> "work" (only the output matters), use AI; if the task is "gym" (the process itself
> builds a skill you need), don't. He applies it concretely to his own policy-writing
> assignments, arguing that AI-drafted homework skips the "gym" function of writing —
> developing critical thinking — and that skill atrophy from this substitution is
> already visible to employers.

## Source Context

- **Type**: blog-post (Simon Willison link-blog excerpt, one paragraph, with attribution
  — Willison's page reproduces a single passage from Schneier's essay without added
  editorial commentary). The excerpted essay itself originally appeared in *The
  Guardian* on 2026-07-24 (https://www.theguardian.com/commentisfree/2026/jul/24/should-you-use-ai)
  and was cross-posted to Schneier's own blog on 2026-07-30
  (https://www.schneier.com/blog/archives/2026/07/should-you-use-ai-for-a-task-heres-a-simple-way-to-decide.html),
  titled "Should You Use AI for a Task? Here's a Simple Way to Decide." This note
  extracts from the full Schneier essay (fetched directly), not just the one-paragraph
  Willison excerpt, per MINER.md's instruction to follow substantive linked pages. It
  additionally follows two links out of the Schneier essay: Daniel Miessler's original
  framework post and a Futurism article Schneier cites as evidence that "employers are
  already noticing" skill atrophy.
- **Author credibility**: Bruce Schneier is a security technologist and Fellow at the
  Harvard Kennedy School's Belfer Center, and teaches public policy at Harvard Kennedy
  School and the Munk School at the University of Toronto — the essay is written from
  direct classroom experience grading his own students' AI-assisted writing, not
  secondhand commentary. Simon Willison (creator of Django, high-signal independent AI
  tooling commentator) selected this piece for his curated feed, itself a relevance
  signal already established in this corpus. Daniel Miessler, credited by Schneier as
  the framework's originator, is an independent security/AI writer and consultant
  (danielmiessler.com) — not previously present in this corpus.
- **Scope**: Covers a personal decision heuristic for when to use AI (work vs. gym),
  applied specifically to writing/education, then extended by Schneier to creative
  professions (writing, visual art) more broadly. Does NOT cover software engineering,
  coding tasks, or team/organizational adoption processes directly — the essay's frame
  is individual cognitive-skill-development, and the guide-relevant extraction here is
  by analogy (writing-as-skill maps to coding-as-skill), not direct software-engineering
  reporting. Does NOT include data beyond the single Futurism-cited FT anecdote for the
  "employers are already noticing" claim — no survey, study, or measured attrition rate
  is given by Schneier himself.

## Extracted Claims

### Claim 1: Schneier frames the core decision heuristic as "work vs. the gym," explicitly attributed to AI researcher Daniel Miessler
- **Evidence**: Schneier's own essay text, direct attribution.
- **Confidence**: anecdotal (a named heuristic borrowed from another author, not an empirical claim)
- **Quote**: "The best way I've found to explain the dilemma comes from the AI researcher Daniel Meissler: it's the difference between work and the gym."
- **Our assessment**: Worth noting Schneier spells the name "Meissler" throughout his essay; Miessler's own site spells it "Miessler" — an apparent transcription error on Schneier's part, reproduced verbatim here as it appears in the source. The underlying framework is genuinely Miessler's (see Claim 9 for his original "Job vs. Gym" framing), so this note cites both spellings where relevant to avoid ambiguity.

### Claim 2: The heuristic is explained by analogy — assistive technology is appropriate at work, but defeats the purpose at the gym
- **Evidence**: Schneier's direct exposition of the borrowed framework.
- **Confidence**: anecdotal
- **Quote**: "At work, if your job is to move a bunch of heavy things from one side of the room to another, you should use whatever assistive tech you have on hand: a wagon, a forklift… even an AI-powered robot. But at the gym, it makes no sense for that robot to lift weights for you. The point of weightlifting isn't to move heavy things across the room; it's to actually lift those heavy things."
- **Our assessment**: This is the cleanest, most portable version of the analogy in the essay and is likely the best pull-quote for guide use — it makes the distinction concrete before Schneier gets to the more abstract "who cares how" formulation in Claim 3.

### Claim 3: The operational decision rule is: use AI if no one cares how the task got done; avoid AI if the process is as important as the outcome
- **Evidence**: Schneier's own restatement of the heuristic as a generalizable rule, immediately following the analogy.
- **Confidence**: anecdotal (a proposed heuristic, not tested against counterexamples in the essay)
- **Quote**: "The same analysis holds for any task an AI can do for you. If it's work—if the task has to be done and no one cares how—then it's fine to use AI assistance. But if the task is more like the gym, and how the task is done is at least as important, then it probably doesn't make sense to use AI."
- **Our assessment**: This is the most directly reusable line for a guide decision-framework section — it's a two-branch test ("does anyone care how?") rather than a vague appeal to caution. It is a self-report heuristic without falsification criteria, though; the essay doesn't address how to resolve disagreement about whether a given task counts as "work" or "gym" (e.g., a junior engineer and a tech lead might classify the same debugging task differently).

### Claim 4: The heuristic presupposes the AI is already reliable and trustworthy for the task — it doesn't apply if the AI can't do the job well in the first place
- **Evidence**: Schneier's own caveat, inserted between the general framework and his specific application to writing.
- **Confidence**: anecdotal
- **Quote**: "This, of course, assumes that the AI is actually up for the task and that it's trustworthy: that it can do the job well, that its mistakes are minimal and correctable, that it's been secured from cyber-attacks that would influence its results. Those are all important, and shouldn't be minimized. There's no point giving an AI something that it can't do reliably. But once you're confident that the AI can perform the task, the work vs. gym distinction helps you decide if it should."
- **Our assessment**: This is a "can vs. should" framing — capability is a gate that must be satisfied before the work-vs-gym question is even worth asking. Useful for a guide section that wants to separate "is the model good enough" (a capability/verification question, already well covered elsewhere in this corpus) from "should a human do this regardless" (the novel contribution of this source).

### Claim 5: Schneier classifies his own policy-writing assignments as "gym tasks" — their value is in the thinking/drafting/revising process, not in producing another memo
- **Evidence**: Schneier's first-person application of the framework to his own teaching practice.
- **Confidence**: anecdotal (personal pedagogical judgment, not a study)
- **Quote**: "The writing assignments I give my students are gym tasks, not work tasks. I ask them to write policy memos not because the world needs more policy memos. I assign them because the very act of writing, which includes thinking and outlining and drafting and editing, making and criticizing and revising arguments, will help develop the critical thinking skills they will need in their future careers. And without this constant mental exercise, those skills will atrophy. Employers are already noticing."
- **Our assessment**: This is the passage the Prospector's triage flagged and the one Willison excerpted verbatim. The "employers are already noticing" clause links out to a Futurism article (see Claim 7) rather than standing alone as an unsupported assertion — worth surfacing that link explicitly since Willison's excerpt strips the hyperlink context.

### Claim 6: Schneier reports he can currently distinguish AI-written from student-written memos, characterizing AI output as polished but not well-reasoned
- **Evidence**: Schneier's own first-person grading experience.
- **Confidence**: anecdotal (single instructor's subjective assessment, not blind-graded or measured)
- **Quote**: "At least today, I can pretty easily tell the difference between an AI-written memo and a student-written one—especially if the student just turns in what the chatbot produces. It's a catchy, plausible, grammatically perfect essay that's not particularly well-crafted or logically coherent—and with all the tells of mid-2026 AI-generated writing."
- **Our assessment**: The "at least today" qualifier is doing real work — Schneier is explicit that this detectability is a present-tense, possibly temporary state, not a durable property of AI writing. A guide citing this should not treat "AI writing is detectable" as a stable assumption.

### Claim 7: Students misread confident, polished AI prose as evidence of good ideas, missing that the struggle of writing is itself part of thinking
- **Evidence**: Schneier's own pedagogical observation, contrasting his students' behavior with his own developed skill at separating style from substance.
- **Confidence**: anecdotal
- **Quote**: "My students don't have that skill; they mistakenly view a confident, well-written essay as evidence of the quality of their ideas... What the students miss is that their initial discomfort is a normal and healthy stage of writing, and not something to quickly get beyond. The very act of struggling with how to express what they think is an important part of the process. It's how they test out their ideas, examine their hypotheses, and actually figure out what they think. Homework is not work; it's the gym."
- **Our assessment**: This is the most cognitively specific claim in the essay — it's not just "skills atrophy from disuse," it's a mechanism claim: writing is a discovery process for the writer's own thinking, and skipping the discomfort of drafting skips the actual thinking, not just the labor of transcription. This mechanism claim is not empirically tested in the essay (no comparison of AI-assisted vs. non-AI-assisted student reasoning quality), but it is a specific, falsifiable-in-principle mechanism rather than a vague "atrophy happens" assertion.

### Claim 8: Schneier extends the framework to professional writing broadly, distinguishing "work writing" (dry, instrumental) from "gym writing" (art), and predicts reduced demand for human writers as AI absorbs the former
- **Evidence**: Schneier's own extension of the classroom argument to the labor market for writers.
- **Confidence**: anecdotal (a market prediction, not measured; no citation of actual writer-employment data)
- **Quote**: "Most of the time when someone hires a writer, they just need the words. They need an instruction manual for a piece of equipment, a detailed sales presentation, a government-mandated disclosure document, or a legal brief. They need dry, predictable, accurate writing: a piece of work, exactly what AIs are good at today and what I don't want in my student assignments. Only sometimes is writing an art form—a book, a poem, an uplifting political speech. That kind of writing is more like the gym: process matters just as much as product... Now, for the first time in human history, we can separate out when we need writing as work and when we want writing as gym. And if AI can do most of the work-type writing, society doesn't need as many human writers."
- **Our assessment**: Directly analogous to this corpus's existing "code as capital asset → code as consumable" claim (`blog-simonwillison-charity-majors-code-economics.md` Claim 3) — Schneier is making the identical supply-side argument for writing labor that Majors makes for code: once the "work"-category output is cheap and instant, the economics and labor demand for that category collapse, leaving only the "gym"/art-category demand intact. Neither source cites the other; this is an independent convergence on the same structural argument applied to a different craft.

### Claim 9: Same work-vs-gym logic applied to visual art — most commissioned visual work is "just an image," not art, and AI absorbing that category reduces overall demand for illustrators
- **Evidence**: Schneier's own extension by analogy, no separate citation given.
- **Confidence**: anecdotal
- **Quote**: "It's the same for visual artists. Sometimes we need an actual artist, but most of the time we just need an image: a corporate mascot, a "beware of the dog" sign, or a packaging label. Historically we gave those jobs to artists, and sometimes beautiful art resulted. But most of the time it was just work. And, as it turns out, the world needs less pure art than simple images."
- **Our assessment**: This is a secondary application of the same argument (Claim 8) to a different craft, offered without independent evidence — it strengthens the generality of the work/gym economic-displacement argument but adds no new evidentiary weight beyond Schneier's own assertion.

### Claim 10: Schneier names a structural incentive problem — no one is paid to protect their own "gym" skills, and the payoff from doing so is diffuse and easy to discount against AI's immediate productivity gains
- **Evidence**: Schneier's own explanation for why the work-vs-gym distinction, though clear in theory, is hard to act on in practice.
- **Confidence**: anecdotal
- **Quote**: "There's also an incentive problem. No one pays us to go to the gym; maintaining healthy habits requires discipline. For me, the payoffs to exercise—fewer aches and pains, less fatigue, better mood/stress management—might make me a better writer and teacher, but they're subtle and easy to miss. For my students, incremental improvements in their reasoning and writing are equally subtle."
- **Our assessment**: This is the most organizationally actionable claim in the essay for a guide audience — it names *why* a purely individual "just don't use AI for gym tasks" policy will predictably fail without external reinforcement (deadlines, peer comparison pressure — Schneier separately notes students "feel like they'll look bad in comparison if their peers are all using AI"). This maps directly onto team-adoption incentive design: if an org wants engineers to preserve certain skills (e.g., manual debugging, architecture reasoning), leaving it to individual discipline against a backdrop of AI-driven peer productivity pressure is unlikely to work without a structural counter-incentive.

### Claim 11: Schneier prescribes deliberately classifying tasks — including tasks assigned to other people — as work or gym, and withholding AI from gym tasks even when delegating to someone else
- **Evidence**: Schneier's own closing prescription, generalizing from individual practice to task-assignment more broadly.
- **Confidence**: anecdotal
- **Quote**: "We can look at the tasks of our lives and separate them into work or gym... we can wall off our cognitive gym tasks from AI and ensure that we don't lose our skills to this technology. And we can do the same when we assign a job to someone else. If it's a work task, we can have AI do it. If it's a gym task, it's a waste of everyone's time to give it to an AI because no one learns or gets stronger as a result."
- **Our assessment**: The extension to "when we assign a job to someone else" is the most directly transferable line for a team-lead/manager audience — it reframes delegation decisions (not just personal-use decisions) through the same lens, which is squarely in this guide's territory (a senior engineer deciding whether a junior's task should be AI-assisted or done by hand for skill-building purposes).

### Claim 12: Schneier treats the work/gym boundary as provisional and expected to shift as AI capability and the nature of work change, but currently clear enough to act on
- **Evidence**: Schneier's own closing caveat and call to action.
- **Confidence**: anecdotal
- **Quote**: "AI is going to fundamentally change the nature of work. Not nearly as fast as the AI companies want you to believe, but eventually it will... More generally, the line between work and gym will change in the future as we humans adapt ourselves to a world with these new intelligences. But for now, the work vs. gym distinction is pretty clear. Use it on yourself."
- **Our assessment**: A useful hedge against over-applying the framework as a permanent taxonomy — Schneier explicitly signals that what counts as "work" (safe to hand to AI) will expand over time. A guide adopting this framework should present it as a live judgment call to be periodically re-evaluated per task/role, not a fixed checklist.

## Concrete Artifacts

### Daniel Miessler's original "Job vs. Gym" framing (source of Schneier's borrowed heuristic)

```
Source: Daniel Miessler, "Keep the Robots Out of the Gym"
(https://danielmiessler.com/blog/keep-the-robots-out-of-the-gym), published
November 24, 2025. Followed as a substantive linked source per MINER.md §1.

"I think of it as Job vs. Gym. If we're working a manual labor job, it's fine
to have AI lift heavy things for us because the actual goal is to move the
thing, not to lift it. This is the exact opposite of going to the gym, where
the goal is to lift the weight, not to move it. In the first case we just
want the output, and in the second the whole point is to do the work
ourselves."

Miessler's own worked example of which of his tasks are "Gym":
"For me, any sort of: Critical thinking / Problem solving / Creating
arguments for or against a given position / Etc. ...are all Gym tasks.
These are core to how I see myself, and I want to not only maintain my
skills with doing these things, but I want to get better at them over time."

Miessler's practical recommendation:
"Think about who you want to be, as your core identity, in a world where AI
can do most things better than us. Take a look at all the different skills
you want to or need to be good at. Divide those into Job skills and Gym
skills. Take note of when you are having AI do Gym work for you. Either
reduce that work, if possible, or build a system similar to mine in which
you work with your AI to make sure you maintain those muscles. Keep the
robots out of the gym."
```

### Miessler's "Socratic trainer" tutoring system (a concrete workflow artifact, not just an opinion)

```
Source: Daniel Miessler, "Keep the Robots Out of the Gym" (as above)

"I've started building a system into my customized AI stack that functions
not just as a worker, but also as a tutor. This is a work-in-progress that
I am just beginning. Currently this takes the form of a weekly session
where my Digital Assistant, Kai, can look at all the Gym tasks that he
performed for me and can interrogate me on how I think it was done, how I
think the code was generated, what I think the architecture was, why I
think he made those decisions, etc... From there, we can go into an
interactive back-and-forth, getting to first principles all the way down
to code-level specifics or whatever. This is currently done via a Claude
Code skill."
```

Note: Miessler's own example of what "Kai" interrogates him about is explicitly
coding-related ("how I think the code was generated... what I think the
architecture was") — this is the one place in either source where the
work-vs-gym framework is applied directly to software engineering rather than
by analogy, and it is a concrete, implemented Claude Code skill rather than a
proposal.

### Evidentiary backing for "employers are already noticing" (linked, not quoted, by Schneier)

```
Source: Joe Wilkins, "Bosses Horrified as 'AI Native' College Graduates Hit
the Workplace," Futurism (https://futurism.com/future-society/college-critical-thinking-ai),
published May 9, 2026. This is the article Schneier's essay hyperlinks under
the words "already noticing."

"As one New York financier told Financial Times journalist Gillian Tett, new
hires who were seen as 'AI natives' are turning out to have alarmingly
shallow ideas. So much so, the anonymous finance worker admitted, that his
firm now actively avoids seeking out AI-literate STEM graduates, and opts to
comb through humanities students instead. 'We want critical thinking, not
just AI,' the financier told the FT."

"as Cal State Chico ethics professor Troy Jollimore told the New Yorker in
2025, 'massive numbers of students are going to emerge from university with
degrees, and into the workforce, who are essentially illiterate.'"
```

## Cross-References

- **Corroborates**: `research-anthropic-ai-transforming-work.md` Claim 8 (Anthropic
  engineers, in their own interview words, name skill atrophy and a "supervision
  paradox" as a present concern: "When producing output is so easy and fast, it gets
  harder to actually take time to learn something"). Schneier's essay (Claims 5–7 here)
  gives a specific causal mechanism for that same phenomenon in a different domain
  (writing/policy analysis rather than coding) — the mechanism is identical: skipping
  the effortful, uncomfortable part of a task (drafting prose / debugging code by hand)
  is what causes the atrophy, not merely "using AI" in the abstract.
- **Corroborates**: `blog-addyosmani-earning-taste-judgment.md` Claim 11, which cites
  the same Anthropic report's "paradox of supervision" finding ("supervising an agent
  requires exactly the skills that atrophy when you over-rely on the agent"). This
  source's Claim 4 (the "can vs. should" gate — trust the AI's capability before asking
  whether a human should still do it) is a sharper, more general statement of the same
  underlying tension: the skill needed to supervise/verify AI output is exactly the
  skill that erodes when a human stops doing the task by hand.
- **Extends**: `blog-fowler-fragments-2026-07-06.md` Claim 13's own assessment notes
  that Charity Majors' "ethics of working with AI" essay names skill atrophy among the
  concrete harms of AI adoption before arguing for pragmatic engagement over
  renunciation. Schneier's essay is a much more granular, mechanism-level treatment of
  that one named harm — where Majors' piece argues for engagement despite named harms
  in general, Schneier proposes a specific decision procedure (work vs. gym) for
  avoiding this particular harm task-by-task rather than abstaining from AI wholesale.
- **Complicates**: `blog-simonwillison-josh-comeau-course-sales-ai.md` Claim 4, where
  course creator Josh Comeau argues LLMs cannot replace a curated learning path because
  "it can only answer the questions that you know to ask." Miessler's "Socratic
  trainer" artifact (see Concrete Artifacts) is a counter-example in practice — a
  concrete, implemented system where the AI proactively interrogates the human about
  work it already did, rather than only answering the human's self-directed questions.
  This doesn't resolve the tension (Miessler's tutor is self-built and personal, not a
  generally available product like the courses Comeau sells), but it shows the
  "AI can only answer known questions" limitation is not universal — it depends on
  whether the AI system is designed to interrogate, not just respond.
- **Novel**:
  - **The "work vs. gym" heuristic itself** (Claims 1–3): no existing corpus note
    proposes this specific two-branch decision test ("does anyone care how the task was
    done?") for whether to delegate a task to AI. The corpus has extensive coverage of
    *capability* gates (can the AI do this reliably) but this is the first source
    proposing a *should* gate independent of capability.
  - **Writing-labor "work vs. gym" market bifurcation** (Claim 8): parallels but does
    not duplicate the code-economics argument in `blog-simonwillison-charity-majors-code-economics.md`
    — independent convergence on the same structural argument in a different craft,
    which strengthens (via a second independent domain) the corpus's existing
    capital-to-consumable economic framing.
  - **Miessler's implemented "Socratic trainer" Claude Code skill** (Concrete
    Artifacts): a specific, working pattern — an AI system that interrogates its user
    about work it already delegated, as a countermeasure to skill atrophy — not
    documented elsewhere in this corpus. Flagged as a candidate for a dedicated
    Miessler source note if further Miessler material is mined later (Daniel Miessler
    has not previously appeared in this corpus).
  - **Named FT/Futurism anecdote on hiring managers avoiding "AI-native" graduates**
    (Concrete Artifacts): a specific, named, dated data point ("We want critical
    thinking, not just AI") for the employer-side consequence of skill atrophy, not
    previously present in this corpus's skill-atrophy coverage (the Anthropic report
    and Addy Osmani notes document the atrophy from the practitioner's own side, not
    the hiring/employer-reaction side).

## Guide Impact

- **Chapter 00 (Principles)**: Add the "work vs. gym" heuristic (Claims 1–3) as a
  candidate decision framework for *when a human should keep doing a task by hand*,
  distinct from and complementary to this guide's existing capability/verification
  framing. Claim 4's "can vs. should" gate is a clean way to sequence it: first
  establish the AI can do the task reliably (existing guide content), then separately
  ask whether the task is one where the process matters as much as the output (new).
- **Chapter 01 (Daily Workflows)**: Cite Claim 11 (wall off gym tasks even when
  delegating to someone else, human or AI) as guidance for individual contributors and
  tech leads deciding which of their own or a junior's tasks to hand to an agent versus
  do by hand for skill-building. Pair with Claim 10's incentive-problem framing —
  recommend the guide explicitly warn that this discipline will not hold without
  structural reinforcement (time budgets, explicit "hand-coding" assignments), since
  peer/deadline pressure predictably erodes purely voluntary skill-preservation.
- **Chapter 05 (Team Adoption)**: Add Miessler's "Socratic trainer" pattern (Concrete
  Artifacts) as a candidate concrete countermeasure to the skill-atrophy risk already
  documented in this chapter via `research-anthropic-ai-transforming-work.md` Claim 8
  and `blog-addyosmani-earning-taste-judgment.md` Claim 11 — rather than only naming the
  atrophy risk, the guide can point to a working example of an AI system designed to
  interrogate the human about delegated work as a countermeasure, plus the FT/Futurism
  hiring-manager anecdote (Concrete Artifacts) as concrete evidence the risk is already
  visible on the employer side, not just a theoretical future concern.

## Extraction Notes

- The Willison page itself is a single-paragraph excerpt with no added commentary; per
  MINER.md §1's instruction to read the full source and follow substantive linked
  pages, this note extracts primarily from Schneier's full essay (fetched directly via
  `curl` after an initial WebFetch call risked model-summarized, non-verbatim text —
  the raw HTML was parsed locally to guarantee verbatim quotes per MINER.md §2a).
- Two linked sub-pages were followed, both substantive and directly load-bearing for
  claims in this note: Daniel Miessler's original "Job vs. Gym" post (source of the
  borrowed framework, and source of the "Socratic trainer" artifact) and the Futurism
  article backing Schneier's "employers are already noticing" clause. Three other links
  in the Schneier essay were not followed as insufficiently substantive for this guide's
  scope: a link to Schneier's own earlier essay on AI and trust (tangential, cited only
  as a one-word caveat), a link to an Inside Higher Ed piece about a professor
  suspecting AI cheating (anecdotal, cited only in passing), and several links to
  "tells of AI writing" pieces (style-detection content, out of scope for this guide).
- No contradiction was identified between this source and any existing corpus note —
  Schneier's essay corroborates and adds mechanism detail to the corpus's existing
  skill-atrophy concern rather than opposing it. No contradiction issue filed.
- Cross-reference claim numbers verified by re-reading the cited source notes before
  writing this note: `research-anthropic-ai-transforming-work.md` Claim 8 (confirmed at
  its "Claim 8" heading, skill-atrophy interview quote); `blog-addyosmani-earning-taste-judgment.md`
  Claim 11 (confirmed, "paradox of supervision"); `blog-fowler-fragments-2026-07-06.md`
  Claim 13 (confirmed — cited here via its "Our assessment" text, not its direct quote,
  since the direct quote itself is about complicity/engagement rather than skill
  atrophy specifically); `blog-simonwillison-josh-comeau-course-sales-ai.md` Claim 4
  (confirmed, the "can only answer questions you know to ask" limitation).
- The two triage comments on issue #2468 gave differing novelty/chapter assessments
  (medium novelty / Ch00+Ch05 vs. low novelty / Ch00+Ch01+Ch05). This note follows the
  higher-novelty first assessment's chapter scope (Ch00, Ch05) and additionally finds
  concrete Ch01 relevance (Claim 11's delegation-assignment guidance) that neither
  triage comment specifically called out, based on the fuller essay text this
  extraction reads (the triage comments were written against the one-paragraph Willison
  excerpt only, per their own text).
