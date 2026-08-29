---
source_url: https://simonwillison.net/2026/Aug/21/matt-webb/
source_type: blog-post
title: "Quoting Matt Webb"
author: Matt Webb (quoted by Simon Willison); primary source is Webb's own blog, Interconnected
date_published: 2026-08-21
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: anecdotal
issue: "#3017"
---

# Quoting Matt Webb (via Simon Willison, primary source Interconnected)

> Indie iOS developer Matt Webb describes deliberately using ChatGPT as an interactive
> tutor — not a code generator — to finally learn quaternions well enough to fix a
> shipped app's rotation math, after both self-study and asking mathematician friends had
> failed. His stated takeaway, "learning doesn't stop just because I outsource a bunch of
> thinking to AI. It pushes me to learn more," is a first-person counter-anecdote to the
> skill-atrophy concern, offered from someone who also names the opposite failure mode
> (an earlier "fire-and-forget vibing" v1.0 that shipped broken because he never understood
> the math the AI produced).

## Source Context

- **Type**: blog-post (link-blog quotation). Simon Willison's weblog entry is a short
  "quoting" post — Willison's own contribution is a two-paragraph excerpt and tags, with
  no added commentary of his own beyond the quote and attribution. Per MINER.md §1, this
  note follows the linked primary source — Matt Webb's own post "Galactic Compass 2: now
  with new augmented reality mode" on his blog, Interconnected (interconnected.org, dated
  11:44, Friday 21 Aug 2026) — since it contains substantially more relevant context than
  the two paragraphs Willison excerpted.
- **Author credibility**: Matt Webb (a.k.a. "genmon") is an independent developer and
  writer who has run Interconnected since February 2000 (336 consecutive weeks of posting
  per the page's own streak counter) and lists Bluesky/X/Instagram/Mastodon/LinkedIn
  presences and an "Unoffice Hours" consulting practice. He is the sole developer of
  Galactic Compass, an iPhone/Watch app; per his own account it "went kinda viral" in 2024
  and briefly ranked in the App Store's "top free apps" (Travel category). This is a
  first-person account of his own app and his own learning process — high credibility for
  what he personally did and experienced, but it is a single indie developer's anecdote,
  not a study.
- **Scope**: Covers Webb's specific experience building Galactic Compass 2 (an AR/Apple
  Watch update to an existing app): why the original v1.0 broke, why he chose to learn
  quaternions via an AI tutor rather than delegate the fix, and one further engineering
  anecdote (an AI/agent-built custom 3D graphics library for watchOS). Does NOT cover: any
  transcript or detail of the actual ChatGPT tutoring session, how long the learning took,
  what specifically he asked or was taught, or any generalization beyond his own
  experience — this is a single anecdote, not a described method others could replicate
  step-by-step.

## Extracted Claims

### Claim 1: Webb deliberately chose to have ChatGPT teach him the underlying math rather than write the code for him, after a first attempt at pure code delegation had failed
- **Evidence**: Webb's own first-person account of a specific choice made after v1.0 shipped broken.
- **Confidence**: anecdotal
- **Quote**: "After I released version 1.0, I figured I would have to do the rotations myself. So I sat down with ChatGPT and I didn't get it to write the code, but I got it to educate me."
- **Our assessment**: This is a deliberate, named choice between two distinct ways of using an AI assistant on the same problem (generate-the-answer vs. teach-me-the-concept), made by someone who had already tried the generate-the-answer path and watched it fail (Claim 4). It's a single data point, but a clean illustration of choosing the "tutor" mode specifically because the "do it for me" mode had already been tried and hit a wall.

### Claim 2: The AI-tutor approach succeeded where two prior, more traditional learning attempts — reading books and asking mathematician friends — had failed
- **Evidence**: Webb's own comparison of the ChatGPT session's outcome against his stated prior attempts.
- **Confidence**: anecdotal
- **Quote**: "With a patient, interactive tutor, I was able to finally do what I hadn't by reading books and asking mathematician friends – I learnt how to use quaternions just enough to make the app work."
- **Our assessment**: The comparison set (books, expert friends) is notable because both are already considered high-quality, effortful learning methods — Webb isn't claiming AI beat a lazy default, he's claiming it succeeded where deliberate, non-trivial effort using traditional channels had already failed him. "Patient, interactive" is doing real work in his framing: he attributes the success specifically to the tutor's interactivity and patience, not just to having another source of information.

