---
source_url: https://openai.com/index/learn-teach-chatgpt-work-codex
source_type: blog-post
title: "New ways to learn and teach with ChatGPT Work and Codex"
author: OpenAI
date_published: 2026-08-04
date_extracted: 2026-08-13
last_checked: 2026-08-13
status: current
confidence_overall: emerging
issue: "#2672"
---

# New ways to learn and teach with ChatGPT Work and Codex

> OpenAI announces three role-specific education "plugins" for ChatGPT Work and
> Codex (K–12 educator, college educator, college student), shipped through
> ChatGPT Edu and ChatGPT for Teachers, alongside a "capability overhang"
> usage-gap statistic for college-age users and a slate of partner/training
> initiatives (AFT's National Academy for AI Instruction, OpenAI Student
> Collective, OpenAI Academy K–12 workshops, an Estonia deployment, and a
> ChatGPT for Academic Researchers program).

## Source Context

- **Type**: blog-post (OpenAI `openai.com/index/` announcement page, published
  August 4, 2026, auto-discovered via the `openai-news` trusted feed; a
  back-to-school product-and-partnerships post, not a technical deep dive).
- **Author credibility**: House-authored OpenAI announcement, no named
  individual author — same genre as other `openai.com/index/` launch posts
  already in the corpus (e.g. `blog-openai-chatgpt-work-ambitious-partner.md`,
  `blog-openai-academy-training-courses.md`). All usage statistics
  (weekly-user counts, the "capability overhang" percentage, educator/student
  counts) are OpenAI's own self-reported figures with no disclosed methodology
  or independent audit — standard vendor-announcement credibility caveats
  apply throughout.
- **Scope**: Covers three new ChatGPT Work/Codex education plugins (K–12
  educator, college educator, college student), the "capability overhang"
  framing for college-age ChatGPT usage, ChatGPT Edu/ChatGPT for Teachers
  program context, the AFT-partnered National Academy for AI Instruction, the
  OpenAI Student Collective, OpenAI Academy K–12 workshops (with the Walton
  Family Foundation), an Estonia deployment example, and the ChatGPT for
  Academic Researchers program. Does NOT cover: any task-success or
  learning-outcome data for the plugins themselves (they are announced, not
  evaluated), pricing/availability dates beyond "available through ChatGPT Edu
  and ChatGPT for Teachers district deployments," or a technical description
  of how a "plugin" is packaged/built (no architecture, manifest format, or
  code shown).

## Extracted Claims

### Claim 1: OpenAI is introducing three new education plugins for ChatGPT Work and Codex — one for college students, one for K–12 educators, one for college educators — available through both ChatGPT Edu and ChatGPT for Teachers district deployments, where a "plugin" is defined as a package of apps, role-specific skills, instructions, and common workflows that lets users start immediately without constructing complex prompts
- **Evidence**: Direct product-announcement statement in the post's opening framing.
- **Confidence**: settled (an unambiguous, dated feature-launch and availability-channel statement from the vendor itself)
- **Quote**: "As students and educators return to classrooms and campuses this fall, we're introducing three new education plugins for ChatGPT Work and Codex, specifically designed to help students and educators leverage agentic capabilities using the course materials and context they choose. A plugin is a package of apps, role-specific skills, instructions, and common workflows that helps students and educators get started immediately without having to construct complex prompts on their own."
- **Our assessment**: This is the post's core announcement and gives the corpus its first explicit OpenAI definition of "plugin" as a packaging concept (apps + role-specific skills + instructions + common workflows). Notably, this Aug 4, 2026 post never mentions "Agent Plugins 1.0," the cross-vendor open plugin standard OpenAI co-published two days later on Aug 6, 2026 (`docs-github-copilot-agent-plugins-1-0.md` Claim 1) — see Cross-References for why this naming overlap is flagged, not treated as confirmed technical overlap.

