---
source_url: https://simonwillison.net/2026/Jun/24/tom-macwright/
source_type: blog-post
title: "A quote from Tom MacWright"
author: Tom MacWright (quoted by Simon Willison)
date_published: 2026-06-24
date_extracted: 2026-06-30
last_checked: 2026-06-30
status: current
confidence_overall: anecdotal
issue: "#1353"
---

# A Quote from Tom MacWright — Accidental Anonymity

> Tom MacWright (quoted by Simon Willison) identifies a new pattern in hiring: LLM-generated
> application chains — resume, portfolio, GitHub projects, commit messages — that create
> "accidental anonymity," leaving hiring managers with no way to know anything about the
> candidate as a person.

## Source Context

- **Type**: blog-post (Simon Willison link-blog entry, June 24, 2026; the entry consists
  solely of a blockquote from Tom MacWright's article "Accidental anonymity" published at
  https://macwright.com/2026/06/24/accidental-anonymity.html with no additional Willison
  commentary. Per MINER.md §1, the MacWright article was read as the primary substantive
  linked page. Tags on the Willison post: careers, ai, tom-macwright, ai-misuse.)
- **Author credibility**: Tom MacWright is a software developer, writer, and musician who
  reviews job applications professionally. He states 12 years of experience reviewing
  applications. He is known in the developer community for Observable, Mapbox contributions,
  and independent writing. Simon Willison is the creator of Django and one of the highest-
  signal independent AI tooling commentators; his selection of this piece for his curated
  feed is itself a relevance signal. MacWright notes he uses LLM tools himself: "I'm no
  purist - I use the tools and cannot deny that they're useful and powerful."
- **Scope**: The accessible content covers: (1) MacWright's observation as a hiring manager
  of the LLM-generated application chain; (2) the emotional and evaluative consequences for
  the hiring manager; (3) the argument that authentic self-presentation requires bravery;
  (4) the purpose of portfolios and resumes beyond credentials; (5) the parallel pattern in
  cold-outreach emails; (6) MacWright's prior writing connecting art appreciation to knowing
  the artist. Does NOT cover: metrics on how common this pattern is, how to detect LLM
  generation reliably, technical mitigations for hiring processes, or the candidate's
  perspective and motivations.

## Extracted Claims

### Claim 1: A full-stack LLM application chain — LLM-cowritten resume, LLM-generated portfolio site, LLM-generated GitHub projects, and LLM-generated commit messages — is now observable to experienced hiring managers

- **Evidence**: MacWright's direct first-person observation from 12 years of reviewing job
  applications. He identifies the specific pattern: each artifact in the chain is
  LLM-generated, forming a coherent but inauthentic application package.
- **Confidence**: anecdotal (single practitioner self-report from an experienced hiring
  manager; no count of how common this is, but MacWright frames it as a recently-emerged
  pattern: "In the last few months, I've started to see...")