### Claim 3: Webb generalizes from this experience to a broader claim that outsourcing thinking to AI does not stop his learning — it increases it — and that he considers this a positive outcome
- **Evidence**: Webb's own closing generalization, stated as a takeaway rather than confined to the quaternions episode.
- **Confidence**: anecdotal
- **Quote**: "So learning doesn't stop just because I outsource a bunch of thinking to AI. It pushes me to learn more. I like that as an outcome."
- **Our assessment**: This is the claim the Prospector flagged as the key counterpoint to skill-atrophy concerns, and it deserves the "anecdotal" ceiling MINER.md's confidence scale implies: it's one practitioner's generalization from one episode, not a pattern he demonstrates recurring across multiple projects in this post. It is also conditional in a way that's easy to miss if only this sentence is quoted — his own two-thirds-broken-then-fixed app (Claim 4) shows the same practitioner has also personally experienced the failure mode this claim is implicitly arguing against (AI output masking un-learned fundamentals). The claim is best read as "when I deliberately choose to learn rather than delegate, learning increases," not as "using AI generally increases learning regardless of how it's used."

### Claim 4: The app's first shipped version had a working-but-limited-and-eventually-broken rotation implementation because ChatGPT-generated code did not correctly handle the underlying 3D rotation math, and Webb did not understand that math well enough himself to catch or fix it before shipping
- **Evidence**: Webb's own diagnosis of the v1.0 bug and its cause.
- **Confidence**: anecdotal
- **Quote**: "That first version of Galactic Compass didn't work when you lifted your phone higher than about 30 degrees. ChatGPT couldn't get the maths right. And there is a lot of maths: device rotation, world frame rotation, astro… the appropriate way to combine these 3D rotations (and avoid gimbal lock) is a method called \"quaternions\" which - despite my physics background - I have never grasped."
- **Our assessment**: This is the concrete failure that sets up Claims 1–3: a real, shipped, user-facing bug (breaks above ~30° phone tilt) traced directly to the combination of "AI got the math wrong" and "the human reviewing/shipping it didn't understand the math well enough to catch it." It's a specific, falsifiable-in-principle instance of the general worry that AI-generated code can encode incorrect domain logic that passes casual review when the reviewer lacks the domain depth to check it — notable because Webb explicitly says this was true *despite* having a physics background, i.e., domain-adjacent expertise wasn't sufficient here; the specific sub-skill (quaternions) still had to be learned.

### Claim 5: Webb explicitly names his original app-building process as early "vibe coding" — copy-pasting between ChatGPT and Xcode — and attributes much of the app's 2024 popularity to it being an early, novel example of that workflow
- **Evidence**: Webb's own retrospective characterization of how v1.0 was originally built.
- **Confidence**: anecdotal
- **Quote**: "Why so popular? Probably because it was early \"vibe coding\" – I copy-and-pasted between ChatGPT and Xcode to code it, and that was new at the time."
- **Our assessment**: Webb self-identifies the original build as vibe coding (his own scare-quotes), predating the term's mainstream 2025 popularization, which is a useful concrete illustration of what "vibe coding" meant in practice before the term existed: manual copy-paste between a chat model and an IDE, not an agentic/autonomous workflow. Combined with Claim 4, this note documents a single developer's full before/after arc: vibe-coded v1.0 (fast, popular, but silently broken above 30°) → deliberately-understood v2.0 (slower, but the author can now vouch for the rotation math himself).

### Claim 6: For the same app's Apple Watch feature, Webb attributes solving a platform gap (RealityKit, Apple's graphics SDK, has no watchOS support) to an AI/agent building its own 3D graphics library from scratch, and frames this positively as agents' capacity to "grind problems into dust"
- **Evidence**: Webb's own "making of" note about the Apple Watch companion app.
- **Confidence**: anecdotal
- **Quote**: "With the Apple Watch app… RealityKit, Apple's graphics SDK, isn't supported on watchOS. So how does the arrow rotate any which way? The joy of AI and agents that grind problems into dust: Claude Fable built its own 3D graphics library. Astounding."
- **Our assessment**: This is a distinct claim from Claims 1–5 (about learning) — it's a claim about agentic capability, not about learning outcomes. It's a strong, unverified assertion ("built its own 3D graphics library") given with no code, repo link, or detail on scope/quality of that library, and no mention of whether Webb reviewed or understood the resulting graphics code the way he now understands the quaternion math — an interesting tension the post itself doesn't address: the same author who insisted on personally learning the rotation math (Claims 1–4) reports being simply delighted ("Astounding") by an agent solving the watchOS graphics gap, with no stated verification step. Should be cited as an enthusiastic practitioner anecdote about agent capability, not as evidence the resulting library is correct or maintainable.