### Claim 2: The K–12 Educator plugin helps teachers create differentiated resources, design interactive visuals, and surface actionable classroom insights, and integrates with Learning Commons (a philanthropic organization funding public AI learning-science datasets) so teachers can align materials to local academic standards and learning progressions while retaining control over pedagogical decisions, grading, and agentic actions
- **Evidence**: Direct feature description in the "Helping students and educators do more with AI" section.
- **Confidence**: emerging (a specific, named integration and named third-party partner, but no usage data since the plugin is newly announced)
- **Quote**: "The K–12 Educator plugin is designed to help teachers plan and create for their classrooms. Developed alongside K–12 educators, it can work with the materials and tools teachers already use to create differentiated resources, design interactive visuals, and surface actionable insights. It also integrates with Learning Commons, a philanthropic organization that funds and builds public AI datasets and resources to help bring more learning science into classrooms, which allows teachers to create materials aligned to local academic standards, the granular learning components beneath them, and the progressions that connect prior and future learning, while remaining in control of pedagogical decisions, grading, and agentic actions."
- **Our assessment**: The "teacher remains in control of pedagogical decisions, grading, and agentic actions" line is a specific human-in-the-loop scoping claim — worth flagging as a named guardrail pattern (agent explicitly excluded from grading authority) rather than a generic "responsible AI" statement.

### Claim 3: The College Educator plugin supports course design, syllabus updates, creation of interactive websites or multimedia assessments, adapting materials for diverse learners, and packaging content for an LMS, with connected calendars and documents letting instructors work across teaching, research, and other tasks without recreating context each time
- **Evidence**: Direct feature description in the "Helping students and educators do more with AI" section.
- **Confidence**: emerging (specific named capabilities, no usage data)
- **Quote**: "The College Educator plugin enables course design, teaching, and academic planning. Faculty can update syllabi, create interactive websites or multimedia assessments, adapt materials for diverse learners, or package content for their LMS. With connected calendars, documents, and other approved tools, instructors can also work across teaching, research, and everyday tasks without having to recreate the context for each new project."
- **Our assessment**: "Without having to recreate the context for each new project" is the same persistent-context value proposition already documented for ChatGPT Work generally (`blog-openai-chatgpt-work-ambitious-partner.md` Claim 1) and for Nathan's ChatGPT Work harness account (`blog-latentspace-nathan-chatgpt-work-harness.md` Claim 9, shared memory across conversations) — this plugin is that same persistent-context mechanism scoped to a faculty role.

### Claim 4: The College Student plugin helps students turn what they're studying into personalized learning experiences via a guided tutor, concept practice, and study guides/quizzes/flashcards/interactive visual explanations built from sources the student selects, designed with university students across majors, geographies, and AI-fluency levels, drawing on learning science to prioritize deeper understanding over answer-shortcutting
- **Evidence**: Direct feature description in the "Helping students and educators do more with AI" section.
- **Confidence**: emerging (specific named capabilities and design process claim, no usage data)
- **Quote**: "The College Student plugin helps students turn what they are already studying into more personalized learning experiences. Students can work with a guided tutor, practice difficult concepts, and create study guides, quizzes, flashcards, and interactive visual explanations from the sources they choose. Designed with university students across majors, geographies, and levels of AI fluency, the plugin draws on learning science to prioritize deeper understanding and build stronger study habits."
- **Our assessment**: Directly reinforces the post's own stated guiding principle (see Claim 5) that AI should support rather than shortcut learning — this plugin's design (tutor + practice + student-selected sources, not answer-generation) is the concrete mechanism OpenAI offers as evidence for that principle, though no independent measure of whether it actually deepens understanding versus a plain ChatGPT session is given.

### Claim 5: OpenAI states its guiding education principle as "AI should support learning, not shortcut it, and the best learning experiences keep educators and students in control"
- **Evidence**: Direct statement of organizational principle, presented as the basis ("This builds on the principle that guides our work in education...") for the plugin launch.
- **Confidence**: settled (an unambiguous, directly quoted statement of stated policy/principle — though as a principle, not independently verifiable as *practiced*)
- **Quote**: "This builds on the principle that guides our work in education: AI should support learning, not shortcut it, and the best learning experiences keep educators and students in control."
- **Our assessment**: A clean, citable statement of OpenAI's public education-AI stance; useful for the guide as a stated design principle to compare against how the plugins are actually scoped (Claim 2's "teacher retains grading control," Claim 4's tutor-not-answer-generator design) — the principle and the shipped feature descriptions are at least internally consistent with each other in this post.