- **Quote** (from Willison's page blockquote, verified verbatim): "In the last few months,
  I've started to see [job applications] that were clearly cowritten by an LLM, link to an
  LLM-generated portfolio site, which then links to LLM-generated GitHub projects, with
  purely LLM-generated commit messages."
- **Our assessment**: The "chain" observation is the critical new element. Prior corpus
  sources (Willison's May 6 post) identified that a single GitHub repository can be
  generated in 30 minutes, breaking one quality signal. MacWright identifies that the
  entire application package — every artifact — can now be generated, which breaks the
  redundant-signal strategy: an evaluator who suspects the readme might check the commit
  history; if both are generated, there is no independent signal to fall back on. The
  full-stack generation pattern is what creates the "accidental anonymity" described in
  subsequent claims.

### Claim 2: LLM-generated application materials create "accidental anonymity" — the hiring manager cannot know anything about the applicant as a person

- **Evidence**: MacWright's direct first-person reaction as a hiring manager, stated
  explicitly as a consequence of observing the LLM-generated chain. This is the central
  claim of the piece, and the key phrase is "I don't know anything about these people" —
  not "I dislike these materials" but a specific epistemic failure: the materials provide
  no information about the person.
- **Confidence**: anecdotal (personal observation; but MacWright's 12-year hiring
  experience makes this more than casual impression)
- **Quote** (from Willison's page blockquote, verified verbatim): "My other reaction is
  that _I don't know anything about these people_. They haven't put themselves out there.
  They haven't said anything true."
- **Our assessment**: The phrase "haven't said anything true" is strong and precise. It
  is not "haven't said anything good" or "haven't said anything impressive" — it is "true."
  MacWright is identifying that LLM-generated materials, however polished, are not
  expressions of the candidate's actual perspectives, choices, or work. They are accurate
  in a narrow sense (the resume lists real credentials) but false in the sense that the
  presentation style, the framing, and the portfolio are generated rather than chosen.
  The "accidental" in "accidental anonymity" is important: candidates who generate their
  materials may not realize they are making themselves invisible; the anonymity is a
  consequence they did not intend.

### Claim 3: The purpose of portfolios and resumes is not just credentials — it is to signal authentic human characteristics, and LLM generation eliminates this signal

- **Evidence**: MacWright's explicit argument about what portfolios are for, contrasted
  with what LLM-generated materials produce. He frames this as a social function, not an
  evaluative one: the portfolio reveals "which kind of person will be sitting next to you."
- **Confidence**: anecdotal (MacWright's view of the hiring manager's goal; coherent and
  internally consistent, but one practitioner's framing of a complex social process)
- **Quote** (from MacWright's article at macwright.com/2026/06/24/accidental-anonymity.html,
  read as a linked page): "the point of resumes and portfolios is not just to list
  credentials, it's to give some hint as to which kind of person will be sitting next to
  you, to be inspired by their arc or their _human characteristics and capabilities_. Are
  they determined? Did they start off building silly stuff in neopets and work their way up
  to programming, or create some project based on their personal interests?"
- **Our assessment**: This is a direct statement of what the evaluative function of a
  portfolio is: not skills inventory, but person-revelation. The questions MacWright asks
  ("Are they determined? Did they start off building silly stuff...") are unanswerable from
  LLM-generated materials. A generated portfolio might exhibit all the surface signals of
  determination (many commits, diverse projects, good documentation) while revealing
  nothing about whether the person actually is determined or merely instructed a model to
  appear so. This is the functional claim underlying the "accidental anonymity" observation.

### Claim 4: The LLM-generated portfolio produces a specific epistemic failure — the evaluator cannot see inputs, process, or struggle, only polished outputs

- **Evidence**: MacWright's explicit statement of what is missing from LLM-generated
  materials, stated as a direct consequence of the generation process.
- **Confidence**: anecdotal (MacWright's observation; but the mechanism is transparently
  correct — LLM generation hides the prompt-and-iterate process that a human creative
  process would make visible)
- **Quote** (from Willison's page blockquote, verified verbatim): "The perfected, generated,
  prompted resume is generic and impersonal. It tells me nothing about this person, other
  than that they use particular tools."
- **Quote** (from MacWright's article): "I can't see the inputs to their outputs, see what
  they typed, or the process of building."
- **Our assessment**: The pair of observations is precise. "Generic and impersonal" names
  the observable surface property (the output is indistinguishable from any other
  LLM-generated output). "I can't see the inputs to their outputs" names the epistemic
  mechanism: the process has been hidden. A hand-built portfolio reveals choices — which
  projects to include, how to describe them, what to emphasize — that reflect the person's
  judgment. A generated portfolio hides all those choices behind the model's defaults.
  The phrase "other than that they use particular tools" is the ironic remainder: the only
  signal the LLM-generated application provides is tool selection — which is itself a
  thin signal compared to the portfolio it replaces.

### Claim 5: LLM-generated cold-outreach emails follow a recognizable formula and fail to create human connection

- **Evidence**: MacWright's direct observation of a pattern in incoming emails, with the
  formula explicitly identified. He notes he is not alone in observing this pattern
  (referring to "Robin and Nolen" as having written about similar experiences).
- **Confidence**: anecdotal (personal observation; but the pattern is observable to anyone
  who receives developer outreach)
- **Quote** (from MacWright's article): "Like Robin, I have been getting a lot of incoming
  emails that follow an LLM-like formula of `observation about me and how it could be
  relevant to some product` + `ask that i try the product`. A lot of these seem
  LLM-generated."
- **Quote** (from MacWright's article): "The email about why I'm the right person to try
  your side project says nothing about you. I don't know why you made it, who you are.
  I don't know your writing style. I don't have any way to connect to you as a person,
  and no reason to care."
- **Our assessment**: The formula MacWright identifies — personalized observation + product
  ask — is the LLM-generation pattern for cold outreach. It is distinguishable from
  authentic email because the "personalization" is generated (observation-about-me drawn
  from public profile data) rather than genuine (something that actually prompted the
  sender to reach out). The consequence MacWright names is practical: no way to connect
  as a person, no reason to care. This is the outreach-marketing parallel to the hiring
  observation: LLM generation of professional communication reduces rather than enhances
  the effectiveness of that communication.

### Claim 6: Authentic self-presentation requires bravery — putting imperfect work out for judgment is an act of courage, and LLM generation allows avoidance of this act at the cost of being unknowable

- **Evidence**: MacWright's personal account of 15 years of publishing work online, used
  to ground his assertion that authentic expression is a character challenge, not a skill
  one. He is explicit that this is his "personal prejudice" — a long-held view, not a
  conclusion from the LLM era alone.
- **Confidence**: anecdotal (personal view; but coherent with the "accidental anonymity"
  mechanism and with a long tradition of discourse about artistic authenticity)
- **Quote** (from MacWright's article): "putting your art, writing, expression out to be
  judged by others is an act of bravery as much as talent, and a lot of people lack
  bravery. Sorry to say it but if you need your work to be polished and beyond reproach,
  that's a determination and character problem, not a skill problem."
- **Quote** (from MacWright's article): "The fear is being found out for being imperfect.
  The fear is also for being _known_ in general..."
- **Our assessment**: This is the mechanism MacWright proposes for why people generate
  rather than express: not inability to write their own materials, but fear. The fear
  operates at two levels: fear of imperfection (judgment about quality) and fear of being
  known (judgment about identity). LLM generation resolves both fears simultaneously —
  the output is polished (no imperfection) and generic (no identity). But as MacWright
  argues, the resolution of both fears by hiding behind a machine produces the worst
  outcome for the person's actual goals: "the person who puts nothing out for judgment
  just isn't known at all." This is the "accidental" quality of the anonymity — it is the
  unintended consequence of avoiding risk.

### Claim 7: Human connection to professional work requires knowing something about who made it — the relationship between work and person is social, not purely evaluative

- **Evidence**: MacWright's prior writing on art appreciation, quoted directly. He extends
  the argument about art and audiences to the hiring context: the same social dynamic
  applies to evaluating developers as people, not just their output.
- **Confidence**: anecdotal (philosophical/aesthetic claim from MacWright's writing; not
  specific to the LLM era, but applied to it)
- **Quote** (MacWright quoting his own prior writing, from MacWright's article):
  "People capable of liking some paintings or prints or whatever can rarely do so without
  knowing something about the artist. Again, the situation is social rather than scientific.
  Any work of art is half of a conversation between two human beings, and it helps a lot
  to know who is talking at you."
- **Our assessment**: This is the philosophical grounding for the "accidental anonymity"
  claim. If work is inherently a conversation between maker and audience, then work that
  reveals nothing about the maker fails as communication regardless of its surface quality.
  The "social rather than scientific" framing is precise: portfolio evaluation is not an
  objective technical assessment (can this code run?) but a social assessment (can I work
  with this person?). The social assessment requires social signal — who is this person,
  what do they care about, how do they think? LLM-generated materials strip all social
  signal while preserving surface technical correctness.

### Claim 8: The countermeasure is explicit — show process, struggle, and imperfection rather than polish

- **Evidence**: MacWright's direct prescriptive statement, the closing line of the article.
  It is not advice about what tools to use or avoid, but about what to reveal.
- **Confidence**: anecdotal (single practitioner recommendation; but logically follows
  from the epistemic failure mechanism identified in Claims 2-4)
- **Quote** (from MacWright's article): "if you want people to connect with you as a
  person, you can't hide behind a machine. Publish your typos and show your struggle
  getting going. Be a human."
- **Our assessment**: "Publish your typos" is a precise inversion of the LLM-generated
  portfolio's properties. A generated portfolio is polished and typo-free; authentic work
  has typos. A generated commit history is coherent and tidy; a genuine developer's
  journey has messy starts and pivots. The advice is to make authenticity signals visible
  — not because typos are good, but because the things you can't fake (struggle, process,
  a specific human trajectory) are now the primary signals in a world where everything
  fakeable has been faked.

## Concrete Artifacts

### The Willison Page Blockquote (verbatim from simonwillison.net)

```
Source: Simon Willison, https://simonwillison.net/2026/Jun/24/tom-macwright/
Published: 24th June 2026 at 6:13 pm
(Quoting Tom MacWright, https://macwright.com/2026/06/24/accidental-anonymity.html)

Tags: careers, ai, tom-macwright, ai-misuse

[Full blockquote as it appears on Willison's page:]

"In the last few months, I've started to see [job applications] that were
clearly cowritten by an LLM, link to an LLM-generated portfolio site, which
then links to LLM-generated GitHub projects, with purely LLM-generated commit
messages. [...] My other reaction is that _I don't know anything about these
people_. They haven't put themselves out there. They haven't said anything true.
[...] The perfected, generated, prompted resume is generic and impersonal. It
tells me nothing about this person, other than that they use particular tools."

Note: The brackets "[job applications]" and "[...]" appear to be Willison's
editorial condensation of MacWright's multi-paragraph original.
```

### The LLM Cold-Outreach Formula (from MacWright's article)

```
Source: Tom MacWright, https://macwright.com/2026/06/24/accidental-anonymity.html
Published: June 2026

LLM cold-outreach email formula observed by MacWright:
  Component 1: "observation about me and how it could be relevant to some product"
  Component 2: "ask that i try the product"

Distinguishing feature: The "personalization" is generated from public profile data,
not from genuine interest or connection.

Consequence: "I don't know why you made it, who you are. I don't know your writing
style. I don't have any way to connect to you as a person, and no reason to care."
```

### MacWright's Purpose-of-Portfolios Statement (from MacWright's article)

```
Source: Tom MacWright, https://macwright.com/2026/06/24/accidental-anonymity.html
Published: June 2026

"the point of resumes and portfolios is not just to list credentials, it's to
give some hint as to which kind of person will be sitting next to you, to be
inspired by their arc or their _human characteristics and capabilities_. Are
they determined? Did they start off building silly stuff in neopets and work
their way up to programming, or create some project based on their personal
interests?"

Contrast: "The perfected, generated, prompted resume is generic and impersonal.
It tells me nothing about this person, other than that they use particular tools.
I can't see the inputs to their outputs, see what they typed, or the process of
building."
```

### The Art-and-Audience Argument (from MacWright's article)

```
Source: Tom MacWright, https://macwright.com/2026/06/24/accidental-anonymity.html
Published: June 2026
(MacWright quoting his own prior writing on art and humanness)

"People capable of liking some paintings or prints or whatever can rarely do
so without knowing something about the artist. Again, the situation is social
rather than scientific. Any work of art is half of a conversation between two
human beings, and it helps a lot to know who is talking at you. Does he or she
have a reputation for seriousness, for religiosity, for suffering, for
concupiscence, for rebellion, for sincerity, for jokes?"

Application to hiring context (MacWright's framing):
The same social dynamic applies to portfolio evaluation: evaluating a developer
is a social act, not a technical one. The question "which kind of person will
be sitting next to you" requires social signal — and LLM generation removes it.
```

## Cross-References

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 4
  ("Traditional software quality markers — commit history, test suites, documentation —
  are no longer reliable signals because they can be generated in 30 minutes"): Willison's
  May 6 observation that a GitHub repository with 100 commits, a good readme, and automated
  tests used to signal care and investment — but no longer does — is the software-quality
  analog of MacWright's hiring-evaluation claim. Willison identified the signal breakdown
  for OSS evaluation; MacWright identifies the same breakdown for career/hiring evaluation.
  The two claims are independent observations (different contexts, different authors,
  different evaluation goals) that converge on the same mechanism: AI generation has made
  previously-expensive-to-fake artifacts cheap to produce.

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 5
  ("Evidence of actual sustained use is now the primary quality signal for software,
  replacing artifact inspection"): Willison's replacement heuristic (use-evidence over
  artifact inspection) maps directly to MacWright's implicit countermeasure. The analog of
  "used every day for two weeks" in the hiring context is what MacWright advises: visible
  struggle, process, and trajectory — evidence of actual investment that cannot be generated
  as an artifact. Both sources converge on the same structural observation: in a world where
  artifacts are generated, evidence of genuine process and use becomes the primary signal.

- **Extends**: `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 11
  ("Aggregate software labor demand will likely remain healthy but individual engineers may
  still face rocky career paths as roles and expectations shift"): Narayanan/Kapoor
  predict individual-career disruption even with stable aggregate demand. MacWright
  provides a concrete mechanism for one form of that individual disruption: candidates
  who over-rely on LLM generation for job materials become invisible to hiring managers,
  not because their skills are worse but because they cannot be known as people. This is
  a disadvantage in a hiring process that is inherently social (Claim 7). The
  Narayanan/Kapoor essay promised a follow-on about individual-career disruption;
  MacWright's observation documents one instance of it already occurring.

- **Extends**: `discussion-hn-agentic-coding-jobs.md` Claim 1 (Zapier job posting
  explicitly requiring "directing and reviewing agent-written code" as core workflow):
  The Zapier posting shows employer expectations shifting — candidates must demonstrate
  agentic engineering competency. MacWright adds the complementary hiring-evaluation
  signal: candidates who generate all their portfolio materials demonstrate only
  "that they use particular tools" and no authentic agentic engineering perspective.
  A candidate who genuinely directs agents to produce meaningful work will have a
  different kind of portfolio than one who generates generic materials — but this
  distinction may not be visible from the generated artifacts themselves, creating a
  new evaluation challenge for employers who value genuine agentic competency.

- **Novel** (not present in any existing corpus note):
  - **The full-stack LLM application chain** (resume → portfolio site → GitHub projects
    → commit messages): No existing corpus note identifies this as an observable pattern.
    Prior sources (Willison May 6) noted individual artifacts can be generated; MacWright
    is the first to describe the complete application package as a coherent generated chain.
  - **"Accidental anonymity" as the hiring consequence**: The framing that LLM generation
    makes candidates invisible (rather than merely inauthentic or detectable) is entirely
    new to the corpus. Existing notes focus on quality signal breakdown from the evaluator's
    technical perspective; MacWright frames it from the human-connection perspective.
  - **The hiring manager's 12-year experienced perspective** observing this as a newly-
    emerged pattern: No corpus note provides a hiring manager's first-person reaction to
    LLM-generated application materials.
  - **The "social rather than scientific" portfolio evaluation frame**: MacWright's
    characterization of portfolio evaluation as a social act — who will be sitting next to
    me — is not present in any existing note. This reframes the quality-signal-breakdown
    problem: it is not only that technical quality signals have been faked, but that the
    social/human signal (the primary function) has been eliminated.
  - **The bravery argument**: The claim that authentic self-presentation requires courage
    and that LLM generation allows avoidance of this courage at the cost of being unknowable
    is entirely new to the corpus. No existing note addresses the psychology of LLM
    generation from the candidate's perspective.
  - **The LLM cold-outreach formula**: The observable formula `observation + ask` is
    documented nowhere else in the corpus. This is a concrete, reproducible pattern that
    practitioners can use to identify LLM-generated professional communication.

- **Contradicts**: None found. No existing corpus note makes claims about hiring/portfolio
  evaluation in the AI era that would contradict MacWright's observations. The signal-
  breakdown finding corroborates rather than contradicts Willison's May 6 claims.

## Guide Impact

- **Chapter 05 (Team Adoption — Hiring in the AI-Native Era)**: This is the most novel
  addition this source makes to the guide. The corpus currently contains no guidance on
  how to evaluate candidates in an era when every traditional portfolio signal can be
  generated. MacWright's source suggests specific guidance: (1) weight evidence of genuine
  process (documented learning trajectory, personal projects with clear personal motivation,
  visible iteration and imperfection) over artifact quality (polished readme, commit count,
  test coverage); (2) use interview techniques that reveal how the candidate thinks and
  what they care about, rather than what they have produced; (3) ask explicitly about the
  candidate's own role in AI-assisted work. The "which kind of person will be sitting next
  to you" framing should anchor any guide section on AI-era hiring practices.

- **Chapter 00 (Principles — Authenticity Cost of Over-Reliance on AI)**: MacWright's
  "accidental anonymity" concept and the "haven't said anything true" claim are principle-
  level observations. They establish that over-reliance on AI for professional communication
  and self-presentation has a cost that is not primarily about quality or detectability —
  it is about the elimination of authentic self. The guide's principles section should name
  this dynamic explicitly: generating all your professional materials with LLMs removes the
  signal by which others evaluate you as a person, not just as a producer of artifacts.
  This extends the principle beyond code quality to encompass the broader practice of
  AI-native professional communication.

- **Chapter 05 (Team Adoption — Professional Communication in the AI Era)**: The cold-
  outreach formula observation has practical team implications. Teams reaching out to
  potential collaborators, customers, or hires via AI-generated email face the same
  "accidental anonymity" problem MacWright names: the recipient has no reason to care
  and no way to connect. The guide could advise teams on when AI assistance in
  communication helps (drafting, editing, refining) vs. when it hinders (replacing the
  genuine human voice and perspective that makes communication land).

## Extraction Notes

- **Two-layer source**: The Willison page (the issue URL) consists entirely of a blockquote
  from MacWright's article with no additional Willison commentary. Per MINER.md §1,
  MacWright's article at https://macwright.com/2026/06/24/accidental-anonymity.html was
  read as the primary substantive linked page; all substantive claims and quotes are
  attributed to MacWright throughout this note. The Willison page's blockquote appears to
  be an editorial condensation of MacWright's paragraphs 3, 5, and 9 (with "[job
  applications]" and "[...]" indicating Willison's editing).
- **Quote attribution**: Quotes marked "(from Willison's page blockquote, verified verbatim)"
  were verified against the Willison page via WebFetch. Quotes marked "(from MacWright's
  article)" were extracted from the MacWright article read as a linked page per MINER.md §1.
- **Cross-reference verification**: Both cited claim numbers from `blog-simonwillison-vibe-
  coding-agentic-engineering.md` were verified by re-reading that note: Claim 4 (lines
  106–123, "Traditional software quality markers are no longer reliable signals") and
  Claim 5 (lines 124–140, "Evidence of actual sustained use is now the primary quality
  signal") — both verified. Claim 11 from `blog-simonwillison-why-ai-hasnt-replaced-
  engineers.md` (lines 247–265, "Aggregate labor demand strong but individual careers may
  be rocky") — verified. Claim 1 from `discussion-hn-agentic-coding-jobs.md` (the Zapier
  posting) was verified as the first claim in that note.
- **Confidence rated anecdotal**: MacWright is a single practitioner reporting personal
  experience. No count of how common the LLM-chain pattern is, no survey data, no
  controlled study. The credibility comes from his 12 years of hiring experience and
  Willison's selection for the curated feed, not from empirical measurement.
- **"Nolen and Robin" references**: MacWright references two other writers who have
  addressed similar observations ("Nolen and Robin and Robin again have written other,
  maybe better versions of it"). These secondary sources were not followed — they are
  mentioned as corroboration that the observation is independently made by others, which
  modestly increases confidence beyond a purely isolated report.