### Claim 7: Webb explicitly contrasts this project's workflow against pure "fire-and-forget vibing with AI agents," positioning the quaternion-learning episode as the counter-example within his own post
- **Evidence**: Webb's own transitional sentence, placed immediately before the quaternions story.
- **Confidence**: anecdotal
- **Quote**: "It isn't all fire-and-forget vibing with AI agents:"
- **Our assessment**: This is a short but load-bearing line: Webb is aware his post could otherwise read as one more "agents are magic" story (per Claim 6) and explicitly flags that at least one part of the project required him to break from that mode and do the understanding-work himself. It's the clearest textual signal that Webb intends the quaternions anecdote as a deliberate counterpoint to unsupervised agent delegation, not just a side note.

## Concrete Artifacts

```
Source: Matt Webb, "Galactic Compass 2: now with new augmented reality mode,"
interconnected.org, 11:44, Friday 21 Aug 2026
(https://interconnected.org/home/2026/08/21/galactic)

Full quaternions passage (verbatim):

"That first version of Galactic Compass didn't work when you lifted your
phone higher than about 30 degrees. ChatGPT couldn't get the maths right.

And there is a lot of maths: device rotation, world frame rotation,
astro… the appropriate way to combine these 3D rotations (and avoid
gimbal lock) is a method called "quaternions" which - despite my physics
background - I have never grasped.

After I released version 1.0, I figured I would have to do the rotations
myself. So I sat down with ChatGPT and I didn't get it to write the
code, but I got it to educate me. With a patient, interactive tutor, I
was able to finally do what I hadn't by reading books and asking
mathematician friends – I learnt how to use quaternions just enough to
make the app work.

So learning doesn't stop just because I outsource a bunch of thinking to
AI. It pushes me to learn more. I like that as an outcome."

Watch-app graphics passage (verbatim):

"With the Apple Watch app… RealityKit, Apple's graphics SDK, isn't
supported on watchOS. So how does the arrow rotate any which way? The
joy of AI and agents that grind problems into dust: Claude Fable built
its own 3D graphics library. Astounding."
```

## Cross-References

- **Corroborates**: `blog-simonwillison-litt-understand-to-participate.md` Claim 4
  (Geoffrey Litt: active participation in directing an agent's process "is something the
  human can learn to do, not something inherently foreclosed by using an agent") — Webb's
  Claim 3 is a first-person, lived instance of exactly this: choosing to learn rather than
  merely delegate, resulting in deeper understanding rather than less.
- **Corroborates**: `blog-kentbeck-jessicakerr-learning-system.md` Claim 9 (Kent Beck: asking
  an AI assistant a question "in a concrete situation at a time when I care about it,"
  interpreted against the asker's own actual example, accelerates learning versus generic
  research) — Webb's Claim 2 describes the same mechanism from a different practitioner:
  quaternions instruction grounded in his specific app's rotation problem succeeded where
  generic self-study (books) had not.
- **Extends**: `blog-simonwillison-schneier-work-vs-gym.md` Claim 3 (Schneier/Miessler's
  work-vs-gym heuristic: use AI if the task is "work" — only the output matters — avoid AI
  if the task is "gym" — the process itself builds a needed skill). Webb's quaternions
  episode is a "gym" task (he needed the skill of understanding 3D rotation math to ship
  and maintain the app) that he did *not* avoid AI for — he used AI *inside* the gym task,
  in tutor mode, rather than either doing it entirely unaided or having AI do it for him
  (which is "work" mode, and the mode that had already failed him in v1.0, per Claim 4).
  This is a third option the Schneier/Miessler binary doesn't name explicitly: using AI as
  a coach for a gym task, rather than as a substitute for it. Worth citing alongside that
  note as a refinement, not a rebuttal — Schneier's framework is about whether to hand off
  the *outcome*; Webb's tutor-mode use never hands off the outcome (he wrote the
  understanding himself), so it doesn't violate the "gym" prohibition even though AI was
  present throughout.
- **Extends**: `blog-simonwillison-vibe-coding-agentic-engineering.md` (Willison's own
  account of vibe coding and agentic engineering "getting closer than I'd like," and the
  risk of normalized deviance from unreviewed AI code). Webb's Claim 5 (self-naming the
  original v1.0 build as early "vibe coding," copy-paste between ChatGPT and Xcode) and
  Claim 4 (that build shipped a real, user-facing bug the author didn't understand well
  enough to catch) is a concrete, dated (2024) instance of exactly the failure mode
  Willison's note warns about in the abstract — un-reviewed/un-understood AI code shipping
  with a defect that surfaces later. Webb's response (deliberately learning the domain
  before fixing it, rather than re-prompting for another patch) is a specific recovery
  pattern that note does not itself describe.