### Claim 6: OpenAI is the founding partner in the American Federation of Teachers' National Academy for AI Instruction, a five-year initiative to equip 400,000 K–12 educators — about one in every 10 teachers in the US — to use AI effectively
- **Evidence**: Direct partnership/initiative announcement naming the partner organization and a specific five-year educator-count target.
- **Confidence**: emerging (a specific, dated, numerically concrete initiative commitment; five-year targets of this kind are not verifiable at time of announcement)
- **Quote**: "OpenAI is the founding partner in the National Academy for AI Instruction, a five-year initiative to equip 400,000 K–12 educators—about one in every 10 teachers in the US—to use AI effectively and lead the way in shaping how AI is taught and used in classrooms across the country."
- **Our assessment**: The largest single numeric commitment in the post (400,000 educators over five years) and the first appearance of the National Academy for AI Instruction / AFT partnership in the corpus. No interim progress numbers are given (the initiative's actual training throughput as of this post's publication is not stated), so this should be read as a target, not a completed outcome.

### Claim 7: More than 200 million young adults ages 18–24 now use ChatGPT every week, but among college-age users OpenAI observes a widening global "capability overhang" — the gap between what AI tools can do and how people actually use them — with even advanced student users leveraging ChatGPT's capabilities roughly 90–99% less than power users
- **Evidence**: OpenAI's own stated usage figures and a named internal metric ("capability overhang") in the "Ensuring AI use in education leads to opportunity" section.
- **Confidence**: emerging (specific, falsifiable absolute and percentage figures, though "capability overhang" and "power users" are OpenAI-defined terms with no disclosed measurement methodology)
- **Quote**: "More than 200 million young adults ages 18–24 now use ChatGPT every week, making them some of the stronger mainstream users. However, among college-age users, we see a widening global "capability overhang," defined as the gap between what AI tools can do and how people actually use them. Even advanced student users leverage ChatGPT's capabilities roughly 90–99% less than power users, pointing to significant room to deepen AI skills."
- **Our assessment**: Novel term for the corpus. The framing is notable for a vendor announcement: OpenAI is stating that its largest weekly-user demographic (200M+ 18-24-year-olds) is nonetheless dramatically underusing the product's own capabilities, which functions as the post's justification for structured plugins/training rather than leaving usage to organic discovery. This is conceptually the same "usage deepens over time" pattern already in `blog-openai-chatgpt-adoption-signals.md` Claim 1 (users send 50% more messages and try 2x as many distinct capabilities six months after signup) — that note quantifies deepening usage over time in general, while this post quantifies the *current gap* for one demographic specifically. Worth flagging for the guide: no source in the corpus yet defines what specific capabilities separate a "power user" from an "advanced student user" in this 90-99% comparison.

### Claim 8: Across ChatGPT Edu deployments, students develop more advanced patterns of use over time than free-tier users, outperforming free users across nearly every capability and moving closer to power-user behavior, particularly in analysis, calculation, and learning
- **Evidence**: OpenAI's own stated comparative usage claim, offered as the mechanism for closing the "capability overhang" described in Claim 7.
- **Confidence**: emerging (a specific comparative claim, "nearly every capability," with no supporting data table, sample size, or measurement definition given in the post)
- **Quote**: "Across ChatGPT Edu deployments, students develop more advanced patterns of use over time, outperforming free users across nearly every capability and moving closer to power-user behavior, particularly in analysis, calculation, and learning."
- **Our assessment**: This is OpenAI's evidentiary basis for recommending institutional/structured deployment (ChatGPT Edu) over ad hoc free-tier use — directly relevant to Ch05 (Team Adoption)'s broader question of managed-deployment value, but as with Claim 7, no underlying data is shown, only the summary comparative claim.

### Claim 9: Since ChatGPT Edu launched in 2024, OpenAI has partnered with K–12 schools and districts including Houston ISD (Texas), Fairfax (Virginia), and Fulton (Georgia), and hundreds of college and university campuses including the Wharton School of the University of Pennsylvania, the University of Texas at Austin, and the California State University system
- **Evidence**: Named list of K–12 districts and university deployments.
- **Confidence**: settled (a specific, named list of institutional partners and a program-launch year — a straightforwardly checkable claim of *who has deployed*, distinct from the unverifiable usage-outcome claims elsewhere in the post)
- **Quote**: "Since the launch of ChatGPT Edu in 2024, we have partnered with K–12 schools and districts including Houston ISD, Texas; Fairfax, Virginia and Fulton, Georgia and hundreds of college and university campuses, including the Wharton School of the University of Pennsylvania⁠, The University of Texas at Austin, and the California State University system to responsibly deploy AI to teachers and campuses."
- **Our assessment**: Extends the corpus's existing ChatGPT Edu institutional-deployment evidence — `blog-openai-samsung-chatgpt-codex-deployment.md` Claim 9 already documents Seoul National University's campus-wide ChatGPT Edu rollout (47,000 community members); this post adds three named US K–12 districts and three named US university systems, giving the corpus a US-side institutional-adoption list to set alongside the Korea example. "Hundreds of college and university campuses" is not itemized beyond the three named examples.

### Claim 10: OpenAI has launched the OpenAI Student Collective, a student-led community for college students, with open applications for students to become "Campus Leads," plus a partnership with Handshake to connect student skills to internships and early-career opportunities
- **Evidence**: Direct program-launch description with a named partner (Handshake).
- **Confidence**: settled (a specific, dated program launch and named partnership — the program's existence and structure are checkable even though its effectiveness is not yet measurable)
- **Quote**: "For college students, the new OpenAI Student Collective is a student-led community for learning, building, and shaping what's next with AI. Applications are now open for students to become Campus Leads and bring the community to life on their campuses. Through peer-led experiences and hands-on projects, students can develop practical skills and put their ideas into practice. And, through partnerships with platforms like Handshake, college students can connect those skills to internships and early-career opportunities."
- **Our assessment**: Novel to the corpus — no existing OpenAI source note documents a peer-led (as opposed to institution-led or OpenAI-staff-led) student community program. Structurally distinct from the OpenAI Academy training courses already in the corpus (`blog-openai-academy-training-courses.md`), which are OpenAI-authored curricula for workplace adoption; this is a student-organized campus-presence model instead.

### Claim 11: In partnership with the Walton Family Foundation, OpenAI Academy is bringing together more than 1,600 K–12 teachers, administrators, and district leaders across eight U.S. cities for free in-person, hands-on workshops on applying AI to real classroom challenges
- **Evidence**: Direct program description with a named foundation partner and specific attendee/city counts.
- **Confidence**: settled (specific, named partner and dated program with concrete attendee and city counts)
- **Quote**: "In partnership with the Walton Family Foundation, OpenAI Academy is bringing together more than 1,600 K–12 teachers, administrators, and district leaders across eight U.S. cities for free in-person, hands-on workshops for building practical skills for applying AI to real classroom challenges."
- **Our assessment**: Extends `blog-openai-academy-training-courses.md` Claim 12, which already documents OpenAI Academy running "audience-segmented webinars organized by department and sector," including "higher-education-specific sessions" — this post adds a K–12-specific, in-person (not webinar) workshop format with a named foundation partner and concrete scale (1,600+ attendees, eight cities), extending that note's webinar-only picture of OpenAI Academy's education programming.

### Claim 12: In Estonia, ChatGPT Edu now reaches more than 20,000 students and 4,600 teachers, alongside a longitudinal research initiative with the University of Tartu and Stanford, as part of OpenAI's "Education for Countries" work with governments and national leaders
- **Evidence**: Direct national-deployment example with specific user counts and named research partners.
- **Confidence**: emerging (specific, named national-scale figures and named academic research partners; no publication or results from the longitudinal research initiative are cited, since it is ongoing)
- **Quote**: "Through OpenAI Education for Countries, we work with governments and national leaders to develop deployments designed for local needs and evidence-based research. In Estonia, for example, ChatGPT Edu now reaches more than 20,000 students and 4,600 teachers alongside a longitudinal research initiative with the University of Tartu and Stanford."
- **Our assessment**: Novel to the corpus — the first source note documenting a national-government-level ChatGPT Edu deployment paired with an academic longitudinal research initiative (as distinct from the corporate/university deployments in Claim 9 and the Korea example in `blog-openai-samsung-chatgpt-codex-deployment.md`). The "longitudinal research initiative" is named but not yet described with any methodology, timeline, or preliminary findings — worth tracking for a future source if Tartu/Stanford publish results.

### Claim 13: The new ChatGPT for Academic Researchers program gives eligible researchers 12 months of free Pro-level access to apply ChatGPT Work and Codex to scientific work in a secure workspace
- **Evidence**: Direct program-launch description.
- **Confidence**: settled (a specific, named, dated program with a concrete access term)
- **Quote**: "The new ChatGPT for Academic Researchers program gives eligible researchers 12 months of free Pro-level access to apply ChatGPT Work and Codex to ambitious scientific work in a secure workspace."
- **Our assessment**: Novel to the corpus — no existing OpenAI source note documents a dedicated free-access research-tier program. Notably reuses the "ambitious work" framing from the ChatGPT Work product-launch post title (`blog-openai-chatgpt-work-ambitious-partner.md`, "ChatGPT is now a partner for your most ambitious work"), suggesting consistent OpenAI messaging language across the product-launch and education verticals rather than independent copy.

## Concrete Artifacts

```
Source: OpenAI, "New ways to learn and teach with ChatGPT Work and Codex,"
https://openai.com/index/learn-teach-chatgpt-work-codex (August 4, 2026)

Three named education plugins (ChatGPT Work + Codex, via ChatGPT Edu /
ChatGPT for Teachers district deployments):
  K-12 Educator plugin      - differentiated resources, interactive visuals,
                               classroom insights; integrates with Learning
                               Commons; teacher retains control of grading
                               and agentic actions
  College Educator plugin   - course design, syllabus updates, multimedia
                               assessments, LMS packaging; connected
                               calendars/documents
  College Student plugin    - guided tutor, concept practice, study guides/
                               quizzes/flashcards/interactive visual
                               explanations from student-chosen sources

Plugin definition (verbatim): "A plugin is a package of apps, role-specific
skills, instructions, and common workflows that helps students and educators
get started immediately without having to construct complex prompts on
their own."

Headline usage/adoption figures:
  >200,000,000   young adults (18-24) using ChatGPT weekly
  90-99%         less capability usage by "advanced student users" vs.
                 "power users" ("capability overhang")
  400,000        K-12 educators targeted over 5 years (National Academy for
                 AI Instruction, with AFT; ~1 in 10 US teachers)
  1,600+         K-12 teachers/administrators/district leaders across 8 US
                 cities (OpenAI Academy workshops, with Walton Family
                 Foundation)
  20,000+        students reached by ChatGPT Edu in Estonia
  4,600          teachers reached by ChatGPT Edu in Estonia
  12 months      free Pro-level access under ChatGPT for Academic
                 Researchers program

Named institutional partners/deployments:
  American Federation of Teachers (AFT) - National Academy for AI
                                            Instruction (5-year initiative)
  Walton Family Foundation               - OpenAI Academy K-12 workshops
  Learning Commons                       - K-12 Educator plugin integration
                                            (academic-standards alignment)
  Handshake                              - OpenAI Student Collective ->
                                            internship/early-career pipeline
  University of Tartu + Stanford         - Estonia ChatGPT Edu longitudinal
                                            research initiative
  Houston ISD (TX), Fairfax (VA),
    Fulton (GA)                          - named K-12 district deployments
  Wharton (UPenn), UT Austin,
    California State University system   - named university deployments

Stated guiding principle (verbatim): "AI should support learning, not
shortcut it, and the best learning experiences keep educators and students
in control."

Programs launched in this post:
  - Three education plugins (K-12 educator, college educator, college
    student)
  - OpenAI Student Collective (peer-led community; Campus Lead applications
    open)
  - ChatGPT for Academic Researchers (12mo free Pro-level access)
```

## Cross-References

- **Corroborates**:
  - `blog-openai-samsung-chatgpt-codex-deployment.md` Claim 9 (Seoul National
    University's campus-wide ChatGPT Edu rollout to 47,000 community
    members) — this post's Claim 9 (Houston ISD, Fairfax, Fulton, Wharton,
    UT Austin, Cal State system) and Claim 12 (Estonia: 20,000+ students,
    4,600 teachers) extend the corpus's ChatGPT Edu institutional-adoption
    evidence from a single Korea example to named US districts/universities
    and a national-government deployment.
  - `blog-openai-academy-training-courses.md` Claim 1 (OpenAI frames
    training/education as integral to its product deployment strategy, not
    a separate marketing function) — this post is the K–12/higher-education
    sibling to that note's enterprise-workplace-training focus; both are
    OpenAI structured-learning programs paired with product rollout.
    Claim 12 of that note (OpenAI Academy runs sector-segmented webinars,
    including a higher-education-audience-tagged session alongside sales,
    finance, marketing, and legal-aid sessions) is directly extended by
    this post's Claim 11 (in-person K–12 workshops with the Walton Family
    Foundation, 1,600+ attendees across eight cities) — same OpenAI Academy
    program, new in-person format and named partner not previously in the
    corpus.
  - `blog-openai-chatgpt-adoption-signals.md` Claim 1 (six months after
    signup, ChatGPT users send 50% more messages/day and try twice as many
    distinct capabilities) — conceptually parallel to this post's Claim 7/8
    "capability overhang" framing: both describe usage capability deepening
    over time, though the adoption-signals note quantifies the trajectory
    in general while this post quantifies a specific demographic's current
    gap and attributes closing it to structured (ChatGPT Edu) rather than
    organic deployment.