- **Novel**:
  - **A single practitioner's own before/after arc from vibe-coded-and-broken to
    deliberately-understood-and-fixed, on the same shipped app** (Claims 4–5 together): the
    corpus has abstract warnings about un-reviewed AI code (Willison's vibe-coding note) and
    abstract endorsements of AI-as-tutor (Litt, Beck), but not previously a single source
    documenting one developer living through both halves of that arc on the same codebase.
  - **"Grind problems into dust" as agent-capability framing, paired in the same post with a
    deliberate refusal to let AI grind through the quaternions problem** (Claims 6–7): a
    specific, self-aware juxtaposition — the same author enthusiastic about full agent
    delegation for one subsystem (watchOS graphics) and deliberately avoiding it for another
    (rotation math) — that models a practitioner actively choosing *when* to delegate versus
    learn, rather than applying one policy uniformly across a project.

- **Contradicts**: None filed. Claim 6 (unverified "Claude Fable built its own 3D graphics
  library," accepted with apparent enthusiasm and no stated review step) sits in tension
  with Claim 4's lesson (unreviewed AI output shipped a real bug) within this same source,
  but this is an internal inconsistency in one author's stated practice, not a factual
  disagreement between sources, so it does not meet the MINER.md §4a bar for a contradiction
  issue — it's flagged in Claim 6's assessment instead.

## Guide Impact

- **Chapter 03 (Learning & Skill Development)**: Add Claim 1–3 as a named, first-person
  counter-anecdote to skill-atrophy concerns, but pair it explicitly with the conditioning
  variable this same source demonstrates: the benefit shows up when the developer
  *chooses* tutor-mode use for a task they need to personally understand (Claim 1), not
  merely from AI being present in the workflow. Cite alongside
  `blog-simonwillison-schneier-work-vs-gym.md` (the work/gym heuristic) as a concrete
  example of applying that heuristic's "gym" case with AI-as-coach rather than AI-as-doer.
- **Chapter 02 (Developer Productivity / Harness Engineering) or Ch01 (Daily Workflows)**:
  Add Claim 4 as a concrete, named example of an AI-code-review-gap failure: a shipped bug
  traceable to incorrect AI-generated math that the reviewing developer's own domain
  knowledge wasn't sufficient to catch, notable because the developer had a *related* but
  not *sufficient* background (physics, not specifically quaternions). Useful as a caution
  against assuming general domain adjacency is enough to safely review AI output in a
  specific sub-domain.
- **Chapter 02 or Chapter 06 (Practices & Guardrails)**: Claim 6 is worth citing only with
  its caveat attached (Our assessment) if the guide discusses agents solving infra/platform
  gaps — it's an enthusiastic, unverified claim, not a documented technical pattern; do not
  cite "built its own 3D graphics library" as a validated technique without flagging the
  absence of any stated review or quality check, especially juxtaposed against Claim 4 in
  the same source.

## Extraction Notes

- Willison's own weblog entry is a short quotation post (his contribution: a dated post,
  the excerpted two paragraphs, and tags — no original Willison commentary). Per MINER.md
  §1, the linked primary source (Matt Webb's full Interconnected post) was fetched and read
  in full, since it contains the app backstory, the v1.0 failure mode, the "vibe coding"
  self-naming, and the Apple Watch/agent anecdote — none of which appear in Willison's
  excerpt. All quotes above were copied verbatim from the raw HTML of both pages (tags
  stripped, HTML entities decoded) rather than from an AI-generated summary, per MINER.md
  §2a; an initial WebFetch-tool pass over the Willison URL returned a paraphrased,
  truncated summary (including a fabricated-sounding "truncated to 125 characters" partial
  quote) and was discarded in favor of a direct raw-HTML fetch of both the Willison and
  Webb pages.
- The Interconnected post also covers non-AI-related product details (App Store category
  history, a drag-to-reposition AR interaction, a Liquid Glass visual refresh, reader emails
  about the app's emotional resonance) that were read but not extracted as claims — they are
  not about AI-native engineering practice.
- Overall confidence is rated `anecdotal`: every claim is a single indie developer's
  first-person account of one project, with no data, no described method beyond "I sat down
  with ChatGPT," and no claim of generalizability beyond his own experience.
- Cross-reference claims were verified by re-reading each cited note's actual numbered
  claims before writing: `blog-simonwillison-litt-understand-to-participate.md` Claim 4,
  `blog-kentbeck-jessicakerr-learning-system.md` Claim 9,
  `blog-simonwillison-schneier-work-vs-gym.md` Claim 3, and
  `blog-simonwillison-vibe-coding-agentic-engineering.md` (cited by topic/theme rather than
  claim number, per MINER.md §4a, since the specific point extended is that note's overall
  thesis rather than one numbered claim).