- **Contradicts**: None identified.
- **Extends**:
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 1 (ChatGPT Work
    gathers information across connected apps/workflows and stays with
    complex projects for hours) — this post's three education plugins are
    role-specific packagings of that same underlying ChatGPT Work agent
    surface, aimed at the K–12/higher-ed vertical rather than the
    enterprise verticals (Sales, Marketing, Finance, etc.) that post
    documented.
  - `blog-latentspace-nathan-chatgpt-work-harness.md` Claim 13 (roughly 100x
    more people use software/code-produced tools than can write code
    themselves, framed as OpenAI's next-stage market after developers) —
    the education plugins are a concrete, named instantiation of extending
    ChatGPT Work/Codex to a large non-developer population (students and
    educators) rather than a general statement of market intent. That
    note's Claim 9 (ChatGPT Work conversations inherit and write back to
    shared user memory) is also the likely underlying mechanism for this
    post's Claim 3 (instructors working "across teaching, research, and
    everyday tasks without having to recreate the context for each new
    project"), though this post does not name the memory system explicitly.
  - `docs-github-copilot-agent-plugins-1-0.md` Claim 1 (Agent Plugins 1.0, a
    cross-vendor open plugin standard co-published by OpenAI among others,
    published August 6, 2026) — flagged, not asserted as confirmed overlap:
    this post's "plugin" (Claim 1, defined as "a package of apps,
    role-specific skills, instructions, and common workflows") was
    published August 4, 2026, two days *before* OpenAI co-published Agent
    Plugins 1.0 on August 6, 2026, and this post never references that
    standard. It is unclear from either source whether ChatGPT Work's
    education plugins are built on the Agent Plugins 1.0 spec, predate it
    as a separate proprietary mechanism, or are unrelated products that
    happen to share a name — a future source note or Smith synthesis should
    resolve this if OpenAI documents it explicitly.
- **Novel**:
  - "Capability overhang" (Claim 7) — first appearance in the corpus of
    this specific OpenAI-coined term and the 90-99% capability-usage gap
    figure for college-age users.
  - The National Academy for AI Instruction / American Federation of
    Teachers partnership (Claim 6) — first appearance of this specific
    5-year, 400,000-educator initiative and the AFT partnership.
  - OpenAI Student Collective (Claim 10) — first appearance of a
    peer-led/student-organized (as opposed to OpenAI-authored) education
    community program.
  - ChatGPT for Academic Researchers (Claim 13) — first appearance of a
    dedicated free-access research tier.
  - Estonia national ChatGPT Edu deployment with University of
    Tartu/Stanford longitudinal research (Claim 12) — first
    national-government-level deployment example with an academic research
    partnership in the corpus.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Claim 8 (structured ChatGPT Edu deployment
  produces more advanced usage patterns than free-tier use, "particularly in
  analysis, calculation, and learning") and Claim 11 (in-person workshop
  format reaching 1,600+ educators) are citable examples of OpenAI's own
  evidence for *structured/managed* rollout outperforming organic adoption —
  directly relevant if the chapter compares managed-deployment vs.
  self-serve adoption strategies, though flag that Claim 8's "nearly every
  capability" comparison is unaudited and unaccompanied by a data table.
- **Chapter 02 (Harness Engineering)**: Claim 1's plugin definition ("a
  package of apps, role-specific skills, instructions, and common
  workflows") is a citable, vendor-stated packaging concept for
  role-scoped agent configuration — pair with the Cross-References flag
  above (Agent Plugins 1.0 timing) if the chapter discusses plugin/skill
  packaging standards, since it's currently unclear whether this is the
  same mechanism as the cross-vendor standard OpenAI co-published two days
  later.
- **Chapter 03 (Verification)**: Claim 2's explicit scoping — the K–12
  Educator plugin keeps the teacher "in control of pedagogical decisions,
  grading, and agentic actions" — is a concrete, named example of a vendor
  excluding a specific high-stakes action class (grading) from agent
  authority by design, worth citing if the chapter discusses scoping agent
  authority away from consequential decisions.
- **Chapter 01 (Daily Workflows)**: Claim 7's "capability overhang" figure
  (90-99% less capability usage among advanced student users vs. power
  users) is a citable, if unaudited, data point for a discussion of the gap
  between what agentic tools can do and how most users actually use them —
  relevant context for any section motivating deliberate skill-building
  rather than assuming capability access alone drives adoption.

## Extraction Notes

- The live `openai.com/index/` URL returned an HTTP 403 (Cloudflare
  bot-challenge) to `WebFetch`, matching the access pattern already
  documented for other `openai.com/index/` posts in the corpus. The
  Prospector's second triage comment on this issue anticipated this and
  recommended a Wayback Machine attempt.
- The Internet Archive Wayback Machine availability API confirmed a
  snapshot exists (`http://web.archive.org/web/20260804191230/https://openai.com/index/learn-teach-chatgpt-work-codex/`),
  but both `WebFetch` and direct `curl` (with a browser user-agent, tried
  over `http://` and `https://`, with retries) were unable to reach
  `web.archive.org` from this environment — `WebFetch` explicitly refused
  the domain, and `curl` returned a synthetic 498/404 response
  characteristic of an environment-level network block on that domain
  specifically. This differs from the precedent in
  `blog-openai-chatgpt-work-ambitious-partner.md`, where Wayback + `curl`
  worked; the Wayback route was not available in this session.
- Extraction instead used the `r.jina.ai` reader proxy. A direct `curl` to
  `r.jina.ai` was itself blocked by a Cloudflare JS challenge (no headless
  browser available via `curl`), but fetching the same `r.jina.ai` URL
  through the `WebFetch` tool succeeded. The first `WebFetch` call (a
  general "return the full text" prompt) returned a suspiciously short,
  paraphrased summary — WebFetch runs fetched content through a small
  processing model per its own tool description, and that model
  paraphrased despite instructions. A second `WebFetch` call, explicitly
  instructing the tool to return the raw markdown character-for-character
  inside a code block, returned a substantially longer, detailed,
  internally consistent article with specific named partners and figures.
  A third `WebFetch` call, asking it to quote back two specific paragraphs
  verbatim, returned text identical to the corresponding passages in the
  second call's full-text response — this consistency check is the basis
  for treating the second call's text as a reliable verbatim source for
  the quotes above, in the absence of being able to independently
  cross-check against the live page or a Wayback snapshot directly. Every
  `Quote` field above was copied character-for-character from that raw
  `r.jina.ai` markdown response.
- No image content, embedded interactive tab content, or footnote markers
  were present in the reader-proxy text beyond image alt-text captions
  (e.g., "K–12 educator plugin screenshot 1"), which are not cited as
  quotes above.
- No contradiction with any existing source note was found during
  cross-referencing (see Cross-References → Contradicts), so no
  contradiction issue was filed per MINER.md §4a. The Agent Plugins 1.0
  timing overlap (see Cross-References → Extends) is flagged as an open
  question for future synthesis, not a contradiction — the two sources
  don't make opposing claims, they simply don't reference each other, and
  we could not independently confirm or rule out a technical relationship.
- The Prospector's triage comments assessed this as "medium novelty,"
  distinct from the July 9, 2026 ChatGPT Work launch post (product
  features/enterprise testimonials) on the basis of a "learning and
  teaching" angle. On full reading, the post's education-specific content
  (three role-specific plugins, the National Academy for AI Instruction,
  the Student Collective, the Estonia national deployment, and the
  Academic Researchers program) is confirmed as substantially novel to the
  corpus and distinct from the enterprise-product-launch and
  workplace-training source notes already present.
